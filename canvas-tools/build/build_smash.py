"""SMASH Performing Arts Studio case study (Smash.dc.html)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import case_common as C

ROOT = sys.argv[1]
B = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'smash', 'blobs.json')))
def blob(k): return '/_blob/' + B[k]

NAVY, MID, GOLD, SKY, PALE, IVORY = '#22306B', '#1A2558', '#CFAE6B', '#97D9F8', '#D3E3F3', '#FAF6EF'
URL = 'smashtheatreschool.ca'
SERIF = C.SERIF
HR_SERIF = "'Cormorant Garamond', Garamond, serif"
SANS = "'Jost', 'Abel', sans-serif"
WRAP, PAD = C.WRAP, C.SECTION_PAD

glow = (f'<span style="position: absolute; top: -30%; left: 50%; width: 90%; height: 120%; transform: translateX(-50%); background: radial-gradient(closest-side, rgba(151, 217, 248, 0.16), rgba(151, 217, 248, 0) 100%)"></span>'
        f'<span style="position: absolute; bottom: -30%; right: -10%; width: 55%; height: 70%; background: radial-gradient(closest-side, rgba(207, 174, 107, 0.16), rgba(207, 174, 107, 0) 100%)"></span>')

HERO = C.hero(
    bg=NAVY, dark=True, label_text='Portfolio · Performing Arts', accent=GOLD,
    title_main='SMASH', title_em='Performing Arts Studio', em_color=SKY,
    lede='A custom-coded website for a musical theatre studio in South Surrey and White Rock, with an AI assistant for families and a members’ portal for everything between classes.',
    visit_url='https://smashtheatreschool.ca/', visit_label=URL,
    meta=[('Client', 'SMASH Performing Arts Studio'), ('Location', 'South Surrey &amp; White Rock, BC'),
          ('What I Did', 'Website design and build · AI assistant · Members’ portal · SEO · Newsletters'), ('Platform', 'Custom-coded website')],
    desk_img=blob('hero-desk'), desk_alt='The SMASH Performing Arts homepage on a desktop screen, with a scene from Matilda JR. and the headline Musical Theatre Training Where Young Performers Shine',
    phone_img=blob('hero-phone'), phone_alt='The SMASH Performing Arts homepage on a phone',
    url=URL, glow=glow, line_color='rgba(207, 174, 107, 0.55)')

BRIEF = C.brief(
    label_text='The Brief', title_main='A lot to share.', title_em='Easy to find.',
    paras=['SMASH runs full-year programs, 10-week sessions, camps, dance classes and four musicals a season, so families have a lot to keep track of.',
           'I designed and built a new custom-coded website that makes each program easy to understand and gives families clear answers, from their very first visit to show week.'],
    did=['Visual design and a custom-coded build', 'Ask SMASH, an AI assistant for families', 'A password-protected members’ portal', 'SEO, blogs, social media and newsletters'],
    num_color=GOLD, em_color='#4E6368')

SCROLL = C.scroller(
    label_text='The Homepage', title_main='A season,', title_em='in six acts',
    intro='The homepage unfolds like a show program, from the opening scene to the moment a family decides to join.',
    chapters=['The opening', 'The 2026/27 season', 'Programs and classes', 'More ways to perform', 'Curtain up', 'A place to belong'],
    numerals=['Act I', 'Act II', 'Act III', 'Act IV', 'Act V', 'Act VI'], num_color='#8C7440',
    img=blob('scroll-home'), img_w=1000, img_h=8296, url=URL,
    alt='The complete SMASH Performing Arts homepage, from the opening slideshow through the 2026/27 season, the programs, more ways to perform, photos, and the invitation to join',
    aria='The full SMASH homepage, scrolling slowly from top to bottom')

card1 = C.type_card(IVORY, f'''<p style="margin: 0; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: #8C7440">Headings · Cormorant Garamond</p>
<p aria-hidden="true" style="margin: 0; font-family: {HR_SERIF}; font-weight: 400; font-size: clamp(34px, 4vw, 64px); line-height: 1.1; letter-spacing: 0.3em; color: {NAVY}; overflow-wrap: anywhere">SMASH</p>
<p style="margin: 0; font-family: {HR_SERIF}; font-weight: 400; font-size: clamp(28px, 2.6vw, 40px); line-height: 1.2; color: {NAVY}">Musical Theatre Training Where Young Performers <em style="color: #B8964F">Shine</em></p>''')
card2 = C.type_card(NAVY, f'''<p style="margin: 0; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: {GOLD}">Navigation and text · Jost</p>
<p aria-hidden="true" style="margin: 0; font-family: {SANS}; font-weight: 400; font-size: clamp(12px, 1vw, 14px); line-height: 2; letter-spacing: 0.4em; color: {GOLD}">PERFORMING ARTS</p>
<p style="margin: 0; font-family: {SANS}; font-weight: 400; font-size: 18px; line-height: 1.75; color: rgba(255, 255, 255, 0.88)">Clear and friendly, so program details, dates and schedules are easy for families to read on any screen.</p>
<span aria-hidden="true" style="align-self: flex-start; display: inline-flex; align-items: center; min-height: 46px; padding: 0 26px; border: 1px solid {GOLD}; font-family: {SANS}; font-weight: 400; font-size: 12px; letter-spacing: 0.26em; color: #FFFFFF">REGISTER</span>''')

DETAILS = C.details(
    title_main='Midnight navy,', title_em='gold and spotlight blue',
    intro='Deep navy sets the stage, gold adds a touch of theatre and spotlight blue lights up the key words. Cormorant Garamond brings the drama to headings, and Jost keeps everything else clear and friendly.',
    swatches=[('Navy', NAVY, False), ('Gold', GOLD, False), ('Spotlight', SKY, False), ('Pale Blue', PALE, True), ('Ivory', IVORY, True)],
    card1=card1, card2=card2)

ASK = f'''<!-- ASK SMASH (AI assistant) -->
<section class="sp-on-dark" aria-labelledby="ask-title" style="position: relative; overflow: hidden; background: {MID}; color: #FFFFFF">
<div aria-hidden="true" style="position: absolute; inset: 0; pointer-events: none; background: radial-gradient(ellipse 55% 60% at 85% 20%, rgba(151, 217, 248, 0.14), rgba(151, 217, 248, 0) 70%)"></div>
<div style="position: relative; {WRAP}; {PAD}; display: flex; flex-direction: column; gap: clamp(48px, 6vw, 88px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; gap: 32px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{C.label('Ask SMASH', GOLD)}
{C.h2('ask-title', 'Answers for families,', 'any time of day', color='#FFFFFF', em_color=SKY)}
</div>
<div style="flex: 1.1 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 24px">
{C.p('Families have a lot of questions, from trial periods to show dates. Ask SMASH is an AI assistant built into the website to help them find answers about the studio and its programs, reducing the need for repetitive email enquiries.', color='rgba(255, 255, 255, 0.9)', size='20px')}
{C.p('Each answer points families to the right page or contact, so they always know where to go next.', color='rgba(255, 255, 255, 0.78)')}
</div>
</div>
<figure class="cs-loupe-stage sp-reveal" style="margin: 0">
<div class="cs-loupe-desk" style="width: 100%">{C.desk(blob('ask-desk'), 'Ask SMASH open on the SMASH website, answering a question about the STAR Collective trial period', URL, 1800, 1125, dark=True)}</div>
<div class="cs-loupe" style="padding: 10px; background: {MID}; border: 1px solid rgba(207, 174, 107, 0.6); box-shadow: 0 40px 90px rgba(5, 10, 30, 0.55)"><img src="{blob('ask-panel')}" alt="A close-up of the Ask SMASH answer explaining the two-week trial and refund for the STAR Collective" width="800" height="1240" loading="lazy" style="display: block; width: 100%; height: auto"></div>
<figcaption style="margin-top: 22px; font-size: 16px; letter-spacing: 0.04em; color: rgba(255, 255, 255, 0.72)">Asked on the site: “Is there a trial period for the STAR Collective?”</figcaption>
</figure>
</div>
</section>
'''

feature_chips = ['Show details', 'Vocal tracks', 'Dates to remember', 'Payment schedule', 'Studio policies', 'Newsletters']
chips = '\n'.join(f'<li style="display: inline-flex; align-items: center; min-height: 44px; padding: 0 20px; border: 1px solid rgba(34, 48, 107, 0.35); font-size: 16px; letter-spacing: 0.04em; color: {NAVY}">{c}</li>' for c in feature_chips)

PORTAL = f'''<!-- MEMBERS' PORTAL -->
<section aria-labelledby="portal-title" style="position: relative; overflow: hidden; background: {IVORY}">
<div style="{WRAP}; {PAD}; display: flex; flex-direction: column; gap: clamp(56px, 6vw, 96px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; gap: 32px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{C.label('Members’ Portal', '#8C7440')}
{C.h2('portal-title', 'Everything families need,', 'behind one password', em_color='#3A5198')}
</div>
<div style="flex: 1.1 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 24px">
{C.p('A password-protected portal gives families show details, vocal tracks, important dates, studio policies and newsletters in one place, organized by their performer’s level.', size='20px')}
<ul class="cs-chips">
{chips}
</ul>
</div>
</div>
<figure class="cs-portal-stage sp-reveal" style="margin: 0 0 clamp(32px, 4vw, 48px)">
<div class="cs-portal-desk" style="width: 84%; margin-left: auto">{C.desk(blob('portal-top'), 'The SMASH Parent Portal, with level tabs, the coming up card and this season’s show, Shrek The Musical JR.', URL, 1600, 1000, dark=True)}</div>
<div class="cs-portal-phone">{C.phone(blob('login-phone'), 'The SMASH Family Portal sign in screen on a phone')}</div>
</figure>
<div class="hr-pair">
<figure class="sp-reveal" style="margin: 0; display: flex; flex-direction: column; gap: 16px">
<div class="sp-device" style="box-shadow: 0 30px 70px rgba(18, 28, 60, 0.22)"><img src="{blob('portal-dates')}" alt="The Dates to remember section of the SMASH Parent Portal" width="1100" height="758" loading="lazy" style="display: block; width: 100%; height: auto"></div>
<figcaption style="font-size: 16px; letter-spacing: 0.04em; color: #4E5558">Dates to remember · each one tagged so families know what to expect</figcaption>
</figure>
<figure class="sp-reveal hr-pair-drop" style="margin: 0; display: flex; flex-direction: column; gap: 16px">
<div class="sp-device" style="box-shadow: 0 30px 70px rgba(18, 28, 60, 0.16); border: 1px solid rgba(34, 48, 107, 0.12)"><img src="{blob('portal-news')}" alt="The Newsletters section of the SMASH Parent Portal" width="1100" height="413" loading="lazy" style="display: block; width: 100%; height: auto"></div>
<figcaption style="font-size: 16px; letter-spacing: 0.04em; color: #4E5558">Newsletters · every issue kept in one place</figcaption>
</figure>
</div>
</div>
</section>
'''

pages = [('nl1', 'The cover of the SMASH October 2026 newsletter'), ('nl2', 'A newsletter page announcing the new SMASH website'),
         ('nl3', 'A newsletter page introducing the 2026/27 season'), ('nl4', 'A newsletter page listing dates to remember')]
pg = '\n'.join(f'<div style="box-shadow: 0 30px 60px -24px rgba(18, 28, 60, 0.45)"><img src="{blob(k)}" alt="{a}" width="900" height="1125" loading="lazy" style="display: block; width: 100%; height: auto"></div>' for k, a in pages)

NEWS = f'''<!-- NEWSLETTERS -->
<section aria-labelledby="news-title" style="position: relative; overflow: hidden; background: {PALE}">
<div style="{WRAP}; {PAD}; display: flex; flex-direction: column; gap: clamp(56px, 6vw, 96px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 24px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{C.label('Monthly Newsletters', NAVY)}
{C.h2('news-title', 'News that feels like', 'part of the show', color=NAVY, em_color='#1F78A8')}
</div>
<div style="flex: 1 1 420px; min-width: 0">{C.p('I design SMASH’s monthly newsletters to match the new website, so every issue feels like part of the same story, with the dates, shows and studio news families need.', color='#1A2558')}</div>
</div>
<div class="cs-pages sp-reveal">
{pg}
</div>
</div>
</section>
'''

BLOG_ITEMS = [
    ('blog-programme', 'hr-L', 'The Programme', 'Longer reads', 'Styled like a theatre programme, with the running time and venue on the cover.',
     'A SMASH blog post designed like a theatre programme, with a navy cover listing the running time and venue'),
    ('blog-poster', 'hr-S hr-drop', 'The Show Poster', 'Show announcements', 'Built around the show poster, with the dates, venue and a ticket button beside it.',
     'A SMASH show announcement for Elf The Musical JR., built around the show poster with dates, venue and a Buy Tickets button'),
    ('blog-guide', 'hr-S', 'The Class Guide', 'Programs and classes', 'Opens with an “In this guide” list of each class and its ages.',
     'A SMASH class guide introducing The STAR Collective, with a list of its classes and ages'),
    ('blog-callboard', 'hr-L hr-drop', 'The Callboard', 'Studio news', 'Pinned up like a notice on a backstage callboard.',
     'A SMASH studio news post styled like a notice pinned to a callboard, beside a pinned photo'),
]
blog_gal = '\n'.join(f"""<figure class="sp-reveal hr-gitem {cls}" style="margin: 0; display: flex; flex-direction: column; gap: 20px">
{C.desk(blob(k), alt, URL, w=1800, h=1125)}
<figcaption style="display: flex; flex-direction: column; gap: 8px">
<span style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 16px"><span style="font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: {GOLD}">{lab}</span><span style="font-family: {SERIF}; font-size: 26px; line-height: 1.2; color: #FFFFFF">{title}</span></span>
<span style="font-size: 18px; line-height: 1.6; color: {PALE}">{cap}</span>
</figcaption>
</figure>""" for k, cls, lab, title, cap, alt in BLOG_ITEMS)

BLOG = f"""<!-- BLOG TEMPLATES -->
<section class="sp-on-dark" aria-labelledby="blog-title" style="position: relative; overflow: hidden; background: {NAVY}; color: #FFFFFF">
<div aria-hidden="true" style="position: absolute; top: -20%; right: -10%; width: 60%; height: 70%; pointer-events: none; background: radial-gradient(closest-side, rgba(151, 217, 248, 0.12), rgba(151, 217, 248, 0) 100%)"></div>
<div style="position: relative; {WRAP}; {PAD}; display: flex; flex-direction: column; gap: clamp(56px, 6vw, 96px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 24px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{C.label('Blog Templates', GOLD)}
{C.h2('blog-title', 'A template for every', 'kind of post', color='#FFFFFF', em_color=SKY)}
</div>
<div style="flex: 1 1 420px; min-width: 0">{C.p('I designed four blog templates for SMASH, each shaped around a different kind of post, so a show announcement, a class guide and studio news each feel distinct while still clearly belonging to SMASH.', color='#E8EEF7')}</div>
</div>
<div class="hr-gallery">
{blog_gal}
</div>
</div>
</section>
"""

MARQUEE = C.marquee(['The Spotlight Academy', 'The STAR Collective', 'The Showstoppers', 'SMASH Dance', 'Musical Theatre Camps', 'Junior Company &amp; The Company'],
                    bg=NAVY, color=GOLD, dot_color=SKY, border='rgba(207, 174, 107, 0.3)')

GALLERY = C.gallery(
    title_main='Every program,', title_em='<span style="white-space: nowrap">its own spotlight</span>',
    intro='Each program, show and schedule has a page of its own, so families can quickly find what fits their performer.',
    url=URL, lab_color='#8C7440',
    items=[
        (blob('show-desk'), 'hr-L', 'Program Pages', 'The Showstoppers', 'Each program page leads with the show and the details families ask about first.', 'The Showstoppers program page on the SMASH website'),
        (blob('schedule-desk'), 'hr-S hr-drop', 'Class Schedule', 'Every class, by day', 'Every musical theatre and dance class in one place, with list and calendar views.', 'The SMASH class schedule page'),
        (blob('elf-desk'), 'hr-S', 'Show Pages', 'Elf The Musical JR.', 'Each show has its own page, with dates, venue and tickets.', 'The Elf The Musical JR. show page on the SMASH website'),
        (blob('company-desk'), 'hr-L hr-drop', 'Companies', 'Junior Company &amp; The Company', 'Two full-year ensembles, each with a page of its own.', 'The Junior Company and The Company page on the SMASH website'),
        (blob('blog-desk'), 'hr-L', 'The SMASH Blog', 'News and stories', 'Show announcements, studio news and stories families can share.', 'The SMASH Blog page'),
        (blob('dance-desk'), 'hr-S hr-drop', 'SMASH Dance', 'Dance classes', 'Non-competitive dance classes with their own schedule and registration.', 'The SMASH Dance page'),
    ])

PHONES = C.phones(
    title_main='Just as considered', title_em='on a phone',
    intro='Families often check schedules and show details on the go, so I designed every page to feel just as clear on a small screen.',
    items=[(blob('show-phone'), 'The Showstoppers page on a phone'), (blob('schedule-phone'), 'The SMASH class schedule on a phone'),
           (blob('blog-phone'), 'The SMASH Blog on a phone'), (blob('elf-phone'), 'The Elf The Musical JR. show page on a phone')])

QUOTE = f'''<!-- TESTIMONIAL -->
<section class="sp-on-dark" aria-label="Testimonial from Sheila R" style="position: relative; overflow: hidden; background: {NAVY}; color: #FFFFFF">
<div aria-hidden="true" style="position: absolute; top: -40%; left: 50%; width: 80%; height: 140%; transform: translateX(-50%); pointer-events: none; background: radial-gradient(closest-side, rgba(151, 217, 248, 0.14), rgba(151, 217, 248, 0) 100%)"></div>
<figure class="sp-reveal" style="position: relative; {WRAP}; padding-top: clamp(72px, 8vw, 112px); padding-bottom: clamp(72px, 8vw, 112px); margin: 0 auto; display: flex; flex-direction: column; align-items: center; gap: 24px; text-align: center">
<span aria-hidden="true" style="font-family: {SERIF}; font-size: 100px; line-height: 0.6; height: 38px; color: {GOLD}">“</span>
<blockquote style="margin: 0; max-width: 900px"><p style="margin: 0; font-family: {SERIF}; font-style: italic; font-weight: 300; font-size: clamp(21px, 1.8vw, 27px); line-height: 1.5; color: #FFFFFF; text-wrap: pretty">Natasha has design, created and maintained my website for the past year. Her work has gone above and beyond! She is fast, efficient, and full of creative ideas to help grow my business! Her creative content, whether it be design or wording, is exemplary and all my customers find it fun and exciting to navigate through! Natasha is on top of the game when it comes to SEO ranking. Highly recommend Natasha!!</p></blockquote>
<figcaption style="display: flex; flex-direction: column; align-items: center; gap: 6px; padding-top: 20px; border-top: 1px solid rgba(207, 174, 107, 0.4)"><span style="font-size: 15px; letter-spacing: 0.2em; text-transform: uppercase; color: {GOLD}">Sheila R</span><span style="font-size: 16px; color: rgba(255, 255, 255, 0.75)">Artistic Director, SMASH Performing Arts Studio</span></figcaption>
</figure>
</section>
'''

R = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'rooster', 'blobs.json')))
CF = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'callum', 'blobs.json')))
NEXT = C.next_project(href='Callum-Frost.dc.html', title='Callum Frost', sub='Custom-coded website · Copywriting · Acting resume · SEO',
                      img='/_blob/' + CF['hero-desk'], img_w=1800, img_h=1125, url='callumfrost.com')
CLOSING = C.closing('Let’s give your business', 'its spotlight')

MAIN = '\n'.join([HERO, BRIEF, SCROLL, DETAILS, ASK, PORTAL, NEWS, BLOG, GALLERY, PHONES, QUOTE, NEXT, CLOSING])

C.write_page(ROOT, 'Smash.dc.html',
             title='SMASH Performing Arts Studio: Website Case Study | Sullivan Park Design',
             desc='How I designed and built a custom-coded website for SMASH Performing Arts Studio in South Surrey and White Rock, with an AI assistant for families, a members’ portal, SEO and monthly newsletters.',
             fonts_href='https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&amp;family=Jost:wght@400;500&amp;display=swap',
             main=MAIN, extra_css='', preview_h=16720)
