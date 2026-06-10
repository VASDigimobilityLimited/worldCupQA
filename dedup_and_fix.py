#!/usr/bin/env python3
"""Conservative within-cluster dedup of WorldCup_ShipReady_ALL.csv, then fix
Excel date-corrupted answers. Verifies every correction against the explanation.
Writes the cleaned result back to WorldCup_ShipReady_ALL.csv (keeps a .pre-dedup backup)."""
import csv,re,shutil
from collections import defaultdict

SRC="WorldCup_ShipReady_ALL.csv"
rows=list(csv.reader(open(SRC,encoding="utf-8")))
HEAD,data=rows[0],rows[1:]

# ---------- 1. cluster (same country+answer, Jaccard>=0.80, excl numeric & distinct-family) ----------
def toks(s): return frozenset(re.sub(r'[^a-z0-9 ]','',s.lower()).split())
def na(s): return re.sub(r'[^a-z0-9]','',s.lower())
T={i:toks(r[2]) for i,r in enumerate(data)}
by=defaultdict(list)
for i,r in enumerate(data): by[r[1]].append(i)
def jac(a,b):
    u=len(a|b); return len(a&b)/u if u else 0
NUM=re.compile(r'^\d+$')
FAM={"stage":{"semifinal":"s","semifinals":"s","semis":"s","semi":"s","quarterfinal":"q","quarterfinals":"q","quarters":"q","quarter":"q"},
 "ord":{"first":"1","1st":"1","second":"2","2nd":"2","third":"3","3rd":"3","fourth":"4","4th":"4"},
 "venue":{"home":"h","away":"a"},
 "ext":{"most":"H","highest":"H","best":"H","oldest":"H","largest":"H","least":"L","lowest":"L","fewest":"L","worst":"L","youngest":"L","smallest":"L"}}
def distinct(a,b):
    ao,bo=a-b,b-a
    for mp in FAM.values():
        sa={mp[t] for t in ao if t in mp}; sb={mp[t] for t in bo if t in mp}
        if sa and sb and sa!=sb: return True
    return False
par={}
def find(x):
    par.setdefault(x,x)
    while par[x]!=x: par[x]=par[par[x]]; x=par[x]
    return x
for c,idxs in by.items():
    inv=defaultdict(list)
    for i in idxs:
        for t in T[i]: inv[t].append(i)
    cand=set()
    for lst in inv.values():
        if len(lst)>1:
            for a in range(len(lst)):
                for b in range(a+1,len(lst)): cand.add((min(lst[a],lst[b]),max(lst[a],lst[b])))
    for i,j in cand:
        if na(data[i][3])!=na(data[j][3]): continue
        if jac(T[i],T[j])<0.80: continue
        if any(NUM.match(t) for t in T[i]^T[j]): continue
        if distinct(T[i],T[j]): continue
        par.setdefault(i,i);par.setdefault(j,j);par[find(i)]=find(j)
clusters=defaultdict(set)
for i in list(par): clusters[find(i)].add(i)
clusters=[sorted(s) for s in clusters.values() if len(s)>1]

# ---------- 2. conservative signature (collapse only synonym/filler/nationality/order) ----------
ADJ={"Algeria":["algerian"],"Argentina":["argentine","argentinian"],"Australia":["australian"],"Austria":["austrian"],"Belgium":["belgian"],"Bosnia and Herzegovina":["bosnian","herzegovinian"],"Brazil":["brazilian"],"Cabo Verde":["cape","verdean","cabo","verde"],"Cameroon":["cameroonian"],"Canada":["canadian"],"Chile":["chilean"],"Colombia":["colombian"],"Costa Rica":["rican","costa","rica"],"Côte d'Ivoire":["ivorian","ivorien"],"Croatia":["croatian"],"Czechia":["czech"],"Denmark":["danish","dane"],"DR Congo":["congolese","congo"],"Ecuador":["ecuadorian","ecuadorean"],"Egypt":["egyptian"],"England":["english"],"France":["french"],"Germany":["german"],"Ghana":["ghanaian"],"Iran":["iranian"],"Iraq":["iraqi"],"Italy":["italian"],"Jamaica":["jamaican"],"Japan":["japanese"],"Jordan":["jordanian"],"Mexico":["mexican"],"Morocco":["moroccan"],"Netherlands":["dutch","netherlands"],"New Zealand":["zealand","kiwi","kiwis"],"Nigeria":["nigerian"],"Paraguay":["paraguayan"],"Senegal":["senegalese"],"Switzerland":["swiss"],"Tunisia":["tunisian"],"USA":["american","americans","us","usa"]}
STOP=set("the a an in on at of for to did was were is are has have had their his her its them they it that this who which what when how by during after before with as from into".split())
FILLER=set("fifa world cup uefa euro afcon copa america concacaf conmebol caf nations africa tournament finals scenario national".split())
SYN={"nation":"team","country":"team","side":"team","teams":"team","nations":"team","footballer":"player","star":"player","players":"player","attacker":"player","striker":"player","forward":"player","man":"player","beaten":"beat","defeat":"beat","defeated":"beat","defeats":"beat","overcame":"beat","downed":"beat","thrashed":"beat","routed":"beat","hammered":"beat","demolished":"beat","thrash":"beat","rout":"beat","topped":"win","won":"win","victory":"win","triumph":"win","wins":"win","keeper":"gk","goalkeeper":"gk","goalie":"gk","manager":"mgr","coach":"mgr","boss":"mgr","gaffer":"mgr","oversaw":"led","achieved":"led","netted":"scored","notched":"scored","struck":"scored","score":"scored","scores":"scored","goals":"goal","matches":"match","games":"match","game":"match"}
def sig(idx):
    country=data[idx][1]
    drop=STOP|FILLER|{w.lower() for w in country.split()}|set(ADJ.get(country,[]))
    return tuple(sorted(SYN.get(t,t) for t in re.sub(r'[^a-z0-9 ]','',data[idx][2].lower()).split() if t not in drop))

# ---------- corruption detection (needed for keep-preference) ----------
MON={m:i for i,m in enumerate(["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"],1)}
FULL={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
MONYY=re.compile(r'^([A-Za-z]{3})-(\d{2})$')         # Nov-18  -> November 2018
DDMON=re.compile(r'^(\d{1,2})-([A-Za-z]{3})$')         # 02-Jan  -> 2-1 (score)
def is_corrupt(ans):
    a=ans.strip()
    return bool(MONYY.match(a) or DDMON.match(a))

# ---------- 3. choose survivor per signature group ----------
remove=set()
for cl in clusters:
    groups=defaultdict(list)
    for i in cl: groups[sig(i)].append(i)
    for g in groups.values():
        if len(g)==1: continue
        # keep: prefer non-corrupted answer, then longest explanation, then lowest index
        keep=sorted(g,key=lambda i:(is_corrupt(data[i][3]), -len(data[i][6]), i))[0]
        for i in g:
            if i!=keep: remove.add(i)

survivors=[data[i] for i in range(len(data)) if i not in remove]

# ---------- 4. fix Excel corruption on survivors, verifying against explanation ----------
fixed=[]; unverified=[]
for rec in survivors:
    ans=rec[3].strip(); expl=rec[6]
    m=MONYY.match(ans)
    if m and m.group(1).lower() in MON:
        mon=MON[m.group(1).lower()]; yr=2000+int(m.group(2))
        corrected=f"{FULL[mon]} {yr}"
        ok=corrected.lower() in expl.lower()
        rec[3]=corrected
        (fixed if ok else unverified).append((rec[1],ans,corrected,ok))
        continue
    m=DDMON.match(ans)
    if m and m.group(2).lower() in MON:
        a=int(m.group(1)); b=MON[m.group(2).lower()]
        corrected=f"{a}-{b}"
        ok=(corrected in expl) or (f"{a}–{b}" in expl)
        rec[3]=corrected
        (fixed if ok else unverified).append((rec[1],ans,corrected,ok))

# ---------- 5. write ----------
shutil.copy(SRC,SRC.replace(".csv",".pre-dedup.csv"))
with open(SRC,"w",encoding="utf-8",newline="") as f:
    w=csv.writer(f,quoting=csv.QUOTE_MINIMAL); w.writerow(HEAD); w.writerows(survivors)

print(f"clusters processed: {len(clusters)}")
print(f"duplicate rows removed: {len(remove)}")
print(f"final row count: {len(survivors)} (from {len(data)})")
print(f"\nExcel corruption fixed (verified vs explanation): {len(fixed)}")
print(f"Excel corruption fixed but NOT found verbatim in explanation: {len(unverified)}")
for c,o,n,ok in unverified:
    print(f"   [{c}] {o!r} -> {n!r}  (review)")
print(f"\nbackup of pre-dedup file: {SRC.replace('.csv','.pre-dedup.csv')}")
print("sample corruption fixes:")
for c,o,n,ok in fixed[:12]:
    print(f"   [{c}] {o!r} -> {n!r}")
