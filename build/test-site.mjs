// Local check of the built site: serves site/ like Cloudflare Pages and exercises it in Chromium.
import fs from 'node:fs'; import path from 'node:path'; import { createRequire } from 'node:module';
const require = createRequire('/tmp/x.js'); const { chromium } = require('playwright');
const SITE = path.resolve('site');
const file = (p) => { p = decodeURIComponent(p.split('?')[0].split('#')[0]); if (p === '/') return 'index.html'; let f = p.slice(1); if (f.endsWith('/')) f += 'index.html';
  if (fs.existsSync(path.join(SITE, f)) && fs.statSync(path.join(SITE, f)).isFile()) return f; if (fs.existsSync(path.join(SITE, f + '.html'))) return f + '.html'; return null; };
const type = (f) => ({ '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.woff2': 'font/woff2', '.webp': 'image/webp', '.png': 'image/png', '.jpg': 'image/jpeg', '.mp4': 'video/mp4', '.xml': 'application/xml', '.txt': 'text/plain' })[path.extname(f)] || 'application/octet-stream';
export async function open(widths = [1440]) {
  const b = await chromium.launch();
  return { b, async page(w, h = 900) { const ctx = await b.newContext({ viewport: { width: w, height: h } });
    await ctx.route('https://www.sullivanparkdesign.com/**', async (route) => { const u = new URL(route.request().url()); const f = file(u.pathname);
      if (!f) return route.fulfill({ status: 404, body: fs.readFileSync(path.join(SITE, '404.html')), contentType: 'text/html' });
      route.fulfill({ status: 200, body: fs.readFileSync(path.join(SITE, f)), contentType: type(f) }); });
    return ctx.newPage(); } };
}
export const pages = () => { const out = []; (function walk(d) { for (const e of fs.readdirSync(d)) { const p = path.join(d, e);
  if (fs.statSync(p).isDirectory()) { if (!['images', 'media', 'assets'].includes(e)) walk(p); } else if (e.endsWith('.html') && e !== '404.html') out.push('/' + path.relative(SITE, p).replace(/index\.html$/, '').replace(/\.html$/, '')); } })(SITE); return out.sort(); };
export { file };
