# QA_FAILED_LIVENESS — Batch 2 (passed mechanical but FAILED TC-06 liveness — dangerous)

> Batch-2 dataset (`Pre-worldcup2.csv` → `QA_PASSED_b2.md`). "Looks clean but is factually wrong."
> Each entry: Q, Answer, why it fails, source URL, remedy. Row N = line N of `Pre-worldcup2.csv`.

Total failed-liveness (batch 2) so far: **69**  (Canada 7821–9330 COMPLETE: 69)

### Row 7822 — Canada (medium) — FAIL
**Q:** After 2022 World Cup qualification, Canada's highest FIFA ranking was which number?
**Answer:** 33rd
**Why it fails:** Out of date: 33rd was Canada's FIFA-ranking peak in Feb 2022, but it is no longer their highest — under Marsch they climbed to a program-record ~26th in September 2025. So '33rd = highest' is stale.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Update: Canada's highest FIFA ranking is now ~26th (2025); 33rd was the 2022 peak, since surpassed.

### Row 7823 — Canada (hard) — FAIL
**Q:** After Canada qualified for the 2022 World Cup, when did they reach their highest FIFA ranking?
**Answer:** In 2022
**Why it fails:** Out of date: Canada did NOT reach their highest FIFA ranking in 2022 — they hit a program-record ~26th in September 2025 (under Marsch). 2022 (33rd) was only their then-record.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Their highest ranking was reached in 2025 (~26th), not 2022.

### Row 7826 — Canada (medium) — FAIL
**Q:** After Canada's 2022 World Cup qualification, which nation's highest FIFA ranking was 33rd?
**Answer:** Canada
**Why it fails:** Out of date: 33rd was Canada's FIFA-ranking peak in Feb 2022, but it is no longer their highest — under Marsch they climbed to a program-record ~26th in September 2025. So '33rd = highest' is stale.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Update: Canada's highest FIFA ranking is now ~26th (2025); 33rd was the 2022 peak, since surpassed.

### Row 7828 — Canada (medium) — FAIL
**Q:** After qualifying for the 2022 FIFA World Cup, Canada's highest FIFA ranking was what position?
**Answer:** 33rd
**Why it fails:** Out of date: 33rd was Canada's FIFA-ranking peak in Feb 2022, but it is no longer their highest — under Marsch they climbed to a program-record ~26th in September 2025. So '33rd = highest' is stale.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Update: Canada's highest FIFA ranking is now ~26th (2025); 33rd was the 2022 peak, since surpassed.

### Row 7831 — Canada (medium) — FAIL
**Q:** After qualifying in 2022, what was Canada's highest FIFA ranking?
**Answer:** 33rd
**Why it fails:** Out of date: 33rd was Canada's FIFA-ranking peak in Feb 2022, but it is no longer their highest — under Marsch they climbed to a program-record ~26th in September 2025. So '33rd = highest' is stale.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Update: Canada's highest FIFA ranking is now ~26th (2025); 33rd was the 2022 peak, since surpassed.

### Row 7833 — Canada (medium) — FAIL
**Q:** After which 2024 Copa América semi-final did Canada's World Cup qualifying campaign begin?
**Answer:** Lost 2-0 to Argentina
**Why it fails:** False premise: as a 2026 CO-HOST, Canada auto-qualifies and has NO World Cup qualifying campaign. There was nothing for the 2024 Copa semi-final to 'begin'.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Canada qualifies automatically as host; there is no 2026 qualifying campaign.

### Row 7859 — Canada (easy) — FAIL
**Q:** At the 2026 World Cup, Canada will co-host. Which nation was announced as a co-host before Canada?
**Answer:** United States
**Why it fails:** Fabricated premise: the 2026 hosting was awarded to a single United bid (USA, Canada, Mexico) jointly on 13 June 2018 — there was no sequence in which the US was 'announced as co-host before Canada'.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The three co-hosts were awarded together; remove the false sequencing.

### Row 7864 — Canada (easy) — FAIL
**Q:** At which 2022 World Cup venue did Canada lose its final group match?
**Answer:** Al Janoub Stadium
**Why it fails:** False venue: Canada's final 2022 group match (the 2-1 loss to Morocco) was played at AL THUMAMA STADIUM, not Al Janoub Stadium.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Change venue to Al Thumama Stadium.

### Row 7913 — Canada (easy) — FAIL
**Q:** Canada lost its final 2022 World Cup group match to Morocco by what score?
**Answer:** 2026-01-02 00:00:00
**Why it fails:** Excel date-corruption: answer stored as '2026-01-02 00:00:00' instead of the score 2-1 (Canada lost 2-1 to Morocco).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Replace with '2-1'.

### Row 7916 — Canada (medium) — FAIL
**Q:** Canada participated in how many CONCACAF Gold Cups from 2006 to 2024?
**Answer:** Eight Gold Cups
**Why it fails:** Inconsistent/likely wrong: there were NINE Gold Cup editions from 2006 to 2024 (2007, 09, 11, 13, 15, 17, 19, 21, 23), and the explanation says Canada appeared in 'every edition' — which is nine, not eight.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Change to nine (Canada appeared in every edition 2007-2023).

### Row 7919 — Canada (medium) — FAIL
**Q:** Canada qualified for the 2022 World Cup after missing how many editions?
**Answer:** Nine World Cups
**Why it fails:** Wrong count: Canada missed EIGHT World Cups between 1986 and 2022 (1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018), not nine. The explanation's '1990 to 2018' is eight tournaments.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Change to eight World Cups.

### Row 7936 — Canada (medium) — FAIL
**Q:** Canada's 2022 World Cup qualification saw them peak at what FIFA ranking?
**Answer:** 33rd
**Why it fails:** Out of date: the explanation calls 33rd Canada's 'highest-ever FIFA ranking', but they have since reached a program-record ~26th (Sept 2025). 33rd was the 2022 peak, not the all-time high.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Their highest-ever is now ~26th (2025); 33rd was the 2022 peak.

### Row 7949 — Canada (easy) — FAIL
**Q:** Canada's BC Place in Vancouver will host 2026 World Cup matches. Which stadium has the larger capacity?
**Answer:** BC Place
**Why it fails:** Wrong: BC Place (~54,500) is NOT the largest of the options — Estadio Azteca (~87,000) and MetLife Stadium (~82,500) are bigger. BC Place is only larger than BMO Field (~30,000).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Azteca/MetLife are larger; the answer is not BC Place.

### Row 7979 — Canada (medium) — FAIL
**Q:** How many CONCACAF Gold Cups did Canada enter from 2006 to 2024?
**Answer:** Seven
**Why it fails:** Wrong/inconsistent count: there were NINE Gold Cup editions from 2006 to 2024 (2007, 09, 11, 13, 15, 17, 19, 21, 23) and the explanation says Canada appeared in 'every edition' — so the figure should be nine, not seven (other rows in this set variously say seven or eight).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Change to nine (Canada played every edition 2007-2023).

### Row 7986 — Canada (medium) — FAIL
**Q:** How many Gold Cups did Canada play in from 2006 to 2024?
**Answer:** Seven tournaments
**Why it fails:** Wrong/inconsistent count: there were NINE Gold Cup editions from 2006 to 2024 (2007, 09, 11, 13, 15, 17, 19, 21, 23) and the explanation says Canada appeared in 'every edition' — so the figure should be nine, not seven (other rows in this set variously say seven or eight).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Change to nine (Canada played every edition 2007-2023).

### Row 8001 — Canada (easy) — FAIL
**Q:** In 2022 qualifying, Canada earned 28 points. Which CONCACAF rival earned 25?
**Answer:** Mexico
**Why it fails:** False: Mexico did NOT earn 25 points — Mexico finished SECOND with 28 points (tied with Canada, behind on goal difference). The teams on 25 were the USA and Costa Rica.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Mexico finished on 28 (2nd); the USA/Costa Rica had 25.

### Row 8004 — Canada (medium) — FAIL
**Q:** In 2022 qualifying, how many games did Canada start unbeaten?
**Answer:** Eight games
**Why it fails:** Wrong/inconsistent: Canada's unbeaten first half of the 2022 CONCACAF Octagonal was SEVEN matches (the Octagonal's 14 games split 7/7), not eight — every other row in this set says seven.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Change to seven matches.

### Row 8015 — Canada (medium) — FAIL
**Q:** In 2022, Canada's highest-ever FIFA ranking of 33rd was achieved after which World Cup event?
**Answer:** Qualifying for the tournament
**Why it fails:** Out of date: 33rd is no longer Canada's 'highest-ever' FIFA ranking — under Marsch they climbed to a program-record ~26th in September 2025. 33rd (Feb 2022) was the then-record.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Highest-ever is now ~26th (2025); 33rd was the 2022 peak.

### Row 8025 — Canada (medium) — FAIL
**Q:** In Canada's 2022 World Cup group stage match, who was their star captain?
**Answer:** Alphonso Davies
**Why it fails:** False: Alphonso Davies was NOT Canada's captain at the 2022 World Cup — Atiba Hutchinson (the 39-year-old most-capped veteran) captained the team. Davies became captain later, under Marsch.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The 2022 captain was Atiba Hutchinson; Davies captained from 2023+.

### Row 8057 — Canada (easy) — FAIL
**Q:** In the 2022 World Cup, Canada lost to Morocco by what score?
**Answer:** 2026-01-02 00:00:00
**Why it fails:** Excel date-corruption: answer stored as '2026-01-02 00:00:00' instead of the score 2-1 (Canada lost 2-1 to Morocco).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Replace with '2-1'.

### Row 8075 — Canada (medium) — FAIL
**Q:** In which FIFA World Cup did Canada's star Alphonso Davies first serve as captain?
**Answer:** 2022 World Cup
**Why it fails:** False: Alphonso Davies was NOT Canada's captain at the 2022 World Cup — Atiba Hutchinson (the 39-year-old most-capped veteran) captained the team. Davies became captain later, under Marsch.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The 2022 captain was Atiba Hutchinson; Davies captained from 2023+.

### Row 8142 — Canada (medium) — FAIL
**Q:** What was Canada's peak FIFA ranking after 2022 World Cup qualification?
**Answer:** 33rd
**Why it fails:** Out of date: 33rd is no longer Canada's highest/peak FIFA ranking — under Marsch they reached a program-record ~26th in September 2025. 33rd (Feb 2022) was only their then-record.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Highest is now ~26th (2025); 33rd was the 2022 peak.

### Row 8153 — Canada (hard) — FAIL
**Q:** When did Canada achieve its highest FIFA ranking after 2022 World Cup qualification?
**Answer:** In 2022
**Why it fails:** Out of date: 33rd is no longer Canada's highest/peak FIFA ranking — under Marsch they reached a program-record ~26th in September 2025. 33rd (Feb 2022) was only their then-record.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Highest is now ~26th (2025); 33rd was the 2022 peak.

### Row 8164 — Canada (hard) — FAIL
**Q:** When did Canada reach its highest FIFA ranking of 33rd?
**Answer:** 2022
**Why it fails:** Out of date: 33rd is no longer Canada's highest/peak FIFA ranking — under Marsch they reached a program-record ~26th in September 2025. 33rd (Feb 2022) was only their then-record.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Highest is now ~26th (2025); 33rd was the 2022 peak.

### Row 8171 — Canada (medium) — FAIL
**Q:** When did Canada's Atiba Hutchinson first surpass 100 international caps?
**Answer:** During 2022 qualifying
**Why it fails:** False: Atiba Hutchinson reached his 100th cap AT the 2022 World Cup (his 100th appearance was v Croatia, 27 Nov 2022), not during 2022 qualifying — qualifying ended in March 2022 with him under 100 caps.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** He passed 100 caps at the 2022 finals, not during qualifying.

### Row 8198 — Canada (medium) — FAIL
**Q:** When was Jesse Marsch appointed as Canada's manager for the 2026 World Cup cycle?
**Answer:** 2023
**Why it fails:** Wrong year: Jesse Marsch was appointed Canada head coach in MAY 2024, not 2023.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Change to 2024.

### Row 8212 — Canada (easy) — FAIL
**Q:** Which 2015 Women's World Cup co-host, Canada or Germany, conceded fewer goals?
**Answer:** Canada
**Why it fails:** False premise: Germany was NOT a co-host of the 2015 Women's World Cup — Canada hosted it alone (Germany only participated). The 'co-host Canada or Germany' framing is incorrect.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Canada solo-hosted the 2015 Women's World Cup; Germany did not co-host.

### Row 8229 — Canada (easy) — FAIL
**Q:** Which 2022 World Cup opponent did Canada score against: Morocco or Croatia?
**Answer:** Morocco
**Why it fails:** False: Canada scored against CROATIA (Alphonso Davies, 2nd minute) — that was a real Canada goal. Their 'goal' in the 2-1 loss to Morocco was an OWN GOAL by Morocco's Nayef Aguerd, not a Canada player. So 'scored only against Morocco' is wrong.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Canada scored v Croatia (Davies); the Morocco goal was an own goal.

### Row 8241 — Canada (easy) — FAIL
**Q:** Which 2026 co-host nation, like Canada, also made its men's World Cup debut as a host?
**Answer:** United States
**Why it fails:** False on both counts: the USA did NOT make its men's World Cup debut as a host in 1994 — it debuted in 1930 (1994 was its 4th appearance). And Canada is not debuting as host in 2026 either (Canada debuted in 1986).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The US debuted in 1930; neither nation debuted 'as host'.

### Row 8246 — Canada (easy) — FAIL
**Q:** Which 2026 host nation, like Canada, will also use two of its own cities?
**Answer:** United States
**Why it fails:** False: the USA will use ELEVEN host cities for 2026, not two. Canada uses two (Toronto, Vancouver) and Mexico three; no co-host matches Canada's two.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The US uses 11 cities; only Canada uses two.

### Row 8273 — Canada (easy) — FAIL
**Q:** Which Canada captain played at Qatar's Al Janoub Stadium in 2022?
**Answer:** Alphonso Davies
**Why it fails:** False on both counts: Canada did NOT play at Al Janoub Stadium in 2022 (their venues were Ahmad bin Ali, Khalifa and Al Thumama), and Alphonso Davies was NOT the captain — Atiba Hutchinson was.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Canada didn't play Al Janoub; the 2022 captain was Hutchinson.

### Row 8284 — Canada (easy) — FAIL
**Q:** Which Canada defender played at Lusail Stadium in the 2022 World Cup?
**Answer:** Richie Laryea
**Why it fails:** False venue: Canada did NOT play at Lusail Stadium in 2022. Their three group games were at Ahmad bin Ali (Belgium), Khalifa (Croatia) and Al Thumama (Morocco).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Canada played no match at Lusail Stadium.

### Row 8300 — Canada (easy) — FAIL
**Q:** Which Canada forward scored his first World Cup goal in 2022?
**Answer:** Cyle Larin
**Why it fails:** False: Alphonso Davies - not Cyle Larin - scored Canada's first-ever men's World Cup goal (v Croatia, 2nd minute, 2022).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Davies scored Canada's first World Cup goal.

### Row 8311 — Canada (easy) — FAIL
**Q:** Which Canada forward was their leading scorer in the 2022 World Cup qualifiers?
**Answer:** Jonathan David
**Why it fails:** False: Canada's leading scorer in/during the 2022 World Cup qualifying campaign was CYLE LARIN (13 goals — the top scorer in all of CONCACAF qualifying), not Jonathan David (9). Larin also became Canada's all-time leading scorer in Jan 2022; David only passed him in Nov 2024.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The 2022 qualifying top scorer (and the all-time leader at that time) was Cyle Larin.

### Row 8315 — Canada (medium) — FAIL
**Q:** Which Canada forward, with over 45 caps and 25+ goals, was their leading scorer during 2022 World Cup qualification?
**Answer:** Jonathan David
**Why it fails:** False: Canada's leading scorer in/during the 2022 World Cup qualifying campaign was CYLE LARIN (13 goals — the top scorer in all of CONCACAF qualifying), not Jonathan David (9). Larin also became Canada's all-time leading scorer in Jan 2022; David only passed him in Nov 2024.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The 2022 qualifying top scorer (and the all-time leader at that time) was Cyle Larin.

### Row 8391 — Canada (easy) — FAIL
**Q:** Which Canada player became the team's leading scorer before the 2022 World Cup?
**Answer:** Jonathan David
**Why it fails:** False: Canada's leading scorer in/during the 2022 World Cup qualifying campaign was CYLE LARIN (13 goals — the top scorer in all of CONCACAF qualifying), not Jonathan David (9). Larin also became Canada's all-time leading scorer in Jan 2022; David only passed him in Nov 2024.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The 2022 qualifying top scorer (and the all-time leader at that time) was Cyle Larin.

### Row 8392 — Canada (easy) — FAIL
**Q:** Which Canada player became their leading scorer during 2022 World Cup qualifying?
**Answer:** Jonathan David
**Why it fails:** False: Canada's leading scorer in/during the 2022 World Cup qualifying campaign was CYLE LARIN (13 goals — the top scorer in all of CONCACAF qualifying), not Jonathan David (9). Larin also became Canada's all-time leading scorer in Jan 2022; David only passed him in Nov 2024.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The 2022 qualifying top scorer (and the all-time leader at that time) was Cyle Larin.

### Row 8443 — Canada (easy) — FAIL
**Q:** Which Canada player scored against Belgium in the 2022 World Cup?
**Answer:** Alphonso Davies
**Why it fails:** False: Davies scored Canada's first World Cup goal against CROATIA, not Belgium. Canada did not score against Belgium at all (they lost 1-0).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Davies scored v Croatia; Canada didn't score v Belgium.

### Row 8446 — Canada (easy) — FAIL
**Q:** Which Canada player scored faster in the 2022 World Cup: Davies vs Croatia or Larin vs Belgium?
**Answer:** Alphonso Davies
**Why it fails:** False premise: Cyle Larin did NOT score against Belgium in 2022 - Canada lost 1-0 to Belgium and did not score. (Davies' 2nd-minute goal v Croatia is real, but the Larin-v-Belgium comparison is invented.)
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Canada didn't score v Belgium; remove the fabricated Larin goal.

### Row 8483 — Canada (easy) — FAIL
**Q:** Which Canada player was the national team's leading scorer during 2022 World Cup qualifying?
**Answer:** Jonathan David
**Why it fails:** False: Canada's leading scorer in/during the 2022 World Cup qualifying campaign was CYLE LARIN (13 goals, the top scorer in all of CONCACAF qualifying), not Jonathan David (9).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The 2022 qualifying top scorer was Cyle Larin (13).

### Row 8524 — Canada (easy) — FAIL
**Q:** Which Canada star was captain at the 2022 FIFA World Cup?
**Answer:** Alphonso Davies
**Why it fails:** False: Alphonso Davies was NOT Canada's captain at the 2022 World Cup - Atiba Hutchinson captained the side. Davies became captain later (under Marsch).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The 2022 captain was Atiba Hutchinson.

### Row 8525 — Canada (easy) — FAIL
**Q:** Which Canada star was named captain before the 2022 World Cup?
**Answer:** Alphonso Davies
**Why it fails:** False: Alphonso Davies was NOT Canada's captain at the 2022 World Cup - Atiba Hutchinson captained the side. Davies became captain later (under Marsch).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The 2022 captain was Atiba Hutchinson.

### Row 8528 — Canada (easy) — FAIL
**Q:** Which Canada striker became their leading scorer during 2022 World Cup qualifying?
**Answer:** Jonathan David
**Why it fails:** False: Canada's leading scorer in/during the 2022 World Cup qualifying campaign was CYLE LARIN (13 goals, the top scorer in all of CONCACAF qualifying), not Jonathan David (9).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The 2022 qualifying top scorer was Cyle Larin (13).

### Row 8574 — Canada (medium) — FAIL
**Q:** Which Canadian city hosted group stage matches in the 2015 FIFA Women's World Cup?
**Answer:** Edmonton
**Why it fails:** Non-unique: Edmonton, Vancouver AND Montreal all hosted 2015 Women's World Cup matches (the six hosts were Edmonton, Vancouver, Winnipeg, Ottawa, Montreal, Moncton). Three of the four options hosted - Toronto did not.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Make the options include only one 2015 WWC host.

### Row 8576 — Canada (easy) — FAIL
**Q:** Which Canadian city hosted the 2015 Gold Cup final and is also home to Canada Soccer's headquarters?
**Answer:** Ottawa
**Why it fails:** False: the 2015 CONCACAF Gold Cup FINAL was played in Philadelphia (USA), not Ottawa. (Ottawa is Canada Soccer's HQ, but it did not host the 2015 Gold Cup final.)
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The 2015 Gold Cup final was in Philadelphia; Ottawa hosted neither.

### Row 8626 — Canada (easy) — FAIL
**Q:** Which Canadian forward was joint-top scorer for his nation at the 2022 World Cup?
**Answer:** Cyle Larin
**Why it fails:** False: Cyle Larin did NOT score at the 2022 World Cup finals - Canada's only goals were Davies (v Croatia) and a Morocco own goal. So Larin was not a 'joint-top scorer at the 2022 World Cup' (Davies, with one, was the top scorer).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Larin didn't score at the 2022 finals; Davies was Canada's only scorer.

### Row 8627 — Canada (easy) — FAIL
**Q:** Which Canadian forward was joint-top scorer with Jonathan David at the 2022 World Cup?
**Answer:** Cyle Larin
**Why it fails:** False: Cyle Larin did NOT score at the 2022 World Cup finals - Canada's only goals were Davies (v Croatia) and a Morocco own goal. So Larin was not a 'joint-top scorer at the 2022 World Cup' (Davies, with one, was the top scorer).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Larin didn't score at the 2022 finals; Davies was Canada's only scorer.

### Row 8628 — Canada (easy) — FAIL
**Q:** Which Canadian forward was the top scorer during 2022 World Cup qualifying?
**Answer:** Jonathan David
**Why it fails:** False: Canada's leading scorer in/during the 2022 World Cup qualifying campaign was CYLE LARIN (13 goals, the top scorer in all of CONCACAF qualifying), not Jonathan David (9).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The 2022 qualifying top scorer was Cyle Larin (13).

### Row 8675 — Canada (easy) — FAIL
**Q:** Which Canadian midfielder, a 2026 prospect, debuted after the 2022 World Cup?
**Answer:** Ismael Koné
**Why it fails:** False: Ismael Kone did NOT debut after the 2022 World Cup - he played at the 2022 finals, coming off the bench in all three group games (his World Cup debut was 2022).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Kone debuted at the 2022 World Cup, not after it.

### Row 8702 — Canada (easy) — FAIL
**Q:** Which Canadian player became their leading scorer before the 2022 World Cup?
**Answer:** Jonathan David
**Why it fails:** False: Jonathan David did NOT become Canada's leading scorer before the 2022 World Cup - Cyle Larin was the all-time leader (from Jan 2022). David only passed Larin in November 2024.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Larin was the leader before/at 2022; David became leader in Nov 2024.

### Row 8709 — Canada (easy) — FAIL
**Q:** Which Canadian player captained the team in 2022 FIFA World Cup qualifying?
**Answer:** Alphonso Davies
**Why it fails:** False: Alphonso Davies did NOT captain Canada in 2022 World Cup qualifying - Atiba Hutchinson was the captain throughout qualifying and the 2022 finals.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The 2022 qualifying/finals captain was Atiba Hutchinson.

### Row 8738 — Canada (easy) — FAIL
**Q:** Which Canadian player led the team in goals at the 2022 World Cup?
**Answer:** Jonathan David
**Why it fails:** False: Jonathan David did NOT score at the 2022 World Cup finals - Canada's only goals there were Davies (v Croatia) and a Morocco own goal. So David was not the team's leading/top scorer at the 2022 World Cup (Davies, with one, was).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** David scored 0 at the 2022 finals; Davies was Canada's only scorer there.

### Row 8769 — Canada (easy) — FAIL
**Q:** Which Canadian player scored more 2022 World Cup goals than Mexico's Raúl Jiménez?
**Answer:** Jonathan David
**Why it fails:** False: Jonathan David did NOT score at the 2022 World Cup, so he did not 'score more 2022 World Cup goals than Raul Jimenez' - both scored zero at the tournament.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Neither David nor Jimenez scored at 2022; the claim is false.

### Row 8816 — Canada (easy) — FAIL
**Q:** Which Canadian player's 25+ goals made him the team's leading scorer at the 2022 World Cup?
**Answer:** Jonathan David
**Why it fails:** False: Jonathan David did NOT score at the 2022 World Cup finals - Canada's only goals there were Davies (v Croatia) and a Morocco own goal. So David was not the team's leading/top scorer at the 2022 World Cup (Davies, with one, was).
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** David scored 0 at the 2022 finals; Davies was Canada's only scorer there.

### Row 8821 — Canada (easy) — FAIL
**Q:** Which Canadian player's goal secured their 2021 Gold Cup semi-final spot?
**Answer:** Cyle Larin
**Why it fails:** False: Cyle Larin did NOT score in Canada's 2-0 Gold Cup quarter-final win over Costa Rica in 2021 - the goals were scored by Junior Hoilett (18') and Stephen Eustaquio (68').
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The QF scorers were Hoilett and Eustaquio, not Larin.

### Row 8842 — Canada (easy) — FAIL
**Q:** Which Canadian scorer debuted for the national team first?
**Answer:** Cyle Larin
**Why it fails:** False: among the options, Atiba Hutchinson debuted first - in 2003, long before Cyle Larin (2014). The explanation only compares Larin and David and ignores Hutchinson.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Hutchinson (2003) debuted earliest of the options.

### Row 8855 — Canada (easy) — FAIL
**Q:** Which Canadian stadium hosted matches at the 2015 Women's World Cup?
**Answer:** BC Place
**Why it fails:** Non-unique: both BC Place (Vancouver) AND Commonwealth Stadium (Edmonton) hosted 2015 Women's World Cup matches (Edmonton hosted the opener). Two of the four options hosted. (Also: Canada solo-hosted the 2015 WWC, not 'co-hosted'.)
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Make only one option a 2015 WWC venue.

### Row 8876 — Canada (medium) — FAIL
**Q:** Which Canadian striker led their 2022 World Cup qualification campaign in goals?
**Answer:** Jonathan David
**Why it fails:** False: Canada's top scorer in the 2022 World Cup qualifying campaign was CYLE LARIN (13 goals), not Jonathan David (9). David led neither the qualifying nor finals scoring.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The 2022 qualifying top scorer was Cyle Larin (13).

### Row 8950 — Canada (easy) — FAIL
**Q:** Which CONCACAF nation reached the 2021 Gold Cup semi-finals like Canada did?
**Answer:** Qatar
**Why it fails:** Category error: Qatar is NOT a CONCACAF nation - it competed at the 2021 Gold Cup as an invited AFC guest. The CONCACAF semi-finalists alongside Canada were the USA and Mexico.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Answer should be a CONCACAF semi-finalist (USA or Mexico), not Qatar.

### Row 8962 — Canada (easy) — FAIL
**Q:** Which CONCACAF nation, besides Canada, has participated in every Gold Cup since 2006?
**Answer:** United States
**Why it fails:** Non-unique/false: Mexico (an option) has ALSO participated in every Gold Cup since 2006 - it is not just the USA. The explanation's 'only CONCACAF nation other than Canada' is wrong.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Both the USA and Mexico have played every Gold Cup since 2006.

### Row 9032 — Canada (easy) — FAIL
**Q:** Which Morocco player scored the winning goal against Canada in 2022?
**Answer:** Hakim Ziyech
**Why it fails:** False: Hakim Ziyech scored Morocco's FIRST goal (4') against Canada, not the second. En-Nesyri scored the second (23'). The explanation's 'Ziyech scored Morocco's second goal' is incorrect.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Ziyech scored the 1st goal; En-Nesyri the 2nd.

### Row 9112 — Canada (easy) — FAIL
**Q:** Which nation, like Canada in 2026, co-hosted a FIFA World Cup in 2015?
**Answer:** United States
**Why it fails:** False: the USA did NOT co-host the 2015 FIFA Women's World Cup with Canada - Canada hosted the 2015 WWC alone. (The US hosted the 1999 and 2003 Women's World Cups.)
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Canada solo-hosted the 2015 WWC; the US did not co-host it.

### Row 9114 — Canada (easy) — FAIL
**Q:** Which nation, like Canada, has been a regular CONCACAF Gold Cup participant since 2006?
**Answer:** United States
**Why it fails:** Non-unique: Mexico, Costa Rica and Panama (options) are ALSO regular Gold Cup participants since 2006, not just the USA - the explanation itself lists all four.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Several options are regular Gold Cup participants; make it unique.

### Row 9125 — Canada (easy) — FAIL
**Q:** Which nation's women's team won Olympic gold before Canada in 2020?
**Answer:** United States
**Why it fails:** Non-unique: Germany (an option) ALSO won women's Olympic football gold before Canada (Germany won in 2016), as did the USA. Two options fit.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Both the USA and Germany won Olympic gold before Canada's 2020.

### Row 9143 — Canada (easy) — FAIL
**Q:** Which stadium did Canada NOT play in during the 2022 FIFA World Cup?
**Answer:** Khalifa International Stadium
**Why it fails:** False: Canada DID play at Khalifa International Stadium in 2022 (their 4-1 loss to Croatia was there). Their venues were Ahmad bin Ali (Belgium), Khalifa (Croatia) and Al Thumama (Morocco) - the stadium they did NOT play at was Al Bayt.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Canada played at Khalifa; the unused venue was Al Bayt.

### Row 9144 — Canada (easy) — FAIL
**Q:** Which stadium did Canada's Sam Adekugbe play in for his 2022 World Cup match?
**Answer:** Al Bayt Stadium
**Why it fails:** False: Canada did NOT play at Al Bayt Stadium in 2022, and they played three group games (not 'only one'). The Belgium match was at Ahmad bin Ali Stadium, not Al Bayt.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Canada never played at Al Bayt; the Belgium game was at Ahmad bin Ali.

### Row 9183 — Canada (easy) — FAIL
**Q:** Which team won Olympic gold after Canada's women in 2020?
**Answer:** Sweden
**Why it fails:** False: Sweden did NOT win the 2024 Paris Olympic women's football gold - the UNITED STATES won it (beating Brazil 1-0 in the final). Sweden took bronze.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** The USA won the 2024 Olympic women's gold, not Sweden.

### Row 9247 — Canada (medium) — FAIL
**Q:** Which year was Jesse Marsch appointed as Canada manager?
**Answer:** 2023
**Why it fails:** Wrong year: Jesse Marsch was appointed Canada head coach in MAY 2024, not 2023.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Change to 2024.

### Row 9270 — Canada (easy) — FAIL
**Q:** Who scored Morocco's winning goal against Canada in the 2022 World Cup?
**Answer:** Hakim Ziyech
**Why it fails:** False: Hakim Ziyech scored Morocco's FIRST/opening goal (4') against Canada, not the second. Youssef En-Nesyri scored the second (23'). The explanation's 'Ziyech scored Morocco's second goal' is wrong.
**Source:** Wikipedia (Canada men's NT / at the FIFA World Cup / 2022 WCQ CONCACAF / 2024 Copa America); ESPN; Canada Soccer; FIFA
**Remedy:** Ziyech scored the 1st goal; En-Nesyri the 2nd.
