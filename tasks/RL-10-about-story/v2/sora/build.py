from pathlib import Path
import argparse,base64,json,re,hashlib
b=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--base',type=Path,default=b.parent/'RG-REDLINE-About-Us-v2.html');args=p.parse_args()
source=args.base.read_text();assets=json.loads((b/'font-assets.json').read_text())
assert hashlib.sha256(source.encode()).hexdigest()=='ff3d73cb1f9eade019d9cf023b9b1d7a3380b375cdb23923fbbc0f5188c26745','Unexpected v2 baseline'
font=assets['woff_base64']
face="@font-face{font-family:'RG Sora';font-style:normal;font-weight:100 800;font-display:swap;src:url(data:font/woff;base64,"+font+") format('woff')}"
s,n=re.subn(r'@font-face\{[^}]+\}','',source)
assert n==2
s=s.replace('<style>','<style>'+face,1)
s=s.replace("'RG Syne'","'RG Sora'").replace("'RG Space'","'RG Sora'").replace("'RG Sora','RG Sora'","'RG Sora'")
s,n=re.subn(r'<!-- Embedded font licences\n.*?\n-->',lambda m:'<!-- Embedded font licence — Sora, Google Fonts / sora-xor project\n'+assets['license']+'\n-->',s,flags=re.S)
assert n==1
# Keep navigation readable with Sora's wider metrics at intermediate widths.
s=s.replace('</style>', '@media(min-width:801px) and (max-width:1000px){.header-inner{height:auto;min-height:105px;flex-wrap:wrap;padding:18px 0 0;gap:14px}.brand-lockup{flex:1}.top-nav{order:3;width:100%;justify-content:center;padding-bottom:11px}.top-nav a,.motion-control{white-space:nowrap}.motion-control{flex-shrink:0}}'+'</style>',1)
assert source[source.index('<body>'):]==s[s.index('<body>'):],'Unexpected body/script change'
out=b/'RG-REDLINE-About-Us-Sora.html';out.write_text(s)
(b/'dist').mkdir(exist_ok=True);(b/'dist/index.html').write_text(s)
summary={'bytes':len(s.encode()),'sha256':hashlib.sha256(s.encode()).hexdigest(),'base_sha256':hashlib.sha256(source.encode()).hexdigest(),'font':'Sora variable upright WOFF, licensed subset from REDLINE font comparison','font_sha256':hashlib.sha256(base64.b64decode(font)).hexdigest(),'weight_range':'100–800','body_and_js_unchanged':True,'layout_rules_preserved_except_tablet_header':True,'external_asset_requests':0,'live_deployment':False}
(b/'build-summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
