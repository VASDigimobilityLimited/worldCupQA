# QA_FAILED_LIVENESS_b2.md — Batch 2 dangerous (passed mechanical, FAILED liveness)

> Rows that cleared `QA_PASSED_b2.md` mechanically but are **factually wrong** on the live
> TC-06 check. Each entry: reason + source + concrete remedy. See HANDOFF.md §6/§7.

**Total dangerous: 997** (Algeria 159, rows 2–513; Argentina 167, rows 514–1543; Belgium 170, rows 3242–4191; Bosnia and Herzegovina 125, rows 4192–5804; Canada 69, rows 7821–9330; Colombia 168, rows 10796–11736; Costa Rica 139, rows 11737–12858)

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
