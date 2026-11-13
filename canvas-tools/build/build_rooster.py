"""The Rooster Den Co case study (Rooster-Den.dc.html)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import case_common as C

ROOT = sys.argv[1]
B = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'rooster', 'blobs.json')))
def blob(k): return '/_blob/' + B[k]

INK, CHAR, SAGE, TERRA, CREAM = '#171717', '#5C5C5C', '#6D7C7C', '#C16452', '#FAF2E6'
TERRA_TXT = '#A84F3E'  # terracotta deep enough for text on light backgrounds
URL = 'theroosterdenco.com'
SERIF = C.SERIF
TRI = "'Trirong', Georgia, serif"
NUN = "'Nunito Sans', 'Abel', sans-serif"
WRAP, PAD = C.WRAP, C.SECTION_PAD

glow = (f'<span style="position: absolute; top: -25%; right: -10%; width: 70%; height: 90%; background: radial-gradient(closest-side, rgba(193, 100, 82, 0.14), rgba(193, 100, 82, 0) 100%)"></span>'
        f'<span style="position: absolute; bottom: -30%; left: -15%; width: 60%; height: 70%; background: radial-gradient(closest-side, rgba(109, 124, 124, 0.16), rgba(109, 124, 124, 0) 100%)"></span>')

HERO = C.hero(
    bg=CREAM, dark=False, label_text='Portfolio · Retail', accent=TERRA_TXT,
    title_main='The Rooster', title_em='Den Co', em_color=TERRA_TXT,
    lede='A cowgirl-chic Shopify redesign for a woman-owned western boutique in White Rock, with clearer shopping journeys, page-by-page SEO and a Google Business Profile.',
    visit_url='https://theroosterdenco.com/', visit_label=URL,
    meta=[('Client', 'The Rooster Den Co'), ('Location', 'White Rock, BC'),
          ('What I Did', 'Shopify redesign · SEO · Google Business Profile setup'), ('Platform', 'Shopify')],
    desk_img=blob('hero-desk'), desk_alt='The Rooster Den Co homepage on a desktop screen, with western boots beside a vintage truck and the headline Grit, Grace and Curated Western Glam',
    phone_img=blob('hero-phone'), phone_alt='The Rooster Den Co homepage on a phone',
    url=URL, glow=glow, line_color='rgba(193, 100, 82, 0.5)')

BRIEF = C.brief(
    label_text='The Story', title_main='It started with SEO.', title_em='It became a whole new store.',
    paras=['The owner first came to me for SEO, because her Shopify admin was showing that it hadn’t been set up.',
           'After we talked and she saw my work, she asked me to redesign the whole store as well. I took on the redesign and the SEO, and set up her Google Business Profile too.'],
    did=['A full Shopify redesign', 'Clearer shopping journeys', 'Page-by-page SEO', 'Google Business Profile setup'],
    num_color=TERRA, em_color=TERRA_TXT)

BA = f'''<!-- BEFORE AND AFTER -->
<section class="sp-on-dark" aria-labelledby="ba-title" style="position: relative; overflow: hidden; background: {INK}; color: #FFFFFF">
<div aria-hidden="true" style="position: absolute; inset: 0; pointer-events: none; background: radial-gradient(ellipse 60% 55% at 15% 0%, rgba(193, 100, 82, 0.18), rgba(193, 100, 82, 0) 70%)"></div>
<div style="position: relative; {WRAP}; {PAD}; display: flex; flex-direction: column; gap: clamp(44px, 5vw, 72px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 24px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{C.label('Before and After', '#E3A08F')}
{C.h2('ba-title', 'The same boutique,', 'completely reimagined', color='#FFFFFF', em_color='#E3A08F')}
</div>
<div style="flex: 1 1 420px; min-width: 0">{C.p('Drag the handle to compare the store before and after the redesign.', color='rgba(255, 255, 255, 0.82)')}</div>
</div>
<figure class="sp-reveal" style="margin: 0; display: flex; flex-direction: column; gap: 18px">
<div class="sp-device" style="background: #1C1F26; border: 1px solid rgba(246, 243, 238, 0.12); box-shadow: 0 40px 90px rgba(0, 0, 0, 0.45)">
<div aria-hidden="true" style="height: 34px; padding: 0 16px; display: flex; align-items: center; gap: 7px; border-bottom: 1px solid rgba(246, 243, 238, 0.12)"><span style="width: 9px; height: 9px; border-radius: 50%; background: #3A3F49"></span><span style="width: 9px; height: 9px; border-radius: 50%; background: #3A3F49"></span><span style="width: 9px; height: 9px; border-radius: 50%; background: #3A3F49"></span><span style="margin-left: 12px; font-size: 13px; color: rgba(246, 243, 238, 0.6)">{URL}</span></div>
<div class="rd-ba" ref="{{{{baRef}}}}">
<div class="rd-ba-after"><img src="{blob('hero-desk')}" alt="After: the redesigned Rooster Den Co homepage" width="1800" height="1125" loading="lazy"></div>
<div class="rd-ba-before"><div class="rd-ba-ph"><span class="rd-ba-ph-in"><span style="font-size: 13px; letter-spacing: 0.24em; text-transform: uppercase; color: #8A6A55">Placeholder</span><span style="font-family: {SERIF}; font-size: clamp(24px, 2.6vw, 40px); line-height: 1.15; color: {INK}">Before screenshot</span><span style="font-size: 16px; color: #5C5C5C">Coming soon</span></span></div></div>
<div class="rd-ba-line" aria-hidden="true"><span class="rd-ba-knob"><svg width="26" height="14" viewBox="0 0 26 14" fill="none"><path d="M8 1L2 7l6 6M18 1l6 6-6 6" stroke="currentColor" stroke-width="1.4"></path></svg></span></div>
<span class="rd-ba-tag rd-ba-tag-b" aria-hidden="true">Before</span><span class="rd-ba-tag rd-ba-tag-a" aria-hidden="true">After</span>
<input class="rd-ba-range" type="range" min="0" max="100" step="1" aria-label="Compare the store before and after the redesign">
</div>
</div>
<figcaption style="font-size: 16px; letter-spacing: 0.04em; color: rgba(255, 255, 255, 0.7)">The homepage, before and after</figcaption>
</figure>
</div>
</section>
'''

SCROLL = C.scroller(
    label_text='The Homepage', title_main='Bold from', title_em='the first scroll',
    intro='The homepage leads with attitude, then gets straight to the collections, the reviews and what’s new.',
    chapters=['Grit, grace and curated western glam', 'Welcome to the Den', 'Featured collections', 'Words from customers', 'What’s hot right now', 'About the store'],
    numerals=['I', 'II', 'III', 'IV', 'V', 'VI'], num_color=TERRA_TXT,
    img=blob('scroll-home'), img_w=1000, img_h=3770, url=URL, duration='60s',
    alt='The complete Rooster Den Co homepage, from the hero image through the featured collections, customer reviews, new arrivals and the story of the store',
    aria='The full Rooster Den Co homepage, scrolling slowly from top to bottom')

card1 = C.type_card(CREAM, f'''<p style="margin: 0; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: {TERRA_TXT}">Headings · Trirong</p>
<p aria-hidden="true" style="margin: 0; font-family: {TRI}; font-weight: 400; font-size: clamp(30px, 3.4vw, 54px); line-height: 1.15; color: {INK}">Grit, Grace &amp; Curated Western Glam</p>
<p style="margin: 0; font-family: {TRI}; font-weight: 400; font-size: clamp(22px, 2vw, 30px); line-height: 1.3; color: {CHAR}">Made To Be Noticed</p>''')
card2 = C.type_card(SAGE, f'''<p style="margin: 0; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: #FFFFFF">Text · Nunito Sans</p>
<p aria-hidden="true" style="margin: 0; font-family: {NUN}; font-weight: 400; font-size: clamp(26px, 2.4vw, 36px); line-height: 1.3; color: #FFFFFF">Giddy Up Gorgeous!</p>
<p style="margin: 0; font-family: {NUN}; font-weight: 400; font-size: 18px; line-height: 1.75; color: rgba(255, 255, 255, 0.9)">Friendly and easy to read, so product details, sizes and prices are clear at a glance.</p>
<span aria-hidden="true" style="align-self: flex-start; display: inline-flex; align-items: center; min-height: 46px; padding: 0 26px; background: {CREAM}; font-family: {NUN}; font-weight: 400; font-size: 15px; color: {INK}">Shop the Den</span>''')

DETAILS = C.details(
    title_main='Warm, bold', title_em='and a little bit country',
    intro='A grounded palette of ink, charcoal, sage and terracotta lets the leather, turquoise and fringe take centre stage. Trirong gives headings a classic western feel, and Nunito Sans keeps shopping easy to read.',
    swatches=[('Ink', INK, False), ('Charcoal', CHAR, False), ('Sage', SAGE, False), ('Terracotta', TERRA, False), ('Cream', CREAM, True)],
    card1=card1, card2=card2)

def step(n, t):
    return f'<span style="display: inline-flex; align-items: center; gap: 12px; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: #E3A08F"><span style="display: inline-flex; align-items: center; justify-content: center; width: 30px; height: 30px; border: 1px solid rgba(227, 160, 143, 0.7); border-radius: 50%; font-family: {SERIF}; font-size: 17px; letter-spacing: 0">{n}</span>{t}</span>'

col_chips = ['Bags, Purses &amp; Wallets', 'Jewelry, Hats &amp; Accessories', 'Home &amp; Pet Essentials']
chips = '\n'.join(f'<li style="display: inline-flex; align-items: center; min-height: 44px; padding: 0 20px; border: 1px solid rgba(227, 160, 143, 0.55); font-size: 16px; letter-spacing: 0.04em; color: #FFFFFF">{c}</li>' for c in col_chips)

JOURNEY = f'''<!-- SHOPPING JOURNEYS -->
<section class="sp-on-dark" aria-labelledby="journey-title" style="position: relative; overflow: hidden; background: #2A2B2B; color: #FFFFFF">
<div style="position: relative; {WRAP}; {PAD}; display: flex; flex-direction: column; gap: clamp(48px, 6vw, 88px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; gap: 32px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{C.label('Shopping Journeys', '#E3A08F')}
{C.h2('journey-title', 'Clearer paths', 'to the perfect find', color='#FFFFFF', em_color='#E3A08F')}
</div>
<div style="flex: 1.1 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 24px">
{C.p('I organized the store around the way her customers shop. Shop the Den opens into three clear collections, and each product page keeps the details simple, so it’s easy to go from browsing to buying.', color='rgba(255, 255, 255, 0.88)', size='20px')}
<ul class="cs-chips">
{chips}
</ul>
</div>
</div>
<div class="rd-journey">
<figure class="sp-reveal rd-j1" style="margin: 0; display: flex; flex-direction: column; gap: 16px">{step(1, 'Shop the Den')}{C.desk(blob('den-desk'), 'The Shop the Den page on The Rooster Den Co website', URL, dark=True)}</figure>
<figure class="sp-reveal rd-j3" style="margin: 0; display: flex; flex-direction: column; gap: 16px">{step(3, 'Find the one')}{C.desk(blob('product-desk'), 'A product page on The Rooster Den Co website for a hand-tooled leather fringe crossbody bag', URL, dark=True)}</figure>
<div class="rd-j2" style="display: flex; flex-direction: column; gap: 16px">
{step(2, 'Choose a collection')}
<div class="rd-trio">
<figure class="sp-reveal" style="margin: 0">{C.desk(blob('bags-desk'), 'The Bags, Purses and Wallets collection page', URL, dark=True)}</figure>
<figure class="sp-reveal" style="margin: 0">{C.desk(blob('hats-desk'), 'The Jewelry, Hats and Accessories collection page', URL, dark=True)}</figure>
<figure class="sp-reveal" style="margin: 0">{C.desk(blob('ranch-desk'), 'The Home and Pet Essentials collection page', URL, dark=True)}</figure>
</div>
</div>
</div>
</div>
</section>
'''

results = [
    ('collections › signature-western-handbags-artisan-accessories', 'Western Handbags, Canvas Totes &amp; Leather Wallets', 'Shop our curated collection of premium Western handbags, including hand-tooled leather purses and one-of-a-kind fringe bags from brands like American Darling and Myra.'),
    ('collections › western-jewelry-for-women', 'Western Jewelry, hats, and accessories for Women | The Rooster Den Co', 'Saddle up with glam-approved cowgirl armor. From bold artisan jewelry to head-turning ‘Cowgirl Era’ hats and statement accessories, we curate looks that refuse to play it safe.'),
    ('pages › about-us', 'About Us | Woman-Owned Western Boutique | The Rooster Den', 'Welcome to The Rooster Den! We are a woman-owned boutique dedicated to bringing you bold, high-end Western handbags and unapologetic modern cowgirl style.'),
]
res_html = '\n'.join(f'''<li class="rd-result" style="padding: 22px 24px; background: #FFFFFF; border: 1px solid rgba(18, 20, 20, 0.08); box-shadow: 0 20px 44px -30px rgba(18, 20, 20, 0.45); display: flex; flex-direction: column; gap: 6px">
<span style="font-size: 14px; color: #4E5558; overflow-wrap: anywhere">theroosterdenco.com › {crumb}</span>
<span style="font-family: {SERIF}; font-size: 24px; line-height: 1.25; color: #2C4A8A">{t}</span>
<span style="font-size: 16px; line-height: 1.6; color: #3B4042">{d}</span>
</li>''' for crumb, t, d in results)

PIN = '<svg width="22" height="28" viewBox="0 0 22 28" fill="none" aria-hidden="true"><path d="M11 27s9-9.2 9-16A9 9 0 0 0 2 11c0 6.8 9 16 9 16z" stroke="currentColor" stroke-width="1.3"></path><circle cx="11" cy="11" r="3.2" stroke="currentColor" stroke-width="1.3"></circle></svg>'

SEO = f'''<!-- SEO AND GOOGLE BUSINESS PROFILE -->
<section aria-labelledby="seo-title" style="position: relative; overflow: hidden; background: {CREAM}">
<div style="{WRAP}; {PAD}; display: flex; flex-wrap: wrap; align-items: center; gap: 56px clamp(48px, 7vw, 120px)">
<div class="sp-reveal" style="flex: 1 1 440px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{C.label('SEO and Google Business Profile', TERRA_TXT)}
{C.h2('seo-title', 'Easier to find,', 'page by page', em_color=TERRA_TXT)}
{C.p('Every page has its own search-friendly title and description, written around what shoppers look for, from western handbags to statement jewelry.')}
{C.p('I also set up her Google Business Profile, so the boutique can be found on Google Search and Maps.')}
<div style="margin-top: 8px; display: flex; gap: 18px; align-items: flex-start; padding: 24px; background: #FFFFFF; border: 1px solid rgba(193, 100, 82, 0.35)">
<span style="flex: none; color: {TERRA}">{PIN}</span>
<span style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 13px; letter-spacing: 0.2em; text-transform: uppercase; color: {TERRA_TXT}">Google Business Profile</span><span style="font-family: {SERIF}; font-size: 24px; line-height: 1.25; color: #121414">The Rooster Den Co</span><span style="font-size: 16px; line-height: 1.6; color: #3B4042">1381 George St, Suite 5B, White Rock, BC</span></span>
</div>
</div>
<div class="sp-reveal" style="flex: 1.2 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
<p style="margin: 0; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: #4E5558">A few of the page titles and descriptions</p>
<ul style="list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 14px">
{res_html}
</ul>
</div>
</div>
</section>
'''

MARQUEE = C.marquee(['Grit', 'Grace', 'Curated Western Glam', 'Made To Be Noticed', 'Giddy Up Gorgeous'], bg=SAGE, color='#FFFFFF', dot_color=CREAM, border='rgba(255, 255, 255, 0.2)')

GALLERY = C.gallery(
    title_main='Every page,', title_em='<span style="white-space: nowrap">made to be noticed</span>',
    intro='Big, warm photography and plenty of personality, with every page still easy to shop.',
    url=URL, lab_color=TERRA_TXT,
    items=[
        (blob('about-desk'), 'hr-L', 'About', 'The Heart of the Den', 'The story of a woman-owned boutique, told with the same bold personality as the store.', 'The About Us page on The Rooster Den Co website'),
        (blob('reviews-desk'), 'hr-S hr-drop', 'Reviews', 'Real Customer Reviews', 'A page of its own for customer reviews, so shoppers can see what others love.', 'The Customer Reviews page on The Rooster Den Co website'),
    ])

PHONES = C.phones(
    title_main='Made for shopping', title_em='on a phone',
    intro='Many shoppers browse on their phones, so I designed every page to be just as easy to shop on a small screen.',
    items=[(blob('den-phone'), 'The Shop the Den page on a phone'), (blob('bags-phone'), 'A collection page on a phone'),
           (blob('product-phone'), 'A product page on a phone'), (blob('about-phone'), 'The About Us page on a phone')])

QUOTE = f'''<!-- TESTIMONIAL (placeholder until the owner's words arrive) -->
<section aria-label="Client testimonial placeholder" style="background: #FFFFFF">
<div class="sp-reveal" style="{WRAP}; padding-top: clamp(72px, 8vw, 112px); padding-bottom: clamp(72px, 8vw, 112px)">
<div style="position: relative; padding: clamp(30px, 3.4vw, 50px); border: 1px dashed rgba(193, 100, 82, 0.6); background: {CREAM}; display: flex; flex-direction: column; align-items: center; gap: 16px; text-align: center">
<span aria-hidden="true" style="font-family: {SERIF}; font-size: 88px; line-height: 0.6; height: 32px; color: {TERRA}">“</span>
<p style="margin: 0; font-size: 13px; letter-spacing: 0.24em; text-transform: uppercase; color: {TERRA_TXT}">Placeholder</p>
<p style="margin: 0; font-family: {SERIF}; font-style: italic; font-weight: 300; font-size: clamp(21px, 1.65vw, 25px); line-height: 1.45; color: #121414">A quote from the owner of The Rooster Den Co will go here.</p>
</div>
</div>
</section>
'''

NEXT = C.next_project(href='Hamish-Ross.dc.html', title='Hamish Ross Real Estate', sub='Custom-coded website · Ongoing SEO &amp; marketing',
                      img='/_blob/2f057afafa2a706726d866726a890535', img_w=1800, img_h=1125, url='hamishross.com')
CLOSING = C.closing('Let’s create something', 'made to be noticed')

MAIN = '\n'.join([HERO, BRIEF, BA, SCROLL, DETAILS, JOURNEY, SEO, GALLERY, PHONES, QUOTE, NEXT, CLOSING])

EXTRA = '''/* ROOSTER DEN */
.rd-ba{--pos:50%;position:relative;aspect-ratio:16 / 10;overflow:hidden;background:#EDE4D6;touch-action:pan-y}
.rd-ba-after img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.rd-ba-before{position:absolute;inset:0;clip-path:inset(0 calc(100% - var(--pos)) 0 0)}
.rd-ba-ph{position:absolute;inset:0;background:repeating-linear-gradient(135deg,#EFE6D8 0 14px,#E9DFCF 14px 28px);display:flex;align-items:center;justify-content:center;padding-right:50%}
.rd-ba-ph-in{display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center;padding:24px 32px;background:rgba(250,242,230,.92);border:1px dashed rgba(138,106,85,.6)}
.rd-ba-line{position:absolute;top:0;bottom:0;left:var(--pos);width:2px;margin-left:-1px;background:#FAF2E6;pointer-events:none}
.rd-ba-knob{position:absolute;top:50%;left:50%;width:54px;height:54px;transform:translate(-50%,-50%);border-radius:50%;background:#FAF2E6;color:#171717;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 30px rgba(0,0,0,.35)}
.rd-ba-tag{position:absolute;top:16px;padding:6px 12px;background:rgba(23,23,23,.72);color:#FFFFFF;font-size:12px;letter-spacing:.2em;text-transform:uppercase;pointer-events:none}
.rd-ba-tag-b{left:16px}.rd-ba-tag-a{right:16px}
.rd-ba-range{position:absolute;inset:0;width:100%;height:100%;margin:0;opacity:0;cursor:ew-resize;-webkit-appearance:none;appearance:none}
.rd-ba:has(.rd-ba-range:focus-visible) .rd-ba-knob{outline:2px solid #E3A08F;outline-offset:4px}
.rd-journey{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:clamp(40px,5vw,72px) clamp(24px,3vw,48px);align-items:start}
.rd-j1{grid-column:1 / span 7}
.rd-j3{grid-column:8 / span 5;margin-top:clamp(40px,8vw,140px)}
.rd-j2{grid-column:1 / -1}
.rd-trio{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(16px,2.4vw,36px)}
@media (max-width: 860px){.rd-j1,.rd-j3{grid-column:1 / -1}.rd-j3{margin-top:0}.rd-j2{order:2}.rd-j3{order:3}.rd-trio{grid-template-columns:1fr}}
.rd-result{transition:transform .5s cubic-bezier(.2,.7,.2,1)}
.rd-result:hover{transform:translateX(6px)}
@media (prefers-reduced-motion: reduce){.rd-result{transition:none}}
/* /ROOSTER DEN */'''

COMPONENT = '''class Component extends DCLogic {
  getBaRef() {
    // Before and after slider: the range input moves the divider.
    if (!this._baRef) {
      this._baRef = (el) => {
        if (this._baOff) { try { this._baOff(); } catch (e) {} this._baOff = null; }
        if (!el) return;
        const input = el.querySelector('.rd-ba-range');
        if (!input) return;
        const move = () => { el.style.setProperty('--pos', (input.value || 50) + '%'); };
        input.addEventListener('input', move);
        input.addEventListener('change', move);
        this._baOff = () => { input.removeEventListener('input', move); input.removeEventListener('change', move); };
      };
    }
    return this._baRef;
  }
  renderVals() {
    const s = this.state || {};
    const menuOpen = !!s.menuOpen;
    return {
      menuOpen: menuOpen,
      menuExpanded: menuOpen ? 'true' : 'false',
      toggleMenu: () => this.setState({ menuOpen: !menuOpen }),
      baRef: this.getBaRef(),
      closeMenu: () => this.setState({ menuOpen: false })
    };
  }
}
'''

C.write_page(ROOT, 'Rooster-Den.dc.html',
             title='The Rooster Den Co: Shopify Redesign Case Study | Sullivan Park Design',
             desc='How I redesigned The Rooster Den Co’s Shopify store in White Rock with clearer shopping journeys, page-by-page SEO and a Google Business Profile.',
             fonts_href='https://fonts.googleapis.com/css2?family=Trirong:wght@400&amp;family=Nunito+Sans:wght@400&amp;display=swap',
             main=MAIN, extra_css=EXTRA, preview_h=13100, component=COMPONENT)
