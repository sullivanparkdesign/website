"""Shared building blocks for the portfolio case study pages (SMASH, Rooster Den).

Mirrors the Hamish Ross page so all three read as one family, while each page
wears its client's colours. Section helpers return HTML strings.
"""
import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import build_hr as HR  # reuse helpers and the case study CSS

SERIF = HR.SERIF
ARROW = HR.ARROW
EXT = HR.EXT
WRAP = HR.WRAP
PORTFOLIO = HR.PORTFOLIO
CASE_CSS = HR.CSS
COMPONENT = HR.COMPONENT
SECTION_PAD = 'padding-top: clamp(88px, 10vw, 136px); padding-bottom: clamp(88px, 10vw, 136px)'


def label(text, color='#4E6368'):
    return HR.label(text, color)


def h2(id_, main, em, color='#121414', em_color='#4E6368', size='clamp(42px, 4.8vw, 76px)'):
    return HR.h2(id_, main, em, color, em_color, size)


def p(text, color='#1F2426', size='19px'):
    return HR.p(text, color, size)


def desk(img, alt, url, w=1600, h=1000, dark=False, lazy=True, priority=False, extra_cls=''):
    return HR.desk(img, alt, w=w, h=h, dark=dark, url=url, extra_cls=extra_cls, lazy=lazy, priority=priority)


def phone(img, alt):
    return HR.phone(img, alt)


def hero(*, bg, dark, label_text, accent, title_main, title_em, em_color, lede, visit_url, visit_label, meta, desk_img, desk_alt, phone_img, phone_alt, url, glow, line_color):
    txt = '#FFFFFF' if dark else '#121414'
    sub = 'rgba(246, 243, 238, 0.86)' if dark else '#1F2426'
    rule = 'rgba(246, 243, 238, 0.16)' if dark else 'rgba(18, 20, 20, 0.14)'
    dd = '#FFFFFF' if dark else '#121414'
    meta_html = '\n'.join(
        f'<div><dt style="margin: 0 0 10px; font-size: 13px; letter-spacing: 0.2em; text-transform: uppercase; color: {accent}">{k}</dt><dd style="margin: 0; font-size: 18px; line-height: 1.55; color: {dd}">{v}</dd></div>'
        for k, v in meta)
    cls = 'sp-on-dark hr-hero' if dark else 'hr-hero'
    return f'''<!-- HERO -->
<section class="{cls}" aria-labelledby="page-title" style="position: relative; z-index: 2; background: {bg}; color: {txt}">
<div aria-hidden="true" style="position: absolute; inset: 0; overflow: hidden; pointer-events: none">{glow}</div>
<div style="position: relative; {WRAP}; padding-top: clamp(150px, 13vw, 190px); display: flex; flex-direction: column; gap: clamp(48px, 6vw, 80px)">
<div style="display: flex; flex-wrap: wrap; align-items: flex-end; gap: 32px clamp(48px, 7vw, 120px)">
<div style="flex: 1.4 1 560px; min-width: 0; display: flex; flex-direction: column; gap: 28px">
{label(label_text, accent)}
<h1 id="page-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(56px, 7.6vw, 128px); line-height: 0.98; letter-spacing: -0.02em; color: {txt}; text-wrap: balance">{title_main} <em style="font-style: italic; color: {em_color}">{title_em}</em></h1>
</div>
<div style="flex: 1 1 380px; min-width: 0; display: flex; flex-direction: column; align-items: flex-start; gap: 26px; padding-bottom: 10px">
<p style="margin: 0; font-size: 21px; line-height: 1.65; color: {sub}">{lede}</p>
<a class="sp-ext hr-visit cs-visit" href="{visit_url}" aria-label="Visit Website, {visit_label}" style="display: inline-flex; align-items: center; gap: 10px; min-height: 44px; font-size: 16px; letter-spacing: 0.14em; text-transform: uppercase; color: {accent}; text-decoration: none; border-bottom: 1px solid currentColor">Visit Website{EXT}</a>
</div>
</div>
<dl class="hr-meta" style="margin: 0; padding: 28px 0 0; border-top: 1px solid {rule}">
{meta_html}
</dl>
<figure class="hr-stage sp-stagebox" style="position: relative; margin: 0 0 calc(-1 * clamp(90px, 12vw, 200px)); padding: 0 0 clamp(28px, 4vw, 56px)">
<span aria-hidden="true" class="hr-frame-line" style="position: absolute; top: clamp(18px, 2.4vw, 32px); left: calc(-1 * clamp(12px, 1.6vw, 24px)); width: 86%; bottom: calc(clamp(28px, 4vw, 56px) - clamp(18px, 2.4vw, 32px)); border: 1px solid {line_color}"></span>
<div class="sp-desk" style="position: relative; width: 86%">{desk(desk_img, desk_alt, url, 1800, 1125, dark=dark, lazy=False, priority=True)}</div>
<div class="sp-phone" style="position: absolute; right: 1%; bottom: 0; width: clamp(110px, 19%, 280px)">{phone(phone_img, phone_alt)}</div>
</figure>
</div>
</section>
'''


def brief(*, label_text, title_main, title_em, paras, did, num_color, em_color='#4E6368'):
    paras_html = '\n'.join(p(t, size='20px' if i == 0 else '19px') for i, t in enumerate(paras))
    lis = '\n'.join(
        f'<li style="display: flex; gap: 16px; align-items: baseline; padding: 18px 0; border-top: 1px solid rgba(18, 20, 20, 0.14)"><span style="font-family: {SERIF}; font-style: italic; font-size: 22px; color: {num_color}">{i + 1:02d}</span><span style="font-size: 18px; line-height: 1.55; color: #121414">{t}</span></li>'
        for i, t in enumerate(did))
    return f'''<!-- THE BRIEF -->
<section aria-labelledby="brief-title" style="position: relative; z-index: 1; background: #FAFAF8">
<div class="sp-reveal" style="{WRAP}; padding-top: calc(clamp(90px, 12vw, 200px) + clamp(80px, 9vw, 140px)); padding-bottom: clamp(88px, 10vw, 136px); display: flex; flex-wrap: wrap; gap: 48px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 440px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{label(label_text)}
{h2('brief-title', title_main, title_em, em_color=em_color)}
</div>
<div style="flex: 1.2 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 24px">
{paras_html}
<ol class="hr-did" style="list-style: none; margin: 12px 0 0; padding: 0; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0 40px">
{lis}
</ol>
</div>
</div>
</section>
'''


def scroller(*, label_text, title_main, title_em, intro, chapters, numerals, num_color, img, img_w, img_h, alt, url, aria, duration='110s'):
    chap = '\n'.join(
        f'<li style="display: flex; align-items: baseline; gap: 18px; padding: 14px 0; border-top: 1px solid rgba(18, 20, 20, 0.12)"><span style="flex: none; width: 58px; font-family: {SERIF}; font-size: 20px; color: {num_color}">{n}</span><span style="font-size: 18px; line-height: 1.5; color: #121414">{c}</span></li>'
        for n, c in zip(numerals, chapters))
    return f'''<!-- THE HOMEPAGE, START TO FINISH (living screenshot) -->
<section aria-labelledby="scroll-title" style="position: relative; overflow: hidden; background: #ECEEED">
<div style="{WRAP}; {SECTION_PAD}; display: flex; flex-wrap: wrap; align-items: center; gap: 56px clamp(48px, 6vw, 104px)">
<div class="sp-reveal" style="flex: 1 1 340px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{label(label_text)}
{h2('scroll-title', title_main, title_em, size='clamp(40px, 4.2vw, 66px)')}
{p(intro)}
<ol style="list-style: none; margin: 6px 0 0; padding: 0; border-bottom: 1px solid rgba(18, 20, 20, 0.12)">
{chap}
</ol>
</div>
<figure class="sp-reveal hr-scrollbox" style="flex: 2 1 560px; min-width: 0; margin: 0; display: flex; flex-direction: column; gap: 16px">
<div class="sp-device" style="background: #FFFFFF; border: 1px solid rgba(18, 20, 20, 0.14); box-shadow: 0 50px 100px rgba(18, 28, 30, 0.18)">
<div aria-hidden="true" style="height: 34px; padding: 0 16px; display: flex; align-items: center; gap: 7px; border-bottom: 1px solid rgba(18, 20, 20, 0.1)"><span style="width: 9px; height: 9px; border-radius: 50%; background: #CDD3D2"></span><span style="width: 9px; height: 9px; border-radius: 50%; background: #CDD3D2"></span><span style="width: 9px; height: 9px; border-radius: 50%; background: #CDD3D2"></span><span style="margin-left: 12px; font-size: 13px; color: #5A6163">{url}</span></div>
<div class="hr-view" tabindex="0" aria-label="{aria}" style="--cs-dur: {duration}">
<img src="{img}" alt="{alt}" width="{img_w}" height="{img_h}" loading="lazy">
</div>
</div>
<figcaption style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 8px 24px; font-size: 15px; letter-spacing: 0.04em; color: #4E5558"><span>The full homepage, scrolling on its own</span><span class="hr-hint">Hover to pause</span></figcaption>
</figure>
</div>
</section>
'''


def details(*, title_main, title_em, intro, swatches, card1, card2):
    sw = '\n'.join(
        f'<li style="display: flex; flex-direction: column; gap: 14px"><span aria-hidden="true" style="display: block; aspect-ratio: 4 / 5; background: {c}; {"border: 1px solid rgba(18, 20, 20, 0.12); " if light else ""}box-shadow: 0 18px 40px -24px rgba(18, 20, 20, 0.45)"></span>'
        f'<span style="display: flex; flex-direction: column; gap: 2px"><span style="font-family: {SERIF}; font-size: 24px; line-height: 1.2; color: #121414">{n}</span><span style="font-size: 15px; letter-spacing: 0.08em; color: #4E5558">{c}</span></span></li>'
        for n, c, light in swatches)
    return f'''<!-- THE DETAILS (palette and type) -->
<section aria-labelledby="details-title" style="background: #FAFAF8">
<div style="{WRAP}; {SECTION_PAD}; display: flex; flex-direction: column; gap: clamp(48px, 5vw, 72px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 24px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{label('The Details')}
{h2('details-title', title_main, title_em)}
</div>
<div style="flex: 1 1 420px; min-width: 0">{p(intro)}</div>
</div>
<ul class="hr-swatches sp-reveal" style="list-style: none; margin: 0; padding: 0">
{sw}
</ul>
<div class="hr-type sp-reveal">
{card1}
{card2}
</div>
</div>
</section>
'''


def type_card(bg, inner):
    return f'<div style="background: {bg}; padding: clamp(32px, 4vw, 56px); display: flex; flex-direction: column; justify-content: space-between; gap: 40px; min-width: 0">{inner}</div>'


def gallery(*, title_main, title_em, intro, items, url, lab_color):
    gal = '\n'.join(f'''<figure class="sp-reveal hr-gitem {cls}" style="margin: 0; display: flex; flex-direction: column; gap: 20px">
{desk(img, alt, url)}
<figcaption style="display: flex; flex-direction: column; gap: 8px">
<span style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 16px"><span style="font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: {lab_color}">{lab}</span><span style="font-family: {SERIF}; font-size: 26px; line-height: 1.2; color: #121414">{title}</span></span>
<span style="font-size: 18px; line-height: 1.6; color: #1F2426">{cap}</span>
</figcaption>
</figure>''' for img, cls, lab, title, cap, alt in items)
    return f'''<!-- A SAMPLE OF THE PAGES -->
<section aria-labelledby="pages-title" style="background: #FAFAF8">
<div style="{WRAP}; {SECTION_PAD}; display: flex; flex-direction: column; gap: clamp(56px, 6vw, 88px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 24px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{label('A Sample of the Pages')}
{h2('pages-title', title_main, title_em)}
</div>
<div style="flex: 1 1 420px; min-width: 0">{p(intro)}</div>
</div>
<div class="hr-gallery">
{gal}
</div>
</div>
</section>
'''


def phones(*, title_main, title_em, intro, items):
    ph = '\n'.join(phone(img, alt) for img, alt in items)
    return f'''<!-- ON EVERY SCREEN -->
<section aria-labelledby="phones-title" style="position: relative; overflow: hidden; background: #ECEEED">
<img class="sp-sway" src="/_blob/fddc24a18e2595d21f63da9f1d7bf0d5" alt="" width="1800" height="1200" loading="lazy" style="position: absolute; top: -40px; left: -60px; width: min(1100px, 100vw); height: auto; max-width: none; opacity: 0.12; mix-blend-mode: multiply; pointer-events: none; z-index: 0; transform-origin: 0 0">
<div style="position: relative; z-index: 1; {WRAP}; {SECTION_PAD}; display: flex; flex-direction: column; gap: clamp(48px, 6vw, 88px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 24px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 26px">
{label('On Every Screen')}
{h2('phones-title', title_main, title_em)}
</div>
<div style="flex: 1 1 420px; min-width: 0">{p(intro)}</div>
</div>
<div class="hr-phones sp-reveal">
{ph}
</div>
</div>
</section>
'''


def marquee(words, *, bg, color, dot_color, border):
    dot = f'<span style="display: inline-block; width: 7px; height: 7px; border-radius: 50%; background: {dot_color}; margin: 0 clamp(24px, 3vw, 48px); transform: translateY(-0.35em)"></span>'
    run = ''.join(f'<span>{w}</span>{dot}' for w in words)
    return f'''<!-- DECORATIVE TICKER -->
<div class="hr-marquee" aria-hidden="true" style="background: {bg}; border-top: 1px solid {border}; border-bottom: 1px solid {border}; padding: clamp(26px, 3vw, 40px) 0; overflow: hidden">
<div class="hr-track" style="display: inline-flex; align-items: center; white-space: nowrap; font-family: {SERIF}; font-style: italic; font-weight: 300; font-size: clamp(34px, 4vw, 64px); line-height: 1; color: {color}">{run}{run}{run}</div>
</div>
'''


def next_project(*, href, title, sub, img, img_w, img_h, url):
    return f'''<!-- NEXT PROJECT -->
<section aria-labelledby="next-title" style="background: #ECEEED">
<div style="{WRAP}; padding-top: clamp(72px, 8vw, 112px); padding-bottom: clamp(72px, 8vw, 112px)">
<a class="hr-next sp-reveal" href="{href}" style="display: flex; flex-wrap: wrap; align-items: center; gap: 40px clamp(40px, 6vw, 96px); color: #121414; text-decoration: none">
<span style="flex: 1 1 380px; min-width: 0; display: flex; flex-direction: column; gap: 22px">
<span style="display: flex; align-items: center; gap: 16px; font-size: 15px; letter-spacing: 0.2em; text-transform: uppercase; color: #4E6368"><span aria-hidden="true" style="display: block; width: 40px; height: 1px; background: #4E6368"></span>Next Project</span>
<span id="next-title" class="hr-next-title" style="font-family: {SERIF}; font-weight: 300; font-size: clamp(40px, 4.6vw, 72px); line-height: 1.04; color: #121414">{title}</span>
<span style="font-size: 17px; letter-spacing: 0.04em; color: #4E6368">{sub}</span>
<span class="hr-next-go" style="display: inline-flex; align-items: center; gap: 14px; margin-top: 8px; font-size: 15px; letter-spacing: 0.16em; text-transform: uppercase; color: #4E6368">View Project{ARROW}</span>
</span>
<span style="flex: 1.3 1 480px; min-width: 0; display: block">
<span class="sp-device hr-next-shot" style="display: block; background: #FFFFFF; border: 1px solid rgba(18, 20, 20, 0.14); box-shadow: 0 40px 90px rgba(18, 28, 30, 0.16)"><span aria-hidden="true" style="height: 34px; padding: 0 16px; display: flex; align-items: center; gap: 7px; border-bottom: 1px solid rgba(18, 20, 20, 0.1)"><span style="width: 9px; height: 9px; border-radius: 50%; background: #CDD3D2"></span><span style="width: 9px; height: 9px; border-radius: 50%; background: #CDD3D2"></span><span style="width: 9px; height: 9px; border-radius: 50%; background: #CDD3D2"></span><span style="margin-left: 12px; font-size: 13px; color: #5A6163">{url}</span></span><img src="{img}" alt="" width="{img_w}" height="{img_h}" loading="lazy" style="display: block; width: 100%; height: auto"></span>
</span>
</a>
<p class="sp-reveal" style="margin: clamp(40px, 5vw, 64px) 0 0; padding-top: 24px; border-top: 1px solid rgba(18, 20, 20, 0.14)"><a class="sp-link" href="{PORTFOLIO}" style="display: inline-flex; align-items: center; gap: 12px; min-height: 44px; font-size: 15px; letter-spacing: 0.16em; text-transform: uppercase; color: #4E6368; text-decoration: none">Back to All Projects{ARROW}</a></p>
</div>
</section>
'''


def closing(main, em):
    return f'''<!-- CLOSING -->
<section aria-labelledby="cta-title" style="position: relative; overflow: hidden; background: #FAFAF8">
<div aria-hidden="true" style="position: absolute; left: -40px; bottom: -40px; width: min(1000px, 100vw); transform: rotate(180deg); pointer-events: none; z-index: 0">
<img src="/_blob/fddc24a18e2595d21f63da9f1d7bf0d5" alt="" width="1800" height="1200" loading="lazy" style="width: 100%; height: auto; opacity: 0.12; mix-blend-mode: multiply">
</div>
<div class="sp-reveal" style="position: relative; z-index: 1; {WRAP}; {SECTION_PAD}; display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 36px clamp(48px, 7vw, 120px)">
<div style="flex: 1.4 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 24px">
{label('Get in Touch')}
<h2 id="cta-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(42px, 5vw, 76px); line-height: 1.02; color: #121414; text-wrap: balance">{main} <em style="font-style: italic; color: #4E6368">{em}</em></h2>
<p style="margin: 0; font-size: 20px; line-height: 1.7; color: #1F2426">Tell me about your business and what you’d like your website to do.</p>
</div>
<div style="flex: 0 1 auto; min-width: 0; display: flex; flex-direction: column; align-items: flex-start; gap: 18px">
<a class="sp-btn sp-btn-blue" href="Contact.dc.html" style="display: inline-flex; align-items: center; justify-content: center; gap: 14px; min-height: 58px; padding: 0 34px; background: #4E6368; border: 1px solid #4E6368; color: #FFFFFF; text-decoration: none; font-size: 18px; letter-spacing: 0.03em">Enquire About Your Project{ARROW}</a>
<p style="margin: 0; font-size: 17px; line-height: 1.6; color: #1F2426">Or email me at <a href="mailto:info@sullivanparkdesign.com" style="color: #4E6368; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 5px">info@sullivanparkdesign.com</a>.</p>
</div>
</div>
</section>
'''


GENERIC_CSS = '''/* CASE STUDY EXTRAS */
.hr-view img{animation-duration:var(--cs-dur,110s) !important}
.cs-visit:hover{opacity:.75}
.cs-chips{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:10px}
.cs-pages{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:clamp(16px,2.4vw,36px);align-items:start}
.cs-pages > :nth-child(1){transform:rotate(-2deg)}
.cs-pages > :nth-child(2){transform:rotate(1.2deg);margin-top:clamp(0px,4vw,64px)}
.cs-pages > :nth-child(3){transform:rotate(-1deg)}
.cs-pages > :nth-child(4){transform:rotate(1.8deg);margin-top:clamp(0px,4vw,64px)}
.cs-pages img{transition:transform .8s cubic-bezier(.2,.7,.2,1)}
.cs-pages > *:hover img{transform:translateY(-8px)}
@media (max-width: 760px){.cs-pages{grid-template-columns:1fr 1fr}.cs-pages > :nth-child(n){transform:none;margin-top:0}.cs-pages > :nth-child(even){margin-top:36px}}
.cs-loupe-stage{position:relative}
.cs-loupe{position:absolute;right:1.2%;top:calc(50% + 17px);width:34%;transform:translateY(-50%)}
@media (max-width: 760px){.cs-loupe-stage .cs-loupe-desk{width:100% !important}.cs-loupe{position:relative;right:auto;top:auto;transform:none;width:72%;margin:-48px auto 0}}
.cs-portal-stage{position:relative}
.cs-portal-phone{position:absolute;left:0;bottom:-32px;width:clamp(110px,17%,240px)}
@media (max-width: 760px){.cs-portal-stage .cs-portal-desk{width:100% !important;margin-left:0 !important}.cs-portal-phone{position:relative;left:auto;bottom:auto;width:44%;margin:-60px 0 0 6%}}
@media (prefers-reduced-motion: reduce){.cs-pages > :nth-child(n){transform:none}.cs-pages img{transition:none}}
/* /CASE STUDY EXTRAS */'''


def write_page(root, name, *, title, desc, fonts_href, main, extra_css, preview_h, component=None):
    s = open(os.path.join(root, 'Website-Design.dc.html')).read()
    s = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', s, count=1)
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', s, count=1)
    s = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{title}">', s, count=1)
    s = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{desc}">', s, count=1)
    s = s.replace('<helmet>\n', f'<helmet>\n<link rel="stylesheet" href="{fonts_href}">\n', 1)
    st0 = s.index('<style>') + len('<style>'); st1 = s.index('</style>')
    base = re.sub(r'/\* NAV v2 \(generated\) \*/.*?/\* /NAV v2 \*/\n?', '', s[st0:st1], flags=re.S)
    s = s[:st0] + base.rstrip('\n') + '\n' + CASE_CSS + '\n' + GENERIC_CSS + '\n' + extra_css + '\n' + s[st1:]
    m0 = s.index('<main id="main">') + len('<main id="main">'); m1 = s.index('</main>')
    s = s[:m0] + '\n\n' + main + '\n' + s[m1:]
    c0 = s.index('class Component extends DCLogic {'); c1 = s.rindex('</script>')
    s = s[:c0] + (component or COMPONENT) + s[c1:]
    s = re.sub(r'"\$preview":\{"width":1440,"height":\d+\}', '"$preview":{"width":1440,"height":%d}' % preview_h, s, count=1)
    s = s.replace('aria-current="page" ', '')
    open(os.path.join(root, name), 'w').write(s)
    print('written', name, len(s))
    return s
