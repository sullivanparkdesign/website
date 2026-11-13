import re, sys, os
src_dir, out_dir = sys.argv[1], sys.argv[2]
tok = re.compile(r'<sc-if\b[^>]*>|</sc-if>')
def strip_scif(body):
    out = []; pos = 0; stack = []  # stack of booleans: True = keep content
    for m in tok.finditer(body):
        keep_now = all(stack)
        if keep_now: out.append(body[pos:m.start()])
        t = m.group(0)
        if t.startswith('</'):
            if stack: stack.pop()
        else:
            stack.append('hint-placeholder-val="{{false}}"' not in t)
        pos = m.end()
    if all(stack): out.append(body[pos:])
    return ''.join(out)
for f in sys.argv[3:]:
    s = open(os.path.join(src_dir, f)).read()
    style = re.search(r'<style>(.*?)</style>', s, re.S).group(1)
    helm = s[s.index('<helmet>'):s.index('</helmet>')]
    extra_links = ''.join(l for l in re.findall(r'<link [^>]*>', helm) if 'Abel' not in l)
    body = s[s.index('</helmet>') + 9:s.index('</x-dc>')]
    body = strip_scif(body)
    body = body.replace('{{heroTintBg}}', 'rgb(137, 175, 188)').replace('{{heroGradBg}}', 'linear-gradient(0deg, rgba(14, 40, 50, 0.42) 0%, rgba(14, 40, 50, 0.06) 60%, rgba(14, 40, 50, 0) 85%), linear-gradient(90deg, rgba(14, 40, 50, 0.32) 0%, rgba(14, 40, 50, 0.03) 85%)')
    body = re.sub(r'\{\{[^}]+\}\}', '', body).replace(' loading="lazy"', '')
    html = f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Abel&family=Cormorant+Infant:ital,wght@0,300;0,400;0,500;1,300;1,400&display=swap">{extra_links}<style>{style}</style></head><body>{body}</body></html>'''
    open(os.path.join(out_dir, f.replace('.dc.html', '.html')), 'w').write(html)
    print(f, 'divs', len(re.findall(r'<div[\s>]', body)), body.count('</div>'))
