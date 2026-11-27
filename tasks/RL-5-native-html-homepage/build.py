from pathlib import Path
import re, hashlib, json

BASE = Path(__file__).resolve().parent
source = (BASE / 'source-original.html').read_text()
root = '#rl-redline-home'
page = 'body.page-id-14'
css = re.search(r'<style>(.*?)</style>', source, re.S)[1]

def chunks(text):
    """Split CSS rules while respecting quoted strings and balanced blocks."""
    pos = 0
    while pos < len(text):
        start = pos
        quote = None
        parens = 0
        while pos < len(text):
            c = text[pos]
            if quote:
                if c == '\\': pos += 2; continue
                if c == quote: quote = None
            elif c in '\"\'': quote = c
            elif c == '(': parens += 1
            elif c == ')': parens -= 1
            elif c == '{' and not parens: break
            pos += 1
        if pos == len(text):
            assert not text[start:].strip(), text[start:]
            return
        prelude = text[start:pos].strip()
        pos += 1
        inner = pos
        depth = 1
        quote = None
        while pos < len(text) and depth:
            c = text[pos]
            if quote:
                if c == '\\': pos += 2; continue
                if c == quote: quote = None
            elif c in '\"\'': quote = c
            elif c == '{': depth += 1
            elif c == '}': depth -= 1
            pos += 1
        assert depth == 0
        yield prelude, text[inner:pos-1]

def scope_selector(s):
    s = s.strip()
    if s == ':root': return root
    if s == 'html': return 'html:has(body.page-id-14)'
    if s.startswith('body'): return s.replace('body', root, 1)
    return root + ' ' + s

def scope(text):
    out = []
    for prelude, body in chunks(text):
        if prelude.startswith('@media'):
            out.append(prelude+'{'+scope(body)+'}')
        elif prelude.startswith('@'):
            out.append(prelude+'{'+body+'}')
        else:
            # Original selectors contain no comma-bearing functions.
            assert not re.search(r'\([^)]*,', prelude), prelude
            out.append(','.join(scope_selector(s) for s in prelude.split(','))+'{'+body+'}')
    return '\n'.join(out)

css = scope(css).replace('RedlineDisplay', 'RL5Display')
for name in ['levitate','orbit','marquee','cue','current','led','route','scan','pulse']:
    css = re.sub(r'(@keyframes\s+)'+name+r'\b', r'\1rl5-'+name, css)
    css = re.sub(r'(animation:)'+name+r'\b', r'\1rl5-'+name, css)

# Remove only the theme shell around page 14. Internal design spacing is retained.
reset = f'''
{page}{{margin:0!important;padding:0!important;background:#08090b!important;}}
{page} .wp-site-blocks{{margin:0!important;padding:0!important;}}
{page} .wp-site-blocks > header.wp-block-template-part,
{page} .wp-site-blocks > footer.wp-block-template-part{{display:none!important;}}
{page} .wp-site-blocks > main,
{page} .wp-block-post-content{{margin:0!important;padding:0!important;max-width:none!important;width:100%!important;}}
{page} .wp-block-post-content > {root}{{margin:0!important;padding:0!important;max-width:none!important;width:100%!important;}}
{root}{{isolation:isolate;text-align:left;}}
{root} h1,{root} h2,{root} h3,{root} p{{color:inherit;}}
'''
# Avoid overbroad typography resets: the original scoped design owns typography.
reset = reset.replace(f'{root} h1,{root} h2,{root} h3,{root} p{{color:inherit;}}\n','')
body = re.search(r'<body>(.*?)</body>', source, re.S)[1]
js = re.search(r'<script>(.*?)</script>', body, re.S)[1]
body = re.sub(r'<script>.*?</script>', '', body, flags=re.S).strip()
body = body.replace('This file works offline. No information is collected or transmitted.', 'Exploratory brand and interface preview. Not a live equipment catalogue.')
js = js.replace("const $=s=>document.querySelector(s);", "const root=document.getElementById('rl-redline-home');if(!root||root.dataset.initialized)return;root.dataset.initialized='true';const $=s=>root.querySelector(s);")
js = js.replace('document.querySelectorAll(', 'root.querySelectorAll(')
js = js.replace("document.body.classList.toggle('motion-off'", "root.classList.toggle('motion-off'")
assert "const root=document.getElementById('rl-redline-home')" in js
assert 'document.querySelector' not in js and 'document.body' not in js
license_comment = re.search(r'<!-- Embedded Open Sans.*?-->', source, re.S)[0]
block = '<!-- wp:html -->\n'+license_comment+'\n<style>\n'+reset+css+'\n</style>\n<div id="rl-redline-home">\n'+body+'\n</div>\n<script>\n'+js.strip()+'\n</script>\n<!-- /wp:html -->'
out = BASE/'homepage-block.html'
out.write_text(block)
(BASE/'homepage.js').write_text(js)
summary = {'page_id':14,'original_sha256':hashlib.sha256(source.encode()).hexdigest(),'block_sha256':hashlib.sha256(block.encode()).hexdigest(),'bytes':len(block.encode()),'native_block':'core/html','template':'page-no-title'}
(BASE/'build-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary))
