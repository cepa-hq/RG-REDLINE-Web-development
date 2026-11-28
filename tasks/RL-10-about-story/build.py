from pathlib import Path
import math,json,hashlib
b=Path(__file__).resolve().parent
assets=json.loads((b/'logo-assets.json').read_text())
data='data:image/png;base64,'+assets['cepa_png_base64']
path=assets['weighted_path']
view=assets['weighted_viewbox']
defs='<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" style="position:absolute;overflow:hidden" aria-hidden="true"><defs><symbol id="rg-weighted" viewBox="'+view+'"><path fill="currentColor" fill-rule="evenodd" d="'+path+'"/></symbol><filter id="cepa-titanium" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0 0 0 0 .90 0 0 0 0 .94 0 0 0 0 .97 0 0 0 1 0"/></filter><symbol id="cepa-original" viewBox="544 819 912 365"><image x="0" y="0" width="2000" height="2001" href="'+data+'" filter="url(#cepa-titanium)"/></symbol></defs></svg>'
# Use explicit, shared curve profiles for contiguous stripes without gaps.
def stripe(y,phase):
 d=-13 if phase==0 else 13
 return f'M0 {y} C75 {y+d} 150 {y-d} 225 {y} S375 {y+d} 450 {y} L450 {y+100} C375 {y+100+d} 300 {y+100+d} 225 {y+100} C150 {y+100-d} 75 {y+100+d} 0 {y+100} Z'
flag='<svg class="india-flag" id="india-flag" viewBox="-12 0 480 348" role="img" aria-label="Waving national flag of India with saffron, white and green bands and the 24-spoke navy-blue Ashoka Chakra"><defs><linearGradient id="flag-fold" x1="0" x2="1"><stop stop-color="#000" stop-opacity=".10"/><stop offset=".25" stop-color="#fff" stop-opacity=".07"/><stop offset=".55" stop-color="#000" stop-opacity=".11"/><stop offset=".8" stop-color="#fff" stop-opacity=".11"/><stop offset="1" stop-color="#000" stop-opacity=".05"/></linearGradient></defs>'
for y,color in [(24,'#FF9933'),(124,'#FFFFFF'),(224,'#138808')]:
 a,c=stripe(y,0),stripe(y,1)
 flag+='<path fill="'+color+'" d="'+a+'"><animate attributeName="d" values="'+a+';'+c+';'+a+'" dur="5s" repeatCount="indefinite"/></path>'
flag+='<g class="flag-chakra" fill="none" stroke="#000080" stroke-width="1.5"><circle cx="225" cy="174" r="29"/><circle cx="225" cy="174" r="3" fill="#000080"/>'
for i in range(24):
 a=math.radians(i*15);flag+=f'<path d="M{225+3*math.cos(a):.3f} {174+3*math.sin(a):.3f} L{225+28*math.cos(a):.3f} {174+28*math.sin(a):.3f}"/>'
flag+='</g>'
for y in [24,124,224]:
 a,c=stripe(y,0),stripe(y,1)
 flag+='<path fill="url(#flag-fold)" d="'+a+'"><animate attributeName="d" values="'+a+';'+c+';'+a+'" dur="5s" repeatCount="indefinite"/></path>'
flag+='</svg>'
s=(b/'page.html').read_text().replace('__LOGO_DEFS__',defs).replace('__RG_VIEWBOX__',view).replace('__INDIA_FLAG__',flag).replace('__SCRIPT__',(b/'about.js').read_text())
(b/'dist').mkdir(exist_ok=True);(b/'dist/index.html').write_text(s);(b/'RG-REDLINE-About-Us-Concept.html').write_text(s)
summary={'bytes':len(s.encode()),'sha256':hashlib.sha256(s.encode()).hexdigest(),'cepa_source':'cepa group_cepa group-03.png / libfile_931967ee432c8191898a4775c23b8717','cepa_treatment':'Original pixels embedded once in an SVG symbol, cropped by viewBox; monochrome titanium rendering through SVG colour filter. Source PNG unchanged.','rg_logo':'RL-7 weighted reference SVG geometry','chakra_spokes':24,'body_font_px':16,'h1_font_px':32,'h2_font_px':24,'heading_weight':600,'live_deployment':False}
(b/'build-summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
