import random,re,html,os
O=os.path.dirname(os.path.abspath(__file__));random.seed(7)
BG,PN,ST,TX,MU="#050b1c","#0a1330","#1b2b55","#e8eeff","#8f9fc4"
G,B,P,Y,C="#22d37a","#4c8dff","#a56bff","#f5c542","#5ee0ff"
SF="Segoe UI,Helvetica,Arial,sans-serif";MO="Consolas,Menlo,monospace"
def t(x,y,s,sz=13,c=TX,w=400,f=SF,a="start",e=""):
    return f'<text x="{x}" y="{y}" font-family="{f}" font-size="{sz}" fill="{c}" font-weight="{w}" text-anchor="{a}" {e}>{html.escape(s)}</text>'
def fade(c,b,d=.6): return f'<g opacity="0">{c}<animate attributeName="opacity" from="0" to="1" begin="{b}s" dur="{d}s" fill="freeze"/></g>'
def svg(n,w,h,body):
    d=f'<defs><pattern id="gr" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="#12204a" stroke-width=".6"/></pattern><linearGradient id="ng" x1="0" x2="1" spreadMethod="reflect"><stop offset="0" stop-color="{B}"/><stop offset=".5" stop-color="{C}"/><stop offset="1" stop-color="{P}"/><animateTransform attributeName="gradientTransform" type="translate" from="-1 0" to="1 0" dur="5s" repeatCount="indefinite"/></linearGradient><linearGradient id="sc" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="{C}" stop-opacity="0"/><stop offset=".5" stop-color="{C}" stop-opacity=".35"/><stop offset="1" stop-color="{C}" stop-opacity="0"/></linearGradient></defs>'
    open(f"{O}/{n}.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{d}<rect width="{w}" height="{h}" rx="14" fill="{BG}"/><rect width="{w}" height="{h}" rx="14" fill="url(#gr)"/>{body}</svg>')
def typed(i,x,y,s,sz,c,b,d,f=MO,w=400,cw=None):
    cw=cw or sz*.62;v=";".join(f"{k*cw:.1f}" for k in range(len(s)+1))
    return f'<clipPath id="k{i}"><rect x="{x}" y="{y-sz-2}" width="0" height="{sz+9}"><animate attributeName="width" values="{v}" calcMode="discrete" begin="{b}s" dur="{d}s" fill="freeze"/></rect></clipPath><g clip-path="url(#k{i})">{t(x,y,s,sz,c,w,f)}</g>'
def orbit(cx,cy,r,items,dur,rev,col):
    k=0 if rev else 1
    d=f"M {cx-r} {cy} a {r} {r} 0 1 {k} {2*r} 0 a {r} {r} 0 1 {k} {-2*r} 0"
    s=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-opacity=".3" stroke-dasharray="3 5"/>'
    for j,l in enumerate(items):
        w=len(l)*5.7+16
        s+=f'<g><rect x="{-w/2}" y="-10" width="{w}" height="20" rx="10" fill="{PN}" stroke="{col}"/>{t(0,3.5,l,9.5,TX,600,SF,"middle")}<animateMotion path="{d}" dur="{dur}s" begin="-{dur*j/len(items):.1f}s" repeatCount="indefinite"/></g>'
    return s
# ---------- HERO ----------
stars="".join(f'<circle cx="{random.randint(8,852)}" cy="{random.randint(8,372)}" r="{random.choice([.6,.9,1.3])}" fill="#9fc4ff"><animate attributeName="opacity" values=".1;1;.1" dur="{random.uniform(2,6):.1f}s" begin="-{random.uniform(0,6):.1f}s" repeatCount="indefinite"/></circle>' for _ in range(80))
cx,cy=690,190
core="".join(f'<circle cx="{cx}" cy="{cy}" r="30" fill="none" stroke="{C}"><animate attributeName="r" values="30;66" dur="3s" begin="{k}s" repeatCount="indefinite"/><animate attributeName="opacity" values=".6;0" dur="3s" begin="{k}s" repeatCount="indefinite"/></circle>' for k in range(3))
core+=f'<circle cx="{cx}" cy="{cy}" r="30" fill="#0d1f4a" stroke="{C}" stroke-width="2"/>'+t(cx,cy+7,"MZ",20,C,800,SF,"middle")
orb=orbit(cx,cy,60,["JS","Python","Git"],14,False,C)+orbit(cx,cy,100,["React","Node","Express","MongoDB"],24,True,B)+orbit(cx,cy,140,["Supabase","WordPress","Tailwind","MySQL"],36,False,P)
roles=["Full-Stack Developer · MERN","Supabase & REST API builder","WordPress / Elementor delivery","Turning ideas into real web apps"]
rl=""
for i,r in enumerate(roles):
    s,e=i*.25,(i+1)*.25
    rl+=f'<g opacity="0">{t(40,172,"▸ "+r,17,Y,600,MO)}<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{s};{s+.02};{e-.02};{e};1" dur="12s" repeatCount="indefinite"/></g>'
pills="".join(fade(f'<rect x="{40+i*92}" y="262" width="82" height="24" rx="12" fill="none" stroke="{c}" stroke-opacity=".7"/>'+t(81+i*92,278,l,11,c,600,SF,"middle"),3.2+i*.25) for i,(l,c) in enumerate([("MERN",G),("Supabase",C),("WordPress",B),("REST",P)]))
live=fade(f'<circle cx="46" cy="318" r="4" fill="{G}"><animate attributeName="opacity" values="1;.2;1" dur="1.6s" repeatCount="indefinite"/></circle>'+t(58,322,"Open to collaborations & freelance work",12,MU),4.2)
svg("hero",860,380,stars+f'<rect width="860" height="3" fill="url(#sc)"><animate attributeName="y" values="-4;380" dur="6s" repeatCount="indefinite"/></rect>'+core+orb+
 typed(1,40,62,"muzammil@github:~$ whoami",14,G,.3,1.2)+
 typed(2,40,118,"Muhammad Muzammil",44,"url(#ng)",1.6,1.4,SF,800,29)+
 fade(rl,3.0)+fade(t(40,212,"BSCS @ KIET Karachi  ·  Full-Stack Intern @ NexSoft Solutions",13,TX)+t(40,234,"Karachi, Pakistan  ·  Grad. 2027",12,MU),3.0)+pills+live)
# ---------- TERMINAL ----------
L=[("$ cat about.json",1),'{','  "name": "Muhammad Muzammil",','  "role": "Full-Stack Developer (MERN)",','  "education": "BSCS @ KIET Karachi, 2027",','  "now": "Intern @ NexSoft Solutions",','  "stack": ["React", "Node", "Express", "MongoDB", "Supabase"],','  "wins": ["CODE JUNG 2025: 1st", "SMIT Hackathon 2025: Top 5"]','}',("$ ls ~/projects",1),"NoteStack/  AssetMaintenance/  AIQuiz/  WorldAtlas/  HospitalMS/  SMITClone/"]
cw=7.4;T=0;ev=[]
for l in L:
    cmd=isinstance(l,tuple);s=l[0] if cmd else l;d=len(s)*.045+.2 if cmd else .35
    ev.append((s,cmd,T,d));T+=d+(.4 if cmd else .05)
TT=T+4
def col(s,cmd):
    if cmd:return f'<tspan fill="{G}">$</tspan><tspan fill="{TX}">{html.escape(s[1:])}</tspan>'
    return "".join(f'<tspan fill="{B if m.endswith(chr(34)) and (s[s.find(m)+len(m):s.find(m)+len(m)+1]==":") else (G if m.startswith(chr(34)) else MU)}">{html.escape(m)}</tspan>' for m in re.findall(r'"[^"]*"|[^"]+',s))
body=f'<rect x="0" y="0" width="860" height="34" rx="14" fill="#0d1838"/><circle cx="22" cy="17" r="5" fill="#ff5f56"/><circle cx="40" cy="17" r="5" fill="#ffbd2e"/><circle cx="58" cy="17" r="5" fill="#27c93f"/>'+t(430,22,"muzammil — zsh — 100×30",11,MU,400,MO,"middle")
for i,(s,cmd,b,d) in enumerate(ev):
    y=64+i*22;n=len(s)
    kt=[0,b/TT]+[(b+d*k/n)/TT for k in range(1,n+1)]+[(TT-1)/TT,1]
    vs=[0,0]+[k*cw for k in range(1,n+1)]+[0,0]
    kt=[0]+[(b+d*k/n)/TT for k in range(n+1)]+[(TT-1)/TT,1];vs=[0]+[k*cw for k in range(n+1)]+[0,0]
    body+=f'<clipPath id="t{i}"><rect x="24" y="{y-14}" width="0" height="20"><animate attributeName="width" calcMode="discrete" values="{";".join(f"{v:.1f}" for v in vs)}" keyTimes="{";".join(f"{k:.4f}" for k in kt)}" dur="{TT:.1f}s" repeatCount="indefinite"/></rect></clipPath><g clip-path="url(#t{i})"><text x="24" y="{y}" font-family="{MO}" font-size="12.3" xml:space="preserve">{col(s,cmd)}</text></g>'
yl=64+len(ev)*22
body+=t(24,yl,"$",12.3,G,400,MO)+f'<rect x="38" y="{yl-12}" width="8" height="15" fill="{C}"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>'
svg("terminal",860,yl+26,body)
# ---------- PROJECTS ----------
Pj=[("NoteStack","Supabase-powered sticky-notes","SaaS with glass auth",P),("Asset Maintenance","QR asset tracking · Admin /","Technician / Public roles",G),("AI Quiz Platform","JavaScript quiz app wired","to the Open Trivia DB API",B),("WorldAtlas","Country & geo data explorer","in vanilla JavaScript",C),("Hospital Mgmt System","Patient, staff and records","management system","#ff6b6b"),("SMIT UI Clone","Pixel-level clone of the","SMIT website UI",Y)]
cd=""
for i,(a,b,c,k) in enumerate(Pj):
    x,y=10+(i%3)*285,56+(i//3)*134
    cd+=f'<g transform="translate({x} {y})"><animateTransform attributeName="transform" type="translate" values="{x} {y};{x} {y-5};{x} {y}" dur="4s" begin="-{i*.7:.1f}s" repeatCount="indefinite"/><rect width="270" height="118" rx="12" fill="{PN}" stroke="{k}" stroke-opacity=".8" stroke-dasharray="7 5"><animate attributeName="stroke-dashoffset" from="0" to="-48" dur="3s" repeatCount="indefinite"/></rect><circle cx="30" cy="32" r="6" fill="{k}"><animate attributeName="r" values="5;8;5" dur="2s" begin="-{i*.3:.1f}s" repeatCount="indefinite"/></circle>'+t(46,37,a,15,TX,700)+t(20,66,b,12,MU)+t(20,84,c,12,MU)+t(20,106,"Live demo  →",11.5,k,600)+'</g>'
bd=""
for i,(e,a,b,k) in enumerate([("1st","CODE JUNG 2025","Web Development",Y),("Top 5","SMIT Hackathon 2025","",B),("CERT","Cisco","Networking Basics",C)]):
    x=10+i*285
    bd+=f'<clipPath id="b{i}"><rect x="{x}" y="332" width="270" height="52" rx="10"/></clipPath><rect x="{x}" y="332" width="270" height="52" rx="10" fill="{PN}" stroke="{k}"/>'+t(x+16,365,e,15,k,800,MO)+t(x+80,357,a,13,TX,600)+(t(x+80,374,b,11,MU) if b else "")+f'<g clip-path="url(#b{i})"><rect y="332" width="40" height="52" fill="#fff" opacity=".12" transform="skewX(-20)"><animate attributeName="x" values="{x-80};{x+330}" dur="3.5s" begin="-{i*1.1:.1f}s" repeatCount="indefinite"/></rect></g>'
svg("projects",860,400,t(10,36,"~/projects  &&  ~/achievements",14,G,700,MO)+cd+bd)
# ---------- HEATMAP PLACEHOLDER (replaced by the Action) ----------
cells="".join(f'<rect x="{20+w*14}" y="{50+d*14}" width="11" height="11" rx="2" fill="#12204a"><animate attributeName="fill" values="#12204a;{G};#12204a" dur="3s" begin="{w*.07:.2f}s" repeatCount="indefinite"/></rect>' for w in range(53) for d in range(7))
svg("contrib-heatmap",780,170,t(20,30,"$ ./contributions.sh   # syncing with GitHub — run the workflow once",12,G,400,MO)+cells)
