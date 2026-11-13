// Build: node build/build.mjs   (reads design-source/*.dc.html, writes the static site into site/)
// The design canvas is the source of truth. This turns each artboard into a plain HTML page with
// clean addresses, real image files, SEO tags and structured data. Interactive pieces are marked
// with data-* attributes and wired up by /assets/site.js.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import * as cheerio from 'cheerio';
import { Renderer, escAttr } from './render.mjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const SRC = path.join(ROOT, 'design-source');
const SITE = path.join(ROOT, 'site');
const BLOBS = path.join(ROOT, 'build', 'blobs'); // canvas image files, named by their canvas id
const ORIGIN = 'https://www.sullivanparkdesign.com';
const CONFIG = JSON.parse(fs.readFileSync(path.join(ROOT, 'build', 'config.json'), 'utf8'));

// ---------- pages and their addresses ----------
const PAGES = [
  { src: 'Main', url: '/' },
  { src: 'About', url: '/about', crumb: 'About' },
  { src: 'Services', url: '/services', crumb: 'Services' },
  { src: 'Website-Design', url: '/services/website-design', crumb: 'Website Design', parent: 'Services' },
  { src: 'Brand-Marketing-Design', url: '/services/brand-marketing-design', crumb: 'Brand and Marketing Design', parent: 'Services' },
  { src: 'SEO', url: '/services/seo', crumb: 'SEO', parent: 'Services' },
  { src: 'Actor-Websites', url: '/services/actor-websites', crumb: 'Actor Websites', parent: 'Services', og: '/_blob/d42d37c59ae9c3b6be701fdf2d142351' },
  { src: 'Portfolio', url: '/portfolio', crumb: 'Portfolio' },
  { src: 'Hamish-Ross', url: '/portfolio/hamish-ross-real-estate', crumb: 'Hamish Ross Real Estate', parent: 'Portfolio' },
  { src: 'Smash', url: '/portfolio/smash-performing-arts', crumb: 'SMASH Performing Arts Studio', parent: 'Portfolio' },
  { src: 'Callum-Frost', url: '/portfolio/callum-frost', crumb: 'Callum Frost', parent: 'Portfolio' },
  { src: 'Party-With-Laura', url: '/portfolio/party-with-laura', crumb: 'pARTy With Laura', parent: 'Portfolio' },
  { src: 'Rooster-Den', url: '/portfolio/the-rooster-den-co', crumb: 'The Rooster Den Co', parent: 'Portfolio' },
  { src: 'Journal', url: '/resources', crumb: 'Resources' },
  { src: 'Article', url: '/resources/what-to-prepare-before-a-website-redesign', crumb: 'What to prepare before a website redesign', parent: 'Journal', guide: true },
  { src: 'Guide-Platforms', url: '/resources/squarespace-shopify-or-custom-coded', crumb: 'Squarespace, Shopify or custom-coded', parent: 'Journal', guide: true },
  { src: 'Guide-Branding', url: '/resources/what-to-have-ready-before-branding', crumb: 'What to have ready before branding or a website build', parent: 'Journal', guide: true },
  { src: 'Guide-Search', url: '/resources/help-google-and-ai-search-find-your-business', crumb: 'How to help Google and AI search find your business', parent: 'Journal', guide: true },
  { src: 'Guide-Support', url: '/resources/ongoing-website-and-marketing-support', crumb: 'What ongoing website and marketing support can include', parent: 'Journal', guide: true },
  { src: 'Testimonials', url: '/testimonials', crumb: 'Testimonials', props: { privatePreview: false } },
  { src: 'Contact', url: '/contact', crumb: 'Contact' },
];
if (fs.existsSync(path.join(SRC, 'Privacy.dc.html'))) PAGES.push({ src: 'Privacy', url: '/privacy', crumb: 'Privacy Policy' });
// pages in config.hiddenPages are built and reachable by address only: noindex, no sitemap entry
for (const p of PAGES) if ((CONFIG.hiddenPages || []).includes(p.url)) p.hidden = true;
const BY_SRC = Object.fromEntries(PAGES.map(p => [p.src, p]));

function linkMap(u) {
  const m = /^([A-Za-z0-9-]+)\.dc\.html(#.*)?$/.exec(u);
  if (m) {
    const p = BY_SRC[m[1]];
    if (p) return p.url + (m[2] || '');
  }
  if (u === '#privacy-policy') return BY_SRC.Privacy ? '/privacy' : 'mailto:info@sullivanparkdesign.com';
  return undefined;
}

// ---------- canvas behaviour -> static markers ----------
const hooks = {
  ref(name) {
    return ({ headerRef: { 'data-header': true }, formRef: { 'data-form': true }, baRef: { 'data-ba': true }, videoRef: { 'data-hero-video': true } })[name] || {};
  },
  scIf(expr, ctx, node, r) {
    const kids = () => r.renderNodes(node.children, ctx);
    let m;
    if (expr === 'menuOpen') return `<div data-mnav hidden>${kids()}</div>`;
    if ((m = /^faq(\d+)Open$/.exec(expr))) return `<div data-faq-panel="${m[1]}"${r.evalExpr(expr, ctx.scope) ? '' : ' hidden'}>${kids()}</div>`;
    if (expr === 'showForm') return `<div data-form-view="form">${kids()}</div>`;
    if (expr === 'sent') return `<div data-form-view="sent" hidden>${kids()}</div>`;
    if (expr === 'sendFailed') return `<div data-form-view="failed" hidden>${kids()}</div>`;
    if ((m = /^(name|email|message)Error$/.exec(expr))) return `<div data-error="${m[1]}" hidden>${kids()}</div>`;
    if (expr === 'videoPlaying') return `<span data-video-icon="playing">${kids()}</span>`;
    if (expr === 'videoPaused') return `<span data-video-icon="paused" hidden>${kids()}</span>`;
    return undefined; // everything else renders from the page's default state
  },
  event(attr, handler) {
    let m;
    if (handler === 'toggleMenu') return { 'data-menu-toggle': true };
    if (handler === 'closeMenu') return { 'data-menu-close': true };
    if ((m = /^toggleFaq(\d+)$/.exec(handler))) return { 'data-faq-btn': m[1] };
    if (handler === 'submitForm') return { 'data-form-submit': true };
    if (handler === 'resetForm') return { 'data-form-reset': true };
    if (handler === 'toggleVideo') return { 'data-video-toggle': true };
    return {};
  },
};

const r = new Renderer({ srcDir: SRC, siteDir: SITE, linkMap, hooks });

// ---------- images ----------
const ext = (buf) => {
  if (buf.slice(0, 4).toString() === 'RIFF' && buf.slice(8, 12).toString() === 'WEBP') return '.webp';
  if (buf.slice(0, 4).toString('hex') === '89504e47') return '.png';
  if (buf.slice(0, 2).toString('hex') === 'ffd8') return '.jpg';
  if (buf.slice(4, 8).toString() === 'ftyp') return '.mp4';
  if (/<svg/.test(buf.slice(0, 200).toString())) return '.svg';
  return '';
};
const slug = (s) => s.toLowerCase().replace(/&amp;/g, 'and').replace(/[’']/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '')
  .split('-').filter(Boolean).slice(0, 7).join('-');
const imgNames = new Map();
const usedNames = new Set();
const NAMED = Object.fromEntries(Object.entries(CONFIG.imageNames || {}));
// Images are cached for a year under their file name, so a name is never reused for a different image.
// image-owners.json records the image that first used each name; a new image with the same description gets the next free name.
const OWNERS_FILE = path.join(ROOT, 'build', 'image-owners.json');
const OWNERS = fs.existsSync(OWNERS_FILE) ? JSON.parse(fs.readFileSync(OWNERS_FILE, 'utf8')) : {};
function nameFor(id, alt, kind) {
  if (imgNames.has(id)) return imgNames.get(id);
  const file = path.join(BLOBS, id);
  if (!fs.existsSync(file)) { r.warnings.push(`missing image file ${id}`); return null; }
  const e = ext(fs.readFileSync(file));
  let base = NAMED[id] || (alt ? slug(alt) : '') || (kind === 'video' ? 'sullivan-park-design-ocean' : 'sullivan-park-design');
  let n = base, i = 2;
  while (usedNames.has(n) || (OWNERS[n] && OWNERS[n] !== id)) n = `${base}-${i++}`;
  usedNames.add(n);
  if (!OWNERS[n]) OWNERS[n] = id;
  const out = (e === '.mp4' ? '/media/' : '/images/') + n + e;
  imgNames.set(id, out);
  fs.copyFileSync(file, path.join(SITE, out));
  return out;
}

// ---------- helpers ----------
const stripTags = (s) => cheerio.load('<div>' + s + '</div>')('div').text().replace(/\s+/g, ' ').trim();
const BUSINESS_ID = ORIGIN + '/#business';

function readHead(src) {
  const raw = fs.readFileSync(path.join(SRC, src + '.dc.html'), 'utf8');
  const head = raw.slice(0, raw.indexOf('<x-dc'));
  const $ = cheerio.load(head, { decodeEntities: false });
  return {
    title: $('title').first().text().trim(),
    desc: $('meta[name="description"]').attr('content') || '',
    ld: $('script[type="application/ld+json"]').first().html() || '',
  };
}

function postProcess(body, page) {
  const $ = cheerio.load(body, { decodeEntities: false }, false);
  // Placeholders stay on the canvas but never go live.
  $('section[aria-label="Client testimonial placeholder"]').remove();
  $('.rd-ba').closest('section').remove();
  $('[aria-describedby=""]').removeAttr('aria-describedby');
  // Contact form: where messages go
  const form = $('form[data-form]');
  if (form.length) {
    form.attr('data-endpoint', CONFIG.formEndpoint || '');
    form.attr('action', CONFIG.formEndpoint || '');
    form.attr('method', 'post');
    if (CONFIG.formEndpoint) {
      // Formspree extras: an email subject, and a hidden field only spam bots fill in
      form.prepend('<input type="hidden" name="_subject" value="Website enquiry"><input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" style="display: none">');
    }
    form.find('[data-error="email"] p').attr('data-error-text', '');
    form.find('[data-form-submit]').attr('data-label', form.find('[data-form-submit]').text().trim());
    const alertBox = form.find('[data-form-view="failed"] [role="alert"]');
    alertBox.attr('data-mailto-note', 'Your email app should open with your message ready to send. If it doesn’t, email me at <a href="mailto:info@sullivanparkdesign.com">info@sullivanparkdesign.com</a>.');
  }
  return $.html();
}

function faqsFrom(body) {
  const $ = cheerio.load(body);
  const out = [];
  $('[data-faq-btn]').each((_, b) => {
    const n = $(b).attr('data-faq-btn');
    const q = $(b).text().replace(/\s+/g, ' ').trim();
    const a = $(`[data-faq-panel="${n}"]`).text().replace(/\s+/g, ' ').trim();
    if (q && a) out.push([q, a]);
  });
  return out;
}

function schema(page, meta, body, ogImage) {
  const graph = [];
  if (page.url === '/' && meta.ld) {
    try { graph.push(...JSON.parse(meta.ld)['@graph']); } catch (e) { r.warnings.push('home schema did not parse'); }
  }
  if (page.url !== '/') {
    const items = [{ name: 'Home', url: ORIGIN + '/' }];
    if (page.parent) items.push({ name: BY_SRC[page.parent].crumb, url: ORIGIN + BY_SRC[page.parent].url });
    items.push({ name: page.crumb, url: ORIGIN + page.url });
    graph.push({ '@type': 'BreadcrumbList', itemListElement: items.map((it, i) => ({ '@type': 'ListItem', position: i + 1, name: it.name, item: it.url })) });
  }
  if (page.guide) {
    const $ = cheerio.load(body);
    graph.push({
      '@type': 'Article', headline: $('h1').first().text().replace(/\s+/g, ' ').trim(), description: meta.desc,
      image: ogImage, url: ORIGIN + page.url, mainEntityOfPage: ORIGIN + page.url,
      author: { '@type': 'Person', name: 'Natasha Young', url: ORIGIN + '/about' },
      publisher: { '@id': BUSINESS_ID, '@type': 'ProfessionalService', name: 'Sullivan Park Design', url: ORIGIN + '/' },
    });
  }
  const faqs = faqsFrom(body);
  if (faqs.length) graph.push({ '@type': 'FAQPage', mainEntity: faqs.map(([q, a]) => ({ '@type': 'Question', name: q, acceptedAnswer: { '@type': 'Answer', text: a } })) });
  if (!graph.length) return '';
  return `<script type="application/ld+json">${JSON.stringify({ '@context': 'https://schema.org', '@graph': graph }).replace(/</g, '\\u003c')}</script>`;
}

function head(page, meta, helmet, ogImage, extra = '') {
  const canonical = ORIGIN + page.url;
  const t = meta.title.replace(/&amp;/g, '&');
  const d = meta.desc.replace(/&amp;/g, '&');
  return [
    '<meta charset="utf-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1">',
    `<title>${meta.title}</title>`,
    d ? `<meta name="description" content="${escAttr(d)}">` : '',
    `<link rel="canonical" href="${canonical}">`,
    page.hidden ? '<meta name="robots" content="noindex">' : '',
    `<meta property="og:type" content="${page.guide ? 'article' : 'website'}">`,
    '<meta property="og:site_name" content="Sullivan Park Design">',
    `<meta property="og:title" content="${escAttr(t)}">`,
    d ? `<meta property="og:description" content="${escAttr(d)}">` : '',
    `<meta property="og:url" content="${canonical}">`,
    `<meta property="og:image" content="${ogImage}">`,
    '<meta property="og:locale" content="en_CA">',
    '<meta name="twitter:card" content="summary_large_image">',
    `<link rel="icon" type="image/png" sizes="48x48" href="${CONFIG.icon}">`,
    `<link rel="apple-touch-icon" sizes="180x180" href="${CONFIG.touchIcon}">`,
    '<link rel="preconnect" href="https://fonts.googleapis.com">',
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
    ...helmet,
    extra,
    '<script src="/assets/site.js" defer></script>',
  ].filter(Boolean).join('\n');
}

function outFile(url) {
  return url === '/' ? path.join(SITE, 'index.html') : path.join(SITE, url.slice(1) + '.html');
}

// ---------- build ----------
fs.rmSync(path.join(SITE, 'images'), { recursive: true, force: true });
fs.rmSync(path.join(SITE, 'media'), { recursive: true, force: true });
for (const d of ['images', 'media', 'assets']) fs.mkdirSync(path.join(SITE, d), { recursive: true });

// name images from their alt text first, so the most descriptive name wins
for (const page of PAGES) {
  const raw = fs.readFileSync(path.join(SRC, page.src + '.dc.html'), 'utf8');
  const $ = cheerio.load(raw, { decodeEntities: false });
  $('img[src^="/_blob/"]').each((_, el) => {
    const id = $(el).attr('src').slice(7); const alt = ($(el).attr('alt') || '').trim();
    if (alt) nameFor(id, alt);
  });
}

const built = [];
let shell = null;
for (const page of PAGES) {
  r.pageHead = [];
  const rendered = r.renderComponent(page.src, page.props || {}, page.src);
  let body = postProcess(rendered.body, page);
  const meta = readHead(page.src);
  const helmet = [...new Set(r.pageHead)];
  // og image: the page's first large picture, or the home poster
  const $b = cheerio.load(body);
  let og = page.og || '';
  // skip decorative images (empty alt); the home page always uses the ocean poster
  if (page.url !== '/') $b('main img').each((_, el) => { if (!og && ($b(el).attr('alt') || '').trim() && +($b(el).attr('width') || 0) >= 800 && ($b(el).attr('src') || '').startsWith('/_blob/')) og = $b(el).attr('src'); });
  if (!og) og = CONFIG.defaultOg;
  let html = `<!doctype html>
<html lang="en-CA">
<head>
${head(page, meta, helmet, og)}
${schema(page, meta, body, og)}
</head>
<body>
${body}
</body>
</html>
`;
  // every canvas image -> a named file
  html = html.replace(/\/_blob\/([0-9a-f]{32})/g, (all, id) => {
    const kind = new RegExp(`<video[^>]*src="/_blob/${id}"`).test(html) ? 'video' : 'image';
    const n = nameFor(id, '', kind);
    return n || all;
  });
  html = html.replace(new RegExp(`content="(/images/[^"]+)"`, 'g'), (m, p) => `content="${ORIGIN}${p}"`).replace(/"image":"\/images\//g, `"image":"${ORIGIN}/images/`);
  const file = outFile(page.url);
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, html);
  if (!page.hidden) built.push(page.url);
  if (page.src === 'Journal') shell = html;
}

// ---------- 404 ----------
{
  const $ = cheerio.load(shell, { decodeEntities: false });
  $('title').text('Page Not Found | Sullivan Park Design');
  $('meta[name="description"], link[rel="canonical"], meta[property^="og:"], script[type="application/ld+json"]').remove();
  $('head').append('<meta name="robots" content="noindex">');
  const serif = "'Cormorant Infant', Garamond, serif";
  $('main').html(`<section aria-labelledby="page-title" style="background: #FAFAF8">
<div style="width: 100%; max-width: 1680px; margin: 0 auto; padding: clamp(160px, 14vw, 220px) clamp(20px, 5vw, 72px) clamp(96px, 10vw, 144px); display: flex; flex-direction: column; gap: 28px">
<p style="margin: 0; display: flex; align-items: center; gap: 16px; font-size: 15px; letter-spacing: 0.2em; text-transform: uppercase; color: #4E6368"><span aria-hidden="true" style="display: block; width: 40px; height: 1px; background: #4E6368"></span>Page not found</p>
<h1 id="page-title" style="margin: 0; font-family: ${serif}; font-weight: 300; font-size: clamp(48px, 6.6vw, 104px); line-height: 1; color: #121414">This page has <em style="font-style: italic; color: #4E6368">moved on</em></h1>
<p style="margin: 0; font-size: 21px; line-height: 1.65; color: #1F2426">The page you’re looking for isn’t here. It may have moved when the site was redesigned.</p>
<div style="display: flex; flex-wrap: wrap; gap: 16px; margin-top: 12px">
<a class="sp-btn sp-btn-blue" href="/" style="display: inline-flex; align-items: center; justify-content: center; min-height: 56px; padding: 0 30px; background: #4E6368; border: 1px solid #4E6368; color: #FFFFFF; text-decoration: none; font-size: 18px; letter-spacing: 0.03em">Go to the Home Page</a>
<a class="sp-btn sp-btn-line" href="/resources" style="display: inline-flex; align-items: center; justify-content: center; min-height: 56px; padding: 0 30px; border: 1px solid #4E6368; color: #4E6368; text-decoration: none; font-size: 18px; letter-spacing: 0.03em">Browse the Guides</a>
<a class="sp-btn sp-btn-line" href="/contact" style="display: inline-flex; align-items: center; justify-content: center; min-height: 56px; padding: 0 30px; border: 1px solid #4E6368; color: #4E6368; text-decoration: none; font-size: 18px; letter-spacing: 0.03em">Contact</a>
</div>
</div>
</section>`);
  $('[aria-current="page"]').removeAttr('aria-current');
  fs.writeFileSync(path.join(SITE, '404.html'), $.html());
}

// ---------- runtime, sitemap, robots, headers, redirects ----------
fs.copyFileSync(path.join(ROOT, 'build', 'site.js'), path.join(SITE, 'assets', 'site.js'));

// ---------- actor website template demos (/templates/<look>/) ----------
// Copied as they are, except: internal notes (HANDOFF.md) are never published, and the
// "Website by Sullivan Park Design" credit points back to the Actor Websites page.
const DEMOS_SRC = path.join(ROOT, 'templates-src');
const DEMOS_OUT = path.join(SITE, 'templates');
fs.rmSync(DEMOS_OUT, { recursive: true, force: true });
if (fs.existsSync(DEMOS_SRC)) {
  const copyDemo = (src, out) => {
    fs.mkdirSync(out, { recursive: true });
    for (const ent of fs.readdirSync(src, { withFileTypes: true })) {
      if (ent.name === 'HANDOFF.md' || ent.name.startsWith('.')) continue;
      const s = path.join(src, ent.name), o = path.join(out, ent.name);
      if (ent.isDirectory()) { copyDemo(s, o); continue; }
      if (ent.name.endsWith('.html')) {
        const html = fs.readFileSync(s, 'utf8').replaceAll('href="https://sullivanparkdesign.com"', 'href="https://www.sullivanparkdesign.com/services/actor-websites"');
        fs.writeFileSync(o, html);
      } else fs.copyFileSync(s, o);
    }
  };
  for (const look of fs.readdirSync(DEMOS_SRC)) if (fs.statSync(path.join(DEMOS_SRC, look)).isDirectory()) copyDemo(path.join(DEMOS_SRC, look), path.join(DEMOS_OUT, look));
}

fs.writeFileSync(path.join(SITE, 'sitemap.xml'), '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
  built.map(u => `  <url><loc>${ORIGIN}${u === '/' ? '/' : u}</loc></url>`).join('\n') + '\n</urlset>\n');
fs.writeFileSync(path.join(SITE, 'robots.txt'), `User-agent: *\nAllow: /\n\nSitemap: ${ORIGIN}/sitemap.xml\n`);
fs.writeFileSync(path.join(SITE, '_headers'), `# Keep the preview copy out of Google. Only the real domain may be indexed.
https://:project.pages.dev/*
  X-Robots-Tag: noindex, nofollow
https://:version.:project.pages.dev/*
  X-Robots-Tag: noindex, nofollow

/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN

/images/*
  Cache-Control: public, max-age=31536000, immutable
/media/*
  Cache-Control: public, max-age=31536000, immutable

# Template demos are mostly placeholder text, so keep them out of search results
/templates/*
  X-Robots-Tag: noindex
`);
fs.writeFileSync(path.join(SITE, '_redirects'), `# Old Squarespace addresses -> new pages
/home            /            301
/articles        /resources   301
/articles/*      /resources   301
/blog            /resources   301
/blog/*          /resources   301
/journal         /resources   301
/web-design      /services/website-design   301
/branding        /services/brand-marketing-design   301
/seo             /services/seo   301

# Actor template demos that were renamed
/templates/feature/headshots.html   /templates/headliner/gallery.html   301
/templates/feature/reel.html        /templates/headliner/media.html     301
/templates/feature/*                /templates/headliner/:splat         301
/templates/luminous/headshots.html  /templates/luminous/gallery.html    301
`);
fs.writeFileSync(OWNERS_FILE, JSON.stringify(Object.fromEntries(Object.entries(OWNERS).sort()), null, 1) + '\n');
fs.writeFileSync(path.join(ROOT, 'build', 'last-build.json'), JSON.stringify({ pages: built, images: Object.fromEntries(imgNames), warnings: r.warnings }, null, 1));
console.log(`built ${built.length} pages + 404, ${imgNames.size} images`);
if (r.warnings.length) console.log('warnings:\n  ' + [...new Set(r.warnings)].join('\n  '));
