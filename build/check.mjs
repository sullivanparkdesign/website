import { open, pages, file } from './test-site.mjs';
const O = 'https://www.sullivanparkdesign.com';
const { b, page } = await open();
const list = pages(); let problems = 0;
for (const w of [320, 390, 768, 1100, 1440]) {
  const p = await page(w);
  for (const u of list) {
    await p.goto(O + u, { waitUntil: 'load' });
    const r = await p.evaluate(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth }));
    if (r.sw > r.cw + 1) { problems++; console.log('OVERFLOW', w, u, r.sw); }
  }
  await p.context().close();
}
// links, images, anchors, ids, h1 at desktop
const p = await page(1440);
for (const u of list) {
  await p.goto(O + u, { waitUntil: 'load' });
  await p.evaluate(async () => {
    const imgs = [...document.images]; imgs.forEach(i => { i.loading = 'eager'; });
    await Promise.all(imgs.map(i => i.complete ? 0 : new Promise(r => { i.addEventListener('load', r, { once: true }); i.addEventListener('error', r, { once: true }); setTimeout(r, 8000); })));
  });
  const r = await p.evaluate(() => ({
    bad: [...document.images].filter(i => !i.complete || i.naturalWidth === 0).map(i => i.getAttribute('src')),
    links: [...document.querySelectorAll('a[href]')].map(a => a.getAttribute('href')).filter(h => h.startsWith('/') ),
    anchors: [...document.querySelectorAll('a[href^="#"]')].map(a => a.getAttribute('href')).filter(h => h.length > 1 && !document.getElementById(h.slice(1))),
    blob: document.documentElement.outerHTML.includes('/_blob/'), dc: document.documentElement.outerHTML.includes('.dc.html'),
    holes: /\{\{[^}]*\}\}/.test(document.body.innerHTML), h1: document.querySelectorAll('h1').length,
    canon: document.querySelector('link[rel=canonical]')?.href, robots: document.querySelector('meta[name=robots]')?.content || '',
  }));
  const dead = [...new Set(r.links.map(h => h.split('#')[0]).filter(h => h && !file(h)))];
  const issues = [];
  if (r.bad.length) issues.push('broken images ' + r.bad.join(','));
  if (dead.length) issues.push('dead links ' + dead.join(','));
  if (r.anchors.length) issues.push('dead anchors ' + [...new Set(r.anchors)].join(','));
  if (r.blob) issues.push('canvas image path left'); if (r.dc) issues.push('.dc.html link left'); if (r.holes) issues.push('template hole left');
  if (r.h1 !== 1) issues.push('h1 count ' + r.h1); if (r.robots) issues.push('robots ' + r.robots);
  if (issues.length) { problems++; console.log(u, issues.join(' | ')); }
}
console.log(list.length, 'pages checked,', problems, 'problems');
await b.close();
