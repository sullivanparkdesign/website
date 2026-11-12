import { open } from './test-site.mjs';
const O = 'https://www.sullivanparkdesign.com';
const { b, page } = await open();
const out = [];
const ok = (name, cond, extra = '') => out.push(`${cond ? 'PASS' : 'FAIL'}  ${name}${extra ? '  ' + extra : ''}`);
// phone menu
let p = await page(390, 844);
await p.goto(O + '/services', { waitUntil: 'load' });
ok('phone menu starts closed', await p.$eval('[data-mnav]', e => e.hidden));
await p.click('[data-menu-toggle]');
ok('menu opens on tap', !(await p.$eval('[data-mnav]', e => e.hidden)), await p.$eval('[data-menu-toggle]', e => 'aria-expanded=' + e.getAttribute('aria-expanded')));
await p.keyboard.press('Escape');
ok('Escape closes the menu', await p.$eval('[data-mnav]', e => e.hidden));
await p.click('[data-menu-toggle]'); await p.click('[data-mnav] a[data-menu-close]');
await p.waitForLoadState('load');
ok('tapping a menu link navigates', p.url() !== O + '/services', p.url());
await p.context().close();
// desktop header + fab + dropdown
p = await page(1440, 900);
await p.goto(O + '/about', { waitUntil: 'load' });
ok('header starts transparent', await p.$eval('[data-header]', e => e.getAttribute('data-scrolled')) === 'false');
await p.mouse.wheel(0, 1200); await p.waitForTimeout(400);
ok('header turns solid on scroll', await p.$eval('[data-header]', e => e.getAttribute('data-scrolled')) === 'true');
ok('back-to-top appears further down', await p.$eval('.sp-fab', e => e.getAttribute('data-show')) === 'true');
await p.evaluate(() => window.scrollTo(0, 0)); await p.waitForTimeout(300);
await p.hover('.sp-dd-about > .sp-navlink'); await p.waitForTimeout(400);
ok('About dropdown opens on hover', await p.$eval('.sp-dd-about .sp-dd-panel', e => getComputedStyle(e).visibility === 'visible'));
await p.keyboard.press('Escape'); await p.waitForTimeout(300);
ok('Escape hides the dropdown', await p.$eval('.sp-dd-about .sp-dd-panel', e => getComputedStyle(e).visibility === 'hidden'));
// FAQ
await p.goto(O + '/services/website-design', { waitUntil: 'load' });
const faq = await p.$('[data-faq-btn="1"]');
if (faq) { await faq.scrollIntoViewIfNeeded(); await faq.click();
  ok('FAQ opens', !(await p.$eval('[data-faq-panel="1"]', e => e.hidden)), await faq.getAttribute('aria-expanded'));
  await faq.click(); ok('FAQ closes', await p.$eval('[data-faq-panel="1"]', e => e.hidden)); } else ok('FAQ present', false);
// actor websites: colourway preview and live demos
await p.goto(O + '/services/actor-websites', { waitUntil: 'load' });
const shown = k => p.$$eval(`.aw-look-${k} .aw-shots img`, a => a.findIndex(i => getComputedStyle(i).opacity === '1'));
ok('first colourway shows to start', await shown('luminous') === 0);
await p.click('.aw-look-luminous .aw-sw:nth-of-type(3)'); await p.waitForTimeout(700);
ok('choosing a colourway swaps the preview', await shown('luminous') === 2);
for (const k of ['luminous', 'editorial', 'headliner']) {
  const href = await p.$eval(`.aw-look-${k} .aw-demo`, a => a.getAttribute('href'));
  const [st, body] = await p.evaluate(u => fetch(u).then(async r => [r.status, await r.text()]), O + new URL(href).pathname);
  ok(`${k} demo link works`, st === 200 && /noindex/.test(body), href);
}
ok('handoff notes are not published', await p.evaluate(u => fetch(u).then(r => r.status), O + '/templates/editorial/HANDOFF.md') === 404);
// placeholders hidden
for (const u of ['/portfolio/the-rooster-den-co', '/portfolio/party-with-laura', '/portfolio/callum-frost', '/testimonials']) {
  await p.goto(O + u, { waitUntil: 'load' });
  const t = await p.evaluate(() => document.body.innerText);
  ok('no placeholders on ' + u, !/placeholder|will go here|coming soon/i.test(t));
}
// contact form
await p.goto(O + '/contact', { waitUntil: 'load' });
await p.click('[data-form-submit]');
ok('empty form shows three errors', await p.$$eval('[data-error]', els => els.filter(e => !e.hidden).length) === 3);
ok('focus moves to first problem', await p.evaluate(() => document.activeElement && document.activeElement.name) === 'name');
await p.fill('#f-name', 'Test Person'); await p.fill('#f-email', 'not-an-email'); await p.fill('#f-message', 'Hello');
await p.click('[data-form-submit]');
ok('bad email flagged', await p.$eval('[data-error="email"]', e => !e.hidden && /valid/.test(e.textContent)));
await p.fill('#f-email', 'test@example.com');
// the form service is mocked here, so tests never send real email
let posted = null;
await p.route('https://formspree.io/**', async r => { posted = r.request().postData() || ''; await r.fulfill({ status: 200, contentType: 'application/json', body: '{"ok":true}' }); });
await p.click('[data-form-submit]');
await p.waitForTimeout(600);
ok('message sends to Formspree', !!posted && /Test Person/.test(posted) && /test@example.com/.test(posted));
ok('subject names the sender', !!posted && /Website enquiry from Test Person/.test(posted));
ok('spam trap left empty', !!posted && /name="_gotcha"\r\n\r\n\r\n/.test(posted));
ok('thank-you message shown', await p.$eval('[data-form-view="sent"]', e => !e.hidden) && await p.$eval('[data-form-view="form"]', e => e.hidden));
await p.click('[data-form-reset]');
await p.unroute('https://formspree.io/**');
await p.route('https://formspree.io/**', r => r.fulfill({ status: 500, body: 'error' }));
await p.fill('#f-name', 'Test Person'); await p.fill('#f-email', 'test@example.com'); await p.fill('#f-message', 'Hello again');
await p.click('[data-form-submit]');
await p.waitForTimeout(600);
ok('if sending fails, details stay and an error shows', await p.$eval('[data-form-view="failed"]', e => !e.hidden && /couldn/.test(e.textContent)) && (await p.inputValue('#f-message')) === 'Hello again');
// home video toggle
await p.goto(O + '/', { waitUntil: 'load' });
ok('hero video present', !!(await p.$('[data-hero-video]')));
await p.click('[data-video-toggle]'); await p.waitForTimeout(200);
ok('video toggle swaps label', /Play|Pause/.test(await p.$eval('[data-video-toggle]', e => e.getAttribute('aria-label'))), await p.$eval('[data-video-toggle]', e => e.getAttribute('aria-label')));
// 404
const r404 = await p.goto(O + '/old-page-that-does-not-exist');
ok('unknown address shows the 404 page', /moved on/.test(await p.textContent('h1')));
console.log(out.join('\n'));
await b.close();
