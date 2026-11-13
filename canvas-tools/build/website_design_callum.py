"""Adds (or refreshes) Callum Frost as the third Selected Work item on the Website Design page, with a quiet
link to the Actor Websites page under it. Built from the SMASH item so it matches exactly.
Run: python3 build/website_design_callum.py canvas/project   (then nav_upgrade.py)"""
import os, re, sys
ROOT = sys.argv[1]
p = os.path.join(ROOT, 'Website-Design.dc.html'); s = open(p).read()
s = re.sub(r'\n<article class="sp-reveal" aria-labelledby="proj-callum".*?</article>', '', s, flags=re.S)
i = s.index('<article class="sp-reveal" aria-labelledby="proj-smash"'); j = s.index('</article>', i) + 10
a = s[i:j]

def swap(old, new):
    global a
    assert a.count(old) == 1, old[:60]
    a = a.replace(old, new)

swap('aria-labelledby="proj-smash"', 'aria-labelledby="proj-callum"')
swap('>smashtheatreschool.ca</span>', '>callumfrost.com</span>')
swap(re.search(r'<img src="/_blob/dd8f707bf480ddbc8b5a593bf32382ff"[^>]*?width="1600" height="1000"', a).group(0),
     '<img src="/_blob/d3978c904a489af5909028a3ecb4bb5a" alt="The Callum Frost homepage on a desktop screen, opening with a full-width black and white headshot" width="1800" height="1125"')
swap(re.search(r'<img src="/_blob/cfdfde9c1ac51fff0423b636bb1dec6e"[^>]*?width="540" height="1169"', a).group(0),
     '<img src="/_blob/d9565222a636eaef6c6bdb26170739fa" alt="The Callum Frost homepage on a phone" width="780" height="1688"')
swap('>Performing Arts</p>', '>Actor &amp; Voice-Over Artist</p>')
swap('id="proj-smash"', 'id="proj-callum"')
swap('>SMASH Performing Arts Studio</h3>', '>Callum Frost</h3>')
swap('>Custom-coded website · Ongoing SEO &amp; marketing</p>', '>Custom-coded website · Copywriting · Ongoing updates</p>')
lis = re.findall(r'(<li [^>]*>)(.*?)</li>', a)
assert len(lis) == 3
for (tag, old), new in zip(lis, ['A black and white design rebuilt from Squarespace in custom code, keeping the look he loves',
                                 'Film-inspired details, like a running timecode on the homepage and film-strip photo frames',
                                 'His acting resume, all the copy and updates whenever he has new photos or credits']):
    swap(tag + old + '</li>', tag + new + '</li>')
swap('href="Smash.dc.html" aria-label="View Project, SMASH Performing Arts Studio"', 'href="Callum-Frost.dc.html" aria-label="View Project, Callum Frost"')
swap('href="https://www.smashtheatreschool.ca/" aria-label="Visit Website, smashtheatreschool.ca"',
     'href="https://sullivanparkdesign.github.io/callumfrost/" aria-label="Visit Website, the new Callum Frost website"')
# the quiet actor link, under Callum's buttons
k = a.rindex('</div>\n</div>\n</article>')
NOTE = ('\n<p style="margin: 6px 0 0; padding-top: 18px; border-top: 1px solid rgba(255, 255, 255, 0.28); font-size: 17px; line-height: 1.6; color: rgba(255, 255, 255, 0.86)">'
        'Are you an actor? I also offer <a class="sp-link" href="Actor-Websites.dc.html" style="color: #FFFFFF; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 5px">ready-made actor websites</a>.</p>')
a = a[:k] + '</div>' + NOTE + '\n</div>\n</article>'
assert a.count('<article') == 1 and a.endswith('</article>')
r = s.index('<article class="sp-reveal" aria-labelledby="proj-rooster"'); e = s.index('</article>', r) + 10
s = s[:e] + '\n' + a + s[e:]
open(p, 'w').write(s)
print('website design: Callum added')
