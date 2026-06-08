# QA — TC-06 Live Factual Check (web-sourced, one-by-one)

Per-row factual verification of `answer` + `explanation` against live web sources
(Wikipedia / FIFA as tie-breaker, plus ESPN, Al Jazeera, CAF, etc.). Processed in
dataset order; **resumable** — the "Last verified row" marker below is the cursor.

- **PASS** = answer and explanation both factually correct per a cited source.
- **FAIL** = answer wrong, explanation wrong, or the question asserts an event that
  did not happen.
- **UNVERIFIED** = could not confirm from reliable sources → treated as FAIL
  (conservative; a competitive quiz must not ship unverified facts).

**Last verified row: 2160**  (✅ ARGENTINA COMPLETE — next sequential country: Australia, resume at row 2161)
**✅ BRAZIL COMPLETE (rows 6097–8182): 1346 ship-ready · 218 dangerous (full per-batch tables at bottom of file).**

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

---

## Batch rows 811–920 (Algeria) — NEW METHOD (only QA_PASSED.md rows)

92 candidates — mostly Mahrez/Slimani/Bounedjah duplicates (correct) plus a dense false-premise
and temporal-contradiction cluster. **Result: 71 PASS · 21 FAIL.**

| Cluster | Verdict | Rows |
|---------|:-------:|------|
| Mahrez / Slimani / Bounedjah correct duplicates | ✅ PASS | 812–814,817,820,823,825,826,831–839,841–851,856,858–867,869–878(in range),882,884–886,888–891,893,894,897,899–904,906–914,916–918,920 |
| 2018/2022 WC false premise (squad/played/captain) | ❌ FAIL | 815,821,852,854,857,880,883 |
| Slimani "top scorer" wrong timing | ❌ FAIL | 818,822,892,895,896,915 |
| Temporal contradiction (2016 PL before 2014) | ❌ FAIL | 879,887,919 |
| Mahrez didn't score 2014 / 2014 WCQ | ❌ FAIL | 811,868 |
| Algeria didn't top 2018 group | ❌ FAIL | 840 |
| Squad-age narrative / non-unique | ❌ FAIL | 855,905 |

**Running totals (new method, rows 231+):** 415 PASS-ALL · 140 FAIL-LIVENESS.

---

## Batch rows 921–1228 (Algeria) — NEW METHOD — FINAL ALGERIA BATCH

175 candidates — mostly correct duplicates (Halilhodžić 2014, Belmadi 2019, Bounedjah 2019
final, beat Senegal/Egypt, failed 2018/2022) plus recurring-error clusters.
**Result: 139 PASS · 36 FAIL.**

| Cluster | Verdict | Count |
|---------|:-------:|------:|
| Correct duplicates (managers / scorers / results / qualification) | ✅ PASS | 139 |
| "intercontinental playoff" mislabel (2010 Egypt) | ❌ FAIL | 935,1013,1017,1020,1024,1094,1097,1144,1218 |
| Self-referential ("like Algeria… → Algeria") | ❌ FAIL | 954,966,1037,1042,1053,1058 |
| "via CAF" non-unique / false "directly" | ❌ FAIL | 929,930,1139,1142,1143 |
| Other non-unique | ❌ FAIL | 1052,1067,1043,1107,956,1054 |
| Wrong fact (Egypt 2nd AFCON) | ❌ FAIL | 955 |
| 2022 WC false premise | ❌ FAIL | 922,927,1147 |
| False contrast (Uruguay/Algeria playoff) | ❌ FAIL | 1039 |
| Squad-rebuild narrative | ❌ FAIL | 1219,1221,1222,1223,1224 |

**Running totals (new method, rows 231+): 554 PASS-ALL · 176 FAIL-LIVENESS.**

# ✅ ALGERIA COMPLETE (rows 2–1228)
- Rows 2–230 (old method): 181 PASS / 48 FAIL (in QA_TC06_PASSED/FAILED.md)
- Rows 231–1228 (new method, QA_PASSED.md pool only): **554 ship-ready** (QA_PASSED_ALL.md)
  + **176 dangerous** (QA_FAILED_LIVENESS_PASSED_OTHERS.md); ~268 rows skipped (in QA_FAILED.md).
- Next country: **Argentina** (rows 1229–2160). (The CSV is alphabetical by country.)

---

# ARGENTINA (rows 1229–2160) — NEW METHOD (only QA_PASSED.md rows)

Fact base (verified this session): WCs won 1978/1986/**2022**; 2022 final beat France 3-3
(4-2 pens), Emi Martínez Golden Glove, Messi Golden Ball, base camp **Qatar University**;
2014 final lost 1-0 to Germany; 2018 R16 lost 4-3 to France (Sampaoli sacked); 2010 QF lost
4-0 Germany; **Copa 2021** beat Brazil 1-0 (Di María, Maracanã) = Messi's 1st major; **Copa 2024**
beat Colombia 1-0 a.e.t.; 2015 & 2016 Copa finals lost to Chile (Messi retired/un-retired after
2016); 2022 Finalissima beat Italy 3-0 (Wembley); FIFA ranking 7th@2014, 5th@2018, 3rd@2022,
#1 from Apr 2023; Messi 13 WC goals incl. 2006; 2008 Olympic gold = Messi+Di María+Agüero.

## Batch rows 1229–1300 (Argentina) — 57 candidates → 42 PASS · 15 FAIL

| Row | Verdict | Note |
|----:|:-------:|------|
| 1244,1246,1259,1277 | ❌ FAIL | corrupted answer (02-Jan=2-1, 04-Feb=4-2, 02-Feb=2-2) |
| 1248 | ❌ FAIL | unverified "10th in early 2018" (were 5th by June) |
| 1264 | ❌ FAIL | unverified squad count (13 leagues) |
| 1268,1278 | ❌ FAIL | non-unique — Di María & Agüero also won 2008 Olympic gold |
| 1276 | ❌ FAIL | false — Argentina never played Brazil at 2024 Copa |
| 1279 | ❌ FAIL | explanation: 13 WC goals "across 2014/18/22" = 12 (omits 2006) |
| 1281 | ❌ FAIL | non-unique — Lisandro Martínez also partnered Otamendi |
| 1296 | ❌ FAIL | self-referential + unverified (>100 in top-5 leagues) |
| 1298 | ❌ FAIL | false — drew 0-0 home vs Brazil; didn't win every home QCG |
| 1299 | ❌ FAIL | unverified (Monumental "multiple times") |
| 1300 | ❌ FAIL | wrong — 2022 base camp was Qatar University, not Ezeiza |
| (other 42) | ✅ PASS | rankings 7th/5th/3rd, 2021 Copa, Finalissima, 2022 final, etc. |

**Running totals (new method, all countries): 596 PASS-ALL · 191 FAIL-LIVENESS.**
**Argentina so far: 42 PASS · 15 FAIL (rows 1229–1300).**

## Batch rows 1301–1390 (Argentina) — 59 candidates → 42 PASS · 17 FAIL

| Row | Verdict | Note |
|----:|:-------:|------|
| 1341,1342 | ❌ FAIL | false — Argentina UNBEATEN in 2022 qualifying (no 2-0 loss to Brazil) |
| 1352 | ❌ FAIL | corrupted answer 04/03/2003 = "4-3-3" |
| 1355,1361 | ❌ FAIL | "four goals in 23 min" false (Germany scored 3',67',74',89') |
| 1369 | ❌ FAIL | 2022 final MOTM was Messi, not Di María |
| 1373 | ❌ FAIL | non-unique — Argentina also topped groups 1998 & 2006 |
| 1378 | ❌ FAIL | non-unique — Messi won Golden Ball 2014 AND 2022 |
| 1335 | ❌ FAIL | non-unique — Monumental bigger than all 4 options |
| 1332,1333 | ❌ FAIL | Messi WC goals "across 2014-22" = 12, not 13 (omits 2006) |
| 1302,1303,1313 | ❌ FAIL | unverified "13 leagues" squad count (cf. 1264) |
| 1334 | ❌ FAIL | combined 2018+2022 qualifying goals ~46, not "over 50" |
| 1336,1339 | ❌ FAIL | unsupported venue claims (rotated venues; not Monumental-primary) |
| (other 42) | ✅ PASS | Messi 116 goals, 8 conceded/15 scored 2022, Agüero 26 GB, Montiel/Emi final, etc. |

**Running totals (new method, all countries): 638 PASS-ALL · 208 FAIL-LIVENESS.**
**Argentina so far: 84 PASS · 32 FAIL (rows 1229–1390).**

## Batch rows 1391–1480 (Argentina) — 71 candidates → 54 PASS · 17 FAIL

| Row | Verdict | Note |
|----:|:-------:|------|
| 1444,1448,1452 | ❌ FAIL | corrupted answer (03-Mar=3-3, 03-Jan=3-1, 02-Jan=2-1) |
| 1451,1455 | ❌ FAIL | false — no Argentina-Brazil match at 2024 Copa |
| 1397,1473 | ❌ FAIL | 2022 qualifying record wrong (unbeaten 11-6-0; didn't win all home) |
| 1415 | ❌ FAIL | Uruguay won 2023 U-20 WC, not Argentina (hosts, R16 exit) |
| 1476 | ❌ FAIL | 2014 Fair Play Award went to Colombia, not Argentina |
| 1414,1395 | ❌ FAIL | non-unique (Emi GG 2021&2024; Messi top scorer 2018 too) |
| 1428,1429,1431 | ❌ FAIL | unverified "10th early 2018" (cf. 1248) |
| 1396,1472 | ❌ FAIL | unverified Monumental 2022-qualifier usage (cf. 1299/1339) |
| 1417 | ❌ FAIL | Messi most-capped ≈2021, not 2022 |
| (other 54) | ✅ PASS | rankings 7/5/3, Copa 2021/2019/2011/2015, Finalissima, 2018 qual, etc. |

**Running totals (new method, all countries): 692 PASS-ALL · 225 FAIL-LIVENESS.**
**Argentina so far: 138 PASS · 49 FAIL (rows 1229–1480).**

## Batch rows 1481–1570 (Argentina) — 72 candidates → 62 PASS · 10 FAIL

| Row | Verdict | Note |
|----:|:-------:|------|
| 1483,1504 | ❌ FAIL | 2023 U-20 WC won by Uruguay, not Argentina (cf. 1415) |
| 1484,1496 | ❌ FAIL | non-unique (Emi GG 2021&2024; Messi top scorer 2018 too) |
| 1521 | ❌ FAIL | non-unique — Argentina also didn't lose to Mexico |
| 1548 | ❌ FAIL | non-unique — Otamendi & Molina also started 2022 final |
| 1566 | ❌ FAIL | Agüero scored 41 goals, not 42 |
| 1529 | ❌ FAIL | combined 2018+2022 qual goals ~46, not over 50 (cf. 1334) |
| 1486 | ❌ FAIL | unverified Monumental 2022-qualifier claim (cf. 1299/1396) |
| 1482 | ❌ FAIL | vague answer + self-referential explanation |
| (other 62) | ✅ PASS | Ezeiza base (correct), Messi captain, Romero/Otamendi/Lisandro/Molina, Rojo 2018, Agüero retirement, etc. |

**Running totals (new method, all countries): 754 PASS-ALL · 235 FAIL-LIVENESS.**
**Argentina so far: 200 PASS · 59 FAIL (rows 1229–1570).**

## Batch rows 1571–1670 (Argentina) — 79 candidates → 75 PASS · 4 FAIL

Mostly unambiguous "who" questions (Emi Martínez GK, Scaloni/Sampaoli/Sabella/Martino/Maradona
managers, De Paul/Mac Allister/Enzo midfielders, Messi). **75 PASS · 4 FAIL.**

| Row | Verdict | Note |
|----:|:-------:|------|
| 1666,1668 | ❌ FAIL | Messi passed Mascherano in 2021 (29 Jun), not 2022 (cf. 1417) |
| 1658 | ❌ FAIL | "116 goals before 2022 WC" — 116 is his 2026 total (~91 before 2022) |
| 1613 | ❌ FAIL | built on unverified "10th in early 2018" premise (cf. 1248) |
| (other 75) | ✅ PASS | Emi 2022 GG/saves, 198 caps, La Bombonera ~54k, Scaloni Nov-2018, etc. |

**Running totals (new method, all countries): 829 PASS-ALL · 239 FAIL-LIVENESS.**
**Argentina so far: 275 PASS · 63 FAIL (rows 1229–1670).**

## Batch rows 1671–1780 (Argentina) — 83 candidates → 74 PASS · 9 FAIL

| Row | Verdict | Note |
|----:|:-------:|------|
| 1748,1749,1750 | ❌ FAIL | non-unique 2008 Olympic gold (Messi+Agüero+Di María) |
| 1718,1720 | ❌ FAIL | Pavón didn't score vs France 2018 (Di María/Mercado/Agüero did) |
| 1686 | ❌ FAIL | non-unique — Lisandro also partnered Otamendi (cf. 1281) |
| 1755 | ❌ FAIL | 2022 final MOTM was Messi, not Di María (cf. 1369) |
| 1695 | ❌ FAIL | 13 WC goals "across 2014/18/22" = 12 (cf. 1332/1333) |
| 1722 | ❌ FAIL | explanation says Agüero 42 goals (it's 41) |
| (other 74) | ✅ PASS | Messi penalties/captain/Ballon d'Or, Di María 2021&2022 finals, Montiel, Tévez offside 2010, etc. |

**Running totals (new method, all countries): 903 PASS-ALL · 248 FAIL-LIVENESS.**
**Argentina so far: 349 PASS · 72 FAIL (rows 1229–1780).**

## Batch rows 1781–1900 (Argentina) — 96 candidates → 83 PASS · 13 FAIL

| Row | Verdict | Note |
|----:|:-------:|------|
| 1835,1836,1893 | ❌ FAIL | non-unique (2008 gold; Di María also every-WC 2010-22) |
| 1884 | ❌ FAIL | non-unique — De Paul also key 2021 Copa + 2022 WC |
| 1873,1900 | ❌ FAIL | Mascherano record passed 2021 not 2022 (cf. 1417) |
| 1795 | ❌ FAIL | 2022 final MOTM was Messi, not Di María |
| 1807 | ❌ FAIL | France-2018 scorers were Di María/Mercado/Agüero, not Pavón |
| 1808 | ❌ FAIL | 2018 qualifying had ~19 goals (<25); combined ~46 (<50) |
| 1849 | ❌ FAIL | 2014 Fair Play Award went to Colombia |
| 1822,1827,1830 | ❌ FAIL | Monumental claims (before-Bombonera false; "multiple" unsupported) |
| (other 83) | ✅ PASS | Messi GB/Ballon d'Or, Emi GG, Enzo Young Player, capacities, Primera/AFA, etc. |

**Running totals (new method, all countries): 986 PASS-ALL · 261 FAIL-LIVENESS.**
**Argentina so far: 432 PASS · 85 FAIL (rows 1229–1900).**

## Batch rows 1901–2010 (Argentina) — 69 candidates → 60 PASS · 9 FAIL

| Row | Verdict | Note |
|----:|:-------:|------|
| 1963,1985,2002 | ❌ FAIL | false — Argentina unbeaten in 2022 qualifying (no Brazil defeat) |
| 1904,1950 | ❌ FAIL | 2014 Fair Play Award was Colombia's (cf. 1476/1849) |
| 1905,1930 | ❌ FAIL | Messi 13 WC goals "across 2014-22" = 12 (omits 2006) |
| 1901 | ❌ FAIL | Mascherano record stood until 2021, not 2022 |
| 1966 | ❌ FAIL | non-unique — Argentina also lost 2007 & 2015 finals |
| (other 60) | ✅ PASS | rankings 7/5/3, Messi 2x Golden Ball, Montiel, Saudi upset, Finalissima, 2024 final, etc. |

**Running totals (new method, all countries): 1046 PASS-ALL · 270 FAIL-LIVENESS.**
**Argentina so far: 492 PASS · 94 FAIL (rows 1229–2010).**

## Batch rows 2011–2160 (Argentina) — FINAL — 86 candidates → 70 PASS · 16 FAIL

| Row | Verdict | Note |
|----:|:-------:|------|
| 2054,2093,2149 | ❌ FAIL | false Brazil "2022 qualifying defeat" (Argentina unbeaten) |
| 2042,2043,2045,2047,2124 | ❌ FAIL | Monumental "multiple 2022 qualifiers" unsupported |
| 2096,2097 | ❌ FAIL | "four goals in 23 minutes" false (Germany 2010) |
| 2037 | ❌ FAIL | no Argentina-Brazil 2024 Copa match |
| 2121 | ❌ FAIL | 2014 Fair Play Award was Colombia's |
| 2110 | ❌ FAIL | fabricated assistant "Matelán" (real: Ayala/Samuel/Aimar) |
| 2082 | ❌ FAIL | non-unique — Poland/Australia also didn't beat Argentina in a group game |
| 2152 | ❌ FAIL | combined qualifying goals ~46, not over 50 |
| 2160 | ❌ FAIL | built on unverified "10th early 2018" premise |
| (other 70) | ✅ PASS | Mbappé hat-trick, Götze 2014, Tévez offside, Lautaro QF penalty, 2024 final, etc. |

**Running totals (new method, all countries): 1116 PASS-ALL · 286 FAIL-LIVENESS.**

# ✅ ARGENTINA COMPLETE (rows 1229–2160)
- New method (QA_PASSED.md pool only): **562 ship-ready** + **110 failed-liveness** = 672 (matches QA_PASSED count).
- Next country: **Australia** (rows 2161–3241).

# ===== BRAZIL (rows 6097–8182) — NEW METHOD (only QA_PASSED.md rows) =====
Separate contributor, started 2026-06-06. Country range 6097–8182 (2086 rows total;
1564 in QA_PASSED.md). Liveness run only on QA_PASSED.md rows; PASS → QA_PASSED_ALL.md,
FAIL → QA_FAILED_LIVENESS_PASSED_OTHERS.md.

## Brazil fact base (web-verified, reused across batches)
- **2010 WC:** Group G winners (NKorea 2-1, Ivory Coast 3-1, Portugal 0-0); R16 beat Chile 3-0;
  **QF lost 2-1 to Netherlands** (Robinho 10'; Sneijder x2). Dunga left after.
- **2014 WC (hosts):** **SF lost 1-7 to Germany** at Mineirão, Belo Horizonte (5 goals in 29 min,
  Oscar consolation); **3rd-place lost 0-3 to Netherlands** → finished 4th. **Scolari** was coach,
  resigned 15 Jul; **Dunga rehired**. Neymar (injury) & Thiago Silva (suspension) missed the SF.
- **2018 WC:** Group E winners — **1-1 Switzerland**, 2-0 Costa Rica, 2-0 Serbia (NO Mexico in group,
  NO 0-0 draw). **R16 beat Mexico 2-0**; **QF lost 2-1 to Belgium**.
- **2022 WC:** Group G winners — 2-0 Serbia (Richarlison bicycle kick), 1-0 Switzerland, **0-1 Cameroon**;
  **R16 beat South Korea 4-1**; **QF lost to Croatia on penalties** (1-1 a.e.t., 4-2 pens). **Brazil scored
  8 goals total** (NOT 15). FIFA No.1 ranked. **Tite resigned immediately after** the Croatia loss.
  Neymar EQUALED Pelé's 77 with his goal v Croatia. Thiago Silva captained at age 38. Dani Alves (44
  titles) most decorated.
- **Copa América:** 2019 WON (SF beat Argentina 2-0 at Mineirão; final beat Peru 3-1 at Maracanã;
  Neymar injured pre-tournament; Alisson best GK). 2021 final **LOST 1-0 to Argentina** at Maracanã
  (Di María). 2016 Centenario **group exit → Dunga sacked, Tite hired**. 2024 **QF lost to Uruguay on pens**.
- **Neymar record:** equaled Pelé (77) v Croatia (2022 WC); **surpassed v Bolivia 8 Sep 2023** (78th & 79th,
  5-1 win) to become Brazil's all-time top scorer.
- **Misc:** 2016 Olympic gold (beat Germany on pens, Maracanã, first men's gold). 2013 Confederations Cup
  final beat Spain 3-0 (Fred x2). 2012 Club World Cup Corinthians 1-0 Chelsea (Guerrero). Flamengo 2019
  Libertadores (Jorge Jesus); Palmeiras 2020 & 2021. **Brazilian clubs: 23 Libertadores titles as of 2023**
  (Fluminense 2023 = 23rd; 24th in 2024, 25th in 2025). Endrick's age-17 goals were all friendlies
  (England/Spain Mar 2024, Mexico Jun 2024), not WC qualifiers.

## Batch rows 6097–6160 (Brazil) — 52 candidates — **40 PASS · 12 FAIL**
| Row | Verdict | Note |
|----:|:-------:|------|
| 6098,6099,6103,6106,6111,6112,6113,6114,6115,6117 | ✅ PASS | manager exits (Tite 2022 / Dunga 2010 & 2016) |
| 6100,6105,6110,6116,6118,6121,6123,6124,6125,6127,6128,6129,6130,6131,6133,6134,6136,6137,6138,6141,6142,6144,6145,6151,6154,6155,6158,6159,6160,6101 | ✅ PASS | results/records verified against fact base |
| 6097 | ❌ FAIL | next Argentina meeting was Nov 2019 friendly, not 2021 Copa final |
| 6102 | ❌ FAIL | non-unique negative (Santos also didn't "spark resurgence") |
| 6108 | ❌ FAIL | explanation wrong (equaled Pelé v Croatia; 78&79 same Bolivia match) |
| 6119,6120 | ❌ FAIL | false premise — no 0-0 Brazil-Mexico 2018 group game |
| 6122 | ❌ FAIL | Neymar equaled Pelé v Croatia, not Bolivia |
| 6126 | ❌ FAIL | Brazilian clubs had 23 Libertadores titles as of 2023, not 24 |
| 6147,6150 | ❌ FAIL | Brazil scored 8 goals at 2022 WC, not 15 |
| 6148 | ❌ FAIL | non-unique stadium (multiple 2022 WCQ venues) |
| 6149 | ❌ FAIL | "04-Jan" = corrupted "4-1" (Excel date mangling) |
| 6157 | ❌ FAIL | Endrick's age-17 goals were friendlies, not a WC qualifier |

## Batch rows 6161–6280 (Brazil) — 101 candidates — **89 PASS · 12 FAIL**
New facts verified: Brazil ranked FIFA No.1 entering BOTH 2010 and 2022 WCs (but Germany were
also No.1 entering 2018 → 6256 non-unique); Thiago Silva in FIFA's 2014 Dream Team; Brazil's
2018 CONMEBOL record = 12W-5D-1L/41pts (one loss to Chile); 2022 qualifying 45 pts, 2010 33 pts;
Casemiro anchored 2018 & 2022; Neymar 4 goals at 2014 before injury; 2011 Copa QF lost to Paraguay
on pens; Di María scored the 2021 Copa final winner; Firmino scored 2nd v Mexico (2018 R16).
| Row | Verdict | Note |
|----:|:-------:|------|
| (89 rows) | ✅ PASS | results/records/managers/qualification verified vs fact base |
| 6197 | ❌ FAIL | "3 goals/match" rests on false 15-goal premise (8 goals at 2022) |
| 6212 | ❌ FAIL | non-unique negative (fell to 22nd, not any listed rank) |
| 6242 | ❌ FAIL | "02-Jan" = corrupted "2-1" (Belgium) |
| 6243 | ❌ FAIL | distractor "Granja Comary" = answer "CBF Training Centre" (same venue) |
| 6244 | ❌ FAIL | ambiguous: reached QF in all four 2010-22; "Four" also defensible |
| 6246,6247,6248 | ❌ FAIL | false 15-goal premise (Brazil scored 8 at 2022) |
| 6256 | ❌ FAIL | non-unique: Germany also entered 2018 as FIFA No.1 |
| 6265,6271 | ❌ FAIL | false "0-0 v Mexico 2018 group" (never played in group) |
| 6277 | ❌ FAIL | 2018 record was 12-5-1, not "0 defeats" |

## Batch rows 6281–6400 (Brazil) — 88 candidates — **77 PASS · 11 FAIL**
New facts: Neymar scored 8 goals in 2022 CONMEBOL qualifying (joint 2nd top scorer) → those rows PASS;
Richarlison scored 3 (not 4) at 2022 WC; Brazil 4-1 Uruguay in Manaus (2-0 was away in Montevideo);
2014 Bronze Ball = Robben (not Neymar); 2022 squad's 6 leagues incl. Mexico (Dani Alves/Pumas), NOT
Germany; Everton Cebolinha 2019 Copa top scorer (3); three managers in 2026 qualifying (Diniz/Dorival/
Ancelotti); Neymar's Ballon d'Or podiums were 2015 & 2017 (but 9 nominations total).
| Row | Verdict | Note |
|----:|:-------:|------|
| (77 rows) | ✅ PASS | qualification points / managers / records verified vs fact base |
| 6305 | ❌ FAIL | non-unique Ballon d'Or years (9 nominations) |
| 6316 | ❌ FAIL | Neymar didn't win 2014 Bronze Ball (Robben did) |
| 6320,6353 | ❌ FAIL | Brazilian clubs had 23 Libertadores titles as of 2023, not 24 |
| 6325,6339 | ❌ FAIL | 2022 squad's 6th league was Mexico, not Germany (explanation wrong) |
| 6357,6358 | ❌ FAIL | Brazil scored 8 goals at 2022 WC, not 15 |
| 6363 | ❌ FAIL | Richarlison scored 3 at 2022 WC, not 4 |
| 6391 | ❌ FAIL | Manaus v Uruguay was 4-1; the 2-0 was in Montevideo |
| 6392 | ❌ FAIL | Neymar equaled Pelé v Croatia; v Bolivia he surpassed (78th/79th) |

## Batch rows 6401–6520 (Brazil) — 102 candidates — **89 PASS · 13 FAIL**
Verified: Richarlison's bicycle kick was a Puskás nominee; Dani Alves = 2019 Copa Best Player;
Brazil finished 2nd (not 1st) in their 2024 Copa group (Colombia won it).
| Row | Verdict | Note |
|----:|:-------:|------|
| (89 rows) | ✅ PASS | mostly duplicate WC-result/record questions vs fact base |
| 6412 | ❌ FAIL | only ~22 of the 26-man squad were Europe-based, not 26 |
| 6413 | ❌ FAIL | 6th country was Mexico, not Germany (explanation) |
| 6422 | ❌ FAIL | "02-Jan" = corrupted "2-1" (Belgium) |
| 6428,6429 | ❌ FAIL | Manaus v Uruguay was 4-1; 2-0 was in Montevideo |
| 6441 | ❌ FAIL | Brazil first faced Mexico in R16, not the 2018 group |
| 6450 | ❌ FAIL | Brazil finished 2nd in their 2024 Copa group, didn't win it |
| 6456 | ❌ FAIL | Neymar equaled Pelé in 2022, not 2023 (false premise) |
| 6468 | ❌ FAIL | 8 goals at 2022 WC, not 15 |
| 6480,6486 | ❌ FAIL | Neymar didn't win 2014 Bronze Ball (Robben) |
| 6503,6504 | ❌ FAIL | no 0-0 v Mexico in 2018 group (false premise) |

## Batch rows 6521–6640 (Brazil) — 89 candidates — **72 PASS · 17 FAIL**
Verified: Ancelotti (May 2025) first long-term non-Brazilian manager; Dorival Júnior 2024; Endrick's
first call-up was Nov 2023 (NOT 2024); Neymar ~€88m to Barça 2013; Flamengo 2022 Libertadores under
Dorival Júnior. Heavy recurring-error cluster this batch.
| Row | Verdict | Note |
|----:|:-------:|------|
| (72 rows) | ✅ PASS | manager/date/result duplicates vs fact base |
| 6522,6523,6597,6622,6623 | ❌ FAIL | "2-0 v Uruguay in Manaus" false (Manaus 4-1; 2-0 was Montevideo) |
| 6538,6586 | ❌ FAIL | 8 goals at 2022 WC, not 15 (and the 3/match derived from it) |
| 6556,6557 | ❌ FAIL | Endrick's first call-up was 2023, not 2024 |
| 6568,6569 | ❌ FAIL | non-unique Ballon d'Or years (9 nominations) |
| 6598,6604,6607,6610,6612 | ❌ FAIL | corrupted score cells (01-Jul/04-Jan/07-Jan/02-Jan) |
| 6625 | ❌ FAIL | no 0-0 v Mexico in 2018 group (false premise) |

## Batch rows 6641–6760 (Brazil) — 95 candidates — **87 PASS · 8 FAIL**
Mostly duplicates (Neymar record / Tite / Olympic gold / managers / venues).
| Row | Verdict | Note |
|----:|:-------:|------|
| (87 rows) | ✅ PASS | duplicates verified vs fact base |
| 6648 | ❌ FAIL | 8 goals at 2022 WC, not 15 |
| 6675,6703,6704,6705 | ❌ FAIL | Neymar equaled Pelé v Croatia (2022); v Bolivia he surpassed |
| 6689 | ❌ FAIL | Richarlison scored 3 at 2022 WC, not 4 |
| 6746 | ❌ FAIL | non-unique: Maracanã & Arena Corinthians also > Mineirão capacity |
| 6752 | ❌ FAIL | Mexico was an R16 opponent, not a 2018 group opponent |

## Batch rows 6761–6880 (Brazil) — 89 candidates — **86 PASS · 3 FAIL**
Almost entirely manager-identity duplicates (Tite/Dunga/Scolari/Mano Menezes/Diniz/Dorival).
| Row | Verdict | Note |
|----:|:-------:|------|
| (86 rows) | ✅ PASS | manager/squad/result duplicates vs fact base |
| 6779 | ❌ FAIL | non-unique negative (Militão also not a first-choice CB in 2022) |
| 6810,6815 | ❌ FAIL | non-unique: Diniz, Dorival & Ancelotti all oversaw 2026 qualifying |

## Batch rows 6881–7000 (Brazil) — 98 candidates — **72 PASS · 26 FAIL** (heavy-defect)
New verified: Marquinhos was NOT Thiago Silva's 2018 CB partner (Miranda was); Brasília DID host
2014 (7 games); Fabinho & Casemiro make "Liverpool/EPL" rows non-unique; Brazil scored 0 v Cameroon;
Raphinha scored 0 at 2022; multiple 2019-Copa scorers among options.
| Row | Verdict | Note |
|----:|:-------:|------|
| (72 rows) | ✅ PASS | Neymar-record (surpassed) / Marquinhos pen / stadiums / squad duplicates |
| 6887,6888,6889,6890,6891,6912,6923,6955,6956 | ❌ FAIL | "Neymar equaled/77th v Bolivia" (he surpassed; equaled v Croatia 2022) |
| 6940,6973 | ❌ FAIL | 2022 squad 6th league = Mexico, not Germany (explanation) |
| 6944 | ❌ FAIL | "3 goals/match" from false 15-goal premise (8 goals) |
| 6960 | ❌ FAIL | distractor "Granja Comary" = answer "CBF Training Centre" |
| 6907,6961 | ❌ FAIL | Brazil scored 0 v Cameroon; Raphinha scored 0 at 2022 |
| 6966 | ❌ FAIL | non-unique: Maracanã & Estádio Nacional also > Castelão |
| 6974,6976 | ❌ FAIL | non-unique league (Casemiro EPL; Fabinho Liverpool) |
| 6993,6999 | ❌ FAIL | non-unique CB (Thiago Silva also fits) |
| 6995,6996 | ❌ FAIL | 2018 CB partner was Miranda, not Marquinhos |
| 6900,6911 | ❌ FAIL | non-unique (Vinícius for 2026; multiple 2019-Copa scorers) |
| 6899 | ❌ FAIL | Neymar was at PSG in 2022, not Al-Hilal (joined 2023) |
| 7000 | ❌ FAIL | Brasília DID host 2014 matches (false) |

## Batch rows 7001–7120 (Brazil) — 91 candidates — **84 PASS · 7 FAIL**
Mostly club-history (Santos/Neymar, Corinthians 2012, Flamengo 2019/2022, Palmeiras 2020/21) and
defender duplicates. Verified: Thiago Silva has 113 caps (not "over 115").
| Row | Verdict | Note |
|----:|:-------:|------|
| (84 rows) | ✅ PASS | club-history & defender duplicates vs fact base |
| 7001 | ❌ FAIL | Manaus v Uruguay was 4-1 (2-0 was Montevideo) |
| 7003 | ❌ FAIL | Porto Alegre WAS a 2014 host (false) |
| 7092,7093,7095 | ❌ FAIL | Thiago Silva has 113 caps, not "over 115" |
| 7094 | ❌ FAIL | non-unique (Thiago Silva also 90+ caps, both WCs) |
| 7118 | ❌ FAIL | both Thiago Silva & David Luiz scored v Colombia (2014 QF) |

## Batch rows 7121–7240 (Brazil) — 96 candidates — **78 PASS · 18 FAIL**
Heavy manager/GK/defender duplicates. Verified Ederson (not Alisson) played v Cameroon 2022.
| Row | Verdict | Note |
|----:|:-------:|------|
| (78 rows) | ✅ PASS | Tite/Alisson/Thiago Silva/Casemiro duplicates vs fact base |
| 7131,7144 | ❌ FAIL | non-unique negatives (Militão also not CB; 3 didn't win Golden Ball) |
| 7136,7137 | ❌ FAIL | Thiago Silva has 113 caps, not "over 115" |
| 7145,7153 | ❌ FAIL | Neymar equaled Pelé v Croatia, not v Bolivia |
| 7155 | ❌ FAIL | all 4 options scored at 2019 Copa (non-unique) |
| 7157,7161,7162,7187 | ❌ FAIL | non-unique (Vinícius/Martinelli also 2022 squad / 2026 key) |
| 7164 | ❌ FAIL | Ederson, not Alisson, played v Cameroon 2022 |
| 7195,7196,7206,7209,7212 | ❌ FAIL | non-unique 2026 manager (Ancelotti/Diniz also) |
| 7197 | ❌ FAIL | Brazil didn't face Mexico in the 2018 group (false premise) |

## Batch rows 7241–7360 (Brazil) — 98 candidates — **73 PASS · 25 FAIL**
Big NEW defect: dataset claims "Fred started in midfield at the 2018 World Cup" — FALSE. Fred was a
fringe player in 2018 (starters: Casemiro/Paulinho/Coutinho; Fernandinho replaced suspended Casemiro
in the QF) and only became a STARTER in 2022. The dataset reversed his two World Cups.
| Row | Verdict | Note |
|----:|:-------:|------|
| (73 rows) | ✅ PASS | Casemiro/Neymar-record(surpassed)/Dani Alves/Thiago Silva duplicates |
| 7258,7262,7263,7264,7265,7266,7268,7269,7271,7272,7273,7274,7275 | ❌ FAIL | "Fred started 2018" — false (he started 2022) |
| 7276,7284 | ❌ FAIL | non-unique Fred (Gabriel Jesus/Casemiro/Paquetá also in squads) |
| 7328,7329,7331,7333,7334,7335,7336,7337 | ❌ FAIL | "Neymar equaled v Bolivia" (he surpassed; equaled v Croatia 2022) |
| 7248 | ❌ FAIL | non-unique 2026 manager (Ancelotti also) |
| 7319 | ❌ FAIL | non-unique negative (Thiago Silva & Oscar both didn't score 2013 final) |

## Batch rows 7361–7480 (Brazil) — 98 candidates — **82 PASS · 16 FAIL**
Player-identity duplicates. Recurring fails: "Richarlison 4 goals at 2022" (he scored 3), non-unique
"in 2022 squad"/"2026 key" (Vinícius/Jesus/Casemiro also fit), Neymar-equaled-v-Bolivia.
| Row | Verdict | Note |
|----:|:-------:|------|
| (82 rows) | ✅ PASS | scorer/Olympic/record/award duplicates vs fact base |
| 7380,7412 | ❌ FAIL | Richarlison scored 3 at 2022, not 4 |
| 7365,7414 | ❌ FAIL | Neymar's 77th was v Croatia; v Bolivia he surpassed |
| 7406,7409 | ❌ FAIL | non-unique 2019-Copa scorer (Coutinho/Richarlison also) |
| 7426 | ❌ FAIL | non-unique 2022 R16 scorer (Richarlison also) |
| 7427 | ❌ FAIL | Raphinha scored 0 at 2022 (false) |
| 7418 | ❌ FAIL | David Luiz didn't score in the 7-1 (Oscar did) |
| 7361,7457,7468,7470,7477,7479 | ❌ FAIL | non-unique 2022-squad/2026-key (Vinícius/Jesus/Casemiro/Fred) |
| 7393 | ❌ FAIL | answer right (no hat-trick) but explanation repeats false 15-goal figure |

## Batch rows 7481–7620 (Brazil) — 107 candidates — **95 PASS · 12 FAIL**
Mostly stadium-capacity and player-award duplicates (clean).
| Row | Verdict | Note |
|----:|:-------:|------|
| (95 rows) | ✅ PASS | stadium/award/scorer duplicates vs fact base |
| 7500,7508,7513 | ❌ FAIL | Neymar didn't win 2014 Bronze Ball (Robben) |
| 7486 | ❌ FAIL | Endrick's age-17 goals were friendlies, not a WC qualifier |
| 7506,7507,7518 | ❌ FAIL | non-unique 2022-squad/2026-key (Vinícius also) |
| 7552 | ❌ FAIL | no record of David Luiz scoring in the 2013 Confederations Cup |
| 7566 | ❌ FAIL | 8 goals at 2022 WC, not 15 |
| 7579 | ❌ FAIL | non-unique: Maracanã/Estádio Nacional/Mineirão all > Arena Corinthians |
| 7614,7620 | ❌ FAIL | Neymar equaled Pelé v Croatia, not v Bolivia |

## Batch rows 7621–7760 (Brazil) — 81 candidates — **62 PASS · 19 FAIL**
| Row | Verdict | Note |
|----:|:-------:|------|
| (62 rows) | ✅ PASS | Neymar injury/Santos / Endrick call-up / Granja Comary / Tite / Zúñiga |
| 7687,7690,7691,7692,7693,7694 | ❌ FAIL | Raphinha scored 0 at 2022 (not v South Korea/Cameroon) |
| 7638,7645,7704 | ❌ FAIL | Neymar didn't win 2014 Bronze Ball (Robben) |
| 7652,7657,7669 | ❌ FAIL | Endrick's age-17 goals were friendlies, not WC qualifiers |
| 7676 | ❌ FAIL | Thiago Silva (not Neymar) captained 2018 & 2022 |
| 7742,7746 | ❌ FAIL | Manaus v Uruguay was 4-1 (2-0 was Montevideo) |
| 7650 | ❌ FAIL | 8 goals at 2022 WC, not 15 |
| 7666 | ❌ FAIL | distractor "Granja Comary" = answer "CBF Training Centre" |
| 7756,7757 | ❌ FAIL | Libertadores count: Argentina (25) led Brazil (23) in 2023 |

## Batch rows 7761–7900 (Brazil) — 108 candidates — **101 PASS · 7 FAIL**
Very clean (manager / 2014-hosts / opponent duplicates).
| Row | Verdict | Note |
|----:|:-------:|------|
| (101 rows) | ✅ PASS | manager/qualification/opponent duplicates vs fact base |
| 7789,7790 | ❌ FAIL | non-unique "league not represented" (Germany also absent) |
| 7872 | ❌ FAIL | Manaus v Uruguay was 4-1 (2-0 was Montevideo) |
| 7886 | ❌ FAIL | Brazil didn't draw Mexico in 2018 group (false premise) |
| 7887 | ❌ FAIL | Paraguay eliminated Brazil in 2011, not vice-versa |
| 7894 | ❌ FAIL | Neymar equaled Pelé v Croatia, not v Bolivia |
| 7896 | ❌ FAIL | non-unique negative (3 nations didn't score 5 in <30 min) |

## Batch rows 7901–8040 (Brazil) — 67 candidates — **63 PASS · 4 FAIL**
Very clean (opponent / elimination / stadium duplicates). Confirmed 2018 Mexico R16 win was at Samara Arena.
| Row | Verdict | Note |
|----:|:-------:|------|
| (63 rows) | ✅ PASS | elimination/opponent/stadium duplicates vs fact base |
| 7938 | ❌ FAIL | Neymar equaled Pelé v Croatia, not v Bolivia |
| 8005 | ❌ FAIL | Manaus v Uruguay was 4-1 (2-0 was Montevideo) |
| 8023 | ❌ FAIL | non-unique: Brazil faced neither Germany nor Argentina in 2022 KO |
| 8025 | ❌ FAIL | Brazil didn't draw Mexico in 2018 group (false premise) |

## Batch rows 8041–8182 (Brazil) — 104 candidates — **96 PASS · 8 FAIL** — FINAL BRAZIL BATCH
| Row | Verdict | Note |
|----:|:-------:|------|
| (96 rows) | ✅ PASS | manager/squad/result/why duplicates vs fact base |
| 8100,8129 | ❌ FAIL | Thiago Silva (not Neymar) captained 2018 & 2022 |
| 8102 | ❌ FAIL | Brazil didn't draw Mexico in 2018 group (false premise) |
| 8148 | ❌ FAIL | Manaus v Uruguay was 4-1 (2-0 was Montevideo) |
| 8152 | ❌ FAIL | 8 goals at 2022 WC, not 15 |
| 8165,8167 | ❌ FAIL | Neymar didn't win 2014 Bronze Ball (Robben) |
| 8169 | ❌ FAIL | Brazilian clubs had 23 Libertadores in 2023 (Argentina led with 25) |

# ✅ BRAZIL COMPLETE (rows 6097–8182)
- 1564 candidates in QA_PASSED.md checked: **1346 ship-ready** (QA_PASSED_ALL.md) + **218 dangerous**
  (QA_FAILED_LIVENESS_PASSED_OTHERS.md). 1346+218 = 1564 ✓ (on-disk verified, no dups).
- **Top recurring Brazil defect patterns** (for a dataset sweep):
  1. "Brazil scored **15** goals at 2022 WC" → actually **8**.
  2. "Neymar **equaled** Pelé v Bolivia (77th)" → he equaled v **Croatia 2022**; v Bolivia he **surpassed** (78th/79th).
  3. "beat Uruguay **2-0 in Manaus**" → Manaus was **4-1**; the 2-0 was away in Montevideo.
  4. "**0-0 v Mexico** in the 2018 group" → never happened (Mexico met only in the R16).
  5. Neymar **2014 Bronze Ball** → Robben won it (Neymar injured, no 2014 award).
  6. "**Richarlison 4 goals** at 2022" → 3; "**Raphinha scored** v S.Korea/Cameroon" → he scored 0.
  7. "**Fred started** in midfield at 2018" → reversed; Fred started in **2022**, fringe in 2018.
  8. Brazilian clubs "**24** Libertadores / led in 2023" → **23**, and Argentina led with **25**.
  9. **Thiago Silva** (not Neymar) captained 2018 & 2022.
  10. Excel score corruption (04-Jan=4-1, 02-Jan=2-1, 07-Jan=7-1, 01-Jul=7-1).
  11. Non-unique "in 2022 squad / 2026 key / 2026 manager / over-90-caps" rows (Vinícius/Jesus/Casemiro/Ancelotti/Thiago Silva).
- Next sequential country: **Australia** (rows 2161–3241).

---

# ===== CAMEROON (rows 9574–10745) — NEW METHOD (only QA_PASSED.md rows) =====
Separate contributor, started 2026-06-06. Country range 9574–10745 (1172 rows; 738 in QA_PASSED.md).

## Cameroon fact base (web-verified, reused across batches)
- **WC appearances: 8** (1982, 1990, 1994, 1998, 2002, 2010, 2014, 2022) — **most by any African nation**.
  **❗ Did NOT qualify for 2026** — lost the CAF playoff to **DR Congo** (Mbemba's late goal, Nov 2025).
  Any "Cameroon qualified/reached 2026" claim is FALSE.
- **2010 WC (Paul Le Guen):** group exit, lost all 3.
- **2014 WC (Volker Finke):** group exit, lost all 3 (Mexico 0-1, Croatia 0-4, Brazil 1-4); **Eto'o's
  farewell** (played 2 of 3, missed Croatia injured).
- **2018 WC:** FAILED to qualify.
- **2022 WC (Rigobert Song):** opener **lost 1-0 to Switzerland**; **drew Serbia 3-3** (Castelletto 29',
  Aboubakar 63', Choupo-Moting 66'); **beat Brazil 1-0** (Aboubakar header, then RED CARD for celebration —
  first African team to beat Brazil at a WC). Finished **3rd in Group G, 4 pts** (Brazil & Switzerland, 6
  each, advanced). André Onana first-choice GK (50+ caps). Squad incl. Castelletto, Toko Ekambi,
  Choupo-Moting, Zambo Anguissa, Aboubakar.
- **AFCON: 5 titles** (1984, 1988, 2000, 2002, 2017). **2017 final beat Egypt 2-1** (coach Hugo Broos).
- **2021 AFCON (HOSTED, played Jan–Feb 2022):** finished **3rd** — beat Burkina Faso **5-3 on pens** (3-3)
  in the 3rd-place playoff (coach Rigobert Song). **Aboubakar Golden Boot / top scorer (8 goals)**.
- **Samuel Eto'o:** **56 goals / 118 caps** (all-time top scorer); **African Footballer of the Year 4×**
  (2003, 2004, 2005, 2010). Now FECAFOOT president.
- **Managers:** Le Guen (2010), Volker Finke (2014), Hugo Broos (2017 AFCON), Rigobert Song (2022 WC +
  2021 AFCON). [Note: actual manager churn 2010–2022 was higher than 4.]
- **Stadiums (AFCON 2021 hosts):** Stade Olembe (Yaoundé, ~60,000, built for AFCON 2021), Stade Ahmadou
  Ahidjo (Yaoundé, ~40,000), **Stade Japoma (Douala, also a host)**, plus Bafoussam/Limbe/Garoua.

## Batch rows 9574–9680 (Cameroon) — 71 candidates — **65 PASS · 6 FAIL**
| Row | Verdict | Note |
|----:|:-------:|------|
| (65 rows) | ✅ PASS | WC/AFCON results, Eto'o stats, managers, stadiums, qualification |
| 9584,9628 | ❌ FAIL | "02-Jan" = corrupted "2-1" (2017 AFCON final) |
| 9588 | ❌ FAIL | "03-Mar" = corrupted "3-3" (Serbia draw) |
| 9619 | ❌ FAIL | Cameroon failed BOTH 2018 and 2026 (didn't qualify for 2026); explanation wrong |
| 9629 | ❌ FAIL | non-unique stadium (Japoma also hosted AFCON 2021) |
| 9652 | ❌ FAIL | Cameroon did NOT qualify for 2026 (lost CAF playoff to DR Congo) |

## Batch rows 9681–9820 (Cameroon) — 113 candidates — **96 PASS · 17 FAIL**
Heavy 2022-WC / 2017-AFCON duplicates. Big Excel-corruption cluster.
| Row | Verdict | Note |
|----:|:-------:|------|
| (96 rows) | ✅ PASS | 2022 results / 2017 AFCON / Eto'o / managers / stadiums |
| 9689,9756,9757,9758,9765,9769,9770,9771 | ❌ FAIL | "03-Mar" = corrupted "3-3" (Serbia) |
| 9755,9761,9762,9767,9776 | ❌ FAIL | "02-Jan" = corrupted "2-1" (2017 AFCON final) |
| 9711 | ❌ FAIL | non-unique (Cameroon failed both 2018 and 2026) |
| 9748,9801 | ❌ FAIL | non-unique (lost all 3 at both 2010 and 2014) |
| 9803 | ❌ FAIL | Cameroon did NOT qualify for 2026 |

## Batch rows 9821–9960 (Cameroon) — 40 candidates — **32 PASS · 8 FAIL**
| Row | Verdict | Note |
|----:|:-------:|------|
| (32 rows) | ✅ PASS | Aboubakar/Broos/Song, stadiums, 2017 AFCON, Mbeumo 2026 |
| 9835,9885,9917,9918 | ❌ FAIL | self-referential "like Cameroon → Cameroon" |
| 9840 | ❌ FAIL | "02-Jan" = corrupted "2-1" |
| 9850 | ❌ FAIL | "Brazil vs Switzerland" wasn't a draw (was 1-0; Germany 1-1 Spain was) |
| 9871 | ❌ FAIL | non-unique negative (3 nations not beaten in 2017 final) |
| 9888 | ❌ FAIL | non-unique (both Cameroon & Nigeria > Ghana in WC qualifications) |

## Batch rows 9961–10120 (Cameroon) — 85 candidates — **73 PASS · 12 FAIL**
Heavy player-ID duplicates (Mbeumo 2026 / Onana-Man Utd / Choupo-Moting veteran / Castelletto-Nkoulou
defenders / Eto'o & Aboubakar captains).
| Row | Verdict | Note |
|----:|:-------:|------|
| (73 rows) | ✅ PASS | player-identity duplicates vs fact base |
| 9984 | ❌ FAIL | non-unique (Nigeria/Morocco also qualified 2018, unlike Cameroon) |
| 9987 | ❌ FAIL | non-unique negative (Brazil & Switzerland games both not 3-3) |
| 10031,10033 | ❌ FAIL | non-unique "key 2022 attacker" (Aboubakar/Choupo-Moting also) |
| 10078,10080,10083,10084,10098,10099,10101,10102 | ❌ FAIL | non-unique "key 2022 forward (70+ caps)" (Aboubakar also fits) |

## Batch rows 10121–10300 (Cameroon) — 142 candidates — **140 PASS · 2 FAIL**
Massive near-identical duplicate block (Eto'o legend/farewell-2014/56-goals/captain · Song-2022 ·
Finke-2014 · Broos-2017 · Anguissa-Napoli · Onana-Man Utd · Aboubakar-2022-red-card · Mbeumo-2026).
| Row | Verdict | Note |
|----:|:-------:|------|
| (140 rows) | ✅ PASS | player/manager identity duplicates vs fact base |
| 10123 | ❌ FAIL | non-unique "40+ caps attacker" (Aboubakar/Choupo-Moting also) |
| 10150 | ❌ FAIL | Cameroon didn't play Croatia in 2022 (Group G: Switzerland/Serbia/Brazil) |

## Batch rows 10301–10500 (Cameroon) — 150 candidates — **147 PASS · 3 FAIL**
Another large duplicate block (Aboubakar-2022 / Eto'o-56-goals-4xAFOTY / Onana / Anguissa / stadiums /
2017 AFCON / 2021 AFCON Golden Boot).
| Row | Verdict | Note |
|----:|:-------:|------|
| (147 rows) | ✅ PASS | player/stadium/tournament identity duplicates vs fact base |
| 10327 | ❌ FAIL | Aboubakar WAS in the 2014 squad (scored their only goal) |
| 10370,10496 | ❌ FAIL | Cameroon did NOT qualify for 2026 (false 2026-CAF claims) |

## Batch rows 10501–10745 (Cameroon) — 137 candidates — **128 PASS · 9 FAIL** — FINAL BATCH
Manager/Embolo/Egypt/stadium duplicates + a 2026-qualification false-claim cluster.
| Row | Verdict | Note |
|----:|:-------:|------|
| (128 rows) | ✅ PASS | manager/result/stadium/Eto'o/Embolo duplicates vs fact base |
| 10651,10652,10659,10672,10723 | ❌ FAIL | Cameroon did NOT qualify for 2026 (false 2026 claims) |
| 10690 | ❌ FAIL | non-unique (CAF secured 2010, 2014 & 2022) |
| 10547 | ❌ FAIL | non-unique negative (didn't draw Switzerland/Brazil/Argentina) |
| 10589 | ❌ FAIL | self-referential + non-unique (2014 CAF qualifiers) |
| 10677 | ❌ FAIL | false "one year after Egypt" (2021 edition, next after Egypt 2019) |

**Cameroon running totals (rows 9574+): 681 PASS-ALL · 57 FAIL-LIVENESS.**

# ✅ CAMEROON COMPLETE (rows 9574–10745)
- New method (QA_PASSED.md pool only): **681 ship-ready** (QA_PASSED_ALL.md) + **57 dangerous**
  (QA_FAILED_LIVENESS_PASSED_OTHERS.md) = 738 candidates checked (matches QA_PASSED count).
- **Key country fact:** Cameroon did NOT qualify for 2026 (lost CAF playoff to DR Congo, Nov 2025) —
  the dataset assumed they had, producing a recurring false-premise cluster.
- Other recurring defects: Excel score corruption ("02-Jan"=2-1, "03-Mar"=3-3); non-unique
  "key 2022 forward/attacker" (Aboubakar fits); self-referential "like Cameroon → Cameroon";
  lost-all-3 in both 2010 & 2014 (non-unique when both offered); one false "Cameroon v Croatia 2022".

---

# ===== ECUADOR (rows 21580–22765) — NEW METHOD (only QA_PASSED.md rows) =====
Separate contributor, started 2026-06-07. Country range 21580–22765 (1186 rows; 782 in QA_PASSED.md).

## Ecuador fact base (web-verified, reused across batches)
- **WC appearances: 2002, 2006, 2014, 2022, and 2026** (missed 2010 & 2018). **✅ Ecuador DID qualify
  for 2026** (clinched 11 Jun 2025, 0-0 at Peru; "watertight" run under Beccacece) — despite a 3-point
  deduction for the Byron Castillo false-documents case. So "Ecuador qualified for 2026" rows are TRUE.
- **2006 WC (best result): Round of 16** — lost 1-0 to England (Beckham free kick, 60'). Beat Poland &
  Costa Rica in the group.
- **2014 WC (Reinaldo Rueda):** group-stage exit. **Enner Valencia scored all 3 Ecuador goals** (1 v
  Switzerland, 2 v Honduras).
- **2022 WC (Gustavo Alfaro), Group A:** beat **Qatar 2-0** (Valencia 2, the tournament's opening match/
  first goal, at Al Bayt), drew **Netherlands 1-1** (Valencia 49'), lost **Senegal 1-2** (**Caicedo 67'**
  scored Ecuador's goal). Group-stage exit (Netherlands & Senegal advanced). **Valencia scored 3 of
  Ecuador's 4 goals; Caicedo scored the other (their most recent WC goal)** — so "Valencia scored all
  their last goals" claims are FALSE.
- **Qualifying:** finished **4th in CONMEBOL** for both 2014 and 2022.
- **Copa América:** QF in **2016** (Centenario) and **2024**.
- **Managers:** Reinaldo Rueda (2014) · Gustavo Alfaro (2022) · Félix Sánchez Bas (2023–2024, **sacked**)
  · **Sebastián Beccacece (Aug 2024–, the 2026 manager)**. So "2026 manager = Sánchez Bas" is STALE/wrong.
- **Key players:** Enner Valencia (all-time top scorer, veteran); **Moisés Caicedo** (Chelsea, record SA
  midfielder fee, 2023); Pervis Estupiñán (LB, Brighton); Piero Hincapié; Gonzalo Plata; Jeremy Sarmiento.
- **Stadiums:** Estadio Rodrigo Paz Delgado / Casa Blanca (Quito, ~2,850 m altitude home) · Estadio
  Monumental Banco Pichincha (Guayaquil, ~57,267 — Ecuador's largest).

## Batch rows 21580–21680 (Ecuador) — 77 candidates — **72 PASS · 5 FAIL**
| Row | Verdict | Note |
|----:|:-------:|------|
| (72 rows) | ✅ PASS | 2022 results / 2014 / Copa QFs / managers / 4th-in-CONMEBOL / 2026 qualify |
| 21606,21640 | ❌ FAIL | "Valencia scored all Ecuador's last five WC goals" — false (Caicedo scored v Senegal) |
| 21618 | ❌ FAIL | stale manager — 2026 manager is Beccacece, not Sánchez Bas (sacked) |
| 21584 | ❌ FAIL | explanation false (Senegal LOST to the Netherlands, didn't win) |
| 21668 | ❌ FAIL | "01-Jan" = corrupted "1-1" (Netherlands draw) |

## Batch rows 21681–21850 (Ecuador) — 120 candidates — **111 PASS · 9 FAIL**
Heavy 2022-result duplicates (Qatar 2-0 / Netherlands 1-1 / Senegal 2-1) + Valencia/Caicedo/managers.
| Row | Verdict | Note |
|----:|:-------:|------|
| (111 rows) | ✅ PASS | 2022 results / Valencia / Caicedo-Chelsea / 4th CONMEBOL / 2026 qualify |
| 21754,21829,21830,21838 | ❌ FAIL | "01-Jan" = corrupted "1-1" (Netherlands) |
| 21842 | ❌ FAIL | "02-Jan" = corrupted "2-1" (Senegal) |
| 21791 | ❌ FAIL | false "Valencia's last five WC goals" run (Caicedo scored v Senegal) |
| 21732 | ❌ FAIL | Hincapié WAS a 2022 starter (claim "not yet key" false) |
| 21685,21740 | ❌ FAIL | stale: 2026 manager is Beccacece, not Sánchez Bas (sacked 2024) |

## Batch rows 21851–22030 (Ecuador) — 63 candidates — **57 PASS · 6 FAIL**
Almost all 2022-result/qualifying duplicates.
| Row | Verdict | Note |
|----:|:-------:|------|
| (57 rows) | ✅ PASS | 2022 results / 4th CONMEBOL / Copa QFs / Valencia / Hincapié-Leverkusen |
| 21880 | ❌ FAIL | false "Valencia's last five WC goals" run (Caicedo scored v Senegal) |
| 21891,21917,21918 | ❌ FAIL | non-unique negative "not draw" (Ecuador's only draw was NED; Qatar & Senegal both fit) |
| 21911 | ❌ FAIL | non-unique negative "did not eliminate" (NED & Qatar both) |
| 22013 | ❌ FAIL | self-referential (answer is Ecuador itself) |

## Batch rows 22031–22230 (Ecuador) — 142 candidates — **134 PASS · 8 FAIL**
Huge player-ID duplicate block (Hincapié-Leverkusen / Estupiñán-Brighton / Caicedo-Chelsea / managers).
| Row | Verdict | Note |
|----:|:-------:|------|
| (134 rows) | ✅ PASS | player/manager identity duplicates vs fact base |
| 22143,22144,22145,22170 | ❌ FAIL | stale: 2026 manager is Beccacece, not Sánchez Bas (sacked 2024) |
| 22106,22226 | ❌ FAIL | Sarmiento DID play at 2022 (sub in all 3 group games) |
| 22207 | ❌ FAIL | Caicedo's Chelsea move was Aug 2023, after the 2022 WC |
| 22228 | ❌ FAIL | non-unique "not in Germany" (Caicedo & Plata also not Germany-based) |

## Batch rows 22231–22430 (Ecuador) — 145 candidates — **136 PASS · 9 FAIL**
Overwhelmingly Valencia (opener brace / 2014 / top scorer) + Caicedo / stadium duplicates.
| Row | Verdict | Note |
|----:|:-------:|------|
| (136 rows) | ✅ PASS | Valencia opener brace v Qatar / NED goal / 2014 / top scorer; Caicedo; stadiums |
| 22276,22277,22278,22280,22281,22352,22375 | ❌ FAIL | false "Valencia scored all/all-five Ecuador WC goals" (Caicedo scored v Senegal) |
| 22326 | ❌ FAIL | wrong scorer — Caicedo (not Valencia) scored in the 2-1 Senegal loss |
| 22373 | ❌ FAIL | Caicedo's record Chelsea transfer was Aug 2023, not "a 2022 transfer" |

## Batch rows 22431–22765 (Ecuador) — 235 candidates — **215 PASS · 20 FAIL** — FINAL BATCH
Manager/result/altitude/club duplicates + a large stale-2026-manager cluster.
| Row | Verdict | Note |
|----:|:-------:|------|
| (215 rows) | ✅ PASS | managers / 2022 results / LDU-2008 / IDV-2022 / Quito altitude / stadiums |
| 22550,22551,22552,22553,22554,22555,22556,22574,22590,22630,22695,22700,22701,22703 | ❌ FAIL | stale: 2026 manager is Beccacece, not Sánchez Bas (present/future-tense "is leading/will lead") |
| 22627,22718 | ❌ FAIL | false "Valencia scored Ecuador's last five WC goals" (Caicedo scored v Senegal) |
| 22656,22657 | ❌ FAIL | non-unique negative ("not draw"/"not the decisive opponent") |
| 22449,22679 | ❌ FAIL | non-unique "matched 2014 qualification" (2022 also qualified) |

**Ecuador running totals (rows 21580+): 725 PASS-ALL · 57 FAIL-LIVENESS.**

# ✅ ECUADOR COMPLETE (rows 21580–22765)
- New method (QA_PASSED.md pool only): **725 ship-ready** (QA_PASSED_ALL.md) + **57 dangerous**
  (QA_FAILED_LIVENESS_PASSED_OTHERS.md) = 782 candidates checked (matches QA_PASSED count).
- **Key country facts:** Ecuador DID qualify for 2026 (clinched Jun 2025 under Beccacece). The dataset's
  recurring stale fact is "**Sánchez Bas is the 2026 manager**" — he was appointed for the cycle (2023)
  but **sacked in 2024**; **Sebastián Beccacece** led/clinched qualification, so present-tense "is the
  2026 manager" rows fail (past-tense "was appointed for the 2026 cycle" rows pass).
- Other recurring defects: false "**Valencia scored all/all-five Ecuador WC goals**" (Caicedo scored v
  Senegal, 2022 — Ecuador's most recent WC goal); one wrong "Valencia scored in the Senegal loss";
  Excel score corruption ("01-Jan"=1-1, "02-Jan"=2-1); non-unique negatives (Ecuador had exactly one
  2022 draw, so "which did Ecuador not draw with" is non-unique); Caicedo's Chelsea move mis-timed to
  2022 (it was Aug 2023); Sarmiento wrongly said to have missed 2022 (he subbed in all 3 games).

---

# ===== FRANCE (rows 25402–27324) — NEW METHOD (only QA_PASSED.md rows) =====
Separate contributor, started 2026-06-07. Country range 25402–27324 (1923 rows; 1413 in QA_PASSED.md — large).

## France fact base (web-verified, reused across batches)
- **WC honours:** 1998 champions (home, 3-0 v Brazil) · 2006 runners-up (lost to Italy on pens; Zidane
  headbutt) · 2018 **champions** (beat Croatia **4-2**; beat Argentina 4-3 in R16, Belgium 1-0 SF;
  Mbappé 4 goals aged 19) · 2022 **runners-up** (final v Argentina **3-3, lost 4-2 on pens**; Mbappé
  hat-trick — 2nd in a WC final after Hurst 1966; beat England 2-1 QF (Giroud winner), Morocco SF).
  · 2014 QF (lost 1-0 to Germany) · 2010 group-stage exit (Anelka sent home, squad mutiny/boycott).
  **✅ France qualified for 2026** (UEFA group winner) — so 2026-qualification rows are TRUE.
- **Coaches:** Domenech (2010) → **Laurent Blanc (2010–12, Euro 2012 QF)** → **Didier Deschamps
  (2012– , won 2018, runner-up 2022; contract extended through 2026)**.
- **All-time top scorer: OLIVIER GIROUD (57)** — passed Henry (51) during the 2022 WC (his 52nd v
  Poland R16); retired from int'l football July 2024. **Mbappé became 2nd all-time in 2025** (passed
  Henry), behind Giroud. So "France's all-time top scorer" = Giroud, not Mbappé/Henry.
- **Mbappé:** France **captain since Sept 2023** (youngest since Platini); **Real Madrid since 2024**
  (PSG before, since 2017); 2022 WC Golden Boot (8 goals).
- **Key players:** Lloris (record 145 caps, captain 2012–22, retired) → Maignan (GK from 2023);
  Griezmann (Euro 2016 Player of Tournament; **2018 WC Bronze Ball**); Pogba, Kanté, Varane, Benzema
  (recalled 2021; 2022 Ballon d'Or), Tchouaméni, Camavinga, Thuram, Dembélé, Kolo Muani.
- **Euros/NL:** Euro 2016 runners-up (hosts; lost final 1-0 to Portugal, at Stade de France) · Euro
  2020 R16 exit (blew 3-1 lead v Switzerland, lost on pens; Mbappé missed decisive pen) · **2021
  Nations League winners** (beat Spain 2-1 in the final) · Euro 2024 SF (lost to Spain).
- **⚠️ Watch:** 2018 **Fair Play Award went to SPAIN** (not France); 2018 Silver Ball = Hazard (Griezmann
  = Bronze); France's lowest FIFA ranking was **27th (2013)**, not "25th in 2010"; Excel score
  corruption ("03-Jan"=3-1, "04-Feb"=4-2).
- **Stadiums:** Stade de France (Saint-Denis, national stadium) · Parc des Princes · Stade Vélodrome —
  all hosted Euro 2016 (so "which ALSO hosted Euro 2016" is often non-unique). Clairefontaine = training base.

## Batch rows 25402–25500 (France) — 76 candidates — **61 PASS · 15 FAIL**
| Row | Verdict | Note |
|----:|:-------:|------|
| (61 rows) | ✅ PASS | 2018/2022 WC, Euros, Mbappé/Giroud/Deschamps, 2026 qualify |
| 25402,25403,25414,25416,25417 | ❌ FAIL | "25th in 2010" ranking unverified/wrong (low was 27th, 2013) |
| 25473,25476 | ❌ FAIL | 2018 Fair Play Award went to Spain, not France |
| 25482 | ❌ FAIL | Griezmann won the 2018 BRONZE Ball (Silver = Hazard) |
| 25467 | ❌ FAIL | France WON the 2021 NL final v Spain (no "2022 final lost to Spain") |
| 25447 | ❌ FAIL | non-unique (Stade de France & Parc des Princes also hosted Euro 2016) |
| 25408 | ❌ FAIL | Mbappé was already at PSG (from 2017), not "joined after 2018 WC" |
| 25434,25436,25437 | ❌ FAIL | "03-Jan" = corrupted "3-1" (v Switzerland) |
| 25443 | ❌ FAIL | "04-Feb" = corrupted "4-2" (2018 final) |

**France running totals (rows 25402+): 61 PASS-ALL · 15 FAIL-LIVENESS.**
**France sub-cursor: last verified row 25500 — resume at 25501.**

> **Correction:** row **25430** ("Euro 2016 France beat Germany 1-0") was initially mis-passed in this
> batch but the score was **2-0** (Griezmann brace) — moved to the FAIL file. Batch 1 net: **60 PASS · 16 FAIL**.

## Batch rows 25501–25640 (France) — 100 candidates — **85 PASS · 15 FAIL**
| Row | Verdict | Note |
|----:|:-------:|------|
| (85 rows) | ✅ PASS | 2018/2022 WC, Euros, NL 2021, Mbappé/Giroud/Griezmann, qualifying |
| 25510,25511,25518,25567,25615,25616,25621 | ❌ FAIL | false "France won all 10 Euro 2020 qualifiers" (lost 0-2 to Turkey; 8W-1D-1L) |
| 25564 | ❌ FAIL | Euro 2016 SF was 2-0 (Griezmann brace), not 1-0 |
| 25527 | ❌ FAIL | "25th in 2010" ranking unverified (low was 27th, 2013) |
| 25633 | ❌ FAIL | 2018 Fair Play Award went to Spain, not France |
| 25534 | ❌ FAIL | France WON the 2021 NL final v Spain (no "2022 final lost to Spain") |
| 25575 | ❌ FAIL | non-unique (PSG also missed 2016-17, Monaco) |
| 25526 | ❌ FAIL | unverified "no other UEFA group winner had 18 points" |
| 25554,25535 | ❌ FAIL | "03-Feb"=3-2 (Ukraine agg); "03-Mar"=3-3 (2022 final) |

## Batch rows 25641–25780 (France) — 107 candidates — **92 PASS · 15 FAIL**
| Row | Verdict | Note |
|----:|:-------:|------|
| (92 rows) | ✅ PASS | 2018/2022 WC, Euros, NL 2021, Mbappé/Giroud/Deschamps/Benzema/Varane |
| 25668,25686 | ❌ FAIL | Kolo Muani did NOT score France's 3rd goal in 2022 final (Mbappé's hat-trick) |
| 25698,25753 | ❌ FAIL | Euro 2016 SF was 2-0 v Germany, not 1-0 |
| 25642 | ❌ FAIL | non-unique (Monaco 2016-17 also won Ligue 1, besides Lille) |
| 25717 | ❌ FAIL | 2018 Fair Play Award went to Spain |
| 25762 | ❌ FAIL | France WON the 2021 NL final v Spain (no "2022 final lost") |
| 25768 | ❌ FAIL | false "France won all 10 Euro 2020 qualifiers" (lost 0-2 to Turkey) |
| 25757,25759 | ❌ FAIL | "25th in 2010" ranking unverified (low was 27th, 2013) |
| 25646,25656,25657,25659,25663 | ❌ FAIL | Excel score corruption (03-Mar/03-Jan/04-Feb/03-Feb) |

## Batch rows 25781–25920 (France) — 114 candidates — **86 PASS · 28 FAIL** (defect-dense)
| Row | Verdict | Note |
|----:|:-------:|------|
| (86 rows) | ✅ PASS | manager/result/Euro/NL/qualifying duplicates vs fact base |
| 25818,25819,25820,25825,25827,25832,25837,25838,25839,25840,25842,25845 | ❌ FAIL | Excel score corruption (04-Feb/03-Jan/04-Mar/02-Jan/03-Feb/03-Mar) |
| 25822,25823,25824,25868,25869,25870 | ❌ FAIL | "25th in 2010" ranking unverified (low was 27th, 2013) |
| 25828,25848,25859 | ❌ FAIL | Euro 2016 SF was 2-0 v Germany, not 1-0 |
| 25905,25906 | ❌ FAIL | 2018 Fair Play Award went to Spain |
| 25882,25883 | ❌ FAIL | France WON the 2021 NL final v Spain (no "2022 final lost") |
| 25903,25904,25920 | ❌ FAIL | false "France won all 10 Euro 2020 qualifiers" (lost 0-2 to Turkey) |

## Batch rows 25921–26060 (France) — 102 candidates — **87 PASS · 15 FAIL**
Heavy Lloris/Deschamps/Varane/Thuram/Saliba/Umtiti duplicates.
| Row | Verdict | Note |
|----:|:-------:|------|
| (87 rows) | ✅ PASS | captain/manager/defender/forward identity duplicates vs fact base |
| 25954,26015,26017,26051,26056,26057,26058 | ❌ FAIL | Lloris NOT in the 2018 WC All-Star Team (Courtois was the GK) |
| 25923,25928 | ❌ FAIL | Kolo Muani did NOT score France's 3rd goal in 2022 final (Mbappé hat-trick) |
| 25992 | ❌ FAIL | 2018 Fair Play Award went to Spain |
| 26023,26059 | ❌ FAIL | false "perfect 10-win Euro 2020 qualifying" (lost 0-2 to Turkey) |
| 26000 | ❌ FAIL | "04/03/2003" = corrupted "4-3-3" formation |
| 25964,25968 | ❌ FAIL | non-unique negatives ("not faced in 2014 playoff"/"2018 match not won") |

## Batch rows 26061–26200 (France) — 115 candidates — **108 PASS · 7 FAIL**
Overwhelmingly Deschamps manager duplicates (longest-serving / 100+ wins / 2026 contract / 4-3-3).
| Row | Verdict | Note |
|----:|:-------:|------|
| (108 rows) | ✅ PASS | Deschamps/Domenech/Blanc + Pogba/Tchouaméni/Koundé/Mbappé/Giroud/Kolo Muani duplicates |
| 26085,26096,26102,26108 | ❌ FAIL | false "perfect 10-win Euro 2020 qualifying" (lost 0-2 to Turkey) |
| 26195,26196 | ❌ FAIL | Lloris NOT in the 2018 WC All-Star Team (Courtois was GK) |
| 26194 | ❌ FAIL | Neymar isn't French; Mbappé (French) also joined PSG in 2017 |

## Batch rows 26201–26340 (France) — 108 candidates — **102 PASS · 6 FAIL**
Heavy player duplicates (Mbappé/Giroud/Griezmann/Lloris/Anelka-2010/Henry-handball/Kolo Muani).
| Row | Verdict | Note |
|----:|:-------:|------|
| (102 rows) | ✅ PASS | player identity/award/2010-mutiny duplicates vs fact base |
| 26245 | ❌ FAIL | Kolo Muani did NOT score France's 3rd goal in 2022 final (Mbappé hat-trick) |
| 26228 | ❌ FAIL | Mbappé scored a hat-trick (3) in the 2022 final, not "four goals" |
| 26274,26300,26303 | ❌ FAIL | Griezmann won the 2018 BRONZE Ball (Silver = Hazard) |
| 26232 | ❌ FAIL | self-contradictory (Mbappé's 2 R16 goals < Griezmann's 4 total) |

## Batch rows 26341–26480 (France) — 106 candidates — **99 PASS · 7 FAIL**
Club (PSG/Lille/Monaco/Lyon)/assistant/Benzema/Varane duplicates.
| Row | Verdict | Note |
|----:|:-------:|------|
| (99 rows) | ✅ PASS | club/Guy Stéphan/Lloris/Varane/Benzema/Mbappé-Monaco duplicates |
| 26348,26350 | ❌ FAIL | false "perfect 10-win Euro 2020 qualifying" (lost 0-2 to Turkey) |
| 26392 | ❌ FAIL | Lloris NOT in the 2018 WC All-Star Team (Courtois was GK) |
| 26408,26409,26429 | ❌ FAIL | non-unique "broke PSG's run" (Monaco 2016-17 also; only 2020-21-scoped rows pass) |
| 26472 | ❌ FAIL | non-unique (Parc des Princes & Stade de Lyon also hosted Euro 2016, not qualifier homes) |

## Batch rows 26481–26620 (France) — 98 candidates — **88 PASS · 10 FAIL**
Lloris/Deschamps/Guy Stéphan + Tchouaméni/Camavinga/Kanté/Pogba midfielder duplicates.
| Row | Verdict | Note |
|----:|:-------:|------|
| (88 rows) | ✅ PASS | GK/manager/midfielder identity duplicates vs fact base |
| 26493,26494,26496,26502,26504 | ❌ FAIL | Lloris NOT in the 2018 WC All-Star Team (Courtois was GK) |
| 26551,26552,26594 | ❌ FAIL | Camavinga debuted for France in 2020 (WC 2022), not the 2023/2026 cycle |
| 26515 | ❌ FAIL | false "perfect 10-win Euro 2020 qualifying" |
| 26553 | ❌ FAIL | non-unique (both Pogba & Kanté missed the 2022 WC; neither started the final) |

## Batch rows 26621–26760 (France) — 96 candidates — **88 PASS · 8 FAIL**
Giroud/Mbappé/Griezmann/Lloris/Benzema duplicates.
| Row | Verdict | Note |
|----:|:-------:|------|
| (88 rows) | ✅ PASS | top-scorer/award/captain/2018-2022 duplicates vs fact base |
| 26680,26681,26704 | ❌ FAIL | Mbappé scored a hat-trick (3) in the 2022 final, not "four" |
| 26653,26654 | ❌ FAIL | Griezmann was 3rd/Bronze Ball at 2018, not 2nd/Silver |
| 26648,26649 | ❌ FAIL | non-unique "did not become top scorer" (Mbappé, Benzema & Griezmann all didn't) |
| 26661 | ❌ FAIL | Lloris NOT in the 2018 WC All-Star Team (Courtois was GK) |

## Batch rows 26761–26920 (France) — 119 candidates — **95 PASS · 24 FAIL** (defect-dense)
| Row | Verdict | Note |
|----:|:-------:|------|
| (95 rows) | ✅ PASS | player/stadium identity duplicates vs fact base |
| 26782,26783,26798,26802,26803,26820,26825,26843,26853,26915 | ❌ FAIL | "Griezmann 2018 Silver Ball" — he won BRONZE (Silver = Hazard) |
| 26770,26827,26832 | ❌ FAIL | Lloris NOT in the 2018 WC All-Star Team (Courtois) |
| 26872,26883,26884,26888,26890 | ❌ FAIL | non-unique "which stadium hosted Euro 2016" (multiple venues did) |
| 26845,26846 | ❌ FAIL | Mbappé scored a hat-trick (3) in the 2022 final, not "four" |
| 26869 | ❌ FAIL | 2018 SF (1-0) was lower than Euro 2016 SF (2-0); explanation garbled |
| 26870 | ❌ FAIL | "25th in 2010" ranking unverified (low was 27th, 2013) |
| 26905,26907 | ❌ FAIL | non-unique PSG-signing (Bernardo Silva too); Neymar isn't French |

## Batch rows 26921–27080 (France) — 113 candidates — **101 PASS · 12 FAIL**
Opponent/result/striker duplicates.
| Row | Verdict | Note |
|----:|:-------:|------|
| (101 rows) | ✅ PASS | result/opponent/striker duplicates vs fact base |
| 26923,26968,26969,26975 | ❌ FAIL | "Neymar = French star" (he's Brazilian) |
| 27010,27013,27048 | ❌ FAIL | France WON the 2021 NL final v Spain (no "2022 final lost") |
| 26949,26950 | ❌ FAIL | false "perfect 10-win Euro 2020 qualifying" |
| 27016 | ❌ FAIL | Euro 2016 SF was 2-0 v Germany, not 1-0 |
| 26989,27052 | ❌ FAIL | non-unique negatives ("not lead at Qatar"/"not face in 2014 playoff") |

## Batch rows 27081–27324 (France) — 159 candidates — **146 PASS · 13 FAIL** — FINAL BATCH
Opponent/qualifier/stadium duplicates.
| Row | Verdict | Note |
|----:|:-------:|------|
| (146 rows) | ✅ PASS | result/opponent/qualifier/stadium duplicates vs fact base |
| 27197,27201,27203 | ❌ FAIL | false "perfect 10-win Euro 2020 qualifying" |
| 27149,27153,27253 | ❌ FAIL | France WON the 2021 NL final v Spain (no "2022 final lost") |
| 27241,27281,27324 | ❌ FAIL | "25th in 2010" ranking unverified (low was 27th, 2013) |
| 27097,27299 | ❌ FAIL | 2018 Fair Play Award went to Spain, not France |
| 27321 | ❌ FAIL | Lloris NOT in the 2018 WC All-Star Team (Courtois) |
| 27261 | ❌ FAIL | Mbappé scored a hat-trick (3) in the 2022 final, not "four" |

**France running totals (rows 25402+): 1237 PASS-ALL · 176 FAIL-LIVENESS.**

# ✅ FRANCE COMPLETE (rows 25402–27324)
- New method (QA_PASSED.md pool only): **1237 ship-ready** (QA_PASSED_ALL.md) + **176 dangerous**
  (QA_FAILED_LIVENESS_PASSED_OTHERS.md) = 1413 candidates checked (matches QA_PASSED count).
  [NB: row 25430, initially mis-passed, was corrected to FAIL — net counts above are accurate on disk.]
- **France DID qualify for 2026** (UEFA group winner), so 2026-qualification rows pass.
- **Recurring dataset defects (high volume):** (1) "**Griezmann 2018 Silver Ball**" — he won the BRONZE
  (Silver = Hazard); (2) "**Lloris in the 2018 All-Star Team**" — Courtois (Golden Glove) was the GK;
  (3) "**France perfect 10-win Euro 2020 qualifying**" — they lost 0-2 to Turkey (8W-1D-1L); (4) "**2018
  Fair Play Award → France**" — it went to Spain; (5) "**France lost the 2022 Nations League final to
  Spain**" — France WON the 2021 NL final v Spain; (6) "**25th in 2010 FIFA ranking**" — documented low
  was 27th (2013); (7) "**Euro 2016 SF France 1-0 Germany**" — it was 2-0 (Griezmann brace); (8) "**Mbappé
  4 goals in the 2022 final**" — it was a hat-trick (3); (9) "**Kolo Muani scored France's 3rd in the 2022
  final**" — Mbappé did (Kolo Muani's shot was saved); (10) "**Neymar = French star**" (he's Brazilian);
  (11) Excel score corruption (03-Jan/04-Feb/03-Mar/02-Jan/04-Mar/04/03/2003); (12) non-unique "broke
  PSG's run" (Monaco 2016-17 also) and "which stadium hosted Euro 2016" (multiple venues).
