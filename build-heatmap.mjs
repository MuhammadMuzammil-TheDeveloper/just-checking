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
