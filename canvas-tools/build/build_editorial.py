"""Editorial guides: all five Resources guides as art-directed features.
Templates (head, nav, practice cards, closing, footer) come from build/guide_src/<file> (the pre-editorial pages).
Shared pieces: arched cover with seal, 'In short' band, sticky chapter rail that tracks reading (CSS scroll-driven,
progressive), margin notes, full-bleed quote and spread interludes, dark 'bottom line', author, up next.
Each guide has its own visuals and interactions (pure CSS, no JavaScript).
Run: python3 build/build_editorial.py canvas/project [file ...]"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = sys.argv[1]
ONLY = sys.argv[2:]
SERIF = "'Cormorant Infant', Garamond, serif"
TEAL, INK, BODY, MUTED = '#4E6368', '#121414', '#1F2426', '#4E5558'
ARROW = '<svg width="22" height="10" viewBox="0 0 26 10" fill="none" aria-hidden="true"><path d="M0 5h24M20 1l4 4-4 4" stroke="currentColor" stroke-width="1.1"></path></svg>'
PALM = '<img class="sp-sway" src="/_blob/fddc24a18e2595d21f63da9f1d7bf0d5" alt="" width="1800" height="1200" style="position: absolute; top: -20px; right: -20px; width: min(1320px, 110vw); height: auto; max-width: none; opacity: 0.16; mix-blend-mode: multiply; pointer-events: none; z-index: 0">'
PALM_DARK = PALM.replace('opacity: 0.16', 'opacity: 0.22').replace('top: -20px; right: -20px', 'top: -60px; right: -120px')
CHECK = '<svg width="16" height="12" viewBox="0 0 16 12" fill="none" aria-hidden="true"><path d="M1.5 6.2 5.8 10.5 14.5 1.5" stroke="currentColor" stroke-width="1.6"></path></svg>'
CROSS = '<svg width="12" height="12" viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M1.5 1.5l9 9M10.5 1.5l-9 9" stroke="currentColor" stroke-width="1.3"></path></svg>'
SEGMENT_RULES = []


def A(href, text):
    return f'<a href="{href}" style="color: {TEAL}; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 4px">{text}</a>'


def P(t):
    return f'<p class="ed-p">{t}</p>'


def label(text, color=TEAL):
    return f'<p style="margin: 0; display: flex; align-items: center; gap: 16px; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: {color}"><span aria-hidden="true" style="display: block; width: 40px; height: 1px; background: {color}"></span>{text}</p>'


def icon(name, size=32):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'


def img(bid, alt, w, h, extra=''):
    return f'<img src="/_blob/{bid}" alt="{alt}" width="{w}" height="{h}" loading="lazy"{extra}>'


ICONS = {
    'calendar': '<rect x="5" y="7" width="22" height="20" rx="1"></rect><path d="M5 13h22M11 4v6M21 4v6"></path>',
    'bag': '<path d="M7 11h18l-1.5 16h-15z"></path><path d="M12 11V9a4 4 0 0 1 8 0v2"></path>',
    'gift': '<rect x="5" y="12" width="22" height="6"></rect><path d="M7 18v9h18v-9M16 12v15M16 12c-2-5-8-6-8-2s6 2 8 2zM16 12c2-5 8-6 8-2s-6 2-8 2z"></path>',
    'mail': '<rect x="4" y="8" width="24" height="16" rx="1"></rect><path d="M4 9l12 9 12-9"></path>',
    'plane': '<path d="M28 5 4 15l9 3 3 9z"></path><path d="M13 18 28 5"></path>',
    'lock': '<rect x="7" y="14" width="18" height="13" rx="1"></rect><path d="M11 14v-3a5 5 0 0 1 10 0v3M16 19v4"></path>',
    'key': '<circle cx="10" cy="16" r="5"></circle><path d="M15 16h13M24 16v4M28 16v3"></path>',
    'monitor': '<rect x="4" y="6" width="24" height="16" rx="1"></rect><path d="M12 27h8M16 22v5"></path>',
    'chat': '<path d="M5 7h22v14H14l-6 5v-5H5z"></path>',
    'megaphone': '<path d="M5 13v6h4l10 6V7L9 13z"></path><path d="M23 12a5 5 0 0 1 0 8"></path>',
    'sign': '<rect x="6" y="6" width="20" height="12" rx="1"></rect><path d="M16 18v9M11 27h10"></path>',
    'card': '<rect x="4" y="8" width="24" height="16" rx="1"></rect><path d="M8 14h9M8 18h6"></path>',
    'box': '<path d="M5 10l11-5 11 5v12l-11 5-11-5z"></path><path d="M5 10l11 5 11-5M16 15v12"></path>',
    'bolt': '<path d="M18 4 8 18h7l-1 10 10-14h-7z"></path>',
    'phone': '<rect x="10" y="4" width="12" height="24" rx="2"></rect><path d="M15 24h2"></path>',
    'compass': '<circle cx="16" cy="16" r="11"></circle><path d="M20 12l-2.5 6.5L11 21l2.5-6.5z"></path>',
    'image': '<rect x="5" y="7" width="22" height="18" rx="1"></rect><circle cx="12" cy="13" r="2"></circle><path d="M5 22l7-6 5 4 4-3 6 5"></path>',
    'search': '<circle cx="14" cy="14" r="8"></circle><path d="M20 20l7 7"></path>',
    'chart': '<path d="M5 27h22M9 23v-6M15 23V11M21 23v-9"></path>',
    'clock': '<circle cx="16" cy="16" r="11"></circle><path d="M16 9v7l5 3"></path>',
}

L_LAURA, L_CALLUM, L_BRAND = 'Party-With-Laura.dc.html', 'Callum-Frost.dc.html', 'Brand-Marketing-Design.dc.html'


# ================================================================== shared visual pieces
def note(t):
    return t


def cards(items, cls='ed-qs', nums=('i', 'ii', 'iii', 'iv', 'v', 'vi')):
    lis = ''.join(f'<li><span class="ed-qs-n" aria-hidden="true">{n}</span><span class="ed-qs-t">{q}</span></li>' for n, q in zip(nums, items))
    return f'<ol class="{cls} sp-reveal">{lis}</ol>'


def tiles(items, extra=''):
    lis = ''.join(f'<li>{icon(k)}<span>{t}</span></li>' for k, t in items)
    return f'<ul class="ed-feats{extra} ed-wide sp-reveal">{lis}</ul>'


def files(names, aria):
    t = ''.join(f'<span class="ed-file{" ed-file-png" if f == "PNG" else ""}">{f}</span>' for f in names)
    return f'<div class="ed-files" aria-label="{aria}">{t}</div>'


def browser(bid, alt, w, h, cap=None, cls=''):
    capt = f'<figcaption class="ed-cap">{cap}</figcaption>' if cap else ''
    return f'<figure class="ed-browser-fig {cls} sp-reveal"><div class="ed-browser"><div class="ed-browser-bar" aria-hidden="true"><i></i><i></i><i></i></div>{img(bid, alt, w, h)}</div>{capt}</figure>'


def checklist(prefix, items, status_of, todo, done, cls='', inline=False, legend=None):
    lis = ''.join(f'<li class="ed-cl-item"><label><input class="ed-vh" type="checkbox" id="{prefix}{i}"><span class="ed-cl-box" aria-hidden="true">{CHECK}</span><span class="ed-cl-t">{t}</span><span class="ed-cl-c" aria-hidden="true">{i:02d}</span></label></li>' for i, t in enumerate(items, 1))
    for i in range(1, len(items) + 1):
        SEGMENT_RULES.append(f'.ed-cl:has(#{prefix}{i}:checked) .ed-cl-bar span:nth-child({i}){{background:#4E6368}}')
    segs = ''.join('<span></span>' for _ in items)
    leg = f'<p class="ed-legend">{legend}</p>' if legend else ''
    return (f'<div class="ed-cl{" ed-cl-inline" if inline else ""}{cls}">' if inline else '') + f'''{leg}<ul class="ed-cl-list">{lis}</ul>
<div class="ed-cl-status">
<p class="ed-cl-count"><span class="ed-cl-n" aria-hidden="true"></span><span class="ed-cl-of">{status_of}</span></p>
<div class="ed-cl-bar" aria-hidden="true" style="grid-template-columns: repeat({len(items)}, minmax(0, 1fr))">{segs}</div>
<p class="ed-cl-msg ed-cl-msg-todo">{todo}</p>
<p class="ed-cl-msg ed-cl-msg-done">{done}</p>
</div>''' + ('</div>' if inline else '')


# ================================================================== guide 01 visuals
def g1_goals():
    goals = ['More enquiries', 'Bookings', 'Online sales', 'Fewer emails asking the same questions']
    chips = ''.join(f'<label class="ed-goal"><input class="ed-vh" type="radio" name="ed-goal" value="{g}"><span class="ed-goal-t">{g}</span><span class="ed-goal-tag" aria-hidden="true"></span></label>' for g in goals)
    return f'<fieldset class="ed-goals sp-reveal"><legend>What’s your main goal?</legend><div class="ed-goal-row">{chips}</div></fieldset>'


def page_node(name, root=False):
    return f'<div class="ed-node{" ed-node-root" if root else ""}"><span class="ed-page" aria-hidden="true"><i></i><i></i><i></i><i></i></span><span class="ed-node-t">{name}</span></div>'


def g1_sitemap():
    core = ''.join(f'<li>{page_node(n)}</li>' for n in ['Services', 'About', 'Your work', 'Contact'])
    extra = ''.join(f'<li>{page_node(n)}</li>' for n in ['Programs', 'Shop', 'Portfolio', 'FAQs'])
    return f'''<figure class="ed-map ed-wide sp-reveal" aria-labelledby="ed-map-cap">
{page_node('Home', True)}
<span class="ed-map-stem" aria-hidden="true"></span>
<ul class="ed-map-row" aria-label="Core pages">{core}</ul>
<p class="ed-map-sep">Yours might also include</p>
<ul class="ed-map-row ed-map-extra" aria-label="Pages yours might also include">{extra}</ul>
<figcaption id="ed-map-cap" class="ed-cap">A simple page plan for a small business website.</figcaption>
</figure>'''


def g1_kit():
    sw = ''.join(f'<li><span class="ed-sw" style="background: {c}"></span>{c}</li>' for c in ['#4E6368', '#121414', '#DCE4E5', '#FAFAF8'])
    return f'''<figure class="ed-kitfig sp-reveal" aria-labelledby="ed-kit-cap">
<div class="ed-kit">
<div class="ed-kit-p"><p class="ed-kit-l">Logo files</p>{files(['SVG', 'EPS', 'PDF', 'PNG'], 'SVG, EPS, PDF and a PNG with a transparent background')}</div>
<div class="ed-kit-p"><p class="ed-kit-l">Colours</p><ul class="ed-sws">{sw}</ul></div>
<div class="ed-kit-p"><p class="ed-kit-l">Fonts</p><div class="ed-type"><span class="ed-type-a" style="font-family: {SERIF}; font-weight: 300">Aa</span><span class="ed-type-n">Cormorant Infant</span></div><div class="ed-type"><span class="ed-type-a ed-type-b" style="font-family: 'Abel', 'Arial Narrow', sans-serif">Aa</span><span class="ed-type-n">Abel</span></div></div>
</div>
<figcaption id="ed-kit-cap" class="ed-cap">Shown with my own brand colours and fonts.</figcaption>
</figure>'''


def g1_pair():
    return '''<div class="ed-pair sp-reveal">
<div><p class="ed-pair-h">Your own photos</p><p class="ed-pair-t">Your work · Your space · Yourself</p></div>
<div><p class="ed-pair-h">Stock photos</p><p class="ed-pair-t">Mood · Atmosphere</p></div>
</div>'''


def g1_logins():
    items = ['Your domain, and where you bought it', 'Your current website platform', 'Google Business Profile, Search Console and Analytics',
             'Your email, if it’s connected to your domain', 'Any booking, payment or newsletter tools you use', 'The social media accounts you’d like linked']
    lis = ''.join(f'<li>{icon("key", 26)}<span>{x}</span></li>' for x in items)
    return f'<ul class="ed-keys sp-reveal">{lis}</ul>'


def collage(a, b):
    return f'''<div class="ed-collage sp-reveal">
<div class="ed-collage-a">{img(*a)}</div>
<div class="ed-collage-b">{img(*b)}</div>
</div>'''


def g1_dates():
    lis = ''.join(f'<li class="ed-date"><span class="ed-date-t">{t}</span></li>' for t in ['Registration opening', 'A new season', 'A product launch'])
    return f'<ul class="ed-dates ed-wide sp-reveal">{lis}</ul>'


# ================================================================== guide 02 visuals
CMP = [
    ('sq', 'Squarespace', 'Updating my own site', ['Service businesses that want a polished site they can update themselves.', 'Easy. You can change text, swap photos and add posts yourself.',
                                                   'Works well for a modest range of products, digital goods or gift cards.', 'Built-in tools, plus a range of extensions.', 'Included and managed for you.']),
    ('sh', 'Shopify', 'Selling products online', ['Online stores that need products, payments and shipping managed in one place.', 'Easy for products, collections and store content.',
                                                 'Built for it, from inventory to checkout.', 'A large app store for almost anything a store needs.', 'Included and managed for you.']),
    ('cu', 'Custom-coded', 'Full design freedom or custom features', ['Projects that need full design freedom or features beyond a template.', 'Depends on how the site is built, so we plan it together first.',
                                                                      'Possible, usually by connecting a dedicated store or payment service.', 'Anything you need, such as a members’ portal or an AI assistant.', 'Arranged separately, as part of the project.']),
]
CMP_ROWS = ['Best for', 'Everyday updates', 'Selling online', 'Extra features', 'Hosting and security']


def g2_finder():
    radios = ''.join(f'<label class="ed-pf-opt"><input class="ed-vh" type="radio" name="ed-pf" id="ed-pf-{k}"><span>{q}</span></label>' for k, _, q, _ in CMP)
    cols = ''.join(f'''<div class="ed-pf-col ed-pf-{k}"><p class="ed-pf-fit" aria-hidden="true">Best fit</p><h3 class="ed-pf-h">{name}</h3>
<dl class="ed-pf-dl">{''.join(f'<div><dt>{r}</dt><dd>{v}</dd></div>' for r, v in zip(CMP_ROWS, vals))}</dl></div>''' for k, name, _, vals in CMP)
    return f'''<div class="ed-pf ed-wide sp-reveal">
<fieldset class="ed-pf-q"><legend>What matters most to you?</legend><div class="ed-pf-opts">{radios}</div></fieldset>
<div class="ed-pf-cols" role="group" aria-label="Squarespace, Shopify and custom-coded websites compared">{cols}</div>
</div>'''


def g2_path():
    return f'''<div class="ed-path sp-reveal" aria-hidden="true">
<div class="ed-path-a"><span>Where you are now</span></div>
<span class="ed-path-arrow"><svg width="64" height="14" viewBox="0 0 64 14" fill="none"><path d="M0 7h60M54 1l6 6-6 6" stroke="currentColor" stroke-width="1.1"></path></svg></span>
<div class="ed-path-b"><span>Where your business is heading</span></div>
</div>'''


# ================================================================== guide 03 visuals
PALETTES = [
    ('smash', 'SMASH', ['#1A2558', '#22306B', '#CFAE6B', '#D3E3F3', '#97D9F8']),
    ('hr', 'Hamish Ross', ['#12141A', '#22384A', '#C9A876', '#F6F3EE', '#A0865C']),
    ('laura', 'pARTy With Laura', ['#066680', '#9FD0D4', '#F9CFCF', '#FEF4F4', '#DCEEEE']),
    ('rooster', 'The Rooster Den Co', ['#171717', '#6D7C7C', '#C16452', '#FAF2E6', '#5C5C5C']),
    ('callum', 'Callum Frost', ['#121212', '#5A5A5A', '#848484', '#F8F8F8', '#CCCACA']),
]


def g3_palettes():
    def dots(cols):
        return ''.join('<i style="background: %s"></i>' % c for c in cols[:3])
    opts = ''.join(f'<label class="ed-palx-opt"><input class="ed-vh" type="radio" name="ed-pal" id="ed-pal-{k}"><span class="ed-palx-dots" aria-hidden="true">{dots(cols)}</span>{name}</label>' for k, name, cols in PALETTES)
    roles = ['Main', 'Second', 'Accent', 'Background', 'Highlight']
    sw = ''.join(f'<li><span class="ed-palx-sw" style="background: var(--p{i})"></span><span class="ed-palx-role">{r}</span><span class="ed-palx-hex" aria-hidden="true"></span></li>' for i, r in enumerate(roles, 1))
    return f'''<figure class="ed-palx ed-wide sp-reveal" aria-labelledby="ed-palx-cap">
<fieldset class="ed-palx-q"><legend>Try a palette from a recent project</legend><div class="ed-palx-opts">{opts}</div></fieldset>
<div class="ed-palx-stage">
<div class="ed-mock" aria-hidden="true">
<div class="ed-mock-nav"><i></i><span><i></i><i></i><i></i></span></div>
<div class="ed-mock-hero"><b></b><b></b><s></s><s></s><span class="ed-mock-btn"></span></div>
<div class="ed-mock-cards"><span></span><span></span><span></span></div>
</div>
<ul class="ed-palx-sws">{sw}</ul>
</div>
<figcaption id="ed-palx-cap" class="ed-cap">The same simple layout, dressed in each project’s colours.</figcaption>
</figure>'''


def g3_typepair():
    return f'''<div class="ed-typepair sp-reveal">
<div class="ed-tp"><span class="ed-tp-a" style="font-family: {SERIF}; font-weight: 300">Aa</span><p class="ed-tp-h">Elegant serif</p><p class="ed-tp-t">Refined and established</p></div>
<div class="ed-tp"><span class="ed-tp-a ed-tp-sans" style="font-family: 'Abel', 'Arial Narrow', sans-serif">Aa</span><p class="ed-tp-h">Clean sans serif</p><p class="ed-tp-t">Modern and approachable</p></div>
<div class="ed-tp ed-tp-pair"><p class="ed-kit-l">One of each</p><span class="ed-tp-head" style="font-family: {SERIF}">Cormorant Infant</span><span class="ed-tp-body">Abel, for everyday text</span><p class="ed-cap">The pairing used on this website.</p></div>
</div>'''


def g3_scales():
    rows = [('bright', 'Bright', 'Moody'), ('polish', 'Polished', 'Relaxed'), ('scale', 'Close-up details', 'Wide open spaces')]
    out = ''
    for k, a, b in rows:
        dots = ''.join(f'<label class="ed-scale-dot"><input class="ed-vh" type="radio" name="ed-sc-{k}" aria-label="{a} to {b}: {i} of 5"><span aria-hidden="true"></span></label>' for i in range(1, 6))
        out += f'<div class="ed-scale-row"><span class="ed-scale-l">{a}</span><span class="ed-scale-dots">{dots}</span><span class="ed-scale-r">{b}</span></div>'
    return f'<fieldset class="ed-scales sp-reveal"><legend>Where does your style sit?</legend>{out}</fieldset>'


def g3_words():
    words = ['Calm', 'Playful', 'Luxurious', 'Warm', 'Bold']
    chips = ''.join(f'<label class="ed-word"><input class="ed-vh" type="checkbox"><span>{w}</span></label>' for w in words)
    return f'''<fieldset class="ed-words sp-reveal"><legend>Which words feel like your business?</legend>
<div class="ed-word-row">{chips}</div>
<p class="ed-words-count"><span class="ed-words-n" aria-hidden="true"></span> chosen</p>
</fieldset>'''


def g3_places():
    items = [('monitor', 'Website'), ('chat', 'Social media'), ('mail', 'Newsletters'), ('megaphone', 'Ads'), ('sign', 'Signage'), ('card', 'Business cards'), ('box', 'Packaging')]
    lis = ''.join(f'<li>{icon(k, 26)}<span>{t}</span></li>' for k, t in items)
    return f'<ul class="ed-places sp-reveal">{lis}</ul>'


def g3_smash_pair():
    return f'''<figure class="ed-duo ed-wide sp-reveal" aria-labelledby="ed-duo-cap">
<div class="ed-duo-a"><div class="ed-browser"><div class="ed-browser-bar" aria-hidden="true"><i></i><i></i><i></i></div>{img('91618c9a67bd147c380fd6ac8ad40c91', 'The SMASH Performing Arts Studio homepage in navy, with a gold accent and serif headline', 1800, 1125)}</div></div>
<div class="ed-duo-b">{img('f4ed28c975a4f9ef06db7deac1eb4b70', 'A SMASH newsletter announcing the new website, in the same navy and serif headlines', 900, 1125)}</div>
<figcaption id="ed-duo-cap" class="ed-cap">The SMASH website and one of its monthly newsletters.</figcaption>
</figure>'''


# ================================================================== guide 04 visuals
def g4_xlate():
    return f'''<div class="ed-xlate sp-reveal">
<div><p class="ed-kit-l">An agent might think</p><p class="ed-xlate-w">Listings</p></div>
<span class="ed-xlate-arrow" aria-hidden="true"><svg width="48" height="14" viewBox="0 0 48 14" fill="none"><path d="M0 7h44M38 1l6 6-6 6" stroke="currentColor" stroke-width="1.1"></path></svg></span>
<div><p class="ed-kit-l">Buyers search for</p><p class="ed-xlate-w">Homes for sale in White Rock</p></div>
</div>'''


def g4_menu():
    items = [('Listings', False), ('Buying', False), ('Selling', False), ('Market report', True), ('Journal', True)]
    lis = ''.join(('<li class="on">%s</li>' if on else '<li>%s</li>') % t for t, on in items)
    return f'<figure class="ed-menu sp-reveal" aria-labelledby="ed-menu-cap"><ul>{lis}</ul><figcaption id="ed-menu-cap" class="ed-cap">Main menu items on Hamish Ross Real Estate, with the market report and journal alongside the essentials.</figcaption></figure>'


def g4_serp():
    return '''<div class="ed-serp ed-wide sp-reveal">
<fieldset class="ed-serp-toggle"><legend class="ed-vh">Compare a specific and a vague page title</legend>
<label><input class="ed-vh" type="radio" name="ed-serp" id="ed-serp-s"><span>Specific title</span></label>
<label><input class="ed-vh" type="radio" name="ed-serp" id="ed-serp-v"><span>Vague title</span></label>
</fieldset>
<div class="ed-serp-card">
<div class="ed-serp-row"><span class="ed-serp-lab">Page address</span><span class="ed-serp-url">partywithlaura.com › weekly-classes</span></div>
<div class="ed-serp-row"><span class="ed-serp-lab">Page title</span><span class="ed-serp-title"><span class="ed-serp-spec">Weekly Kids Art Classes | Small Group Lessons in Cloverdale</span><span class="ed-serp-vague">Services</span></span></div>
<div class="ed-serp-row"><span class="ed-serp-lab">Description</span><span class="ed-serp-desc">Personalized art instruction for kids and teens (ages 6–18). Small class sizes (2–5 students) ensure individual guidance in painting, sketching, and mixed media.</span></div>
</div>
</div>'''


def g4_schema():
    rows = [('Business name', 'Sullivan Park Design'), ('Location', 'Vancouver, British Columbia'), ('Services', 'Website design, brand and marketing design, SEO')]
    dl = ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in rows)
    return f'<figure class="ed-schema sp-reveal" aria-labelledby="ed-schema-cap"><div class="ed-schema-card"><p class="ed-schema-l">Behind the scenes</p><dl>{dl}</dl></div><figcaption id="ed-schema-cap" class="ed-cap">The kind of details schema labels, shown with my own business.</figcaption></figure>'


def g4_areas():
    areas = ['White Rock', 'South Surrey', 'Ocean Park', 'Morgan Creek', 'Hazelmere']
    spans = ''.join('<span>%s</span>' % a for a in areas)
    return f'<figure class="ed-areas sp-reveal" aria-labelledby="ed-areas-cap"><div class="ed-areas-bar">{spans}</div><figcaption id="ed-areas-cap" class="ed-cap">The service areas along the top of the Hamish Ross Real Estate website.</figcaption></figure>'


def g4_nap():
    rows = ['Business name', 'Address', 'Phone number']
    lis = ''.join(f'<li>{CHECK}{r}</li>' for r in rows)
    col = lambda t: f'<div class="ed-nap-c"><p class="ed-nap-h">{t}</p><ul>{lis}</ul></div>'
    return f'<div class="ed-nap ed-wide sp-reveal" role="group" aria-label="The same details everywhere">{col("Your website")}{col("Google Business Profile")}{col("Everywhere else you’re listed")}</div>'


def g4_tools():
    t = [('search', 'Google Search Console', 'Which searches bring people to your site, and problems Google finds.'), ('chart', 'Google Analytics', 'What visitors do once they arrive.')]
    return '<div class="ed-tools sp-reveal">' + ''.join(f'<div class="ed-tool">{icon(k)}<p class="ed-tool-h">{h}</p><p class="ed-tool-t">{d}</p><span class="ed-tool-tag">Free</span></div>' for k, h, d in t) + '</div>'


def g4_growth():
    return '''<figure class="ed-growth sp-reveal" aria-labelledby="ed-growth-cap">
<svg class="ed-growth-svg" viewBox="0 0 600 160" preserveAspectRatio="none" aria-hidden="true"><path d="M0 150 C 90 140, 150 112, 230 104 S 420 70, 600 14" fill="none" stroke="#4E6368" stroke-width="1.4" vector-effect="non-scaling-stroke"></path><path d="M0 150 C 90 140, 150 112, 230 104 S 420 70, 600 14 L600 160 L0 160 Z" fill="rgba(78,99,104,0.08)"></path></svg>
<div class="ed-growth-labels"><div><p class="ed-kit-l">Early on</p><p class="ed-growth-t">Some improvements can show up fairly quickly</p></div><div><p class="ed-kit-l">Over months</p><p class="ed-growth-t">Broader progress comes from steady work</p></div></div>
<figcaption id="ed-growth-cap" class="ed-vh">SEO builds gradually over time.</figcaption>
</figure>'''


def g4_avoid():
    items = ['Stuffing keywords into every sentence', 'Near-identical pages for every town', 'Buying links']
    lis = ''.join(f'<li>{CROSS}<span>{t}</span></li>' for t in items)
    return f'<div class="ed-avoid sp-reveal"><p class="ed-legend">Shortcuts to avoid</p><ul>{lis}</ul></div>'


# ================================================================== guide 05 visuals
def g5_tokens():
    items = ['Prices', 'Programs', 'Team members', 'Photos', 'Opening hours']
    clock = icon('clock', 18)
    lis = ''.join(f'<li>{clock}<span>{t}</span></li>' for t in items)
    return f'<div class="ed-tokens sp-reveal"><p class="ed-legend">Details that go out of date quickly</p><ul>{lis}</ul></div>'


def g5_log():
    items = ['New photos', 'Updated text', 'New pages', 'Seasonal changes', 'Fixes as they come up']
    lis = ''.join('<li><span>%s</span></li>' % t for t in items)
    return f'<div class="ed-log sp-reveal"><p class="ed-legend">The everyday care</p><ol>{lis}</ol></div>'


def g5_related():
    return f'''<a class="ed-related sp-reveal" href="Guide-Search.dc.html">
<span class="ed-related-l">Related Guide · 04</span>
<span class="ed-related-h">How to help Google and AI search <em>find your business</em></span>
<span class="ed-related-go" aria-hidden="true">{ARROW}</span>
</a>'''


def g5_fan():
    return f'''<figure class="ed-fan ed-wide sp-reveal" aria-labelledby="ed-fan-cap">
<div class="ed-fan-a">{img('0a5c93774294911ca46174f0b6da6cc5', 'A SMASH newsletter page listing dates to remember and upcoming show weeks', 900, 1125)}</div>
<div class="ed-fan-b">{img('f4ed28c975a4f9ef06db7deac1eb4b70', 'A SMASH newsletter announcing the studio’s new website', 900, 1125)}</div>
<div class="ed-fan-c">{img('32ccb724087bf89ec2f8941ce96b551c', 'A SMASH newsletter page introducing the season’s four musicals', 900, 1125)}</div>
<figcaption id="ed-fan-cap" class="ed-cap">Pages from the monthly SMASH newsletters.</figcaption>
</figure>'''


def g5_formats():
    def mock(cls, name):
        return f'<div class="ed-fmt {cls}"><div class="ed-fmt-art" aria-hidden="true"><span class="ed-fmt-band"></span><b>Aa</b><s></s><s></s><span class="ed-fmt-btn"></span></div><p class="ed-kit-l">{name}</p></div>'
    return f'<figure class="ed-formats ed-wide sp-reveal" aria-labelledby="ed-fmt-cap"><div class="ed-formats-row">{mock("ed-fmt-sq", "Social graphic")}{mock("ed-fmt-wide", "Ad")}{mock("ed-fmt-tall", "Printed piece")}</div><figcaption id="ed-fmt-cap" class="ed-cap">Different formats, one consistent look.</figcaption></figure>'


def g5_opts():
    o = [('One area', 'like monthly newsletters'), ('Several together', 'such as SEO, blogs, social content and website updates')]
    return '<div class="ed-opts sp-reveal">' + ''.join(f'<div class="ed-opt"><span class="ed-qs-n" aria-hidden="true">{n}</span><p class="ed-opt-h">{h}</p><p class="ed-opt-t">{t}</p></div>' for n, (h, t) in zip(['i', 'ii'], o)) + '</div>'


def g5_routine():
    rows = [('Every month', 'Check your key pages and contact form every month.'), ('As soon as they change', 'Update photos, prices and dates as soon as they change.'),
            ('Now and then', 'Look at Search Console now and then for errors or new searches.'), ('Ongoing', 'Keep your Google Business Profile hours and photos current.'),
            ('Once a year', 'Review your main pages once a year to make sure they still reflect your business.')]
    return '<ol class="ed-routine sp-reveal">' + ''.join(f'<li><span class="ed-routine-f">{f}</span><span class="ed-routine-t">{t}</span></li>' for f, t in rows) + '</ol>'


# ================================================================== guide specs
def ch(id, short, title, body, note=None):
    return dict(id=id, short=short, title=title, body=body, note=note)


G01 = dict(
    file='Article.dc.html', num='01', seal='PLANNING', tag='Planning', read=5,
    title_main='What to prepare before', title_em='a website redesign',
    stand='The goals, content, photos and logins worth gathering first, so your project starts smoothly.',
    cover=('arch', '9095e97c95708cc67b261cafbb8c1d21', 'An open, light-filled pavilion with a long table, looking out over a calm sea', 1200, 800, '50% 70%'),
    wide=('c88afba51f29e1af4a1ad91e130aa1ec', 'An open, light-filled pavilion with a long table, looking out over a calm sea', 1800, 771),
    takeaways=['Start with what you want your website to do, not how you want it to look.', 'Note what’s working on your current site, so the redesign builds on it.',
               'Gather your words, brand files and best photos in one place.', 'Collect logins for your domain, website and Google tools early.',
               'Share a few websites you like, and say what you like about them.'],
    intro='A website redesign runs more smoothly when a few things are ready before the design work begins. You don’t need everything perfect, and you don’t need to do it alone. But the more of this you can gather, the more of our time goes into the parts that make your site stand out. Here’s what helps most, in the order I’d tackle it.',
    items=[
        ch('goals', 'Goals', 'Know what you want your website to do', [
            P('Before colours and layouts, think about the job your website needs to do. More enquiries? Bookings? Online sales? Fewer emails asking the same questions? Most businesses have one main goal and a few supporting ones, and knowing them shapes every decision that follows, from the pages you need to where each button goes.'),
            g1_goals(),
            P(f'It also helps to know who you most want to reach. A website for {A(L_LAURA, "parents booking art classes")} needs different things than one for {A(L_CALLUM, "agents discovering a new actor")}, even when both are simple and clean.')]),
        ch('current', 'Your current site', 'Take stock of your current site', [
            P('Make a quick list of what’s working and what isn’t.'),
            cards(['Which pages do people actually use?', 'What do customers ask you that the site should already answer?', 'What feels out of date, or no longer reflects how you work?']),
            P(f'Those everyday questions are useful. For {A(L_LAURA, "pARTy With Laura")}, common parent questions (what to wear, what to bring, whether there’s a snack break) became short, expandable answers on each program page.')],
            'If you have Google Analytics or Search Console, note your most visited pages and the searches that bring people in. Keeping those pages at the same address, or redirecting them properly, means a redesign builds on what you already have instead of starting from zero.'),
        ('quote', 'Start with what you want your website to <span class="ed-q-em">do</span>, not how you want it to <span class="ed-q-em">look</span>.'),
        ch('content', 'Pages and words', 'Plan your pages and words', [
            P('List the pages you think you need and the main thing each one should say. A home page, services, about, contact and a few examples of your work cover most small businesses, but your list might also include programs, a shop, a portfolio or FAQs.'),
            g1_sitemap(),
            P('Gather the words you already have, even rough notes. Copy you love can stay, and anything that isn’t working can be rewritten.')],
            'If writing isn’t your favourite thing, tell me. Turning notes into clear, warm copy is something I help with.'),
        ch('brand', 'Brand files', 'Gather your brand files', [
            P('Find your logo in the best quality you have. Ideally that’s a vector file (SVG, EPS or PDF) plus a PNG with a transparent background. Add your brand colours, fonts and any brand guidelines you’ve been given.'),
            g1_kit(),
            P(f'If you don’t have a palette or fonts yet, that’s okay. A redesign is a natural time to define them, and {A(L_BRAND, "brand and marketing design")} is part of what I offer.')],
            'I don’t design logos, but I can build your colours, typography and imagery around the one you have.'),
        ('spread', ('87b256f87275018e5bfde23768efc920', 'An open notebook of handwritten plans beside a laptop on a wooden desk', 1080, 720), '3 / 2', 'A Gentle Reminder', 'You don’t need everything perfect, and you don’t need to do it <em>alone</em>.'),
        ch('photos', 'Photos', 'Choose your photos', [
            P('Photos shape how a website feels more than almost anything else. Your own photos of your work, your space and yourself build a kind of trust that stock photos can’t. Gather the best ones you have, in the largest size available.'),
            g1_pair(),
            P(f'If you’re planning a photo shoot, plan it with the website in mind. Before {A(L_CALLUM, "Callum’s")} headshot session, I gave advice on the kinds of photos I wanted for his site, so the shoot and the design worked together.')],
            'Stock photos still have a place, especially for mood and atmosphere. Choose ones that feel like your brand rather than ones that could belong to anyone.'),
        ch('access', 'Logins', 'Collect your logins', [
            P('Waiting on logins is one of the easiest ways for a project to stall, so it’s worth gathering access early:'), g1_logins()],
            'You don’t need to send passwords by email. Most of these tools let you add a collaborator instead, which is safer and easy to undo later.'),
        ch('features', 'Features', 'List your must-have features', [
            P('Think about what your website needs to do behind the scenes. Booking, online sales, gift certificates, a contact form that sorts enquiries, a newsletter sign-up or a private area for clients or families are all possible, but each one affects how the site is built.'),
            tiles([('calendar', 'Booking'), ('bag', 'Online sales'), ('gift', 'Gift certificates'), ('mail', 'A contact form that sorts enquiries'), ('plane', 'A newsletter sign-up'), ('lock', 'A private area for clients or families')]),
            P(f'Listing them early helps choose the right platform, since {A("Guide-Platforms.dc.html", "Squarespace, Shopify and custom-coded sites")} each handle them differently. {A("Smash.dc.html", "SMASH")}, for example, needed a portal for families, while {A("Rooster-Den.dc.html", "The Rooster Den Co")} needed a store that’s easy to shop.')]),
        ch('inspiration', 'Inspiration', 'Collect a few websites you like', [
            P('Find two or three websites you love, in any industry, and note what you like about each one: the colours, the photos, how easy it is to find things, how it makes you feel. Sites you don’t like are just as helpful, as long as you can say why.'),
            collage(('21d0b9968ab468f637664c26edcb8093', 'A mood board flat lay with photos, colour swatches and paper samples', 800, 1000), ('c1b0714f4853e4cc5257cad7b3ca5bd0', 'A website colour palette board with five soft blue and green swatches above landscape photos', 1080, 720))],
            'A short list of your main competitors is useful too, so your new site can stand apart from them rather than blend in.'),
        ch('timing', 'Timing', 'Share your timing', [
            P('If your new site needs to be ready for something specific, like registration opening, a new season or a product launch, mention it at the start. It’s much easier to plan around a date we both know about.'), g1_dates()]),
    ],
    finale=dict(id='ed-checklist', short='Checklist', label='Before We Begin', title='Your redesign <em>checklist</em>', intro='Tick off what you have so far.',
                items=['Your website’s main goal', 'Notes on your current site', 'A list of pages and words', 'Your logo and brand files', 'Your best photos',
                       'Logins and access', 'Your must-have features', 'A few websites you like', 'Your timing'],
                of='of 9 ready', todo='Every item you gather now is one less thing to chase later.', done='That’s everything. You’re ready to start.'),
    bottom='You don’t need all of this before we talk. A rough idea of your goals and a few links to sites you like is a great place to start, and we can work through the rest together. The more you gather, the more of our time can go into the parts that make your website feel like yours.',
)

G02 = dict(
    file='Guide-Platforms.dc.html', num='02', seal='PLATFORMS', tag='Website Design', read=4,
    title_main='Squarespace, Shopify or <span style="white-space: nowrap">custom-coded:</span>', title_em='choosing your platform',
    stand='How the three platforms I build on compare, and how to tell which one suits your business.',
    cover=('trio', [('847dd40e5930540aa242b3716c025439', 'The pARTy With Laura website on a phone, built on Squarespace', 'Squarespace'),
                    ('d10c98749309b9a833f8b3a2e20d6430', 'The Rooster Den Co store on a phone, built on Shopify', 'Shopify'),
                    ('f912b4f6d45ae4b94acd03c3ac4a84b8', 'SMASH Performing Arts Studio on a phone, custom-coded', 'Custom-coded')]),
    wide=('a6cbf2c369e1a2b92fd12c9d8462bbf8', 'Three websites side by side: pARTy With Laura on Squarespace, The Rooster Den Co on Shopify and SMASH Performing Arts Studio, custom-coded', 1800, 771),
    takeaways=['Squarespace suits service businesses that want to update their own site.', 'Shopify suits businesses that sell products online.',
               'Custom code suits projects that need full design freedom or features beyond a template.', 'Think about who will update the site, and how often.',
               'Choose for where your business is heading, not only where it is today.'],
    intro='The platform behind your website shapes what it can do, how easy it is to update and how it grows with you. I build on Squarespace, Shopify and custom code, so I don’t have a favourite to push. The right choice depends on your business. Here’s how the three compare, and the questions that usually point to the right one.',
    items=[
        ch('glance', 'At a glance', 'The three platforms at a glance', [P('Each platform is a good choice for the right business. Here’s the short version:'), g2_finder()]),
        ('quote', 'The right platform is the one that <span class="ed-q-em">fits</span> how your business works, not the one with the longest feature list.'),
        ch('squarespace', 'Squarespace', 'When Squarespace is the right fit', [
            P('Squarespace is a great home for service businesses, studios and creatives who want a website that looks polished and stays easy to manage. Hosting, security and updates are handled for you, and everyday changes like editing text, swapping photos or adding a blog post don’t need a designer.'),
            browser('dcd61ed19cc8b6da096a0a4dd00cea55', 'The pARTy With Laura homepage, built on Squarespace', 1800, 1125, 'pARTy With Laura, built on Squarespace.'),
            P(f'It also handles more than people expect. {A("Party-With-Laura.dc.html", "pARTy With Laura")} uses it for program pages, booking requests and digital gift certificates.')],
            'Where it can feel limiting is with highly unusual layouts or features it wasn’t designed for. Some of those can be added with code or extensions, but if they’re central to your business, it’s worth looking at custom code.'),
        ch('shopify', 'Shopify', 'When Shopify is the right fit', [
            P('If selling products is at the heart of your business, Shopify is built for it. Products, inventory, payments, shipping and orders all live in one system, and there’s an app for almost any extra feature a store might need.'),
            browser('a392d0d3f88ef802da8c30746b2b7015', 'The Rooster Den Co homepage, built on Shopify', 1800, 1125, 'The Rooster Den Co, built on Shopify.'),
            P(f'{A("Rooster-Den.dc.html", "The Rooster Den Co")} is a good example. The redesign focused on making the store easier to shop, page by page, while the day-to-day running of the business stayed in one place.')],
            'Apps can add monthly costs, so it’s worth choosing them carefully. And if your business is mostly services with only a few products, Squarespace may be the simpler choice.'),
        ch('custom', 'Custom code', 'When custom code is the right fit', [
            P('A custom-coded website is built from the ground up for your business. It makes sense when you need complete design freedom, a feature no template offers or a site that brings several tools together.'),
            browser('f0c930075e2e8c051a7214d5859d72bb', 'The SMASH blog with the Ask SMASH assistant open, answering a question about a trial period', 1800, 1125, 'SMASH Performing Arts Studio, custom-coded, with its AI assistant open.'),
            P(f'{A("Smash.dc.html", "SMASH Performing Arts Studio")} needed a password-protected portal for families and an AI assistant that answers questions about the studio and its programmes. {A("Hamish-Ross.dc.html", "Hamish Ross Real Estate")} needed a high-end, luxury identity carried from page to page. Both are things a custom build does well.')],
            'The trade-off is that editing depends on how the site is built. Some custom sites include an easy way to update content, and others are updated with help. We decide that together before the build starts, so there are no surprises.'),
        ('spread', ('a6cbf2c369e1a2b92fd12c9d8462bbf8', 'Three websites side by side: pARTy With Laura on Squarespace, The Rooster Den Co on Shopify and SMASH Performing Arts Studio, custom-coded', 1800, 771), '16 / 10', 'Looking Ahead', 'Choose for where your business is <em>heading</em>, not only where it is today.'),
        ch('questions', 'Questions', 'Questions that point to the right platform', [
            cards(['Do you sell products online, or mainly services?', 'Who will update the website, and how often?',
                   'Do you need anything a template can’t do, like a portal, an AI assistant or a connection to another system?',
                   'How important is complete control over the design?', 'Where do you see your business in a few years?'], cls='ed-qs ed-qs-5')],
            'If you’re not sure about some of these, that’s normal. We’ll talk through the options before deciding on a direction.'),
        ch('switching', 'Switching later', 'What about switching later?', [
            P('Moving a website from one platform to another is often possible. What’s involved depends on where your site is now and where it’s going.'),
            g2_path(),
            P('It’s still worth choosing for where your business is heading, not just where it is today. A platform that fits your plans saves you from rebuilding sooner than you’d like.')]),
    ],
    bottom='There’s no single best platform, only the best fit for your business. Squarespace keeps things simple and easy to manage, Shopify is built for selling and custom code gives you complete freedom. Tell me about your business and what you need your website to do, and I’ll recommend the platform that suits it.',
)

G03 = dict(
    file='Guide-Branding.dc.html', num='03', seal='BRANDING', tag='Brand and Marketing', read=3,
    title_main='What to have ready before', title_em='branding or a website build',
    stand='Logo files, colours, fonts and photos: what helps, and what we can shape together.',
    cover=('arch', '1f31822f8797726ca4c0926e614ef42b', 'A coastal colour palette of soft sea blues and greens beside a photo of a misty shoreline', 900, 1125, '50% 50%'),
    wide=('5cff939fb0c6c09242fc1bc76414a376', 'Five colour palettes from recent projects: SMASH, Hamish Ross, pARTy With Laura, The Rooster Den Co and Callum Frost', 1800, 771),
    takeaways=['Your logo, in the best file formats you have.', 'Your colours, with their exact codes if you know them.', 'Your fonts, or a sense of the style you like.',
               'Photos that show your work and your personality.', 'A few words that describe how you want your business to feel.'],
    intro='A consistent brand makes a business easier to recognise and easier to trust. Before we start on your website or marketing, it helps to know what you already have and what still needs defining. You don’t need a finished brand guide. Here’s what to gather, and what we can shape together.',
    items=[
        ch('logo', 'Logo files', 'Your logo files', [
            P('Your logo is usually the starting point. Look for a vector version (SVG, EPS, AI or PDF), which can be resized without losing quality, and a PNG with a transparent background for everyday use.'),
            f'<div class="ed-kit-p ed-files-wide sp-reveal"><p class="ed-kit-l">Logo files worth finding</p>{files(["SVG", "EPS", "AI", "PDF", "PNG"], "SVG, EPS, AI, PDF and a PNG with a transparent background")}</div>',
            P('If you have more than one version, such as a stacked logo, a horizontal one or a small icon, gather them all. Each one is useful in different places, from the top of your website to a social profile picture.')],
            f'I don’t design logos, but if you have one you love, I can build the wider look around it. That’s what happened with {A("Party-With-Laura.dc.html", "pARTy With Laura")}, where the palette grew from her existing brush-script logo.'),
        ch('colours', 'Colours', 'Your colours', [
            P('Note your brand colours and, if you know them, their codes. HEX codes (like #4E6368) are used on screens, while CMYK or Pantone values are used in print.'),
            P('A good palette usually has one or two main colours, an accent for buttons and highlights, and a few neutrals for backgrounds and text. If yours feels incomplete, or the colours don’t quite work together on screen, that’s something we can refine.'),
            g3_palettes()],
            f'Colour sets the mood, too. {A("Callum-Frost.dc.html", "Callum Frost")} wanted something classy and simple, so we chose black and white together and let his headshots do the talking.'),
        ch('fonts', 'Fonts', 'Your fonts', [
            P('If you don’t have brand fonts yet, think about the feel you’re after. An elegant serif can feel refined and established, while a clean sans serif can feel modern and approachable. Many brands pair one of each: one for headings and one for everyday text.'),
            g3_typepair()],
            'If your brand uses specific fonts, note their names and where they came from. Some fonts are free to use on websites, while others need a licence, so it’s worth checking before we start.'),
        ('spread', ('71e6579541514b77d25f0c390675b259', 'A font specimen for an elegant display typeface called Baletic, in deep teal', 900, 1125), '4 / 5', 'Why It Matters', 'A consistent brand makes a business easier to <em>recognise</em> and easier to trust.'),
        ch('imagery', 'Photos', 'Your photos and imagery', [
            P('Photos carry your brand as much as colours and fonts do. Gather your best photos of your work, your space and the people behind the business, in the largest size you have.'),
            P('Think about the style that feels like you, too: bright or moody, polished or relaxed, close-up details or wide open spaces. A consistent style across your website and marketing helps everything feel connected.'),
            g3_scales()]),
        ('quote', 'You don’t need a finished brand guide to start. You need a clear sense of how you want people to <span class="ed-q-em">feel</span>.'),
        ch('words', 'Words', 'The words that describe you', [
            P('Before any design decisions, it helps to put the feeling into words. Write down three to five words that describe how you want your business to feel. Calm, playful, luxurious, warm and bold all lead to very different designs.'),
            g3_words(),
            P('Then add a sentence about who you serve and what makes you different. It shapes the look as much as the copy, and it becomes the reference point for every choice that follows.')]),
        ch('inspiration', 'Inspiration', 'Images you’re drawn to', [
            P('Collect images that capture the feeling you want, from websites, magazines, interiors, nature or anywhere else. Don’t worry about why yet. Patterns tend to appear once you have a dozen or so.'),
            collage(('21d0b9968ab468f637664c26edcb8093', 'A mood board flat lay with photos, colour swatches and paper samples', 800, 1000), ('4fc3a891bb11afcf3293d60c8de857ae', 'White pebbles beside a neutral palette of soft greys and stone', 900, 900))],
            'A mood board brings these together: a single page of colours, textures, type and photos that shows the direction before anything is designed. It’s a quick way to make sure we’re picturing the same thing.'),
        ch('where', 'Where it appears', 'Where your brand will appear', [
            P('List the places your brand needs to work: your website, social media, newsletters, ads, signage, business cards or packaging. Knowing this early means colours, fonts and layouts are chosen to work everywhere, not just on screen.'),
            g3_places(),
            P(f'That’s how a look carries from a website into everyday marketing, like the monthly newsletters for {A("Smash.dc.html", "SMASH Performing Arts Studio")}, which share the same navy, gold and elegant serif headlines as the site.'),
            g3_smash_pair()]),
    ],
    bottom='Whether you’re starting fresh or carrying an established look forward, gathering these pieces makes the design process faster and the result more consistent. If some are missing, that’s what we work out together. Tell me what you have, and we’ll take it from there.',
)

G04 = dict(
    file='Guide-Search.dc.html', num='04', seal='SEARCH', tag='SEO', read=4,
    title_main='How to help Google and AI search', title_em='find your business',
    stand='The foundations that help search engines and AI tools understand who you are and what you offer.',
    cover=('arch', '45cb69a70875d32f60c5bd0a6db8fea4', 'Sunlight rippling through clear, shallow blue water', 900, 1125, '50% 50%'),
    wide=('99c229f238a46297d17abd3836a64f4e', 'Search result cards showing page titles and descriptions from pARTy With Laura and The Rooster Den Co', 1800, 771),
    takeaways=['Know the words and questions your customers actually use.', 'Give every page one clear purpose, title and description.', 'Answer common questions in plain language.',
               'Set up Google Business Profile and Search Console.', 'Build steadily over time, never with shortcuts.'],
    intro='People now find businesses in two ways: through search results and through AI tools like ChatGPT, Perplexity and Google’s AI results. The good news is that both reward the same things: a clear, well-organized website that genuinely answers people’s questions. Here are the foundations I focus on, and the ones you can start on today.',
    items=[
        ch('customers', 'How people search', 'Start with how your customers search', [
            P('Good SEO starts with knowing what your customers search for. Think about the words they use (which aren’t always the words you use), the questions they ask and the places they live or work.'),
            g4_xlate(),
            P('A real estate agent might think in terms of listings, while buyers search for homes for sale in White Rock. Writing for the way people actually search makes it much easier for them to find you.')]),
        ch('pages', 'One clear job', 'Give every page one clear job', [
            P('Each important service or topic deserves its own page, with one clear heading that says exactly what it is. A single page trying to cover everything is harder for visitors and search engines to understand.'),
            P(f'Organize your menu around what people look for, too. On {A("Hamish-Ross.dc.html", "Hamish Ross Real Estate")}, the market report and journal sit in the main menu alongside listings, buying and selling.'),
            g4_menu()]),
        ch('titles', 'Titles', 'Write titles and descriptions that say what’s there', [
            P('Every page has a title and a short description that can appear in search results. They’re often the first thing someone reads about your business, so make them specific: what the page offers, and where, if that matters.'),
            g4_serp(),
            P('Vague titles like Services or Home waste that space. A title like Weekly Kids Art Classes in Cloverdale tells people, and search engines, exactly what they’ll find.')]),
        ('quote', 'Clear, well-organized and <span class="ed-q-em">genuinely useful</span> content helps you in search results and in AI answers.'),
        ch('answers', 'Plain answers', 'Answer questions in plain language', [
            P('AI tools in particular look for clear, direct answers. Pages that plainly explain what you offer, who it’s for, where you work and what happens next are easier for them to understand and mention.'),
            cards(['What you offer', 'Who it’s for', 'Where you work', 'What happens next'], cls='ed-qs ed-qs-4'),
            P('FAQs, service pages that explain the details and guides like this one all help. So does structured information behind the scenes (often called schema), which labels things like your business name, location and services so they can be read reliably.'),
            g4_schema()]),
        ('spread', ('99c229f238a46297d17abd3836a64f4e', 'Search result cards showing page titles and descriptions from pARTy With Laura and The Rooster Den Co', 1800, 771), '16 / 10', 'The Good News', 'Search and AI reward the same things: a clear website that genuinely <em>answers</em> people’s questions.'),
        ch('local', 'Location', 'Show where you are', [
            P(f'If you serve a particular area, say so clearly in your page titles, headings and copy. Name the neighbourhoods and cities you serve, the way {A("Hamish-Ross.dc.html", "Hamish Ross Real Estate")} names White Rock, South Surrey and Ocean Park.'),
            g4_areas(),
            P(f'Set up a Google Business Profile with accurate details, photos and hours, and keep your business name, address and phone number the same everywhere they appear online. I set one up for {A("Rooster-Den.dc.html", "The Rooster Den Co")} as part of the store’s redesign.'),
            g4_nap()]),
        ch('experience', 'Easy to use', 'Make your site easy to use', [
            P('Search engines pay attention to the experience a site offers. Pages should load quickly, work well on phones and be easy to navigate. Descriptive image file names and alt text help too, for search and for people using screen readers.'),
            tiles([('bolt', 'Loads quickly'), ('phone', 'Works well on phones'), ('compass', 'Easy to navigate'), ('image', 'Descriptive image names and alt text')], ' ed-feats-4')]),
        ch('tools', 'Tools', 'Connect the right tools', [
            P('Google Search Console shows which searches bring people to your site and flags problems Google finds. Google Analytics shows what visitors do once they arrive. Both are free, and setting them up at launch means you have useful information from day one.'),
            g4_tools()]),
        ch('steady', 'Steady growth', 'Build steadily, without shortcuts', [
            P('SEO builds over time. Some improvements can show up fairly quickly, while broader progress usually takes months of steady work.'),
            g4_growth(),
            P('Avoid tricks like stuffing keywords into every sentence, creating near-identical pages for every town or buying links. They can do more harm than good. Useful content and a well-organized website are what last.'),
            g4_avoid()],
            'Be wary of anyone who promises fast rankings or a guaranteed spot.'),
    ],
    bottom='You don’t need to master every detail of SEO to make progress. Start with clear pages, specific titles, plain-language answers and an accurate Google Business Profile, then keep improving over time. If you’d like help, I can look at where your website is now and make each page clearer, whether I built it or not.',
)

G05 = dict(
    file='Guide-Support.dc.html', num='05', seal='SUPPORT', tag='Ongoing Support', read=3,
    title_main='What ongoing website and marketing support', title_em='can include',
    stand='SEO, content, newsletters and website updates: what it looks like to have someone keeping things moving.',
    cover=('arch', '9d930f0005e922e78c45f80d54d6cf07', 'A laptop and an open notebook on a bright white desk beside a window', 900, 1125, '50% 50%'),
    wide=('e3423a54ddc73a58c47dfc70bdc215f7', 'A laptop on a small table on a sunny balcony overlooking the sea, beside two cups of coffee and a vase of flowers', 1800, 771),
    takeaways=['A website works best when it’s kept current after launch.', 'Support can cover SEO, content, newsletters, social media and updates.',
               'Scope and priorities are agreed in advance, so you know what’s covered.', 'It suits you if you’d rather spend your time running your business.',
               'Even without support, a simple routine keeps your site healthy.'],
    intro='A website isn’t finished the day it launches. Your business changes, your customers’ questions change and search keeps moving. Ongoing support means someone is looking after your website and marketing so they keep up, without it landing on your to-do list. Here’s what it can include, and how to tell if it’s right for you.',
    items=[
        ch('why', 'Why it matters', 'Why a website needs looking after', [
            P('Information goes out of date quickly: prices, programs, team members, photos and opening hours. An out-of-date page can quietly cost you trust, and search engines tend to favour sites that stay current and useful.'),
            g5_tokens()],
            'Small, regular attention also keeps little problems from growing, like a broken link, a form that’s stopped sending or a page that no longer reflects how you work.'),
        ch('updates', 'Updates', 'Website updates', [
            P(f'This is the everyday care: new photos, updated text, new pages, seasonal changes and fixes as they come up. For {A("Callum-Frost.dc.html", "Callum Frost")}, that means adding his new headshots and resume changes whenever he has them.'),
            g5_log()]),
        ('quote', 'A website works hardest when someone is <span class="ed-q-em">paying attention</span> to it.'),
        ch('seo', 'SEO and content', 'SEO and website content', [
            P(f'Ongoing SEO builds on the foundations set at launch. It can include planning content around what your customers search for, refining pages that could be clearer and keeping an eye on how your site appears in search. My {A("Guide-Search.dc.html", "guide to search and AI")} covers those foundations.'),
            g5_related()],
            'Blogs and articles can be part of this, too, written around real customer questions rather than posted for the sake of it.'),
        ch('newsletters', 'Newsletters', 'Newsletters', [
            P(f'A regular newsletter keeps you in touch with the people who already know you. As part of their ongoing support, I create the monthly newsletters for {A("Smash.dc.html", "SMASH Performing Arts Studio")}, sharing studio news and important dates with families.'),
            g5_fan()]),
        ch('social', 'Social and design', 'Social content and marketing design', [
            P('Social graphics, ads and printed pieces work best when they clearly belong to the same business as your website. Ongoing support can include designing these regularly, so your marketing stays consistent without you briefing someone new each time.'),
            g5_formats()]),
        ('spread', ('e3423a54ddc73a58c47dfc70bdc215f7', 'A laptop on a small table on a sunny balcony overlooking the sea, beside two cups of coffee and a vase of flowers', 1800, 771), '16 / 10', 'The Idea', 'Someone looking after your website and marketing, without it landing on your <em>to-do list</em>.'),
        ch('how', 'How it works', 'How ongoing support works', [
            P('Every business needs something different. We agree on the scope and priorities in advance, so you know what I’m handling and how it supports your wider plans.'),
            P('It can focus on one area, like monthly newsletters, or bring several together around your business priorities, such as SEO, blogs, social content and website updates.'),
            g5_opts()]),
        ch('signs', 'Signs', 'Signs it might be time', [
            checklist('ed-sg', ['Your website has information you know is out of date.', 'Updates sit on your to-do list for weeks.', 'Your marketing looks a little different every time.',
                                'You know SEO matters but don’t have time for it.', 'You’d rather spend your time on your actual work.'],
                      'of 5 sound familiar', 'Tick any that sound like you.', 'Sound familiar? That’s exactly what ongoing support is for.', cls=' ed-cl-any', inline=True, legend='Which of these sound familiar?')]),
        ch('diy', 'Do it yourself', 'If you’d rather do it yourself', [
            P('Ongoing support isn’t for everyone, and plenty of small businesses look after their own sites. If that’s you, a simple routine goes a long way:'),
            g5_routine()]),
    ],
    bottom='Ongoing support is about keeping your website and marketing moving, so they keep reflecting your business as it grows. If you’d like help with some or all of it, tell me what’s on your plate and we’ll work out the right scope together.',
)

GUIDES = [G01, G02, G03, G04, G05]


# ================================================================== page assembly
def seal(word, num):
    return f'''<svg class="ed-seal" viewBox="0 0 200 200" aria-hidden="true">
<defs><path id="ed-seal-path" d="M100,100 m-76,0 a76,76 0 1,1 152,0 a76,76 0 1,1 -152,0"></path></defs>
<circle cx="100" cy="100" r="99" fill="#FAFAF8"></circle>
<circle cx="100" cy="100" r="91" fill="none" stroke="#4E6368" stroke-width="0.8"></circle>
<circle cx="100" cy="100" r="58" fill="none" stroke="#4E6368" stroke-width="0.6"></circle>
<text font-family="Abel, 'Arial Narrow', sans-serif" font-size="13" fill="#4E6368"><textPath href="#ed-seal-path" textLength="472" lengthAdjust="spacing">THE SULLIVAN PARK GUIDES · {word} ·</textPath></text>
<text x="100" y="121" text-anchor="middle" font-family="'Cormorant Infant', Garamond, serif" font-style="italic" font-weight="300" font-size="60" fill="#121414">{num}</text>
</svg>'''


def cover_visual(g):
    c = g['cover']
    if c[0] == 'arch':
        _, bid, alt, w, h, pos = c
        return f'''<div class="ed-arch">
<span class="ed-arch-frame" aria-hidden="true"></span>
<div class="ed-arch-img"><img src="/_blob/{bid}" alt="{alt}" width="{w}" height="{h}" fetchpriority="high" style="object-position: {pos}"></div>
{seal(g['seal'], g['num'])}
</div>'''
    hi, lazy = ' fetchpriority="high"', ' loading="lazy"'
    arches = ''.join(f'<figure class="ed-trio-i"><div class="ed-trio-arch"><img src="/_blob/{bid}" alt="{alt}" width="600" height="1298"{hi if i == 1 else lazy}></div><figcaption>{lab}</figcaption></figure>' for i, (bid, alt, lab) in enumerate(c[1]))
    return f'<div class="ed-trio">{arches}{seal(g["seal"], g["num"])}</div>'


def chapter(n, c, row):
    note = c.get('note')
    notehtml = f'<aside class="ed-note" aria-label="Good to know"><p class="ed-note-l">Good to know</p><p class="ed-note-t">{note}</p></aside>' if note else ''
    return f'''<section class="ed-ch{'' if note else ' ed-ch-nonote'}" id="{c['id']}" aria-labelledby="{c['id']}-h" style="grid-row: {row}">
<div class="ed-ch-main">
<p class="ed-kick"><span class="ed-kick-n" aria-hidden="true">{n:02d}</span><span class="ed-kick-l">{c['short']}</span></p>
<h2 id="{c['id']}-h" class="ed-h2">{c['title']}</h2>
{chr(10).join(c['body'])}
</div>
{notehtml}
</section>'''


def quote(row, text):
    return f'''<blockquote class="ed-bleed ed-quote" style="grid-row: {row}">
<img class="ed-quote-img" src="/_blob/073cf407ae15e1c7bada61ba8e7a8dd6" alt="" width="852" height="480" loading="lazy">
<span class="ed-quote-tint" aria-hidden="true"></span>
<div class="ed-wrap ed-quote-in"><p class="sp-reveal">{text}</p></div>
</blockquote>'''


def spread(row, im, aspect, lab, line):
    bid, alt, w, h = im
    return f'''<div class="ed-bleed ed-spread" style="grid-row: {row}">
<div class="ed-wrap ed-spread-in">
<figure class="ed-spread-fig sp-reveal"><span class="ed-frame" aria-hidden="true"></span><div class="sp-photo" style="position: relative"><img src="/_blob/{bid}" alt="{alt}" width="{w}" height="{h}" loading="lazy" style="width: 100%; aspect-ratio: {aspect}; object-fit: cover"></div></figure>
<div class="ed-spread-t sp-reveal">{label(lab)}<p class="ed-spread-q">{line}</p></div>
</div>
</div>'''


def finale(row, f):
    body = checklist('ed-ck', f['items'], f['of'], f['todo'], f['done'])
    return f'''<section class="ed-bleed ed-cl-band" id="{f['id']}" aria-labelledby="ed-cl-h" style="grid-row: {row}">
<div class="ed-wrap"><div class="ed-cl">
<div class="ed-cl-head">{label(f['label'])}<h2 id="ed-cl-h" class="ed-h2 ed-cl-title">{f['title']}</h2><p class="ed-p">{f['intro']}</p></div>
{body}
</div></div>
</section>'''


def bottom(row, text):
    return f'''<section class="ed-bleed ed-bottom sp-on-dark" aria-labelledby="bottom-line" id="ed-bottom" style="grid-row: {row}">
{PALM_DARK}
<div class="ed-wrap ed-bottom-in">
<h2 id="bottom-line" class="ed-bottom-h sp-reveal">The bottom <em>line</em></h2>
<div class="ed-bottom-t sp-reveal"><p>{text}</p>
<a class="sp-btn sp-btn-light" href="Contact.dc.html" style="align-self: flex-start; display: inline-flex; align-items: center; justify-content: center; gap: 14px; min-height: 56px; padding: 0 30px; background: #FAFAF8; border: 1px solid #FAFAF8; color: {INK}; text-decoration: none; font-size: 18px; letter-spacing: 0.03em">Enquire About Your Project{ARROW}</a></div>
</div>
</section>'''


def build(g, template):
    nxt = GUIDES[(GUIDES.index(g) + 1) % len(GUIDES)]
    chapters = [c for c in g['items'] if isinstance(c, dict)]
    rows = []; r = 2; n = 0
    for c in g['items']:
        if isinstance(c, dict):
            n += 1; rows.append(chapter(n, c, r))
        elif c[0] == 'quote': rows.append(quote(r, c[1]))
        elif c[0] == 'spread': rows.append(spread(r, *c[1:]))
        r += 1
    if g.get('finale'):
        rows.append(finale(r, g['finale'])); r += 1
    rows.append(bottom(r, g['bottom'])); last = r

    rail = ''.join(f'<li><a href="#{c["id"]}"><span class="ed-rail-n" aria-hidden="true">{i:02d}</span>{c["short"]}</a></li>' for i, c in enumerate(chapters, 1))
    if g.get('finale'):
        rail += f'<li><a href="#{g["finale"]["id"]}"><span class="ed-rail-n" aria-hidden="true">✓</span>{g["finale"]["short"]}</a></li>'
    short = ''.join(f'<li><span class="ed-short-n" aria-hidden="true">{i:02d}</span><span class="ed-short-t">{t}</span></li>' for i, t in enumerate(g['takeaways'], 1))
    cover = f'''<!-- EDITORIAL COVER -->
<header class="ed-cover{' ed-cover-trio' if g['cover'][0] == 'trio' else ''}">
{PALM}
<div class="ed-wrap ed-cover-grid">
<div class="ed-cover-text">
{label(f"Guide {g['num']} · {g['tag']}")}
<h1 id="page-title" class="ed-title">{g['title_main']} <em>{g['title_em']}</em></h1>
<p class="ed-stand">{g['stand']}</p>
<div class="ed-meta">
<span style="display: inline-flex; align-items: center; gap: 14px"><img src="/_blob/61209a65a04271cd5c18338b2938e4f1" alt="" width="1000" height="1000" style="width: 48px; height: 48px; border-radius: 50%; object-fit: cover; object-position: 50% 20%; border: 1px solid rgba(78, 99, 104, 0.35); padding: 3px; background: #FFFFFF"><span>By <span style="color: {INK}">Natasha</span></span></span>
<span aria-hidden="true" class="ed-meta-rule"></span><span>{g['read']} min read</span>
<span aria-hidden="true" class="ed-meta-rule ed-meta-ch"></span><span class="ed-meta-ch">{len(chapters)} chapters</span>
</div>
<a class="ed-begin sp-link" href="#ed-start">Begin Reading<svg width="10" height="22" viewBox="0 0 10 26" fill="none" aria-hidden="true"><path d="M5 0v24M1 20l4 4 4-4" stroke="currentColor" stroke-width="1.1"></path></svg></a>
</div>
{cover_visual(g)}
</div>
</header>

<!-- IN SHORT -->
<section class="ed-short" aria-labelledby="ed-short-h">
<div class="ed-wrap ed-short-in">
<h2 id="ed-short-h" class="ed-short-h"><span aria-hidden="true"></span>In Short</h2>
<ol class="ed-short-list">{short}</ol>
</div>
</section>'''

    body = f'''<!-- EDITORIAL BODY -->
<div class="ed-body-bg">
<div class="ed-wrap ed-body">
<nav class="ed-rail" aria-label="Chapters" style="grid-row: 1 / span {last}">
<p class="ed-rail-h">In This Guide</p>
<div class="ed-rail-track"><span class="ed-rail-fill" aria-hidden="true"></span><ol>{rail}</ol></div>
</nav>
<div class="ed-intro" id="ed-start" style="grid-row: 1"><p class="ed-standfirst">{g['intro']}</p></div>
{chr(10).join(rows)}
</div>
</div>'''

    s = template
    a0 = s.index('<aside class="sp-card sp-reveal" aria-label="About the author"'); a1 = s.index('</aside>', a0) + len('</aside>')
    author = s[a0:a1].replace('margin-top: 36px; ', '')
    wb, wa, ww, wh = nxt['wide']
    after = f'''<!-- AUTHOR -->
<section aria-label="About the author" style="background: #FFFFFF">
<div class="ed-wrap" style="padding-top: clamp(72px, 8vw, 112px); padding-bottom: clamp(56px, 6vw, 88px); display: flex; flex-direction: column; align-items: center; gap: 28px">
<div style="width: 100%; max-width: 960px">{author}</div>
</div>
</section>

<!-- UP NEXT -->
<section class="ed-next-band" aria-labelledby="ed-next-h">
<div class="ed-wrap" style="padding-top: clamp(56px, 6vw, 88px); padding-bottom: clamp(80px, 9vw, 128px)">
<a class="ed-next" href="{nxt['file']}">
<span class="ed-next-t">
{label(f"Up Next · Guide {nxt['num']}")}
<span id="ed-next-h" class="ed-next-h">{nxt['title_main']} <em>{nxt['title_em']}</em></span>
<span class="ed-next-go">Read the Guide{ARROW}</span>
</span>
<span class="ed-next-img"><span class="ed-frame" aria-hidden="true"></span><span class="sp-photo" style="position: relative; display: block"><img src="/_blob/{wb}" alt="{wa}" width="{ww}" height="{wh}" loading="lazy" style="width: 100%; aspect-ratio: 16 / 9; object-fit: cover"></span></span>
</a>
<a class="sp-link" href="Journal.dc.html" style="margin-top: 36px; display: inline-flex; align-items: center; gap: 12px; min-height: 44px; color: {TEAL}; font-size: 17px; letter-spacing: 0.03em; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 6px">Browse All Guides{ARROW}</a>
</div>
</section>'''
    m0 = s.index('<!-- SEE IT IN PRACTICE -->'); m1 = s.index('</main>')
    tail = s[m0:m1].rstrip()
    main = f'<article aria-labelledby="page-title">\n\n{cover}\n\n{body}\n\n</article>\n\n{after}\n\n{tail}'
    a = s.index('<main id="main">'); b = s.index('</main>') + len('</main>')
    s = s[:a] + '<main id="main">\n' + main + '\n</main>' + s[b:]

    css = open(os.path.join(HERE, 'editorial.css')).read().strip()
    names = ','.join(f'--ed-c{i}' for i in range(1, len(chapters) + 1))
    chap_tl = '\n'.join(f'#{c["id"]}{{view-timeline-name:--ed-c{i}}}\n.ed-rail li:nth-child({i}) a{{animation-timeline:--ed-c{i}}}' for i, c in enumerate(chapters, 1))
    css = css.replace('/*SEGMENTS*/', '\n'.join(SEGMENT_RULES)).replace('/*TL_NAMES*/', names).replace('/*CHAPTER_TIMELINES*/', chap_tl)
    block = f'/* EDITORIAL */\n{css}\n/* /EDITORIAL */\n'
    if '/* EDITORIAL */' in s:
        x = s.index('/* EDITORIAL */'); y = s.index('/* /EDITORIAL */') + len('/* /EDITORIAL */') + 1
        s = s[:x] + block + s[y:]
    else:
        s = s.replace('/* NAV v2 (generated) */', block + '/* NAV v2 (generated) */', 1)
    heights = {}
    hp = os.path.join(HERE, 'editorial_heights.txt')
    if os.path.exists(hp):
        for line in open(hp):
            k, v = line.split(); heights[k] = int(v)
    h = heights.get(g['file'], 14000)
    s = re.sub(r'"\$preview":\{"width":1440,"height":\d+\}', f'"$preview":{{"width":1440,"height":{h}}}', s, count=1)
    txt = re.sub(r'<[^>]+>', ' ', main)
    assert '—' not in txt and ' -- ' not in txt and 'bespoke' not in txt.lower(), ('copy rule', g['file'])
    return s


for g in GUIDES:
    if ONLY and g['file'] not in ONLY:
        continue
    SEGMENT_RULES.clear()
    # visuals that register segment rules are created at import time; re-add those for this guide
    for c in g['items']:
        if isinstance(c, dict):
            for b in c['body']:
                for m in re.finditer(r'id="(ed-[a-z]+)(\d+)"', b):
                    if 'type="checkbox"' in b:
                        SEGMENT_RULES.append(f'.ed-cl:has(#{m.group(1)}{m.group(2)}:checked) .ed-cl-bar span:nth-child({m.group(2)}){{background:#4E6368}}')
    tpl = open(os.path.join(HERE, 'guide_src', g['file'])).read()
    out = build(g, tpl)
    open(os.path.join(ROOT, g['file']), 'w').write(out)
    print('written', g['file'], len(out))
