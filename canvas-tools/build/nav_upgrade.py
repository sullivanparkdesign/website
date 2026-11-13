"""Site-wide navigation upgrade for the Sullivan Park Design canvas.

Rewrites the header (desktop dropdowns, phone menu, sticky bar), the footer
Services column, adds an "Other services" section to the three service pages,
and wires the header behaviour into each page's component.
Run once from anywhere; it is idempotent (re-running replaces its own output).
"""
import re, sys, os

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
PAGES = ['Main', 'About', 'Services', 'Website-Design', 'Brand-Marketing-Design', 'SEO',
         'Journal', 'Article', 'Testimonials', 'Contact', 'Hamish-Ross', 'Smash', 'Rooster-Den', 'Party-With-Laura', 'Callum-Frost', 'Portfolio', 'Guide-Platforms', 'Guide-Branding', 'Guide-Search', 'Guide-Support', 'Privacy', 'Actor-Websites']

LOGO_INK = '/_blob/946ef92befcc2436e37a8b858f03f1a7'
LOGO_LIGHT = '/_blob/4a336d6b0727926ee15001a1ba42622f'
PORTFOLIO = 'Portfolio.dc.html'
SERIF = "'Cormorant Infant', Garamond, serif"
ARROW = '<svg width="22" height="10" viewBox="0 0 26 10" fill="none" aria-hidden="true"><path d="M0 5h24M20 1l4 4-4 4" stroke="currentColor" stroke-width="1.1"></path></svg>'
CARET = '<svg class="sp-caret" width="10" height="6" viewBox="0 0 10 6" fill="none" aria-hidden="true"><path d="M.6.8 5 5 9.4.8" stroke="currentColor" stroke-width="1.1"></path></svg>'

SERVICES = [
    dict(key='web', num='01', name='Website Design', href='Website-Design.dc.html',
         short='New websites, redesigns and custom-coded builds',
         line='A new website or a better version of the one you have',
         thumb='/_blob/6c04b495000b663692a52bc44c8e472b',
         photo='/_blob/c2e5a8babbfa54d0f171e839673ee60f', pos='50% 50%', pw=1440, ph=960),
    dict(key='brand', num='02', name='Brand &amp; Marketing Design', href='Brand-Marketing-Design.dc.html',
         short='A consistent look across your website and marketing',
         line='A consistent identity across your website and marketing',
         thumb='/_blob/566fd5dcf72a6e8e27cbe554523c7a1b',
         photo='/_blob/1164e7d2af63c3bb162607bac351f168', pos='50% 50%', pw=1440, ph=960),
    dict(key='seo', num='03', name='SEO', href='SEO.dc.html',
         short='Make your website easier to find and understand',
         line='Make your website easier to find and understand',
         thumb='/_blob/85654ee79e5184e234a9b405db248d06',
         photo='/_blob/d0af229df2e363b1a9a642b6c1426b3d', pos='50% 50%', pw=1440, ph=960),
]
ONGOING_HREF = 'Services.dc.html#ongoing-title'
ACTOR_HREF = 'Actor-Websites.dc.html'
SHOW_ACTOR = True  # Actor Websites in the Services menu, phone menu and footer (approved 2026-11-12)

# Which top item is active, and which exact link is the current page.
STATE = {
    'Main': (None, None),
    'About': ('about', 'about'),
    'Services': ('services', 'services-all'),
    'Website-Design': ('services', 'web'),
    'Brand-Marketing-Design': ('services', 'brand'),
    'SEO': ('services', 'seo'),
    'Journal': ('about', 'resources'),
    'Article': ('about', None),
    'Guide-Platforms': ('about', None),
    'Guide-Branding': ('about', None),
    'Guide-Search': ('about', None),
    'Guide-Support': ('about', None),
    'Testimonials': ('about', 'testimonials'),
    'Contact': (None, 'contact'),
    'Hamish-Ross': ('portfolio', None),
    'Smash': ('portfolio', None),
    'Rooster-Den': ('portfolio', None),
    'Party-With-Laura': ('portfolio', None),
    'Callum-Frost': ('portfolio', None),
    'Portfolio': ('portfolio', 'portfolio'),
    'Privacy': (None, None),
    'Actor-Websites': ('services', 'actor'),
}

ABOUT_ITEMS = [
    ('about', 'About.dc.html', 'About Natasha', 'Who I am and how I work', '/_blob/16024f4c845dba8adfabba46c19c436e'),
    ('testimonials', 'Testimonials.dc.html', 'Testimonials', 'What clients say about working with me', '/_blob/05f12a1707f1469290c05e56e4fe7d13'),
    ('resources', 'Journal.dc.html', 'Resources', 'Guides to planning, branding and search', '/_blob/99260137b68de049a7efbe19bcbf4176'),
]


def cur(page, key):
    return ' aria-current="page"' if STATE[page][1] == key else ''


def header(page):
    dark = page in ('Main', 'Hamish-Ross', 'Smash', 'Callum-Frost')
    ink = '#FFFFFF' if dark else '#121414'
    top, _ = STATE[page]
    navstyle = f'color: {ink}; text-decoration: none; font-size: 15px; letter-spacing: 0.14em; text-transform: uppercase'

    def toplink(key, href, label, dd=False):
        cls = 'sp-navlink' + (' is-active' if top == key and STATE[page][1] != key and not (key == 'services' and STATE[page][1] == 'services-all') else '')
        ac = ''
        if (key == 'about' and STATE[page][1] == 'about') or (key == 'services' and STATE[page][1] == 'services-all'):
            ac = ' aria-current="page"'
        return f'<a class="{cls}" href="{href}"{ac} style="{navstyle}">{label}{CARET if dd else ""}</a>'

    sheet_open = '<div class="sp-dd-sheet" style="position: relative; background: #FAFAF8; box-shadow: 0 34px 80px rgba(18, 20, 20, 0.2), 0 2px 10px rgba(18, 20, 20, 0.06)">\n<span aria-hidden="true" style="position: absolute; inset: 10px; border: 1px solid rgba(78, 99, 104, 0.22); pointer-events: none"></span>'

    about_cards = '\n'.join(
        f'<li><a class="sp-dd-card" href="{h}"{cur(page, k)} style="display: flex; flex-direction: column; gap: 8px; height: 100%; text-decoration: none; color: #121414">'
        f'<span class="sp-dd-thumb" style="display: block; overflow: hidden; background: #E9ECEB"><img src="{t}" alt="" width="600" height="400" loading="lazy" style="display: block; width: 100%; height: auto; aspect-ratio: 3 / 2; object-fit: cover"></span>'
        f'<span class="sp-dd-name" style="margin-top: 10px; font-family: {SERIF}; font-size: 24px; line-height: 1.15">{n}</span>'
        f'<span style="font-size: 15px; line-height: 1.5; color: #4E5558">{d}</span></a></li>'
        for (k, h, n, d, t) in ABOUT_ITEMS)
    about_panel = f'''<div class="sp-dd-panel sp-dd-mega-panel" style="position: absolute; top: 100%; right: clamp(20px, 5vw, 72px); width: min(840px, calc(100% - 2 * clamp(20px, 5vw, 72px))); z-index: 30">
{sheet_open}
<div style="position: relative; padding: 32px 34px 28px">
<ul style="list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 26px">
{about_cards}
</ul>
<div style="margin-top: 26px; padding-top: 20px; border-top: 1px solid rgba(18, 20, 20, 0.12); display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px 32px">
<a class="sp-dd-row" href="{PORTFOLIO}" style="display: inline-flex; flex-wrap: wrap; align-items: baseline; gap: 4px 14px; text-decoration: none; color: #121414"><span class="sp-dd-name" style="font-family: {SERIF}; font-size: 22px; line-height: 1.2">Portfolio</span><span style="font-size: 15px; line-height: 1.5; color: #4E5558">Recent websites I’ve designed</span></a>
<a class="sp-dd-all" href="Contact.dc.html" style="display: inline-flex; align-items: center; gap: 12px; font-size: 14px; letter-spacing: 0.16em; text-transform: uppercase; color: #4E6368; text-decoration: none">Get in Touch{ARROW}</a>
</div>
</div>
</div>
</div>'''

    cards = '\n'.join(
        f'<li><a class="sp-dd-card" href="{s["href"]}"{cur(page, s["key"])} style="display: flex; flex-direction: column; gap: 8px; height: 100%; text-decoration: none; color: #121414">'
        f'<span class="sp-dd-thumb" style="display: block; overflow: hidden; background: #E9ECEB"><img src="{s["thumb"]}" alt="" width="600" height="400" loading="lazy" style="display: block; width: 100%; height: auto; aspect-ratio: 3 / 2; object-fit: cover"></span>'
        f'<span style="display: flex; align-items: baseline; gap: 12px; margin-top: 10px"><span style="font-size: 13px; letter-spacing: 0.18em; color: #4E6368">{s["num"]}</span><span class="sp-dd-name" style="font-family: {SERIF}; font-size: 24px; line-height: 1.15">{s["name"]}</span></span>'
        f'<span style="font-size: 15px; line-height: 1.5; color: #4E5558">{s["short"]}</span></a></li>'
        for s in SERVICES)
    all_cur = cur(page, 'services-all')
    ACTOR_ROW = f'''<a class="sp-dd-row" href="{ACTOR_HREF}"{cur(page, 'actor')} style="display: inline-flex; flex-wrap: wrap; align-items: baseline; gap: 4px 14px; text-decoration: none; color: #121414"><span class="sp-dd-name" style="font-family: 'Cormorant Infant', Garamond, serif; font-size: 22px; line-height: 1.2">Actor Websites</span><span style="font-size: 15px; line-height: 1.5; color: #4E5558">Ready-made looks for actors</span></a>'''
    services_panel = f'''<div class="sp-dd-panel sp-dd-mega-panel" style="position: absolute; top: 100%; right: clamp(20px, 5vw, 72px); width: min(840px, calc(100% - 2 * clamp(20px, 5vw, 72px))); z-index: 30">
{sheet_open}
<div style="position: relative; padding: 32px 34px 28px">
<ul style="list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 26px">
{cards}
</ul>
<div style="margin-top: 26px; padding-top: 20px; border-top: 1px solid rgba(18, 20, 20, 0.12); display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px 32px">
<a class="sp-dd-row" href="{ONGOING_HREF}" style="display: inline-flex; flex-wrap: wrap; align-items: baseline; gap: 4px 14px; text-decoration: none; color: #121414"><span class="sp-dd-name" style="font-family: {SERIF}; font-size: 22px; line-height: 1.2">Ongoing Support</span><span style="font-size: 15px; line-height: 1.5; color: #4E5558">Keep your website and marketing moving</span></a>
{ACTOR_ROW if SHOW_ACTOR else ''}
<a class="sp-dd-all" href="Services.dc.html"{all_cur} style="display: inline-flex; align-items: center; gap: 12px; font-size: 14px; letter-spacing: 0.16em; text-transform: uppercase; color: #4E6368; text-decoration: none">All Services{ARROW}</a>
</div>
</div>
</div>
</div>'''

    if dark:
        logo = (f'<img class="sp-logo sp-logo-light" src="{LOGO_LIGHT}" alt="" width="227" height="192" style="height: 58px; width: auto">\n'
                f'<img class="sp-logo sp-logo-ink" src="{LOGO_INK}" alt="" width="227" height="192" style="height: 58px; width: auto">')
        cta = f'<a class="sp-btn sp-btn-ghost sp-header-cta" href="Contact.dc.html"{cur(page, "contact")} style="display: inline-flex; align-items: center; min-height: 50px; padding: 0 26px; border: 1px solid rgba(255, 255, 255, 0.75); color: #FFFFFF; text-decoration: none; font-size: 17px; letter-spacing: 0.03em">Contact</a>'
        btn_border = 'rgba(255, 255, 255, 0.75)'
    else:
        logo = f'<img class="sp-logo" src="{LOGO_INK}" alt="" width="227" height="192" style="height: 58px; width: auto">'
        cta = f'<a class="sp-btn sp-btn-ink sp-header-cta" href="Contact.dc.html"{cur(page, "contact")} style="display: inline-flex; align-items: center; min-height: 50px; padding: 0 26px; border: 1px solid #121414; color: #121414; text-decoration: none; font-size: 17px; letter-spacing: 0.03em">Contact</a>'
        btn_border = '#121414'

    # Phone menu
    big = f"font-family: {SERIF}; font-size: 28px; color: #121414; text-decoration: none"
    sub = "display: flex; align-items: center; gap: 14px; min-height: 44px; font-size: 16px; letter-spacing: 0.12em; text-transform: uppercase; color: #4E6368; text-decoration: none"
    dash = '<span aria-hidden="true" style="display: block; width: 18px; height: 1px; background: currentColor"></span>'

    def msub(key, href, label):
        return f'<li><a class="sp-msub" href="{href}"{cur(page, key)} onClick="{{{{closeMenu}}}}" style="{sub}">{dash}{label}</a></li>'

    about_cur = ' aria-current="page"' if STATE[page][1] == 'about' else ''
    svc_cur = ' aria-current="page"' if STATE[page][1] == 'services-all' else ''
    mobile = f'''<sc-if value="{{{{menuOpen}}}}" hint-placeholder-val="{{{{false}}}}">
<nav class="sp-mnav" aria-label="Mobile" style="position: absolute; left: clamp(20px, 5vw, 72px); right: clamp(20px, 5vw, 72px); top: 100%; background: #FAFAF8; padding: 12px 28px 28px; display: flex; flex-direction: column; box-shadow: 0 30px 70px rgba(18, 20, 20, 0.22)">
<div style="padding-bottom: 12px; border-bottom: 1px solid rgba(18, 20, 20, 0.12)">
<a href="About.dc.html"{about_cur} onClick="{{{{closeMenu}}}}" style="display: block; padding: 18px 0 6px; {big}">About</a>
<ul style="list-style: none; margin: 0; padding: 0">
{msub('testimonials', 'Testimonials.dc.html', 'Testimonials')}
{msub('resources', 'Journal.dc.html', 'Resources')}
</ul>
</div>
<div style="padding-bottom: 12px; border-bottom: 1px solid rgba(18, 20, 20, 0.12)">
<a href="Services.dc.html"{svc_cur} onClick="{{{{closeMenu}}}}" style="display: block; padding: 18px 0 6px; {big}">Services</a>
<ul style="list-style: none; margin: 0; padding: 0">
{msub('web', 'Website-Design.dc.html', 'Website Design')}
{msub('brand', 'Brand-Marketing-Design.dc.html', 'Brand &amp; Marketing Design')}
{msub('seo', 'SEO.dc.html', 'SEO')}
{msub('ongoing', ONGOING_HREF, 'Ongoing Support')}
{msub('actor', ACTOR_HREF, 'Actor Websites') if SHOW_ACTOR else ''}
</ul>
</div>
<a href="{PORTFOLIO}"{cur(page, 'portfolio')} onClick="{{{{closeMenu}}}}" style="display: block; padding: 18px 0; border-bottom: 1px solid rgba(18, 20, 20, 0.12); {big}">Portfolio</a>
<a class="sp-btn sp-btn-blue" href="Contact.dc.html"{cur(page, "contact")} onClick="{{{{closeMenu}}}}" style="margin-top: 28px; display: inline-flex; align-items: center; justify-content: center; min-height: 56px; padding: 0 28px; background: #4E6368; border: 1px solid #4E6368; color: #FFFFFF; text-decoration: none; font-size: 17px; letter-spacing: 0.03em">Contact</a>
</nav>
</sc-if>'''

    return f'''<header class="sp-header{' sp-on-dark' if dark else ''}" ref="{{{{headerRef}}}}" data-scrolled="{{{{headerScrolled}}}}" style="position: fixed; top: 0; left: 0; right: 0; z-index: 20">
<div class="sp-headbar" style="width: 100%; max-width: 1680px; margin: 0 auto; padding: 24px clamp(20px, 5vw, 72px); display: flex; align-items: center; justify-content: space-between; gap: 32px">
<a class="sp-brand" href="Main.dc.html" aria-label="Sullivan Park Design, home" style="display: flex; align-items: center; gap: 16px; text-decoration: none; color: {ink}">
{logo}
<span class="sp-wordmark" style="font-family: {SERIF}; font-weight: 400; font-size: 23px; line-height: 1.1; color: {ink}">Sullivan Park Design</span>
</a>
<nav class="sp-nav" aria-label="Primary" data-hush="{{{{navHush}}}}" style="display: flex; align-items: center; gap: 40px; margin-left: auto; margin-right: 16px">
<div class="sp-dd sp-dd-about">
{toplink('about', 'About.dc.html', 'About', True)}
{about_panel}
</div>
<div class="sp-dd sp-dd-mega">
{toplink('services', 'Services.dc.html', 'Services', True)}
{services_panel}
</div>
<a class="sp-navlink{' is-active' if top == 'portfolio' and STATE[page][1] != 'portfolio' else ''}" href="{PORTFOLIO}"{cur(page, 'portfolio')} style="{navstyle}">Portfolio</a>
</nav>
<div style="display: flex; align-items: center; gap: 12px">
{cta}
<button class="sp-menu-btn" type="button" aria-label="Menu" aria-expanded="{{{{menuExpanded}}}}" onClick="{{{{toggleMenu}}}}" style="display: none; width: 50px; height: 50px; align-items: center; justify-content: center; background: transparent; border: 1px solid {btn_border}; color: {ink}; cursor: pointer; padding: 0"><svg width="22" height="12" viewBox="0 0 22 12" fill="none" aria-hidden="true"><path d="M0 1h22M0 11h22" stroke="currentColor" stroke-width="1.2"></path></svg></button>
</div>
</div>
{mobile}
</header>'''


def footer_services(page):
    fl = 'color: #121414; text-decoration: none; font-size: 18px; line-height: 1.5'
    links = [('services-all', 'Services.dc.html', 'All Services')] + [(s['key'], s['href'], s['name']) for s in SERVICES] + [('ongoing', ONGOING_HREF, 'Ongoing Support')] + ([('actor', ACTOR_HREF, 'Actor Websites')] if SHOW_ACTOR else [])
    items = '\n'.join(f'<a class="sp-flink" href="{h}"{cur(page, k)} style="{fl}">{n}</a>' for k, h, n in links)
    return f'''<nav aria-label="Services" style="flex: 0 1 220px; display: flex; flex-direction: column; gap: 12px">
<p style="margin: 0 0 6px; font-size: 14px; letter-spacing: 0.18em; text-transform: uppercase; color: #4E6368">Services</p>
{items}
</nav>'''


def other_services(page):
    me = {'Website-Design': 'web', 'Brand-Marketing-Design': 'brand', 'SEO': 'seo'}[page]
    label = '<p style="margin: 0; display: flex; align-items: center; gap: 16px; font-size: 15px; letter-spacing: 0.2em; text-transform: uppercase; color: #DCE4E5"><span aria-hidden="true" style="display: block; width: 40px; height: 1px; background: #DCE4E5"></span>Explore More</p>'
    cards = []
    for s in SERVICES:
        if s['key'] == me:
            continue
        cards.append(f'''<li style="display: flex"><a class="sp-more-card" href="{s['href']}" style="flex: 1; display: flex; flex-direction: column; background: #FAFAF8; color: #121414; text-decoration: none; padding: 14px 14px 32px">
<span style="display: block; overflow: hidden; background: #E9ECEB"><img src="{s['photo']}" alt="" width="{s['pw']}" height="{s['ph']}" loading="lazy" style="display: block; width: 100%; height: auto; aspect-ratio: 3 / 2; object-fit: cover; object-position: {s['pos']}"></span>
<span style="flex: 1; display: flex; flex-direction: column; gap: 12px; padding: 28px clamp(10px, 1.4vw, 20px) 0">
<span style="font-size: 14px; letter-spacing: 0.2em; color: #4E6368">{s['num']}</span>
<span style="font-family: {SERIF}; font-weight: 400; font-size: clamp(30px, 2.5vw, 38px); line-height: 1.1; color: #121414">{s['name']}</span>
<span style="font-size: 18px; line-height: 1.6; color: #1F2426">{s['line']}</span>
<span class="sp-more-go" style="margin-top: auto; padding-top: 16px; display: inline-flex; align-items: center; gap: 12px; font-size: 14px; letter-spacing: 0.16em; text-transform: uppercase; color: #4E6368">Explore {s['name'] if s['key'] != 'brand' else 'Brand Design'}{ARROW}</span>
</span>
</a></li>''')
    bullet = '<span aria-hidden="true" style="flex: none; display: block; width: 18px; height: 1px; margin-top: 14px; background: #DCE4E5"></span>'
    ongoing_items = ['SEO and website content', 'Blogs and newsletters', 'Social content and marketing design', 'Website updates']
    lis = '\n'.join(f'<li style="display: flex; gap: 14px; font-size: 18px; line-height: 1.6; color: #FFFFFF">{bullet}{t}</li>' for t in ongoing_items)
    cards.append(f'''<li style="display: flex"><div class="sp-more-ongoing" style="flex: 1; display: flex; flex-direction: column; gap: 20px; padding: clamp(30px, 3vw, 44px); border: 1px solid rgba(255, 255, 255, 0.4); color: #FFFFFF">
<p style="margin: 0; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: #DCE4E5">Ongoing Support</p>
<h3 style="margin: 0; font-family: {SERIF}; font-weight: 400; font-size: clamp(30px, 2.5vw, 38px); line-height: 1.1; color: #FFFFFF; text-wrap: balance">Keep your website and marketing moving</h3>
<p style="margin: 0; font-size: 18px; line-height: 1.65; color: #E3E9EA">Once your website is in place, I can help keep your content current and your marketing consistent.</p>
<ul style="list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 6px">
{lis}
</ul>
<a class="sp-link sp-more-link" href="{ONGOING_HREF}" style="margin-top: auto; align-self: flex-start; display: inline-flex; align-items: center; gap: 12px; min-height: 44px; font-size: 14px; letter-spacing: 0.16em; text-transform: uppercase; color: #FFFFFF; text-decoration: none; border-bottom: 1px solid rgba(255, 255, 255, 0.5)">About Ongoing Support{ARROW}</a>
</div></li>''')
    cards_html = '\n'.join(cards)
    return f'''<!-- OTHER SERVICES (cross-links) -->
<section aria-labelledby="more-title" class="sp-on-dark" style="position: relative; overflow: hidden; background: #4E6368; color: #FFFFFF">
<div class="sp-reveal" style="position: relative; z-index: 1; width: 100%; max-width: 1680px; margin: 0 auto; padding: clamp(88px, 10vw, 136px) clamp(20px, 5vw, 72px); display: flex; flex-direction: column; gap: clamp(44px, 5vw, 64px)">
<div style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 24px 48px">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 22px">
{label}
<h2 id="more-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(42px, 4.6vw, 72px); line-height: 1.04; color: #FFFFFF; text-wrap: balance">Other ways <em style="font-style: italic; color: #DCE4E5">I can help</em></h2>
</div>
<a class="sp-link sp-more-link" href="Services.dc.html" style="display: inline-flex; align-items: center; gap: 12px; min-height: 44px; font-size: 15px; letter-spacing: 0.16em; text-transform: uppercase; color: #FFFFFF; text-decoration: none; border-bottom: 1px solid rgba(255, 255, 255, 0.5)">View All Services{ARROW}</a>
</div>
<ul class="sp-more-grid" style="list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: clamp(20px, 2.4vw, 32px)">
{cards_html}
</ul>
</div>
</section>
<!-- /OTHER SERVICES -->

'''


CSS_START = '/* NAV v2 (generated) */'
CSS_END = '/* /NAV v2 */'
CSS = CSS_START + '''
html{scroll-padding-top:104px}
.sp-header{transition:background-color .45s ease,box-shadow .45s ease}
.sp-headbar{position:relative;--hpad:24px;padding-top:var(--hpad) !important;padding-bottom:var(--hpad) !important;transition:padding .45s cubic-bezier(.2,.7,.2,1)}
.sp-logo{transition:height .45s cubic-bezier(.2,.7,.2,1)}
.sp-header[data-scrolled="true"]{background:rgba(250,250,248,.94);-webkit-backdrop-filter:saturate(1.3) blur(14px);backdrop-filter:saturate(1.3) blur(14px);box-shadow:0 1px 0 rgba(18,20,20,.08),0 18px 40px -30px rgba(18,20,20,.5)}
.sp-header[data-scrolled="true"] .sp-headbar{--hpad:12px}
.sp-header[data-scrolled="true"] .sp-logo{height:46px !important}
.sp-logo-ink{display:none !important}
.sp-header.sp-on-dark[data-scrolled="true"] .sp-logo-light{display:none !important}
.sp-header.sp-on-dark[data-scrolled="true"] .sp-logo-ink{display:block !important}
.sp-header.sp-on-dark[data-scrolled="true"] .sp-brand,.sp-header.sp-on-dark[data-scrolled="true"] .sp-wordmark,.sp-header.sp-on-dark[data-scrolled="true"] .sp-nav .sp-navlink{color:#121414 !important}
.sp-header.sp-on-dark[data-scrolled="true"] .sp-header-cta,.sp-header.sp-on-dark[data-scrolled="true"] .sp-menu-btn{color:#121414 !important;border-color:#121414 !important}
.sp-header.sp-on-dark[data-scrolled="true"] .sp-header-cta:hover{background:#121414 !important;color:#FFFFFF !important}
.sp-header.sp-on-dark[data-scrolled="true"] :focus-visible{outline-color:#121414}
.sp-nav{align-self:stretch}
.sp-dd{display:flex;align-items:center;align-self:stretch;padding-block:var(--hpad);margin-block:calc(var(--hpad) * -1)}
.sp-dd > .sp-navlink{display:inline-flex !important;align-items:center;gap:9px}
.sp-caret{transition:transform .35s cubic-bezier(.2,.7,.2,1)}
.sp-navlink.is-active::after,.sp-dd:hover > .sp-navlink::after,.sp-dd:focus-within > .sp-navlink::after{transform:scaleX(1)}
.sp-dd-panel{opacity:0;visibility:hidden;transform:translateY(-8px);pointer-events:none;transition:opacity .25s ease .12s,transform .3s ease .12s,visibility 0s linear .42s}
.sp-dd:hover > .sp-dd-panel,.sp-dd:focus-within > .sp-dd-panel{opacity:1;visibility:visible;transform:none;pointer-events:auto;transition:opacity .35s ease,transform .45s cubic-bezier(.2,.7,.2,1),visibility 0s}
.sp-dd:hover > .sp-navlink .sp-caret,.sp-dd:focus-within > .sp-navlink .sp-caret{transform:rotate(180deg)}
.sp-nav[data-hush="true"] .sp-dd-panel{opacity:0 !important;visibility:hidden !important;pointer-events:none !important}
.sp-dd-card img{transition:transform .9s cubic-bezier(.2,.7,.2,1)}
.sp-dd-card:hover img,.sp-dd-card:focus-visible img{transform:scale(1.05)}
.sp-dd-name{transition:color .3s}
.sp-dd-card:hover .sp-dd-name,.sp-dd-line:hover .sp-dd-name,.sp-dd-row:hover .sp-dd-name,.sp-dd-card[aria-current="page"] .sp-dd-name,.sp-dd-line[aria-current="page"] .sp-dd-name{color:#4E6368}
.sp-dd-card[aria-current="page"] .sp-dd-thumb{outline:1px solid #4E6368;outline-offset:4px}
.sp-dd-all svg,.sp-more-go svg,.sp-more-link svg{transition:transform .35s cubic-bezier(.2,.7,.2,1)}
.sp-dd-all:hover svg,.sp-more-card:hover .sp-more-go svg,.sp-more-link:hover svg{transform:translateX(5px)}
@media (max-width: 1240px){.sp-nav{gap:30px !important}}
.sp-foot-grid{display:grid !important;grid-template-columns:minmax(0,1.5fr) repeat(3,minmax(0,1fr));gap:48px clamp(32px,4vw,64px) !important}
.sp-foot-grid > :first-child p{max-width:520px}
@media (max-width: 1000px){.sp-foot-grid{grid-template-columns:repeat(3,minmax(0,1fr))}.sp-foot-grid > :first-child{grid-column:1 / -1}}
@media (max-width: 680px){.sp-foot-grid{grid-template-columns:1fr 1fr}.sp-foot-grid > :last-child{grid-column:1 / -1}}
@media (max-width: 420px){.sp-foot-grid{grid-template-columns:1fr}}
.sp-mnav{max-height:calc(100vh - 110px);max-height:calc(100dvh - 110px);overflow-y:auto;overscroll-behavior:contain}
.sp-mnav a[aria-current="page"]{color:#4E6368 !important}
.sp-mnav .sp-msub[aria-current="page"]{color:#121414 !important}
.sp-mnav .sp-msub[aria-current="page"] span{width:28px !important}
.sp-msub{transition:color .3s}
.sp-msub:hover{color:#121414 !important}
.sp-more-card{transition:transform .6s cubic-bezier(.2,.7,.2,1),box-shadow .6s cubic-bezier(.2,.7,.2,1)}
.sp-more-card:hover{transform:translateY(-4px);box-shadow:0 34px 60px -34px rgba(0,0,0,.55)}
.sp-more-card img{transition:transform 1.1s cubic-bezier(.2,.7,.2,1)}
.sp-more-card:hover img{transform:scale(1.04)}
@media (max-width: 980px){.sp-more-grid{grid-template-columns:1fr 1fr !important}.sp-more-grid > li:last-child{grid-column:1 / -1}}
@media (max-width: 640px){.sp-more-grid{grid-template-columns:1fr !important}}
@media (prefers-reduced-motion: no-preference){.sp-fab{transition:transform .3s cubic-bezier(.2,.7,.2,1),background-color .3s,color .3s,opacity .4s ease,visibility 0s}}
.sp-fab[data-show="false"]{opacity:0;visibility:hidden;pointer-events:none;transform:translateY(10px)}
@media (prefers-reduced-motion: reduce){.sp-dd-panel{transform:none !important}.sp-dd-card img,.sp-more-card,.sp-more-card img{transition:none !important;transform:none !important}}
''' + CSS_END

JS_METHOD = '''  getHeaderRef() {
    // Sticky header: turns solid once the page scrolls, shows the back-to-top
    // button further down, and lets Escape close the phone menu or a dropdown.
    if (!this._headerRef) {
      this._headerRef = (el) => {
        if (this._headerOff) { try { this._headerOff(); } catch (e) {} this._headerOff = null; }
        if (!el) return;
        const doc = el.ownerDocument || document;
        const win = doc.defaultView || window;
        const sync = () => {
          const y = win.pageYOffset || (doc.documentElement && doc.documentElement.scrollTop) || 0;
          const st = this.state || {};
          const scrolled = y > 24;
          const deep = y > 640;
          if (!!st.scrolled !== scrolled || !!st.deep !== deep) this.setState({ scrolled: scrolled, deep: deep });
        };
        const unhush = () => { if ((this.state || {}).navHush) this.setState({ navHush: false }); };
        const onKey = (e) => {
          if (e.key !== 'Escape' && e.key !== 'Esc') return;
          const st = this.state || {};
          const active = doc.activeElement;
          const inHeader = !!(active && el.contains(active));
          if (st.menuOpen) {
            this.setState({ menuOpen: false });
            const btn = el.querySelector('.sp-menu-btn');
            if (btn && inHeader) { try { btn.focus(); } catch (err) {} }
            return;
          }
          if (inHeader && active.closest && active.closest('.sp-dd-panel')) {
            const dd = active.closest('.sp-dd');
            const topLink = dd && dd.querySelector('.sp-navlink');
            if (topLink) { try { topLink.focus(); } catch (err) {} }
          }
          this.setState({ navHush: true });
        };
        const nav = el.querySelector('.sp-nav');
        win.addEventListener('scroll', sync, { passive: true });
        doc.addEventListener('keydown', onKey);
        if (nav) { nav.addEventListener('pointerleave', unhush); nav.addEventListener('focusout', unhush); }
        const raf = win.requestAnimationFrame ? win.requestAnimationFrame(sync) : 0;
        this._headerOff = () => {
          win.removeEventListener('scroll', sync);
          doc.removeEventListener('keydown', onKey);
          if (nav) { nav.removeEventListener('pointerleave', unhush); nav.removeEventListener('focusout', unhush); }
          if (raf && win.cancelAnimationFrame) win.cancelAnimationFrame(raf);
        };
      };
    }
    return this._headerRef;
  }
'''
JS_VALS = ''',
      headerRef: this.getHeaderRef(),
      headerScrolled: (this.state && this.state.scrolled) ? 'true' : 'false',
      fabShow: (this.state && this.state.deep && !this.state.menuOpen) ? 'true' : 'false',
      navHush: (this.state && this.state.navHush) ? 'true' : 'false\''''


def main():
    for page in PAGES:
        path = os.path.join(ROOT, page + '.dc.html')
        if not os.path.exists(path):
            continue
        s = open(path).read()
        orig = s

        # 1. header (replace whole element, with its leading comment untouched)
        a = s.index('<header'); b = s.index('</header>') + len('</header>')
        s = s[:a] + header(page) + s[b:]

        # 2. footer Services column
        m = re.search(r'<nav aria-label="Services".*?</nav>', s, re.S)
        s = s[:m.start()] + footer_services(page) + s[m.end():]

        # 2b. footer columns on a grid so they line up at every width
        s = s.replace('<div style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 48px 64px">\n<div style="flex: 1 1 340px;', '<div class="sp-foot-grid" style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 48px 64px">\n<div style="flex: 1 1 340px;', 1)

        # 3. back-to-top button only appears further down the page
        if 'data-show="{{fabShow}}"' not in s:
            s = s.replace('<a class="sp-fab" href="#top"', '<a class="sp-fab" href="#top" data-show="{{fabShow}}"', 1)

        # 4. other services section
        if page in ('Website-Design', 'Brand-Marketing-Design', 'SEO'):
            s = re.sub(r'<!-- OTHER SERVICES \(cross-links\) -->.*?<!-- /OTHER SERVICES -->\n\n', '', s, flags=re.S)
            k = s.index('<!-- CLOSING (simple enquiry band) -->')
            s = s[:k] + other_services(page) + s[k:]

        # 5. enquiry button wording
        s = re.sub(r'(href="Contact\.dc\.html"[^>]*>)Let’s Talk', r'\1Enquire About Your Project', s)

        # 6. CSS
        s = re.sub(re.escape(CSS_START) + r'.*?' + re.escape(CSS_END) + r'\n?', '', s, flags=re.S)
        st_end = s.index('</style>')
        s = s[:st_end] + CSS + '\n' + s[st_end:]

        # 7. JS
        if 'getHeaderRef()' not in s:
            s = s.replace('class Component extends DCLogic {\n', 'class Component extends DCLogic {\n' + JS_METHOD, 1)
            needle = "closeMenu: () => this.setState({ menuOpen: false })"
            assert s.count(needle) == 1, (page, s.count(needle))
            s = s.replace(needle, needle + JS_VALS, 1)

        open(path, 'w').write(s)
        print(page, 'updated', len(orig), '->', len(s))


if __name__ == '__main__':
    main()
