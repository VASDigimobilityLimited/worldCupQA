# QA_FAILED_LIVENESS_b2.md — Batch 2 dangerous (passed mechanical, FAILED liveness)

> Rows that cleared `QA_PASSED_b2.md` mechanically but are **factually wrong** on the live
> TC-06 check. Each entry: reason + source + concrete remedy. See HANDOFF.md §6/§7.

**Total dangerous: 1895** (Algeria 159, rows 2–513; Argentina 167, rows 514–1543; Australia 123, rows 1544–2396; Austria 161, rows 2401–3241; Belgium 170, rows 3242–4191; Bosnia and Herzegovina 125, rows 4192–5804; Canada 69, rows 7821–9330; Colombia 168, rows 10796–11736; Costa Rica 139, rows 11737–12858; Czechia 234, rows 16004–16893; DR Congo 82, rows 16894–17345; Ecuador 143, rows 17346–18086; Egypt 155, rows 18087–18876)

---

## Algeria (batch-2 rows 2–513)

**Fact base (sourced):** Algeria did **NOT** qualify for the 2022 World Cup (lost CAF playoff to Cameroon on away goals, Toko Ekambi 124'). Algeria **DID** qualify for 2026 (CAF Group G winners, clinched Oct 2025, first since 2014). 2010 WC spot came via a **CAF** playoff v Egypt — **not** intercontinental. Sources: ESPN/Al Jazeera (2022 playoff), FIFA/ESPN (2026 qualification).

- **Row 3** — Q asks which CAF star also starred in a **2022 WC group stage**; answer **Riyad Mahrez** is FALSE — Algeria failed to qualify for 2022, so Mahrez did not play. The only listed player who actually featured in the 2022 group stage is **Sadio Mané** (Senegal) → non-unique premise is moot; answer is simply wrong. *Remedy:* change answer to Mané, or reframe to a tournament Algeria/Mahrez actually played.
- **Row 4** — "rebuilt squad" + "2022 World Cup qualifiers featured" — unverifiable squad-rebuild narrative AND implies a successful 2022 cycle (Algeria failed). UNVERIFIED→FAIL. *Remedy:* drop the "rebuilt squad" framing; use a verifiable qualifying fact.
- **Row 5** — "When did Algeria next qualify for a World Cup [after 2019 AFCON]?" answer **2022** is FALSE; Algeria's next qualification was **2026** (not even an option). *Remedy:* add 2026 as the answer.
- **Row 8** — "Which team did Senegal beat in the 2022 World Cup?" answer **Ecuador** is **non-unique**: Senegal also beat **Qatar** 3-1 (Qatar is a listed option). *Remedy:* specify "final group match" or remove Qatar.
- **Row 15** — Explanation states Algeria "lost **1-0** to Nigeria in their final 2018 qualifier"; the final qualifier (10 Nov 2017) was a **1-1 draw** (later awarded 3-0 to Algeria for Nigeria's ineligible player). Explanation factually wrong. *Remedy:* fix scoreline/match, or cite the 2016 Uyo 3-1 loss. [source: Wikipedia 2018 CAF 3rd round / Premium Times]
- **Row 16** — "unlike which other CAF nation that qualified for both 2018 and 2022?" answer **Tunisia** is **non-unique**: **Senegal** and **Morocco** (both options) also qualified for both. *Remedy:* keep only one qualifier among the options.
- **Row 18** — Explanation claims Algeria qualified for 2010 "via an **intercontinental** playoff, not direct CAF" — FALSE; it was a **CAF** playoff v Egypt. *Remedy:* fix explanation; note 2014 was also via a CAF playoff (Burkina Faso), so the premise is muddy.
- **Row 20** — "Which World Cup did Algeria next qualify for [after 2019 AFCON]?" answer **2022** is FALSE; correct option present is **2026**. *Remedy:* change answer to 2026.
- **Row 26** — "2019 AFCON 1-0 margin matched which CAF champion's final win?" answer **Senegal in 2021**: Senegal's 2021 AFCON final (v Egypt) was **0-0 a.e.t., won on penalties** — NOT a 1-0 win. False match + wrong explanation. *Remedy:* pick a genuine 1-0 final.
- **Row 28** — "2019 AFCON win contrasts with which 2014 WC result?" answer **Germany beat Algeria** is **non-unique**: **Belgium** also beat Algeria 2-1 in the 2014 group stage (Belgium is an option). *Remedy:* remove Belgium.
- **Row 32** — "Belmadi was in charge for which FIFA World Cup?" answer **2022** is FALSE — Algeria failed to qualify for 2022, so Belmadi never managed Algeria *at* a World Cup. False premise. *Remedy:* reframe to a qualifying campaign, not WC participation.
- **Row 33** — Explanation claims 2010 qualification "via an **intercontinental** playoff, not directly through CAF" — FALSE (CAF playoff v Egypt). *Remedy:* fix explanation.
- **Row 38** — "Algeria (R16) matched which nation's best-ever finish?" answer **Costa Rica**: Costa Rica's best-ever is the **quarter-finals** (2014), not R16. No listed option actually has R16 as its best result. *Remedy:* replace with a nation whose ceiling is R16.
- **Row 39** — Answer **Nigeria** is correct (only other CAF R16 side in 2014), but explanation says "both lost **2-1** to European opponents" — Nigeria lost **0-2** to France, not 2-1. Explanation factually wrong. *Remedy:* fix Nigeria's scoreline.
- **Row 51** — Answer **"An intercontinental playoff"** for how Algeria qualified for 2010 is FALSE — it was a **CAF** playoff v Egypt. *Remedy:* answer = CAF (African) playoff.
- **Row 58** — "For which World Cup did Algeria qualify via CAF qualification?" answer **2026** is **non-unique**: **2014** (also an option) was likewise via CAF qualification. *Remedy:* remove 2014.
- **Row 66** — "How many 2019 AFCON winners played in the 2022 WC qualifiers?" answer **Less than five** is false/unverifiable — many 2019 winners (Mahrez, Bounedjah, Slimani, Bennacer, Mandi…) featured in 2022 qualifying. UNVERIFIED→FAIL. *Remedy:* drop the squad-rebuild claim.
- **Row 69** — Answer **Egypt** correct, but explanation calls it an "**intercontinental** playoff" — it was a **CAF** playoff. Explanation factually wrong. *Remedy:* fix explanation.
- **Row 71** — False premise: Algeria's 2010 match v England was **0-0**, not a "**2-2** draw"; plus the "USM Alger most players" club-count is unverifiable. *Remedy:* correct the score / drop the club claim.
- **Row 74** — "Which Ligue 1 club had the most players in the 2014 squad?" (USM Alger, 4) — unverifiable squad-composition claim (2014 squad was overwhelmingly Europe-based). UNVERIFIED→FAIL.
- **Row 84** — "In which WC did Saïd Benrahma debut?" answer **2022 World Cup** is FALSE — Algeria did not qualify for 2022; Benrahma has never played at a World Cup. False premise. *Remedy:* reframe to a qualifying campaign.
- **Row 88** — "In which qualifying campaign did Slimani first reach 40+ goals?" (2022 qualifiers) — obscure, unverifiable goal-tally claim. UNVERIFIED→FAIL.
- **Row 90** — "First hosted a qualifier at the 64,000-seat Stade 5 Juillet for which WC?" (2010) — false/unverifiable: the stadium (opened 1972) hosted qualifiers for decades before 2010. *Remedy:* drop the "first" framing.
- **Row 93** — Answer **2009** correct, but explanation calls the Egypt playoff "**intercontinental**" — it was a **CAF** playoff. Explanation factually wrong. *Remedy:* fix explanation.
- **Row 96** — "Year Benrahma made his WC qualifying debut?" (2020) — unverifiable/likely wrong (Benrahma's Algeria debut was Oct 2019; the 2022 CAF cycle began 2021). UNVERIFIED→FAIL.
- **Row 100** — "Under which manager did Algeria qualify for the 2022 WC?" answer **Belmadi** rests on a FALSE premise — Algeria did **not** qualify for 2022. *Remedy:* reframe to the (failed) qualifying campaign, not "qualified."
- **Row 104** — Answer cell is spreadsheet-date-corrupted (**"2026-01-02 00:00:00"** = mangled "2-1"); options (1-0/3-1/2-0) don't even contain the correct 2-1. Broken answer. *Remedy:* restore "2-1" and fix options; flag for dataset sweep.
- **Row 105** — Answer date-corrupted (**"2026-02-01 00:00:00"**); options (0-1/1-3/0-2) lack the correct scoreline. Broken answer. *Remedy:* restore the score.
- **Row 106** — Answer date-corrupted (**"2026-02-01 00:00:00"**) although the correct **2-1** is present as a distractor. Broken answer field. *Remedy:* set answer = 2-1.
- **Row 110** — "When did Algeria **first** exit a World Cup after the group stage?" answer **2010** is false — Algeria's first group-stage exits were **1982 and 1986**. *Remedy:* fix to 1982, or drop "first."
- **Row 111** — Answer **2009** correct, but explanation calls the Egypt playoff "**intercontinental**" — it was a CAF playoff. *Remedy:* fix explanation.
- **Row 112** — Same: explanation "intercontinental playoff against Egypt" is wrong (CAF). *Remedy:* fix explanation.
- **Row 114** — Same: explanation "intercontinental playoff against Egypt" wrong (CAF). *Remedy:* fix explanation.
- **Row 120** — "When did Slimani become all-time leading scorer?" answer **After 2018** is **non-unique/ambiguous**: he broke the record c.2021, so "after 2014/2016/2020" are all also true. *Remedy:* use a single precise year.
- **Row 125** — "Which 2019 AFCON champion matched Algeria in 2014 qualifying group points?" (Burkina Faso, both 12 pts) — unverifiable; also Burkina Faso is not an AFCON champion and was Algeria's playoff (not group) opponent. UNVERIFIED→FAIL.
- **Row 133** — False premise: Algeria did **not** lose the **2010 AFCON final** (they lost the 2010 semi-final to Egypt; Egypt beat Ghana in that final). *Remedy:* drop the false 2010-final claim.
- **Row 134** — Misleading premise: "Which AFCON winner did Algeria defeat at 2014 WC?" → **South Korea** is not an AFCON winner. *Remedy:* reword so Algeria (not the opponent) is the AFCON winner.
- **Row 135** — "Which AFCON-winning manager coached Algeria at the 2022 World Cup?" — FALSE: Algeria did not play the 2022 WC; Belmadi never coached them at a WC. *Remedy:* reframe.
- **Row 137** — Answer **Egypt** correct, but explanation calls it an "**intercontinental** playoff" (it was CAF, as the Q itself says "African nation"). *Remedy:* fix explanation.
- **Row 139** — "Which AFCON win led to 2022 WC qualification?" — FALSE premise: Algeria failed to qualify for 2022. *Remedy:* remove the qualification claim.
- **Row 142** — "Which attacker made his WC debut in 2022?" (Benrahma) — FALSE: Algeria absent from 2022; Benrahma has no WC appearance. *Remedy:* reframe.
- **Row 143** — "Which attacker scored in the 2014 WC group stage?" answer **Mahrez** is FALSE — Mahrez did **not** score at the 2014 WC (Algeria's scorers v Korea were Slimani, Halliche, Djabou; Slimani v Russia; Feghouli v Belgium). Slimani (a listed option) is correct. *Remedy:* change answer to Slimani.
- **Row 145** — "key player during 2022 qualifying?" (Benrahma) — **non-unique**: Mahrez, Slimani, Bounedjah (all options) were also key. *Remedy:* make the trait distinctive.
- **Row 146** — "key player at the 2022 World Cup?" — FALSE premise (Algeria absent). *Remedy:* reframe.
- **Row 147** — "key player in 2022 qualifiers?" (Benrahma) — non-unique (Mahrez/Slimani/Bounedjah). FAIL.
- **Row 148** — "key selection for 2022 qualifiers?" (Benrahma) — non-unique. FAIL.
- **Row 151** — "selected for the 2022 WC squad?" — FALSE premise: there was no 2022 WC squad (Algeria DNQ). *Remedy:* reframe.
- **Row 152** — "attacker with 90+ caps who scored in 2022 qualifying?" answer **Mahrez** is **non-unique**: Slimani (option) also has 90+ caps and scored in that campaign. *Remedy:* add a distinguishing trait.
- **Row 153** — "attacker with 90+ caps who played for **Man City during the 2014 WC**?" answer **Mahrez** is FALSE — in 2014 Mahrez was a Leicester (Championship) player; he joined Man City in **2018**. *Remedy:* fix the club/era claim.
- **Row 169** — "manager who oversaw the failed 2018 qualification?" answer **Christian Gourcuff** is wrong — the decisive 2018 third-round campaign (2016–17) was run by **Rajevac, then Leekens, then Alcaraz**; Gourcuff had resigned in 2016. *Remedy:* correct the manager. [source: Wikipedia / ESPN]
- **Row 172** — "manager who secured 2026 qualification?" answer **Belmadi** is FALSE — Belmadi left in 2024; 2026 was secured under **Vladimir Petković** (clinched Oct 2025). *Remedy:* change to Petković. [source: FIFA/ESPN]
- **Row 188** — "became all-time top scorer **at the 2021 AFCON**?" (Slimani) — false/unverifiable timing; Slimani didn't score at the 2021 AFCON (Algeria scored once, via Bounedjah). *Remedy:* drop the 2021-AFCON timing.
- **Row 194** — "player with 90+ caps and 25+ goals?" answer **Mahrez** is **non-unique**: Slimani (option) also has 90+ caps and 40+ goals. *Remedy:* add a distinguishing trait.
- **Row 197** — "all-time leading scorer **at the 2022 FIFA World Cup**?" — FALSE premise (Algeria absent from 2022). *Remedy:* drop "at the 2022 World Cup."
- **Row 141** — "Which attacker debuted in WC qualifiers **after the 2018 tournament**?" answer **Benrahma** is FALSE — Benrahma debuted **13 Oct 2015** (v Senegal), before 2018. *Remedy:* fix the debut timing. [source: Wikipedia]
- **Row 201** — "nearly scored a winner against Germany" + explanation "Djabou scored Algeria's **second goal**… nearly forcing penalties": Algeria scored only **one** goal (Djabou 120+4', a consolation from 2-0 down); never "nearly forced penalties." *Remedy:* fix the narrative.
- **Row 202** — "Which player **retired** after the 2022 qualification failure?" answer **Mahrez** is FALSE — Mahrez did not retire; he later captained the 2026 qualifying campaign. *Remedy:* name an actual retiree.
- **Row 204** — Explanation "Djabou scored Algeria's **second goal**" is false (Algeria's only goal); Germany scored first. *Remedy:* fix.
- **Row 208** — "extra-time **equalizer** against Germany" / "120th-minute equalizer" — FALSE: Djabou's goal made it 2-1, never equalized. *Remedy:* call it a consolation.
- **Row 211** — Explanation "Algeria's **second goal**" is false (only goal). *Remedy:* fix.
- **Row 212** — "**equalizer** against Germany" / "equalizing goal" — FALSE (made it 2-1). *Remedy:* fix.
- **Row 215** — "Which player scored their goal in the 2014 group stage?" answer **Slimani** is **non-unique**: **Feghouli** (v Belgium) and **Djabou** (v Korea), both options, also scored in the 2014 group stage. *Remedy:* specify the match.
- **Row 219** — "part of their best-ever WC run in 2014?" answer **Slimani** is **non-unique**: Mahrez, Feghouli, Brahimi (all options) were also in the 2014 squad. *Remedy:* add a distinctive trait.
- **Row 220** — "CAF's **top scorer** at the 2014 WC?" (Slimani, 2 goals) — unverified superlative; Gervinho also scored 2 for CIV. UNVERIFIED→FAIL.
- **Row 221** — "Algeria's **top scorer** in 2014 WC qualifying?" (Slimani) — unverified; El Arbi Hillel Soudani (a listed option) was a prolific scorer in that campaign. UNVERIFIED→FAIL.
- **Row 223** — "2019 final winner **aided their 2022 WC qualification**?" — FALSE premise: Algeria failed to qualify for 2022. *Remedy:* remove the qualification claim.
- **Row 229** — Explanation "Feghouli played for **USM Alger** before 2014" is false — Feghouli was developed in France (Grenoble) / at Valencia. Fabricated club history. *Remedy:* fix.
- **Row 230** — Explanation "2010 entry via an **intercontinental** playoff" is false (CAF playoff v Egypt). *Remedy:* fix.
- **Row 234** — "made WC debut in 2014?" answer **Mahrez** is **non-unique**: Slimani, Feghouli, Brahimi (all options) also made their WC debut in 2014. *Remedy:* add a distinctive trait.
- **Row 235** — "scored in the 2022 qualifiers?" (Mahrez) — **non-unique**: Slimani and Bounedjah (options) also scored. *Remedy:* specify.
- **Row 236** — "more WC goals, Mahrez or Slimani?" answer **Slimani** is correct (2 v 0), but explanation says **Mahrez scored one (2014)** — false; Mahrez has **no** WC goals. *Remedy:* fix explanation to 0.
- **Row 237** — "most 2022 qualifying goals?" answer **Mahrez** is FALSE — **Slimani** led with 9 (Mahrez 6). *Remedy:* change answer to Slimani. [source: Goal.com]
- **Row 246** — "Which **World Cup squad** was rebuilt after 2019?" answer **2022 World Cup squad** is FALSE — Algeria had no 2022 WC squad (DNQ). *Remedy:* say "2022 qualifying squad."
- **Row 248** — "all-time scorer netted in 2014 R16?" answer **Slimani** is FALSE — **Djabou** scored in the R16; Slimani's 2014 goals were in the group stage. *Remedy:* change answer to Djabou.
- **Row 250** — "debuted at the 2014 WC before starring in 2022 qualifiers?" (Mahrez) — **non-unique**: Slimani (option) also debuted at 2014 and featured in 2022 qualifying. *Remedy:* add a distinctive trait.
- **Row 251** — "debuted **during 2022 WC qualifying**?" answer **Benrahma** is FALSE — he debuted in 2015. *Remedy:* fix.
- **Row 252** — Explanation "Benrahma's debut in **2020**" / "Benrahma's **World Cup debut**" — both false (debuted 2015; never played a WC). *Remedy:* fix.
- **Row 254** — "Which attacker did **not** play for Man City?" answer **Slimani** is **non-unique**: Benrahma and Bounedjah (options) also never played for Man City. *Remedy:* keep only one non-City player among the options.
- **Row 257** — "made his senior debut **in a 2014 World Cup qualifier**?" answer **Mahrez** is FALSE — Mahrez debuted in a **friendly** (v Armenia, May 2014), after 2014 qualifying had ended (Nov 2013). *Remedy:* fix.
- **Row 258** — "played for **Man City during 2018 WC qualifying**?" answer **Mahrez** is FALSE — during 2016–17 Mahrez was at **Leicester**; he joined Man City in 2018. *Remedy:* fix the club/era.
- **Row 259** — "scored a crucial goal in a 2022 qualifier?" (Mahrez) — **non-unique**: Slimani and Bounedjah (options) also scored. *Remedy:* specify.
- **Row 260** — "scored **against Tunisia in 2022 WC qualifying**?" — FALSE premise: Tunisia was not in Algeria's 2022 qualifying path (group A: Burkina Faso/Niger/Djibouti; playoff v Cameroon). *Remedy:* fix the opponent.
- **Row 261** — "scored over 25 goals for the national team?" answer **Mahrez** is **non-unique**: Slimani (option, 40+) also exceeds 25. *Remedy:* add a distinctive trait.
- **Row 263** — "starred for the 2014 **and 2022 World Cup squads**?" — FALSE: no 2022 WC squad (Algeria DNQ). *Remedy:* fix.
- **Row 267 / 270 / 271 / 272 / 275 / 286** — "Benrahma a key attacker in 2022 qualifying": **non-unique** (Mahrez/Slimani/Bounedjah, all options, were as/more central) and rests on a soft "modern era" narrative. *Remedy:* make the trait distinctive.
- **Row 273** — "first selected for a WC squad in 2014?" answer **Mahrez** is **non-unique**: Slimani (option) was also first selected in 2014. *Remedy:* add a distinctive trait.
- **Row 274** — "in their **2022 FIFA World Cup squad**?" — FALSE: no 2022 WC squad (DNQ). *Remedy:* say "qualifying squad."
- **Row 280** — "attacker with 90+ caps who helped qualify for **2014**?" answer **Mahrez** is FALSE — Mahrez debuted in 2014 (after qualifying ended) and did not feature in 2014 qualifying. *Remedy:* name Slimani.
- **Row 281** — "90+ caps in the **2022 World Cup squad**?" — FALSE premise (no 2022 WC squad). *Remedy:* say "qualifying squad."
- **Row 285** — "90+ caps, **scored at the 2014 WC**?" answer **Mahrez** is FALSE — Mahrez did not score at the 2014 WC. *Remedy:* name a real 2014 scorer.
- **Row 287** — "goals key for **2014 WC qualification**?" answer **Mahrez** is FALSE — Mahrez did not play 2014 qualifying. *Remedy:* name Slimani.
- **Row 289** — "club with the most players in the 2019 AFCON squad?" (USM Alger) — unverifiable; the 2019 squad was overwhelmingly Europe/Gulf-based. UNVERIFIED→FAIL.
- **Row 291** — "Which is a top side in the Algerian Ligue 1?" answer **MC Alger** is **non-unique**: CR Belouizdad and ES Sétif (options) are also top sides. *Remedy:* keep one top side.
- **Row 293** — Explanation "Slimani played for **USM Alger**" is false — Slimani's Algerian club was **CR Belouizdad** (via JSM Chéraga). Fabricated club history. *Remedy:* fix.
- **Row 295** — Explanation "Feghouli (**USM Alger**) debuted in 2014" — false club attribution (Feghouli developed in France). *Remedy:* fix.
- **Row 296** — "Which club's player was absent from the 2014 squad?" (MC Alger) — unverifiable squad-composition claim. UNVERIFIED→FAIL.
- **Row 297** — Explanation "USM Alger players like Slimani and Carl Medjani" — false: Slimani was at CR Belouizdad/Sporting; Medjani played in Europe. *Remedy:* fix.
- **Row 302** — "top scorer in **2018** WC qualifying?" (Slimani) — unverified superlative; not established over the campaign. UNVERIFIED→FAIL.
- **Row 304** — "key attacker featured in 2022 qualifiers?" (Benrahma) — **non-unique** (Mahrez/Slimani/Bounedjah, all options, also featured) + soft narrative. FAIL.
- **Row 305** — "key attacker in the 2021 AFCON squad?" (Benrahma) — **non-unique**: Mahrez/Slimani/Bounedjah (options) were all in that squad. FAIL.
- **Row 306** — "selected for the 2022 FIFA World Cup?" — FALSE premise (Algeria DNQ; no 2022 WC squad). *Remedy:* reframe.
- **Row 307** — "started on the right wing in the 2014 WC?" (Mahrez) — Mahrez was largely a substitute in 2014; Feghouli was the right-sided starter. Also "90+ caps" is anachronistic for 2014. UNVERIFIED/FALSE→FAIL.
- **Row 309** — "played for Man City **at the 2022 World Cup**?" — FALSE premise (Algeria absent). *Remedy:* drop "at the 2022 World Cup."
- **Row 312 / 314** — "Feghouli played for **USM Alger**" — false: Feghouli was developed in France (Grenoble), his senior debut was for Grenoble. Fabricated club history. *Remedy:* fix.
- **Row 313** — "Slimani began his career at **JS Kabylie**" — false: Slimani came through JSM Chéraga / CR Belouizdad. *Remedy:* fix.
- **Row 315** — "USM Alger's **Carl Medjani** in the 2014 squad" — false: Medjani was a Europe-based player, not a USM Alger player. *Remedy:* fix.
- **Row 317** — "MC Alger produced players for the 2014 squad" — unverifiable; the 2014 squad was overwhelmingly Europe-based. UNVERIFIED→FAIL.
- **Row 318** — Explanation is a self-referential non-answer ("The question requires applying knowledge…") and the club-scorer claim is unverifiable. FAIL (GEN + unverified).
- **Row 321** — "manager who led 2026 qualification?" answer **Belmadi** is FALSE — 2026 was secured under **Petković** (Belmadi left 2024). *Remedy:* change to Petković.
- **Row 324** — "Which opponent did **not** face Algeria in the 2019 AFCON knockouts?" answer **Ivory Coast** is FALSE — Algeria beat Côte d'Ivoire 4-3 on pens in the **quarter-final**; in fact all four options faced them. *Remedy:* replace with a team they didn't play. [source: ESPN/France24]
- **Row 328** — "became all-time leading scorer during the **2018** qualifying cycle?" (Slimani) — FALSE: he became top scorer in 2021, during the **2022** cycle. *Remedy:* fix to 2022 cycle. [source: Goal.com]
- **Row 330** — "became top scorer during **2018** qualifying?" (Slimani) — FALSE (became top scorer 2021). *Remedy:* fix.
- **Row 332** — "debuted in the **2014 WC qualifiers**?" answer **Nabil Bentaleb** is wrong — Bentaleb debuted in a 2014 friendly (after qualifying ended), c.2014, not in the qualifiers. *Remedy:* fix.
- **Row 333** — "from the 2019 AFCON win who also started the 2022 qualifiers?" (Mahrez) — **non-unique**: Bennacer, Belaïli, Bounedjah (options) all also did. *Remedy:* add a distinctive trait.
- **Row 334** — "had over 40 goals during the **2018** qualifying cycle?" (Slimani) — FALSE: he reached 40 around 2021, not by the 2018 cycle. *Remedy:* fix timing.
- **Row 338** — "all-time leading scorer **in World Cup matches**?" (Slimani) — contested superlative: Djabou also has 2 WC goals (tied), plus older scorers. UNVERIFIED→FAIL.
- **Row 340** — "Which player scored at the **2010** WC?" answer **Karim Matmour** is FALSE — Algeria scored **zero** goals at the 2010 World Cup. *Remedy:* remove; there was no 2010 Algeria WC goal.
- **Row 341** — "scored in a 2014 WC match (PL winner 2016)?" (Mahrez) + explanation "scored against South Korea" — FALSE: Mahrez did not score at the 2014 WC. *Remedy:* name a real scorer.
- **Row 343** — "scored the **equalizer** against Germany?" (Djabou) — explanation "120th-minute goal to **level** the match" is FALSE (it made it 2-1). *Remedy:* call it a consolation.
- **Row 347** — "scored the **most** goals at the 2014 WC?" (Slimani, 2) — **tied/non-unique**: Djabou (a listed option) also scored 2. *Remedy:* fix.
- **Row 348** — "most goals in **2018** qualifiers?" (Slimani) — unverified; El Arbi Hillel Soudani (an option) was a prolific scorer in that campaign. UNVERIFIED→FAIL.
- **Row 366** — "all-time top scorer **at the 2022 FIFA World Cup**?" — FALSE premise (Algeria absent). *Remedy:* drop the 2022-WC framing.
- **Row 369** — "all-time leading scorer **during the 2014 WC** match v Russia?" (Slimani) — FALSE: in 2014 the record was Tasfaout's; Slimani became top scorer in 2021. *Remedy:* fix.
- **Row 370** — "all-time top scorer during **2018** qualifying?" (Slimani) — FALSE (became top scorer 2021). *Remedy:* fix.
- **Row 376** — "2016 PL win preceded Algeria's **2018 World Cup qualification**?" — FALSE premise: Algeria did not qualify for 2018. *Remedy:* remove the qualification claim.
- **Row 388** — "Which squad issue caused the 2022 qualification failure?" (A major squad rebuild) — unverifiable narrative causation; the failure was a 124'-minute away-goals playoff loss to Cameroon, not a documented "rebuild." UNVERIFIED→FAIL.
- **Row 389** — "captained the **2022 World Cup squad**?" — FALSE premise (no 2022 WC squad). *Remedy:* say "qualifying squad."
- **Row 390** — "debuted at the 2014 WC before winning the 2019 AFCON?" (Mahrez) — **non-unique**: Slimani (option) also debuted at 2014 and won 2019. *Remedy:* add a distinctive trait.
- **Row 392** — "scored **four goals** in 2022 qualifying?" (Mahrez) — Mahrez scored **6** (and was not the top scorer; Slimani had 9). *Remedy:* fix the count. [source: Goal.com]
- **Row 393** — "scored in the 2014 group v South Korea?" (Mahrez, "fourth goal") — FALSE: Mahrez did not score at the 2014 WC. *Remedy:* name Slimani/Halliche/Djabou.
- **Row 394** — "key selection **for the 2022 FIFA World Cup**?" (Mahrez) — FALSE premise (no 2022 WC) + non-unique among Algerian options. *Remedy:* reframe.
- **Row 395** — "star attacker selected for the 2022 qualifiers?" (Mahrez) — **non-unique**: Slimani (option) also selected. *Remedy:* add a distinctive trait.
- **Row 397** — "scored 4 goals in 2022 qualifying, **top scorer**?" (Mahrez) — FALSE: top scorer was **Slimani** (9); Mahrez had 6. *Remedy:* change answer. [source: Goal.com]
- **Row 402** — "2016 PL win preceded his **2018 WC qualifying heroics**?" (Mahrez) — misleading: Algeria finished bottom of its 2018 group; no "heroics." *Remedy:* drop the success framing.
- **Row 403** — "WC debut before his 2019 AFCON triumph?" (Mahrez) — **non-unique**: Slimani (option) also debuted at 2014 and won 2019. *Remedy:* add a distinctive trait.
- **Row 404** — "goals central to 2022 qualification?" (Mahrez) — **non-unique/wrong emphasis**: Slimani (option) was the top scorer (9 v 6). *Remedy:* name Slimani or add a trait.
- **Row 409** — "all-time leading scorer **during the 2019 AFCON**?" (Slimani) — FALSE: Slimani became top scorer in Sept 2021; Tasfaout held the record in 2019. *Remedy:* fix timing. [source: Goal.com]
- **Row 412** — "scored 2019 final winner, was in the **2022 World Cup squad**?" (Bounedjah) — FALSE premise (no 2022 WC squad). *Remedy:* say "qualifying squad."
- **Row 416** — "veteran who played in 2022 qualifying?" (Mahrez) — **non-unique**: Slimani (option) also did. *Remedy:* add a distinctive trait.
- **Row 417** — "winger who played for Man City **at the 2022 World Cup**?" (Mahrez) — FALSE premise (Algeria absent). *Remedy:* drop the 2022-WC framing.
- **Row 446** — "manager **at the 2022 FIFA World Cup**?" (Belmadi) — FALSE premise (Algeria DNQ). *Remedy:* say "2022 qualifying campaign."
- **Row 456** — "did NOT face in the 2014 knockout stage?" (Brazil) — **non-unique**: South Korea and Russia (options) were also not knockout opponents (group only). *Remedy:* keep only never-played teams as the other distractors.
- **Row 463** — "nation that, like Algeria, lost **2-1 to Germany** in a WC knockout?" (Sweden, 2006 R16) — FALSE: Germany beat Sweden **2-0** in the 2006 R16. *Remedy:* name a real 2-1 knockout loss.
- **Row 472** — "star attacker **for the 2022 FIFA World Cup**?" (Mahrez) — FALSE premise (no 2022 WC). *Remedy:* say "qualifying campaign."
- **Row 473** — "in the 2019 AFCON winning squad?" (Mahrez) — **non-unique**: Slimani and Brahimi (options) were also in the 2019 squad. *Remedy:* add a distinctive trait.
- **Row 474** — "rival Mahrez's Algeria **defeated** in the 2022 qualifiers?" (Cameroon) — FALSE: Algeria were **eliminated by** Cameroon (lost on away goals, 2-2 agg) and did NOT qualify. *Remedy:* reverse — Algeria lost to Cameroon.
- **Row 488** — "Which WC did Algeria qualify for **via CAF qualification**?" (2026) — **non-unique**: 2010 and 2014 (both options) were also via CAF. *Remedy:* keep only one CAF qualification among options.
- **Row 489** — "campaign failed to reach?" (2022) — **non-unique**: Algeria also failed to reach **2018** (an option). *Remedy:* remove 2018.
- **Row 491** — "year Algeria qualified for the 2014 WC?" (2014) — FALSE: they clinched it in **2013** (Nov playoff v Burkina Faso). *Remedy:* change to 2013 (cf. Row 113).
- **Row 505** — "Why did Algeria qualify for 2014?" answer **"Topped CAF qualification group"** is incomplete/misleading — the WC berth came via the **CAF playoff v Burkina Faso** (away goals), which is also a listed option. *Remedy:* answer = won the CAF playoff.
- **Row 508** — "Why did the 2014 squad include MC Alger / JS Kabylie / USM Alger players?" — FALSE premise: Algeria's 2014 squad was **entirely Europe-based**; it had no players from those clubs. *Remedy:* remove the false premise.
- **Row 509** — "Why did the 2022 qualification fail?" (Post-AFCON squad rebuild) — unverifiable narrative; the failure was a 124'-minute away-goals playoff loss to Cameroon. UNVERIFIED→FAIL.
- **Row 512** — "Why eliminated in the 2021 group?" (Lost to Equatorial Guinea) — **non-unique**: "Lost to Ivory Coast" and "Drew with Sierra Leone" (both options) are also true contributing results. *Remedy:* make the other options false.

---

## Argentina (batch-2 rows 514–1543)

**Fact base (sourced):** Argentina **won** the 2022 WC (3-3 v France, 4-2 pens; **Messi** was final MOTM). **2024 Copa group = A** (Canada/Chile/Peru) — they beat **Chile** 1-0 and did **not** play Brazil in the group. Finalissima was June 2022 (**before** the WC). Unbeaten through 2022 CONMEBOL qualifying. Sources: ESPN/Wikipedia (2024 Copa), Wikipedia (2022 final MOTM).

- **Row 521** — "next 1-0 win after 2021 = 2024 Copa" rests on explanation "beat **Brazil** 1-0 in the 2024 group stage" — FALSE: Argentina didn't play Brazil in the 2024 group (they beat Chile 1-0). *Remedy:* fix the cited match.
- **Row 529** — "after which final did Argentina win the 2022 **Finalissima**?" answer **2022 World Cup** is FALSE — the Finalissima (June 2022) came **after the 2021 Copa** and **before** the WC. *Remedy:* answer = 2021 Copa América.
- **Row 532** — Parade-date answer is spreadsheet-corrupted (**"2022-12-01 00:00:00"**); the parade was ~Dec 20, 2022, and no clean "December 2022" option exists. *Remedy:* restore the correct date.
- **Row 536** — "beat which nation 1-0 in the 2024 Copa group?" answer **Brazil** is FALSE — Argentina beat **Chile** 1-0; Brazil was in a different group. *Remedy:* change to Chile.
- **Row 538** — "only 2022 qualifying defeat = Brazil (2-0, Nov 2019)" — FALSE: Argentina were **unbeaten** in 2022 CONMEBOL qualifying, and Nov 2019 predates that qualifying. *Remedy:* remove (no qualifying defeat).
- **Row 539** — "Messi did NOT score vs **Australia** in the 2022 knockouts" — FALSE: Messi **scored** v Australia in the R16 (35'). *Remedy:* pick a team he didn't score against.
- **Row 541** — 2022 final pen-score answer is date-corrupted (**"2026-02-04 00:00:00"** = mangled 4-2); 4-2 isn't even a clean option. *Remedy:* restore 4-2.
- **Row 549** — "which nation also co-founded CONMEBOL?" answer **Brazil** is **non-unique**: Uruguay and Chile (both options) were also 1916 founders. *Remedy:* keep one founder.
- **Row 550** — 2015 Copa final pen-score answer date-corrupted (**"2026-01-04"** = mangled 4-1); 4-1 isn't a clean option. *Remedy:* restore 4-1.
- **Row 551** — 2016 Copa final pen-score answer date-corrupted (**"2026-02-04"** = mangled 4-2); 4-2 isn't a clean option. *Remedy:* restore 4-2.
- **Row 553** — "which other champion qualified for 2018 via CONMEBOL = Brazil" + explanation "Brazil **won the 2014 World Cup**" — FALSE (Germany won 2014); also non-unique (Uruguay, a champion, also qualified via CONMEBOL). *Remedy:* fix.
- **Row 555** — "scored over 50 goals in which two combined qualifiers (2018 & 2022)" — unverifiable combined-goal stat. UNVERIFIED→FAIL.
- **Row 560** — "1-0 win over **Brazil** in the 2024 group matched the 2021 final" — FALSE premise (no Argentina–Brazil 2024 group match). *Remedy:* fix.
- **Row 566** — "Argentina averaged 28; which group squad was oldest (Mexico)" — unverifiable squad-age stat. UNVERIFIED→FAIL.
- **Row 574** — "2014 player who won 2008 Olympic gold = Messi" — **non-unique**: Di María and Agüero (both options) also won 2008 gold and were in the 2014 squad. *Remedy:* add a distinctive trait.
- **Row 579** — "why did **Di María** win Man of the Match in the 2022 final?" — FALSE: **Messi** was the final's MOTM (Di María scored but didn't win it). *Remedy:* fix.
- **Row 583** — "how many 2022 squad in Europe's top-5 leagues (over 20)" — explanation is self-admittedly a guess; unverifiable. UNVERIFIED→FAIL.
- **Row 596** — "squad from **13 different club leagues** at which WC (2022)" — obscure, unverifiable count is the crux. UNVERIFIED→FAIL.
- **Row 603** — "finished top of group at which two WCs?" (2022 & 2014) — **non-unique**: Argentina also topped their group in **2010** (so "2010 and 2022", a listed option, is equally valid). *Remedy:* fix options.
- **Row 605** — "won the FIFA Fair Play Award at which WC?" (2014) — FALSE: the **2014** Fair Play award went to **Colombia**. *Remedy:* fix. [source: FIFA/ColombiaReports]
- **Row 614** — "which major league had the fewest Argentine players during 2022 qualifying (Bundesliga)" — unverifiable (and contradicts Row 670, which says Ligue 1). UNVERIFIED→FAIL.
- **Row 646** — "Higuaín international goals = **32**" — FALSE: he scored **31** in 75 caps (31 is a listed distractor). *Remedy:* change to 31. [source: Wikipedia/FBref]
- **Row 655** — "Messi WC goals in 2014+2018+2022 = **13**" — FALSE: 4+1+7 = **12**. *Remedy:* change to 12.
- **Row 656 / 657 / 677** — "scored over 50 combined goals in the 2018 & 2022 qualifiers" — unverifiable combined-goal stat (cf. Row 555). UNVERIFIED→FAIL.
- **Row 660** — "Argentina 11 wins; which nation won 12? (Brazil)" — FALSE: Brazil won **14** in 2022 qualifying. *Remedy:* fix the count.
- **Row 661** — "11W, 5D, 1L = 39 points" — FALSE record: Argentina were **11W 6D 0L** (unbeaten). *Remedy:* fix the W-D-L. [source: Wikipedia]
- **Row 662** — "11W, 5D, how many losses? (1)" — FALSE: **0 losses** (6 draws). *Remedy:* change to 0.
- **Row 667** — "which domestic club had the most 2022 WC winners (River Plate)" — unverifiable; the 2022 squad was overwhelmingly Europe-based. UNVERIFIED→FAIL.
- **Row 669** — "which top league did Argentina NOT have 100+ players in (Primeira Liga)" — incoherent/false premise (the ~100+ figure is the *combined* top-5 total, not per-league). UNVERIFIED→FAIL.
- **Row 670** — "which top league had the fewest Argentine professionals (Ligue 1)" — unverifiable (and contradicts Row 614). UNVERIFIED→FAIL.
- **Row 679** — "which team scored four goals **in just 23 minutes** in 2010? (Germany)" — FALSE: Germany's 4-0 goals came at 3', 68', 74', 89' — spread across the match, not a 23-minute span. *Remedy:* drop the false detail.
- **Row 685** — "in the 2024 Copa group stage Argentina beat which rival 1-0? (Brazil)" — FALSE: they beat **Chile** 1-0; Brazil was in another group. *Remedy:* change to Chile.
- **Row 690** — "in which 2018 group match did Europe-based players feature? (v Iceland)" — vacuous/**non-unique**: all three group matches featured Europe-based players. *Remedy:* make the question discriminating.
- **Row 627 / 650 / 724** — "won **every/all home** qualifier(s) for 2022" — FALSE: Argentina drew **1-1 with Paraguay at La Bombonera** (Buenos Aires, Nov 2020). *Remedy:* drop the "all home wins" claim. [source: ESPN/FOX]
- **Row 703** — "lost 2-0 to Brazil in 2022 qualifying (Nov 2019)" — FALSE premise (Argentina unbeaten; Nov 2019 predates qualifying) + date-corrupted cell ("2019-11-01 00:00:00"). *Remedy:* remove.
- **Row 705** — "scored over 50 goals combined (2018 & 2022 qualifiers)" — unverifiable combined stat. UNVERIFIED→FAIL.
- **Row 721 / 782** — "Di María named Man of the Match in the 2022 final" — FALSE: **Messi** was the final's MOTM. *Remedy:* fix. [source: Wikipedia]
- **Row 731** — "Messi surpassed Mascherano's caps record in which year (2022)" — FALSE: it was **28 June 2021** (148th cap, 2021 Copa). *Remedy:* change to 2021. [source: CNN/Wikipedia]
- **Row 741** — "Higuaín retired from international football in 2018" — FALSE: he announced retirement in **March 2019** (2019 is a listed option). *Remedy:* change to 2019.
- **Row 746 / 758** — "since/which World Cup has Argentina qualified for every tournament (2010)" — FALSE: Argentina have qualified for every WC since **1974**; 2006 (a listed option) is also within that streak. *Remedy:* fix.
- **Row 759 / 760** — "dropped to **10th** in early 2018 under Sampaoli" — unverifiable and inconsistent with their well-established 5th ranking at the 2018 WC. UNVERIFIED→FAIL.
- **Row 766** — 2022 final pen-score answer is date-corrupted ("2026-02-04" = mangled 4-2). *Remedy:* restore 4-2.
- **Row 772** — 2019 Copa 3rd-place answer date-corrupted ("2026-01-02" = mangled 2-1). *Remedy:* restore 2-1.
- **Row 774** — 2022 final ET-score answer date-corrupted ("2026-03-03" = mangled 3-3). *Remedy:* restore 3-3.
- **Row 779** — Saudi-Arabia-score answer date-corrupted ("2026-01-02" = mangled 2-1). *Remedy:* restore 2-1.
- **Row 783** — Scaloni-appointment answer is a corrupted datetime cell ("2018-11-01 00:00:00") where a text option belongs. *Remedy:* restore "November 2018."
- **Row 784** — "beat Brazil 1-0 in a Copa group stage (2024)" — FALSE: in the 2024 group Argentina beat **Chile** 1-0; Brazil was in another group. *Remedy:* change to Chile.
- **Row 795** — "last qualified by topping their group (2022 & 2014)" — **non-unique**: Argentina also topped their 2010 group ("2022 and 2010", a listed option, is equally valid). *Remedy:* fix options.
- **Row 796 / 799** — "lost (its only) 2022 qualifier to Brazil, Nov 2019" — FALSE premise (unbeaten) + date-corrupted cell. *Remedy:* remove.
- **Row 801 / 811** — "lost their only 2022 qualifier (Brazil, Nov 2019)" — FALSE premise (Argentina unbeaten in 2022 qualifying) + date-corrupted cell. *Remedy:* remove.
- **Row 808** — "scored over 50 goals across the 2018 & 2022 qualifying cycles" — unverifiable combined stat. UNVERIFIED→FAIL.
- **Row 812** — "won the Copa América without losing a match (2021)" — **non-unique**: Argentina were also unbeaten winning the **2024** Copa (a listed option). *Remedy:* add a distinguishing detail.
- **Row 817** — "won the FIFA Fair Play Award (2014)" — FALSE: **Colombia** won the 2014 Fair Play award. *Remedy:* fix.
- **Row 827** — "Messi scored **13** WC goals across 2014/2018/2022" — FALSE: 4+1+7 = **12**. *Remedy:* change to 12.
- **Row 831** — "Romero–Otamendi first partnered at a major tournament (2022 WC)" — FALSE: they already partnered at the **2021 Copa** (a listed option). *Remedy:* change to 2021 Copa.
- **Row 834** — "Argentina's U-20 won the 2023 U-20 World Cup" — FALSE: **Uruguay** won 2023; hosts Argentina lost in the R16. *Remedy:* fix. [source: Wikipedia]
- **Row 835 / 884** — "squad from 13 different club leagues (2022)" / "Lusail hosted the 13-leagues squad" — obscure, unverifiable count. UNVERIFIED→FAIL.
- **Row 882** — "won every home match (Argentina)" — FALSE: they drew 1-1 with Paraguay at La Bombonera. *Remedy:* drop the claim.
- **Row 886** — "57,000-capacity stadium hosted the 2022 qualifier **vs Paraguay** (Kempes)" — FALSE: the home Paraguay qualifier was at **La Bombonera** (1-1). *Remedy:* fix the match/venue.
- **Row 891** — "2022 coach who played for Argentina in 2006 (Walter Samuel)" — **non-unique**: Roberto Ayala and Lionel Scaloni (both options) also played at the 2006 WC. *Remedy:* add a distinguishing detail.
- **Row 892** — "2022 coach who was an ex-defender (Walter Samuel)" — **non-unique**: Roberto Ayala (an option) was also an ex-defender. *Remedy:* add a distinguishing detail.
- **Row 906 / 907 / 935 / 979 / 980 / 985 / 988** — "Argentina dropped to **10th** in early 2018 under Sampaoli" — FALSE: Argentina were **5th** in the April 2018 ranking (never 10th). *Remedy:* fix the ranking. [source: FIFA April 2018 ranking]
- **Row 919** — "won the Copa América without a single loss (2021)" — **non-unique**: Argentina were also unbeaten winning the **2024** Copa (a listed option). *Remedy:* distinguish.
- **Row 939** — "which forward debuted internationally **at the 2010 WC** (Higuaín)" — FALSE: Higuaín's senior debut was in **2009** (v Peru). *Remedy:* fix.
- **Row 942** — "Higuaín 32-in-75 goal ratio" — FALSE: **31** goals in 75 caps. *Remedy:* change to 31.
- **Row 946** — "forward with 100 caps and **42** goals (Agüero)" — FALSE: Agüero scored **41** in 101 caps. *Remedy:* change to 41. [source: Wikipedia]
- **Row 947 / 949** — "Higuaín retired from international football **in 2018**" — FALSE: he retired in **March 2019**. *Remedy:* change to 2019.
- **Row 958** — "kept **4 clean sheets** at the 2022 WC (Emi Martínez)" — FALSE: Argentina kept **3** (Mexico, Poland, Croatia). *Remedy:* change to 3.
- **Row 962** — "saved **three penalties in the 2022 final shootout** (Emi)" — FALSE: he saved **one** in the final shootout (Coman); Tchouaméni missed. (He saved 3 across the whole tournament — cf. Row 961.) *Remedy:* fix.
- **Row 971** — "home venue with a perfect win record in 2022 qualifying (Buenos Aires)" — FALSE: they drew 1-1 with Paraguay at La Bombonera (BA). *Remedy:* drop.
- **Row 973** — "left-back who played the 2022 group stage (Marcos Acuña)" — **non-unique**: Nicolás Tagliafico (a listed option) also played LB at 2022. *Remedy:* distinguish.
- **Row 852 / 1059** — "Messi was Argentina's top scorer in 2022 qualifying" — unverified/contradicted: **Lautaro Martínez** (7) is the commonly cited Argentina top scorer; Messi was not among the CONMEBOL leaders (Moreno 10, Neymar 8, Suárez 8). UNVERIFIED→FAIL. [source: FIFA/World Soccer Talk]
- **Row 1030** — "midfielder NOT in the 2022 World Cup-winning squad (Almada)" — FALSE: **Almada was in the squad** (replaced Correa, won a medal). All four options were in the squad. *Remedy:* fix.
- **Row 1035** — "who assisted Messi's goal v Croatia (Álvarez)" — FALSE/confused: Messi's SF goal was a **penalty** (unassisted); it was **Messi who assisted Álvarez** off the Gvardiol dribble. *Remedy:* fix.
- **Row 1037** — "captain of the 2023 U-20 World Cup-winning team (Perrone)" — FALSE: Argentina did **not** win the 2023 U-20 WC (Uruguay did). *Remedy:* remove.
- **Row 1042** — "debuted at 2022 after **years in Europe's top leagues** (Enzo)" — FALSE: Enzo had just moved to Benfica (Portugal, not a top-5 league) months earlier. *Remedy:* the trait fits the distractors, not Enzo.
- **Row 1043** — "Messi dribbled past Gvardiol **to score** Argentina's second goal" — FALSE: that dribble was an **assist** for Álvarez's third goal; Messi's SF goal was a penalty. *Remedy:* fix.
- **Row 1052** — "more WC assists in the 2010s: Messi or Di María" — explanation is a self-referential non-answer ("This question analyzes…") and the comparison is unverified. UNVERIFIED→FAIL.
- **Row 1056** — "expected to debut at the 2026 World Cup (Almada)" — FALSE: Almada **already debuted** at the 2022 WC (v Poland, 83'). *Remedy:* fix.
- **Row 1069** — "Messi outscored Brazil's top scorer in 2022 qualifying" — FALSE: **Neymar scored 8** (Argentina's Lautaro had 7; Messi fewer/equal). *Remedy:* remove. [source: FIFA]
- **Row 1085** — "scored in the 4-3 loss to France 2018 (Cristián Pavón)" — FALSE: Argentina's scorers were **Di María, Mercado, Agüero**; Pavón did not score. *Remedy:* fix.
- **Row 1097** — "scored **twice** in the 2022 Finalissima (Lautaro)" — FALSE: Lautaro scored **once**; the 3-0 scorers were Lautaro, Di María, Dybala. *Remedy:* change to one goal.
- **Row 1105** — "surpassed Mascherano's cap record **in 2022** (Messi)" — FALSE year: Messi did so on **28 June 2021**. *Remedy:* change to 2021.
- **Row 1109** — "in both the 2008 gold squad and the 2022 WC team (Messi)" — **non-unique**: **Di María** (an option) also won 2008 gold and was in the 2022 squad. *Remedy:* distinguish.
- **Row 1112** — "which player was in the 2022 squad? (Dybala)" — **non-unique**: Romero, Otamendi and Paredes (all options) were also in the squad. *Remedy:* add a distinguishing trait.
- **Row 1115** — "part of the 28-avg 2022 squad (Lisandro Martínez)" — **non-unique**: Almada and Enzo (options) were also in the squad (only Barco wasn't). *Remedy:* fix options.
- **Row 1125 / 1128 / 1178 / 1179** — "which player won 2008 Olympic gold (Messi)" — **non-unique**: Agüero and Di María (both options) also won 2008 gold (only Higuaín didn't). *Remedy:* keep one gold medallist. [source: Wikipedia]
- **Row 1136** — "Emi Martínez's 2022 celebration **referenced the barras bravas**" — unverifiable interpretive claim. UNVERIFIED→FAIL.
- **Row 1149** — "most-played international fixture in South America (Argentina vs Brazil)" — FALSE: it is **Argentina vs Uruguay** (197 matches; a listed option). *Remedy:* change to Uruguay. [source: Guinness/Wikipedia]
- **Row 1154** — "FIFA Fair Play Award (2014 squad)" — FALSE: **Colombia** won the 2014 Fair Play award. *Remedy:* fix.
- **Row 1188 / 1190** — "scored **42** goals in 101 caps (Agüero)" — FALSE: **41** goals. *Remedy:* change to 41.
- **Row 1197** — "scored over 50 combined qualifying goals (2018 & 2022)" — unverifiable combined stat. UNVERIFIED→FAIL.
- **Row 1200** — "2021 Copa final before the **2024 group-stage win over Brazil**" — FALSE premise: Argentina did not beat Brazil in the 2024 group (they beat Chile). *Remedy:* fix.
- **Row 1201** — "FIFA Fair Play Award (2014)" — FALSE: **Colombia** won it. *Remedy:* fix.
- **Row 1206** — "youth product who debuted at the 2010 WC (Di María)" — **non-unique**: Agüero and Higuaín (both options) also made their WC debut in 2010. *Remedy:* distinguish.
- **Row 1209** — "Higuaín scored in the 2014 **semi-final**" — FALSE: the 2014 SF v Netherlands was **0-0** (won on pens); Higuaín scored in the QF v Belgium. *Remedy:* fix.
- **Row 1211** — "scored the most 2014 WC goals (Higuaín, 4)" — FALSE: **Messi** scored 4 at 2014; Higuaín scored 1. *Remedy:* change to Messi.
- **Row 1213** — "scored **13** WC goals across 2010/14/18 (Higuaín)" — FALSE: Higuaín scored ~2-3 WC goals. *Remedy:* fix.
- **Row 1215** — "league with the most Argentines in the 2026 squad (La Liga)" — unverifiable league-composition claim. UNVERIFIED→FAIL.
- **Row 1249 / 1250** — "which left-back played at the 2022 WC (Acuña)" — **non-unique**: Tagliafico (an option) also played LB at 2022. *Remedy:* distinguish.
- **Row 1263** — "became their all-time top scorer **at the 2022 WC** (Messi)" — FALSE: Messi passed Batistuta's record in **2016**. *Remedy:* fix the timing.
- **Row 1277** — "surpassed Mascherano's cap record **in 2022** (Messi)" — FALSE: it was **June 2021**. *Remedy:* change to 2021.
- **Row 1278** — "which player was in the 2022 squad? (Dybala)" — **non-unique**: Di María, De Paul and Otamendi (all options) were also in the squad. *Remedy:* fix options.
- **Row 1279 / 1288** — "Di María named Man of the Match in the 2022 final" — FALSE: **Messi** was MOTM. *Remedy:* fix.
- **Row 1284** — "won 2008 Olympic gold (Messi)" — **non-unique**: Agüero and Di María (both options) also won 2008 gold. *Remedy:* keep one.
- **Row 1290** — "playmaker who started the 2014 group v Nigeria (Ever Banega)" — unverified/misleading: Banega was a squad backup, not the "key playmaker" (Di María was). UNVERIFIED→FAIL.
- **Row 1295** — "stadium that hosted **all** their 2022 home qualifier wins (Monumental)" — FALSE: Argentina won home qualifiers at multiple venues (Kempes, Madre de Ciudades). *Remedy:* fix.
- **Row 1311** — "won the **2022 Ballon d'Or** after the World Cup (Messi)" — FALSE: **Benzema** won the 2022 Ballon d'Or; Messi won it in **2023**. *Remedy:* change to 2023.
- **Row 1316** — "scored in **both** the 2014 and 2022 finals (Di María)" — FALSE: Di María was **injured and did not play** the 2014 final. *Remedy:* fix.
- **Row 1334** — "rival faced as top-ranked team in 2023 (Uruguay)" — **non-unique**: Argentina also played **Brazil** (an option) in Nov 2023. *Remedy:* distinguish.
- **Row 1336 / 1369 / 1442 / 1448 / 1449** — "team that beat Argentina in 2022 qualifying (Brazil, Nov 2019)" — FALSE: Argentina were **unbeaten** in 2022 qualifying (and Nov 2019 predates it). *Remedy:* remove.
- **Row 1344** — "continental champion with more than Argentina's 13 leagues (2020 Euro/Italy)" — FALSE/unverifiable: Italy's Euro 2020 squad was overwhelmingly Serie A-based (fewer leagues). UNVERIFIED→FAIL.
- **Row 1350** — "FIFA ranking in early 2018 under Sampaoli (10th)" — FALSE: Argentina were **5th**. *Remedy:* fix.
- **Row 1352 / 1390 / 1416 / 1419 / 1420 / 1421** — "Argentina's most-played South American fixture is vs **Brazil**" — FALSE: it is vs **Uruguay** (197 matches; a listed option in most). *Remedy:* change to Uruguay. [source: Guinness/Wikipedia]
- **Row 1354** — Formation answer is a corrupted datetime cell ("2003-03-04 00:00:00" = mangled 4-3-3). *Remedy:* restore "4-3-3."
- **Row 1371** — "beat Brazil 1-0 in 2024, after losing the 2014 final to them" — FALSE: the 2014 final was v **Germany**, and the 2024 group win was v **Chile** (not Brazil). *Remedy:* fix.
- **Row 1412** — "Argentina's top scorer in 2022 qualifying (Messi)" — unverified/contradicted: **Lautaro Martínez** (7) is the cited top scorer. UNVERIFIED→FAIL.
- **Row 1434** — "stadium for the 3-1 win over Ecuador in 2018 qualifying (Estadio Monumental)" — FALSE: that match was **away in Quito** (Estadio Olímpico Atahualpa). *Remedy:* fix.
- **Row 894 / 1481 / 1484 / 1485 / 1486 / 1487** — "Scaloni's two 2022 assistants = **Matelán and Ayala**" — the answer names **Aníbal Matelán**, who is not a documented Scaloni assistant (the real staff were Aimar, Ayala, Samuel, Manna). Fabricated name. *Remedy:* use real assistants. [source: Wikipedia/Transfermarkt]
- **Row 1452 / 1468** — "team that beat Argentina in 2022 qualifying (Brazil, Nov 2019)" — FALSE: Argentina were **unbeaten**. *Remedy:* remove.
- **Row 1464** — "did NOT face in 2010/2014 knockouts (Italy)" — **non-unique**: France (an option) was also not a 2010/2014 knockout opponent. *Remedy:* fix options.
- **Row 1469** — "Argentina's most-played rivalry hosted a WC final (Brazil)" — FALSE premise: the most-played rivalry is vs **Uruguay**, not Brazil. *Remedy:* fix.
- **Row 1490 / 1542** — "squad from 13 different club leagues (2022)" — obscure, unverifiable count. UNVERIFIED→FAIL.
- **Row 1495** — "qualifying campaign Messi top-scored (2022)" — unverified/contradicted: **Lautaro Martínez** is the cited 2022 top scorer. UNVERIFIED→FAIL.
- **Row 1521** — "why face Brazil in the 2021 Copa final (most-played SA fixture)" — FALSE premise: the most-played fixture is vs **Uruguay**. *Remedy:* fix.
- **Row 1529** — "why score over 50 combined qualifying goals (2018 & 2022)" — built on an unverifiable combined-goal stat. UNVERIFIED→FAIL.
- **Row 1539** — "why is Argentina vs **Brazil** South America's most-played fixture" — FALSE premise: it is vs **Uruguay**. *Remedy:* fix.

---

## Colombia (rows 10796–11736) — batch 2

**Chunk 10797–10843 (10 dangerous):**
- **Row 10801** — "unbeaten run under Lorenzo began [date]" — answer is a **corrupted datetime** ("2022-06-01 00:00:00"); the 28-match run actually began Feb 2022 (under Rueda), Lorenzo's first game was Sep 2022. *Remedy:* restore a clean answer + fix premise.
- **Row 10802** — "Lorenzo appointed **after the 2022 World Cup**" — FALSE: appointed **June 2022**, before the Nov 2022 WC (after Colombia failed to qualify). Answer "2022 World Cup" + explanation both wrong. *Remedy:* fix to 2018 cycle / "after failing to qualify for 2022."
- **Row 10810/10812/10813** — "Colombia lost **3-0 to Argentina** at the 2014 WC" — FALSE premise: Colombia never played Argentina at 2014 (group C: Greece/Ivory Coast/Japan; then Uruguay, Brazil). *Remedy:* remove. [source: Wikipedia 2014 WC Group C]
- **Row 10819** — "beat **Japan 1-0** in 2014 group stage" — FALSE: beat Japan **4-1** (no 1-0 group win). *Remedy:* fix to 4-1. [source: Wikipedia]
- **Row 10821** — "Yerry Mina scored in **every knockout match** (2018)" — explanation FALSE (claims "three goals in the knockout stage + shootout"); Colombia played only **one** knockout game (R16 v England), where Mina scored once. *Remedy:* rewrite.
- **Row 10824** — "**At the 2022 World Cup**, which Colombian star…" — FALSE premise: Colombia **failed to qualify** for 2022. *Remedy:* reframe without the 2022 WC premise.
- **Row 10827** — "venue of the 2014 **3-0 loss to Argentina** (Maracanã)" — FALSE premise (no such match). *Remedy:* remove.
- **Row 10834** — "Colombia **lost** the 2016 Copa Centenario third-place play-off" — FALSE: Colombia **won 1-0** v USA (Bacca, 31') at University of Phoenix Stadium. *Remedy:* change "lost" to "won." [source: rsssf / Bleacher Report]

**Chunk 10844–10893 (7 dangerous):**
- **Row 10847** — embeds "beat **Japan 1-0** in 2014" — FALSE (was 4-1); the answer (next loss = 2018) is right but the premise is wrong. *Remedy:* fix the 1-0 to 4-1.
- **Row 10848** — "which **other** team did Colombia defeat in [2014] group?" (Ivory Coast) — **non-unique**: Colombia also beat **Greece** (a listed option); plus false 1-0 Japan premise. *Remedy:* fix.
- **Row 10849** — "their 2014 **knockout match**" (Beat Uruguay 2-0) — **non-unique**: Colombia had two 2014 knockout games; "Lost to Brazil 2-1" (an option) is also valid. *Remedy:* specify the round.
- **Row 10853** — "lost **3-0 to Argentina at the 2014 WC**" — FALSE premise (no such match). *Remedy:* remove.
- **Row 10855** — "Colombia **lost** the 2021 Copa third-place match, eliminated by Peru" — FALSE: Colombia **won 3-2** v Peru (Luis Díaz double) for 3rd; they were eliminated in the SF by Argentina. *Remedy:* fix. [source: ESPN]
- **Row 10861** — "which year did they **also** fail to qualify?" (2010) — **non-unique**: Colombia also failed to qualify for **2006** (a listed option). *Remedy:* fix options.
- **Row 10877** — "which qualifier venue holds more than 46,788?" (Estadio Monumental, Lima) — **non-unique**: Uruguay's **Estadio Centenario** (~60k) and Chile's Estadio Nacional (~48k), both options, also exceed it. *Remedy:* fix options.

**Chunk 10870 + 10894–10953 (17 dangerous):**
- **Row 10870** — "2018 qualifier **altitude advantage at Bogotá's El Campín**" — FALSE premise: Colombia's home qualifiers (since 1990) are in **Barranquilla** (Estadio Metropolitano, sea level), not Bogotá altitude. *Remedy:* change venue to Barranquilla / drop the altitude claim. [source: FCF venue history]
- **Row 10903** — "**eight** Copa América matches unbeaten before the 2024 final" — wrong/contradicted: in 2024 they went 5 unbeaten to the final; the documented streak is the **28-match** overall run. *Remedy:* fix the number.
- **Row 10911 / 10912 / 10916 / 10919 / 10921 / 10952** — all assert Colombia's "**altitude advantage at Bogotá El Campín (2,640m)**" — FALSE premise (home venue is Barranquilla, sea level). 10921 also fabricates a "3-1 v Ecuador at El Campín." *Remedy:* correct venue/remove altitude claim.
- **Row 10918** — "2022 qualifier v Brazil hosted at **Estadio Atanasio Girardot, Medellín**" — unsupported/contradicted: Colombia's qualifiers were in **Barranquilla**. UNVERIFIED→FAIL.
- **Row 10925** — "midfielder who anchored the 2022 defensive setup (Lerma)" — **non-unique**: **Wilmar Barrios** (a listed option) was equally Colombia's holding-midfield anchor. *Remedy:* distinguish.
- **Row 10926** — "2026 midfield steel like Casemiro (Lerma)" — **non-unique**: **Wilmar Barrios** (an option) is the deeper holding midfielder. *Remedy:* fix.
- **Row 10933** — 2015 penalty score answer is a **corrupted datetime** ("2026-05-04 00:00:00" = mangled 5-4). *Remedy:* restore "5-4."
- **Row 10937** — "2016 Copa Centenario: finished **fourth**" — FALSE: Colombia **won the third-place play-off 1-0 v USA**, finishing **3rd**. *Remedy:* change to 3rd. [source: rsssf]
- **Row 10946 / 10947 / 10948** — "eliminated in the **third-place play-off** (2016)" — FALSE: Colombia were eliminated in the **semi-final** (lost 0-2 to Chile) and **won** the third-place play-off. *Remedy:* fix to semi-final.
- **Row 10949** — "2018 qualifier hosting **Peru at Atanasio Girardot, Medellín**" — unsupported/contradicted: home qualifiers are in **Barranquilla**. UNVERIFIED→FAIL.

**Chunk 10954–11003 (7 dangerous):**
- **Row 10961** — "which Copa did Colombia **finish in the third-place play-off**?" (2016) — **non-unique**: Colombia also reached/won the third-place play-off in **2021** (a listed option). *Remedy:* distinguish.
- **Row 10973** — "stadium where Colombia was **eliminated** in the 2016 3rd-place play-off … **lost to the USA**" — FALSE: Colombia **won 1-0** (finished 3rd; eliminated in the SF). Venue (Univ. of Phoenix) is right but premise/explanation wrong. *Remedy:* fix.
- **Row 10979** — "in which WC did Colombia **beat Japan 1-0**?" — FALSE premise: the 2014 win was **4-1** (no WC 1-0 v Japan). *Remedy:* fix to 4-1.
- **Row 10994** — "in which WC did **Messi score against Colombia**?" (2014) — FALSE: Argentina did **not** play Colombia at the 2014 WC. *Remedy:* remove. [source: Wikipedia 2014 WC]
- **Row 10996 / 11002** — "Colombia's **Bogotá / El Campín altitude advantage** first a major factor (2010)" — FALSE premise: home qualifiers are in **Barranquilla**, sea level. *Remedy:* remove altitude claim.
- **Row 11001** — "first hosted at **Estadio Metropolitano Roberto Meléndez** in the 2018 cycle" — FALSE: it has been Colombia's qualifier home since **1990**, well before 2018. *Remedy:* fix the cycle.

**Chunk 11004–11053 (12 dangerous):**
- **Row 11004** — "beat **Japan 1-0** in the 2014 group stage" — FALSE: was **4-1**. *Remedy:* fix to 4-1.
- **Row 11006 / 11010 / 11011 / 11045** — "Colombia hosted a WC qualifier at **Estadio Atanasio Girardot, Medellín**" — FALSE: the cited Sept 7 2012 match (and all home qualifiers) were at **Estadio Metropolitano, Barranquilla**; opponent was Uruguay (4-0), not Paraguay. *Remedy:* fix venue. [source: 2014 CONMEBOL qualifying, Wikipedia]
- **Row 11008** — "in which year did Colombia **fail to qualify**?" (2022) — **non-unique**: Colombia also failed for **2010** (a listed option). *Remedy:* disambiguate.
- **Row 11015** — "which Copa did Colombia reach the **third-place match**?" (2021, "lost to Peru") — **non-unique** (also 2016, a listed option) **and** explanation FALSE (Colombia **won** 3-2 v Peru). *Remedy:* fix.
- **Row 11017 / 11019** — "Estadio Metropolitano primary home **since the 2018 qualifiers**" — FALSE: it has been the home venue since **1990**. *Remedy:* fix.
- **Row 11025 / 11047** — "lost **3-0 to Argentina at the 2014 WC**" — FALSE premise (no such match). *Remedy:* remove.
- **Row 11032** — 2018 v England full-time score is a **corrupted datetime** ("2026-01-01 00:00:00" = mangled 1-1). *Remedy:* restore "1-1."

**Chunk 11054–11105 (5 dangerous):**
- **Row 11058** — "Bogotá **2,640m altitude** first affected a qualifier (2006)" — FALSE premise: home qualifiers are in **Barranquilla** (sea level). *Remedy:* remove altitude claim.
- **Row 11064** — "Estadio Metropolitano became the main venue **in the 2010s**" — FALSE: it has been the home venue since the **1990s** (a listed option). *Remedy:* change to 1990s.
- **Row 11070** — Lorenzo appointment answer is a **corrupted datetime** ("2022-06-01 00:00:00"). *Remedy:* restore "June 2022."
- **Row 11077** — "**eliminated in the third-place play-off** (2016)" — FALSE: Colombia were eliminated in the **semi-final** and **won** the 3rd-place play-off 1-0. *Remedy:* fix to semi-final.
- **Row 11098** — "2014 opponent who beat them by a larger margin than the 2024 final (**Argentina 3-0**)" — FALSE premise: no Colombia–Argentina match at the 2014 WC. *Remedy:* remove.

**Chunk 11106–11157 (9 dangerous):**
- **Row 11106** — "2026 Colombia player based in a **South American league** (Jhon Córdoba)" — FALSE: Córdoba plays in **Russia** (Krasnodar); none of the options is South-America-based. UNVERIFIED/FALSE→FAIL.
- **Row 11108 / 11110 / 11113** — "Messi scored as Colombia **lost 3-0 to Argentina at the 2014 WC**" — FALSE premise (no such match). *Remedy:* remove.
- **Row 11114** — "**Bogotá El Campín 2,640m altitude advantage** in qualifiers" — FALSE premise (home venue is Barranquilla, sea level). *Remedy:* remove.
- **Row 11132** — "2021 Copa third-place match: **Lost to Peru**" — FALSE: Colombia **won 3-2**. *Remedy:* change to "Beat Peru." [source: ESPN]
- **Row 11137 / 11138** — "Mina scored in **every/each 2018 knockout match** (three goals across R16 + QF)" — FALSE: Colombia played only **one** 2018 knockout game (R16); Mina's 3 goals were 2 group-stage + 1 R16. *Remedy:* rewrite.

**Chunk 11158–11206 (11 dangerous):**
- **Row 11165** — "which manager's tenure did **NOT** start after a World Cup? (Queiroz)" — answer is **backwards**: Queiroz (Feb 2019) is the one who *did* start right after a WC; the explanation even contradicts the answer. *Remedy:* fix answer/logic.
- **Row 11170 / 11171 / 11174** — "Richard Ríos **debuted at the 2024 Copa América**" — FALSE: he debuted **12 Oct 2023** v Uruguay. *Remedy:* fix to 2023. [source: Wikipedia]
- **Row 11172** — "Lerma had more **World Cup caps in 2022** than 2018" — FALSE premise: Colombia **did not play the 2022 WC**. *Remedy:* remove.
- **Row 11176** — "Lerma made his **senior debut in 2018**" — FALSE: debut was **Nov 2017** v South Korea. *Remedy:* fix to 2017. [source: Wikipedia]
- **Row 11177** — "Lerma in their **2022 World Cup squad**" — FALSE premise: no 2022 WC squad (failed to qualify). *Remedy:* reframe to qualifying.
- **Row 11178** — "key midfielder at the 2024 Copa (Lerma)" — **non-unique**: **James** (an option) was the standout (Best Player). *Remedy:* fix.
- **Row 11186** — Mina equaliser described as a "**group stage** match" — FALSE: it was the **round of 16**. *Remedy:* fix the stage.
- **Row 11198** — "Cuadrado **missed** a penalty in the 2015 QF" — FALSE: Cuadrado **scored**; Colombia's missers were **Muriel and Murillo**. *Remedy:* fix. [source: Wikinews]
- **Row 11206** — "missed the **decisive** penalty v England (Uribe)" — **non-unique**: both **Uribe** and **Bacca** (options) missed. *Remedy:* disambiguate.

**Chunk 11207–11263 (5 dangerous):**
- **Row 11207** — "**Edwin Cardona** missed the decisive 2015 QF penalty" — FALSE: Colombia's missers were **Muriel and Zúñiga** (James/Falcao/Cuadrado scored). *Remedy:* fix. [source: Wikipedia Copa shoot-outs]
- **Row 11212** — "Falcao **reached 36 goals by the 2018 WC**" — FALSE: 36 is his later career total; he had ~31 by 2018. *Remedy:* drop the "by 2018" timing.
- **Row 11219** — "Mina scored **all three goals in the 2018 knockout stage** (R16 + QF)" — FALSE: only one knockout game (R16); 2 of his goals were group-stage. *Remedy:* rewrite.
- **Row 11227** — "Roger Martínez scored **twice** in the 2019 win over Argentina" — FALSE: the 2-0 had one each from **Roger Martínez and Duván Zapata**. *Remedy:* fix to one goal.
- **Row 11249** — "Sánchez's 2018 red card came earlier than **Quintero's in 2014**" — false premise: **Quintero was not sent off in 2014** (the explanation admits it). *Remedy:* remove the comparison.

**Chunk 11264–11309 (11 dangerous):**
- **Row 11264** — "RB who debuted **for the 2026 cycle before the 2022 WC** (Muñoz)" — internally **contradictory** timeframe (the explanation itself contradicts the stem). *Remedy:* fix the timing.
- **Row 11269** — "Estadio **Atanasio Girardot** hosted a 2014 qualifier" — FALSE: qualifiers were in **Barranquilla**. *Remedy:* fix venue.
- **Row 11272 / 11294** — "**El Campín / Bogotá 2,640m altitude** aids qualifiers" — FALSE premise (home venue is Barranquilla, sea level). *Remedy:* remove.
- **Row 11274** — "James scored Colombia's **first goal** of 2014 (v Greece)" — FALSE: **Armero** scored first (5'); James scored late. *Remedy:* fix.
- **Row 11275** — "James scored in **both 2014 and 2018** WCs" — FALSE: James scored **0** at the 2018 WC (injured). *Remedy:* fix to 2014 only.
- **Row 11303** — "league James played in before 2014 (Liga BetPlay Dimayor)" — FALSE/anachronistic: the BetPlay name dates to **2019**; James's last Colombian club (Envigado) was in the pre-2014 Primera A. *Remedy:* fix.
- **Row 11304** — "top division **during the 2018 WC** = Liga BetPlay Dimayor" — FALSE: in 2018 it was **Liga Águila** (a listed option); BetPlay began 2019. *Remedy:* change to Liga Águila.
- **Row 11306** — explanation: "James … played for **Atlético Nacional**" — FALSE: James never played for Nacional (Envigado→Banfield→Porto). *Remedy:* fix explanation.
- **Row 11307** — "Colombian club that **never won the Libertadores** (Millonarios)" — **non-unique**: **América de Cali** (an option) also never won it. *Remedy:* fix options.
- **Row 11309** — "2018 captain's club = **Atlético Nacional** (Falcao)" — FALSE: Falcao never played for Nacional (youth at River Plate; club Monaco in 2018). *Remedy:* fix.

**Chunk 11310–11360 (15 dangerous):**
- **Row 11318 / 11319 / 11320 / 11321** — "Mina scored **all 3 of Colombia's 2018 knockout goals**" — FALSE: Colombia played only **one** 2018 knockout game (R16); 2 of Mina's 3 goals were group-stage. Explanations fabricate non-existent QF/3rd-place/Japan/Senegal knockout games. *Remedy:* rewrite.
- **Row 11325** — "Mina scored **two** WC goals in 2018 (Poland & England)" — FALSE: he scored **three** (also v Senegal). *Remedy:* fix count.
- **Row 11326** — "Mina played 2018 qualifiers at **Atanasio Girardot**" — FALSE: qualifiers were in **Barranquilla**. *Remedy:* fix venue.
- **Row 11328 / 11330 / 11347 / 11348** — top-division questions list "**Categoría Primera A**" (the league's official name) as a distractor alongside "Liga BetPlay Dimayor" (its sponsor name) — **non-unique** (same competition). *Remedy:* remove the synonym option.
- **Row 11329** — "most 2018 squad players from the domestic league" — FALSE: the 2018 squad was overwhelmingly **Europe-based**; also "BetPlay" is a post-2019 name. *Remedy:* fix.
- **Row 11337 / 11346** — "first-choice after the **2022 Copa América**" — false premise: there was **no 2022 Copa América** (editions: 2021, 2024). *Remedy:* fix.
- **Row 11338** — "Vargas first-choice **at the 2022 World Cup**" — false premise: Colombia didn't play the 2022 WC. *Remedy:* reframe.
- **Row 11360** — "Richard Ríos **debuted at the 2024 Copa**" — FALSE: debuted Oct 2023. *Remedy:* fix.

**Chunk 11365–11413 (5 dangerous):**
- **Row 11372** — "which did **NOT** record 6 assists at 2024 Copa (Cuadrado)" — **non-unique**: Carrascal and Díaz (both options) also didn't; only James did. *Remedy:* fix.
- **Row 11373** — "featured in 2014 but missed the 2010 qualifiers (Cuadrado)" — **non-unique**: **James** (an option) equally fits. *Remedy:* fix.
- **Row 11383** — explanation: Tesillo's pen "saved by **Claudio Bravo**" — FALSE: Chile's keeper was **Gabriel Arias** (Bravo wasn't in the 2019 squad). *Remedy:* fix keeper.
- **Row 11396** — "Mina scored **all three 2018 knockout goals**" — FALSE: only one 2018 knockout game (R16). *Remedy:* rewrite.
- **Row 11413** — "James a **key player in the 1-1 draw with England** (2018)" — misleading/FALSE: James was **injured and did not play** that R16 match. *Remedy:* fix.

**Chunk 11414–11460 (13 dangerous):**
- **Row 11414** — "which player was in the **2014 squad** (James)" — **non-unique**: Cuadrado and Ospina (both options) were also in the 2014 squad. *Remedy:* fix options.
- **Row 11415** — "**NOT** a key defender at 2024 Copa (James)" — **non-unique**: Lerma (an option) is a midfielder, not a defender, either. *Remedy:* fix.
- **Row 11416** — "**NOT** an emerging midfielder at 2024 Copa (James)" — **non-unique**: Lerma (established) and Córdoba (a forward) also fit. *Remedy:* fix.
- **Row 11433** — "Falcao **announced retirement** after 2022 failure" — unverified/likely FALSE: no documented national-team retirement; he remained available. UNVERIFIED→FAIL.
- **Row 11448 / 11449 / 11450 / 11451 / 11452 / 11453 / 11455 / 11456** — "2018/2014 qualifier v Chile/Uruguay/Brazil/Peru hosted at **Estadio Atanasio Girardot, Medellín**" — FALSE: Colombia's qualifiers were at the **Metropolitano, Barranquilla** (cf. the correct row 11457). *Remedy:* fix venue.
- **Row 11458** — "**El Campín 2,640m altitude** aided 2018 qualifiers" — FALSE premise (Barranquilla, sea level). *Remedy:* remove.

**Chunk 11461–11535 (9 dangerous):**
- **Row 11462** — "star **from Liga BetPlay** who scored at 2014 (James)" — **non-unique**: Cuadrado (Independiente Medellín) also came through the domestic league and scored at 2014; also anachronistic name. *Remedy:* fix.
- **Row 11466** — "star who **missed 2010 due to non-qualification** (Cuadrado)" — **non-unique**: James/Mina/Sánchez (all options) also missed it (no Colombian played). *Remedy:* fix.
- **Row 11468** — "star who played the **2016 Copa Centenario** (James)" — **non-unique**: Falcao and Cuadrado (options) also played it. *Remedy:* fix.
- **Row 11470** — "James scored at **both 2014 and 2018**" — FALSE: 0 goals in 2018. *Remedy:* fix.
- **Row 11478** — "James **top assist provider at 2014 WC with six assists**" — FALSE: the 6 assists were the **2024 Copa**; at 2014 he had ~2 and was not the assist leader. *Remedy:* fix.
- **Row 11482** — "James's **club success rooted in Liga BetPlay**" — FALSE: his club success was in **Europe** (Porto/Real Madrid/Bayern). *Remedy:* fix.
- **Row 11505** — "lost the 2021 Copa third-place to **Peru**" — FALSE: Colombia **won 3-2**. *Remedy:* fix. [source: ESPN]
- **Row 11527** — "like Colombia in 2016, who **lost** a Copa 3rd-place play-off (USA)" — false premise: Colombia **won** the 2016 3rd-place match. *Remedy:* fix.
- **Row 11528** — "Colombia & Venezuela were the **only** CONMEBOL nations to miss 2010" — FALSE: Ecuador (an option), Peru, Bolivia also missed it. *Remedy:* fix.

**Chunk 11536–11592 (3 dangerous):**
- **Row 11542** — "**Peru beat Colombia on the final 2022 qualifying day**" — FALSE: on the final day Colombia beat **Venezuela** while Peru beat **Paraguay**; the two didn't play. *Remedy:* fix.
- **Row 11546** — "**Ecuador** finished 3rd directly below Colombia (2014)" — FALSE: **Chile** (an option) finished 3rd; Ecuador 4th. *Remedy:* change to Chile.
- **Row 11575** — "Queiroz led the **2022 qualifiers in 2019**" — false premise: CONMEBOL 2022 qualifying began **Oct 2020** (no 2019 qualifiers). *Remedy:* fix the year.

**Chunk 11593–11656 (14 dangerous):**
- **Row 11602 / 11656** — "**USA defeated/eliminated Colombia** in the 2016 3rd-place play-off" — FALSE: Colombia **won 1-0**. (11656's answer "USA" is who they *faced*, but the explanation falsely says "lost.") *Remedy:* fix.
- **Row 11604 / 11651** — "**Peru** eliminated/defeated Colombia in the 2021 3rd-place match" — FALSE: Colombia **won 3-2**. *Remedy:* fix.
- **Row 11616** — "**Colombia's El Campín (Bogotá) hosts high-altitude qualifiers**" — FALSE premise (Barranquilla, sea level). *Remedy:* remove.
- **Row 11630 / 11638 / 11639 / 11645 / 11646** — "2014/2018 qualifier v Chile/Peru at **Atanasio Girardot, Medellín**" — FALSE: qualifiers were in **Barranquilla** (cf. correct rows 11637/11640/11641/11642). *Remedy:* fix venue.
- **Row 11631** — "2015 Copa match v Brazil at **Atanasio Girardot, Medellín**" — FALSE: the 2015 Copa was hosted by **Chile** (match at Estadio Monumental, Santiago). *Remedy:* fix.
- **Row 11633** — "2016 Copa match v Costa Rica at **Atanasio Girardot, Medellín**" — FALSE: the 2016 Centenario was in the **USA** (match at NRG Stadium, Houston). *Remedy:* fix.
- **Row 11643** — "Atanasio Girardot an **alternate venue for 2022 qualifiers**" — FALSE: home qualifiers were in Barranquilla. *Remedy:* remove.
- **Row 11647** — "**Argentina beat Colombia 3-0 at the 2014 WC**" — FALSE premise (no such match). *Remedy:* remove.

**Chunk 11657–11736 (15 dangerous):**
- **Row 11657** — "faced Peru in 2021 3rd-place, **lost to Peru**" — explanation FALSE: Colombia **won 3-2**. *Remedy:* fix.
- **Row 11660** — "did NOT **face Brazil en route to the 2024 final**" — FALSE: Colombia faced **Brazil in the group** (1-1). *Remedy:* fix.
- **Row 11662** — "did NOT lose on pens to (Argentina) in a 2018 knockout" — **non-unique**: Germany and Brazil (options) also weren't lost-to. *Remedy:* fix.
- **Row 11663** — "did NOT play in the 2014 WC (England)" — **non-unique**: Colombia also did **not** play **Argentina** (an option); explanation falsely says they faced Argentina. *Remedy:* fix.
- **Row 11664** — "did NOT play in the 2019 Copa **knockout** (Argentina)" — **non-unique**: Paraguay and Uruguay (options) also weren't knockout opponents. *Remedy:* fix.
- **Row 11665** — "team James scored against in the 2014 group (Japan)" — **non-unique**: James scored v **Greece and Ivory Coast** (both options) too. *Remedy:* fix.
- **Row 11669** — "**USA eliminated Colombia** in the 2016 3rd-place match" — FALSE: Colombia **won 1-0**. *Remedy:* fix.
- **Row 11678** — "two CONMEBOL nations above Colombia in 2022 (Peru & Uruguay)" — **non-unique**: **Argentina & Brazil** (an option pair) also finished above. *Remedy:* fix.
- **Row 11703** — "stadium of Colombia's **3-0 loss to Argentina in 2014** (Mineirão)" — FALSE premise (no such match). *Remedy:* remove.
- **Row 11712** — "Queiroz managed the **2022 qualifiers in 2019**" — false premise: CONMEBOL 2022 qualifying began **Oct 2020**. *Remedy:* fix year.
- **Row 11715** — "**Messi scored in Argentina's 3-0 win over Colombia at 2014**" — FALSE premise (no such match). *Remedy:* remove.
- **Row 11727** — "coach chose **Atanasio Girardot** for a 2018 qualifier for lower altitude" — FALSE: qualifiers were in **Barranquilla**. *Remedy:* fix.
- **Row 11730 / 11731 / 11733** — "Colombia's **Bogotá / El Campín high-altitude** qualifiers challenge visitors" — FALSE premise: home venue is **Barranquilla** (sea level, heat/humidity). *Remedy:* remove altitude claim.

**Addendum (Colombia):**
- **Row 11146** — "which forward was in the **2015 Copa squad** (Bacca)" — **non-unique**: Falcao, James and Cuadrado (all options) were also in the 2015 squad. *Remedy:* fix options.

---

## Costa Rica (rows 11737–12858) — batch 2

> Key facts: peak FIFA rank **13th (2015)** (NOT 15th); **did NOT qualify for 2026** (3rd in CONCACAF final group; Panama/Curaçao/Haiti qualified). Home venue: Estadio Nacional, San José.

**Chunk 11737–11784 (6 dangerous):**
- **Row 11741 / 11746 / 11747 / 11749 / 11753** — "Costa Rica's **highest/best/peak FIFA ranking = 15th**" — FALSE: their highest-ever ranking is **13th** (2015); 15th was a 2014 figure. *Remedy:* change to 13th. [source: MLSsoccer/FIFA]
- **Row 11742** — "which CONCACAF nation **also** reached top-15 after CR's 2014 run? (Costa Rica)" — **self-referential** answer (names the subject); also USA/Mexico reached top-15 historically. *Remedy:* fix.

**Chunk 11786–11840 (8 dangerous):**
- **Row 11789** — "Estadio Nacional hosted CR's decisive **2022 inter-confederation playoff**" — FALSE: that playoff (v New Zealand) was in **Qatar** (Al Rayyan). *Remedy:* fix venue.
- **Row 11817** — "Navas first won the **CL in 2014**, before his WC debut" — FALSE: he joined Real Madrid **after** the 2014 WC; first CL title **2016**. *Remedy:* fix.
- **Row 11818** — margin v Uruguay is a **corrupted datetime** ("2026-01-03" = mangled 3-1). *Remedy:* restore "3-1."
- **Row 11820** — "CONCACAF nation with more consecutive Gold Cups since 2007 (USA)" — **non-unique**: **Mexico** (an option) also played every edition. *Remedy:* fix.
- **Row 11824** — "who finished **third** in Group D (England)" — FALSE: **Italy** finished 3rd; England were 4th. *Remedy:* change to Italy.
- **Row 11828** — "Uruguay's next WC win after 2014 was **2018 v Saudi**" — FALSE: Uruguay **beat England and Italy later in 2014** (after losing to CR). *Remedy:* fix.
- **Row 11832** — "CR also **defeated England**" to top the 2014 group — FALSE: they **drew 0-0**. *Remedy:* fix.
- **Row 11835** — "CR faced **Mexico** in the 2014 WC" — FALSE: CR's group was Uruguay/Italy/England. *Remedy:* fix.

**Chunk 11842–11891 (11 dangerous):**
- **Row 11842** — "other CR **defeat** (Netherlands 2014)" — **non-unique**: Germany 2006 and Brazil 2018 (both options) were also defeats; explanation wrongly calls them "wins." *Remedy:* fix.
- **Row 11852 / 11857** — "**peaked/highest FIFA ranking = 15th**" — FALSE: highest is **13th** (2015). *Remedy:* fix.
- **Row 11853** — "**five consecutive** WCs 2006–2022" — FALSE: CR **missed 2010**; the run is 2014/2018/2022 (three). *Remedy:* fix.
- **Row 11858** — "CONCACAF nation that did NOT reach its highest rank after 2014 (USA)" — **non-unique/false**: Mexico (an option) also peaked earlier; the premise others peaked post-2014 is wrong. *Remedy:* fix.
- **Row 11863** — "**Costa Rica topped** their 2018 qualifying group, Panama 2nd" — FALSE: **Mexico** topped the 2018 Hexagonal; CR 2nd, Panama 3rd. *Remedy:* fix.
- **Row 11867** — "2014 draw v England at CR's 35,175 **home venue** (Estadio Nacional)" — FALSE: the match was in **Brazil** (Estádio Mineirão). *Remedy:* fix.
- **Row 11882** — scoreline v Uruguay is a **corrupted datetime** ("2026-01-03" = 3-1). *Remedy:* restore "3-1."
- **Row 11883** — "Óscar Ramírez also coached which **other** nation? (Costa Rica)" — **self-referential** (he coached only CR). *Remedy:* fix.
- **Row 11884** — "Ramírez oversaw **two** 2018 draws (incl. **2-2 v Germany**)" — FALSE: CR had **one** draw (2-2 v Switzerland); never played Germany (group: Brazil/Switzerland/Serbia). *Remedy:* fix.
- **Row 11885** — "which nation **beat** CR **3-1** in 2014? (Uruguay)" — contradictory: **CR beat Uruguay** 3-1 (CR won). *Remedy:* fix stem.

**Chunk 11892–11949 (11 dangerous):**
- **Row 11897** — "Mexico's Azteca holds **~65,000**" — FALSE: capacity is **~87,000** (cf. correct row 11898). *Remedy:* fix figure.
- **Row 11914** — "CR secured its **2026** place via CONCACAF qualification" — FALSE: CR **did not qualify** for 2026 (3rd in final group). *Remedy:* remove.
- **Row 11917 / 11918 / 11924 / 11925** — Gold Cup counts (Eight/Six/Six/Seven) contradict the correct **Nine** (2007–2023). *Remedy:* fix to nine.
- **Row 11931** — "other WC group with **three former champions** = 2018 Group F" — FALSE: Group F (Germany/Mexico/Sweden/Korea) had only one. *Remedy:* fix.
- **Row 11933** — "nation CR did **NOT** face in a WC playoff (Australia)" — **non-unique**: Uruguay and Peru (options) also weren't faced (only NZ was). *Remedy:* fix.
- **Row 11937** — "Saprissa supplied defenders **González, Duarte, Mora** (2014)" — FALSE: González was at **Columbus Crew**, Duarte at **Club Brugge**; only Mora was Saprissa. *Remedy:* fix.
- **Row 11941** — "Navas's **three CL titles** crucial for the **2014** campaign" — FALSE/anachronistic: he won his first CL in **2016** (0 titles in 2014). *Remedy:* fix.
- **Row 11949** — "2022 starter at an **MLS club** (Francisco Calvo, San Jose)" — FALSE: by the 2022 WC Calvo had moved to **Konyaspor** (Turkey). *Remedy:* fix.

**Chunk 11950–11997 (2 dangerous):**
- **Row 11950** — "2022 squad player **based in MLS** (Francisco Calvo, San Jose)" — FALSE: by the 2022 WC Calvo was at **Konyaspor**. *Remedy:* fix.
- **Row 11994** — "CR beat Italy, the **defending champions**, in 2014" — FALSE: the 2014 defending champions were **Spain** (2010 winners); Italy won 2006. *Remedy:* fix.

**Chunk 11998–12051 (13 dangerous):**
- **Row 11998** — "year CR eliminated in the **group stage** (2022)" — **non-unique**: 2018 (an option) was also a group-stage exit. *Remedy:* disambiguate.
- **Row 12000 / 12007 / 12051** — "qualified for **every WC since 2006 / 3rd or 4th consecutive (2006,2010,2014…)**" — FALSE: CR **missed 2010**; the consecutive run is 2014/2018/2022. *Remedy:* fix.
- **Row 12009** — "Estadio Nacional **first hosted a qualifier in 2011**" — FALSE: CR's first 2014 qualifier there was **2012** (cf. correct row 12001). *Remedy:* fix.
- **Row 12011** — "Navas WC-qualifying **debut 2006**" — FALSE: debut **11 Oct 2008** (2010 cycle). *Remedy:* change to 2008/2010 cycle. [source: Wikipedia]
- **Row 12016** — "CR qualified for **more** WCs than the USA since 2006" — FALSE: USA has as many/more (incl. 2026 host). *Remedy:* fix.
- **Row 12018** — "CONCACAF nation with **fewer** WCs than CR since 2006 (Panama)" — **non-unique**: **Honduras** (an option, 2 since 2006) also fewer. *Remedy:* fix.
- **Row 12024 / 12025 / 12029 / 12030** — Uruguay scoreline is a **corrupted datetime** ("2026-01-03" = 3-1). *Remedy:* restore "3-1."
- **Row 12038** — Borges qualifying-debut answer is a **corrupted datetime** ("2008-06-01 00:00:00"). *Remedy:* restore "June 2008."

**Chunk 12052–12122 (10 dangerous):**
- **Row 12056** — "Estadio Nacional **first hosted a qualifier in 2011**" — FALSE: CR's first qualifier there was **2012** (cf. row 12001). *Remedy:* fix.
- **Row 12058** — "Estadio Nacional hosted a **2010** qualifier in **2009**" — FALSE: the stadium **opened in 2011** (couldn't host a 2009 match). *Remedy:* remove.
- **Row 12060** — "generational transition began **after the 2018 WC**" — FALSE: CR's 2022 squad was still veteran-heavy; transition began **after 2022** (cf. row 12059). *Remedy:* fix.
- **Row 12073** — "2014 champion CR did NOT beat (England)" — explanation FALSE ("did not play England"; they **drew 0-0**); also Brazil (an option) wasn't in the group. *Remedy:* fix.
- **Row 12083** — "2014 QF-finalist CR did not surpass (Argentina)" — **non-unique**: Netherlands, Germany, Brazil (all options) also went further than CR's QF. *Remedy:* fix.
- **Row 12091** — "2022 GK NOT from Costa Rica (Lloris)" — **non-unique**: Neuer and Courtois (options) are also non-Costa Rican; explanation wrongly calls them Costa Rican. *Remedy:* fix.
- **Row 12096** — "CONCACAF nation that did NOT match CR's consistency (USA)" — **non-unique**: Honduras and Canada (options) also less consistent. *Remedy:* fix.
- **Row 12120** — "CR's **10** Gold Cup appearances 2007–2023" — FALSE: there are **9** editions. *Remedy:* fix count.
- **Row 12121 / 12122** — "Mexico matched CR's **every-WC / six-straight** qualification 2006–2022" — FALSE premise: CR **missed 2010**, so didn't qualify for every WC. *Remedy:* fix.

**Chunk 12123–12216 (9 dangerous):**
- **Row 12123** — "matched CR's **three straight 2006–2014** (USA)" — false premise: CR **missed 2010** (no three-straight). *Remedy:* fix.
- **Row 12150 / 12157** — "CONCACAF nation, alongside CR, regular Gold Cup (USA)" — **non-unique**: both **USA and Mexico** (options) are regulars. *Remedy:* fix.
- **Row 12154 / 12155** — "Mexico & CR **only** ones to qualify for every WC 2006–2022" — FALSE: CR **missed 2010**. *Remedy:* fix.
- **Row 12162** — "USA earned a **higher** 2014 ranking than CR (13th vs 15th)" — FALSE: CR (QF) ranked above USA after 2014; CR's peak is 13th. *Remedy:* fix.
- **Row 12179** — "CR faced **USA** at the 2014 WC (Group G)" — FALSE: CR was **Group D**, USA Group G; they never met. *Remedy:* fix.
- **Row 12189** — "2014 match decided by **penalties** (QF v Netherlands)" — **non-unique**: the **R16 v Greece** (an option) was also a shootout. *Remedy:* disambiguate.
- **Row 12210** — "Bryan Ruiz had **over 120 caps by the 2014 WC**" — FALSE: he had ~80 in 2014 (reached 120+ years later). *Remedy:* fix.

**Chunk 12217–12265 (4 dangerous):**
- **Row 12239** — "Navas played in a **2023 Gold Cup final**" — FALSE: CR did **not** reach the 2023 Gold Cup final (eliminated by Panama in the QF). *Remedy:* remove.
- **Row 12243** — "Navas saved a penalty in the **2014 quarter-final** (Gekas, v Greece)" — FALSE: the Gekas save was the **R16 v Greece**; the QF was v Netherlands (CR lost the shootout). *Remedy:* fix.
- **Row 12245** — "Navas saved **two penalties** in the 2014 QF, from **Bryan Ruiz and Celso Borges**" — FALSE/nonsensical: those are CR's own players; **Krul (NED)** saved CR's penalties. *Remedy:* remove.
- **Row 12248** — "Navas started **more 2026 than 2022 qualifiers**" — FALSE: Navas **retired from the national team (2024)** and did not play the 2026 qualifiers. *Remedy:* fix.

**Chunk 12266–12311 (1 dangerous):**
- **Row 12299** — "CR entered 2018 ranked 23rd, lower than their **13th ranking entering 2014**" — FALSE: CR were ranked ~28th **entering** 2014 (the 13th came in 2015, after the run). *Remedy:* fix the comparison.

**Chunk 12312–12359 (6 dangerous):**
- **Row 12325** — "Borges had **over 150 caps at the 2018 WC**" — FALSE: he had ~120 in 2018; reached 150 in the 2022 cycle (cf. 12324). *Remedy:* fix.
- **Row 12328** — "Borges **scored in the 2014 quarter-final**" — FALSE: the QF v Netherlands was **0-0**. *Remedy:* remove.
- **Row 12333** — "Borges based in **MLS (Chicago Fire)** at 2022" — FALSE: he was at **Alajuelense** (domestic; cf. 12334). *Remedy:* fix.
- **Row 12340** — "Bennette **debuted during 2026 qualification**" — FALSE: he debuted **2022** (cf. 12341). *Remedy:* fix.
- **Row 12350** — "Kendall Waston based in **MLS (FC Cincinnati)** at 2022" — FALSE: he was at **Saprissa** (cf. 12348). *Remedy:* fix.
- **Row 12355** — "Umaña's pen saved by **Cillessen**" — FALSE: **Tim Krul** saved it (van Gaal's sub; cf. 12353). *Remedy:* fix keeper.

**Chunk 12360–12406 (5 dangerous):**
- **Row 12362** — "**Borges missed** the first 2014 QF penalty (Krul save)" — FALSE: Borges **scored**; the missers were **Ruiz and Umaña**. *Remedy:* fix.
- **Row 12366** — "Navas saved **three penalties** in the 2014 QF (v Greece)" — FALSE: the QF was v Netherlands (Navas saved 0); v Greece (R16) he saved **one** (Gekas). *Remedy:* fix.
- **Row 12381** — "Ruiz scored in the **1-1 draw with the Netherlands**" — FALSE: the QF was **0-0**. *Remedy:* fix (Greece R16 was 1-1).
- **Row 12388 / 12389** — "Campbell scored **twice** in the 3-1 v Uruguay" — FALSE: he scored **once** (others: Duarte, Ureña). *Remedy:* fix.

**Chunk 12407–12453 (5 dangerous):**
- **Row 12408** — "2022 squad player at an **MLS club** (Calvo, San Jose)" — FALSE: by the WC Calvo was at **Konyaspor**. *Remedy:* fix.
- **Row 12419** — "**Bennette** scored the decisive 2022 playoff goal v New Zealand" — FALSE: **Joel Campbell** scored the 1-0 winner (cf. 12379). *Remedy:* fix.
- **Row 12421** — "Ruiz scored crucial goals against **Italy and Uruguay**" — FALSE: Ruiz scored v Italy (and Greece), **not** v Uruguay (Campbell/Duarte/Ureña). *Remedy:* fix.
- **Row 12428** — "2014 QF at **Arena Pernambuco**" — FALSE: the QF v Netherlands was at **Arena Fonte Nova** (an option); Pernambuco hosted the Italy win. *Remedy:* fix venue.
- **Row 12451** — "2022 rival with a larger home stadium than Estadio Nacional (Japan)" — **non-unique**: Germany and Spain (options) also have far larger stadiums. *Remedy:* fix.

**Chunk 12454–12501 (9 dangerous):**
- **Row 12454** — "Bryan Ruiz played for **Saprissa** before 2014" — FALSE: Ruiz came through **Alajuelense** (cf. 12463). *Remedy:* fix.
- **Row 12455** — "Celso Borges a 2014 starter **playing for Alajuelense**" — FALSE: in 2014 Borges was at **AIK (Sweden)**. *Remedy:* fix.
- **Row 12468** — "CR club that has **NOT won the CCL since 2006** (Herediano)" — **non-unique**: Saprissa (2005) and Alajuelense (2004) also haven't won it since 2006. *Remedy:* fix.
- **Row 12474** — "CR club **NOT in the Primera División** (Pérez Zeledón)" — FALSE: Pérez Zeledón **is** a Primera División club. *Remedy:* fix.
- **Row 12478** — "club rivalry that fuelled 2014 (Saprissa vs Alajuelense)" — **non-unique**: "Deportivo Saprissa vs Liga Deportiva Alajuelense" (an option) is the **same** rivalry. *Remedy:* fix options.
- **Row 12481** — "Saprissa won the **2009** CONCACAF Champions' Cup" — FALSE: Saprissa's last was **2005**; the 2009 CCL was won by **Atlante**. *Remedy:* fix.
- **Row 12487** — "defender who debuted at the 2006 WC (Badilla)" — **non-unique**: Wallace and Fernández (options) were also 2006 debutants; explanation is nonsensical. *Remedy:* fix.
- **Row 12488** — "defender **from MLS** who started all 3 in 2022 (Waston)" — FALSE: Waston was at **Saprissa** (domestic). *Remedy:* fix.
- **Row 12490** — "FIFA ranking **peak** after 2014 = 15th" — FALSE: the peak is **13th** (2015). *Remedy:* fix.

**Chunk 12502–12547 (2 dangerous):**
- **Row 12514** — "Navas first won the CL **during 2014 World Cup qualifying**" — FALSE: his first CL was **2016**. *Remedy:* fix timing.
- **Row 12542** — "Navas won the CL **in 2014, before the 2014 WC**" — FALSE: first CL **2016** (joined Real Madrid after the 2014 WC). *Remedy:* fix.

**Chunk 12548–12594 (9 dangerous):**
- **Row 12549** — "Navas's **2014 CL win** inspired the WC run" — FALSE: first CL **2016**. *Remedy:* fix.
- **Row 12553** — "Navas's **2022 Champions League win**" — FALSE: Navas won no CL in 2022 (his were 2016–2018; at PSG in 2022). *Remedy:* fix.
- **Row 12566** — "Pinto managed **Saprissa** before 2014" — FALSE/unsupported: Pinto came to the CR national team, not Saprissa. UNVERIFIED→FAIL.
- **Row 12570** — "Borges debuted in **2006** qualifying" — FALSE: debut **2008** (2010 cycle; cf. 12579). *Remedy:* fix.
- **Row 12573** — "Borges had **over 150 caps for the 2014 squad**" — FALSE: ~80 in 2014; reached 150 in 2022. *Remedy:* fix.
- **Row 12575** — "Borges **started all five** 2014 matches" — FALSE: he was **suspended for the QF** (v Netherlands). *Remedy:* fix.
- **Row 12580** — "Borges faced **Brazil in 2018 and 2022**" — FALSE: CR's 2022 group was Spain/Japan/Germany (no Brazil). *Remedy:* fix.
- **Row 12587** — "Navas played in the **2026 qualifiers**" — FALSE: he retired from the NT (2024). *Remedy:* fix.
- **Row 12592** — "Júnior Díaz featured in both the 2014 Uruguay win and the **2022 Spain loss**" — FALSE: Díaz (b.1983) was not in the 2022 squad. *Remedy:* fix.

**Chunk 12595–12642 (5 dangerous):**
- **Row 12595** — "Navas first won the CL **in 2014**" — FALSE: first CL **2016**. *Remedy:* fix.
- **Row 12597** — "2022 opener starter **from MLS (Calvo, Chicago Fire)**" — FALSE: Calvo was at **Konyaspor** by the WC. *Remedy:* fix.
- **Row 12605** — "Navas in both **2022 and 2026** qualification" — FALSE: he retired (2024), no 2026. *Remedy:* fix.
- **Row 12612 / 12613** — "Campbell scored **twice** in the 3-1 v Uruguay" — FALSE: he scored **once**. *Remedy:* fix.

**Chunk 12643–12694 (1 dangerous):**
- **Row 12665** — "four consecutive qualifications from 2006 (**2006, 2010, 2014, 2018**)" — FALSE: CR **missed 2010**. *Remedy:* fix.

**Chunk 12695–12754 (5 dangerous):**
- **Row 12736 / 12737** — "Ferran Torres scored a **hat-trick** v CR (2022)" — FALSE: he scored **two** (cf. 12738). *Remedy:* fix.
- **Row 12742** — "2014 QF at **Estádio Castelão**" — FALSE: the QF v Netherlands was at **Arena Fonte Nova** (an option); Castelão hosted the Uruguay game. *Remedy:* fix.
- **Row 12750** — "CR **beat Switzerland** at 2018" — FALSE: they **drew 2-2** (explanation admits it). *Remedy:* fix.
- **Row 12754** — "team CR beat in the 2014 **quarter-finals** (Greece)" — FALSE: Greece was the **R16**; CR **lost** the QF (Netherlands). *Remedy:* fix.

**Chunk 12755–12808 (9 dangerous):**
- **Row 12760** — "did NOT face in the 2014 **QF** (Argentina)" — **non-unique**: Brazil and Germany (options) also weren't QF opponents. *Remedy:* fix.
- **Row 12761** — "did NOT lose to at 2018 (Germany)" — **non-unique**: Switzerland (an option, 2-2 draw) also not lost to. *Remedy:* fix.
- **Row 12762** — "did NOT lose to in the 2022 group (Germany)" — FALSE: CR **lost to Germany 4-2**; they did not lose to **Japan** (they won). Explanation doubly wrong. *Remedy:* fix.
- **Row 12763** — "team that did NOT defeat CR in the 2014 knockout (Netherlands)" — contradictory: the Netherlands **eliminated** CR (explanation says they lost to NED). *Remedy:* fix.
- **Row 12770** — "three teams CR beat in the 2014 group (Italy, Uruguay, **England**)" — FALSE: they **drew England 0-0** (beat only two). *Remedy:* fix.
- **Row 12777 / 12780** — "Spain and **Japan** beat CR (2022)" — FALSE: CR **beat Japan**; they lost to Spain and **Germany**. *Remedy:* fix.
- **Row 12784** — "first 21st-century qualification = **2006**" — FALSE: CR qualified for **2002** (a listed option). *Remedy:* fix.
- **Row 12790** — "CR qualified via CONCACAF direct entry for **2026**" — FALSE: CR **did not qualify** for 2026. *Remedy:* remove.

**Correction sweep — "CR lost to Japan" false premise (7 rows reclassified from PASS):**
> CR **beat** Japan 1-0 in 2022 and **lost to Spain (7-0) and Germany (4-2)** — not "Spain and Japan."
- **Row 11843** — "Japan beat CR 1-0 in 2022" — FALSE: CR won that match. *Remedy:* fix.
- **Row 11847** — "lost to Spain and Japan (2022 group)" — FALSE premise. *Remedy:* change Japan→Germany.
- **Row 11886** — "conceded 8 (Spain 7 + Japan 1)" — FALSE: Japan was a clean-sheet win; conceded 11 (Spain 7 + Germany 4). *Remedy:* fix.
- **Row 11990 / 11997** — "eliminated after losing to Spain and Japan" — FALSE premise. *Remedy:* change Japan→Germany.
- **Row 12005 / 12014** — "lost to Spain and Japan (2022)" — FALSE premise. *Remedy:* change Japan→Germany.

**Chunk 12810–12858 (1 dangerous):**
- **Row 12815** — "Ferran Torres scored a **hat-trick** v CR (2022)" — FALSE: he scored **two** (cf. 12738). *Remedy:* fix.

## Canada (batch-2 rows 7821–9330) — COMPLETE: 69 dangerous

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

### Belgium fail clusters (rows 3242–4191)
- **Non-unique answers (the biggest cluster):** "which player had multiple Ballon d'Or nominations"
  (De Bruyne, Lukaku, Hazard, Courtois all qualify); "which attacker played at X & Y" (Carrasco, Mertens,
  Hazard, Lukaku all fit); duplicate-venue options ("King Baudouin Stadium" = "Stade Roi Baudouin";
  "Belgian FA" = "Royal Belgian FA"); "won their UEFA group" for 2014/2018/2022/2026 (all true); "missed
  the World Cup" (2006 **and** 2010); Genk-academy + 2014-debut traits shared by De Bruyne **and** Courtois.
- **Excel date-corruption in the answer cell:** scores/dates mangled to `2026-02-03 00:00:00` etc.
  (e.g. the 3-2 NL score, the Euro 2020 2-1, the 3-4-3 formation, Tedesco's Feb-2023 appointment).
- **Stale facts:** Belgium qualified for **2026 under Rudi Garcia**, not Tedesco (sacked Jan 2025) — many
  rows still say Tedesco. Openda now plays in Italy (Juventus).
- **Wrong scorers / non-events:** Origi "scored vs Japan" (it was Vertonghen/Fellaini/Chadli); Lukaku
  "hat-trick" at 2018 (he scored 2+2); De Bruyne/Lukaku "scored vs Japan" (they didn't); the Euro 2024
  goal was a **Vertonghen own goal**, not a Kolo Muani goal; Benzema "scored twice" in 2021 (once); no
  red card vs Croatia 2022; Belgium scored **16** at 2018 (not 9); 2018 Fair Play went to **Spain**.
- **Eurostadium confusion:** it was a **Euro 2020** venue (cancelled Jan 2018), not a World Cup project.
- **Self-referential / wrong-detail:** "which nation, like Belgium, …" answered "Belgium"; Hazard "three"
  Chelsea POTY (four); Vertonghen "154 caps" milestones placed at 2022 (he had ~140 then; record set 2017);
  Mertens "debuted 2013" (2011); Tielemans "debuted 2018" (2016).

---

### Row 3242 — Belgium (hard) — FAIL: wrong answer (miscounted streak)
**Q:** After Belgium's 2018 World Cup group stage win over Panama, how many consecutive major tournaments had they qualified for?
**Answer:** Four tournaments
**Why it fails:** As of the June 2018 win over Panama, Belgium's run of consecutive major tournaments qualified for was 2014 WC, Euro 2016, 2018 WC = THREE, not four. The explanation ('four consecutive 2014 to 2022') counts tournaments that hadn't happened yet at that point and still miscounts. 'Three tournaments' is a listed option.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Change the answer to 'Three tournaments' (2014 WC, Euro 2016, 2018 WC), or reword to ask about the full 2014–2024 run.

### Row 3244 — Belgium (easy) — FAIL: non-unique (Union SG also fits)
**Q:** After Belgium's 2018 World Cup run, which resurgent club won its first league title in decades?
**Answer:** Royal Antwerp
**Why it fails:** Answer 'Royal Antwerp' (2022-23 Pro League, first since 1957) is correct, but the distractor Union Saint-Gilloise ALSO won its first league title in decades after 2018 — the 2024-25 title, its first since 1935. Both are 'resurgent clubs that won a first league title in decades,' so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Royale_Union_Saint-Gilloise
**Remedy:** Pin Antwerp uniquely (e.g. 'won the 2022-23 title, first since 1957') or drop Union Saint-Gilloise as a distractor.

### Row 3272 — Belgium (medium) — FAIL: non-unique (generic trait)
**Q:** At the 2022 World Cup, which Belgium player had multiple Ballon d'Or nominations?
**Answer:** Kevin De Bruyne
**Why it fails:** 'Multiple Ballon d'Or nominations' is not unique to De Bruyne: distractors Romelu Lukaku and Thibaut Courtois have also appeared on multiple Ballon d'Or shortlists (Courtois won the 2022 Yashin Trophy and placed in the Ballon d'Or top 10). A generic 'which player has [trait]' with several valid options fails uniqueness.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Make it specific (e.g. 'finished 3rd in the 2022 Ballon d'Or') so only De Bruyne qualifies.

### Row 3289 — Belgium (hard) — FAIL: false premise (name post-dates 2018)
**Q:** Before which FIFA World Cup did Belgium first use Proximus Basecamp?
**Answer:** The 2018 World Cup
**Why it fails:** The "Proximus Basecamp" name did not exist before the 2018 World Cup: the RBFA's Tubize national centre was rebranded "Proximus Basecamp" only in August 2020 (the upgraded facility opened ~2021). So Belgium could not have "first used Proximus Basecamp" ahead of 2018.
**Source:** https://www.proximus.com/news/2020/20200825_proximus_basecamp.html
**Remedy:** Change the answer to 2022 (first World Cup after the 2020 renaming) or reword to the Tubize national training centre, which predates the Proximus naming.

### Row 3293 — Belgium (easy) — FAIL: non-unique (duplicate option)
**Q:** Belgium hosted all 2022 World Cup qualifiers at which stadium?
**Answer:** King Baudouin Stadium
**Why it fails:** Two of the four options name the SAME venue: "King Baudouin Stadium" and "Stade Roi Baudouin" are the English and French names of the identical Brussels stadium. The answer is therefore non-unique.
**Source:** https://en.wikipedia.org/wiki/King_Baudouin_Stadium
**Remedy:** Replace the duplicate French-name option with a genuinely different stadium.

### Row 3295 — Belgium (easy) — FAIL: wrong answer (date mismatch)
**Q:** Belgium hosted which World Cup qualifier match exclusively at King Baudouin Stadium in 2017?
**Answer:** Against Bosnia-Herzegovina
**Why it fails:** Belgium's home 2018-qualifier vs Bosnia & Herzegovina was on 7 October 2016, NOT 2017. Belgium's 2017 home qualifiers at King Baudouin included Greece (25 March 2017), Gibraltar and Cyprus. So "against Bosnia-Herzegovina" is wrong for 2017, and the 2017 answer is in any case non-unique.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_H
**Remedy:** Either change the year to 2016 (Bosnia) or change the answer to Greece for 2017; pin a single match/date for uniqueness.

### Row 3297 — Belgium (easy) — FAIL: Excel date-corruption in answer
**Q:** Belgium led 2-0 but lost what final score to France in the 2021 Nations League semis?
**Answer:** 2026-02-03 00:00:00
**Why it fails:** The answer cell is corrupted to "2026-02-03 00:00:00" — an Excel mangling of the scoreline 3-2. The actual result (Belgium lost 3-2 to France after leading 2-0) is not even among the options (2-1 / 3-1 / 4-2).
**Source:** https://en.wikipedia.org/wiki/2021_UEFA_Nations_League_Finals
**Remedy:** Restore the answer to 3-2 and ensure it appears as an option; sweep the dataset for date-corrupted score cells.

### Row 3308 — Belgium (easy) — FAIL: false premise (wrong goal total)
**Q:** Belgium scored 9 goals in 7 matches at the 2018 World Cup. Which 2018 team had a higher goals-per-game average?
**Answer:** Croatia
**Why it fails:** Belgium scored 16 goals at the 2018 World Cup (the tournament's HIGHEST-scoring team), not 9 (9 was only their group-stage tally). Croatia scored 14. So the premise is wrong AND the conclusion is backwards — Belgium (2.29/game) outscored Croatia (2.0/game); no listed team had a higher average than Belgium.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_statistics
**Remedy:** Fix Belgium's total to 16 and drop the false claim that another 2018 team averaged more goals per game.

### Row 3313 — Belgium (easy) — FAIL: false premise (Belgium didn't win 2018 Fair Play)
**Q:** Belgium won the 2018 FIFA Fair Play Award. Which nation won it in 2014?
**Answer:** Colombia
**Why it fails:** The stem asserts "Belgium won the 2018 FIFA Fair Play Award" — false. Spain won the 2018 World Cup FIFA Fair Play Trophy. (The asked sub-answer, Colombia for 2014, is correct, but the embedded premise is wrong.)
**Source:** https://www.fifa.com/en/tournaments/mens/worldcup/articles/fair-play-award-winners
**Remedy:** Remove/replace the false claim that Belgium won the 2018 Fair Play Award (it was Spain).

### Row 3314 — Belgium (medium) — FAIL: wrong answer (Spain won 2018 Fair Play)
**Q:** Belgium won the FIFA Fair Play Award at which World Cup?
**Answer:** 2018 World Cup
**Why it fails:** Belgium did not win the FIFA Fair Play Award at the 2018 World Cup — Spain did. So no World Cup option is correct for Belgium.
**Source:** https://www.fifa.com/en/tournaments/mens/worldcup/articles/fair-play-award-winners
**Remedy:** This Belgium-framed question has no correct answer; drop it or re-attribute to Spain.

### Row 3315 — Belgium (medium) — FAIL: non-unique (all options valid)
**Q:** Belgium won their 2022 World Cup qualifying group. Which other tournament did they also win their UEFA qualifying group for?
**Answer:** 2018 World Cup
**Why it fails:** Belgium won their UEFA qualifying group for 2014 WC, 2018 WC, 2022 WC, Euro 2024 AND the 2026 WC. All four options (2018 WC, 2014 WC, Euro 2024, 2026 WC) are therefore correct — the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Replace the distractors with tournaments Belgium did NOT top their group for, or reword to a uniquely identifying detail.

### Row 3318 — Belgium (easy) — FAIL: non-unique (Portugal also 60k+)
**Q:** Belgium's 2018 World Cup qualifiers were at the 50,093-capacity King Baudouin Stadium. Which nation's home qualifiers used a 60,000+ capacity stadium?
**Answer:** Germany
**Why it fails:** Not unique: besides Germany (rotating 60,000+ grounds), Portugal also plays home qualifiers at the Estádio da Luz (64,642), well over 60,000. Two listed options fit.
**Source:** https://en.wikipedia.org/wiki/Est%C3%A1dio_da_Luz
**Remedy:** Drop Portugal as a distractor or reword to a uniquely identifying venue/nation.

### Row 3319 — Belgium (easy) — FAIL: self-referential answer
**Q:** Belgium's 2018 World Cup squad was built from 2000s academy investment. Which nation's 'Golden Generation' had this same origin?
**Answer:** Belgium
**Why it fails:** The stem describes Belgium's 2000s academy-built Golden Generation, then asks 'which nation's Golden Generation had this same origin?' and answers 'Belgium' — the subject names itself. Circular/self-referential.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Reword so the answer is a different nation, or drop the self-reference.

### Row 3320 — Belgium (hard) — FAIL: non-unique (temporal)
**Q:** Belgium's 28-point 2018 qualifier win came before which other World Cup qualification?
**Answer:** 2022 World Cup
**Why it fails:** Belgium's 28-point 2018 qualifying campaign came before BOTH the 2022 and the 2026 World Cup qualifications. Two listed options (2022 WC, 2026 WC) are therefore correct.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Say 'immediately before' or remove the 2026 option to make the answer unique.

### Row 3323 — Belgium (medium) — FAIL: false premise (Eurostadium = Euro 2020, not a WC bid)
**Q:** Belgium's Eurostadium plans faced delays after which World Cup hosting bid?
**Answer:** 2018 World Cup
**Why it fails:** The Eurostadium was proposed as a UEFA Euro 2020 venue (Brussels was a chosen host city in 2014); it has nothing to do with a World Cup hosting bid. The explanation's claim that it 'was part of a joint bid with the Netherlands to host the 2018 World Cup' is false.
**Source:** https://en.wikipedia.org/wiki/Eurostadium
**Remedy:** Re-attribute the Eurostadium to Euro 2020 (delays cost Brussels its host status in Dec 2017; project cancelled Jan 2018).

### Row 3324 — Belgium (medium) — FAIL: false premise (Eurostadium = Euro 2020)
**Q:** Belgium's Eurostadium plans faced delays after which World Cup?
**Answer:** 2018 World Cup
**Why it fails:** Same defect: the Eurostadium's delays related to UEFA Euro 2020, not any World Cup. Linking the delays to the 2018 World Cup is a false premise.
**Source:** https://en.wikipedia.org/wiki/Eurostadium
**Remedy:** Re-frame around Euro 2020, the tournament the Eurostadium was actually meant for.

### Row 3325 — Belgium (hard) — FAIL: non-unique (constant fact)
**Q:** Belgium's FA headquarters were in Brussels before which World Cup?
**Answer:** The 2018 World Cup
**Why it fails:** The Belgian FA's headquarters were in Brussels before EVERY World Cup (2006, 2014, 2018, 2022 alike), so 'before which World Cup' has no unique answer.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Drop the question or anchor it to a specific datable change; the HQ location is a constant.

### Row 3329 — Belgium (easy) — FAIL: non-unique (won none of the four)
**Q:** Belgium's Golden Generation were ranked number 1 in the world but failed to win which major trophy?
**Answer:** The FIFA World Cup
**Why it fails:** Belgium's Golden Generation failed to win ALL four listed trophies — the World Cup, the European Championship, the Nations League AND the Confederations Cup. Every option is correct, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Restrict the options to trophies they DID win except one, or reword to a uniquely missed trophy.

### Row 3330 — Belgium (easy) — FAIL: non-unique (all were home opponents)
**Q:** Belgium's King Baudouin Stadium hosted a 2014 World Cup qualifier against which nation?
**Answer:** Wales
**Why it fails:** All four options — Wales, Scotland, Croatia and Serbia — were in Belgium's 2014 World Cup qualifying group (Group A) and all were hosted at the King Baudouin Stadium. The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_A
**Remedy:** Replace the distractors with nations Belgium did NOT host in that campaign.

### Row 3331 — Belgium (hard) — FAIL: false (KB hosted WC qualifiers long before 2018)
**Q:** Belgium's King Baudouin Stadium hosted its first World Cup qualifier for which FIFA tournament?
**Answer:** The 2018 World Cup
**Why it fails:** False: the King Baudouin Stadium (formerly Heysel, opened 1930) hosted Belgium World Cup qualifiers for decades — for 2002, 2010, 2014 and earlier cycles — not first for 2018. The dataset's own row 3306 says 'since at least 2006'.
**Source:** https://en.wikipedia.org/wiki/King_Baudouin_Stadium
**Remedy:** Drop the claim that 2018 was the first qualifier there; it long predates 2018.

### Row 3336 — Belgium (hard) — FAIL: wrong answer (run began after 2010)
**Q:** Belgium's run of four consecutive FIFA World Cup qualifications began after which tournament?
**Answer:** 2014 World Cup
**Why it fails:** Belgium's four-consecutive-World-Cup run is 2014, 2018, 2022, 2026 — it began after they MISSED the 2010 World Cup, i.e. 'after the 2010 World Cup', not after 2014. The listed option '2010 World Cup' is the correct one.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Change the answer to '2010 World Cup' (the last edition they missed before the streak).

### Row 3347 — Belgium (medium) — FAIL: false premise (Proximus name post-dates 2018)
**Q:** For which FIFA World Cup did Belgium first use the Proximus Basecamp in Tubize?
**Answer:** 2018 World Cup
**Why it fails:** Same defect as row 3289: the Tubize centre was renamed 'Proximus Basecamp' only in 2020, so Belgium did not 'first use the Proximus Basecamp' for the 2018 World Cup.
**Source:** https://www.proximus.com/news/2020/20200825_proximus_basecamp.html
**Remedy:** Use 2022 (first WC after the 2020 renaming) or refer to the Tubize national centre generically.

### Row 3349 — Belgium (easy) — FAIL: wrong answer (Home, not All)
**Q:** For which World Cup qualifiers has Belgium exclusively used King Baudouin Stadium?
**Answer:** All qualifiers
**Why it fails:** Belgium uses the King Baudouin Stadium for its HOME qualifiers only — away qualifiers are obviously played in the opponents' countries. The answer should be 'Home qualifiers' (a listed option), not 'All qualifiers'. The explanation itself says 'all their HOME qualifiers'.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Change the answer to 'Home qualifiers'.

### Row 3350 — Belgium (medium) — FAIL: non-unique (multiple campaigns)
**Q:** For which World Cup qualifying campaign was Romelu Lukaku Belgium's top scorer?
**Answer:** 2022 World Cup
**Why it fails:** Lukaku was Belgium's top scorer across multiple qualifying campaigns — top scorer for 2022 AND joint-top scorer (6 goals, with Malick Fofana) for 2026. Both 2022 and 2026 are listed options, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/List_of_international_goals_scored_by_Romelu_Lukaku
**Remedy:** Reword to a campaign where he was the sole, uniquely-identifiable top scorer, or remove the 2026 option.

### Row 3357 — Belgium (medium) — FAIL: wrong answer & explanation (3 scorers)
**Q:** How many Belgium players scored against Japan at the 2018 World Cup?
**Answer:** Two players
**Why it fails:** THREE Belgians scored against Japan in the 2018 round of 16 (3-2): Jan Vertonghen (69'), Marouane Fellaini (74') and Nacer Chadli (90+4'). The answer 'Two players' is wrong (correct: 'Three players', a listed option), and the explanation naming De Bruyne and Lukaku as the scorers is also wrong — De Bruyne assisted the winner, neither scored.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_knockout_stage
**Remedy:** Change the answer to 'Three players' and fix the scorers to Vertonghen, Fellaini, Chadli.

### Row 3360 — Belgium (medium) — FAIL: wrong number (four, not three)
**Q:** How many times had Belgian star Eden Hazard won Chelsea Player of the Year before his 2019 Real Madrid move?
**Answer:** Three times
**Why it fails:** Eden Hazard won the Chelsea Player of the Year award FOUR times — 2014, 2015, 2017 and 2019 — and the 2019 award came before his June-2019 Real Madrid transfer. So 'before his 2019 move' he had won it four times, not three. 'Four times' is a listed option.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Change the answer to 'Four times'.

### Row 3364 — Belgium (medium) — FAIL: non-unique (Hazard also a nominee)
**Q:** In Belgium's 2018 World Cup group stage, which player was a Ballon d'Or nominee?
**Answer:** Kevin De Bruyne
**Why it fails:** 'Ballon d'Or nominee' is not unique to De Bruyne — distractor Eden Hazard was also a Ballon d'Or nominee/shortlisted player (top-10 finishes). Two listed options fit the generic trait.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Make it specific (e.g. a podium finish in a named year) so only De Bruyne qualifies.

### Row 3365 — Belgium (easy) — FAIL: non-unique (scored 0 vs France)
**Q:** In Belgium's 2018 World Cup run, which knockout opponent did they score more goals against than France?
**Answer:** Brazil
**Why it fails:** Belgium scored 0 against France (SF) at the 2018 World Cup, and scored MORE than that against three of the four listed knockout opponents — Brazil (2), Japan (3) and England (2, third-place play-off). So Brazil, Japan and England all satisfy 'more goals than France'; the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Reword so only one knockout opponent fits (e.g. ask which side they scored the MOST against — Japan, 3).

### Row 3368 — Belgium (hard) — FAIL: wrong total (16, not 9)
**Q:** In the 2018 World Cup group stage, Belgium beat Tunisia 5-2. How many total goals did Belgium score in the entire 2018 tournament?
**Answer:** 9 goals
**Why it fails:** Belgium scored 16 goals across their seven 2018 matches (tournament's highest), not 9. The correct figure (16) is not even among the options (9/7/11/13).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_statistics
**Remedy:** Set the answer to 16 and include it as an option.

### Row 3369 — Belgium (easy) — FAIL: Excel date-corruption in answer
**Q:** In the Euro 2020 quarter-finals, Belgium lost to Italy by what scoreline?
**Answer:** 2026-01-02 00:00:00
**Why it fails:** The answer cell is corrupted to '2026-01-02 00:00:00' — an Excel mangling of a scoreline. Belgium lost 2-1 to Italy in the Euro 2020 QF; the correct score (2-1) is not even among the clean options (1-0/3-1/2-0).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Restore the answer to 2-1 and add it as an option; sweep for date-corrupted score cells.

### Row 3384 — Belgium (medium) — FAIL: false premise (Origi didn't score vs Japan)
**Q:** In which World Cup did Belgium's Divock Origi score against Japan?
**Answer:** 2018 World Cup
**Why it fails:** Divock Origi did not score against Japan at the 2018 World Cup. The three scorers in the 3-2 round-of-16 win were Jan Vertonghen, Marouane Fellaini and Nacer Chadli. The question's premise is false, so no World Cup year is a valid answer.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_knockout_stage
**Remedy:** Remove the question or re-attribute to an actual scorer (Vertonghen/Fellaini/Chadli).

### Row 3393 — Belgium (medium) — FAIL: Excel date-corruption in answer
**Q:** In which year did Belgium first reach FIFA's number one ranking?
**Answer:** 2015-11-01 00:00:00
**Why it fails:** The answer cell is the corrupted datetime '2015-11-01 00:00:00' instead of a clean 'November 2015'. Per the dataset's date-corruption rule this is a broken answer cell to be cleaned (the value is right but the format is mangled, and it sits oddly beside text options).
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Restore the answer to 'November 2015' and sweep the dataset for date-serial corruption.

### Row 3406 — Belgium (hard) — FAIL: wrong stage (R16, not group stage)
**Q:** In which year's World Cup group stage did Belgium beat Japan 3-2?
**Answer:** 2018
**Why it fails:** The 3-2 win over Japan was the ROUND OF 16, not the group stage. The asked year (2018) is right, but the stem mis-states the stage — a factual error that would ship as misinformation.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_knockout_stage
**Remedy:** Change 'group stage' to 'round of 16'.

### Row 3415 — Belgium (easy) — FAIL: Excel date-corruption in answer
**Q:** What was the final score when Belgium beat Brazil in the 2018 World Cup quarter-final?
**Answer:** 2026-01-02 00:00:00
**Why it fails:** The answer cell is corrupted to '2026-01-02 00:00:00' instead of the scoreline 2-1 (Belgium beat Brazil 2-1 in the 2018 QF). The correct score is not among the clean options (1-0/3-2/2-0).
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Restore the answer to 2-1 and add it as an option.

### Row 3418 — Belgium (medium) — FAIL: wrong year (2017, not 2024)
**Q:** When did Belgian defender Jan Vertonghen become his nation's most-capped player?
**Answer:** In 2024
**Why it fails:** Vertonghen became Belgium's most-capped player on 10 October 2017 (his 97th cap, vs Cyprus, surpassing Jan Ceulemans' 96). He RETIRED in 2024 with 157 caps, but he had held the record since 2017. The answer 'In 2024' is wrong (and the explanation's '154 caps' is also wrong — he finished on 157); 2017 isn't even an option.
**Source:** https://en.wikipedia.org/wiki/Jan_Vertonghen
**Remedy:** Change the answer to 2017 and fix the cap figure (157 at retirement).

### Row 3423 — Belgium (medium) — FAIL: Excel date-corruption in answer
**Q:** When did Belgium appoint Domenico Tedesco as manager?
**Answer:** 2023-02-01 00:00:00
**Why it fails:** The answer cell is the corrupted datetime '2023-02-01 00:00:00' rather than a clean 'February 2023'. Value is right but the cell is mangled and sits oddly beside text-formatted options.
**Source:** https://en.wikipedia.org/wiki/Domenico_Tedesco
**Remedy:** Restore the answer to 'February 2023'; sweep for date-serial corruption.

### Row 3424 — Belgium (medium) — FAIL: Excel date-corruption in answer
**Q:** When did Belgium appoint Tedesco to transition from their Golden Generation?
**Answer:** 2023-02-01 00:00:00
**Why it fails:** Same defect: the answer cell is the corrupted datetime '2023-02-01 00:00:00' instead of 'February 2023'.
**Source:** https://en.wikipedia.org/wiki/Domenico_Tedesco
**Remedy:** Restore the answer to 'February 2023'.

### Row 3428 — Belgium (easy) — FAIL: false premise (Eurostadium = Euro 2020)
**Q:** When did Belgium discuss Eurostadium plans for World Cup hosting?
**Answer:** In the 2010s
**Why it fails:** The Eurostadium was a UEFA Euro 2020 venue proposal, not a World Cup hosting project. 'Eurostadium plans for World Cup hosting' is a false premise (the decade, 2010s, is right but the World-Cup framing is wrong).
**Source:** https://en.wikipedia.org/wiki/Eurostadium
**Remedy:** Re-frame the Eurostadium around Euro 2020.

### Row 3429 — Belgium (medium) — FAIL: false (KB hosted WC qualifiers before 2006)
**Q:** When did Belgium first host a World Cup qualifier at King Baudouin Stadium?
**Answer:** 2006
**Why it fails:** The King Baudouin Stadium (renamed 1995, formerly Heysel/1930) hosted Belgium World Cup qualifiers well before 2006 — e.g. the 1998 (1996-97) and 2002 (2000-01) qualifying cycles. '2006' is not when it first hosted a WC qualifier.
**Source:** https://en.wikipedia.org/wiki/King_Baudouin_Stadium
**Remedy:** Remove/replace the false 2006 'first' claim; the venue long predates 2006 as a qualifier host.

### Row 3435 — Belgium (medium) — FAIL: non-unique (2018 WC also 1-0 to France)
**Q:** When did Belgium lose 1-0 to France in a major tournament?
**Answer:** Euro 2024
**Why it fails:** Belgium lost 1-0 to France in TWO major tournaments: the 2018 World Cup semi-final (Umtiti) and the Euro 2024 round of 16 (Vertonghen OG). Both 'Euro 2024' and 'World Cup 2018' are listed options, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Remove the 'World Cup 2018' option or add a distinguishing detail.

### Row 3442 — Belgium (medium) — FAIL: false premise (Proximus name post-dates 2018)
**Q:** When did Belgium open its Proximus Basecamp training centre for the 2018 World Cup?
**Answer:** 2017
**Why it fails:** The 'Proximus Basecamp' name dates from 2020 (facility opened ~2021), so Belgium did not 'open its Proximus Basecamp for the 2018 World Cup' in 2017.
**Source:** https://www.proximus.com/news/2020/20200825_proximus_basecamp.html
**Remedy:** Drop the 2017/2018 Proximus framing; refer to the Tubize centre generically.

### Row 3445 — Belgium (medium) — FAIL: wrong year & coach (2025, Garcia)
**Q:** When did Belgium qualify for the 2026 World Cup under coach Tedesco?
**Answer:** 2026
**Why it fails:** Belgium qualified for the 2026 World Cup in NOVEMBER 2025 (final matchday, 7-0 v Liechtenstein), under coach RUDI GARCIA — not in 2026 and not under Tedesco, who was sacked on 24 January 2025. Both the answer year (2026) and the named coach are wrong.
**Source:** https://www.espn.com/soccer/story/_/id/43543199/belgium-hire-rudi-garcia-new-coach-domenico-tedesco-exit
**Remedy:** Change the answer to 2025 and the coach to Rudi Garcia.

### Row 3447 — Belgium (medium) — FAIL: false premise (16 goals, not 9)
**Q:** When did Belgium score 9 goals in 7 matches at a World Cup?
**Answer:** 2018
**Why it fails:** Belgium scored 16 goals in their seven 2018 matches, not 9 (9 was only the group-stage total). The premise '9 goals in 7 matches' is false.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_statistics
**Remedy:** Fix the total to 16 (the tournament's highest).

### Row 3449 — Belgium (hard) — FAIL: Excel date-corruption in answer
**Q:** When did Belgium start their record 1,735-day FIFA ranking streak?
**Answer:** 2018-09-01 00:00:00
**Why it fails:** The answer cell is the corrupted datetime '2018-09-01 00:00:00' instead of a clean 'September 2018'. Value right, cell mangled.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Restore the answer to 'September 2018'.

### Row 3450 — Belgium (medium) — FAIL: non-unique (all four valid)
**Q:** When did Belgium win their UEFA group to qualify for the World Cup?
**Answer:** 2022 World Cup
**Why it fails:** Belgium won their UEFA qualifying group for ALL four listed World Cups — 2014, 2018, 2022 and 2026. Every option is correct, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Constrain to a uniquely identifying campaign or remove the redundant options.

### Row 3456 — Belgium (medium) — FAIL: false (KB hosted WC qualifiers before 2006)
**Q:** When did Belgium's King Baudouin Stadium host its first World Cup qualifier?
**Answer:** In 2006
**Why it fails:** Same defect as row 3429: the King Baudouin Stadium hosted Belgium World Cup qualifiers before 2006 (1998 and 2002 cycles), so 2006 was not the first.
**Source:** https://en.wikipedia.org/wiki/King_Baudouin_Stadium
**Remedy:** Remove the false 2006 'first qualifier' claim.

### Row 3457 — Belgium (medium) — FAIL: Excel date-corruption in answer
**Q:** When did Belgium's manager Tedesco begin transitioning from their aging Golden Generation?
**Answer:** 2023-02-01 00:00:00
**Why it fails:** Answer cell corrupted to '2023-02-01 00:00:00' instead of 'February 2023'.
**Source:** https://en.wikipedia.org/wiki/Domenico_Tedesco
**Remedy:** Restore to 'February 2023'.

### Row 3459 — Belgium (medium) — FAIL: Excel date-corruption in answer
**Q:** When did Belgium's record 1,735-day reign as FIFA's top-ranked team end?
**Answer:** 2022-03-01 00:00:00
**Why it fails:** Answer cell corrupted to '2022-03-01 00:00:00' instead of 'March 2022'.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Restore to 'March 2022'.

### Row 3468 — Belgium (medium) — FAIL: wrong year (first #1 was 2015)
**Q:** When did the Belgian national team first reach FIFA's number 1 ranking?
**Answer:** 2018
**Why it fails:** Belgium FIRST reached FIFA #1 in November 2015 (under Wilmots), not 2018. 2018 was the start of their longest unbroken run at the top, but their first-ever #1 was 2015. The correct year (2015) is not among the options.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Change the answer to 2015 (or reword to 'began their record run', which would be 2018).

### Row 3474 — Belgium (medium) — FAIL: Excel date-corruption in answer
**Q:** When was Domenico Tedesco appointed as Belgium's manager?
**Answer:** 2023-02-01 00:00:00
**Why it fails:** Answer cell corrupted to '2023-02-01 00:00:00' instead of 'February 2023'.
**Source:** https://en.wikipedia.org/wiki/Domenico_Tedesco
**Remedy:** Restore to 'February 2023'.

### Row 3495 — Belgium (easy) — FAIL: confused/contradictory premise
**Q:** Which 2014 World Cup quarter-final opponent did Belgium beat in 2018?
**Answer:** Brazil
**Why it fails:** Brazil was NOT Belgium's 2014 World Cup quarter-final opponent — Argentina was (Belgium lost 1-0). The question asks 'which 2014 QF opponent did Belgium beat in 2018', but the only 2014 QF opponent (Argentina, a listed option) was not beaten in 2018, while the intended answer (Brazil) was not a 2014 opponent. The premise is self-contradictory and traps a knowledgeable player into picking Argentina.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Reword like row 3305 ('Belgium lost to Argentina in 2014 but beat which team in 2018?').

### Row 3503 — Belgium (medium) — FAIL: wrong score in explanation (0-2, not 1-0)
**Q:** Which 2022 World Cup team eliminated Belgium in the group stage?
**Answer:** Morocco
**Why it fails:** Belgium lost to Morocco 0-2 at the 2022 World Cup (Sabiri 73', Aboukhlal 90+2'), not 1-0 as the explanation states. (Row 3502 correctly says 2-0.) Also, strictly, Belgium were only mathematically eliminated after the final-game 0-0 draw with Croatia, though the Morocco defeat was the decisive blow.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_F
**Remedy:** Fix the score to 0-2 (Belgium lost 2-0).

### Row 3511 — Belgium (easy) — FAIL: non-unique (Lukaku also fits)
**Q:** Which Belgian academy product debuted at the 2014 World Cup?
**Answer:** Kevin De Bruyne
**Why it fails:** Romelu Lukaku — an Anderlecht academy product (a Belgian academy) — also made his World Cup debut at the 2014 tournament (Belgium missed 2010). So both De Bruyne and Lukaku satisfy 'Belgian academy product who debuted at the 2014 World Cup'; the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Romelu_Lukaku
**Remedy:** Specify 'Genk academy product' (uniquely De Bruyne among the options) or remove Lukaku.

### Row 3517 — Belgium (easy) — FAIL: wrong debut year (2011, not 2013)
**Q:** Which Belgian attacker debuted for the national team in 2013?
**Answer:** Dries Mertens
**Why it fails:** Dries Mertens made his Belgium debut on 9 February 2011 (vs Finland), not 2013. The answer player (Mertens) is otherwise the intended one, but the stated debut year is wrong.
**Source:** https://en.wikipedia.org/wiki/Dries_Mertens
**Remedy:** Change the debut year to 2011.

### Row 3518 — Belgium (easy) — FAIL: wrong debut year (2011, not 2013)
**Q:** Which Belgian attacker debuted internationally in 2013?
**Answer:** Dries Mertens
**Why it fails:** Same error: Mertens debuted internationally in February 2011, not 2013.
**Source:** https://en.wikipedia.org/wiki/Dries_Mertens
**Remedy:** Change the debut year to 2011.

### Row 3519 — Belgium (easy) — FAIL: non-unique (multiple at 2018 & 2022)
**Q:** Which Belgian attacker featured at the 2018 and 2022 FIFA World Cups?
**Answer:** Yannick Carrasco
**Why it fails:** Both Carrasco AND Mertens (and wing-back Meunier) featured at BOTH the 2018 and 2022 World Cups. Several options satisfy 'attacker at 2018 and 2022'; the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Add a distinguishing detail so only one option fits.

### Row 3520 — Belgium (easy) — FAIL: non-unique (Carrasco & Mertens)
**Q:** Which Belgian attacker played at both Euro 2016 and the 2022 World Cup?
**Answer:** Yannick Carrasco
**Why it fails:** Both Carrasco and Mertens played at Euro 2016 AND the 2022 World Cup, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Constrain to a uniquely-identifying player detail.

### Row 3521 — Belgium (easy) — FAIL: non-unique (all four fit)
**Q:** Which Belgian attacker played at Euro 2016, 2020, and 2022?
**Answer:** Dries Mertens
**Why it fails:** Mertens, Hazard, Lukaku AND Carrasco all played at Euro 2016, Euro 2020 and the 2022 World Cup. Every listed option satisfies the criteria, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Replace the distractors with players who did NOT feature in all three tournaments.

### Row 3522 — Belgium (easy) — FAIL: non-unique (Carrasco & Mertens at 2018)
**Q:** Which Belgian attacker played at the 2018 FIFA World Cup in Russia?
**Answer:** Yannick Carrasco
**Why it fails:** Both Carrasco and Mertens were in Belgium's 2018 World Cup squad, so 'attacker who played at the 2018 World Cup' is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Add a distinguishing detail or change the distractors.

### Row 3527 — Belgium (easy) — FAIL: wrong retirement year (2022, not 2024)
**Q:** Which Belgian attacker retired from international football in 2024 after 126 caps?
**Answer:** Eden Hazard
**Why it fails:** Hazard retired from international football on 7 December 2022 (right after the 2022 World Cup), not 2024 — he never played for Belgium in 2024. (The 126-cap figure is correct.) The 'retired in 2024' claim is false.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Change the retirement year to 2022.

### Row 3528 — Belgium (easy) — FAIL: false (retired before, not after, Euro 2024)
**Q:** Which Belgian attacker retired internationally after Euro 2024?
**Answer:** Eden Hazard
**Why it fails:** Hazard retired internationally in December 2022 — BEFORE Euro 2024, not after. He was not in the Euro 2024 squad and never played in 2024.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Reword: he retired after the 2022 World Cup, before Euro 2024.

### Row 3529 — Belgium (easy) — FAIL: false (retired Dec 2022, not after 2024 Euros)
**Q:** Which Belgian attacker retired internationally after the 2024 Euros with 126 caps?
**Answer:** Eden Hazard
**Why it fails:** Hazard retired internationally on 7 December 2022, after the 2022 World Cup — not 'after the 2024 Euros'. (126 caps is correct.)
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Change to 'after the 2022 World Cup'.

### Row 3530 — Belgium (easy) — FAIL: wrong match (Mertens scored vs Panama, not Tunisia)
**Q:** Which Belgian attacker scored against Tunisia at the 2018 World Cup?
**Answer:** Dries Mertens
**Why it fails:** Dries Mertens did not score against Tunisia at the 2018 World Cup. The 5-2 win over Tunisia was scored by Eden Hazard (2), Lukaku (2) and Batshuayi. Mertens scored in the OTHER group game, the 3-0 win over Panama (his 47'-minute opener).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_G
**Remedy:** Change the opponent to Panama (or pick an actual Tunisia scorer: Hazard/Lukaku/Batshuayi).

### Row 3532 — Belgium (easy) — FAIL: non-unique (Hazard also fits)
**Q:** Which Belgian attacker was a key offensive contributor from 2013 to 2022?
**Answer:** Dries Mertens
**Why it fails:** Eden Hazard (a listed option) was at least as much a 'key offensive contributor from 2013 to 2022' as Mertens. The trait is not unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Use a uniquely-identifying detail or drop Hazard as a distractor.

### Row 3535 — Belgium (easy) — FAIL: non-unique (Hazard, Mertens, Carrasco all in 2018)
**Q:** Which Belgian attacker was in their 2018 World Cup squad?
**Answer:** Eden Hazard
**Why it fails:** Three of the four options — Hazard, Mertens and Carrasco — were all in Belgium's 2018 World Cup squad. Mere squad membership is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Only Doku (not in 2018) is uniquely separable; reword to a distinguishing trait.

### Row 3538 — Belgium (medium) — FAIL: non-unique (Hazard also scored in 2018 group stage)
**Q:** Which Belgian attacker, not Lukaku, scored in the 2018 World Cup group stage?
**Answer:** Dries Mertens
**Why it fails:** 'Belgian attacker (not Lukaku) who scored in the 2018 group stage' is non-unique: Eden Hazard (a listed option) scored twice against Tunisia in the group stage, as well as Mertens (vs Panana). Multiple options fit.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_G
**Remedy:** Pin to a specific match/goal so only one option qualifies.

### Row 3540 — Belgium (easy) — FAIL: wrong retirement year (2022, not 2024)
**Q:** Which Belgian attacker, with 126 caps, retired in 2024?
**Answer:** Eden Hazard
**Why it fails:** Hazard (126 caps) retired internationally in December 2022, not 2024.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Change the retirement year to 2022.

### Row 3541 — Belgium (easy) — FAIL: non-unique (Lukaku also overlapped)
**Q:** Which Belgian attacker's key international era overlapped with Dries Mertens' from 2013 to 2022?
**Answer:** Eden Hazard
**Why it fails:** Romelu Lukaku (Belgium 2010-present) also overlapped Dries Mertens' 2013-2022 era, so 'whose era overlapped Mertens' is non-unique between Hazard and Lukaku.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Drop Lukaku as a distractor or add a distinguishing detail.

### Row 3543 — Belgium (medium) — FAIL: non-unique (Lukaku/Hazard also nominees at 2022)
**Q:** Which Belgian Ballon d'Or nominee played at the 2022 FIFA World Cup?
**Answer:** Kevin De Bruyne
**Why it fails:** 'Belgian Ballon d'Or nominee who played at the 2022 World Cup' is non-unique — De Bruyne, Romelu Lukaku and Eden Hazard were all Ballon d'Or shortlisted players and all played at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Make the distinction specific (e.g. a Ballon d'Or podium finish).

### Row 3550 — Belgium (easy) — FAIL: false (Openda was at Lens, not Union SG)
**Q:** Which Belgian club had a player debut for Belgium's 2022 FIFA World Cup squad?
**Answer:** Union Saint-Gilloise
**Why it fails:** The explanation claims Openda debuted for Belgium at the 2022 World Cup 'while playing for Union Saint-Gilloise' — false. Openda was a Lens player by the 2022 World Cup (signed from Club Brugge in July 2022) and never played for Union SG. No Union Saint-Gilloise player was in Belgium's 2022 squad, so the premise is false.
**Source:** https://en.wikipedia.org/wiki/Lo%C3%AFs_Openda
**Remedy:** Remove the Union SG claim; Openda was at Lens at the 2022 World Cup.

### Row 3565 — Belgium (easy) — FAIL: false premise (no 2010 WC debut)
**Q:** Which Belgian club's academy produced Kevin De Bruyne's 2010 World Cup debut?
**Answer:** Genk
**Why it fails:** De Bruyne did NOT make a '2010 World Cup debut' — Belgium failed to qualify for the 2010 World Cup, and De Bruyne's actual World Cup debut was 2014. The Genk-academy answer is right, but the '2010 World Cup debut' premise is fabricated.
**Source:** https://en.wikipedia.org/wiki/Kevin_De_Bruyne
**Remedy:** Change '2010' to '2014' (De Bruyne's real World Cup debut).

### Row 3575 — Belgium (medium) — FAIL: wrong match for 100th cap
**Q:** Which Belgian defender earned his 100th cap in a 2018 World Cup group stage win over England?
**Answer:** Jan Vertonghen
**Why it fails:** Vertonghen earned his 100th cap on 2 June 2018 against Portugal (a pre-tournament friendly), 11 years to the day after his debut — NOT in the 2018 World Cup group win over England (28 June 2018), by which point he was already past 100.
**Source:** https://en.wikipedia.org/wiki/Jan_Vertonghen
**Remedy:** Change the milestone match to the 2 June 2018 friendly vs Portugal.

### Row 3576 — Belgium (easy) — FAIL: wrong timing (had ~140 at 2022)
**Q:** Which Belgian defender earned his 150th cap at the 2022 World Cup?
**Answer:** Jan Vertonghen
**Why it fails:** Vertonghen did NOT earn his 150th cap at the 2022 World Cup — he had roughly 140 caps then and only reached 150 in 2023. (He finished on 157.) The milestone is misplaced.
**Source:** https://en.wikipedia.org/wiki/Jan_Vertonghen
**Remedy:** Remove the false 150th-cap-at-2022 claim.

### Row 3577 — Belgium (easy) — FAIL: wrong timing (154th cap was 2024)
**Q:** Which Belgian defender earned his 154th cap before the 2022 World Cup?
**Answer:** Jan Vertonghen
**Why it fails:** Vertonghen did not have 154 caps before the 2022 World Cup — he had roughly 140 then and reached 154 only in 2024 (finishing on 157). The claim is chronologically false.
**Source:** https://en.wikipedia.org/wiki/Jan_Vertonghen
**Remedy:** Remove the false 154-caps-before-2022 claim.

### Row 3578 — Belgium (easy) — FAIL: wrong timing (record set 2017)
**Q:** Which Belgian defender earned his record cap at the 2022 World Cup?
**Answer:** Jan Vertonghen
**Why it fails:** Vertonghen did not earn his 'record cap' at the 2022 World Cup — he broke Belgium's appearance record back on 10 October 2017 (97th cap). He was already the record-holder for five years before Qatar.
**Source:** https://en.wikipedia.org/wiki/Jan_Vertonghen
**Remedy:** Move the record-breaking milestone to October 2017.

### Row 3581 — Belgium (easy) — FAIL: non-unique (Vertonghen also >120)
**Q:** Which Belgian defender had over 120 caps at the 2022 World Cup?
**Answer:** Toby Alderweireld
**Why it fails:** Both Alderweireld AND Vertonghen (a listed option) had well over 120 caps by the 2022 World Cup (Vertonghen ~140, Alderweireld ~124). The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Add a distinguishing detail or drop Vertonghen as a distractor.

### Row 3582 — Belgium (easy) — FAIL: non-unique (Vertonghen also >120)
**Q:** Which Belgian defender had over 120 caps by the 2022 World Cup?
**Answer:** Toby Alderweireld
**Why it fails:** Same defect: both Alderweireld and Vertonghen had over 120 caps by the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Make the criterion uniquely identifying.

### Row 3584 — Belgium (easy) — FAIL: non-unique (all retired before 2026)
**Q:** Which Belgian defender retired before the 2026 World Cup cycle?
**Answer:** Jan Vertonghen
**Why it fails:** All four options retired before the 2026 World Cup cycle: Kompany (2019), Vermaelen (2022), Alderweireld (2024) and Vertonghen (2024). The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Reword (e.g. 'most-capped defender to retire') so only one option fits.

### Row 3589 — Belgium (easy) — FAIL: non-unique (duplicate body)
**Q:** Which Belgian football body organized the 2018 World Cup qualifiers from Brussels?
**Answer:** Belgian Football Association
**Why it fails:** 'Belgian Football Association' and 'Royal Belgian FA' are the SAME organisation (the RBFA — Royal Belgian Football Association). Two options name the identical body, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Royal_Belgian_Football_Association
**Remedy:** Replace the duplicate with a genuinely different organisation.

### Row 3596 — Belgium (easy) — FAIL: false premise (no Belgium-Netherlands game at 2022)
**Q:** Which Belgian goalkeeper started against the Netherlands in the 2022 World Cup?
**Answer:** Thibaut Courtois
**Why it fails:** Belgium did not play the Netherlands at the 2022 World Cup. Belgium were in Group F (Morocco, Croatia, Canada) and exited in the group stage; the Netherlands were in Group A. The match never happened.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_F
**Remedy:** Remove the question or change the opponent to an actual 2022 Belgium opponent (Canada/Morocco/Croatia).

### Row 3608 — Belgium (easy) — FAIL: non-unique (Courtois also Genk debut)
**Q:** Which Belgian Golden Generation star debuted for Genk before the 2014 World Cup?
**Answer:** Kevin De Bruyne
**Why it fails:** Both De Bruyne AND Thibaut Courtois (a listed option) made their senior professional debuts at Genk before the 2014 World Cup. The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Thibaut_Courtois
**Remedy:** Drop Courtois as a distractor or add a distinguishing detail.

### Row 3609 — Belgium (easy) — FAIL: non-unique (all four played 2018)
**Q:** Which Belgian Golden Generation star played at the 2018 FIFA World Cup?
**Answer:** Kevin De Bruyne
**Why it fails:** De Bruyne, Hazard, Lukaku AND Vertonghen all played at the 2018 World Cup. Every listed option fits, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Reword to a uniquely-identifying trait.

### Row 3610 — Belgium (medium) — FAIL: false (Lukaku didn't score vs England)
**Q:** Which Belgian Golden Generation star scored in their 2018 World Cup group stage win over England?
**Answer:** Romelu Lukaku
**Why it fails:** Lukaku did not score against England at the 2018 World Cup. The group-stage win was 1-0 (Adnan Januzaj's goal), not 2-0; the 2-0 result was the THIRD-PLACE play-off (Meunier and Hazard scored). Lukaku scored in neither.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_G
**Remedy:** Re-attribute to Januzaj (group, 1-0) or Meunier/Hazard (3rd place, 2-0).

### Row 3618 — Belgium (medium) — FAIL: wrong manager (Garcia, not Tedesco)
**Q:** Which Belgian manager led qualification for the 2026 FIFA World Cup?
**Answer:** Tedesco
**Why it fails:** Belgium's 2026 World Cup qualifying campaign was led by Rudi Garcia, not Tedesco. Tedesco was sacked on 24 January 2025, before the campaign began (June 2025); Garcia took them through to qualification in November 2025. The correct manager (Garcia) is not even an option.
**Source:** https://www.espn.com/soccer/story/_/id/43543199/belgium-hire-rudi-garcia-new-coach-domenico-tedesco-exit
**Remedy:** Change the answer to Rudi Garcia.

### Row 3634 — Belgium (easy) — FAIL: wrong answer (DB had ~93, Witsel 100+)
**Q:** Which Belgian midfielder earned over 100 caps by 2022?
**Answer:** Kevin De Bruyne
**Why it fails:** De Bruyne did NOT have over 100 caps by 2022 — he earned his 100th cap on 5 June 2024 (he had ~93 at the 2022 World Cup). The listed option Axel Witsel DID have 100+ caps by 2022 (his 100th came in November 2018, ~130 by Qatar). So the answer should be Witsel.
**Source:** https://en.wikipedia.org/wiki/Kevin_De_Bruyne
**Remedy:** Change the answer to Axel Witsel.

### Row 3647 — Belgium (easy) — FAIL: non-unique (Witsel/Chadli also 2014 debut)
**Q:** Which Belgian midfielder made his World Cup debut in 2014?
**Answer:** Kevin De Bruyne
**Why it fails:** Several midfielders made their World Cup debut at the 2014 tournament (Belgium's first since 2002): De Bruyne, Axel Witsel AND Nacer Chadli (all listed options). The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Pin to a uniquely-identifying detail or change the distractors.

### Row 3648 — Belgium (easy) — FAIL: non-unique (De Bruyne also 2014/18/22)
**Q:** Which Belgian midfielder played key roles at the 2014, 2018, and 2022 World Cups?
**Answer:** Axel Witsel
**Why it fails:** Both Witsel AND De Bruyne (a listed option) played key roles at the 2014, 2018 and 2022 World Cups. The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Add a distinguishing detail or drop De Bruyne as a distractor.

### Row 3649 — Belgium (easy) — FAIL: wrong answer (DB hit 100 in 2024)
**Q:** Which Belgian midfielder reached 100 caps before the 2022 World Cup?
**Answer:** Kevin De Bruyne
**Why it fails:** De Bruyne did not reach 100 caps before the 2022 World Cup — his 100th cap was 5 June 2024. The listed option Axel Witsel reached 100 caps in November 2018, so he is the midfielder who had 100+ caps before 2022.
**Source:** https://en.wikipedia.org/wiki/Kevin_De_Bruyne
**Remedy:** Change the answer to Axel Witsel.

### Row 3652 — Belgium (easy) — FAIL: non-unique (De Bruyne also started both)
**Q:** Which Belgian midfielder started in both the 2018 Russia and 2022 Qatar World Cups?
**Answer:** Axel Witsel
**Why it fails:** Both Witsel AND De Bruyne (a listed option) are midfielders who started at both the 2018 and 2022 World Cups. The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Drop De Bruyne as a distractor or add a distinguishing detail.

### Row 3653 — Belgium (easy) — FAIL: non-unique (De Bruyne also started vs Canada)
**Q:** Which Belgian midfielder started the 2022 World Cup rivalry match vs Canada?
**Answer:** Amadou Onana
**Why it fails:** Several midfielders started Belgium's 2022 opener against Canada, including De Bruyne (a listed option), not just Onana. The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_F
**Remedy:** Use the 'new generation' framing only, or change the distractors.

### Row 3662 — Belgium (easy) — FAIL: false (Witsel was rested vs England)
**Q:** Which Belgian midfielder with over 130 caps started in their 2018 World Cup group win over England?
**Answer:** Axel Witsel
**Why it fails:** Witsel did NOT start Belgium's 1-0 group win over England at the 2018 World Cup — Martínez made nine changes and rested his first-choice players; the XI was Vermaelen, Boyata, Dendoncker, Fellaini, Tielemans, T. Hazard, Dembélé, Januzaj, Chadli, Batshuayi (plus the keeper). The 130-cap detail identifies Witsel, but he did not start that match.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_G
**Remedy:** Change the match (Witsel started other 2018 games) or the premise.

### Row 3671 — Belgium (medium) — FAIL: false premise (no Belgium-France 2022 group game)
**Q:** Which Belgian next-gen attacker faced France in the 2022 World Cup group stage?
**Answer:** Jérémy Doku
**Why it fails:** Belgium did not face France in the 2022 World Cup group stage. Belgium were in Group F (Morocco, Croatia, Canada); France were in Group D. The match never happened.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_F
**Remedy:** Change the opponent to an actual 2022 Belgium group opponent.

### Row 3672 — Belgium (easy) — FAIL: false (Doku debuted 2020) / non-unique
**Q:** Which Belgian next-generation attacker debuted for the 2026 World Cup cycle?
**Answer:** Jérémy Doku
**Why it fails:** Doku did not 'debut for the 2026 World Cup cycle' — he debuted for Belgium in 2020 and played at the 2022 World Cup. Also, 'next-generation attacker' is non-unique among Doku, Openda and Onana.
**Source:** https://en.wikipedia.org/wiki/J%C3%A9r%C3%A9my_Doku
**Remedy:** Fix the debut framing (2020) and pin a uniquely-identifying detail.

### Row 3680 — Belgium (medium) — FAIL: non-unique (generic Ballon d'Or trait)
**Q:** Which Belgian player had Ballon d'Or nominations during the 2022 World Cup cycle?
**Answer:** Kevin De Bruyne
**Why it fails:** 'Belgian player with Ballon d'Or nominations during the 2022 cycle' is non-unique — De Bruyne, Lukaku and Hazard were all Ballon d'Or shortlisted around that period.
**Source:** https://en.wikipedia.org/wiki/Kevin_De_Bruyne
**Remedy:** Make the criterion specific (e.g. a podium finish).

### Row 3681 — Belgium (easy) — FAIL: false (Lukaku tied Ronaldo at 4)
**Q:** Which Belgian player had more 2018 World Cup goals than Portugal's Cristiano Ronaldo?
**Answer:** Romelu Lukaku
**Why it fails:** Lukaku did NOT score MORE 2018 World Cup goals than Ronaldo — both scored exactly 4 (the explanation itself says '4 ... while Ronaldo scored 4'). No Belgian outscored Ronaldo's 4 in 2018, so the premise is false/self-contradictory.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Reword to 'equalled' or pick a year/comparison where a Belgian genuinely scored more.

### Row 3684 — Belgium (easy) — FAIL: wrong number (four, not three)
**Q:** Which Belgian player had won Chelsea Player of the Year three times before his 2019 transfer?
**Answer:** Eden Hazard
**Why it fails:** Hazard won the Chelsea Player of the Year award four times (2014, 2015, 2017 and 2019), and the 2019 award preceded his June-2019 Real Madrid transfer. So 'three times before his 2019 transfer' undercounts — it was four.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Change 'three times' to 'four times'.

### Row 3685 — Belgium (medium) — FAIL: non-unique (generic Ballon d'Or trait)
**Q:** Which Belgian player has earned multiple Ballon d'Or nominations?
**Answer:** Kevin De Bruyne
**Why it fails:** 'Belgian player with multiple Ballon d'Or nominations' is non-unique — De Bruyne, Lukaku and Hazard all qualify.
**Source:** https://en.wikipedia.org/wiki/Kevin_De_Bruyne
**Remedy:** Make the criterion specific so only one option fits.

### Row 3696 — Belgium (medium) — FAIL: non-unique (generic Ballon d'Or trait)
**Q:** Which Belgian player received multiple Ballon d'Or nominations before the 2022 FIFA World Cup?
**Answer:** Kevin De Bruyne
**Why it fails:** 'Multiple Ballon d'Or nominations before the 2022 World Cup' is non-unique — De Bruyne, Lukaku and Hazard all qualify.
**Source:** https://en.wikipedia.org/wiki/Kevin_De_Bruyne
**Remedy:** Make the criterion specific.

### Row 3698 — Belgium (easy) — FAIL: non-unique (many scored home qualifiers)
**Q:** Which Belgian player scored a 2018 World Cup qualifier goal at their exclusive home venue?
**Answer:** Romelu Lukaku
**Why it fails:** Many Belgians scored 2018 World Cup qualifier goals at the King Baudouin Stadium (Belgium scored 43 in that campaign) — De Bruyne, Hazard and Mertens (all listed options) as well as Lukaku. The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_H
**Remedy:** Pin to a specific match/goal so only one option fits.

### Row 3703 — Belgium (easy) — FAIL: non-unique (all four scored in 2018)
**Q:** Which Belgian player scored at the 2018 FIFA World Cup?
**Answer:** Romelu Lukaku
**Why it fails:** All four options scored at the 2018 World Cup: Lukaku (4), Hazard (3), De Bruyne (1 vs Brazil) and Vertonghen (1 vs Japan). 'Which Belgian player scored at the 2018 World Cup' is therefore non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Pin to a specific match/goal so only one option fits.

### Row 3705 — Belgium (easy) — FAIL: false (Origi didn't score vs Japan)
**Q:** Which Belgian player scored in the 2018 World Cup round of 16 against Japan?
**Answer:** Divock Origi
**Why it fails:** Origi did not score against Japan at the 2018 World Cup — the scorers were Vertonghen, Fellaini and Chadli. The listed option Nacer Chadli actually scored (the 90+4' winner), so the answer should be Chadli, not Origi.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_knockout_stage
**Remedy:** Change the answer to Chadli (or Vertonghen/Fellaini).

### Row 3706 — Belgium (easy) — FAIL: non-unique (Meunier & Hazard both scored)
**Q:** Which Belgian player scored in the 2018 World Cup third-place win over England?
**Answer:** Thomas Meunier
**Why it fails:** Both Meunier (4') and Eden Hazard (82', a listed option) scored in Belgium's 2-0 third-place win over England. 'Which player scored' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_knockout_stage
**Remedy:** Ask who scored FIRST (Meunier) to make it unique.

### Row 3716 — Belgium (easy) — FAIL: first goal was an own goal, not De Bruyne
**Q:** Which Belgian player scored their first goal against Brazil in 2018?
**Answer:** Kevin De Bruyne
**Why it fails:** Belgium's FIRST goal against Brazil (2018 QF) was a Fernandinho own goal (13'); De Bruyne scored Belgium's SECOND (31'). The question asks for 'their first goal' but the explanation itself says 'second goal' — an internal contradiction, and the actual first goal was the own goal.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_knockout_stage
**Remedy:** Reword to 'second goal' (De Bruyne) or 'first goal' (Fernandinho own goal).

### Row 3717 — Belgium (easy) — FAIL: wrong scorer (Lukaku scored the 2nd)
**Q:** Which Belgian player scored their second goal in the 2021 Nations League semi-final?
**Answer:** Yannick Carrasco
**Why it fails:** Carrasco scored Belgium's FIRST goal (37'); Romelu Lukaku scored the SECOND (40') to make it 2-0. So 'Carrasco scored their second goal to give them a 2-0 lead' is wrong — that was Lukaku (a listed option).
**Source:** https://www.skysports.com/football/belgium-vs-france/440156
**Remedy:** Change the answer to Lukaku for the second goal, or ask who scored first (Carrasco).

### Row 3720 — Belgium (medium) — FAIL: non-unique (generic Ballon d'Or trait)
**Q:** Which Belgian player was a Ballon d'Or nominee at the 2022 World Cup?
**Answer:** Kevin De Bruyne
**Why it fails:** 'Belgian Ballon d'Or nominee at the 2022 World Cup' is non-unique — De Bruyne, Lukaku, Hazard and Courtois (who won the 2022 Yashin Trophy) all qualify.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Make the criterion specific.

### Row 3726 — Belgium (easy) — FAIL: non-unique (all in the 2018 squad)
**Q:** Which Belgian player was in the squad for their 2-0 win over England in the 2018 World Cup?
**Answer:** Thomas Meunier
**Why it fails:** All four options (Meunier, Alderweireld, Mertens, Vertonghen) were in Belgium's 2018 World Cup squad and available for the third-place win over England. Mere squad membership is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Ask who SCORED (Meunier/Hazard) or another distinguishing detail.

### Row 3727 — Belgium (easy) — FAIL: non-unique (all in the 2015 squad)
**Q:** Which Belgian player was in the squad when they first reached FIFA #1 in 2015?
**Answer:** Kevin De Bruyne
**Why it fails:** De Bruyne, Vertonghen, Lukaku and Hazard were ALL Belgium regulars in the squad when they first topped the FIFA ranking in November 2015. The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Use a uniquely-identifying detail.

### Row 3729 — Belgium (easy) — FAIL: non-unique (generic Ballon d'Or trait)
**Q:** Which Belgian player was nominated for multiple Ballons d'Or?
**Answer:** Kevin De Bruyne
**Why it fails:** De Bruyne, Hazard and Lukaku were all nominated for multiple Ballons d'Or. Non-unique.
**Source:** https://en.wikipedia.org/wiki/Kevin_De_Bruyne
**Remedy:** Make the criterion specific.

### Row 3742 — Belgium (easy) — FAIL: wrong number (four Chelsea POTY, not three)
**Q:** Which Belgian player won Chelsea's Player of the Year award three times before his 2019 Real Madrid transfer?
**Answer:** Eden Hazard
**Why it fails:** Hazard won the Chelsea Player of the Year award four times (2014, 2015, 2017, 2019), with the 2019 award coming before his June-2019 Real Madrid transfer. 'Three times before his 2019 transfer' undercounts.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Change 'three times' to 'four times'.

### Row 3746 — Belgium (medium) — FAIL: false premise (De Bruyne didn't score at 2022)
**Q:** Which Belgian player, after scoring in the 2022 World Cup, has multiple Ballon d'Or nominations?
**Answer:** Kevin De Bruyne
**Why it fails:** De Bruyne did not score at the 2022 World Cup — Belgium scored only one goal in the entire tournament (Batshuayi vs Canada). None of the listed options scored at 2022, so 'after scoring in the 2022 World Cup' is a false premise. ('Multiple Ballon d'Or nominations' is also non-unique.)
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_F
**Remedy:** Remove the false 'scored in the 2022 World Cup' premise.

### Row 3749 — Belgium (easy) — FAIL: false (Origi didn't score vs Japan)
**Q:** Which Belgian player, besides Nacer Chadli, scored against Japan at the 2018 World Cup?
**Answer:** Divock Origi
**Why it fails:** Besides Chadli, the scorers against Japan (2018 R16) were Jan Vertonghen (69') and Marouane Fellaini (74') — NOT Divock Origi, who did not score. None of the listed options (Origi/Lukaku/Hazard/Mertens) scored in that match.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_knockout_stage
**Remedy:** Change the answer to Vertonghen or Fellaini.

### Row 3751 — Belgium (easy) — FAIL: non-unique (Lukaku also fits)
**Q:** Which Belgian player, developed in Belgium's youth system, debuted for his national team at the 2014 FIFA World Cup?
**Answer:** Kevin De Bruyne
**Why it fails:** Lukaku (Anderlecht academy, a Belgian youth system) also made his World Cup debut at the 2014 tournament. So both De Bruyne and Lukaku satisfy 'developed in Belgium's youth system, debuted at the 2014 World Cup'; non-unique.
**Source:** https://en.wikipedia.org/wiki/Romelu_Lukaku
**Remedy:** Specify the Genk academy (uniquely De Bruyne) or drop Lukaku.

### Row 3763 — Belgium (easy) — FAIL: false (no Lukaku disallowed goal vs France)
**Q:** Which Belgian player's missed chance led to their 2024 Euro loss to France?
**Answer:** Romelu Lukaku
**Why it fails:** In the Euro 2024 round-of-16 loss to France (1-0), Belgium were undone by Vertonghen's 85th-minute own goal; Lukaku managed just one shot and had NO goal disallowed in that match. Lukaku's VAR-disallowed goals came in the GROUP stage (notably vs Slovakia), not the France game.
**Source:** https://www.uefa.com/euro2024/news/028f-1b43f36e020a-5b72455ab74b-1000--france-1-0-belgium-own-goal-sends-les-bleus-into-quarter-f/
**Remedy:** Remove the false 'disallowed goal vs France' claim; the decisive moment was Vertonghen's own goal.

### Row 3772 — Belgium (easy) — FAIL: wrong scorers (Vertonghen & Fellaini)
**Q:** Which Belgian players scored before the 94th-minute winner against Japan in the 2018 World Cup?
**Answer:** De Bruyne and Lukaku
**Why it fails:** The two Belgian goals before Chadli's 90+4' winner vs Japan were scored by Jan Vertonghen (69') and Marouane Fellaini (74') — NOT De Bruyne and Lukaku. The correct pairing ('Fellaini and Vertonghen') is even a listed option.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_knockout_stage
**Remedy:** Change the answer to 'Fellaini and Vertonghen'.

### Row 3795 — Belgium (easy) — FAIL: false (Eurostadium was for Euro 2020, not 2024)
**Q:** Which Belgian stadium project for Euro 2024 faced significant delays?
**Answer:** Eurostadium
**Why it fails:** The Eurostadium was the proposed venue for UEFA Euro 2020, not Euro 2024. It was cancelled in January 2018. 'Eurostadium project for Euro 2024' is a false attribution.
**Source:** https://en.wikipedia.org/wiki/Eurostadium
**Remedy:** Change 'Euro 2024' to 'Euro 2020' (the tournament the Eurostadium was actually meant for).

### Row 3804 — Belgium (medium) — FAIL: non-unique (generic Ballon d'Or trait)
**Q:** Which Belgian star earned Ballon d'Or nods after the 2018 World Cup?
**Answer:** Kevin De Bruyne
**Why it fails:** De Bruyne, Lukaku and Hazard all earned Ballon d'Or nominations after 2018. Non-unique.
**Source:** https://en.wikipedia.org/wiki/Kevin_De_Bruyne
**Remedy:** Make the criterion specific.

### Row 3807 — Belgium (easy) — FAIL: non-unique (De Bruyne also Genk + 2014)
**Q:** Which Belgian star from Genk's academy debuted at the 2014 FIFA World Cup?
**Answer:** Thibaut Courtois
**Why it fails:** Both Courtois AND De Bruyne (a listed option) are Genk academy products who debuted at the 2014 World Cup. The very next row (3808) asks the same question with the answer 'De Bruyne', confirming the non-uniqueness.
**Source:** https://en.wikipedia.org/wiki/Thibaut_Courtois
**Remedy:** Add a distinguishing detail (e.g. position) so only one fits.

### Row 3808 — Belgium (easy) — FAIL: non-unique (Courtois also Genk + 2014)
**Q:** Which Belgian star from Genk's academy debuted at the 2014 World Cup?
**Answer:** Kevin De Bruyne
**Why it fails:** Both De Bruyne and Courtois (a listed option) are Genk academy products who debuted at the 2014 World Cup. Non-unique (row 3807 asks the same with the answer 'Courtois').
**Source:** https://en.wikipedia.org/wiki/Kevin_De_Bruyne
**Remedy:** Add a distinguishing detail so only one fits.

### Row 3809 — Belgium (easy) — FAIL: false (Courtois also debuted 2014)
**Q:** Which Belgian star from Genk's academy debuted first at a FIFA World Cup?
**Answer:** Kevin De Bruyne
**Why it fails:** The explanation claims 'Courtois and others debuted later' — false. Courtois was Belgium's starting keeper at the SAME 2014 World Cup, as was Alderweireld (a listed option). All debuted at 2014, so 'debuted first' has no unique answer.
**Source:** https://en.wikipedia.org/wiki/Thibaut_Courtois
**Remedy:** Remove the false claim that Courtois debuted later; all debuted at 2014.

### Row 3812 — Belgium (easy) — FAIL: non-unique (Courtois also Genk, started Euro 2016)
**Q:** Which Belgian star from Genk's academy started at Euro 2016?
**Answer:** Kevin De Bruyne
**Why it fails:** Both De Bruyne and Courtois (a listed option) are Genk academy products who started at Euro 2016. Non-unique.
**Source:** https://en.wikipedia.org/wiki/Thibaut_Courtois
**Remedy:** Add a distinguishing detail (position) so only one fits.

### Row 3816 — Belgium (medium) — FAIL: non-unique (generic Ballon d'Or trait)
**Q:** Which Belgian star has been nominated for the Ballon d'Or multiple times?
**Answer:** Kevin De Bruyne
**Why it fails:** De Bruyne, Hazard, Lukaku and Courtois (2022 Yashin winner) all have multiple Ballon d'Or shortlist appearances. Non-unique.
**Source:** https://en.wikipedia.org/wiki/Kevin_De_Bruyne
**Remedy:** Make the criterion specific.

### Row 3817 — Belgium (medium) — FAIL: non-unique (generic Ballon d'Or trait)
**Q:** Which Belgian star has earned multiple Ballon d'Or nominations?
**Answer:** Kevin De Bruyne
**Why it fails:** Same as 3816 — multiple options (De Bruyne, Hazard, Lukaku, Courtois) have multiple Ballon d'Or nominations.
**Source:** https://en.wikipedia.org/wiki/Kevin_De_Bruyne
**Remedy:** Make the criterion specific.

### Row 3819 — Belgium (easy) — FAIL: non-unique (all four started 2018 SF)
**Q:** Which Belgian star started the 2018 World Cup semi-final against France?
**Answer:** Kevin De Bruyne
**Why it fails:** De Bruyne, Lukaku, Vertonghen AND Hazard all started Belgium's 2018 World Cup semi-final against France. Every option fits; non-unique.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_knockout_stage
**Remedy:** Use a uniquely-identifying detail.

### Row 3821 — Belgium (medium) — FAIL: non-unique (all in the 2015 squad)
**Q:** Which Belgian star was in the squad when they first topped FIFA rankings in 2015?
**Answer:** Kevin De Bruyne
**Why it fails:** De Bruyne, Lukaku, Vertonghen and Hazard were all in the squad when Belgium first topped the ranking in November 2015. Non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Use a uniquely-identifying detail.

### Row 3822 — Belgium (easy) — FAIL: wrong number (four Chelsea POTY, not three)
**Q:** Which Belgian star won Chelsea Player of the Year three times before his 2019 Real Madrid move?
**Answer:** Eden Hazard
**Why it fails:** Hazard won the Chelsea Player of the Year four times (2014, 2015, 2017, 2019); the 2019 award preceded his June-2019 Real Madrid move. 'Three times before his 2019 move' undercounts.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Change 'three times' to 'four times'.

### Row 3828 — Belgium (easy) — FAIL: non-unique (all are Belgian)
**Q:** Which Belgian star's FA is based in Brussels, after his 2018 World Cup?
**Answer:** Eden Hazard
**Why it fails:** All four options are Belgian players, so all share the same federation (RBFA, based in Brussels). 'Which star's FA is based in Brussels' has no unique answer.
**Source:** https://en.wikipedia.org/wiki/Royal_Belgian_Football_Association
**Remedy:** Drop the question or reword to a genuinely distinguishing fact.

### Row 3830 — Belgium (easy) — FAIL: stale (Openda now plays in Italy, Juventus)
**Q:** Which Belgian striker for the 2026 World Cup cycle does NOT play in Italy?
**Answer:** Loïs Openda
**Why it fails:** As of 2025-26 Openda plays for Juventus — in Italy — so 'the striker who does NOT play in Italy' is no longer Openda (the explanation's 'RB Leipzig' is stale). Moreover, Mertens (Galatasaray, Turkey) and Batshuayi also do not play in Italy, so the question is non-unique regardless.
**Source:** https://en.wikipedia.org/wiki/Lo%C3%AFs_Openda
**Remedy:** Refresh club data; with Openda at Juventus the premise no longer holds.

### Row 3849 — Belgium (easy) — FAIL: non-unique (Hazard also fits)
**Q:** Which Belgian veteran retired before the 2026 cycle, having played at the 2018 World Cup?
**Answer:** Jan Vertonghen
**Why it fails:** Both Vertonghen AND Hazard (a listed option) retired before the 2026 cycle and played at the 2018 World Cup. Non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Add a distinguishing detail (e.g. the appearance record) so only one fits.

### Row 3850 — Belgium (easy) — FAIL: non-unique (all retired before 2026)
**Q:** Which Belgian veteran retired before the 2026 World Cup cycle?
**Answer:** Jan Vertonghen
**Why it fails:** All four options retired before the 2026 cycle: Vertonghen (2024), Hazard (2022), Kompany (2019), Alderweireld (2024). Non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Reword to a uniquely-identifying trait.

### Row 3868 — Belgium (medium) — FAIL: non-unique (2014/18/22 all group wins)
**Q:** Which Belgian World Cup qualifying campaign ended with a group win?
**Answer:** 2022 World Cup
**Why it fails:** Belgium won their UEFA qualifying group in 2014, 2018 AND 2022 — three of the four listed options ended with a group win. Non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Replace distractors with campaigns Belgium did NOT win their group.

### Row 3878 — Belgium (medium) — FAIL: false (Wilmots oversaw 2014 & 2016 quals)
**Q:** Which Belgium coach oversaw their four consecutive major tournament qualifications from 2014 to 2022?
**Answer:** Roberto Martínez
**Why it fails:** Martínez did NOT oversee all four qualifications from 2014 — he was appointed in August 2016, AFTER Euro 2016. The 2014 World Cup and 2016 Euro qualifying campaigns were run by Marc Wilmots; Martínez oversaw the 2018, 2020 and 2022 qualifications. The explanation wrongly credits him with the 2016 Euro qualifying too.
**Source:** https://en.wikipedia.org/wiki/Roberto_Mart%C3%ADnez
**Remedy:** Split the credit: Wilmots (2014, 2016), Martínez (2018, 2020, 2022).

### Row 3881 — Belgium (easy) — FAIL: wrong timing (150 caps in 2023, not 2022)
**Q:** Which Belgium defender reached 150 caps at the 2022 FIFA World Cup?
**Answer:** Jan Vertonghen
**Why it fails:** Vertonghen did NOT reach 150 caps at the 2022 World Cup — he had roughly 140 then and only passed 150 in 2023. The milestone is misplaced.
**Source:** https://en.wikipedia.org/wiki/Jan_Vertonghen
**Remedy:** Remove the false '150 caps at 2022' claim.

### Row 3938 — Belgium (easy) — FAIL: non-unique (Lukaku also Anderlecht + 2014)
**Q:** Which Belgium player from Anderlecht debuted at the 2014 FIFA World Cup?
**Answer:** Adnan Januzaj
**Why it fails:** Lukaku is also an Anderlecht academy product who debuted at the 2014 World Cup. So both Januzaj and Lukaku (a listed option) fit 'Belgium player from Anderlecht who debuted at the 2014 World Cup'; non-unique.
**Source:** https://en.wikipedia.org/wiki/Romelu_Lukaku
**Remedy:** Add a distinguishing detail so only one fits.

### Row 3943 — Belgium (easy) — FAIL: wrong debut (2016, away v Netherlands)
**Q:** Which Belgium player made his senior debut at the King Baudouin Stadium in 2018?
**Answer:** Youri Tielemans
**Why it fails:** Tielemans made his senior Belgium debut on 9 November 2016, AWAY against the Netherlands (1-1) — not in a 2018 friendly vs Saudi Arabia at the King Baudouin Stadium. Both the year and the venue are wrong.
**Source:** https://en.wikipedia.org/wiki/Youri_Tielemans
**Remedy:** Fix the debut to 9 November 2016 (vs Netherlands).

### Row 3945 — Belgium (easy) — FAIL: false (Lukaku quiet vs France; misses were vs Croatia)
**Q:** Which Belgium player missed a late one-on-one against France at Euro 2024?
**Answer:** Romelu Lukaku
**Why it fails:** In the Euro 2024 round-of-16 loss to France, Lukaku managed just one shot and two touches in the box, struggling to make his mark — there was no notable 'late one-on-one' miss. Lukaku's infamous missed sitters were against CROATIA at the 2022 World Cup, not France 2024.
**Source:** https://www.skysports.com/football/croatia-vs-belgium/report/463002
**Remedy:** Re-attribute the missed chances to the 2022 Croatia game, or remove the claim.

### Row 3952 — Belgium (easy) — FAIL: false (Origi didn't score vs Japan)
**Q:** Which Belgium player scored a goal against Japan at the 2018 World Cup?
**Answer:** Divock Origi
**Why it fails:** Origi did not score against Japan at the 2018 World Cup — the scorers were Vertonghen, Fellaini and Chadli. The listed option Nacer Chadli actually scored (the winner).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_knockout_stage
**Remedy:** Change the answer to Chadli (or Vertonghen/Fellaini).

### Row 3953 — Belgium (easy) — FAIL: non-unique (all four scored in 2018)
**Q:** Which Belgium player scored a goal at the 2018 FIFA World Cup?
**Answer:** Romelu Lukaku
**Why it fails:** Lukaku, De Bruyne, Hazard and Mertens all scored at the 2018 World Cup. Every option fits; non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Pin to a specific match/goal.

### Row 3954 — Belgium (easy) — FAIL: false (Origi didn't score in R16)
**Q:** Which Belgium player scored a goal in the 2018 World Cup round of 16?
**Answer:** Divock Origi
**Why it fails:** Origi did not score in Belgium's 2018 round-of-16 win over Japan; the scorers were Vertonghen, Fellaini and Chadli. The listed option Chadli actually scored.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_knockout_stage
**Remedy:** Change the answer to Chadli.

### Row 3955 — Belgium (medium) — FAIL: false (no Lukaku hat-trick vs Tunisia)
**Q:** Which Belgium player scored a hat-trick in a 2018 World Cup group stage match?
**Answer:** Romelu Lukaku
**Why it fails:** Lukaku did not score a hat-trick against Tunisia (or anywhere) at the 2018 World Cup — he scored TWO vs Tunisia (Hazard also scored two) and two vs Panama. No Belgian scored a hat-trick at 2018.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_G
**Remedy:** Remove the hat-trick claim (Lukaku scored 2 vs Tunisia).

### Row 3956 — Belgium (easy) — FAIL: false (no Lukaku hat-trick vs Panama)
**Q:** Which Belgium player scored a hat-trick to help reach their 9-goal 2018 World Cup total?
**Answer:** Romelu Lukaku
**Why it fails:** Lukaku scored TWO against Panama (Mertens got the other), not a hat-trick. (The '9-goal 2018 total' is also wrong — Belgium scored 16.)
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_G
**Remedy:** Remove the hat-trick claim; fix the goal total to 16.

### Row 3958 — Belgium (easy) — FAIL: explanation false (Origi didn't score)
**Q:** Which Belgium player scored in the 94th minute against Japan at the 2018 World Cup?
**Answer:** Nacer Chadli
**Why it fails:** The answer (Chadli, 90+4') is correct, but the explanation falsely says 'Divock Origi also scored earlier in that match' — Origi did not score; the earlier goals were Vertonghen (69') and Fellaini (74').
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_knockout_stage
**Remedy:** Fix the explanation: the earlier scorers were Vertonghen and Fellaini, not Origi.

### Row 3961 — Belgium (easy) — FAIL: false (Carrasco scored once, not twice)
**Q:** Which Belgium player scored twice before their 2021 Nations League loss?
**Answer:** Yannick Carrasco
**Why it fails:** Carrasco scored ONE of Belgium's two goals in the 2021 Nations League semi (37'); Lukaku scored the other (40'). 'Carrasco scored both goals' is wrong.
**Source:** https://www.skysports.com/football/belgium-vs-france/440156
**Remedy:** Carrasco and Lukaku scored one each; reword accordingly.

### Row 3963 — Belgium (medium) — FAIL: non-unique (generic Ballon d'Or trait)
**Q:** Which Belgium player was a Ballon d'Or nominee at the 2022 FIFA World Cup?
**Answer:** Kevin De Bruyne
**Why it fails:** De Bruyne, Courtois (2022 Yashin winner), Lukaku and Hazard were all Ballon d'Or shortlisted players who played at the 2022 World Cup. Non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Make the criterion specific.

### Row 3964 — Belgium (easy) — FAIL: non-unique (Alderweireld also key defender)
**Q:** Which Belgium player was a key defender during their 2018-2022 FIFA number 1 ranking?
**Answer:** Jan Vertonghen
**Why it fails:** Vertonghen and Alderweireld (a listed option) were BOTH key central defenders throughout Belgium's 2018-2022 reign at #1. Non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Add a distinguishing detail (e.g. most-capped) so only one fits.

### Row 3965 — Belgium (easy) — FAIL: non-unique (multiple key starters)
**Q:** Which Belgium player was a key starter during their 2018-2022 FIFA number 1 reign?
**Answer:** Jan Vertonghen
**Why it fails:** Vertonghen, Alderweireld AND Witsel (all listed options) were core starters throughout the 2018-2022 #1 reign. Non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Use a uniquely-identifying detail.

### Row 3967 — Belgium (medium) — FAIL: non-unique (Hazard nominated earlier)
**Q:** Which Belgium player was first nominated for the Ballon d'Or before the 2018 World Cup?
**Answer:** Kevin De Bruyne
**Why it fails:** Eden Hazard (a listed option) was nominated for the Ballon d'Or before 2018 too — in fact earlier than De Bruyne. So 'first nominated before the 2018 World Cup' is non-unique.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Pin a specific year/finish so only one option fits.

### Row 3970 — Belgium (easy) — FAIL: false (no red card vs Croatia)
**Q:** Which Belgium player was sent off in their 0-0 draw with Croatia at the 2022 World Cup?
**Answer:** Jan Vertonghen
**Why it fails:** There was no sending-off in Belgium's 0-0 draw with Croatia at the 2022 World Cup — nobody, least of all Vertonghen, was shown a red card. The notable Vertonghen moment was a VAR-overturned penalty (offside by millimetres). Lukaku missing four big chances is what defined the game.
**Source:** https://www.skysports.com/football/croatia-vs-belgium/report/463002
**Remedy:** Remove the false red-card claim.

### Row 3974 — Belgium (easy) — FAIL: wrong number (four Chelsea POTY, not three)
**Q:** Which Belgium player won Chelsea Player of the Year three times before his 2019 transfer?
**Answer:** Eden Hazard
**Why it fails:** Hazard won the Chelsea Player of the Year four times (2014, 2015, 2017, 2019); the 2019 award preceded his June-2019 transfer. 'Three times before his 2019 transfer' undercounts.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Change 'three times' to 'four times'.

### Row 3978 — Belgium (medium) — FAIL: non-unique (generic Ballon d'Or trait)
**Q:** Which Belgium player's Ballon d'Or nominations coincided with four straight qualifications?
**Answer:** Kevin De Bruyne
**Why it fails:** De Bruyne, Lukaku and Hazard all received Ballon d'Or nominations during Belgium's 2014-2022 run. Non-unique.
**Source:** https://en.wikipedia.org/wiki/Kevin_De_Bruyne
**Remedy:** Make the criterion specific.

### Row 4001 — Belgium (easy) — FAIL: wrong coach (Garcia, not Tedesco)
**Q:** Which coach led Belgium to qualify for the 2026 World Cup?
**Answer:** Domenico Tedesco
**Why it fails:** Belgium qualified for the 2026 World Cup under Rudi Garcia, not Tedesco. Tedesco was sacked on 24 January 2025, before the qualifying campaign began; Garcia led them to qualification in November 2025. Garcia is not even an option.
**Source:** https://www.espn.com/soccer/story/_/id/43543199/belgium-hire-rudi-garcia-new-coach-domenico-tedesco-exit
**Remedy:** Change the answer to Rudi Garcia.

### Row 4012 — Belgium (easy) — FAIL: Excel date-corruption in answer
**Q:** Which formation did Belgium use under Roberto Martínez at the 2018 World Cup?
**Answer:** 2003-04-03 00:00:00
**Why it fails:** The answer cell is corrupted to '2003-04-03 00:00:00' instead of the formation '3-4-3'. The correct value is not among the clean options (4-3-3/4-4-2/3-5-2).
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Restore the answer to '3-4-3' and add it as an option.

### Row 4017 — Belgium (easy) — FAIL: own goal (Vertonghen), not a Kolo Muani goal
**Q:** Which France player scored to beat Belgium in Euro 2024?
**Answer:** Randal Kolo Muani
**Why it fails:** France's winner in the Euro 2024 round of 16 is officially recorded as a Jan Vertonghen OWN GOAL (85') — Kolo Muani's shot deflected in off Vertonghen. No France player is credited with the goal, so 'Kolo Muani scored the only goal' is inaccurate.
**Source:** https://www.uefa.com/euro2024/news/028f-1b43f36e020a-5b72455ab74b-1000--france-1-0-belgium-own-goal-sends-les-bleus-into-quarter-f/
**Remedy:** Record it as a Vertonghen own goal (off a Kolo Muani shot).

### Row 4018 — Belgium (easy) — FAIL: false (Benzema scored once, not twice)
**Q:** Which France player scored twice to beat Belgium in 2021?
**Answer:** Karim Benzema
**Why it fails:** In France's 3-2 comeback (2021 Nations League semi), the scorers were Benzema (62'), Mbappé (69' pen) and Theo Hernández (90') — one goal each. Benzema did NOT score twice.
**Source:** https://www.skysports.com/football/belgium-vs-france/440156
**Remedy:** Benzema scored once; reword (France's goals came from three different scorers).

### Row 4031 — Belgium (medium) — FAIL: wrong coach (Garcia, not Tedesco)
**Q:** Which manager led Belgium's 2026 FIFA World Cup qualification?
**Answer:** Domenico Tedesco
**Why it fails:** Belgium's 2026 World Cup qualification was led by Rudi Garcia, not Tedesco (sacked Jan 2025). Garcia is not even an option.
**Source:** https://www.espn.com/soccer/story/_/id/43543199/belgium-hire-rudi-garcia-new-coach-domenico-tedesco-exit
**Remedy:** Change the answer to Rudi Garcia.

### Row 4032 — Belgium (medium) — FAIL: wrong coach (Garcia, not Tedesco)
**Q:** Which manager led Belgium's 2026 World Cup qualification, unlike their 2014 campaign?
**Answer:** Domenico Tedesco
**Why it fails:** Same as 4031 — the 2026 qualification was under Rudi Garcia, not Tedesco.
**Source:** https://www.espn.com/soccer/story/_/id/43543199/belgium-hire-rudi-garcia-new-coach-domenico-tedesco-exit
**Remedy:** Change the answer to Rudi Garcia.

### Row 4048 — Belgium (medium) — FAIL: non-unique (drew Croatia too)
**Q:** Which nation did Belgium fail to beat in the 2022 World Cup group stage?
**Answer:** Morocco
**Why it fails:** Belgium failed to beat TWO sides in the 2022 group: they lost to Morocco AND drew 0-0 with Croatia (a listed option). 'Which nation did Belgium fail to beat' is therefore non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_F
**Remedy:** Ask which nation BEAT Belgium (Morocco) to make it unique.

### Row 4053 — Belgium (easy) — FAIL: wrong nation (overtook Argentina, not Germany)
**Q:** Which nation did Belgium overtake to become FIFA's top-ranked team in 2015?
**Answer:** Germany
**Why it fails:** Belgium overtook ARGENTINA to reach #1 for the first time in November 2015 ('Belgium take number 1 from Argentina'), not Germany. Argentina retook the top in April 2016.
**Source:** https://www.espn.com/soccer/story/_/id/37438374/belgium-take-number-1-argentina
**Remedy:** Change the answer to Argentina.

### Row 4057 — Belgium (easy) — FAIL: non-unique (Wales & Italy both Euro QF)
**Q:** Which nation eliminated Belgium from a Euro quarter-final?
**Answer:** Italy
**Why it fails:** Belgium were eliminated from a Euro quarter-final TWICE: by Wales (Euro 2016) and by Italy (Euro 2020). Both are listed options, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify the year so only one nation fits.

### Row 4070 — Belgium (easy) — FAIL: broken (wrong total, self-referential)
**Q:** Which nation scored more goals than Belgium at the 2018 World Cup?
**Answer:** Belgium scored 9
**Why it fails:** Multiple defects: Belgium scored 16 at 2018 (not 9) and were the tournament's HIGHEST scorers, so no nation scored more than them; and the answer 'Belgium scored 9' is not a nation that outscored Belgium — it names Belgium itself. The premise is false and the answer self-referential.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_statistics
**Remedy:** Belgium top-scored with 16; drop the false 'a nation scored more' premise.

### Row 4073 — Belgium (easy) — FAIL: self-referential (answer is Belgium)
**Q:** Which nation, like Belgium, uses one stadium for all home World Cup qualifiers?
**Answer:** Belgium
**Why it fails:** The question asks 'which nation, LIKE Belgium, uses one stadium for all home qualifiers?' and answers 'Belgium' — the subject names itself. Circular.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Reword so the answer is a different nation (e.g. England/Wembley).

### Row 4078 — Belgium (easy) — FAIL: self-referential (answer is Belgium)
**Q:** Which nation's 2022 World Cup training centre was in Tubize, like Belgium's?
**Answer:** Belgium
**Why it fails:** Tubize IS Belgium's training centre, so 'which nation's centre was in Tubize, like Belgium's?' answered 'Belgium' is circular/self-referential.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Reword so the answer is a different nation, or drop the question.

### Row 4109 — Belgium (medium) — FAIL: non-unique (didn't draw 3 of them)
**Q:** Which team did Belgium NOT draw against in their 2022 World Cup group stage?
**Answer:** Morocco
**Why it fails:** Belgium drew only Croatia in the 2022 group; they did NOT draw Morocco (lost), Canada (won) — and didn't play Brazil. So 'which team did Belgium NOT draw' has three valid options, not one.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_F
**Remedy:** Ask which team they DID draw (Croatia) to make it unique.

### Row 4114 — Belgium (easy) — FAIL: wrong scorers (Vertonghen/Fellaini, not DB/Lukaku)
**Q:** Which two Belgium players scored in their 3-2 comeback win against Japan at the 2018 World Cup?
**Answer:** De Bruyne and Lukaku
**Why it fails:** De Bruyne and Lukaku did NOT score in the 3-2 comeback vs Japan. The three scorers were Vertonghen (69'), Fellaini (74') and Chadli (90+4'). The listed option 'Chadli and Fellaini' is an actually-correct pair.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_knockout_stage
**Remedy:** Change the answer to two actual scorers (e.g. 'Chadli and Fellaini' or 'Vertonghen and Fellaini').

### Row 4122 — Belgium (easy) — FAIL: three nations finished above, not two
**Q:** Which two UEFA nations finished above Belgium in their 2010 World Cup qualifying group?
**Answer:** Spain and Türkiye
**Why it fails:** Belgium finished FOURTH in their 2010 qualifying group, so THREE nations finished above them — Spain (1st), Bosnia & Herzegovina (2nd) and Türkiye (3rd). The answer 'Spain and Türkiye' omits Bosnia, who also finished above Belgium.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_5
**Remedy:** Either list all three (Spain, Bosnia, Türkiye) or reword; Belgium were 4th, not 3rd.

### Row 4148 — Belgium (hard) — FAIL: non-unique (also missed 2006)
**Q:** Which World Cup did Belgium's national team fail to qualify for?
**Answer:** 2010 FIFA World Cup
**Why it fails:** Belgium failed to qualify for BOTH the 2006 and 2010 World Cups, and both are listed options. The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Add a distinguishing detail (e.g. 'in South Africa') so only 2010 fits.

### Row 4150 — Belgium (medium) — FAIL: non-unique (also missed 2006)
**Q:** Which World Cup edition did Belgium fail to qualify for?
**Answer:** 2010 World Cup
**Why it fails:** Belgium missed both the 2006 and 2010 World Cups; both are listed options. Non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Add a distinguishing detail so only one fits.

### Row 4160 — Belgium (medium) — FAIL: non-unique (2014/18/22 all group wins)
**Q:** Which year did Belgium win their UEFA World Cup qualifying group?
**Answer:** 2022
**Why it fails:** Belgium won their UEFA World Cup qualifying group for 2014, 2018 AND 2022 — three of the four listed options. The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Add a distinguishing detail so only one campaign fits.

### Row 4166 — Belgium (easy) — FAIL: own goal (Vertonghen), not Kolo Muani
**Q:** Who scored France's goal in their Euro 2024 win over Belgium?
**Answer:** Randal Kolo Muani
**Why it fails:** France's Euro 2024 winner is officially a Jan Vertonghen own goal (85') — Kolo Muani's shot deflected in off Vertonghen. No France player is credited, so 'Kolo Muani scored France's goal' is inaccurate.
**Source:** https://www.uefa.com/euro2024/news/028f-1b43f36e020a-5b72455ab74b-1000--france-1-0-belgium-own-goal-sends-les-bleus-into-quarter-f/
**Remedy:** Record it as a Vertonghen own goal (off a Kolo Muani shot).

### Row 4170 — Belgium (medium) — FAIL: wrong coach (Garcia, not Tedesco)
**Q:** Who was Belgium's manager for their 2026 World Cup qualification?
**Answer:** Domenico Tedesco
**Why it fails:** Belgium's 2026 World Cup qualification was led by Rudi Garcia, not Tedesco (sacked Jan 2025). Garcia is not even an option.
**Source:** https://www.espn.com/soccer/story/_/id/43543199/belgium-hire-rudi-garcia-new-coach-domenico-tedesco-exit
**Remedy:** Change the answer to Rudi Garcia.

### Row 4172 — Belgium (medium) — FAIL: false (Brugge finished 2nd, not 1st)
**Q:** Why did Belgian club Brugge reach the 2022 Champions League knockout stages?
**Answer:** Won their group
**Why it fails:** Club Brugge did NOT win their 2022-23 Champions League group — they finished SECOND in Group B (11 points), behind group winners Porto (12), qualifying for the knockouts as runners-up.
**Source:** https://www.uefa.com/uefachampionsleague/match/2035707--club-brugge-vs-porto/standings/
**Remedy:** Change to 'finished second / qualified as runners-up'.

### Bosnia and Herzegovina fail clusters (rows 4192–5804) — 125 FAIL
- **Stadium error (biggest single cluster):** dozens of rows say the **Asim Ferhatović Hase / Koševo** Stadium (Sarajevo, ~34,500) hosted Bosnia's **2014 World Cup qualifiers** (incl. the 3-1 v Greece). They were actually at **Bilino Polje, Zenica (~15,292)** — the team's fortress. (The dataset even contradicts itself, with some rows correctly naming Bilino Polje.)
- **"Bosnia's first open-play WC goal = Džeko":** false — **Ibišević's** first-ever goal (vs Argentina) was itself open play and came first. Failed only where the gradeable claim is the unscoped "first open-play"; passed where scoped to the Iran match/Salvador.
- **Stale "only" facts (Bosnia qualified for 2026 under Barbarez):** "Sušić is the **only** coach to reach a WC" and "Džeko **retired** after 2022 qualifying" are now false (Barbarez led 2026; Džeko is the 2026 captain).
- **Euro 2012 play-off aggregate stated as 5-1** — it was **6-2** (failed where 5-1 is in the question stem; passed where only in the explanation).
- **False premises:** Bosnia "at Euro 2024 / at the 2022 WC" (they didn't qualify for either); "2014 qualifier vs Argentina/Portugal" (Argentina was a finals opponent; Portugal was never a 2014-qualifying opponent); "2014 qualifying play-off" (they qualified directly); faced **Croatia/Serbia in WC qualifiers** (they never did — the rival was Greece).
- **Wrong specifics:** Pjanić "110 caps **by 2014**" / "Serie A TOTY **before** 2014" (his TOTY came 2015-16+); Džeko "Bundesliga top scorer **2012-13**" (it was 2009-10; he was at Man City by 2012-13) and "**65 goals in WC qualifiers**" (that's his total internationals); Džeko "scored **twice** vs Iran" (once); Misimović "**not** in the 2014 squad" (he was); Hadžibegić "won the **2022-23 NL** promotion" (that was Petev); 5494 "**Portugal** won Bosnia's 2022 group" (it was **France**, Group D); Germany 7-0 / Misimović retirement details.
- **Non-unique answers:** "which player scored / played at 2014" (multiple options qualify); "which did Bosnia NOT face / finish behind" (2+ valid); "which UEFA nation topped their 2014 group" (all four did); 5639 "two nations above Bosnia in Euro 2020 Group J" (three did — Italy, Finland, Greece); Džeko's WC-qualifying-goals record / both-leagues distinctions shared.
- **Self-referential:** "which nation, like Bosnia, did X" answered **"Bosnia and Herzegovina"**.
- **Other:** Bosnia "scored a goal vs Nigeria" (Džeko's was disallowed; they scored 0); Misimović "retired in 2014" passed (correct — Aug 2014) after initial review.

---

## Bosnia and Herzegovina — rows 4192–5804 (liveness on QA_PASSED_b2.md rows) — 125 FAIL

### Row 4193 — Bosnia and Herzegovina (medium) — FAIL: false (Belgium peaked #1 in 2015, not 2013)
**Q:** After Bosnia and Herzegovina's 2014 World Cup qualifiers, which UEFA nation also peaked in FIFA ranking in 2013?
**Answer:** Belgium
**Why it fails:** Belgium's all-time FIFA ranking peak was #1 (first reached November 2015, again 2018), NOT 5th in 2013. So 'Belgium also peaked in 2013' is false; no listed nation clearly shares Bosnia's 2013 peak (13th, Aug 2013).
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Remove the false claim about Belgium's 2013 peak.

### Row 4204 — Bosnia and Herzegovina (easy) — FAIL: false (2020-21 NL was Italy/Netherlands/Poland)
**Q:** Against which 2020-21 Nations League A opponent did Bosnia and Herzegovina fail to win?
**Answer:** Portugal
**Why it fails:** Bosnia's 2020-21 Nations League A group (Group A1) was Italy, the Netherlands and Poland — NOT Portugal, France or Croatia. Bosnia finished bottom (0W 2D 4L) and were relegated. So 'failed to win against Portugal' is false; they never played Portugal in that campaign.
**Source:** https://en.wikipedia.org/wiki/2020%E2%80%9321_UEFA_Nations_League_A
**Remedy:** Replace Portugal with an actual 2020-21 NL opponent (Italy/Netherlands/Poland).

### Row 4231 — Bosnia and Herzegovina (easy) — FAIL: false (Ibisevic's goal was also open play)
**Q:** At the 2014 World Cup, which Bosnian player scored his nation's first open-play goal?
**Answer:** Edin DÅ¾eko
**Why it fails:** Ibišević's first-ever Bosnia World Cup goal (vs Argentina, 85') was scored in OPEN PLAY (he ran onto a through ball and finished), so it — not Džeko's vs Iran — was Bosnia's first open-play World Cup goal. The 'first open-play goal = Džeko' distinction is false.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Bosnia's first open-play (and first-ever) WC goal was Ibišević's vs Argentina.

### Row 4232 — Bosnia and Herzegovina (easy) — FAIL: false (Ibisevic's goal was also open play)
**Q:** At the 2014 World Cup, which Bosnian player scored the team's first open-play goal?
**Answer:** Edin DÅ¾eko
**Why it fails:** Same as 4231: Ibišević's goal vs Argentina was open play and came first, so Džeko's vs Iran was not Bosnia's 'first open-play' World Cup goal.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Bosnia's first open-play WC goal was Ibišević's vs Argentina.

### Row 4240 — Bosnia and Herzegovina (easy) — FAIL: false framing (NL match, not a WC qualifier)
**Q:** At the 2026 World Cup qualifiers, which team inflicted Bosnia's worst competitive loss in 2024?
**Answer:** Germany
**Why it fails:** The Germany 7-0 thrashing (16 Nov 2024, Freiburg) was a UEFA NATIONS LEAGUE match that relegated Bosnia — not a 2026 World Cup qualifier (those were played in 2025). The score/opponent are right but the 'at the 2026 World Cup qualifiers' framing is false.
**Source:** https://www.espn.com/soccer/match/_/gameId/699011/bosnia-and-herzegovina-germany
**Remedy:** Re-label as a Nations League match (Nov 2024), not a World Cup qualifier.

### Row 4258 — Bosnia and Herzegovina (easy) — FAIL: non-unique / wrong venue in explanation
**Q:** At which stadium did Bosnia and Herzegovina NOT play during the 2014 World Cup?
**Answer:** Estádio Nacional
**Why it fails:** Bosnia played Nigeria at the Arena Pantanal (Cuiabá), NOT Arena da Baixada. So Bosnia did not play at BOTH Estádio Nacional AND Arena da Baixada (two listed options) — the 'not played' answer is non-unique, and the explanation's 'Arena da Baixada vs Nigeria' is wrong.
**Source:** https://www.espn.com/soccer/match/_/gameId/383276/bosnia-and-herzegovina-nigeria
**Remedy:** Fix the Nigeria venue to Arena Pantanal; only one option should be a stadium Bosnia actually didn't play at.

### Row 4287 — Bosnia and Herzegovina (easy) — FAIL: false (Croatia joined FIFA in 1992, not 1996)
**Q:** Bosnia and Herzegovina's FIFA membership year matches which other UEFA nation's?
**Answer:** Croatia
**Why it fails:** Bosnia joined FIFA in 1996, but Croatia was re-admitted to FIFA on 3 July 1992 — so their membership years do NOT match. (Slovenia 1992, Montenegro 2007 also don't match 1996.) The answer 'Croatia' is wrong.
**Source:** https://en.wikipedia.org/wiki/Croatia_national_football_team
**Remedy:** None of the listed nations joined FIFA in 1996 with Bosnia; replace the options.

### Row 4310 — Bosnia and Herzegovina (hard) — FAIL: wrong year (first Serie A TOTY was 2015-16)
**Q:** During which Bosnia & Herzegovina World Cup campaign was Miralem PjaniÄ‡ first named to the Serie A Team of the Year?
**Answer:** 2014 World Cup
**Why it fails:** Pjanić was first named to the Serie A Team of the Year in 2015-16 (then 2016-17, 2017-18, 2018-19), NOT 2013-14. That falls in the 2018 World Cup cycle, not the 2014 one, so '2014 World Cup' is wrong.
**Source:** https://en.wikipedia.org/wiki/Miralem_Pjani%C4%87
**Remedy:** Change the answer to the 2018 World Cup cycle (his first Serie A TOTY was 2015-16).

### Row 4329 — Bosnia and Herzegovina (medium) — FAIL: stale (Bosnia have qualified for TWO WCs now)
**Q:** How many FIFA World Cups has Bosnia and Herzegovina qualified for as an independent nation?
**Answer:** One
**Why it fails:** Bosnia and Herzegovina have now qualified for TWO World Cups as an independent nation — 2014 AND 2026 (via the March 2026 play-offs, beating Italy on penalties). '2014 was their first and only' is no longer true; the answer should be 'Two'.
**Source:** https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/bosnia-herzegovina-qualify
**Remedy:** Update to 'Two' (2014 and 2026).

### Row 4330 — Bosnia and Herzegovina (medium) — FAIL: stale (Bosnia have qualified for TWO WCs now)
**Q:** How many FIFA World Cups has Bosnia and Herzegovina qualified for?
**Answer:** One
**Why it fails:** Bosnia qualified for the 2026 World Cup (beating Italy in the March 2026 play-off final), so they have qualified for TWO World Cups (2014 and 2026), not one.
**Source:** https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/bosnia-herzegovina-qualify
**Remedy:** Update to 'Two'.

### Row 4362 — Bosnia and Herzegovina (easy) — FAIL: wrong group (2026 was Group H, not J)
**Q:** In 2026 World Cup qualifying, which group did Bosnia and Herzegovina finish in?
**Answer:** Group J
**Why it fails:** Bosnia's 2026 World Cup qualifying group was Group H (Austria, Bosnia, Romania, Cyprus, San Marino), where they finished 2nd behind Austria. Group J was their EURO 2024/2020 qualifying group, not the 2026 WC group.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_H
**Remedy:** Change the answer to Group H.

### Row 4382 — Bosnia and Herzegovina (easy) — FAIL: wrong minute (68th, not 78th)
**Q:** In Bosnia's 2014 World Cup qualifier, which minute did Vedad IbiÅ¡eviÄ‡ score the winner?
**Answer:** 78th minute
**Why it fails:** Ibišević scored the winner that sent Bosnia to their first World Cup in the 68th minute (not 78th) of the 1-0 win away to Lithuania in Kaunas on 15 October 2013 (Džeko assist).
**Source:** https://www.si.com/soccer/2013/10/15/bosnia-herzegovina-qualifies-first-world-cup
**Remedy:** Change the minute to 68th.

### Row 4392 — Bosnia and Herzegovina (easy) — FAIL: Excel date-corruption in answer
**Q:** In Bosnia's first World Cup win in 2014, what was their final score?
**Answer:** 2026-01-03 00:00:00
**Why it fails:** The answer cell is corrupted to '2026-01-03 00:00:00' instead of the scoreline 3-1 (Bosnia beat Iran 3-1). The correct score is not among the clean options (2-1/1-0/2-0).
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Restore the answer to 3-1 and add it as an option.

### Row 4403 — Bosnia and Herzegovina (easy) — FAIL: false (Bosnia BEAT Iran 3-1, did not draw)
**Q:** In the 2014 World Cup, which nation's draw with Bosnia and Herzegovina symbolized its post-war unity?
**Answer:** Iran
**Why it fails:** Bosnia did not DRAW with Iran at the 2014 World Cup — they BEAT Iran 3-1 (their first-ever World Cup win). The premise 'Iran's draw with Bosnia' is false.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** It was a 3-1 Bosnia win, not a draw.

### Row 4413 — Bosnia and Herzegovina (easy) — FAIL: Excel date-corruption in answer
**Q:** In their 2014 World Cup win, by what margin did Bosnia and Herzegovina defeat Iran?
**Answer:** 2026-01-03 00:00:00
**Why it fails:** The answer cell is corrupted to '2026-01-03 00:00:00' instead of the 3-1 margin (Bosnia beat Iran 3-1). The correct value is not among the clean options.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Restore the answer to 3-1.

### Row 4443 — Bosnia and Herzegovina (hard) — FAIL: Excel date-corruption in answer
**Q:** In which month of 2013 did Bosnia and Herzegovina reach their highest FIFA ranking?
**Answer:** 2013-08-01 00:00:00
**Why it fails:** The answer cell is the corrupted datetime '2013-08-01 00:00:00' instead of a clean 'August 2013'. (One distractor is also mojibake-corrupted.)
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_national_football_team
**Remedy:** Restore the answer to 'August 2013' and clean the options.

### Row 4446 — Bosnia and Herzegovina (easy) — FAIL: false premise (Portugal not in 2014 WC qualifying)
**Q:** In which stadium did Bosnia and Herzegovina host Portugal in a 2014 World Cup qualifier?
**Answer:** Bilino Polje
**Why it fails:** Portugal were NOT in Bosnia's 2014 World Cup qualifying group (Group G: Greece, Slovakia, Lithuania, Latvia, Liechtenstein). Bosnia faced Portugal in the 2010 WC play-off and the Euro 2012 play-off — not a 2014 WC qualifier. So 'hosted Portugal in a 2014 World Cup qualifier' never happened.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** Remove the false premise; Bosnia never hosted Portugal in a 2014 WC qualifier.

### Row 4449 — Bosnia and Herzegovina (medium) — FAIL: false (2012 was a EURO play-off, not a WC)
**Q:** In which two World Cup years did Bosnia and Herzegovina lose play-offs to Portugal?
**Answer:** 2010 and 2012
**Why it fails:** Only ONE of these was a World Cup play-off: 2010 (vs Portugal). The 2012 play-off loss to Portugal was for the EUROPEAN CHAMPIONSHIP (Euro 2012), not a World Cup. So 'two World Cup years' is wrong (also, the play-offs were played in 2009 and 2011).
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_national_football_team
**Remedy:** Only 2010 was a WC play-off vs Portugal; 2012 was a Euro play-off.

### Row 4473 — Bosnia and Herzegovina (medium) — FAIL: wrong year (Susic appointed Dec 2009)
**Q:** In which year did Bosnia and Herzegovina appoint a new manager for 2014 World Cup qualifying?
**Answer:** 2011
**Why it fails:** Safet Sušić was appointed Bosnia head coach on 28 December 2009 (succeeding Blažević), not 2011. He led the entire 2014 World Cup qualifying campaign from 2009.
**Source:** https://en.wikipedia.org/wiki/Safet_Su%C5%A1i%C4%87
**Remedy:** Change the appointment year to 2009.

### Row 4479 — Bosnia and Herzegovina (medium) — FAIL: false (2011 Kosevo match was a Euro 2012 play-off)
**Q:** In which year did Bosnia and Herzegovina host a key World Cup qualifier at Sarajevo's KoÅ¡evo Stadium?
**Answer:** 2011
**Why it fails:** The 2011 match Bosnia hosted Portugal at Koševo was a EURO 2012 qualifying play-off, NOT a World Cup qualifier — and there were no 2014 WC qualifiers in 2011 (they began in September 2012). The 'key World Cup qualifier' framing is false.
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_national_football_team
**Remedy:** Re-label as a Euro 2012 play-off, not a World Cup qualifier.

### Row 4497 — Bosnia and Herzegovina (medium) — FAIL: impossible (Argentina never a WC-qualifying foe)
**Q:** In which year did Bosnia host Argentina at KoÅ¡evo Stadium for a World Cup qualifier?
**Answer:** 2013
**Why it fails:** Bosnia (UEFA) and Argentina (CONMEBOL) are in different confederations and never meet in World Cup qualifying. Bosnia did not host Argentina at Koševo in a 2014 WC qualifier in 2013 — their only meeting was the 2014 World Cup group stage (in Brazil). The premise is impossible.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** Remove the false premise; Argentina was never a Bosnia WC-qualifying opponent.

### Row 4503 — Bosnia and Herzegovina (medium) — FAIL: wrong aggregate (6-2, not 5-1)
**Q:** In which year's Euro play-offs did Bosnia lose 5-1 to Portugal?
**Answer:** 2012
**Why it fails:** Portugal beat Bosnia 6-2 on aggregate in the Euro 2012 play-off (0-0 in Zenica, then 6-2 in Lisbon with a Ronaldo double), NOT 5-1.
**Source:** https://www.uefa.com/uefaeuro/match/2008831--portugal-vs-bosnia-and-herzegovina/
**Remedy:** Change the aggregate to 6-2.

### Row 4505 — Bosnia and Herzegovina (hard) — FAIL: date-corruption + wrong value (was 6-2)
**Q:** What aggregate score did Bosnia and Herzegovina lose by to Portugal in the Euro 2012 play-offs?
**Answer:** 2026-01-05 00:00:00
**Why it fails:** The answer cell is the corrupted datetime '2026-01-05 00:00:00'. The intended value (and the explanation's '5-1') is also wrong — Portugal beat Bosnia 6-2 on aggregate in the Euro 2012 play-off.
**Source:** https://www.uefa.com/uefaeuro/match/2008831--portugal-vs-bosnia-and-herzegovina/
**Remedy:** Restore a clean answer of 6-2 (not 5-1).

### Row 4515 — Bosnia and Herzegovina (hard) — FAIL: date-corruption + wrong value (was 6-2)
**Q:** What was Bosnia and Herzegovina's aggregate defeat to Portugal in the Euro 2012 play-offs?
**Answer:** 2026-01-05 00:00:00
**Why it fails:** Corrupted datetime answer '2026-01-05 00:00:00'; the explanation's '5-1' is also wrong (the Euro 2012 aggregate was 6-2).
**Source:** https://www.uefa.com/uefaeuro/match/2008831--portugal-vs-bosnia-and-herzegovina/
**Remedy:** Restore a clean answer of 6-2.

### Row 4517 — Bosnia and Herzegovina (easy) — FAIL: Excel date-corruption in answer
**Q:** What was Bosnia and Herzegovina's winning scoreline against Iran in their first-ever World Cup victory?
**Answer:** 2026-01-03 00:00:00
**Why it fails:** The answer cell is corrupted to '2026-01-03 00:00:00' instead of the 3-1 scoreline (Bosnia beat Iran 3-1).
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Restore the answer to 3-1.

### Row 4518 — Bosnia and Herzegovina (easy) — FAIL: Excel date-corruption in answer
**Q:** What was Bosnia and Herzegovina's winning scoreline in their first World Cup victory at the 2014 tournament?
**Answer:** 2026-01-03 00:00:00
**Why it fails:** Corrupted datetime '2026-01-03 00:00:00' instead of 3-1.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Restore the answer to 3-1.

### Row 4519 — Bosnia and Herzegovina (easy) — FAIL: Excel date-corruption in answer
**Q:** What was Bosnia and Herzegovina's winning scoreline vs Iran at the 2014 World Cup?
**Answer:** 2026-01-03 00:00:00
**Why it fails:** Corrupted datetime '2026-01-03 00:00:00' instead of 3-1.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Restore the answer to 3-1.

### Row 4520 — Bosnia and Herzegovina (hard) — FAIL: Excel date-corruption in answer
**Q:** What was Bosnia's aggregate defeat by the Republic of Ireland in the Euro 2016 play-offs?
**Answer:** 2026-01-03 00:00:00
**Why it fails:** Corrupted datetime '2026-01-03 00:00:00' instead of the 3-1 aggregate (Bosnia lost 1-3 to Ireland in the Euro 2016 play-off).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2016_qualifying_play-offs
**Remedy:** Restore the answer to 3-1.

### Row 4527 — Bosnia and Herzegovina (easy) — FAIL: Excel date-corruption in answer
**Q:** What was Bosnia's scoreline in their first World Cup win at Brazil 2014?
**Answer:** 2026-01-03 00:00:00
**Why it fails:** Corrupted datetime '2026-01-03 00:00:00' instead of 3-1 (Bosnia 3-1 Iran).
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Restore the answer to 3-1.

### Row 4529 — Bosnia and Herzegovina (hard) — FAIL: wrong aggregate (6-2, not 5-1)
**Q:** What was the aggregate score when Bosnia and Herzegovina lost to Portugal in the Euro 2012 play-offs?
**Answer:** 5-1 to Portugal
**Why it fails:** The Euro 2012 play-off aggregate was Portugal 6-2 Bosnia (0-0 then 6-2), not 5-1.
**Source:** https://www.uefa.com/uefaeuro/match/2008831--portugal-vs-bosnia-and-herzegovina/
**Remedy:** Change the aggregate to 6-2.

### Row 4532 — Bosnia and Herzegovina (hard) — FAIL: date-corruption + wrong value (was 6-2)
**Q:** What was the aggregate score when Bosnia lost to Portugal in the Euro 2012 play-offs?
**Answer:** 2026-01-05 00:00:00
**Why it fails:** Corrupted datetime answer; the explanation's '5-1' is also wrong (Euro 2012 aggregate was 6-2).
**Source:** https://www.uefa.com/uefaeuro/match/2008831--portugal-vs-bosnia-and-herzegovina/
**Remedy:** Restore a clean answer of 6-2.

### Row 4534 — Bosnia and Herzegovina (easy) — FAIL: Excel date-corruption in answer
**Q:** What was the final score in Bosnia and Herzegovina's first-ever World Cup victory in 2014?
**Answer:** 2026-01-03 00:00:00
**Why it fails:** The answer cell is corrupted to '2026-01-03 00:00:00' instead of the 3-1 scoreline (Bosnia beat Iran 3-1).
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Restore the answer to 3-1.

### Row 4538 — Bosnia and Herzegovina (easy) — FAIL: Excel date-corruption in answer
**Q:** What was the final score when Bosnia and Herzegovina beat Iran for their first World Cup win in 2014?
**Answer:** 2026-01-03 00:00:00
**Why it fails:** Corrupted datetime '2026-01-03 00:00:00' instead of 3-1 (Bosnia 3-1 Iran).
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Restore the answer to 3-1.

### Row 4546 — Bosnia and Herzegovina (easy) — FAIL: Excel date-corruption in answer
**Q:** What was the final score when Bosnia lost to Argentina at the 2014 World Cup?
**Answer:** 2026-01-02 00:00:00
**Why it fails:** Corrupted datetime '2026-01-02 00:00:00' instead of the 2-1 scoreline (Bosnia lost 2-1 to Argentina).
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Restore the answer to 2-1.

### Row 4548 — Bosnia and Herzegovina (medium) — FAIL: Excel date-corruption in answer
**Q:** What was the score when Bosnia and Herzegovina beat Iran at the 2014 World Cup?
**Answer:** 2026-01-03 00:00:00
**Why it fails:** Corrupted datetime '2026-01-03 00:00:00' instead of 3-1 (Bosnia 3-1 Iran).
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Restore the answer to 3-1.

### Row 4554 — Bosnia and Herzegovina (medium) — FAIL: Excel date-corruption in answer
**Q:** What was the score when Bosnia lost to Argentina in 2014?
**Answer:** 2026-01-02 00:00:00
**Why it fails:** Corrupted datetime '2026-01-02 00:00:00' instead of 2-1 (Bosnia lost 2-1 to Argentina).
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Restore the answer to 2-1.

### Row 4555 — Bosnia and Herzegovina (medium) — FAIL: Excel date-corruption in answer
**Q:** What was the score when Bosnia lost to Argentina in their 2014 World Cup opener?
**Answer:** 2026-01-02 00:00:00
**Why it fails:** Corrupted datetime '2026-01-02 00:00:00' instead of 2-1 (Bosnia lost 2-1 to Argentina).
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Restore the answer to 2-1.

### Row 4580 — Bosnia and Herzegovina (hard) — FAIL: Excel date-corruption in answer
**Q:** When did Bosnia and Herzegovina first reach their highest FIFA ranking after the war?
**Answer:** 2013-08-01 00:00:00
**Why it fails:** The answer cell is the corrupted datetime '2013-08-01 00:00:00' instead of a clean 'August 2013'.
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_national_football_team
**Remedy:** Restore the answer to 'August 2013'.

### Row 4587 — Bosnia and Herzegovina (hard) — FAIL: wrong aggregate (6-2, not 5-1)
**Q:** When did Bosnia and Herzegovina lose 5-1 on aggregate to Portugal in Euro play-offs?
**Answer:** 2012
**Why it fails:** The year (2012) is right, but the embedded '5-1 on aggregate' is wrong — Portugal beat Bosnia 6-2 on aggregate in the Euro 2012 play-off.
**Source:** https://www.uefa.com/uefaeuro/match/2008831--portugal-vs-bosnia-and-herzegovina/
**Remedy:** Fix the aggregate to 6-2.

### Row 4588 — Bosnia and Herzegovina (medium) — FAIL: Excel date-corruption in answer
**Q:** When did Bosnia and Herzegovina lose 7-0 to Germany in a UEFA Nations League match?
**Answer:** 2024-11-01 00:00:00
**Why it fails:** The answer cell is the corrupted datetime '2024-11-01 00:00:00' instead of a clean 'November 2024'.
**Source:** https://www.espn.com/soccer/match/_/gameId/699011/bosnia-and-herzegovina-germany
**Remedy:** Restore the answer to 'November 2024'.

### Row 4590 — Bosnia and Herzegovina (medium) — FAIL: Excel date-corruption in answer
**Q:** When did Bosnia and Herzegovina lose 7-0 to Germany?
**Answer:** 2024-11-01 00:00:00
**Why it fails:** Corrupted datetime '2024-11-01 00:00:00' instead of 'November 2024'.
**Source:** https://www.espn.com/soccer/match/_/gameId/699011/bosnia-and-herzegovina-germany
**Remedy:** Restore the answer to 'November 2024'.

### Row 4618 — Bosnia and Herzegovina (hard) — FAIL: Excel date-corruption in answer
**Q:** When did Bosnia and Herzegovina reach their peak FIFA ranking during 2014 World Cup qualification?
**Answer:** 2013-08-01 00:00:00
**Why it fails:** The answer cell is the corrupted datetime '2013-08-01 00:00:00' instead of 'August 2013'.
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_national_football_team
**Remedy:** Restore the answer to 'August 2013'.

### Row 4637 — Bosnia and Herzegovina (medium) — FAIL: Excel date-corruption in answer
**Q:** When did Bosnia and Herzegovina's fans celebrate in Sarajevo after qualifying for the 2014 World Cup?
**Answer:** 2013-10-01 00:00:00
**Why it fails:** The answer cell is the corrupted datetime '2013-10-01 00:00:00' instead of 'October 2013'.
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_national_football_team
**Remedy:** Restore the answer to 'October 2013'.

### Row 4659 — Bosnia and Herzegovina (hard) — FAIL: wrong aggregate (6-2, not 5-1)
**Q:** When did Bosnia lose 5-1 on aggregate to Portugal in Euro play-offs?
**Answer:** In 2012
**Why it fails:** The year (2012) is right, but '5-1 on aggregate' is wrong — Portugal beat Bosnia 6-2 on aggregate in the Euro 2012 play-off.
**Source:** https://www.uefa.com/uefaeuro/match/2008831--portugal-vs-bosnia-and-herzegovina/
**Remedy:** Fix the aggregate to 6-2.

### Row 4662 — Bosnia and Herzegovina (medium) — FAIL: wrong season (Dzeko top-scored 2009-10)
**Q:** When did Bosnia's Edin DÅ¾eko become the Bundesliga top scorer?
**Answer:** 2009
**Why it fails:** Džeko won the Bundesliga Torjägerkanone in the 2009-10 season (22 goals for Wolfsburg), NOT 2008-09 (when Grafite was top scorer). The explanation's '2008-09 season' is wrong.
**Source:** https://en.wikipedia.org/wiki/Edin_D%C5%BEeko
**Remedy:** Change the season to 2009-10.

### Row 4713 — Bosnia and Herzegovina (easy) — FAIL: false (Canada did not qualify for 2010 WC)
**Q:** Which 2014 Bosnia star also played for a nation that qualified for the 2010 World Cup?
**Answer:** Asmir BegoviÄ‡
**Why it fails:** Begović represented Canada at youth level, but Canada did NOT qualify for the 2010 World Cup — Canada had not reached a World Cup since 1986 (their next appearance was 2022). So 'a nation that qualified for the 2010 World Cup' is false for Begović (and for every 2014 Bosnia star).
**Source:** https://en.wikipedia.org/wiki/Canada_at_the_FIFA_World_Cup
**Remedy:** Remove the false premise; Canada were not at the 2010 World Cup.

### Row 4719 — Bosnia and Herzegovina (easy) — FAIL: non-unique (didn't beat Argentina OR Nigeria)
**Q:** Which 2014 World Cup opponent did Bosnia and Herzegovina NOT defeat in their group?
**Answer:** Argentina
**Why it fails:** Bosnia defeated only Iran in the 2014 group; they did NOT beat Argentina (lost 2-1) OR Nigeria (lost 1-0). So 'which opponent did Bosnia NOT defeat' has multiple valid answers (Argentina and Nigeria, plus Portugal whom they never played).
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Ask which team Bosnia DID beat (Iran) to make it unique.

### Row 4720 — Bosnia and Herzegovina (easy) — FAIL: non-unique (England also scored more)
**Q:** Which 2014 World Cup qualifier scored more goals than Bosnia and Herzegovina?
**Answer:** Netherlands
**Why it fails:** Both the Netherlands (34) AND England (~31) scored more than Bosnia's 30 goals in 2014 World Cup qualifying. Two listed options exceed Bosnia, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Replace England with a team that scored fewer than 30, or reword.

### Row 4729 — Bosnia and Herzegovina (easy) — FAIL: false (2018 group had no Croatia/Serbia/Montenegro)
**Q:** Which Balkan neighbor has Bosnia and Herzegovina NOT faced in a 2018 World Cup qualifier?
**Answer:** Montenegro
**Why it fails:** Bosnia's 2018 World Cup qualifying group (Group H) was Belgium, Greece, Estonia, Cyprus and Gibraltar — NOT Croatia or Serbia. The explanation that 'Bosnia played Croatia and Serbia in their 2018 group' is false, and they did not face Montenegro, Croatia OR Serbia, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_H
**Remedy:** Bosnia's 2018 group Balkan opponent was Greece; they faced none of Croatia/Serbia/Montenegro.

### Row 4731 — Bosnia and Herzegovina (easy) — FAIL: non-unique/false (hasn't faced Croatia/Serbia in WC quals)
**Q:** Which Balkan neighbor has Bosnia and Herzegovina NOT faced in World Cup qualifiers?
**Answer:** Montenegro
**Why it fails:** The premise that Bosnia faced Croatia and Serbia in World Cup qualifying is unsupported — they have not shared a WC qualifying group with Croatia or (separate) Serbia. So 'not faced Montenegro' is not unique; Croatia and Serbia would equally apply.
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_national_football_team
**Remedy:** Reword; Bosnia hasn't faced Croatia or Serbia in recent WC qualifying either.

### Row 4732 — Bosnia and Herzegovina (easy) — FAIL: backwards (Bosnia finished ABOVE Greece)
**Q:** Which Balkan rival finished above Bosnia in 2014 World Cup qualifying?
**Answer:** Greece
**Why it fails:** Bosnia TOPPED Group G in 2014 qualifying (on goal difference over Greece) and qualified directly; Greece finished SECOND and went to the play-offs. So Greece did NOT finish above Bosnia — it was the other way round. The explanation has it reversed.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** Bosnia finished 1st, above Greece; reword or change the answer.

### Row 4757 — Bosnia and Herzegovina (easy) — FAIL: stale (Barbarez also reached a WC, 2026)
**Q:** Which Bosnia and Herzegovina coach is their only one to reach a FIFA World Cup?
**Answer:** Safet SuÅ¡iÄ‡
**Why it fails:** Sušić is no longer the ONLY Bosnia coach to reach a World Cup — Sergej Barbarez led Bosnia to the 2026 World Cup (winning the March 2026 play-off final vs Italy on penalties). So 'only coach to reach a FIFA World Cup' is false.
**Source:** https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/bosnia-herzegovina-qualify
**Remedy:** Two coaches have now reached a WC: Sušić (2014) and Barbarez (2026).

### Row 4789 — Bosnia and Herzegovina (easy) — FAIL: false premise (Bosnia not at Euro 2024)
**Q:** Which Bosnia and Herzegovina defender started at the 2024 European Championship?
**Answer:** Sead KolaÅ¡inac
**Why it fails:** Bosnia and Herzegovina did NOT play at the 2024 European Championship — they were eliminated in the Euro 2024 qualifying play-off semi-final by Ukraine (2-1). No Bosnian defender 'started at Euro 2024'.
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_national_football_team
**Remedy:** Remove the false premise; Bosnia did not qualify for Euro 2024.

### Row 4824 — Bosnia and Herzegovina (easy) — FAIL: false (Susic departed AFTER the 2014 WC)
**Q:** Which Bosnia and Herzegovina manager departed before the 2014 World Cup?
**Answer:** Safet SuÅ¡iÄ‡
**Why it fails:** Sušić did not depart BEFORE the 2014 World Cup — he led Bosnia AT the 2014 World Cup and was dismissed AFTER the group-stage exit (July 2014). The 'departed before' framing contradicts the explanation and the facts.
**Source:** https://en.wikipedia.org/wiki/Safet_Su%C5%A1i%C4%87
**Remedy:** Sušić left after the 2014 World Cup, not before.

### Row 4840 — Bosnia and Herzegovina (easy) — FAIL: wrong manager (Petev led the 2022-23 NL promotion)
**Q:** Which Bosnia and Herzegovina manager led them to UEFA Nations League A promotion in 2023?
**Answer:** Faruk HadÅ¾ibegiÄ‡
**Why it fails:** The 2022-23 Nations League B group win (and promotion back to League A) was achieved under Ivaylo Petev, whose tenure ended 31 December 2022. Faruk Hadžibegić only took over in January 2023, AFTER the NL group stage. So Hadžibegić did not lead the NL promotion.
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_national_football_team
**Remedy:** Change the answer to Ivaylo Petev.

### Row 4843 — Bosnia and Herzegovina (easy) — FAIL: false premise (no Croatia/Serbia in 2014 quals)
**Q:** Which Bosnia and Herzegovina manager oversaw key World Cup qualifiers against Croatia and Serbia in 2013?
**Answer:** Safet SuÅ¡iÄ‡
**Why it fails:** Bosnia's 2014 World Cup qualifying group (Group G) was Greece, Slovakia, Lithuania, Latvia and Liechtenstein — NOT Croatia or Serbia. There were no 'qualifiers against Croatia and Serbia in 2013'. Sušić was the manager, but the premise is false.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** Remove the false Croatia/Serbia qualifier claim.

### Row 4850 — Bosnia and Herzegovina (easy) — FAIL: false premise (no Croatia/Serbia WC qualifiers)
**Q:** Which Bosnia and Herzegovina manager oversaw World Cup qualifiers against Croatia and Serbia?
**Answer:** Safet SuÅ¡iÄ‡
**Why it fails:** Bosnia have not faced Croatia or Serbia in World Cup qualifying (their groups never included them). Sušić oversaw the 2014 qualifying group of Greece/Slovakia/Lithuania/Latvia/Liechtenstein, not Croatia/Serbia.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** Remove the false Croatia/Serbia premise.

### Row 4871 — Bosnia and Herzegovina (easy) — FAIL: wrong timing (Pjanic had ~55 caps by 2014)
**Q:** Which Bosnia and Herzegovina midfielder had over 110 caps by the 2014 World Cup?
**Answer:** Miralem PjaniÄ‡
**Why it fails:** Pjanić did NOT have over 110 caps by the 2014 World Cup — he debuted in 2008 and had roughly 50-55 caps in 2014. He reached 115 caps only at his 2024 retirement. The '110 caps by 2014' timing is false.
**Source:** https://en.wikipedia.org/wiki/Miralem_Pjani%C4%87
**Remedy:** Remove the 'by the 2014 World Cup' qualifier (115 was his career total).

### Row 4885 — Bosnia and Herzegovina (hard) — FAIL: wrong aggregate (6-2, not 5-1)
**Q:** Which Bosnia and Herzegovina opponent won 5-1 on aggregate in the Euro 2012 play-offs?
**Answer:** Portugal
**Why it fails:** Portugal is the correct opponent, but the Euro 2012 play-off aggregate was 6-2, not 5-1.
**Source:** https://www.uefa.com/uefaeuro/match/2008831--portugal-vs-bosnia-and-herzegovina/
**Remedy:** Fix the aggregate to 6-2.

### Row 4899 — Bosnia and Herzegovina (easy) — FAIL: false (Pjanic DID score at 2014)
**Q:** Which Bosnia and Herzegovina player did NOT score a goal at the 2014 FIFA World Cup?
**Answer:** Miralem PjaniÄ‡
**Why it fails:** Pjanić scored at the 2014 World Cup — he netted the 59th-minute goal in the 3-1 win over Iran. In fact all four options scored (Ibišević vs Argentina; Džeko, Pjanić and Vršajević vs Iran), so 'did NOT score' has no valid answer.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Pjanic scored vs Iran; pick a player who actually didn't score.

### Row 4906 — Bosnia and Herzegovina (easy) — FAIL: wrong club (Dzeko was at Man City in 2014)
**Q:** Which Bosnia and Herzegovina player from the 2014 World Cup squad played for AS Roma?
**Answer:** Edin DÅ¾eko
**Why it fails:** At the 2014 World Cup, Džeko played for Manchester City — he joined AS Roma only in August 2015. The 2014 Bosnia squad's AS Roma player was Miralem Pjanić (a listed option), so the answer should be Pjanić.
**Source:** https://en.wikipedia.org/wiki/Edin_D%C5%BEeko
**Remedy:** Change the answer to Pjanic (Dzeko was at Man City, joining Roma in 2015).

### Row 4907 — Bosnia and Herzegovina (easy) — FAIL: false (Bosnia not at Euro 2016)
**Q:** Which Bosnia and Herzegovina player from their 2014 World Cup squad also played in the 2016 European Championship?
**Answer:** Edin DÅ¾eko
**Why it fails:** Bosnia did NOT play at UEFA Euro 2016 — they lost the qualifying play-off to the Republic of Ireland (1-3 aggregate). So no 2014 squad member 'also played in the 2016 European Championship'.
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_national_football_team
**Remedy:** Remove the false premise; Bosnia did not qualify for Euro 2016.

### Row 4951 — Bosnia and Herzegovina (easy) — FAIL: false (Ibisevic scored Bosnias first open-play goal)
**Q:** Which Bosnia and Herzegovina player scored his nation's first open-play World Cup goal at the 2014 FIFA World Cup?
**Answer:** Edin DÅ¾eko
**Why it fails:** Bosnia's first open-play World Cup goal was Ibišević's vs Argentina (85', a through-ball finish), NOT Džeko's vs Iran. So the answer to 'who scored his nation's first open-play World Cup goal' should be Ibišević, not Džeko.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Bosnia's first (open-play) WC goal was Ibisevic vs Argentina.

### Row 4957 — Bosnia and Herzegovina (medium) — FAIL: non-unique (Pjanic also scored win not loss)
**Q:** Which Bosnia and Herzegovina player scored in their 2014 group stage win but not in their opening defeat?
**Answer:** Edin DÅ¾eko
**Why it fails:** Pjanić (a listed option) also scored in the group-stage win (vs Iran) and did NOT score in the opening defeat (vs Argentina) — same as Džeko. So 'scored in the win but not the opening defeat' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Add a distinguishing detail; Pjanic also fits.

### Row 4960 — Bosnia and Herzegovina (easy) — FAIL: wrong metric (65+ is total intl, not WC quals)
**Q:** Which Bosnia and Herzegovina player scored over 65 goals in World Cup qualifiers?
**Answer:** Edin DÅ¾eko
**Why it fails:** Džeko's 65+ goals are his TOTAL international goals (73), not goals 'in World Cup qualifiers' — his WC-qualifying tally is far lower (~25-30). The explanation itself says 'over 65 INTERNATIONAL goals'.
**Source:** https://en.wikipedia.org/wiki/Edin_D%C5%BEeko
**Remedy:** Change 'in World Cup qualifiers' to 'in internationals' (total).

### Row 4980 — Bosnia and Herzegovina (easy) — FAIL: false (Bosnia lost the first leg 0-1; Misimovic didnt score)
**Q:** Which Bosnia and Herzegovina player scored their 2010 World Cup play-off away goal against Portugal?
**Answer:** Zvjezdan MisimoviÄ‡
**Why it fails:** Bosnia did NOT win the first leg of the 2010 play-off — Portugal won 1-0 in Lisbon (and 1-0 in Zenica), 2-0 on aggregate. Bosnia scored NO goals across the tie, so Misimović did not score 'their only goal in a 1-0 first-leg win'.
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_national_football_team
**Remedy:** Bosnia lost both legs 0-1; nobody scored for them.

### Row 4982 — Bosnia and Herzegovina (easy) — FAIL: false (Ibisevic scored Bosnias first open-play goal)
**Q:** Which Bosnia and Herzegovina player scored their first open-play World Cup goal at the 2014 FIFA World Cup?
**Answer:** Edin DÅ¾eko
**Why it fails:** Bosnia's first open-play World Cup goal was Ibišević's vs Argentina, not Džeko's vs Iran. The answer should be Ibišević.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Bosnia's first WC goal (open play) was Ibisevic vs Argentina.

### Row 5068 — Bosnia and Herzegovina (easy) — FAIL: false (2014 quals were at Bilino Polje, not Kosevo)
**Q:** Which Bosnia and Herzegovina stadium held 34,500 fans for 2014 World Cup qualifiers?
**Answer:** Asim FerhatoviÄ‡ Hase Stadium
**Why it fails:** Bosnia's 2014 World Cup home qualifiers were played at Bilino Polje, Zenica (~15,292), not the 34,500-capacity Asim Ferhatović Hase in Sarajevo. So no 34,500-capacity stadium 'held fans for 2014 qualifiers'.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** The 2014 qualifiers were at Bilino Polje (Zenica), ~15,292.

### Row 5069 — Bosnia and Herzegovina (easy) — FAIL: wrong stadium (Bilino Polje hosted 2014 quals)
**Q:** Which Bosnia and Herzegovina stadium hosted 2014 World Cup qualifiers?
**Answer:** Asim FerhatoviÄ‡ Hase Stadium
**Why it fails:** Bosnia hosted their 2014 World Cup qualifiers at Bilino Polje (Zenica), not the Asim Ferhatović Hase Stadium. The correct option is Bilino Polje.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** Change the answer to Bilino Polje.

### Row 5070 — Bosnia and Herzegovina (easy) — FAIL: false (2014 quals were at Bilino Polje)
**Q:** Which Bosnia and Herzegovina stadium hosted a 2014 World Cup qualifier and a Euro 2016 qualifier?
**Answer:** Asim FerhatoviÄ‡ Hase Stadium
**Why it fails:** Bosnia's 2014 World Cup home qualifiers were at Bilino Polje, Zenica, not the Asim Ferhatović Hase. The premise that Asim Ferhatović Hase hosted a 2014 WC qualifier is false.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** The 2014 home qualifiers were at Bilino Polje.

### Row 5071 — Bosnia and Herzegovina (easy) — FAIL: wrong stadium (Greece game at Bilino Polje)
**Q:** Which Bosnia and Herzegovina stadium hosted a 2014 World Cup qualifier vs Greece?
**Answer:** Asim FerhatoviÄ‡ Hase
**Why it fails:** Bosnia's 2014 qualifier vs Greece (3-1, March 2013) was played at Bilino Polje in Zenica, NOT the Asim Ferhatović Hase in Sarajevo. (The dataset's own row 5072 correctly says Bilino Polje.)
**Source:** https://athlet.org/football/world-cup/2014/qualifiers/uefa/group-g/2013-03-22-bosniaandherzegovina-greece.html
**Remedy:** Change the answer to Bilino Polje.

### Row 5073 — Bosnia and Herzegovina (easy) — FAIL: wrong stadium (Greece game at Bilino Polje)
**Q:** Which Bosnia and Herzegovina stadium hosted the 2014 World Cup qualifier against Greece?
**Answer:** Asim FerhatoviÄ‡ Hase Stadium
**Why it fails:** The 2014 qualifier vs Greece was at Bilino Polje (Zenica), not the Asim Ferhatović Hase.
**Source:** https://athlet.org/football/world-cup/2014/qualifiers/uefa/group-g/2013-03-22-bosniaandherzegovina-greece.html
**Remedy:** Change the answer to Bilino Polje.

### Row 5077 — Bosnia and Herzegovina (easy) — FAIL: false (2014 quals were at Bilino Polje)
**Q:** Which Bosnia and Herzegovina stadium, capacity ~34,500, hosted 2014 World Cup qualifiers?
**Answer:** Asim FerhatoviÄ‡ Hase Stadium
**Why it fails:** Bosnia's 2014 home qualifiers were at Bilino Polje (Zenica, ~15,292), not the 34,500-capacity Asim Ferhatović Hase.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** The 2014 qualifiers were at Bilino Polje.

### Row 5079 — Bosnia and Herzegovina (easy) — FAIL: false (2014 quals were at Bilino Polje)
**Q:** Which Bosnia and Herzegovina stadium, with a 34,500 capacity, hosted a 2014 World Cup qualifier?
**Answer:** Asim FerhatoviÄ‡ Hase
**Why it fails:** The 2014 home qualifiers were at Bilino Polje (Zenica), not the 34,500-capacity Asim Ferhatović Hase.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** The 2014 qualifiers were at Bilino Polje.

### Row 5080 — Bosnia and Herzegovina (easy) — FAIL: false (2014 quals were at Bilino Polje)
**Q:** Which Bosnia and Herzegovina stadium, with a capacity of roughly 34,500, hosted a high-profile 2014 World Cup qualifier?
**Answer:** Estadio Asim FerhatoviÄ‡ Hase
**Why it fails:** The 2014 home qualifiers were at Bilino Polje (Zenica), not the 34,500-capacity Asim Ferhatović Hase.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** The 2014 qualifiers were at Bilino Polje.

### Row 5090 — Bosnia and Herzegovina (easy) — FAIL: false (Ibisevic scored Bosnias first open-play goal)
**Q:** Which Bosnia and Herzegovina star from the 2014 World Cup squad scored their first open-play goal in Brazil?
**Answer:** Edin DÅ¾eko
**Why it fails:** Bosnia's first open-play World Cup goal was Ibišević's vs Argentina, not Džeko's vs Iran. The answer should be Ibišević.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Bosnia's first WC goal (open play) was Ibisevic vs Argentina.

### Row 5106 — Bosnia and Herzegovina (easy) — FAIL: non-unique (Ibisevic also Bundesliga)
**Q:** Which Bosnia and Herzegovina star played in Germany's top league during their golden era?
**Answer:** Edin DÅ¾eko
**Why it fails:** Vedad Ibišević (a listed option) also played in Germany's top flight during the golden era — at Hoffenheim and VfB Stuttgart — so 'played in Germany's top league' is non-unique with Džeko (Wolfsburg).
**Source:** https://en.wikipedia.org/wiki/Vedad_Ibi%C5%A1evi%C4%87
**Remedy:** Add a distinguishing detail; Ibisevic was also a Bundesliga player.

### Row 5119 — Bosnia and Herzegovina (easy) — FAIL: false (Pjanic TOTY came after 2014)
**Q:** Which Bosnia and Herzegovina star was named in the Serie A Team of the Year multiple times before the 2014 World Cup?
**Answer:** Miralem PjaniÄ‡
**Why it fails:** Pjanić had ZERO Serie A Team of the Year selections before the 2014 World Cup — his first was 2015-16 (then 2016-17, 2017-18, 2018-19). So 'multiple times before the 2014 World Cup' is false.
**Source:** https://en.wikipedia.org/wiki/Miralem_Pjani%C4%87
**Remedy:** His Serie A TOTY honours were 2015-16 onward, after 2014.

### Row 5129 — Bosnia and Herzegovina (easy) — FAIL: false (Dzeko is still active, 2026 captain)
**Q:** Which Bosnia and Herzegovina striker retired from internationals after the 2022 World Cup qualifiers?
**Answer:** Edin DÅ¾eko
**Why it fails:** Edin Džeko did NOT retire from internationals after the 2022 World Cup qualifiers — he remained Bosnia's captain and is in their 2026 World Cup squad (he played the March 2026 play-offs). He is still active.
**Source:** https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/bosnia-herzegovina-qualify
**Remedy:** Remove the false retirement claim; Dzeko captains Bosnia at the 2026 WC.

### Row 5142 — Bosnia and Herzegovina (easy) — FAIL: false premise (Bosnia not at Euro 2024)
**Q:** Which Bosnia and Herzegovina veteran anchored their youthful defense at UEFA Euro 2024?
**Answer:** Sead KolaÅ¡inac
**Why it fails:** Bosnia did not play at UEFA Euro 2024 — they lost the qualifying play-off semi-final to Ukraine. No Bosnian 'anchored their defense at Euro 2024'.
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_national_football_team
**Remedy:** Remove the false premise; Bosnia did not qualify for Euro 2024.

### Row 5193 — Bosnia and Herzegovina (easy) — FAIL: false (Dzekos goal was disallowed; Bosnia scored 0)
**Q:** Which Bosnia player scored a goal against Nigeria in the 2014 World Cup?
**Answer:** Edin DÅ¾eko
**Why it fails:** Bosnia did NOT score against Nigeria — they lost 1-0. Džeko's effort was DISALLOWED (wrongly, for offside), so it was not a goal. No Bosnia player scored a valid goal in that match.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Reword: Dzeko had a goal disallowed; Bosnia scored none (lost 1-0).

### Row 5207 — Bosnia and Herzegovina (easy) — FAIL: false (Ibisevics first goal was already open play)
**Q:** Which Bosnia player scored the nation's first open-play World Cup goal after their first-ever goal?
**Answer:** Edin DÅ¾eko
**Why it fails:** Ibišević's first-ever WC goal (vs Argentina) was itself scored in open play, so Džeko's vs Iran was not 'the first open-play goal after the first-ever goal' — they were both open play, with Ibišević's coming first.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Bosnia's first goal (Ibisevic) was already open play.

### Row 5244 — Bosnia and Herzegovina (easy) — FAIL: false (Ibisevic scored Bosnias first open-play goal)
**Q:** Which Bosnia player's 2014 World Cup goal was the team's first from open play?
**Answer:** Edin DÅ¾eko
**Why it fails:** Bosnia's first open-play World Cup goal was Ibišević's vs Argentina, not Džeko's vs Iran. The answer should be Ibišević.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Bosnia's first WC goal (open play) was Ibisevic vs Argentina.

### Row 5260 — Bosnia and Herzegovina (easy) — FAIL: wrong season (Bundesliga top scorer 2009-10, not 2012-13)
**Q:** Which Bosnia striker was Bundesliga top scorer when they qualified for the 2014 World Cup?
**Answer:** Edin DÅ¾eko
**Why it fails:** Džeko was Bundesliga top scorer in 2009-10 (Wolfsburg). By 2012-13 — when Bosnia qualified for 2014 — he was at Manchester City in the Premier League, not the Bundesliga. So 'Bundesliga top scorer in 2012-13' is false.
**Source:** https://en.wikipedia.org/wiki/Edin_D%C5%BEeko
**Remedy:** His Bundesliga Torjagerkanone was 2009-10; in 2012-13 he was at Man City.

### Row 5281 — Bosnia and Herzegovina (easy) — FAIL: false premise (Bosnia not at 2022 WC)
**Q:** Which Bosnian defender's leadership stabilized their youthful defense at the 2022 FIFA World Cup?
**Answer:** Sead KolaÅ¡inac
**Why it fails:** Bosnia did not play at the 2022 FIFA World Cup — they failed to qualify (4th in their group behind France, Ukraine, Finland). No Bosnian defender stabilized a defense 'at the 2022 World Cup'.
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_national_football_team
**Remedy:** Remove the false premise; Bosnia did not qualify for the 2022 WC.

### Row 5295 — Bosnia and Herzegovina (easy) — FAIL: false timing (Pjanic TOTY came after 2014)
**Q:** Which Bosnian midfielder was in the Serie A Team of the Year during 2014 World Cup qualifying?
**Answer:** Miralem PjaniÄ‡
**Why it fails:** Pjanić was NOT in a Serie A Team of the Year during 2014 World Cup qualifying — his first selection was 2015-16, after the 2014 World Cup. (Only Pjanic is Bosnian among the options, but the timing is false.)
**Source:** https://en.wikipedia.org/wiki/Miralem_Pjani%C4%87
**Remedy:** His Serie A TOTY honours were 2015-16 onward, after 2014.

### Row 5302 — Bosnia and Herzegovina (easy) — FAIL: non-unique (Dzeko, Pjanic, Ibisevic all scored)
**Q:** Which Bosnian player scored at the 2014 FIFA World Cup?
**Answer:** Edin DÅ¾eko
**Why it fails:** Three of the four options scored at the 2014 World Cup — Ibišević (vs Argentina), Džeko and Pjanić (both vs Iran). 'Which player scored at the 2014 WC' is non-unique. (The explanation also wrongly calls Dzeko's the 'first-ever' goal — that was Ibisevic.)
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Pin to a specific match/goal.

### Row 5305 — Bosnia and Herzegovina (medium) — FAIL: non-unique + wrong explanation
**Q:** Which Bosnian player scored in the 2014 FIFA World Cup group stage?
**Answer:** Edin DÅ¾eko
**Why it fails:** Ibišević, Džeko and Pjanić all scored in the 2014 group stage, so the answer is non-unique. The explanation is also wrong: Džeko scored vs Iran, not Argentina, and Bosnia's first goal was Ibišević's vs Argentina.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Pin to a specific match; fix the explanation (Dzeko scored vs Iran).

### Row 5308 — Bosnia and Herzegovina (easy) — FAIL: false (Ibisevic scored the first open-play goal)
**Q:** Which Bosnian player scored the team's first-ever open-play World Cup goal in 2014?
**Answer:** Edin DÅ¾eko
**Why it fails:** Bosnia's first open-play World Cup goal was Ibišević's vs Argentina, not Džeko's vs Iran.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Change the answer to Ibisevic.

### Row 5312 — Bosnia and Herzegovina (medium) — FAIL: false (Dzeko scored once vs Iran, not twice)
**Q:** Which Bosnian player scored twice in the 2014 World Cup group stage?
**Answer:** Edin DÅ¾eko
**Why it fails:** Džeko did NOT score twice — Bosnia's 3-1 win over Iran had three different scorers: Džeko (1), Pjanić (1) and Avdija Vršajević (1). No Bosnia player scored twice at the 2014 World Cup.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Dzeko scored once vs Iran; the others were Pjanic and Vrsajevic.

### Row 5327 — Bosnia and Herzegovina (easy) — FAIL: wrong stadium (Greece game at Bilino Polje)
**Q:** Which Bosnian stadium hosted a 2014 World Cup qualifier against Greece?
**Answer:** Asim FerhatoviÄ‡ Hase
**Why it fails:** Bosnia's 2014 qualifier vs Greece was at Bilino Polje (Zenica), not the Asim Ferhatović Hase. Bilino Polje is the correct (listed) option.
**Source:** https://athlet.org/football/world-cup/2014/qualifiers/uefa/group-g/2013-03-22-bosniaandherzegovina-greece.html
**Remedy:** Change the answer to Bilino Polje.

### Row 5328 — Bosnia and Herzegovina (easy) — FAIL: false (2014 quals were at Bilino Polje)
**Q:** Which Bosnian stadium hosted a 2014 World Cup qualifier before the 2016 Euros?
**Answer:** Asim FerhatoviÄ‡ Hase
**Why it fails:** Bosnia's 2014 home qualifiers were at Bilino Polje (Zenica), not the Asim Ferhatović Hase.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** The 2014 qualifiers were at Bilino Polje.

### Row 5329 — Bosnia and Herzegovina (easy) — FAIL: wrong stadium (Greece game at Bilino Polje)
**Q:** Which Bosnian stadium hosted the 2013 World Cup qualifier vs Greece?
**Answer:** Asim FerhatoviÄ‡ Hase Stadium
**Why it fails:** The 2014 Greece qualifier was at Bilino Polje (Zenica), not the Asim Ferhatović Hase (and it was a group game, not a 'play-off').
**Source:** https://athlet.org/football/world-cup/2014/qualifiers/uefa/group-g/2013-03-22-bosniaandherzegovina-greece.html
**Remedy:** Change the answer to Bilino Polje.

### Row 5330 — Bosnia and Herzegovina (easy) — FAIL: wrong stadium (Greece game at Bilino Polje, not Kosevo)
**Q:** Which Bosnian stadium hosted the 2014 World Cup qualifier against Greece?
**Answer:** KoÅ¡evo Stadium
**Why it fails:** The 2014 Greece qualifier (3-1) was at Bilino Polje in Zenica, not the Koševo Stadium in Sarajevo. Bilino Polje is the correct option.
**Source:** https://athlet.org/football/world-cup/2014/qualifiers/uefa/group-g/2013-03-22-bosniaandherzegovina-greece.html
**Remedy:** Change the answer to Bilino Polje.

### Row 5331 — Bosnia and Herzegovina (easy) — FAIL: wrong stadium (Greece game at Bilino Polje)
**Q:** Which Bosnian stadium hosted their 2014 World Cup qualifier against Greece?
**Answer:** Asim FerhatoviÄ‡ Hase Stadium
**Why it fails:** The 2014 Greece qualifier was at Bilino Polje (Zenica), not the Asim Ferhatović Hase.
**Source:** https://athlet.org/football/world-cup/2014/qualifiers/uefa/group-g/2013-03-22-bosniaandherzegovina-greece.html
**Remedy:** Change the answer to Bilino Polje.

### Row 5333 — Bosnia and Herzegovina (easy) — FAIL: false (2014 quals were at Bilino Polje)
**Q:** Which Bosnian stadium, capacity 34,500, hosted 2014 World Cup qualifiers?
**Answer:** Asim FerhatoviÄ‡ Hase Stadium
**Why it fails:** The 2014 home qualifiers were at Bilino Polje (~15,292), not the 34,500-capacity Asim Ferhatović Hase.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** The 2014 qualifiers were at Bilino Polje.

### Row 5334 — Bosnia and Herzegovina (easy) — FAIL: false (2014 quals were at Bilino Polje)
**Q:** Which Bosnian stadium, capacity 34,500, hosted a 2014 World Cup qualifier?
**Answer:** Asim FerhatoviÄ‡ Hase
**Why it fails:** The 2014 home qualifiers were at Bilino Polje, not the 34,500-capacity Asim Ferhatović Hase.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** The 2014 qualifiers were at Bilino Polje.

### Row 5340 — Bosnia and Herzegovina (easy) — FAIL: non-unique (all options played at 2014)
**Q:** Which Bosnian star played for Bosnia at the 2014 FIFA World Cup?
**Answer:** Miralem PjaniÄ‡
**Why it fails:** All four options — Pjanić, Džeko, Begović and Ibišević — played for Bosnia at the 2014 World Cup. 'Which star played at the 2014 WC' is non-unique.
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_at_the_FIFA_World_Cup
**Remedy:** Add non-2014 distractors or a distinguishing detail.

### Row 5341 — Bosnia and Herzegovina (easy) — FAIL: non-unique (all options in the 2014 squad)
**Q:** Which Bosnian star played for Bosnia at the 2014 World Cup?
**Answer:** Edin DÅ¾eko
**Why it fails:** All four options — Džeko, Pjanić, Begović and Misimović — were in Bosnia's 2014 World Cup squad. The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_at_the_FIFA_World_Cup
**Remedy:** Add non-2014 distractors or a distinguishing detail.

### Row 5348 — Bosnia and Herzegovina (easy) — FAIL: false (Misimovic WAS in the 2014 squad)
**Q:** Which Bosnian star was not in their 2014 World Cup squad?
**Answer:** Zvjezdan MisimoviÄ‡
**Why it fails:** Misimović WAS in Bosnia's 2014 World Cup squad (the 24-man roster, then playing for Guizhou Renhe). He retired from internationals in August 2014, after the tournament. So 'Misimović was not in the 2014 squad' is false.
**Source:** https://bleacherreport.com/articles/2056403-bosnia-and-herzegovina-2014-fifa-world-cup-squad-player-by-player-guide
**Remedy:** Misimovic was in the 2014 squad; pick a player who genuinely wasn't.

### Row 5352 — Bosnia and Herzegovina (easy) — FAIL: false (Ibisevic scored the first open-play goal)
**Q:** Which Bosnian striker scored his nation's first open-play World Cup goal in 2014?
**Answer:** Edin DÅ¾eko
**Why it fails:** Bosnia's first open-play World Cup goal was Ibišević's vs Argentina, not Džeko's vs Iran.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Change the answer to Ibisevic.

### Row 5374 — Bosnia and Herzegovina (easy) — FAIL: non-unique (also never won the PL Golden Boot)
**Q:** Which league's top scorer award did Bosnia's Edin DÅ¾eko NOT win?
**Answer:** La Liga
**Why it fails:** Džeko won the Bundesliga (2009-10) and Serie A (2016-17) top-scorer awards but did NOT win EITHER La Liga (never played in Spain) OR the Premier League Golden Boot. So 'which did he NOT win' has two valid answers among the options.
**Source:** https://en.wikipedia.org/wiki/Edin_D%C5%BEeko
**Remedy:** He also never won the Premier League top scorer; make it unique.

### Row 5389 — Bosnia and Herzegovina (hard) — FAIL: wrong aggregate (6-2, not 5-1)
**Q:** Which nation beat Bosnia and Herzegovina 5-1 on aggregate in the Euro 2012 play-offs?
**Answer:** Portugal
**Why it fails:** Portugal is the correct nation, but the Euro 2012 play-off aggregate was 6-2 (0-0 then 6-2), not 5-1.
**Source:** https://www.uefa.com/uefaeuro/match/2008831--portugal-vs-bosnia-and-herzegovina/
**Remedy:** Fix the aggregate to 6-2.

### Row 5417 — Bosnia and Herzegovina (hard) — FAIL: non-unique (faced only N. Ireland in a shootout)
**Q:** Which nation did Bosnia and Herzegovina NOT face in a UEFA Euro 2020 play-off penalty shootout?
**Answer:** Republic of Ireland
**Why it fails:** Bosnia's only Euro 2020 play-off penalty shootout was vs Northern Ireland (the SF, which they lost). So they did NOT face Republic of Ireland, Ukraine OR Portugal in a shootout — three of the four options qualify, making 'NOT faced' non-unique.
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_national_football_team
**Remedy:** Ask which nation they DID face (N. Ireland) to make it unique.

### Row 5418 — Bosnia and Herzegovina (medium) — FAIL: non-unique (Portugal AND Germany not faced)
**Q:** Which nation did Bosnia and Herzegovina NOT face in the 2014 World Cup group stage?
**Answer:** Portugal
**Why it fails:** Bosnia's 2014 group was Argentina, Nigeria and Iran. So they did NOT face Portugal OR Germany — both listed options — making 'which did they NOT face' non-unique.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Use only one non-opponent distractor.

### Row 5427 — Bosnia and Herzegovina (easy) — FAIL: non-unique (Portugal/Croatia/Serbia all not faced)
**Q:** Which nation did Bosnia not face in bitter 2014-2019 qualifiers?
**Answer:** Portugal
**Why it fails:** Bosnia did not face Portugal, Croatia OR Serbia in 2014-2019 World Cup/Euro qualifiers — their bitter qualifying rivalry was with Greece. So 'NOT faced' is non-unique (three options qualify), and the explanation wrongly implies they regularly faced Croatia and Serbia.
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_national_football_team
**Remedy:** Greece was the actual frequent opponent; the other three were all not faced.

### Row 5474 — Bosnia and Herzegovina (hard) — FAIL: wrong aggregate (6-2, not 5-1)
**Q:** Which nation inflicted a 5-1 aggregate defeat on Bosnia and Herzegovina in the Euro 2012 play-offs?
**Answer:** Portugal
**Why it fails:** Portugal is correct, but the Euro 2012 play-off aggregate was 6-2, not 5-1.
**Source:** https://www.uefa.com/uefaeuro/match/2008831--portugal-vs-bosnia-and-herzegovina/
**Remedy:** Fix the aggregate to 6-2.

### Row 5494 — Bosnia and Herzegovina (easy) — FAIL: wrong group (Bosnia in Group D w/ France, not Portugals Group A)
**Q:** Which nation qualified for the 2022 World Cup instead of Bosnia and Herzegovina?
**Answer:** Portugal
**Why it fails:** Bosnia were in 2022 World Cup qualifying Group D (France, Ukraine, Finland, Bosnia, Kazakhstan), won by France — NOT Portugal's Group A. So Portugal did not 'qualify instead of Bosnia from that group'; France did.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_D
**Remedy:** Change the answer to France (Bosnia's Group D winner).

### Row 5511 — Bosnia and Herzegovina (easy) — FAIL: self-referential (answer is Bosnia itself)
**Q:** Which nation, like Bosnia, qualified for their first World Cup in 2014?
**Answer:** Bosnia and Herzegovina
**Why it fails:** The question asks which OTHER nation, like Bosnia, qualified for its first World Cup in 2014, but the answer is 'Bosnia and Herzegovina' itself — self-referential. (None of the other options fit either: Costa Rica debuted 1990, Iceland and Panama 2018.)
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup
**Remedy:** The answer must be a different nation; none of the options qualify.

### Row 5517 — Bosnia and Herzegovina (easy) — FAIL: self-referential (answer is Bosnia itself)
**Q:** Which nation's unbeaten home World Cup qualifying run from 2011-2014 matched Bosnia and Herzegovina's?
**Answer:** Bosnia and Herzegovina
**Why it fails:** The question asks which nation's unbeaten home run 'matched Bosnia's', but the answer is 'Bosnia and Herzegovina' — self-referential.
**Source:** https://en.wikipedia.org/wiki/Bosnia_and_Herzegovina_national_football_team
**Remedy:** The answer must be a different nation.

### Row 5535 — Bosnia and Herzegovina (easy) — FAIL: false premise (no 2014 play-off; clincher was away in Kaunas)
**Q:** Which stadium did Bosnia and Herzegovina use for their 2014 World Cup qualifying playoff home leg?
**Answer:** Bilino Polje
**Why it fails:** Bosnia qualified for 2014 DIRECTLY by winning Group G — they did not play a 2014 qualifying play-off. Their decisive game was AWAY at Lithuania (Kaunas), not a home leg at Bilino Polje. The 'qualifying playoff home leg' premise is false.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** Bosnia qualified directly; the clincher was away in Kaunas.

### Row 5543 — Bosnia and Herzegovina (easy) — FAIL: wrong stadium (Greece game at Bilino Polje)
**Q:** Which stadium hosted Bosnia's 2014 World Cup qualifier against Greece?
**Answer:** Asim FerhatoviÄ‡ Hase Stadium
**Why it fails:** Bosnia's 2014 qualifier vs Greece was at Bilino Polje (Zenica), not the Asim Ferhatović Hase.
**Source:** https://athlet.org/football/world-cup/2014/qualifiers/uefa/group-g/2013-03-22-bosniaandherzegovina-greece.html
**Remedy:** Change the answer to Bilino Polje.

### Row 5544 — Bosnia and Herzegovina (easy) — FAIL: false premise (Argentina was a finals opponent, not a qualifier)
**Q:** Which stadium hosted Bosnia's 2014 World Cup qualifier vs Argentina?
**Answer:** Asim FerhatoviÄ‡ Hase Stadium
**Why it fails:** Bosnia never played Argentina in 2014 World Cup QUALIFYING — Argentina was their group opponent at the 2014 finals (at the Maracanã). There was no 'qualifier vs Argentina'.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Remove the false premise; Argentina was a 2014 finals opponent.

### Row 5545 — Bosnia and Herzegovina (easy) — FAIL: false premise (no 2014 qualifier vs Portugal)
**Q:** Which stadium hosted Bosnia's 2014 World Cup qualifier vs Portugal?
**Answer:** Asim FerhatoviÄ‡ Hase Stadium
**Why it fails:** Bosnia did NOT play Portugal in 2014 World Cup qualifying — their Group G was Greece, Slovakia, Lithuania, Latvia, Liechtenstein. (They met Portugal in the 2010 WC and Euro 2012 play-offs.)
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** Remove the false premise; no 2014 qualifier vs Portugal.

### Row 5546 — Bosnia and Herzegovina (easy) — FAIL: wrong stadium (Greece game at Bilino Polje)
**Q:** Which stadium hosted Bosnia's 3-1 win over Greece in a 2014 World Cup qualifier?
**Answer:** Asim FerhatoviÄ‡ Hase Stadium
**Why it fails:** Bosnia's 3-1 win over Greece was at Bilino Polje (Zenica), not the Asim Ferhatović Hase.
**Source:** https://athlet.org/football/world-cup/2014/qualifiers/uefa/group-g/2013-03-22-bosniaandherzegovina-greece.html
**Remedy:** Change the answer to Bilino Polje.

### Row 5547 — Bosnia and Herzegovina (hard) — FAIL: wrong aggregate (6-2, not 5-1)
**Q:** Which stadium hosted Bosnia's 5-1 aggregate loss to Portugal in the 2012 Euro play-offs?
**Answer:** Estádio da Luz
**Why it fails:** The Euro 2012 play-off aggregate was 6-2, not 5-1. (Portugal's home leg was indeed in Lisbon.)
**Source:** https://www.uefa.com/uefaeuro/match/2008831--portugal-vs-bosnia-and-herzegovina/
**Remedy:** Fix the aggregate to 6-2.

### Row 5552 — Bosnia and Herzegovina (easy) — FAIL: wrong stadium (Greece game at Bilino Polje)
**Q:** Which stadium hosted Bosnia's key 2014 World Cup qualifier against Greece?
**Answer:** Asim FerhatoviÄ‡ Hase
**Why it fails:** The 2014 Greece qualifier was at Bilino Polje (Zenica), not the Asim Ferhatović Hase.
**Source:** https://athlet.org/football/world-cup/2014/qualifiers/uefa/group-g/2013-03-22-bosniaandherzegovina-greece.html
**Remedy:** Change the answer to Bilino Polje.

### Row 5576 — Bosnia and Herzegovina (hard) — FAIL: wrong aggregate (6-2, not 5-1)
**Q:** Which team defeated Bosnia and Herzegovina 5-1 on aggregate in the UEFA Euro 2012 play-offs?
**Answer:** Portugal
**Why it fails:** Portugal is correct, but the Euro 2012 play-off aggregate was 6-2, not 5-1.
**Source:** https://www.uefa.com/uefaeuro/match/2008831--portugal-vs-bosnia-and-herzegovina/
**Remedy:** Fix the aggregate to 6-2.

### Row 5596 — Bosnia and Herzegovina (easy) — FAIL: non-unique (Portugal AND Iran did not eliminate them)
**Q:** Which team did NOT eliminate Bosnia and Herzegovina from the 2014 World Cup?
**Answer:** Portugal
**Why it fails:** Bosnia were eliminated by their losses to Argentina and Nigeria. Both Portugal (not in the group) AND Iran (whom Bosnia beat 3-1) did NOT eliminate them, so 'which did NOT eliminate' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Use only one non-eliminator distractor.

### Row 5639 — Bosnia and Herzegovina (easy) — FAIL: non-unique (Greece also finished above Bosnia)
**Q:** Which two nations finished above Bosnia and Herzegovina in Euro 2020 qualifying Group J?
**Answer:** Italy and Finland
**Why it fails:** Bosnia finished 4th in Euro 2020 qualifying Group J, behind Italy (1st), Finland (2nd) AND Greece (3rd). So three nations finished above them — the option pairs 'Italy and Greece' and 'Finland and Greece' are equally valid, making the answer non-unique.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020_qualifying_Group_J
**Remedy:** Three teams finished above Bosnia (Italy, Finland, Greece); the question is non-unique.

### Row 5670 — Bosnia and Herzegovina (easy) — FAIL: false (Argentina & Nigeria are not UEFA teams)
**Q:** Which two UEFA teams did Bosnia and Herzegovina finish behind in their 2014 World Cup group?
**Answer:** Argentina and Nigeria
**Why it fails:** Argentina (CONMEBOL) and Nigeria (CAF) are NOT UEFA teams. Bosnia finished behind them at the 2014 World Cup, but the 'two UEFA teams' premise is false — no UEFA team finished above Bosnia in Group F.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_F
**Remedy:** Drop 'UEFA'; Argentina and Nigeria are not European.

### Row 5693 — Bosnia and Herzegovina (easy) — FAIL: non-unique (all four topped their groups)
**Q:** Which UEFA nation, besides Bosnia and Herzegovina, topped their 2014 World Cup qualifying group?
**Answer:** Netherlands
**Why it fails:** The explanation itself notes that the Netherlands, Switzerland, Belgium AND England all topped their respective 2014 World Cup qualifying groups. So all four options are correct — the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** All four listed nations topped their 2014 qualifying groups.

### Row 5706 — Bosnia and Herzegovina (easy) — FAIL: self-referential (answer is Bosnia itself)
**Q:** Which UEFA team matched Bosnia's 2014 World Cup qualifying rate of 3 goals per game?
**Answer:** Bosnia and Herzegovina
**Why it fails:** The question asks which UEFA team MATCHED Bosnia's 3-goals-per-game rate, but the answer is 'Bosnia and Herzegovina' itself — self-referential. The explanation even says only Bosnia achieved it, so no other option qualifies.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** The answer must be a different team; none of the options match.

### Row 5773 — Bosnia and Herzegovina (easy) — FAIL: false premise (2014 quals were at Bilino Polje)
**Q:** Why did Bosnia and Herzegovina host a 2014 World Cup qualifier at Sarajevo's Asim FerhatoviÄ‡ Hase Stadium?
**Answer:** Host high-profile international match
**Why it fails:** Bosnia did not host their 2014 World Cup qualifiers at the Asim Ferhatović Hase (Koševo) — their home qualifiers were at Bilino Polje (Zenica). The premise is false.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_G
**Remedy:** The 2014 home qualifiers were at Bilino Polje, not Kosevo.

### Row 5802 — Bosnia and Herzegovina (easy) — FAIL: false premise (Greece game at Bilino Polje, not Kosevo)
**Q:** Why was Bosnia's 2014 World Cup qualifier vs Greece held at KoÅ¡evo Stadium?
**Answer:** Larger capacity for fans
**Why it fails:** Bosnia's 2014 qualifier vs Greece (3-1) was played at Bilino Polje in Zenica, NOT the Koševo Stadium in Sarajevo. The premise that it was held at Koševo for capacity is false.
**Source:** https://athlet.org/football/world-cup/2014/qualifiers/uefa/group-g/2013-03-22-bosniaandherzegovina-greece.html
**Remedy:** The Greece qualifier was at Bilino Polje (Zenica).
---

## Czechia (batch-2 rows 16004–16893)

**Fact base (sourced):** Czechia's **only WC played** = **2006** (group-stage exit). They did **NOT** play at 2010/2014/2018/2022 — so "At the 2014/2022 World Cup, which Czech…" questions carry a **false premise**. They **DID qualify for 2026** (UEFA play-off win over Denmark, 31 Mar 2026) — so "2006 = only independent *qualification*" is now **false**. Euro record vs Netherlands is **2-1 (lost 0-1 at Euro 2000)** — **not** perfect/2-0. FIFA ranking dropped below 40 after 2010 (lowest ~67). They did **not** play Germany in 2022 WC qualifying (different groups). Sources: UEFA.com, Wikipedia, ESPN.

**Chunk 16004–16039 (13 dangerous):**
- **Row 16005** — "next automatic Euro qualification after beating England 2019 = **2023**" — FALSE: they clinched **Euro 2020 automatic qualification on 14 Nov 2019** (after the 11 Oct 2019 England win). *Remedy:* answer is 2019/Euro 2020, or reword.
- **Row 16006** — "maintained world's **top 40** since 2010" — FALSE: ranking fell well below 40 (lowest ~67). *Remedy:* drop the claim.
- **Row 16007** — "relegated from Nations League A in **2023**" — FALSE: relegation was determined finishing last in the 2022-23 League A group, matches ending **Sep 2022**. *Remedy:* answer 2022.
- **Row 16008** — "hold a **2-0** Euro finals record v Netherlands" — FALSE: Euro meetings were L 0-1 (2000), W 3-2 (2004), W 2-0 (2020). *Remedy:* drop "2-0 record" premise.
- **Row 16009** — "**perfect** Euro finals record v Netherlands" — FALSE: lost 0-1 at **Euro 2000**. *Remedy:* drop "perfect" premise.
- **Row 16016** — "**At the 2014 FIFA World Cup**, Czechia's fiercest regional rival…" — false premise: Czechia did **not** play at the 2014 WC. *Remedy:* drop the WC framing (rivalry fact = Slovakia/Federal Derby).
- **Row 16017** — "**At the 2022 World Cup**, which Czech First League club had most players…" — false premise: Czechia did **not** qualify for 2022 (explanation itself says "qualifiers"). *Remedy:* reframe to qualifiers.
- **Row 16018** — "**At the 2022 World Cup**, which Czech striker led the attack" — false premise (not at 2022 WC). *Remedy:* reframe.
- **Row 16019** — "**At the 2022 World Cup**, which Czechia player held the Euro distance goal record" — false premise (not at 2022 WC; Schick's record is real but not "at" a tournament they didn't play). *Remedy:* reframe.
- **Row 16022** — "2006 stadium where Czechia did **not** play = Signal Iduna Park" — broken: Czechia played at **Gelsenkirchen, Cologne, Hamburg**, none of the four options; explanation's stadium list (AWD-Arena/Commerzbank-Arena/Gottlieb-Daimler-Stadion) is wrong and all four options are non-played → **non-unique**. *Remedy:* rebuild with the correct venues.
- **Row 16025** — "Czechia's **only independent qualification** was for 2006" — FALSE now: they **qualified for 2026**. *Remedy:* update (debut = 2006, but not "only").
- **Row 16030** — "Czechia hosted **Germany** in **2022 World Cup qualifying** at epet ARENA" — false premise: Czechia & Germany were in different 2022 WC qualifying groups; no such fixture. *Remedy:* remove/replace opponent.
- **Row 16037** — "2018 World Cup qualification relied heavily on **aerially dominant strikers**" — unverifiable soft narrative; Czechia also **failed** to qualify for 2018. UNVERIFIED→FAIL. *Remedy:* drop.

**Chunk 16040–16075 (11 dangerous):**
- **Row 16041 / 16047 / 16048** — "top-40 ranking through the 2010s/2020s (incl. 2018 & 2022 cycles)" — FALSE: ranking fell well below 40 (lowest ~67), and they failed the 2018/2022 cycles. *Remedy:* drop the top-40 premise.
- **Row 16049** — "2022 WC qualifier hosted outside Prague at Doosan Arena" — unverified/likely-fabricated: Czechia's 2022 home qualifiers were in Prague; no confirmed Plzeň qualifier. UNVERIFIED→FAIL. *Remedy:* verify venue or drop.
- **Row 16050** — "2022 qualifier v Belgium at fortuna Arena (cap 19,370)" — **non-unique**: option **epet ARENA = fortuna Arena** (same Slavia stadium, just a later sponsor name). *Remedy:* remove the duplicate-name distractor.
- **Row 16053** — "Prague stadium cap 19,370 = fortuna Arena" — **non-unique**: option **Eden Arena = fortuna Arena** (same stadium). *Remedy:* remove duplicate.
- **Row 16056** — "league that does NOT supply a core of the 2024 squad = Premier League" — FALSE: **Souček & Coufal (West Ham)** are core Premier League players. *Remedy:* pick a league that truly doesn't (e.g. Serie A/La Liga, but check uniqueness).
- **Row 16062** — "2022 qualifiers league NOT relied on = Serie A" — **non-unique** (La Liga also not relied on) and PL *was* relied on. *Remedy:* rebuild.
- **Row 16063** — "WC Czechia qualified for in the 21st century = 2006 (only one)" — FALSE now: they **also qualified for 2026**. *Remedy:* note 2026.
- **Row 16067** — "most 2006 WC squad players from Sparta Prague" — unverifiable obscure squad-composition count. UNVERIFIED→FAIL. *Remedy:* drop or verify.
- **Row 16075** — "Euro **knockout** matches v Portugal by 2012 = Three (1996, 2008, 2012)" — FALSE: only **two** were knockout (1996 QF, 2012 QF); **2008 was a group game**. *Remedy:* answer Two.

**Chunk 16076–16139 (29 dangerous):**
- **Row 16076 / 16077 / 16116** — "Euro **knockout** matches v Portugal = Three (1996/2008/2012)" — FALSE: only **two** knockout (1996 QF, 2012 QF); **2008 was a group game**. *Remedy:* answer Two.
- **Row 16078** — "WCs Czechia **qualified for** as independent nation = One" — FALSE now: also **qualified for 2026**. *Remedy:* update.
- **Row 16089 / 16131 / 16135** — "Doosan Arena/Plzeň hosted a 2022 WC qualifier (v Estonia)" — FALSE: Czechia's 2022 home qualifiers were at **Sinobo Stadium & Letná (Prague) and Ostrava**; the Estonia game was at **Stadion Letná, Prague** (no Plzeň qualifier). *Remedy:* Prague.
- **Row 16090 / 16099** — "Prague stadium cap 19,370 = fortuna Arena" — **non-unique**: option **Eden Arena = fortuna Arena** (same Slavia ground). *Remedy:* drop duplicate.
- **Row 16091** — "2022 play-off v Sweden hosted at epet ARENA (Letná)" — FALSE: the play-off SF was played **in Sweden** (Solna), not Prague; also "epet ARENA (Letná)" conflates Slavia's Eden ground with Sparta's Letná. *Remedy:* rebuild.
- **Row 16093** — "Koller scored **two** headers v USA (2006)" — FALSE: Koller scored **one**; Rosický scored the brace. *Remedy:* fix.
- **Row 16096** — "Slovakia faced Slovenia while Czechia played Belgium (Sep 2021)" — obscure unverified cross-fixture. UNVERIFIED→FAIL.
- **Row 16097** — "2022 World Cup **group stage** match…" — false premise: Czechia did **not** play the 2022 WC. *Remedy:* drop.
- **Row 16098** — "2022 WC qualifier: Czechia hosted **England**" — false premise: England was **not** in Czechia's 2022 WCQ group (that was Euro 2020 qualifying). *Remedy:* reframe to Euro 2020 Q.
- **Row 16100** — "stadium cap **18,887** = epet ARENA" — FALSE capacity (it's **19,370**) and **non-unique** (epet = fortuna option). *Remedy:* fix.
- **Row 16101** — "2024 World Cup qualifier" — no such tournament (WCs are 2022/2026). False premise. *Remedy:* reframe.
- **Row 16103** — "Rosický = most-capped in the 2006 opener XI" — FALSE: 105 was his career total; in 2006 **Nedvěd/Šmicer** had more caps. *Remedy:* fix.
- **Row 16104** — "Brückner's 2006 formation = 4-4-2 diamond" — unverifiable/non-unique (explanation hedges 4-2-3-1). UNVERIFIED→FAIL.
- **Row 16107** — "creative winger supporting Schick (2022 Q) = Václav Černý" — unverifiable/non-unique soft claim (Provod also fits). UNVERIFIED→FAIL.
- **Row 16113** — "finished above **Scotland** in Euro 2012 qualifying" — **non-unique**: Czechia (2nd) also finished above **Lithuania** (an option). *Remedy:* fix.
- **Row 16114** — "nation that finished **second** in Czechia's Euro 2020 qualifying group = England" — FALSE: **England finished 1st**, Czechia 2nd. *Remedy:* answer Czechia / reword.
- **Row 16118** — "2006 starting midfielder who played for **Sparta Prague** = Galásek" — FALSE: Galásek was at **Nürnberg** in 2006 (ex-Ajax). *Remedy:* fix.
- **Row 16119** — "2022 WC cycle ranking = world's top 40" — FALSE: below 40 (lowest ~67). *Remedy:* drop.
- **Row 16122 / 16125** — "historically produces aerially dominant strikers / winning-header striker" — unverifiable soft narrative (and no decisive "winning header" in the 3-0 v USA). UNVERIFIED→FAIL.
- **Row 16123** — "In the **2026 World Cup qualifiers**, when did Czechia secure **Euro 2024** automatic qualification?" — incoherent: conflates two different campaigns. *Remedy:* reframe to Euro 2024 Q.
- **Row 16130** — "faced **Slovakia** in 2018 WCQ Group C" — FALSE: Slovakia was in **Group F**; not in Czechia's group. *Remedy:* fix.
- **Row 16132** — "**2023-24** Nations League B" — no 2023-24 senior NL edition exists (editions: 2022-23, 2024-25). *Remedy:* fix edition.
- **Row 16138** — "beat England 2-1 (Euro 2020 Q) at Sinobo Stadium" — **non-unique**: option **Eden Arena = Sinobo Stadium** (same ground, former name). *Remedy:* drop duplicate.

**Chunk 16141–16200 (6 dangerous):**
- **Row 16164** — "relegated from Nations League A in **2023**" — FALSE: the 2022-23 League A group stage ended **Sep 2022**, when relegation was determined. *Remedy:* answer 2022. (cf. 16007)
- **Row 16169** — "played **Turkey** in a 2022 WC qualifier on 16 Nov 2021" — FALSE: that fixture was v **Estonia** (Stadion Letná); Turkey was not in Czechia's group. *Remedy:* fix opponent.
- **Row 16172 / 16173** — "In which **year** did Schick score his Euro goal? **2020**" — the goal was scored **14 June 2021**; **2021** is offered as a distractor → answer should be 2021. *Remedy:* answer 2021.
- **Row 16177** — "Since which **World Cup finals** has Czechia been captained by Souček? 2022" — false premise: Czechia did **not** play the 2022 WC finals. *Remedy:* reframe to the 2022 qualifying campaign.
- **Row 16191** — "When did a Bundesliga-supplemented Czechia squad **last qualify** for the WC? 2006" — FALSE now: they **last qualified for 2026**. *Remedy:* update.

**Chunk 16201–16260 (14 dangerous):**
- **Row 16203** — "first met Slovakia in WC qualifying = 2006" — FALSE: their only WCQ meeting was **2010** (Group 3, drew 2-2). *Remedy:* 2010.
- **Row 16208** — "last faced Slovakia in a WC qualifier = 2022" — FALSE: they were **not** in the same 2022 group; last (only) WCQ meeting was **2010**. *Remedy:* 2010.
- **Row 16209** — "last faced Slovakia in WCQ = 2018 qualifiers" — FALSE: not in the same 2018 group; last was **2010**. *Remedy:* 2010.
- **Row 16214** — "qualify for its **only** FIFA World Cup = 2006" — FALSE now: also **qualified for 2026**. *Remedy:* update.
- **Row 16225** — "Bundesliga-supplemented core **qualify for the WC** = 2022 qualifiers" — FALSE: Czechia **failed** to qualify for 2022 (3rd, lost play-off). *Remedy:* fix.
- **Row 16230** — "Schick's **World Cup debut** = 2022" — FALSE: Czechia did **not** play the 2022 WC; Schick has **never** played a WC. *Remedy:* remove.
- **Row 16235** — "Čech set his clean-sheet record **during 2006 qualifiers**" — FALSE/unverifiable: the record accrued across his 2002-2016 career, not "during 2006 qualifiers." UNVERIFIED→FAIL.
- **Row 16242** — "Souček first captained Czechia **at a FIFA World Cup** = 2022" — false premise: Czechia did **not** play the 2022 WC. *Remedy:* reframe to qualifiers.
- **Row 16250** — "hosted 2022 qualifier v Belgium at epet ARENA" — **non-unique**: option **Fortuna Arena = epet ARENA** (same Sinobo/Slavia ground). *Remedy:* drop duplicate.
- **Row 16254** — "Czech city whose stadium hosted a 2022 WC qualifier = Plzeň" — FALSE: 2022 home qualifiers were in **Prague & Ostrava**, not Plzeň. *Remedy:* Prague/Ostrava.
- **Row 16255** — "Slavia Prague contributed **more** players to the 2022 squad" — unverifiable exact squad count. UNVERIFIED→FAIL.
- **Row 16256** — "Czech club in the **2022 UCL group stage** = Sparta Prague" — FALSE: it was **Viktoria Plzeň** (Group C with Bayern/Barça/Inter). *Remedy:* Viktoria Plzeň.
- **Row 16257** — "Czech club with players in the 2022 squad = Slavia Prague" — **non-unique**: Sparta Prague (an option) also had squad players. *Remedy:* rebuild.
- **Row 16260** — "Czech club in the **2023/24 UCL group stage** = Sparta Prague" — FALSE: Sparta were eliminated in UCL Q3 (Copenhagen) and played the **Europa League**; no Czech club was in the 2023-24 UCL group stage. *Remedy:* fix.

**Chunk 16261–16330 (39 dangerous):**
*Stadium-name facts: Slavia's ground = Eden = Sinobo = Fortuna Arena = epet ARENA (one stadium, cap 19,370). Sparta's Letná = Generali Arena is a DIFFERENT stadium. Doosan Arena = Plzeň, Andrův Stadion = Olomouc. Confirmed: Czechia's 2018 & 2022 home qualifiers were at Eden/Sinobo & Letná (Prague), Ostrava, never Plzeň.*
- **Row 16291 / 16294 / 16295 / 16304** — answer "**epet ARENA (Letná)**" — FALSE conflation: epet ARENA **is** Slavia's Eden ground, **not** Sparta's Letná; capacity given (18,887) is Letná's. Also options repeat the same stadium (Eden/Fortuna) → non-unique. *Remedy:* rebuild.
- **Row 16302 / 16305 / 16306 / 16307 / 16308** — **non-unique**: options pair **Fortuna Arena + epet ARENA** (same stadium). *Remedy:* drop duplicate-name distractor.
- **Row 16292 (San Marino) / 16293 (Norway)** — "hosted at **Doosan Arena/Plzeň**" — FALSE: both 2018 qualifiers were at **Eden Arena, Prague**. *Remedy:* Eden/Prague.
- **Row 16296 (Belarus) / 16297 (Estonia) / 16298 (Wales) / 16299** — wrong 2022 venues: Belarus was at **Ostrava**, Estonia at **Letná (Prague)**, Wales at **Sinobo (Prague)** — none at Doosan/Andrův. *Remedy:* fix venues.
- **Row 16310** — "Doosan & Andrův host 2026 qualifiers" — unverified venue claim. UNVERIFIED→FAIL.
- **Row 16261** — "**Sparta**'s frequent UCL group play fed the 2022 squad" — misleading: the 2022-cycle UCL club was **Viktoria Plzeň**; Sparta were not UCL regulars. *Remedy:* fix.
- **Row 16263 / 16264** — "Slavia/Sparta supplied the **most** players (2022/2006)" — unverifiable exact squad counts. UNVERIFIED→FAIL.
- **Row 16272** — "Rosický scored in Czechia's **2-0 win over Ghana** (2006)" — FALSE: Czechia **lost 0-2** to Ghana and scored nothing. *Remedy:* remove.
- **Row 16273** — "**Schick** scored in the 2-1 v England (2019)" — FALSE: scorers were **Brabec & Ondrášek**. *Remedy:* fix.
- **Row 16276** — "**Ondrášek scored both** goals v England (2019)" — FALSE: **Brabec & Ondrášek** scored one each. *Remedy:* fix.
- **Row 16280** — "2020 Euro **quarter-final** goal" — explanation describes the **R16 v Netherlands** (wrong match) + soft "aerial striker" archetype. *Remedy:* rebuild.
- **Row 16283** — "won the Ballon d'Or in a **World Cup year** = Nedvěd" — FALSE: Nedvěd won **2003**, which is **not** a WC year (explanation admits it). *Remedy:* remove.
- **Row 16285** — "**Sparta Prague** midfielder = Masopust" — FALSE: Masopust plays for **Slavia**. *Remedy:* fix.
- **Row 16286** — "features for **Sparta Prague** in UCL = Holeš" — FALSE: Holeš is a **Slavia** player. *Remedy:* fix.
- **Row 16289** — "Schick header v Netherlands in **2022 WC qualifiers**" — false premise: Czechia didn't play NL in 2022 WCQ (that header was Euro 2020). *Remedy:* reframe.
- **Row 16314** — "which striker **debuted** at the 2006 WC" — **non-unique**: the entire squad (incl. Baroš) debuted there (Czechia's only WC). *Remedy:* rebuild.
- **Row 16315 / 16322** — "Czech striker **at the 2018/2022 World Cup**" — false premise: Czechia missed both tournaments. *Remedy:* remove.
- **Row 16316 / 16318** — "Koller scored **3 / two headed** goals at 2006 WC" — FALSE: Koller scored **one** (v USA). *Remedy:* fix.
- **Row 16317** — "Schick scored **4 goals** in 2022 WCQ" — unverified goal tally. UNVERIFIED→FAIL.
- **Row 16319 / 16320** — "aerially dominant strikers powered 2006/2018 qualification" — unverifiable soft narrative. UNVERIFIED→FAIL.
- **Row 16323** — "aerially dominant striker who led the line at 2006 = **Baroš**" — FALSE: that archetype is **Koller**; Baroš was a pacey forward. *Remedy:* Koller.
- **Row 16324** — "Koller scored **against Ghana** (2006)" — FALSE: Czechia lost 0-2 to Ghana; Koller scored v USA. *Remedy:* fix.
- **Row 16326** — "Škoda's aerial headers key in 2018 WCQ" — unverifiable soft claim. UNVERIFIED→FAIL.
- **Row 16327** — "which 2022 squad fed by Sparta/Slavia = the 2022 squad" — circular + self-referential explanation + Czechia had no 2022 WC squad. *Remedy:* remove.

**Chunk 16331–16400 (11 dangerous):**
- **Row 16341** — "captain of the **failed 2006** WC qualification = Nedvěd" — FALSE premise: Czechia **qualified** for 2006. *Remedy:* remove.
- **Row 16342** — "captain at the **2006 World Cup** = Nedvěd" — FALSE: **Galásek** captained at 2006 (Nedvěd had retired after Euro 2004). *Remedy:* Galásek.
- **Row 16367** — "attacking focal point **at the 2022 FIFA World Cup** = Schick" — false premise: Czechia didn't play the 2022 WC. *Remedy:* reframe to qualifiers.
- **Row 16369** — "Čech had 124 caps **for the 2014 World Cup squad**" — false premise: Czechia missed the 2014 WC. *Remedy:* remove.
- **Row 16380** — "Čech kept the **most clean sheets in 2018 WC qualifying**" — unverifiable/likely wrong (Čech retired in 2016, mid-cycle). UNVERIFIED→FAIL.
- **Row 16381 / 16382 / 16383** — "Čech **set** his clean-sheet record **during the 2014/2018 WC qualifiers**" — FALSE: the career record wasn't established in a single campaign. UNVERIFIED→FAIL. (cf. 16235)
- **Row 16386** — "Čech's **2018 World Cup** performances built his record" — false premise: Czechia missed the 2018 WC. *Remedy:* remove.
- **Row 16387** — "2022 home qualifier at epet ARENA = vs Estonia" — FALSE: Estonia was at **Stadion Letná**; the epet/Sinobo (Eden) games were Belgium & Wales. *Remedy:* fix.
- **Row 16388** — "2018 WC qualifiers home stadium = Fortuna Arena" — **non-unique**: option **epet ARENA = Fortuna Arena** (same Eden ground). *Remedy:* drop duplicate.

**Chunk 16401–16470 (10 dangerous):**
- **Row 16401** — "manager ensured consistent **top-40** ranks through the 2010s = Jarolím" — FALSE: ranking dropped below 40 (lowest ~67); Jarolím only coached 2016-18. *Remedy:* remove.
- **Row 16426** — "manager started a **Sparta Prague striker** at 2006 = Brückner" — false premise: the 2006 strikers (**Koller**=Dortmund/Monaco, **Baroš**=Villa/Lyon) were **not** at Sparta. *Remedy:* rebuild.
- **Row 16449 / 16468 / 16469** — "captained **at the 2022 FIFA World Cup** = Souček" — false premise: Czechia did **not** play the 2022 WC. *Remedy:* reframe to qualifiers.
- **Row 16456** — "which **Czechia opponent** lost a Euro final to Germany via golden goal? **Czechia**" — incoherent/self-referential (Czechia isn't its own opponent; the fact is real but the framing is broken). *Remedy:* reword.
- **Row 16458** — "opponents who beat Czechia 2-0 (2006) = Ghana and Italy" — **non-unique**: options include both "**Ghana and Italy**" and "**Italy and Ghana**" (same pair). *Remedy:* drop the duplicate.
- **Row 16460** — "player archetype that starred at 2006 = tactically intelligent midfielder" — **non-unique/soft**: a "technically sound midfielder" (option) and "aerially dominant striker" also starred. *Remedy:* rebuild.
- **Row 16461** — "Euro 2020 player from **Sparta Prague** = Souček" — FALSE: Souček came from **Slavia** and was a **West Ham** player by Euro 2020. *Remedy:* fix.
- **Row 16467** — "captained the 2022 WCQ **against Slovakia** = Souček" — false premise: Czechia & Slovakia were **not** in the same 2022 WCQ group (no such match). *Remedy:* remove.

**Chunk 16471–16550 (17 dangerous):**
- **Row 16474** — "captained **at the 2022 FIFA World Cup** = Souček" — false premise (Czechia missed the 2022 WC). *Remedy:* qualifiers.
- **Row 16479** — "Souček rose through **Sparta Prague's** academy" — FALSE: he's a **Slavia** youth product. *Remedy:* fix.
- **Row 16482** — "2022-squad player who played for **Sparta Prague** = Holeš" — FALSE: Holeš is a **Slavia** player. *Remedy:* fix.
- **Row 16483 / 16484** — "from **Sparta Prague's 2023-24 UCL squad** at the 2022 WC = Čvančara" — FALSE: Sparta did **not** reach the 2023-24 UCL group stage (Europa League), and Czechia didn't play the 2022 WC. *Remedy:* rebuild.
- **Row 16485** — "Souček played UCL for **Sparta Prague** before the 2022 WC" — FALSE: he was at **West Ham** (ex-Slavia), never Sparta; no 2022 WC. *Remedy:* rebuild.
- **Row 16489** — "record for **most World Cup goals** = Koller" — FALSE: **Rosický** scored 2 at 2006, Koller 1. *Remedy:* Rosický.
- **Row 16490** — "main striker at the **2024 FIFA World Cup** qualifiers" — no such tournament. *Remedy:* reframe (Euro 2024 / 2026 WCQ).
- **Row 16513** — "Schick's 50-yard goal in a **2022 WC qualifier** v Scotland" — FALSE: that goal was at **Euro 2020**; Czechia didn't play Scotland in 2022 WCQ. *Remedy:* fix competition.
- **Row 16525 / 16528** — "Euro 2020 R16 win over NL = **3-2**" — FALSE: it was **2-0**. *Remedy:* fix score.
- **Row 16529** — "which player scored in the 2-0 v NL (Euro 2020) = Holeš" — **non-unique** (Holeš **and** Schick both scored; Holeš scored 1st, not "the second goal"). *Remedy:* rebuild.
- **Row 16527 / 16530** — "**Jankto** scored in the 2-1 v England (2019)" — FALSE: scorers were **Brabec & Ondrášek**. *Remedy:* fix.
- **Row 16532** — "Koller scored the first goal in the 3-0 v Germany (2007)" — FALSE: scorers were **Sionko, Matějovský & Plašil** (and it was a Euro 2008 **qualifier**, not a friendly). *Remedy:* rebuild.
- **Row 16539** — "Rosický scored the **opening** goal v USA (2006)" — FALSE: **Koller** opened (5'); Rosický scored 36' & 76'. *Remedy:* fix.
- **Row 16546** — "Jiráček scored in the 2012 Euro **QF** (1-1 v Portugal)" — FALSE: the QF was a **1-0 loss** to Portugal; Czechia didn't score. *Remedy:* fix.

**Chunk 16551–16640 (42 dangerous):**
- **Row 16560** — "attacking focal point **at the 2022 FIFA World Cup**" — false premise (missed the WC). *Remedy:* qualifiers.
- **Row 16563** — "**top scorer at 2006 WC** = Koller (2 of 3)" — FALSE: **Rosický** scored 2, Koller 1. *Remedy:* Rosický.
- **Row 16573** — "2006 WC goal not from a nation that reached a final = Koller" — incoherent (all four options are Czech players; explanation nonsensical). *Remedy:* remove.
- **Row 16575 / 16583** — "Souček/squad from **Sparta** UEFA runs **helped qualify for the 2022 WC**" — FALSE: Souček is Slavia/West Ham, and Czechia **failed** to qualify for 2022. *Remedy:* rebuild.
- **Row 16582 / 16594 / 16604** — "ranked in the **top 40** (2010s-2020s streak)" — FALSE: ranking fell below 40. *Remedy:* drop.
- **Row 16588 / 16589** — "**Rosický** captained at the 2006 WC" — FALSE: **Galásek** captained 2006. *Remedy:* Galásek.
- **Row 16599** — "rival faced in a **2022 WC qualifier** = Slovakia" — false premise: not in the same 2022 WCQ group. *Remedy:* remove.
- **Stadium cluster (Rows 16605, 16606, 16607, 16610, 16614, 16622, 16628, 16629, 16630, 16633, 16634, 16639)** — **non-unique**: options pair **Fortuna Arena + epet ARENA** (or Eden), all the same Slavia ground. *Remedy:* drop duplicate-name distractor.
- **Rows 16608, 16609, 16618, 16636, 16637, 16638** — answer "**epet ARENA (Letná)**" / cap 18,887 attributed to epet — FALSE conflation: epet ARENA **is** Slavia's Eden (19,370), not Sparta's Letná (18,887). *Remedy:* rebuild.
- **Rows 16612 / 16616 / 16632 (Estonia), 16613 (Belarus), 16626 (Norway)** — wrong venue: Estonia was at **Letná**, Belarus at **Ostrava**, Norway (2016) at **Eden** — none at Doosan/Plzeň. *Remedy:* fix.
- **Row 16611** — "Doosan hosted a WCQ first (2011)" — unverified/likely-fabricated venue history. UNVERIFIED→FAIL.
- **Rows 16620 / 16621 / 16627** — 2018 WCQ (Germany/Norway) "= epet ARENA" — wrong club ("fortress of Sparta") + non-unique (epet=fortuna); the games were at **Eden, Prague**. *Remedy:* fix.
- **Row 16619** — "**2010 World Cup playoff vs Montenegro**" — false premise: that was the **Euro 2012** play-off; Czechia didn't reach the 2010 WC play-offs. *Remedy:* rebuild.
- **Row 16624** — "2022 WCQ vs **Albania**" — false premise: Albania wasn't in Czechia's 2022 WCQ group (that was Euro 2024 Q). *Remedy:* fix.
- **Row 16625** — "2-1 v England (Euro 2020 Q) = Sinobo Stadium" — **non-unique**: option **Eden Arena = Sinobo Stadium** (same ground). *Remedy:* drop duplicate.
- **Row 16631** — "2022 WCQ home game vs **Sweden** = fortuna Arena" — false premise: the Sweden play-off SF was **away (in Sweden)**; no home WCQ v Sweden. *Remedy:* remove.

**Chunk 16641–16740 (17 dangerous):**
- **Row 16643 / 16663 / 16671 / 16672** — "focal point/top scorer **at the 2022 FIFA World Cup**" — false premise (Czechia missed it). *Remedy:* qualifiers.
- **Row 16646** — "Schick scored **4 goals** at Euro 2020" — FALSE: he scored **5** (joint Golden Boot). *Remedy:* 5.
- **Row 16677** — "Škoda's aerial dominance secured a 2018 WCQ win" — unverifiable soft claim. UNVERIFIED→FAIL.
- **Row 16681** — "3-0 v Germany (Munich) = **2007 friendly**" — FALSE: it was a **Euro 2008 qualifier**. *Remedy:* fix.
- **Row 16686** — "WC squad with highest average age since 2006" — false premise: Czechia had **no** 2010/2014/2018 WC squads (missed all). *Remedy:* remove.
- **Row 16692** — "WC Czechia **qualified for** as an independent nation = 2006 (only one)" — FALSE now: also **qualified for 2026**. *Remedy:* update.
- **Row 16695** — "first captained **at the 2022 FIFA World Cup** = Souček" — false premise (no 2022 WC). *Remedy:* reframe.
- **Row 16707 / 16708 / 16709 / 16710 / 16724** — "faced Portugal in a **Euro 2008 quarter-final/knockout**" — FALSE: Czechia were **eliminated in the Euro 2008 group** (the 1-3 loss to Portugal was a group game); their only Portugal Euro knockouts were 1996 & 2012. *Remedy:* fix.
- **Row 16716** — "nation Czechia did NOT finish behind (Euro 2020 Q) = Albania" — **non-unique**: they only finished behind **England**, so Croatia & Slovakia (options) also qualify. *Remedy:* rebuild.
- **Row 16734** — "finished **second** in Czechia's Euro 2024 group = Albania" — FALSE: **Albania finished 1st**, Czechia 2nd. *Remedy:* Czechia.

**Chunk 16741–16893 (25 dangerous) — completes Czechia:**
- **Row 16745** — "nation that qualified for 2014 (that Czechia missed) = Ghana" — **non-unique**: **Italy & USA** (options) also qualified for 2014. *Remedy:* rebuild.
- **Row 16756** — "rival faced in **2006 WC qualifiers** = Slovakia" — false premise: not in the same 2006 WCQ group (first met in 2010). *Remedy:* fix.
- **Row 16758 / 16760** — "= **epet ARENA (Letná)**" — conflation (epet = Slavia's Eden, not Letná) + non-unique (Eden/Fortuna option). *Remedy:* rebuild.
- **Row 16759** — "2018 WCQ v Norway = epet ARENA or Fortuna Arena" — **non-unique**: both are the same Eden ground. *Remedy:* drop duplicate.
- **Row 16761** — "decisive 2022 WCQ v **Sweden** = epet ARENA" — false premise: the Sweden play-off was **away (Sweden)**. *Remedy:* remove.
- **Row 16763** — "Plzeň stadium hosted **2022 WC qualifiers** = Doosan" — false premise: no 2022 qualifier in Plzeň. *Remedy:* fix.
- **Row 16776 / 16777 / 16778** — "faced Portugal in a **Euro 2008 quarter-final**" — FALSE: that was a **group** game (Czechia exited the Euro 2008 group). *Remedy:* fix.
- **Row 16810** — "two stadiums hosting 2018 WCQ = Doosan & Andrův" — FALSE: 2018 home qualifiers were at **Eden, Prague**. *Remedy:* fix.
- **Row 16841** — "UEFA nation that lost a play-off SF 1-0 aet (like Czechia) = **Sweden**" — FALSE: Sweden **won** that SF (then lost the final). *Remedy:* rebuild.
- **Row 16842 / 16844 / 16893** — "top-40 (2010s-2020s) mainstay" — FALSE: Czechia's ranking fell below 40. *Remedy:* drop. (16844 also self-referential.)
- **Row 16850** — "WC Czechia **qualified for** as independent = 2006 (only)" — FALSE now: also **qualified for 2026**. *Remedy:* update.
- **Row 16853 / 16855** — "captained at the **2006 WC** = Nedvěd" — FALSE: **Galásek** captained 2006. *Remedy:* Galásek.
- **Row 16860** — "led the team for the **2024 World Cup** qualifiers" — no such tournament. *Remedy:* reframe.
- **Row 16866** — "captain **at the 2022 FIFA World Cup** = Souček" — false premise (missed the WC). *Remedy:* qualifiers.
- **Row 16871 / 16872 / 16889** — "hosted 2022 WCQ at **Doosan/Plzeň/Andrův**" — false premise: 2022 home games were Prague & Ostrava. *Remedy:* fix.
- **Row 16879** — "qualified for the 2022 play-off due to a **strong European club core**" — misleading: they reached the play-off via **UEFA Nations League ranking** (finished 3rd in group). *Remedy:* fix.
- **Row 16890** — "host some 2026 WCQ in Plzeň & Olomouc" — unverified venue claim. UNVERIFIED→FAIL.

---

## DR Congo (batch-2 rows 16894–17345)

**Fact base (sourced):** DR Congo **qualified for the 2026 WC** (1st since 1974/Zaire), via **2nd in CAF Group B → African play-off (beat Cameroon, then Nigeria) → beat Jamaica** in the intercontinental final. 2026 is their first *as DR Congo* but **2nd overall** (1974 as Zaire) — so "first ever WC" is wrong. 2018 WCQ group: **Tunisia/Libya/Guinea** (no Nigeria/Zambia). AFCON: 2 titles (1968, 1974); 2015 & 2023 = SF. Sources: Al Jazeera/ESPN/Wikipedia.

**Chunk 16894–16940 (12 dangerous):**
- **Row 16894** — "**after beating Senegal**, DR Congo qualified for 2026" — FALSE: Senegal **won** the group; DRC qualified via the play-offs (beat Cameroon, Nigeria, Jamaica). *Remedy:* reframe.
- **Row 16896** — "**At the 2014 World Cup**, which DRC club developed players" — false premise: DRC didn't play the 2014 WC. *Remedy:* drop the WC framing.
- **Row 16899** — "At the 2026 WCQ, reached the 2023 AFCON QF in which year? 2023" — incoherent (mixes two competitions) and the 2023 AFCON was **played in 2024**. *Remedy:* rebuild.
- **Row 16902** — "DRC players compete in which European league? Premier League" — **non-unique**: they have players in **all four** offered leagues. *Remedy:* rebuild.
- **Row 16912** — "finished **third** in CAF Group B" — FALSE: DRC finished **2nd** (runner-up, went to play-offs). *Remedy:* second.
- **Row 16913 / 16918** — "2026 = DRC's **first ever** WC appearance" — FALSE: their first was **1974 (as Zaire)**; 2026 is the first *under the DR Congo name*. *Remedy:* qualify "as DR Congo".
- **Row 16914 / 16926** — "which **other** nation also qualified after a 50-yr gap / under its current name = **DR Congo**" — self-referential (answer is the subject nation). *Remedy:* rebuild.
- **Row 16923** — "2018 WCQ **vs Nigeria** at Stade des Martyrs" — false premise: DRC's 2018 group was **Tunisia/Libya/Guinea** (no Nigeria). *Remedy:* fix opponent.
- **Row 16932** — "2018 WCQ hosting **Zambia**" + answer "**2016-09-01 00:00:00**" — false fixture (Zambia not in DRC's group) **and** Excel date-corruption in the answer. *Remedy:* rebuild.
- **Row 16937** — "qualified for **nine** AFCONs (2006-2023)" — FALSE: DRC reached ~**7** AFCON finals in that span (missed 2008/2010/2012). *Remedy:* fix count.

**Chunk 16941–17010 (11 dangerous):**
- **Row 16943** — "2015 AFCON **host nation** DR Congo beat in the QF = Congo" — FALSE: the **host was Equatorial Guinea**; Congo (Brazzaville) wasn't the host. *Remedy:* drop "host nation".
- **Row 16947** — "2026 group stage, North African rival DR Congo would likely face = Morocco" — speculative & false: their 2026 group is **Portugal/Colombia/Uzbekistan** (no Morocco). *Remedy:* remove.
- **Row 16955** — "AFCON tournaments since 2006 = **seven** (list includes 2010)" — FALSE: **six** (2006/2013/2015/2017/2019/2023); they missed 2010. *Remedy:* six.
- **Row 16958** — "first faced **Tunisia** in WCQ = 2006" — unverified specific "first meeting" claim. UNVERIFIED→FAIL.
- **Row 16960** — "Mbemba's **World Cup debut** = 2014" — false premise: DRC didn't play the 2014 WC; Mbemba has never played a WC. *Remedy:* remove.
- **Row 16962** — "faced **Morocco** in a WC qualifier in **2021**" — FALSE: that was the **2022 WCQ play-off in March 2022**, not 2021. *Remedy:* 2022.
- **Row 16965** — "reached the AFCON **QF** in which year? 2023" — **non-unique**: **2015** (an option) also reached the QF/SF. *Remedy:* rebuild.
- **Row 16980** — "hosted Senegal (2026 WCQ), when? **2024-11-01 00:00:00**" — Excel date-corruption in the answer. *Remedy:* rebuild.
- **Row 16981** — "hosted **Morocco** in a **2018** WC qualifier" — false premise: DRC's 2018 group was Tunisia/Libya/Guinea; they met Morocco in **2022 WCQ**. *Remedy:* fix.
- **Row 17009** — "CAF nation that (unlike DRC) qualified for 2018 = Senegal" — **non-unique**: **Nigeria & Morocco** (options) also qualified for 2018 (and explanation wrongly includes Ghana). *Remedy:* rebuild.
- **Row 17010** — "CAF nation whose 2026 qualification ended a **longer** absence than DRC = **DR Congo**" — self-referential/incoherent (a team can't exceed its own absence). *Remedy:* remove.

**Chunk 17015–17090 (9 dangerous):**
- **Row 17015** — "CAF club that reached a CWC final = **Wydad Casablanca** (2022)" — FALSE: Wydad never reached a CWC final (the African finalists were TP Mazembe 2010 & **Raja Casablanca** 2013; none of the options qualify). *Remedy:* rebuild.
- **Row 17020** — "CAF team that qualified for 2018 (unlike DRC) = Tunisia" — **non-unique**: **Nigeria, Senegal, Egypt** (all options) also qualified for 2018. *Remedy:* rebuild.
- **Row 17023 / 17027** — "which team/squad **like DR Congo** … = **DR Congo**" — self-referential (the question implies a peer but answers the subject). *Remedy:* rebuild.
- **Row 17030** — "AFCON streak 2015 to 2023" — FALSE: DRC **missed 2021**, so there was no continuous 2015-2023 streak. *Remedy:* fix.
- **Row 17033** — "AFCON rival that is **North African** = Morocco" — **non-unique**: Egypt, Tunisia, Algeria (all options) are North African too. *Remedy:* rebuild.
- **Row 17044** — "Wissa scored **3 goals in 2023 World Cup qualifiers**" — muddled framing (no 2023 WC) + unverified specific tally. UNVERIFIED→FAIL.
- **Row 17089 / 17090** — "Mbemba **debuted in a FIFA World Cup** (2014/2018)" — false premise: DRC didn't play 2014/2018; Mbemba has **never** played a WC. *Remedy:* remove.

**Chunk 17091–17177 (12 dangerous):**
- **Row 17098 / 17100 / 17120 / 17121** — "Mbemba's **World Cup debut** (2022) / played at the **2018 WC** / 2026 WC **knockout stage** / selected for **2018 WC**" — false premise: DRC has **not played a WC** (1974→2026), and the 2026 tournament hasn't been played yet. *Remedy:* reframe to qualifiers.
- **Row 17117** — "Masuaku in their **2018 World Cup squad**" — false premise (no 2018 WC for DRC). *Remedy:* reframe.
- **Row 17118 / 17148** — "**2023 World Cup squad** / **World Cup debut in 2024**" — no such tournaments. *Remedy:* fix.
- **Row 17143** — "forward who **debuted in the 2026 qualifying cycle** = Wissa" — FALSE: Wissa debuted earlier (2019). *Remedy:* pick a genuine new cap.
- **Row 17164** — "DR Congo name **never used** for a WC qualification = DR Congo" — FALSE now: they **qualified as DR Congo** for 2026. *Remedy:* update.
- **Row 17169** — "DRC player at Napoli = **André-Frank Zambo Anguissa**" — FALSE: Anguissa is a **Cameroon** international. *Remedy:* remove.
- **Row 17173** — "DRC player who **debuted in 2023** after four European leagues = Wissa" — inconsistent (Wissa debuted earlier) + unverified. UNVERIFIED→FAIL.
- **Row 17174** — "player who **debuted in the 2026 qualifiers** = Silas Katompa" — inconsistent with his earlier (~2021) debut. UNVERIFIED→FAIL.

**Chunk 17179–17258 (15 dangerous):**
- **Row 17181** — "player in their **2023 World Cup squad**" — no such tournament. *Remedy:* fix.
- **Row 17185** — "player who **missed** the 2014 WCQ = Mbokani" — contradicts its own explanation (Mbokani was a key striker **in** that campaign). *Remedy:* rebuild.
- **Row 17193** — "scored in the 2023 AFCON opener **after 2026 WC qualification**" — chronologically false: the 2023 AFCON (early 2024) preceded the **March 2026** qualification. *Remedy:* fix order.
- **Row 17195** — "DRC player who starred for **Bayern Munich** = Choupo-Moting" — FALSE: Choupo-Moting is a **Cameroon** international. *Remedy:* remove.
- **Row 17199** — "in European leagues **for the 2022 World Cup**" — false premise (DRC didn't play the 2022 WC). *Remedy:* reframe to qualifiers.
- **Row 17215** — "2026 qualifying rival who also faced them at AFCON = Mauritania" — unverified/likely-false (no DRC-Mauritania AFCON meeting). UNVERIFIED→FAIL.
- **Row 17216** — "West African rival in the 2018 WCQ = Ghana" — FALSE: Ghana wasn't in DRC's group; the West African opponent was **Guinea**. *Remedy:* Guinea.
- **Row 17221** — "rival that is **also a regular AFCON participant** = Nigeria" — **non-unique**: Morocco & Egypt (options) are regulars too. *Remedy:* rebuild.
- **Row 17222** — "rival that is North African, not West African = Morocco" — **non-unique**: Algeria, Tunisia, Egypt (all options) are North African. *Remedy:* rebuild.
- **Row 17224** — "squad era following TP Mazembe's 2010 landmark = **2018** WCQ" — FALSE: the **2014 WCQ** (an option) was the next campaign. *Remedy:* 2014.
- **Row 17230** — "2022 WCQ vs **Senegal** at Stade des Martyrs" — false premise: Senegal wasn't in DRC's 2022 WCQ group (that was 2026). *Remedy:* fix opponent.
- **Row 17231** — "Stade des Martyrs hosted the **2024 AFCON final**" — FALSE: the 2023 AFCON (early 2024) was hosted by **Côte d'Ivoire** (final in Abidjan). *Remedy:* remove.
- **Row 17236** — "2026 qualification **decider** at Stade des Martyrs" — FALSE: the decider was the intercontinental play-off **v Jamaica in Mexico** (neutral venue). *Remedy:* fix.
- **Row 17242** — "DRC star who played for **Inter Milan** = Tisserand" — unverified/likely-false club history. UNVERIFIED→FAIL.
- **Row 17249** — "Bakambu played at the **2018 World Cup** venue in Saransk" — false premise: DRC didn't play the 2018 WC. *Remedy:* remove.

**Chunk 17259–17345 (23 dangerous) — completes DR Congo:**
- **Row 17264** — "2026 WCQ opponent that is North African = Egypt" — false premise: Egypt wasn't in DRC's 2026 group (Senegal/Sudan/Togo/Mauritania/South Sudan). *Remedy:* fix.
- **Row 17267 / 17345** — "their **first** World Cup (2026)" / "first time for country" — FALSE: 1974 (as Zaire) was their first; 2026 is the second / first *as DR Congo*. *Remedy:* qualify the claim.
- **Row 17270** — "TP Mazembe **beat Internazionale** in the 2010 SF" — FALSE: the SF was v **Internacional (Brazil)**; **Inter Milan beat** TP Mazembe 3-0 in the **final**. *Remedy:* rebuild.
- **Row 17276** — "league not represented **at the 2022 World Cup**" — false premise (DRC didn't play the 2022 WC). *Remedy:* reframe to qualifiers.
- **Row 17279 / 17286 / 17290 / 17294** — "which **other** nation [did X] = **DR Congo**" — self-referential (and 17279/17290 non-unique: Ivory Coast/Senegal/Ghana also qualified-2026 / reached the 2015 SF). *Remedy:* rebuild.
- **Row 17292** — "nation hosting DRC's 2026 WC = United States" — **non-unique**: USA, **Canada & Mexico** all co-host. *Remedy:* rebuild.
- **Row 17298** — "North African AFCON rival = Morocco" — **non-unique**: Egypt/Tunisia/Algeria (all options) are North African. *Remedy:* rebuild.
- **Row 17303 / 17307** — "2017 AFCON QF opponent = Tunisia / Egypt" — FALSE: DRC lost the 2017 QF to **Ghana** (1-2). *Remedy:* Ghana.
- **Row 17305** — "2023 AFCON **QF** opponent = Egypt" — FALSE: the QF was v **Guinea** (3-1); Egypt was the **R16**. *Remedy:* Guinea.
- **Row 17312** — "rival that qualified ahead of DRC for 2014 = Ivory Coast (same group)" — FALSE: DRC's 2014 group was won by **Cameroon**; IC was in a different group. *Remedy:* Cameroon.
- **Row 17313** — "round DRC reached at the 2023 AFCON = the **quarter-finals**" — understated: they reached the **semi-finals** (4th). *Remedy:* semi-finals.
- **Row 17316 / 17317** — "**decisive/clinching** 2026 qualifier at Stade des Martyrs" — FALSE: the deciders (African play-off, then v Jamaica) were at **neutral venues** (Morocco / Mexico). *Remedy:* fix.
- **Row 17321 / 17324** — "which WC did DRC **fail to qualify for** = 2014 / 2022" — **non-unique**: they failed **all** of 2010/2014/2018/2022 (all options). *Remedy:* rebuild.
- **Row 17329** — "why DRC faced **Morocco** in the 2019 AFCON group" — false premise: Morocco was in **Group D**, DRC in **Group A** (they didn't meet). *Remedy:* remove.
- **Row 17331** — "why DRC faced North Africans in **2018 WC qualifiers** = AFCON group draws" — wrong mechanism (it was the **CAF WC-qualifying** draw, not AFCON). *Remedy:* fix.
- **Row 17336** — "hosted **Senegal** at Stade des Martyrs for 2022 WCQ" — false premise: Senegal wasn't in DRC's 2022 WCQ group (that was 2026). *Remedy:* fix.

## Ecuador — rows 17346–18086 (liveness on QA_PASSED_b2.md rows) — 143 FAIL

**Fact base (sourced):** Ecuador finished **4th in CONMEBOL qualifying for BOTH 2014 and 2022** (so "4th place"/"group-stage exit" answers are non-unique). The 2014/2022 home qualifiers were at **Casa Blanca / Estadio Atahualpa in Quito**, **NOT** Guayaquil's **Estadio Monumental**. **Enner Valencia** scored **all 3** of Ecuador's 2022 goals (Ecuador scored 4 total across the group, not 2). **Moisés Caicedo**'s move to Chelsea was **Aug 2023** (after the 2022 WC, a **British** record, after Enzo Fernández's Jan 2023 fee — not a world record). **Independiente del Valle** won the **Copa Sudamericana in Oct 2022**, AFTER World Cup qualifying ended (March 2022). Defenders **Estupiñán, Torres, Preciado, Hincapié** all started, so "which defender started" is non-unique. Several rows carry Excel **date-corruption** in the answer cell. Sources: Wikipedia (Ecuador NT, 2022 WC Group A, CONMEBOL qualifying), transfer reporting.

### Row 17348 — Ecuador (hard) — FAIL: wrong points (2022~26, 2026~29, not 19->26)
**Q:** After losing 0-4 to Uruguay in 2022 qualifying, Ecuador improved their CONMEBOL points total by how many in the 2026 cycle?
**Answer:** 7 points
**Why it fails:** Ecuador's CONMEBOL points were ~26 in the 2022 cycle (4th) and ~29 in the 2026 cycle (2nd, their best-ever finish, after a 3-point deduction). The claim of '19 for 2022' and '26 for 2026' (a 7-point increase) is wrong on both figures — the real improvement was roughly 26->29 (~3 points).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Use the actual totals (~26 in 2022, ~29 in 2026).

### Row 17356 — Ecuador (easy) — FAIL: wrong stadium (Brazil qualifier was in Quito)
**Q:** At the 2022 World Cup qualifiers, which Ecuador stadium hosted a key match against Brazil?
**Answer:** Estadio Monumental
**Why it fails:** Ecuador's home 2022 qualifier vs Brazil (1-1, 27 Jan 2022) was played in QUITO at the Estadio Rodrigo Paz Delgado (Casa Blanca) — Ecuador use Quito's altitude for qualifiers — NOT the sea-level Estadio Monumental in Guayaquil.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the answer to Estadio Rodrigo Paz Delgado (Quito).

### Row 17366 — Ecuador (hard) — FAIL: non-unique (Valencia scored 3 at both 2014 and 2022)
**Q:** At which 2014 World Cup did Ecuador's Enner Valencia score three goals?
**Answer:** 2014 FIFA World Cup
**Why it fails:** Enner Valencia scored THREE goals at the 2014 World Cup (1 v Switzerland, 2 v Honduras) AND three at the 2022 World Cup (2 v Qatar, 1 v Netherlands) — his record 6 WC goals split 3+3. So 'which WC did he score three goals' is non-unique (2014 and 2022 both qualify).
**Source:** https://en.wikipedia.org/wiki/Enner_Valencia
**Remedy:** He scored 3 at both 2014 and 2022; make it unique.

### Row 17370 — Ecuador (medium) — FAIL: non-unique (Valencia scored 3 at both 2014 and 2022)
**Q:** At which FIFA World Cup did Ecuador's Enner Valencia score three goals?
**Answer:** 2014 World Cup
**Why it fails:** Valencia scored 3 WC goals at 2014 AND 3 at 2022, so 'at which World Cup did he score three goals' has two valid answers among the options.
**Source:** https://en.wikipedia.org/wiki/Enner_Valencia
**Remedy:** He scored 3 at both 2014 and 2022.

### Row 17374 — Ecuador (easy) — FAIL: wrong timing (Caicedo->Chelsea was Aug 2023, after the 2022 WC)
**Q:** Before Ecuador's 2022 World Cup, which Chelsea signing was a record transfer?
**Answer:** Moisés Caicedo
**Why it fails:** Moisés Caicedo's record move to Chelsea was in August 2023 — AFTER the 2022 World Cup, not before. At the 2022 World Cup he was a Brighton player. The 'before the 2022 World Cup' framing is false.
**Source:** https://en.wikipedia.org/wiki/Mois%C3%A9s_Caicedo
**Remedy:** Caicedo joined Chelsea in 2023, after the 2022 WC.

### Row 17375 — Ecuador (easy) — FAIL: wrong stadium (qualifiers in Quito, not Guayaquil)
**Q:** During 2022 World Cup qualifying, which Ecuador stadium held key home matches?
**Answer:** Estadio Monumental
**Why it fails:** Ecuador's home 2022 World Cup qualifiers were played in Quito (Estadio Rodrigo Paz Delgado, altitude ~2,800m) to exploit altitude — NOT the sea-level Estadio Monumental in Guayaquil. The Monumental is the largest stadium but was not the key qualifier venue.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change to a Quito venue (Estadio Rodrigo Paz Delgado / Atahualpa).

### Row 17376 — Ecuador (hard) — FAIL: false (highest FIFA ranking was 10th in 2013, not 30th)
**Q:** Ecuador achieved their highest FIFA ranking after which successful CONMEBOL qualifying campaign?
**Answer:** The 2022 cycle
**Why it fails:** Ecuador's highest-ever FIFA ranking was 10th (June 2013), not 30th, and it came around the 2014 qualifying cycle — not the 2022 cycle. Both the '30th' figure and the '2022 cycle' attribution are wrong.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** Ecuador peaked at 10th (June 2013).

### Row 17377 — Ecuador (easy) — FAIL: non-unique (both Senegal and Netherlands beat Qatar)
**Q:** Ecuador beat Qatar 2-0 in the 2022 opener. Which other 2022 host group opponent also beat Qatar?
**Answer:** Senegal
**Why it fails:** Qatar lost all three Group A games — to Ecuador, Senegal (3-1) AND the Netherlands (2-0). Both Senegal and the Netherlands are listed options, so 'which other group opponent also beat Qatar' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Both Senegal and the Netherlands beat Qatar.

### Row 17385 — Ecuador (medium) — FAIL: false premise (Honduras is CONCACAF, not CONMEBOL)
**Q:** Ecuador qualified for the 2014 World Cup. Which CONMEBOL nation did they beat 2-1 in the 2014 group stage?
**Answer:** Honduras
**Why it fails:** Ecuador did beat Honduras 2-1 at the 2014 World Cup, but Honduras is a CONCACAF nation, not CONMEBOL. The 'which CONMEBOL nation' framing is false, and none of the options are a CONMEBOL side Ecuador beat 2-1.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_E
**Remedy:** Drop 'CONMEBOL' (Honduras is CONCACAF).

### Row 17387 — Ecuador (medium) — FAIL: non-unique (Ecuador finished 4th in both 2014 and 2022)
**Q:** Ecuador qualified for which World Cup by finishing 4th in CONMEBOL?
**Answer:** 2022 World Cup
**Why it fails:** Ecuador finished 4th in CONMEBOL qualifying for BOTH the 2014 and 2022 World Cups (Uruguay 5th in each). With both years as options, 'which World Cup did Ecuador qualify for by finishing 4th' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Ecuador also finished 4th for 2014; add a distinguishing detail.

### Row 17396 — Ecuador (easy) — FAIL: false premise (no 2023 Copa America)
**Q:** Ecuador's 2022 World Cup loss to Senegal occurred before which 2023 continental final?
**Answer:** Copa America final
**Why it fails:** There was no 2023 Copa América — the tournament was held in 2021 and 2024. So 'the 2023 Copa America final' did not exist; the answer is to a non-event.
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica
**Remedy:** No Copa America final occurred in 2023.

### Row 17399 — Ecuador (easy) — FAIL: false (Ecuador drew Brazil 1-1, did not win 2-0)
**Q:** Ecuador's 2022 World Cup qualifier win over Brazil was at which high-altitude stadium?
**Answer:** Estadio Rodrigo Paz Delgado
**Why it fails:** Ecuador did NOT beat Brazil 2-0 in 2022 qualifying — their home game (27 Jan 2022, in Quito) was a 1-1 draw, and the away game was a 0-2 loss. There was no 2-0 win over Brazil. (The Quito venue is correct, but the result is wrong.)
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** It was a 1-1 draw, not a 2-0 win.

### Row 17400 — Ecuador (hard) — FAIL: false (2026 was Ecuadors 5th qualification, not 3rd)
**Q:** Ecuador's 2026 World Cup qualification was their third successful CONMEBOL campaign after which years?
**Answer:** 2014 and 2022
**Why it fails:** Ecuador have qualified for five World Cups via CONMEBOL — 2002, 2006, 2014, 2022 and 2026 — so 2026 is their FIFTH successful campaign, not their third. The answer '2014 and 2022' omits 2002 and 2006.
**Source:** https://en.wikipedia.org/wiki/Ecuador_at_the_FIFA_World_Cup
**Remedy:** Ecuador also qualified for 2002 and 2006; 2026 is the 5th.

### Row 17410 — Ecuador (medium) — FAIL: non-unique (4th in both 2014 and 2022)
**Q:** For which FIFA World Cup did Ecuador qualify by finishing 4th in CONMEBOL?
**Answer:** 2022 World Cup
**Why it fails:** Ecuador finished 4th in CONMEBOL for both 2014 and 2022, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Ecuador also finished 4th for 2014.

### Row 17416 — Ecuador (medium) — FAIL: wrong count (7 Copas since 2007, not 6)
**Q:** How many Copa Américas has Ecuador played in since 2006?
**Answer:** Six tournaments
**Why it fails:** Ecuador has played in SEVEN Copa Américas since 2006 — 2007, 2011, 2015, 2016 (Centenario), 2019, 2021 and 2024 — not six. (Row 17415 correctly says seven.)
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** The count is seven.

### Row 17417 — Ecuador (medium) — FAIL: non-unique threshold (49 goals also satisfies 45+)
**Q:** How many goals has Ecuador's Enner Valencia scored?
**Answer:** 40+ goals
**Why it fails:** Enner Valencia has ~49 international goals, which satisfies the '45+' option as well as '40+' (and 35+, 30+). With 45+ also a listed option and true, the answer is non-unique — '45+' is the tighter correct bound.
**Source:** https://en.wikipedia.org/wiki/Enner_Valencia
**Remedy:** Use 45+ (he has ~49); avoid nested thresholds.

### Row 17420 — Ecuador (medium) — FAIL: wrong count (5 home wins, not 6)
**Q:** In 2022 FIFA World Cup qualifying, Ecuador's home record in Quito was how many wins?
**Answer:** Six wins
**Why it fails:** Ecuador had FIVE home wins in 2022 CONMEBOL qualifying (with home draws v Brazil and Argentina and one home defeat), not six. (Row 17421 correctly says five; 17422 wrongly says seven.)
**Source:** https://www.aljazeera.com/sports/2022/11/13/world-cup-2022-ecuador
**Remedy:** It was five home wins.

### Row 17422 — Ecuador (medium) — FAIL: wrong count (5 home wins, not 7 of 8)
**Q:** In 2022 World Cup qualifying, Ecuador's home record in Quito was how many wins?
**Answer:** Seven wins
**Why it fails:** Ecuador won FIVE home qualifiers in the 2022 cycle, not seven — and there were nine home games (not eight). They drew at home v Brazil and Argentina.
**Source:** https://www.aljazeera.com/sports/2022/11/13/world-cup-2022-ecuador
**Remedy:** It was five home wins out of nine home games.

### Row 17423 — Ecuador (easy) — FAIL: false (Brazil drew 1-1 in Quito, did not lose)
**Q:** In 2022 World Cup qualifying, which CONMEBOL team struggled in Ecuador's high-altitude Quito?
**Answer:** Brazil
**Why it fails:** Brazil did NOT lose to Ecuador in Quito in 2022 qualifying — the game was a 1-1 draw (27 Jan 2022). Brazil were unbeaten throughout 2022 CONMEBOL qualifying.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** It was a 1-1 draw; Brazil lost no qualifier.

### Row 17428 — Ecuador (medium) — FAIL: self-referential + British (not world) record
**Q:** In a 2022 World Cup group stage match, Ecuador faced the Netherlands. Which CONMEBOL nation's player later made a world-record transfer?
**Answer:** Ecuador
**Why it fails:** The question's answer is 'Ecuador' — the very nation it's describing (self-referential). Also, Caicedo's £115m move to Chelsea was a BRITISH transfer record, not a world record (the world record is Neymar's €222m).
**Source:** https://en.wikipedia.org/wiki/Mois%C3%A9s_Caicedo
**Remedy:** Reframe; Caicedo's was a British record, not a world record.

### Row 17438 — Ecuador (medium) — FAIL: false (England beat Iran 6-2, not 2-0)
**Q:** In the 2022 World Cup group stage, Ecuador beat Qatar 2-0. Which other team won their opening match 2-0?
**Answer:** England
**Why it fails:** England did NOT win their 2022 opener 2-0 — they beat Iran 6-2. The team that won its 2022 opener 2-0 was Brazil (2-0 v Serbia), a listed option.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Change the answer to Brazil (2-0 v Serbia); England won 6-2.

### Row 17439 — Ecuador (medium) — FAIL: self-referential + non-unique
**Q:** In the 2022 World Cup group stage, Ecuador drew 1-1 with the Netherlands. Which CONMEBOL nation has been a regular Copa América participant?
**Answer:** Ecuador
**Why it fails:** The answer 'Ecuador' is self-referential (the subject of the question), and all four options — Ecuador, Paraguay, Colombia, Peru — are regular Copa América participants, so the answer is also non-unique.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** Reframe; the trait is shared by all options.

### Row 17449 — Ecuador (medium) — FAIL: Excel date-corruption in the answer cell
**Q:** In which 2022 World Cup qualifier did Ecuador first use Estadio Rodrigo Paz Delgado?
**Answer:** 2021-10-01 00:00:00
**Why it fails:** The answer is mangled to a datetime serial '2021-10-01 00:00:00' (Excel corruption). The intended answer (per the explanation, vs Bolivia in October 2021) is not rendered as a clean option.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Restore the answer to a clean date/label (October 2021).

### Row 17453 — Ecuador (medium) — FAIL: non-unique (4th in both 2014 and 2022)
**Q:** In which CONMEBOL World Cup qualifying cycle did Ecuador achieve their highest final position?
**Answer:** 2022 qualifying
**Why it fails:** Ecuador's highest CONMEBOL finish among the listed cycles is tied — they finished 4th in BOTH 2014 and 2022 (and 2nd in 2026, not listed). So '2022' is not their uniquely highest position among the options.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** 2014 was also 4th; their best was actually 2026 (2nd).

### Row 17454 — Ecuador (medium) — FAIL: false (top-4 finishes in 2002/2006/2014, not first in 2022)
**Q:** In which CONMEBOL World Cup qualifying cycle did Ecuador first finish in the top four?
**Answer:** The 2022 cycle
**Why it fails:** Ecuador's first top-four CONMEBOL finish was NOT the 2022 cycle — they qualified 2nd in 2002, 3rd in 2006 and 4th in 2014, all top-four finishes before 2022.
**Source:** https://en.wikipedia.org/wiki/Ecuador_at_the_FIFA_World_Cup
**Remedy:** Their first top-four was 2002 (2nd).

### Row 17455 — Ecuador (hard) — FAIL: non-unique (reached group stage in 2014 and 2022)
**Q:** In which FIFA World Cup did Ecuador reach the group stage?
**Answer:** 2014 World Cup
**Why it fails:** Ecuador reached the group stage in both 2014 and 2022 (both listed options), so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Ecuador_at_the_FIFA_World_Cup
**Remedy:** They reached the group stage in 2014 and 2022 (and 2002, 2006).

### Row 17458 — Ecuador (hard) — FAIL: non-unique (group-stage exit in 2014 and 2022)
**Q:** In which FIFA World Cup edition was Ecuador eliminated in the group stage?
**Answer:** 2022 FIFA World Cup
**Why it fails:** Ecuador were eliminated in the group stage in both 2014 and 2022 (and 2002), so with both years as options the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Ecuador_at_the_FIFA_World_Cup
**Remedy:** Group-stage exits came in 2002, 2014 and 2022.

### Row 17463 — Ecuador (medium) — FAIL: non-unique (4th in both 2014 and 2022)
**Q:** In which World Cup did Ecuador qualify by finishing 4th in CONMEBOL?
**Answer:** 2022
**Why it fails:** Ecuador finished 4th in CONMEBOL for both 2014 and 2022 — both options — so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** 2014 was also a 4th-place finish.

### Row 17471 — Ecuador (hard) — FAIL: non-unique (4th in both 2014 and 2022)
**Q:** In which World Cup qualifiers did Ecuador finish 4th in CONMEBOL?
**Answer:** 2022 World Cup qualifiers
**Why it fails:** Ecuador finished 4th in CONMEBOL for both 2014 and 2022, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** 2014 was also a 4th-place finish.

### Row 17472 — Ecuador (hard) — FAIL: wrong cycle (altitude first decisive in 2002, not 2006)
**Q:** In which World Cup qualifiers did Ecuador's altitude in Quito first prove decisive?
**Answer:** 2006 World Cup qualifiers
**Why it fails:** Ecuador's Quito altitude advantage FIRST proved decisive in the 2002 qualifying cycle — when they first qualified, famously beating Brazil and Argentina at home in Quito — not 2006.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** It first proved decisive in the 2002 cycle.

### Row 17475 — Ecuador (hard) — FAIL: wrong cycle (first used Rodrigo Paz Delgado for 2022, not 2006)
**Q:** In which World Cup qualifying cycle did Ecuador first use Estadio Rodrigo Paz Delgado?
**Answer:** 2006 World Cup qualifiers
**Why it fails:** Ecuador's national team historically played in Quito at the Estadio Olímpico Atahualpa; they switched to the Estadio Rodrigo Paz Delgado (Casa Blanca) for the 2022 qualifiers because Atahualpa was being demolished (~2020). So they first used Rodrigo Paz Delgado in the 2022 cycle, not 2006.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** They first used Rodrigo Paz Delgado for the 2022 cycle.

### Row 17476 — Ecuador (hard) — FAIL: wrong cycle (altitude major factor from 2002, not 2006)
**Q:** In which World Cup qualifying cycle did Ecuador's altitude advantage in Quito become a major factor?
**Answer:** 2006 World Cup qualifiers
**Why it fails:** Ecuador's Quito altitude advantage became a major factor in the 2002 qualifying cycle (their first qualification), not 2006.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** It became a major factor in the 2002 cycle.

### Row 17481 — Ecuador (medium) — FAIL: false (2022 qualifiers were at Casa Blanca, Quito)
**Q:** In which year did Ecuador host a 2022 World Cup qualifier at their largest stadium?
**Answer:** 2021
**Why it fails:** Ecuador's 2022 World Cup qualifiers were hosted at the Casa Blanca (Estadio Rodrigo Paz Delgado) in Quito for altitude — NOT the Estadio Monumental in Guayaquil. (They only used the Monumental in the later 2026 cycle.)
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** The 2022 qualifiers were in Quito (Rodrigo Paz Delgado).

### Row 17485 — Ecuador (medium) — FAIL: false (2022 qualifiers were at Casa Blanca, Quito)
**Q:** In which year did Ecuador's largest stadium, Estadio Monumental, host a key World Cup qualifier?
**Answer:** 2022
**Why it fails:** The Estadio Monumental (Guayaquil) did NOT host Ecuador's key 2022 World Cup qualifiers — those were at the Casa Blanca (Rodrigo Paz Delgado) in Quito. The Monumental was used only for the later 2026 cycle.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** The 2022 qualifiers were in Quito.

### Row 17493 — Ecuador (easy) — FAIL: Excel date-corruption in the answer cell
**Q:** What score did Ecuador lose by to Senegal in the 2022 World Cup?
**Answer:** 2026-01-02 00:00:00
**Why it fails:** The answer is mangled to a datetime '2026-01-02 00:00:00' instead of the score. Ecuador lost 1-2 to Senegal (Senegal won 2-1).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Restore the score (Ecuador 1-2 Senegal).

### Row 17498 — Ecuador (medium) — FAIL: false (2022 qualifiers were in Quito, not the Monumental)
**Q:** When did Ecuador host a 2022 World Cup qualifier at Estadio Monumental?
**Answer:** 2021
**Why it fails:** Ecuador's 2022 World Cup home qualifiers were at the Casa Blanca (Rodrigo Paz Delgado) in Quito for altitude, not the Estadio Monumental in Guayaquil.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** The 2022 qualifiers were in Quito.

### Row 17501 — Ecuador (medium) — FAIL: non-unique (4th in both 2014 and 2022)
**Q:** When did Ecuador qualify by finishing 4th in CONMEBOL?
**Answer:** 2022 World Cup
**Why it fails:** Ecuador finished 4th in CONMEBOL for both 2014 and 2022 (both options), so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** 2014 was also a 4th-place finish.

### Row 17502 — Ecuador (medium) — FAIL: non-unique (4th in both 2014 and 2022)
**Q:** When did Ecuador qualify for the World Cup by finishing 4th in CONMEBOL?
**Answer:** 2022 World Cup
**Why it fails:** Ecuador finished 4th in CONMEBOL for both 2014 and 2022, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** 2014 was also a 4th-place finish.

### Row 17508 — Ecuador (medium) — FAIL: Excel date-corruption in the answer cell
**Q:** When did Ecuador's Moisés Caicedo set a South American midfield transfer record?
**Answer:** 2023-08-01 00:00:00
**Why it fails:** The answer is mangled to a datetime '2023-08-01 00:00:00' instead of a clean date. Caicedo's move was completed in August 2023.
**Source:** https://en.wikipedia.org/wiki/Mois%C3%A9s_Caicedo
**Remedy:** Restore the answer to 'August 2023'.

### Row 17519 — Ecuador (easy) — FAIL: false (2022 qualifiers were in Quito, not the Monumental)
**Q:** Where did Ecuador's coach make a 2022 World Cup qualifying tactical decision for home advantage at their largest stadium?
**Answer:** Estadio Monumental
**Why it fails:** The Estadio Monumental (Guayaquil) is Ecuador's largest stadium but was NOT the venue for their 2022 World Cup home qualifiers — those were at the Casa Blanca (Rodrigo Paz Delgado) in Quito for altitude advantage.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** The 2022 home-advantage venue was Quito (Rodrigo Paz Delgado).

### Row 17520 — Ecuador (easy) — FAIL: non-unique (Ecuador also did not lose to Qatar)
**Q:** Which 2022 World Cup group opponent did Ecuador not lose to?
**Answer:** Netherlands
**Why it fails:** Ecuador beat Qatar, drew the Netherlands and lost to Senegal — so they 'did not lose to' BOTH Qatar and the Netherlands (both options), making the answer non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Ask which they drew (Netherlands) to make it unique.

### Row 17537 — Ecuador (easy) — FAIL: false (Netherlands is UEFA, not CONMEBOL; game was 1-1)
**Q:** Which CONMEBOL nation faced Ecuador at the 2022 FIFA World Cup?
**Answer:** Netherlands
**Why it fails:** The Netherlands is a UEFA nation, not CONMEBOL — no CONMEBOL side was in Ecuador's 2022 group (Qatar/Senegal/Netherlands). The explanation also wrongly says Ecuador 'lost 2-0' — it was a 1-1 draw.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Drop 'CONMEBOL'; the Netherlands is European, and the result was 1-1.

### Row 17541 — Ecuador (medium) — FAIL: non-unique (Ecuador 8th; all options finished above)
**Q:** Which CONMEBOL nation finished above Ecuador for 2018 WC qualification?
**Answer:** Peru
**Why it fails:** Ecuador finished 8th in 2018 CONMEBOL qualifying, so Peru, Colombia, Chile AND Paraguay (all options) finished above them — the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Ask which took the last (5th) spot (Peru) to make it unique.

### Row 17553 — Ecuador (easy) — FAIL: non-unique (all options are Copa regulars)
**Q:** Which CONMEBOL nation is a regular Copa América participant alongside Ecuador?
**Answer:** Brazil
**Why it fails:** All four options — Brazil, Paraguay, Chile, Uruguay — are regular Copa América participants, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica
**Remedy:** The trait is shared by every CONMEBOL nation.

### Row 17554 — Ecuador (easy) — FAIL: non-unique (Venezuela also reached the 2016 QF)
**Q:** Which CONMEBOL nation matched Ecuador's 2016 Copa América quarter-final run?
**Answer:** Peru
**Why it fails:** Both Peru AND Venezuela (listed options) reached the quarter-finals of the 2016 Copa América Centenario, so 'which matched Ecuador's QF run' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2016_Copa_Am%C3%A9rica_Centenario
**Remedy:** Venezuela also reached the 2016 QF.

### Row 17558 — Ecuador (easy) — FAIL: false (Chile missed the 2006 World Cup)
**Q:** Which CONMEBOL nation qualified for the 2006 and 2014 World Cups like Ecuador?
**Answer:** Chile
**Why it fails:** Chile did NOT qualify for the 2006 World Cup — they were absent (their WCs around then were 1998, 2010, 2014). So 'Chile qualified for 2006 and 2014 like Ecuador' is false; no listed option qualified for both 2006 and 2014.
**Source:** https://en.wikipedia.org/wiki/Chile_at_the_FIFA_World_Cup
**Remedy:** Chile missed 2006; the teams in both 2006 & 2014 were Brazil, Argentina, Ecuador.

### Row 17561 — Ecuador (easy) — FAIL: non-unique (Colombia also qualified for 2018)
**Q:** Which CONMEBOL nation qualified for the 2018 World Cup instead of Ecuador?
**Answer:** Peru
**Why it fails:** Both Peru (5th, via playoff) AND Colombia (4th, direct) qualified for the 2018 World Cup while Ecuador did not — so 'which qualified instead of Ecuador' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Colombia also qualified for 2018.

### Row 17568 — Ecuador (easy) — FAIL: self-referential (answer is Ecuador itself)
**Q:** Which CONMEBOL nation, like Ecuador in 2022, qualified for a World Cup by finishing 4th?
**Answer:** Ecuador
**Why it fails:** The question asks which CONMEBOL nation, LIKE Ecuador, finished 4th — but the answer is 'Ecuador' itself, which is self-referential.
**Source:** https://en.wikipedia.org/wiki/Ecuador_at_the_FIFA_World_Cup
**Remedy:** The answer must be a different nation.

### Row 17570 — Ecuador (easy) — FAIL: non-unique (all options are Copa regulars)
**Q:** Which CONMEBOL nation, like Ecuador, has also been a regular Copa América participant since 2006?
**Answer:** Colombia
**Why it fails:** Colombia, Bolivia, Venezuela and Paraguay are all regular Copa América participants since 2006, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica
**Remedy:** The trait is shared by all CONMEBOL nations.

### Row 17588 — Ecuador (medium) — FAIL: non-unique (Chile and Paraguay also finished ahead)
**Q:** Which CONMEBOL team finished ahead of Ecuador for 2010 World Cup qualification?
**Answer:** Uruguay
**Why it fails:** Ecuador finished 6th in 2010 CONMEBOL qualifying; Chile (2nd), Paraguay (3rd) AND Uruguay (5th) — all listed options — finished ahead of them, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Ask which took the last (5th) spot (Uruguay) to make it unique.

### Row 17593 — Ecuador (easy) — FAIL: false (Uruguay drew Ghana 1-1 and WON on penalties)
**Q:** Which CONMEBOL team, like Ecuador in 2022, also lost 2-1 to an African side in a World Cup?
**Answer:** Uruguay
**Why it fails:** Uruguay did NOT lose 2-1 to Ghana in the 2010 quarter-final — the game was 1-1 after extra time and Uruguay WON 4-2 on penalties (Suárez handball, Gyan missed pen). So there is no Uruguay '2-1 loss to an African side'.
**Source:** https://en.wikipedia.org/wiki/Uruguay_v_Ghana_(2010_FIFA_World_Cup)
**Remedy:** Uruguay beat Ghana on penalties; the premise is false.

### Row 17606 — Ecuador (easy) — FAIL: non-unique (all options are 2026 CB starters)
**Q:** Which Ecuador centre-back was a tactical starter for the 2026 World Cup cycle?
**Answer:** Piero Hincapié
**Why it fails:** All four options — Hincapié, Arboleda, Félix Torres, William Pacho — are Ecuador centre-backs; both Hincapié and Pacho are key 2026-cycle starters, so 'which CB was a tactical starter' is non-unique.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** Use non-CB distractors to make it unique.

### Row 17616 — Ecuador (easy) — FAIL: non-unique (all options first played a WC in 2022)
**Q:** Which Ecuador defender debuted at the 2022 FIFA World Cup?
**Answer:** Piero Hincapié
**Why it fails:** All four options — Hincapié, Estupiñán, Félix Torres, Arboleda — made their World Cup debut at the 2022 tournament (none played in 2014), so 'which defender debuted at the 2022 WC' is non-unique.
**Source:** https://en.wikipedia.org/wiki/Ecuador_at_the_FIFA_World_Cup
**Remedy:** Use distractors who debuted at a different WC.

### Row 17617 — Ecuador (easy) — FAIL: false framing (both debuted at the same 2022 WC)
**Q:** Which Ecuador defender debuted at the 2022 World Cup, before Estupiñán's first?
**Answer:** Piero Hincapié
**Why it fails:** Hincapié and Estupiñán BOTH made their World Cup debut at the 2022 tournament — so 'Hincapié debuted before Estupiñán's first' is false; their WC debuts were simultaneous.
**Source:** https://en.wikipedia.org/wiki/Ecuador_at_the_FIFA_World_Cup
**Remedy:** Both debuted at the 2022 WC; remove the 'before' framing.

### Row 17619 — Ecuador (easy) — FAIL: non-unique (Estupinan also debuted at 2022)
**Q:** Which Ecuador defender made his World Cup debut in 2022?
**Answer:** Piero Hincapié
**Why it fails:** Both Hincapié and Estupiñán (a defender, listed option) made their World Cup debut at the 2022 tournament, so 'which defender debuted in 2022' is non-unique.
**Source:** https://en.wikipedia.org/wiki/Ecuador_at_the_FIFA_World_Cup
**Remedy:** Use non-defender distractors or a CB-specific trait.

### Row 17625 — Ecuador (easy) — FAIL: non-unique (Estupinan & Torres also started)
**Q:** Which Ecuador defender started a 2022 World Cup match for tactical defensive quality?
**Answer:** Piero Hincapié
**Why it fails:** Ecuador's settled 2022 back line (Preciado-Hincapié-Torres-Estupiñán) all started — both Estupiñán and Félix Torres (listed options) started for 'defensive quality' too, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Use a Hincapie-specific trait (e.g. Leverkusen, centre-back).

### Row 17626 — Ecuador (easy) — FAIL: non-unique (Estupinan also started v Senegal)
**Q:** Which Ecuador defender started against Senegal in the 2022 World Cup?
**Answer:** Piero Hincapié
**Why it fails:** Estupiñán (a listed option) also started against Senegal, so 'which defender started' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Use non-defender distractors.

### Row 17627 — Ecuador (easy) — FAIL: non-unique (Torres & Preciado also started all 3)
**Q:** Which Ecuador defender started all group matches at the 2022 FIFA World Cup?
**Answer:** Piero Hincapié
**Why it fails:** Both Félix Torres and Ángelo Preciado (listed options) also started all three 2022 group matches, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Use distractors who did not start all three.

### Row 17628 — Ecuador (easy) — FAIL: non-unique (Hincapie & Torres also started all 3)
**Q:** Which Ecuador defender started all three 2022 World Cup matches?
**Answer:** Pervis Estupiñán
**Why it fails:** Estupiñán did start all three, but so did Hincapié and Félix Torres (both listed options) — the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Use distractors who did not start all three.

### Row 17629 — Ecuador (easy) — FAIL: non-unique (Estupinan & Torres also started)
**Q:** Which Ecuador defender started at the 2022 FIFA World Cup?
**Answer:** Piero Hincapié
**Why it fails:** Estupiñán and Félix Torres (listed options) also started at the 2022 World Cup, so 'which defender started' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Use non-defender distractors.

### Row 17630 — Ecuador (easy) — FAIL: non-unique (Preciado also started the 2024 Copa)
**Q:** Which Ecuador defender started at the 2024 Copa America?
**Answer:** Piero Hincapié
**Why it fails:** Ángelo Preciado (a listed defender option) also started for Ecuador at the 2024 Copa América, so 'which defender started' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2024_Copa_Am%C3%A9rica
**Remedy:** Use non-defender distractors.

### Row 17631 — Ecuador (medium) — FAIL: non-unique (Estupinan also started)
**Q:** Which Ecuador defender started in the 2022 World Cup group stage?
**Answer:** Piero Hincapié
**Why it fails:** Estupiñán (a listed option) also started in the 2022 group stage, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Use non-defender distractors.

### Row 17632 — Ecuador (easy) — FAIL: non-unique (Estupinan & Torres also started v Qatar)
**Q:** Which Ecuador defender started in their 2022 World Cup win over Qatar?
**Answer:** Piero Hincapié
**Why it fails:** Estupiñán and Félix Torres (listed options) also started in the 2-0 win over Qatar, so 'which defender started' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Use non-defender distractors.

### Row 17633 — Ecuador (easy) — FAIL: false (Hincapie & Estupinan each started all 3 - tied)
**Q:** Which Ecuador defender started more World Cup 2022 matches, Hincapié or Estupiñán?
**Answer:** Piero Hincapié
**Why it fails:** Hincapié and Estupiñán each started all three of Ecuador's 2022 matches, so neither started 'more' — they are tied. The answer 'Hincapié' is wrong.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** They started an equal number (3 each).

### Row 17634 — Ecuador (easy) — FAIL: non-unique (Estupinan & Torres also started v Senegal)
**Q:** Which Ecuador defender started the 2022 World Cup match against Senegal?
**Answer:** Piero Hincapié
**Why it fails:** Estupiñán and Félix Torres (listed options) also started against Senegal, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Use non-defender distractors.

### Row 17635 — Ecuador (easy) — FAIL: non-unique (Estupinan also started v Netherlands)
**Q:** Which Ecuador defender started versus the Netherlands in the 2022 World Cup?
**Answer:** Piero Hincapié
**Why it fails:** Estupiñán (a listed option) also started against the Netherlands, so 'which defender started' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Use non-defender distractors.

### Row 17636 — Ecuador (easy) — FAIL: non-unique (Estupinan also a 2026 defender)
**Q:** Which Ecuador defender was selected for the 2026 World Cup squad?
**Answer:** Piero Hincapié
**Why it fails:** Estupiñán (a listed option) is also a defender in Ecuador's 2026 squad, so 'which defender was selected' is non-unique.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** Use non-defender distractors or a CB-specific trait.

### Row 17643 — Ecuador (easy) — FAIL: wrong stadium (2014 qualifiers were at Atahualpa)
**Q:** Which Ecuador home qualifier for the 2014 World Cup leveraged their high-altitude stadium advantage?
**Answer:** Estadio Rodrigo Paz Delgado
**Why it fails:** For the 2014 qualifiers, Ecuador's national team played in Quito at the Estadio Olímpico Atahualpa — they only switched to the Rodrigo Paz Delgado (Casa Blanca) for the 2022 cycle (when Atahualpa was being demolished). So the 2014 altitude venue was Atahualpa, not Rodrigo Paz Delgado.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** The 2014 home venue was the Estadio Olimpico Atahualpa.

### Row 17645 — Ecuador (easy) — FAIL: duplicate option (Rodrigo Paz Delgado = Estadio de Liga)
**Q:** Which Ecuador home stadium for 2022 qualifiers is highest above sea level?
**Answer:** Estadio Rodrigo Paz Delgado
**Why it fails:** 'Estadio Rodrigo Paz Delgado' and 'Estadio de Liga Deportiva Universitaria' are the SAME stadium (LDU Quito's Casa Blanca). Both being options makes the 'highest altitude' answer non-unique / duplicated. (Atahualpa is also high-altitude.)
**Source:** https://en.wikipedia.org/wiki/Estadio_Rodrigo_Paz_Delgado
**Remedy:** Remove the duplicate-name option.

### Row 17669 — Ecuador (easy) — FAIL: false (Pekerman, not Rueda, coached Colombia at 2015 Copa)
**Q:** Which Ecuador manager at the 2014 World Cup also coached Colombia at Copa America 2015?
**Answer:** Reinaldo Rueda
**Why it fails:** Rueda managed Ecuador at the 2014 World Cup, but he did NOT coach Colombia at the 2015 Copa América — that was José Pékerman (a listed option). Rueda coached Colombia only from 2018.
**Source:** https://en.wikipedia.org/wiki/Reinaldo_Rueda
**Remedy:** Colombia's 2015 Copa coach was Pekerman.

### Row 17686 — Ecuador (easy) — FAIL: false (Alfaro coached AT the 2022 WC, left after)
**Q:** Which Ecuador manager left before the 2022 World Cup?
**Answer:** Gustavo Alfaro
**Why it fails:** Gustavo Alfaro did NOT leave before the 2022 World Cup — he managed Ecuador AT the tournament in Qatar and departed afterward (late 2022). The 'left before the 2022 World Cup' claim is false.
**Source:** https://en.wikipedia.org/wiki/Gustavo_Alfaro
**Remedy:** Alfaro coached at the 2022 WC and left after it.

### Row 17695 — Ecuador (easy) — FAIL: false (Bolillo Gomez was appointed earlier, for 2002)
**Q:** Which Ecuador manager was appointed earliest for his World Cup cycle?
**Answer:** Reinaldo Rueda
**Why it fails:** Among the options, Hernán Darío 'Bolillo' Gómez was appointed earliest — he managed Ecuador's 2002 World Cup cycle (from 1999), before Rueda's 2014 cycle. So Rueda was not 'appointed earliest'.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** Bolillo Gomez (2002 cycle) was appointed earlier than Rueda.

### Row 17709 — Ecuador (easy) — FAIL: wrong timing (transfer was 2023, after the 2022 WC)
**Q:** Which Ecuador midfielder was selected for the 2022 World Cup after his record transfer?
**Answer:** Moisés Caicedo
**Why it fails:** Caicedo's record transfer to Chelsea was August 2023 — AFTER the 2022 World Cup. He was a Brighton player at the 2022 WC, so he was not 'selected after his record transfer'.
**Source:** https://en.wikipedia.org/wiki/Mois%C3%A9s_Caicedo
**Remedy:** His Chelsea move came after the 2022 WC.

### Row 17719 — Ecuador (easy) — FAIL: contradiction (a 2023 transfer cannot be 'before the 2022 WC')
**Q:** Which Ecuador midfielder's 2023 transfer fee was a record before the 2022 World Cup?
**Answer:** Moisés Caicedo
**Why it fails:** The question is self-contradictory: Caicedo's transfer was in 2023, which cannot have been 'a record before the 2022 World Cup'. The move came after the 2022 WC.
**Source:** https://en.wikipedia.org/wiki/Mois%C3%A9s_Caicedo
**Remedy:** The transfer was 2023, after the 2022 WC.

### Row 17724 — Ecuador (easy) — FAIL: overstated (most expensive SA MIDFIELDER, not overall)
**Q:** Which Ecuador midfielder's 2023 transfer was the most expensive for a South American?
**Answer:** Moisés Caicedo
**Why it fails:** Caicedo's £115m move was the most expensive transfer for a South American MIDFIELDER — NOT the most expensive for a South American overall (Neymar's ~€222m move is far higher). The question drops 'midfielder', making the claim false.
**Source:** https://en.wikipedia.org/wiki/Mois%C3%A9s_Caicedo
**Remedy:** Add 'midfielder'; Neymar's SA transfer is more expensive.

### Row 17727 — Ecuador (easy) — FAIL: non-unique (Caicedo was also at Brighton in 2022)
**Q:** Which Ecuador player at the 2022 World Cup plays for Brighton?
**Answer:** Pervis Estupiñán
**Why it fails:** At the 2022 World Cup, BOTH Estupiñán and Caicedo (a listed option) were Brighton players — Caicedo only moved to Chelsea in 2023. So 'which player plays for Brighton' is non-unique.
**Source:** https://en.wikipedia.org/wiki/Mois%C3%A9s_Caicedo
**Remedy:** Caicedo was also a Brighton player at the 2022 WC.

### Row 17728 — Ecuador (easy) — FAIL: non-unique (Preciado & Caicedo also European-based)
**Q:** Which Ecuador player at the 2022 World Cup represented the squad's European growth?
**Answer:** Pervis Estupiñán
**Why it fails:** Multiple listed options were European-based at the 2022 World Cup — Estupiñán (Brighton), Preciado (Genk) and Caicedo (Brighton) — so 'which player represented the squad's European growth' is non-unique.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** The trait is shared by several squad members.

### Row 17729 — Ecuador (easy) — FAIL: non-unique (Caicedo & Estupinan also European-based)
**Q:** Which Ecuador player at the 2022 World Cup represents their growing European-based squad?
**Answer:** Piero Hincapié
**Why it fails:** Hincapié (Leverkusen), Caicedo (Brighton) and Estupiñán (Brighton) were all European-based at the 2022 World Cup, so 'which player represents the growing European-based squad' is non-unique.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** The trait is shared by several squad members.

### Row 17736 — Ecuador (easy) — FAIL: wrong timing (transfer 2023, after his 2022 WC debut)
**Q:** Which Ecuador player debuted at the 2022 World Cup after a record transfer?
**Answer:** Moisés Caicedo
**Why it fails:** Caicedo's record transfer (Chelsea, Aug 2023) came AFTER his 2022 World Cup debut, so 'debuted at the 2022 WC after a record transfer' is false — he was a Brighton player at that tournament.
**Source:** https://en.wikipedia.org/wiki/Mois%C3%A9s_Caicedo
**Remedy:** His record transfer came after, not before, the 2022 WC.

### Row 17739 — Ecuador (easy) — FAIL: non-unique (Caicedo also debuted in the 2022 qualifiers)
**Q:** Which Ecuador player debuted in the 2022 World Cup qualifiers?
**Answer:** Jeremy Sarmiento
**Why it fails:** Caicedo (a listed option) debuted in October 2020 during the 2022 qualifying cycle, the same campaign as Sarmiento — so 'which player debuted in the 2022 WC qualifiers' is non-unique.
**Source:** https://en.wikipedia.org/wiki/Mois%C3%A9s_Caicedo
**Remedy:** Caicedo also debuted during the 2022 qualifiers.

### Row 17743 — Ecuador (easy) — FAIL: non-unique (Gruezo also featured at 2016 Copa)
**Q:** Which Ecuador player featured at the 2016 Copa América Centenario quarter-finals?
**Answer:** Antonio Valencia
**Why it fails:** Multiple listed players featured for Ecuador at the 2016 Copa América Centenario (Antonio Valencia AND Carlos Gruezo were both regulars), so 'which player featured' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2016_Copa_Am%C3%A9rica_Centenario
**Remedy:** Use a captain-specific or distinguishing trait.

### Row 17757 — Ecuador (easy) — FAIL: non-unique (Caicedo & Hincapie also not 'emerging')
**Q:** Which Ecuador player is not an emerging talent for the 2026 World Cup cycle?
**Answer:** Enner Valencia
**Why it fails:** Among the options, only Jeremy Sarmiento is an 'emerging talent' — Valencia, Caicedo AND Hincapié are all established players, so 'which is NOT an emerging talent' has three valid answers.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** Only one option should be the established player.

### Row 17762 — Ecuador (easy) — FAIL: wrong year (Caicedo joined Chelsea in 2023, not 2022)
**Q:** Which Ecuador player joined Chelsea for a record fee in 2022?
**Answer:** Moisés Caicedo
**Why it fails:** Caicedo joined Chelsea in August 2023, not 2022. At the 2022 World Cup he was still a Brighton player.
**Source:** https://en.wikipedia.org/wiki/Mois%C3%A9s_Caicedo
**Remedy:** The transfer was 2023.

### Row 17765 — Ecuador (easy) — FAIL: false (Caicedo's record move was after the 2022 WC)
**Q:** Which Ecuador player made a record transfer before the 2022 World Cup?
**Answer:** Moisés Caicedo
**Why it fails:** Caicedo's record transfer to Chelsea was August 2023 — AFTER the 2022 World Cup, not before. No Ecuador player made a record transfer before the 2022 WC.
**Source:** https://en.wikipedia.org/wiki/Mois%C3%A9s_Caicedo
**Remedy:** His record move came after the 2022 WC.

### Row 17767 — Ecuador (easy) — FAIL: non-unique (all options missed 2010 & 2018)
**Q:** Which Ecuador player missed both the 2010 and 2018 World Cups?
**Answer:** Enner Valencia
**Why it fails:** Ecuador failed to qualify for both 2010 and 2018, so EVERY player of that era 'missed' those World Cups — Antonio Valencia, Felipe Caicedo and Christian Noboa (all options) missed them too. Non-unique.
**Source:** https://en.wikipedia.org/wiki/Ecuador_at_the_FIFA_World_Cup
**Remedy:** Use a player-specific distinguishing trait.

### Row 17774 — Ecuador (easy) — FAIL: wrong stadium (opener was at Al Bayt, not Lusail)
**Q:** Which Ecuador player scored at the 2022 FIFA World Cup venue Lusail Stadium?
**Answer:** Enner Valencia
**Why it fails:** Ecuador's 2022 opener vs Qatar (where Valencia scored both goals) was at the Al Bayt Stadium in Al Khor — NOT the Lusail Stadium. So Valencia did not score 'at Lusail Stadium'.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** The opener was at Al Bayt Stadium.

### Row 17775 — Ecuador (easy) — FAIL: non-unique (Caicedo also scored at 2022)
**Q:** Which Ecuador player scored at the 2022 FIFA World Cup?
**Answer:** Enner Valencia
**Why it fails:** Both Valencia (3 goals) and Caicedo (1, vs Senegal) scored at the 2022 World Cup, and Caicedo is a listed option — so 'which player scored at the 2022 WC' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Caicedo also scored at 2022 (vs Senegal).

### Row 17783 — Ecuador (easy) — FAIL: false (Caicedo, not Valencia, scored v Senegal)
**Q:** Which Ecuador player scored in their 2022 World Cup loss to Senegal?
**Answer:** Enner Valencia
**Why it fails:** Ecuador's goal in the 1-2 loss to Senegal was scored by Moisés Caicedo (67'), NOT Enner Valencia. (The dataset's own row 17781 correctly credits Caicedo.)
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Change the scorer to Caicedo.

### Row 17784 — Ecuador (easy) — FAIL: false (Messi scored 7 at 2022, more than Valencia's 3)
**Q:** Which Ecuador player scored more 2022 World Cup goals than Lionel Messi?
**Answer:** Enner Valencia
**Why it fails:** Messi scored SEVEN goals at the 2022 World Cup (Golden Ball winner) — more than Valencia's 3. The claim only holds for the group stage (Messi 2), but the question asks about '2022 World Cup goals' overall.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Restrict to the group stage, or the claim is false overall.

### Row 17793 — Ecuador (easy) — FAIL: wrong year (Delgados first WC goal was 2002 v Mexico)
**Q:** Which Ecuador player scored their first World Cup goal in 2006?
**Answer:** Agustín Delgado
**Why it fails:** Agustín Delgado scored Ecuador's FIRST-EVER World Cup goal in 2002 (v Mexico), not 2006 v Costa Rica. The '2006 / Costa Rica / first-ever' framing is wrong.
**Source:** https://en.wikipedia.org/wiki/Ecuador_at_the_FIFA_World_Cup
**Remedy:** Ecuador's first WC goal was Delgado v Mexico in 2002.

### Row 17799 — Ecuador (easy) — FAIL: false (Caicedo scored Ecuadors most recent WC goal)
**Q:** Which Ecuador player scored their nation's last five World Cup goals?
**Answer:** Enner Valencia
**Why it fails:** Valencia did NOT score Ecuador's last five World Cup goals — Moisés Caicedo scored their most recent WC goal (v Senegal, 2022). So the run of 'last five' is broken by Caicedo's goal.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Caicedo scored the last one (v Senegal); reword.

### Row 17813 — Ecuador (easy) — FAIL: non-unique (several 2006 players missed 2010)
**Q:** Which Ecuador player was in their 2006 squad but missed the 2010 World Cup?
**Answer:** Iván Hurtado
**Why it fails:** Ecuador failed to qualify for 2010, so multiple 2006 squad members 'missed' it — Iván Hurtado, Agustín Delgado and Ulises de la Cruz (all listed) were 2006 players who did not play at a 2010 World Cup. Non-unique.
**Source:** https://en.wikipedia.org/wiki/Ecuador_at_the_FIFA_World_Cup
**Remedy:** Use a player-specific distinguishing trait.

### Row 17816 — Ecuador (easy) — FAIL: non-unique (Caicedo & Hincapie also not 'emerging')
**Q:** Which Ecuador player was NOT an emerging talent at the 2022 World Cup?
**Answer:** Enner Valencia
**Why it fails:** Among the options only Sarmiento was an 'emerging talent' — Valencia, Caicedo AND Hincapié were all established players at 2022, so 'which was NOT an emerging talent' has three valid answers.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** Only one option should be an emerging talent.

### Row 17817 — Ecuador (easy) — FAIL: false (Caicedo WAS in the 2022 squad)
**Q:** Which Ecuador player was not in their 2022 FIFA World Cup squad?
**Answer:** Moisés Caicedo
**Why it fails:** Moisés Caicedo WAS in Ecuador's 2022 World Cup squad — he started matches and scored against Senegal. The claim that he was 'not in the 2022 squad' is false.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Caicedo played at the 2022 WC; pick a player who genuinely wasn't there.

### Row 17837 — Ecuador (easy) — FAIL: false (British record, not a world record)
**Q:** Which Ecuador player's 2023 transfer was a world-record fee?
**Answer:** Moisés Caicedo
**Why it fails:** Caicedo's £115m move to Chelsea was a BRITISH transfer record, not a world record (the world record is Neymar's ~€222m). The explanation itself says 'British transfer record'.
**Source:** https://en.wikipedia.org/wiki/Mois%C3%A9s_Caicedo
**Remedy:** It was a British record, not a world record.

### Row 17842 — Ecuador (easy) — FAIL: false (Valencia helped qualify for at most 3 WCs)
**Q:** Which Ecuador player's goals helped them qualify for four World Cups?
**Answer:** Enner Valencia
**Why it fails:** Enner Valencia debuted in 2012, so he could only have contributed to qualifying for 2014, 2022 and 2026 — at most THREE World Cups, not four. He had no role in the 2002/2006 qualifications.
**Source:** https://en.wikipedia.org/wiki/Enner_Valencia
**Remedy:** He helped qualify for 3 WCs (2014, 2022, 2026), not four.

### Row 17845 — Ecuador (easy) — FAIL: false (transfer was 2023, fee went to Brighton)
**Q:** Which Ecuador player's record transfer helped fund their 2022 World Cup campaign?
**Answer:** Moisés Caicedo
**Why it fails:** Caicedo's record transfer was August 2023 — AFTER the 2022 World Cup — and the fee went to Brighton (his club), not Ecuador's federation. It did not 'fund their 2022 World Cup campaign'.
**Source:** https://en.wikipedia.org/wiki/Mois%C3%A9s_Caicedo
**Remedy:** The transfer was 2023 and the fee went to Brighton.

### Row 17854 — Ecuador (easy) — FAIL: false (2022 qualifiers were at Casa Blanca, Quito)
**Q:** Which Ecuador stadium did coach Gustavo Alfaro select for the crucial 2022 World Cup qualifier against Uruguay?
**Answer:** Estadio Monumental
**Why it fails:** Ecuador's 2022 home qualifiers (including vs Uruguay) were at the Casa Blanca (Rodrigo Paz Delgado) in Quito for altitude — NOT the sea-level Estadio Monumental in Guayaquil.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** The 2022 qualifiers were in Quito (Casa Blanca).

### Row 17855 — Ecuador (easy) — FAIL: false (2022 qualifiers were at Casa Blanca, Quito)
**Q:** Which Ecuador stadium hosted a 2022 World Cup qualifier with record attendance?
**Answer:** Estadio Monumental
**Why it fails:** Ecuador's 2022 qualifiers were at the Casa Blanca in Quito, not the Estadio Monumental in Guayaquil.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** The 2022 qualifiers were in Quito.

### Row 17856 — Ecuador (easy) — FAIL: false (2014 qualifiers were at Atahualpa, Quito)
**Q:** Which Ecuador stadium hosted the 2014 World Cup qualifier vs Argentina with the largest capacity?
**Answer:** Estadio Monumental
**Why it fails:** Ecuador's 2014 home qualifiers (including vs Argentina) were at the Estadio Olímpico Atahualpa in Quito for altitude — not the Estadio Monumental in Guayaquil.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** The 2014 qualifiers were at Atahualpa (Quito).

### Row 17857 — Ecuador (easy) — FAIL: false (2022 qualifiers were at Casa Blanca, Quito)
**Q:** Which Ecuador stadium hosted the 2022 World Cup qualifier against Argentina?
**Answer:** Estadio Monumental
**Why it fails:** The 2022 Argentina qualifier was hosted in Quito (Casa Blanca), not the Estadio Monumental in Guayaquil.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** The 2022 qualifiers were in Quito.

### Row 17858 — Ecuador (easy) — FAIL: false (2022 qualifiers were at Casa Blanca, Quito)
**Q:** Which Ecuador stadium hosted the 2022 World Cup qualifiers and holds 57,267 fans?
**Answer:** Estadio Monumental
**Why it fails:** Ecuador's 2022 qualifiers were at Casa Blanca (Quito), not the 57,267-capacity Estadio Monumental in Guayaquil.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** The 2022 qualifiers were in Quito.

### Row 17859 — Ecuador (easy) — FAIL: false (Colombia game in Quito; 'win' vs 0-0 draw contradiction)
**Q:** Which Ecuador stadium hosted the 2022 World Cup qualifying win over Colombia?
**Answer:** Estadio Monumental
**Why it fails:** Ecuador's 2022 qualifiers were in Quito, not the Monumental. The row is also internally inconsistent — it asks about a 'win over Colombia' while the explanation describes a 0-0 draw (the actual win, 6-1, was in Quito).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** The 2022 Colombia games were in Quito; fix the win/draw mismatch.

### Row 17860 — Ecuador (easy) — FAIL: false premise (no Copa America qualifiers / no 2023 Copa)
**Q:** Which Ecuador stadium hosted the 2023 Copa América qualifiers due to its capacity?
**Answer:** Estadio Monumental
**Why it fails:** There are no 'Copa América qualifiers' — the Copa has no qualifying round — and there was no 2023 Copa América. The premise is a non-event.
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica
**Remedy:** Remove the false premise.

### Row 17861 — Ecuador (easy) — FAIL: false (2014 qualifiers were at Atahualpa, Quito)
**Q:** Which Ecuador stadium hosted their 2014 World Cup qualifier vs Uruguay?
**Answer:** Estadio Monumental
**Why it fails:** Ecuador's 2014 qualifier vs Uruguay was in Quito (Atahualpa), not the Estadio Monumental in Guayaquil.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** The 2014 qualifiers were at Atahualpa (Quito).

### Row 17862 — Ecuador (easy) — FAIL: false (2022 Brazil qualifier was in Quito, 1-1)
**Q:** Which Ecuador stadium hosted their 2022 World Cup qualifier against Brazil?
**Answer:** Estadio Monumental
**Why it fails:** Ecuador's 2022 qualifier vs Brazil (1-1) was at the Casa Blanca in Quito, not the Estadio Monumental in Guayaquil.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** The 2022 Brazil qualifier was in Quito.

### Row 17863 — Ecuador (easy) — FAIL: false (2022 qualifiers were at Casa Blanca, Quito)
**Q:** Which Ecuador stadium hosted their 2022 World Cup qualifiers due to its large capacity?
**Answer:** Estadio Monumental
**Why it fails:** Ecuador's 2022 qualifiers were at Casa Blanca (Quito), not the Estadio Monumental.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** The 2022 qualifiers were in Quito.

### Row 17864 — Ecuador (easy) — FAIL: false (2022 qualifiers were at Casa Blanca, Quito)
**Q:** Which Ecuador stadium hosted their 2022 World Cup qualifying match against Argentina?
**Answer:** Estadio Monumental
**Why it fails:** The 2022 Argentina qualifier was in Quito (Casa Blanca), not the Estadio Monumental.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** The 2022 qualifiers were in Quito.

### Row 17869 — Ecuador (easy) — FAIL: false (2022 qualifiers were at Casa Blanca, Quito)
**Q:** Which Ecuador stadium, capacity ~57,267, hosted 2022 World Cup qualifiers?
**Answer:** Estadio Monumental
**Why it fails:** Ecuador's 2022 qualifiers were at Casa Blanca (Quito), not the 57,267-capacity Estadio Monumental.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** The 2022 qualifiers were in Quito.

### Row 17871 — Ecuador (easy) — FAIL: false (the 6-1 Colombia win was in Quito)
**Q:** Which Ecuador stadium, its largest, hosted their record 2022 World Cup qualifying win?
**Answer:** Estadio Monumental
**Why it fails:** Ecuador's record 6-1 win over Colombia in 2022 qualifying was in Quito (altitude), not the Estadio Monumental in Guayaquil.
**Source:** https://www.aljazeera.com/sports/2022/11/13/world-cup-2022-ecuador
**Remedy:** The 6-1 win was in Quito.

### Row 17874 — Ecuador (easy) — FAIL: false (2022 qualifiers were at Casa Blanca, Quito)
**Q:** Which Ecuador stadium, with a 57,267 capacity, hosted a key 2022 World Cup qualifier?
**Answer:** Estadio Monumental
**Why it fails:** Ecuador's 2022 qualifiers were at Casa Blanca (Quito), not the 57,267-capacity Estadio Monumental.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** The 2022 qualifiers were in Quito.

### Row 17876 — Ecuador (easy) — FAIL: false (2022 qualifiers were at Casa Blanca, Quito)
**Q:** Which Ecuador stadium, with a 57,267 capacity, was their largest for 2022 World Cup qualifiers?
**Answer:** Estadio Monumental
**Why it fails:** The Estadio Monumental is Ecuador's largest stadium but was NOT used for the 2022 qualifiers — those were at the Casa Blanca (Rodrigo Paz Delgado) in Quito.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** The 2022 qualifier venue was Casa Blanca (Quito).

### Row 17877 — Ecuador (easy) — FAIL: false premise (Ecuador qualified directly, no 2022 playoff)
**Q:** Which Ecuador stadium's large capacity made it the 2022 World Cup playoff host?
**Answer:** Estadio Monumental
**Why it fails:** Ecuador qualified for 2022 DIRECTLY by finishing 4th in CONMEBOL — they did NOT play an inter-confederation play-off. So there was no '2022 World Cup playoff' for any stadium to host.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Ecuador qualified directly; there was no play-off.

### Row 17881 — Ecuador (easy) — FAIL: non-unique (several stars missed both 2010 & 2018)
**Q:** Which Ecuador star missed both the 2010 and 2018 World Cups?
**Answer:** Antonio Valencia
**Why it fails:** Ecuador failed to qualify for both 2010 and 2018, so multiple players active across that span 'missed both' — Antonio Valencia, Felipe Caicedo and Christian Noboa (all options) all did. Non-unique.
**Source:** https://en.wikipedia.org/wiki/Ecuador_at_the_FIFA_World_Cup
**Remedy:** Use a player-specific distinguishing trait.

### Row 17882 — Ecuador (easy) — FAIL: non-unique (Antonio Valencia also in the 2014 squad)
**Q:** Which Ecuador star was in their 2014 World Cup squad?
**Answer:** Enner Valencia
**Why it fails:** Both Enner Valencia AND Antonio Valencia (a listed option, the captain) were in Ecuador's 2014 World Cup squad — so 'which star was in the 2014 squad' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_E
**Remedy:** Antonio Valencia was also in the 2014 squad.

### Row 17883 — Ecuador (easy) — FAIL: false (transfer was 2023; fee went to Brighton)
**Q:** Which Ecuador star's 2023 sale funded their 2022 World Cup squad development?
**Answer:** Moisés Caicedo
**Why it fails:** Caicedo's record sale was August 2023 — after the 2022 World Cup — and the fee went to Brighton, not Ecuador. It did not 'fund their 2022 World Cup squad development'.
**Source:** https://en.wikipedia.org/wiki/Mois%C3%A9s_Caicedo
**Remedy:** The 2023 sale couldn't fund the 2022 squad.

### Row 17899 — Ecuador (easy) — FAIL: false (Plata did not score at the 2022 WC)
**Q:** Which Ecuador winger scored a goal at the 2022 World Cup?
**Answer:** Gonzalo Plata
**Why it fails:** Gonzalo Plata did NOT score at the 2022 World Cup — Ecuador's only scorers were Valencia (3) and Caicedo (1, vs Senegal). Plata scored none.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Plata did not score; Ecuador's scorers were Valencia and Caicedo.

### Row 17904 — Ecuador (hard) — FAIL: non-unique (every campaign relied on Quitos altitude)
**Q:** Which Ecuador World Cup qualification campaign relied on their high-altitude Quito stadium?
**Answer:** 2022 qualification
**Why it fails:** EVERY Ecuador qualifying campaign relied on Quito's high altitude (Atahualpa through 2018, Casa Blanca for 2022) — so 'which campaign relied on the high-altitude Quito stadium' is non-unique among the options.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** All campaigns used Quito; make it specific.

### Row 17908 — Ecuador (easy) — FAIL: non-unique (all options are LigaPro clubs)
**Q:** Which Ecuadorian club is a classic LigaPro member?
**Answer:** Barcelona SC
**Why it fails:** Barcelona SC, LDU Quito, Emelec AND Independiente del Valle are all LigaPro clubs, so 'which is a classic LigaPro member' is non-unique.
**Source:** https://en.wikipedia.org/wiki/Ecuadorian_Serie_A
**Remedy:** All four are LigaPro members.

### Row 17917 — Ecuador (easy) — FAIL: anachronism (IDV won Oct 2022, after qualifying)
**Q:** Which Ecuadorian club's 2022 continental success boosted their players' World Cup qualifying experience?
**Answer:** Independiente del Valle
**Why it fails:** Independiente del Valle won the 2022 Copa Sudamericana on 1 October 2022 — AFTER Ecuador's WC qualifying had already ended (March 2022). So the win could not have 'boosted their players' World Cup qualifying experience'.
**Source:** https://en.wikipedia.org/wiki/2022_Copa_Sudamericana
**Remedy:** The Sudamericana win came after qualifying.

### Row 17918 — Ecuador (medium) — FAIL: anachronism (IDV won Oct 2022, after qualifying)
**Q:** Which Ecuadorian club's 2022 continental title boosted the nation's FIFA ranking before World Cup qualifying?
**Answer:** Independiente del Valle
**Why it fails:** IDV's 2022 Copa Sudamericana win (Oct 2022) came AFTER Ecuador's 2022 WC qualifying ended (March 2022), so it cannot have boosted the FIFA ranking 'before World Cup qualifying'.
**Source:** https://en.wikipedia.org/wiki/2022_Copa_Sudamericana
**Remedy:** The win came after qualifying, not before.

### Row 17919 — Ecuador (easy) — FAIL: anachronism (IDV won Oct 2022, after qualifiers)
**Q:** Which Ecuadorian club's 2022 continental win boosted morale before the 2022 FIFA World Cup qualifiers?
**Answer:** Independiente del Valle
**Why it fails:** IDV's 2022 Copa Sudamericana win (1 Oct 2022) came AFTER the 2022 WC qualifiers (ended March 2022), so it could not have boosted morale 'before the 2022 qualifiers'.
**Source:** https://en.wikipedia.org/wiki/2022_Copa_Sudamericana
**Remedy:** The win came after the qualifiers.

### Row 17923 — Ecuador (medium) — FAIL: anachronism (IDV win Oct 2022, after qualifying)
**Q:** Which Ecuadorian club's 2022 Sudamericana win boosted their FIFA ranking for World Cup qualifying?
**Answer:** Independiente del Valle
**Why it fails:** IDV's Sudamericana win (Oct 2022) came after WC qualifying ended (March 2022), so it cannot have boosted the FIFA ranking 'for World Cup qualifying'.
**Source:** https://en.wikipedia.org/wiki/2022_Copa_Sudamericana
**Remedy:** The win came after qualifying.

### Row 17942 — Ecuador (medium) — FAIL: wrong timing (Paez debuted 2023, before 2026 qualification)
**Q:** Which Ecuadorian player debuted after their 2026 World Cup qualification?
**Answer:** Kendry Páez
**Why it fails:** Kendry Páez made his Ecuador debut in June 2023 — at the START of the 2026 cycle, roughly two years BEFORE Ecuador secured 2026 qualification (2025). He did not debut 'after' qualification.
**Source:** https://en.wikipedia.org/wiki/Kendry_P%C3%A1ez
**Remedy:** Paez debuted in 2023, before qualification was secured.

### Row 17944 — Ecuador (easy) — FAIL: false (Estupinan was at Brighton, not IDVs squad)
**Q:** Which Ecuadorian player from Independiente del Valle's 2022 Copa Sudamericana win started in the 2022 FIFA World Cup opener?
**Answer:** Pervis Estupiñán
**Why it fails:** Pervis Estupiñán was a Brighton player at the 2022 World Cup — he was NOT part of Independiente del Valle's 2022 Copa Sudamericana-winning squad (he came through IDV's academy years earlier but had long since moved to Europe).
**Source:** https://en.wikipedia.org/wiki/Pervis_Estupi%C3%B1%C3%A1n
**Remedy:** Estupinan was not in IDV's 2022 squad.

### Row 17950 — Ecuador (easy) — FAIL: false (2022 qualifiers were at Casa Blanca, Quito)
**Q:** Which Ecuadorian stadium, capacity 57,267, hosted a 2022 World Cup qualifier?
**Answer:** Estadio Monumental
**Why it fails:** Ecuador's 2022 qualifiers were at Casa Blanca (Quito), not the 57,267-capacity Estadio Monumental in Guayaquil.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** The 2022 qualifiers were in Quito.

### Row 17951 — Ecuador (easy) — FAIL: false (2014 qualifiers were at Atahualpa, Quito)
**Q:** Which Ecuadorian stadium, with a 57,267 capacity, hosted their 2014 World Cup qualifier wins?
**Answer:** Estadio Monumental
**Why it fails:** Ecuador's 2014 qualifier wins were at the Estadio Olímpico Atahualpa in Quito, not the Estadio Monumental in Guayaquil.
**Source:** https://en.wikipedia.org/wiki/Ecuador_national_football_team
**Remedy:** The 2014 qualifiers were at Atahualpa (Quito).

### Row 17963 — Ecuador (easy) — FAIL: false (Caicedo's move came AFTER Enzo's, not before)
**Q:** Which Ecuadorian's record transfer occurred before Enzo Fernández's in 2023?
**Answer:** Moisés Caicedo
**Why it fails:** Enzo Fernández moved to Chelsea in January 2023 (then a British record); Caicedo moved in August 2023 and BROKE Enzo's record. So Caicedo's transfer came AFTER Enzo's, not before.
**Source:** https://en.wikipedia.org/wiki/Mois%C3%A9s_Caicedo
**Remedy:** Caicedo's move (Aug 2023) was after Enzo's (Jan 2023).

### Row 17977 — Ecuador (easy) — FAIL: wrong club (Valencia came from Emelec, was at Fenerbahce in 2022)
**Q:** Which LigaPro club did Ecuador's 2022 World Cup captain Enner Valencia play for?
**Answer:** Barcelona SC
**Why it fails:** Enner Valencia's LigaPro club was Emelec (a listed option), not Barcelona SC — and at the 2022 World Cup he played for Fenerbahçe in Turkey. He never played for Barcelona SC.
**Source:** https://en.wikipedia.org/wiki/Enner_Valencia
**Remedy:** Change to Emelec (his Ecuadorian club).

### Row 17978 — Ecuador (medium) — FAIL: false premise (Ecuador did not qualify for 2010)
**Q:** Which LigaPro club's 2008 continental title preceded Ecuador's 2010 World Cup qualification?
**Answer:** LDU Quito
**Why it fails:** Ecuador FAILED to qualify for the 2010 World Cup, so LDU's 2008 Libertadores title did not 'precede Ecuador's 2010 World Cup qualification' — there was no 2010 qualification.
**Source:** https://en.wikipedia.org/wiki/Ecuador_at_the_FIFA_World_Cup
**Remedy:** Ecuador did not qualify for 2010.

### Row 18002 — Ecuador (easy) — FAIL: false (Sarr scored once; Koulibaly scored the other)
**Q:** Which Senegal player scored twice in their 2022 World Cup win over Ecuador?
**Answer:** Ismaïla Sarr
**Why it fails:** Sarr did NOT score twice — Senegal's two goals vs Ecuador were Sarr (penalty) and Koulibaly. Neither player scored twice.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Sarr scored once; Koulibaly scored the winner.

### Row 18008 — Ecuador (easy) — FAIL: false (opener was at Al Bayt, not all at Khalifa)
**Q:** Which stadium hosted Ecuador's 2022 FIFA World Cup matches?
**Answer:** Khalifa International Stadium
**Why it fails:** Ecuador did NOT play all their 2022 matches at Khalifa — their opener vs Qatar was at the Al Bayt Stadium (a listed option). Only the Netherlands and Senegal games were at Khalifa.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** The opener was at Al Bayt; matches were split.

### Row 18009 — Ecuador (easy) — FAIL: false (2022 qualifiers were at Casa Blanca, Quito)
**Q:** Which stadium hosted Ecuador's 2022 World Cup qualifiers with the largest capacity?
**Answer:** Estadio Monumental
**Why it fails:** Ecuador's 2022 qualifiers were at Casa Blanca (Quito), not the Estadio Monumental. (The other options are stadiums in Peru and Colombia.)
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** The 2022 qualifiers were in Quito.

### Row 18019 — Ecuador (easy) — FAIL: non-unique (Ecuador 4th, above all four options)
**Q:** Which team did Ecuador finish above in the 2022 World Cup qualifying table?
**Answer:** Colombia
**Why it fails:** Ecuador finished 4th in 2022 qualifying, above Peru (5th), Colombia (6th), Chile (7th) AND Paraguay (8th) — all four options. 'Which did Ecuador finish above' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Ask which finished directly below (Peru, 5th).

### Row 18020 — Ecuador (easy) — FAIL: non-unique / wrong (they DID face the Netherlands)
**Q:** Which team did Ecuador NOT face in their decisive 2022 World Cup group match?
**Answer:** Netherlands
**Why it fails:** In their decisive final group match Ecuador faced Senegal — so they did NOT face the Netherlands, Qatar OR Germany in that match (non-unique). And overall Ecuador DID face the Netherlands in the group, so 'not faced' is misleading.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Reframe; the only team never faced was Germany.

### Row 18021 — Ecuador (medium) — FAIL: non-unique (Ecuador also did not lose to Qatar)
**Q:** Which team did Ecuador NOT lose to in the 2022 FIFA World Cup group stage?
**Answer:** The Netherlands
**Why it fails:** Ecuador beat Qatar, drew the Netherlands and lost to Senegal — so they did NOT lose to BOTH Qatar and the Netherlands (both listed). Non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Ask which they drew (Netherlands).

### Row 18039 — Ecuador (medium) — FAIL: non-unique (4th in both 2014 and 2022)
**Q:** Which World Cup did Ecuador reach by finishing 4th in CONMEBOL qualifiers?
**Answer:** 2022 World Cup
**Why it fails:** Ecuador finished 4th in CONMEBOL for both 2014 and 2022 (both listed options), so 'which World Cup did Ecuador reach by finishing 4th' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** 2014 was also a 4th-place finish.

### Row 18042 — Ecuador (hard) — FAIL: non-unique (group-stage exit in 2014 and 2022)
**Q:** Which World Cup saw Ecuador eliminated in the group stage?
**Answer:** 2022 FIFA World Cup
**Why it fails:** Ecuador were eliminated in the group stage in both 2014 and 2022 (both listed), so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Ecuador_at_the_FIFA_World_Cup
**Remedy:** Group-stage exits came in 2002, 2014 and 2022.

### Row 18051 — Ecuador (easy) — FAIL: false (Ecuador scored 4 at 2022; Valencia 3, Caicedo 1)
**Q:** Who scored both of Ecuador's goals at the 2022 FIFA World Cup?
**Answer:** Enner Valencia
**Why it fails:** Ecuador scored FOUR goals at the 2022 World Cup — Valencia (3) and Caicedo (1, vs Senegal) — not two. So Valencia did not score 'both' of Ecuador's goals.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Valencia scored 3 of Ecuadors 4 goals; Caicedo scored vs Senegal.

### Row 18054 — Ecuador (easy) — FAIL: false (2016 QF was 2-1 USA; Valencia didnt score)
**Q:** Who scored Ecuador's goal in their 2016 Copa América quarter-final?
**Answer:** Enner Valencia
**Why it fails:** Ecuador's 2016 Copa América Centenario QF loss to the USA was 2-1, not 4-1, and Ecuador's goal was not scored by Enner Valencia (Michael Arroyo scored it; Valencia did not feature as the scorer).
**Source:** https://en.wikipedia.org/wiki/2016_Copa_Am%C3%A9rica_Centenario
**Remedy:** The QF was 2-1; the scorer was not Valencia.

### Row 18064 — Ecuador (easy) — FAIL: backwards (Gakpo gave the lead; Valencia equalized)
**Q:** Why did Ecuador draw 1-1 with the Netherlands at the 2022 World Cup?
**Answer:** Cody Gakpo equalized
**Why it fails:** Cody Gakpo did NOT score the equalizer — he scored the OPENING goal to put the Netherlands 1-0 up; Enner Valencia then equalized for Ecuador (1-1). The 'Gakpo equalized' framing is reversed.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_A
**Remedy:** Gakpo scored first; Valencia equalized.

### Row 18072 — Ecuador (easy) — FAIL: false (2022 qualifiers were in Quito, not Guayaquil)
**Q:** Why did Ecuador's 2022 World Cup coach choose to play key qualifiers in Guayaquil?
**Answer:** Largest stadium's home support
**Why it fails:** Ecuador played their key 2022 qualifiers in QUITO (Casa Blanca, altitude) — NOT in Guayaquil at the Estadio Monumental. The premise that the coach chose Guayaquil is false.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** The 2022 qualifiers were in Quito for altitude.

### Row 18079 — Ecuador (hard) — FAIL: nonsensical (clubs do not enter WC qualifiers)
**Q:** Why did Independiente del Valle enter the 2023 FIFA World Cup qualifiers for Ecuador?
**Answer:** Won 2022 Copa Sudamericana
**Why it fails:** Clubs do not 'enter FIFA World Cup qualifiers' — only national teams do. Independiente del Valle won the 2022 Copa Sudamericana (a club competition); this has nothing to do with entering World Cup qualifiers, and the explanation's reasoning is incoherent.
**Source:** https://en.wikipedia.org/wiki/2022_Copa_Sudamericana
**Remedy:** Remove the false premise; clubs don't play WC qualifiers.

## Egypt — rows 18087–18876 (liveness on QA_PASSED_b2.md rows) — 155 FAIL

**Fact base (sourced):** Egypt **FAILED to qualify for the 2022 World Cup** (lost the Senegal playoff on penalties), so every "at the 2022 World Cup / 2022 squad / captained at 2022 / coached at 2022 / secured 2022 qualification" claim is a **false premise**. The **2010 AFCON final was a 1-0 win over Ghana (Gedo, open play) — NOT a penalty shootout**, so all "won on penalties / scored the winning penalty in 2010" rows are false. **Salah was NOT Egypt's 2018 captain** (El-Hadary/Elmohamady were) and **did not take a penalty in the 2021 AFCON final** (he was the 5th taker; Egypt's misses were Abdelmonem & Lasheen) — he **did** miss the first kick in the 2022 *qualifying* shootout. The **2021 AFCON was hosted by Cameroon**, not Egypt. Egypt's **2018 home qualifiers were at Borg El Arab (Alexandria, ~86k — larger than Cairo International ~75k)**, not Cairo. **Elneny had ~60 caps at 2018** (not 100+); **Ahmed Hassan's 184 caps** was his 2012 career total (not by 2006/2010); **El-Hadary won 4 AFCONs** (not 7); **Salah played for Arab Contractors, not Al Ahly**; the **2018-19 Golden Boot was shared** with Mané & Aubameyang. Several rows carry Excel **date-corruption** in the answer cell. Sources: Wikipedia (Egypt at the FIFA WC, 2018 CAF qualifying, 2010/2017/2021 AFCON finals, 2022 CAF qualifying, player pages).

### Row 18106 — Egypt (easy) — FAIL: non-unique (all options qualified for 2018)
**Q:** Egypt beat Congo to qualify for the 2018 World Cup. Which other CAF nation qualified in 2018?
**Answer:** Senegal
**Why it fails:** All four options — Senegal, Nigeria, Morocco AND Tunisia — qualified for the 2018 World Cup from CAF (alongside Egypt). So 'which other CAF nation qualified' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CAF)
**Remedy:** All five CAF nations listed qualified for 2018.

### Row 18121 — Egypt (easy) — FAIL: false (2010 final was 1-0, not on penalties)
**Q:** Egypt won the 2010 AFCON final by beating which nation on penalties?
**Answer:** Ghana
**Why it fails:** Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85') — it was NOT a penalty shootout.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** It was a 1-0 win (Gedo), not a shootout.

### Row 18139 — Egypt (medium) — FAIL: non-unique (Salah scored vs Russia too)
**Q:** Egypt's Mohamed Salah, a two-time Premier League Golden Boot winner, scored in which 2018 World Cup group stage match?
**Answer:** Egypt vs Saudi Arabia
**Why it fails:** Salah scored in TWO of Egypt's 2018 group games — vs Saudi Arabia (22') AND vs Russia (73' penalty). Both are listed options, so 'which match did Salah score in' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** Salah also scored vs Russia.

### Row 18146 — Egypt (easy) — FAIL: false (Borg El Arab is larger than Cairo International)
**Q:** For Egypt's 2018 qualifiers, which stadium held the most fans?
**Answer:** Cairo International Stadium
**Why it fails:** Cairo International (~75,000) is NOT Egypt's largest stadium — Borg El Arab in Alexandria (~86,000, a listed option) is bigger. So it did not 'hold the most fans'.
**Source:** https://en.wikipedia.org/wiki/Borg_El_Arab_Stadium
**Remedy:** Borg El Arab (~86,000) is larger.

### Row 18147 — Egypt (medium) — FAIL: false (2018 group stage was in Russia, not Cairo)
**Q:** For Egypt's 2018 World Cup group stage, which stadium was the primary venue?
**Answer:** Cairo International Stadium
**Why it fails:** The 2018 World Cup GROUP STAGE was hosted in Russia — Egypt played in Yekaterinburg, Saint Petersburg and Volgograd. Cairo International was not a 2018 World Cup venue.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** The 2018 finals were in Russia; Cairo hosted qualifiers only.

### Row 18150 — Egypt (easy) — FAIL: false (FNB and Borg El Arab are larger than Cairo)
**Q:** For Egypt's 2022 World Cup qualifiers, which stadium's capacity was larger?
**Answer:** Cairo International Stadium
**Why it fails:** Cairo International (~75,000) is not the largest among the options — FNB Stadium (Johannesburg, ~94,000) and Borg El Arab (~86,000) both have larger capacities.
**Source:** https://en.wikipedia.org/wiki/Borg_El_Arab_Stadium
**Remedy:** FNB Stadium is the largest of the listed venues.

### Row 18180 — Egypt (easy) — FAIL: non-unique (faced only Senegal in the playoff)
**Q:** In 2022 FIFA World Cup qualifying, which team did Egypt NOT face in their playoff?
**Answer:** Nigeria
**Why it fails:** Egypt's only 2022 World Cup playoff opponent was Senegal — so they did NOT face Nigeria, Cameroon OR Algeria (three of the four options) in the playoff. Non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Ask which they DID face (Senegal).

### Row 18184 — Egypt (medium) — FAIL: non-unique (Salah scored vs Russia too)
**Q:** In Egypt's 2018 World Cup group stage, Mohamed Salah scored against which nation?
**Answer:** Saudi Arabia
**Why it fails:** Salah scored vs both Saudi Arabia and Russia at the 2018 World Cup — both listed options — so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** Salah also scored vs Russia.

### Row 18186 — Egypt (medium) — FAIL: non-unique (Salah, also an attacker, started)
**Q:** In Egypt's 2018 World Cup group stage, which key AFCON attacker started?
**Answer:** Trézéguet
**Why it fails:** Mohamed Salah (a listed option) is Egypt's key attacker and started at the 2018 World Cup too — so 'which key attacker started' is non-unique with Trézéguet.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** Salah also started as an attacker.

### Row 18187 — Egypt (medium) — FAIL: false (Salah was not Egypts 2018 captain)
**Q:** In Egypt's 2018 World Cup group stage, which player was their captain?
**Answer:** Mohamed Salah
**Why it fails:** Salah was Egypt's talisman but NOT the captain at the 2018 World Cup — the armband was worn by veterans Essam El-Hadary (a listed option) and Ahmed Elmohamady/Ahmed Fathi. Salah became captain later.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** The 2018 captain was El-Hadary (and Elmohamady), not Salah.

### Row 18192 — Egypt (easy) — FAIL: Excel date-corruption in the answer cell
**Q:** In the 2017 AFCON final, Egypt lost to Cameroon by what score?
**Answer:** 2026-01-02 00:00:00
**Why it fails:** The answer is mangled to a datetime '2026-01-02 00:00:00' instead of the score. Egypt lost the 2017 AFCON final 2-1 to Cameroon.
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations_Final
**Remedy:** Restore the score (2-1).

### Row 18206 — Egypt (medium) — FAIL: false premise (Salah had no 2022 WC appearance)
**Q:** In which World Cup did Egypt's Mohamed Salah debut, before his 2022 appearance?
**Answer:** 2018 World Cup
**Why it fails:** Egypt did not qualify for the 2022 World Cup, so Salah had no '2022 appearance'. He debuted at the 2018 WC; the 'before his 2022 appearance' clause is false.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Salah/Egypt were absent from the 2022 WC.

### Row 18207 — Egypt (medium) — FAIL: false (Salahs first WC goal was vs Russia, not Saudi)
**Q:** In which World Cup did Egyptian star Mohamed Salah score his first finals goal?
**Answer:** 2018 World Cup
**Why it fails:** Salah's first World Cup finals goal came against RUSSIA (19 June 2018, 73' penalty) — chronologically before the Saudi Arabia game (25 June). So his first finals goal was vs Russia, not Saudi Arabia.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** His first WC goal was vs Russia.

### Row 18218 — Egypt (medium) — FAIL: wrong year (Al Ahlys 10th title was 2021, not 2012)
**Q:** In which year did Egypt's Al Ahly win their 10th CAF Champions League title?
**Answer:** 2012
**Why it fails:** Al Ahly's 10th CAF Champions League title came in 2020-21, NOT 2012 — 2012 was their 7th (titles: 1982, 1987, 2001, 2005, 2006, 2008, 2012, 2013, 2019-20, 2020-21, 2022-23, 2023-24).
**Source:** https://en.wikipedia.org/wiki/List_of_Al_Ahly_SC_records_and_statistics
**Remedy:** Their 10th title was 2021; 2012 was the 7th.

### Row 18227 — Egypt (medium) — FAIL: false (2010 final was 1-0, not penalties)
**Q:** When did Egypt beat Ghana on penalties in an AFCON final?
**Answer:** 2010
**Why it fails:** Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** It was a 1-0 win, not a shootout.

### Row 18234 — Egypt (medium) — FAIL: Excel date-corruption in the answer cell
**Q:** When did Egypt lose to Senegal in 2022 World Cup qualifying?
**Answer:** 2022-03-01 00:00:00
**Why it fails:** The answer is mangled to a datetime '2022-03-01 00:00:00' instead of a clean date. Egypt lost the 2nd leg in March 2022.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Restore the answer to 'March 2022'.

### Row 18240 — Egypt (medium) — FAIL: false (2010 final was 1-0, not penalties)
**Q:** When did Egypt win an AFCON final on penalties, after losing two later finals?
**Answer:** 2010
**Why it fails:** Egypt won the 2010 AFCON final 1-0 over Ghana (Gedo), NOT on penalties.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** It was a 1-0 win, not a shootout.

### Row 18241 — Egypt (medium) — FAIL: false (2010 final was 1-0, not penalties)
**Q:** When did Egypt win the 2010 Africa Cup of Nations final?
**Answer:** 2010
**Why it fails:** The 2010 AFCON final was Egypt 1-0 Ghana (Gedo), not a penalty shootout.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** It was a 1-0 win.

### Row 18242 — Egypt (medium) — FAIL: false (2010 final was 1-0, not penalties)
**Q:** When did Egypt win the AFCON, beating Ghana on penalties?
**Answer:** 2010
**Why it fails:** The 2010 AFCON final was a 1-0 win over Ghana, not a penalty shootout.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** It was a 1-0 win.

### Row 18244 — Egypt (medium) — FAIL: false (Cairo hosted WC qualifiers long before 2009)
**Q:** When did Egypt's 75,000-capacity Cairo International Stadium first host a World Cup qualifier?
**Answer:** 2009
**Why it fails:** Cairo International Stadium opened in 1960 and has hosted Egypt's home World Cup qualifiers for decades (e.g. the 1990 cycle) — so 2009 was NOT the first time it hosted a WC qualifier.
**Source:** https://en.wikipedia.org/wiki/Cairo_International_Stadium
**Remedy:** It hosted WC qualifiers from the 1960s-70s onward.

### Row 18251 — Egypt (medium) — FAIL: Excel date-corruption in the answer cell
**Q:** When did Egypt's manager leave before the 2018 FIFA World Cup?
**Answer:** 2018-06-01 00:00:00
**Why it fails:** The answer is mangled to a datetime '2018-06-01 00:00:00' instead of a clean date (Cuper left in June/July 2018).
**Source:** https://en.wikipedia.org/wiki/H%C3%A9ctor_C%C3%BAper
**Remedy:** Restore the answer to a clean date.

### Row 18263 — Egypt (easy) — FAIL: false (Ghana won the tie 6-1; Egypt won 2nd leg 2-1)
**Q:** Where did Egypt host Ghana for a 2014 World Cup qualifier?
**Answer:** Borg El Arab Stadium
**Why it fails:** Egypt did NOT win 6-1 over Ghana in the 2014 playoff — GHANA won the first leg 6-1 (Kumasi). Egypt won the second leg only 2-1 and lost the tie 7-3 on aggregate.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Ghana won 6-1; Egypt's 2nd-leg win was 2-1.

### Row 18264 — Egypt (easy) — FAIL: false premise (Egypt qualified directly for 2018, no playoff)
**Q:** Where did Egypt host their 2018 World Cup qualifying playoff home leg?
**Answer:** Cairo International Stadium
**Why it fails:** Egypt qualified for the 2018 World Cup DIRECTLY by winning CAF Group E — there was no 2018 qualifying play-off. (The play-off was in the 2014 cycle, vs Ghana.)
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CAF)
**Remedy:** There was no 2018 play-off; Egypt won their group.

### Row 18266 — Egypt (easy) — FAIL: incoherent (2010 final was 1-0, not penalties)
**Q:** Which 2010 AFCON finalist beat Ghana on penalties, unlike Egypt?
**Answer:** None of them
**Why it fails:** The premise is false — the 2010 AFCON final was a 1-0 win, not a penalty shootout — so the whole question ('which finalist beat Ghana on penalties, unlike Egypt') is incoherent.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Egypt beat Ghana 1-0, not on penalties.

### Row 18276 — Egypt (easy) — FAIL: non-unique (all options have fewer than 7)
**Q:** Which AFCON champion has won fewer titles than Egypt's record seven?
**Answer:** Cameroon
**Why it fails:** All four options have fewer AFCON titles than Egypt's 7 — Cameroon (5), Ghana (4), Nigeria (3), Ivory Coast (3). The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Africa_Cup_of_Nations
**Remedy:** All four have fewer than 7.

### Row 18310 — Egypt (easy) — FAIL: non-unique (all options qualified for 2018)
**Q:** Which CAF nation qualified for the 2018 World Cup like Egypt?
**Answer:** Nigeria
**Why it fails:** Nigeria, Senegal, Morocco AND Tunisia all qualified for the 2018 World Cup from CAF — non-unique.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CAF)
**Remedy:** All four CAF options qualified.

### Row 18311 — Egypt (easy) — FAIL: non-unique (all options qualified for 2018)
**Q:** Which CAF nation, like Egypt, qualified for the 2018 World Cup?
**Answer:** Tunisia
**Why it fails:** Tunisia, Senegal, Nigeria AND Morocco all qualified for the 2018 World Cup from CAF — non-unique.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CAF)
**Remedy:** All four CAF options qualified.

### Row 18318 — Egypt (easy) — FAIL: false (Aboubakar scored once; N'Koulou scored the other)
**Q:** Which Cameroon player scored twice to beat Egypt in the 2017 AFCON final?
**Answer:** Vincent Aboubakar
**Why it fails:** Aboubakar did NOT score twice in the 2017 final — Cameroon's goals were N'Koulou (59') and Aboubakar (88'). Aboubakar scored once.
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations_Final
**Remedy:** N'Koulou scored Cameroon's first goal.

### Row 18320 — Egypt (easy) — FAIL: false (Trezeguet scored ~1 at 2019, not 4)
**Q:** Which Egypt attacker scored 4 goals at the 2019 Africa Cup of Nations?
**Answer:** Trézéguet
**Why it fails:** Trézéguet scored only about one goal at the 2019 AFCON (vs Zimbabwe) — Egypt exited in the R16 having played four games. He did not score 4.
**Source:** https://en.wikipedia.org/wiki/Tr%C3%A9z%C3%A9guet_(Egyptian_footballer)
**Remedy:** He scored ~1 at the 2019 AFCON.

### Row 18322 — Egypt (easy) — FAIL: false (Trezeguet scored ~1 at 2021, not 2)
**Q:** Which Egypt attacker scored twice at the 2021 Africa Cup of Nations?
**Answer:** Trézéguet
**Why it fails:** Trézéguet scored about one goal at the 2021 AFCON — the extra-time QF winner vs Morocco. Egypt won three ties on penalties (few open-play goals); he did not score twice.
**Source:** https://en.wikipedia.org/wiki/Tr%C3%A9z%C3%A9guet_(Egyptian_footballer)
**Remedy:** He scored ~1 (the Morocco QF winner).

### Row 18323 — Egypt (easy) — FAIL: false (Trezeguet scored ~1 at 2021, not 2)
**Q:** Which Egypt attacker scored two goals at the 2021 Africa Cup of Nations?
**Answer:** Trézéguet
**Why it fails:** Trézéguet scored about one goal at the 2021 AFCON (the QF winner vs Morocco), not two.
**Source:** https://en.wikipedia.org/wiki/Tr%C3%A9z%C3%A9guet_(Egyptian_footballer)
**Remedy:** He scored ~1 at the 2021 AFCON.

### Row 18330 — Egypt (medium) — FAIL: non-unique (Salah, also a key attacker, started)
**Q:** Which Egypt attacker, key at AFCONs, started their 2018 World Cup group stage match?
**Answer:** Trézéguet
**Why it fails:** Salah (a listed option) is also a key AFCON attacker who started 2018 group games — so 'which key attacker started' is non-unique with Trézéguet.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** Salah also started as an attacker.

### Row 18331 — Egypt (easy) — FAIL: false (Salah was not Egypts 2018 captain)
**Q:** Which Egypt captain at the 2018 World Cup also played for Liverpool?
**Answer:** Mohamed Salah
**Why it fails:** Salah played for Liverpool but was NOT Egypt's 2018 World Cup captain — the captains were El-Hadary and Elmohamady.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** The 2018 captain was El-Hadary/Elmohamady.

### Row 18334 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC)
**Q:** Which Egypt captain led the team at the 2022 FIFA World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Egypt did not play at the 2022 World Cup (lost the playoff to Senegal), so no one captained Egypt 'at the 2022 FIFA World Cup'. (Salah did captain the qualifying campaign.)
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt did not reach the 2022 finals.

### Row 18336 — Egypt (easy) — FAIL: false (Salah was not Egypts 2018 captain)
**Q:** Which Egypt captain played at the 2018 World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Salah was not Egypt's captain at the 2018 World Cup — El-Hadary (and Elmohamady) wore the armband.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** The 2018 captain was El-Hadary/Elmohamady.

### Row 18338 — Egypt (easy) — FAIL: false (Salah was not Egypts 2018 captain)
**Q:** Which Egypt captain scored more World Cup goals in Russia 2018?
**Answer:** Mohamed Salah
**Why it fails:** Salah scored both of Egypt's 2018 goals, but he was NOT the captain — the armband was El-Hadary's/Elmohamady's. Calling him 'Egypt captain' in Russia 2018 is false.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** Salah was the scorer, not the 2018 captain.

### Row 18341 — Egypt (easy) — FAIL: false (Salah was not Egypts 2018 captain)
**Q:** Which Egypt captain was their top scorer at the 2018 World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Salah was Egypt's top scorer at 2018 but NOT the captain (El-Hadary/Elmohamady wore the armband).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** Salah was the scorer, not captain.

### Row 18342 — Egypt (easy) — FAIL: non-unique (Zamalek also had players in the 2018 squad)
**Q:** Which Egypt club had players in the 2018 World Cup squad?
**Answer:** Al Ahly
**Why it fails:** Both Al Ahly AND Zamalek (e.g. Tarek Hamed) had players in Egypt's 2018 squad — so 'which club had players' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** Zamalek also contributed players.

### Row 18344 — Egypt (easy) — FAIL: false (Egypt LOST the 2017 AFCON final)
**Q:** Which Egypt coach oversaw their 2017 AFCON win?
**Answer:** Héctor Cúper
**Why it fails:** Egypt did NOT win the 2017 AFCON — they LOST the final 2-1 to Cameroon. Cúper was the coach, but there was no 2017 'win'.
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations_Final
**Remedy:** Egypt lost the 2017 final; they last won in 2010.

### Row 18353 — Egypt (medium) — FAIL: false (Salah had ONE Golden Boot before 2018)
**Q:** Which Egypt forward had won two Premier League Golden Boots before the 2018 World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Before the June 2018 World Cup, Salah had won only ONE Premier League Golden Boot (2017-18). His second came in 2018-19, AFTER the World Cup.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Salah
**Remedy:** He had one Golden Boot before 2018, not two.

### Row 18358 — Egypt (easy) — FAIL: false (Cuper never coached the Argentina national team)
**Q:** Which Egypt manager at the 2018 World Cup had previously led Argentina?
**Answer:** Héctor Cúper
**Why it fails:** Héctor Cúper is Argentine but never managed the Argentina national team — he coached clubs (Valencia, Inter) and national sides Georgia, Uzbekistan, Egypt, DR Congo and Syria.
**Source:** https://en.wikipedia.org/wiki/H%C3%A9ctor_C%C3%BAper
**Remedy:** Cuper never led Argentina's NT.

### Row 18360 — Egypt (easy) — FAIL: false (Cuper never coached Argentina)
**Q:** Which Egypt manager at the 2018 World Cup previously coached Argentina in 2006?
**Answer:** Héctor Cúper
**Why it fails:** Cúper did NOT coach Argentina in 2006 (or ever) — Argentina's 2006 coach was José Pékerman. Cúper was at clubs then.
**Source:** https://en.wikipedia.org/wiki/H%C3%A9ctor_C%C3%BAper
**Remedy:** Argentina's 2006 coach was Pekerman.

### Row 18363 — Egypt (easy) — FAIL: non-unique (none of the options won 3 in a row)
**Q:** Which Egypt manager did NOT win three consecutive AFCON titles?
**Answer:** Héctor Cúper
**Why it fails:** Only Hassan Shehata (not an option) won three consecutive AFCONs. ALL four options — Cúper, Queiroz, Gharieb, Bradley — did NOT, so 'which did NOT win three' is non-unique.
**Source:** https://en.wikipedia.org/wiki/Egypt_national_football_team
**Remedy:** None of the listed managers won three in a row.

### Row 18390 — Egypt (easy) — FAIL: false (Elneny had ~60 caps at 2018, not 100+)
**Q:** Which Egypt midfielder at the 2018 World Cup had over 100 caps?
**Answer:** Mohamed Elneny
**Why it fails:** Elneny debuted in 2011 and had only ~55-60 caps at the 2018 World Cup — he reached 100 caps years later. He did not have 'over 100 caps' in 2018.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Elneny
**Remedy:** He had ~60 caps in 2018.

### Row 18393 — Egypt (easy) — FAIL: false (Elneny had ~60 caps at 2018, not 100+)
**Q:** Which Egypt midfielder had over 100 caps during the 2018 FIFA World Cup?
**Answer:** Mohamed Elneny
**Why it fails:** Elneny had roughly 60 caps at the 2018 World Cup, not over 100. He reached 100 caps much later.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Elneny
**Remedy:** He had ~60 caps in 2018.

### Row 18394 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC)
**Q:** Which Egypt midfielder played for Arsenal at the 2022 World Cup?
**Answer:** Mohamed Elneny
**Why it fails:** Egypt did not qualify for the 2022 World Cup, so Elneny did not play 'at the 2022 World Cup'. (He did play the qualifiers.)
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals; use 'qualifiers'.

### Row 18397 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC)
**Q:** Which Egypt midfielder with over 100 caps played for Arsenal at the 2022 World Cup?
**Answer:** Mohamed Elneny
**Why it fails:** Egypt did not play the 2022 World Cup, so Elneny did not play 'at the 2022 World Cup'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18399 — Egypt (easy) — FAIL: non-unique (Mohsen also played domestically)
**Q:** Which Egypt player at the 2018 FIFA World Cup played his club football domestically?
**Answer:** Ahmed Fathy
**Why it fails:** Both Ahmed Fathy (Al Ahly) and Marwan Mohsen (Al Ahly, a listed option) played domestically at the 2018 WC — so 'which player played domestically' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** Several 2018 squad members were domestic-based.

### Row 18400 — Egypt (easy) — FAIL: false (El-Hadary won 4 AFCONs, not 7)
**Q:** Which Egypt player at the 2018 World Cup had seven AFCON winner's medals?
**Answer:** Essam El-Hadary
**Why it fails:** El-Hadary personally won FOUR AFCON titles (1998, 2006, 2008, 2010), not seven. Egypt's record 7 titles include 1957, 1959 and 1986 — before his time.
**Source:** https://en.wikipedia.org/wiki/Essam_El_Hadary
**Remedy:** He had 4 AFCON medals.

### Row 18401 — Egypt (easy) — FAIL: false (Hegazi was at West Brom, not domestic)
**Q:** Which Egypt player at the 2018 World Cup played his club football domestically?
**Answer:** Ahmed Hegazi
**Why it fails:** Ahmed Hegazi played for West Bromwich Albion in England at the 2018 World Cup — NOT for Al Ahly domestically.
**Source:** https://en.wikipedia.org/wiki/Ahmed_Hegazi
**Remedy:** Hegazi was a West Brom player in 2018.

### Row 18403 — Egypt (easy) — FAIL: false (Egypt absent from 2022 WC; Al-Ittihad is Saudi)
**Q:** Which Egypt player at the 2022 FIFA World Cup was from the Egyptian Premier League?
**Answer:** Ahmed Hegazi
**Why it fails:** Egypt did not play the 2022 World Cup. Also, Hegazi's club Al-Ittihad is a SAUDI club (Jeddah), not in the Egyptian Premier League.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals; Al-Ittihad is Saudi.

### Row 18404 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC)
**Q:** Which Egypt player at the 2022 FIFA World Cup was not based in the Egyptian Premier League?
**Answer:** Mohamed Salah
**Why it fails:** Egypt did not play the 2022 World Cup, so no Egypt player was 'at the 2022 FIFA World Cup'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18407 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC)
**Q:** Which Egypt player captained the side at the 2022 FIFA World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Egypt did not play the 2022 World Cup, so no one captained Egypt 'at the 2022 FIFA World Cup'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18408 — Egypt (easy) — FAIL: false (Salah was not Egypts 2018 captain)
**Q:** Which Egypt player captained the squad at the 2018 FIFA World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Salah did not captain Egypt at the 2018 World Cup — El-Hadary (and Elmohamady) wore the armband.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** The 2018 captain was El-Hadary/Elmohamady.

### Row 18416 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC)
**Q:** Which Egypt player for the 2022 World Cup was based in the Egyptian Premier League?
**Answer:** Mostafa Mohamed
**Why it fails:** Egypt did not play the 2022 World Cup, so no player was 'for/during the 2022 World Cup'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18417 — Egypt (easy) — FAIL: false premise (no Egypt 2022 WC squad)
**Q:** Which Egypt player from the 2022 FIFA World Cup squad plays for Al Ahly?
**Answer:** Mohamed El Shenawy
**Why it fails:** Egypt did not qualify for the 2022 World Cup, so there was no 'Egypt 2022 World Cup squad'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18418 — Egypt (easy) — FAIL: false (Hassans 184 caps was his 2012 career total)
**Q:** Which Egypt player had 184 caps before the 2006 World Cup?
**Answer:** Ahmed Hassan
**Why it fails:** Ahmed Hassan did NOT have 184 caps before the 2006 World Cup — 184 was his career total at his 2012 retirement. By 2006 he had roughly 100-120 caps.
**Source:** https://en.wikipedia.org/wiki/Ahmed_Hassan_(footballer,_born_1975)
**Remedy:** 184 was his final (2012) total.

### Row 18419 — Egypt (easy) — FAIL: non-unique (El-Hadary & Aboutrika also had more caps)
**Q:** Which Egypt player had more caps than Mohamed Salah in 2018?
**Answer:** Ahmed Hassan
**Why it fails:** In 2018, multiple Egyptians had more caps than Salah — Ahmed Hassan (184), El-Hadary (~159) and Aboutrika (100) all exceed his ~60. The answer is non-unique. (The explanation's '90 caps' for Salah in 2018 is also too high — he had ~60.)
**Source:** https://en.wikipedia.org/wiki/Mohamed_Salah
**Remedy:** El-Hadary and Aboutrika also had more.

### Row 18420 — Egypt (easy) — FAIL: false (Salah had ~35 goals/~55 caps during 2018 qualifying)
**Q:** Which Egypt player had over 50 goals and 90 caps during 2018 World Cup qualifying?
**Answer:** Mohamed Salah
**Why it fails:** During the 2018 qualifying campaign (2016-17) Salah had roughly 35 goals and ~55 caps — not 'over 50 goals and 90 caps'. He passed 50 goals only around 2021-22.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Salah
**Remedy:** He had ~35 goals then.

### Row 18421 — Egypt (easy) — FAIL: non-unique (all options had 90+ caps)
**Q:** Which Egypt player had over 90 caps by the 2022 FIFA World Cup?
**Answer:** Mohamed Salah
**Why it fails:** All four options had over 90 caps — Salah (~90), Ahmed Hassan (184), El-Hadary (159), Elneny (~90). Non-unique.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Salah
**Remedy:** Several players had 90+ caps.

### Row 18434 — Egypt (medium) — FAIL: false premise (Egypt absent from the 2022 WC)
**Q:** Which Egypt player matched his 2018 Golden Boot tally at the 2022 World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Egypt did not play the 2022 World Cup, so Salah did not 'match his Golden Boot tally at the 2022 World Cup'. (And a comedian, Trevor Noah, is a distractor.)
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18437 — Egypt (easy) — FAIL: false (Salah did NOT take/miss in the 2021 final)
**Q:** Which Egypt player missed a penalty in the 2021 AFCON final and 2022 WC qualifying shootout against Senegal?
**Answer:** Mohamed Salah
**Why it fails:** Salah missed in the 2022 qualifying shootout, but he did NOT miss in the 2021 AFCON final — he was the 5th designated taker and Egypt lost (4-2) before his turn. Egypt's final misses were Abdelmonem and Lasheen.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** He didn't take a penalty in the AFCON final.

### Row 18442 — Egypt (easy) — FAIL: false (Salah did not take/miss in the 2021 AFCON final)
**Q:** Which Egypt player missed in the 2021 AFCON final shootout?
**Answer:** Mohamed Salah
**Why it fails:** Salah did NOT miss in the 2021 AFCON final shootout — he was the 5th taker and never took one (Egypt lost 4-2 first). The misses were Abdelmonem and Lasheen.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** Salah didn't take a penalty in the final.

### Row 18443 — Egypt (easy) — FAIL: false (Salah took no penalty in the 2021 final)
**Q:** Which Egypt player missed the crucial penalty in the 2021 AFCON final?
**Answer:** Mohamed Salah
**Why it fails:** There was no Egyptian '5th penalty' missed by Salah — the shootout ended 4-2 before Egypt's 5th. Egypt's misses were Abdelmonem (post) and Lasheen (saved).
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** Egypt's missers were Abdelmonem and Lasheen.

### Row 18445 — Egypt (easy) — FAIL: false (Gabaski was the GK; missers were Abdelmonem & Lasheen)
**Q:** Which Egypt player missed the decisive penalty in the 2021 AFCON final?
**Answer:** Mohamed Abou Gabal
**Why it fails:** Mohamed Abou Gabal (Gabaski) was Egypt's GOALKEEPER in the 2021 final — he did not 'miss the decisive penalty'. Egypt's missed penalties were taken by Abdelmonem and Lasheen.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** Egypt's missers were Abdelmonem and Lasheen.

### Row 18451 — Egypt (easy) — FAIL: false (Salah has ~20 WC-qualifying goals, not 56)
**Q:** Which Egypt player scored 56 goals in FIFA World Cup qualifiers?
**Answer:** Mohamed Salah
**Why it fails:** Salah's goals in FIFA World Cup qualifiers are around 20 (he is the all-time top scorer in African WC qualifying) — not 56. The 56 figure is wrong.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Salah
**Remedy:** He has ~20 WC-qualifying goals.

### Row 18452 — Egypt (easy) — FAIL: wrong count (Salah scored ~5 in 2022 qualifying, not 8)
**Q:** Which Egypt player scored 8 goals in 2022 World Cup qualifiers?
**Answer:** Mohamed Salah
**Why it fails:** Salah scored roughly 5 goals in Egypt's 2022 CAF qualifying (group + playoff), not 8 — and the dataset's own row 18450 says 5.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CAF)
**Remedy:** He scored ~5 in 2022 qualifying.

### Row 18456 — Egypt (hard) — FAIL: false (2010 final was 1-0, no shootout)
**Q:** Which Egypt player scored in the penalty shootout of their 2010 AFCON final win?
**Answer:** Mohamed Aboutrika
**Why it fails:** The 2010 AFCON final was a 1-0 win (Gedo), NOT a penalty shootout — so no one 'scored in the shootout'.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** There was no 2010 final shootout.

### Row 18458 — Egypt (easy) — FAIL: false (Salah had ~35 goals by 2018 qualifying)
**Q:** Which Egypt player scored over 50 goals in 2018 World Cup qualifying?
**Answer:** Mohamed Salah
**Why it fails:** Salah did NOT have over 50 international goals by the 2018 qualifying campaign — he had ~35 then, reaching 50 around 2021-22.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Salah
**Remedy:** He had ~35 goals by 2018.

### Row 18465 — Egypt (easy) — FAIL: false (2010 final was 1-0 open play, no shootout)
**Q:** Which Egypt player scored the winning penalty against Ghana in the 2010 AFCON final?
**Answer:** Mohamed Aboutrika
**Why it fails:** The 2010 AFCON final was won 1-0 by Gedo in open play — there was NO penalty shootout, so Aboutrika did not score a 'winning penalty'.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Gedo scored the open-play winner; no shootout.

### Row 18466 — Egypt (easy) — FAIL: false (2010 final was 1-0, no shootout)
**Q:** Which Egypt player scored the winning penalty in the 2010 AFCON final?
**Answer:** Mohamed Aboutrika
**Why it fails:** The 2010 AFCON final was a 1-0 win (Gedo), not a penalty shootout — there was no 'winning penalty'.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Gedo scored the winner in open play.

### Row 18471 — Egypt (easy) — FAIL: false (Egypt scored 2 goals at 2018, both Salah)
**Q:** Which Egypt player scored their only goal at the 2018 World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Egypt scored TWO goals at the 2018 World Cup — both by Salah (vs Russia and vs Saudi Arabia) — so 'their only goal' (singular) is wrong.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** Salah scored 2; Egypt's goals weren't just one.

### Row 18477 — Egypt (easy) — FAIL: false (Salah did NOT take a penalty in the 2021 final)
**Q:** Which Egypt player took a penalty in the 2021 AFCON final?
**Answer:** Mohamed Salah
**Why it fails:** Salah did not take a penalty in the 2021 AFCON final shootout — he was the 5th designated taker and Egypt lost 4-2 before his turn.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** He never took a penalty in the final.

### Row 18480 — Egypt (easy) — FAIL: false (Salah was not Egypts 2018 captain)
**Q:** Which Egypt player was captain at the 2018 FIFA World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Salah was not Egypt's captain at the 2018 World Cup — El-Hadary/Elmohamady wore the armband.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** The 2018 captain was El-Hadary/Elmohamady.

### Row 18484 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC)
**Q:** Which Egypt player was the talismanic captain at the 2022 FIFA World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Egypt did not play the 2022 World Cup, so no one was 'captain at the 2022 FIFA World Cup'. (Salah captained the qualifiers.)
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18494 — Egypt (easy) — FAIL: duplicate option (Trezequet = Mahmoud Trezeguet)
**Q:** Which Egypt player was top scorer in their 2022 World Cup qualifying group?
**Answer:** Mohamed Salah
**Why it fails:** Two of the options are the same player — 'Trezequet' and 'Mahmoud Trezeguet' — violating the requirement for three distinct distractors.
**Source:** https://en.wikipedia.org/wiki/Tr%C3%A9z%C3%A9guet_(Egyptian_footballer)
**Remedy:** Remove the duplicate Trezeguet option.

### Row 18496 — Egypt (easy) — FAIL: false (Salah played for Arab Contractors, not Al Ahly)
**Q:** Which Egypt player, key to their 2018 World Cup qualifying, benefited from playing for Africa's most successful CAF Champions League club?
**Answer:** Mohamed Salah
**Why it fails:** Salah began his career at El Mokawloon (Arab Contractors), NOT Al Ahly — he never played for Al Ahly. The 'played for Al Ahly early in his career' claim is false.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Salah
**Remedy:** Salah's first club was Arab Contractors.

### Row 18501 — Egypt (easy) — FAIL: false (Salah had ~60 caps/~35 goals at 2018)
**Q:** Which Egypt player, with over 90 caps and 50+ goals, was selected for the 2018 FIFA World Cup?
**Answer:** Mohamed Salah
**Why it fails:** When selected for the 2018 World Cup, Salah had roughly 60 caps and ~35 goals — NOT 'over 90 caps and 50+ goals'. Those figures came years later.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Salah
**Remedy:** His 2018 figures were ~60 caps / ~35 goals.

### Row 18507 — Egypt (easy) — FAIL: false (Egypt LOST to Senegal; 1st leg 1-0 was an own goal)
**Q:** Which Egypt player's penalty secured their 2022 World Cup qualifying win over Senegal?
**Answer:** Mohamed Salah
**Why it fails:** Egypt did NOT win their 2022 qualifying tie vs Senegal — they lost on penalties (1-1 agg). Their 1-0 first-leg win came from a Saliou Ciss OWN GOAL, not a Salah penalty.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Egypt lost the tie; the 1-0 was an own goal.

### Row 18514 — Egypt (medium) — FAIL: false (2017-18 was his FIRST Golden Boot)
**Q:** Which Egypt star won his second Premier League Golden Boot in the same year as the 2018 World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Salah's 2017-18 Golden Boot (the one concluding in 2018) was his FIRST, not his second — his second came in 2018-19.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Salah
**Remedy:** 2017-18 was his first Golden Boot.

### Row 18517 — Egypt (medium) — FAIL: false (Salah had ONE Golden Boot before 2018)
**Q:** Which Egypt star's Premier League Golden Boot wins preceded his 2018 World Cup campaign?
**Answer:** Mohamed Salah
**Why it fails:** Before the 2018 World Cup Salah had won only ONE Premier League Golden Boot (2017-18), not two — the second came 2018-19, after the WC.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Salah
**Remedy:** One Golden Boot before 2018, not two.

### Row 18519 — Egypt (medium) — FAIL: false (the 2026 squad is more overseas-based than 2018)
**Q:** Which Egypt World Cup squad had the most overseas players: 2018 or 2026?
**Answer:** 2018
**Why it fails:** Egypt's 2018 squad was domestic-heavy (as the dataset's own rows state), whereas the 2026 squad has more Europe/overseas-based players (Salah, Marmoush, Elneny, etc.). So 2018 did NOT have the most overseas players.
**Source:** https://en.wikipedia.org/wiki/Egypt_national_football_team
**Remedy:** The 2026 squad is more overseas-based.

### Row 18525 — Egypt (easy) — FAIL: false (Trezeguet WAS in the 2018 squad)
**Q:** Which Egyptian attacker was key at AFCONs but missed the 2018 World Cup?
**Answer:** Trézéguet
**Why it fails:** Trézéguet was IN Egypt's 2018 World Cup squad and played (he started the opener vs Uruguay) — he did NOT miss the 2018 World Cup.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** Trezeguet played at the 2018 WC.

### Row 18529 — Egypt (easy) — FAIL: false (Egypt did not play Guinea in 2022 qualifying)
**Q:** Which Egyptian captain scored a hat-trick in a 2022 World Cup qualifier?
**Answer:** Mohamed Salah
**Why it fails:** Egypt's 2022 CAF qualifying group (2nd round) was Gabon, Libya and Angola — they did NOT play Guinea. So Salah did not score a hat-trick vs Guinea in a 2022 qualifier. (The options are also garbled.)
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Egypt's 2022 group had no Guinea.

### Row 18530 — Egypt (medium) — FAIL: false (Egypt did NOT qualify for 2022)
**Q:** Which Egyptian captain's goals secured their 2022 FIFA World Cup qualification?
**Answer:** Mohamed Salah
**Why it fails:** Egypt FAILED to qualify for the 2022 World Cup (lost the playoff to Senegal), so no captain's goals 'secured their 2022 qualification'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt did not qualify for 2022.

### Row 18534 — Egypt (easy) — FAIL: false (Elneny was at Arsenal in 2017, not Al Ahly)
**Q:** Which Egyptian club did Mohamed Elneny play for during the 2017 AFCON?
**Answer:** Al Ahly
**Why it fails:** Elneny joined Arsenal in January 2016 — so at the 2017 AFCON he was an Arsenal player, NOT Al Ahly. (He last played for Al Ahly in 2013.)
**Source:** https://en.wikipedia.org/wiki/Mohamed_Elneny
**Remedy:** Elneny was at Arsenal in 2017.

### Row 18541 — Egypt (easy) — FAIL: non-unique (Zamalek and Ismaily also won the CAF CL)
**Q:** Which Egyptian club has won the CAF Champions League?
**Answer:** Al Ahly
**Why it fails:** Multiple listed Egyptian clubs have won the CAF Champions League — Al Ahly (12), Zamalek (5) AND Ismaily (1) — so 'which has won' is non-unique.
**Source:** https://en.wikipedia.org/wiki/CAF_Champions_League
**Remedy:** Zamalek and Ismaily also won it.

### Row 18556 — Egypt (easy) — FAIL: false (Wydad won the 2021-22 CAF CL, not Al Ahly)
**Q:** Which Egyptian club's fans saw their team win the 2022 CAF Champions League?
**Answer:** Al Ahly
**Why it fails:** Al Ahly did NOT win 'the 2022 CAF Champions League' — Wydad Casablanca beat Al Ahly 2-0 in the 2021-22 final (May 2022). Al Ahly won 2020-21 and 2022-23.
**Source:** https://en.wikipedia.org/wiki/2021%E2%80%9322_CAF_Champions_League
**Remedy:** Wydad won the 2022 final.

### Row 18557 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC finals)
**Q:** Which Egyptian club's players featured at the 2022 FIFA World Cup?
**Answer:** Al Ahly
**Why it fails:** Egypt did not play the 2022 World Cup, so no club's players 'featured at the 2022 FIFA World Cup' (the explanation's 'tournament' claim is false).
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18575 — Egypt (easy) — FAIL: false (Elneny had ~35 caps when he joined Arsenal in 2016)
**Q:** Which Egyptian midfielder debuted for Arsenal in 2016 after over 100 caps?
**Answer:** Mohamed Elneny
**Why it fails:** Elneny joined Arsenal in January 2016 with roughly 35-40 caps, NOT 'over 100'. He reached 100 caps years later.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Elneny
**Remedy:** He had ~35 caps in 2016.

### Row 18582 — Egypt (easy) — FAIL: false (Elneny had ~60 caps at 2018, not 100+)
**Q:** Which Egyptian midfielder with over 100 caps played for Arsenal and was a key part of their 2018 World Cup squad?
**Answer:** Mohamed Elneny
**Why it fails:** Elneny had roughly 60 caps at the 2018 World Cup, not over 100.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Elneny
**Remedy:** He had ~60 caps in 2018.

### Row 18583 — Egypt (easy) — FAIL: false (Elneny had ~60 caps in 2018, not 100+)
**Q:** Which Egyptian midfielder with over 100 caps played for Arsenal in 2018?
**Answer:** Mohamed Elneny
**Why it fails:** Elneny had ~60 caps at the 2018 World Cup, not over 100.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Elneny
**Remedy:** He had ~60 caps in 2018.

### Row 18584 — Egypt (easy) — FAIL: false (Elneny had ~60 caps in 2018, not 100+)
**Q:** Which Egyptian midfielder with over 100 caps started the 2018 World Cup match vs Saudi Arabia?
**Answer:** Mohamed Elneny
**Why it fails:** Elneny started vs Saudi Arabia but had ~60 caps at the 2018 World Cup, not 'over 100'.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Elneny
**Remedy:** He had ~60 caps in 2018.

### Row 18585 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC)
**Q:** Which Egyptian player at the 2022 World Cup had over 90 caps?
**Answer:** Mohamed Salah
**Why it fails:** Egypt did not play the 2022 World Cup, so no Egypt player was 'at the 2022 World Cup'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18586 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC)
**Q:** Which Egyptian player at the 2022 World Cup played for a European club?
**Answer:** Mohamed Salah
**Why it fails:** Egypt did not play the 2022 World Cup, so no Egypt player was 'at the 2022 World Cup'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18587 — Egypt (medium) — FAIL: false (Egypt did NOT qualify for 2022)
**Q:** Which Egyptian player captained and scored to secure 2022 World Cup qualification?
**Answer:** Mohamed Salah
**Why it fails:** Egypt FAILED to qualify for the 2022 World Cup (lost the playoff to Senegal), so no captain 'scored to secure 2022 qualification'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt did not qualify for 2022.

### Row 18589 — Egypt (easy) — FAIL: false (El-Hadary captained the Saudi game, not Salah)
**Q:** Which Egyptian player captained the side against Saudi Arabia at the 2018 World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Salah was not captain at the 2018 World Cup — El-Hadary captained Egypt against Saudi Arabia (where he became the oldest WC player).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** El-Hadary captained the Saudi game.

### Row 18593 — Egypt (easy) — FAIL: false (Salah is a Liverpool player, not Al Ahly/Zamalek)
**Q:** Which Egyptian player from Al Ahly or Zamalek scored more 2022 World Cup qualifier goals?
**Answer:** Mohamed Salah
**Why it fails:** Salah plays for Liverpool, NOT Al Ahly or Zamalek — so 'which player FROM Al Ahly or Zamalek scored more' cannot be Salah. The top Al Ahly/Zamalek scorer would be someone like Mostafa Mohamed (Zamalek).
**Source:** https://en.wikipedia.org/wiki/Mohamed_Salah
**Remedy:** Salah isn't from those clubs; reframe.

### Row 18594 — Egypt (easy) — FAIL: false (184 was Hassans 2012 total, not by 2006)
**Q:** Which Egyptian player had 184 caps before 2006?
**Answer:** Ahmed Hassan
**Why it fails:** Ahmed Hassan did NOT have 184 caps before 2006 — 184 was his final total at his 2012 retirement. By 2006 he had ~100-120.
**Source:** https://en.wikipedia.org/wiki/Ahmed_Hassan_(footballer,_born_1975)
**Remedy:** 184 was his 2012 career total.

### Row 18595 — Egypt (easy) — FAIL: false (Hassan had ~170 caps by 2010, not 180+)
**Q:** Which Egyptian player had over 180 caps before 2010?
**Answer:** Ahmed Hassan
**Why it fails:** Ahmed Hassan had roughly 170-175 caps by 2010 — he only reached 184 in 2012. He did not have 'over 180' before 2010.
**Source:** https://en.wikipedia.org/wiki/Ahmed_Hassan_(footballer,_born_1975)
**Remedy:** He reached 184 in 2012.

### Row 18606 — Egypt (easy) — FAIL: non-unique (El-Hadary & Elneny also not most-capped)
**Q:** Which Egyptian player is NOT their nation's most-capped player?
**Answer:** Mohamed Salah
**Why it fails:** Ahmed Hassan is Egypt's most-capped player, so Salah, El-Hadary AND Elneny (three options) are all 'NOT the most-capped'. Non-unique.
**Source:** https://en.wikipedia.org/wiki/Ahmed_Hassan_(footballer,_born_1975)
**Remedy:** Three options are not the most-capped.

### Row 18612 — Egypt (easy) — FAIL: false (Salah did NOT take/miss in the 2021 final)
**Q:** Which Egyptian player missed a penalty in the 2021 AFCON final shootout?
**Answer:** Mohamed Salah
**Why it fails:** Salah did not miss in the 2021 AFCON final shootout — he was the 5th designated taker and never took one. Egypt's misses were Abdelmonem and Lasheen.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** Salah took no penalty in the final.

### Row 18613 — Egypt (easy) — FAIL: false (Salah, not Elneny, missed the first 2022 penalty)
**Q:** Which Egyptian player missed his penalty in the 2022 World Cup qualifying shootout loss to Senegal?
**Answer:** Mohamed Elneny
**Why it fails:** It was MOHAMED SALAH (a listed option) who missed Egypt's FIRST penalty in the 2022 qualifying shootout — not Elneny.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Salah missed the first penalty.

### Row 18614 — Egypt (medium) — FAIL: non-unique (El-Hadary also participated in 2018 qualifying)
**Q:** Which Egyptian player participated in their 2018 World Cup qualification campaign?
**Answer:** Mohamed Salah
**Why it fails:** Both Salah AND El-Hadary (a listed option, the GK) participated in Egypt's 2018 qualifying campaign — so the answer is non-unique. (Amr Zaki and Ahmed Hassan had retired.)
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CAF)
**Remedy:** El-Hadary also participated.

### Row 18615 — Egypt (easy) — FAIL: false (Ahmed Hassan retired 2012, not before 2010)
**Q:** Which Egyptian player retired before the 2010 FIFA World Cup era?
**Answer:** Ahmed Hassan
**Why it fails:** Ahmed Hassan retired from international football in 2012 — AFTER the 2010 World Cup era (he played in the 2010 qualifying). He did not retire 'before the 2010 World Cup era'.
**Source:** https://en.wikipedia.org/wiki/Ahmed_Hassan_(footballer,_born_1975)
**Remedy:** He retired in 2012.

### Row 18620 — Egypt (easy) — FAIL: duplicate option (Mahmoud Trezeguet = Trezeguet)
**Q:** Which Egyptian player scored in the 2019 AFCON opener hosted by Egypt?
**Answer:** Mahmoud Trezeguet
**Why it fails:** Two options are the same player — 'Mahmoud Trezeguet' and 'Trézéguet' — violating the distinct-distractors rule. (He did score the 2019 opener winner vs Zimbabwe.)
**Source:** https://en.wikipedia.org/wiki/Tr%C3%A9z%C3%A9guet_(Egyptian_footballer)
**Remedy:** Remove the duplicate Trezeguet option.

### Row 18626 — Egypt (easy) — FAIL: false (Gedos 2010 winner was open play, not a penalty)
**Q:** Which Egyptian player scored the winning penalty in the 2010 AFCON final?
**Answer:** Mohamed Nagy (Gedo)
**Why it fails:** Gedo scored the 2010 AFCON final winner in OPEN PLAY (85'), in a 1-0 win — it was NOT a penalty, and there was no shootout.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Gedo's goal was open play.

### Row 18628 — Egypt (easy) — FAIL: non-unique (all four started the 2010 final)
**Q:** Which Egyptian player started in the 2010 AFCON final win?
**Answer:** Essam El-Hadary
**Why it fails:** All four options — El-Hadary, Aboutrika, Ahmed Hassan and Wael Gomaa — started Egypt's 2010 AFCON final. So 'which player started' is non-unique.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** All four were starters.

### Row 18631 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC)
**Q:** Which Egyptian player was captain at the 2022 FIFA World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Egypt did not play the 2022 World Cup, so no one was 'captain at the 2022 FIFA World Cup'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18634 — Egypt (easy) — FAIL: false premise (no 2022 squad; non-unique)
**Q:** Which Egyptian player was in the squad for the 2018 World Cup but not 2022?
**Answer:** Mohamed Elneny
**Why it fails:** Egypt had no 2022 World Cup squad (they didn't qualify), so 'in 2018 but not 2022' applies to ALL the listed 2018 players (Salah, Trezeguet, Hegazi too) — the premise is false and the answer non-unique.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18636 — Egypt (easy) — FAIL: false premise (Salah wasnt captain; non-unique)
**Q:** Which Egyptian player was not a World Cup captain in 2018?
**Answer:** Mohamed Elneny
**Why it fails:** The premise that 'Salah was Egypt's 2018 captain' is false (El-Hadary/Elmohamady were) — so Salah, Elneny AND Fathy were all 'not captains', making 'which was NOT a captain' non-unique and built on a false claim.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** Salah was not the 2018 captain either.

### Row 18637 — Egypt (easy) — FAIL: false premise (no Egypt 2022 squad)
**Q:** Which Egyptian player was the leading scorer in their 2022 World Cup squad?
**Answer:** Mohamed Salah
**Why it fails:** Egypt did not qualify for the 2022 World Cup, so there was no 'Egypt 2022 World Cup squad'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18638 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC)
**Q:** Which Egyptian player was the team's captain and talisman at the 2022 FIFA World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Egypt did not play the 2022 World Cup, so no one was 'captain/talisman at the 2022 World Cup'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18647 — Egypt (easy) — FAIL: false premise (no Egypt 2010 WC squad)
**Q:** Which Egyptian player's 184 caps made him their 2010 World Cup squad's most experienced?
**Answer:** Ahmed Hassan
**Why it fails:** Egypt FAILED to qualify for the 2010 World Cup — there was no 'Egypt 2010 World Cup squad' for Ahmed Hassan to be the most experienced in.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt did not qualify for 2010.

### Row 18654 — Egypt (medium) — FAIL: false (Egypt did NOT qualify for 2022)
**Q:** Which Egyptian player's goals secured their 2022 World Cup qualification?
**Answer:** Mohamed Salah
**Why it fails:** Egypt FAILED to qualify for the 2022 World Cup (lost the playoff to Senegal), so no player's goals 'secured their 2022 qualification'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt did not qualify for 2022.

### Row 18661 — Egypt (easy) — FAIL: false (Egypt LOST to Senegal; 1st leg was an own goal)
**Q:** Which Egyptian scored two goals vs Senegal to qualify for the 2022 World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Egypt did NOT win both legs or qualify — they drew 1-1 on aggregate and lost on penalties. The 1-0 first leg was a Saliou Ciss OWN GOAL, not a Salah goal, and they lost the 2nd leg 0-1.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Egypt lost the tie; the 1-0 was an own goal.

### Row 18662 — Egypt (easy) — FAIL: false (2018 qualifiers were at Borg El Arab)
**Q:** Which Egyptian stadium hosted 2018 qualifiers and holds about 75,000 people?
**Answer:** Cairo International Stadium
**Why it fails:** Egypt's 2018 World Cup home qualifiers (incl. vs Ghana and Congo) were played at Borg El Arab Stadium in Alexandria — NOT Cairo International. (Borg El Arab ~86,000 is also larger than Cairo's ~75,000.)
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_%E2%80%93_CAF_third_round
**Remedy:** The 2018 qualifiers were at Borg El Arab.

### Row 18669 — Egypt (easy) — FAIL: false (Ghana 2018 qualifier was at Borg El Arab)
**Q:** Which Egyptian stadium hosted the 2017 World Cup qualifier vs Ghana, its primary venue?
**Answer:** Cairo International Stadium
**Why it fails:** Egypt's qualifier vs Ghana (2-0, Nov 2016) was at Borg El Arab Stadium in Alexandria, NOT Cairo International.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_%E2%80%93_CAF_third_round
**Remedy:** It was at Borg El Arab.

### Row 18670 — Egypt (easy) — FAIL: false (Ghana 2018 qualifier was at Borg El Arab)
**Q:** Which Egyptian stadium hosted the 2018 World Cup qualifier vs Ghana?
**Answer:** Cairo International Stadium
**Why it fails:** The Egypt-Ghana 2018 qualifier was at Borg El Arab (Alexandria), not Cairo International.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_%E2%80%93_CAF_third_round
**Remedy:** It was at Borg El Arab.

### Row 18676 — Egypt (easy) — FAIL: false (Ghana 2018 qualifier was at Borg El Arab)
**Q:** Which Egyptian stadium hosted their 2018 World Cup qualifier against Ghana?
**Answer:** Cairo International Stadium
**Why it fails:** The Egypt-Ghana 2018 qualifier was at Borg El Arab, not Cairo International.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_%E2%80%93_CAF_third_round
**Remedy:** It was at Borg El Arab.

### Row 18678 — Egypt (easy) — FAIL: false (Borg El Arab was the primary 2018 venue)
**Q:** Which Egyptian stadium was the primary venue for their 2018 World Cup qualifiers?
**Answer:** Cairo International Stadium
**Why it fails:** Egypt's 2018 home qualifiers (Ghana, Congo) were at Borg El Arab in Alexandria — that was their primary 2018 qualifier venue, not Cairo International.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_%E2%80%93_CAF_third_round
**Remedy:** Borg El Arab was the primary 2018 venue.

### Row 18683 — Egypt (easy) — FAIL: false (2018 qualifiers were at Borg El Arab)
**Q:** Which Egyptian stadium, capacity near 75,000, hosted 2018 World Cup qualifiers?
**Answer:** Cairo International Stadium
**Why it fails:** Egypt's 2018 home qualifiers were at Borg El Arab, not the 75,000-capacity Cairo International.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_%E2%80%93_CAF_third_round
**Remedy:** The 2018 qualifiers were at Borg El Arab.

### Row 18684 — Egypt (easy) — FAIL: false (Cairo ~75k is SMALLER than Borg El Arab ~86k)
**Q:** Which Egyptian stadium, used for 2018 World Cup qualifiers, has a larger capacity than Alexandria's Borg El Arab?
**Answer:** Cairo International Stadium
**Why it fails:** Cairo International (~75,000) is NOT larger than Borg El Arab (~86,000) — Borg El Arab is bigger. And the 2018 qualifiers were at Borg El Arab.
**Source:** https://en.wikipedia.org/wiki/Borg_El_Arab_Stadium
**Remedy:** Borg El Arab (~86k) is larger.

### Row 18685 — Egypt (easy) — FAIL: false (Cairo ~75k is smaller than Borg El Arab ~86k)
**Q:** Which Egyptian stadium, used for 2022 World Cup qualifiers, has a larger capacity?
**Answer:** Cairo International Stadium
**Why it fails:** Cairo International (~75,000) is smaller than Borg El Arab (~86,000), not larger.
**Source:** https://en.wikipedia.org/wiki/Borg_El_Arab_Stadium
**Remedy:** Borg El Arab is larger.

### Row 18686 — Egypt (easy) — FAIL: false (Ghana 2018 qualifier was at Borg El Arab)
**Q:** Which Egyptian stadium, with a 75,000 capacity, hosted the 2017 World Cup qualifier against Ghana?
**Answer:** Cairo International Stadium
**Why it fails:** The Egypt-Ghana 2018 qualifier was at Borg El Arab, not Cairo International.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_%E2%80%93_CAF_third_round
**Remedy:** It was at Borg El Arab.

### Row 18687 — Egypt (easy) — FAIL: false (2018 qualifiers were at Borg El Arab)
**Q:** Which Egyptian stadium's 75,000 capacity was a 2018 World Cup qualifier venue?
**Answer:** Cairo International Stadium
**Why it fails:** Egypt's 2018 home qualifiers were at Borg El Arab, not Cairo International.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_%E2%80%93_CAF_third_round
**Remedy:** The 2018 qualifiers were at Borg El Arab.

### Row 18689 — Egypt (easy) — FAIL: non-unique (Egypt absent from 2010; all 2018 players fit)
**Q:** Which Egyptian star was in Russia 2018 but not in South Africa 2010?
**Answer:** Mohamed Salah
**Why it fails:** Egypt did not play the 2010 World Cup, so EVERY 2018 squad member was 'in 2018 but not 2010' — Salah, El-Hadary AND Elneny all fit. Non-unique.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Use a player-specific trait.

### Row 18690 — Egypt (easy) — FAIL: non-unique (El-Hadary & Elneny also in the 2018 squad)
**Q:** Which Egyptian star was included in their 2018 World Cup squad?
**Answer:** Mohamed Salah
**Why it fails:** Salah, El-Hadary AND Elneny (three options) were all in Egypt's 2018 squad — non-unique. (Only Ahmed Hassan, retired, was not.)
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** Several options were in the 2018 squad.

### Row 18698 — Egypt (easy) — FAIL: false (Salah not 2018 captain; Egypt absent from 2022 WC)
**Q:** Which Egyptian talisman captained his side in both the 2018 and 2022 World Cups?
**Answer:** Mohamed Salah
**Why it fails:** Salah did not captain Egypt at BOTH the 2018 and 2022 World Cups — he wasn't the 2018 captain (El-Hadary was), and Egypt didn't play the 2022 World Cup at all.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** He wasn't 2018 captain; Egypt missed 2022.

### Row 18699 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC)
**Q:** Which Egyptian talisman captained his team at the 2022 World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Egypt did not play the 2022 World Cup, so no one captained Egypt 'at the 2022 World Cup'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18709 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC finals)
**Q:** Which manager coached Egypt at the 2022 FIFA World Cup?
**Answer:** Carlos Queiroz
**Why it fails:** Egypt did not play the 2022 World Cup, so no one 'coached Egypt at the 2022 FIFA World Cup'. (Queiroz coached the qualifying campaign.)
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18710 — Egypt (easy) — FAIL: non-unique (Queiroz & Bradley also never coached Egypt at a WC)
**Q:** Which manager did NOT coach Egypt at a FIFA World Cup?
**Answer:** Hassan Shehata
**Why it fails:** Only Cúper coached Egypt at a World Cup (2018). Shehata, Queiroz AND Bradley all did NOT — so 'which did NOT coach at a WC' is non-unique.
**Source:** https://en.wikipedia.org/wiki/Egypt_national_football_team
**Remedy:** Three options never coached Egypt at a WC.

### Row 18714 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC finals)
**Q:** Which manager led Egypt at the 2022 FIFA World Cup?
**Answer:** Carlos Queiroz
**Why it fails:** Egypt did not play the 2022 World Cup finals — Queiroz led only the qualifying campaign.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18719 — Egypt (easy) — FAIL: false (Hossam Hassan led the 2026 qualification, not Vitoria)
**Q:** Which manager led Egypt to qualify for the 2026 FIFA World Cup?
**Answer:** Rui Vitória
**Why it fails:** Rui Vitória departed in 2024; HOSSAM HASSAN (a listed option) took over in Feb 2024 and led Egypt to 2026 World Cup qualification (clinched Oct 2025).
**Source:** https://en.wikipedia.org/wiki/Hossam_Hassan
**Remedy:** Change the answer to Hossam Hassan.

### Row 18728 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC finals)
**Q:** Which manager led Egypt's squad at the 2022 World Cup?
**Answer:** Carlos Queiroz
**Why it fails:** Egypt did not play the 2022 World Cup, so no one 'led Egypt's squad at the 2022 World Cup'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18735 — Egypt (easy) — FAIL: false premise (no Egypt 2022 WC squad)
**Q:** Which manager selected Egypt's squad for the 2022 FIFA World Cup?
**Answer:** Carlos Queiroz
**Why it fails:** Egypt did not qualify for the 2022 World Cup, so there was no '2022 World Cup squad' to select.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18756 — Egypt (easy) — FAIL: non-unique (none of the four shares Egypts 7)
**Q:** Which nation does NOT share Egypt's record of seven AFCON titles?
**Answer:** Senegal
**Why it fails:** Egypt holds the record alone with 7 AFCON titles — so NONE of Senegal (1), Cameroon (5), Ghana (4) or Nigeria (3) 'shares' it. The 'does not share' answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Africa_Cup_of_Nations
**Remedy:** None of the four has 7 titles.

### Row 18764 — Egypt (easy) — FAIL: non-unique (all four have fewer than 7)
**Q:** Which nation has won fewer AFCON titles than Egypt's seven?
**Answer:** Nigeria
**Why it fails:** All four options have fewer AFCON titles than Egypt's 7 — Cameroon (5), Ghana (4), Nigeria (3), Ivory Coast (3). Non-unique.
**Source:** https://en.wikipedia.org/wiki/Africa_Cup_of_Nations
**Remedy:** All four have fewer than 7.

### Row 18765 — Egypt (easy) — FAIL: false (Cameroon never solely held the AFCON record)
**Q:** Which nation held the record for most AFCON titles before Egypt's seventh win?
**Answer:** Cameroon
**Why it fails:** Cameroon did NOT hold the AFCON record before Egypt's 7th — Egypt already led with 6 titles (from 2008), and earlier the most-decorated was Ghana (4 by 1982). Cameroon only reached 5 in 2017, and had just 4 before 2010.
**Source:** https://en.wikipedia.org/wiki/Africa_Cup_of_Nations
**Remedy:** Egypt led from 2006; Cameroon never held it alone.

### Row 18767 — Egypt (easy) — FAIL: garbled premise (Egypt hosted 2019, not 2023)
**Q:** Which nation hosted the 2019 AFCON before Egypt in 2023?
**Answer:** Cameroon
**Why it fails:** The question is incoherent — the 2019 AFCON was hosted by EGYPT (reassigned from Cameroon), and Egypt did NOT host in 2023 (the 2023 edition was hosted by Ivory Coast). The 'before Egypt in 2023' framing is false.
**Source:** https://en.wikipedia.org/wiki/2019_Africa_Cup_of_Nations
**Remedy:** Egypt hosted 2019; Ivory Coast hosted 2023.

### Row 18773 — Egypt (easy) — FAIL: false premise (2010 final was 1-0, not penalties)
**Q:** Which nation lost to Egypt on penalties in the 2010 AFCON final?
**Answer:** Ghana
**Why it fails:** Egypt beat Ghana 1-0 in the 2010 final (Gedo) — NOT on penalties. The question's 'on penalties' premise is false.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** It was a 1-0 win.

### Row 18782 — Egypt (easy) — FAIL: self-referential (answer is Egypt itself)
**Q:** Which nation, like Egypt under Hassan Shehata, won three consecutive AFCON titles?
**Answer:** Egypt
**Why it fails:** Egypt is the ONLY nation to win three consecutive AFCONs, so 'which nation, like Egypt, did it' has no distinct answer — the answer is Egypt itself (self-referential/circular).
**Source:** https://en.wikipedia.org/wiki/Africa_Cup_of_Nations
**Remedy:** No other nation has done it; rephrase.

### Row 18786 — Egypt (easy) — FAIL: false (Egypt didnt surpass Cameroon with the 7th)
**Q:** Which nation's record did Egypt surpass by winning a seventh AFCON title?
**Answer:** Cameroon
**Why it fails:** Egypt did not surpass 'Cameroon's record' by winning a 7th — Egypt had led since their 5th (2006), and Cameroon had only 4 titles then (their 5th came in 2017). Egypt never shared a record-at-6 with Cameroon.
**Source:** https://en.wikipedia.org/wiki/Africa_Cup_of_Nations
**Remedy:** Egypt led from 2006; not a Cameroon record.

### Row 18798 — Egypt (easy) — FAIL: false (Mane scored the deciding penalty, not twice in the legs)
**Q:** Which Senegal player scored twice to eliminate Egypt in 2022 World Cup qualifying?
**Answer:** Sadio Mané
**Why it fails:** Mané did NOT score twice in the two legs — the legs' goals were a Ciss own goal (1st leg) and Boulaye Dia (2nd leg). Mané scored the WINNING PENALTY in the shootout.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Mane scored the shootout winner, not 2 open-play goals.

### Row 18806 — Egypt (easy) — FAIL: false (2018 qualifiers were at Borg El Arab)
**Q:** Which stadium hosted Egypt's 2018 World Cup qualifiers as its primary 75,000-capacity venue?
**Answer:** Cairo International Stadium
**Why it fails:** Egypt's 2018 home qualifiers (Ghana, Congo) were at Borg El Arab — Cairo International was NOT the primary 2018 qualifier venue.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_%E2%80%93_CAF_third_round
**Remedy:** Borg El Arab was the 2018 venue.

### Row 18807 — Egypt (easy) — FAIL: false (the 2022 playoff was in Dakar, not Olembe)
**Q:** Which stadium hosted Egypt's 2021 AFCON final and 2022 WC qualifying losses to Senegal?
**Answer:** Olembe Stadium
**Why it fails:** The 2021 AFCON final was at Olembe Stadium (Yaoundé), but the 2022 WC qualifying playoff 2nd leg was at the Stade Abdoulaye Wade in Dakar, NOT Olembe. They were not at the same stadium.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CAF)
**Remedy:** The 2022 playoff 2nd leg was in Dakar.

### Row 18811 — Egypt (easy) — FAIL: false (the 2021 AFCON was in Cameroon, not Cairo)
**Q:** Which stadium hosts Egypt's 2021 AFCON matches as their primary venue?
**Answer:** Cairo International Stadium
**Why it fails:** Egypt's 2021 AFCON matches were played in CAMEROON (Douala, Yaoundé) — Cameroon hosted that tournament (Jan 2022). Cairo International did NOT host Egypt's 2021 AFCON matches.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations
**Remedy:** The 2021 AFCON was in Cameroon.

### Row 18816 — Egypt (easy) — FAIL: false (Egypt was NOT the 2021 AFCON host)
**Q:** Which team beat host nation Egypt in the 2021 AFCON final?
**Answer:** Senegal
**Why it fails:** Egypt was not the host of the 2021 AFCON — CAMEROON hosted it. Egypt reached the final but were not the host nation.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations
**Remedy:** Cameroon hosted 2021; Egypt hosted 2019.

### Row 18825 — Egypt (easy) — FAIL: false premise (2010 final was 1-0, not penalties)
**Q:** Which team lost to Egypt on penalties in the 2010 AFCON final?
**Answer:** Ghana
**Why it fails:** Egypt beat Ghana 1-0 in the 2010 final (Gedo), NOT on penalties — the 'on penalties' premise is false.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** It was a 1-0 win.

### Row 18832 — Egypt (medium) — FAIL: incomplete (Egypt lost to THREE, incl. Saudi Arabia)
**Q:** Which two nations defeated Egypt in the 2018 World Cup group stage?
**Answer:** Uruguay and Russia
**Why it fails:** Egypt lost ALL THREE 2018 group games — to Uruguay, Russia AND Saudi Arabia. Naming only 'two' (Uruguay and Russia) omits Saudi Arabia, who also defeated Egypt 2-1.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_A
**Remedy:** Egypt lost to all three group opponents.

### Row 18839 — Egypt (hard) — FAIL: false (Egypt did not play 2022 qualifiers in 2019)
**Q:** Which World Cup qualifiers did Egypt host in 2019?
**Answer:** 2022 FIFA World Cup
**Why it fails:** Egypt, as a seeded team, entered the CAF 2022 qualifying in the second round (2021) — they did NOT play any 2022 World Cup qualifiers in 2019 (the 2019 first round was for lower-ranked teams).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Egypt's 2022 qualifying began in 2021.

### Row 18847 — Egypt (easy) — FAIL: false (Egypt did NOT qualify for 2022)
**Q:** Who captained Egypt to qualify for the 2022 FIFA World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Egypt failed to qualify for the 2022 World Cup, so no one 'captained Egypt to qualify' for it. (Salah captained the failed campaign.)
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt did not qualify for 2022.

### Row 18849 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC)
**Q:** Who captained the Egypt team at the 2022 FIFA World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Egypt did not play the 2022 World Cup, so no one captained Egypt 'at the 2022 FIFA World Cup'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18858 — Egypt (easy) — FAIL: false premise (Egypt absent from the 2022 WC)
**Q:** Who was Egypt's captain at the 2022 FIFA World Cup?
**Answer:** Mohamed Salah
**Why it fails:** Egypt did not play the 2022 World Cup, so there was no captain 'at the 2022 FIFA World Cup'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

### Row 18860 — Egypt (easy) — FAIL: false premise (no Egypt 2022 WC finals squad)
**Q:** Whose club Al Ahly's 12 Champions League wins aided Egypt's World Cup 2022 squad?
**Answer:** Al Ahly players
**Why it fails:** Egypt did not qualify for the 2022 World Cup, so there was no '2022 World Cup squad'. (Al Ahly did supply the core of the qualifying squad.)
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_FIFA_World_Cup
**Remedy:** Egypt missed the 2022 finals.

## Australia (rows 1544–2396)

### Row 1544 — Australia (medium) — FAIL: false premise ("2006 World Cup debut")
**Q:** After Australia's 2006 World Cup debut, when did they join the AFC?
**Answer:** 2006
**Why it fails:** The question calls 2006 Australia's "World Cup debut" — this is factually wrong. Australia's actual World Cup debut was **1974** (West Germany). 2006 was their return after a 32-year absence. Additionally, Australia joined the AFC in **January 2006**, *before* the 2006 World Cup (June–July), not after it, so the causal framing is also reversed.
**Source:** https://en.wikipedia.org/wiki/Australia_at_the_FIFA_World_Cup
**Remedy:** Rewrite as "In which year did Australia move from the OFC to the AFC?" Answer: 2006.

### Row 1549 — Australia (medium) — FAIL: non-unique answer
**Q:** After Australia's 2022 World Cup group stage win over Tunisia, which nation also reached the round of 16?
**Answer:** South Korea
**Why it fails:** **Three** AFC nations reached the 2022 WC round of 16: Australia, South Korea, **and Japan**. Japan beat Spain 2–1 to win Group E and reach the R16 (lost to Croatia on penalties). South Korea is therefore not the only valid answer — Japan is equally correct, but is not listed as a distractor (it is absent from the options entirely, making the question non-unique and incomplete).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Narrow to a uniquely answerable fact, e.g. "Which AFC nation beat Portugal to reach the 2022 WC R16?" (South Korea) or "Which AFC nation eliminated Croatia on penalties in the 2022 WC R16?" (Japan).

### Row 1555 — Australia (easy) — FAIL: false premise (drew vs won)
**Q:** After drawing with Tunisia, which team did Australia beat in their 2022 World Cup group?
**Answer:** Denmark
**Why it fails:** Australia did **not** draw with Tunisia — they **won 1–0** (Mitchell Duke, 23'). The question's premise "after drawing with Tunisia" is factually false.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_D
**Remedy:** Replace "drawing with Tunisia" with "beating Tunisia 1–0" — the rest of the question (beating Denmark) is correct.

### Row 1558 — Australia (medium) — FAIL: wrong answer / misleading framing
**Q:** After their 2022 World Cup run, Australia's best FIFA ranking was which position?
**Answer:** 14th
**Why it fails:** Australia's **all-time best ranking of 14th was achieved in September 2009**, not after the 2022 WC. After the 2022 WC, Australia's best ranking was **27th** (end of calendar year 2022, their highest year-end ranking since 2011). The question implies 14th was a post-2022 achievement, which is incorrect.
**Source:** https://socceroos.com.au/news/socceroos-learn-new-fifa-ranking ; https://www.11v11.com/teams/australia/option/ranking/
**Remedy:** Either fix to "What is Australia's all-time best FIFA ranking?" (Answer: 14th, from Sept 2009) or "What was Australia's best FIFA ranking after the 2022 World Cup?" (Answer: ~27th).

### Row 1565 — Australia (easy) — FAIL: non-unique answer
**Q:** Against which nation did Australian Tim Cahill score in 2014 World Cup qualifying?
**Answer:** Iraq
**Why it fails:** Tim Cahill scored in 2014 WC AFC qualifying against **both Iraq** (16 Oct 2012) **and Oman** (26 Mar 2013). Iraq is one correct answer but not the only one — Oman is equally valid. The question implies a single nation, making the answer non-unique.
**Source:** https://en.wikipedia.org/wiki/List_of_international_goals_scored_by_Tim_Cahill
**Remedy:** Specify: "Against which nation did Tim Cahill score his first 2014 WC qualifying goal?" (Answer: Iraq, Oct 2012) or add Oman to the distractors and rephrase to "which of the following nations."

### Row 1569 — Australia (medium) — FAIL: false premise / wrong answer
**Q:** At the 2018 World Cup, which 2015 Asian Cup finalist did Australia face in their group?
**Answer:** Denmark
**Why it fails:** The 2015 Asian Cup finalists were **Australia** and **South Korea**. Denmark is a European team and did not participate in the 2015 Asian Cup. At the 2018 WC, Australia was in **Group C (France, Denmark, Peru)** — South Korea was in Group F. No 2015 Asian Cup finalist was in Australia's 2018 WC group.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_C ; https://en.wikipedia.org/wiki/2015_AFC_Asian_Cup_Final
**Remedy:** Drop this question; the premise is unfixable. (No 2015 Asian Cup finalist faced Australia in their 2018 WC group.)

### Row 1571 — Australia (easy) — FAIL: non-unique answer
**Q:** At the 2022 World Cup in Qatar, which team did Australia beat 1-0?
**Answer:** Denmark
**Why it fails:** Australia beat **both Tunisia 1–0** (26 Nov) **and Denmark 1–0** (30 Nov) in the 2022 WC group stage. Both Tunisia and Denmark appear in the option list, making the answer non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_D
**Remedy:** Specify the match: "Which team did Australia beat 1–0 in their final group game at the 2022 World Cup?" (Answer: Denmark) to make it unique.

---

## Australia chunk 2 (rows 1580–1650)

### Row 1592 — Australia (hard) — FAIL: wrong venue
**Q:** At which 2014 World Cup stadium did Australian scorer Tim Cahill net his famous volley?
**Answer:** Arena da Baixada
**Why it fails:** Tim Cahill's famous volley against the Netherlands on 18 June 2014 was scored at **Estádio Beira-Rio** in Porto Alegre, not Arena da Baixada (which is in Curitiba). The two stadiums are in different cities entirely.
**Source:** https://www.espn.co.uk/football/match/_/gameId/383286/netherlands-australia
**Remedy:** Change answer to "Estádio Beira-Rio."

### Row 1593 — Australia (medium) — FAIL: wrong venue
**Q:** At which 2014 World Cup venue did Tim Cahill score an acrobatic volley for Australia?
**Answer:** Arena da Baixada
**Why it fails:** Same error as Row 1592 — Australia vs Netherlands was played at **Estádio Beira-Rio** (Porto Alegre), not Arena da Baixada (Curitiba).
**Source:** https://www.espn.co.uk/football/match/_/gameId/383286/netherlands-australia
**Remedy:** Change answer to "Estádio Beira-Rio."

### Row 1604 — Australia (easy) — FAIL: wrong answer
**Q:** At which World Cup did Australia first reach the round of 16?
**Answer:** 2022 World Cup
**Why it fails:** Australia first reached the round of 16 at the **2006 World Cup** (defeated Japan 3–1 in the group stage, then lost to Italy 0–1 on a Totti 95' pen in the R16). The 2022 R16 was their **second** such appearance, not their first.
**Source:** https://en.wikipedia.org/wiki/Australia_at_the_FIFA_World_Cup
**Remedy:** Change answer to "2006 World Cup."

### Row 1611 — Australia (medium) — FAIL: wrong venue + wrong goal type
**Q:** At which World Cup venue did Australia's Tim Cahill score his first acrobatic bicycle kick?
**Answer:** Estádio Nacional Mané Garrincha
**Why it fails:** Two errors. (1) The famous Cahill 2014 WC goal vs Netherlands was a **volley** (left-foot half-volley), not a bicycle kick. Cahill's bicycle kick was scored in a friendly against China in January 2015, not at a World Cup. (2) The venue was **Estádio Beira-Rio** (Porto Alegre), not Estádio Nacional Mané Garrincha (Brasília).
**Source:** https://www.espn.co.uk/football/match/_/gameId/383286/netherlands-australia ; https://www.caughtoffside.com/2015/01/22/video-tim-cahill-bicycle-kick-v-china-is-better-than-his-volley-against-the-netherlands/
**Remedy:** Drop or rewrite as "At which stadium did Cahill score his famous volley vs Netherlands at the 2014 WC?" Answer: Estádio Beira-Rio.

### Row 1613 — Australia (medium) — FAIL: false claim (group stage ≠ knockout match)
**Q:** Australia beat South Korea 2-1 in the 2015 Asian Cup final. Which other nation did Australia beat in a World Cup knockout match?
**Answer:** Denmark
**Why it fails:** Australia beat Denmark 1–0 in the **group stage** of the 2022 WC, not in a knockout match. Australia has **never won a World Cup knockout match** — they lost to Italy in the 2006 R16 and to Argentina in the 2022 R16.
**Source:** https://en.wikipedia.org/wiki/Australia_at_the_FIFA_World_Cup
**Remedy:** Remove or rewrite entirely; there is no valid answer since Australia has no WC knockout wins.

### Row 1615 — Australia (medium) — FAIL: false premise (goals conceded)
**Q:** Australia conceded the fewest goals in their group at the 2022 World Cup using which system?
**Answer:** Defensive organisation and counter-attacking
**Why it fails:** Australia did **not** concede the fewest goals in Group D — **Tunisia** did (1 goal conceded). Australia conceded 4 goals (all in the 1–4 loss to France). France and Denmark each conceded 2. The premise that Australia conceded the fewest goals is factually false.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_D
**Remedy:** Rewrite premise: "Despite conceding 4 goals to France, what system did Graham Arnold use to secure results vs Tunisia and Denmark?" or just drop this question.

### Row 1618 — Australia (medium) — FAIL: false premise (inter-confederation WC qualifier)
**Q:** Australia hosted Argentina in a 2022 World Cup qualifier at which 83,500-capacity Sydney stadium?
**Answer:** Stadium Australia
**Why it fails:** Australia (AFC) and Argentina (CONMEBOL) are in different confederations and **never meet in regular World Cup qualification matches**. No such qualifier took place. The question appears to confuse a friendly/exhibition match (if one occurred) with a WC qualifier.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(AFC)
**Remedy:** Drop the question; the factual premise is impossible (different confederation qualifying paths).

### Row 1621 — Australia (medium) — FAIL: non-unique answer
**Q:** Australia played Germany in the 2010 World Cup group stage. Which AFC nation qualified for the 2018 World Cup?
**Answer:** Saudi Arabia
**Why it fails:** **Five** AFC nations qualified for the 2018 WC: Australia, Japan, South Korea, Saudi Arabia, and Iran (Iran via direct AFC qualification). Saudi Arabia is one correct answer but Japan, South Korea, Australia, and Iran are equally correct. The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(AFC)
**Remedy:** Specify: "Which AFC nation qualified for the 2018 World Cup for the first time since 2006?" or name a uniquely identifying fact about Saudi Arabia.

### Row 1622 — Australia (medium) — FAIL: non-unique answer
**Q:** Australia qualified directly via AFC for which FIFA World Cup?
**Answer:** The 2014 World Cup
**Why it fails:** Australia qualified **directly** through AFC qualification for **both the 2010 and 2014 WC** (and 2026). The 2010 WC option appears in the option list and is equally correct. The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_(AFC) ; https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_(AFC)
**Remedy:** Narrow to a unique fact, e.g. "In which WC qualifying campaign did Australia first compete as an AFC member?" (Answer: 2010).

### Row 1627 — Australia (easy) — FAIL: non-unique answer
**Q:** Australia qualified for which FIFA World Cup through AFC qualification?
**Answer:** 2010 World Cup
**Why it fails:** Australia also qualified directly through AFC for the **2014 World Cup** (and 2026). The 2014 option appears in the option list, making the answer non-unique between 2010 and 2014.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_(AFC)
**Remedy:** Specify "first" — "Australia first qualified for which WC through AFC qualification?" (Answer: 2010 WC).

### Row 1631 — Australia (easy) — FAIL: non-unique answer
**Q:** Australia reached the 2022 World Cup round of 16. Which team did they beat in the group stage to help secure this?
**Answer:** Denmark
**Why it fails:** Australia beat **both Tunisia 1–0** and **Denmark 1–0** in the group stage. Both wins contributed to securing their R16 place. Tunisia appears in the option list and is an equally valid answer. Non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_D
**Remedy:** Specify: "Which team did Australia beat in their decisive final group game to clinch R16 qualification?" (Answer: Denmark) — making it unique by specifying it was the final/decisive match.

---

## Australia chunk 3 (rows 1651–1750)

### Row 1654 — Australia (easy) — FAIL: false premise (WC debut)
**Q:** Australia's growing football infrastructure supported their debut at which World Cup?
**Answer:** The 2006 World Cup
**Why it fails:** The question calls 2006 Australia's "debut" at the World Cup, but Australia's actual World Cup debut was in **1974** (West Germany). 2006 was their return after a 32-year absence, not a debut.
**Source:** https://en.wikipedia.org/wiki/Australia_at_the_FIFA_World_Cup
**Remedy:** Replace "debut" with "return" or "2006 comeback campaign."

### Row 1665 — Australia (medium) — FAIL: wrong cycle for 14th ranking
**Q:** During which FIFA World Cup cycle did Australia first reach 14th in the FIFA rankings?
**Answer:** 2006 World Cup cycle
**Why it fails:** Australia's 14th ranking was achieved in **September 2009**, which falls in the **2010 World Cup cycle** (not 2006). The 2006 WC qualification window was roughly 2004–2005; the 2010 cycle was 2007–2010. September 2009 clearly belongs to the 2010 cycle.
**Source:** https://socceroos.com.au/news/socceroos-learn-new-fifa-ranking
**Remedy:** Change answer to "2010 World Cup cycle."

### Row 1672 — Australia (medium) — FAIL: non-unique answer
**Q:** For which FIFA World Cup did Australia qualify via AFC, unlike 2018?
**Answer:** 2026 World Cup
**Why it fails:** Australia qualified directly via AFC (not via intercontinental playoff) for the **2010, 2014, and 2026** WCs. Both 2014 and 2010 are listed in the options and are equally valid. The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_(AFC) ; https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_(AFC)
**Remedy:** Specify: "For which WC did Australia qualify directly via AFC for the FIRST time after the 2014 WC, requiring no playoff?" (Answer: 2026 WC).

### Row 1674 — Australia (medium) — FAIL: non-unique answer
**Q:** For which World Cup did Australia qualify directly through AFC matches?
**Answer:** The 2014 World Cup
**Why it fails:** Australia qualified directly through AFC for **both the 2010 and 2014 WCs** (and 2026). The 2010 World Cup option is in the list and is equally correct, making the answer non-unique.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_(AFC)
**Remedy:** Specify "which WC did Australia qualify for via direct AFC for the LAST time before needing a playoff?" (Answer: 2014).

### Row 1675 — Australia (medium) — FAIL: non-unique answer
**Q:** For which World Cup did Australia qualify directly through the AFC?
**Answer:** 2014
**Why it fails:** Same as Row 1674 — Australia also qualified directly via AFC for 2010 (both options in the list). Non-unique.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_(AFC)
**Remedy:** Same as 1674 — add a uniqueness constraint.

### Row 1689 — Australia (easy) — FAIL: non-unique answer
**Q:** In 2022, Australia lost 4-1 to France but beat which nation 1-0?
**Answer:** Denmark
**Why it fails:** Australia beat **both Denmark 1–0 (30 Nov) and Tunisia 1–0 (26 Nov)** in the 2022 WC group stage. Tunisia is listed in the options and is an equally valid answer. Non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_D
**Remedy:** Specify: "In their final group game in 2022, Australia beat which nation 1–0?" (Answer: Denmark).

### Row 1690 — Australia (medium) — FAIL: false premise (Cahill retired at 2014 WC)
**Q:** In Australia's 2014 World Cup group stage match, which player retired as their all-time leading scorer with 50 goals?
**Answer:** Tim Cahill
**Why it fails:** Tim Cahill did **not** retire at or after the 2014 WC. He continued playing until **2018**, scoring his 50th international goal in his farewell match in 2018. The 2014 WC was not his retirement; framing him as retiring there is factually wrong.
**Source:** https://en.wikipedia.org/wiki/Tim_Cahill
**Remedy:** Rewrite: "Which Australian player retired in 2018 as the national team's all-time leading scorer with 50 goals?" Answer: Tim Cahill.

### Row 1691 — Australia (medium) — FAIL: wrong number of goals vs Netherlands
**Q:** In Australia's 2014 World Cup group stage, which player scored two acrobatic goals?
**Answer:** Tim Cahill
**Why it fails:** Tim Cahill scored **one** goal against the Netherlands at the 2014 WC — the famous left-foot volley (21'). Australia scored two goals in the match but the second was scored by **Ryan McGowan** (58'). The claim that Cahill scored two acrobatic goals in a single match is wrong.
**Source:** https://www.givemesport.com/88085354-world-cup-2014-tim-cahill-australia-netherlands/
**Remedy:** Change to "which player scored the iconic acrobatic volley for Australia against the Netherlands?" Answer: Tim Cahill.

### Row 1698 — Australia (medium) — FAIL: wrong result vs Ghana (drew, not lost)
**Q:** In the 2010 World Cup group stage, which two teams did Australia lose to?
**Answer:** Germany and Ghana
**Why it fails:** Australia **drew** with Ghana 1–1 in the 2010 WC group stage — they did not lose. Their only loss in the group was to **Germany (0–4)**; they also beat Serbia 2–1. The question's premise ("lose to Ghana") is factually false.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_Group_D
**Remedy:** Change question to "which two teams did Australia fail to beat in the 2010 group stage?" or fix answer to "Germany only."

### Row 1700 — Australia (medium) — FAIL: unverified claim (zero A-League players)
**Q:** In the 2022 FIFA World Cup, how many Australian players debuted in the A-League?
**Answer:** Zero players
**Why it fails:** The claim that the entire 2022 WC squad was overseas-based cannot be confirmed from authoritative sources. Several Australia squad members had recent A-League ties. UNVERIFIED → FAIL.
**Source:** (no authoritative source for this specific claim)
**Remedy:** Remove or verify with official squad data; the framing "debuted in the A-League" is also ambiguous.

### Row 1702 — Australia (medium) — FAIL: wrong opponent in question
**Q:** In their 2022 qualifier, Australia used which venue for the Socceroos' 3-1 win over New Zealand?
**Answer:** Melbourne Rectangular Stadium
**Why it fails:** The explanation itself says this match was against **Saudi Arabia** at Melbourne Rectangular Stadium (AAMI Park) in November 2021 — not New Zealand. New Zealand is an OFC nation and was not in Australia's AFC 2026 WC qualifying group. The question contains a factually wrong opponent.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(AFC)
**Remedy:** Replace "New Zealand" with "Saudi Arabia" in the question.

### Row 1712 — Australia (medium) — FAIL: wrong World Cup year for 14th ranking
**Q:** In which FIFA World Cup year did Australia reach 14th in the rankings?
**Answer:** 2006
**Why it fails:** Australia's 14th ranking was achieved in **September 2009**, not during the 2006 WC year. The 2006 WC was in June–July 2006. September 2009 falls in the 2010 WC cycle.
**Source:** https://socceroos.com.au/news/socceroos-learn-new-fifa-ranking
**Remedy:** Change answer to "2010" (or the answer "2009" in a year-format question — see Row 1733 for correct phrasing).

### Row 1713 — Australia (easy) — FAIL: non-unique answer
**Q:** In which host nation did Australia NOT compete at the 2022 FIFA World Cup?
**Answer:** South Africa
**Why it fails:** The 2022 World Cup was held entirely in **Qatar**. Australia competed in Qatar and did NOT compete in South Africa, Germany, Brazil, or Argentina — all four options are equally valid answers. The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Drop or rewrite; any answer from the option list is correct since the 2022 WC was in Qatar.

### Row 1717 — Australia (easy) — FAIL: wrong answer (R16 debut was 2006)
**Q:** In which World Cup did Australia first reach the round of 16?
**Answer:** 2022 World Cup
**Why it fails:** Australia first reached the round of 16 at the **2006 World Cup** (lost to Italy 0–1 on a Totti 95' penalty). The 2022 R16 was their second such appearance. Same error as Row 1604.
**Source:** https://en.wikipedia.org/wiki/Australia_at_the_FIFA_World_Cup
**Remedy:** Change answer to "2006 World Cup."

### Row 1719 — Australia (easy) — FAIL: false premise (drew Ghana, didn't lose)
**Q:** In which World Cup did Australia lose to Germany and Ghana in the group stage?
**Answer:** 2010 FIFA World Cup
**Why it fails:** Australia **drew** 1–1 with Ghana at the 2010 WC — they did not lose to Ghana. They only lost to Germany (0–4) in that group. Same factual error as Row 1698.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_Group_D
**Remedy:** Change "lose to Germany and Ghana" to "fail to beat Germany and Ghana" (drew Ghana, lost to Germany).

### Row 1722 — Australia (medium) — FAIL: unverified WC goal
**Q:** In which World Cup did Australia's Ajdin Hrustic score a goal?
**Answer:** 2022 World Cup
**Why it fails:** Ajdin Hrustic is known for scoring in World Cup **qualifying** matches (e.g., the free-kick vs Kuwait), but there is no evidence he scored during the 2022 WC tournament itself. Australia's 2022 WC scorers were Craig Goodwin, Mitchell Duke, Mathew Leckie, and one in the R16. UNVERIFIED → FAIL.
**Source:** https://en.wikipedia.org/wiki/Ajdin_Hrusti%C4%87
**Remedy:** Verify against the official 2022 WC match sheets; if incorrect, drop or replace with a confirmed scorer.

### Row 1723 — Australia (easy) — FAIL: wrong World Cup for acrobatic volley
**Q:** In which World Cup did Australia's Tim Cahill first score his iconic acrobatic volley?
**Answer:** 2006 FIFA World Cup
**Why it fails:** Cahill's famous acrobatic left-foot volley was scored against the Netherlands at the **2014 FIFA World Cup**, not 2006. At the 2006 WC, Cahill scored conventional headers/finishes vs Japan.
**Source:** https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/tim-cahill-goal-australia-netherlands-2014
**Remedy:** Change answer to "2014 FIFA World Cup."

### Row 1726 — Australia (medium) — FAIL: wrong match for iconic acrobatic goal
**Q:** In which World Cup group stage match did Australian Tim Cahill first score an iconic acrobatic goal?
**Answer:** 2006 vs Japan
**Why it fails:** Cahill's iconic acrobatic goal (the left-foot volley) was scored at the **2014 WC vs Netherlands**, not 2006 vs Japan. His 2006 goals vs Japan were conventional headed/close-range finishes.
**Source:** https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/tim-cahill-goal-australia-netherlands-2014
**Remedy:** Change answer to "2014 vs Netherlands."

### Row 1730 — Australia (easy) — FAIL: non-unique answer
**Q:** In which World Cup year did Tim Cahill score for Australia?
**Answer:** 2006
**Why it fails:** Tim Cahill scored for Australia at the **2006, 2010, 2014, and 2018** World Cups — all four appear in the option list. Every option is a correct answer, making this question entirely non-unique.
**Source:** https://en.wikipedia.org/wiki/Tim_Cahill
**Remedy:** Rewrite to specify a unique event, e.g. "In which World Cup year did Tim Cahill score his famous acrobatic volley?" (Answer: 2014).

### Row 1731 — Australia (easy) — FAIL: non-existent WC bicycle kick
**Q:** In which World Cup year did Tim Cahill score his iconic bicycle kick for Australia?
**Answer:** 2006
**Why it fails:** Two errors: (1) Cahill's 2014 WC goal vs Netherlands was a **volley**, not a bicycle kick. (2) Cahill's actual bicycle kick was scored in a **January 2015 friendly against China** — not at any World Cup.
**Source:** https://www.caughtoffside.com/2015/01/22/video-tim-cahill-bicycle-kick-v-china-is-better-than-his-volley-against-the-netherlands/
**Remedy:** Drop this question; the premise that Cahill scored a WC bicycle kick is factually wrong.

### Row 1734 — Australia (medium) — FAIL: wrong opponent (New Zealand vs Saudi Arabia)
**Q:** In which year did Australia host a 2022 World Cup qualifier at Melbourne Rectangular Stadium?
**Answer:** 2021
**Why it fails:** The question asks about a "qualifier against New Zealand" but the explanation confirms the match at Melbourne Rectangular Stadium in November 2021 was against **Saudi Arabia**, not New Zealand. New Zealand is an OFC nation and was not in Australia's AFC qualifying group.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(AFC)
**Remedy:** Replace "New Zealand" with "Saudi Arabia."

### Row 1746 — Australia (medium) — FAIL: stale fact (four is now five)
**Q:** Since Australia moved to the AFC in 2006, how many World Cups have they qualified for?
**Answer:** Four
**Why it fails:** Australia has now qualified for **five** World Cups since joining the AFC: 2010, 2014, 2018, 2022, **and 2026**. The explanation lists only four (up to 2022), but the 2026 qualification is confirmed. Answer "Four" is outdated.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(AFC)
**Remedy:** Update answer to "Five" (or "Six" if counting the 2006 WC, which Australia attended as AFC member despite qualifying via OFC).

### Row 1747 — Australia (medium) — FAIL: wrong confederation + non-unique
**Q:** Since Australia moved to the AFC in 2006, which confederation have they faced in World Cup playoffs?
**Answer:** CONCACAF
**Why it fails:** Two errors: (1) Australia faced **both CONCACAF** (Honduras, 2018 WC playoff) **and CONMEBOL** (Peru, 2022 WC playoff). (2) The explanation erroneously describes Peru as a "CONCACAF team" — Peru is **CONMEBOL** (South American). Both confederations are correct answers, making the answer non-unique; and the explanation contains a factual geographic error.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_%E2%80%93_inter-confederation_play-offs ; https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_%E2%80%93_inter-confederation_play-offs
**Remedy:** Fix answer to "CONCACAF and CONMEBOL" (both); correct explanation to note Peru is CONMEBOL.

### Row 1748 — Australia (medium) — FAIL: unverifiable subjective claim
**Q:** Since Australia's 2006 AFC move, which nation has dominated Asian World Cup qualifying?
**Answer:** Australia
**Why it fails:** The claim that Australia has "dominated" Asian WC qualifying is a subjective assertion without an authoritative source. Japan has also consistently qualified for every WC during this period; South Korea has qualified for all but potentially one. "Domination" is not a definable fact. UNVERIFIED → FAIL.
**Source:** (no authoritative source)
**Remedy:** Replace with a specific verifiable claim, e.g. "Which AFC nation topped their qualifying group in both 2010 and 2014 without needing a playoff?"

### Row 1749 — Australia (easy) — FAIL: stale fact (four is now five)
**Q:** Since joining the AFC, how many FIFA World Cup finals has Australia qualified for?
**Answer:** Four
**Why it fails:** Same as Row 1746 — Australia has now qualified for **five** WC finals since joining the AFC (adding 2026). The answer "Four" was accurate before 2026 qualification was confirmed but is now outdated.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(AFC)
**Remedy:** Update to "Five."

### Row 1750 — Australia (easy) — FAIL: false claim (group stage exit ≠ contenders)
**Q:** Since joining the AFC, when did Australia first become Asian Cup contenders?
**Answer:** 2007 Asian Cup
**Why it fails:** Australia were **eliminated in the group stage** of the 2007 Asian Cup (1W 1D 1L, did not reach the knockout rounds). Calling them "contenders" at their first Asian Cup is false — they became genuine contenders at the **2011 Asian Cup** (reached the final) and won in 2015.
**Source:** https://en.wikipedia.org/wiki/2007_AFC_Asian_Cup
**Remedy:** Change answer to "2011 Asian Cup" (where Australia reached the final for the first time).

### Row 1751 — Australia (medium) — FAIL: stale (four campaigns → now five)
**Q:** Since moving to the AFC in 2006, how many FIFA World Cup qualifying campaigns have Australia dominated?
**Answer:** Four campaigns
**Why it fails:** The explanation cites 2010, 2014, 2018, and 2022 — but Australia also qualified for the **2026 World Cup** via AFC, making it **five campaigns**. Additionally "dominated" overstates 2018 and 2022, both of which required inter-confederation playoffs. Answer is now outdated and count is incorrect.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(AFC)
**Remedy:** Update answer to "Five campaigns" and revise explanation accordingly.

### Row 1760 — Australia (hard) — FAIL: Excel date corruption
**Q:** What was Australia's aggregate score against Honduras in their 2018 World Cup playoff?
**Answer:** 2026-01-03 00:00:00
**Why it fails:** The answer is an **Excel date-corruption artifact** — "3-1" was misread by the spreadsheet as 3 January 2026. The correct answer is **3-1** (Australia won the two-legged playoff 3-1 on aggregate). All four options contain the date-corrupted value or other wrong answers.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Replace answer with "3-1" and remove date-corrupted options.

### Row 1769 — Australia (easy) — FAIL: Excel date corruption
**Q:** What was Australia's scoreline against South Korea in the 2015 Asian Cup final?
**Answer:** 2026-01-02 00:00:00
**Why it fails:** Excel date corruption — "2-1" was misread as 2 January 2026. The correct answer is **2-1** (Australia beat South Korea 2-1 AET in the 2015 Asian Cup final).
**Source:** https://en.wikipedia.org/wiki/2015_AFC_Asian_Cup_Final
**Remedy:** Replace answer with "2-1" and fix corrupted options.

### Row 1772 — Australia (medium) — FAIL: Excel date corruption
**Q:** What was the score when Australia beat South Korea in the 2015 Asian Cup final?
**Answer:** 2026-01-02 00:00:00
**Why it fails:** Same Excel date corruption as Row 1769 — "2-1" corrupted to 2 January 2026. Correct answer: **2-1**.
**Source:** https://en.wikipedia.org/wiki/2015_AFC_Asian_Cup_Final
**Remedy:** Replace answer with "2-1" and remove date-corrupted options.

### Row 1773 — Australia (medium) — FAIL: Excel date corruption
**Q:** What was the score when Australia lost to France in their 2022 World Cup opener?
**Answer:** 2026-01-04 00:00:00
**Why it fails:** Excel date corruption — "4-1" corrupted to 4 January 2026. Correct answer: **4-1** (France 4-1 Australia).
**Source:** https://en.wikipedia.org/wiki/France_v_Australia_(2022_FIFA_World_Cup)
**Remedy:** Replace answer with "4-1" and remove date-corrupted options.

### Row 1775 — Australia (medium) — FAIL: false claim (joined 2006 ≠ contenders immediately)
**Q:** What year did Australia join the AFC and become Asian Cup contenders?
**Answer:** 2006
**Why it fails:** Australia joined the AFC in 2006 (correct) but were **NOT Asian Cup contenders** at that point — they exited in the group stage of the 2007 AFC Asian Cup. Australia became genuine contenders at the **2011 Asian Cup** (reached the final) and proved it in 2015 (won). The premise "become Asian Cup contenders" tied to 2006 is false.
**Source:** https://en.wikipedia.org/wiki/2007_AFC_Asian_Cup
**Remedy:** Either split the question ("When did Australia join the AFC? → 2006") or rewrite to ask when they became genuine contenders (→ 2011).

### Row 1787 — Australia (medium) — FAIL: wrong (first R16 was 2006)
**Q:** When did Australia first reach the FIFA World Cup round of 16?
**Answer:** 2022
**Why it fails:** Australia first reached the World Cup round of 16 in **2006** (lost to Italy 1-0 in the R16 in Kaiserslautern). The explanation also incorrectly states "advanced to the round of 16 for the first time at the 2022 World Cup." 2022 was Australia's **second** R16 appearance.
**Source:** https://en.wikipedia.org/wiki/Australia_at_the_2006_FIFA_World_Cup
**Remedy:** Change answer to "2006" and correct the explanation.

### Row 1788 — Australia (medium) — FAIL: false claim (not regular contenders until 2011)
**Q:** When did Australia join the AFC and become regular Asian Cup contenders?
**Answer:** 2006
**Why it fails:** Australia joined the AFC in 2006 but their first Asian Cup (2007) ended in a group stage elimination. "Regular Asian Cup contenders" is a false premise applied to 2006 — Australia only became regular contenders from **2011** (first final) and confirmed with the 2015 win.
**Source:** https://en.wikipedia.org/wiki/2007_AFC_Asian_Cup
**Remedy:** Separate the two claims, or change the question to ask when their "dominant" era began (answer: 2011 or 2015).

### Row 1818 — Australia (medium) — FAIL: qualifying goal ≠ World Cup tournament goal
**Q:** When did Australian midfielder Ajdin Hrustic score at the FIFA World Cup?
**Answer:** In 2022
**Why it fails:** Hrustic scored his notable goal in the **2022 World Cup qualifying campaign** (AFC playoff vs UAE, 7 June 2022), **not during the World Cup tournament itself** in Qatar. His goal helped Australia reach the inter-confederation playoff, but that is a qualifier, not the tournament. No confirmed goal by Hrustic in the Qatar 2022 tournament matches has been found.
**Source:** https://www.socceroos.com.au/news/watch-hrustic-volley-seals-2-1-victory-over-uae
**Remedy:** Rewrite to ask when Hrustic scored in WC qualifying (→ "2022 qualifying"); or remove entirely.

### Row 1821 — Australia (medium) — FAIL: wrong (iconic acrobatic WC goal was 2014, not after 2006)
**Q:** When did Tim Cahill's acrobatic goals become iconic for Australia at World Cups?
**Answer:** After 2006
**Why it fails:** Cahill's 2006 WC goals vs Japan were **headers**, not acrobatic goals. His iconic acrobatic WC moment was the stunning **left-foot volley vs Netherlands at the 2014 World Cup** (Estádio Beira-Rio). The explanation incorrectly ties the acrobatic-goal reputation to performances "starting at the 2006 FIFA World Cup." The correct answer would be "After 2014."
**Source:** https://en.wikipedia.org/wiki/Tim_Cahill
**Remedy:** Change answer to "After 2014" and update explanation to reference the 2014 volley vs Netherlands.

### Row 1828 — Australia (medium) — FAIL: timeline impossible (14th ranking was September 2009)
**Q:** Which 2015 Asian Cup win helped Australia reach a 14th FIFA ranking?
**Answer:** Australia's continental title
**Why it fails:** Australia reached 14th in the FIFA rankings in **September 2009** — over **five years before** the 2015 Asian Cup. The 2015 win could not have "helped them reach 14th"; that ranking had already been achieved (and passed) in a previous cycle. The explanation is factually wrong about the causal relationship.
**Source:** https://en.wikipedia.org/wiki/Australia_national_football_team
**Remedy:** Remove the causal claim. Either ask which achievement contributed to their 2009 peak ranking, or reframe entirely.

### Row 1842 — Australia (easy) — FAIL: false premise (A-League clubs don't qualify for FIFA WC)
**Q:** Which A-League club from Australia did NOT qualify for the 2022 FIFA World Cup?
**Answer:** Western Sydney Wanderers
**Why it fails:** The question's premise is false — **no A-League club qualifies for the FIFA World Cup**, as it is a national team tournament (the CSV explanation itself concedes this: "No A-League club qualifies for the FIFA World Cup, as it is a national team tournament"). All four options (Melbourne Victory, Sydney FC, WSW, Central Coast Mariners) equally "did not qualify" — the question is unanswerable as asked.
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup
**Remedy:** Delete or completely rewrite; perhaps ask about which Socceroos squad player came from an A-League club.

### Row 1843 — Australia (easy) — FAIL: UNVERIFIED
**Q:** Which A-League club had a player score for Australia in 2022 World Cup qualifying?
**Answer:** Melbourne Victory
**Why it fails:** The explanation claims "Melbourne Victory's Nick D'Agostino scored for Australia in a 2022 World Cup qualifier against Vietnam." This specific claim (D'Agostino, Melbourne Victory, 2022 WC qualifying vs Vietnam) cannot be independently verified. Hrustic's confirmed 2022-qualifying goal was against UAE (not vs Vietnam), and Hrustic was not at Melbourne Victory. UNVERIFIED → FAIL.
**Source:** No confirmable source found for Nick D'Agostino scoring in 2022 WC qualifying vs Vietnam.
**Remedy:** Verify D'Agostino's goal or replace with a verifiable example (e.g., Mathew Leckie who was at Hertha Berlin).

### Row 1844 — Australia (easy) — FAIL: anachronistic distractor (Western Sydney Wanderers ≠ 2010)
**Q:** Which A-League club had players in Australia's 2010 World Cup squad?
**Answer:** Melbourne Victory
**Why it fails:** One of the four options — **Western Sydney Wanderers** — was not founded until October 2012, two years after the 2010 World Cup. A club that didn't exist cannot be a valid distractor for a 2010 squad question. The question is structurally compromised by this anachronistic option, making it trivially easy to eliminate one distractor and undermining the question's validity.
**Source:** https://en.wikipedia.org/wiki/Western_Sydney_Wanderers_FC
**Remedy:** Replace "Western Sydney Wanderers" distractor with a club that existed in 2010 (e.g., Brisbane Roar, Perth Glory, Adelaide United).

### Row 1849 — Australia (easy) — FAIL: wrong (Japan and Australia each won 2 group matches at 2022 WC)
**Q:** Which AFC nation had more 2022 World Cup wins than Australia?
**Answer:** Japan
**Why it fails:** The explanation states "Japan won two group stage matches in 2022, while Australia won one." This is factually wrong — **Australia also won two group stage matches** (Tunisia 1-0 and Denmark 1-0). Japan won two (Germany and Spain). Both nations won exactly two group matches; Japan did NOT have more wins than Australia.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_D
**Remedy:** Correct the explanation and change the question premise, or replace with a factual comparison (e.g., Japan won more knockout matches than Australia historically).

### Row 1850 — Australia (medium) — FAIL: wrong (Australia has 0 WC knockout wins)
**Q:** Which AFC nation had more knockout stage wins than Australia by 2022?
**Answer:** Japan
**Why it fails:** The explanation claims "Australia's only knockout win was in 2006." This is **false** — Australia has **never won a World Cup knockout match**. In 2006 they lost to Italy 1-0 in the R16; in 2022 they lost to Argentina 2-1 in the R16. Australia has zero World Cup knockout wins. Japan, by contrast, has won multiple knockout matches (e.g., 2022: beat Germany and Spain in group, then reached R16; historically beat Yugoslavia in 2002 group stage).
**Source:** https://en.wikipedia.org/wiki/Australia_at_the_FIFA_World_Cup
**Remedy:** Fix explanation to reflect Australia's actual knockout record (0 wins). Revise or remove question.

### Row 1872 — Australia (easy) — FAIL: non-unique (South Korea also reached 2022 WC R16)
**Q:** Which AFC team also reached the 2022 World Cup round of 16 like Australia?
**Answer:** Japan
**Why it fails:** The question implies only ONE other AFC team reached the 2022 WC R16. However, **both Japan AND South Korea** reached the Round of 16 (Japan: beat Germany and Spain in group stage, then lost to Croatia; South Korea: beat Portugal, then lost to Brazil). With Japan and South Korea both valid in the option set, the answer is non-unique. CSV explanation ("Japan was the only other AFC team") is factually wrong.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Rewrite to specify "which AFC team beat a European giant to reach the 2022 WC R16" (Japan beat Germany and Spain), or choose a uniquely answerable angle.

### Row 1876 — Australia (easy) — FAIL: non-unique (South Korea also reached 2022 WC R16)
**Q:** Which AFC team, like Australia in 2022, reached a World Cup round of 16?
**Answer:** Japan
**Why it fails:** Same issue as Row 1872 — South Korea ALSO reached the 2022 WC R16 (beat Portugal in the group stage, then lost to Brazil in the R16). Both Japan and South Korea are valid answers; the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Specify a particular achievement that distinguishes Japan from South Korea in the 2022 WC R16 context.

### Row 1885 — Australia (easy) — FAIL: wrong stage (Japan beat Australia in FINAL, not semi-finals)
**Q:** Which Asian team beat Australia in the 2011 Asian Cup semi-finals?
**Answer:** Japan
**Why it fails:** Japan did **NOT** beat Australia in the semi-finals of the 2011 AFC Asian Cup. Australia beat **Uzbekistan 6-0** in the semi-finals. Japan then beat Australia **1-0 in the FINAL**. The question's premise is factually wrong — Japan beat Australia in the final, not the semi-finals.
**Source:** https://en.wikipedia.org/wiki/2011_AFC_Asian_Cup
**Remedy:** Change question to "Which team beat Australia in the 2011 Asian Cup final?" (Answer: Japan).

### Row 1891 — Australia (medium) — FAIL: wrong (Popovic, not Arnold, led 2026 WC qualification)
**Q:** Which Australia coach led their 2026 FIFA World Cup qualification?
**Answer:** Graham Arnold
**Why it fails:** Graham Arnold was replaced by **Tony Popovic** in September 2024. Popovic managed Australia through the critical later stages of 2026 WC qualifying (including the match vs Saudi Arabia that clinched qualification) and selected the 2026 WC squad. Arnold managed the early stages but Popovic is the manager who completed the qualification.
**Source:** https://en.wikipedia.org/wiki/Tony_Popovic
**Remedy:** Change answer to "Tony Popovic."

### Row 1907 — Australia (easy) — FAIL: stale/wrong (Popovic, not Arnold, is 2026 cycle builder)
**Q:** Which Australia manager builds his 2026 squad core from A-League and European players?
**Answer:** Graham Arnold
**Why it fails:** Arnold was replaced by **Tony Popovic** in September 2024. Popovic is the manager building and selecting the 2026 WC squad. Arnold is no longer managing Australia. CSV explanation ("Graham Arnold is the manager building Australia's squad for the 2026 World Cup cycle") is outdated and factually wrong.
**Source:** https://en.wikipedia.org/wiki/Tony_Popovic
**Remedy:** Change answer to "Tony Popovic" and update explanation.

### Row 1927 — Australia (easy) — FAIL: non-unique (multiple managers served shorter than Postecoglou)
**Q:** Which Australia manager served for a shorter period than Ange Postecoglou's four-year term?
**Answer:** Holger Osieck
**Why it fails:** Among the options (Osieck, Arnold, van Marwijk, Popovic), **three** served shorter than Postecoglou's four years: Osieck (~3 years, 2010–2013), van Marwijk (~7 months, 2017–2018), and Popovic (under 2 years, ongoing from 2024). Only Arnold (6 years) served longer. The answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Australia_national_football_team
**Remedy:** Rewrite to ask "Which manager had the shortest tenure?" (Answer: Bert van Marwijk, ~7 months).

### Row 1936 — Australia (easy) — FAIL: qualifying goal ≠ World Cup tournament goal
**Q:** Which Australia midfielder scored a goal at the 2022 FIFA World Cup in Qatar?
**Answer:** Ajdin Hrustic
**Why it fails:** Hrustic's confirmed goal was in the **2022 WC qualifying** (AFC playoff vs UAE, June 2022), NOT during the 2022 FIFA World Cup tournament in Qatar (November–December 2022). No confirmed goal by Hrustic in Qatar tournament matches has been found.
**Source:** https://www.socceroos.com.au/news/watch-hrustic-volley-seals-2-1-victory-over-uae
**Remedy:** Remove this row or change to ask about Craig Goodwin (scored vs France) or Mathew Leckie (scored vs Denmark).

### Row 1937 — Australia (easy) — FAIL: non-unique (both Leckie and Maclaren were at Melbourne City A-League)
**Q:** Which Australia player at the 2022 FIFA World Cup was based in the A-League?
**Answer:** Mathew Leckie
**Why it fails:** Both **Mathew Leckie** (Melbourne City, A-League) AND **Jamie Maclaren** (Melbourne City, A-League) were in Australia's 2022 WC squad and based in the A-League at Melbourne City. Both are in the option set, making the answer non-unique.
**Source:** https://en.wikipedia.org/wiki/Jamie_Maclaren
**Remedy:** Reframe question to specifically ask about Mathew Leckie (e.g., "Which Melbourne City A-League player scored the 2022 WC winner vs Denmark?").

### Row 1939 — Australia (easy) — FAIL: Boyle was withdrawn before tournament; Mooy was Scotland-based
**Q:** Which Australia player at the 2022 World Cup was based in Scotland?
**Answer:** Martin Boyle
**Why it fails:** Martin Boyle was **withdrawn from the 2022 WC squad before the tournament began** due to a knee injury (20 November 2022, replaced by Marco Tilio). He did not participate in Qatar. The correct answer is **Aaron Mooy** (Celtic FC, Scotland), who was in the squad and played. Additionally, Boyle had moved to Saudi Arabia (Al-Faisaly) in January 2022, not Scotland.
**Source:** https://socceroos.com.au/news/martin-boyle-withdrawn-socceroos-fifa-world-cup-qatar-2022tm-squad
**Remedy:** Change answer to "Aaron Mooy" (Celtic, Scotland).

### Row 1943 — Australia (easy) — FAIL: UNVERIFIED (2026 WC debut is a future event)
**Q:** Which Australia player debuted at the 2026 World Cup?
**Answer:** Nestor Irankunda
**Why it fails:** The 2026 FIFA World Cup had not yet occurred at the time this dataset was created, and Irankunda's debut at that tournament is unverifiable — it is a speculative future claim. UNVERIFIED → FAIL.
**Source:** No authoritative source can confirm a 2026 WC debut before the tournament.
**Remedy:** Remove or wait until post-tournament to verify.

### Row 1944 — Australia (easy) — FAIL: wrong year and wrong event
**Q:** Which Australia player debuted for the Socceroos at AAMI Park in 2016?
**Answer:** Awer Mabil
**Why it fails:** Awer Mabil made his Socceroos debut on **16 October 2018** vs Kuwait — **not in 2016**. The CSV explanation also claims "2016 friendly against Greece at Melbourne's AAMI Park" which contradicts the confirmed 2018 debut date.
**Source:** https://en.wikipedia.org/wiki/Awer_Mabil
**Remedy:** Correct year to 2018; verify the exact match and venue.

### Row 1946 — Australia (easy) — FAIL: UNVERIFIED
**Q:** Which Australia player emerged as a new squad pillar after the 2022 World Cup?
**Answer:** Alessandro Circati
**Why it fails:** The claim that Circati became a "new squad pillar" after the 2022 WC is unverifiable — it is a soft subjective claim with no authoritative source confirming his prominent role. UNVERIFIED → FAIL.
**Source:** No source confirming Circati as a squad pillar post-2022.
**Remedy:** Replace with a verifiable player claim (e.g., a player confirmed to have featured regularly since 2022).

### Row 1954 — Australia (easy) — FAIL: wrong (Okazaki also scored 50 goals — not fewer)
**Q:** Which Australia player scored 50 goals, more than Japan's Shinji Okazaki at the 2018 World Cup?
**Answer:** Tim Cahill
**Why it fails:** Shinji Okazaki scored **50 international goals** in 119 caps for Japan — the **same** as Cahill's 50 goals in 108 caps. Cahill's 50 goals was NOT "more than Okazaki's"; they are equal. The "more than" claim is factually wrong.
**Source:** https://en.wikipedia.org/wiki/Shinji_Okazaki
**Remedy:** Change "more than" to "matching Japan's Shinji Okazaki's tally" or pick a comparison where Cahill genuinely exceeded another player.

### Row 1969 — Australia (easy) — FAIL: wrong/misleading (Cahill did not score at 2018 WC)
**Q:** Which Australia player scored iconic World Cup goals from 2006 to 2018?
**Answer:** Tim Cahill
**Why it fails:** Tim Cahill scored at the 2006, 2010, and 2014 World Cups but **did NOT score at the 2018 World Cup** — he appeared only as a substitute in one match (vs Peru, 0-2 loss) and did not find the net. The "to 2018" framing falsely implies he scored at the 2018 tournament.
**Source:** https://en.wikipedia.org/wiki/Tim_Cahill
**Remedy:** Change to "from 2006 to 2014" (where Cahill actually scored at three consecutive tournaments).

### Row 1973 — Australia (easy) — FAIL: wrong (OWN GOAL, not Goodwin)
**Q:** Which Australia player scored in their 2-1 2022 World Cup loss to Argentina?
**Answer:** Craig Goodwin
**Why it fails:** Australia's only goal in the 2-1 R16 loss to Argentina was an own goal by Enzo Fernández (deflected off Goodwin's shot in the 77th minute). It was not officially credited to Goodwin. The premise "Craig Goodwin scored" is factually wrong.
**Source:** https://www.skysports.com/football/news/11095/12756117
**Remedy:** Change question to ask "Which Argentina player scored an own goal vs Australia in the 2022 WC R16?" (answer: Enzo Fernández) or remove entirely.

### Row 1979 — Australia (easy) — FAIL: non-unique (multiple 2022 WC winners)
**Q:** Which Australia player scored the winner at the 2022 FIFA World Cup?
**Answer:** Mathew Leckie
**Why it fails:** Both Mitchell Duke (vs Tunisia, 23') and Mathew Leckie (vs Denmark, 60') scored match-winning goals at the 2022 WC. Both are in the option set. Non-unique answer.
**Source:** https://www.skysports.com/football/news/11095/12755131
**Remedy:** Specify the match: "scored the winner against Denmark" or "scored the winner against Tunisia" (two separate unambiguous questions).

### Row 1985 — Australia (easy) — FAIL: wrong (no Australian scored in 2022 WC R16)
**Q:** Which Australia player scored their goal in the 2022 World Cup round of 16?
**Answer:** Craig Goodwin
**Why it fails:** Australia's only goal in the R16 (vs Argentina, 77') was an OWN GOAL by Enzo Fernández — no Australian player was credited with a tournament R16 goal. Goodwin scored in the GROUP STAGE (vs France), not the R16. False premise.
**Source:** https://www.skysports.com/football/news/11095/12756117
**Remedy:** Remove this question or replace with "Which Australian scored Australia's only group-stage goal against France?" (answer: Craig Goodwin).

### Row 1987 — Australia (easy) — FAIL: wrong (Australia scored multiple 2014 WC goals)
**Q:** Which Australia player scored their only 2014 World Cup goal?
**Answer:** Tim Cahill
**Why it fails:** Australia scored three goals at the 2014 WC, not one: Cahill vs Chile (group stage), Cahill's famous volley vs Netherlands, and Jedinak's penalty vs Netherlands. The premise "only one goal" is factually wrong.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_B
**Remedy:** Change to "Which Australia player scored twice at the 2014 World Cup?" (answer: Tim Cahill) or "Who scored Australia's famous volley vs Netherlands in 2014?" (answer: Tim Cahill).

### Row 1989 — Australia (easy) — FAIL: wrong (Troisi scored once, not twice)
**Q:** Which Australia player scored twice in the 2015 Asian Cup final?
**Answer:** James Troisi
**Why it fails:** Troisi scored only ONCE in the 2015 AFC Asian Cup final — the winning goal in the 105th minute of extra time. The equalizer (making it 1-1) was scored by Massimo Luongo. Troisi did not score twice.
**Source:** https://en.wikipedia.org/wiki/2015_AFC_Asian_Cup_Final
**Remedy:** Change to "Which Australia player scored the winning goal in the 2015 Asian Cup final?" (answer: James Troisi), or change "scored twice" to "scored the decisive goal."

### Row 1996 — Australia (easy) — FAIL: false premise (no 87th-minute winner by Argentina)
**Q:** Which Australia player was substituted off just before Argentina's 87th-minute winner in 2022?
**Answer:** Aziz Behich
**Why it fails:** Argentina's decisive second goal was scored by Julián Álvarez in the 57th minute, making it 2-0. The only goal scored after the 57th minute was Australia's consolation (own goal by Enzo Fernández, 77'). There was no 87th-minute winner by Argentina. The question's premise is factually wrong.
**Source:** https://www.skysports.com/football/news/11095/12756117
**Remedy:** Remove or rephrase around a factually accurate substitution event from the 2022 WC R16 match.

### Row 2007 — Australia (easy) — FAIL: wrong (Duke started vs Tunisia, did not come on as sub)
**Q:** Which Australia striker was substituted on to score against Tunisia at the 2022 World Cup?
**Answer:** Mitchell Duke
**Why it fails:** Mitchell Duke scored with a glancing header in the 23rd minute as a STARTER — he was in the starting XI, not substituted on. The question's premise "substituted on" is factually wrong.
**Source:** https://www.espn.com/soccer/fifa-world-cup/story/4806892/mitchell-duke-leads-australia-to-world-cup-win-over-tunisia
**Remedy:** Change to "Which Australia striker headed home to give Australia the lead against Tunisia at the 2022 World Cup?" (answer: Mitchell Duke).

### Row 2009 — Australia (easy) — FAIL: wrong (14th ranking achieved 2009, not 2022)
**Q:** Which Australia team's 2022 World Cup run helped them reach 14th?
**Answer:** The Socceroos
**Why it fails:** Australia reached their all-time best FIFA ranking of 14th in September 2009 — three years after the 2006 WC campaign, not after the 2022 WC. Australia's ranking after the 2022 WC was approximately 27th, well below 14th.
**Source:** https://en.wikipedia.org/wiki/Australia_national_soccer_team
**Remedy:** Remove this question or replace with a factually accurate claim linking the 2022 WC R16 run to ranking gains (e.g. "improved to around 27th").

### Row 2010 — Australia (hard) — FAIL: non-unique (both 2010 and 2014 via direct AFC)
**Q:** Which Australia World Cup qualification was via AFC, 2010 or 2018?
**Answer:** 2010
**Why it fails:** Australia qualified DIRECTLY via AFC automatic berths for both 2010 AND 2014. The 2018 and 2022 qualifications required inter-confederation playoffs. With 2014 in the option set, both 2010 and 2014 are valid answers — non-unique.
**Source:** https://en.wikipedia.org/wiki/Australia_national_soccer_team#World_Cup_history
**Remedy:** Rephrase to "Which was the last time Australia qualified for the World Cup directly via AFC without a playoff?" (answer: 2014) or remove the ambiguous option.

### Row 2014 — Australia (easy) — FAIL: non-unique (both Leckie and Maclaren A-League based)
**Q:** Which Australian 2022 World Cup player is based in the A-League?
**Answer:** Mathew Leckie
**Why it fails:** Both Mathew Leckie (Melbourne City) and Jamie Maclaren (Melbourne City) were A-League based at the time of the 2022 WC. Both are in the option set. Non-unique answer.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_squads
**Remedy:** Specify a player not shared with another A-League option, e.g. "Which Australian 2022 WC captain-candidate was based at Melbourne City?" or split into separate questions.

### Row 2019 — Australia (easy) — FAIL: false premise (no Australian 2023 Asian Cup)
**Q:** Which Australian 2023 Asian Cup venue holds approximately 83,500 fans?
**Answer:** Stadium Australia
**Why it fails:** Australia did NOT host the 2023 AFC Asian Cup — that tournament was held in Qatar (January–February 2024). Australia co-hosted the 2023 FIFA Women's World Cup, not an Asian Cup. The question's premise is factually wrong.
**Source:** https://en.wikipedia.org/wiki/2023_AFC_Asian_Cup
**Remedy:** Change to "Which stadium hosted Australia's 2023 Women's World Cup matches with ~83,500 capacity?" (answer: Stadium Australia) or "Which Australian stadium holds approximately 83,500?"

### Row 2021 — Australia (easy) — FAIL: UNVERIFIED (Hrustic not at Melbourne Victory)
**Q:** Which Australian A-League club did 2022 World Cup midfielder Ajdin Hrustic play for?
**Answer:** Melbourne Victory
**Why it fails:** Hrustic's professional career went directly to European clubs (NEC Nijmegen, then Eintracht Frankfurt, Hellas Verona). He has no confirmed stint at Melbourne Victory. The claim is UNVERIFIED and almost certainly wrong — he was never an A-League player.
**Source:** https://en.wikipedia.org/wiki/Ajdin_Hrustic
**Remedy:** Remove this question — Hrustic had no A-League career to reference.

### Row 2026 — Australia (easy) — FAIL: non-unique (multiple clubs existed before 2006)
**Q:** Which Australian club existed before their 2006 AFC move: Melbourne Victory, Sydney FC, or Western Sydney Wanderers?
**Answer:** Melbourne Victory
**Why it fails:** Melbourne Victory (founded 2004), Sydney FC (founded 2004), AND Adelaide United (founded 2003) all existed before Australia's 2006 move to the AFC. All three of those options (plus Adelaide United in the option set) are valid answers — non-unique.
**Source:** https://en.wikipedia.org/wiki/A-League_Men
**Remedy:** The only unique answer would be Western Sydney Wanderers (founded 2012, after the AFC move) — the question should ask "Which club did NOT exist before Australia's 2006 AFC move?" instead.

### Row 2030 — Australia (easy) — FAIL: false premise (no 2015 FIFA World Cup)
**Q:** Which Australian club's 2014 ACL win preceded a 2015 World Cup?
**Answer:** Western Sydney Wanderers
**Why it fails:** There was no 2015 FIFA Men's World Cup. The World Cup is held every four years: 2014 and 2018 were the surrounding editions. The premise "preceded a 2015 World Cup" is factually wrong.
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup
**Remedy:** Change to "Which Australian club's 2014 continental win preceded the 2018 FIFA World Cup?" (answer: Western Sydney Wanderers) — Row 2035 already covers this.

### Row 2062 — Australia (easy) — FAIL: non-unique (Irvine also played both 2018 and 2022 WCs)
**Q:** Which Australian midfielder at the 2022 World Cup also played in the 2018 tournament?
**Answer:** Aaron Mooy
**Why it fails:** Jackson Irvine was also in Australia's 2018 WC squad (he appeared as a substitute) AND played at the 2022 WC. Both Mooy and Irvine satisfy the condition. Non-unique answer.
**Source:** https://en.wikipedia.org/wiki/Jackson_Irvine
**Remedy:** Narrow the question to a unique fact, e.g. "Which Australian midfielder started every group match at both the 2018 and 2022 World Cups?" (answer: Aaron Mooy).

### Row 2063 — Australia (easy) — FAIL: non-unique (multiple midfielders played at 2022 WC)
**Q:** Which Australian midfielder played at the 2022 World Cup?
**Answer:** Jackson Irvine
**Why it fails:** Jackson Irvine, Aaron Mooy, AND Ajdin Hrustic all played at the 2022 WC — three of the four options are valid answers. Non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_squads
**Remedy:** Distinguish by a unique attribute, e.g. "Which Australian midfielder started all three 2022 WC group matches?" (answer: Aaron Mooy) or "Which Australian midfielder scored in 2022 WC qualifying?" (answer: Hrustic).

### Row 2064 — Australia (easy) — FAIL: wrong (Goodwin scored at Al Janoub, not Hrustic)
**Q:** Which Australian midfielder scored at the Al Janoub Stadium in 2022?
**Answer:** Ajdin Hrustic
**Why it fails:** Craig Goodwin scored Australia's goal at Al Janoub Stadium (vs France, 9') at the 2022 World Cup. Hrustic scored in the 2022 WC qualifying playoff vs UAE at a different venue — and in any case, a qualifying goal ≠ a WC tournament goal.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_D
**Remedy:** Change answer to Craig Goodwin ("Which Australian winger scored at Al Janoub in 2022?") or remove.

### Row 2065 — Australia (easy) — FAIL: wrong (Hrustic did not score at 2022 WC tournament)
**Q:** Which Australian midfielder scored one goal at the 2022 World Cup?
**Answer:** Ajdin Hrustic
**Why it fails:** Hrustic did not score at the 2022 FIFA World Cup tournament. His well-known goal was in the 2022 WC qualifying inter-confederation playoff vs UAE (a qualifying match, not a tournament match). No Australian midfielder scored at the 2022 WC tournament (Australia's goals were Goodwin, Duke, Leckie — all in different positions/context).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Remove this question entirely or replace with a factually accurate scorer (e.g. "Which Australian player scored in the group stage opener vs France?" → Craig Goodwin).

### Row 2068 — Australia (easy) — FAIL: false premise (Hrustic did not score at 2022 WC)
**Q:** Which Australian midfielder was key in 2022, unlike the scorer Hrustic?
**Answer:** Aaron Mooy
**Why it fails:** The question's framing "unlike the scorer Hrustic" implies Hrustic scored at the 2022 WC tournament, which is false. Hrustic scored in the WC qualifying playoff vs UAE, not at the 2022 WC. The false premise contaminates the question.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Remove this question. If contrasting Mooy and Hrustic is desired, base it on a factually accurate distinction (e.g. "started every group match" vs "came off the bench").

### Row 2076 — Australia (easy) — FAIL: non-unique (all players made WC debut at 2006)
**Q:** Which Australian player debuted at the 2006 FIFA World Cup?
**Answer:** Tim Cahill
**Why it fails:** Australia last qualified for the World Cup in 1974. All players who appeared for Australia at the 2006 WC (including Cahill, Kewell, Viduka, Schwarzer — all four options) were making their FIRST World Cup appearance in 2006. Non-unique answer.
**Source:** https://en.wikipedia.org/wiki/Australia_at_the_FIFA_World_Cup
**Remedy:** Reframe to "Which Australian player scored twice in his first World Cup match in 2006?" (Answer: Cahill) or remove.

### Row 2078 — Australia (medium) — FAIL: non-unique (all options debuted before 2006)
**Q:** Which Australian player debuted before their first of six straight World Cup qualifications?
**Answer:** Tim Cahill
**Why it fails:** Australia's "first of six straight WC qualifications" was 2006. All four options debuted internationally before 2006: Cahill (2004), Kewell (1996), Viduka (1994), Aloisi (1997). The condition is satisfied by all options — non-unique.
**Source:** https://en.wikipedia.org/wiki/Australia_national_soccer_team
**Remedy:** Add a distinguishing qualifier — e.g. "Which player debuted before 2006 AND scored at four consecutive World Cups?" (answer: Cahill, uniquely) or remove.

### Row 2080 — Australia (easy) — FAIL: wrong answer (Cahill DID score at 2014 WC)
**Q:** Which Australian player did NOT score at the 2014 FIFA World Cup?
**Answer:** Tim Cahill
**Why it fails:** Tim Cahill scored TWICE at the 2014 WC: a header vs Chile (group stage) and his famous left-foot volley vs Netherlands (group stage). He also scored from the penalty spot via Jedink... actually Cahill scored the non-penalty goals. The answer "Tim Cahill did NOT score" is factually wrong.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_B
**Remedy:** Change the answer to "Mathew Leckie" (who played but did not score at the 2014 WC), and update the question accordingly. Remove Tim Cahill from the options.

### Row 2092 — Australia (easy) — FAIL: wrong WC years (acrobatic WC goal was 2014, not 2006/2010)
**Q:** Which Australian player scored acrobatic goals at both the 2006 and 2010 World Cups?
**Answer:** Tim Cahill
**Why it fails:** Cahill's celebrated ACROBATIC WC goal was his left-foot volley vs Netherlands at the 2014 WC — not 2006 or 2010. His 2006 goals vs Japan were diving headers, and his 2010 goal vs Serbia was a header. Neither is typically characterized as "acrobatic." The question correctly identifies Cahill but applies the wrong WC years.
**Source:** https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/tim-cahill-goal-australia-netherlands-2014
**Remedy:** Change to "Which Australian player scored an acrobatic volley goal at the 2014 FIFA World Cup?" (Answer: Tim Cahill).

### Row 2099 — Australia (easy) — FAIL: non-unique (three options all scored fewer than 50 goals)
**Q:** Which Australian player scored fewer than 50 goals for the national team?
**Answer:** Harry Kewell
**Why it fails:** Among the options: Kewell (14 goals), Viduka (11 goals), and Aloisi (27 goals) ALL scored fewer than 50 goals. Only Tim Cahill scored exactly 50. Three of the four options are valid answers — non-unique.
**Source:** https://en.wikipedia.org/wiki/Harry_Kewell
**Remedy:** Invert: "Which Australian player scored exactly 50 goals?" (Answer: Tim Cahill) — already covered by many other rows. Alternatively, remove.

### Row 2102 — Australia (easy) — FAIL: wrong WC years (iconic acrobatic goals were 2006 headers and 2014 volley)
**Q:** Which Australian player scored iconic acrobatic goals at the 2006 and 2010 World Cups?
**Answer:** Tim Cahill
**Why it fails:** Same error as Row 2092. The iconic ACROBATIC Cahill WC goal was at the 2014 WC (volley vs Netherlands). His 2006 goals were headers (not typically "acrobatic volleys") and his 2010 goal was a header. The CSV explanation itself confirms: "Tim Cahill's acrobatic volley against the Netherlands at the 2014 World Cup."
**Source:** https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/tim-cahill-goal-australia-netherlands-2014
**Remedy:** Change to "2006 and 2014" to correctly identify the WC editions where Cahill scored memorable goals, or specify the volley as a 2014 goal.

### Row 2106 — Australia (easy) — FAIL: wrong year (Cahill's iconic volley was 2014, not 2006)
**Q:** Which Australian player scored iconic goals like a 2006 World Cup volley?
**Answer:** Tim Cahill
**Why it fails:** Cahill did NOT score a "volley" at the 2006 WC. His 2006 goals vs Japan were diving headers in the 84th and 89th minutes. His iconic volley was scored at the 2014 WC vs Netherlands. Calling his 2006 goals a "volley" is factually wrong.
**Source:** https://en.wikipedia.org/wiki/2006_FIFA_World_Cup_Group_F
**Remedy:** Change "2006 World Cup volley" to "2014 World Cup volley" — the iconic Cahill volley was at the 2014 WC.

### Row 2120 — Australia (medium) — FAIL: misleading (Hrustic's was 4th of 5 penalties in shootout, not THE decisive one)
**Q:** Which Australian player scored the penalty that secured their 2022 World Cup qualification?
**Answer:** Ajdin Hrustic
**Why it fails:** Australia qualified for the 2022 WC by beating Peru 5-4 on penalties after a 0-0 draw. Hrustic scored the FOURTH of Australia's five successful shootout penalties, making it 4-2. Australia's FIFTH penalty secured the win. The framing "the penalty that secured qualification" implies a decisive/final penalty, which was not Hrustic's. Multiple players scored penalties in the shootout.
**Source:** https://abcnews.go.com/Sports/wireStory/australia-qualifies-world-cup-edging-peru-85369146
**Remedy:** Change to "Which Australian player scored a direct free kick vs UAE to help secure 2022 WC qualification?" (Answer: Hrustic — his June 7, 2022 free kick vs UAE in the 2-1 win was the specific memorable Hrustic qualifying moment).

### Row 2131 — Australia (easy) — FAIL: non-unique (three midfielders played at 2022 WC)
**Q:** Which Australian player was a key midfielder at the 2022 World Cup in Qatar?
**Answer:** Jackson Irvine
**Why it fails:** Jackson Irvine, Aaron Mooy, AND Ajdin Hrustic all played as midfielders at the 2022 WC. All three are in the option set. Non-unique answer.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_squads
**Remedy:** Distinguish by a specific attribute — e.g. "Which Australian midfielder started every group match at the 2022 World Cup?" (Answer: Aaron Mooy, uniquely).

### Row 2133 — Australia (easy) — FAIL: non-unique (all four options were in the 2018 WC squad)
**Q:** Which Australian player was in the 2018 FIFA World Cup squad?
**Answer:** Mathew Leckie
**Why it fails:** All four options (Leckie, Cahill, Jedinak, Mooy) were in Australia's 2018 WC squad. Non-unique answer.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_squads
**Remedy:** The distractors should be players who were NOT in the 2018 WC squad. Replace Cahill/Jedinak/Mooy with players like Craig Goodwin, Jackson Irvine, or Harry Souttar (who were not in the 2018 squad).

### Row 2144 — Australia (easy) — FAIL: wrong WC years (iconic acrobatic goals were 2006 headers and 2014 volley)
**Q:** Which Australian player's acrobatic goals became iconic at the 2006 and 2010 World Cups?
**Answer:** Tim Cahill
**Why it fails:** Cahill's iconic acrobatic WC moments were: 2006 diving headers vs Japan, and the 2014 LEFT-FOOT VOLLEY vs Netherlands. The 2010 WC goal (header vs Serbia) is not typically cited as "acrobatic." The CSV explanation itself says "acrobatic volleys and bicycle kicks at the 2006 and 2014 World Cups" — confirming the correct years are 2006 and 2014, not 2006 and 2010.
**Source:** https://en.wikipedia.org/wiki/Tim_Cahill
**Remedy:** Change "2006 and 2010" to "2006 and 2014" (the correct WC years for Cahill's iconic/acrobatic goals).

### Row 2147 — Australia (easy) — FAIL: wrong (Cahill's famous bicycle kick was in a friendly, not at a World Cup)
**Q:** Which Australian player's bicycle kicks defined his World Cup legacy?
**Answer:** Tim Cahill
**Why it fails:** Cahill's famous BICYCLE KICK was scored in a friendly vs China on January 22, 2015 — NOT at a World Cup. His actual WC goals were: 2006 (diving headers vs Japan), 2010 (header vs Serbia), 2014 (left-foot volley vs Netherlands). None were bicycle kicks. The question conflates his friendly bicycle kick with his WC legacy.
**Source:** https://en.wikipedia.org/wiki/Tim_Cahill
**Remedy:** Change to "Which Australian player's acrobatic volley became his most iconic World Cup moment?" (Answer: Tim Cahill, 2014 vs Netherlands).

### Row 2177 — Australia (easy) — FAIL: wrong venue (2022 WC playoff was in Qatar)
**Q:** Which Australian stadium hosted the 2022 FIFA World Cup playoff due to its 83,500 capacity?
**Answer:** Stadium Australia
**Why it fails:** The Australia vs Peru 2022 WC intercontinental playoff (June 13, 2022) was played at Ahmad Bin Ali Stadium in Al Rayyan, Qatar — a neutral ground. Stadium Australia did not host this match. The 83,500 capacity claim is irrelevant since the game was not in Australia at all.
**Source:** https://www.aljazeera.com/gallery/2022/6/14/photos-australia-won-playoff-againt-peru-in-doha
**Remedy:** Change to reference a 2022 WC AFC qualifying group match (which WAS played in Australia at Stadium Australia) rather than the intercontinental playoff.

### Row 2178 — Australia (easy) — FAIL: wrong venue (2022 WC playoff was in Qatar, not AAMI Park)
**Q:** Which Australian stadium hosted the 2022 World Cup playoff against Peru?
**Answer:** AAMI Park
**Why it fails:** The Australia vs Peru 2022 WC inter-confederation playoff was held in Qatar (Ahmad Bin Ali Stadium), not in Australia. Neither AAMI Park nor any Australian stadium hosted this match.
**Source:** https://www.aljazeera.com/gallery/2022/6/14/photos-australia-won-playoff-againt-peru-in-doha
**Remedy:** Change to a genuine Australia home match — e.g. "Which Australian stadium hosted Australia's 2022 WC AFC qualifying match against Saudi Arabia?" (Answer: AAMI Park).

### Row 2187 — Australia (easy) — FAIL: wrong venue (2022 WC playoff was in Qatar)
**Q:** Which Australian stadium, capacity ~83,500, hosted the 2022 World Cup playoff vs Peru?
**Answer:** Stadium Australia
**Why it fails:** The 2022 WC inter-confederation playoff vs Peru was played at Ahmad Bin Ali Stadium, Qatar — not at Stadium Australia. No Australian stadium hosted this match.
**Source:** https://www.aljazeera.com/gallery/2022/6/14/photos-australia-won-playoff-againt-peru-in-doha
**Remedy:** Correct to "hosted the 2022 WC AFC qualifying playoff home leg" (which was a different match played in Australia).

### Row 2191 — Australia (easy) — FAIL: wrong venue (2022 WC playoff was in Qatar)
**Q:** Which Australian stadium, with an 83,500 capacity, hosted the 2022 FIFA World Cup qualifier playoff?
**Answer:** Stadium Australia
**Why it fails:** The 2022 WC inter-confederation playoff (vs Peru) was held in Qatar (Ahmad Bin Ali Stadium). Stadium Australia did not host the intercontinental playoff.
**Source:** https://www.aljazeera.com/gallery/2022/6/14/photos-australia-won-playoff-againt-peru-in-doha
**Remedy:** Reframe the question as "hosted a 2022 WC AFC group qualifying match" rather than the playoff.

### Row 2193 — Australia (easy) — FAIL: wrong venue (2022 WC playoff was in Qatar)
**Q:** Which Australian stadium's 83,500 capacity hosted the 2022 World Cup playoff?
**Answer:** Stadium Australia
**Why it fails:** The 2022 WC inter-confederation playoff vs Peru was hosted in Qatar (Ahmad Bin Ali Stadium, Al Rayyan). Not hosted at Stadium Australia.
**Source:** https://www.aljazeera.com/gallery/2022/6/14/photos-australia-won-playoff-againt-peru-in-doha
**Remedy:** Change to reference a genuine Australian-hosted qualifier. "Which Australian stadium's 83,500 capacity hosted a 2022 WC AFC qualifying match?" (Answer: Stadium Australia, correct).

### Row 2195 — Australia (easy) — FAIL: wrong venue (2022 WC playoff was in Qatar)
**Q:** Which Australian stadium's 83,500 capacity made it the 2022 FIFA World Cup playoff venue?
**Answer:** Stadium Australia
**Why it fails:** The 2022 WC inter-confederation playoff was played in Qatar, not Australia. Stadium Australia's capacity was not a factor in the neutral-venue playoff selection.
**Source:** https://www.aljazeera.com/gallery/2022/6/14/photos-australia-won-playoff-againt-peru-in-doha
**Remedy:** Remove "playoff venue" claim; rephrase to "Which Australian stadium's 83,500 capacity makes it the primary AFC qualifying venue?" (Answer: Stadium Australia, correct).

### Row 2256 — Australia (easy) — FAIL: non-unique (all four options debuted at WC after Australia's 2006 debut)
**Q:** Which nation debuted at a FIFA World Cup after Australia's 2006 debut?
**Answer:** Iceland
**Why it fails:** All four options debuted at the WC after 2006: Slovakia (2010), Bosnia (2014), Iceland (2018), Panama (2018). Any of the four is a valid answer, making the question non-unique.
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup
**Remedy:** Keep Iceland but replace the other three options with nations that debuted BEFORE 2006 (e.g. Czech Republic 1994, Paraguay 1930, Cameroon 1982) to make Iceland the only post-2006 debutant.

### Row 2267 — Australia (medium) — FAIL: non-unique (multiple teams Australia didn't lose to in 2010 group stage)
**Q:** Which nation did Australia NOT lose to in the 2010 World Cup group stage?
**Answer:** Serbia
**Why it fails:** Australia's 2010 WC Group D opponents were Germany, Serbia, Ghana. (1) Australia BEAT Serbia 2-1 ✓, (2) Australia DREW 1-1 with Ghana (did not lose) ✓, (3) Netherlands was NOT even in Australia's group, so Australia trivially "did not lose to" Netherlands either. Serbia, Ghana, and Netherlands are all valid answers → non-unique.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_Group_D
**Remedy:** Change the distractors to teams Australia actually lost to or drew with — e.g. replace Ghana with Ivory Coast and Netherlands with Brazil (neither in Australia's 2010 group). "Serbia" remains the clean unique answer as the team they beat.

### Row 2270 — Australia (easy) — FAIL: false premise (Australia only beat Denmark once at WC — 2022)
**Q:** Which nation has Australia beaten at two different FIFA World Cups?
**Answer:** Denmark
**Why it fails:** Australia vs Denmark WC record: 2018 WC — 1-1 DRAW (not a win); 2022 WC — 1-0 WIN. Australia has beaten Denmark at exactly ONE World Cup (2022), not two. The premise "beaten at two WCs" is false for Denmark and for all the other options (Japan beaten once in 2006, South Korea and Saudi Arabia never met Australia at WC tournament).
**Source:** https://en.wikipedia.org/wiki/Australia_v_Denmark_(2022_FIFA_World_Cup)
**Remedy:** Remove the "two WCs" premise. A valid replacement: "Which nation did Australia beat to qualify for the 2022 WC knockout stage?" (Answer: Denmark — 1-0 win in group stage).

### Row 2273 — Australia (easy) — FAIL: non-unique (all four options also qualified for 6 consecutive WCs 2006-2026)
**Q:** Which nation matched Australia's six consecutive World Cups from 2006 to 2026?
**Answer:** Brazil
**Why it fails:** All four options (Brazil, Japan, South Korea, Mexico) qualified for the 2006, 2010, 2014, 2018, 2022, and 2026 World Cups. Mexico and USA/Canada are 2026 hosts (automatic). Japan and South Korea are consistent AFC qualifiers. Brazil has qualified for every WC. All four match or exceed Australia's six-consecutive streak — the question has no unique answer.
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup
**Remedy:** Replace three options with nations that have NOT had six consecutive WC appearances since 2006 (e.g. Ecuador, Ivory Coast, Nigeria) so only Brazil remains as a valid match.

### Row 2279 — Australia (easy) — FAIL: self-referential (answer is Australia, the subject of the question)
**Q:** Which nation, like Australia in 2022, last reached a World Cup round of 16 16 years prior?
**Answer:** Australia
**Why it fails:** The question is self-referential — it describes Australia's own situation ("like Australia in 2022") and the answer is Australia itself. A question that defines a property unique to Australia and then asks "which nation has this property" is logically circular and provides no test of knowledge.
**Source:** https://en.wikipedia.org/wiki/Australia_national_football_team
**Remedy:** Compare with a different nation — e.g. "Which Asian nation also reached the 2022 WC round of 16?" (Answer: South Korea or Japan) — to make it a genuine factual question.

### Row 2303 — Australia (easy) — FAIL: wrong venue (2022 WC playoff was in Qatar)
**Q:** Which stadium hosted Australia's 2022 World Cup playoff due to its primary venue status?
**Answer:** Stadium Australia
**Why it fails:** The 2022 WC inter-confederation playoff vs Peru was played at Ahmad Bin Ali Stadium in Qatar, not at Stadium Australia. The neutral venue in Qatar was chosen by FIFA, not based on Stadium Australia's "primary venue" status.
**Source:** https://www.aljazeera.com/gallery/2022/6/14/photos-australia-won-playoff-againt-peru-in-doha
**Remedy:** Change to ask about a qualifier actually hosted in Australia: "Which stadium hosted Australia's 2022 WC AFC qualifying match vs Vietnam?" (both Stadium Australia and AAMI Park could work depending on verification).

### Row 2304 — Australia (easy) — FAIL: wrong venue (R16 vs Argentina was at Ahmad bin Ali Stadium, not Al Janoub)
**Q:** Which stadium hosted Australia's 2022 World Cup round of 16 match?
**Answer:** Al Janoub Stadium
**Why it fails:** Australia's 2022 WC group stage matches (vs France, Tunisia, Denmark) were all at Al Janoub Stadium. However, the R16 match vs Argentina was played at Ahmad Bin Ali Stadium (Al Rayyan Stadium), not Al Janoub. Row 2302 in the same pool correctly states Ahmad Bin Ali Stadium for the same match.
**Source:** https://en.wikipedia.org/wiki/Argentina_v_Australia_(2022_FIFA_World_Cup)
**Remedy:** Change the answer to Ahmad Bin Ali Stadium (the actual R16 venue).

### Row 2335 — Australia (medium) — FAIL: non-unique (2010 and 2014 both qualify as direct AFC entry)
**Q:** Which World Cup did Australia qualify for via AFC direct entry?
**Answer:** 2026 World Cup
**Why it fails:** Among the options (2026, 2010, 2014, 2022): Australia qualified for 2010 via direct AFC (Group B 2nd place, automatic), for 2014 via direct AFC, and for 2026 via direct AFC. Only 2022 required an intercontinental playoff (vs UAE + Peru). The question therefore has three valid answers (2010, 2014, 2026) → non-unique.
**Source:** https://en.wikipedia.org/wiki/Australia_national_football_team
**Remedy:** Change the question to specify the MOST RECENT or FIRST direct AFC qualification, or restrict options so only one represents direct AFC entry.

### Row 2340 — Australia (medium) — FAIL: non-unique (2006, 2010, and 2014 all valid — Australia competed in all three)
**Q:** Which year did Australia compete in the FIFA World Cup?
**Answer:** 2006
**Why it fails:** The options are 2006, 2002, 2010, 2014. Australia competed in the 2006, 2010, and 2014 WCs (all three are valid answers). Only 2002 is wrong (Australia didn't qualify for 2002). The question has three correct answers → non-unique.
**Source:** https://en.wikipedia.org/wiki/Australia_national_football_team
**Remedy:** Change the question to "Which year did Australia FIRST compete in the FIFA World Cup after re-joining in the modern era?" (Answer: 2006) and replace 2010 and 2014 with years Australia did NOT qualify (1998, 2002).

### Row 2354 — Australia (easy) — FAIL: wrong answer (Álvarez scored the decisive/winning goal vs Australia, not Messi)
**Q:** Who scored Argentina's winner against Australia in the 2022 World Cup round of 16?
**Answer:** Lionel Messi
**Why it fails:** In Argentina's 2-1 win over Australia (Dec 3, 2022): Messi scored the OPENER in the 35th minute, Julián Álvarez scored the SECOND goal in the 57th minute (which proved decisive as the winner), and Australia pulled one back via Goodwin in the 77th minute. In football terminology, the "winner" is the decisive goal — Álvarez's 57th-minute goal. Messi scored first but not the winning goal.
**Source:** https://en.wikipedia.org/wiki/Argentina_v_Australia_(2022_FIFA_World_Cup)
**Remedy:** Change answer to Julián Álvarez (and update question to "first goal" or "opening goal" if Messi is the intended answer).

### Row 2359 — Australia (easy) — FAIL: wrong answer (Rabiot scored France's first goal vs Australia, not Giroud)
**Q:** Who scored the first goal for France against Australia in the 2022 World Cup?
**Answer:** Olivier Giroud
**Why it fails:** In France 4-1 Australia (Nov 22, 2022): Australia led 1-0 via Goodwin (9'), then ADRIEN RABIOT scored France's first equaliser in the 27th minute. Giroud scored France's second goal (32') and fourth goal (71') — but NOT the first. Rabiot is the correct answer.
**Source:** https://en.wikipedia.org/wiki/France_v_Australia_(2022_FIFA_World_Cup)
**Remedy:** Change answer to Adrien Rabiot. Or change question to "Who scored the most goals for France against Australia in the 2022 WC?" (Answer: Giroud, with 2 goals).

### Row 2360 — Australia (easy) — FAIL: stale (Graham Arnold was replaced by Tony Popovic in September 2024)
**Q:** Who selects the A-League and European core of Australia's 2026 World Cup squad?
**Answer:** Graham Arnold
**Why it fails:** Graham Arnold left the Socceroos manager role after the 2022 WC cycle. Tony Popovic was appointed as Australia manager in September 2024 and is responsible for squad selection for the 2026 WC cycle. Arnold has no role in the 2026 squad.
**Source:** https://en.wikipedia.org/wiki/Tony_Popovic
**Remedy:** Change answer to Tony Popovic (the current 2026 WC cycle manager).

---

## Austria — Chunk 1 (rows 2402–2499)

### Row 2404 — Austria (medium) — FAIL: false premise + wrong answer
**Q:** After Austria's 2022 World Cup group stage win, which manager led them to 10th in FIFA rankings?
**Answer:** Franz Koller
**Why it fails:** Austria did NOT qualify for or participate in the 2022 FIFA World Cup — the question's premise is entirely false. Additionally, the answer "Franz Koller" is a non-existent person; the manager who led Austria to their peak FIFA ranking of 10th was **Marcel Koller** (served 2011–2017).
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Rewrite removing any 2022 WC reference. E.g. "Which manager led Austria to their all-time peak FIFA ranking of 10th?" Answer: Marcel Koller.

### Row 2407 — Austria (hard) — FAIL: wrong count and wrong starting year
**Q:** After which World Cup did Austria's four-tournament qualification failure streak begin?
**Answer:** 2006
**Why it fails:** Two errors. (1) Austria's qualification failure streak is SIX consecutive World Cups (2002, 2006, 2010, 2014, 2018, 2022), not four. (2) The streak began AFTER the **1998** World Cup (Austria's last appearance), not after 2006 — Austria did not compete at 2006 at all.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Change to "After which World Cup did Austria's six-tournament qualification failure streak begin?" Answer: 1998.

### Row 2418 — Austria (medium) — FAIL: wrong facts (Switzerland had 5 points at 2018 WC)
**Q:** At the 2018 World Cup, Austria's Euro 2008 co-host had how many points?
**Answer:** Zero points
**Why it fails:** Austria's Euro 2008 co-host is Switzerland. At the 2018 FIFA World Cup, Switzerland finished with **5 points** in Group E — they drew Brazil 1-1, beat Serbia 2-1, and drew Costa Rica 2-2 (advancing to the Round of 16). "Zero points" is factually wrong.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_E
**Remedy:** Change answer to "Five points" (or "six points" if counting differently — confirmed 5 points by standard scoring: 1+3+1). Correct answer is Five points.

### Row 2419 — Austria (easy) — FAIL: false premise (Austria not at 2022 WC)
**Q:** At the 2022 FIFA World Cup, Austria's squad featured several Bundesliga-based players. Which other UEFA nation's 2022 squad also had many Bundesliga players?
**Answer:** Switzerland
**Why it fails:** Austria did NOT qualify for or participate in the 2022 FIFA World Cup. There was no "Austria's 2022 World Cup squad." The entire question premise is false.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Remove 2022 WC reference. Use qualifying-squad context only: "During Austria's 2022 World Cup qualifying campaign, which other UEFA nation's squad also featured many Bundesliga players?"

### Row 2422 — Austria (easy) — FAIL: false premise (Austria not at 2022 WC)
**Q:** At the 2022 World Cup, which Austrian attacker was a key offensive player?
**Answer:** Christoph Baumgartner
**Why it fails:** Austria did not qualify for the 2022 FIFA World Cup. There was no Austria squad, no Austrian attacker, and no Austrian WC performance at Qatar 2022.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Reframe to a tournament Austria actually attended: "At Euro 2024, which Austrian attacker was a key offensive player?" — Baumgartner was prominent there.

### Row 2423 — Austria (easy) — FAIL: false premise (Austria not at 2022 WC)
**Q:** At the 2022 World Cup, which Austrian club had the most players in its squad?
**Answer:** Red Bull Salzburg
**Why it fails:** Austria did not qualify for or participate in the 2022 FIFA World Cup. There was no Austrian WC squad.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Change to: "During Austria's 2022 World Cup qualifying campaign, which Austrian club provided the most players to the national squad?" — Red Bull Salzburg remains correct.

### Row 2424 — Austria (easy) — FAIL: false premise + wrong club
**Q:** At the 2022 World Cup, which Austrian midfielder played for Borussia Dortmund?
**Answer:** Marcel Sabitzer
**Why it fails:** Two errors. (1) Austria did NOT qualify for the 2022 FIFA World Cup, so no Austrian midfielder played at Qatar 2022. (2) Marcel Sabitzer was at **Bayern Munich** in 2022 (joined Bayern in September 2021 on loan, then signed permanently), NOT Borussia Dortmund.
**Source:** https://en.wikipedia.org/wiki/Marcel_Sabitzer
**Remedy:** Remove 2022 WC reference entirely. If testing Sabitzer's club, use correct club: "Which Austrian midfielder moved from RB Leipzig to Bayern Munich in 2021?" Answer: Marcel Sabitzer.

### Row 2425 — Austria (easy) — FAIL: false premise (Austria not at 2022 WC)
**Q:** At the 2022 World Cup, which coach transformed Austria into a pressing team at Euro 2024?
**Answer:** Ralf Rangnick
**Why it fails:** Austria was not at the 2022 World Cup. The question's 2022 WC premise is false. (Rangnick did transform Austria, but his work was showcased at Euro 2024, not the 2022 WC.)
**Source:** https://en.wikipedia.org/wiki/Ralf_Rangnick
**Remedy:** Remove the "2022 World Cup" framing: "Which coach transformed Austria into a high-pressing team that impressed at Euro 2024?" Answer: Ralf Rangnick.

### Row 2426 — Austria (easy) — FAIL: false premise (Austria not at 2022 WC)
**Q:** At the 2022 World Cup, which manager later transformed Austria into a pressing team at Euro 2024?
**Answer:** Ralf Rangnick
**Why it fails:** Austria was not at the 2022 FIFA World Cup, so no Austrian manager worked there. Rangnick did manage Austria from January 2022 and led them at Euro 2024, but there was no 2022 WC connection.
**Source:** https://en.wikipedia.org/wiki/Ralf_Rangnick
**Remedy:** Remove the 2022 WC anchor: "Which manager took over Austria in 2022 and later transformed them into a pressing team at Euro 2024?" Answer: Ralf Rangnick.

### Row 2430 — Austria (easy) — FAIL: Excel date corruption
**Q:** At the 2026 World Cup qualifiers, which score did Austria beat the Netherlands by at Euro 2024?
**Answer:** 2026-02-03 00:00:00
**Why it fails:** The answer "2026-02-03 00:00:00" is an Excel date-serial corruption of the scoreline **3-2** (February 3, 2026 in date format ≈ serial for 3-2). No user-facing question should display an ISO timestamp as the answer to a score question.
**Source:** https://en.wikipedia.org/wiki/Austria_v_Netherlands_(UEFA_Euro_2024)
**Remedy:** Replace answer with "3-2". All options need similar correction.

### Row 2441 — Austria (easy) — FAIL: non-unique answer
**Q:** Austria beat the Netherlands 3-2 at Euro 2024. Which nation also beat the Dutch in a major tournament?
**Answer:** Czech Republic
**Options:** Czech Republic | Italy | Portugal | Belgium
**Why it fails:** Multiple options are correct, making the answer non-unique. **Italy** beat the Netherlands in the Euro 2000 semi-final (0-0 AET, 3-1 pens). **Portugal** beat the Netherlands 1-0 in the 2006 FIFA World Cup Round of 16 ("Battle of Nuremberg"). Both Italy and Portugal appear as distractors but are valid correct answers. Belgium has also beaten the Netherlands in various Nations League matches.
**Source:** https://en.wikipedia.org/wiki/Italy_v_Netherlands_(UEFA_Euro_2000) ; https://en.wikipedia.org/wiki/Netherlands_v_Portugal_(2006_FIFA_World_Cup)
**Remedy:** Tighten the question to a specific competition or timeframe, or replace distractors with nations that have NOT beaten the Netherlands at a major tournament.

### Row 2442 — Austria (medium) — FAIL: Excel date corruption
**Q:** Austria beat the Netherlands in a Euro 2024 group stage match. What was the final score?
**Answer:** 2026-02-03 00:00:00
**Why it fails:** "2026-02-03 00:00:00" is an Excel date corruption of the scoreline **3-2**.
**Source:** https://en.wikipedia.org/wiki/Austria_v_Netherlands_(UEFA_Euro_2024)
**Remedy:** Replace answer and options with correct scorelines; correct answer is "3-2".

### Row 2443 — Austria (medium) — FAIL: Excel date corruption
**Q:** Austria beat the Netherlands in the Euro 2024 group stage by what score?
**Answer:** 2026-02-03 00:00:00
**Why it fails:** "2026-02-03 00:00:00" is an Excel date corruption of the scoreline **3-2**.
**Source:** https://en.wikipedia.org/wiki/Austria_v_Netherlands_(UEFA_Euro_2024)
**Remedy:** Replace answer with "3-2".

### Row 2444 — Austria (medium) — FAIL: Excel date corruption
**Q:** Austria beat the Netherlands in the Euro 2024 group stage by what scoreline?
**Answer:** 2026-02-03 00:00:00
**Why it fails:** "2026-02-03 00:00:00" is an Excel date corruption of the scoreline **3-2**.
**Source:** https://en.wikipedia.org/wiki/Austria_v_Netherlands_(UEFA_Euro_2024)
**Remedy:** Replace answer with "3-2".

### Row 2450 — Austria (medium) — FAIL: wrong count
**Q:** Austria failed to qualify for how many consecutive World Cups before 2026?
**Answer:** Four
**Why it fails:** Austria missed **SIX** consecutive World Cups before qualifying for 2026: 2002, 2006, 2010, 2014, 2018, and 2022. The answer "Four" understates the streak by two.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Change answer to "Six". Also update distractors — "Five tournaments" should become a distractor and the options should reflect the corrected count.

### Row 2451 — Austria (medium) — FAIL: false premise + wrong answer
**Q:** Austria failed to reach four consecutive World Cups after which one?
**Answer:** 2006
**Why it fails:** Two errors. (1) Austria's last World Cup before 2026 was **1998** (France), not 2006 — Austria did not participate in the 2006 WC at all. The answer "2006" implies Austria was at the 2006 WC, which is false. (2) The streak is **six** consecutive misses (2002–2022), not four.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Change to "Austria failed to reach six consecutive World Cups after which one?" Answer: 1998.

### Row 2459 — Austria (easy) — FAIL: Excel date corruption
**Q:** Austria lost to Türkiye by what scoreline in the Euro 2024 round of 16?
**Answer:** 2026-01-02 00:00:00
**Why it fails:** "2026-01-02 00:00:00" is an Excel date corruption of the scoreline **2-1** (i.e. Austria lost 2-1 to Türkiye).
**Source:** https://en.wikipedia.org/wiki/Austria_v_T%C3%BCrkiye_(UEFA_Euro_2024)
**Remedy:** Replace answer with "2-1". Update all options accordingly.

### Row 2462 — Austria (easy) — FAIL: wrong answer (Serbia topped the group, not Germany)
**Q:** Austria missed the 2010 World Cup. Which nation topped their qualifying group?
**Answer:** Germany
**Why it fails:** Austria was in **UEFA 2010 WC Qualifying Group 7** (France, Romania, Serbia, Lithuania, Austria, Faroe Islands). **Serbia** topped the group and qualified directly; France was second and went to the playoffs. Germany was in a completely different qualifying group.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_7
**Remedy:** Change answer to "Serbia". Update distractors — "Germany" should become a distractor and "Serbia" the correct answer.

### Row 2466 — Austria (easy) — FAIL: non-unique answer
**Q:** Austria qualified for Euro 2016 under Marcel Koller. Which manager did NOT guide them to a World Cup?
**Answer:** Marcel Koller
**Options:** Marcel Koller | Ralf Rangnick | Franco Foda | Dietmar Constantini
**Why it fails:** Only Ralf Rangnick guided Austria to a World Cup (2026). Marcel Koller, Franco Foda, AND Dietmar Constantini all failed to qualify Austria for a World Cup. Three of the four options are valid correct answers, making the answer non-unique.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Reframe to identify the ONE manager who DID guide them: "Which manager finally guided Austria to a World Cup qualification?" Answer: Ralf Rangnick. Alternatively, specify a time period to make the answer unique.

### Row 2467 — Austria (medium) — FAIL: wrong count
**Q:** Austria qualified for the 2026 World Cup after missing how many consecutive tournaments?
**Answer:** Seven tournaments
**Why it fails:** Austria missed **six** consecutive World Cups (2002, 2006, 2010, 2014, 2018, 2022) before qualifying for 2026. "Seven tournaments" overstates the streak.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Change answer to "Six tournaments".

### Row 2471 — Austria (medium) — FAIL: false premise (Austria not at 2018 WC)
**Q:** Austria's 2018 World Cup group stage match vs Brazil preceded which manager's Euro 2016 qualification?
**Answer:** Marcel Koller
**Why it fails:** Austria did NOT qualify for or participate in the 2018 FIFA World Cup. There was no "Austria's 2018 World Cup group stage match vs Brazil." The premise is entirely false. (Koller was Austria's manager for Euro 2016 qualifying but had no 2018 WC involvement.)
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Remove the 2018 WC premise. E.g. "Which manager qualified Austria for Euro 2016 for the first time since 2008?" Answer: Marcel Koller.

### Row 2475 — Austria (easy) — FAIL: false premise (Austria not at 2022 WC)
**Q:** Austria's 2022 World Cup squad included players from which Bundesliga club?
**Answer:** Red Bull Salzburg
**Why it fails:** Austria did NOT qualify for the 2022 FIFA World Cup; there was no "Austria's 2022 World Cup squad." Red Bull Salzburg is actually the Austrian Bundesliga, not the German Bundesliga — so the question also conflates leagues.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Change to Austria's qualifying squad context: "During Austria's 2022 World Cup qualifying campaign, which Austrian club provided the most players?" Answer: Red Bull Salzburg.

### Row 2476 — Austria (hard) — FAIL: false premise (Austria not at 2022 WC)
**Q:** Austria's 2024 Euro loss to Türkiye came after which World Cup group stage match?
**Answer:** Austria vs France 2022
**Why it fails:** Austria did NOT participate in the 2022 FIFA World Cup. There was no "Austria vs France 2022" World Cup group stage match. The entire premise is false.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Remove 2022 WC reference. E.g. "Austria's Euro 2024 loss to Türkiye in the Round of 16 followed a group-stage win over which nation?" Answer: the Netherlands.

### Row 2480 — Austria (hard) — FAIL: wrong count
**Q:** Austria's 2026 World Cup qualification under Rangnick ended a streak of how many consecutive failed campaigns?
**Answer:** Four
**Why it fails:** Austria missed **six** consecutive World Cup qualifying campaigns (for 2002, 2006, 2010, 2014, 2018, and 2022), not four. Rangnick's 2026 qualification ended a six-campaign streak.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Change answer to "Six".

### Row 2483 — Austria (medium) — FAIL: wrong answer (Austria never beat Costa Rica at a WC)
**Q:** Austria's 3-2 win over the Netherlands at Euro 2024 was a group stage match. Which other nation did Austria beat in a World Cup group stage?
**Answer:** Costa Rica
**Why it fails:** Austria has never played Costa Rica at a FIFA World Cup. Austria's last WC was 1998 (Group B: Italy, Chile, Cameroon). Austria beat Chile 2-1 and drew with Cameroon in that tournament. Costa Rica were never Austria's World Cup group opponents.
**Source:** https://en.wikipedia.org/wiki/Austria_at_the_1998_FIFA_World_Cup
**Remedy:** Change answer to Chile (beat 2-1 at 1998 WC group stage) or Cameroon (drew 1-1 at 1998 WC). E.g. "Which other nation did Austria beat in a World Cup group stage?" Answer: Chile.

### Row 2484 — Austria (hard) — FAIL: wrong year (peak ranking was 2016, not 2017)
**Q:** Austria's best FIFA ranking of 10th under Koller was achieved in which 2018 qualifying year?
**Answer:** 2017
**Why it fails:** Austria's all-time peak FIFA ranking of 10th was reached in **2016**, not 2017. The web confirms "In 2016 the national team reached its highest position ever (10th) in the FIFA World Rankings" under Marcel Koller.
**Source:** https://en.wikipedia.org/wiki/Marcel_Koller
**Remedy:** Change answer to "2016".

### Row 2485 — Austria (easy) — FAIL: Excel date corruption
**Q:** Austria's biggest Euro 2024 shock was beating the Netherlands by what score?
**Answer:** 2026-02-03 00:00:00
**Why it fails:** "2026-02-03 00:00:00" is an Excel date corruption of the scoreline **3-2**.
**Source:** https://en.wikipedia.org/wiki/Austria_v_Netherlands_(UEFA_Euro_2024)
**Remedy:** Replace answer with "3-2".

### Row 2487 — Austria (easy) — FAIL: Excel date corruption
**Q:** Austria's Euro 2020 round of 16 loss to Italy finished with what score?
**Answer:** 2026-01-02 00:00:00
**Why it fails:** "2026-01-02 00:00:00" is an Excel date corruption of the scoreline **2-1** (Italy won 2-1 AET).
**Source:** https://en.wikipedia.org/wiki/Italy_v_Austria_(UEFA_Euro_2020)
**Remedy:** Replace answer with "2-1". Update all options accordingly.

### Row 2488 — Austria (medium) — FAIL: self-referential / circular
**Q:** Austria's Euro 2024 group stage win over Netherlands was a shock. Which other team pulled a major upset?
**Answer:** Austria beat Netherlands
**Why it fails:** The answer ("Austria beat Netherlands") is identical to the scenario described in the question itself. This is self-referential — the question asks "which other team pulled an upset" but the answer is just restating the question's own premise. No factual knowledge is tested.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024
**Remedy:** Replace with a genuine comparison upset from Euro 2024. E.g. Georgia beat Portugal 2-0 in the group stage, or Slovakia beat Belgium 1-0.

### Row 2490 — Austria (easy) — FAIL: false premise (Austria not at 2018 WC in Russia)
**Q:** Austria's Euro 2024 win over the Netherlands was more successful than their 2018 World Cup performance where?
**Answer:** Russia
**Why it fails:** Austria did NOT qualify for the 2018 FIFA World Cup, which was held in Russia. There was no "Austria's 2018 World Cup performance." The question's premise is entirely false.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Remove the 2018 WC comparison. E.g. "Austria's Euro 2024 win over the Netherlands was more impressive than their 2020 Euro exit to which nation?" Answer: Italy.

### Row 2492 — Austria (medium) — FAIL: false premise (Austria not at 2018 WC)
**Q:** Austria's Karim Onisiwo debuted at which FIFA World Cup after his Salzburg development?
**Answer:** 2018 World Cup
**Why it fails:** Austria did NOT qualify for the 2018 FIFA World Cup, so no Austrian player debuted at the 2018 WC. Karim Onisiwo could not have made his WC debut for Austria at a tournament Austria did not attend.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Remove WC reference. Reframe to tournaments Austria did attend: "Karim Onisiwo debuted for Austria at which UEFA European Championship?" — verify which Euro he first played at.

### Row 2496 — Austria (hard) — FAIL: wrong timing (transformation began BEFORE the 2022 WC, not after)
**Q:** Austria's praised transformation under Ralf Rangnick began after which World Cup?
**Answer:** 2022 FIFA World Cup
**Why it fails:** Ralf Rangnick was officially appointed Austria national team manager on **January 1, 2022** — approximately 11 months BEFORE the 2022 FIFA World Cup (November–December 2022). The transformation began in early 2022, not after the 2022 WC. The correct answer would be "after the 2022 WC qualifying campaign failed" or simply that Rangnick started in 2022 before the WC.
**Source:** https://en.wikipedia.org/wiki/Ralf_Rangnick
**Remedy:** Reframe: "Austria's praised transformation under Ralf Rangnick bore fruit at which tournament?" Answer: UEFA Euro 2024. Or: "Ralf Rangnick succeeded which manager to begin Austria's transformation?" Answer: Franco Foda.

---

## Austria — Chunk 2 (rows 2500–2632)

### Row 2499 — Austria (medium) — CORRECTION: moved from PASS to FAIL
**Q:** Before the 2022 qualifiers, which Austrian striker had already become his nation's all-time top scorer?
**Answer:** Marko Arnautović
**Why it fails:** False premise — Arnautović did NOT become Austria's all-time top scorer before the 2022 qualifiers. He broke Thomas Polster's record of 44 goals in October 2025 (during 2026 WC qualifying, scoring 4 goals in a 10-0 win over San Marino). During the 2022 qualifying campaign he had around 30 goals, well short of the record.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change answer to "Thomas Polster" (who actually held the record before and during the 2022 qualifiers) or rewrite question to ask who was the all-time top scorer before Arnautović.

### Row 2517 — Austria (hard) — FAIL: false premise / unverifiable claim
**Q:** Which RB Salzburg product scored for Germany in the 2018 World Cup group stage, showcasing Red Bull's influence?
**Answer:** Timo Werner
**Why it fails:** Austria was not at the 2018 World Cup (false premise context). More critically, Timo Werner was NOT an RB Salzburg product — he came from Stuttgart/Leipzig (RB Leipzig). No player from RB Salzburg's youth academy scored for Germany in the 2018 WC group stage. Germany's 2018 WC group stage scorers were Müller, Goretzka, Kroos, Reus, Draxler.
**Source:** https://en.wikipedia.org/wiki/Germany_at_the_2018_FIFA_World_Cup
**Remedy:** Delete — premise is false. Timo Werner was an RB Leipzig player, not RB Salzburg product.

### Row 2542 — Austria (medium) — FAIL: false premise
**Q:** Which Austria attacker debuted at the 2022 World Cup?
**Answer:** Christoph Baumgartner
**Why it fails:** Austria was NOT at the 2022 World Cup (false premise). Baumgartner debuted for Austria in September 2020, more than two years before the 2022 WC.
**Source:** https://en.wikipedia.org/wiki/Christoph_Baumgartner
**Remedy:** Delete or rewrite — Austria was not at the 2022 WC.

### Row 2543 — Austria (medium) — FAIL: wrong duration
**Q:** Austria's 2026 World Cup qualification ended how many years of absence?
**Answer:** 16 years
**Why it fails:** Austria's last WC was France 1998. Their return at 2026 ends a 28-year absence (1998–2026), not 16 years.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Change answer to "28 years".

### Row 2553 — Austria (hard) — FAIL: unverifiable specific statistic
**Q:** What was the average age of Austria's squad during their 2022 World Cup qualifiers?
**Answer:** 26.8 years
**Why it fails:** The specific average squad age figure of 26.8 years cannot be verified from available sources. This is a highly specific statistical claim with no reliable verifiable source.
**Source:** N/A — unverifiable
**Remedy:** Remove the specific figure or replace with a verifiable general claim about Austria's relatively young squad during the 2022 qualifiers.

### Row 2555 — Austria (medium) — FAIL: Excel date corruption
**Q:** What was the score in Austria's 2022 World Cup qualifying win against the Faroe Islands?
**Answer:** 2026-02-03 00:00:00
**Why it fails:** Excel date corruption. "2026-02-03 00:00:00" represents the score "3-2" stored as a date timestamp.
**Source:** N/A — data corruption
**Remedy:** Fix data pipeline to prevent Excel auto-converting scorelines to dates. Correct answer should be "3-2".

### Row 2558 — Austria (easy) — FAIL: Excel date corruption
**Q:** What was the score in Austria's first Euro 2020 qualifying win?
**Answer:** 2026-01-02 00:00:00
**Why it fails:** Excel date corruption. "2026-01-02 00:00:00" represents the score "2-1" stored as a date timestamp.
**Source:** N/A — data corruption
**Remedy:** Fix data pipeline. Correct answer should be "2-1".

### Row 2564 — Austria (medium) — FAIL: Excel date corruption
**Q:** On what date did Austria beat Denmark in their 2022 World Cup qualifier?
**Answer:** 2021-03-01 00:00:00
**Why it fails:** Excel date corruption — the date "2021-03-01 00:00:00" has been corrupted into a timestamp format during CSV processing. Even if the date were accurate, the question cannot be properly served with a corrupted answer.
**Source:** N/A — data corruption
**Remedy:** Fix data pipeline. Verify actual match date of Austria vs Denmark in 2022 WC qualifiers (Group F).

### Row 2565 — Austria (hard) — FAIL: wrong factual claim
**Q:** In their 2022 World Cup qualifying group, who did Austria host in Vienna to face the tournament favorites?
**Answer:** France
**Why it fails:** France was NOT in Austria's 2022 WC qualifying group. Austria were in Group F: Denmark, Scotland, Israel, Austria, Faroe Islands, Moldova. France were in Group D.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_F
**Remedy:** Change the question/answer to reference a team actually in Group F, such as Denmark (who were the group favorites).

### Row 2578 — Austria (medium) — FAIL: Excel date corruption
**Q:** When did Austria play their most important 2018 World Cup qualifier?
**Answer:** 2017-09-05 00:00:00
**Why it fails:** Excel date corruption — "2017-09-05 00:00:00" is a date shown as a raw timestamp. Answer cannot be evaluated in this format.
**Source:** N/A — data corruption
**Remedy:** Fix data pipeline. Note also that if this refers to a specific match date, it needs to be formatted as a readable date.

### Row 2583 — Austria (medium) — FAIL: wrong factual claim
**Q:** When did the Austrian national team first reach the Euro group stage?
**Answer:** Euro 2016
**Why it fails:** Austria co-hosted Euro 2008 with Switzerland (automatic qualifier) and played in the group stage — that was their first Euro group stage appearance, not Euro 2016. Euro 2016 was their first *earned* qualification for a Euro group stage, but the question asks "first reach the Euro group stage" without that distinction.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2008
**Remedy:** Rewrite as "When did Austria first qualify for a European Championship group stage (as non-host)?" Answer: Euro 2016. Or change answer to Euro 2008.

### Row 2587 — Austria (hard) — FAIL: unverifiable specific claim
**Q:** In 2017, which Austrian player became his country's all-time leading scorer in World Cup qualifiers?
**Answer:** Marko Arnautović
**Why it fails:** This is an unverifiable specific claim about being the all-time leading WC qualifier scorer specifically in 2017. Arnautović's overall all-time record (breaking Polster's 44-goal total record) wasn't achieved until October 2025. Whether he specifically topped the WC qualifier goals tally in 2017 cannot be independently verified.
**Source:** N/A — unverifiable
**Remedy:** Remove or replace with a verifiable claim about Arnautović's scoring achievements.

### Row 2588 — Austria (medium) — FAIL: wrong year
**Q:** When did Marko Arnautović become Austria's all-time leading scorer?
**Answer:** 2022
**Why it fails:** Arnautović broke Thomas Polster's all-time Austria scoring record (44 goals) in October 2025 when he scored 4 goals in a 10-0 victory over San Marino during 2026 WC qualifying — NOT in 2022.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change answer to "2025" (or more precisely "October 2025").

### Row 2604 — Austria (hard) — FAIL: non-unique answer
**Q:** Which country will co-host the 2026 FIFA World Cup with Canada and Mexico?
**Answer:** USA
**Why it fails:** The question has a non-unique answer structure issue — looking at the original pool options, the answer should be USA. However, this question is ambiguous since the 2026 WC is hosted by USA, Canada, AND Mexico (all three are hosts). The question implies only one more co-host beyond Canada and Mexico, but Canada and Mexico are both co-hosts alongside USA. The phrasing creates potential for non-unique answers if options include any combination of the three hosts.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup
**Remedy:** Rewrite to avoid ambiguity — e.g., "Which three nations are co-hosting the 2026 FIFA World Cup?" or restructure so only one co-host relationship is tested.

### Row 2606 — Austria (medium) — FAIL: false premise
**Q:** Which Austria midfielder debuted for the national team just before the 2022 World Cup?
**Answer:** Christoph Baumgartner
**Why it fails:** False premise — Baumgartner debuted for Austria in September 2020, more than two years before the November 2022 World Cup. Also, Austria were not at the 2022 WC.
**Source:** https://en.wikipedia.org/wiki/Christoph_Baumgartner
**Remedy:** Delete — both the "just before" timing claim and the WC context are false.

### Row 2607 — Austria (medium) — FAIL: false premise
**Q:** Which Austria midfielder made his debut just before the 2022 World Cup qualifying campaign?
**Answer:** Christoph Baumgartner
**Why it fails:** Baumgartner debuted for Austria in September 2020. The 2022 WC qualifying campaign began in March 2021, so his debut was about 6 months before qualifying started — not "just before." This is a borderline claim but "just before" is inaccurate given the time gap.
**Source:** https://en.wikipedia.org/wiki/Christoph_Baumgartner
**Remedy:** Rewrite — Baumgartner debuted in September 2020, about 6 months before the qualifying campaign opened.

### Row 2609 — Austria (easy) — FAIL: false premise
**Q:** Which Austria striker scored at the 2022 FIFA World Cup?
**Answer:** Marko Arnautović
**Why it fails:** Austria was NOT at the 2022 FIFA World Cup (false premise). Austria failed to qualify — they lost their play-off to Wales in March 2022.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Delete entirely — Austria was not at the 2022 WC.

### Row 2614 — Austria (easy) — FAIL: false premise
**Q:** Which Austria attacker was in the 2022 World Cup squad?
**Answer:** Marko Arnautović
**Why it fails:** Austria was NOT at the 2022 World Cup (false premise). Austria did not qualify; they lost to Wales in the play-off.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Delete entirely — Austria was not at the 2022 WC.

### Row 2622 — Austria (hard) — FAIL: false premise
**Q:** How did Austria defender David Alaba's club success shape their 2022 World Cup tactics?
**Answer:** His Real Madrid experience improved Austria's defensive structure
**Why it fails:** Austria was NOT at the 2022 World Cup (false premise). Austria failed to qualify for the 2022 WC.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Delete — Austria was not at the 2022 WC.

### Row 2624 — Austria (hard) — FAIL: false claim about record status
**Q:** Which Austria striker, their all-time leading scorer, was selected for the Euro 2024 squad?
**Answer:** Marko Arnautović
**Why it fails:** While Arnautović was selected for Euro 2024 (held June–July 2024), he did NOT break Thomas Polster's all-time Austria scoring record until October 2025. At Euro 2024, Arnautović was NOT yet Austria's all-time leading scorer — Polster still held the record at the time.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change the description to "Austria's then-leading active scorer" or rewrite the question to be temporally accurate.

### Row 2632 — Austria (medium) — FAIL: wrong duration
**Q:** Austria's 2026 World Cup qualification ended how long a drought?
**Answer:** 16-year World Cup drought
**Why it fails:** Austria's last WC was France 1998. Their 2026 qualification ends a 28-year absence (1998–2026), not 16 years.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Change answer to "28-year World Cup drought".

## Austria — Chunk 3 (rows 2633–3241)

### Row 2660 — Austria (easy) — FAIL: false premise
**Q:** Which Austria manager's praised transformation led to a 2022 World Cup qualifying campaign?
**Answer:** Ralf Rangnick
**Why it fails:** Rangnick was appointed January 2022, AFTER the 2022 WC qualifying campaign ended (November 2021). He had no role in any "2022 WC qualifying campaign."
**Source:** https://en.wikipedia.org/wiki/Ralf_Rangnick
**Remedy:** Change to "Which Austria manager's praised transformation led to a 2026 World Cup qualifying campaign?"

### Row 2664 — Austria (easy) — FAIL: wrong fact
**Q:** Which Austria midfielder debuted in the 2014 World Cup qualifiers?
**Answer:** Marcel Sabitzer
**Why it fails:** Sabitzer's first cap was March 29, 2014 (a friendly). Austria's 2014 WC qualifying ran 2012–2013, before his debut.
**Source:** https://en.wikipedia.org/wiki/Marcel_Sabitzer
**Remedy:** Change to "Which Austria midfielder made his senior debut in 2014?"

### Row 2675 — Austria (easy) — FAIL: wrong fact
**Q:** Which Austria midfielder was key in 2022 WC qualifiers, but not in 2018?
**Answer:** Marcel Sabitzer
**Why it fails:** Sabitzer was also a key player in the 2018 WC qualifying campaign (he debuted in 2014 and was a regular by 2016). He was prominent in both qualifying campaigns.
**Source:** https://en.wikipedia.org/wiki/Marcel_Sabitzer
**Remedy:** Remove this row or rephrase to reflect Sabitzer's consistent presence across multiple campaigns.

### Row 2677 — Austria (easy) — FAIL: wrong timing
**Q:** Which Austria player became their all-time leading scorer before Euro 2024?
**Answer:** Marko Arnautović
**Why it fails:** Arnautović broke Anton Polster's all-time record in October 2025 (4 goals vs San Marino), which is AFTER Euro 2024 (June/July 2024).
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change to "Which Austria player became their all-time leading scorer in 2025?"

### Row 2683 — Austria (easy) — FAIL: false premise
**Q:** Which Austria player has the most FIFA World Cup goals?
**Answer:** Marko Arnautović
**Why it fails:** Austria last appeared at a WC in 1998, before Arnautović's international career. He has zero WC goals. Hans Krankl (4 goals in 1978) holds the real record.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Remove or rewrite entirely around WC qualifying goals instead.

### Row 2692 — Austria (easy) — FAIL: false premise
**Q:** Which Austria player scored a Euro 2024 winner, unlike his World Cup goal?
**Answer:** Marcel Sabitzer
**Why it fails:** Austria has not competed at a World Cup since 1998. Sabitzer has no World Cup goal to contrast with.
**Source:** https://en.wikipedia.org/wiki/Marcel_Sabitzer
**Remedy:** Remove the "unlike his World Cup goal" clause entirely.

### Row 2712 — Austria (easy) — FAIL: wrong timing
**Q:** Which Austria player was their all-time leading scorer at Euro 2024?
**Answer:** Marko Arnautović
**Why it fails:** At Euro 2024 (June/July 2024), Polster's 44-goal record still stood. Arnautović broke it in October 2025.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change to "…at the 2026 World Cup" or "…in 2025."

### Row 2713 — Austria (easy) — FAIL: wrong timing
**Q:** Which Austria player was their all-time leading scorer for the 2022 World Cup qualifiers?
**Answer:** Marko Arnautović
**Why it fails:** During the 2022 WC qualifying (2020–21), Polster still held the record. Arnautović broke it in October 2025.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change to "…during the 2026 World Cup qualifiers."

### Row 2715 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian player, a Champions League winner with Bayern and Real Madrid, played at the 2022 World Cup stadium in Qatar?
**Answer:** David Alaba
**Why it fails:** Austria did not qualify for the 2022 World Cup; no Austrian player played at a 2022 WC stadium for Austria.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove or rewrite as "…won the Champions League with both Bayern Munich and Real Madrid."

### Row 2728 — Austria (easy) — FAIL: wrong timing
**Q:** Which Austrian striker led their 2022 World Cup qualifying campaign as all-time top scorer?
**Answer:** Marko Arnautović
**Why it fails:** Arnautović was NOT Austria's all-time top scorer during the 2022 WC qualifying (2020–21). Polster's 44-goal record stood until October 2025.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change to "…2026 World Cup qualifying campaign as all-time top scorer."

### Row 2731 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian 2022 World Cup squad member previously played for Red Bull Salzburg?
**Answer:** Karim Onisiwo
**Why it fails:** Austria did not qualify for the 2022 World Cup. There is no "Austrian 2022 World Cup squad."
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change to "2026 World Cup squad" or "2022 World Cup qualifying squad."

### Row 2734 — Austria (easy) — FAIL: wrong fact
**Q:** Which Austrian attacker debuted in the 2022 FIFA World Cup qualifiers?
**Answer:** Christoph Baumgartner
**Why it fails:** Baumgartner's international debut was November 2019, before the 2022 WC qualifying started.
**Source:** https://en.wikipedia.org/wiki/Christoph_Baumgartner
**Remedy:** Change to "…debuted in the 2022 Nations League?" or adjust the date.

### Row 2738 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian attacker made his World Cup debut in 2022?
**Answer:** Christoph Baumgartner
**Why it fails:** Austria did not qualify for the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove or rewrite around the 2026 WC.

### Row 2740 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian attacker scored at the 2022 FIFA World Cup?
**Answer:** Christoph Baumgartner
**Why it fails:** Austria did not qualify for the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove or rewrite around the 2026 WC.

### Row 2743 — Austria (medium) — FAIL: false premise
**Q:** Which Austrian attacker started versus France in the 2022 World Cup group stage?
**Answer:** Christoph Baumgartner
**Why it fails:** Austria was not in the 2022 World Cup group stage.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove entirely.

### Row 2750 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian attacker was a key starter like Portugal's Ronaldo at the 2022 World Cup?
**Answer:** Christoph Baumgartner
**Why it fails:** Austria was not at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove entirely.

### Row 2753 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian attacker was in the 2022 World Cup squad?
**Answer:** Christoph Baumgartner
**Why it fails:** Austria did not qualify for the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change to "2026 World Cup squad."

### Row 2760 — Austria (easy) — FAIL: wrong timing
**Q:** Which Austrian became their all-time top scorer during the 2022 World Cup qualifiers?
**Answer:** Marko Arnautović
**Why it fails:** Arnautović did not break Polster's record during the 2022 WC qualifying (2020–21); the record fell in October 2025.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change to "…2026 World Cup qualifiers."

### Row 2762 — Austria (easy) — FAIL: broken question
**Q:** Which Austrian Bundesliga club did not co-host Euro 2008?
**Answer:** Red Bull Salzburg
**Why it fails:** Clubs do not "co-host" national tournaments — nations do. Additionally, Salzburg's Wals-Siezenheim stadium WAS used at Euro 2008, making Red Bull Salzburg the wrong answer even under a charitable reading.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2008
**Remedy:** Remove entirely — the question premise is incoherent.

### Row 2766 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian Bundesliga club had players in Austria's 2022 FIFA World Cup squad?
**Answer:** Red Bull Salzburg
**Why it fails:** Austria had no 2022 FIFA World Cup squad — they did not qualify.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change to "2022 World Cup qualifying squad" or "2026 World Cup squad."

### Row 2772 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian Bundesliga club produced the most players for the 2022 FIFA World Cup?
**Answer:** Red Bull Salzburg
**Why it fails:** In the Austria context, this implies Austria had players at the 2022 WC — they did not qualify.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Reframe to the 2026 WC or specify "for all national teams at the 2022 WC."

### Row 2776 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian Bundesliga club provided the most players to Austria's 2018 World Cup squad?
**Answer:** Red Bull Salzburg
**Why it fails:** Austria did not qualify for the 2018 World Cup.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change to "2018 World Cup qualifying squad."

### Row 2777 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian Bundesliga club saw its player debut at the 2022 FIFA World Cup?
**Answer:** Red Bull Salzburg
**Why it fails:** Austria was not at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove or rewrite around 2026 WC.

### Row 2781 — Austria (medium) — FAIL: false premise
**Q:** Which Austrian Bundesliga club's feeder nation reached the 2022 World Cup knockout stage?
**Answer:** Red Bull Salzburg
**Why it fails:** Austria (the feeder nation) did not qualify for the 2022 WC, let alone reach the knockout stage.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove entirely.

### Row 2782 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian Bundesliga club's player debuted for Austria at the 2018 FIFA World Cup?
**Answer:** Red Bull Salzburg
**Why it fails:** Austria did not qualify for the 2018 World Cup.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove or rewrite around the 2026 WC.

### Row 2784 — Austria (easy) — FAIL: unverifiable/false
**Q:** Which Austrian Bundesliga club's player scored a goal for Germany at the 2014 World Cup?
**Answer:** Red Bull Salzburg
**Why it fails:** No known Red Bull Salzburg alumnus scored for Germany at the 2014 World Cup. Germany's scorers came predominantly from Bayern Munich, Borussia Dortmund, etc.
**Source:** https://en.wikipedia.org/wiki/Germany_at_the_2014_FIFA_World_Cup
**Remedy:** Remove — claim is not verifiable and appears false.

### Row 2786 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian Bundesliga club's players helped Austria qualify for the 2022 World Cup?
**Answer:** Red Bull Salzburg
**Why it fails:** Austria did not qualify for the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change to "…qualify for the 2026 World Cup."

### Row 2787 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian Bundesliga club's players starred for Austria at the 2018 World Cup?
**Answer:** Red Bull Salzburg
**Why it fails:** Austria did not qualify for the 2018 World Cup.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove entirely.

### Row 2794 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian club had the most players at the 2022 FIFA World Cup?
**Answer:** Red Bull Salzburg
**Why it fails:** In the Austria context, this implies Austria participated in the 2022 WC — they did not qualify.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Reframe to 2026 WC or specify "among all nations at the 2022 WC."

### Row 2804 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian club produced most players in Austria's 2022 World Cup squad?
**Answer:** Red Bull Salzburg
**Why it fails:** Austria had no 2022 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change to "2026 World Cup squad."

### Row 2809 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian club's academy graduates helped Austria qualify for the 2022 World Cup?
**Answer:** Red Bull Salzburg
**Why it fails:** Austria did not qualify for the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change to "2026 World Cup."

### Row 2811 — Austria (easy) — FAIL: unverifiable/false
**Q:** Which Austrian club's academy produced stars for Germany's 2014 World Cup team?
**Answer:** Red Bull Salzburg
**Why it fails:** No confirmed Red Bull Salzburg alumnus featured for Germany at the 2014 WC. The claim is unverifiable and appears false.
**Source:** https://en.wikipedia.org/wiki/Germany_at_the_2014_FIFA_World_Cup
**Remedy:** Remove — claim appears baseless.

### Row 2814 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian club's players qualified for the 2022 FIFA World Cup?
**Answer:** Red Bull Salzburg
**Why it fails:** Austria did not qualify for the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change to "2026 FIFA World Cup."

### Row 2815 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian club's talent pipeline contributed players to Austria's 2022 FIFA World Cup squad?
**Answer:** Red Bull Salzburg
**Why it fails:** Austria had no 2022 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change to "2026 FIFA World Cup squad."

### Row 2820 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian club's youth academy produced Erling Haaland before his 2022 World Cup debut?
**Answer:** Red Bull Salzburg
**Why it fails:** Norway did not qualify for the 2022 World Cup. Haaland did not have a "2022 World Cup debut."
**Source:** https://en.wikipedia.org/wiki/Norway_at_the_2022_FIFA_World_Cup
**Remedy:** Change to "…before his 2026 World Cup debut" or "…before his move to Borussia Dortmund."

### Row 2828 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian defender at the 2022 World Cup had over 100 caps?
**Answer:** David Alaba
**Why it fails:** Austria was not at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove "at the 2022 World Cup" — Alaba does have 100+ caps, just not at that tournament.

### Row 2829 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian defender at the 2022 World Cup has won the Champions League with Bayern Munich and Real Madrid?
**Answer:** David Alaba
**Why it fails:** Austria was not at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove "at the 2022 World Cup."

### Row 2832 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian defender in the 2022 World Cup squad won the Champions League with both Bayern Munich and Real Madrid?
**Answer:** David Alaba
**Why it fails:** Austria had no 2022 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove "2022 World Cup squad" framing.

### Row 2833 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian defender was in the 2022 World Cup squad after winning the Champions League with Real Madrid?
**Answer:** David Alaba
**Why it fails:** Austria had no 2022 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove "2022 World Cup squad" framing.

### Row 2834 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian defender was selected for the 2022 World Cup squad due to his Champions League wins?
**Answer:** David Alaba
**Why it fails:** Austria had no 2022 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove "2022 World Cup squad" framing.

### Row 2838 — Austria (easy) — FAIL: wrong timeline
**Q:** Which Austrian defender won the Champions League with Bayern and Real before EURO 2020?
**Answer:** David Alaba
**Why it fails:** Alaba won the UCL with Real Madrid in May 2022, which is AFTER Euro 2020 (held June–July 2021). He only won with Bayern (2013, 2020) before Euro 2020, not with Real.
**Source:** https://en.wikipedia.org/wiki/David_Alaba
**Remedy:** Change to "…won the Champions League with two different clubs?" or remove the "before EURO 2020" clause.

### Row 2848 — Austria (easy) — FAIL: wrong timing
**Q:** Which Austrian forward became their all-time top scorer during 2022 World Cup qualifying?
**Answer:** Marko Arnautović
**Why it fails:** Arnautović broke Polster's record in October 2025, not during the 2022 WC qualifying (2020–21).
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change to "…during 2026 World Cup qualifying."

### Row 2851 — Austria (easy) — FAIL: wrong fact
**Q:** Which Austrian forward, a Red Bull Salzburg product, started the 2022 World Cup qualifier against Scotland?
**Answer:** Marko Arnautović
**Why it fails:** Arnautović is NOT a Red Bull Salzburg product. His career began at Floridsdorfer AC / Kapfenberger SV, then Twente (Netherlands) at age 16.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Remove "a Red Bull Salzburg product."

### Row 2857 — Austria (easy) — FAIL: wrong fact
**Q:** Which Austrian international moved from Red Bull Salzburg to Bayern Munich in 2012?
**Answer:** David Alaba
**Why it fails:** Alaba never played for Red Bull Salzburg. He joined Bayern Munich's youth academy from Vienna clubs (FK Austria Wien youth) in 2008.
**Source:** https://en.wikipedia.org/wiki/David_Alaba
**Remedy:** Remove "from Red Bull Salzburg" — Alaba moved from FK Austria Wien youth to Bayern Munich.

### Row 2859 — Austria (easy) — FAIL: wrong club/era
**Q:** Which Austrian key midfielder played for Borussia Dortmund during 2022 World Cup qualifiers?
**Answer:** Marcel Sabitzer
**Why it fails:** Sabitzer was at Bayern Munich during the 2022 WC qualifying campaign (2020–21). He joined Borussia Dortmund in January 2024.
**Source:** https://en.wikipedia.org/wiki/Marcel_Sabitzer
**Remedy:** Change to "…during Euro 2024" (when he was indeed at Dortmund).

### Row 2869 — Austria (easy) — FAIL: wrong timing
**Q:** Which Austrian manager implemented gegenpressing after the 2022 World Cup?
**Answer:** Ralf Rangnick
**Why it fails:** Rangnick implemented his gegenpressing system from the start of his tenure (January 2022), well BEFORE the 2022 World Cup (November–December 2022), not after it.
**Source:** https://en.wikipedia.org/wiki/Ralf_Rangnick
**Remedy:** Change to "…before the 2022 World Cup" or "…ahead of the 2026 World Cup."

### Row 2871 — Austria (easy) — FAIL: wrong manager
**Q:** Which Austrian manager implemented pressing football during 2022 World Cup qualifying?
**Answer:** Ralf Rangnick
**Why it fails:** The 2022 WC qualifying ran September 2020 – November 2021, entirely under Franco Foda. Rangnick was only appointed in January 2022, after qualifying ended.
**Source:** https://en.wikipedia.org/wiki/Franco_Foda
**Remedy:** Change answer to Franco Foda, or change the question to the 2026 WC qualifying campaign.

### Row 2916 — Austria (easy) — FAIL: wrong club/era
**Q:** Which Austrian midfielder at Borussia Dortmund played in 2022 World Cup qualifiers?
**Answer:** Marcel Sabitzer
**Why it fails:** Sabitzer was at RB Leipzig (until August 2021) then Bayern Munich during the 2022 WC qualifying campaign. He joined Dortmund in January 2024.
**Source:** https://en.wikipedia.org/wiki/Marcel_Sabitzer
**Remedy:** Change Borussia Dortmund to Bayern Munich/RB Leipzig, or change the tournament to Euro 2024.

### Row 2917 — Austria (easy) — FAIL: wrong club/era
**Q:** Which Austrian midfielder at the 2022 World Cup qualifiers plays for Borussia Dortmund?
**Answer:** Marcel Sabitzer
**Why it fails:** Same as row 2916 — Sabitzer was not at Dortmund during 2022 WC qualifying.
**Source:** https://en.wikipedia.org/wiki/Marcel_Sabitzer
**Remedy:** Change club to RB Leipzig / Bayern Munich for that period.

### Row 2918 — Austria (easy) — FAIL: wrong year
**Q:** Which Austrian midfielder debuted for the national team in 2012?
**Answer:** Marcel Sabitzer
**Why it fails:** Sabitzer's first Austria cap was March 29, 2014 (friendly vs Slovakia), not 2012.
**Source:** https://en.wikipedia.org/wiki/Marcel_Sabitzer
**Remedy:** Change 2012 to 2014.

### Row 2924 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian midfielder made his World Cup debut in 2022?
**Answer:** Konrad Laimer
**Why it fails:** Austria did not qualify for the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove entirely or rewrite for the 2026 WC.

### Row 2931 — Austria (easy) — FAIL: wrong opponent
**Q:** Which Austrian midfielder scored a crucial goal against Ukraine in 2022 World Cup qualifying?
**Answer:** Konrad Laimer
**Why it fails:** Ukraine was NOT in Austria's 2022 WC qualifying group (Group F: Denmark, Scotland, Israel, Faroe Islands, Moldova). Austria never played Ukraine in this campaign.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_–_UEFA_Group_F
**Remedy:** Change Ukraine to Scotland, Denmark, or Israel (their actual group opponents).

### Row 2935 — Austria (easy) — FAIL: false venue
**Q:** Which Austrian midfielder started the 2022 World Cup qualifier at Wembley Stadium?
**Answer:** Marcel Sabitzer
**Why it fails:** Austria never played a 2022 WC qualifier at Wembley. Wembley hosts England home games; Austria and England were in different qualifying groups.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_–_UEFA_Group_F
**Remedy:** Remove or change venue to Ernst-Happel-Stadion.

### Row 2939 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian midfielder with over 70 caps was in the 2022 FIFA World Cup squad?
**Answer:** Marcel Sabitzer
**Why it fails:** Austria had no 2022 FIFA World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change to "2022 World Cup qualifying squad."

### Row 2944 — Austria (easy) — FAIL: wrong club/false premise
**Q:** Which Austrian midfielder's Bayern Munich faced Austria in 2022 World Cup qualifiers?
**Answer:** Konrad Laimer
**Why it fails:** Laimer was at RB Leipzig during the 2022 WC qualifying (he joined Bayern Munich in 2023). Additionally, clubs don't play national team qualifiers — the premise conflates club football with international football.
**Source:** https://en.wikipedia.org/wiki/Konrad_Laimer
**Remedy:** Remove entirely — the question is incoherent.

### Row 2951 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian player at the 2022 World Cup has Champions League titles with Bayern and Real?
**Answer:** David Alaba
**Why it fails:** Austria was not at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove "at the 2022 World Cup."

### Row 2953 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian player at the 2022 World Cup has won the Champions League with two clubs?
**Answer:** David Alaba
**Why it fails:** Austria was not at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove "at the 2022 World Cup."

### Row 2954 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian player at the 2022 World Cup was not based in the Bundesliga?
**Answer:** David Alaba
**Why it fails:** Austria was not at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove "at the 2022 World Cup."

### Row 2955 — Austria (easy) — FAIL: wrong timing
**Q:** Which Austrian player became his nation's all-time top scorer during 2022 World Cup qualifying?
**Answer:** Marko Arnautović
**Why it fails:** Arnautović broke Polster's record in October 2025, not during 2022 WC qualifying (2020–21).
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change to "…during 2026 World Cup qualifying."

### Row 2956 — Austria (easy) — FAIL: wrong year
**Q:** Which Austrian player became their all-time top scorer in 2023?
**Answer:** Marko Arnautović
**Why it fails:** Arnautović broke Polster's record in October 2025, not in 2023.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change 2023 to 2025.

### Row 2957 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian player debuted after Austria co-hosted Euro 2008, at the 2014 World Cup?
**Answer:** Kevin Wimmer
**Why it fails:** Austria did not qualify for the 2014 World Cup. No Austrian player could have debuted "at the 2014 World Cup."
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove "at the 2014 World Cup" framing.

### Row 2958 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian player developed at Red Bull Salzburg played at the 2018 FIFA World Cup?
**Answer:** Konrad Laimer
**Why it fails:** Austria did not qualify for the 2018 World Cup. Laimer played for RB Leipzig in 2018, not Salzburg.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove entirely or rewrite around a friendly/qualifier.

### Row 2960 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian player from Red Bull Salzburg debuted at the 2018 FIFA World Cup?
**Answer:** Xaver Schlager
**Why it fails:** Austria did not qualify for the 2018 World Cup.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove entirely.

### Row 2961 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian player from Red Bull Salzburg debuted at the 2022 FIFA World Cup?
**Answer:** Nicolas Seiwald
**Why it fails:** Austria did not qualify for the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove entirely or rewrite around the 2026 WC.

### Row 2974 — Austria (easy) — FAIL: non-unique answer
**Q:** Which Austrian player missed the 2010, 2014, 2018, and 2022 FIFA World Cups?
**Answer:** Marko Arnautović
**Why it fails:** Every Austrian player of that era (Alaba, Sabitzer, Baumgartlinger, etc.) missed those same four World Cups — Austria as a team did not qualify. The answer is not unique to Arnautović.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Remove or rewrite to name something distinctly Arnautović (e.g., record scorer, appearance milestones).

### Row 2975 — Austria (easy) — FAIL: wrong player
**Q:** Which Austrian player reached 100 caps during 2022 World Cup qualifying?
**Answer:** Marko Arnautović
**Why it fails:** It was David Alaba who earned his 100th cap in a 2022 WC qualifier (confirmed in pool row 2679 as a PASS). Arnautović's 100th cap timing needs separate verification.
**Source:** https://en.wikipedia.org/wiki/David_Alaba
**Remedy:** Change answer to David Alaba, or verify Arnautović's 100th cap date independently.

### Row 2980 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian player scored in a 2022 World Cup qualifier to extend his national team goal record?
**Answer:** Marko Arnautović
**Why it fails:** Arnautović was NOT the all-time record holder during the 2022 WC qualifying — Polster held the record until October 2025. He could not "extend his record" since the record was not yet his.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change to "…scored in a 2026 World Cup qualifier to extend his national team goal record."

### Row 2981 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian player scored in the 2014 World Cup to join his nation's scoring leaders?
**Answer:** Marko Arnautović
**Why it fails:** Austria did not qualify for the 2014 World Cup.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove entirely.

### Row 2983 — Austria (easy) — FAIL: wrong match
**Q:** Which Austrian player scored in their Euro 2008 opening match?
**Answer:** Ivica Vastic
**Why it fails:** Austria's opening match at Euro 2008 was June 8 vs Croatia (lost 0–1) — they scored ZERO goals. Vastic scored a penalty in Austria's SECOND group match vs Poland (June 12, 1–1 draw).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2008_Group_B
**Remedy:** Change "opening match" to "second group match vs Poland."

### Row 2988 — Austria (easy) — FAIL: wrong fact
**Q:** Which Austrian player scored the winning goal against North Macedonia at Euro 2020?
**Answer:** Marko Arnautović
**Why it fails:** Arnautović's goal vs North Macedonia was DISALLOWED for offside. Austria won 3–1 with goals from Lainer, Alaba, and Gregoritsch; Arnautović did not score the winner.
**Source:** https://en.wikipedia.org/wiki/Austria_v_North_Macedonia_(UEFA_Euro_2020)
**Remedy:** Change to Lainer (1st goal), Alaba (2nd), or Gregoritsch (3rd/winner). Remove Arnautović.

### Row 2990 — Austria (easy) — FAIL: wrong scorer
**Q:** Which Austrian player scored twice to beat Netherlands at Euro 2024?
**Answer:** Marko Arnautovic
**Why it fails:** It was Marcel Sabitzer who scored twice (including the winner). Arnautović scored once or not at all in that match.
**Source:** https://en.wikipedia.org/wiki/Netherlands_v_Austria_(UEFA_Euro_2024)
**Remedy:** Change answer to Marcel Sabitzer.

### Row 2994 — Austria (easy) — FAIL: wrong timing
**Q:** Which Austrian player was his nation's all-time top scorer at the 2022 World Cup qualifiers?
**Answer:** Marko Arnautović
**Why it fails:** Polster (44 goals) held the record throughout the 2022 WC qualifying. Arnautović broke it in October 2025.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change to "…at the 2026 World Cup qualifiers."

### Row 2997 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian player was NOT their nation's top scorer at the 2022 FIFA World Cup?
**Answer:** Marko Arnautović
**Why it fails:** Austria was not at the 2022 FIFA World Cup; the premise of any Austrian "top scorer at the 2022 WC" is false.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove entirely.

### Row 3000 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian player was the team's all-time top scorer at the 2022 FIFA World Cup?
**Answer:** Marko Arnautović
**Why it fails:** Austria was not at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove or rewrite around the 2026 WC.

### Row 3001 — Austria (easy) — FAIL: wrong timing
**Q:** Which Austrian player was the team's all-time top scorer during their 2022 World Cup qualifying campaign?
**Answer:** Marko Arnautović
**Why it fails:** Polster's record stood through the 2022 WC qualifying. Arnautović broke it in October 2025.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change to "…2026 World Cup qualifying campaign."

### Row 3007 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian player, active in the 2014 World Cup, holds the national team's all-time scoring record?
**Answer:** Marko Arnautović
**Why it fails:** Austria was not at the 2014 World Cup. No Austrian player was "active in the 2014 World Cup" for Austria.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove "active in the 2014 World Cup" clause.

### Row 3008 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian player, from their 2022 World Cup squad, won the Champions League with Bayern Munich and Real Madrid?
**Answer:** David Alaba
**Why it fails:** Austria had no 2022 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove "2022 World Cup squad" framing.

### Row 3009 — Austria (easy) — FAIL: wrong timing
**Q:** Which Austrian player, their all-time top scorer, scored in a 2022 World Cup qualifier?
**Answer:** Marko Arnautović
**Why it fails:** Arnautović was NOT the all-time top scorer during 2022 WC qualifying — Polster held the record until October 2025.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change to "…scored in a 2026 World Cup qualifier."

### Row 3011 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian player's Champions League success aided his 2022 World Cup selection?
**Answer:** David Alaba
**Why it fails:** Austria had no 2022 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change to "2026 World Cup selection."

### Row 3012 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian player's Champions League wins enabled his 2022 World Cup squad selection?
**Answer:** David Alaba
**Why it fails:** Austria had no 2022 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change to "2026 World Cup squad selection."

### Row 3013 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian player's elite club pedigree led to his 2022 World Cup tactical deployment as a midfielder?
**Answer:** David Alaba
**Why it fails:** Austria was not at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove "2022 World Cup" framing.

### Row 3015 — Austria (medium) — FAIL: false premise + wrong timing
**Q:** Which Austrian player's scoring record was key to their 2022 World Cup qualification?
**Answer:** Marko Arnautović
**Why it fails:** (1) Austria did not qualify for the 2022 WC. (2) Arnautović was not the all-time scoring record holder during 2022 WC qualifying.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change to "2026 World Cup qualification."

### Row 3016 — Austria (easy) — FAIL: non-unique/invalid answer
**Q:** Which Austrian player's World Cup debut will end a 28-year absence in 2026?
**Answer:** Any current Austrian player
**Why it fails:** "Any current Austrian player" is not a specific, unique answer — it's a generic statement applicable to the entire squad.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Name a specific player (e.g., Christoph Baumgartner, Konrad Laimer) or remove.

### Row 3028 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian stadium hosted the 2022 World Cup qualifying playoff final?
**Answer:** Ernst-Happel-Stadion
**Why it fails:** Austria was NOT in any 2022 WC qualifying playoff. They finished low in Group F and did not advance to the playoffs.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_–_UEFA_Group_F
**Remedy:** Remove entirely — the event described never happened.

### Row 3047 — Austria (easy) — FAIL: wrong timing
**Q:** Which Austrian striker became the nation's all-time top scorer during the 2018 World Cup qualifying cycle?
**Answer:** Marko Arnautović
**Why it fails:** Arnautović did not break Polster's 44-goal record during the 2018 WC qualifying (2016–17). The record fell in October 2025.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change to "…during the 2026 World Cup qualifying cycle."

### Row 3048 — Austria (easy) — FAIL: wrong fact
**Q:** Which Austrian striker had more international goals than Sweden's Zlatan Ibrahimović by the 2022 World Cup?
**Answer:** Marko Arnautović
**Why it fails:** Ibrahimović finished with 62 goals for Sweden. By the 2022 WC (late 2022), Arnautović had approximately 32–34 goals. Arnautović had far FEWER, not more.
**Source:** https://en.wikipedia.org/wiki/Zlatan_Ibrahimovi%C4%87
**Remedy:** Remove entirely — the claim is factually false.

### Row 3050 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian striker was in their 2018 World Cup squad?
**Answer:** Marko Arnautović
**Why it fails:** Austria did not qualify for the 2018 World Cup.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change to "2018 World Cup qualifying squad."

### Row 3051 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian striker was included in the 2022 FIFA World Cup squad?
**Answer:** Marko Arnautović
**Why it fails:** Austria did not qualify for the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change to "2022 World Cup qualifying squad" or "2026 World Cup squad."

### Row 3052 — Austria (easy) — FAIL: wrong timing
**Q:** Which Austrian striker, their all-time top scorer, played in 2022 World Cup qualifying?
**Answer:** Marko Arnautović
**Why it fails:** Arnautović was NOT the all-time top scorer during 2022 WC qualifying (Polster held the record until October 2025).
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Change to "…their all-time top scorer, played in 2026 World Cup qualifying."

### Row 3053 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian striker's goals secured their 2022 World Cup playoff spot?
**Answer:** Marko Arnautović
**Why it fails:** Austria did NOT reach a 2022 WC qualifying playoff. They finished 5th in Group F (below Denmark, Scotland, Israel, and Faroe Islands in the final standings), far below the playoff threshold.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_–_UEFA_Group_F
**Remedy:** Remove entirely — the event described never occurred.

### Row 3064 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian World Cup 2022 player developed at Red Bull Salzburg?
**Answer:** Karim Onisiwo
**Why it fails:** Austria was not at the 2022 World Cup. There are no "Austrian World Cup 2022 players."
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change to "2026 World Cup squad."

### Row 3071 — Austria (easy) — FAIL: false premise
**Q:** Which Austrian, a Red Bull Salzburg product, debuted in the 2022 FIFA World Cup?
**Answer:** Konrad Laimer
**Why it fails:** Austria was not at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove entirely or rewrite for the 2026 WC.

### Row 3081 — Austria (easy) — FAIL: false premise
**Q:** Which key Austrian attacker debuted at the 2022 FIFA World Cup?
**Answer:** Christoph Baumgartner
**Why it fails:** Austria was not at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Remove or rewrite for the 2026 WC.

### Row 3091 — Austria (medium) — FAIL: wrong name
**Q:** Which manager led Austria to their highest FIFA ranking before the 2018 World Cup?
**Answer:** Franz Koller
**Why it fails:** No manager named "Franz Koller" has ever managed Austria. The correct answer is Marcel Koller (who managed Austria 2011–2017 and oversaw their peak ranking of 10th).
**Source:** https://en.wikipedia.org/wiki/Marcel_Koller
**Remedy:** Change answer to Marcel Koller.

### Row 3150 — Austria (easy) — FAIL: false premise
**Q:** Which stadium hosted Austria's 2022 World Cup qualifying playoff final?
**Answer:** Ernst-Happel-Stadion
**Why it fails:** Austria was not in any 2022 WC qualifying playoff. They finished low in Group F and did not reach the playoff stage.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_–_UEFA_Group_F
**Remedy:** Remove entirely.

### Row 3181 — Austria (medium) — FAIL: self-referential answer
**Q:** Which UEFA nation, like Austria, peaked at 10th in the FIFA rankings between 2006-2026?
**Answer:** Austria
**Why it fails:** The question asks which nation "like Austria" matches this achievement, but the answer is Austria itself — a self-referential, trivially wrong structure.
**Source:** https://www.fifa.com/fifa-world-ranking/
**Remedy:** Replace Austria in the answer with the actual other nation that peaked at 10th (e.g., Denmark, Switzerland), or rewrite the question.

### Row 3199 — Austria (medium) — FAIL: false premise
**Q:** Which World Cup did Austria qualify for after co-hosting Euro 2008?
**Answer:** 2010 World Cup
**Why it fails:** Austria did NOT qualify for the 2010 World Cup. They have not qualified for any WC since 1998 (France) — missing 2002, 2006, 2010, 2014, 2018, and 2022 before qualifying for 2026.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Remove entirely — the event described never occurred.

### Row 3202 — Austria (hard) — FAIL: false premise
**Q:** Which World Cup did Austria's David Alaba miss due to injury?
**Answer:** 2022 FIFA World Cup
**Why it fails:** Austria did not qualify for the 2022 World Cup. While Alaba was injured during the qualifying period, Austria's failure was a team qualification failure, not Alaba's personal injury absence from a tournament.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Rewrite as "Which World Cup qualifying campaign did Alaba miss key matches in due to injury?"

### Row 3203 — Austria (hard) — FAIL: wrong World Cup cycle
**Q:** Which World Cup qualifying cycle was concurrent with Austria's Euro 2016 qualification under Marcel Koller?
**Answer:** 2014 World Cup cycle
**Why it fails:** Austria's Euro 2016 qualifying ran September 2014 – November 2015. The 2014 WC qualifying cycle had already ended in 2013. The cycle concurrent with Euro 2016 qualifying was the early stages of the 2018 WC cycle (2014–2018 period).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2016_qualifying
**Remedy:** Change answer to "2018 World Cup cycle."

### Row 3222 — Austria (easy) — FAIL: wrong timing
**Q:** Who transformed Austrian football before their 2022 World Cup qualifiers?
**Answer:** Ralf Rangnick
**Why it fails:** Rangnick was appointed January 2022. The 2022 WC qualifying campaign ended November 2021 — he was not involved in any 2022 WC qualifier.
**Source:** https://en.wikipedia.org/wiki/Ralf_Rangnick
**Remedy:** Change to "…before their 2026 World Cup qualifiers."

### Row 3224 — Austria (easy) — FAIL: false premise
**Q:** Who was Austria's star defender selected for the 2022 FIFA World Cup squad?
**Answer:** David Alaba
**Why it fails:** Austria had no 2022 FIFA World Cup squad — they did not qualify.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change to "2026 FIFA World Cup squad."

### Row 3237 — Austria (easy) — FAIL: false premise
**Q:** Why did Austria's 2022 FIFA World Cup squad have many overseas players?
**Answer:** Austrian Bundesliga exports talent
**Why it fails:** Austria had no 2022 FIFA World Cup squad — they did not qualify.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change to "2026 FIFA World Cup squad."

### Row 2934 — Austria (easy) — FAIL: wrong scorer
**Q:** Which Austrian midfielder scored more goals in 2022 World Cup qualifying: Marcel Sabitzer or Christoph Baumgartner?
**Answer:** Marcel Sabitzer
**Why it fails:** Baumgartner scored 4 goals (Austria's top scorer in the 2022 WC qualifying campaign); Sabitzer scored 2. Baumgartner scored MORE, not Sabitzer.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_–_UEFA_Group_F
**Remedy:** Change answer to Christoph Baumgartner.

### Row 2986 — Austria (easy) — FAIL: wrong top scorer
**Q:** Which Austrian player scored the most goals in 2022 World Cup qualifying?
**Answer:** Marko Arnautović
**Why it fails:** Christoph Baumgartner scored 4 goals in the 2022 WC qualifying campaign — the most of any Austrian player. Arnautović scored fewer than Baumgartner in that specific campaign.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_–_UEFA_Group_F
**Remedy:** Change answer to Christoph Baumgartner. (For all-time WC qualifying goals across all campaigns, Arnautović leads — but the question asks about the 2022 campaign.)

### Row 2996 — Austria (easy) — FAIL: wrong top scorer
**Q:** Which Austrian player was his team's top scorer in 2022 World Cup qualifying?
**Answer:** Marko Arnautović
**Why it fails:** Baumgartner scored 4 goals in the 2022 WC qualifying campaign — more than Arnautović. Baumgartner was Austria's top scorer in that campaign.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_–_UEFA_Group_F
**Remedy:** Change answer to Christoph Baumgartner.

### Row 2998 — Austria (easy) — FAIL: wrong top scorer
**Q:** Which Austrian player was the nation's top scorer during 2022 World Cup qualifying?
**Answer:** Marko Arnautović
**Why it fails:** Baumgartner (4 goals) was the top scorer, not Arnautović, in the 2022 WC qualifying campaign.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_–_UEFA_Group_F
**Remedy:** Change answer to Christoph Baumgartner.

### Row 3003 — Austria (easy) — FAIL: wrong top scorer
**Q:** Which Austrian player was their top scorer during 2022 World Cup qualifiers?
**Answer:** Marko Arnautović
**Why it fails:** Same as rows 2986/2996/2998 — Baumgartner (4) outscored Arnautović in the 2022 campaign.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_–_UEFA_Group_F
**Remedy:** Change answer to Christoph Baumgartner.

### Row 3004 — Austria (easy) — FAIL: wrong top scorer
**Q:** Which Austrian player was their top scorer in the 2022 World Cup qualifiers?
**Answer:** Marko Arnautović
**Why it fails:** Same — Baumgartner scored 4 goals (most) vs Arnautović's fewer goals in the 2022 WC qualifying campaign.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_–_UEFA_Group_F
**Remedy:** Change answer to Christoph Baumgartner.
