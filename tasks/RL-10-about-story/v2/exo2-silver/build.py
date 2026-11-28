from pathlib import Path
import argparse,json,re,hashlib,base64
b=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--base',type=Path,default=b.parent/'sora/spacing/RG-REDLINE-About-Us-Sora-Spaced.html');a=p.parse_args()
s=a.base.read_text();assert hashlib.sha256(s.encode()).hexdigest()=='4918d619fb492e2b344342081888cfca83dda3bfd23330da72b25dea58ad8bb2','Unexpected baseline'
assets=json.loads((b/'font-assets.json').read_text())
face="@font-face{font-family:'RG Exo 2';font-style:normal;font-weight:100 900;font-display:swap;src:url(data:font/woff;base64,"+assets['woff_base64']+") format('woff')}"
s,n=re.subn(r'@font-face\{[^}]+\}',lambda m:face,s);assert n==1
s=s.replace("'RG Sora'","'RG Exo 2'")
s,n=re.subn(r'<!-- Embedded font licence.*?\n-->',lambda m:'<!-- Embedded font licence — Exo 2, Google Fonts\n'+assets['license']+'\n-->',s,flags=re.S);assert n==1
s=s.replace('font-weight:650;line-height:1.32;letter-spacing:.012em','font-weight:650;line-height:1.32;letter-spacing:.02em')
css='''
#rg-about{--heading-silver:#c4c8cd}#rg-about h1,#rg-about h2,#rg-about h3,#rg-about .hero-copy h1 em{color:var(--heading-silver);transition:color .25s}
.finish-settings{padding:12px 0 0}.finish-settings fieldset{border:0;margin:0;padding:0;min-width:0}.finish-settings legend{color:#9f9aa5;font-size:.8125rem;padding:0;margin-bottom:10px}.finish-options{display:flex;gap:10px;flex-wrap:wrap}.finish-option{display:flex;align-items:center;gap:12px;border:1px solid #ffffff26;border-radius:15px;background:#080808;padding:10px 15px;cursor:pointer;transition:border-color .2s,background .2s;position:relative}.finish-option:has(input:checked){border-color:#b5c0cb85;background:#101112;box-shadow:inset 0 1px #ffffff0e}.finish-option:focus-within{outline:2px solid #8bff83;outline-offset:4px}.finish-option input{margin:0;accent-color:#b9c4ce;width:15px;height:15px;cursor:pointer}.finish-swatch{width:23px;height:23px;border-radius:50%;background:var(--swatch);box-shadow:inset 0 1px 3px #fff3;flex:none}.finish-option strong{font-size:.875rem;font-weight:500;display:block;color:#c7cbd0;line-height:1.5}.finish-option small{font-size:.6875rem;line-height:1.5;display:block;letter-spacing:.06em;color:#888a91}.finish-settings .finish-note{color:#88838f;font-size:.75rem;margin-top:10px}.finish-option:hover{border-color:#c0c7d060}
@media(max-width:450px){.finish-options{display:grid;grid-template-columns:1fr 1fr;gap:9px}.finish-option{padding:10px;gap:8px}.finish-swatch{width:18px;height:18px}.finish-option strong{font-size:.8125rem}.finish-option small{font-size:.625rem}.finish-option input{width:13px;height:13px}.finish-settings{padding-top:10px}}
'''
s=s.replace('</style>',css+'</style>',1)
controls='''<aside class="finish-settings wrap" aria-label="Preview heading colours"><fieldset><legend>Choose a silver for the headings</legend><div class="finish-options"><label class="finish-option" style="--swatch:#c4c8cd"><input type="radio" name="heading-silver" value="brushed" checked><span class="finish-swatch" aria-hidden="true"></span><span><strong>Brushed silver</strong><small>#C4C8CD</small></span></label><label class="finish-option" style="--swatch:#98a2ad"><input type="radio" name="heading-silver" value="titanium"><span class="finish-swatch" aria-hidden="true"></span><span><strong>Titanium silver</strong><small>#98A2AD</small></span></label></div><p class="finish-note">Brushed is lighter and neutral. Titanium is darker and cooler.</p></fieldset></aside>'''
s=s.replace('<main id="main">',controls+'<main id="main">',1)
extra="""(()=>{'use strict';const root=document.getElementById('rg-about');const colours={brushed:'#c4c8cd',titanium:'#98a2ad'};root.querySelectorAll('input[name="heading-silver"]').forEach(input=>input.addEventListener('change',()=>{if(!input.checked)return;root.style.setProperty('--heading-silver',colours[input.value]);root.dataset.headingFinish=input.value}));})();"""
s=s.replace('</body>','<script>'+extra+'</script></body>',1)
(b/'RG-REDLINE-About-Us-Exo2-Silver.html').write_text(s);(b/'dist').mkdir(exist_ok=True);(b/'dist/index.html').write_text(s)
summary={'bytes':len(s.encode()),'sha256':hashlib.sha256(s.encode()).hexdigest(),'font':'Exo 2 variable upright, 100–900','heading_tracking':'+0.02em','heading_line_height':1.32,'heading_colours':{'Brushed silver':'#C4C8CD','Titanium silver':'#98A2AD'},'external_asset_requests':0,'live_deployment':False}
(b/'build-summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
