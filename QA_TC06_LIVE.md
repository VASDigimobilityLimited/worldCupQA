# QA — TC-06 Live Factual Check (web-sourced, one-by-one)

Per-row factual verification of `answer` + `explanation` against live web sources
(Wikipedia / FIFA as tie-breaker, plus ESPN, Al Jazeera, CAF, etc.). Processed in
dataset order; **resumable** — the "Last verified row" marker below is the cursor.

- **PASS** = answer and explanation both factually correct per a cited source.
- **FAIL** = answer wrong, explanation wrong, or the question asserts an event that
  did not happen.
- **UNVERIFIED** = could not confirm from reliable sources → treated as FAIL
  (conservative; a competitive quiz must not ship unverified facts).

**Last verified row: 30309 — all claimed countries through Ghana verified.**
**Algeria (2–1228) COMPLETE. Argentina (1229–2160) COMPLETE. Australia (2161–3241) COMPLETE. Austria (3242–4282) COMPLETE. Cabo Verde (8183–9573) COMPLETE. Canada (10746–12428) COMPLETE. Costa Rica (15528–16571) COMPLETE. Côte d'Ivoire (16572–17486) COMPLETE. Croatia (17487–19101) COMPLETE. Denmark (19102–20581) COMPLETE. DR Congo (20582–21579) COMPLETE. England (23687–25401) COMPLETE. Ghana (29166–30309) COMPLETE.**
**BRAZIL in progress (rows 6097–8182), separate contributor — verified to 6760, resume 6761. Brazil sub-cursor at bottom of file.**
**Skipped/not started: Belgium, Cameroon, Chile, Colombia, Ecuador, Egypt, France, Germany, and all countries after Ghana. Next unclaimed country: ask the user before beginning a new country.**

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

**Brazil running totals (rows 6097+): 454 PASS-ALL · 73 FAIL-LIVENESS.**
**Brazil sub-cursor: last verified row 6760 — resume at 6761.**

- **Australia batch 2161–2240** (61 candidates): 51 PASS / 10 FAIL. FAIL: 2164 (self-ref), 2168 (14th was Sept-2009 not Apr-2023), 2175 & 2230 (2011 Asian Cup = final not semis), 2196 (first R16 was 2006), 2216 (host-winners ≥5: omits Kuwait 1980/Qatar 2023), 2227 (first AFC qualifier 2008 not 2006), 2228 (non-unique: 2018 & 2022 both intercontinental playoffs), 2235 (`02-Jan`=2-1), 2238 (Uruguay playoff was 2006 not 2010).
- **Australia batch 2241–2320** (69 candidates): 54 PASS / 15 FAIL. FAIL: 2250 (2006 not WC debut; 1974), 2255 (non-unique; Japan also 2006–2026), 2259/2261/2303 (14th was Sep-2009 / SK 17th was 1998), 2260 (Cahill record 5-Mar-2014 not 2018 cycle), 2270/2272/2273 (non-unique direct-AFC: 2010/2014/2026), 2289 (now 5 WCs incl 2026), 2296 (unverifiable '10 players'), 2307 (`01-Jan`=1-1), 2314 (drew Ghana not lost), 2315/2317 (`02-Jan`=2-1).
- **Australia batch 2321–2400** (66 candidates): 57 PASS / 9 FAIL. FAIL: 2328 (2022 Saudi qualifier was CommBank Sydney not AAMI Park), 2334 (first AAMI Park WCQ was Feb-2012/2014-cycle), 2340 (Hrustic didn't score at 2022 finals), 2342 (Cahill first intl goal 2004 vs Tahiti), 2360 (Greece Jun-2016 was a friendly), 2376/2377/2381 (now 5 WCs incl 2026), 2394 (unverifiable '26.8 yrs').
- **Australia batch 2401–2480** (64 candidates): 52 PASS / 12 FAIL. FAIL: 2408/2410/2411/2413 (date corruption), 2426 (first Chile WC was 1974), 2429 & 2432 (AAMI Park venue — games were abroad/Sydney), 2443 (2014 WC secured in 2013), 2451 (qualified Jun-2025 not 2026), 2452/2467/2471 (non-unique: SF in 2011 & 2015). Also corrected the reason on row 2230 (non-unique, not false-premise).
- **Australia batch 2481–2560** (38 candidates): 30 PASS / 8 FAIL. FAIL: 2488 (2011=final not SF), 2498 (Leckie in 2026 squad, never retired), 2508 (Goodwin not in 2015 squad; ans=Leckie), 2513 (Leckie=Melbourne City), 2518 (SK also reached 2022 R16), 2536 (Qatar host-win was 2023 not 2019/UAE), 2538 (SK/UAE not 2022 opponents), 2555 (Japan also reached 2010 R16).
- **Australia batch 2561–2640** (71 candidates): 65 PASS / 6 FAIL. FAIL: 2591 (Postecoglou resigned after completing 2018 qualifying), 2609 (Osieck not Postecoglou won 2014 qual), 2626/2627/2628 (Hrustic didn't score at 2022 finals), 2637 (Arzani debuted vs Czech Rep abroad, not Hungary/AAMI Park).
- **Australia batch 2641–2720** (69 candidates): 59 PASS / 10 FAIL. FAIL: 2646/2655 (Hrustic didn't score), 2652/2662/2673/2697 (Argentina goal = Enzo Fernández OG not Goodwin), 2666 (Goodwin not in 2015 squad), 2679 (Kennedy decisive goal was 2014 vs Iraq), 2683 (2006 WC in Germany not Stadium Australia), 2696 (Redmayne saved decisive pen, didn't score).
- **Australia batch 2721–2800** (59 candidates): 49 PASS / 10 FAIL. FAIL: 2721 (Lawrence Thomas/WSW not in 2022 squad), 2746 (Ryan was 1st-choice at 2014), 2756/2765/2767/2768 (Hrustic didn't score), 2779/2782 (Irvine WAS in 2018 squad), 2798 (Arzani not AAMI Park), 2800 (2004 not a WC year).
- **Australia batch 2801–2880** (65 candidates): 59 PASS / 6 FAIL. FAIL: 2806 (Viduka scored 0 WC goals not 2), 2825 (Leckie didn't score decisive Peru pen — Redmayne saved), 2835/2864 (Argentina goal = own goal), 2852/2853 (Cahill scored in 3 tournaments not 4; none in 2018).
- **Australia batch 2881–2960** (73 candidates): 61 PASS / 12 FAIL (all venue errors). FAIL: 2932/2933/2940/2941/2945/2946 (Peru playoff was in QATAR not Australia), 2934 (Saudi 2021=Sydney), 2948/2950 (Japan 2022=Sydney), 2928 (2015 QF vs China=Brisbane), 2929 (2017 Saudi=Adelaide), 2953 (2023 Asian Cup=Qatar).
- **Australia batch 2961–3040** (61 candidates): 57 PASS / 4 FAIL. FAIL: 2971 (2006 not WC debut), 2992 (qualified for 2006 via OFC, left after), 3011 (Popovic not Arnold secured 2026), 3016 (2014 qualification was successful not failed).
- **Australia batch 3042–3140** (63 candidates): 54 PASS / 9 FAIL. FAIL: 3049 (first 2006 match=Japan not Brazil), 3081 (non-unique: 2010 & 2014 both direct AFC), 3083/3100 (2011 furthest=final not SF), 3093/3095 (Peru playoff in Qatar), 3096 (Saudi 2022=Sydney), 3097 (no AFC qualifier in 2006), 3124 (SK didn't play Aus in 2022).
- **Australia batch 3141–3241** (76 candidates): 66 PASS / 10 FAIL. FAIL: 3150 (Peru playoff in Qatar), 3155/3156 (drew Ghana not lost), 3159 (2006 also R16 → non-unique best), 3161/3162/3163 (non-unique direct-AFC), 3178 (qualified 2017 not 2018), 3213/3239 (2006 was OFC not AFC).
- **✅ AUSTRALIA COMPLETE (rows 2161–3241): 714 PASS / 121 FAIL of 835 QA_PASSED candidates.** Next country: Austria (3242).

---

## Côte d'Ivoire (rows 16572–17486) — separate contributor (azibabari)

Liveness run on the **542** Côte d'Ivoire rows present in `QA_PASSED.md`. Fact base: 3 World Cups
(2006/2010/2014, all group-stage exits; **missed 2018 & 2022**; **qualified for 2026** as CAF Group F
winners, unbeaten 8W-2D, 25–0 GD); **3 AFCON titles** (1992, 2015 v Ghana 9–8 pens, **2023 as hosts**
v Nigeria 2–1 after nearly exiting the group stage — Gasset sacked mid-tournament, Emerse Faé took over;
Kessié 62' + Haller 81'); Drogba record scorer **65 goals** (last WC goal 2010, none in 2014); Yaya Touré
**101 caps** (debuted at 2006 WC); Pépé 53 caps; Adingra **2023 Best Young Player**.

**Recurring CIV defect clusters:** (1) **fake "2022 World Cup" questions** — CIV did not qualify, so any
"2022 World Cup squad/match/finals" framing is a false premise (≈25 fails); (2) **mangled score cells**
(`02-Jan`=2-1, `09-Aug`=9-8); (3) **non-unique** "scored in 2023 final" (Kessié also scored), CAF-qual
year (2010/2014/2026 all CAF), multiple 2010 CAF co-qualifiers (Ghana/Nigeria/Cameroon/Algeria); (4)
**Drogba 2014 goal** false premise (he scored none in 2014); (5) self-referential 2023-champion/host rows.

| Batch (rows) | Candidates | PASS | FAIL |
|--------------|-----------:|-----:|-----:|
| 16573–16698 | 90 | 76 | 14 |
| 16699–16882 | 95 | 83 | 12 |
| 16883–17017 | 95 | 82 | 13 |
| 17018–17151 | 95 | 81 | 14 |
| 17152–17358 | 95 | 80 | 15 |
| 17363–17485 | 72 | 61 | 11 |
| **TOTAL** | **542** | **463** | **79** |

**✅ CÔTE D'IVOIRE COMPLETE (rows 16572–17486): 463 PASS / 79 FAIL of 542 QA_PASSED candidates.**

---

## Croatia (rows 17487–19101) — separate contributor (azibabari)

Liveness run on the **1188** Croatia rows in `QA_PASSED.md`. Fact base: WC 1998 (3rd), 2002/2006/2014
(group), **2018 runners-up** (lost final 4-2 to France; Modrić Golden Ball + 2018 Ballon d'Or; Mandžukić
OG+goal & SF winner v England 2-1 AET; Perišić scored once in the final; beat Denmark & Russia on pens),
**2022 third place** (beat Morocco 2-1; beat Japan & Brazil on pens, Livaković heroics; lost SF 3-0 to
Argentina; Gvardiol scored 3rd-place); **missed 2010** (3rd in group — NO playoff); **qualified 2026 by
winning the group** (2022 also a direct group win; only 2014/2018 were playoffs — Iceland, Greece, both won).
Euros best = QF 1996/2008; **Euro 2024 group exit W0-D2-L1** (lost Spain 0-3, drew Albania 2-2 & Italy 1-1).
**Lost the 2022-23 Nations League FINAL to Spain on pens** (beat Netherlands only in the semi). Modrić
most-capped (196 by 2026, ~160 in 2022, ~120 in 2018), b. Sept 1985 (37 at 2022 WC, 40 at 2026). Dalić
manager since Oct 2017; Čačić (Euro 2016), Kovač (2013-15/2014 WC), Bilić (Euro 2008/2010 quals).

**Recurring Croatia defect clusters (154 fails):**
1. **False 2023 Nations League "win"** (~35 rows) — Croatia LOST the final to Spain; the Netherlands was the SEMI. Any "won the NL / beat the Netherlands in the final" is wrong.
2. **Fabricated 2010 playoff loss to Ukraine** (~13 rows) — Croatia missed 2010 by finishing 3rd in their group; there was no playoff.
3. **Euro 2024 errors** (~11 rows) — "beat Albania" / "lost to Spain AND Italy" are false: only loss was Spain; Albania & Italy were draws.
4. **"Lost to Cameroon" in 2014** (~7 rows) — Croatia beat Cameroon 4-0; they lost only to Brazil & Mexico.
5. **Gvardiol = 2022 Best Young Player** (~7 rows) — that award went to Enzo Fernández.
6. **Modrić age/caps** — 37 (not 39) at 2022 WC, 40 at 2026; ~160 caps (not 175+) by 2022.
7. **Date/formation corruption** — `02-Jan`=2-1, `04-Feb`=4-2, `09-Aug`=9-8, `03-Jan`=3-1, `04/03/2003`=4-3-3.
8. **"Only team to win all 3 groups in 2018"** — Belgium & Uruguay also did.
9. **Misc** — Perišić "scored twice" in 2018 final (once), Croatia "won the final" (lost), self-referential and non-unique items.

| Batch (rows) | PASS | FAIL |
|--------------|-----:|-----:|
| 17487–17609 | 83 | 17 |
| 17611–17750 | 102 | 8 |
| 17752–17894 | 92 | 18 |
| 17895–18028 | 95 | 15 |
| 18030–18164 | 100 | 10 |
| 18165–18326 | 101 | 9 |
| 18327–18465 | 98 | 12 |
| 18466–18626 | 103 | 7 |
| 18627–18782 | 93 | 17 |
| 18783–18964 | 90 | 20 |
| 18965–19100 | 67 | 21 |
| **TOTAL** | **1034** | **154** |

**✅ CROATIA COMPLETE (rows 17487–19101): 1034 PASS / 154 FAIL of 1188 QA_PASSED candidates.**

---

## Denmark (rows 19102–20581) — separate contributor (azibabari)

Liveness run on the **1041** Denmark rows in `QA_PASSED.md`. Fact base: WC 2010 (group exit), 2018 (R16,
lost Croatia on pens; mgr Hareide; 5 group pts), 2022 (group exit, 0 wins/1 pt; lost Australia 1-0 & France
2-1, drew Tunisia; mgr Hjulmand); **missed 2006, 2014, and — crucially — 2026** (lost the UEFA playoff final
to Czechia 2-2, 3-1 pens, 31 Mar 2026). Euro 1992 champions; **Euro 2020 semi-final** (Eriksen cardiac
arrest v Finland; beat Russia 4-1 / Wales 4-0 / Czechia 2-1; lost England 2-1 AET; Kjær's heroics → 2021
Ballon d'Or nom, 18th); Euro 2024 R16 (lost Germany 2-0). Top scorers Tomasson & Poul Nielsen 52 (joint);
Eriksen ~41 (5th). Managers: **Riemer (2024–, leads 2026 cycle)**, Hjulmand (2020–24), Hareide (2016–20),
Morten Olsen (2000–15). Home venue **Parken Stadium, Copenhagen**; **DBU HQ is in BRØNDBY** (not Copenhagen).
Højlund **now plays for Napoli/Serie A** (permanent 3 Jun 2026), not Manchester United.

**Recurring Denmark defect clusters (182 fails):**
1. **DBU HQ "in Copenhagen"** (~40) — it's in **Brøndby** (often even offered as a distractor).
2. **"Telia Parken" distractor** (~35) — that IS Parken Stadium (2014-2020 sponsor name) → non-unique.
3. **"Hjulmand leads/manages the 2026 cycle"** (~35) — he resigned July 2024; **Brian Riemer** leads 2026.
4. **"Eriksen is 2nd-highest scorer"** (~25) — he's **5th** (~41 goals; Tomasson & Nielsen lead on 52).
5. **"Denmark qualified for 2026"** (~12) — FALSE; they lost the playoff to Czechia. (Squad-composition "2026 cycle" facts were PASSED as the qualifying squad is real.)
6. **"40+ goals" non-unique** when Tomasson (52) is a distractor.
7. **"peak/highest FIFA ranking 10th"** — Denmark's all-time peak is **6th** (1996); 10th was only a 2022 high (rows scoped to "in 2022" passed).
8. **Højlund "plays for Manchester United"** — he moved to **Napoli (Serie A)**; also flips "Serie A not represented" rows.
9. **Date corruption** (`02-Jan`=2-1, `04-Jan`=4-1, `01-Jan`=1-1) and **wrong cap stats** (Kjær ~115 not 130+ in 2022; Poulsen ~35 not 70 in 2018).
10. **Misc** — self-referential ("which nation… → Denmark") and non-unique items.

| Batch (rows) | PASS | FAIL |
|--------------|-----:|-----:|
| 19102–19240 | 89 | 11 |
| 19241–19397 | 90 | 25 (+1 corr. to 19145) |
| 19398–19535 | 101 | 14 |
| 19536–19697 | 82 | 38 |
| 19698–19854 | 104 | 16 |
| 19857–20021 | 93 | 27 |
| 20022–20175 | 100 | 20 (+4 corr. to earlier) |
| 20176–20380 | 109 | 11 |
| 20381–20580 | 95 | 16 |
| **TOTAL** | **859** | **182** |

**✅ DENMARK COMPLETE (rows 19102–20581): 859 PASS / 182 FAIL of 1041 QA_PASSED candidates.**

---

## DR Congo (rows 20582–21579) — separate contributor (azibabari)

Liveness run on the **586** DR Congo rows in `QA_PASSED.md`. Fact base: DR Congo (Léopards; formerly
**Zaire**). Only prior WC was **1974 as Zaire** (lost all 3, 0 goals; Mwepu Ilunga's free-kick incident).
**QUALIFIED for 2026** — first under the name DR Congo, first in 52 years — via the **intercontinental
playoff** (beat Nigeria in the CAF playoff Nov 2025, then Jamaica 1-0 AET, 31 Mar 2026; Tuanzebe scored)
under **Sébastien Desabre**; did NOT qualify 2006/2010/2014/2018/2022. **2 AFCON titles** (1968 v Ghana,
1974 v Zambia). **2015 AFCON semis** (mgr Florent Ibenge); **2023 AFCON 4th** — reached the SEMIS (lost SF
1-0 to Ivory Coast, then 3rd-place to South Africa on pens), mgr **Desabre** (not Ibenge). Top scorer
Mbokani (22), Bakambu (21, 40+ caps), captain Mbemba (107 caps, **now Lille** — was Marseille), Wissa
(**now Newcastle** — was Brentford), Silas (Stuttgart/Bundesliga). Home: Stade des Martyrs, Kinshasa
(~80,000). TP Mazembe: 2010 Club World Cup final + CAF Champions League 2009/2010/2015.

**Recurring DR Congo defect clusters (127 fails):**
1. **2023 AFCON = "quarter-finals"** — they reached the **SEMI-finals** (4th place). Many rows assert QF.
2. **Self-referential** "which nation/team/who, like DR Congo, …? → DR Congo" (~30 rows).
3. **2018/2022 World Cup false premises** — DR Congo were not at those finals ("at the 2018/2022 WC, who…").
4. **Outdated clubs** — Wissa now at **Newcastle** (not Brentford), Mbemba now at **Lille** (not Marseille). Present-tense club claims fail; "Premier League player" and past-tense "played for X in 2023/2024" pass.
5. **Outdated "never qualified under current name"** — DR Congo HAVE now qualified (2026).
6. **Misc** — Desabre (not Ibenge) managed the 2023 AFCON; Bundesliga IS represented (Silas/Stuttgart); DR Congo don't "consistently struggle" at AFCON (2 titles, recent semis); TP Mazembe's 3 *modern* CAF CL titles (2009/2010/2015) treated as defensible; non-unique items.

**NOTE — what was PASSED (not failed):** squad-composition "2026 cycle/qualifying/squad" facts (the
qualifying squad is real), and the "first WC under the current name = 2026 / first in 52 years" framing
(accurate — 1974 was as Zaire). Only explicit *finals participation in 2018/2022* and *outdated* facts failed.

| Batch (rows) | PASS | FAIL |
|--------------|-----:|-----:|
| 20582–20761 | 78 | 22 (+2 later un-failed: TP Mazembe count) |
| 20762–21008 | 88 | 32 |
| 21009–21164 | 104 | 16 |
| 21165–21376 | 94 | 26 |
| 21377–21576 | 95 | 31 |
| **TOTAL** | **459** | **127** |

**✅ DR CONGO COMPLETE (rows 20582–21579): 459 PASS / 127 FAIL of 586 QA_PASSED candidates.**
# AUSTRIA (rows 3242–4282) — NEW METHOD (only QA_PASSED.md rows)

761 Austria rows are in QA_PASSED.md. Started at user's request (row 3242), skipping
Argentina & Australia (still unclaimed). Fact base built from live sources:
- Euro appearances: **2008** (co-host, group exit), **2016** (group exit), **2020** (R16,
  lost 2-1 to Italy a.e.t.), **2024** (R16). → first-ever Euro group stage = **2008**, not 2016.
- **Euro 2024:** beat Netherlands **3-2** in the group stage (won Group D), lost R16 to
  **Türkiye 2-1** (Demiral 2, Gregoritsch). Manager **Ralf Rangnick** (pressing style).
- Missed the **2018 and 2022** World Cups.
Sources: [Austria at the Euros (Wikipedia)](https://en.wikipedia.org/wiki/Austria_at_the_UEFA_European_Championship),
[CBC — Türkiye 2-1 Austria, 2 Jul 2024](https://www.cbc.ca/sports/soccer/european-championship-soccer-roundup-july2-1.7252081).

## Batch rows 3242–3289 (Austria) — 34 candidates. Result: 30 PASS · 4 FAIL.

| Row | Verdict | Note |
|----:|:-------:|------|
| 3242,3254,3255,3264 | ✅ PASS | Euro 2024 R16 loss to Türkiye 2-1 |
| 3243,3258,3263,3272,3278,3280,3282 | ✅ PASS | Rangnick pressing transformation, Euro 2024 |
| 3244 | ✅ PASS | missed 2018 & 2022 WCs |
| 3245,3274 | ✅ PASS | Euro 2016 group-stage exit (3274: most recent group-only) |
| 3250 | ✅ PASS | Euro 2020 R16, lost 2-1 to Italy a.e.t. |
| 3252,3253,3256,3257,3260,3261,3265,3269,3273,3275,3279,3286,3289 | ✅ PASS | beat Netherlands 3-2, Euro 2024 group stage |
| 3262 | ✅ PASS | Euro 2024 run ended in R16 |
| 3285 | ✅ PASS | lost 2-1 in knockout at both Euro 2020 (Italy) & 2024 (Türkiye) |
| 3251 | ❌ FAIL | answer "03-Feb" = corrupted "3-2" (Excel date mangling) |
| 3270 | ❌ FAIL | false premise — Austria not at 2022 WC (didn't qualify) |
| 3276,3277 | ❌ FAIL | first Euro group stage was 2008 (co-host), not 2016 |

**Running totals (new method, rows 231+): 584 PASS-ALL · 180 FAIL-LIVENESS.**
**Austria so far: 30 PASS · 4 FAIL (rows 3242–3289).**

---

## Batch rows 3291–3460 (Austria) — NEW METHOD. Result: 91 PASS · 31 FAIL.

122 candidates. Recurring FAIL clusters: Excel date-mangled scorelines; "qualified 2026 → 2025";
non-unique Euro tournament-year questions; first Euro = 2008 not 2016; Rangnick Bayern-rejection
keyed 2022 (was 2024); Arnautović top-scorer time-bounding; 2022-WC false premises.
Full per-cluster detail in QA_FAILED_LIVENESS_PASSED_OTHERS.md (this batch's section).

## Batch rows 3461–3660 (Austria) — NEW METHOD. Result: 124 PASS · 45 FAIL.

169 candidates. FAIL rows by cluster:
| Cluster | Rows |
|---------|------|
| Excel date-mangled scoreline (3-2 / 2-1) | 3461,3462,3463,3465,3468 |
| Euro 2020 keyed 2020 (played 2021) | 3480,3498 |
| Non-unique tournament-year | 3491,3496,3500,3508,3523 |
| First Euro was 2008, not 2016 | 3497 |
| Qualified 2025, not 2026 | 3493,3494,3495 |
| Rangnick rejected Bayern in 2024, not 2022 | 3505,3518,3519,3547,3548,3549,3554,3583,3584,3586,3591,3592,3593,3594 |
| Rangnick not in charge of 2022 WC qualifying | 3557 |
| Arnautović all-time top scorer only from 2025 | 3545,3623,3625,3638,3644 |
| Wrong/non-unique player-club facts | 3615,3622,3629,3635,3636 |
| 2022 WC finals false premise (Alaba injury) | 3654,3655,3656,3657 |

## Batch rows 3661–3860 (Austria) — NEW METHOD. Result: 141 PASS · 23 FAIL.

164 candidates. FAIL rows by cluster:
| Cluster | Rows |
|---------|------|
| Wrong manager name "Franz Koller" (is Marcel Koller) | 3719,3747,3773 |
| Rangnick rejected Bayern in 2024, not 2022 | 3785 |
| Arnautović all-time top scorer only from 2025 | 3742,3858 |
| False premise — Austria not at 2022 WC finals | 3661,3679,3682,3683,3720,3839,3843 |
| Non-unique "not based in the Bundesliga" (Alaba) | 3672,3673,3857,3859 |
| Sabitzer at Bayern (not Dortmund) in 2022 cycle | 3826 |
| Non-unique tournament/opponent | 3732,3734 |
| Internal temporal contradiction | 3675,3807 |
| False premise — Austria didn't face Germany in 2022 WCQ | 3751 |

## Batch rows 3861–4060 (Austria) — NEW METHOD. Result: 130 PASS · 21 FAIL.

151 candidates. FAIL rows by cluster:
| Cluster | Rows |
|---------|------|
| Alaba had no 100+ caps before 2022 WC (reached 100 on 17 Jun 2023) | 3862 |
| Non-unique "based in the Bundesliga" (Sabitzer also) | 3867 |
| "2022 World Cup squad/player" false premise | 3868,3941 |
| Arnautović all-time top scorer only from 2025 / time-bound | 3875,3878 |
| Arnautović has no World Cup goal | 3881,3902 |
| Vienna/Ernst-Happel was not a Euro 2020 host | 3908 |
| Alaba injury framed around 2022 WC finals (false premise) | 3914,3918,3920,3927 |
| Austria Wien IS a main Austrian Bundesliga club | 3944 |
| Rangnick rejected Bayern in 2024, not 2022 | 3945,4026 |
| Netherlands win was group stage, not a knockout win | 3950 |
| Non-unique answer | 3955,3960 |
| Rangnick not in charge of the 2022 WC cycle (Foda was) | 3969,4027 |

## Batch rows 4061–4282 (Austria) — NEW METHOD — FINAL AUSTRIA BATCH. Result: 110 PASS · 11 FAIL.

121 candidates (mostly Euro result/manager duplicates, all correct). FAIL rows by cluster:
| Cluster | Rows |
|---------|------|
| Self-referential answer ("like Austria → Austria") | 4105,4204 |
| Netherlands win was group stage, not a knockout win | 4140 |
| Non-unique answer | 4147,4148,4241 |
| False premise (Austria's first Euros was 2008) + non-unique | 4203 |
| "Which year did Austria qualify → 2026" (qualified 2025) | 4233,4238,4240 |
| Answer is a consequence, not a cause ("why qualify") | 4276 |

---

# ✅ AUSTRIA COMPLETE (rows 3242–4282)
- 761 candidates in QA_PASSED.md pool. **626 PASS** → QA_PASSED_ALL.md · **135 FAIL** → QA_FAILED_LIVENESS_PASSED_OTHERS.md.
- Per batch: 3242–3289 (30P/4F) · 3291–3460 (91P/31F) · 3461–3660 (124P/45F) · 3661–3860 (141P/23F) · 3861–4060 (130P/21F) · 4061–4282 (110P/11F).

**Running totals (new method, rows 231+): 1180 PASS-ALL · 311 FAIL-LIVENESS.**

---

# CABO VERDE (rows 8183–9573) — NEW METHOD (only QA_PASSED.md rows)

696 Cabo Verde rows are in QA_PASSED.md. Fact base built from live sources:
- **First-ever FIFA World Cup qualification: 2026** (no earlier finals; contested but did not
  win the 2022 qualifying campaign). One of the smallest nations (~525,000 pop) ever to qualify
  — compared to **Iceland**, whose own debut was **2018** (not 2026).
- **AFCON appearances: 2013, 2021, 2023** (did NOT play 2015). 2013 debut → quarter-finals;
  **2023 → quarter-finals**, eliminated by **South Africa** (0-0, 2-1 pens) in the **QF**, not the R16.
- Nicknamed the **Blue Sharks**; peak FIFA ranking **27th** (2014). Manager **Bubista**
  (= Pedro Leitão Brito). Squad built on the **Portugal-based diaspora / European leagues**,
  not the domestic Campeonato Caboverdiano. Home: Estádio Nacional, Praia (~15,000).
Sources: [Cape Verde national football team (Wikipedia)](https://en.wikipedia.org/wiki/Cape_Verde_national_football_team),
[2023 Africa Cup of Nations (Wikipedia)](https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations).

## Batch rows 8183–8530 (Cabo Verde) — Result: 176 PASS · 16 FAIL.
## Batch rows 8531–8880 (Cabo Verde) — Result: 190 PASS · 11 FAIL.

## Batch rows 8881–9230 (Cabo Verde) — Result: 87 PASS · 26 FAIL.
113 candidates. FAIL rows by cluster:
| Cluster | Rows |
|---------|------|
| Self-referential ("like Cabo Verde → Cabo Verde"); 9163 also false 2015-AFCON premise | 8886,8902,9003,9004,9005,9006,9024,9146,9163,9169,9173,9179,9181,9184,9210,9220 |
| Non-unique answer | 8881,8942,9087,9096 |
| Wrong answer — WC squad Europe-based, not domestic league | 9048 |
| Wrong explanation — 2023 AFCON exit was QF, not R16 | 9127,9129 |
| False premise — no R16 loss to South Africa (was QF) | 9131 |
| False premise — Iceland's debut was 2018, not 2026 | 9206,9219 |

## Batch rows 9231–9573 (Cabo Verde) — NEW METHOD — FINAL CABO VERDE BATCH. Result: 170 PASS · 20 FAIL.
190 candidates. FAIL rows by cluster:
| Cluster | Rows |
|---------|------|
| Wrong answer — 2023 AFCON best stage was the QF (keyed R16) | 9286,9287 |
| False premise — no R16 loss to South Africa (was QF); 9388 also mislabels SA "West African" | 9344,9388,9423 |
| Wrong explanation — states R16 for the QF exit | 9353,9356,9411,9454 |
| False premise — Cabo Verde did not play the 2015 AFCON | 9341 |
| Wrong answer — WC squad Europe-based, not domestic league | 9375 |
| Self-referential answer (names Cabo Verde) | 9263,9305 |
| False premise — Iceland's debut was 2018, not 2026 | 9320 |
| False premise — no 2018/2022 WC qualification (first is 2026) | 9453,9462,9475,9559 |
| Non-unique answer | 9280,9389 |

---

# ✅ CABO VERDE COMPLETE (rows 8183–9573)
- 696 candidates in QA_PASSED.md pool. **623 PASS** → QA_PASSED_ALL.md · **73 FAIL** → QA_FAILED_LIVENESS_PASSED_OTHERS.md.
- Per batch: 8183–8530 (176P/16F) · 8531–8880 (190P/11F) · 8881–9230 (87P/26F) · 9231–9573 (170P/20F).
- Next unclaimed country: **Cameroon** — NOT started (ask the user before beginning a new country).

**Running totals (new method, rows 231+): 1803 PASS-ALL · 384 FAIL-LIVENESS.**

---

# CANADA (rows 10746–12428) — NEW METHOD (only QA_PASSED.md rows)

1003 Canada rows are in QA_PASSED.md. Fact base built from live sources (Wikipedia
Canada men's national soccer team + web searches):
- **2022 World Cup** (ended a **36-year absence**; previous finals 1986): topped the
  CONCACAF Octagonal (**28 pts**, above Mexico & USA) under **John Herdman**; clinched with a
  **4-0 win over Jamaica** at BMO Field, Toronto (27 Mar 2022). At the finals lost all three:
  **1-0 Belgium** (Batshuayi; Davies penalty saved by Courtois), **4-1 Croatia**, **2-1 Morocco**.
  **Alphonso Davies** scored Canada's **first-ever WC goal** (2nd min vs Croatia).
- **Key players:** Davies (captain/LB-winger, 2020 UCL with Bayern); **Jonathan David** (Lille,
  all-time top scorer — reached **25 intl goals in 2023, not by 2022**); **Cyle Larin** (record
  scorer ~25 by 2022); **Atiba Hutchinson** (most-capped, 100+, retired after 2022);
  **Milan Borjan** (GK); **Stephen Eustáquio** (creator); **Tajon Buchanan** (winger);
  **Ismael Koné** (debuted **Jan 2022**, played the 2022 WC — *not* a post-2022/2026-only debut).
- **Managers:** Herdman 2018–2023 (left for **Toronto FC in 2023**); **Jesse Marsch appointed
  2024** (first American; high-pressing) — led Canada to the **2024 Copa América semis** (lost
  **2-0 to Argentina**, 4th place). **2021 Gold Cup → semis.**
- **FIFA ranking:** reached **33rd in Feb 2022** — but this is **no longer the peak** (31st Dec
  2024, **26th Sept 2025**), so all-time "highest/peak = 33rd" claims FAIL; year-bounded
  "33rd in 2022" PASS.
- **2026:** co-hosts with USA & Mexico (auto-qualify); venues **BMO Field, Toronto (~30,000)**
  and **BC Place, Vancouver (~54,500)**. Canada Soccer HQ in **Ottawa**. **CPL founded 2019**;
  **Toronto FC won 2017 MLS Cup**; women won **Tokyo 2020 Olympic gold** (Priestman; Grosso PK).
Source: [Canada men's national soccer team (Wikipedia)](https://en.wikipedia.org/wiki/Canada_men%27s_national_soccer_team).

## Batch rows 10746–11085 (Canada) — Result: 228 PASS · 17 FAIL.
113... see QA_FAILED_LIVENESS_PASSED_OTHERS.md. FAIL clusters: stale ranking superlative (10753,10755,10756,10757,10758,10815,10839,10843,10846,11028,11067); Excel date-mangled scoreline (11071,11072,11079); temporal contradiction/false premise (10747); 2-0 is not a three-goal margin (10805); BMO did not host 2022 WC matches (10995).

## Batch rows 11086–11425 (Canada) — Result: 214 PASS · 11 FAIL.
FAIL clusters: Marsch appointed 2024 not 2023 (11090,11184,11186); stale ranking superlative (11089,11125,11126,11128,11134); David 25+ goals by/in 2022 premature (11154,11402,11409).

## Batch rows 11426–11765 (Canada) — Result: 227 PASS · 5 FAIL.
FAIL clusters: Koné debuted 2022 not after/2026 (11663,11664,11710); non-unique (11711 — Davies & Hutchinson both lack 25+ goals); David 25+ by 2022 premature (11717).

## Batch rows 11766–12105 (Canada) — Result: 157 PASS · 5 FAIL.
FAIL clusters: stale ranking superlative (11810); David 25+ by/during 2022 premature (11791,11890); non-unique CPL founding clubs (11823); non-unique "NOT a top scorer" — Davies & Buchanan (11787).

## Batch rows 12106–12428 (Canada) — FINAL CANADA BATCH. Result: 136 PASS · 3 FAIL.
FAIL clusters: stale "FIFA ranking peak = 33rd" superlative (12391,12403,12404).

---

# ✅ CANADA COMPLETE (rows 10746–12428)
- 1003 candidates in QA_PASSED.md pool. **962 PASS** → QA_PASSED_ALL.md · **41 FAIL** → QA_FAILED_LIVENESS_PASSED_OTHERS.md.
- Per batch: 10746–11085 (228P/17F) · 11086–11425 (214P/11F) · 11426–11765 (227P/5F) · 11766–12105 (157P/5F) · 12106–12428 (136P/3F).
- Dominant FAIL themes: stale FIFA-ranking superlative (33rd no longer the peak), "Jonathan David 25+ goals by 2022" (he reached 25 in 2023), Marsch appointed 2024 not 2023, Koné debuted 2022 not 2026, Excel date-mangled scorelines, and non-unique options.
- Cameroon (rows 9574–10745) was **skipped** (not started). Next unclaimed country: ask the user before beginning a new country.

**Running totals (new method, rows 231+): 2765 PASS-ALL · 425 FAIL-LIVENESS.**

---

# ✅ COSTA RICA (rows 15528–16571) — COMPLETE

**Pool:** 734 QA_PASSED candidates across CSV rows 15528–16571. Verified against the Costa Rica men's national team fact base (2014 quarter-final run; 2018 & 2022 group exits; Keylor Navas).

**Fact base:** 2014 WC — topped Group D (beat Uruguay 3-1, Italy 1-0, drew England 0-0, 7 pts), beat Greece on pens (R16), lost QF to Netherlands on pens (0-0, 4-3, van Gaal's Tim Krul sub); manager Jorge Luis Pinto, captain Bryan Ruiz, GK Keylor Navas (→ Real Madrid 2014, 3× UCL 2016–2018, first Central American UCL winner). 2018 WC — group exit under Óscar Ramírez (lost Serbia & Brazil, drew Switzerland). 2022 WC — group exit under Luis Fernando Suárez (1-0 v Japan via Keysher Fuller; 7-0 loss to Spain); qualified via intercontinental playoff v New Zealand. Celso Borges = most-capped (164). Home venue Estadio Nacional, San José (~35,175). Primera División giants: Saprissa, Alajuelense, Herediano.

**Two systematic dataset errors (web-verified):**
1. **FIFA-ranking peak.** Dataset says highest = **15th (2014)**; actual all-time peak = **13th (Feb 2015)**. → all "highest/peak 15th" claims FAIL.
2. **2026 World Cup.** Dataset says Costa Rica **qualified** (direct CONCACAF); in reality they were **eliminated 19 Nov 2025** (0-0 v Honduras) and are **not** at the 2026 finals. → all "qualified for 2026" claims FAIL.

| Batch | Rows | Candidates | PASS | FAIL |
|-------|------|-----------:|-----:|-----:|
| 1 | 15528–15750 | 156 | 123 | 33 |
| 2 | 15751–15980 | 122 | 105 | 17 |
| 3 | 15981–16200 | 174 | 164 | 10 |
| 4 | 16201–16400 | 149 | 143 | 6 |
| 5 | 16401–16571 | 133 | 119 | 14 |
| **Total** | **15528–16571** | **734** | **654** | **80** |

**FAIL themes:** false FIFA-ranking peak (15th vs actual 13th); false 2026 World Cup qualification (eliminated Nov 2025); Excel date-mangled scorelines (3-1→"03-Jan", 4-3→"04-Mar", 3-4→"03-Apr"); non-unique answers (multiple CONCACAF-direct years, multiple "not beaten"/"not conceded 7" teams, all-four Gold-Cup-nation options); self-referential answers (Navas-vs-Navas, stadium-vs-itself, CR-lost-by-larger-margin-than-CR); a wrong answer (New Zealand "qualified" via playoff — they lost); anachronistic cap claim (Borges "150 caps at 2018" — had ~110).

# ✅ COSTA RICA COMPLETE

- Per batch: 15528–15750 (123P/33F) · 15751–15980 (105P/17F) · 15981–16200 (164P/10F) · 16201–16400 (143P/6F) · 16401–16571 (119P/14F).
- Cameroon (9574–10745), Chile (12429–13847) and Colombia (13848–15527) were **skipped** (not started). Next unclaimed country: ask the user before beginning a new country.

**Running totals (new method, rows 231+): 3419 PASS-ALL · 505 FAIL-LIVENESS.**

---

# ✅ ENGLAND (rows 23687–25401) — COMPLETE

**Pool:** 1315 QA_PASSED candidates across CSV rows 23687–25401 (the largest country processed). Verified against the England men's national team fact base.

**Fact base:** 2010 WC — lost 4-1 to Germany in R16 (Bloemfontein; Lampard's disallowed goal), Capello manager, Gerrard captain. 2014 WC — bottom of group, 1 pt (lost Italy & Uruguay 2-1, drew Costa Rica), Hodgson manager. 2018 WC — 4th place under Southgate (beat Colombia on pens — first WC shootout win, Dier decisive pen; beat Sweden 2-0; lost SF 2-1 to Croatia AET; lost 3rd-place 2-0 Belgium); Kane Golden Boot (6). 2022 WC — beat Iran 6-2, drew USA 0-0, beat Wales 3-0 (Rashford brace), beat Senegal 3-0, lost QF 2-1 France (Kane missed pen). Euro 2016 — lost R16 2-1 Iceland (Hodgson resigned). Euro 2020 — lost final to Italy on pens at Wembley (Shaw scored 2nd min; Rashford/Sancho/Saka missed; Pickford saved pens; beat Germany 2-0 R16; beat Denmark 2-1 SF AET). Euro 2024 — lost final 2-1 to Spain in Berlin (Palmer equalised; Bellingham 95th-min overhead kick vs Slovakia). Southgate resigned Jul 2024 (record 61-18-23 in 102), Carsley interim H2 2024, Tuchel appointed Jan 2025 (3rd non-English mgr). **2026 WC — qualified with a PERFECT 8-win, 0-conceded record (Group K) under Tuchel.** Kane all-time top scorer (broke Rooney's 53 in Mar 2023). Highest FIFA ranking 3rd (2012 & 2017-18). Wembley 90,000 (Europe's 2nd-largest after Camp Nou). St George's Park (opened 2012, 13 pitches, Wembley replica). FA founded 1863.

**Verified corrections (web-sourced):**
1. **FIFA ranking after 2014 group exit:** dataset says **17th**; actually fell to **20th** (Jul 2014). All "17th in 2014" claims FAIL.
2. **2022 World Cup squad:** dataset says all 26 were England/Premier-League based; **Jude Bellingham was at Borussia Dortmund** → "all 26 / zero abroad" FAIL.
3. **Euro 2024 Young Player:** dataset credits **Bellingham**; actually **Lamine Yamal (Spain)** → FAIL.
4. **Euro 2020 Team of the Tournament:** dataset credits **Pickford**; the GK was **Donnarumma** (England: Walker, Maguire, Sterling) → FAIL. (Caught mid-run; 10 mis-passed rows pulled from PASS_ALL.)

| Batch | Rows | Candidates | PASS | FAIL |
|-------|------|-----------:|-----:|-----:|
| 1 | 23687–23920 | 179 | 161 | 18 |
| 2 | 23921–24170 | 214 | 182 | 32 |
| 3 | 24171–24420 | 205 | 194 | 11 |
| 4 | 24421–24700 | 233 | 225 | 8 |
| 5 | 24701–25050 | 258 | 245 | 13 |
| 6 | 25051–25401 | 226 | 221 | 5 |
| **Total** | **23687–25401** | **1315** | **1228** | **87** |

**FAIL themes:** Excel date-mangled scorelines/formations (2-1→"02-Jan", 6-2→"06-Feb", 4-1→"04-Jan", 3-5-2→"03/05/2002", etc.); wrong "17th in 2014" ranking (actual 20th); "Bellingham = Euro 2024 Young Player" (Yamal); "Pickford in Euro 2020 Team of the Tournament" (Donnarumma); "all 26 squad England-based" (Bellingham at Dortmund); temporal errors (Kane as record holder "by/at 2022" — actually Mar 2023; Rooney record holder "during 2014 WC" — actually Charlton until Sept 2015; Henderson "WC debut 2018" — actually 2014); false premises (England "2018 World Cup final"; "did not defeat Hungary" — beat them 4-0; Kane's 54th in "2023 World Cup qualifying" — a Euro 2024 qualifier); non-unique answers (all qualifying groups won; multiple 2-1 WC knockout losses; "Three Lions" = "Football's Coming Home"; etc.); and miscounts (English CL titles 2008-23 = 5 not 6; 2010 qualifying 9W-1L not 9W-1D).
**Note:** "2026 perfect 8-win qualification," "highest FIFA ranking 3rd (2012 & 2018)," and "Saka 2022 Kopa Trophy nominee" were all web-verified TRUE and PASS.

# ✅ ENGLAND COMPLETE

- Per batch: 23687–23920 (161P/18F) · 23921–24170 (182P/32F) · 24171–24420 (194P/11F) · 24421–24700 (225P/8F) · 24701–25050 (245P/13F) · 25051–25401 (221P/5F).
- Rows 16572–23686 (Côte d'Ivoire through Egypt) and earlier Cameroon/Chile/Colombia were **skipped** (not started). Next unclaimed country: ask the user before beginning a new country.

**Running totals (new method, rows 231+): 4647 PASS-ALL · 592 FAIL-LIVENESS.**

---

# ✅ GHANA (rows 29166–30309) — COMPLETE

**Pool:** 855 QA_PASSED candidates across CSV rows 29166–30309. Verified against the Ghana men's national team (Black Stars) fact base.

**Fact base:** 2010 WC — QF run under Milovan Rajevac; beat USA 2-1 R16 (Gyan extra-time winner); lost QF to Uruguay on penalties after **Luis Suárez's goal-line handball** and **Gyan's missed penalty**. 2014 WC — group exit under James Kwesi Appiah (**lost USA & Portugal, DREW Germany 2-2**). 2022 WC — group exit under Otto Addo (beat South Korea 3-2 via **Kudus** brace, lost Portugal 3-2, lost Uruguay 2-0 [de Arrascaeta 2]); qualified by beating Nigeria on away goals (1-1 agg); André Ayew captain & most-capped (110+); Inaki Williams switched from Spain (2022); Chris Hughton technical adviser. **2026 WC — qualified (topped CAF Group I under Otto Addo, his 2nd WC qualification).** Asamoah Gyan all-time top scorer (51), once Africa's top WC scorer. 4× AFCON winner; 2015 final lost to Côte d'Ivoire on pens; 2010 AFCON **final** (lost to Egypt); 2017 AFCON semis. Only African FIFA U-20 World Cup winner (2009, Black Satellites). Failed to qualify only for 2018. Avram Grant managed 2014-2017. Venues: Accra Sports Stadium & Baba Yara Stadium (Kumasi), both ~40,000.

**Verified corrections (web-sourced):**
1. **2014 group results:** dataset says Ghana "lost to USA and Germany"; they actually **drew Germany 2-2** and lost to USA and Portugal.
2. **2010 AFCON:** dataset says "semi-finals"; Ghana reached the **final** (runners-up to Egypt).
3. **Mohammed Kudus's club:** dataset says "West Ham at the 2022 World Cup"; he was at **Ajax** in 2022 and moved to **Tottenham in July 2025** — every "Kudus = West Ham" claim is wrong. (Caught mid-run; 4 mis-passed rows pulled from PASS_ALL.)
4. **Two ~40,000 stadiums:** Accra Sports & Baba Yara are both ~40k, so generic "which ~40k stadium" items with both as options are non-unique. (2 mis-passed rows pulled.)
5. **2026 qualification = TRUE** (CAF Group I winners).

| Batch | Rows | Candidates | PASS | FAIL |
|-------|------|-----------:|-----:|-----:|
| 1 | 29166–29420 | 190 | 163 | 27 |
| 2 | 29421–29700 | 196 | 185 | 11 |
| 3 | 29701–29970 | 216 | 203 | 13 |
| 4 | 29971–30240 | 197 | 177 | 20 |
| 5 | 30241–30309 | 56 | 55 | 1 |
| **Total** | **29166–30309** | **855** | **783** | **72** |

**FAIL themes:** "lost to USA and Germany" in 2014 (drew Germany); "2010 AFCON semi-finals" (was the final); Kudus at "West Ham" (Ajax in 2022 / Tottenham now); Excel date-mangled scorelines ("02-Jan"=2-1, "03-Feb"=3-2, "01-Jan"=1-1); "four managers at World Cups" (only three — Grant managed at no WC); non-unique answers (two ~40k stadiums; all-options-are-GPL-clubs; "over 25 caps" all qualify; multiple CONCACAF/qualification years); self-referential "which nation like Ghana…→ Ghana"; and wrong facts (Costa Rica "qualified for 2010" — they missed it; Hughton placed in the 2014 cycle).
**Note:** "2026 CAF qualification," "Gyan 51 goals / Africa's top WC scorer," "André Ayew most-capped," and "Inaki Williams switched from Spain 2022" were all web-verified TRUE and PASS. Partey-Arsenal rows PASS (Arsenal correct for the 2022 WC; he moved to Villarreal Aug 2025).

# ✅ GHANA COMPLETE

- Per batch: 29166–29420 (163P/27F) · 29421–29700 (185P/11F) · 29701–29970 (203P/13F) · 29971–30240 (177P/20F) · 30241–30309 (55P/1F).
- Skipped/not started: rows 16572–23686 (Côte d'Ivoire…Egypt), rows 25402–29165 (France, Germany), and earlier Cameroon/Chile/Colombia. Next unclaimed country: ask the user before beginning a new country.

**Running totals (new method, rows 231+): 5430 PASS-ALL · 664 FAIL-LIVENESS.**
