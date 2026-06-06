# QA — TC-06 Live Check: FAILED

Rows where the `answer` is wrong, the `explanation` is wrong, the question asserts
an event that did not happen, or the fact could not be confirmed (UNVERIFIED →
conservative fail). Dataset order. Cursor lives in `QA_TC06_LIVE.md`.

Total failed so far: **48** (rows 2–230 checked)

---

### Row 3 — Algeria (medium) — FAIL (false premise + wrong answer)
**Q:** After Algeria's 2018 AFCON win, which World Cup did Djamel Belmadi coach them at?
**Answer:** 2022 World Cup
**Why it failed:** False on two counts. (1) There was no "2018 AFCON" — Algeria's title was the **2019** AFCON (editions are 2017, 2019). (2) Belmadi did not coach Algeria *at* a World Cup; they **failed to qualify** for 2022.
**Source:** [Wikipedia — 2019 AFCON final](https://en.wikipedia.org/wiki/2019_Africa_Cup_of_Nations_final), [ESPN — Algeria 1-2 Cameroon (2022 playoff)](https://www.espn.com/soccer/match/_/gameId/629214/cameroon-algeria)
**Remedy:** Re-anchor to a real event, e.g. "Which AFCON did Djamel Belmadi win with Algeria?" → **2019**; or drop.

### Row 4 — Algeria (medium) — FAIL (answer right, explanation false)
**Q:** After Algeria's 2019 AFCON win, how many FIFA World Cups have they qualified for since?
**Answer:** One
**Why it failed:** The **answer "One" is correct** (failed 2022, qualified 2026), but the stored **explanation is false** — "Algeria qualified for the 2022 FIFA World Cup" never happened. Wrong explanation = TC-06 fail.
**Source:** [FIFA — Algeria qualify (2026)](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/algeria-qualify), [ESPN — 2022 playoff loss](https://www.espn.com/soccer/match/_/gameId/629214/cameroon-algeria)
**Remedy:** Keep answer "One"; rewrite explanation: "Algeria failed to qualify for 2022 but qualified for the 2026 World Cup — one since their 2019 AFCON title."

### Row 5 — Algeria (medium) — UNVERIFIED → FAIL
**Q:** After Algeria's 2019 AFCON win, when did their squad rebuild start?
**Answer:** 2019
**Why it failed:** "Squad rebuild started 2019" is a soft narrative claim with no authoritative source; explanation is also self-referential ("The verified fact states…"). Cannot confirm.
**Source:** none located.
**Remedy:** Hold for source confirmation, or drop — not a crisp, verifiable fact.

### Row 6 — Algeria (medium) — FAIL (misleading/contradictory + unverifiable)
**Q:** After Algeria's 2019 AFCON win, when did their World Cup squad rebuild begin?
**Answer:** After 2022 qualification
**Why it failed:** The answer "After 2022 qualification" implies Algeria qualified for 2022 (false). The explanation says the rebuild followed their **failure** to qualify — contradicting the answer. The underlying rebuild date is unverifiable.
**Source:** [ESPN — 2022 playoff loss](https://www.espn.com/soccer/match/_/gameId/629214/cameroon-algeria)
**Remedy:** Drop, or rephrase to "After failing to qualify for 2022" with a sourced date.

### Row 8 — Algeria (hard) — FAIL (wrong answer)
**Q:** After Algeria's 2019 AFCON win, which World Cup did they qualify for?
**Answer:** 2022 FIFA World Cup
**Why it failed:** Wrong. Algeria did **not** qualify for 2022. The first World Cup they qualified for after the 2019 AFCON was **2026**.
**Source:** [FIFA — Algeria qualify (2026)](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/algeria-qualify), [ESPN — 2022 playoff loss](https://www.espn.com/soccer/match/_/gameId/629214/cameroon-algeria)
**Remedy:** Change answer to **2026 FIFA World Cup**; adjust distractors and fix the explanation.

### Row 10 — Algeria (medium) — FAIL (logically broken)
**Q:** After Algeria's 2021 AFCON group stage exit, which other defending champion also failed to advance?
**Answer:** Algeria
**Why it failed:** The answer "Algeria" restates the subject of the question, so it cannot be the "other" team — internally broken. (Algeria, the 2019 champion, did exit the group at the 2021 AFCON, but the question asks for a *different* defending champion.)
**Source:** [Wikipedia — 2019 AFCON final (Algeria = defending champion)](https://en.wikipedia.org/wiki/2019_Africa_Cup_of_Nations_final)
**Remedy:** Drop — the answer restates the subject; the question is logically broken.

### Row 18 — Algeria (easy) — FAIL (wrong scorer for the stated match)
**Q:** After winning the 2019 AFCON, which Algeria player scored in a 1-1 World Cup qualifier draw with Burkina Faso?
**Answer:** Riyad Mahrez
**Why it failed:** In the **1-1** Algeria–Burkina Faso 2022 qualifier (7 Sep 2021), the Algeria scorer was **Sofiane Feghouli**, not Mahrez. Mahrez scored in the *other* fixture, the **2-2** draw (16 Nov 2021). So the answer is wrong for the match described — and Feghouli isn't even among the options (Slimani / Bounedjah / Belaïli).
**Source:** [Wikipedia — 2022 WC qualification (CAF) second round, Group A](https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_%E2%80%93_CAF_Second_Round)
**Remedy:** Set answer to **Sofiane Feghouli** (and include him as an option); or re-anchor the question to the 2-2 draw, for which **Riyad Mahrez** is correct.

### Row 37 — Algeria (medium) — FAIL (TC-03: multiple valid answers)
**Q:** Algeria faced Germany in the 2014 World Cup round of 16. Which team did they NOT play in the knockout stage?
**Answer:** Brazil
**Why it failed:** Algeria played **only** Germany in the 2014 knockout stage, so they did not play Brazil — *but* they also did not play France, Argentina or Netherlands (the three distractors). All four options are equally correct, so there is no unique answer.
**Source:** [Wikipedia — 2014 World Cup knockout stage](https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_knockout_stage)
**Remedy:** Drop, or rewrite so exactly one option is true (e.g. "Which team DID Algeria face in the 2014 knockout stage?" → Germany, with three teams they didn't face as distractors).

### Row 41 — Algeria (easy) — FAIL (TC-03: multiple valid answers)
**Q:** Algeria lost 2-1 to Germany in 2014. Which other CAF team lost a World Cup knockout match to a European side?
**Answer:** Nigeria
**Why it failed:** Nigeria did lose 0-2 to France in the 2014 R16, but the unbounded question is satisfied by distractors too — **Cameroon** lost a knockout to England (1990 QF) and **Senegal** lost to Turkey (2002 QF, a UEFA side). The answer is not unique.
**Source:** [Wikipedia — 2014 World Cup knockout stage](https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_knockout_stage)
**Remedy:** Anchor to 2014 ("…lost a 2014 World Cup knockout match to a European side?") so only Nigeria qualifies.

### Row 42 — Algeria (easy) — FAIL (TC-03: multiple valid answers)
**Q:** Algeria lost 2-1 to Germany in the 2014 World Cup last 16. Which nation also lost their 2014 knockout match 2-1?
**Answer:** United States
**Why it failed:** The USA did lose 1-2 to Belgium (a.e.t.), but **Mexico also lost 2-1** in the 2014 R16 (Netherlands 2-1 Mexico) — and Mexico is one of the distractors. Two options are correct.
**Source:** [Wikipedia — 2014 World Cup knockout stage](https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_knockout_stage)
**Remedy:** Replace the Mexico distractor (e.g. with a team that lost by a different margin) so only the USA fits, or change the answer focus.

### Row 53 — Algeria (easy) — FAIL (explanation factually wrong)
**Q:** Algeria qualified for the 2010 World Cup via a playoff against which CAF nation?
**Answer:** Egypt
**Why it failed:** The answer "Egypt" is correct, but the **explanation is wrong**: it calls the tie an "intercontinental playoff." It was a **CAF qualifying play-off** (one-off match, Algeria 1-0 Egypt, Khartoum, 18 Nov 2009) — an all-African tie, not intercontinental.
**Source:** [France 24 — Algeria beat Egypt 1-0 to qualify](https://www.france24.com/en/20091118-algeria-beat-egypt-1-0-qualify-2010-world-cup), [Wikipedia — 2010 WC qualification (CAF) third round](https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round)
**Remedy:** Keep answer "Egypt"; fix explanation to "…via a CAF qualifying play-off against Egypt."

### Row 54 — Algeria (easy) — FAIL (TC-03 + false premise)
**Q:** Algeria qualified for the 2014 FIFA World Cup directly. Which other CAF nation also qualified directly in 2014?
**Answer:** Ivory Coast
**Why it failed:** Two problems. (1) No CAF team qualified "directly" for 2014 — the final round was five two-legged play-offs. (2) **Ghana and Nigeria** (both distractors) also qualified for 2014, so the answer is not unique.
**Source:** [Wikipedia — 2014 WC qualification (CAF) third round](https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_CAF_third_round)
**Remedy:** Drop or rewrite, e.g. "Which CAF teams won play-offs to reach 2014?" — but the four-option single-answer format can't hold five correct teams; recommend removal.

### Row 55 — Algeria (medium) — FAIL (wrong answer)
**Q:** Algeria qualified for the 2014 FIFA World Cup through CAF qualification, but how did they qualify for the 2010 World Cup?
**Answer:** Intercontinental playoff
**Why it failed:** Wrong. Algeria reached 2010 through **CAF qualification**, decided by a one-off CAF play-off vs Egypt — not an intercontinental play-off. Ironically "CAF qualification" is one of the distractors and is the more correct choice.
**Source:** [Wikipedia — 2010 WC qualification (CAF) third round](https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round), [France 24 — Algeria 1-0 Egypt](https://www.france24.com/en/20091118-algeria-beat-egypt-1-0-qualify-2010-world-cup)
**Remedy:** Change answer to "CAF play-off (vs Egypt)"; rebuild distractors (e.g. "Direct group qualification", "Intercontinental play-off", "Hosts").

### Row 57 — Algeria (medium) — FAIL (wrong answer)
**Q:** Algeria qualified for the 2014 World Cup through CAF qualification, but how did they qualify for the 2010 tournament?
**Answer:** Intercontinental playoff vs Egypt
**Why it failed:** The Egypt tie was a **CAF qualifying play-off**, not an intercontinental one (Algeria 1-0 Egypt, Khartoum, 18 Nov 2009). The distractor "CAF group stage winner" is closer to the truth than the keyed answer.
**Source:** [France 24 — Algeria 1-0 Egypt](https://www.france24.com/en/20091118-algeria-beat-egypt-1-0-qualify-2010-world-cup), [Wikipedia — 2010 WC qualification (CAF) third round](https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round)
**Remedy:** Change answer to "CAF play-off vs Egypt"; fix explanation accordingly.

### Row 58 — Algeria (medium) — FAIL (wrong answer)
**Q:** Algeria qualified for the 2026 World Cup via CAF qualification, but how did they qualify in 2010?
**Answer:** Intercontinental playoff
**Why it failed:** Wrong — 2010 was via CAF qualification (CAF play-off vs Egypt), not an intercontinental play-off. (The 2026 premise is correct — Group G winners.)
**Source:** [Wikipedia — 2010 WC qualification (CAF) third round](https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round)
**Remedy:** Change answer to "CAF qualification (play-off vs Egypt)"; rebuild distractors.

### Row 70 — Algeria (medium) — FAIL (false answer)
**Q:** Algeria won AFCON in 2019, but which World Cup year did they next qualify for?
**Answer:** 2022
**Why it failed:** Algeria did **not** qualify for 2022 (lost the playoff to Cameroon). The next World Cup they qualified for was **2026**.
**Source:** [FIFA — Algeria qualify (2026)](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/algeria-qualify), [ESPN — Algeria 1-2 Cameroon (2022 playoff)](https://www.espn.com/soccer/match/_/gameId/629214/cameroon-algeria)
**Remedy:** Change answer to **2026** (and update distractors/explanation). Note: 2026 is not currently an option.

### Row 75 — Algeria (medium) — FAIL (false answer; correct option present as distractor)
**Q:** Algeria won the 2019 AFCON, but which year did they next qualify for the FIFA World Cup?
**Answer:** 2022
**Why it failed:** Wrong — they failed to qualify for 2022; the correct answer is **2026**, which is listed among the distractors. The keyed answer and a distractor are effectively swapped.
**Source:** [FIFA — Algeria qualify (2026)](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/algeria-qualify), [ESPN — Algeria 1-2 Cameroon (2022 playoff)](https://www.espn.com/soccer/match/_/gameId/629214/cameroon-algeria)
**Remedy:** Set answer to **2026**; replace it as a distractor with a different wrong year; fix the explanation.

### Row 81 — Algeria (easy) — FAIL (explanation factually wrong)
**Q:** Algeria's 2010 World Cup playoff opponent was which nation?
**Answer:** Egypt
**Why it failed:** Answer "Egypt" is correct, but the explanation again mislabels the tie as an "intercontinental playoff" — it was a CAF qualifying play-off.
**Source:** [Wikipedia — 2010 WC qualification (CAF) third round](https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round)
**Remedy:** Keep "Egypt"; change explanation to "…in a CAF qualifying play-off."

### Row 82 — Algeria (easy) — FAIL (TC-03 multiple valid answers)
**Q:** Algeria's 2010 World Cup playoff win over Egypt contrasts with which 2022 CAF playoff winner?
**Answer:** Senegal
**Why it failed:** The 2022 CAF play-off winners were Senegal, Cameroon, Ghana, Morocco and Tunisia — so **all four options (Senegal, Morocco, Ghana, Cameroon) won 2022 CAF play-offs**. No unique answer.
**Source:** [Wikipedia — 2022 WC qualification (CAF) third round](https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_%E2%80%93_CAF_third_round)
**Remedy:** Drop, or replace the three distractors with teams that did NOT win a 2022 CAF play-off (e.g. Algeria, Egypt, Nigeria, DR Congo).

### Row 83 — Algeria (easy) — FAIL (explanation factually wrong)
**Q:** Algeria's 2010 World Cup spot came via a playoff against which nation?
**Answer:** Egypt
**Why it failed:** Answer correct; explanation again says "intercontinental playoff" (it was a CAF play-off).
**Source:** [Wikipedia — 2010 WC qualification (CAF) third round](https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round)
**Remedy:** Keep "Egypt"; fix explanation wording.

### Row 84 — Algeria (medium) — FAIL (explanation factually wrong)
**Q:** Algeria's 2014 World Cup qualification path differed from which other CAF nation's 2010 route?
**Answer:** Egypt
**Why it failed:** The explanation is wrong twice: Algeria reached 2014 via a two-legged **play-off** (vs Burkina Faso), not "directly"; and Egypt did **not** qualify in 2010 (they lost the play-off to Algeria), so "needed a playoff to qualify" misstates the outcome.
**Source:** [Wikipedia — 2014 WC qualification (CAF) third round](https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_CAF_third_round), [Wikipedia — 2010 WC qualification (CAF) third round](https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round)
**Remedy:** Drop or rewrite with accurate routes (Algeria 2014 via play-off vs Burkina Faso; Egypt 2010 lost the play-off and did not qualify).

### Row 86 — Algeria (hard) — FAIL (false claim)
**Q:** Algeria's 2019 AFCON win came after which World Cup qualification?
**Answer:** 2018 World Cup
**Why it failed:** The explanation states Algeria won the 2019 AFCON "after qualifying for the 2018 FIFA World Cup" — but Algeria did **not** qualify for 2018.
**Source:** [Wikipedia — 2018 FIFA World Cup qualification (CAF)](https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CAF))
**Remedy:** Reword to chronological adjacency ("the AFCON following the 2018 World Cup") with no qualification claim — i.e. make it match row 87.

### Row 88 — Algeria (easy) — FAIL (false claim)
**Q:** Algeria's 2019 AFCON win secured them a spot in which 2022 tournament?
**Answer:** The FIFA World Cup
**Why it failed:** Winning the AFCON does **not** grant a World Cup berth, and Algeria did not qualify for the 2022 World Cup. The premise and answer are both false.
**Source:** [ESPN — Algeria 1-2 Cameroon (2022 playoff)](https://www.espn.com/soccer/match/_/gameId/629214/cameroon-algeria)
**Remedy:** Drop — the cause-and-effect is fabricated.

### Row 89 — Algeria (easy) — FAIL (wrong answer)
**Q:** Algeria's 2019 AFCON win was its second. Which CAF nation won its second title first?
**Answer:** Ivory Coast
**Why it failed:** Ivory Coast's second title (2015) came **later** than the distractors': Egypt's 2nd was 1959, Cameroon's 1988, Nigeria's 1994. So Ivory Coast is the *last*, not "first," to win a second title, and the answer is not unique/ordered correctly.
**Source:** [Wikipedia — Africa Cup of Nations (titles by nation)](https://en.wikipedia.org/wiki/Africa_Cup_of_Nations)
**Remedy:** Drop or rewrite; if the intent is "earliest second title" among the options, the answer is Egypt (1959).

### Row 91 — Algeria (easy) — FAIL (false claim)
**Q:** Algeria's 2019 AFCON win was their second title, matching which nation's 2021 total?
**Answer:** Senegal
**Why it failed:** Senegal's 2021 AFCON was their **first** title — so after 2021 Senegal had one title, not two; it does not match Algeria's two.
**Source:** [Wikipedia — 2021 Africa Cup of Nations final (Senegal's first title)](https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final)
**Remedy:** Drop, or change to a nation that genuinely had two titles in 2021 (e.g. Nigeria already had 3 — none of the options fit cleanly); recommend removal.

### Row 92 — Algeria (easy) — FAIL (outdated/wrong)
**Q:** Algeria's 2019 AFCON win was their second title. Which nation also has two?
**Answer:** Ivory Coast
**Why it failed:** As of 2024 Ivory Coast has **three** AFCON titles (1992, 2015, 2023), so it no longer "has two." No option has exactly two.
**Source:** [Olympics.com — Côte d'Ivoire win 2023 AFCON](https://www.olympics.com/en/news/afcon-2023-final-cote-d-ivoire-beats-nigeria-to-capture-african-crown)
**Remedy:** Drop, or change the answer to a nation that currently has exactly two (e.g. DR Congo: 1968, 1974) and use it as the option.

### Row 93 — Algeria (medium) — FAIL (outdated/wrong)
**Q:** Algeria's 2019 AFCON win was their second title. Which other CAF nation has won exactly two AFCON titles?
**Answer:** Ivory Coast
**Why it failed:** Ivory Coast now has three titles (1992, 2015, 2023); the explanation ("twice, 1992 and 2015") is out of date.
**Source:** [Olympics.com — Côte d'Ivoire win 2023 AFCON](https://www.olympics.com/en/news/afcon-2023-final-cote-d-ivoire-beats-nigeria-to-capture-african-crown)
**Remedy:** Change answer to DR Congo (1968, 1974); update explanation.

### Row 94 — Algeria (easy) — FAIL (outdated/wrong)
**Q:** Algeria's 2019 AFCON win was their second. Which other CAF nation has two titles?
**Answer:** Ivory Coast
**Why it failed:** Same as rows 92/93 — Ivory Coast has three titles since 2023.
**Source:** [Olympics.com — Côte d'Ivoire win 2023 AFCON](https://www.olympics.com/en/news/afcon-2023-final-cote-d-ivoire-beats-nigeria-to-capture-african-crown)
**Remedy:** Change answer to a nation with exactly two (DR Congo).

### Row 95 — Algeria (hard) — FAIL (false answer)
**Q:** Algeria's 2019 AFCON win was their second. Which World Cup did they next qualify for?
**Answer:** 2022 FIFA World Cup
**Why it failed:** Algeria failed to qualify for 2022; the next World Cup they qualified for was **2026**.
**Source:** [FIFA — Algeria qualify (2026)](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/algeria-qualify)
**Remedy:** Change answer to **2026 FIFA World Cup**; rebuild distractors/explanation.

### Row 96 — Algeria (medium) — FAIL (wrong answer / contradictory wording)
**Q:** Algeria's 2019 AFCON win was their second. Which World Cup year was it before?
**Answer:** 2018
**Why it failed:** The 2019 AFCON came **before the 2022 World Cup**, not 2018 (2018 was earlier). The answer/explanation treat "before" as "after," contradicting the question. The correct "before" answer (2022) is even listed as a distractor.
**Source:** [Wikipedia — 2022 FIFA World Cup](https://en.wikipedia.org/wiki/2022_FIFA_World_Cup)
**Remedy:** If the question means the next WC, answer is **2022**; reword the stem for clarity and swap distractors.

### Row 97 — Algeria (easy) — FAIL (false premise/venue)
**Q:** Algeria's 64,000-seat primary stadium hosted which 2014 World Cup qualifier they won 1-0?
**Answer:** Burkina Faso
**Why it failed:** Opponent is right (Algeria 1-0 Burkina Faso, 19 Nov 2013), but the venue premise is wrong: the match was played in **Blida** (Stade Mustapha Tchaker, ~30k), decided by Bougherra — not the 64,000-seat Stade 5 Juillet 1962.
**Source:** [ESPN — Algeria 1-0 Burkina Faso, 19 Nov 2013 (Blida)](https://www.espn.com/soccer/match/_/gameId/381879/burkina-faso-algeria)
**Remedy:** Remove the stadium/capacity premise, or correct it to Stade Mustapha Tchaker (Blida).

### Row 121 — Algeria (easy) — FAIL (wrong answer)
**Q:** At the 2010 FIFA World Cup, Algeria finished in which group position?
**Answer:** Third place
**Why it failed:** Algeria finished **fourth/last** in Group C with one point (order: USA, England, Slovenia, Algeria) — not third.
**Source:** [Wikipedia — 2010 FIFA World Cup Group C](https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_Group_C)
**Remedy:** Change answer to **Fourth place** (and adjust the explanation, which also says "third").

### Row 125 — Algeria (medium) — FAIL (malformed / no correct option)
**Q:** At the 2010 World Cup, Algeria finished in which group stage position?
**Answer:** Group stage
**Why it failed:** The question asks for a *position*, but the keyed answer "Group stage" is a phase, not a position; and the only positional option offered ("Third place") is wrong — Algeria finished 4th. No option states the correct position.
**Source:** [Wikipedia — 2010 FIFA World Cup Group C](https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_Group_C)
**Remedy:** Reword to "…were eliminated at which stage?" (answer Group stage), or fix the options so "Fourth place" is the correct choice.

### Row 128 — Algeria (medium) — FAIL (TC-03 multiple valid answers)
**Q:** At the 2010 World Cup, which CAF team was eliminated in the group stage?
**Answer:** Algeria
**Why it failed:** At 2010 only Ghana advanced — Algeria, **Nigeria and Ivory Coast** (both distractors) and Cameroon all exited at the group stage. The answer is not unique.
**Source:** [Wikipedia — 2010 FIFA World Cup](https://en.wikipedia.org/wiki/2010_FIFA_World_Cup)
**Remedy:** Replace the distractors with CAF/other teams that advanced (e.g. Ghana) so only Algeria fits, or rephrase.

### Row 133 — Algeria (easy) — FAIL (false premise/detail)
**Q:** At the 2014 World Cup, which Algeria player scored an 88th-minute equalizer against Germany?
**Answer:** Abdelmoumene Djabou
**Why it failed:** Djabou did score Algeria's goal, but at **120'+1'** (a consolation in extra time), not an "88th-minute equalizer." The match was 0-0 after 90 minutes; Germany scored twice in extra time before Djabou pulled one back. No 88th-minute goal occurred, and it didn't "force extra time."
**Source:** [ESPN — Germany 2-1 Algeria, 30 Jun 2014](https://www.espn.com/soccer/match/_/gameId/383249/algeria-germany)
**Remedy:** Reword to "…scored Algeria's late consolation in extra time" (Djabou, 120'+1'); fix the explanation.

### Row 134 — Algeria (easy) — UNVERIFIED → FAIL
**Q:** At the 2014 World Cup, which Algerian Ligue 1 club did not have a player in Algeria's squad?
**Answer:** USM Alger
**Why it failed:** Could not verify. The 2014 squad was overwhelmingly Europe-based (only ~4 home-based players), and reliable sources don't confirm that MC Alger and JS Kabylie had squad players while USM Alger did not. A competitive quiz should not ship this unconfirmed.
**Source:** [Bleacher Report — Algeria 2014 squad guide](https://bleacherreport.com/articles/2060536-algeria-2014-fifa-world-cup-squad-player-by-player-guide) (does not substantiate the specific club claim)
**Remedy:** Hold for source confirmation of the exact domestic clubs represented; otherwise drop.

### Row 135 — Algeria (easy) — FAIL (wrong answer)
**Q:** At the 2014 World Cup, which Germany player scored against Algeria in the round of 16?
**Answer:** Thomas Müller
**Why it failed:** Müller did **not** score in that match (he assisted Schürrle's opener). Germany's scorers were **André Schürrle (92')** and **Mesut Özil (120')** — and Özil is one of the distractors, so the keyed answer is wrong while a distractor is correct.
**Source:** [ESPN — Germany 2-1 Algeria, 30 Jun 2014](https://www.espn.com/soccer/match/_/gameId/383249/algeria-germany)
**Remedy:** Change answer to **Mesut Özil** (or Schürrle, adding him as an option); replace the now-correct distractor.

### Row 159 — Algeria (easy) — FAIL (wrong by timeline)
**Q:** By the 2018 World Cup, which Algerian player was their all-time top scorer?
**Answer:** Islam Slimani
**Why it failed:** Slimani did not become Algeria's all-time top scorer until **8 Oct 2021**. At the 2018 World Cup the record was still held by **Abdelhafid Tasfaout** (36 goals, since 2002).
**Source:** [Goal — Slimani becomes Algeria's all-time top scorer (Oct 2021)](https://www.goal.com/en/news/2022-world-cup-qualifiers-slimani-becomes-algerias-all-time-top-scorer-as-mahrez-scores-brace-in-niger-thrashing/mhzszuy3ia4c1tzjra8pr7hfp)
**Remedy:** Change the anchor to "by the 2022 World Cup" (then Slimani is correct), or change the answer to Tasfaout for a 2018 framing.

### Row 167 — Algeria (easy) — FAIL (explanation factually wrong)
**Q:** How did Algeria reach the 2010 FIFA World Cup?
**Answer:** Beat Egypt in playoff
**Why it failed:** The answer is correct, but the explanation again calls it an "intercontinental playoff" — it was a **CAF qualifying play-off** (one-off, Khartoum, Algeria 1-0 Egypt).
**Source:** [Wikipedia — 2010 WC qualification (CAF) third round](https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round)
**Remedy:** Keep the answer; fix the explanation to "CAF qualifying play-off against Egypt."

### Row 181 — Algeria (medium) — FAIL (false fact)
**Q:** In 2014, Algeria lost 2-1 to Germany. Which other CAF team lost by the same score in the 2010 knockout stage?
**Answer:** Ghana
**Why it failed:** Ghana's 2010 quarter-final vs Uruguay finished **1-1** (Uruguay won 4-2 on penalties), not 2-1. Ghana was the only CAF team in the 2010 knockouts, so no CAF team lost 2-1 there — the question is unanswerable as posed.
**Source:** [FIFA — Uruguay 1-1 Ghana (4-2 pens)](https://www.fifa.com/en/tournaments/mens/worldcup/articles/uruguay-ghana-south-africa-2010)
**Remedy:** Drop — the premise (a CAF team losing 2-1 in the 2010 KO) is false.

### Row 182 — Algeria (easy) — UNVERIFIED → FAIL
**Q:** In 2022 WC qualifying, which Algerian top-flight club contributed players?
**Answer:** MC Alger
**Why it failed:** All four options are Algerian top-flight clubs, and no reliable source confirms MC Alger specifically supplied a player to the 2022-qualifying squad (which was overwhelmingly Europe-based). Ambiguous and unverified.
**Source:** none substantiating the specific club.
**Remedy:** Hold for source confirmation of the exact domestic clubs called up, or drop.

### Row 183 — Algeria (easy) — FAIL (TC-03 multiple valid answers)
**Q:** In 2026, which CAF nation qualified directly without a playoff?
**Answer:** Algeria
**Why it failed:** Egypt and Senegal (both distractors) also qualified directly as group winners for 2026; only Nigeria (the remaining option) went to the playoffs. The answer is not unique.
**Source:** [FIFA — Algeria qualify (2026, lists direct qualifiers)](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/algeria-qualify)
**Remedy:** Replace Egypt/Senegal distractors with CAF teams that did NOT qualify directly (e.g. Nigeria, DR Congo, Cameroon).

### Row 184 — Algeria (easy) — FAIL (false fact)
**Q:** In a 2014 World Cup group match, which Algerian club's player scored?
**Answer:** USM Alger
**Why it failed:** Algeria's 2014 scorers (Slimani, Halliche, Djabou, Brahimi vs South Korea) were all at foreign clubs; **Feghouli did not score** vs South Korea and was a Valencia player (only a USM Alger *youth* product). No USM Alger player scored.
**Source:** [ESPN — South Korea 2-4 Algeria (scorers)](https://www.espn.com/soccer/match/_/gameId/383274/algeria-south-korea)
**Remedy:** Drop — the premise that a domestic-club player scored is false; the 2014 squad was Europe-based.

### Row 190 — Algeria (medium) — FAIL (false detail)
**Q:** In Algeria's 2014 near-upset of Germany, which player's late equalizer forced extra time?
**Answer:** Abdelmoumene Djabou
**Why it failed:** Same error as row 133 — Djabou's goal was at **120'+1'** (a consolation), not an "88th-minute equalizer," and it did not force extra time (the match was 0-0 at 90').
**Source:** [ESPN — Germany 2-1 Algeria (goal times)](https://www.espn.com/soccer/match/_/gameId/383249/algeria-germany)
**Remedy:** Reword to "scored Algeria's stoppage-time consolation in extra time" (Djabou).

### Row 193 — Algeria (easy) — FAIL (false premise)
**Q:** In Algeria's 2022 FIFA World Cup group, which key modern attacker played?
**Answer:** Saïd Benrahma
**Why it failed:** Algeria did **not** qualify for the 2022 World Cup, so they had no 2022 World Cup group — the premise describes an event that did not happen.
**Source:** [ESPN — Algeria 1-2 Cameroon (2022 playoff)](https://www.espn.com/soccer/match/_/gameId/629214/cameroon-algeria)
**Remedy:** Re-anchor to "2022 World Cup qualifying" if the intent is the squad, or drop.

### Row 194 — Algeria (medium) — FAIL (false premise)
**Q:** In Algeria's 2022 World Cup group stage, which player was their primary attacking threat?
**Answer:** Riyad Mahrez
**Why it failed:** Same false premise — Algeria were not at the 2022 World Cup.
**Source:** [ESPN — Algeria 1-2 Cameroon (2022 playoff)](https://www.espn.com/soccer/match/_/gameId/629214/cameroon-algeria)
**Remedy:** Re-anchor to the qualifying campaign, or drop.

### Row 205 — Algeria (medium) — UNVERIFIED → FAIL
**Q:** In their 2022 World Cup qualifier group, how many Algerian starters were also 2014 World Cup starters?
**Answer:** Two or three
**Why it failed:** Not verifiable, and likely an undercount — Mahrez, Slimani, Feghouli, Brahimi and M'Bolhi all featured in both eras. No source supports the precise "two or three."
**Source:** none confirming the count.
**Remedy:** Hold for source confirmation, or drop (soft, unverifiable count).

### Row 215 — Algeria (easy) — FAIL (false premise / wrong answer)
**Q:** In which 2022 FIFA World Cup qualifier did Algeria's Saïd Benrahma make his senior debut?
**Answer:** Against Zambia
**Why it failed:** Benrahma made his Algeria debut against **Senegal on 13 Oct 2015** (as a substitute), not in a 2022 World Cup qualifier — and Algeria never played Zambia in 2022 WC qualifying (their group was Burkina Faso, Niger, Djibouti).
**Source:** [Wikipedia — Saïd Benrahma](https://en.wikipedia.org/wiki/Sa%C3%AFd_Benrahma)
**Remedy:** Drop — the premise (a 2022 WCQ debut vs Zambia) is false; if rewritten, the debut was 2015 vs Senegal.
