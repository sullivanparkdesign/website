"""pARTy With Laura case study (Party-With-Laura.dc.html). A shorter page than the custom-coded ones."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import case_common as C

ROOT = sys.argv[1]
HERE = os.path.dirname(__file__)
B = json.load(open(os.path.join(HERE, '..', 'laura', 'blobs.json')))
R = json.load(open(os.path.join(HERE, '..', 'rooster', 'blobs.json')))
def blob(k): return '/_blob/' + B[k]

DEEP, DEEP_DARK, TEAL, MIST, FOAM, BLUSH, PINK = '#066680', '#04495C', '#9FD0D4', '#DCEEEE', '#F6FBFB', '#FEF4F4', '#F9CFCF'
URL = 'partywithlaura.com'
SERIF = C.SERIF
GAEGU = "'Gaegu', 'Cormorant Infant', cursive"
SANS = "'Source Sans 3', 'Abel', sans-serif"
WRAP, PAD = C.WRAP, C.SECTION_PAD

glow = (f'<span style="position: absolute; top: -25%; right: -10%; width: 70%; height: 90%; background: radial-gradient(closest-side, rgba(159, 208, 212, 0.45), rgba(159, 208, 212, 0) 100%)"></span>'
        f'<span style="position: absolute; bottom: -30%; left: -15%; width: 60%; height: 70%; background: radial-gradient(closest-side, rgba(249, 207, 207, 0.55), rgba(249, 207, 207, 0) 100%)"></span>')

HERO = C.hero(
    bg=BLUSH, dark=False, label_text='Portfolio · Art Studio', accent=DEEP,
    title_main='pARTy With', title_em='Laura', em_color=DEEP,
    lede='A bright, playful Squarespace website for a Cloverdale art studio, bringing weekly classes, paint parties, workshops and summer camps together in one welcoming place.',
    visit_url='https://www.partywithlaura.com/', visit_label=URL,
    meta=[('Client', 'pARTy With Laura'), ('Location', 'Cloverdale, BC'),
          ('What I Did', 'Website design · Copywriting · SEO'), ('Platform', 'Squarespace')],
    desk_img=blob('hero-desk'), desk_alt='The pARTy With Laura homepage on a desktop screen, with the headline Art Classes, Camps and Painting Parties in Cloverdale and Beyond and a photo of Laura with her paintings',
    phone_img=blob('hero-phone'), phone_alt='The pARTy With Laura homepage on a phone',
    url=URL, glow=glow, line_color='rgba(6, 102, 128, 0.35)')

BRIEF = C.brief(
    label_text='The Story', title_main='Four ways to create.', title_em='One place to start.',
    paras=['Laura Webb is a certified Bob Ross landscape and floral instructor with more than 15 years of teaching experience. From her home studio in Cloverdale, she runs weekly classes, paint parties, workshops and summer camps, and brings the studio to homes, offices and community events across the Fraser Valley.',
           'Her business was already well established. What she needed was a website that felt as inspiring as her classes, explained each program clearly, made booking simple and helped local families find her.'],
    did=['Website design, built from scratch', 'Copywriting for every page', 'SEO and local search', 'Booking, enquiries and gift certificates'],
    num_color=DEEP, em_color=DEEP)

SCROLL = C.scroller(
    label_text='The Homepage', title_main='Bright, welcoming', title_em='and easy to follow',
    intro='The homepage introduces Laura, shows every program at a glance and always makes the next step clear.',
    chapters=['Art classes, camps and painting parties in Cloverdale and beyond', 'Welcome. Discover your inner artist', 'Creative art experiences for all ages', 'A welcoming home studio', 'Ready for your next creative adventure?'],
    numerals=['I', 'II', 'III', 'IV', 'V'], num_color=DEEP,
    img=blob('scroll-home'), img_w=1000, img_h=1951, url=URL, duration='40s',
    alt='The complete pARTy With Laura homepage, from the welcome banner and Laura’s introduction through the four programs, the home studio and the invitation to book',
    aria='The full pARTy With Laura homepage, scrolling slowly from top to bottom')

programs = [
    ('card-classes', 'Weekly Classes', ['Ages 6 to 18', 'Small groups of 2 to 5', 'September to June'], 'The Weekly Classes card, with a colourful lion painting'),
    ('card-parties', 'Paint Parties', ['Birthdays, bachelorettes and team events', 'Guided, no experience needed', 'At her studio or yours'], 'The Painting Parties card, with a cherry blossom painting'),
    ('card-camps', 'Summer Camps', ['Ages 7 and up', 'Small groups of 3 to 6', 'Half-day or full-day'], 'The Summer Camps card, with a toucan painting'),
    ('card-workshops', 'Workshops', ['Themed weekend projects', 'Bob Ross oil painting', 'Acrylics and mixed media'], 'The Workshops card, with a wildflower painting'),
]
prog_html = '\n'.join(f'''<li class="lw-prog sp-reveal">
<span class="lw-prog-img"><img src="{blob(k)}" alt="{alt}" width="480" height="1124" loading="lazy"></span>
<span class="lw-prog-txt">
<span style="font-family: {SERIF}; font-size: clamp(24px, 2vw, 30px); line-height: 1.15; color: #121414">{name}</span>
<span class="lw-facts">{''.join(f'<span>{f}</span>' for f in facts)}</span>
</span>
</li>''' for k, name, facts, alt in programs)

PROGRAMS = f'''<!-- FOUR PROGRAMS -->
<section aria-labelledby="programs-title" style="position: relative; overflow: hidden; background: {FOAM}">
<div aria-hidden="true" style="position: absolute; inset: 0; pointer-events: none; background: radial-gradient(ellipse 50% 45% at 100% 0%, rgba(249, 207, 207, 0.45), rgba(249, 207, 207, 0) 70%), radial-gradient(ellipse 45% 40% at 0% 100%, rgba(159, 208, 212, 0.35), rgba(159, 208, 212, 0) 70%)"></div>
<div style="position: relative; {WRAP}; {PAD}; display: flex; flex-direction: column; gap: clamp(48px, 6vw, 88px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 24px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{C.label('Four Programs', DEEP)}
{C.h2('programs-title', 'Four programs,', 'four clear paths', em_color=DEEP)}
</div>
<div style="flex: 1 1 420px; min-width: 0">{C.p('Weekly classes, paint parties, summer camps and workshops each serve a different crowd, from young artists to bachelorette parties. Each one has its own card, its own page and its own next step, so every visitor can find the right fit.')}</div>
</div>
<ul class="lw-programs">
{prog_html}
</ul>
</div>
</section>
'''

card1 = C.type_card(MIST, f'''<p style="margin: 0; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: {DEEP_DARK}">Headings · Gaegu</p>
<p aria-hidden="true" style="margin: 0; font-family: {GAEGU}; font-weight: 400; font-size: clamp(36px, 3.8vw, 60px); line-height: 1.1; color: {DEEP}">Small Groups, Big Inspiration.</p>
<p style="margin: 0; font-family: {GAEGU}; font-weight: 400; font-size: clamp(24px, 2.2vw, 34px); line-height: 1.2; color: {DEEP}">Curated Creativity for Every Celebration.</p>''')
card2 = C.type_card(DEEP, f'''<p style="margin: 0; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: #FFFFFF">Text · Source Sans</p>
<p aria-hidden="true" style="margin: 0; font-family: {GAEGU}; font-weight: 400; font-size: clamp(30px, 2.8vw, 44px); line-height: 1.15; color: #FFFFFF">Infinite Variety. Total Flexibility.</p>
<p style="margin: 0; font-family: {SANS}; font-weight: 400; font-size: 19px; line-height: 1.7; color: rgba(255, 255, 255, 0.92)">Each event is designed for all ages, with customized themes and materials to match the group’s style.</p>
<span aria-hidden="true" style="align-self: flex-start; display: inline-flex; align-items: center; min-height: 46px; padding: 0 26px; background: {TEAL}; border-radius: 4px; font-family: {SANS}; font-weight: 400; font-size: 16px; color: {DEEP_DARK}">Book Your Party Now!</span>''')

DETAILS = C.details(
    title_main='Warm words,', title_em='in her colours',
    intro='I turned Laura’s notes into warm, clear copy for every page, with short headlines that make each program easy to picture. The palette is built around her existing logo: soft teal, deep teal for headings and buttons, and warm pink accents.',
    swatches=[('Soft Teal', TEAL, False), ('Deep Teal', DEEP, False), ('Mist', MIST, True), ('Blush', BLUSH, True), ('Pink', PINK, True)],
    card1=card1, card2=card2)

BEHIND = C.gallery(
    title_main='The details', title_em='that save her time',
    intro='Beyond the design, I set up the pieces that answer questions, take enquiries and sell gift certificates, so Laura can spend more of her time teaching.',
    url=URL, lab_color=DEEP,
    items=[
        (blob('faq-desk'), 'hr-L', 'Class Details', 'Answers before they’re asked', 'Expandable answers on each program page cover what parents ask most, from schedules and class sizes to what to wear and whether there’s a snack break.', 'The Class Details section on the Weekly Classes page, with the Class Size answer open'),
        (blob('gift-desk'), 'hr-S hr-drop', 'Gift Certificates', 'Give the gift of creativity', 'Digital gift certificates in five amounts, with clear terms on how they can be used.', 'The Gift Certificates page on the pARTy With Laura website, with an order form'),
        (blob('booking-desk'), 'hr-L lw-right', 'Booking', 'Here’s how it works', 'Three simple steps explain what happens next, followed by a short request form for private events.', 'The Booking page on the pARTy With Laura website, with three steps and a booking request form'),
    ]).replace('A Sample of the Pages', 'Behind the Scenes')

results = [
    ('weekly-classes', 'Weekly Kids Art Classes | Small Group Lessons in Cloverdale', 'Personalized art instruction for kids and teens (ages 6–18). Small class sizes (2–5 students) ensure individual guidance in painting, sketching, and mixed media.'),
    ('paint-parties', 'Private Paint Parties &amp; Team Building | Mobile Art Studio BC', 'Host an unforgettable paint party! Perfect for birthdays, bachelorettes, and corporate events. We bring supplies and guided instruction to your location.'),
    ('summer-camps', 'Kids Creative Art Summer Camps 2026 | Cloverdale &amp; Surrey', 'Register for boutique summer art camps for ages 7+. Small groups (3–6 students) mean personalized fun in painting, clay, and crafts. Registration opens in May!'),
]
res_html = '\n'.join(f'''<li class="rd-result" style="padding: 22px 24px; background: #FFFFFF; border: 1px solid rgba(18, 20, 20, 0.08); box-shadow: 0 20px 44px -30px rgba(18, 20, 20, 0.45); display: flex; flex-direction: column; gap: 6px">
<span style="font-size: 14px; color: #4E5558; overflow-wrap: anywhere">{URL} › {crumb}</span>
<span style="font-family: {SERIF}; font-size: 24px; line-height: 1.25; color: #2C4A8A">{t}</span>
<span style="font-size: 16px; line-height: 1.6; color: #3B4042">{d}</span>
</li>''' for crumb, t, d in results)

SEO = f'''<!-- SEO AND LOCAL SEARCH -->
<section aria-labelledby="seo-title" style="position: relative; overflow: hidden; background: {MIST}">
<div style="{WRAP}; {PAD}; display: flex; flex-wrap: wrap; align-items: center; gap: 56px clamp(48px, 7vw, 120px)">
<div class="sp-reveal" style="flex: 1 1 440px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{C.label('SEO and Local Search', DEEP_DARK)}
{C.h2('seo-title', 'Found close', 'to home', em_color=DEEP)}
{C.p('Every page has its own search-friendly title and description, written around what local families look for, with Cloverdale, Surrey, Langley and the Fraser Valley woven naturally into the copy.')}
{C.p('I also tidied up the page addresses and moved the site onto her own domain for launch.')}
</div>
<div class="sp-reveal" style="flex: 1.2 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
<p style="margin: 0; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: #3B4F55">A few of the page titles and descriptions</p>
<ul style="list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 14px">
{res_html}
</ul>
</div>
</div>
</section>
'''

PHONES = C.phones(
    title_main='Just as bright', title_em='on a phone',
    intro='Parents often plan on the go, so I designed every page to work just as well on a small screen, from booking a party to buying a gift certificate.',
    items=[(blob('offer-phone'), 'The What We Offer page on a phone'), (blob('about-phone'), 'The Meet Laura page on a phone'),
           (blob('gift-phone'), 'The Gift Certificates page on a phone'), (blob('gallery-phone'), 'The Gallery page on a phone')])

QUOTE = f'''<!-- TESTIMONIAL (placeholder until Laura's words arrive) -->
<section aria-label="Client testimonial placeholder" style="background: #FFFFFF">
<div class="sp-reveal" style="{WRAP}; padding-top: clamp(72px, 8vw, 112px); padding-bottom: clamp(72px, 8vw, 112px)">
<div style="position: relative; padding: clamp(30px, 3.4vw, 50px); border: 1px dashed rgba(6, 102, 128, 0.5); background: {BLUSH}; display: flex; flex-direction: column; align-items: center; gap: 16px; text-align: center">
<span aria-hidden="true" style="font-family: {SERIF}; font-size: 88px; line-height: 0.6; height: 32px; color: {DEEP}">“</span>
<p style="margin: 0; font-size: 13px; letter-spacing: 0.24em; text-transform: uppercase; color: {DEEP_DARK}">Placeholder</p>
<p style="margin: 0; font-family: {SERIF}; font-style: italic; font-weight: 300; font-size: clamp(21px, 1.65vw, 25px); line-height: 1.45; color: #121414">A quote from Laura will go here.</p>
</div>
</div>
</section>
'''

NEXT = C.next_project(href='Rooster-Den.dc.html', title='The Rooster Den Co', sub='Shopify redesign · SEO · Google Business Profile setup',
                      img='/_blob/' + R['hero-desk'], img_w=1800, img_h=1125, url='theroosterdenco.com')
CLOSING = C.closing('Let’s create a website', 'as inspiring as your work')

MAIN = '\n'.join([HERO, BRIEF, SCROLL, PROGRAMS, DETAILS, BEHIND, SEO, PHONES, QUOTE, NEXT, CLOSING])

EXTRA = '''/* PARTY WITH LAURA */
.lw-programs{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:clamp(20px,2.6vw,44px);align-items:start}
.lw-prog{display:flex;flex-direction:column;gap:24px;min-width:0}
.lw-programs > :nth-child(even){margin-top:clamp(0px,4vw,64px)}
.lw-prog-img{display:block;box-shadow:0 30px 60px -30px rgba(6,70,90,.45);transition:transform .8s cubic-bezier(.2,.7,.2,1)}
.lw-prog-img img{display:block;width:100%;height:auto}
.lw-programs > :nth-child(1) .lw-prog-img{transform:rotate(-2deg)}
.lw-programs > :nth-child(2) .lw-prog-img{transform:rotate(1.4deg)}
.lw-programs > :nth-child(3) .lw-prog-img{transform:rotate(-1deg)}
.lw-programs > :nth-child(4) .lw-prog-img{transform:rotate(1.8deg)}
.lw-prog:hover .lw-prog-img{transform:translateY(-8px) rotate(0deg)}
.lw-prog-txt{display:flex;flex-direction:column;gap:12px;min-width:0}
.lw-facts{display:flex;flex-direction:column;border-top:1px solid rgba(6,102,128,.25)}
.lw-facts > span{padding:10px 0;border-bottom:1px solid rgba(6,102,128,.25);font-size:17px;line-height:1.45;color:#1F2426}
@media (max-width: 960px){.lw-programs{grid-template-columns:repeat(2,minmax(0,1fr));gap:48px clamp(20px,4vw,40px)}.lw-programs > :nth-child(even){margin-top:40px}}
@media (max-width: 560px){.lw-programs{grid-template-columns:minmax(0,1fr);gap:40px}.lw-programs > :nth-child(even){margin-top:0}.lw-prog{display:grid;grid-template-columns:minmax(0,2fr) minmax(0,3fr);gap:20px;align-items:center}.lw-programs > :nth-child(n) .lw-prog-img{transform:none}}
.lw-right{grid-column:6 / span 7}
@media (max-width: 860px){.lw-right{grid-column:1 / -1}}
.rd-result{transition:transform .5s cubic-bezier(.2,.7,.2,1)}
.rd-result:hover{transform:translateX(6px)}
@media (prefers-reduced-motion: reduce){.lw-prog-img,.rd-result{transition:none}.lw-programs > :nth-child(n) .lw-prog-img{transform:none}}
/* /PARTY WITH LAURA */'''

C.write_page(ROOT, 'Party-With-Laura.dc.html',
             title='pARTy With Laura: Squarespace Website Case Study | Sullivan Park Design',
             desc='How I designed a bright, playful Squarespace website for pARTy With Laura, a Cloverdale art studio, with clear program pages, warm copy, local SEO and simple booking.',
             fonts_href='https://fonts.googleapis.com/css2?family=Gaegu:wght@400&amp;family=Source+Sans+3:wght@400&amp;display=swap',
             main=MAIN, extra_css=EXTRA, preview_h=12100)
