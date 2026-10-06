import base64,html,os
D=os.path.dirname(os.path.abspath(__file__))
BG,PN,P2,BD,TX,MU,BI="#060d1f","#0a1330","#08112a","#1a2a52","#e8eeff","#93a1c4","#c3cde6"
G,B,P,Y,C="#22d37a","#4c8dff","#a56bff","#f5c542","#5ee0ff"
SF="Segoe UI,Helvetica,Arial,sans-serif";MO="Consolas,Menlo,'DejaVu Sans Mono',monospace";CU="Brush Script MT,Segoe Script,Apple Chancery,cursive"
def T(x,y,s,sz=13,c=TX,w=400,f=SF,a="start",e=""):
    return f'<text x="{x}" y="{y}" font-family="{f}" font-size="{sz}" fill="{c}" font-weight="{w}" text-anchor="{a}" {e}>{html.escape(s)}</text>'
def R(x,y,w,h,r=10,f=PN,s=BD,e=""): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{f}" stroke="{s}" {e}/>'
def PR(x,y,cmd,cur=False):
    s=f'<text x="{x}" y="{y}" font-family="{MO}" font-size="12.5"><tspan fill="{G}" font-weight="700">&gt; </tspan><tspan fill="{G}">muzammil@github</tspan><tspan fill="{TX}"> ~ $ {html.escape(cmd)}</tspan></text>'
    if cur: s+=f'<rect x="{x+(len(cmd)+23)*7.55}" y="{y-11}" width="7" height="14" fill="{C}"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>'
    return s
def b64(p,m): return f"data:{m};base64,"+base64.b64encode(open(f"{D}/{p}","rb").read()).decode()
LN=lambda *a,**k:f'<path {" ".join(f"{x.replace(chr(95),chr(45))}=\"{y}\"" for x,y in k.items())}/>'
def ic(d,x,y,c="#cfd8f2",sw=1.6,f="none"): return f'<g transform="translate({x} {y})"><path d="{d}" fill="{f}" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/></g>'
USER="M-5 -6a5 5 0 1 0 10 0a5 5 0 1 0 -10 0M-9 11a9 7 0 0 1 18 0"
BRIEF="M-10 -5h20v14h-20zM-4 -5v-3h8v3M-10 1h20"
CAP="M-12 -3l12 -6l12 6l-12 6zM-7 0v6c4 3 10 3 14 0v-6"
PIN="M0 11c-7 -8 -8 -11 -8 -15a8 8 0 0 1 16 0c0 4 -1 7 -8 15zM-3 -4a3 3 0 1 0 6 0a3 3 0 1 0 -6 0"
b=[]
a=b.append
# ---- background / nav ----
a(f'<defs><radialGradient id="gl" cx=".78" cy=".13" r=".5"><stop offset="0" stop-color="#1c3b9a" stop-opacity=".55"/><stop offset="1" stop-color="{BG}" stop-opacity="0"/></radialGradient><linearGradient id="ng" x1="0" x2="1" spreadMethod="reflect"><stop offset="0" stop-color="#3b82f6"/><stop offset=".5" stop-color="#5aa2ff"/><stop offset="1" stop-color="#3b82f6"/><animateTransform attributeName="gradientTransform" type="translate" from="-1 0" to="1 0" dur="6s" repeatCount="indefinite"/></linearGradient><linearGradient id="mh" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".14" stop-color="#fff"/><stop offset=".86" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient><linearGradient id="mv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".12" stop-color="#fff"/></linearGradient><mask id="m1"><rect x="585" y="62" width="335" height="334" fill="url(#mh)"/></mask><mask id="m2"><rect x="585" y="62" width="335" height="334" fill="url(#mv)"/></mask><linearGradient id="cta" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1a3c"/><stop offset="1" stop-color="#241a4d"/></linearGradient><linearGradient id="sc" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{C}" stop-opacity="0"/><stop offset=".5" stop-color="{C}" stop-opacity=".25"/><stop offset="1" stop-color="{C}" stop-opacity="0"/></linearGradient><clipPath id="ac"><rect x="42" y="433" width="233" height="196" rx="8"/></clipPath></defs>')
a(f'<rect width="1024" height="1536" fill="{BG}"/><rect width="1024" height="420" fill="url(#gl)"/><rect width="1024" height="54" fill="#070e24"/><line x1="0" y1="54.5" x2="1024" y2="54.5" stroke="{BD}"/>')
a(T(40,38,"MZ",25,"#7aa7ff",800,SF)+T(90,34,"Muhammad Muzammil",15.5,TX,600))
nv=[(507,"⌂","Home"),(596,"</>","Projects"),(697,"⚙","Skills"),(785,"♛","Achievements"),(911,"☺","Connect")]
for x,g,l in nv:
    on=l=="Home";c=B if on else MU
    a(T(x,33,g,14,c if on else MU,400,MO)+T(x+(25 if len(g)==1 else 30),33,l,12,TX if on else MU,400))
a(f'<rect x="505" y="52" width="57" height="2.5" fill="{B}"><animate attributeName="opacity" values="1;.4;1" dur="3s" repeatCount="indefinite"/></rect>')
# ---- hero ----
a(f'<g mask="url(#m1)"><g mask="url(#m2)"><image href="{b64("photo.jpg","image/jpeg")}" x="585" y="62" width="335" height="334" preserveAspectRatio="none"/></g></g>')
a("".join(T(955+ (i%2)*3,138+i*26,w,22,TX,400,CU,"middle",f'font-style="italic" transform="rotate(-12 955 {138+i*26})"') for i,w in enumerate(["Better","Code","Bigger","Dreams"])))
a(f'<line x1="925" y1="232" x2="972" y2="214" stroke="{TX}" stroke-width="1.3"/>')
a(f'<rect x="40" y="95" width="173" height="28" rx="14" fill="#0e3a3a"/><circle cx="59" cy="109" r="4.5" fill="{G}"><animate attributeName="opacity" values="1;.3;1" dur="1.8s" repeatCount="indefinite"/></circle>'+T(75,114,"Full-Stack Developer",13,G,600))
a(f'<text x="42" y="178" font-family="{SF}" font-size="47" font-weight="800" fill="{TX}" letter-spacing="-.5">Muhammad <tspan fill="url(#ng)">Muzammil</tspan></text>')
a(T(41,212,"Full-Stack Web Developer (MERN Stack)  |  Karachi, Pakistan",18.5,TX,500))
for i,l in enumerate(["I'm Muhammad Muzammil, a Full-Stack Web Developer and BSCS student","at KIET, Karachi, Pakistan, working across the MERN stack (MongoDB,","Express.js, React.js, Node.js) and WordPress. I build web apps end to end —","from Supabase/MongoDB-backed backends to React and vanilla-JS frontends."]): a(T(41,248+i*21.5,l,14.3,BI))
a(f'<path d="M52 336c-9 8-11 22-2 33c1 -5 2 -10 2 -14c0 4 1 9 2 14c8 -10 7 -26 -2 -33z" fill="{G}"/>'+T(107,360,"ex",25,"#d7def2",300)+
 f'<g transform="translate(164 352)" fill="none" stroke="#4cc9f0" stroke-width="1.6"><ellipse rx="17" ry="6.5"/><ellipse rx="17" ry="6.5" transform="rotate(60)"/><ellipse rx="17" ry="6.5" transform="rotate(120)"/><circle r="2.5" fill="#4cc9f0"/></g>'+
 f'<path d="M222 335l15 8v18l-15 8l-15 -8v-18z" fill="none" stroke="#7ac943" stroke-width="1.8"/>'+T(222,357,"JS",13,"#7ac943",700,SF,"middle")+
 f'<circle cx="283" cy="352" r="17" fill="none" stroke="#cfd8f2" stroke-width="1.8"/>'+T(283,358,"W",16,"#cfd8f2",700,SF,"middle")+
 f'<line x1="330" y1="337" x2="330" y2="368" stroke="{BD}" stroke-width="1.4"/>'+T(358,357,"Build  →  Learn  →  Grow",17,B,400,CU,"start",'font-style="italic"'))
# ---- whoami ----
a(R(30,398,544,245,12)+PR(45,418,"whoami")+R(41,432,235,198,8,P2)+f'<g clip-path="url(#ac)"><image href="{b64("ascii.png","image/png")}" x="44" y="435" width="230" height="192"/><rect x="42" y="433" width="233" height="55" fill="url(#sc)"><animate attributeName="y" values="380;640" dur="4s" repeatCount="indefinite"/></rect></g>')
a(R(292,432,270,198,8,P2))
for i,(g,t1,t2) in enumerate([(USER,"Muhammad Muzammil","Full Stack Developer Intern"),(BRIEF,"NexSoft Solutions","(Current)"),(CAP,"BSCS – KIET Karachi","(Grad. 2027)"),(PIN,"Karachi, Pakistan","")]):
    y=461+i*50
    a(ic(g,327,y)+(T(356,y-5,t1,13.5,TX,500)+T(356,y+13,t2,12,MU) if t2 else T(356,y+4,t1,13.5,TX,500)))
a(R(590,398,406,245,12)+R(612,418,22,22,4,"none","#cfd8f2")+T(617,434,">_",10,"#cfd8f2",700,MO)+T(647,435,"Current Status",15.5,TX,500))
for i,(c,s) in enumerate([(G,"Full Stack Developer Intern @ NexSoft Solutions"),(B,"Previously: WordPress Blog Developer @ Webera Solution"),(P,"Education: BSCS, KIET Karachi (gradu. 2027)"),(Y,"Location: Karachi, Pakistan")]):
    y=469+i*33.3
    a(f'<circle cx="620" cy="{y}" r="6.5" fill="{c}"><animate attributeName="opacity" values="1;.45;1" dur="2.4s" begin="{i*.4}s" repeatCount="indefinite"/></circle>'+T(641,y+4.5,s,13,TX))
a(T(611,618,"❝",30,"#3a4a78",800,"Georgia,serif")+T(646,614,"“Turning ideas into real web applications.”",13.3,MU,400,SF,"start",'font-style="italic"'))
# ---- contributions ----
a(R(30,661,966,176,12)+PR(45,681,"./contributions.sh")+T(982,682,"View more on GitHub  →",10.5,MU,400,SF,"end"))
a(R(41,698,720,128,8,"#07102a","#13224a"))
cols=["#0f1d42","#0f5a3a","#157f4b","#22c55e","#33e089"]
for r in range(7):
    for c in range(53):
        k=abs(__import__("math").sin((r*53+c)*12.9898)*43758.5453)%1
        l=(0 if k<.7 else 1) if r<2 else (0 if k<.35 else 1 if k<.5 else 2 if k<.72 else 3 if k<.92 else 4) if r>=3 else (0 if k<.6 else 1 if k<.8 else 2)
        dl=(c*.07+r*.05)%4
        a(f'<rect x="{53+c*13.1:.1f}" y="{712+r*12.9:.1f}" width="11" height="11" rx="2" fill="{cols[l]}">'+(f'<animate attributeName="opacity" values="1;.55;1" dur="4s" begin="-{dl:.2f}s" repeatCount="indefinite"/>' if l else '')+'</rect>')
for x,m in zip([65,126,181,240,298,357,416,475,533,591,651,709],["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]): a(T(x,814,m,10.5,MU,400,SF,"middle"))
a(f'<line x1="771" y1="697" x2="771" y2="826" stroke="{BD}"/>')
for i,(g,n,l) in enumerate([("▦","1,200+","Total Contributions"),("▣","20+","Repositories"),("◷","2+","Years on GitHub")]):
    y=720+i*43
    a(T(798,y+5,g,20,[G,P,B][i],400,SF,"middle")+T(822,y,n,15.5,TX,700)+T(822,y+15,l,11,MU))
# ---- projects ----
a(R(30,854,966,233,12)+PR(45,874,"ls -la ~/projects")+T(982,875,"View all projects  →",10.5,MU,400,SF,"end"))
PJ=[("📝",P,["NoteStack"],["Supabase-powered","sticky-notes SaaS with","glassmorphism auth and","a pastel dashboard."]),("▦",G,["Asset Maintenance","System"],["QR-based asset tracking","with Admin / Technician /","Public roles on Supabase."]),("🧠",B,["AI Quiz Platform"],["JavaScript quiz app wired","to the Open Trivia DB API."]),("🌐","#38bdf8",["WorldAtlas"],["Country/geo data explorer","built with vanilla","JavaScript."]),("➕","#ef4444",["Hospital Management","System"],["Patient, staff, and records","management system."]),("🖥",P,["SMIT UI Clone"],["Pixel-level clone of the","SMIT website UI."])]
for i,(e,c,ti,de) in enumerate(PJ):
    x=42+i*160
    a(f'<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -3;0 0" dur="4s" begin="-{i*.7:.1f}s" repeatCount="indefinite"/>'+R(x,894,148,182,10,P2,BD)+f'<rect x="{x+13}" y="907" width="34" height="34" rx="8" fill="{c}" fill-opacity=".28"/>'+T(x+30,930,e,17,c,400,SF,"middle")
      +"".join(T(x+13,962+k*15-(len(ti)-1)*3,l,13.3,TX,600) for k,l in enumerate(ti))
      +"".join(T(x+13,(996 if len(ti)==2 else 984)+k*15.5-(0 if len(ti)==2 else 0),l,10.4,MU) for k,l in enumerate(de))+T(x+13,1060,"Live Demo  →",11,B,500)+'</g>')
# ---- skills ----
a(R(30,1105,632,252,12)+PR(45,1124,"cat skills.txt")+f'<line x1="424" y1="1142" x2="424" y2="1340" stroke="{BD}"/>'+T(45,1165,"</>",14,TX,700,MO)+T(75,1165,"Tech Stack",14.5,TX,500))
for ri,row in enumerate(["JavaScript,Node.js,Express.js,MongoDB,React.js","Tailwind CSS,Bootstrap,Supabase,WordPress","Python,C++,HTML5,CSS3,REST APIs","Firebase,MySQL,Git,GitHub,Postman","VS Code,Netlify,Vercel,Elementor"]):
    x=45;y=1180+ri*30.6
    for s in row.split(","):
        w=len(s)*6.6+26;a(R(x,y,w,24,12,"#101c3d","#1d2e5c")+T(x+w/2,y+16,s,11,TX,400,SF,"middle"));x+=w+6
a(T(440,1165,"🏆",15)+T(466,1165,"Achievements",14.5,TX,500))
for i,(e,c,t1,t2,t3) in enumerate([("🏆",Y,"1st Place","CODE JUNG 2025","(Web Development)"),("🏅",B,"Top 5","SMIT Hackathon 2025",""),("📜","#38bdf8","Cisco","Networking Basics","Certification")]):
    y=[1192,1259,1306][i];a(T(458,y+22,e,28,TX,400,SF,"middle")+T(490,y,t1,12.8,c if i==0 else TX,700)+T(490,y+17,t2,11.5,MU)+(T(490,y+32,t3,11.5,MU) if t3 else ""))
# CTA
a(f'<rect x="677" y="1105" width="319" height="252" rx="12" fill="url(#cta)" stroke="{BD}"/>')
import random;random.seed(3)
a("".join(f'<circle cx="{random.randint(690,985)}" cy="{random.randint(1115,1260)}" r="{random.choice([.6,.9,1.2])}" fill="#bcd0ff"><animate attributeName="opacity" values=".15;1;.15" dur="{random.uniform(2,5):.1f}s" begin="-{random.uniform(0,5):.1f}s" repeatCount="indefinite"/></circle>' for _ in range(40)))
a('<polygon points="677,1357 677,1300 740,1255 790,1290 860,1210 930,1280 996,1240 996,1357" fill="#0a1228" opacity=".85"/><polygon points="860,1210 835,1245 850,1240 862,1255 872,1238 890,1246" fill="#c8d6ff" opacity=".35"/>')
a(T(710,1181,"Let's Build",24,TX,700)+T(710,1210,"Something Great",24,TX,700)+T(710,1242,"Open for collaborations, freelance",13.2,"#c3cde6")+T(710,1261,"projects and opportunities.",13.2,"#c3cde6")+f'<line x1="710" y1="1289" x2="748" y2="1289" stroke="{B}" stroke-width="2"/>')
a(f'<g><animateTransform attributeName="transform" type="translate" values="0 0;6 -5;0 0" dur="3.5s" repeatCount="indefinite"/><path d="M810 1305l46 -22l-8 28l-14 -7l-9 8l-2 -10z" fill="none" stroke="{B}" stroke-width="1.6" stroke-linejoin="round"/></g>')
# ---- connect ----
a(R(30,1374,966,138,12)+PR(45,1394,"connect",True)+T(54,1432,"Connect with Muhammad Muzammil",19,TX,500)+T(54,1462,"Feel free to reach out — I'm always open to new opportunities,",12.2,MU)+T(54,1479,"collaborations and interesting projects.",12.2,MU))
for i,(g,l,v) in enumerate([("◉","GitHub","MuhammadMuzammil-TheDeveloper"),("in","LinkedIn","Muhammad Muzammil"),("✉","Email","muzammil.muhammad7782@gmail.com"),("◎","Portfolio","(Your Portfolio URL)")]):
    y=1400+i*26.2;a(R(426,y,397,24,6,P2,BD)+T(447,y+16,g,12.5,TX,700,SF,"middle")+T(467,y+16,l,10.8,TX,600)+T(529,y+16,v,10.8,MU))
a("".join(T(928,1433+i*24,w,20,TX,400,CU,"middle",f'font-style="italic" transform="rotate(-14 928 {1433+i*24})"') for i,w in enumerate(["Code","— Create","Contribute"])))
a(f'<line x1="888" y1="1492" x2="935" y2="1475" stroke="{TX}" stroke-width="1.2"/>')
open(f"{D}/profile.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1536" viewBox="0 0 1024 1536" role="img" aria-label="Muhammad Muzammil — Full-Stack Web Developer (MERN Stack), Karachi, Pakistan"><title>Muhammad Muzammil — Full-Stack Web Developer (MERN)</title>{"".join(b)}</svg>')
