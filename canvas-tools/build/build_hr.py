"""Builds the Hamish Ross Real Estate case study page (Hamish-Ross.dc.html).

Uses Website-Design.dc.html as the shell (head, shared CSS, footer, back-to-top),
swaps in the case study content and a simple component, then nav_upgrade.py adds
the shared header, footer services column, nav CSS and header logic.
"""
import re, json, sys, os

ROOT = sys.argv[1]
B = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'hr', 'blobs.json')))
def blob(k): return '/_blob/' + B[k]

SERIF = "'Cormorant Infant', Garamond, serif"
HR_SERIF = "'Cormorant Garamond', Garamond, serif"
HR_SANS = "'Jost', 'Abel', sans-serif"
INK, HARBOUR, GOLD, BRONZE, LINEN = '#12141A', '#22384A', '#C9A876', '#A0865C', '#F6F3EE'
ARROW = '<svg width="22" height="10" viewBox="0 0 26 10" fill="none" aria-hidden="true"><path d="M0 5h24M20 1l4 4-4 4" stroke="currentColor" stroke-width="1.1"></path></svg>'
EXT = '<svg width="12" height="12" viewBox="0 0 18 18" fill="none" aria-hidden="true"><path d="M5 13L13 5M6.5 5H13v6.5" stroke="currentColor" stroke-width="1.3"></path></svg>'
WRAP = 'width: 100%; max-width: 1680px; margin: 0 auto; padding-left: clamp(20px, 5vw, 72px); padding-right: clamp(20px, 5vw, 72px)'
PORTFOLIO = 'Portfolio.dc.html'
SMASH_PAGE = 'Smash.dc.html'


def label(text, color='#4E6368'):
    return (f'<p style="margin: 0; display: flex; align-items: center; gap: 16px; font-size: 15px; letter-spacing: 0.2em; '
            f'text-transform: uppercase; color: {color}"><span aria-hidden="true" style="display: block; width: 40px; height: 1px; background: {color}"></span>{text}</p>')


def h2(id_, main, em, color='#121414', em_color='#4E6368', size='clamp(42px, 4.8vw, 76px)'):
    return (f'<h2 id="{id_}" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: {size}; line-height: 1.04; '
            f'letter-spacing: -0.01em; color: {color}; text-wrap: balance">{main} <em style="font-style: italic; color: {em_color}">{em}</em></h2>')


def p(text, color='#1F2426', size='19px'):
    return f'<p style="margin: 0; font-size: {size}; line-height: 1.7; color: {color}">{text}</p>'


def desk(img, alt, w=1600, h=1000, dark=False, url='hamishross.com', extra_cls='', lazy=True, priority=False):
    chrome_bg = '#1C1F26' if dark else '#FFFFFF'
    dot = '#3A3F49' if dark else '#CDD3D2'
    txt = 'rgba(246, 243, 238, 0.6)' if dark else '#5A6163'
    border = 'rgba(246, 243, 238, 0.12)' if dark else 'rgba(18, 20, 20, 0.14)'
    load = ' fetchpriority="high"' if priority else (' loading="lazy"' if lazy else '')
    return (f'<div class="sp-device hr-desk {extra_cls}" style="background: {chrome_bg}; border: 1px solid {border}; box-shadow: 0 40px 90px rgba(10, 14, 20, 0.28)">'
            f'<div aria-hidden="true" style="height: 34px; padding: 0 16px; display: flex; align-items: center; gap: 7px; border-bottom: 1px solid {border}">'
            f'<span style="width: 9px; height: 9px; border-radius: 50%; background: {dot}"></span><span style="width: 9px; height: 9px; border-radius: 50%; background: {dot}"></span><span style="width: 9px; height: 9px; border-radius: 50%; background: {dot}"></span>'
            f'<span style="margin-left: 12px; font-size: 13px; color: {txt}">{url}</span></div>'
            f'<img src="{img}" alt="{alt}" width="{w}" height="{h}"{load} style="display: block; width: 100%; height: auto"></div>')


def phone(img, alt, extra_style=''):
    return (f'<div class="sp-device hr-phone" style="padding: 8px; background: #121414; border-radius: clamp(22px, 2.6vw, 38px); box-shadow: 0 30px 70px rgba(10, 14, 20, 0.28){extra_style}">'
            f'<img src="{img}" alt="{alt}" width="600" height="1298" loading="lazy" style="display: block; width: 100%; height: auto; border-radius: clamp(15px, 2vw, 30px)"></div>')


# ---------------------------------------------------------------- sections
HERO = f'''<!-- HERO (Hamish's world: ink, harbour blue and champagne) -->
<section class="sp-on-dark hr-hero" aria-labelledby="page-title" style="position: relative; z-index: 2; background: {INK}; color: #FFFFFF">
<div class="hr-glow" aria-hidden="true" style="position: absolute; inset: 0; overflow: hidden; pointer-events: none">
<span style="position: absolute; top: -20%; right: -10%; width: 70%; height: 90%; background: radial-gradient(closest-side, rgba(34, 56, 74, 0.95), rgba(34, 56, 74, 0) 100%)"></span>
<span style="position: absolute; bottom: -30%; left: -15%; width: 60%; height: 70%; background: radial-gradient(closest-side, rgba(160, 134, 92, 0.16), rgba(160, 134, 92, 0) 100%)"></span>
</div>
<div style="position: relative; {WRAP}; padding-top: clamp(150px, 13vw, 190px); display: flex; flex-direction: column; gap: clamp(48px, 6vw, 80px)">
<div style="display: flex; flex-wrap: wrap; align-items: flex-end; gap: 32px clamp(48px, 7vw, 120px)">
<div style="flex: 1.4 1 560px; min-width: 0; display: flex; flex-direction: column; gap: 28px">
{label('Portfolio · Real Estate', GOLD)}
<h1 id="page-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(56px, 7.6vw, 128px); line-height: 0.98; letter-spacing: -0.02em; color: #FFFFFF; text-wrap: balance">Hamish Ross <em style="font-style: italic; color: {GOLD}">Real Estate</em></h1>
</div>
<div style="flex: 1 1 380px; min-width: 0; display: flex; flex-direction: column; align-items: flex-start; gap: 26px; padding-bottom: 10px">
<p style="margin: 0; font-size: 21px; line-height: 1.65; color: rgba(246, 243, 238, 0.86)">A custom-coded website for a White Rock and South Surrey realtor, designed to feel as considered as the homes he represents.</p>
<a class="sp-ext hr-visit" href="https://www.hamishross.com/" aria-label="Visit Website, hamishross.com" style="display: inline-flex; align-items: center; gap: 10px; min-height: 44px; font-size: 16px; letter-spacing: 0.14em; text-transform: uppercase; color: {GOLD}; text-decoration: none; border-bottom: 1px solid rgba(201, 168, 118, 0.6)">Visit Website{EXT}</a>
</div>
</div>
<dl class="hr-meta" style="margin: 0; padding: 28px 0 0; border-top: 1px solid rgba(246, 243, 238, 0.16)">
<div><dt style="margin: 0 0 10px; font-size: 13px; letter-spacing: 0.2em; text-transform: uppercase; color: {GOLD}">Client</dt><dd style="margin: 0; font-size: 18px; line-height: 1.55; color: #FFFFFF">Hamish Ross, Macdonald Realty</dd></div>
<div><dt style="margin: 0 0 10px; font-size: 13px; letter-spacing: 0.2em; text-transform: uppercase; color: {GOLD}">Location</dt><dd style="margin: 0; font-size: 18px; line-height: 1.55; color: #FFFFFF">White Rock &amp; South Surrey, BC</dd></div>
<div><dt style="margin: 0 0 10px; font-size: 13px; letter-spacing: 0.2em; text-transform: uppercase; color: {GOLD}">What I Did</dt><dd style="margin: 0; font-size: 18px; line-height: 1.55; color: #FFFFFF">Website design and build · Custom IDX search · SEO · Ongoing marketing</dd></div>
<div><dt style="margin: 0 0 10px; font-size: 13px; letter-spacing: 0.2em; text-transform: uppercase; color: {GOLD}">Platform</dt><dd style="margin: 0; font-size: 18px; line-height: 1.55; color: #FFFFFF">Custom-coded website</dd></div>
</dl>
<figure class="hr-stage sp-stagebox" style="position: relative; margin: 0 0 calc(-1 * clamp(90px, 12vw, 200px)); padding: 0 0 clamp(28px, 4vw, 56px)">
<span aria-hidden="true" class="hr-frame-line" style="position: absolute; top: clamp(18px, 2.4vw, 32px); left: calc(-1 * clamp(12px, 1.6vw, 24px)); width: 86%; bottom: calc(clamp(28px, 4vw, 56px) - clamp(18px, 2.4vw, 32px)); border: 1px solid rgba(201, 168, 118, 0.55)"></span>
<div class="sp-desk" style="position: relative; width: 86%">{desk(blob('hero-desk'), 'The Hamish Ross Real Estate homepage on a desktop screen, with a modern home lit at dusk beside a pool', 1800, 1125, dark=True, lazy=False, priority=True)}</div>
<div class="sp-phone" style="position: absolute; right: 1%; bottom: 0; width: clamp(110px, 19%, 280px)">{phone(blob('hero-phone'), 'The Hamish Ross Real Estate homepage on a phone')}</div>
<figcaption class="sp-visually-hidden" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap">The Hamish Ross Real Estate website on desktop and phone</figcaption>
</figure>
</div>
</section>
'''

BRIEF = f'''<!-- THE BRIEF -->
<section aria-labelledby="brief-title" style="position: relative; z-index: 1; background: #FAFAF8">
<div class="sp-reveal" style="{WRAP}; padding-top: calc(clamp(90px, 12vw, 200px) + clamp(80px, 9vw, 140px)); padding-bottom: clamp(88px, 10vw, 136px); display: flex; flex-wrap: wrap; gap: 48px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 440px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{label('The Brief')}
{h2('brief-title', 'Big, luxurious photography.', 'Smarter ways to search.')}
</div>
<div style="flex: 1.2 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 24px">
{p('Hamish came to me wanting a website that felt slick and modern, with big, luxurious photography and a better way for his clients to search than a standard real estate site allows.', size='20px')}
{p('He specializes in family, luxury and ocean view homes, so every page needed to feel as considered as the properties he represents, while still making it easy for buyers and sellers to find what they came for.')}
<ol class="hr-did" style="list-style: none; margin: 12px 0 0; padding: 0; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0 40px">
<li style="display: flex; gap: 16px; align-items: baseline; padding: 18px 0; border-top: 1px solid rgba(18, 20, 20, 0.14)"><span style="font-family: {SERIF}; font-style: italic; font-size: 22px; color: {BRONZE}">01</span><span style="font-size: 18px; line-height: 1.55; color: #121414">Visual design and a custom-coded build</span></li>
<li style="display: flex; gap: 16px; align-items: baseline; padding: 18px 0; border-top: 1px solid rgba(18, 20, 20, 0.14)"><span style="font-family: {SERIF}; font-style: italic; font-size: 22px; color: {BRONZE}">02</span><span style="font-size: 18px; line-height: 1.55; color: #121414">Custom IDX search collections</span></li>
<li style="display: flex; gap: 16px; align-items: baseline; padding: 18px 0; border-top: 1px solid rgba(18, 20, 20, 0.14)"><span style="font-family: {SERIF}; font-style: italic; font-size: 22px; color: {BRONZE}">03</span><span style="font-size: 18px; line-height: 1.55; color: #121414">Property and market resources</span></li>
<li style="display: flex; gap: 16px; align-items: baseline; padding: 18px 0; border-top: 1px solid rgba(18, 20, 20, 0.14)"><span style="font-family: {SERIF}; font-style: italic; font-size: 22px; color: {BRONZE}">04</span><span style="font-size: 18px; line-height: 1.55; color: #121414">SEO, blogs, social media and newsletters</span></li>
</ol>
</div>
</div>
</section>
'''

CHAPTERS = ['A first impression', 'The homes he represents', 'Words from his clients', 'The monthly market report', 'Every way to search', 'The journal']
ROMAN = ['I', 'II', 'III', 'IV', 'V', 'VI']
chap_lis = '\n'.join(
    f'<li style="display: flex; align-items: baseline; gap: 18px; padding: 14px 0; border-top: 1px solid rgba(18, 20, 20, 0.12)"><span style="flex: none; width: 34px; font-family: {SERIF}; font-size: 20px; color: {BRONZE}">{r}</span><span style="font-size: 18px; line-height: 1.5; color: #121414">{c}</span></li>'
    for r, c in zip(ROMAN, CHAPTERS))

SCROLL = f'''<!-- THE HOMEPAGE, START TO FINISH (living screenshot) -->
<section aria-labelledby="scroll-title" style="position: relative; overflow: hidden; background: #ECEEED">
<div style="{WRAP}; padding-top: clamp(88px, 10vw, 136px); padding-bottom: clamp(88px, 10vw, 136px); display: flex; flex-wrap: wrap; align-items: center; gap: 56px clamp(48px, 6vw, 104px)">
<div class="sp-reveal" style="flex: 1 1 340px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{label('The Homepage')}
{h2('scroll-title', 'Start to finish,', 'like a good showing', size='clamp(40px, 4.2vw, 66px)')}
{p('The homepage unfolds in the order a buyer or seller needs it, from a striking first impression to every way to search.')}
<ol style="list-style: none; margin: 6px 0 0; padding: 0; border-bottom: 1px solid rgba(18, 20, 20, 0.12)">
{chap_lis}
</ol>
</div>
<figure class="sp-reveal hr-scrollbox" style="flex: 2 1 560px; min-width: 0; margin: 0; display: flex; flex-direction: column; gap: 16px">
<div class="sp-device" style="background: #FFFFFF; border: 1px solid rgba(18, 20, 20, 0.14); box-shadow: 0 50px 100px rgba(18, 28, 30, 0.18)">
<div aria-hidden="true" style="height: 34px; padding: 0 16px; display: flex; align-items: center; gap: 7px; border-bottom: 1px solid rgba(18, 20, 20, 0.1)"><span style="width: 9px; height: 9px; border-radius: 50%; background: #CDD3D2"></span><span style="width: 9px; height: 9px; border-radius: 50%; background: #CDD3D2"></span><span style="width: 9px; height: 9px; border-radius: 50%; background: #CDD3D2"></span><span style="margin-left: 12px; font-size: 13px; color: #5A6163">hamishross.com</span></div>
<div class="hr-view" tabindex="0" aria-label="The full Hamish Ross homepage, scrolling slowly from top to bottom">
<img src="{blob('scroll-home')}" alt="The complete Hamish Ross Real Estate homepage, from the hero image through current listings, client reviews, the market report, MLS search collections, the journal and the footer" width="1000" height="8970" loading="lazy">
</div>
</div>
<figcaption style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 8px 24px; font-size: 15px; letter-spacing: 0.04em; color: #4E5558"><span>The full homepage, scrolling on its own</span><span class="hr-hint">Hover to pause</span></figcaption>
</figure>
</div>
</section>
'''

SWATCHES = [('Ink', INK, '#FFFFFF'), ('Harbour', HARBOUR, '#FFFFFF'), ('Champagne', GOLD, INK), ('Bronze', BRONZE, '#FFFFFF'), ('Linen', LINEN, INK)]
sw = '\n'.join(
    f'<li style="display: flex; flex-direction: column; gap: 14px"><span aria-hidden="true" style="display: block; aspect-ratio: 4 / 5; background: {c}; {"border: 1px solid rgba(18, 20, 20, 0.12); " if n == "Linen" else ""}box-shadow: 0 18px 40px -24px rgba(18, 20, 20, 0.45)"></span>'
    f'<span style="display: flex; flex-direction: column; gap: 2px"><span style="font-family: {SERIF}; font-size: 24px; line-height: 1.2; color: #121414">{n}</span><span style="font-size: 15px; letter-spacing: 0.08em; color: #4E5558">{c}</span></span></li>'
    for n, c, t in SWATCHES)

IDENTITY = f'''<!-- THE DETAILS (palette and type) -->
<section aria-labelledby="details-title" style="background: #FAFAF8">
<div style="{WRAP}; padding-top: clamp(88px, 10vw, 136px); padding-bottom: clamp(88px, 10vw, 136px); display: flex; flex-direction: column; gap: clamp(48px, 5vw, 72px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 24px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{label('The Details')}
{h2('details-title', 'Ink, harbour blue', 'and champagne gold')}
</div>
<div style="flex: 1 1 420px; min-width: 0">{p('A quiet, confident palette lets the photography lead. Cormorant Garamond gives the headings an editorial elegance, and Jost keeps navigation and text clean and easy to read.')}</div>
</div>
<ul class="hr-swatches sp-reveal" style="list-style: none; margin: 0; padding: 0">
{sw}
</ul>
<div class="hr-type sp-reveal">
<div style="background: {LINEN}; padding: clamp(32px, 4vw, 56px); display: flex; flex-direction: column; justify-content: space-between; gap: 40px; min-width: 0">
<p style="margin: 0; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: {BRONZE}">Headings · Cormorant Garamond</p>
<p aria-hidden="true" class="hr-wordmark" style="margin: 0; font-family: {HR_SERIF}; font-weight: 300; font-size: clamp(30px, 3.6vw, 58px); line-height: 1.1; letter-spacing: 0.3em; color: {INK}; overflow-wrap: anywhere">HAMISH ROSS</p>
<p style="margin: 0; font-family: {HR_SERIF}; font-weight: 300; font-size: clamp(28px, 2.6vw, 40px); line-height: 1.2; color: {INK}">You deserve more than <em style="color: {BRONZE}">ordinary</em> representation.</p>
</div>
<div style="background: {INK}; padding: clamp(32px, 4vw, 56px); display: flex; flex-direction: column; justify-content: space-between; gap: 40px; min-width: 0">
<p style="margin: 0; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: {GOLD}">Navigation and text · Jost</p>
<p aria-hidden="true" style="margin: 0; font-family: {HR_SANS}; font-weight: 400; font-size: clamp(12px, 1vw, 14px); line-height: 2; letter-spacing: 0.32em; color: rgba(246, 243, 238, 0.7)">WHITE ROCK · SOUTH SURREY · OCEAN PARK · MORGAN CREEK · HAZELMERE</p>
<p style="margin: 0; font-family: {HR_SANS}; font-weight: 400; font-size: 18px; line-height: 1.75; color: rgba(246, 243, 238, 0.86)">Clear, modern and easy on the eyes, so listings, guides and market reports stay comfortable to read on any screen.</p>
<span aria-hidden="true" style="align-self: flex-start; display: inline-flex; align-items: center; min-height: 46px; padding: 0 24px; background: {GOLD}; font-family: {HR_SANS}; font-weight: 500; font-size: 11px; letter-spacing: 0.26em; color: {INK}">ASK HAMISH A QUESTION</span>
</div>
</div>
</div>
</section>
'''

COLLECTIONS = ['Ocean View Homes', 'Homes with Pools', 'Estates and Acreage', 'Penthouses']
chips = '\n'.join(f'<li style="display: inline-flex; align-items: center; min-height: 44px; padding: 0 20px; border: 1px solid rgba(201, 168, 118, 0.55); font-size: 16px; letter-spacing: 0.06em; color: #FFFFFF">{c}</li>' for c in COLLECTIONS)

IDX = f'''<!-- CUSTOM IDX -->
<section class="sp-on-dark" aria-labelledby="idx-title" style="position: relative; overflow: hidden; background: {HARBOUR}; color: #FFFFFF">
<div aria-hidden="true" style="position: absolute; inset: 0; pointer-events: none; background: radial-gradient(ellipse 60% 50% at 90% 10%, rgba(201, 168, 118, 0.14), rgba(201, 168, 118, 0) 70%)"></div>
<div style="position: relative; {WRAP}; padding-top: clamp(88px, 10vw, 136px); padding-bottom: clamp(88px, 10vw, 136px); display: flex; flex-direction: column; gap: clamp(48px, 6vw, 88px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; gap: 32px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{label('Custom IDX Search', GOLD)}
{h2('idx-title', 'Search the way', 'buyers actually think', color='#FFFFFF', em_color=GOLD)}
</div>
<div style="flex: 1.1 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 24px">
{p('Hamish wanted his website to highlight the features his clients ask about most, like pools and ocean views, in a way standard templates couldn’t.', color='rgba(246, 243, 238, 0.88)', size='20px')}
{p('I customized the IDX integration with the MLS® system so homes like these have collections of their own, updated automatically and easy to browse.', color='rgba(246, 243, 238, 0.78)')}
<div style="display: flex; flex-direction: column; gap: 14px; margin-top: 6px">
<p style="margin: 0; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: {GOLD}">Collections include</p>
<ul style="list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 10px">
{chips}
</ul>
</div>
</div>
</div>
<div class="hr-pair">
<figure class="sp-reveal" style="margin: 0; display: flex; flex-direction: column; gap: 16px">
{desk(blob('ocean-desk'), 'The Ocean View Homes collection page on the Hamish Ross website', dark=True)}
<figcaption style="font-size: 16px; letter-spacing: 0.04em; color: rgba(246, 243, 238, 0.72)">Ocean View Homes · updated live from the MLS®</figcaption>
</figure>
<figure class="sp-reveal hr-pair-drop" style="margin: 0; display: flex; flex-direction: column; gap: 16px">
{desk(blob('pools-desk'), 'The Homes with Pools collection page on the Hamish Ross website', dark=True)}
<figcaption style="font-size: 16px; letter-spacing: 0.04em; color: rgba(246, 243, 238, 0.72)">Homes with Pools · White Rock and South Surrey</figcaption>
</figure>
</div>
</div>
</section>
'''

AREAS = ['White Rock', 'South Surrey', 'Ocean Park', 'Morgan Creek', 'Hazelmere']
dot = f'<span style="display: inline-block; width: 7px; height: 7px; border-radius: 50%; background: {GOLD}; margin: 0 clamp(24px, 3vw, 48px); transform: translateY(-0.35em)"></span>'
run = ''.join(f'<span>{a}</span>{dot}' for a in AREAS)
MARQUEE = f'''<!-- AREAS (decorative ticker) -->
<div class="hr-marquee" aria-hidden="true" style="background: {LINEN}; border-top: 1px solid rgba(160, 134, 92, 0.25); border-bottom: 1px solid rgba(160, 134, 92, 0.25); padding: clamp(26px, 3vw, 40px) 0; overflow: hidden">
<div class="hr-track" style="display: inline-flex; align-items: center; white-space: nowrap; font-family: {SERIF}; font-style: italic; font-weight: 300; font-size: clamp(34px, 4vw, 64px); line-height: 1; color: {BRONZE}">{run}{run}{run}{run}</div>
</div>
'''

GALLERY_ITEMS = [
    ('listing-desk', 'hr-L', 'Listing Pages', '1087 Finlay Street', 'Each listing opens with full-width photography and the details buyers look for first.', 'A listing page on the Hamish Ross website for 1087 Finlay Street, opening with a large aerial photo of the home and the ocean'),
    ('report-desk', 'hr-S hr-drop', 'The Market Report', 'Updated monthly', 'A monthly read on White Rock and South Surrey: benchmark prices, sales ratios and what they mean.', 'The Market Report page on the Hamish Ross website'),
    ('hood-desk', 'hr-S', 'Neighbourhood Guides', 'Crescent Beach and Ocean Park', 'Each neighbourhood guide sits alongside its own live MLS® listings.', 'The Crescent Beach and Ocean Park neighbourhood guide on the Hamish Ross website'),
    ('selling-desk', 'hr-L hr-drop', 'For Sellers', 'Bringing a home to market', 'A calm, clear page for sellers, with an easy way to request an appraisal.', 'The selling page on the Hamish Ross website, with a patio overlooking the ocean'),
    ('marketing-desk', 'hr-L', 'Marketing', 'Bigger, better, bolder marketing', 'Shows sellers how their home will be marketed and presented.', 'The real estate marketing page on the Hamish Ross website'),
    ('journal-desk', 'hr-S hr-drop', 'The Journal', 'Notes from the field', 'Market updates, new listings and local stories, all in one place.', 'The Journal page on the Hamish Ross website'),
]
gal = '\n'.join(f'''<figure class="sp-reveal hr-gitem {cls}" style="margin: 0; display: flex; flex-direction: column; gap: 20px">
{desk(blob(k), alt)}
<figcaption style="display: flex; flex-direction: column; gap: 8px">
<span style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 16px"><span style="font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: {BRONZE}">{lab}</span><span style="font-family: {SERIF}; font-size: 26px; line-height: 1.2; color: #121414">{title}</span></span>
<span style="font-size: 18px; line-height: 1.6; color: #1F2426">{cap}</span>
</figcaption>
</figure>''' for k, cls, lab, title, cap, alt in GALLERY_ITEMS)

GALLERY = f'''<!-- A SAMPLE OF THE PAGES -->
<section aria-labelledby="pages-title" style="background: #FAFAF8">
<div style="{WRAP}; padding-top: clamp(88px, 10vw, 136px); padding-bottom: clamp(88px, 10vw, 136px); display: flex; flex-direction: column; gap: clamp(56px, 6vw, 88px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 24px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{label('A Sample of the Pages')}
{h2('pages-title', 'Every page,', '<span style="white-space: nowrap">its own moment</span>')}
</div>
<div style="flex: 1 1 420px; min-width: 0">{p('From listings to market reports, each page gives buyers and sellers something genuinely useful, wrapped in the same calm, luxurious design.')}</div>
</div>
<div class="hr-gallery">
{gal}
</div>
</div>
</section>
'''

PHONES = f'''<!-- ON EVERY SCREEN -->
<section aria-labelledby="phones-title" style="position: relative; overflow: hidden; background: #ECEEED">
<img class="sp-sway" src="/_blob/fddc24a18e2595d21f63da9f1d7bf0d5" alt="" width="1800" height="1200" loading="lazy" style="position: absolute; top: -40px; left: -60px; width: min(1100px, 100vw); height: auto; max-width: none; opacity: 0.12; mix-blend-mode: multiply; pointer-events: none; z-index: 0; transform-origin: 0 0">
<div style="position: relative; z-index: 1; {WRAP}; padding-top: clamp(88px, 10vw, 136px); padding-bottom: clamp(88px, 10vw, 136px); display: flex; flex-direction: column; gap: clamp(48px, 6vw, 88px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 24px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{label('On Every Screen')}
{h2('phones-title', 'Just as considered', 'on a phone')}
</div>
<div style="flex: 1 1 420px; min-width: 0">{p('Many buyers browse homes on their phones, so I designed every page to feel just as calm and easy to use on a small screen.')}</div>
</div>
<div class="hr-phones sp-reveal">
{phone(blob('listing-phone'), 'A Hamish Ross listing page on a phone')}
{phone(blob('report-phone'), 'The Hamish Ross market report on a phone')}
{phone(blob('hood-phone'), 'A Hamish Ross neighbourhood guide on a phone')}
{phone(blob('journal-phone'), 'The Hamish Ross journal on a phone')}
</div>
</div>
</section>
'''

bullet = f'<span aria-hidden="true" style="flex: none; display: block; width: 22px; height: 1px; margin-top: 15px; background: {BRONZE}"></span>'
MARKETING_ITEMS = ['Newsletters, social media and ads for each of Hamish’s listings',
                   'Marketing updates for sellers on the 1st and 15th of every month, showing the work done',
                   'SEO and blog content that keeps the website useful and easy to find']
mk = '\n'.join(f'<li style="display: flex; gap: 18px; font-size: 19px; line-height: 1.65; color: #1F2426">{bullet}<span>{t}</span></li>' for t in MARKETING_ITEMS)

MARKETING = f'''<!-- BEYOND THE LAUNCH + TESTIMONIAL -->
<section aria-labelledby="beyond-title" style="background: #FFFFFF">
<div style="{WRAP}; padding-top: clamp(88px, 10vw, 136px); padding-bottom: clamp(88px, 10vw, 136px); display: flex; flex-wrap: wrap; align-items: center; gap: 56px clamp(48px, 7vw, 120px)">
<div class="sp-reveal" style="flex: 1 1 460px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{label('Beyond the Launch')}
{h2('beyond-title', 'Marketing that', 'keeps going')}
{p('The website was only the beginning. I continue to look after the marketing for Hamish’s listings, so each home is presented with the same care online, in inboxes and on social media.')}
<ul style="list-style: none; margin: 4px 0 0; padding: 0; display: flex; flex-direction: column; gap: 12px">
{mk}
</ul>
</div>
<figure class="sp-reveal" style="flex: 1 1 480px; min-width: 0; margin: 0; position: relative; padding: 0 0 clamp(14px, 1.6vw, 22px) clamp(14px, 1.6vw, 22px)">
<span aria-hidden="true" style="position: absolute; top: clamp(14px, 1.6vw, 22px); right: clamp(14px, 1.6vw, 22px); bottom: 0; left: 0; border: 1px solid rgba(160, 134, 92, 0.5)"></span>
<div style="position: relative; background: {INK}; color: #FFFFFF; padding: clamp(30px, 3.4vw, 50px); display: flex; flex-direction: column; gap: 22px">
<span aria-hidden="true" style="font-family: {SERIF}; font-size: 88px; line-height: 0.6; height: 32px; color: {GOLD}">“</span>
<blockquote style="margin: 0"><p style="margin: 0; font-family: {SERIF}; font-style: italic; font-weight: 300; font-size: clamp(21px, 1.65vw, 25px); line-height: 1.45; color: #FFFFFF">Natasha is an amazing force of nature and she continues to impress with all of the creative work she does for us. Her website design and business savvy are of the highest caliber and I would not hesitate to choose her!</p></blockquote>
<figcaption style="display: flex; flex-direction: column; gap: 4px; padding-top: 18px; border-top: 1px solid rgba(246, 243, 238, 0.16)"><span style="font-size: 15px; letter-spacing: 0.2em; text-transform: uppercase; color: {GOLD}">Hamish R</span><span style="font-size: 16px; color: rgba(246, 243, 238, 0.72)">Macdonald Realty West Beach</span></figcaption>
</div>
</figure>
</div>
</section>
'''

NEXT = f'''<!-- NEXT PROJECT -->
<section aria-labelledby="next-title" style="background: #ECEEED">
<div style="{WRAP}; padding-top: clamp(72px, 8vw, 112px); padding-bottom: clamp(72px, 8vw, 112px)">
<a class="hr-next sp-reveal" href="{SMASH_PAGE}" style="display: flex; flex-wrap: wrap; align-items: center; gap: 40px clamp(40px, 6vw, 96px); color: #121414; text-decoration: none">
<span style="flex: 1 1 380px; min-width: 0; display: flex; flex-direction: column; gap: 22px">
<span style="display: flex; align-items: center; gap: 16px; font-size: 15px; letter-spacing: 0.2em; text-transform: uppercase; color: #4E6368"><span aria-hidden="true" style="display: block; width: 40px; height: 1px; background: #4E6368"></span>Next Project</span>
<span id="next-title" class="hr-next-title" style="font-family: {SERIF}; font-weight: 300; font-size: clamp(40px, 4.6vw, 72px); line-height: 1.04; color: #121414">SMASH Performing Arts Studio</span>
<span style="font-size: 17px; letter-spacing: 0.04em; color: #4E6368">Custom-coded website · Ongoing SEO &amp; marketing</span>
<span class="hr-next-go" style="display: inline-flex; align-items: center; gap: 14px; margin-top: 8px; font-size: 15px; letter-spacing: 0.16em; text-transform: uppercase; color: #4E6368">View Project{ARROW}</span>
</span>
<span style="flex: 1.3 1 480px; min-width: 0; display: block">
<span class="sp-device hr-next-shot" style="display: block; background: #FFFFFF; border: 1px solid rgba(18, 20, 20, 0.14); box-shadow: 0 40px 90px rgba(18, 28, 30, 0.16)"><span aria-hidden="true" style="height: 34px; padding: 0 16px; display: flex; align-items: center; gap: 7px; border-bottom: 1px solid rgba(18, 20, 20, 0.1)"><span style="width: 9px; height: 9px; border-radius: 50%; background: #CDD3D2"></span><span style="width: 9px; height: 9px; border-radius: 50%; background: #CDD3D2"></span><span style="width: 9px; height: 9px; border-radius: 50%; background: #CDD3D2"></span><span style="margin-left: 12px; font-size: 13px; color: #5A6163">smashtheatreschool.ca</span></span><img src="/_blob/dd8f707bf480ddbc8b5a593bf32382ff" alt="" width="1600" height="1000" loading="lazy" style="display: block; width: 100%; height: auto"></span>
</span>
</a>
<p class="sp-reveal" style="margin: clamp(40px, 5vw, 64px) 0 0; padding-top: 24px; border-top: 1px solid rgba(18, 20, 20, 0.14)"><a class="sp-link" href="{PORTFOLIO}" style="display: inline-flex; align-items: center; gap: 12px; min-height: 44px; font-size: 15px; letter-spacing: 0.16em; text-transform: uppercase; color: #4E6368; text-decoration: none">Back to All Projects{ARROW}</a></p>
</div>
</section>
'''

CLOSING = f'''<!-- CLOSING -->
<section aria-labelledby="cta-title" style="position: relative; overflow: hidden; background: #FAFAF8">
<div aria-hidden="true" style="position: absolute; left: -40px; bottom: -40px; width: min(1000px, 100vw); transform: rotate(180deg); pointer-events: none; z-index: 0">
<img src="/_blob/fddc24a18e2595d21f63da9f1d7bf0d5" alt="" width="1800" height="1200" loading="lazy" style="width: 100%; height: auto; opacity: 0.12; mix-blend-mode: multiply">
</div>
<div class="sp-reveal" style="position: relative; z-index: 1; {WRAP}; padding-top: clamp(88px, 10vw, 136px); padding-bottom: clamp(88px, 10vw, 136px); display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 36px clamp(48px, 7vw, 120px)">
<div style="flex: 1.4 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 24px">
{label('Get in Touch')}
<h2 id="cta-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(42px, 5vw, 76px); line-height: 1.02; color: #121414; text-wrap: balance">Let’s create something <em style="font-style: italic; color: #4E6368">this considered for you</em></h2>
<p style="margin: 0; font-size: 20px; line-height: 1.7; color: #1F2426">Tell me about your business and what you’d like your website to do.</p>
</div>
<div style="flex: 0 1 auto; min-width: 0; display: flex; flex-direction: column; align-items: flex-start; gap: 18px">
<a class="sp-btn sp-btn-blue" href="Contact.dc.html" style="display: inline-flex; align-items: center; justify-content: center; gap: 14px; min-height: 58px; padding: 0 34px; background: #4E6368; border: 1px solid #4E6368; color: #FFFFFF; text-decoration: none; font-size: 18px; letter-spacing: 0.03em">Enquire About Your Project{ARROW}</a>
<p style="margin: 0; font-size: 17px; line-height: 1.6; color: #1F2426">Or email me at <a href="mailto:info@sullivanparkdesign.com" style="color: #4E6368; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 5px">info@sullivanparkdesign.com</a>.</p>
</div>
</div>
</section>
'''

MAIN = '\n'.join([HERO, BRIEF, SCROLL, IDENTITY, IDX, GALLERY, PHONES, MARKETING, NEXT, CLOSING])

CSS = '''/* HAMISH ROSS CASE STUDY */
.hr-meta{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px 32px}
@media (max-width: 1000px){.hr-meta{grid-template-columns:1fr 1fr}}
@media (max-width: 520px){.hr-meta{grid-template-columns:1fr}}
.hr-stage .sp-desk,.hr-stage .sp-phone{transition:transform .9s cubic-bezier(.2,.7,.2,1)}
.hr-stage:hover .sp-desk{transform:translateY(-6px)}
.hr-stage:hover .sp-phone{transform:translateY(-14px)}
@media (max-width: 760px){.hr-stage .sp-desk{width:90% !important}.hr-frame-line{width:90% !important}.hr-stage .sp-phone{width:30% !important}}
@media (max-width: 640px){.hr-did{grid-template-columns:1fr !important}}
.hr-view{position:relative;aspect-ratio:16 / 10;overflow:hidden;container-type:inline-size;background:#F6F3EE}
.hr-view img{position:absolute;top:0;left:0;display:block;width:100%;height:auto;max-width:none}
@keyframes hrScroll{0%,5%{translate:0 0}95%,100%{translate:0 calc(-100% + 62.5cqw)}}
@media (prefers-reduced-motion: no-preference){.hr-view img{animation:hrScroll 110s ease-in-out -24s infinite alternate}.hr-scrollbox:hover .hr-view img,.hr-view:focus-visible img{animation-play-state:paused}}
@media (prefers-reduced-motion: reduce){.hr-view{overflow-y:auto}.hr-view img{position:static}.hr-hint{display:none}}
@media (hover: none){.hr-hint{display:none}}
.hr-swatches{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:clamp(14px,2vw,28px)}
@media (max-width: 760px){.hr-swatches{grid-template-columns:repeat(3,minmax(0,1fr))}}
.hr-type{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:clamp(14px,2vw,28px)}
@media (max-width: 860px){.hr-type{grid-template-columns:1fr}}
.hr-pair{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:clamp(24px,3vw,48px);align-items:start}
.hr-pair-drop{margin-top:clamp(40px,7vw,120px)}
@media (max-width: 760px){.hr-pair{grid-template-columns:1fr}.hr-pair-drop{margin-top:0}}
.hr-marquee .hr-track{animation:hrMarquee 70s linear infinite}
@keyframes hrMarquee{to{transform:translateX(-50%)}}
@media (prefers-reduced-motion: reduce){.hr-marquee .hr-track{animation:none}}
.hr-gallery{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:clamp(56px,6vw,96px) clamp(24px,3vw,56px);align-items:start}
.hr-L{grid-column:span 7}
.hr-S{grid-column:span 5}
.hr-drop{margin-top:clamp(40px,8vw,140px)}
@media (max-width: 860px){.hr-L,.hr-S{grid-column:1 / -1}.hr-drop{margin-top:0}}
.hr-gitem .sp-device{transition:transform .7s cubic-bezier(.2,.7,.2,1),box-shadow .7s}
.hr-gitem:hover .sp-device{transform:translateY(-6px)}
.hr-phones{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:clamp(16px,3vw,48px);align-items:start}
.hr-phones > :nth-child(even){margin-top:clamp(0px,6vw,96px)}
@media (max-width: 760px){.hr-phones{grid-template-columns:1fr 1fr}.hr-phones > :nth-child(even){margin-top:44px}}
.hr-phones .sp-device{transition:transform .8s cubic-bezier(.2,.7,.2,1)}
.hr-phones .sp-device:hover{transform:translateY(-10px)}
.hr-visit svg,.hr-next-go svg{transition:transform .35s cubic-bezier(.2,.7,.2,1)}
.hr-visit:hover{color:#FFFFFF !important;border-color:#FFFFFF !important}
.hr-visit:hover svg{transform:translate(2px,-2px)}
.hr-next-title{transition:color .3s}
.hr-next:hover .hr-next-title{color:#4E6368 !important}
.hr-next:hover .hr-next-go svg{transform:translateX(6px)}
.hr-next-shot{transition:transform .7s cubic-bezier(.2,.7,.2,1)}
.hr-next:hover .hr-next-shot{transform:translateY(-6px)}
@media (prefers-reduced-motion: reduce){.hr-stage .sp-desk,.hr-stage .sp-phone,.hr-gitem .sp-device,.hr-phones .sp-device,.hr-next-shot{transition:none !important;transform:none !important}}
/* /HAMISH ROSS CASE STUDY */'''

COMPONENT = '''class Component extends DCLogic {
  renderVals() {
    const s = this.state || {};
    const menuOpen = !!s.menuOpen;
    return {
      menuOpen: menuOpen,
      menuExpanded: menuOpen ? 'true' : 'false',
      toggleMenu: () => this.setState({ menuOpen: !menuOpen }),
      closeMenu: () => this.setState({ menuOpen: false })
    };
  }
}
'''

TITLE = 'Hamish Ross Real Estate: Website Case Study | Sullivan Park Design'
DESC = 'How I designed and built a custom-coded luxury real estate website for Hamish Ross in White Rock and South Surrey, with custom IDX search collections, SEO and ongoing marketing.'


def main():
    s = open(os.path.join(ROOT, 'Website-Design.dc.html')).read()
    # head
    s = re.sub(r'<title>.*?</title>', f'<title>{TITLE}</title>', s, count=1)
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{DESC}">', s, count=1)
    s = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{TITLE}">', s, count=1)
    s = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{DESC}">', s, count=1)
    # fonts for the type specimens
    fonts = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300&amp;family=Jost:wght@400;500&amp;display=swap">'
    s = s.replace('<helmet>\n', '<helmet>\n' + fonts + '\n', 1)
    # css: keep shared base, drop generated nav block (re-added by nav_upgrade) and add page css
    st0 = s.index('<style>') + len('<style>'); st1 = s.index('</style>')
    base = s[st0:st1]
    base = re.sub(r'/\* NAV v2 \(generated\) \*/.*?/\* /NAV v2 \*/\n?', '', base, flags=re.S)
    s = s[:st0] + base.rstrip('\n') + '\n' + CSS + '\n' + s[st1:]
    # main content
    m0 = s.index('<main id="main">') + len('<main id="main">'); m1 = s.index('</main>')
    s = s[:m0] + '\n\n' + MAIN + '\n' + s[m1:]
    # component
    c0 = s.index('class Component extends DCLogic {'); c1 = s.rindex('</script>')
    s = s[:c0] + COMPONENT + s[c1:]
    s = re.sub(r'"\$preview":\{"width":1440,"height":\d+\}', '"$preview":{"width":1440,"height":12300}', s, count=1)
    # footer: nothing is current here
    s = s.replace('aria-current="page" ', '')
    open(os.path.join(ROOT, 'Hamish-Ross.dc.html'), 'w').write(s)
    print('written', len(s))


if __name__ == '__main__':
    main()
