from pathlib import Path
import json,base64,hashlib
b=Path(__file__).resolve().parent
assets=json.loads((b/'logo-assets.json').read_text())
defs='<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" style="position:absolute;overflow:hidden" aria-hidden="true"><defs><symbol id="rg-weighted" viewBox="'+assets['weighted_viewbox']+'"><path fill="currentColor" fill-rule="evenodd" d="'+assets['weighted_path']+'"/></symbol><filter id="cepa-titanium" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0 0 0 0 .94 0 0 0 0 .94 0 0 0 0 .92 0 0 0 1 0"/></filter><symbol id="cepa-original" viewBox="544 819 912 365"><image width="2000" height="2001" href="data:image/png;base64,'+assets['cepa_png_base64']+'" filter="url(#cepa-titanium)"/></symbol></defs></svg>'
rg='<svg class="rg-wordmark" viewBox="'+assets['weighted_viewbox']+'" role="img" aria-label="Weighted Roun Groun wordmark"><use href="#rg-weighted"/></svg>'
cepa='<svg class="cepa-wordmark" viewBox="0 0 912 365" role="img" aria-label="CEPA Group"><use href="#cepa-original"/></svg>'
font_assets=json.loads((b/'font-assets.json').read_text())
fonts=''
for name,family in [('SpaceGrotesk','RG Space'),('Syne','RG Syne')]:
 fonts+="@font-face{font-family:'"+family+"';font-style:normal;font-weight:400 700;font-display:swap;src:url(data:font/woff;base64,"+font_assets[name]['woff_base64']+") format('woff')}"
arch=[
 ('structure','Structure & protection','M5 9 16 3 27 9v13L16 29 5 22ZM5 9l11 7 11-7M16 16v13','Mechanical architecture','Protection begins with the structure.','The enclosure, internal supports, mounting points and physical controls form a protective system. Their design considers impact, vibration, exposure and repeated handling.','The objective is to protect critical functions while keeping the equipment practical to carry, secure and operate.','Preserve the integrity of the complete product under demanding use.'),
 ('electronics','Electronics & control','M9 9h14v14H9ZM13 2v7M19 2v7M13 23v7M19 23v7M2 13h7M2 19h7M23 13h7M23 19h7','Electronic architecture','Controlled electrical behaviour.','Circuit protection, power delivery, thermal behaviour and control logic are considered together. The electronics must be developed for the environment around them and the functions they support.','Reliable operation depends on the interaction between these elements and the protective structure that contains them.','Stable, deliberate system behaviour as operating conditions change.'),
 ('power','Power discipline','M24 7H5v18h19V7ZM24 12h4v8h-4M16 10l-5 8h7l-4 6','Energy architecture','Power must serve the task.','Energy use is considered against intended functions, operating conditions and sustained demand. Power decisions belong within the architecture from the beginning.','The aim is a disciplined balance between capability, load and useful operation, with clear consideration of the product’s limits.','Predictable and purposeful power behaviour.'),
 ('operation','Clear operation','M5 5h22v22H5ZM9 10h14M9 15h9M20 21h3','Human interface','Critical functions. Clear action.','Physical controls, information hierarchy and feedback are designed around deliberate action. The interface should help the user understand what the equipment is doing and what action is required.','Clarity remains a priority when attention is divided or surrounding conditions make operation more difficult.','Reduce uncertainty at the point of use.'),
 ('validation','Validation & revision','M5 7h22v21H5ZM12 7V3h8v4M10 17l4 4 8-9','Development feedback','Testing must change the design.','REDLINE’s R&D and testing work is based in India. Evaluation feeds back into the product, informing revisions to its structure, electronics and operation.','Reliability is pursued through that repeated connection between design, observation and improvement.','Use testing to identify weaknesses and guide meaningful revisions.')
]
tabs=[];panels=[]
for i,(key,label,icon,kicker,title,p1,p2,priority) in enumerate(arch):
 tabs.append(f'<button class="arch-tab" id="tab-{key}" role="tab" aria-selected="{str(i==0).lower()}" aria-controls="panel-{key}" tabindex="{0 if i==0 else -1}"><svg viewBox="0 0 32 32" aria-hidden="true"><path d="{icon}"/></svg><span>{label.replace("&","&amp;")}</span></button>')
 hidden='' if i==0 else ' hidden'
 panels.append(f'<article class="arch-panel lumen" id="panel-{key}" role="tabpanel" aria-labelledby="tab-{key}" tabindex="0"{hidden}><i class="edge-strip" aria-hidden="true"></i><div class="arch-visual" aria-hidden="true"><div class="stack-art"><div class="stack-slice"></div><div class="stack-slice"></div><div class="stack-slice"></div><div class="stack-slice"></div><div class="stack-core"></div></div><span class="visual-note">System illustration · design principles</span></div><div class="arch-copy"><div class="kicker">{kicker}</div><h3>{title}</h3><p>{p1}</p><p>{p2}</p><p class="priority">Engineering priority: {priority}</p></div></article>')
s=(b/'page.html').read_text()
licenses='\n'.join(name+' — '+data['source']+'\n'+data['license'] for name,data in font_assets.items())
s=s.replace('</head>','<!-- Embedded font licences\n'+licenses+'\n--></head>')
for token,value in {'__FONTS__':fonts,'__LOGO_DEFS__':defs,'__RG_LOGO__':rg,'__CEPA_LOGO__':cepa,'__ARCH_TABS__':''.join(tabs),'__ARCH_PANELS__':''.join(panels),'__SCRIPT__':(b/'about.js').read_text()}.items():s=s.replace(token,value)
assert '__' not in s
(b/'dist').mkdir(exist_ok=True)
for p in [b/'dist/index.html',b/'RG-REDLINE-About-Us-v2.html']:p.write_text(s)
summary={'bytes':len(s.encode()),'sha256':hashlib.sha256(s.encode()).hexdigest(),'background':'#000000','fonts':['Space Grotesk variable, Latin subset','Syne variable, Latin subset'],'external_requests':0,'live_deployment':False}
(b/'build-summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
