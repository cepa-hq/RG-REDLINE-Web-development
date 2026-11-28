from pathlib import Path
import argparse,re,json,hashlib
b=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--source',type=Path,default=b.parent/'v2/exo2-silver/RG-REDLINE-About-Us-Exo2-Silver.html');p.add_argument('--page-id',type=int,default=19);a=p.parse_args()
source=a.source.read_text();assert hashlib.sha256(source.encode()).hexdigest()=='8fadcbf7c2139611f49525ca625d779d73a68fbd14e2f3f373016f7ae1f3e330'
final,n=re.subn(r'<aside class="finish-settings wrap".*?</aside>','',source,flags=re.S);assert n==1
final,n=re.subn(r'<script>\(\(\)=>\{\x27use strict\x27;const root=document.getElementById\(\x27rg-about\x27\);const colours=.*?</script>','',final,flags=re.S);assert n==1
# Remove only comparison-control styles; retain the locked silver heading rule.
final,n=re.subn(r'\.finish-settings\{padding:12px.*?\n@media\(max-width:450px\)\{\.finish-options.*?\}\n','',final,flags=re.S);assert n==1
assert 'name="heading-silver"' not in final and 'Titanium silver' not in final and 'finish-settings' not in final
final=final.replace('href="#main" class="brand-lockup" aria-label="RG REDLINE About"','href="https://rg-redline.com/" class="brand-lockup" aria-label="RG REDLINE home"')
# Inline && is entity-encoded by this site's content renderer. Use an equivalent guard locally.
final=final.replace('if(fine.matches&&pointer.x>0)','if(fine.matches ? pointer.x>0 : false)')
scripts=re.findall(r'<script>(.*?)</script>',final,re.S);assert len(scripts)==1 and '&&' not in scripts[0]
(b/'RG-REDLINE-About-Us-Final.html').write_text(final)
(b/'about.js').write_text(scripts[0])
css=re.search(r'<style>(.*?)</style>',final,re.S)[1]
body=re.search(r'<body>(.*?)</body>',final,re.S)[1]
notice=re.search(r'<!-- Embedded font licence.*?-->',final,re.S)[0]
# Scope every selector in the standalone stylesheet. Keyframes and font faces remain definitions.
def seek(text,start,char):
 quote=None;comment=False;escape=False
 for i in range(start,len(text)):
  c=text[i]
  if comment:
   if text[i-1:i+1]=='*/':comment=False
   continue
  if quote:
   if escape:escape=False
   elif c=='\\':escape=True
   elif c==quote:quote=None
   continue
  if text[i:i+2]=='/*':comment=True;continue
  if c in '\"\x27':quote=c;continue
  if c==char:return i
 return -1
def closing(text,start):
 depth=1;pos=start+1
 while depth:
  left=seek(text,pos,'{');right=seek(text,pos,'}')
  assert right>=0,'Unbalanced CSS'
  if left>=0 and left<right:depth+=1;pos=left+1
  else:depth-=1;pos=right+1
 return pos-1
def selector(s):
 s=s.strip()
 if s==':root':return '#rg-about'
 if s=='html':return f'html:has(body.page-id-{a.page_id})'
 if s=='body':return '#rg-about'
 if s=='*':return '#rg-about,#rg-about *'
 if s.startswith('#rg-about'):return s
 if s.startswith('.motion-paused'):return '#rg-about'+s
 if s.startswith('.js-ready'):return '#rg-about'+s
 return '#rg-about '+s
def scoped(text):
 out=[];pos=0
 while pos<len(text):
  opening=seek(text,pos,'{')
  if opening<0:out.append(text[pos:]);break
  head=text[pos:opening].strip();end=closing(text,opening);inside=text[opening+1:end]
  if head.startswith('@media') or head.startswith('@supports'):out.append(head+'{'+scoped(inside)+'}')
  elif head.startswith('@'):out.append(head+'{'+inside+'}')
  else:out.append(','.join(selector(s) for s in head.split(','))+'{'+inside+'}')
  pos=end+1
 return '\n'.join(out)
css=scoped(css)
for old,new in [('chip-float','rga-chip-float'),('signal-run','rga-signal-run')]:css=css.replace(old,new)
shell=f'''
html:has(body.page-id-{a.page_id}){{font-size:16px;background:#000;color-scheme:dark}}
body.page-id-{a.page_id}{{margin:0!important;padding:0!important;background:#000!important}}
body.page-id-{a.page_id} .wp-site-blocks{{margin:0!important;padding:0!important}}
body.page-id-{a.page_id} .wp-site-blocks > header.wp-block-template-part,
body.page-id-{a.page_id} .wp-site-blocks > footer.wp-block-template-part{{display:none!important}}
body.page-id-{a.page_id} .wp-site-blocks > main,
body.page-id-{a.page_id} .wp-block-post-content{{margin:0!important;padding:0!important;max-width:none!important;width:100%!important}}
body.page-id-{a.page_id} .wp-block-post-content > #rg-about{{margin:0!important;padding:0!important;max-width:none!important;width:100%!important}}
body.page-id-{a.page_id}.admin-bar #rg-about .site-header{{top:35px}}
body.page-id-{a.page_id}.admin-bar #rg-about .reading-track{{top:32px}}
@media(max-width:782px){{body.page-id-{a.page_id}.admin-bar #rg-about .site-header{{top:49px}}body.page-id-{a.page_id}.admin-bar #rg-about .reading-track{{top:46px}}}}
'''
block='<!-- wp:html -->\n'+notice+'\n<style>\n'+css+'\n'+shell+'\n</style>\n'+body.strip()+'\n<!-- /wp:html -->'
(b/'about-native-block.html').write_text(block)
assert block.count('<!-- wp:html -->')==1 and block.count('<!-- /wp:html -->')==1
assert not re.search(r'<(?:html|body|head)(?:\s|>)',block)
summary={'page_id':a.page_id,'slug':'about','template':'page-no-title','native_block':'core/html','font':'Exo 2','heading_colour':'#C4C8CD','heading_tracking':'+0.02em','heading_line_height':1.32,'source_sha256':hashlib.sha256(source.encode()).hexdigest(),'block_sha256':hashlib.sha256(block.encode()).hexdigest(),'block_bytes':len(block.encode()),'final_html_sha256':hashlib.sha256(final.encode()).hexdigest(),'settings_mutations':[],'homepage_mutation':False,'temporary_colour_controls_removed':True}
(b/'manifest.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
