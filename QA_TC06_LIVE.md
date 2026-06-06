# QA — TC-06 Live Factual Check (web-sourced, one-by-one)

Per-row factual verification of `answer` + `explanation` against live web sources
(Wikipedia / FIFA as tie-breaker, plus ESPN, Al Jazeera, CAF, etc.). Processed in
dataset order; **resumable** — the "Last verified row" marker below is the cursor.

- **PASS** = answer and explanation both factually correct per a cited source.
- **FAIL** = answer wrong, explanation wrong, or the question asserts an event that
  did not happen.
- **UNVERIFIED** = could not confirm from reliable sources → treated as FAIL
  (conservative; a competitive quiz must not ship unverified facts).

**Last verified row: 810**  (resume from row 811)

Running totals (rows 2–230, old method — every row checked): **181 PASS / 48 FAIL**.

> **METHOD CHANGE from row 231 onward (per user, this session):**
> Only run the liveness check on rows that are in **`QA_PASSED.md`** (mechanically/
> heuristically passed). Skip rows in `QA_FAILED.md`. Route verdicts to the two new files:
> - PASS (passed mechanical AND liveness) → **`QA_PASSED_ALL.md`**
> - FAIL liveness (but passed mechanical) → **`QA_FAILED_LIVENESS_PASSED_OTHERS.md`**
> Of rows 231–1228, **730** are in `QA_PASSED.md` and need checking (~268 are skipped).
> Keep advancing the cursor below and keep the per-batch tables here.

---

### Row 2 — Algeria (medium) — ✅ PASS
**Q:** After 2014, which two World Cups did Algeria fail to qualify for?
**Answer:** 2018 and 2022
**Verdict:** Correct. Algeria reached 2014, then failed to qualify for both 2018 and 2022 (lost the 2022 CAF playoff to Cameroon 2–1, agg 2–2 on away goals).
**Source:** [ESPN — Algeria 1-2 Cameroon, 29 Mar 2022](https://www.espn.com/soccer/match/_/gameId/629214/cameroon-algeria), [Xinhua — Algeria fail to reach 2022 World Cup](https://english.news.cn/20220330/379de2e8ddb04d0793ea2fd307ee88cf/c.html)

### Row 3 — Algeria (medium) — ❌ FAIL
**Q:** After Algeria's 2018 AFCON win, which World Cup did Djamel Belmadi coach them at?
**Answer:** 2022 World Cup
**Verdict:** False on two counts. (1) There was no "2018 AFCON" — Algeria's title was the **2019** AFCON (AFCON editions are 2017, 2019). (2) Belmadi did not coach Algeria *at* a World Cup: they **failed to qualify** for 2022. The premise asserts an event that did not happen.
**Source:** [Wikipedia — 2019 AFCON final](https://en.wikipedia.org/wiki/2019_Africa_Cup_of_Nations_final), [ESPN — Algeria 1-2 Cameroon (2022 playoff)](https://www.espn.com/soccer/match/_/gameId/629214/cameroon-algeria)
**Remedy:** Re-anchor to a real event, e.g. "Which AFCON did Djamel Belmadi win with Algeria?" → **2019**; or drop.

### Row 4 — Algeria (medium) — ❌ FAIL (answer right, explanation wrong)
**Q:** After Algeria's 2019 AFCON win, how many FIFA World Cups have they qualified for since?
**Answer:** One
**Verdict:** The **answer "One" is correct** — since 2019 Algeria failed to qualify for 2022 but **qualified for 2026** (Group G winners). However, the stored **explanation is false** ("Algeria qualified for the 2022 FIFA World Cup after winning the 2019 AFCON") — they did not qualify for 2022. Wrong explanation = TC-06 fail.
**Source:** [FIFA — Algeria qualify (2026)](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/algeria-qualify), [ESPN — 2022 playoff loss](https://www.espn.com/soccer/match/_/gameId/629214/cameroon-algeria)
**Remedy:** Keep answer "One"; rewrite explanation: "Algeria failed to qualify for 2022 but qualified for the 2026 World Cup — one since their 2019 AFCON title."

### Row 5 — Algeria (medium) — ⚠️ UNVERIFIED → FAIL
**Q:** After Algeria's 2019 AFCON win, when did their squad rebuild start?
**Answer:** 2019
**Verdict:** "Squad rebuild started 2019" is a soft, narrative claim with no authoritative source; the explanation is also self-referential ("The verified fact states…"). Cannot confirm.
**Source:** none located.
**Remedy:** Hold for source confirmation, or drop — not a crisp, verifiable fact.

### Row 6 — Algeria (medium) — ❌ FAIL
**Q:** After Algeria's 2019 AFCON win, when did their World Cup squad rebuild begin?
**Answer:** After 2022 qualification
**Verdict:** The answer phrase "After 2022 qualification" implies Algeria qualified for 2022, which is false (they failed). The explanation itself says the rebuild followed their **failure** to qualify — contradicting the answer's wording. Misleading/contradictory and the underlying "rebuild date" is unverifiable.
**Source:** [ESPN — 2022 playoff loss](https://www.espn.com/soccer/match/_/gameId/629214/cameroon-algeria)
**Remedy:** Drop, or rephrase answer to "After failing to qualify for 2022" with a sourced date — currently unverifiable.

### Row 7 — Algeria (easy) — ✅ PASS
**Q:** After Algeria's 2019 AFCON win, which manager led their 2022 World Cup qualifying campaign?
**Answer:** Djamel Belmadi
**Verdict:** Correct. Belmadi managed Algeria through the 2022 qualifying campaign and the playoff loss to Cameroon.
**Source:** [Al Jazeera — Algerian FA complaint (Belmadi's side, 2022 qualifier)](https://www.aljazeera.com/news/2022/3/31/algerian-fa-complaint-fifa-qatar-2022-world-cup-qualifier-cameroon)
**Note:** Still carries GEN-7 (self-referential explanation) in the mechanical report.

### Row 8 — Algeria (hard) — ❌ FAIL
**Q:** After Algeria's 2019 AFCON win, which World Cup did they qualify for?
**Answer:** 2022 FIFA World Cup
**Verdict:** Wrong. Algeria did **not** qualify for 2022. The first World Cup they qualified for after the 2019 AFCON was **2026**.
**Source:** [FIFA — Algeria qualify (2026)](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/algeria-qualify), [ESPN — 2022 playoff loss](https://www.espn.com/soccer/match/_/gameId/629214/cameroon-algeria)
**Remedy:** Change answer to **2026 FIFA World Cup**; adjust distractors (e.g. 2018, 2014, 2010 World Cup) and fix the explanation.

### Row 9 — Algeria (easy) — ✅ PASS
**Q:** After Algeria's 2019 AFCON win, who led their squad rebuild for 2022 World Cup qualifying?
**Answer:** Djamel Belmadi
**Verdict:** Correct — Belmadi was Algeria's manager throughout the 2022 qualifying cycle.
**Source:** [Wikipedia — 2019 AFCON final (Belmadi as coach)](https://en.wikipedia.org/wiki/2019_Africa_Cup_of_Nations_final)

### Row 10 — Algeria (medium) — ⚠️ UNVERIFIED → FAIL
**Q:** After Algeria's 2021 AFCON group stage exit, which other defending champion also failed to advance?
**Answer:** Algeria
**Verdict:** The answer "Algeria" is the same nation the question is about, so it cannot be the "other" team — internally broken. (Separately, the 2021 AFCON was played in Jan 2022 and Algeria, the defending champion, did exit in the group stage — but the question asks for *another* defending champion, which is incoherent here.)
**Source:** [Wikipedia — 2019 AFCON final (Algeria = defending champion)](https://en.wikipedia.org/wiki/2019_Africa_Cup_of_Nations_final)
**Remedy:** Drop — the answer restates the subject; question is logically broken.

---

## Batch rows 11–30 (Algeria) — fact base built from sources

Fact base verified this batch: 2010 WC (Algeria last in Group C, 0-0 vs England,
lost to Slovenia & USA, group-stage exit); 2014 WC (lost 2-1 to Germany AET in R16);
2019 AFCON (beat Senegal 1-0, Algeria's 2nd title, first since 1990); 2022 qualifiers
(Burkina Faso 1-1 Algeria on 7 Sep 2021 — Feghouli scored; Algeria 2-2 Burkina Faso on
16 Nov 2021 — Mahrez scored). Sources cited per row in the passed/failed files.

| Row | Verdict | Note |
|----:|:-------:|------|
| 11 | ✅ PASS | 2022 was the next WC qualification cycle after 2019 AFCON |
| 12 | ✅ PASS | 2022 = first WC the post-2019 squad attempted |
| 13 | ✅ PASS | 2019 Africa Cup of Nations |
| 14 | ✅ PASS | 2019 AFCON |
| 15 | ✅ PASS | 2019 AFCON (near-dup of 14, see mechanical TC-01) |
| 16 | ✅ PASS | 2019 AFCON |
| 17 | ✅ PASS | Two continental titles (1990, 2019) |
| 18 | ❌ FAIL | scorer of the 1-1 BF draw was **Feghouli**, not Mahrez |
| 19 | ✅ PASS | 1-0 vs Senegal |
| 20 | ✅ PASS | 2019 |
| 21 | ✅ PASS | lost 2-1 to Germany, 2014 R16 |
| 22 | ✅ PASS | Germany |
| 23 | ✅ PASS | 2019 |
| 24 | ✅ PASS | beat Senegal |
| 25 | ✅ PASS | Senegal |
| 26 | ✅ PASS | Senegal |
| 27 | ✅ PASS | Senegal |
| 28 | ✅ PASS | 0-0 vs England, 2010 |
| 29 | ✅ PASS | group-stage exit (also TC-04 coherence fail in mechanical report) |
| 30 | ✅ PASS | group-stage exit (also TC-04 coherence fail in mechanical report) |

---

## Batch rows 31–55 (Algeria)

Fact base added: 2021 AFCON (Algeria bottom of Group E, group-stage exit as holders);
2014 R16 scorelines (Ger 2-1 Alg, Ned 2-1 Mex, Fra 2-0 Nga, Bel 2-1 USA); 2010
qualification (CAF play-off vs Egypt 1-0 in Khartoum — a CAF tie, **not** intercontinental);
2014 CAF qualifiers all via two-legged play-offs (Algeria, Cameroon, Ghana, Ivory Coast,
Nigeria). Sources per row in passed/failed files.

| Row | Verdict | Note |
|----:|:-------:|------|
| 31 | ✅ PASS | 2010 group-stage exit (also TC-04 malformed) |
| 32 | ✅ PASS | 2010 group-stage exit (also TC-04 malformed) |
| 33 | ✅ PASS | exited 2021 AFCON as defending champions |
| 34 | ✅ PASS | 2021 AFCON group stage |
| 35 | ✅ PASS | 2021 AFCON group stage |
| 36 | ✅ PASS | 2021 AFCON group stage |
| 37 | ❌ FAIL | non-unique: Algeria played none of Brazil/France/Argentina/Netherlands in 2014 KO |
| 38 | ✅ PASS | missed 2018 & 2022 |
| 39 | ✅ PASS | Belmadi hired 2018 |
| 40 | ✅ PASS | also lost to USA (0-1) in 2010 |
| 41 | ❌ FAIL | non-unique: Cameroon (1990 v England) etc. also lost KO to European side |
| 42 | ❌ FAIL | non-unique: Mexico also lost 2014 KO 2-1 (Ned 2-1 Mex) |
| 43 | ✅ PASS | Germany |
| 44 | ✅ PASS | Germany |
| 45 | ✅ PASS | Germany |
| 46 | ✅ PASS | Germany |
| 47 | ✅ PASS | Germany |
| 48 | ✅ PASS | Italy also missed 2018 & 2022 (unique among options) |
| 49 | ✅ PASS | 2018 & 2022 |
| 50 | ✅ PASS | 2018 & 2022 |
| 51 | ✅ PASS | 2018 & 2022 |
| 52 | ✅ PASS | Round of 16 |
| 53 | ❌ FAIL | explanation mislabels the CAF play-off as "intercontinental" |
| 54 | ❌ FAIL | non-unique: Ghana & Nigeria also qualified for 2014; nobody "directly" |
| 55 | ❌ FAIL | answer "intercontinental playoff" wrong — it was a CAF play-off |

---

## Batch rows 56–80 (Algeria)

Fact base added/reused: 2019 AFCON final winning goal = **Baghdad Bounedjah** (2nd min,
deflected off Salif Sané); 2026 qualification = **CAF Group G** winners; 2010 = 1 point
group exit; 2014 = R16; 2021 AFCON group exit. Sources per row in passed/failed files.

| Row | Verdict | Note |
|----:|:-------:|------|
| 56 | ✅ PASS | CAF qualification (Algeria is CAF) |
| 57 | ❌ FAIL | "intercontinental playoff vs Egypt" wrong — it was a CAF play-off |
| 58 | ❌ FAIL | "intercontinental playoff" wrong — CAF play-off |
| 59 | ✅ PASS | 2026 via CAF Group G |
| 60 | ✅ PASS | 2026 via CAF Group G (near-dup of 59) |
| 61 | ✅ PASS | next knockout after 2010 was 2014 |
| 62 | ✅ PASS | 2021 AFCON group stage |
| 63 | ✅ PASS | 2021 AFCON (as holders) |
| 64 | ✅ PASS | 2021 AFCON |
| 65 | ✅ PASS | 1-0 |
| 66 | ✅ PASS | 1-0, Bounedjah goal |
| 67 | ✅ PASS | 1-0 |
| 68 | ✅ PASS | one point at 2021 AFCON |
| 69 | ✅ PASS | Algeria eliminated 2021 group (unique among options) |
| 70 | ❌ FAIL | "next qualified for 2022" — false, did not qualify (next was 2026) |
| 71 | ✅ PASS | 2nd AFCON title = 2019 (1st was 1990) |
| 72 | ✅ PASS | 2019 |
| 73 | ✅ PASS | decisive goal: Bounedjah |
| 74 | ✅ PASS | nearly beat Germany, 2014 |
| 75 | ❌ FAIL | "next qualified for 2022" — false; 2026 (listed as a distractor) is correct |
| 76 | ✅ PASS | next group-stage exit = 2021 AFCON |
| 77 | ✅ PASS | 2022 WC chronologically followed the 2019 AFCON (no qualification claim) |
| 78 | ✅ PASS | 2021 AFCON group stage |
| 79 | ✅ PASS | 2010 group exit worse than 2014 R16 |
| 80 | ✅ PASS | one point in 2010 group |

---

## Batch rows 81–105 (Algeria) — high contamination

Fact base added: **Ivory Coast now has 3 AFCON titles** (1992, 2015, **2023**) — so
"Ivory Coast has two" is outdated; 2022 CAF play-off winners = Senegal, Cameroon, Ghana,
Morocco, Tunisia (all four of row 82's options won); Algeria 1-0 Burkina Faso (19 Nov 2013)
was in **Blida** (Bougherra), not the 5 Juillet stadium; Senegal's 1st AFCON title was 2021
(so 1 title, not 2). Sources per row in passed/failed files.

| Row | Verdict | Note |
|----:|:-------:|------|
| 81 | ❌ FAIL | explanation calls the Egypt tie "intercontinental" (it was CAF) |
| 82 | ❌ FAIL | non-unique: Senegal, Morocco, Ghana, Cameroon all won 2022 CAF play-offs |
| 83 | ❌ FAIL | explanation "intercontinental playoff" wrong |
| 84 | ❌ FAIL | explanation errors (Algeria not "direct" in 2014; Egypt didn't qualify 2010) |
| 85 | ✅ PASS | 1-0 |
| 86 | ❌ FAIL | explanation claims Algeria qualified for 2018 — false |
| 87 | ✅ PASS | 2018 WC chronologically preceded the 2019 AFCON (no qualification claim) |
| 88 | ❌ FAIL | AFCON win did not secure a 2022 WC spot — false |
| 89 | ❌ FAIL | Ivory Coast not "first" to win 2nd title; Egypt/Cameroon/Nigeria earlier |
| 90 | ✅ PASS | Belmadi |
| 91 | ❌ FAIL | Senegal had ONE title after 2021 (their first), not two |
| 92 | ❌ FAIL | Ivory Coast now has 3 titles, not two |
| 93 | ❌ FAIL | Ivory Coast now has 3 titles |
| 94 | ❌ FAIL | Ivory Coast now has 3 titles |
| 95 | ❌ FAIL | next WC was 2026, not 2022 |
| 96 | ❌ FAIL | 2019 AFCON was before the 2022 WC, not 2018; wording/answer contradict |
| 97 | ❌ FAIL | venue wrong — the 1-0 BF win was in Blida, not the 64k 5 Juillet |
| 98 | ✅ PASS | Bounedjah, 2nd minute |
| 99 | ✅ PASS | R16 best finish |
| 100 | ✅ PASS | 2014 best result |
| 101 | ✅ PASS | Belmadi won 2019 |
| 102 | ✅ PASS | 5 Juillet ≈ 64,000 capacity (difficulty blank → TC-08 in mechanical) |
| 103 | ✅ PASS | correctly says Algeria MISSED 2022 |
| 104 | ✅ PASS | 2019 (explanation has GEN-7 self-reference in mechanical report) |
| 105 | ✅ PASS | 1990→2019 = 29 years |

---

## Batch rows 106–130 (Algeria)

Fact base added: Slimani = Algeria's joint-top 2014 WC scorer (2 goals, incl. decisive
Russia equalizer); 2010 WC Group C final order USA, England, Slovenia, **Algeria 4th/last**
(1 pt); at 2010 only Ghana advanced — Algeria, Nigeria, Ivory Coast, Cameroon all
group-exited. Sources per row in passed/failed files.

| Row | Verdict | Note |
|----:|:-------:|------|
| 106–109 | ✅ PASS | 2010 group exit / 2014 R16 |
| 110,113,114 | ✅ PASS | Slimani key 2014 goals (joint-top scorer) |
| 111 | ✅ PASS | Algeria reached R16 (unique among options) |
| 112 | ✅ PASS | Germany |
| 115,118 | ✅ PASS | Bounedjah scored the 2019 final winner |
| 116,117,119 | ✅ PASS | Mahrez starred (only Algerian among options) |
| 120 | ✅ PASS | 2021 AFCON group stage |
| 121 | ❌ FAIL | "third place" wrong — Algeria finished 4th/last in Group C |
| 122,123 | ✅ PASS | 2010 group-stage exit |
| 124 | ✅ PASS | Ghana advanced (only CAF team, unique) |
| 125 | ❌ FAIL | malformed: asks "position", answer "Group stage" isn't one; correct (4th) not offered |
| 126,127 | ✅ PASS | 2010 group stage |
| 128 | ❌ FAIL | non-unique: Nigeria & Ivory Coast also group-exited 2010 |
| 129 | ✅ PASS | 2010 group stage |
| 130 | ✅ PASS | USA beat Algeria 1-0 to eliminate them |

---

## Batch rows 131–155 (Algeria)

Fact base added: 2014 Ger 2-1 Alg goal detail — **Schürrle 92', Özil 120', Djabou 120+1'**
(Müller did NOT score; no 88th-min equalizer; match 0-0 at 90'); venue Estádio Beira-Rio,
Porto Alegre; Halilhodžić = 2014 coach; 2014 squad mostly Europe-based (~4 home-based).
Sources per row in passed/failed files.

| Row | Verdict | Note |
|----:|:-------:|------|
| 131,138,139 | ✅ PASS | Germany / nearly beat Germany, 2014 R16 |
| 132 | ✅ PASS | Mahrez (2014 WC + 2019 AFCON captain) |
| 133 | ❌ FAIL | Djabou's goal was 120+1' (consolation), not an 88th-min equalizer |
| 134 | ⚠️ FAIL | UNVERIFIED — can't confirm which domestic club had/lacked a 2014 squad player |
| 135 | ❌ FAIL | Müller did not score vs Algeria; Schürrle & Özil did (Özil is a distractor) |
| 136 | ✅ PASS | Algeria reached R16 (unique among options) |
| 137,152,153 | ✅ PASS | Halilhodžić managed Algeria at 2014 |
| 140 | ✅ PASS | Bounedjah winner vs Senegal |
| 141 | ✅ PASS | poor form after 2021 AFCON group exit (anchored) |
| 142,144 | ✅ PASS | rebuild after 2019 AFCON (dataset narrative, anchored) |
| 143 | ✅ PASS | two AFCON titles |
| 145 | ✅ PASS | Mahrez = star attacker |
| 146 | ✅ PASS | Algeria won 2nd title in 2019 (unique) |
| 147 | ✅ PASS | failed 2022 — lost to Cameroon |
| 148,149 | ✅ PASS | venue Estádio Beira-Rio, Porto Alegre |
| 150 | ✅ PASS | best result 2014 |
| 151,155 | ✅ PASS | Slimani key goals 2014 |
| 154 | ✅ PASS | group-stage exit 2010 |

---

## Batch rows 156–180 (Algeria)

Fact base added: **Slimani became Algeria's all-time top scorer on 8 Oct 2021** (surpassed
Tasfaout's 36; held since 2002) — so "by 2018" is false, "by 2022" is true; Mahrez won the
2016 PL with Leicester; Belmadi appointed 2018; Mahrez has 0 World Cup goals (only 2014).
Sources per row in passed/failed files.

| Row | Verdict | Note |
|----:|:-------:|------|
| 156 | ✅ PASS | Halilhodžić = 2014 |
| 157 | ✅ PASS | Mahrez won 2016 PL with Leicester |
| 158 | ✅ PASS | Belmadi appointed 2018 |
| 159 | ❌ FAIL | Slimani was NOT all-time top scorer by 2018 (Tasfaout still held it) |
| 160 | ✅ PASS | Slimani top scorer by 2022 (since Oct 2021) |
| 161 | ✅ PASS | 2019 AFCON goal after the 2014 Germany near-miss |
| 162 | ✅ PASS | 5 Juillet ≈64,000 (difficulty blank → TC-08) |
| 163,164 | ✅ PASS | failed 2018 & 2022 (two consecutive) |
| 165,166,168,169,170,171 | ✅ PASS | 2014/2026 via CAF qualification |
| 167 | ❌ FAIL | answer ok but explanation says "intercontinental playoff" (it was CAF) |
| 172,174 | ✅ PASS | one AFCON title before 2019 |
| 173,175,176,177 | ✅ PASS | two AFCON titles by 2019/2022/2024 |
| 178,179 | ✅ PASS | Bounedjah scored in the 2nd minute |
| 180 | ✅ PASS | Mahrez has 0 World Cup goals |

---

## Batch rows 181–205 (Algeria)

Fact base added: Ghana–Uruguay 2010 QF was **1-1 (Uruguay won on pens)**, not 2-1; 2014
Algeria 4-2 South Korea scorers = Slimani, Halliche, Djabou, Brahimi (**Feghouli did NOT
score**); Algeria did **not** play at the 2022 WC (no group); 2026 CAF direct qualifiers
include Algeria, Egypt and Senegal (Nigeria went to playoffs). Sources per row in passed/
failed files.

| Row | Verdict | Note |
|----:|:-------:|------|
| 181 | ❌ FAIL | Ghana lost 1-1 (pens) to Uruguay in 2010, not "2-1"; no CAF team lost 2-1 in 2010 KO |
| 182 | ⚠️ FAIL | UNVERIFIED — can't confirm MC Alger specifically supplied a 2022-qualifying player |
| 183 | ❌ FAIL | non-unique: Egypt & Senegal also qualified directly for 2026 |
| 184 | ❌ FAIL | no USM Alger player scored; Feghouli didn't score vs S.Korea & was at Valencia |
| 185 | ✅ PASS | 2016 (Mahrez PL); Algeria did beat S.Korea 4-2 |
| 186,188 | ✅ PASS | 5 Juillet ≈64,000 (difficulty blank → TC-08) |
| 187 | ✅ PASS | Bounedjah opening goal |
| 189 | ✅ PASS | Mahrez (only Leicester winner in Algeria's match) |
| 190 | ❌ FAIL | Djabou's goal was 120+1', not an 88th-min equalizer (same error as row 133) |
| 191,192 | ✅ PASS | Bounedjah, 2nd minute / only goal |
| 193 | ❌ FAIL | false premise — Algeria had no 2022 World Cup group (didn't qualify) |
| 194 | ❌ FAIL | false premise — no 2022 World Cup group |
| 195 | ✅ PASS | Belmadi led 2022 *qualifying* |
| 196 | ✅ PASS | 2-1 to Germany |
| 197 | ✅ PASS | drew Russia 1-1 |
| 198 | ✅ PASS | Germany |
| 199,200,203,204 | ✅ PASS | 2019 final: Algeria beat Senegal 1-0 |
| 201,202 | ✅ PASS | Bounedjah 2nd minute |
| 205 | ⚠️ FAIL | UNVERIFIED — "two or three" 2014→2022 starters; likely undercount, unconfirmed |

---

## Batch rows 206–230 (Algeria)

Fact base added: Algeria sealed 2026 qualification on **9 Oct 2025** (3-0 v Somalia, Oran;
Amoura 2, Mahrez); Mahrez's only WC was 2014 (his WC debut); **Benrahma debuted for Algeria
v Senegal on 13 Oct 2015** (not a 2022 qualifier v Zambia). Sources per row in passed/failed.

| Row | Verdict | Note |
|----:|:-------:|------|
| 206 | ✅ PASS | 2026 via CAF |
| 207,213 | ✅ PASS | Belmadi appointed 2018 |
| 208,210,211 | ✅ PASS | 2019 AFCON final vs Senegal |
| 209 | ✅ PASS | qualified 2026 in 2025 (9 Oct 2025) |
| 212 | ✅ PASS | Mahrez 2016 PL |
| 214,225 | ✅ PASS | Bounedjah early goal, 2019 AFCON final |
| 215 | ❌ FAIL | Benrahma debuted v Senegal in 2015, not a 2022 WCQ v Zambia (no such match) |
| 216,217,224 | ✅ PASS | 2021 AFCON group exit as holders |
| 218,227 | ✅ PASS | best result 2014 |
| 219,220,221 | ✅ PASS | Mahrez WC debut 2014 |
| 222 | ✅ PASS | Halilhodžić 2014 |
| 223 | ✅ PASS | Bounedjah 2nd minute |
| 226 | ✅ PASS | failed 2018 & 2022 |
| 228 | ✅ PASS | advanced past group only in 2014 |
| 229 | ✅ PASS | finished last in group in 2010 |
| 230 | ✅ PASS | lost 2-1 to Germany, 2014 |

---

## Batch rows 231–275 (Algeria) — NEW METHOD (only QA_PASSED.md rows)

44 candidates (rows 231–275 present in QA_PASSED.md; 259 was not in the passed pool, skipped).
Adjudicated against the established Algeria fact base — no new searches required.
**Result: 37 PASS → QA_PASSED_ALL.md · 7 FAIL → QA_FAILED_LIVENESS_PASSED_OTHERS.md.**

| Row | Verdict | Note |
|----:|:-------:|------|
| 231,232,233,234,240,241,248,272 | ✅ PASS | 2014 R16 / 2-1 loss to Germany |
| 235 | ✅ PASS | Slimani scored key goals at 2014 WC |
| 236,237,266 | ✅ PASS | Mahrez WC/senior debut 2014 |
| 238 | ✅ PASS | eliminated Group C, 2010 |
| 239 | ✅ PASS | Slimani top scorer in 2022 WCQ cycle (8 Oct 2021) |
| 242 | ❌ FAIL | "intercontinental playoff" — was a CAF play-off vs Egypt |
| 243 | ❌ FAIL | record-breaker was 37th goal (passed Tasfaout 36), not 41st |
| 244 | ❌ FAIL | wrong answer — Mahrez WC debut 2014, not 2018 |
| 245 | ❌ FAIL | "intercontinental playoff" — CAF play-off vs Egypt (2009) |
| 246 | ❌ FAIL | wrong answer — qualified 2026 in Oct **2025**; 2025 not an option |
| 247 | ❌ FAIL | false premise — 2014 squad Europe-based, not "MC Alger/Ligue 1" |
| 249,250,251,252,253,254,255,256,257,258,260 | ✅ PASS | 2019 AFCON (1-0 v Senegal, Belmadi) |
| 261,262 | ✅ PASS | Bounedjah 2nd-minute final goal, 2019 |
| 263,269,270 | ✅ PASS | Mahrez key to 2019 AFCON |
| 264,265,271 | ✅ PASS | Mahrez 2016 Premier League |
| 267,268 | ✅ PASS | Belmadi appointed 2018 |
| 273 | ✅ PASS | qualified 2014 via CAF |
| 274 | ✅ PASS | Halilhodžić, 2014 knockout stage |
| 275 | ❌ FAIL | explanation "directly" — 2014 via CAF play-off vs Burkina Faso; misleading 2010 framing |

**Running totals (new method, rows 231+):** 37 PASS-ALL · 7 FAIL-LIVENESS.

---

## Batch rows 276–320 (Algeria) — NEW METHOD (only QA_PASSED.md rows)

30 candidates (rows in QA_PASSED.md within 276–320). All scoreline/result questions covered
by the Algeria fact base — no new searches. **Result: 29 PASS · 1 FAIL.**

| Row | Verdict | Note |
|----:|:-------:|------|
| 279,289,291,292,299,301,302,303,304,305,310,311,316,320 | ✅ PASS | 2019 AFCON final, Algeria 1-0 Senegal |
| 280,281,282,283,284,285,318 | ✅ PASS | best-ever WC result = Round of 16 (2014) |
| 287,294,297,307,308,309,315 | ✅ PASS | 2014 R16, lost 2-1 to Germany (a.e.t.) |
| 319 | ✅ PASS | Belmadi appointed 2018 (distractors have stray &nbsp;) |
| 314 | ❌ FAIL | answer "02-Jan" = corrupted "2-1" scoreline (Excel date mangling) |

**Running totals (new method, rows 231+):** 66 PASS-ALL · 8 FAIL-LIVENESS.

---

## Batch rows 321–385 (Algeria) — NEW METHOD (only QA_PASSED.md rows)

56 candidates. Mostly fact-base coverage; one web check (Benrahma WCQ debut → 2021, confirmed).
**Result: 48 PASS · 8 FAIL.**

| Row | Verdict | Note |
|----:|:-------:|------|
| 321,322,342,344,345,346,347,348,350,351,352,354,356,362,364,371,372,376,377,383 | ✅ PASS | 2019 AFCON (1-0 v Senegal; Bounedjah 2'; Mahrez) |
| 332,334,335,340,341,359,360,366,368,378,384,385 | ✅ PASS | 2014 R16 / 2-1 to Germany / Slimani goals / Halilhodžić |
| 324,379,381,382 | ✅ PASS | 2010 group-stage exit |
| 326,327,328,329,380 | ✅ PASS | 2021 AFCON group-stage exit as holders |
| 330,331,333 | ✅ PASS | failed to qualify 2018 & 2022 |
| 337 | ✅ PASS | 2014 qualification secured 2013 (correct) |
| 353,373 | ✅ PASS | Belmadi appointed 2018 |
| 370 | ✅ PASS | Benrahma WC-qualifying debut 2021 (verified) |
| 336,338 | ❌ FAIL | "qualify for 2014 WC → 2014"; sealed Nov 2013 (cf. row 337) |
| 339,363 | ❌ FAIL | "qualify for 2026 WC → 2026"; sealed Oct 2025 |
| 358 | ❌ FAIL | record broken *during* 2022 qualifiers (8 Oct 2021), not before |
| 365,367,369 | ❌ FAIL | unverifiable "squad rebuild" narrative |

**Running totals (new method, rows 231+):** 114 PASS-ALL · 16 FAIL-LIVENESS.

---

## Batch rows 386–460 (Algeria) — NEW METHOD (only QA_PASSED.md rows)

48 candidates. High fail rate — this range is mostly a flawed generated "Which Algeria
attacker…" template. **Result: 31 PASS · 17 FAIL.**

| Row | Verdict | Note |
|----:|:-------:|------|
| 387,419,420,421,429,437,449,451,452,453,458,459 | ✅ PASS | 2019 AFCON (beat Senegal 1-0; Bounedjah; Mahrez capt.; Belmadi) |
| 389,390,391,415 | ✅ PASS | 2021 AFCON group exit as holders |
| 392 | ✅ PASS | 2010 group-stage exit |
| 394,395,397,398,401,427,454,455,456,460 | ✅ PASS | 2014 R16 / Germany / Halilhodžić |
| 445,446,450,457 | ✅ PASS | Mahrez (Man City/2022 WCQ star) / Belmadi |
| 430,434,441,442,447 | ❌ FAIL | false premise — Algeria not at 2022 WC (no squad, didn't play) |
| 433,438,439,440,443 | ❌ FAIL | non-unique — "key modern attacker" fits Mahrez ≥ Benrahma |
| 435,436 | ❌ FAIL | non-unique — Slimani also fits the caps/goals description |
| 428,448 | ❌ FAIL | non-unique — multiple Algeria players satisfy |
| 396 | ❌ FAIL | non-unique (France also not faced) + wrong explanation |
| 417 | ❌ FAIL | wrong answer — Halilhodžić DID manage Ivory Coast |
| 423 | ❌ FAIL | self-referential answer ("Algeria matched Algeria") |

**Running totals (new method, rows 231+):** 145 PASS-ALL · 33 FAIL-LIVENESS.

---

## Batch rows 461–540 (Algeria) — NEW METHOD (only QA_PASSED.md rows)

63 candidates — mostly coach/player-identity questions. Four web checks (2023 AFCON scorers,
Chetti debut, Guedioura retirement). **Result: 55 PASS · 8 FAIL.**

| Row | Verdict | Note |
|----:|:-------:|------|
| 461,470–472,474,475,478,480,483–485,487,488,490,492–500,502–506 | ✅ PASS | Belmadi (2018 appt / 2019 AFCON / 2022 WCQ) |
| 476,477,479,481,482,486,489,491 | ✅ PASS | Halilhodžić (2014 WC) |
| 464,465,517,519,521,522,530 | ✅ PASS | Slimani (all-time top scorer / 2014 goals) |
| 466,468,509,510,514,516,524 | ✅ PASS | Mahrez (PL 2016 / Man City / 2019 captain) |
| 463,534,535 | ✅ PASS | 2014 R16 (Djabou's 120'+1' goal) |
| 473 | ✅ PASS | Leekens during failed 2018 qualifying |
| 526 | ✅ PASS | Ghoulam debut 2013 (2014 WCQ) |
| 462 | ❌ FAIL | Chetti debut was Arab Cup (Dec 2021), not the 2021 AFCON |
| 507 | ❌ FAIL | false premise — Halilhodžić has no AFCON win |
| 508 | ❌ FAIL | Slimani became top scorer Oct 2021, not "during 2019 AFCON" |
| 512 | ❌ FAIL | Bennacer was the 2019 AFCON star, not a post-rebuild emergence |
| 513 | ❌ FAIL | Djabou did NOT force ET (0-0 at 90'); his goal was 120'+1', 2-1 |
| 515 | ❌ FAIL | non-unique — Bennacer/Belaïli also fit |
| 527 | ❌ FAIL | Guedioura's last cap was Mar 2022, not a 2019 retirement |
| 540 | ❌ FAIL | non-unique — Bounedjah scored at the 2023 AFCON |

**Running totals (new method, rows 231+):** 200 PASS-ALL · 41 FAIL-LIVENESS.

---

## Batch rows 541–620 (Algeria) — NEW METHOD (only QA_PASSED.md rows)

63 candidates — many near-duplicate scorer questions plus a false-premise cluster.
**Result: 47 PASS · 16 FAIL.**

| Row | Verdict | Note |
|----:|:-------:|------|
| 541–543,548,553,556,560,562,563,566,567,570,571,575,576,600–605,612 | ✅ PASS | Bounedjah 2nd-min winner, 2019 AFCON final |
| 546,572,573 | ✅ PASS | Djabou's 120'+1' goal in the 2-1 loss (correctly framed) |
| 549,552,588,606–609 | ✅ PASS | Slimani key 2014 goals / all-time top scorer |
| 578–585,591,596–598,619 | ✅ PASS | Mahrez (captain 2019 / PL 2016 / 2022 WCQ star) |
| 587 | ✅ PASS | Aouar NOT in 2019 squad (joined 2023) |
| 616 | ✅ PASS | post-2019 rebuild → 2026 cycle (only temporally-valid option) |
| 545,577 | ❌ FAIL | non-unique — Feghouli/Brahimi/Slimani also qualify |
| 547,561 | ❌ FAIL | wrong scorer (Djabou / Bougherra, not Slimani) |
| 558,565 | ❌ FAIL | false "Djabou equalizer" — no 2-2, goal was 120'+1' |
| 574 | ❌ FAIL | false premise — Algeria lost to Cameroon, didn't reach 2022 |
| 589 | ❌ FAIL | Slimani wasn't top scorer in 2014 (became so in 2021) |
| 599 | ❌ FAIL | Algeria didn't face Tunisia in 2018 qualifying |
| 610 | ❌ FAIL | Madjer retired ~1992, not 2009 |
| 611 | ❌ FAIL | Atal WAS in the 2019 AFCON-winning squad |
| 620 | ❌ FAIL | Mahrez played no 2014 qualifiers (debuted after) |
| 613,615,617,618 | ❌ FAIL | unverifiable squad-rebuild / squad-age narrative |

**Running totals (new method, rows 231+):** 247 PASS-ALL · 57 FAIL-LIVENESS.

---

## Batch rows 621–710 (Algeria) — NEW METHOD (only QA_PASSED.md rows)

73 candidates — a badly-flawed stretch (fabricated club histories, Benrahma template,
2022-WC false premises, non-unique club/caps questions). **Result: 32 PASS · 41 FAIL.**

| Cluster | Verdict | Rows |
|---------|:-------:|------|
| Mahrez (2019/2022 WCQ/PL/captain/ManCity/debut) | ✅ PASS | 621,622,624,649,651,654,655,657,665,675,677,681,682,683,686,696,698,703,641 |
| Slimani 2014 / top scorer | ✅ PASS | 625,633,635,695 |
| Misc correct | ✅ PASS | 627,631,632,634,638,653,687,689,694 |
| Fabricated club history (Mahrez/Brahimi/Slimani "USM Alger") | ❌ FAIL | 693,704,705,706,707 |
| Benrahma "key modern attacker" non-unique | ❌ FAIL | 644,645,646,647,648,663,666,670,672,674,701 |
| "2022 World Cup squad/finals" false premise | ❌ FAIL | 628,636,637,658,664,680,684 |
| Non-unique "over 90 caps" | ❌ FAIL | 639,642,702 |
| Non-unique scorer / <40 goals | ❌ FAIL | 626,659,660,661 |
| Broken/non-unique club questions | ❌ FAIL | 688,690,692 |
| Other (nickname/debut/role/comparison/narrative) | ❌ FAIL | 623,629,630,656,662,699,708,710 |

**Running totals (new method, rows 231+):** 279 PASS-ALL · 98 FAIL-LIVENESS.

---

## Batch rows 711–810 (Algeria) — NEW METHOD (only QA_PASSED.md rows)

86 candidates — mostly Slimani "all-time top scorer" + Bounedjah "2019 final" duplicates (correct),
plus a club-history cluster and false-premise rows. One web check (Slimani WCQ goal tallies).
**Result: 65 PASS · 21 FAIL.**

| Cluster | Verdict | Rows |
|---------|:-------:|------|
| Slimani all-time top scorer / 2014 goals | ✅ PASS | 725,727,728,736,737,741–744,746–750,752,753,758,761,765,776,779,799,803,804,806,807 |
| Bounedjah 2019 AFCON final | ✅ PASS | 763,769,772,773,775,781–787,789–795,797,800,801 |
| Mahrez (captain/PL/star) | ✅ PASS | 729,730,738,756,757,802,809,810 |
| Belmadi / Djabou / misc | ✅ PASS | 711,719,721–724,734,766,798 |
| Fabricated/false club facts | ❌ FAIL | 712,713,714,715,717 |
| Wrong debut facts | ❌ FAIL | 731,732,733 |
| Non-unique | ❌ FAIL | 759,770,778 |
| False premise / timing | ❌ FAIL | 718,720,726,760 |
| Unverified goal stats | ❌ FAIL | 762,764 |
| False explanation (caps/venue/group goals) | ❌ FAIL | 735,739,767,805 |

**Running totals (new method, rows 231+):** 344 PASS-ALL · 119 FAIL-LIVENESS.
