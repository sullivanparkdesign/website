"""Portfolio index (Portfolio.dc.html), grouped by platform."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import case_common as C

ROOT = sys.argv[1]
SERIF, WRAP, PAD, ARROW, EXT = C.SERIF, C.WRAP, C.SECTION_PAD, C.ARROW, C.EXT

PROJECTS = {
    'hr': dict(name='Hamish Ross Real Estate', industry='Real Estate', line='Custom-coded website · Ongoing SEO &amp; marketing',
               cap='Luxury design paired with useful property and market resources, supported by ongoing SEO, blogs, social media and newsletters.',
               page='Hamish-Ross.dc.html', site='https://www.hamishross.com/', host='hamishross.com',
               desk='/_blob/2f057afafa2a706726d866726a890535', phone='/_blob/ad7621e45ae0d89b602e15c79ee2eede',
               panel='#12141A', dark=True, line_c='rgba(201, 168, 118, 0.55)', glow='rgba(34, 56, 74, 0.95)', accent='#A0865C'),
    'smash': dict(name='SMASH Performing Arts Studio', industry='Performing Arts', line='Custom-coded website · Ongoing SEO &amp; marketing',
                  cap='A full website design with an AI assistant to help families find answers, supported by ongoing SEO, blogs, social media and newsletters.',
                  page='Smash.dc.html', site='https://smashtheatreschool.ca/', host='smashtheatreschool.ca',
                  desk='/_blob/91618c9a67bd147c380fd6ac8ad40c91', phone='/_blob/f912b4f6d45ae4b94acd03c3ac4a84b8',
                  panel='#22306B', dark=True, line_c='rgba(207, 174, 107, 0.55)', glow='rgba(151, 217, 248, 0.2)', accent='#8C7440'),
    'rooster': dict(name='The Rooster Den Co', industry='Retail', line='Shopify redesign · SEO · Google Business Profile setup',
                    cap='A cowgirl-chic redesign with clearer shopping journeys, page-by-page SEO and Google Business Profile setup.',
                    page='Rooster-Den.dc.html', site='https://theroosterdenco.com/', host='theroosterdenco.com',
                    desk='/_blob/a392d0d3f88ef802da8c30746b2b7015', phone='/_blob/d10c98749309b9a833f8b3a2e20d6430',
                    panel='#FAF2E6', dark=False, line_c='rgba(193, 100, 82, 0.5)', glow='rgba(193, 100, 82, 0.14)', accent='#A84F3E'),
    'callum': dict(name='Callum Frost', industry='Actor &amp; Voice-Over Artist', line='Custom-coded website · Copywriting · Ongoing updates',
                   cap='A classic black and white website for a Vancouver actor and voice-over artist, rebuilt in custom code with film-inspired details that let his headshots take the lead.',
                   page='Callum-Frost.dc.html', site='https://sullivanparkdesign.github.io/callumfrost/', host='callumfrost.com', visit_name='the new Callum Frost website',
                   desk='/_blob/d3978c904a489af5909028a3ecb4bb5a', phone='/_blob/d9565222a636eaef6c6bdb26170739fa',
                   panel='#1E1E1E', dark=True, line_c='rgba(255, 255, 255, 0.35)', glow='rgba(255, 255, 255, 0.08)', accent='#4E5558'),
    'laura': dict(name='pARTy With Laura', industry='Art Classes &amp; Parties', line='Squarespace website · Built from scratch',
                  cap='A bright, playful website for art classes, camps and paint parties in Cloverdale, with easy paths to booking.',
                  page='Party-With-Laura.dc.html', site='https://www.partywithlaura.com/', host='partywithlaura.com',
                  desk='/_blob/9c4d67173f82a60a0650a4246e6eb526', phone='/_blob/2ddafa117d3819e434b2ecc872337509',
                  panel='#9FD0D4', dark=False, line_c='rgba(6, 102, 128, 0.45)', glow='rgba(255, 245, 245, 0.7)', accent='#066680'),
    # website-only cards (no case study page yet)
    'moscone': dict(name='Moscone Developments', industry='Custom Home Builder', line='Squarespace redesign · SEO · Ongoing care',
                    cap='A full redesign from WordPress to Squarespace for a Vancouver custom home builder, with new design, copy and photos, project pages including the Michael Bublé Residence, full SEO and Google Business Profile setup.',
                    page=None, site='https://www.mosconedevelopments.com/', host='mosconedevelopments.com',
                    desk='/_blob/98681ccb2acb68ad8f36d5046b76e475', phone='/_blob/543d1fc4f6d81da6ae6c67d41265a051',
                    panel='#1E2F44', dark=True, line_c='rgba(201, 214, 228, 0.42)', glow='rgba(120, 160, 200, 0.2)', accent='#3D5A7A'),
    'strength': dict(name='Building Strength Counselling', industry='Counselling &amp; Education', line='Squarespace redesign · Brand refresh · SEO',
                     cap='A move from a self-built Wix site to Squarespace for a North Vancouver counsellor, with refreshed copy, a stronger brand, a large resource centre of articles and full behind-the-scenes SEO.',
                     page=None, site='https://www.buildingstrength.ca/', host='buildingstrength.ca',
                     desk='/_blob/1c6ea9a795fa7c750e1503505e41b447', phone='/_blob/9338778f86bee92bc0c5d11bf41cc6e8',
                     panel='#DDE2D9', dark=False, line_c='rgba(96, 111, 106, 0.45)', glow='rgba(255, 255, 255, 0.6)', accent='#5F706A'),
}

SECTIONS = [
    ('custom', 'Custom-coded', 'websites', 'Projects that need full design freedom or features beyond a template.', ['hr', 'smash', 'callum']),
    ('squarespace', 'Squarespace', 'websites', 'Service businesses that want a polished site they can update themselves.', ['laura', 'moscone', 'strength']),
    ('shopify', 'Shopify', 'stores', 'Online stores that need products, payments and shipping managed in one place.', ['rooster']),
]


def stage(k, large=True):
    d = PROJECTS[k]
    pad = 'clamp(28px, 4.4vw, 72px) clamp(24px, 4vw, 64px) clamp(40px, 5vw, 80px)' if large else 'clamp(24px, 3.4vw, 52px) clamp(20px, 3vw, 44px) clamp(36px, 4vw, 60px)'
    img = C.desk(d['desk'], f"The {d['name']} website on a desktop screen", d['host'], 1800, 1125, dark=d['dark'])
    ph = C.phone(d['phone'], f"The {d['name']} website on a phone")
    inner = f'''<span aria-hidden="true" style="position: absolute; inset: 0; background: radial-gradient(ellipse 70% 60% at 85% 10%, {d['glow']}, rgba(0, 0, 0, 0) 70%); pointer-events: none"></span>
<span aria-hidden="true" class="pf-line" style="position: absolute; inset: clamp(10px, 1.2vw, 16px); border: 1px solid {d['line_c']}; pointer-events: none"></span>
<span class="pf-devices" style="position: relative; display: block; padding-bottom: clamp(18px, 2.6vw, 36px)">
<span class="pf-desk" style="display: block; width: 86%">{img}</span>
<span class="pf-phone" style="position: absolute; right: 0; bottom: 0; width: clamp(80px, 19%, 220px)">{ph}</span>
</span>'''
    style = f'position: relative; display: block; overflow: hidden; background: {d["panel"]}; padding: {pad}; text-decoration: none'
    if d['page']:
        return f'<a class="pf-stage" href="{d["page"]}" tabindex="-1" aria-hidden="true" style="{style}">{inner}</a>'
    return f'<div class="pf-stage" style="{style}">{inner}</div>'


def visit(d):
    return (f'<a class="sp-ext" href="{d["site"]}" aria-label="Visit Website, {d.get("visit_name", d["host"])}" style="display: inline-flex; align-items: center; gap: 8px; min-height: 44px; font-size: 16px; letter-spacing: 0.03em; color: #4E6368; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 6px">Visit Website{EXT}</a>')


def view(d):
    return (f'<a class="sp-btn sp-btn-line" href="{d["page"]}" aria-label="View Project, {d["name"]}" style="display: inline-flex; align-items: center; gap: 12px; min-height: 54px; padding: 0 24px; border: 1px solid #4E6368; color: #4E6368; text-decoration: none; font-size: 17px; letter-spacing: 0.03em">View Project{ARROW}</a>')


def text_block(k, num, size='clamp(36px, 3.4vw, 54px)'):
    d = PROJECTS[k]
    buttons = (view(d) + visit(d)) if d['page'] else visit(d)
    return f'''<span style="font-family: {SERIF}; font-style: italic; font-size: 24px; color: {d['accent']}">{num}</span>
<p style="margin: 0; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: #4E6368">{d['industry']}</p>
<h3 style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: {size}; line-height: 1.06; color: #121414; text-wrap: balance">{d['name']}</h3>
<p style="margin: 0; font-size: 17px; letter-spacing: 0.03em; color: #4E6368">{d['line']}</p>
<p style="margin: 0; font-size: 19px; line-height: 1.7; color: #1F2426">{d['cap']}</p>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 12px 28px; margin-top: 8px">{buttons}</div>'''


def feature(k, num, reverse):
    return f'''<article class="pf-feature sp-reveal{' pf-rev' if reverse else ''}" aria-label="{PROJECTS[k]['name']}">
<div class="pf-feature-stage">{stage(k)}</div>
<div class="pf-feature-text" style="display: flex; flex-direction: column; align-items: flex-start; gap: 16px; min-width: 0">
{text_block(k, num)}
</div>
</article>'''


def card(k, num):
    return f'''<article class="pf-card sp-reveal" aria-label="{PROJECTS[k]['name']}" style="display: flex; flex-direction: column; gap: 28px; min-width: 0">
{stage(k, large=False)}
<div style="display: flex; flex-direction: column; align-items: flex-start; gap: 14px; min-width: 0">
{text_block(k, num, size='clamp(32px, 2.8vw, 46px)')}
</div>
</article>'''


BG = {'custom': '#FFFFFF', 'squarespace': '#ECEEED', 'shopify': '#FFFFFF'}
jump_items = []
sections_html = []
for si, (sid, plat, word, best, keys) in enumerate(SECTIONS):
    n = f'{si + 1:02d}'
    jump_items.append(f'''<li><a class="pf-jump-link" href="#{sid}" style="display: flex; flex-direction: column; gap: 10px; height: 100%; padding: 22px 24px 24px; border: 1px solid rgba(78, 99, 104, 0.35); background: rgba(255, 255, 255, 0.6); color: #121414; text-decoration: none">
<span style="font-family: {SERIF}; font-style: italic; font-size: 20px; color: #4E6368">{n}</span>
<span class="pf-jump-name" style="display: flex; align-items: center; justify-content: space-between; gap: 16px; font-family: {SERIF}; font-size: clamp(28px, 2.4vw, 36px); line-height: 1.1"><span>{plat}</span><svg width="14" height="18" viewBox="0 0 14 18" fill="none" aria-hidden="true"><path d="M7 0v16M1 10l6 6 6-6" stroke="currentColor" stroke-width="1.1"></path></svg></span>
<span style="font-size: 16px; line-height: 1.55; color: #4E5558">{best}</span>
</a></li>''')
    if len(keys) == 2 and sid == 'squarespace':
        body = f'<div class="pf-cards">\n' + '\n'.join(card(k, f'{i + 1:02d}') for i, k in enumerate(keys)) + '\n</div>'
    elif len(keys) == 3 and sid == 'squarespace':
        # the case study leads, then the two website-only projects side by side
        body = feature(keys[0], '01', False) + f'\n<div class="pf-cards">\n' + '\n'.join(card(k, f'{i + 2:02d}') for i, k in enumerate(keys[1:])) + '\n</div>'
    else:
        body = '\n'.join(feature(k, f'{i + 1:02d}', i % 2 == 1) for i, k in enumerate(keys))
    sections_html.append(f'''<!-- {plat.upper()} -->
<section id="{sid}" aria-labelledby="{sid}-title" style="background: {BG[sid]}">
<div style="{WRAP}; {PAD}; display: flex; flex-direction: column; gap: clamp(56px, 7vw, 112px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 24px clamp(48px, 7vw, 120px); padding-bottom: clamp(28px, 3vw, 40px); border-bottom: 1px solid rgba(78, 99, 104, 0.3)">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 24px">
{C.label(f'{n} · Platform')}
<h2 id="{sid}-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(44px, 5vw, 80px); line-height: 1.02; color: #121414">{plat} <em style="font-style: italic; color: #4E6368">{word}</em></h2>
</div>
<div style="flex: 1 1 420px; min-width: 0; display: flex; flex-direction: column; gap: 8px"><p style="margin: 0; font-size: 14px; letter-spacing: 0.16em; text-transform: uppercase; color: #4E6368">Best for</p><p style="margin: 0; font-size: 19px; line-height: 1.7; color: #1F2426">{best}</p></div>
</div>
{body}
</div>
</section>
''')

HERO = f'''<!-- HERO -->
<section aria-labelledby="page-title" style="position: relative; overflow: hidden; background: #FAFAF8">
<img class="sp-sway" src="/_blob/fddc24a18e2595d21f63da9f1d7bf0d5" alt="" width="1800" height="1200" style="position: absolute; top: -20px; right: -20px; width: min(1320px, 110vw); height: auto; max-width: none; opacity: 0.16; mix-blend-mode: multiply; pointer-events: none; z-index: 0">
<div style="position: relative; z-index: 1; {WRAP}; padding-top: clamp(170px, 15vw, 230px); padding-bottom: clamp(72px, 8vw, 112px); display: flex; flex-direction: column; gap: clamp(48px, 5vw, 72px)">
<div style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 32px clamp(48px, 7vw, 120px)">
<div style="flex: 1.2 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 28px">
{C.label('Portfolio')}
<h1 id="page-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(60px, 8vw, 132px); line-height: 0.98; letter-spacing: -0.02em; color: #121414">Selected <em style="font-style: italic; color: #4E6368">work</em></h1>
</div>
<p style="flex: 1 1 420px; min-width: 0; margin: 0; padding-bottom: 12px; font-size: 21px; line-height: 1.65; color: #1F2426">Custom-coded websites, Squarespace sites and Shopify stores, each designed around the business it represents.</p>
</div>
<nav aria-label="Jump to a platform">
<ul class="pf-jump" style="list-style: none; margin: 0; padding: 0">
{chr(10).join(jump_items)}
</ul>
</nav>
<div class="pf-actors sp-reveal">
<p class="pf-actors-t"><em>Are you an actor?</em> I also offer ready-made actor websites, from $650 + tax.</p>
<a class="sp-btn sp-btn-ghost" href="Actor-Websites.dc.html" style="flex: none; display: inline-flex; align-items: center; justify-content: center; gap: 14px; min-height: 52px; padding: 0 26px; background: transparent; border: 1px solid #4E6368; color: #121414; text-decoration: none; font-size: 17px; letter-spacing: 0.03em">Actor Websites{C.ARROW}</a>
</div>
</div>
</section>
'''

CLOSING = C.closing('Let’s find the right fit', 'for your business')
_old_p = 'Tell me about your business and what you’d like your website to do.'
assert _old_p in CLOSING
CLOSING = CLOSING.replace(_old_p, 'This is a small selection of my work. Looking for an example in your industry? Ask me and I’ll share more.')
MAIN = HERO + '\n' + '\n'.join(sections_html) + '\n' + CLOSING

CSS = '''/* PORTFOLIO */
.pf-jump{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(12px,1.6vw,24px)}
@media (max-width: 860px){.pf-jump{grid-template-columns:1fr}}
.pf-jump-link{transition:background-color .35s,border-color .35s}
.pf-jump-link svg{transition:transform .35s cubic-bezier(.2,.7,.2,1)}
.pf-jump-link:hover{background:#FFFFFF !important;border-color:#4E6368 !important}
.pf-jump-link:hover svg{transform:translateY(4px)}
.pf-feature{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:40px clamp(32px,4vw,72px);align-items:center}
.pf-feature-stage{grid-column:1 / span 7}
.pf-feature-text{grid-column:8 / span 5}
.pf-rev .pf-feature-stage{grid-column:6 / span 7;order:2}
.pf-rev .pf-feature-text{grid-column:1 / span 5;order:1}
@media (max-width: 960px){.pf-feature{grid-template-columns:minmax(0,1fr)}.pf-feature-stage,.pf-rev .pf-feature-stage,.pf-feature-text,.pf-rev .pf-feature-text{grid-column:1 / -1;order:0}}
.pf-cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:clamp(48px,5vw,80px) clamp(24px,3vw,56px);align-items:start}
.pf-cards > :nth-child(2){margin-top:clamp(0px,8vw,140px)}
@media (max-width: 860px){.pf-cards{grid-template-columns:1fr}.pf-cards > :nth-child(2){margin-top:0}}
.pf-stage .pf-desk,.pf-stage .pf-phone{transition:transform .9s cubic-bezier(.2,.7,.2,1)}
.pf-feature:hover .pf-desk,.pf-card:hover .pf-desk{transform:translateY(-6px)}
.pf-feature:hover .pf-phone,.pf-card:hover .pf-phone{transform:translateY(-14px)}
@media (prefers-reduced-motion: reduce){.pf-stage .pf-desk,.pf-stage .pf-phone{transition:none !important;transform:none !important}}
/* /PORTFOLIO */.pf-actors{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:18px 40px;padding:22px 0 0;border-top:1px solid rgba(78,99,104,.3)}
.pf-actors-t{margin:0;flex:1 1 420px;min-width:0;font-size:19px;line-height:1.6;color:#1F2426}
.pf-actors-t em{font-family:'Cormorant Infant',Garamond,serif;font-size:1.3em;font-style:italic;color:#4E6368;margin-right:6px}
'''

C.write_page(ROOT, 'Portfolio.dc.html',
             title='Portfolio | Website Design by Sullivan Park Design',
             desc='Custom-coded websites, Squarespace sites and Shopify stores designed by Sullivan Park Design, including Hamish Ross Real Estate, SMASH Performing Arts Studio and The Rooster Den Co.',
             fonts_href='https://fonts.googleapis.com/css2?family=Jost:wght@400&amp;display=swap',
             main=MAIN, extra_css=CSS, preview_h=7270)

# footer-current: mark the footer Portfolio link as the current page
_p = os.path.join(ROOT, 'Portfolio.dc.html'); _s = open(_p).read()
_s = _s.replace('<a class="sp-flink" href="Portfolio.dc.html" style=', '<a class="sp-flink" href="Portfolio.dc.html" aria-current="page" style=', 1)
open(_p, 'w').write(_s)
