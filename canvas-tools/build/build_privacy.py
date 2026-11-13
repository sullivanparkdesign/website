"""Privacy Policy page (Privacy.dc.html), cloned from the Resources page shell.
Run: python3 build/build_privacy.py canvas/project   (then nav_upgrade.py)"""
import os, re, sys

ROOT = sys.argv[1]
SERIF = "'Cormorant Infant', Garamond, serif"
TEAL, INK, BODY, MUTED = '#4E6368', '#121414', '#1F2426', '#4E5558'
WRAP = 'width: 100%; max-width: 1680px; margin: 0 auto'
GUTTER = 'clamp(20px, 5vw, 72px)'
MAIL = f'<a href="mailto:info@sullivanparkdesign.com" style="color: {TEAL}; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 4px">info@sullivanparkdesign.com</a>'

SECTIONS = [
    ('What I collect', [
        'When you use the contact form or email me, I receive the details you choose to share. That’s usually your name, email address, website, the service you’re interested in and your message.',
        'I don’t ask for payment details or sensitive personal information through this website.']),
    ('How I use it', [
        'I use your details to reply to your enquiry, to discuss and provide the work you’ve asked about, and to keep basic business records.',
        'I don’t sell, rent or trade your personal information, and I won’t add you to a mailing list without your permission.']),
    ('Services that help run this website', [
        'A few trusted services handle information on my behalf. Cloudflare hosts this website, a form service delivers contact form messages to my inbox, and my email provider stores our correspondence.',
        'This website also loads its fonts from Google Fonts, which means your browser connects to Google’s servers when a page loads. Some of these providers may process information outside Canada.']),
    ('Cookies and analytics', [
        'This website doesn’t use advertising cookies or tracking pixels. If I add website analytics in the future, I’ll update this page to explain what’s collected and how to opt out.']),
    ('How long I keep it', [
        'I keep enquiries and project correspondence only as long as I need them to respond to you, provide my services and keep proper business records.']),
    ('Your choices', [
        f'You can ask to see the personal information I hold about you, ask me to correct it or ask me to delete it, unless I need to keep it for legal or business reasons. Email me at {MAIL} and I’ll respond as soon as I can.']),
    ('Keeping it safe', [
        'I take reasonable steps to protect your information, including secure (HTTPS) connections on this website and trusted service providers. No way of sending or storing information online is completely secure, but I work to keep yours safe.']),
    ('Changes to this policy', [
        'I may update this page from time to time. The date at the top shows when it last changed.']),
    ('Questions', [
        f'If you have any questions about your privacy, email me at {MAIL}.']),
]


def label(text):
    return f'<p style="margin: 0; display: flex; align-items: center; gap: 16px; font-size: 15px; letter-spacing: 0.2em; text-transform: uppercase; color: {TEAL}"><span aria-hidden="true" style="display: block; width: 40px; height: 1px; background: {TEAL}"></span>{text}</p>'


def build():
    p = os.path.join(ROOT, 'Journal.dc.html'); s = open(p).read()
    secs = '\n'.join(f'''<section aria-labelledby="pp-{i}" style="display: flex; flex-direction: column; gap: 14px; padding-top: 32px; border-top: 1px solid rgba(78, 99, 104, 0.25)">
<h2 id="pp-{i}" style="margin: 0; font-family: {SERIF}; font-weight: 400; font-size: clamp(28px, 2.6vw, 38px); line-height: 1.15; color: {INK}">{title}</h2>
{''.join(f'<p style="margin: 0; font-size: 19px; line-height: 1.8; color: {BODY}">{t}</p>' for t in paras)}
</section>''' for i, (title, paras) in enumerate(SECTIONS))
    palm = '<img class="sp-sway" src="/_blob/fddc24a18e2595d21f63da9f1d7bf0d5" alt="" width="1800" height="1200" style="position: absolute; top: -20px; right: -20px; width: min(1320px, 110vw); height: auto; max-width: none; opacity: 0.16; mix-blend-mode: multiply; pointer-events: none; z-index: 0">'
    main = f'''<!-- HERO -->
<section aria-labelledby="page-title" style="position: relative; overflow: hidden; background: #FAFAF8">
{palm}
<div style="position: relative; z-index: 1; {WRAP}; padding: clamp(140px, 12vw, 172px) {GUTTER} clamp(56px, 6vw, 80px); display: flex; flex-direction: column; gap: 26px">
{label('Your Privacy')}
<h1 id="page-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(54px, 7.4vw, 120px); line-height: 0.98; letter-spacing: -0.015em; color: {INK}">Privacy <em style="font-style: italic; color: {TEAL}">Policy</em></h1>
<p style="margin: 0; font-size: 16px; letter-spacing: 0.08em; color: {MUTED}">Last updated November 2026</p>
</div>
</section>

<!-- POLICY -->
<section aria-label="Privacy policy details" style="background: #FFFFFF">
<div style="{WRAP}; padding: clamp(56px, 6vw, 88px) {GUTTER} clamp(88px, 10vw, 140px); display: flex; justify-content: center">
<div style="flex: 1 1 auto; max-width: 820px; min-width: 0; display: flex; flex-direction: column; gap: 36px">
<p style="margin: 0; font-size: 21px; line-height: 1.75; color: {BODY}">Your privacy matters to me. This page explains what information I collect through this website, how I use it and the choices you have.</p>
{secs}
</div>
</div>
</section>'''
    a = s.index('<main id="main">'); b = s.index('</main>') + len('</main>')
    s = s[:a] + '<main id="main">\n' + main + '\n</main>' + s[b:]
    t = 'Privacy Policy | Sullivan Park Design'
    d = 'How Sullivan Park Design collects, uses and protects the personal information you share through this website.'
    s = re.sub(r'<title>.*?</title>', f'<title>{t}</title>', s, count=1)
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{d}">', s, count=1)
    s = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{t}">', s, count=1)
    s = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{d}">', s, count=1)
    s = re.sub(r'"\$preview":\{"width":1440,"height":\d+\}', '"$preview":{"width":1440,"height":3400}', s, count=1)
    assert '—' not in re.sub(r'<[^>]+>', ' ', main) and 'bespoke' not in main.lower()
    open(os.path.join(ROOT, 'Privacy.dc.html'), 'w').write(s)
    print('written Privacy.dc.html')


build()
# Contact form's privacy link now points at the page
cp = os.path.join(ROOT, 'Contact.dc.html'); c = open(cp).read()
if 'href="#privacy-policy"' in c:
    open(cp, 'w').write(c.replace('href="#privacy-policy"', 'href="Privacy.dc.html"')); print('contact link updated')
