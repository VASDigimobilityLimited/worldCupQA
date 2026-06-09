# QA_FAILED_LIVENESS_b2.md — Batch 2 dangerous (passed mechanical, FAILED liveness)

> Rows that cleared `QA_PASSED_b2.md` mechanically but are **factually wrong** on the live
> TC-06 check. Each entry: reason + source + concrete remedy. See HANDOFF.md §6/§7.

**Total dangerous: 702** (Algeria 159, rows 2–513; Argentina 167, rows 514–1543; Canada 69, rows 7821–9330; Colombia 168, rows 10796–11736; Costa Rica 139, rows 11737–12858)

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
