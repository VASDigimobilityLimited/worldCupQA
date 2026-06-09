# HANDOFF — World Cup Trivia QA Review

> For any Claude (or person) resuming this work after pulling the repo. **Read this top to
> bottom.** This is a **shared, multi-contributor** effort: several people pull this repo and
> run the live fact-check in parallel, each taking a different country/row range. The rules in
> §A exist so nobody clobbers anyone else's work.
>
> **There are now three tracks of the same job:** **batch 1** (the original dataset, liveness
> in progress), **batch 2** (a second, larger dataset — mechanics done, liveness not started),
> and the **cleaned** re-check (rectified ex-batch-1 fails). They share one procedure (§5) and
> one set of judgment rules (§6/§7) but use **different files and different row numbers** — the
> §5 selector table maps each track to its file set. Always know which track you're on.

---

## A. ⚠️ COLLABORATION RULES (read first — this repo has multiple contributors)

**This repo is pulled and worked on by several people at once.** Before doing anything:

1. **ASK the user which BATCH, then which country, then which rows.** Do **not** assume any of
   the three. First ask **which batch** — **batch 1** (§4 table) or **batch 2** (§9(d) table); the
   two are different datasets with different files and different row numbers. Then show that
   batch's per-country status table (done / in-progress / not started + row ranges) and let them
   pick a country and a starting row *inside* it. The unit of work is "a batch → a country (or a
   row range within that country)."
2. **Only liveness-check rows present in your batch's pool file** (the mechanically/heuristically
   passed pool — `QA_PASSED.md` / `QA_PASSED_b2.md` / `QA_PASSED_cleaned.md`; see §5 selector). Skip
   any row in that batch's failed file — those already fail, no point fact-checking them.
3. **Coordinate so two people don't check the same rows.** Pick a country/range nobody else has
   claimed in your batch's status table (§4 for batch 1, §9(d) for batch 2). If unsure, ask the
   user to confirm with their team.
4. **Before pushing back to the repo, you MUST update this handoff document** (`HANDOFF.md`):
   - update the country's row in your batch's status table (§4, or §9(d)+§9(e), or §9(f)),
   - bump the totals in §3 (including the GRAND TOTAL line),
   - and, **for batch 1 only**, advance the cursor + per-chunk table in `QA_TC06_LIVE.md`.
   **Remind the user to do this every session, before they `git push`.** A push without an
   updated handoff will desync everyone.
5. `HANDOFF.md` is **tracked in git** (it is no longer git-ignored) precisely so this shared
   state travels with the repo. Keep it accurate.
6. **There are now TWO datasets in flight.** Everything in §1–§7 below is **batch 1**
   (`Pre-worldcup-clean.csv` → `QA_PASSED.md` → `QA_PASSED_ALL.md`). **Batch 2** is a separate,
   larger dataset with its **own coordination table, pool, and output files in §9** — same rules,
   different files. **Before claiming work, decide which batch you're on**, then claim a country
   from that batch's table (§4 for batch 1, §9(d) for batch 2). Don't mix the two. Each batch's
   file set is in the §5 selector table.

**Suggested per-session flow for a contributor's Claude:**
> "**First: which batch — batch 1 or batch 2?** (They're different datasets with different row
> numbers.) Then, which country and from which row? Here's what's done so far … [show the §4 or
> §9(d) table for that batch]. I'll only check rows in that batch's passed pool and route results
> into that batch's PASS/FAIL files (see the §5 selector). When we stop, I'll update `HANDOFF.md`
> (+ `QA_TC06_LIVE.md` for batch 1) so you can push clean state back."

---

## 0. Environment

- **Repo:** `https://github.com/VASDigimobilityLimited/worldCupQA.git` (this *is* a git repo now).
- Platform: macOS. Use `python3`.
- **You need the web tools** `WebSearch` and `WebFetch` (deferred — load via ToolSearch
  `select:WebSearch,WebFetch`). The factual check is done against live sources.
- **"As of now" matters.** The 2026 World Cup is upcoming; CAF/most 2026 qualifying concluded in
  late 2025. Keep facts current (e.g. **Ivory Coast has 3 AFCON titles** since winning 2023).

## 1. The task

QA-review a competitive **World Cup trivia dataset** against the battery in
[QA_REVIEW_PROMPT.md](QA_REVIEW_PROMPT.md). Each question PASSES only if it clears every
applicable test; otherwise it FAILS (list all failing tests + a concrete remedy). The task is the
same for every track (batch 1, batch 2, cleaned) — **only the files change** (§5 selector).

**What you fact-check:** the questions listed in your track's **pool file** — only those. For
batch 1 that's [QA_PASSED.md](QA_PASSED.md); for batch 2 [QA_PASSED_b2.md](QA_PASSED_b2.md); for
cleaned `QA_PASSED_cleaned.md`. Each entry gives `### Row N`, **Q**, **Answer**, **Options**, and a
"Why it passed" note, verbatim from the dataset. **Never check a row that isn't in your pool file.**

**One gotcha — the `explanation` field:** the pool file does **not** include each question's
`explanation`. But a question ships with its explanation, and a *wrong explanation* is a TC-06
failure (many Algeria fails were exactly this — "intercontinental playoff", etc.). The explanation
lives in your track's **dataset CSV**, looked up by the same `Row N`: batch 1 →
[Pre-worldcup-clean.csv](Pre-worldcup-clean.csv); batch 2 → [Pre-worldcup2.csv](Pre-worldcup2.csv);
cleaned → `QA_CLEANED_dataset.csv`. Drive the loop off the pool file (the set + Q/A/Options) and
open the CSV *only* for the `explanation`.

**Dataset reference (for the `explanation` lookup only).** All three share the same columns:
`category_id, country, question, answer, options, difficulty, explanation`. `options` is a JSON
array of the **3 distractors**; the correct choice is `answer` (stored separately); the 4 rendered
choices = answer + 3 distractors. `category_id` is constant 12 (ignore); the real category is
`country`. In every file, **row N = line N (header = line 1)** and matches that track's pool file —
**but the numbering is per-file, so the same Row N is a different question in each track.**

| Track | Dataset CSV | rows | data rows | countries |
|-------|-------------|-----:|-----------|-----------|
| Batch 1 | `Pre-worldcup-clean.csv` | 46,517 | 2–46518 | 38 (Algeria → USA) |
| Batch 2 | `Pre-worldcup2.csv` | 51,061 | 2–51062 | 48 (incl. 17 new, e.g. Portugal, Spain, Scotland — see §9) |
| Cleaned | `QA_CLEANED_dataset.csv` | 3,489 | 2–3490 | subset of batch-1 countries (carries original batch-1 Row in col 1) |

## 2. What is already DONE

### (a) Mechanical + heuristic pass — COMPLETE for every track
- Script: [qa_review.py](qa_review.py) (built on [tc_validate.py](tc_validate.py)), now
  parameterized (`--src/--passed/--failed`).
- Outputs (regenerate with the commands in §9):
  - **Batch 1** (`python3 qa_review.py`): [QA_PASSED.md](QA_PASSED.md) 32,490 ← pool ·
    [QA_FAILED.md](QA_FAILED.md) 14,027 ← skip.
  - **Batch 2:** `QA_PASSED_b2.md` 39,321 ← pool · `QA_FAILED_b2.md` 11,740 ← skip (see §9(b)).
  - **Cleaned:** `QA_PASSED_cleaned.md` 393 ← pool · `QA_FAILED_cleaned.md` 3,096 ← back for re-fix
    (see §9(a)).
- Covers TC-01 (near-dup), TC-03, TC-04, TC-05, TC-06 *proxy only*, TC-08, TC-10, TC-11, TC-13,
  TC-14, TC-15, TC-16, generation rules. **Negative-framing rule was removed at the user's
  request** — do not re-add it. This layer does NOT verify factual accuracy — see (b).

### (b) TC-06 LIVE factual fact-check — IN PROGRESS (this is the loop everyone runs)
Per-row, web-sourced verification of `answer` + `explanation`, **only on rows in the track's pool
file**. The status below is **batch 1**; **batch-2 and cleaned liveness have NOT started** (their
status/totals are in §9(e)/(f)). Verdicts route into each track's two files (§5 selector); for
batch 1:
- **`QA_PASSED_ALL.md`** — passed mechanical/heuristic **AND** liveness (ship-ready).
- **`QA_FAILED_LIVENESS_PASSED_OTHERS.md`** — passed mechanical but **failed liveness**
  (the dangerous "looks clean but is factually wrong" rows). Each entry has reason + source URL + remedy.

**✅ Algeria** (rows 2–1228) and **✅ Argentina** (rows 1229–2160) are complete, and **34 countries are
now COMPLETE in total** (full table in §4; running counts in §3). Key findings per country:

- **✅ Australia** (2161–3241): 714 ship-ready / 121 dangerous. **✅ Austria** (3242–4282): 626 / 135.
- **✅ Belgium** (4283–6096): 1135 / 192. **✅ Brazil** (6097–8182): 1346 / 218.
- **✅ Cabo Verde** (8183–9573): 623 / 73. **✅ Cameroon** (9574–10745): 681 / 57 — Cameroon did NOT
  qualify for 2026 (lost the CAF playoff to DR Congo), so "Cameroon qualified for 2026" rows fail.
- **✅ Canada** (10746–12428): 962 / 41. **✅ Chile** (12429–13845): 769 / 191 — Chile FAILED to qualify
  for 2026 (last in CONMEBOL, Gareca resigned); dataset wrongly credits Reinaldo Rueda with the failed
  2018 qualifying (actually Pizzi).
- **✅ Costa Rica** (15528–16571): 654 / 80. **✅ Côte d'Ivoire** (16572–17486): 463 / 79.
- **✅ Croatia** (17487–19101): 1034 / 154. **✅ Denmark** (19102–20581): 859 / 182.
- **✅ DR Congo** (20582–21579): 459 / 127. **✅ Ecuador** (21580–22765): 725 / 57 — Ecuador DID qualify
  for 2026, but "Sánchez Bas is the 2026 manager" is stale (sacked 2024; **Sebastián Beccacece** clinched it).
- **✅ Egypt** (22766–23686): 532 / 104 — DID qualify for 2026; fails incl. 2010 AFCON final wrongly "on
  penalties" (1-0 v Ghana), "hosted 2021 AFCON" (hosted 2019), Salah Golden Boot "twice" (actually 4).
- **✅ England** (23687–25401): 1228 / 87. **✅ France** (25402–27324): 1237 / 176 — DID qualify for 2026;
  recurring errors "Griezmann 2018 Silver Ball" (Bronze), "Lloris 2018 All-Star Team" (Courtois),
  "perfect Euro 2020 qualifying" (lost to Turkey), "2018 Fair Play → France" (Spain), "lost 2022 NL final" (won 2021).
- **✅ Germany** (27325–29161): 1291 / 65 — DID qualify for 2026; very accurate data; fails incl. Euro 2024 QF
  crediting Füllkrug/Oyarzabal (actually **Wirtz** 89' & **Merino** 119'), "Kroos recalled for 2026" (retired).
- **✅ Ghana** (29166–30309): 783 / 72. **✅ Italy** (32568–34327): 1061 / 225 — Italy FAILED to qualify for
  2026 (lost the playoff final to **Bosnia**, Gattuso ran the failed campaign — 3rd straight WC miss).
- **✅ Iran** (30310–31698): 775 / 151. **✅ Iraq** (31699–32567): 425 / 112.
- **✅ Japan** (34954–36397): 935 / 62 — DID qualify for 2026 (first non-host to qualify, Mar 2025); fails
  incl. "17th FIFA ranking after 2011 Asian Cup" (~19th) and "won their 2010 AFC group" (2nd behind Australia).
- **✅ Jordan** (36398–37773): 691 / 159. **✅ Mexico** (37774–39364): 901 / 173 — DID qualify for 2026 (co-host).
- **✅ Morocco** (39365–40186): 460 / 98 — first nation in the world to qualify for 2026 (2026 rows pass); fails
  incl. "11th = highest FIFA ranking" (actually 7th, June 2026), "missed/failed 2018" (they played 2018), "co-hosted
  AFCON 2025 with Kenya & Tanzania" (Morocco was SOLE host; KTU host 2027), "won the Arab Cup" (Algeria won 2021),
  "Brahim Díaz = Real Madrid academy" (Man City academy; Hakimi is the RM product).
- **✅ Netherlands** (40187–41273): 761 / 117 — qualified for 2026 (won UEFA Group G unbeaten under Koeman); fails
  incl. "highest FIFA ranking = 3rd in 2011" (actually **1st**), "Robben won the 2010 Golden/Silver Ball" (Forlán
  Golden, **Sneijder** Silver), Van Persie "scored in the 2010 final" (NL scored 0), 2022 shootout errors (Van Dijk
  & Berghuis both missed).
- **✅ Jamaica** (34328–34953): 381 / 43 — **did NOT qualify for 2026** (lost the intercontinental playoff
  final 1-0 aet to DR Congo; 1998 remains their only WC). **✅ New Zealand** (41274–42086): 398 / 166 — high
  fail rate from systematic dataset errors (2026 qualification fabricated as "via intercontinental playoff" —
  NZ qualified **directly** as the first OFC direct slot). **✅ Nigeria** (42087–42203): 91 / 2 — smallest
  country, very clean. (Jamaica/New Zealand/Nigeria verified by a separate contributor.)
- **✅ Tunisia** (44757–45514): 500 / 73 — DID qualify for 2026 (CAF Group H, perfect 22-0 campaign), so the
  dataset's recurring "qualified for SIX World Cups" is now stale (it's SEVEN). Other big errors: **Msakni
  played at 2018** (he MISSED it with an ACL injury — first WC was 2022), the 2018 decider v Libya scored a goal
  (it was 0-0; the goals were the 4-1 Guinea win), Khazri/Mejbri "played for Espérance" (neither did), and France
  / Saudi Arabia called "CAF teams".
- **✅ USA** (45515–46518): 611 / 78 — **2026 CO-HOST** (auto-qualified; Pochettino coach since Sept 2024).
  Recurring errors: "USA reached the 2024 Copa América semis" (they exited in the GROUP STAGE), "won the 2024
  Gold Cup" (no such tournament — 2024 trophy was the Nations League), "highest FIFA ranking 13th in 2010" (it
  was 4th in 2006; the post-2018 drop was ~32nd not 34th), "Pulisic youngest American to score at a WC" (Julian
  Green, 2014), and "Berhalter fired in 2023" (it was July 2024).

The remaining 4 countries are **not started** (§4). Next sequential not-started country: **Colombia** (rows 13848–15527).

> Note on rows 2–230 (Algeria only): these were done under an older method that checked *every*
> row (not just `QA_PASSED.md`). Their record lives in
> [QA_TC06_PASSED.md](QA_TC06_PASSED.md) / [QA_TC06_FAILED.md](QA_TC06_FAILED.md). From row 231
> onward, the new "QA_PASSED.md pool only" method applies. New countries use the new method
> throughout.

## 3. Running totals (update these every session)

**Batch 1** (batch-2 totals are in §9(e), cleaned in §9(f); the grand-total line below spans all three):

- **Rows 2–230 (Algeria, old method):** 181 PASS / 48 FAIL.
- **New method (231+, all countries) — `QA_PASSED_ALL.md`:** **25227** ship-ready.
- **New method (231+, all countries) — `QA_FAILED_LIVENESS_PASSED_OTHERS.md`:** **3956** dangerous.
- **Total ship-ready so far (both methods):** 25359 (132 backfill rows 2–230 + 25227 new method).
- **🎯 GRAND TOTAL ship-ready (all three tracks):** **30674** =
  batch 1 `QA_PASSED_ALL.md` **25359** + batch 2 `QA_PASSED_ALL_b2.md` **4956** +
  cleaned `QA_PASSED_ALL_cleaned.md` **359**. *Batch-1 liveness: 34 countries complete (incl. Morocco, Netherlands,
  Jamaica, New Zealand, Nigeria, Tunisia, USA). Batch-2 liveness IN PROGRESS: Algeria (269/159) + Argentina (662/167) +
  Belgium (618/170) + Bosnia and Herzegovina (948/125) + Canada (1060/69) + Colombia (607/168) + Costa Rica (792/139) = 4956 ship-ready / 997 dangerous (7 of 48). Cleaned
  liveness **COMPLETE** (359 ship-ready / 34 dangerous of 393). Pools: batch-2 39,321; cleaned 393. Re-sum every
  session — count `### Row`/`- **Row` entries in each file.*
- **34 countries COMPLETE** — per-country **pass-all / fail-liveness** (detailed key findings are in §2):
  Algeria 554/176 · Argentina 562/110 · Australia 714/121 · Austria 626/135 · Belgium 1135/192 ·
  Brazil 1346/218 · Cabo Verde 623/73 · Cameroon 681/57 · Canada 962/41 · Chile 769/191 ·
  Costa Rica 654/80 · Côte d'Ivoire 463/79 · Croatia 1034/154 · Denmark 859/182 · DR Congo 459/127 ·
  Ecuador 725/57 · Egypt 532/104 · England 1228/87 · France 1237/176 · Germany 1291/65 ·
  Ghana 783/72 · Iran 775/151 · Iraq 425/112 · Italy 1061/225 · Jamaica 381/43 · Japan 935/62 ·
  Jordan 691/159 · Mexico 901/173 · Morocco 460/98 · Netherlands 761/117 · New Zealand 398/166 ·
  Nigeria 91/2 · Tunisia 500/73 · USA 611/78.

## 4. Batch-1 per-country status (THE batch-1 coordination table — batch 2 is in §9(d))

`QA_PASSED` = how many of that country's rows are in `QA_PASSED.md` (i.e. how many need liveness).
Claim a country, set Status to your name + "in progress", and fill in the last verified row.

| Country | CSV rows | total | QA_PASSED | Status / last verified row |
|---------|----------|------:|----------:|----------------------------|
| Algeria | 2–1228 | 1227 | 907 | ✅ **COMPLETE** (row 1228) — 554 PASS / 176 FAIL (new method, 231–1228); rows 2–230 old method: 181 PASS / 48 FAIL |
| Argentina | 1229–2160 | 932 | 672 | ✅ **COMPLETE** (row 2160) — 562 PASS / 110 FAIL |
| Australia | 2161–3241 | 1081 | 835 | ✅ **COMPLETE** (row 3241) — 714 PASS / 121 FAIL |
| Austria | 3242–4282 | 1041 | 761 | ✅ **COMPLETE** (row 4282) — 626 PASS / 135 FAIL |
| Belgium | 4283–6096 | 1814 | 1327 | ✅ **COMPLETE** (row 6096) — 1135 PASS / 192 FAIL |
| Brazil | 6097–8182 | 2086 | 1564 | ✅ **COMPLETE** (row 8182) — 1346 PASS / 218 FAIL |
| Cabo Verde | 8183–9573 | 1391 | 696 | ✅ **COMPLETE** (row 9573) — 623 PASS / 73 FAIL |
| Cameroon | 9574–10745 | 1172 | 738 | ✅ **COMPLETE** (row 10745) — 681 PASS / 57 FAIL |
| Canada | 10746–12428 | 1683 | 1003 | ✅ **COMPLETE** (row 12428) — 962 PASS / 41 FAIL |
| Chile | 12429–13847 | 1419 | 960 | ✅ **COMPLETE** (row 13845) — 769 PASS / 191 FAIL |
| Colombia | 13848–15527 | 1680 | 1132 | ⬜ not started |
| Costa Rica | 15528–16571 | 1044 | 734 | ✅ **COMPLETE** (row 16571) — 654 PASS / 80 FAIL |
| Côte d'Ivoire | 16572–17486 | 915 | 542 | ✅ **COMPLETE** (row 17485) — 463 PASS / 79 FAIL |
| Croatia | 17487–19101 | 1615 | 1188 | ✅ **COMPLETE** (row 19100) — 1034 PASS / 154 FAIL |
| Denmark | 19102–20581 | 1480 | 1041 | ✅ **COMPLETE** (row 20580) — 859 PASS / 182 FAIL |
| DR Congo | 20582–21579 | 998 | 586 | ✅ **COMPLETE** (row 21576) — 459 PASS / 127 FAIL |
| Ecuador | 21580–22765 | 1186 | 782 | ✅ **COMPLETE** (row 22765) — 725 PASS / 57 FAIL |
| Egypt | 22766–23686 | 921 | 636 | ✅ **COMPLETE** (row 23686) — 532 PASS / 104 FAIL |
| England | 23687–25401 | 1715 | 1315 | ✅ **COMPLETE** (row 25401) — 1228 PASS / 87 FAIL |
| France | 25402–27324 | 1923 | 1413 | ✅ **COMPLETE** (row 27324) — 1237 PASS / 176 FAIL |
| Germany | 27325–29165 | 1841 | 1356 | ✅ **COMPLETE** (row 29161) — 1291 PASS / 65 FAIL |
| Ghana | 29166–30309 | 1144 | 855 | ✅ **COMPLETE** (row 30309) — 783 PASS / 72 FAIL |
| Iran | 30310–31698 | 1389 | 926 | ✅ **COMPLETE** (row 31698) — 775 PASS / 151 FAIL |
| Iraq | 31699–32567 | 869 | 537 | ✅ **COMPLETE** (row 32567) — 425 PASS / 112 FAIL |
| Italy | 32568–34327 | 1760 | 1286 | ✅ **COMPLETE** (row 34327) — 1061 pass-all / 225 fail-liveness |
| Jamaica | 34328–34953 | 626 | 424 | ✅ **COMPLETE** (row 34953) — 381 PASS / 43 FAIL |
| Japan | 34954–36397 | 1444 | 997 | ✅ **COMPLETE** (row 36397) — 935 PASS / 62 FAIL |
| Jordan | 36398–37773 | 1376 | 850 | ✅ **COMPLETE** (row 37773) — 691 PASS / 159 FAIL |
| Mexico | 37774–39364 | 1591 | 1074 | ✅ **COMPLETE** (row 39364) — 901 PASS / 173 FAIL |
| Morocco | 39365–40186 | 822 | 558 | ✅ **COMPLETE** (row 40186) — 460 pass-all / 98 fail-liveness |
| Netherlands | 40187–41273 | 1087 | 878 | ✅ **COMPLETE** (row 41273) — 761 pass-all / 117 fail-liveness |
| New Zealand | 41274–42086 | 813 | 564 | ✅ **COMPLETE** (row 42086) — 398 PASS / 166 FAIL |
| Nigeria | 42087–42203 | 117 | 93 | ✅ **COMPLETE** (row 42203) — 91 PASS / 2 FAIL |
| Paraguay | 42204–42927 | 724 | 505 | ⬜ not started |
| Senegal | 42928–43782 | 855 | 661 | ⬜ not started |
| Switzerland | 43783–44756 | 974 | 832 | ⬜ not started |
| Tunisia | 44757–45514 | 758 | 573 | ✅ **COMPLETE** (row 45514) — 500 PASS / 73 FAIL |
| USA | 45515–46518 | 1004 | 689 | ✅ **COMPLETE** (row 46518) — 611 PASS / 78 FAIL |

## 5. How to run the loop (exact procedure, per chunk ~25–90 candidate rows)

**Step 0 — pin your file set from the batch the user chose (§A rule 1).** The procedure is
identical for every track; only these four files change. Use the row in this selector for your
batch and keep them straight all session:

| Track | Pool file (drive off this) | `explanation` source | PASS → | FAIL → |
|-------|----------------------------|----------------------|--------|--------|
| **Batch 1** | `QA_PASSED.md` | `Pre-worldcup-clean.csv` (same Row N) | `QA_PASSED_ALL.md` | `QA_FAILED_LIVENESS_PASSED_OTHERS.md` |
| **Batch 2** | `QA_PASSED_b2.md` | `Pre-worldcup2.csv` (same Row N — **different numbering!**) | `QA_PASSED_ALL_b2.md` | `QA_FAILED_LIVENESS_b2.md` |
| **Cleaned** | `QA_PASSED_cleaned.md` | already in `QA_CLEANED_dataset.csv` (same row order) | `QA_PASSED_ALL_cleaned.md` | `QA_FAILED_LIVENESS_cleaned.md` |

Below, **POOL** = your batch's pool file, **DATASET** = its explanation source, **PASS/FAIL** = its
two output files.

1. **Print the next chunk from POOL** — parse it for `### Row N` within your country's range and
   read each entry's Q / Answer / Options straight from POOL. Then, for those same `Row N`, look up
   the **`explanation`** field in DATASET (POOL omits it; for the Cleaned track it's already in the
   dataset). Each candidate = Q, Answer, Options (from POOL) + explanation (from DATASET). **Never
   check a row that isn't in POOL.** (See the `python3` snippets in `QA_TC06_LIVE.md` for the
   parse pattern — adapt the filename to your batch.)
2. **Build a per-country fact base first** (squad/results/qualification history), then adjudicate.
   Only run new `WebSearch`/`WebFetch` for facts not already established this session.
3. For each candidate decide **PASS / FAIL / UNVERIFIED→FAIL** per §6. *(Cleaned track only: also
   FAIL if the spliced explanation contradicts the now-fixed answer — see §9(c).)*
4. Append: PASS → PASS file; FAIL → FAIL file (group per fact-cluster to stay concise; always cite
   a source URL; for fails give a concrete remedy).
5. **Update state for your batch:** the `Total …` lines in both output files, the §3 grand total,
   and your batch's status row — **§4** (batch 1) or **§9(d)+§9(e)** (batch 2) or **§9(f)**
   (cleaned). For batch 1 also advance the cursor + batch table in `QA_TC06_LIVE.md`.
6. Report the chunk result to the user. **Before they push, confirm the right batch's status tables
   (and the §3 grand total) are updated.**

## 6. Judgment rules (be consistent — apply to ALL tracks; these are what Algeria was graded on)

- **PASS** = answer AND explanation both factually correct, and the answer is **unique** (no
  distractor is also correct).
- **FAIL** if any of: answer wrong; explanation wrong; **false premise** (asserts an event that
  didn't happen — e.g. a team "at the 2022 World Cup" that failed to qualify); **non-unique
  answer** (a distractor is also valid — "which *other* nation…" and "which player has [generic
  trait]" are the usual culprits); self-referential answer ("which nation like X → X"); internal
  temporal contradiction.
- **UNVERIFIED → FAIL** (conservative): soft/narrative claims with no authoritative source —
  e.g. "squad rebuild" dates/ages, obscure squad-composition counts, unconfirmed goal tallies.
- A row may pass TC-06 yet still carry a mechanical flag noted in QA_PASSED/QA_FAILED — note it
  but judge TC-06 on factual grounds.
- Watch for **spreadsheet date-corruption**: a scoreline like `2-1` can appear as `02-Jan` in the
  `answer` cell (Excel mangling). Treat as a broken answer (FAIL) and flag for a dataset sweep.

## 7. Recurring defect patterns found in Algeria (likely repeat per country, ALL tracks — watch for them)

1. **Mislabeled play-offs** — calling a CAF play-off "intercontinental" (or claiming a team
   qualified "directly" when they went through a play-off).
2. **False "qualified/played at WC YYYY"** when the team actually failed to qualify that year.
3. **Stale facts** — e.g. trophy counts that changed after 2023.
4. **Non-unique answers** — distractors that are also correct (other scorers, other qualifiers,
   other clubs in the same league, players sharing a generic trait like "90+ caps").
5. **Fabricated player/club histories** — e.g. Europe-developed players credited to a domestic club.
6. **Wrong dates/scorers/minutes** — goal minutes, who scored, debut years, record-setting dates.
7. **Self-referential / "which *other* nation"** answers that name the subject team itself.
8. **Unverifiable "squad rebuild / squad age"** narrative claims, and self-referential
   explanations ("The verified fact states…", also caught mechanically as GEN-7).

## 8. File inventory

| File | What it is |
|------|-----------|
| `QA_REVIEW_PROMPT.md` | The original task spec / test battery |
| `Pre-worldcup-clean.csv` | Underlying dataset. The check is driven off `QA_PASSED.md`; open this **only** to look up the `explanation` field (which `QA_PASSED.md` omits) for the same Row N. Row numbers match `QA_PASSED.md`. |
| `Pre-worldcup.csv` / `.md` | Pre-repair originals (don't use) |
| `repair_worldcup.py` | The CSV repair pass (already applied) |
| `tc_validate.py` | Original mechanical validator |
| `qa_review.py` | Full mechanical+heuristic QA → QA_PASSED.md / QA_FAILED.md |
| `VALIDATION_REPORT.md` | Notes on the repair + which TCs apply |
| `QA_PASSED.md` / `QA_FAILED.md` | Mechanical+heuristic verdicts (all 46k rows). **Liveness pool = rows in `QA_PASSED.md`.** |
| `QA_TC06_LIVE.md` | TC-06 live-check log + **cursor** + per-batch tables |
| `QA_TC06_PASSED.md` / `QA_TC06_FAILED.md` | TC-06 live verdicts for Algeria **rows 2–230 only** (old method) |
| `QA_PASSED_ALL.md` | **Ship-ready**: passed mechanical **and** liveness (new method) |
| `QA_FAILED_LIVENESS_PASSED_OTHERS.md` | **Dangerous**: passed mechanical but **failed liveness** |
| `HANDOFF.md` | This file — shared coordination state; **keep it updated and commit it** |
| `QA_CLEANED.csv` | The ex-`QA_FAILED.md` rows, "rectified programmatically" and sent back (schema `Row,Country,Difficulty,Question,Answer,Options,Failed,Why,Remedy`; **no explanation column**). Input to §9. |
| `adapt_cleaned.py` → `QA_CLEANED_dataset.csv` | Adapter that converts `QA_CLEANED.csv` to the 7-col dataset schema for re-check (splices `explanation` back from `Pre-worldcup-clean.csv` by Row). |
| `PRE-worldcup2.xlsx` | **Batch 2** raw source (xlsx). Corrupted like batch-1 raw: broken `options` quoting + UTF-8/Latin-1 mojibake. |
| `convert_batch2.py` → `Pre-worldcup2.csv` | Converts/repairs batch 2 to clean 7-col CSV (reuses `repair_worldcup.extract_options` + a demojibake pass). |
| `QA_PASSED_b2.md` / `QA_FAILED_b2.md` | Batch-2 mechanics verdicts. `QA_PASSED_b2.md` = batch-2 liveness pool. |
| `QA_PASSED_cleaned.md` / `QA_FAILED_cleaned.md` | Cleaned-rows mechanics re-check. `QA_FAILED_cleaned.md` = still broken → send back. |
| `QA_PASSED_ALL_b2.md` / `QA_FAILED_LIVENESS_b2.md` | Batch-2 liveness results (to be produced by the loop). |
| `QA_PASSED_ALL_cleaned.md` / `QA_FAILED_LIVENESS_cleaned.md` | Cleaned-rows liveness results (to be produced by the loop). |

## 9. Batch 2 & Cleaned re-check (parallel tracks — kept separate from batch 1)

`qa_review.py` is now **parameterized**: `--src/--passed/--failed` (defaults unchanged, so a bare
`python3 qa_review.py` still reproduces batch 1: 32,490 / 14,027). It also warns when a row's
country is missing from the `ADJ` keyword map (those would false-fail TC-03). The `ADJ` map was
**extended with the 17 new batch-2 countries** (Bosnia and Herzegovina, Curaçao, Czechia, Haiti,
Norway, Panama, Portugal, Qatar, Saudi Arabia, Scotland, South Africa, South Korea, Spain, Sweden,
Türkiye, Uruguay, Uzbekistan).

### (a) Cleaned rows (ex-`QA_FAILED.md`, "rectified programmatically")
```
python3 adapt_cleaned.py                                   # QA_CLEANED.csv -> QA_CLEANED_dataset.csv (3489 rows)
python3 qa_review.py --src QA_CLEANED_dataset.csv \
        --passed QA_PASSED_cleaned.md --failed QA_FAILED_cleaned.md
```
**Result: only 393 of 3,489 clear the re-check; 3,096 still FAIL.** ⚠️ The dominant failure is
**TC-06 (2,179)** because `QA_CLEANED.csv` dropped the explanation column — the cleaning fixed
Q/A/Options but **not the explanations**, and the original self-referential explanations
(re-attached from the master CSV) re-trigger TC-06. Also **613 rows have the answer not among the
options** (TC-05). **Action:** the 3,096 in `QA_FAILED_cleaned.md` are not ready — send back for a
second fix round that also rewrites explanations. The 393 in `QA_PASSED_cleaned.md` go to liveness.

### (b) Batch 2
```
python3 convert_batch2.py                                  # PRE-worldcup2.xlsx -> Pre-worldcup2.csv (51,061 rows)
python3 qa_review.py --src Pre-worldcup2.csv \
        --passed QA_PASSED_b2.md --failed QA_FAILED_b2.md
```
**Result: 39,321 PASS / 11,740 FAIL.** `QA_PASSED_b2.md` is the batch-2 liveness pool. (~823 rows'
options didn't recover to exactly 3, and ~1,012 still carry stubborn mojibake — both surface as
mechanical fails, which is the safe outcome.)

### (c) Liveness for both new tracks
Run the **exact same §5 procedure and §6/§7 judgment rules** as batch 1 — only the I/O files change:
- **Batch 2:** drive off `QA_PASSED_b2.md`; look up `explanation` in **`Pre-worldcup2.csv`** (NOT the
  batch-1 CSV — row numbers differ!); route PASS → `QA_PASSED_ALL_b2.md`,
  FAIL → `QA_FAILED_LIVENESS_b2.md`.
- **Cleaned:** drive off `QA_PASSED_cleaned.md`; `explanation` is already in
  `QA_CLEANED_dataset.csv` (same row order). Route PASS → `QA_PASSED_ALL_cleaned.md`,
  FAIL → `QA_FAILED_LIVENESS_cleaned.md`. ⚠️ Extra liveness caveat for cleaned rows: the
  explanation was spliced from the *original* row, so if the cleaning changed the answer the
  explanation may now contradict it — treat answer/explanation mismatch as a FAIL.
After each session, re-sum the **GRAND TOTAL** line in §3 across all three `QA_PASSED_ALL*` files.

### (d) Batch-2 per-country coordination table (THE batch-2 claim table — same role as §4)
Same rules as §A/§4: **claim a country**, set Status to your name + "in progress", only liveness
rows that are in `QA_PASSED_b2.md`, and update this table + §3 grand total + the batch-2 totals in
(e) before you push. `QA_PASSED_b2` = how many of that country's rows are in `QA_PASSED_b2.md`.
Row numbers are **lines in `Pre-worldcup2.csv`** (header = line 1) and match `QA_PASSED_b2.md`.

> ⚠️ Batch 2 is a **different file with different row numbers** from batch 1 — e.g. batch-2
> "Algeria 2–513" is NOT batch-1 "Algeria 2–1228". Always confirm you opened `Pre-worldcup2.csv`.

| Country | CSV rows | total | QA_PASSED_b2 | Status / last verified row |
|---------|----------|------:|----------:|----------------------------|
| Algeria | 2–513 | 512 | 428 | ✅ **COMPLETE** (row 513) — 269 PASS / 159 FAIL |
| Argentina | 514–1543 | 1030 | 829 | ✅ **COMPLETE** (row 1543) — 662 PASS / 167 FAIL |
| Australia | 1544–2400 | 857 | 716 | ⬜ not started |
| Austria | 2401–3241 | 841 | 740 | ⬜ not started |
| Belgium | 3242–4191 | 950 | 788 | ✅ **COMPLETE** (row 4191) — 618 PASS / 170 FAIL |
| Bosnia and Herzegovina | 4192–5804 | 1613 | 1073 | ✅ **COMPLETE** (row 5804) — 948 PASS / 125 FAIL |
| Brazil | 5805–6402 | 598 | 517 | ⬜ not started |
| Cabo Verde | 6403–7107 | 705 | 450 | ⬜ not started |
| Cameroon | 7108–7820 | 713 | 592 | ⬜ not started |
| Canada | 7821–9330 | 1510 | 1129 | ✅ **COMPLETE** (row 9330) — 1060 PASS / 69 FAIL |
| Chile | 9331–10795 | 1465 | 1193 | ⬜ not started |
| Colombia | 10796–11736 | 941 | 775 | ✅ **COMPLETE** (row 11736) — 607 PASS / 168 FAIL |
| Costa Rica | 11737–12858 | 1122 | 931 | ✅ **COMPLETE** (row 12858) — 792 PASS / 139 FAIL |
| Croatia | 12859–14120 | 1262 | 1029 | ⬜ not started |
| Curaçao | 14121–16003 | 1883 | 1159 | ⬜ not started |
| Czechia | 16004–16893 | 890 | 702 | ⬜ not started |
| DR Congo | 16894–17345 | 452 | 345 | ⬜ not started |
| Ecuador | 17346–18086 | 741 | 624 | ⬜ not started |
| Egypt | 18087–18876 | 790 | 683 | ⬜ not started |
| England | 18877–20254 | 1378 | 1175 | ⬜ not started |
| France | 20255–21124 | 870 | 742 | ⬜ not started |
| Germany | 21125–21194 | 70 | 60 | ⬜ not started |
| Haiti | 21195–22697 | 1503 | 939 | ⬜ not started |
| Iran | 22698–23586 | 889 | 692 | ⬜ not started |
| Iraq | 23587–24379 | 793 | 567 | ⬜ not started |
| Japan | 24380–25217 | 838 | 684 | ⬜ not started |
| Jordan | 25218–25979 | 762 | 577 | ⬜ not started |
| Mexico | 25980–26815 | 836 | 646 | ⬜ not started |
| Morocco | 26816–27006 | 191 | 147 | ⬜ not started |
| Netherlands | 27007–27485 | 479 | 406 | ⬜ not started |
| New Zealand | 27486–28080 | 595 | 440 | ⬜ not started |
| Norway | 28081–29812 | 1732 | 1388 | ⬜ not started |
| Panama | 29813–31099 | 1287 | 943 | ⬜ not started |
| Paraguay | 31100–31761 | 662 | 517 | ⬜ not started |
| Portugal | 31762–33741 | 1980 | 1550 | ⬜ not started |
| Qatar | 33742–34843 | 1102 | 791 | ⬜ not started |
| Saudi Arabia | 34844–36341 | 1498 | 1050 | ⬜ not started |
| Scotland | 36342–38412 | 2071 | 1597 | ⬜ not started |
| Senegal | 38413–39239 | 827 | 664 | ⬜ not started |
| South Africa | 39240–40419 | 1180 | 816 | ⬜ not started |
| South Korea | 40420–42027 | 1608 | 1214 | ⬜ not started |
| Spain | 42028–43364 | 1337 | 1030 | ⬜ not started |
| Sweden | 43365–45111 | 1747 | 1396 | ⬜ not started |
| Switzerland | 45112–46456 | 1345 | 1158 | ⬜ not started |
| Tunisia | 46457–47006 | 550 | 445 | ⬜ not started |
| Türkiye | 47007–48666 | 1660 | 1234 | ⬜ not started |
| Uruguay | 48667–50153 | 1487 | 1128 | ⬜ not started |
| Uzbekistan | 50154–51062 | 909 | 622 | ⬜ not started |

### (e) Batch-2 running totals (update every session)
- **`QA_PASSED_ALL_b2.md` (ship-ready):** 4956 *(Algeria 269 + Argentina 662 + Belgium 618 + Bosnia and Herzegovina 948 + Canada 1060 + Colombia 607 + Costa Rica 792; pool = 39,321 across 48 countries)*
- **`QA_FAILED_LIVENESS_b2.md` (dangerous):** 997 *(Algeria 159 + Argentina 167 + Belgium 170 + Bosnia and Herzegovina 125 + Canada 69 + Colombia 168 + Costa Rica 139)*
- **Countries COMPLETE (batch 2):** 7 of 48 (Algeria 269/159, Argentina 662/167, Belgium 618/170, Bosnia and Herzegovina 948/125, Canada 1060/69, Colombia 607/168, Costa Rica 792/139). Next sequential not-started: **Australia** (rows 1544–2400).

### (f) Cleaned-track status — ✅ LIVENESS COMPLETE
All 393 rows in `QA_PASSED_cleaned.md` (36 countries) have been TC-06 liveness-checked.
Totals: **`QA_PASSED_ALL_cleaned.md`** **359** ship-ready · **`QA_FAILED_LIVENESS_cleaned.md`**
**34** dangerous (359 + 34 = 393 ✓). The 3,096 in `QA_FAILED_cleaned.md` are **not** in scope for
liveness — they go back for a second mechanical fix round (must also rewrite explanations; see §9(a)).

**The 34 liveness fails cluster into recurring defect types (see §7):**
- **Non-unique / unverifiable "key players/scorers/clubs" soft narratives** (the biggest cluster):
  Netherlands 2847, Mexico 2873, DR Congo 2124, Colombia 1880/1907, Belgium 2781, and the six Chile
  Sánchez/Vidal rows (1849, 1852, 2824–2826, 2830).
- **Self-referential "closest to itself" stadium questions:** Costa Rica 2708, Chile 2707.
- **Non-unique answers where ≥2 options are correct:** USA 1474 (all four 2026 venue/city pairs
  correct), France 510 (Stade de France 80,698 *and* 81,338 both offered), Denmark 1425 (Telia Parken
  = Parken), Switzerland 1430 (Stade de Suisse = Wankdorf; also wrong venue/date), CIV 1488.
- **Wrong figure for a stated tournament/year (correct value often offered as a distractor):**
  Switzerland 409 (Euro 2008 = 42,500), Germany 383 (Euro 2024 Allianz = 66,000), England 335/747
  (2010 qualifying was 9W-0D-1L), Croatia 702 (Euro 2024 was 0W-2D-1L), Belgium 385/517/518/519/520/607
  (FIFA #1 streak ~1,290 days, never 1,735 — impossible vs the 1,352-day cumulative).
- **Wrong fact / false premise:** Argentina 815 (no Arg–Bra match at Copa 2024), Iraq 1340 (Zico hired
  2011 not 2012), Egypt 2083 (2010 AFCON final won 1–0, not on penalties), Senegal 1210 (2008 AFCON
  hosted by Ghana, not Senegal).
