import re, json
B='/tmp/claude-0/-home-claude/af2e7c4f-b0c2-5453-8ecb-cf465c9edaf4/scratchpad/canvas/project/'
wd=open(B+'Website-Design.dc.html').read()
seo_old=open(B+'SEO.dc.html').read()
brand_old=open(B+'Brand-Marketing-Design.dc.html').read()

PORT='https://www.sullivanparkdesign.com/website-design-portfolio'
HRP=PORT+'/hamish-ross-real-estate'; SMP=PORT+'/smash'
ARROW='<svg width="20" height="10" viewBox="0 0 26 10" fill="none" aria-hidden="true"><path d="M0 5h24M20 1l4 4-4 4" stroke="currentColor" stroke-width="1.1"></path></svg>'
ARROWB='<svg width="22" height="10" viewBox="0 0 26 10" fill="none" aria-hidden="true"><path d="M0 5h24M20 1l4 4-4 4" stroke="currentColor" stroke-width="1.1"></path></svg>'
EXT='<svg width="12" height="12" viewBox="0 0 18 18" fill="none" aria-hidden="true"><path d="M5 13L13 5M6.5 5H13v6.5" stroke="currentColor" stroke-width="1.3"></path></svg>'
PALM='/_blob/fddc24a18e2595d21f63da9f1d7bf0d5'

def label(text, dark=False):
    c='#FFFFFF' if dark else '#4E6368'
    return f'<p style="margin: 0; display: flex; align-items: center; gap: 16px; font-size: 15px; letter-spacing: 0.2em; text-transform: uppercase; color: {c}"><span aria-hidden="true" style="display: block; width: 40px; height: 1px; background: {c}"></span>{text}</p>'

def bar(url, h=34, fs=13):
    d=9 if h>=34 else 8
    return f'<div aria-hidden="true" style="height: {h}px; padding: 0 {16 if h>=34 else 14}px; display: flex; align-items: center; gap: {7 if h>=34 else 6}px; border-bottom: 1px solid rgba(18, 20, 20, 0.1)"><span style="width: {d}px; height: {d}px; border-radius: 50%; background: #CDD3D2"></span><span style="width: {d}px; height: {d}px; border-radius: 50%; background: #CDD3D2"></span><span style="width: {d}px; height: {d}px; border-radius: 50%; background: #CDD3D2"></span><span style="margin-left: 12px; font-size: {fs}px; color: #5A6163">{url}</span></div>'

def btn_primary(text='Enquire About Your Project', extra=''):
    return f'<a class="sp-btn sp-btn-blue" href="Contact.dc.html" style="{extra}display: inline-flex; align-items: center; justify-content: center; gap: 14px; min-height: 58px; padding: 0 34px; background: #4E6368; border: 1px solid #4E6368; color: #FFFFFF; text-decoration: none; font-size: 18px; letter-spacing: 0.03em">{text}{ARROWB}</a>'

def links(name, proj, visit, visit_label, dark=False):
    if dark:
        vp=f'<a class="sp-btn sp-btn-ghost" href="{proj}" aria-label="View Project, {name}" style="display: inline-flex; align-items: center; gap: 12px; min-height: 54px; padding: 0 24px; border: 1px solid rgba(255, 255, 255, 0.75); color: #FFFFFF; text-decoration: none; font-size: 17px; letter-spacing: 0.03em">View Project{ARROW}</a>'
        col='#FFFFFF'
    else:
        vp=f'<a class="sp-btn sp-btn-line" href="{proj}" aria-label="View Project, {name}" style="display: inline-flex; align-items: center; gap: 12px; min-height: 54px; padding: 0 24px; border: 1px solid #4E6368; color: #4E6368; text-decoration: none; font-size: 17px; letter-spacing: 0.03em">View Project{ARROW}</a>'
        col='#4E6368'
    vw=f'<a class="sp-ext" href="{visit}" aria-label="Visit Website, {visit_label}" style="display: inline-flex; align-items: center; gap: 8px; min-height: 44px; font-size: 16px; letter-spacing: 0.03em; color: {col}; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 6px">Visit Website{EXT}</a>'
    return vp, vw

def hero(lbl, h1, intro, desk, desk_alt, desk_w, desk_h, url, phone, phone_alt, name, line, proj, visit, visit_label, markers='', legend=''):
    vp,vw=links(name,proj,visit,visit_label)
    return f'''<!-- HERO: real work leads (desktop and phone pairing) -->
<section aria-labelledby="page-title" style="position: relative; overflow: hidden; background: #FAFAF8">
<img class="sp-sway" src="{PALM}" alt="" width="1800" height="1200" style="position: absolute; top: -20px; right: -20px; width: min(1320px, 110vw); height: auto; max-width: none; opacity: 0.16; mix-blend-mode: multiply; pointer-events: none; z-index: 0">
<div style="position: relative; z-index: 1; width: 100%; max-width: 1680px; margin: 0 auto; padding: clamp(140px, 12vw, 172px) clamp(20px, 5vw, 72px) clamp(72px, 8vw, 112px); display: flex; flex-direction: column; gap: clamp(48px, 6vw, 80px)">
<div style="display: flex; flex-wrap: wrap; align-items: flex-end; gap: 28px clamp(48px, 7vw, 120px)">
<div style="flex: 1.3 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 28px">
{label(lbl)}
<h1 id="page-title" style="margin: 0; font-family: 'Cormorant Infant', Garamond, serif; font-weight: 300; font-size: clamp(48px, 6vw, 100px); line-height: 1.02; letter-spacing: -0.015em; color: #121414; text-wrap: balance">{h1}</h1>
</div>
<div style="flex: 1 1 400px; min-width: 0; display: flex; flex-direction: column; align-items: flex-start; gap: 26px; padding-bottom: 8px">
<p style="margin: 0; font-size: 20px; line-height: 1.65; color: #1F2426">{intro}</p>
{btn_primary()}
</div>
</div>
<figure class="sp-reveal" style="margin: 0; display: flex; flex-direction: column; gap: 24px">
<div class="sp-stage sp-stagebox" style="position: relative; padding-bottom: clamp(28px, 4.5vw, 64px)">
<div class="sp-device sp-desk" style="width: 84%; background: #FFFFFF; border: 1px solid rgba(18, 20, 20, 0.14); box-shadow: 0 40px 90px rgba(18, 28, 30, 0.16)">
{bar(url)}
<div style="position: relative">
<img src="{desk}" alt="{desk_alt}" width="{desk_w}" height="{desk_h}" fetchpriority="high" style="width: 100%; height: auto">
{markers}
</div>
</div>
<div class="sp-device sp-phone" style="position: absolute; right: 2%; bottom: 0; width: clamp(110px, 19%, 270px); padding: 8px; background: #121414; border-radius: clamp(20px, 2.8vw, 40px); box-shadow: 0 30px 70px rgba(18, 28, 30, 0.28)">
<img src="{phone}" alt="{phone_alt}" width="540" height="1169" style="width: 100%; height: auto; border-radius: clamp(14px, 2.2vw, 32px)">
</div>
</div>
<figcaption style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px 32px; padding-top: 20px; border-top: 1px solid rgba(18, 20, 20, 0.14)">
<span style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 6px 18px"><span style="font-family: 'Cormorant Infant', Garamond, serif; font-size: 26px; line-height: 1.2; color: #121414">{name}</span><span style="font-size: 16px; line-height: 1.5; letter-spacing: 0.04em; color: #4E6368">{line}</span></span>
<span style="display: flex; flex-wrap: wrap; align-items: center; gap: 12px 28px">
{vp}
{vw}
</span>
</figcaption>
{legend}
</figure>
</div>
</section>'''

def approach(lbl, h2, paras):
    ps='\n'.join(f'<p style="margin: 0; font-size: 19px; line-height: 1.7; color: #1F2426">{p}</p>' for p in paras)
    return f'''<!-- APPROACH (condensed) -->
<section aria-labelledby="approach-title" style="background: #FFFFFF">
<div class="sp-reveal" style="width: 100%; max-width: 1680px; margin: 0 auto; padding: clamp(72px, 8vw, 112px) clamp(20px, 5vw, 72px); display: flex; flex-wrap: wrap; align-items: flex-start; gap: 28px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 380px; min-width: 0; display: flex; flex-direction: column; gap: 20px">
{label(lbl)}
<h2 id="approach-title" style="margin: 0; font-family: 'Cormorant Infant', Garamond, serif; font-weight: 300; font-size: clamp(36px, 4vw, 60px); line-height: 1.04; color: #121414; text-wrap: balance">{h2}</h2>
</div>
<div style="flex: 1.4 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 18px">
{ps}
</div>
</div>
</section>'''

def work_item(pid, reverse, url, desk, desk_alt, phone, phone_alt, industry, name, line, points, proj, visit, visit_label):
    vp,vw=links(name,proj,visit,visit_label,dark=True)
    lis='\n'.join(f'<li style="padding: 14px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.28); font-size: 18px; line-height: 1.55; color: #FFFFFF">{p}</li>' for p in points)
    rr='flex-direction: row-reverse; ' if reverse else ''
    deskpos='margin-left: auto; ' if reverse else ''
    phonepos='left: 2%;' if reverse else 'right: 2%;'
    return f'''<article class="sp-reveal" aria-labelledby="{pid}" style="display: flex; {rr}flex-wrap: wrap; align-items: center; gap: 40px clamp(48px, 6vw, 96px)">
<div class="sp-stage sp-stagebox" style="flex: 1.5 1 560px; min-width: 0; position: relative; padding-bottom: clamp(28px, 4vw, 56px)">
<div class="sp-device sp-desk" style="width: 84%; {deskpos}background: #FFFFFF; box-shadow: 0 34px 80px rgba(10, 18, 20, 0.35)">
{bar(url, 30, 12)}
<img src="{desk}" alt="{desk_alt}" width="1440" height="900" loading="lazy" style="width: 100%; height: auto">
</div>
<div class="sp-device sp-phone" style="position: absolute; {phonepos} bottom: 0; width: clamp(96px, 22%, 210px); padding: 7px; background: #121414; border-radius: clamp(18px, 2.4vw, 32px); box-shadow: 0 26px 60px rgba(10, 18, 20, 0.4)">
<img src="{phone}" alt="{phone_alt}" width="540" height="1169" loading="lazy" style="width: 100%; height: auto; border-radius: clamp(12px, 1.8vw, 26px)">
</div>
</div>
<div style="flex: 1 1 340px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
<p style="margin: 0; font-size: 15px; letter-spacing: 0.2em; text-transform: uppercase; color: #DCE4E5">{industry}</p>
<h3 id="{pid}" style="margin: 0; font-family: 'Cormorant Infant', Garamond, serif; font-weight: 400; font-size: clamp(32px, 3vw, 42px); line-height: 1.1; color: #FFFFFF">{name}</h3>
<p style="margin: 0; font-size: 16px; line-height: 1.5; letter-spacing: 0.04em; color: #DCE4E5">{line}</p>
<ul style="list-style: none; margin: 6px 0 0; padding: 0; border-top: 1px solid rgba(255, 255, 255, 0.28)">
{lis}
</ul>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 12px 28px; margin-top: 6px">
{vp}
{vw}
</div>
</div>
</article>'''

def work_section(lbl, h2, items):
    return f'''<!-- SELECTED WORK -->
<section aria-labelledby="work-title" class="sp-on-dark" style="position: relative; overflow: hidden; background: #4E6368; color: #FFFFFF">
<div aria-hidden="true" style="position: absolute; right: 0; top: 0; width: min(1100px, 100vw); pointer-events: none">
<img src="{PALM}" alt="" width="1800" height="1200" loading="lazy" style="width: 100%; height: auto; filter: brightness(0) invert(1); opacity: 0.07">
</div>
<div style="position: relative; width: 100%; max-width: 1680px; margin: 0 auto; padding: clamp(80px, 9vw, 128px) clamp(20px, 5vw, 72px) clamp(96px, 10vw, 144px); display: flex; flex-direction: column; gap: clamp(64px, 8vw, 112px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 24px 64px">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 20px">
{label(lbl, True)}
<h2 id="work-title" style="margin: 0; font-family: 'Cormorant Infant', Garamond, serif; font-weight: 300; font-size: clamp(40px, 4.6vw, 70px); line-height: 1.04; color: #FFFFFF; text-wrap: balance">{h2}</h2>
</div>
<a class="sp-btn sp-btn-ghost" href="{PORT}" style="display: inline-flex; align-items: center; justify-content: center; min-height: 54px; padding: 0 28px; border: 1px solid rgba(255, 255, 255, 0.75); color: #FFFFFF; text-decoration: none; font-size: 17px; letter-spacing: 0.03em">View the Full Portfolio</a>
</div>

{chr(10).join(items)}

</div>
</section>'''

def rows_section(lbl, h2, intro, rows, colA, colB, after=''):
    out=[]
    for name, sub, a, b in rows:
        subhtml=f'<p style="margin: 6px 0 0; font-family: \'Cormorant Infant\', Garamond, serif; font-style: italic; font-size: 20px; line-height: 1.35; color: #4E6368">{sub}</p>' if sub else ''
        def cell(head, body):
            if isinstance(body, list):
                inner='<ul style="list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 8px">'+''.join(f'<li style="font-size: 18px; line-height: 1.6; color: #1F2426">{x}</li>' for x in body)+'</ul>'
            else:
                inner=f'<p style="margin: 0; font-size: 18px; line-height: 1.7; color: #1F2426">{body}</p>'
            return f'<div style="display: flex; flex-direction: column; gap: 8px"><p style="margin: 0; font-size: 14px; letter-spacing: 0.16em; text-transform: uppercase; color: #4E6368">{head}</p>{inner}</div>'
        out.append(f'''<li class="sp-row sp-rowgrid" style="gap: 14px clamp(32px, 4vw, 64px); padding: clamp(28px, 3vw, 40px) clamp(8px, 1.5vw, 24px); border-bottom: 1px solid rgba(78, 99, 104, 0.4)">
<div><h3 style="margin: 0; font-family: 'Cormorant Infant', Garamond, serif; font-weight: 400; font-size: clamp(30px, 2.6vw, 38px); line-height: 1.1; color: #121414">{name}</h3>{subhtml}</div>
{cell(colA, a)}
{cell(colB, b)}
</li>''')
    return f'''<!-- COMPARISON ROWS -->
<section aria-labelledby="rows-title" style="background: #FAFAF8">
<div style="width: 100%; max-width: 1680px; margin: 0 auto; padding: clamp(80px, 9vw, 128px) clamp(20px, 5vw, 72px); display: flex; flex-direction: column; gap: clamp(40px, 5vw, 64px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 20px 64px">
<div style="flex: 1 1 420px; min-width: 0; display: flex; flex-direction: column; gap: 20px">
{label(lbl)}
<h2 id="rows-title" style="margin: 0; font-family: 'Cormorant Infant', Garamond, serif; font-weight: 300; font-size: clamp(40px, 4.6vw, 70px); line-height: 1.04; color: #121414; text-wrap: balance">{h2}</h2>
</div>
<p style="margin: 0; flex: 1.3 1 480px; min-width: 0; font-size: 19px; line-height: 1.7; color: #1F2426">{intro}</p>
</div>
<ul class="sp-reveal" style="list-style: none; margin: 0; padding: 0; border-top: 1px solid rgba(78, 99, 104, 0.4)">
{chr(10).join(out)}
</ul>
{after}
</div>
</section>'''

def closing(h2, body):
    return f'''<!-- CLOSING (simple enquiry band) -->
<section aria-labelledby="cta-title" style="position: relative; overflow: hidden; background: #FAFAF8">
<div aria-hidden="true" style="position: absolute; left: -40px; bottom: -40px; width: min(1000px, 100vw); transform: rotate(180deg); pointer-events: none; z-index: 0">
<img src="{PALM}" alt="" width="1800" height="1200" loading="lazy" style="width: 100%; height: auto; opacity: 0.12; mix-blend-mode: multiply">
</div>
<div class="sp-reveal" style="position: relative; z-index: 1; width: 100%; max-width: 1680px; margin: 0 auto; padding: clamp(88px, 10vw, 136px) clamp(20px, 5vw, 72px); display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 36px clamp(48px, 7vw, 120px)">
<div style="flex: 1.4 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 24px">
{label('Get in Touch')}
<h2 id="cta-title" style="margin: 0; font-family: 'Cormorant Infant', Garamond, serif; font-weight: 300; font-size: clamp(42px, 5vw, 76px); line-height: 1.02; color: #121414; text-wrap: balance">{h2}</h2>
<p style="margin: 0; font-size: 20px; line-height: 1.7; color: #1F2426">{body}</p>
</div>
<div style="flex: 0 1 auto; min-width: 0; display: flex; flex-direction: column; align-items: flex-start; gap: 18px">
{btn_primary()}
<p style="margin: 0; font-size: 17px; line-height: 1.6; color: #1F2426">Or email me at <a href="mailto:info@sullivanparkdesign.com" style="color: #4E6368; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 5px">info@sullivanparkdesign.com</a>.</p>
</div>
</div>
</section>'''

def extract(s, start, end):
    a=s.index(start); b=s.index(end,a); return s[a:b]

def assemble(base, title, desc, main, footer_current, extra_css=''):
    s=base
    s=re.sub(r'<title>.*?</title>', f'<title>{title}</title>', s, 1)
    s=re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', s, 1)
    if extra_css: s=s.replace('</style>\n</helmet>', extra_css+'</style>\n</helmet>',1)
    a=s.index('<main id="main">'); b=s.index('</main>')+len('</main>')
    s=s[:a]+'<main id="main">\n\n'+main+'\n\n</main>'+s[b:]
    s=s.replace(' aria-current="page" style="color: #121414; text-decoration: none; font-size: 18px; line-height: 1.5">',' style="color: #121414; text-decoration: none; font-size: 18px; line-height: 1.5">')
    s=s.replace(f'<a class="sp-flink" href="{footer_current}" style=', f'<a class="sp-flink" href="{footer_current}" aria-current="page" style=',1)
    return s

# ---------------- BRAND ----------------
brand_faq=extract(brand_old,'<!-- FAQ -->','<!-- CLOSING')
twoways=extract(brand_old,'<!-- TWO STARTING POINTS -->','<!-- FAQ -->')
# restyle two-ways for a light (#ECEEED) band like the Website Design detail list
twoways=(twoways.replace('class="sp-on-dark" style="position: relative; overflow: hidden; background: #4E6368; color: #FFFFFF"','style="position: relative; overflow: hidden; background: #ECEEED; color: #121414"')
 .replace('filter: brightness(0) invert(1); opacity: 0.07','opacity: 0.1; mix-blend-mode: multiply')
 .replace('color: #FFFFFF"><span aria-hidden="true" style="display: block; width: 40px; height: 1px; background: #FFFFFF"></span>','color: #4E6368"><span aria-hidden="true" style="display: block; width: 40px; height: 1px; background: #4E6368"></span>')
 .replace('color: #FFFFFF; text-wrap: balance">Two ways <em style="font-style: italic; color: #DCE4E5">','color: #121414; text-wrap: balance">Two ways <em style="font-style: italic; color: #4E6368">')
 .replace('border-top: 1px solid rgba(255, 255, 255, 0.4)','border-top: 1px solid rgba(78, 99, 104, 0.45)')
 .replace('line-height: 1.15; color: #FFFFFF">','line-height: 1.15; color: #121414">')
 .replace('font-size: 19px; line-height: 1.7; color: #FFFFFF">','font-size: 19px; line-height: 1.7; color: #1F2426">')
 .replace('font-size: 18px; line-height: 1.7; color: #DCE4E5">','font-size: 18px; line-height: 1.7; color: #1F2426">')
 .replace('style="color: #FFFFFF; text-decoration: underline;','style="color: #4E6368; text-decoration: underline;'))

brand_main='\n\n'.join([
 hero('Brand &amp; Marketing Design','A consistent identity across <em style="font-style: italic; color: #4E6368">your website and marketing</em>',
      'For businesses that need a clear visual direction or help carrying an established look into everyday marketing. I work with colour, typography, imagery and layout to create materials that feel connected.',
      '/_blob/904617f7e11e4609441ca9dacbaac242','The Shop the Den page on The Rooster Den Co website, with a fringed western handbag and the headline Made To Be Noticed',1600,1040,
      'theroosterdenco.com/pages/shop-the-den','/_blob/b71bb3c923babc219a3b39bb7c0f740d','The same Rooster Den Co page on a phone',
      'The Rooster Den Co','Shopify redesign · SEO · Google Business Profile setup',PORT,'https://theroosterdenco.com/pages/shop-the-den','theroosterdenco.com'),
 approach('The Approach','Built around how you want <em style="font-style: italic; color: #4E6368">to be seen</em>',
      ['I translate the way you want your business to feel into colour, typography, imagery and design.',
       'That visual direction carries through your website, social content, newsletters, ads and printed materials, so your business feels recognisable wherever people find it.']),
 work_section('Selected Work','One look, <em style="font-style: italic; color: #DCE4E5">carried everywhere</em>',[
   work_item('proj-smash',False,'smashtheatreschool.ca/smash-musical-theatre-news','/_blob/761082449bb2a3217b0051642b4aeca2','The SMASH Blog page, with a navy background, serif headline and an Elf The Musical JR. poster',
             '/_blob/e75f9d2269ba8ccc8d243f9dff8d411e','The SMASH Blog page on a phone','Performing Arts','SMASH Performing Arts Studio','Custom-coded website · Ongoing SEO &amp; marketing',
             ['A navy, purple and gold palette with elegant serif headlines, used consistently across the site','Monthly newsletters that share studio news and dates with families','Ongoing support with blogs and social media'],
             SMP,'https://www.smashtheatreschool.ca/','smashtheatreschool.ca'),
   work_item('proj-hamish',True,'hamishross.com/real-estate-marketing','/_blob/58ce49b0e881dd22837c67d61676c190','The Real Estate Marketing page on the Hamish Ross website, with the headline Bigger, better, bolder marketing',
             '/_blob/edbd0350d8647fd8e4906c294896664f','The Hamish Ross marketing page on a phone','Real Estate','Hamish Ross Real Estate','Custom-coded website · Ongoing SEO &amp; marketing',
             ['A high-end luxury identity, carried from page to page','A refined serif and gold-accent style across the website','Ongoing support with blogs, social media and newsletters'],
             HRP,'https://www.hamishross.com/real-estate-marketing','hamishross.com')]),
 rows_section('What It Covers','From direction <em style="font-style: italic; color: #4E6368">to finished materials</em>',
      'The work can start with a new direction or build on the look you already have. We’ll agree on the specific pieces as part of the project scope.',
      [('Visual brand direction','','A clear direction for how your business looks and feels, based on how you want it to be seen.','Your website, social content and marketing materials.'),
       ('Colour and typography','','A palette and type pairing chosen to work together.','On screen and in print.'),
       ('Social graphics and ads','','Designs for social content and ads that clearly belong to the same business.','Social media and online ads.'),
       ('Newsletter and print design','','Newsletter layouts and printed materials that carry the same visual direction.','Email newsletters and printed materials.')],
      'What it is','Where it shows up',
      after='<p class="sp-reveal" style="margin: 0; font-family: \'Cormorant Infant\', Garamond, serif; font-style: italic; font-size: clamp(21px, 1.8vw, 25px); line-height: 1.45; color: #4E6368">This service covers visual direction and marketing design. It doesn’t include logo creation.</p>'),
 twoways.strip(),
 brand_faq.strip(),
 closing('Let’s talk <em style="font-style: italic; color: #4E6368">about your brand</em>','Tell me how you’d like your business to feel and where your marketing appears today.')
])
brand=assemble(wd,'Brand &amp; Marketing Design in Vancouver | Sullivan Park Design',
  'Brand and marketing design from Sullivan Park Design in Vancouver: visual brand direction, colour and typography, social graphics, ads, newsletters and print design.',
  brand_main,'Brand-Marketing-Design.dc.html')
open(B+'Brand-Marketing-Design.dc.html','w').write(brand)

# ---------------- SEO ----------------
seo_faq=extract(seo_old,'<!-- FAQ -->','<!-- CLOSING')
markers='''<span class="sp-marker" aria-hidden="true" style="left: 43%; top: 2.2%">1</span>
<span class="sp-marker" aria-hidden="true" style="left: 58%; top: 16.5%">2</span>
<span class="sp-marker" aria-hidden="true" style="left: 26%; top: 45%">3</span>
<span class="sp-marker" aria-hidden="true" style="left: 33.8%; top: 87%">4</span>'''
notes=[('Local areas, named clearly','White Rock, South Surrey, Ocean Park and nearby neighbourhoods appear at the top of the site.'),
       ('Navigation that reflects what people look for','Market Report and Journal sit in the main menu alongside listings, buying and selling.'),
       ('One clear page heading','The page says exactly what it is, so visitors and search engines know where they’ve landed.'),
       ('Descriptive, local article titles','Titles like the monthly White Rock and South Surrey market report say exactly what each article covers.')]
legend='<ol style="list-style: none; margin: 8px 0 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(240px, 100%), 1fr)); gap: 20px clamp(24px, 3vw, 40px)">'+''.join(
  f'<li style="display: flex; gap: 14px"><span aria-hidden="true" class="sp-marker sp-marker-static">{i+1}</span><span style="display: flex; flex-direction: column; gap: 4px"><span style="font-family: \'Cormorant Infant\', Garamond, serif; font-size: 22px; line-height: 1.2; color: #121414">{t}</span><span style="font-size: 16px; line-height: 1.6; color: #1F2426">{d}</span></span></li>' for i,(t,d) in enumerate(notes))+'</ol>'
geo=extract(seo_old,'<!-- SEO AND GEO -->','<!-- FAQ -->')
geo=(geo.replace('class="sp-on-dark" style="position: relative; overflow: hidden; background: #4E6368; color: #FFFFFF"','style="position: relative; overflow: hidden; background: #ECEEED; color: #121414"')
 .replace('filter: brightness(0) invert(1); opacity: 0.07','opacity: 0.1; mix-blend-mode: multiply')
 .replace('color: #FFFFFF"><span aria-hidden="true" style="display: block; width: 40px; height: 1px; background: #FFFFFF"></span>','color: #4E6368"><span aria-hidden="true" style="display: block; width: 40px; height: 1px; background: #4E6368"></span>')
 .replace('color: #FFFFFF; text-wrap: balance">The same foundation, <em style="font-style: italic; color: #DCE4E5">','color: #121414; text-wrap: balance">The same foundation, <em style="font-style: italic; color: #4E6368">')
 .replace('font-size: 19px; line-height: 1.7; color: #FFFFFF">','font-size: 19px; line-height: 1.7; color: #1F2426">')
 .replace('border-top: 1px solid rgba(255, 255, 255, 0.4)','border-top: 1px solid rgba(78, 99, 104, 0.45)')
 .replace('border-bottom: 1px solid rgba(255, 255, 255, 0.22)','border-bottom: 1px solid rgba(18, 20, 20, 0.12)')
 .replace('line-height: 1.15; color: #FFFFFF">','line-height: 1.15; color: #121414">')
 .replace('font-size: 17px; line-height: 1.6; color: #FFFFFF">','font-size: 17px; line-height: 1.6; color: #1F2426">')
 .replace('text-transform: uppercase; color: #DCE4E5">','text-transform: uppercase; color: #4E6368">'))
seo_main='\n\n'.join([
 hero('SEO','Helping the right customers <em style="font-style: italic; color: #4E6368">find you</em>',
      'Good SEO starts with knowing what your customers search for. I research the words they use, organize your pages around their questions and refine your content so search engines, and the AI tools people now ask for recommendations, can understand what you offer.',
      '/_blob/c5995f733ebb06f0a46185b48e8815e1','The Journal page on the Hamish Ross Real Estate website, with local area names, a Journal heading and market report articles',1440,900,
      'hamishross.com/white-rock-real-estate-blog','/_blob/ceb671628baf2dc9ce90696e82d970e4','The Hamish Ross Journal page on a phone',
      'Hamish Ross Real Estate','Ongoing SEO &amp; marketing',HRP,'https://www.hamishross.com/white-rock-real-estate-blog','hamishross.com',
      markers=markers, legend=legend),
 approach('The Approach','Steady, practical <em style="font-style: italic; color: #4E6368">search work</em>',
      ['SEO isn’t about tricks or quick fixes. It’s about making your website genuinely useful and easy for search engines to understand.',
       'I start by learning how your customers search: the words they use, the questions they ask and what they hope to find. Then I make sure your pages answer those questions clearly and are organized in a way search engines can follow.']),
 work_section('Selected Work','Search work <em style="font-style: italic; color: #DCE4E5">on recent websites</em>',[
   work_item('proj-rooster',False,'theroosterdenco.com/collections/all','/_blob/ee32ca664eb227c36da54285d51c67f1','The products page on The Rooster Den Co online store',
             '/_blob/08fa071b6c00d9dac40df7b84e77bd8a','The Rooster Den Co products page on a phone','Online Retail','The Rooster Den Co','Shopify redesign · SEO · Google Business Profile setup',
             ['Page-by-page SEO across the redesigned store','On-page and technical SEO','Google Business Profile setup to support the store’s visibility'],
             PORT,'https://theroosterdenco.com/','theroosterdenco.com'),
   work_item('proj-smash',True,'smashtheatreschool.ca/schedule','/_blob/873e26c61cfcfeaa7b98375cf3458f8f','The Class Schedule page on the new SMASH Performing Arts Studio website',
             '/_blob/e13b5f0c032070088305da2f48b61b13','The SMASH Class Schedule page on a phone','Performing Arts','SMASH Performing Arts Studio','Custom-coded website · Ongoing SEO &amp; marketing',
             ['Page titles that name the programmes and the areas families search in, such as South Surrey and White Rock','A blog with news and stories for musical theatre families','Ongoing support with SEO, blogs, social media and newsletters'],
             SMP,'https://www.smashtheatreschool.ca/','smashtheatreschool.ca')]),
 rows_section('How I Work','What I assess, improve <em style="font-style: italic; color: #4E6368">and maintain</em>',
      'Three parts that build on each other, whether your website is brand new or has been around for years.',
      [('Assess','Understanding where you are now','How your customers search, and how your pages are organized today.',['The words and questions your customers use','Page titles, headings and descriptions','Where your content answers customer questions, and where it doesn’t yet']),
       ('Improve','Making each page clearer','Clearer pages that search engines can follow.',['Clear page titles, headings and descriptions','Pages organized around the questions customers ask','Refined content, so your offer is easy to understand']),
       ('Maintain','Building on it over time','Steady improvements as your business and website change.',['Content planning, from service pages to blog articles','Regular improvements over time','Blogs and website content as part of <a href="Services.dc.html#ongoing-title" style="color: #4E6368; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 4px">ongoing support</a>'])],
      'In short','What it includes'),
 geo.strip(),
 seo_faq.strip(),
 closing('Let’s talk <em style="font-style: italic; color: #4E6368">about being found</em>','Tell me about your website and the customers you’d like to reach, and we’ll talk about where to start.')
])
marker_css='''.sp-marker{position:absolute;transform:translate(-50%,-50%);width:30px;height:30px;border-radius:50%;background:#4E6368;color:#FFFFFF;border:2px solid #FFFFFF;box-shadow:0 6px 16px rgba(18,28,30,0.3);display:inline-flex;align-items:center;justify-content:center;font-family:'Abel','Arial Narrow',sans-serif;font-size:15px;line-height:1}
.sp-marker-static{position:static;transform:none;flex:none;margin-top:2px;box-shadow:none;border-color:#4E6368}
@media (max-width: 760px){.sp-marker{width:20px;height:20px;font-size:11px;border-width:1.5px}.sp-marker-static{width:30px;height:30px;font-size:15px}}
'''
seo=assemble(wd,'SEO Services in Vancouver | Sullivan Park Design',
  'Practical SEO from Sullivan Park Design in Vancouver: keyword research, on-page SEO, page and content structure and content planning, so the right customers can find your business.',
  seo_main,'SEO.dc.html',marker_css)
open(B+'SEO.dc.html','w').write(seo)

# ---------------- View Project links on Home + Website Design ----------------
for f in ['Main.dc.html','Website-Design.dc.html']:
    s=open(B+f).read()
    s=s.replace(f'<a class="sp-btn sp-btn-line" href="{PORT}" aria-label="View Project, Hamish Ross Real Estate"',f'<a class="sp-btn sp-btn-line" href="{HRP}" aria-label="View Project, Hamish Ross Real Estate"')
    s=s.replace(f'<a class="sp-btn sp-btn-line" href="{PORT}" aria-label="View Project, SMASH Performing Arts Studio"',f'<a class="sp-btn sp-btn-line" href="{SMP}" aria-label="View Project, SMASH Performing Arts Studio"')
    s=s.replace(f'<a class="sp-btn sp-btn-ghost" href="{PORT}" aria-label="View Project, SMASH Performing Arts Studio"',f'<a class="sp-btn sp-btn-ghost" href="{SMP}" aria-label="View Project, SMASH Performing Arts Studio"')
    # home portfolio screenshot links for HR and SMASH
    s=s.replace(f'<a class="sp-shot" href="{PORT}" tabindex="-1" style="display: block; flex: 1.9 1 560px;',f'<a class="sp-shot" href="{HRP}" tabindex="-1" style="display: block; flex: 1.9 1 560px;')
    open(B+f,'w').write(s)
    print(f, 'HR project links', s.count(HRP), 'SMASH project links', s.count(SMP))

# SMASH screenshot link on home (second sp-shot that precedes SMASH image)
s=open(B+'Main.dc.html').read()
i=s.index('aria-labelledby="proj-smash"'); j=s.index(f'href="{PORT}" tabindex="-1"', i)
s=s[:j]+f'href="{SMP}" tabindex="-1"'+s[j+len(f'href="{PORT}" tabindex="-1"'):]
open(B+'Main.dc.html','w').write(s)

for f in ['Brand-Marketing-Design.dc.html','SEO.dc.html']:
    s=open(B+f).read()
    for t in ['div','section','ul','ol','dl','figure','a','article','sc-if','span']:
        o=len(re.findall(r'<%s[\s>]'%t,s)); c=s.count('</%s>'%t)
        if o!=c: print('MISMATCH',f,t,o,c)
    print(f,'ok', 'dash',len(re.findall(r'—|–',s)), 'LetsTalk',len(re.findall(r'>Let’s Talk<',s)), 'FAQ', s.count('class="sp-faq-btn"'), 'FAQ_COUNT', re.search(r'FAQ_COUNT = (\d+)',s).group(1))
