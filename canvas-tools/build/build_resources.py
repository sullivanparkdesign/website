"""Resources page (Journal.dc.html) as a guide library, and Guide 01 (Article.dc.html).
Edits the existing pages in place: head meta, <main> content and a scoped CSS block."""
import json, os, re, sys

ROOT = sys.argv[1]
HERE = os.path.dirname(__file__)
LB = json.load(open(os.path.join(HERE, '..', 'laura', 'blobs.json')))
CB = json.load(open(os.path.join(HERE, '..', 'callum', 'blobs.json')))
SB = json.load(open(os.path.join(HERE, '..', 'smash', 'blobs.json')))

SERIF = "'Cormorant Infant', Garamond, serif"
TEAL, INK, BODY, MUTED = '#4E6368', '#121414', '#1F2426', '#4E5558'
ARROW = '<svg width="22" height="10" viewBox="0 0 26 10" fill="none" aria-hidden="true"><path d="M0 5h24M20 1l4 4-4 4" stroke="currentColor" stroke-width="1.1"></path></svg>'
WRAP = 'width: 100%; max-width: 1680px; margin: 0 auto'
GUTTER = 'clamp(20px, 5vw, 72px)'
IMG = {'hero': '/_blob/c88afba51f29e1af4a1ad91e130aa1ec', 'card': '/_blob/9095e97c95708cc67b261cafbb8c1d21',
       'notebook': '/_blob/87b256f87275018e5bfde23768efc920', 'mood': '/_blob/21d0b9968ab468f637664c26edcb8093'}
GUIDE1 = 'Article.dc.html'

GUIDES = [
    ('Planning', 'What to prepare before a website redesign', 'The goals, content, photos and logins worth gathering first, so your project starts smoothly.', GUIDE1),
    ('Website Design', 'Squarespace, Shopify or custom-coded: choosing your platform', 'How the three platforms I build on compare, and how to tell which one suits your business.', None),
    ('Brand and Marketing', 'What to have ready before branding or a website build', 'Logo files, colours, fonts and photos: what helps, and what we can create together.', None),
    ('SEO', 'How to help Google and AI search find your business', 'The foundations that help search engines and AI tools understand who you are and what you offer.', None),
    ('Ongoing Support', 'What ongoing website and marketing support can include', 'SEO, content, newsletters and website updates: what it looks like to have someone keeping things moving.', None),
]


def label(text, color=TEAL, size=15):
    return f'<p style="margin: 0; display: flex; align-items: center; gap: 16px; font-size: {size}px; letter-spacing: 0.2em; text-transform: uppercase; color: {color}"><span aria-hidden="true" style="display: block; width: 40px; height: 1px; background: {color}"></span>{text}</p>'


def link(href, text):
    return f'<a href="{href}" style="color: {TEAL}; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 4px">{text}</a>'


def swap_head(s, title, desc):
    s = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', s, count=1)
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', s, count=1)
    s = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{title}">', s, count=1)
    s = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{desc}">', s, count=1)
    return s


def swap_main(s, main):
    a = s.index('<main id="main">'); b = s.index('</main>') + len('</main>')
    return s[:a] + '<main id="main">\n' + main + '\n</main>' + s[b:]


def swap_css(s, css, tag):
    start, end = f'/* {tag} */', f'/* /{tag} */'
    block = f'{start}\n{css}\n{end}\n'
    if start in s:
        a = s.index(start); b = s.index(end) + len(end) + 1
        return s[:a] + block + s[b:]
    anchor = '/* NAV v2 (generated) */'
    return s.replace(anchor, block + anchor, 1)


def set_preview(s, h):
    return re.sub(r'"\$preview":\{"width":1440,"height":\d+\}', f'"$preview":{{"width":1440,"height":{h}}}', s, count=1)


CLOSING_RE = re.compile(r'<!-- CLOSING -->.*?</section>', re.S)

# ---------------------------------------------------------------- RESOURCES
def resources():
    p = os.path.join(ROOT, 'Journal.dc.html'); s = open(p).read()
    closing = CLOSING_RE.search(s).group(0)

    hero = f'''<!-- HERO -->
<section aria-labelledby="page-title" style="position: relative; overflow: hidden; background: #FAFAF8">
<img class="sp-sway" src="/_blob/fddc24a18e2595d21f63da9f1d7bf0d5" alt="" width="1800" height="1200" style="position: absolute; top: -20px; right: -20px; width: min(1320px, 110vw); height: auto; max-width: none; opacity: 0.16; mix-blend-mode: multiply; pointer-events: none; z-index: 0">
<div style="position: relative; z-index: 1; {WRAP}; padding: clamp(140px, 12vw, 172px) {GUTTER} clamp(64px, 7vw, 96px); display: flex; flex-wrap: wrap; align-items: flex-end; gap: 64px clamp(48px, 7vw, 120px)">
<div style="flex: 1.5 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 28px; padding-bottom: clamp(0px, 3vw, 40px)">
{label('Guides')}
<h1 id="page-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(54px, 7.4vw, 120px); line-height: 0.98; letter-spacing: -0.015em; color: {INK}; text-wrap: balance">Resources</h1>
<p style="margin: 0; font-size: 21px; line-height: 1.65; color: {BODY}">Practical guides to planning your website, preparing your brand and helping the right people find you.</p>
</div>
<div class="sp-hero-photo" style="flex: 0 1 380px; min-width: 0; position: relative; padding: 0 0 24px 24px; margin-left: auto">
<span aria-hidden="true" style="position: absolute; top: 24px; left: 0; right: 24px; bottom: 0; border: 1px solid rgba(78, 99, 104, 0.45)"></span>
<div class="sp-photo" style="position: relative"><img src="{IMG['mood']}" alt="A mood board flat lay with photos, colour swatches and paper samples" width="800" height="1000" fetchpriority="high" style="width: 100%; aspect-ratio: 4 / 5; object-fit: cover"></div>
</div>
</div>
</section>'''

    feature = f'''<!-- START HERE: Guide 01 -->
<section aria-labelledby="start-title" style="background: #FFFFFF">
<div style="{WRAP}; padding: clamp(72px, 8vw, 112px) {GUTTER}">
<a class="sp-feature sp-reveal" href="{GUIDE1}" style="display: flex; flex-wrap: wrap; align-items: center; gap: 40px clamp(48px, 6vw, 104px); text-decoration: none; color: {INK}">
<div style="flex: 1.3 1 520px; min-width: 0; position: relative; padding: 0 24px 24px 0">
<span aria-hidden="true" style="position: absolute; top: 24px; left: 24px; right: 0; bottom: 0; border: 1px solid rgba(78, 99, 104, 0.45)"></span>
<div class="sp-photo" style="position: relative"><img src="{IMG['card']}" alt="An open, light-filled pavilion overlooking a calm sea" width="1200" height="800" loading="lazy" style="width: 100%; aspect-ratio: 3 / 2; object-fit: cover"></div>
</div>
<div style="flex: 1 1 380px; min-width: 0; display: flex; flex-direction: column; gap: 22px">
{label('Start Here · Guide 01')}
<h2 id="start-title" class="sp-feature-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(38px, 4vw, 62px); line-height: 1.06; color: {INK}; text-wrap: balance">What to prepare before a website redesign</h2>
<p style="margin: 0; font-size: 19px; line-height: 1.7; color: {BODY}">The goals, content, photos and logins worth gathering first, so your project starts smoothly and our time goes into the parts that matter most.</p>
<p style="margin: 0; font-size: 16px; letter-spacing: 0.08em; color: {MUTED}">{{READ}} min read · Natasha</p>
<span style="align-self: flex-start; display: inline-flex; align-items: center; gap: 12px; min-height: 48px; color: {TEAL}; font-size: 18px; letter-spacing: 0.03em; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 7px">Read the Guide<svg width="26" height="10" viewBox="0 0 26 10" fill="none" aria-hidden="true"><path d="M0 5h24M20 1l4 4-4 4" stroke="currentColor" stroke-width="1.1"></path></svg></span>
</div>
</a>
</div>
</section>'''

    rows = []
    for i, (tag, title, desc, href) in enumerate(GUIDES):
        num = f'{i + 1:02d}'
        inner = f'''<span class="rs-num" aria-hidden="true">{num}</span>
<span class="rs-main"><span class="rs-tag">{tag}</span><span class="rs-title{' sp-row-title' if href else ''}">{title}</span><span class="rs-desc">{desc}</span></span>
{'<span class="rs-go sp-row-arrow" aria-hidden="true"><svg width="16" height="10" viewBox="0 0 26 10" fill="none"><path d="M0 5h24M20 1l4 4-4 4" stroke="currentColor" stroke-width="1.3"></path></svg></span>' if href else '<span class="rs-soon">Coming soon</span>'}'''
        if href:
            rows.append(f'<li class="sp-reveal"><a class="rs-row sp-row" href="{href}"><span class="sp-visually-hidden">Guide {num}: </span>{inner}</a></li>')
        else:
            rows.append(f'<li class="sp-reveal"><div class="rs-row rs-row-soon"><span class="sp-visually-hidden">Guide {num}: </span>{inner}</div></li>')

    guides = f'''<!-- THE GUIDES -->
<section aria-labelledby="guides-title" style="background: #ECEEED">
<div style="{WRAP}; padding: clamp(80px, 9vw, 128px) {GUTTER}; display: flex; flex-direction: column; gap: clamp(36px, 4vw, 56px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 20px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 24px">
{label('The Guides')}
<h2 id="guides-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(40px, 4.6vw, 70px); line-height: 1.04; color: {INK}; text-wrap: balance">Five guides, <em style="font-style: italic; color: {TEAL}">one for every step</em></h2>
</div>
<p style="flex: 1 1 420px; min-width: 0; margin: 0; font-size: 19px; line-height: 1.7; color: {BODY}">Each guide answers a question that comes up before a project begins, from planning and platforms to search and ongoing care.</p>
</div>
<ol class="rs-list">
{chr(10).join(rows)}
</ol>
</div>
</section>'''

    main = '\n\n'.join([hero, feature, guides, closing])
    css = '''.sp-visually-hidden{position:absolute !important;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.rs-list{list-style:none;margin:0;padding:0;border-top:1px solid rgba(78,99,104,.35)}
.rs-list > li{border-bottom:1px solid rgba(78,99,104,.35)}
.rs-row{display:grid;grid-template-columns:72px minmax(0,1fr) auto;align-items:center;gap:12px clamp(24px,3vw,56px);padding:clamp(26px,2.8vw,40px) clamp(8px,1.5vw,24px);text-decoration:none;color:#121414}
.rs-num{font-family:'Cormorant Infant',Garamond,serif;font-style:italic;font-weight:300;font-size:clamp(36px,3.4vw,52px);line-height:1;color:#4E6368}
.rs-main{display:flex;flex-direction:column;gap:10px;min-width:0}
.rs-tag{font-size:14px;letter-spacing:.2em;text-transform:uppercase;color:#4E5558}
.rs-title{font-family:'Cormorant Infant',Garamond,serif;font-weight:400;font-size:clamp(28px,2.6vw,40px);line-height:1.15;color:#121414}
.rs-desc{font-size:18px;line-height:1.6;color:#1F2426}
.rs-go{flex:none;width:52px;height:52px;display:inline-flex;align-items:center;justify-content:center;border:1px solid #4E6368;color:#4E6368}
.rs-soon{font-size:14px;letter-spacing:.18em;text-transform:uppercase;color:#4E5558;white-space:nowrap}
.rs-row-soon .rs-title{color:#3B4042}
@media (max-width: 700px){.rs-row{grid-template-columns:minmax(0,1fr);gap:14px}.rs-go{width:44px;height:44px}.rs-soon{white-space:normal}}'''
    s = swap_head(s, 'Resources: Guides to Website Design, Branding and SEO | Sullivan Park Design',
                  'Practical guides from Sullivan Park Design to help you plan a website redesign, choose a platform, prepare your brand, get found in search and keep your site moving.')
    s = swap_main(s, main)
    s = swap_css(s, css, 'RESOURCES')
    s = set_preview(s, 4000)
    return p, s


# ---------------------------------------------------------------- GUIDE 01
SECTIONS = []  # (id, title, html)

def sec(id_, title, body):
    SECTIONS.append((id_, title))
    n = f'{len(SECTIONS):02d}'
    return f'''<section aria-labelledby="{id_}" style="display: flex; flex-direction: column; gap: 18px; padding-top: 28px">
<p aria-hidden="true" style="margin: 0; font-family: {SERIF}; font-style: italic; font-weight: 300; font-size: 56px; line-height: 1; color: {TEAL}">{n}</p>
<h2 id="{id_}" style="margin: 0; font-family: {SERIF}; font-weight: 400; font-size: clamp(32px, 3vw, 44px); line-height: 1.12; color: {INK}">{title}</h2>
{body}
</section>'''

def P(t):
    return f'<p style="margin: 0; font-size: 19px; line-height: 1.8; color: {BODY}">{t}</p>'

def ticks(items):
    lis = ''.join(f'<li style="display: flex; gap: 16px; font-size: 19px; line-height: 1.6; color: {BODY}"><span aria-hidden="true" style="flex: none; width: 18px; height: 1px; margin-top: 15px; background: {TEAL}"></span>{x}</li>' for x in items)
    return f'<ul style="list-style: none; margin: 4px 0; padding: 0; display: flex; flex-direction: column; gap: 12px">{lis}</ul>'


def guide():
    p = os.path.join(ROOT, 'Article.dc.html'); s = open(p).read()
    closing = CLOSING_RE.search(s).group(0)
    a0 = s.index('<aside class="sp-card sp-reveal" aria-label="About the author"'); a1 = s.index('</aside>', a0) + len('</aside>')
    author = s[a0:a1]
    SECTIONS.clear()

    body = []
    body.append(f'<p class="sp-dropcap" style="margin: 0; font-size: 21px; line-height: 1.8; color: {BODY}">A website redesign runs more smoothly when a few things are ready before the design work begins. You don’t need everything perfect, and you don’t need to do it alone. But the more of this you can gather, the more of our time goes into the parts that make your site stand out. Here’s what helps most, in the order I’d tackle it.</p>')
    body.append(sec('goals', 'Know what you want your website to do',
        P('Before colours and layouts, think about the job your website needs to do. More enquiries? Bookings? Online sales? Fewer emails asking the same questions? Most businesses have one main goal and a few supporting ones, and knowing them shapes every decision that follows, from the pages you need to where each button goes.') +
        P(f'It also helps to know who you most want to reach. A website for {link("Party-With-Laura.dc.html", "parents booking art classes")} needs different things than one for {link("Callum-Frost.dc.html", "agents discovering a new actor")}, even when both are simple and clean.')))
    body.append(sec('current', 'Take stock of your current site',
        P('Make a quick list of what’s working and what isn’t. Which pages do people actually use? What do customers ask you that the site should already answer? What feels out of date, or no longer reflects how you work?') +
        P(f'Those everyday questions are useful. For {link("Party-With-Laura.dc.html", "pARTy With Laura")}, common parent questions (what to wear, what to bring, whether there’s a snack break) became short, expandable answers on each program page.') +
        P('If you have Google Analytics or Search Console, note your most visited pages and the searches that bring people in. Keeping those pages at the same address, or redirecting them properly, means a redesign builds on what you already have instead of starting from zero.')))
    body.append(f'<blockquote class="sp-reveal" style="margin: 36px 0; padding: clamp(32px, 4vw, 48px) 0; border-top: 1px solid {TEAL}; border-bottom: 1px solid {TEAL}; text-align: center"><p style="margin: 0; font-family: {SERIF}; font-style: italic; font-weight: 300; font-size: clamp(30px, 3.2vw, 46px); line-height: 1.25; color: {INK}; text-wrap: balance">Start with what you want your website to do, not how you want it to look.</p></blockquote>')
    body.append(sec('content', 'Plan your pages and words',
        P('List the pages you think you need and the main thing each one should say. A home page, services, about, contact and a few examples of your work cover most small businesses, but your list might also include programs, a shop, a portfolio or FAQs.') +
        P('Gather the words you already have, even rough notes. Copy you love can stay, and anything that isn’t working can be rewritten. If writing isn’t your favourite thing, tell me. Turning notes into clear, warm copy is something I help with.')))
    body.append(sec('brand', 'Gather your brand files',
        P('Find your logo in the best quality you have. Ideally that’s a vector file (SVG, EPS or PDF) plus a PNG with a transparent background. Add your brand colours, fonts and any brand guidelines you’ve been given.') +
        P(f'If you don’t have these yet, that’s okay. A redesign is a natural time to define them, and {link("Brand-Marketing-Design.dc.html", "brand and marketing design")} is part of what I offer.')))
    body.append(f'''<figure class="sp-reveal" style="margin: 28px 0 0; position: relative; padding: 0 20px 20px 0">
<span aria-hidden="true" style="position: absolute; top: 20px; left: 20px; right: 0; bottom: 0; border: 1px solid rgba(78, 99, 104, 0.45)"></span>
<div class="sp-photo" style="position: relative"><img src="{IMG['notebook']}" alt="An open notebook of handwritten plans beside a laptop on a wooden desk" width="1080" height="720" loading="lazy" style="width: 100%; aspect-ratio: 3 / 2; object-fit: cover"></div>
</figure>''')
    body.append(sec('photos', 'Choose your photos',
        P('Photos shape how a website feels more than almost anything else. Your own photos of your work, your space and yourself build a kind of trust that stock photos can’t. Gather the best ones you have, in the largest size available.') +
        P(f'If you’re planning a photo shoot, plan it with the website in mind. Before {link("Callum-Frost.dc.html", "Callum’s")} headshot session, I gave advice on the kinds of photos I wanted for his site, so the shoot and the design worked together.') +
        P('Stock photos still have a place, especially for mood and atmosphere. Choose ones that feel like your brand rather than ones that could belong to anyone.')))
    body.append(sec('access', 'Collect your logins',
        P('Waiting on logins is one of the easiest ways for a project to stall, so it’s worth gathering access early:') +
        ticks(['Your domain, and where you bought it', 'Your current website platform', 'Google Business Profile, Search Console and Analytics',
               'Your email, if it’s connected to your domain', 'Any booking, payment or newsletter tools you use', 'The social media accounts you’d like linked']) +
        P('You don’t need to send passwords by email. Most of these tools let you add a collaborator instead, which is safer and easy to undo later.')))
    body.append(sec('features', 'List your must-have features',
        P('Think about what your website needs to do behind the scenes. Booking, online sales, gift certificates, a contact form that sorts enquiries, a newsletter sign-up or a private area for clients or families are all possible, but each one affects how the site is built.') +
        P(f'Listing them early helps choose the right platform, since {link("Website-Design.dc.html", "Squarespace, Shopify and custom-coded sites")} each handle them differently. {link("Smash.dc.html", "SMASH")}, for example, needed a portal for families, while {link("Rooster-Den.dc.html", "The Rooster Den Co")} needed a store that’s easy to shop.')))
    body.append(sec('inspiration', 'Collect a few websites you like',
        P('Find two or three websites you love, in any industry, and note what you like about each one: the colours, the photos, how easy it is to find things, how it makes you feel. Sites you don’t like are just as helpful, as long as you can say why.') +
        P('A short list of your main competitors is useful too, so your new site can stand apart from them rather than blend in.')))
    body.append(sec('timing', 'Share your timing',
        P('If your new site needs to be ready for something specific, like registration opening, a new season or a product launch, mention it at the start. It’s much easier to plan around a date we both know about.')))
    body.append(f'''<section class="sp-on-dark sp-reveal" aria-labelledby="bottom-line" style="margin-top: 36px; background: {TEAL}; padding: 12px; box-shadow: 0 30px 70px rgba(18, 28, 30, 0.18)">
<div style="border: 1px solid rgba(255, 255, 255, 0.4); padding: clamp(30px, 4vw, 52px); display: flex; flex-direction: column; gap: 20px">
<h2 id="bottom-line" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(34px, 3.2vw, 48px); line-height: 1.1; color: #FFFFFF">The bottom <em style="font-style: italic; color: #DCE4E5">line</em></h2>
<p style="margin: 0; font-size: 19px; line-height: 1.8; color: #FFFFFF">You don’t need all of this before we talk. A rough idea of your goals and a few links to sites you like is a great place to start, and we can work through the rest together. The more you gather, the more of our time can go into the parts that make your website feel like yours.</p>
<a class="sp-btn sp-btn-light" href="Contact.dc.html" style="align-self: flex-start; margin-top: 6px; display: inline-flex; align-items: center; justify-content: center; gap: 14px; min-height: 56px; padding: 0 30px; background: #FAFAF8; border: 1px solid #FAFAF8; color: {INK}; text-decoration: none; font-size: 18px; letter-spacing: 0.03em">Enquire About Your Project{ARROW}</a>
</div>
</section>''')
    body.append(author)
    body.append(f'<a class="sp-link" href="Journal.dc.html" style="align-self: flex-start; display: inline-flex; align-items: center; gap: 12px; min-height: 44px; color: {TEAL}; font-size: 17px; letter-spacing: 0.03em; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 6px">Browse All Guides{ARROW}</a>')

    # reading time from the visible article text
    words = len(re.sub(r'<[^>]+>', ' ', '\n'.join(body[:-2])).split())
    read = max(1, round(words / 220))

    toc = ''.join(f'<li style="border-bottom: 1px solid rgba(78, 99, 104, 0.3)"><a href="#{i}" style="display: flex; gap: 14px; padding: 12px 0; font-size: 16px; line-height: 1.45; color: #1F2426; text-decoration: none"><span aria-hidden="true" style="flex: none; width: 24px; font-family: {SERIF}; font-style: italic; font-size: 19px; color: {TEAL}">{n + 1:02d}</span>{t}</a></li>' for n, (i, t) in enumerate(SECTIONS))
    toc += f'<li style="border-bottom: 1px solid rgba(78, 99, 104, 0.3)"><a href="#bottom-line" style="display: flex; gap: 14px; padding: 12px 0; font-size: 16px; line-height: 1.45; color: #1F2426; text-decoration: none"><span aria-hidden="true" style="flex: none; width: 24px; font-family: {SERIF}; font-style: italic; font-size: 19px; color: {TEAL}">·</span>The bottom line</a></li>'

    takeaways = ['Start with what you want your website to do, not how you want it to look.',
                 'Note what’s working on your current site, so the redesign builds on it.',
                 'Gather your words, brand files and best photos in one place.',
                 'Collect logins for your domain, website and Google tools early.',
                 'Share a few websites you like, and say what you like about them.']
    tk = ''.join(f'<li style="display: flex; gap: 14px; font-size: 17px; line-height: 1.6; color: #1F2426"><span aria-hidden="true" style="flex: none; width: 16px; height: 1px; margin-top: 13px; background: {TEAL}"></span>{t}</li>' for t in takeaways)

    article = f'''<article aria-labelledby="page-title">

<!-- GUIDE HERO -->
<header style="position: relative; overflow: hidden; background: #FAFAF8">
<img class="sp-sway" src="/_blob/fddc24a18e2595d21f63da9f1d7bf0d5" alt="" width="1800" height="1200" style="position: absolute; top: -20px; right: -20px; width: min(1320px, 110vw); height: auto; max-width: none; opacity: 0.16; mix-blend-mode: multiply; pointer-events: none; z-index: 0">
<div style="position: relative; z-index: 1; {WRAP}; padding: clamp(140px, 12vw, 176px) {GUTTER} clamp(56px, 6vw, 88px); display: flex; flex-direction: column; gap: clamp(48px, 5vw, 72px)">
<div style="display: flex; flex-direction: column; gap: 28px; max-width: 1260px">
{label('Guide 01 · Planning')}
<h1 id="page-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(48px, 6.6vw, 108px); line-height: 1; letter-spacing: -0.015em; color: {INK}; text-wrap: balance">What to prepare before <em style="font-style: italic; color: {TEAL}">a website redesign</em></h1>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 14px 22px; font-size: 16px; letter-spacing: 0.06em; color: {MUTED}">
<span style="display: inline-flex; align-items: center; gap: 14px"><img src="/_blob/61209a65a04271cd5c18338b2938e4f1" alt="" width="1000" height="1000" style="width: 48px; height: 48px; object-fit: cover; object-position: 50% 20%; border: 1px solid rgba(78, 99, 104, 0.35); padding: 3px; background: #FFFFFF"><span>By <span style="color: {INK}">Natasha</span></span></span>
<span aria-hidden="true" style="width: 24px; height: 1px; background: rgba(78, 99, 104, 0.5)"></span>
<span>{read} min read</span>
</div>
</div>
<div style="position: relative; padding: 0 24px 24px 0">
<span aria-hidden="true" style="position: absolute; top: 24px; left: 24px; right: 0; bottom: 0; border: 1px solid rgba(78, 99, 104, 0.45)"></span>
<div class="sp-photo" style="position: relative"><img src="{IMG['hero']}" alt="An open, light-filled pavilion with a long table, looking out over a calm sea" width="1800" height="771" fetchpriority="high" style="width: 100%; aspect-ratio: 21 / 9; object-fit: cover"></div>
</div>
</div>
</header>

<!-- GUIDE BODY -->
<div style="background: #FFFFFF">
<div style="{WRAP}; padding: clamp(64px, 7vw, 104px) {GUTTER} clamp(80px, 9vw, 128px); display: flex; flex-wrap: wrap; justify-content: center; align-items: flex-start; gap: 48px clamp(40px, 5vw, 88px)">

<!-- Sticky contents -->
<nav class="sp-toc" aria-label="In this guide" style="flex: 0 0 260px; min-width: 0; position: sticky; top: 104px; display: flex; flex-direction: column; gap: 18px">
<p style="margin: 0; display: flex; align-items: center; gap: 14px; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: {TEAL}"><span aria-hidden="true" style="display: block; width: 28px; height: 1px; background: {TEAL}"></span>In This Guide</p>
<ol style="list-style: none; margin: 0; padding: 0; border-top: 1px solid rgba(78, 99, 104, 0.3)">{toc}</ol>
</nav>

<!-- Reading column -->
<div style="flex: 1 1 600px; max-width: 760px; min-width: 0; display: flex; flex-direction: column; gap: 28px">

<aside class="sp-card" aria-labelledby="takeaways-title" style="background: #FAFAF8; padding: 12px; box-shadow: 0 24px 60px rgba(18, 28, 30, 0.08); margin-bottom: 16px">
<div style="border: 1px solid rgba(78, 99, 104, 0.3); padding: clamp(26px, 3vw, 40px); display: flex; flex-direction: column; gap: 16px">
<h2 id="takeaways-title" style="margin: 0; font-family: {SERIF}; font-weight: 400; font-size: 30px; line-height: 1.15; color: {INK}">Key <em style="font-style: italic; color: {TEAL}">takeaways</em></h2>
<ul style="list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 12px">{tk}</ul>
</div>
</aside>

{chr(10).join(body)}

</div>

<div class="sp-spacer" aria-hidden="true" style="flex: 0 0 260px"></div>

</div>
</div>

</article>'''

    cards = [('Party-With-Laura.dc.html', '/_blob/' + LB['hero-desk'], 'Squarespace · Art Studio', 'pARTy With Laura', 'The pARTy With Laura homepage'),
             ('Callum-Frost.dc.html', '/_blob/' + CB['hero-desk'], 'Squarespace · Actor', 'Callum Frost', 'The Callum Frost homepage'),
             ('Smash.dc.html', '/_blob/' + SB['hero-desk'], 'Custom-coded · Performing Arts', 'SMASH Performing Arts Studio', 'The SMASH Performing Arts Studio homepage')]
    card_html = []
    for i, (href, img, tag, title, alt) in enumerate(cards):
        off = ' sp-offset' if i == 1 else ''
        mt = ' margin-top: clamp(0px, 4.5vw, 72px);' if i == 1 else ''
        card_html.append(f'''<a class="sp-reveal{off}" href="{href}" style="flex: 1 1 320px; min-width: 0;{mt} display: flex; flex-direction: column; gap: 20px; text-decoration: none; color: {INK}">
<div style="position: relative; padding: 0 16px 16px 0"><span aria-hidden="true" style="position: absolute; top: 16px; left: 16px; right: 0; bottom: 0; border: 1px solid rgba(78, 99, 104, 0.45)"></span><div class="sp-photo" style="position: relative; background: #FFFFFF"><img src="{img}" alt="{alt}" width="1800" height="1125" loading="lazy" style="width: 100%; aspect-ratio: 16 / 10; object-fit: cover; object-position: top"></div></div>
<p style="margin: 0; font-size: 15px; letter-spacing: 0.12em; text-transform: uppercase; color: {MUTED}">{tag}</p>
<h3 class="sp-more-title" style="margin: 0; font-family: {SERIF}; font-weight: 400; font-size: 30px; line-height: 1.2; color: {INK}">{title}</h3>
</a>''')
    practice = f'''<!-- SEE IT IN PRACTICE -->
<section aria-labelledby="more-title" style="background: #ECEEED">
<div style="{WRAP}; padding: clamp(80px, 9vw, 128px) {GUTTER} clamp(104px, 11vw, 160px); display: flex; flex-direction: column; gap: clamp(40px, 5vw, 64px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 24px 64px">
<div style="display: flex; flex-direction: column; gap: 20px">
{label('See It in Practice')}
<h2 id="more-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(40px, 4.6vw, 70px); line-height: 1.04; color: {INK}">Projects <em style="font-style: italic; color: {TEAL}">from this guide</em></h2>
</div>
<a class="sp-btn sp-btn-line" href="Portfolio.dc.html" style="display: inline-flex; align-items: center; justify-content: center; min-height: 54px; padding: 0 28px; border: 1px solid {TEAL}; color: {TEAL}; text-decoration: none; font-size: 17px; letter-spacing: 0.03em">View All Work</a>
</div>
<div style="display: flex; flex-wrap: wrap; align-items: flex-start; gap: 48px clamp(24px, 2.6vw, 36px)">
{chr(10).join(card_html)}
</div>
</div>
</section>'''

    main = '\n\n'.join([article, practice, closing])
    s = swap_head(s, 'What to Prepare Before a Website Redesign | Sullivan Park Design',
                  'A practical guide from Sullivan Park Design to the goals, content, photos, brand files and logins worth gathering before your website redesign begins.')
    s = swap_main(s, main)
    s = set_preview(s, 10000)
    return p, s, read


gp, gs, read = guide()
rp, rs = resources()
rs = rs.replace('{READ}', str(read))
for path, content in [(gp, gs), (rp, rs)]:
    assert '—' not in re.sub(r'<style.*?</style>', '', content.split('<main id="main">')[1].split('</main>')[0], flags=re.S), 'em dash in copy'
    assert 'bespoke' not in content.lower()
    open(path, 'w').write(content)
    print('written', os.path.basename(path), len(content))
print('read time', read)
