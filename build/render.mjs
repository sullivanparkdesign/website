// Renders design-canvas (.dc.html) artboards into plain static HTML.
// Every piece of text ends up in the HTML source (good for Google and AI search);
// interactive bits are marked with data-* attributes and wired up by /assets/site.js.
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import crypto from 'node:crypto';
import * as cheerio from 'cheerio';

const VOID = new Set(['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr']);
const DROP_ATTRS = /^(hint-|data-screen-label$|data-slot$|ref$|data-dc-script$|data-props$|data-narrow-ok$)/;

export function escHtml(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}
export function escAttr(s) {
  return String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}
// Text inside the design files is already HTML-encoded (&amp; etc.); keep it as-is.
const decode = (s) => s;

export class Renderer {
  constructor({ srcDir, siteDir, linkMap, hooks = {} }) {
    this.srcDir = srcDir;
    this.siteDir = siteDir;
    this.linkMap = linkMap;
    this.hooks = hooks;
    this.hoverRules = new Map(); // class -> css
    this.warnings = [];
  }

  load(name) {
    const file = path.join(this.srcDir, name + '.dc.html');
    const raw = fs.readFileSync(file, 'utf8');
    const $ = cheerio.load(raw, { decodeEntities: false, lowerCaseAttributeNames: false }, true);
    const script = $('script[type="text/x-dc"]').html() || '';
    const helmet = $('helmet').first();
    const head = [];
    helmet.children().each((_, el) => head.push(el));
    const title = $('helmet title').first().text() || $('head title').first().text() || '';
    const xdc = $('x-dc').first();
    xdc.find('helmet').remove();
    return { $, script, head, title, root: xdc };
  }

  // Run the component's logic in a sandbox and return its render values.
  instance(name, script, props, state) {
    const dataDir = this.siteDir;
    const docState = { title: '' };
    const syncThen = (v) => ({ then: (f) => syncThen(f(v)) });
    const sandbox = {
      console,
      React: { createRef: () => ({ current: null }) },
      setInterval: () => 0, clearInterval: () => {}, setTimeout: () => 0, clearTimeout: () => {},
      URLSearchParams,
      location: { search: '' },
      window: { location: { search: '' }, addEventListener() {}, removeEventListener() {}, claude: null },
      document: {
        set title(v) { docState.title = v; }, get title() { return docState.title; },
        body: { style: {} },
      },
      fetch: (url) => {
        const p = path.join(dataDir, String(url).replace(/^\.?\//, ''));
        const json = JSON.parse(fs.readFileSync(p, 'utf8'));
        return syncThen({ json: () => json });
      },
    };
    sandbox.DCLogic = class DCLogic {
      constructor(p) { this.props = p || {}; }
      setState(u) {
        const patch = typeof u === 'function' ? u(this.state || {}) : u;
        this.state = { ...(this.state || {}), ...patch };
      }
    };
    vm.createContext(sandbox);
    if (!script.trim()) return { vals: {}, inst: null, docTitle: '' };
    const C = vm.runInContext(script + '\n;Component', sandbox, { filename: name });
    const inst = new C(props);
    if (state) inst.state = { ...(inst.state || {}), ...state };
    if (typeof inst.componentDidMount === 'function') {
      try { inst.componentDidMount(); } catch (e) { this.warnings.push(`${name}: mount ${e.message}`); }
    }
    if (state) inst.state = { ...(inst.state || {}), ...state };
    const vals = typeof inst.renderVals === 'function' ? inst.renderVals() : {};
    return { vals, inst, docTitle: docState.title };
  }

  evalExpr(expr, scope) {
    expr = expr.replace(/\.(\d+)\b/g, '[$1]'); // template paths like L.times.0
    const keys = Object.keys(scope).filter(k => /^[A-Za-z_$][\w$]*$/.test(k));
    try {
      return Function(...keys, `"use strict"; return (${expr});`)(...keys.map(k => scope[k]));
    } catch (e) {
      this.warnings.push(`expr "${expr}": ${e.message}`);
      return undefined;
    }
  }

  interp(str, scope, esc) {
    return str.replace(/\{\{\s*([^}]+?)\s*\}\}/g, (_, e) => {
      const v = this.evalExpr(e, scope);
      if (v === undefined || v === null || v === false) return '';
      return esc(v);
    });
  }

  hoverClass(css) {
    const cls = 'hv-' + crypto.createHash('md5').update(css).digest('hex').slice(0, 7);
    if (!this.hoverRules.has(cls)) {
      const decls = css.split(';').map(s => s.trim()).filter(Boolean).map(d => d + ' !important').join(';');
      this.hoverRules.set(cls, `.${cls}:hover{${decls}}`);
    }
    return cls;
  }

  rewriteUrl(u) {
    if (!u) return u;
    const m = this.linkMap(u);
    if (m !== undefined) return m;
    if (/^images\//.test(u) || /^data\//.test(u) || /^audio\//.test(u)) return '/' + u;
    if (/\.dc\.html/.test(u)) this.warnings.push(`unmapped link ${u}`);
    return u;
  }

  // ctx: { page, $, scope, vals, inst, compName, compScript, props }
  renderNodes(nodes, ctx) {
    let out = '';
    for (const n of nodes) out += this.renderNode(n, ctx);
    return out;
  }

  renderNode(node, ctx) {
    if (node.type === 'text') return this.interp(node.data, ctx.scope, escHtml);
    if (node.type === 'comment') return '';
    if (node.type !== 'tag' && node.type !== 'script' && node.type !== 'style') return '';
    const tag = node.name;
    const kids = node.children || [];

    if (tag === 'helmet') return '';
    if (tag === 'sc-for') {
      const list = this.evalExpr(node.attribs.list.replace(/^\{\{\s*|\s*\}\}$/g, ''), ctx.scope) || [];
      const as = node.attribs.as || 'item';
      return list.map((item, i) => this.renderNodes(kids, { ...ctx, scope: { ...ctx.scope, [as]: item, [as + 'Index']: i } })).join('');
    }
    if (tag === 'sc-if') {
      const expr = node.attribs.value.replace(/^\{\{\s*|\s*\}\}$/g, '');
      const hook = this.hooks.scIf && this.hooks.scIf(expr, ctx, node, this);
      if (hook !== undefined) return hook;
      return this.evalExpr(expr, ctx.scope) ? this.renderNodes(kids, ctx) : '';
    }
    if (tag === 'dc-import') {
      const name = node.attribs.name;
      if (this.hooks.skipImport && this.hooks.skipImport(name, ctx)) return '';
      const props = {};
      for (const [k, v] of Object.entries(node.attribs)) {
        if (k === 'name' || /^hint-/.test(k)) continue;
        const m = /^\{\{\s*([^}]+?)\s*\}\}$/.exec(v);
        props[k] = m ? this.evalExpr(m[1], ctx.scope) : v;
      }
      return this.renderComponent(name, props, ctx.page).body;
    }

    let attrs = '';
    const classes = [];
    const extra = {};
    for (let [k, v] of Object.entries(node.attribs || {})) {
      if (k === 'ref' && this.hooks.ref) {
        const m = /^\{\{\s*([^}]+?)\s*\}\}$/.exec(v);
        if (m) Object.assign(extra, this.hooks.ref(m[1], ctx, node) || {});
        continue;
      }
      if (DROP_ATTRS.test(k)) continue;
      if (k === 'style-hover') { classes.push(this.hoverClass(this.interp(v, ctx.scope, String))); continue; }
      if (/^on[A-Z]/.test(k) || /^on[a-z]+$/.test(k)) {
        const m = /^\{\{\s*([^}]+?)\s*\}\}$/.exec(v);
        if (m && this.hooks.event) Object.assign(extra, this.hooks.event(k, m[1], ctx, node) || {});
        continue;
      }
      if (k === 'class') { classes.push(v); continue; }
      if (this.hooks.attr) Object.assign(extra, this.hooks.attr(k, v, ctx, node) || {});
      const whole = /^\{\{\s*([^}]+?)\s*\}\}$/.exec(v);
      if (whole) {
        const val = this.evalExpr(whole[1], ctx.scope);
        if (val === false || val === null || val === undefined) continue;
        if (typeof val === 'function') continue;
        if (val === true) { attrs += ` ${k}`; continue; }
        v = escAttr(val);
      } else {
        v = this.interp(v, ctx.scope, escAttr);
      }
      if (k === 'href' || k === 'src' || k === 'action' || k === 'poster') v = this.rewriteUrl(v);
      if (k === 'style') v = v.replace(/url\((&quot;|["']?)(images\/)/g, (_, q, p) => `url(${q}/${p}`);
      attrs += ` ${k}="${v}"`;
    }
    for (const [k, v] of Object.entries(extra)) {
      if (k === 'class') classes.push(v); else attrs += v === true ? ` ${k}` : ` ${k}="${escAttr(v)}"`;
    }
    if (classes.length) attrs = ` class="${classes.join(' ')}"` + attrs;
    if (VOID.has(tag)) return `<${tag}${attrs}>`;
    const inner = (tag === 'script' || tag === 'style') ? kids.map(k => k.data || '').join('') : this.renderNodes(kids, ctx);
    return `<${tag}${attrs}>${inner}</${tag}>`;
  }

  renderComponent(name, props = {}, page = null, state = null, extraVals = null) {
    const f = this.load(name);
    const { vals, inst, docTitle } = this.instance(name, f.script, props, state);
    if (extraVals) Object.assign(vals, extraVals(vals));
    const ctx = { page: page || name, $: f.$, scope: { ...vals }, vals, inst, compName: name, script: f.script, props, file: f };
    const body = this.renderNodes(f.root.contents().toArray(), ctx);
    const headHtml = f.head.map(el => f.$.html(el));
    (this.pageHead ||= []).push(...headHtml);
    return { body, head: headHtml, title: f.title, docTitle, vals, inst };
  }

  hoverCss() { return [...this.hoverRules.values()].join('\n'); }
}
