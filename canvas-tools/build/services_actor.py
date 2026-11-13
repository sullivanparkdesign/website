"""NOT IN USE: Natasha asked to keep actor websites off the Services page (2026-11-12). Adds (or refreshes) the Actor Websites band on the Services page, between Ongoing Support and How It Works.
Run: python3 build/services_actor.py canvas/project   (then nav_upgrade.py)"""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import case_common as C
ROOT = sys.argv[1]
p = os.path.join(ROOT, 'Services.dc.html'); s = open(p).read()
s = re.sub(r'<!-- ACTOR WEBSITES \(services\) -->.*?</section>\n', '', s, flags=re.S)
PH = [('486a8a3d6be578c3ac350cb6a2ff6501', 'The Luminous look on a phone'), ('b95e5af154fbc22ab85573cbcf79d9a9', 'The Editorial look on a phone'), ('7631c869597229b71a306cd2c4d838cc', 'The Headliner look on a phone')]
phones = ''.join(f'<div class="sv-aw-phone{" sv-aw-mid" if i == 1 else ""}"><img src="/_blob/{b}" alt="{a}" width="780" height="1688" loading="lazy"></div>' for i, (b, a) in enumerate(PH))
BAND = f'''<!-- ACTOR WEBSITES (services) -->
<section aria-labelledby="actors-title" style="background: #FFFFFF">
<div class="sv-aw" style="width: 100%; max-width: 1680px; margin: 0 auto; padding: clamp(80px, 9vw, 128px) clamp(20px, 5vw, 72px)">
<div class="sv-aw-text sp-reveal">
<p style="margin: 0; display: flex; align-items: center; gap: 16px; font-size: 15px; letter-spacing: 0.2em; text-transform: uppercase; color: #4E6368"><span aria-hidden="true" style="display: block; width: 40px; height: 1px; background: #4E6368"></span>For Actors</p>
<h2 id="actors-title" style="margin: 0; font-family: 'Cormorant Infant', Garamond, serif; font-weight: 300; font-size: clamp(40px, 4.4vw, 66px); line-height: 1.04; color: #121414; text-wrap: balance">Ready-made websites <em style="font-style: italic; color: #4E6368">for actors</em></h2>
<p style="margin: 0; font-size: 19px; line-height: 1.7; color: #1F2426">Choose from three polished looks, each in three colourways, with your own edit screen for headshots, credits and bio. $650 + tax, with your first year of care included. Fully custom actor websites start at $2,000 + tax.</p>
<a class="sp-btn sp-btn-blue" href="Actor-Websites.dc.html" style="align-self: flex-start; display: inline-flex; align-items: center; justify-content: center; gap: 14px; min-height: 58px; padding: 0 34px; background: #4E6368; border: 1px solid #4E6368; color: #FFFFFF; text-decoration: none; font-size: 18px; letter-spacing: 0.03em">See Actor Websites{C.ARROW}</a>
</div>
<div class="sv-aw-phones sp-reveal">{phones}</div>
</div>
</section>
'''
CSS = '''/* ACTOR WEBSITES BAND */
.sv-aw{display:grid;grid-template-columns:minmax(0,1fr);gap:clamp(48px,6vw,72px);align-items:center}
@media (min-width:1000px){.sv-aw{grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);column-gap:clamp(56px,6vw,112px)}}
.sv-aw-text{display:flex;flex-direction:column;gap:24px;min-width:0}
.sv-aw-phones{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(12px,1.6vw,24px);align-items:end;width:100%;max-width:560px;justify-self:center}
.sv-aw-phone{border-radius:26px;overflow:hidden;background:#121414;padding:6px;box-shadow:0 36px 64px -32px rgba(18,28,30,.5)}
.sv-aw-phone img{display:block;width:100%;aspect-ratio:390/844;object-fit:cover;object-position:50% 0;border-radius:20px}
.sv-aw-mid{margin-bottom:clamp(28px,3.6vw,56px)}
'''
a = '<!-- HOW IT WORKS -->'
assert s.count(a) == 1
s = s.replace(a, BAND + a, 1)
if '/* ACTOR WEBSITES BAND */' not in s:
    k = s.index('</style>', s.index('<helmet>')) if '<helmet>' in s else s.index('</style>')
    s = s[:k] + CSS + s[k:]
open(p, 'w').write(s)
print('services band ok')
