"""Callum Frost case study (Callum-Frost.dc.html): his custom-coded 2.0 site (first built on Squarespace; that version is build_callum.squarespace.py)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import case_common as C

ROOT = sys.argv[1]
HERE = os.path.dirname(__file__)
B = json.load(open(os.path.join(HERE, '..', 'callum', 'blobs.json')))
L = json.load(open(os.path.join(HERE, '..', 'laura', 'blobs.json')))
def blob(k): return '/_blob/' + B[k]

INK, BLACK, CHAR, SILVER, MIST = '#141414', '#1C1C1C', '#5A5A5A', '#DCDCDC', '#F8F8F8'
MONO = "'Roboto Mono', ui-monospace, monospace"
NEW_SITE = 'https://sullivanparkdesign.github.io/callumfrost/'  # switch to https://www.callumfrost.com/ once the domain points at 2.0
SOFT = '#BDBDBD'      # light grey for accents on black
GREY_TXT = '#4D4D4D'  # grey deep enough for small text on light backgrounds
URL = 'callumfrost.com'
SERIF = C.SERIF
ROBOTO = "'Roboto', 'Abel', sans-serif"
WRAP, PAD = C.WRAP, C.SECTION_PAD

glow = (f'<span style="position: absolute; top: -30%; right: -12%; width: 70%; height: 90%; background: radial-gradient(closest-side, rgba(255, 255, 255, 0.09), rgba(255, 255, 255, 0) 100%)"></span>'
        f'<span style="position: absolute; bottom: -35%; left: -15%; width: 60%; height: 70%; background: radial-gradient(closest-side, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0) 100%)"></span>')

HERO = C.hero(
    bg=INK, dark=True, label_text='Portfolio · Actor', accent=SOFT,
    title_main='Callum', title_em='Frost', em_color=SOFT,
    lede='A classic black and white website for a Vancouver actor and voice-over artist, rebuilt from Squarespace in custom code, with film-inspired details that let his headshots take the lead.',
    visit_url=NEW_SITE, visit_label='the new Callum Frost website',
    meta=[('Client', 'Callum Frost'), ('Location', 'Vancouver, BC'),
          ('What I Did', 'Website design · Copywriting · Acting resume · SEO'), ('Platform', 'Custom code')],
    desk_img=blob('hero-desk'), desk_alt='The Callum Frost homepage on a desktop screen, opening with a full-width black and white headshot',
    phone_img=blob('hero-phone'), phone_alt='The Callum Frost homepage on a phone',
    url=URL, glow=glow, line_color='rgba(255, 255, 255, 0.3)')

BRIEF = C.brief(
    label_text='The Story', title_main='Classy, simple', title_em='and all about him',
    paras=['When Callum was starting out as an actor, his family asked me to build him a website. At the time, the goal was to give agents a polished, professional place to see his work.',
           'We talked it through together. Callum wanted something classy and simple, so we chose black and white and let his headshots do the talking. He now has an agent.',
           'His first site was built on Squarespace. As his career grew, I rebuilt it in custom code, keeping the look he loves and adding more polish to every page.'],
    did=['Website design, now custom-coded', 'Headshot direction', 'His acting resume and all the copy', 'SEO, domain and ongoing updates'],
    num_color=CHAR, em_color=CHAR)

upgrades = [
    ('Film-inspired details', 'A running timecode on the homepage, film-strip frames around his photos and a soft film reel shadow.'),
    ('A photo viewer', 'Every photo opens larger, with arrows, thumbnails and keyboard controls for browsing.'),
    ('A gallery for each show', 'His theatre productions each have their own gallery, alongside his headshots and film and TV photos.'),
    ('A resume to share', 'Visitors can download or print his resume right from the page.'),
]
up_html = '\n'.join(f'''<li style="display: flex; flex-direction: column; gap: 12px; padding-top: 22px; border-top: 1px solid rgba(20, 20, 20, 0.22)">
<span style="font-family: {MONO}; font-size: 14px; letter-spacing: 0.14em; color: {GREY_TXT}">f.{i + 1:02d}</span>
<span style="font-family: {SERIF}; font-size: clamp(24px, 2vw, 30px); line-height: 1.15; color: #121414">{t}</span>
<span style="font-size: 17px; line-height: 1.65; color: #1F2426">{d}</span>
</li>''' for i, (t, d) in enumerate(upgrades))
UPGRADE = f'''<!-- VERSION 2.0 -->
<section aria-labelledby="v2-title" style="background: {MIST}">
<div style="{WRAP}; {PAD}; display: flex; flex-direction: column; gap: clamp(56px, 6vw, 96px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 24px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{C.label('Version 2.0', CHAR)}
{C.h2('v2-title', 'Everything he loved,', 'with more polish', em_color=CHAR)}
</div>
<div style="flex: 1 1 420px; min-width: 0">{C.p('Callum loved his original site, so the new version keeps the same pages, colours, photos and style. Rebuilding it in custom code let me add film-inspired details and a few useful new features.')}</div>
</div>
<ol class="cf-extras sp-reveal">
{up_html}
</ol>
</div>
</section>
'''

SCROLL = C.scroller(
    label_text='The Homepage', title_main='One look,', title_em='then straight to the work',
    intro='The homepage opens on a full-width black and white headshot with a running timecode, then leads visitors to everything an agent or casting director needs.',
    chapters=['A full-width opening headshot', 'Vancouver based actor and voice-over artist', 'On the rise: resume, portfolio and media', 'Every page one click away'],
    numerals=['I', 'II', 'III', 'IV'], num_color=CHAR,
    img=blob('scroll-home'), img_w=1000, img_h=3548, url=URL, duration='60s',
    alt='The complete Callum Frost homepage, from the opening headshot through his introduction and links to his resume, portfolio and media',
    aria='The full Callum Frost homepage, scrolling slowly from top to bottom')

card1 = C.type_card(MIST, f'''<p style="margin: 0; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: {GREY_TXT}">Headings · Roboto</p>
<p aria-hidden="true" style="margin: 0; font-family: {ROBOTO}; font-weight: 400; font-size: clamp(44px, 5vw, 80px); line-height: 1; letter-spacing: -0.035em; color: {CHAR}">callum frost.</p>
<p style="margin: 0; font-family: {ROBOTO}; font-weight: 400; font-size: clamp(24px, 2.2vw, 34px); line-height: 1.2; letter-spacing: -0.02em; color: {CHAR}">on the rise…</p>''')
card2 = C.type_card(CHAR, f'''<p style="margin: 0; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: #FFFFFF">Labels · Roboto Mono</p>
<p aria-hidden="true" style="margin: 0; display: flex; align-items: center; gap: 12px; font-family: {MONO}; font-size: 15px; letter-spacing: 0.14em; color: #FFFFFF"><span style="width: 9px; height: 9px; border-radius: 50%; background: #E5484D"></span>rec</p>
<p aria-hidden="true" style="margin: 0; font-family: {MONO}; font-weight: 400; font-size: clamp(30px, 3vw, 46px); line-height: 1.1; letter-spacing: 0.04em; color: #FFFFFF">00:12:34:22</p>
<p style="margin: 0; font-family: {ROBOTO}; font-weight: 300; font-size: 18px; line-height: 1.75; color: rgba(255, 255, 255, 0.92)">Small monospaced labels, like the timecode on his homepage and the frame numbers on his photos, give the site its film-set feel.</p>
<span aria-hidden="true" style="align-self: flex-start; display: inline-flex; align-items: center; min-height: 46px; padding: 0 26px; background: {SILVER}; font-family: {MONO}; font-weight: 400; font-size: 14px; letter-spacing: 0.1em; color: {BLACK}">f.01 · headshots.</span>''')

DETAILS = C.details(
    title_main='Black and white,', title_em='nothing to distract',
    intro='A quiet palette of charcoal, grey and silver keeps every page calm and classic, so the focus stays on Callum, with a small red “rec” light on the homepage. Lowercase headings in Roboto feel modern and understated, and Roboto Mono adds the film details.',
    swatches=[('Black', BLACK, False), ('Charcoal', CHAR, False), ('Grey', '#767676', False), ('Silver', SILVER, True), ('Mist', MIST, True)],
    card1=card1, card2=card2)

extras = [
    ('Headshot direction', 'Before his headshot session, I gave advice on the kinds of photos I wanted for the site, so the shoot and the design worked together.'),
    ('Resume and copy', 'I built his acting resume and wrote all the copy on the site.'),
    ('Ongoing updates', 'I look after the site for him. When he has new photos or resume changes, I add them.'),
    ('SEO and domain', 'I set up the SEO, helped him buy his domain and was there with advice along the way.'),
]
ex_html = '\n'.join(f'''<li style="display: flex; flex-direction: column; gap: 12px; padding-top: 22px; border-top: 1px solid rgba(255, 255, 255, 0.22)">
<span style="font-family: {SERIF}; font-style: italic; font-size: 22px; color: {SOFT}">{i + 1:02d}</span>
<span style="font-family: {SERIF}; font-size: clamp(24px, 2vw, 30px); line-height: 1.15; color: #FFFFFF">{t}</span>
<span style="font-size: 17px; line-height: 1.65; color: rgba(255, 255, 255, 0.84)">{d}</span>
</li>''' for i, (t, d) in enumerate(extras))

def shot(img, cls, lab, title, cap, alt):
    return f'''<figure class="sp-reveal hr-gitem {cls}" style="margin: 0; display: flex; flex-direction: column; gap: 20px">
{C.desk(img, alt, URL, dark=True)}
<figcaption style="display: flex; flex-direction: column; gap: 8px">
<span style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 16px"><span style="font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: {SOFT}">{lab}</span><span style="font-family: {SERIF}; font-size: 26px; line-height: 1.2; color: #FFFFFF">{title}</span></span>
<span style="font-size: 18px; line-height: 1.6; color: rgba(255, 255, 255, 0.84)">{cap}</span>
</figcaption>
</figure>'''

EXTRAS = f'''<!-- MORE THAN A WEBSITE -->
<section class="sp-on-dark" aria-labelledby="extras-title" style="position: relative; overflow: hidden; background: {INK}; color: #FFFFFF">
<div aria-hidden="true" style="position: absolute; inset: 0; pointer-events: none; background: radial-gradient(ellipse 55% 50% at 100% 0%, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0) 70%)"></div>
<div style="position: relative; {WRAP}; {PAD}; display: flex; flex-direction: column; gap: clamp(56px, 6vw, 96px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 24px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{C.label('Behind the Scenes', SOFT)}
{C.h2('extras-title', 'More than', 'a website', color='#FFFFFF', em_color=SOFT)}
</div>
<div style="flex: 1 1 420px; min-width: 0">{C.p('An actor’s website is only as good as the photos and resume behind it, so I helped with those too, and I still keep everything up to date.', color='rgba(255, 255, 255, 0.86)')}</div>
</div>
<ol class="cf-extras sp-reveal">
{ex_html}
</ol>
<div class="hr-gallery">
{shot(blob('resume-desk'), 'hr-L', 'Resume', 'Theatre, training and more', 'His resume page sits beside a collage of photos, with a one-page resume visitors can download or print.', 'The Resume page on the Callum Frost website, with a photo collage and his acting resume')}
{shot(blob('gallery-desk'), 'hr-S hr-drop', 'Gallery', 'Headshots, screen and stage', 'Each gallery frames his photos like film stills, and every photo opens larger in a viewer.', 'The Gallery page on the Callum Frost website, with three black and white photos in film-strip frames')}
</div>
</div>
</section>
'''

PHONES = C.phones(
    title_main='Ready for', title_em='a quick look',
    intro='Agents and casting directors often check a site on their phones, so every page is just as clean and easy to browse on a small screen.',
    items=[(blob('about-phone'), 'The About page on a phone'), (blob('resume-phone'), 'The Resume page on a phone'),
           (blob('gallery-phone'), 'The Gallery page on a phone'), (blob('media-phone'), 'The Media page on a phone')])

QUOTE = f'''<!-- TESTIMONIAL (Callum's family, word for word) -->
<section aria-label="Testimonial from Callum’s family" style="background: #FFFFFF">
<figure class="sp-reveal" style="{WRAP}; padding-top: clamp(72px, 8vw, 112px); padding-bottom: clamp(72px, 8vw, 112px); margin: 0 auto; display: flex; flex-direction: column; align-items: center; gap: 24px; text-align: center">
<span aria-hidden="true" style="font-family: {SERIF}; font-size: 100px; line-height: 0.6; height: 38px; color: {CHAR}">“</span>
<blockquote style="margin: 0; max-width: 900px; display: flex; flex-direction: column; gap: 18px; font-family: {SERIF}; font-style: italic; font-weight: 300; font-size: clamp(20px, 1.6vw, 25px); line-height: 1.55; color: #121414; text-wrap: pretty">
<p style="margin: 0">I honestly can’t recommend Natasha enough! She designed a beautiful website for my son, Callum, and we couldn’t be happier with how it turned out.</p>
<p style="margin: 0">Natasha is incredibly talented, creative, and has such a great eye for detail. She really took the time to understand what we wanted and brought it all together beautifully. You can tell she genuinely cares about her work and takes pride in getting everything just right.</p>
<p style="margin: 0">The whole experience was a pleasure, and the finished website was even better than we imagined. We’re so grateful for all the time, care, and effort she put into it.</p>
<p style="margin: 0">Thank you, Natasha, for doing such a wonderful job for Callum. We absolutely love it and wouldn’t hesitate to recommend you to anyone!</p>
</blockquote>
<figcaption style="display: flex; flex-direction: column; align-items: center; gap: 6px; padding-top: 20px; border-top: 1px solid {SILVER}"><span style="font-size: 15px; letter-spacing: 0.2em; text-transform: uppercase; color: {INK}">Callum’s family</span><span style="font-size: 16px; color: {GREY_TXT}">Custom-coded actor website</span></figcaption>
</figure>
</section>
'''

NEXT = C.next_project(href='Party-With-Laura.dc.html', title='pARTy With Laura', sub='Squarespace website · Copywriting · SEO',
                      img='/_blob/' + L['hero-desk'], img_w=1800, img_h=1125, url='partywithlaura.com')
CLOSING = C.closing('Let’s make your first impression', 'count')

ACTOR_BAND = f'''<!-- ACTOR WEBSITES -->
<section aria-labelledby="actor-band-title" style="background: #141414; color: #FFFFFF">
<div class="sp-reveal" style="{WRAP}; padding-top: clamp(64px, 7vw, 96px); padding-bottom: clamp(64px, 7vw, 96px); display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 32px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 560px; min-width: 0; display: flex; flex-direction: column; gap: 20px">
{C.label('For Actors', '#BDBDBD')}
<h2 id="actor-band-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(36px, 3.6vw, 56px); line-height: 1.06; color: #FFFFFF; text-wrap: balance">Want a website like <em style="font-style: italic; color: #BDBDBD">Callum’s?</em></h2>
<p style="margin: 0; font-size: 19px; line-height: 1.7; color: rgba(255, 255, 255, 0.86)">I also offer ready-made actor websites in three polished looks, with your own edit screen for headshots, credits and bio. They start at $650 + tax, with your first year of care included.</p>
</div>
<a class="sp-btn" href="Actor-Websites.dc.html" style="flex: none; display: inline-flex; align-items: center; justify-content: center; gap: 14px; min-height: 56px; padding: 0 30px; background: #FFFFFF; border: 1px solid #FFFFFF; color: #141414; text-decoration: none; font-size: 18px; letter-spacing: 0.03em">See Actor Websites{C.ARROW}</a>
</div>
</section>'''

MAIN = '\n'.join([HERO, BRIEF, UPGRADE, SCROLL, DETAILS, EXTRAS, PHONES, ACTOR_BAND, QUOTE, NEXT, CLOSING])

EXTRA = '''/* CALLUM FROST */
.cf-extras{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:40px clamp(24px,3vw,48px)}
@media (max-width: 960px){.cf-extras{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width: 560px){.cf-extras{grid-template-columns:minmax(0,1fr);gap:28px}}
/* /CALLUM FROST */'''

C.write_page(ROOT, 'Callum-Frost.dc.html',
             title='Callum Frost: Actor Website Case Study | Sullivan Park Design',
             desc='How I designed a classic black and white website for Vancouver actor Callum Frost, first on Squarespace and now custom-coded, with headshot direction, his acting resume, all the copy, SEO and ongoing updates.',
             fonts_href='https://fonts.googleapis.com/css2?family=Roboto:wght@300;400&amp;family=Roboto+Mono:wght@400&amp;display=swap',
             main=MAIN, extra_css=EXTRA, preview_h=10280)
