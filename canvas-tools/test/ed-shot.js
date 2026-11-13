const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const dir = __dirname;
const route = async (route) => {
  const u = new URL(route.request().url()); let p = decodeURIComponent(u.pathname);
  if (p.startsWith('/_blob/')) { const f = path.join(dir, '_blob', p.slice(7)); if (fs.existsSync(f)) { const buf = fs.readFileSync(f); return route.fulfill({ status: 200, body: buf, contentType: buf.slice(8,12).toString() === 'WEBP' ? 'image/webp' : (buf.slice(0,4).toString('hex') === '89504e47' ? 'image/png' : 'image/jpeg') }); } return route.fulfill({ status: 404, body: '' }); }
  const f = path.join(dir, p.replace(/^\//, '')); if (fs.existsSync(f)) return route.fulfill({ status: 200, body: fs.readFileSync(f), contentType: 'text/html' }); return route.fulfill({ status: 404, body: '' });
};
(async () => {
  const b = await chromium.launch({ proxy: process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined });
  const mode = process.argv[2] || 'full';
  const widths = (process.argv[3] || '1440,390').split(',').map(Number);
  for (const w of widths) {
    const ctx = await b.newContext({ reducedMotion: 'no-preference', viewport: { width: w, height: w > 600 ? 900 : 844 } });
    await ctx.route('http://preview.test/**', route);
    const p = await ctx.newPage();
    const errs = []; p.on('pageerror', e => errs.push(String(e)));
    await p.goto('http://preview.test/' + (process.env.PAGE || 'Article-Editorial') + '.html', { waitUntil: 'load' });
    await p.evaluate(async () => { await document.fonts.ready; });
    await p.waitForTimeout(500);
    if (mode === 'full') {
      await p.evaluate(() => { document.querySelectorAll('.sp-fab').forEach(e => e.style.display = 'none'); document.querySelector('.sp-header').style.position = 'absolute'; document.querySelectorAll('.sp-reveal').forEach(e => { e.style.animation = 'none'; e.style.opacity = 1; e.style.translate = 'none'; }); });
      const info = await p.evaluate(() => {
        const over = [...document.querySelectorAll('body *')].filter(e => { const r = e.getBoundingClientRect(); return r.width && (r.right > innerWidth + 1) && !e.closest('.ed-bleed') && !e.closest('.ed-cover') && getComputedStyle(e).position !== 'fixed'; }).slice(0, 6).map(e => e.className + ' ' + Math.round(e.getBoundingClientRect().right));
        return { h: document.documentElement.scrollHeight, sw: document.documentElement.scrollWidth, over, broken: [...document.images].filter(i => !i.naturalWidth).map(i => i.src) };
      });
      console.log(w, JSON.stringify(info), errs.join(' | '));
      await p.screenshot({ path: path.join(dir, `ed-${process.env.PAGE || 'x'}-${w}-full.png`), fullPage: true });
    }
    if (mode === 'scroll') {
      for (const id of (process.argv[4] || 'current,brand,features').split(',')) {
        await p.evaluate((id) => { const el = document.getElementById(id); window.scrollTo(0, el.getBoundingClientRect().top + scrollY - 200); }, id);
        await p.waitForTimeout(700);
        const active = await p.evaluate(() => [...document.querySelectorAll('.ed-rail a')].filter(a => getComputedStyle(a).color === 'rgb(18, 20, 20)').map(a => a.textContent));
        console.log(w, id, 'active:', JSON.stringify(active));
        await p.screenshot({ path: path.join(dir, `ed-${w}-at-${id}.png`) });
      }
    }
    if (mode === 'interact') {
      await p.evaluate(() => { document.querySelector('.ed-goal').scrollIntoView({ block: 'center' }); });
      await p.click('.ed-goal:nth-child(2)'); await p.waitForTimeout(500);
      const g = await p.locator('.ed-goals').boundingBox();
      await p.screenshot({ path: path.join(dir, `ed-${w}-goals.png`), clip: { x: 0, y: Math.max(0, g.y - 30), width: w, height: g.height + 60 } });
      await p.evaluate(() => document.getElementById('ed-checklist').scrollIntoView());
      for (const i of [1, 2, 4, 6]) await p.click(`label:has(#ed-ck${i})`);
      await p.waitForTimeout(600);
      await p.screenshot({ path: path.join(dir, `ed-${w}-checklist.png`), fullPage: false });
      for (const i of [3, 5, 7, 8, 9]) await p.click(`label:has(#ed-ck${i})`);
      await p.waitForTimeout(600);
      const st = await p.locator('.ed-cl-status').boundingBox();
      await p.evaluate((y) => window.scrollTo(0, y + scrollY - 200), st.y);
      await p.waitForTimeout(300);
      await p.screenshot({ path: path.join(dir, `ed-${w}-checklist-done.png`), fullPage: false });
      console.log(w, 'checked', await p.evaluate(() => document.querySelectorAll('.ed-cl input:checked').length), 'done msg', await p.evaluate(() => getComputedStyle(document.querySelector('.ed-cl-msg-done')).display));
    }
    await ctx.close();
  }
  await b.close();
})();
