import { open } from './test-site.mjs';
const O = 'https://www.sullivanparkdesign.com';
import fs from 'node:fs'; fs.mkdirSync('shots', { recursive: true });
const { b, page } = await open();
for (const [u, n] of [['/', 'home'], ['/portfolio/hamish-ross-real-estate', 'hamish'], ['/contact', 'contact'], ['/resources', 'resources']]) {
  for (const w of [1440, 390]) {
    const p = await page(w, w > 600 ? 900 : 844);
    await p.goto(O + u, { waitUntil: 'load' });
    await p.evaluate(async () => { const imgs = [...document.images]; imgs.forEach(i => { i.loading = 'eager'; }); await Promise.all(imgs.map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; setTimeout(r, 6000); }))); });
    await p.addStyleTag({ content: '.sp-reveal{animation:none!important;opacity:1!important;transform:none!important}' });
    await p.screenshot({ path: `shots/${n}-${w}.png`, fullPage: true });
    await p.context().close();
  }
}
await b.close();
