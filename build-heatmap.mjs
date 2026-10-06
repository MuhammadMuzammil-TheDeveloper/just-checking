import fs from 'node:fs';
const u=process.env.GH_USER,tk=process.env.GITHUB_TOKEN;
const q=`query($u:String!){user(login:$u){repositories(ownerType:OWNER,privacy:PUBLIC){totalCount}contributionsCollection{contributionCalendar{totalContributions weeks{contributionDays{contributionCount date}}}}}}`;
const r=await fetch('https://api.github.com/graphql',{method:'POST',headers:{Authorization:`bearer ${tk}`,'Content-Type':'application/json'},body:JSON.stringify({query:q,variables:{u}})});
const j=await r.json();if(!j.data)throw new Error(JSON.stringify(j));
const {repositories:rp,contributionsCollection:cc}=j.data.user,cal=cc.contributionCalendar;
const all=cal.weeks.flatMap(w=>w.contributionDays),max=Math.max(1,...all.map(d=>d.contributionCount));
const best=all.reduce((a,b)=>b.contributionCount>a.contributionCount?b:a);
const lv=['#12204a','#0e4f3a','#12834f','#22d37a','#7dffb8'];
let c='';cal.weeks.forEach((w,i)=>w.contributionDays.forEach((d,k)=>{
 const n=d.contributionCount,l=n?Math.min(4,1+Math.floor(3*n/max)):0;
 c+=`<rect x="${20+i*14}" y="${50+k*14}" width="11" height="11" rx="2" fill="${lv[l]}" opacity="0"><title>${d.date}: ${n}</title><animate attributeName="opacity" to="1" begin="${(i*.03).toFixed(2)}s" dur=".4s" fill="freeze"/>${n?`<animate attributeName="opacity" values="1;.55;1" dur="4s" begin="${(3+i*.08).toFixed(2)}s" repeatCount="indefinite"/>`:''}</rect>`;}));
const m="font-family='Consolas,Menlo,monospace'";
fs.writeFileSync('contrib-heatmap.svg',`<svg xmlns="http://www.w3.org/2000/svg" width="780" height="190" viewBox="0 0 780 190"><rect width="780" height="190" rx="14" fill="#050b1c"/><text x="20" y="30" ${m} font-size="12" fill="#22d37a">$ ./contributions.sh</text><text x="760" y="30" ${m} font-size="12" fill="#8f9fc4" text-anchor="end">${cal.totalContributions} contributions · ${rp.totalCount} public repos · best day ${best.contributionCount} (${best.date})</text>${c}<rect y="44" width="3" height="104" fill="#5ee0ff" opacity=".6"><animate attributeName="x" values="20;762" dur="5s" repeatCount="indefinite"/></rect><text x="20" y="172" ${m} font-size="10" fill="#8f9fc4">updated ${new Date().toISOString().slice(0,10)} · synced by GitHub Actions</text></svg>`);
// ---- stats.svg: followers, stars, repos, top languages ----
const q2=`query($u:String!){user(login:$u){followers{totalCount}repositories(ownerType:OWNER,privacy:PUBLIC,first:100,isFork:false){totalCount nodes{stargazerCount languages(first:5,orderBy:{field:SIZE,direction:DESC}){edges{size node{name color}}}}}}}`;
const j2=await(await fetch('https://api.github.com/graphql',{method:'POST',headers:{Authorization:`bearer ${tk}`,'Content-Type':'application/json'},body:JSON.stringify({query:q2,variables:{u}})})).json();
const us=j2.data.user,rs=us.repositories.nodes,L={};
rs.forEach(x=>x.languages.edges.forEach(e=>{L[e.node.name]??={s:0,c:e.node.color||'#5ee0ff'};L[e.node.name].s+=e.size}));
const tot=Object.values(L).reduce((a,x)=>a+x.s,0)||1,top=Object.entries(L).sort((a,b)=>b[1].s-a[1].s).slice(0,5);
const cards=[['Contributions (1y)',cal.totalContributions],['Public repos',us.repositories.totalCount],['Stars earned',rs.reduce((a,x)=>a+x.stargazerCount,0)],['Followers',us.followers.totalCount]];
const sf="font-family='Segoe UI,Arial,sans-serif'";
let s=cards.map((c,i)=>`<g opacity="0"><animate attributeName="opacity" to="1" begin="${i*.2}s" dur=".5s" fill="freeze"/><rect x="${20+i*210}" y="50" width="190" height="74" rx="10" fill="#0a1330" stroke="#1b2b55"/><text x="${115+i*210}" y="92" ${sf} font-size="30" font-weight="800" fill="#5ee0ff" text-anchor="middle">${c[1]}</text><text x="${115+i*210}" y="112" ${sf} font-size="11" fill="#8f9fc4" text-anchor="middle">${c[0]}</text></g>`).join('');
s+=top.map(([n,v],i)=>{const w=Math.max(4,Math.round(520*v.s/tot)),y=156+i*24;return `<text x="20" y="${y+11}" ${sf} font-size="12" fill="#e8eeff">${n}</text><rect x="120" y="${y}" width="520" height="14" rx="7" fill="#12204a"/><rect x="120" y="${y}" width="0" height="14" rx="7" fill="${v.c}"><animate attributeName="width" to="${w}" begin="${.6+i*.15}s" dur="1s" fill="freeze"/></rect><text x="652" y="${y+11}" ${sf} font-size="12" fill="#8f9fc4">${(100*v.s/tot).toFixed(1)}%</text>`}).join('');
fs.writeFileSync('stats.svg',`<svg xmlns="http://www.w3.org/2000/svg" width="860" height="290" viewBox="0 0 860 290"><rect width="860" height="290" rx="14" fill="#050b1c"/><text x="20" y="30" font-family="Consolas,monospace" font-size="13" fill="#22d37a" font-weight="700">$ ./stats.sh --languages</text>${s}</svg>`);
