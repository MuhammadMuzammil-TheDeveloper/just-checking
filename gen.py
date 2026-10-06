import os,base64,html
O=os.path.dirname(os.path.abspath(__file__))
BG,PN,ST,TX,MU="#070e22","#0b1530","#1c2c52","#e8eeff","#9aa8c7"
G,B,P,Y="#22d37a","#4c8dff","#a56bff","#f5c542"
SF="Segoe UI,Helvetica,Arial,sans-serif";MO="Consolas,Menlo,monospace";CU="Brush Script MT,Segoe Script,cursive"
def t(x,y,s,sz=13,c=TX,w=400,f=SF,a="start",i=False,r=0):
    it=' font-style="italic"' if i else ''
    tr=f' transform="rotate({r} {x} {y})"' if r else ''
    return f'<text x="{x}" y="{y}" font-family="{f}" font-size="{sz}" fill="{c}" font-weight="{w}" text-anchor="{a}"{it}{tr}>{html.escape(s)}</text>'
def box(x,y,w,h,fill=PN,s=ST,r=10): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{s}"/>'
def pr(x,y,cmd): return f'<text x="{x}" y="{y}" font-family="{MO}" font-size="12"><tspan fill="{G}" font-weight="700">&gt; </tspan><tspan fill="{G}">muzammil@github</tspan><tspan fill="{TX}"> ~ $ {html.escape(cmd)}</tspan></text>'
def svg(n,w,h,body):
    d=f'<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#3b82f6"/><stop offset="1" stop-color="#60d0ff"/></linearGradient><radialGradient id="o" cx=".75" cy=".4" r=".6"><stop offset="0" stop-color="#1d3f9a" stop-opacity=".55"/><stop offset="1" stop-color="{BG}" stop-opacity="0"/></radialGradient><linearGradient id="c" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d1b3d"/><stop offset="1" stop-color="#2a1b52"/></linearGradient></defs>'
    open(f"{O}/{n}.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{d}<rect width="{w}" height="{h}" rx="14" fill="{BG}"/>{body}</svg>')
def emb(p,m):
    p=f"{O}/{p}"
    return f"data:{m};base64,"+base64.b64encode(open(p,'rb').read()).decode() if os.path.exists(p) else None

# HERO
ph=emb("photo.png","image/png")
pic=(f'<image xlink:href="{ph}" x="520" y="10" width="340" height="320" preserveAspectRatio="xMidYMax slice"/>' if ph else
 f'<circle cx="700" cy="150" r="52" fill="#16264f"/><path d="M590 330c0-80 50-120 110-120s110 40 110 120z" fill="#101c3d"/>{t(700,265,"</>",20,B,700,MO,"middle")}{t(700,300,"add photo.png and re-run gen.py",10,MU,400,SF,"middle")}')
ic=[(G,"M"),("#e8eeff","ex"),("#61dafb","⚛"),("#7ac943","JS"),("#4c8dff","W")]
icons="".join(f'<circle cx="{58+i*58}" cy="272" r="20" fill="none" stroke="{c}" stroke-opacity=".6"/>{t(58+i*58,277,s,13,c,700,SF,"middle")}' for i,(c,s) in enumerate(ic))
bio=["I'm Muhammad Muzammil, a Full-Stack Web Developer and BSCS student","at KIET, Karachi, Pakistan, working across the MERN stack (MongoDB,","Express.js, React.js, Node.js) and WordPress. I build web apps end to end —","from Supabase/MongoDB-backed backends to React and vanilla-JS frontends."]
svg("hero",860,320,'<rect width="860" height="320" rx="14" fill="url(#o)"/>'+pic+
 f'<rect x="34" y="24" width="150" height="28" rx="14" fill="#0e3a3a"/><circle cx="52" cy="38" r="4" fill="{G}"/>'+t(64,43,"Full-Stack Developer",12,G,600)+
 f'<text x="34" y="106" font-family="{SF}" font-size="46" font-weight="800" fill="{TX}">Muhammad <tspan fill="url(#g)">Muzammil</tspan></text>'+
 t(34,142,"Full-Stack Web Developer (MERN Stack)  |  Karachi, Pakistan",17,TX,500)+
 "".join(t(34,178+i*21,l,12.5,MU) for i,l in enumerate(bio))+icons+
 f'<line x1="330" y1="252" x2="330" y2="292" stroke="{ST}"/>'+t(350,277,"Build  →  Learn  →  Grow",17,B,400,CU,"start",True)+
 "".join(t(800,52+i*24,l,19,TX,400,CU,"middle",True,-12) for i,l in enumerate(["Better","Code","Bigger","Dreams"])))

# WHOAMI
avi=emb("avi-ascii.svg","image/svg+xml")
av=(f'<image xlink:href="{avi}" x="16" y="44" width="210" height="190" preserveAspectRatio="xMidYMid meet"/>' if avi else t(121,140,"avi-ascii.svg",11,MU,400,MO,"middle"))
rows=[("👤","Muhammad Muzammil","Full Stack Developer Intern"),("💼","NexSoft Solutions","(Current)"),("🎓","BSCS – KIET Karachi","(Grad. 2027)"),("📍","Karachi, Pakistan","")]
det="".join(t(258,80+i*46,e,18,TX)+t(288,78+i*46,a,12.5,TX,600)+(t(288,94+i*46,b,11,MU) if b else "") for i,(e,a,b) in enumerate(rows))
st=[(G,"Full Stack Developer Intern @ NexSoft Solutions"),(B,"Previously: WordPress Blog Developer @ Webera Solution"),(P,"Education: BSCS, KIET Karachi (grad. 2027)"),(Y,"Location: Karachi, Pakistan")]
sts="".join(f'<circle cx="534" cy="{82+i*34}" r="6" fill="{c}"/>'+t(550,86+i*34,s,11,TX) for i,(c,s) in enumerate(st))
svg("whoami",860,250,box(0,0,490,250)+pr(16,26,"whoami")+box(16,40,216,196,"#08112a")+av+box(244,40,230,196,"#0a1430")+det+
 box(506,0,354,250)+t(526,36,"⌨  Current Status",15,TX,600)+sts+t(526,222,"❝  Turning ideas into real web applications.",11.5,MU,400,SF,"start",True))

# PROJECTS
P_=[("📝",["NoteStack"],["Supabase sticky-notes","SaaS, glass auth &","pastel dashboard"],P),
("▦",["Asset Maintenance","System"],["QR asset tracking with","Admin/Technician/","Public roles"],G),
("🧠",["AI Quiz Platform"],["JS quiz app wired to","the Open Trivia DB","API"],B),
("🌐",["WorldAtlas"],["Country/geo data","explorer built with","vanilla JavaScript"],"#38bdf8"),
("➕",["Hospital Management","System"],["Patient, staff and","records management","system"],"#ef4444"),
("🖥",["SMIT UI Clone"],["Pixel-level clone of","the SMIT website","UI"],"#8b5cf6")]
cs=""
for i,(e,ti,de,c) in enumerate(P_):
    x=16+i*140
    cs+=box(x,40,132,172,"#0a1430")+f'<rect x="{x+12}" y="52" width="38" height="38" rx="9" fill="{c}" fill-opacity=".22"/>'+t(x+31,78,e,18,c,400,SF,"middle")
    cs+="".join(t(x+12,112+k*14,l,11.5,TX,700) for k,l in enumerate(ti))+"".join(t(x+12,148+k*13,l,9.5,MU) for k,l in enumerate(de))+t(x+12,202,"Live Demo →",10.5,B,500)
svg("projects",860,226,box(0,0,860,226)+pr(16,26,"ls -la ~/projects")+cs)

# SKILLS + ACHIEVEMENTS + CTA
tech="JavaScript,Node.js,Express.js,MongoDB,React.js,Tailwind CSS,Bootstrap,Supabase,WordPress,Python,C++,HTML5,CSS3,REST APIs,Firebase,MySQL,Git,GitHub,Postman,VS Code,Netlify,Vercel,Elementor".split(",")
x=y=0;pl=""
for s in tech:
    w=len(s)*6.4+22
    if x+w>360:x=0;y+=31
    pl+=f'<rect x="{20+x}" y="{74+y}" width="{w}" height="24" rx="12" fill="#101c3d" stroke="{ST}"/>'+t(20+x+w/2,90+y,s,11,TX,400,SF,"middle");x+=w+7
ac=[("🏆",Y,"1st Place","CODE JUNG 2025 (Web Development)"),("🏅",B,"Top 5","SMIT Hackathon 2025"),("📜","#38bdf8","Cisco","Networking Basics Certification")]
acs="".join(t(410,98+i*62,e,26)+t(448,92+i*62,a,13,c,700)+t(448,110+i*62,b,11,MU) for i,(e,c,a,b) in enumerate(ac))
svg("skills-achievements",860,290,box(0,0,616,290)+pr(16,26,"cat skills.txt")+t(20,62,"</>  Tech Stack",14,TX,600)+pl+f'<line x1="392" y1="48" x2="392" y2="270" stroke="{ST}"/>'+t(410,62,"🏆  Achievements",14,TX,600)+acs+
 f'<rect x="632" y="0" width="228" height="290" rx="10" fill="url(#c)" stroke="{ST}"/><polygon points="632,290 700,200 750,245 800,190 860,260 860,290" fill="#0a1226" opacity=".8"/>'+
 t(652,110,"Let's Build",24,TX,800)+t(652,138,"Something Great",24,TX,800)+t(652,168,"Open for collaborations,",11.5,MU)+t(652,184,"freelance projects and",11.5,MU)+t(652,200,"opportunities.",11.5,MU)+f'<line x1="652" y1="222" x2="690" y2="222" stroke="{B}" stroke-width="2"/>'+t(790,236,"➤",22,B))

# CONNECT
L=[("GH","GitHub","MuhammadMuzammil-TheDeveloper"),("in","LinkedIn","Muhammad Muzammil"),("@","Email","muzammil.muhammad7782@gmail.com"),("🌐","Portfolio","(Your Portfolio URL)")]
ls="".join(box(330,36+i*32,380,26,"#0a1430",ST,6)+t(344,54+i*32,a,11,B,700,SF)+t(380,54+i*32,b,11,TX,600)+t(450,54+i*32,c,11,MU) for i,(a,b,c) in enumerate(L))
svg("connect",860,176,box(0,0,860,176)+pr(16,26,"connect")+t(20,78,"Connect with Muhammad Muzammil",21,TX,700)+t(20,106,"Feel free to reach out — I'm always open to new opportunities,",12,MU)+t(20,124,"collaborations and interesting projects.",12,MU)+ls+
 "".join(t(785,70+i*26,l,17,TX,400,CU,"middle",True,-8) for i,l in enumerate(["Code","— Create","Contribute"])))
