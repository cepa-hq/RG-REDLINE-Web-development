from pathlib import Path
import argparse,base64,json,re,hashlib
b=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--base',type=Path,default=b.parent/'RG-REDLINE-About-Us-v2.html');args=p.parse_args()
source=args.base.read_text();assets=json.loads((b/'font-assets.json').read_text())
assert hashlib.sha256(source.encode()).hexdigest()=='ff3d73cb1f9eade019d9cf023b9b1d7a3380b375cdb23923fbbc0f5188c26745','Unexpected v2 baseline'
font=assets['woff2_base64']
face="@font-face{font-family:'RG Crimson';font-style:normal;font-weight:200 900;font-display:swap;src:url(data:font/woff2;base64,"+font+") format('woff2')}"
s,n=re.subn(r'@font-face\{[^}]+\}','',source)
assert n==2
s=s.replace('<style>','<style>'+face,1)
s=s.replace("'RG Syne'","'RG Crimson'").replace("'RG Space'","'RG Crimson'").replace("'RG Crimson','RG Crimson'","'RG Crimson'").replace(',sans-serif',',serif')
s,n=re.subn(r'<!-- Embedded font licences\n.*?\n-->',lambda m:'<!-- Embedded font licence — supplied CrimsonPro_Complete.zip\n'+assets['license']+'\n-->',s,flags=re.S)
assert n==1
assert source[source.index('<body>'):]==s[s.index('<body>'):],'Unexpected body/script change'
out=b/'RG-REDLINE-About-Us-Crimson-Pro.html';out.write_text(s)
(b/'dist').mkdir(exist_ok=True);(b/'dist/index.html').write_text(s)
summary={'bytes':len(s.encode()),'sha256':hashlib.sha256(s.encode()).hexdigest(),'base_sha256':hashlib.sha256(source.encode()).hexdigest(),'font':'Uploaded Crimson Pro variable upright WOFF2, original unmodified bytes','font_sha256':hashlib.sha256(base64.b64decode(font)).hexdigest(),'weight_range':'200–900','body_and_js_unchanged':True,'layout_rules_unchanged':True,'external_asset_requests':0,'live_deployment':False}
(b/'build-summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
