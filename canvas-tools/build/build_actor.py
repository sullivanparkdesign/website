"""Actor Websites page (Actor-Websites.dc.html): the three custom-coded actor looks with live demos.
Run: python3 build/build_actor.py canvas/project   (then nav_upgrade.py)"""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import case_common as C

ROOT = sys.argv[1]
SERIF, ARROW, WRAP, PAD = C.SERIF, C.ARROW, C.WRAP, C.SECTION_PAD
TEAL, INK, BODY, MUTED = '#4E6368', '#121414', '#1F2426', '#4E5558'
DEMO = 'https://www.sullivanparkdesign.com/templates/'
EXT = '<svg width="12" height="12" viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M4.5 2H2v8h8V7.5M7 2h3v3M10 2 5.5 6.5" stroke="currentColor" stroke-width="1.1"></path></svg>'
PALM = '<img class="sp-sway" src="/_blob/fddc24a18e2595d21f63da9f1d7bf0d5" alt="" width="1800" height="1200" style="position: absolute; top: -20px; right: -20px; width: min(1320px, 110vw); height: auto; max-width: none; opacity: 0.16; mix-blend-mode: multiply; pointer-events: none; z-index: 0">'

LOOKS = [
    dict(key='luminous', name='Luminous', person='Hannah Ross',
         line='Soft and refined, with rounded serif headings, framed photos and rich bands for your story and your reel.',
         points=['An offset frame behind each photo, and thin rules finished with a small star', 'A gallery for headshots, production stills and stage photos', 'Includes a contact form'],
         pals=[('Navy &amp; Gold', ['#1c2b45', '#e2e6e9', '#c2a060'], '701cecdd168e1a625db8f130b38de806'),
               ('Sea Glass', ['#f5f3ee', '#8fbcb6', '#2b4f52'], 'a00522c050f4d48cf043145e3b7941cf'),
               ('Popcorn', ['#fbf3d6', '#fffbf2', '#c99b2c'], '4149ac54b72a923ee4eae1b15075ea41')]),
    dict(key='editorial', name='Editorial', person='Callum Frost',
         line='Magazine style, with a letterspaced name, italic serif titles, numbered sections and staggered headshots.',
         points=['Headshots visitors can filter by type', 'A ready-made “coming soon” reel section, for when you don’t have a reel yet', 'Includes a contact form'],
         pals=[('Stone', ['#1b2530', '#3d5a78', '#eef0ef'], '78a3e0507bc9cc66ab01029492bacc43'),
               ('Denim', ['#4a4f5e', '#e5e5e5', '#c5cab9'], 'a953b79bb3dfffd31a68944cd7023d72'),
               ('Sage', ['#5e6e62', '#f4eddd', '#f9eecf'], 'ec7f0f7d1c8fc50c29fd557e2038125f')]),
    dict(key='headliner', name='Headliner', person='Natasha Young',
         line='Cinematic and simple: one full-screen photo and your name on the home page, with no credits up front.',
         points=['Wide, cinema-style crops, and a gallery with a different layout in each section', 'Your home photo eases gently into place as the page opens', 'No contact form, so there’s no extra account to set up'],
         pals=[('Sky', ['#f4f6f9', '#e1e9f2', '#24477a'], '60296e964c11878f2403a88af5ee56d4'),
               ('Charcoal', ['#131518', '#93b0e6', '#eceef1'], 'df7694f2840b9d6056fcdc0db910a03b'),
               ('Garnet', ['#ffffff', '#ececee', '#8c1c2b'], '340a3ebdf973e98d478633e6b721a55d')]),
]
PHONES = [('486a8a3d6be578c3ac350cb6a2ff6501', 'The Luminous look on a phone'), ('b95e5af154fbc22ab85573cbcf79d9a9', 'The Editorial look on a phone'),
          ('7631c869597229b71a306cd2c4d838cc', 'The Headliner look on a phone')]


def btn(href, text, dark=True, ext=False):
    tgt = ' target="_blank" rel="noopener"' if ext else ''
    if dark:
        return f'<a class="sp-btn sp-btn-blue" href="{href}"{tgt} style="display: inline-flex; align-items: center; justify-content: center; gap: 14px; min-height: 56px; padding: 0 30px; background: {TEAL}; border: 1px solid {TEAL}; color: #FFFFFF; text-decoration: none; font-size: 18px; letter-spacing: 0.03em">{text}{ARROW}</a>'
    return f'<a class="sp-btn sp-btn-ghost" href="{href}"{tgt} style="display: inline-flex; align-items: center; justify-content: center; gap: 14px; min-height: 56px; padding: 0 30px; background: transparent; border: 1px solid {TEAL}; color: {INK}; text-decoration: none; font-size: 18px; letter-spacing: 0.03em">{text}{ARROW}</a>'


# ------------------------------------------------------------------ sections
phones = ''.join(f'<div class="aw-phone aw-phone-{i}"><img src="/_blob/{b}" alt="{a}" width="780" height="1688"{" fetchpriority=\"high\"" if i == 1 else " loading=\"lazy\""}></div>' for i, (b, a) in enumerate(PHONES))
HERO = f'''<!-- HERO -->
<section aria-labelledby="page-title" class="aw-hero" style="position: relative; overflow: hidden; background: #FAFAF8">
{PALM}
<div class="aw-hero-in" style="position: relative; z-index: 1; {WRAP}">
<div class="aw-hero-text">
{C.label('Actor Websites')}
<h1 id="page-title" class="aw-title">Your own website, made for <em>actors</em></h1>
<p class="aw-lede">A polished home for your headshots, resume and reel, in a look you choose and colours that suit you. You update your headshots, credits and bio yourself, whenever you like.</p>
<div class="aw-price-row"><span class="aw-price">$650<span class="aw-tax">+ tax</span></span><span class="aw-price-note">One-time, with your first year of care included</span></div>
<div style="display: flex; flex-wrap: wrap; gap: 14px">{btn('#looks', 'See the Looks')}{btn('Contact.dc.html', 'Enquire About Your Project', dark=False)}</div>
</div>
<div class="aw-phones" aria-hidden="false">{phones}</div>
</div>
</section>'''


def look_row(i, L):
    k = L['key']
    radios = ''.join(f'''<label class="aw-sw"><input class="aw-vh" type="radio" name="aw-{k}" id="aw-{k}-{j}"><span class="aw-dots" aria-hidden="true">{''.join(f'<i style="background: {c}"></i>' for c in cols)}</span><span>{name}</span></label>''' for j, (name, cols, _) in enumerate(L['pals']))
    imgs = ''.join(f'<img src="/_blob/{b}" alt="The {L["name"]} look in {name}, shown with {L["person"]}’s photos" width="1800" height="1125" loading="lazy">' for name, _, b in L['pals'])
    pts = ''.join(f'<li>{p}</li>' for p in L['points'])
    return f'''<article class="aw-look aw-look-{k}{' aw-flip' if i % 2 else ''} sp-reveal" aria-labelledby="aw-{k}-h">
<div class="aw-look-media">
<div class="aw-browser"><div class="aw-browser-bar" aria-hidden="true"><i></i><i></i><i></i></div><div class="aw-shots">{imgs}</div></div>
<fieldset class="aw-sws"><legend class="aw-vh">Preview the {L['name']} colourways</legend>{radios}</fieldset>
</div>
<div class="aw-look-text">
<p class="aw-look-n">{i + 1:02d}</p>
<h3 id="aw-{k}-h" class="aw-look-h">{L['name']}</h3>
<p class="aw-look-line">{L['line']}</p>
<ul class="aw-look-pts">{pts}</ul>
<a class="aw-demo" href="{DEMO}{k}/" target="_blank" rel="noopener">Try the Live Demo{EXT}<span class="aw-vh"> (opens in a new tab)</span></a>
</div>
</article>'''


LOOKS_SEC = f'''<!-- THE LOOKS -->
<section id="looks" aria-labelledby="looks-title" style="background: #FFFFFF; scroll-margin-top: 80px">
<div style="{WRAP}; {PAD}; display: flex; flex-direction: column; gap: clamp(64px, 7vw, 112px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 24px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 26px">{C.label('Three Looks')}{C.h2('looks-title', 'Choose a look, then make it', 'yours')}</div>
<div style="flex: 1 1 420px; min-width: 0">{C.p('Each look comes in three colourways, or for an additional $75 I can set it up in your own colours and fonts. Try them here, or open a live demo and click through every page. The demos use placeholder text, so you can picture your own.')}</div>
</div>
{chr(10).join(look_row(i, L) for i, L in enumerate(LOOKS))}
</div>
</section>'''

INCLUDED = [
    ('Six pages', 'Home, about, gallery, reel, resume and contact.'),
    ('Your look and colours', 'Any of the three looks, in the colourway that suits you, or your own colours and fonts for an additional $75.'),
    ('Your own edit screen', 'Update headshots, credits, training, skills and your bio, then publish. Your site updates about a minute later.'),
    ('A resume that prints', 'Your resume page prints as a clean, one-page resume.'),
    ('Your reel on the page', 'YouTube and Vimeo reels play right on your site.'),
    ('Ready for search', 'Page titles, descriptions, structured data, a sitemap and a summary for AI search tools.'),
    ('No monthly hosting fee', 'Fast, secure hosting is included.'),
    ('Your name, your domain', 'You own your web address, and I connect it for you.'),
]
inc = ''.join(f'<li><span class="aw-inc-n" aria-hidden="true">{i:02d}</span><span class="aw-inc-h">{h}</span><span class="aw-inc-t">{t}</span></li>' for i, (h, t) in enumerate(INCLUDED, 1))
INCLUDED_SEC = f'''<!-- WHAT'S INCLUDED -->
<section aria-labelledby="inc-title" style="background: #FAFAF8">
<div style="{WRAP}; {PAD}; display: flex; flex-direction: column; gap: clamp(48px, 5vw, 72px)">
<div class="sp-reveal" style="display: flex; flex-direction: column; gap: 26px">{C.label('What’s Included')}{C.h2('inc-title', 'Everything an actor’s site', 'needs')}</div>
<ul class="aw-inc sp-reveal">{inc}</ul>
</div>
</section>'''

PRICING_SEC = f'''<!-- PRICING -->
<section class="sp-on-dark" aria-labelledby="price-title" style="position: relative; overflow: hidden; background: {TEAL}; color: #FFFFFF">
{PALM.replace('opacity: 0.16', 'opacity: 0.2')}
<div style="position: relative; z-index: 1; {WRAP}; {PAD}">
<div class="aw-pricing">
<div class="aw-pricing-intro sp-reveal">
{C.label('Pricing', '#DCE4E5')}
<h2 id="price-title" class="aw-price-h">One price, <em>any look</em></h2>
<p class="aw-price-p">Your only other cost is your domain name, which you own and renew yourself.</p>
</div>
<div class="aw-cards sp-reveal">
<div class="aw-card aw-card-main"><p class="aw-card-l">Your website</p><p class="aw-card-price">$650<span class="aw-tax">+ tax</span></p><p class="aw-card-sub">One-time</p>
<ul><li>Your choice of look and colourway</li><li>Six pages and your own edit screen</li><li>Domain connected, search-ready setup</li><li>Your first year of care included</li></ul></div>
<div class="aw-card"><p class="aw-card-l">Care, after year one</p><p class="aw-card-price">$100<span class="aw-tax">+ tax</span></p><p class="aw-card-sub">A year, optional</p>
<ul><li>Up to 3 change requests a year, for new wording or small design tweaks</li><li>Help if you get stuck with your edit screen</li><li>Headshots, credits and your bio are always yours to update</li></ul></div>
</div>
<div class="aw-addon sp-reveal"><div class="aw-addon-text"><p class="aw-card-l">Optional add-on</p><p class="aw-addon-h">Your own colours and fonts</p><p class="aw-addon-t">Want something other than the three colourways? I’ll set up any look in colours and a font pairing chosen just for you, checked so every page stays easy to read.</p></div><p class="aw-addon-price">+$75<span>Additional, plus tax</span></p></div>
</div>
<p class="aw-request sp-reveal">A change request is one email with a batch of changes. Five small tweaks sent together count as one request.</p>
</div>
</section>'''

STEPS = [('Choose your look', 'Pick Luminous, Editorial or Headliner, and the colourway you like best.'),
         ('Send me your materials', 'Your headshots, resume, reel links and a short bio. I’ll help you organize them.'),
         ('I build your site', 'I set up your pages, connect your domain and make sure everything is ready for search.'),
         ('Keep it current yourself', 'Update your headshots, credits and bio whenever you book something new.')]
steps = ''.join(f'<li><span class="aw-step-n">{i:02d}</span><span class="aw-step-h">{h}</span><span class="aw-step-t">{t}</span></li>' for i, (h, t) in enumerate(STEPS, 1))
HOW_SEC = f'''<!-- HOW IT WORKS -->
<section aria-labelledby="how-title" style="background: #FFFFFF">
<div style="{WRAP}; {PAD}; display: flex; flex-direction: column; gap: clamp(48px, 5vw, 72px)">
<div class="sp-reveal" style="display: flex; flex-direction: column; gap: 26px">{C.label('How It Works')}{C.h2('how-title', 'From headshots to', 'live site')}</div>
<ol class="aw-steps sp-reveal">{steps}</ol>
<aside class="aw-young sp-reveal" aria-labelledby="young-title">
<p id="young-title" class="aw-young-h">Building for a young actor?</p>
<p class="aw-young-t">I keep personal phone numbers, emails and home addresses off the site and use your agent’s details instead. If you’d like a contact form, I set it up in a parent’s name, so messages go to you.</p>
</aside>
</div>
</section>'''

FAQS = [
    ('Is there a monthly fee?', 'No. Hosting is included, and there’s no monthly platform fee. Your only ongoing cost is your domain name, which you own. After your first year, care is optional at $100 a year plus tax.'),
    ('Can I update the site myself?', 'Yes. Your edit screen lets you add and reorder headshots, update your credits, training and skills, add a resume PDF and edit your bio. Press Publish changes and your site updates about a minute later.'),
    ('Could I break the design by mistake?', 'No. The edit screen only changes your content, never the fonts, colours or layout. Every change is saved, so nothing is ever lost.'),
    ('Do I need a contact form?', 'It’s up to you. Luminous and Editorial include one, set up in your name (or a parent’s), so messages go straight to you. Headliner uses an email link instead, so there’s no extra account to create.'),
    ('What if I’d rather use Squarespace?', 'I build on Squarespace too. If you’d like to edit everything yourself in Squarespace, ask me about that option.'),
]


def faq_item(i, q, a):
    return f'''<div style="border-top: 1px solid rgba(18, 20, 20, 0.16)">
<h3 style="margin: 0"><button id="faq-{i + 1}-btn" class="sp-faq-btn" type="button" aria-expanded="{{{{faq{i}Expanded}}}}" aria-controls="faq-{i + 1}-panel" onClick="{{{{toggleFaq{i}}}}}" style="width: 100%; display: flex; justify-content: space-between; align-items: center; gap: 28px; padding: 22px 0; background: transparent; border: 0; cursor: pointer; text-align: left; color: #121414"><span class="sp-faq-q" style="font-family: {SERIF}; font-weight: 400; font-size: clamp(22px, 1.9vw, 27px); line-height: 1.25">{q}</span><span class="sp-plus" aria-hidden="true" style="flex: none; width: 40px; height: 40px; display: inline-flex; align-items: center; justify-content: center; border: 1px solid #4E6368; color: #4E6368"><svg width="12" height="12" viewBox="0 0 14 14" fill="none"><path d="M7 1v12M1 7h12" stroke="currentColor" stroke-width="1.2"></path></svg></span></button></h3>
<sc-if value="{{{{faq{i}Open}}}}" hint-placeholder-val="{{{{{'true' if i == 0 else 'false'}}}}}"><div id="faq-{i + 1}-panel" style="padding: 0 68px 26px 0"><p style="margin: 0; font-size: 18px; line-height: 1.7; color: #1F2426">{a}</p></div></sc-if>
</div>'''


FAQ_SEC = f'''<!-- FAQ -->
<section aria-labelledby="faq-title" style="background: #FAFAF8">
<div style="width: 100%; max-width: 1680px; margin: 0 auto; padding: clamp(80px, 9vw, 128px) clamp(20px, 5vw, 72px); display: flex; flex-wrap: wrap; align-items: flex-start; gap: 40px clamp(48px, 7vw, 120px)">
<div class="sp-reveal" style="flex: 1 1 360px; max-width: 520px; min-width: 0; display: flex; flex-direction: column; gap: 22px">
{C.label('FAQ')}
<h2 id="faq-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(40px, 4.4vw, 66px); line-height: 1.04; color: #121414; text-wrap: balance">Actor website <em style="font-style: italic; color: #4E6368">questions</em></h2>
</div>
<div class="sp-reveal" style="flex: 1.6 1 600px; min-width: 0; display: flex; flex-direction: column; border-bottom: 1px solid rgba(18, 20, 20, 0.16)">
{chr(10).join(faq_item(i, q, a) for i, (q, a) in enumerate(FAQS))}
</div>
</div>
</section>'''

CLOSING_RAW = C.closing('Ready for a website as polished as', 'your headshots?').replace(
    'Tell me about your business and what you’d like your website to do.', 'Tell me which look you love and where you are in your career, and we’ll take it from there.')
# a hairline at content width so the FAQ and the closing section (same background) don't run together
OPEN = '<section aria-labelledby="cta-title" style="position: relative; overflow: hidden; background: #FAFAF8">'
assert CLOSING_RAW.count(OPEN) == 1
CLOSING_WITH_LINE = CLOSING_RAW.replace(OPEN, OPEN + '\n<div aria-hidden="true" style="position: relative; z-index: 1; max-width: 1680px; margin: 0 auto; padding: 0 clamp(20px, 5vw, 72px)"><div style="border-top: 1px solid rgba(78, 99, 104, 0.35)"></div></div>', 1)


# fully custom builds, with Callum Frost's 2.0 site as the example
CUSTOM_BTN = 'display: inline-flex; align-items: center; justify-content: center; gap: 14px; min-height: 56px; padding: 0 30px; text-decoration: none; font-size: 18px; letter-spacing: 0.03em'
CUSTOM_SEC = f'''<!-- FULLY CUSTOM -->
<section class="sp-on-dark" aria-labelledby="custom-title" style="position: relative; overflow: hidden; background: #141414; color: #FFFFFF">
<div aria-hidden="true" style="position: absolute; inset: 0; pointer-events: none; background: radial-gradient(ellipse 55% 60% at 100% 0%, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0) 70%)"></div>
<div style="position: relative; z-index: 1; {WRAP}; {PAD}">
<div class="aw-custom">
<div class="aw-custom-text sp-reveal">
{C.label('Fully Custom', '#BDBDBD')}
<h2 id="custom-title" class="aw-custom-h">Want something <em>one of a kind?</em></h2>
<p class="aw-custom-p">I also design fully custom actor websites from scratch, built around you and your work. Callum Frost’s new site is a recent example, with film-inspired details like a running timecode on the homepage, film-strip frames around his photos and a photo viewer.</p>
<p class="aw-custom-price"><span>Custom builds start at</span>$2,000<span class="aw-tax">+ tax</span></p>
<div style="display: flex; flex-wrap: wrap; gap: 14px">
<a class="sp-btn" href="Callum-Frost.dc.html" style="{CUSTOM_BTN}; background: #FFFFFF; border: 1px solid #FFFFFF; color: #141414">View Callum’s Project{ARROW}</a>
<a class="sp-btn" href="Contact.dc.html" style="{CUSTOM_BTN}; background: transparent; border: 1px solid rgba(255, 255, 255, 0.6); color: #FFFFFF">Enquire About Your Project{ARROW}</a>
</div>
</div>
<div class="aw-custom-media sp-reveal">
<div class="aw-custom-desk">{C.desk('/_blob/d3978c904a489af5909028a3ecb4bb5a', 'Callum Frost’s custom-coded website on a desktop screen', 'callumfrost.com', 1800, 1125, dark=True)}</div>
<div class="aw-custom-phone">{C.phone('/_blob/d9565222a636eaef6c6bdb26170739fa', 'Callum Frost’s custom-coded website on a phone')}</div>
</div>
</div>
</div>
</section>'''
CLOSING = CLOSING_WITH_LINE

CSS = r'''/* ACTOR WEBSITES */
.aw-vh{position:absolute !important;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.aw-hero-in{display:grid;grid-template-columns:minmax(0,1fr);gap:clamp(48px,6vw,72px);padding-top:clamp(132px,12vw,180px);padding-bottom:clamp(72px,8vw,112px)}
.aw-hero-text{display:flex;flex-direction:column;gap:clamp(22px,2.2vw,30px);min-width:0}
.aw-title{margin:0;font-family:'Cormorant Infant',Garamond,serif;font-weight:300;font-size:clamp(50px,6.6vw,112px);line-height:.98;letter-spacing:-.02em;color:#121414;text-wrap:balance}
.aw-title em{font-style:italic;color:#4E6368}
.aw-lede{margin:0;font-size:clamp(19px,1.5vw,22px);line-height:1.65;color:#1F2426}
.aw-price-row{display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 18px;padding:18px 0;border-top:1px solid rgba(78,99,104,.3);border-bottom:1px solid rgba(78,99,104,.3)}
.aw-price{font-family:'Cormorant Infant',Garamond,serif;font-weight:300;font-size:clamp(48px,4.4vw,64px);line-height:1;color:#121414}
.aw-price-note{font-size:16px;letter-spacing:.06em;color:#4E5558}
.aw-phones{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(12px,1.6vw,24px);align-items:end;width:100%;max-width:620px;justify-self:center}
.aw-phone{border-radius:28px;overflow:hidden;background:#121414;padding:7px;box-shadow:0 40px 70px -34px rgba(18,28,30,.55)}
.aw-phone img{display:block;width:100%;aspect-ratio:390/844;object-fit:cover;object-position:50% 0;border-radius:22px}
.aw-phone-1{margin-bottom:clamp(32px,4vw,64px)}
@media (min-width:1000px){.aw-hero-in{grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);align-items:center;column-gap:clamp(56px,6vw,112px)}.aw-phones{justify-self:end}}

.aw-look{display:grid;grid-template-columns:minmax(0,1fr);gap:32px;align-items:center}
@media (min-width:1000px){.aw-look{grid-template-columns:minmax(0,1.45fr) minmax(0,1fr);column-gap:clamp(48px,6vw,104px)}.aw-flip .aw-look-media{order:2}}
.aw-look-media{display:flex;flex-direction:column;gap:18px;min-width:0}
.aw-browser{background:#FFFFFF;border:1px solid rgba(78,99,104,.28);box-shadow:0 40px 80px -44px rgba(18,28,30,.5);overflow:hidden}
.aw-browser-bar{height:30px;display:flex;align-items:center;gap:7px;padding:0 14px;border-bottom:1px solid rgba(78,99,104,.18);background:#FAFAF8}
.aw-browser-bar i{width:9px;height:9px;border-radius:50%;background:#D5DAD9}
.aw-shots{position:relative;aspect-ratio:16/10;background:#ECEEED}
.aw-shots img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 0;opacity:0;transition:opacity .5s ease}
.aw-shots img:first-child{opacity:1}
.aw-look:has(.aw-sw:nth-of-type(2) input:checked) .aw-shots img,.aw-look:has(.aw-sw:nth-of-type(3) input:checked) .aw-shots img{opacity:0}
.aw-look:has(.aw-sw:nth-of-type(2) input:checked) .aw-shots img:nth-child(2){opacity:1}
.aw-look:has(.aw-sw:nth-of-type(3) input:checked) .aw-shots img:nth-child(3){opacity:1}
.aw-sws{border:0;margin:0;padding:0;min-width:0;display:flex;flex-wrap:wrap;gap:10px}
.aw-sw{cursor:pointer;display:inline-flex;align-items:center;gap:12px;min-height:44px;padding:8px 16px 8px 12px;border:1px solid rgba(78,99,104,.45);background:#FFFFFF;font-size:14px;letter-spacing:.12em;text-transform:uppercase;color:#1F2426;transition:background-color .3s,color .3s,border-color .3s}
.aw-sw:hover{border-color:#4E6368}
.aw-dots{display:flex;padding-left:4px}
.aw-dots i{width:16px;height:16px;border-radius:50%;margin-left:-4px;box-shadow:0 0 0 2px #FFFFFF,inset 0 0 0 1px rgba(18,20,20,.16)}
.aw-sw:has(input:checked),.aw-look:not(:has(.aw-sw input:checked)) .aw-sw:first-of-type{background:#121414;border-color:#121414;color:#FFFFFF}
.aw-sw:has(input:focus-visible){outline:2px solid #4E6368;outline-offset:3px}
.aw-look-text{display:flex;flex-direction:column;gap:18px;min-width:0}
.aw-look-n{margin:0;font-family:'Cormorant Infant',Garamond,serif;font-style:italic;font-weight:300;font-size:clamp(56px,5vw,84px);line-height:.8;color:#4E6368}
.aw-look-h{margin:0;font-family:'Cormorant Infant',Garamond,serif;font-weight:300;font-size:clamp(40px,3.8vw,60px);line-height:1;color:#121414}
.aw-look-line{margin:0;font-size:20px;line-height:1.65;color:#1F2426}
.aw-look-pts{list-style:none;margin:4px 0 6px;padding:0;border-top:1px solid rgba(78,99,104,.25)}
.aw-look-pts li{padding:12px 0 12px 22px;border-bottom:1px solid rgba(78,99,104,.25);position:relative;font-size:17px;line-height:1.5;color:#1F2426}
.aw-look-pts li::before{content:"";position:absolute;left:2px;top:22px;width:9px;height:1px;background:#4E6368}
.aw-demo{align-self:flex-start;display:inline-flex;align-items:center;gap:10px;min-height:44px;color:#4E6368;font-size:18px;letter-spacing:.03em;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:6px}

.aw-inc{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,250px),1fr));gap:1px;background:rgba(78,99,104,.22);border:1px solid rgba(78,99,104,.22)}
.aw-inc li{background:#FAFAF8;padding:28px 26px 30px;display:flex;flex-direction:column;gap:10px}
.aw-inc-n{font-family:'Cormorant Infant',Garamond,serif;font-style:italic;font-size:22px;color:#4E6368}
.aw-inc-h{font-family:'Cormorant Infant',Garamond,serif;font-size:26px;line-height:1.15;color:#121414}
.aw-inc-t{font-size:17px;line-height:1.6;color:#1F2426}
@media (min-width:1100px){.aw-inc{grid-template-columns:repeat(4,minmax(0,1fr))}}

.aw-pricing{display:grid;grid-template-columns:minmax(0,1fr);gap:clamp(40px,5vw,64px)}
@media (min-width:1000px){.aw-pricing{grid-template-columns:minmax(0,.8fr) minmax(0,1.4fr);align-items:start;column-gap:clamp(56px,7vw,120px)}}
.aw-pricing-intro{display:flex;flex-direction:column;gap:24px}
.aw-price-h{margin:0;text-wrap:balance;font-family:'Cormorant Infant',Garamond,serif;font-weight:300;font-size:clamp(46px,5vw,80px);line-height:1;color:#FFFFFF}
.aw-price-h em{font-style:italic;color:#DCE4E5}
.aw-price-p{margin:0;font-size:19px;line-height:1.7;color:#E8EEEF}
.aw-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr));gap:16px}
.aw-card{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.28);padding:30px 28px 32px;display:flex;flex-direction:column;gap:6px}
.aw-card-main{background:#FAFAF8;border-color:#FAFAF8;color:#121414}
.aw-card-l{margin:0;font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:#DCE4E5}
.aw-card-main .aw-card-l{color:#4E6368}
.aw-card-price{margin:10px 0 0;font-family:'Cormorant Infant',Garamond,serif;font-weight:300;font-size:clamp(56px,5vw,76px);line-height:1;color:#FFFFFF}
.aw-card-main .aw-card-price{color:#121414}
.aw-card-sub{margin:0 0 14px;font-size:15px;letter-spacing:.08em;color:#DCE4E5}
.aw-card-main .aw-card-sub{color:#4E5558}
.aw-card ul{list-style:none;margin:0;padding:0;border-top:1px solid rgba(255,255,255,.25)}
.aw-card-main ul{border-top-color:rgba(78,99,104,.25)}
.aw-card li{padding:12px 0;border-bottom:1px solid rgba(255,255,255,.18);font-size:17px;line-height:1.5;color:#FFFFFF}
.aw-card-main li{border-bottom-color:rgba(78,99,104,.2);color:#1F2426}
.aw-addon{margin-top:calc(16px - clamp(40px,5vw,64px));display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px 40px;padding:26px 28px;border:1px solid rgba(255,255,255,.28);background:rgba(255,255,255,.06)}
.aw-addon-text{flex:1 1 460px;min-width:0;display:flex;flex-direction:column;gap:6px}
.aw-addon-h{margin:0;font-family:'Cormorant Infant',Garamond,serif;font-size:clamp(28px,2.4vw,34px);line-height:1.15;color:#FFFFFF}
.aw-addon-t{margin:0;font-size:17px;line-height:1.6;color:#E8EEEF}
.aw-addon-price span{display:block;margin-top:8px;font-family:Abel,sans-serif;font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:#DCE4E5}
.aw-addon-price{margin:0;flex:none;font-family:'Cormorant Infant',Garamond,serif;font-weight:300;font-size:clamp(48px,4vw,60px);line-height:1;color:#FFFFFF}
@media (min-width:1000px){.aw-addon{grid-column:2}}
.aw-request{margin:clamp(32px,4vw,48px) 0 0;font-size:16px;line-height:1.7;letter-spacing:.02em;color:#E8EEEF}

.aw-steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:clamp(24px,2.6vw,40px)}
.aw-steps li{display:flex;flex-direction:column;gap:12px;padding-top:22px;border-top:1px solid #4E6368}
.aw-step-n{font-family:'Cormorant Infant',Garamond,serif;font-style:italic;font-weight:300;font-size:46px;line-height:.9;color:#4E6368}
.aw-step-h{font-family:'Cormorant Infant',Garamond,serif;font-size:27px;line-height:1.15;color:#121414}
.aw-step-t{font-size:17px;line-height:1.65;color:#1F2426}
.aw-young{display:flex;flex-wrap:wrap;align-items:baseline;gap:12px 40px;padding:28px clamp(22px,3vw,40px);background:#FAFAF8;border-left:2px solid #4E6368}
.aw-young-h{margin:0;flex:0 1 auto;font-family:'Cormorant Infant',Garamond,serif;font-style:italic;font-size:28px;line-height:1.2;color:#121414}
.aw-young-t{margin:0;flex:1 1 420px;min-width:0;font-size:18px;line-height:1.7;color:#1F2426}
.aw-tax{margin-left:10px;font-family:Abel,'Helvetica Neue',Arial,sans-serif;font-size:clamp(15px,1.2vw,18px);font-weight:400;font-style:normal;letter-spacing:.06em;opacity:.78}
.aw-custom{display:grid;grid-template-columns:minmax(0,1fr);gap:clamp(48px,6vw,80px);align-items:center}
@media (min-width:1000px){.aw-custom{grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);column-gap:clamp(56px,6vw,104px)}}
.aw-custom-text{display:flex;flex-direction:column;gap:24px;min-width:0}
.aw-custom-h{margin:0;font-family:'Cormorant Infant',Garamond,serif;font-weight:300;font-size:clamp(44px,4.6vw,72px);line-height:1.02;color:#FFFFFF;text-wrap:balance}
.aw-custom-h em{font-style:italic;color:#BDBDBD}
.aw-custom-p{margin:0;font-size:19px;line-height:1.7;color:rgba(255,255,255,.86)}
.aw-custom-price{margin:0;padding:18px 0;display:flex;flex-wrap:wrap;align-items:baseline;gap:8px 0;border-top:1px solid rgba(255,255,255,.22);border-bottom:1px solid rgba(255,255,255,.22);font-family:'Cormorant Infant',Garamond,serif;font-weight:300;font-size:clamp(44px,4vw,60px);line-height:1;color:#FFFFFF}
.aw-custom-price > span:first-child{flex-basis:100%;font-family:Abel,'Helvetica Neue',Arial,sans-serif;font-size:14px;letter-spacing:.2em;text-transform:uppercase;color:#BDBDBD}
.aw-custom-media{position:relative;min-width:0;padding-bottom:clamp(18px,2.6vw,36px)}
.aw-custom-desk{width:86%}
.aw-custom-phone{position:absolute;right:0;bottom:0;width:clamp(80px,19%,200px)}
@media (prefers-reduced-motion: reduce){.aw-shots img,.aw-sw{transition:none}}
'''

MAIN = '\n'.join([HERO, LOOKS_SEC, INCLUDED_SEC, PRICING_SEC, HOW_SEC, CUSTOM_SEC, FAQ_SEC, CLOSING])
txt = re.sub(r'<[^>]+>', ' ', MAIN)
assert '—' not in txt and ' -- ' not in txt and 'bespoke' not in txt.lower()

seo = open(os.path.join(ROOT, 'SEO.dc.html')).read()
comp = seo[seo.index('class Component extends DCLogic {'):seo.rindex('</script>')].replace('const FAQ_COUNT = 4;', f'const FAQ_COUNT = {len(FAQS)};')
FONTS = 'https://fonts.googleapis.com/css2?family=Abel&amp;family=Cormorant+Infant:ital,wght@0,300;0,400;0,500;1,300;1,400&amp;display=swap'
h = 7600
hp = os.path.join(os.path.dirname(__file__), 'actor_height.txt')
if os.path.exists(hp): h = int(open(hp).read())
C.write_page(ROOT, 'Actor-Websites.dc.html',
             title='Actor Websites in Vancouver | Sullivan Park Design',
             desc='Websites for actors in three polished looks, with your own edit screen for headshots, credits and bio, and no monthly hosting fee. $650 plus tax, with your first year of care included.',
             fonts_href=FONTS, main=MAIN, extra_css=CSS, preview_h=h, component=comp)
# the shell already loads the site fonts, so drop the duplicate link write_page adds
_p = os.path.join(ROOT, 'Actor-Websites.dc.html'); _s = open(_p).read()
_ln = f'<link rel="stylesheet" href="{FONTS}">\n'
if _s.count(_ln) > 1: open(_p, 'w').write(_s.replace(_ln, '', 1))
