# HANDOFF — World Cup Trivia QA Review

> For any Claude (or person) resuming this work after pulling the repo. **Read this top to
> bottom.** This is a **shared, multi-contributor** effort: several people pull this repo and
> run the live fact-check in parallel, each taking a different country/row range. The rules in
> §A exist so nobody clobbers anyone else's work.

---

## A. ⚠️ COLLABORATION RULES (read first — this repo has multiple contributors)

**This repo is pulled and worked on by several people at once.** Before doing anything:

1. **ASK the user which country and which rows they want to start from.** Do **not** assume.
   Show them the per-country status table in **§4** (which country is done / in-progress / not
   started, and each country's row range) and let them pick a country and a starting row
   *inside* that country. The unit of work is "a country (or a row range within a country)."
2. **Only liveness-check rows that are present in `QA_PASSED.md`** (the mechanically/heuristically
   passed pool). Skip any row in `QA_FAILED.md` — those already fail, no point fact-checking them.
3. **Coordinate so two people don't check the same rows.** Pick a country/range nobody else has
   claimed (see §4 "Status"). If unsure, ask the user to confirm with their team.
4. **Before pushing back to the repo, you MUST update this handoff document** (`HANDOFF.md`):
   - update the country's row in the §4 status table (Status, "last verified row", counts),
   - bump the totals in §3,
   - and advance the cursor + per-batch table in `QA_TC06_LIVE.md`.
   **Remind the user to do this every session, before they `git push`.** A push without an
   updated handoff will desync everyone.
5. `HANDOFF.md` is **tracked in git** (it is no longer git-ignored) precisely so this shared
   state travels with the repo. Keep it accurate.

**Suggested per-session flow for a contributor's Claude:**
> "Which country do you want to work on, and from which row? Here's what's done so far …
> [show §4 table]. I'll only check rows that are in `QA_PASSED.md` and route results into
> `QA_PASSED_ALL.md` / `QA_FAILED_LIVENESS_PASSED_OTHERS.md`. When we stop, I'll update
> `HANDOFF.md` and `QA_TC06_LIVE.md` so you can push clean state back."

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
applicable test; otherwise it FAILS (list all failing tests + a concrete remedy).

**What you fact-check:** the questions listed in **[QA_PASSED.md](QA_PASSED.md)** — only those.
Each entry there gives `### Row N`, **Q**, **Answer**, **Options**, and a "Why it passed" note.
The question/answer/options text in `QA_PASSED.md` is verbatim the real question (it was generated
from the dataset; verified identical for every Algeria row).

**One gotcha — the `explanation` field:** `QA_PASSED.md` does **not** include each question's
`explanation`. But a question ships with its explanation, and a *wrong explanation* is a TC-06
failure (many Algeria fails were exactly this — "intercontinental playoff", etc.). The explanation
text lives only in the underlying dataset file **[Pre-worldcup-clean.csv](Pre-worldcup-clean.csv)**.
So: drive the loop off `QA_PASSED.md` (that's the set and the Q/A/Options), and open the CSV *only*
to look up the `explanation` for the same `Row N` you're checking. **Do not pull questions from the
CSV that aren't in `QA_PASSED.md`.**

**Dataset reference (for the `explanation` lookup only):** `Pre-worldcup-clean.csv` — **46,517 rows**,
data rows numbered **2–46518** (row N = line N of the CSV; header = line 1). Columns:
`category_id, country, question, answer, options, difficulty, explanation`. `options` is a JSON
array of the **3 distractors**; the correct choice is `answer` (stored separately). The 4 rendered
choices = answer + 3 distractors. `category_id` is constant 12 (ignore); the real category is
`country` (**38 countries, alphabetical**, Algeria → USA). Row numbers match `QA_PASSED.md` exactly.

## 2. What is already DONE

### (a) Mechanical + heuristic pass — COMPLETE for all 46,517 rows
- Script: [qa_review.py](qa_review.py) (built on [tc_validate.py](tc_validate.py)).
- Outputs (regenerate by `python3 qa_review.py`):
  - [QA_PASSED.md](QA_PASSED.md) — 32,490 rows  ← **the liveness pool**
  - [QA_FAILED.md](QA_FAILED.md) — 14,027 rows  ← skip these
- Covers TC-01 (near-dup), TC-03, TC-04, TC-05, TC-06 *proxy only*, TC-08, TC-10, TC-11, TC-13,
  TC-14, TC-15, TC-16, generation rules. **Negative-framing rule was removed at the user's
  request** — do not re-add it. This layer does NOT verify factual accuracy — see (b).

### (b) TC-06 LIVE factual fact-check — IN PROGRESS (this is the loop everyone runs)
Per-row, web-sourced verification of `answer` + `explanation`, **only on rows in `QA_PASSED.md`**.
Verdicts route into two files:
- **`QA_PASSED_ALL.md`** — passed mechanical/heuristic **AND** liveness (ship-ready).
- **`QA_FAILED_LIVENESS_PASSED_OTHERS.md`** — passed mechanical but **failed liveness**
  (the dangerous "looks clean but is factually wrong" rows). Each entry has reason + source URL + remedy.

**✅ Algeria is fully complete** (rows 2–1228). **✅ Argentina is also complete** (rows 1229–2160).
**✅ Brazil is complete** (rows 6097–8182): 1346 ship-ready / 218 dangerous — per-batch tables +
recurring-defect summary at the bottom of `QA_TC06_LIVE.md`. **🔵 Australia is in progress** (rows
2161–3241). The remaining countries are **not started** (§4).

> Note on rows 2–230 (Algeria only): these were done under an older method that checked *every*
> row (not just `QA_PASSED.md`). Their record lives in
> [QA_TC06_PASSED.md](QA_TC06_PASSED.md) / [QA_TC06_FAILED.md](QA_TC06_FAILED.md). From row 231
> onward, the new "QA_PASSED.md pool only" method applies. New countries use the new method
> throughout.

## 3. Running totals (update these every session)

- **Rows 2–230 (Algeria, old method):** 181 PASS / 48 FAIL.
- **New method (231+, all countries) — `QA_PASSED_ALL.md`:** **2462** ship-ready
  (Algeria 554 + Argentina 562 + Brazil 1346).
- **New method (231+, all countries) — `QA_FAILED_LIVENESS_PASSED_OTHERS.md`:** **504** dangerous
  (Algeria 176 + Argentina 110 + Brazil 218).
- **Total ship-ready so far (both methods):** 2594 (132 backfill rows 2–230 + 2462 new method).
- **✅ Brazil is COMPLETE** (rows 6097–8182): 1346 ship-ready / 218 dangerous = 1564 candidates
  (the full Brazil `QA_PASSED.md` pool; on-disk verified, no duplicates). Per-batch tables +
  recurring-defect summary at the bottom of `QA_TC06_LIVE.md`.

## 4. Per-country status (THE coordination table — pick from here, then update it)

`QA_PASSED` = how many of that country's rows are in `QA_PASSED.md` (i.e. how many need liveness).
Claim a country, set Status to your name + "in progress", and fill in the last verified row.

| Country | CSV rows | total | QA_PASSED | Status / last verified row |
|---------|----------|------:|----------:|----------------------------|
| Algeria | 2–1228 | 1227 | 907 | ✅ **COMPLETE** (row 1228) |
| Argentina | 1229–2160 | 932 | 672 | ✅ **COMPLETE** (row 2160) — 562 PASS / 110 FAIL |
| Australia | 2161–3241 | 1081 | 835 | 🔵 **in progress** — resume at row 2161 |
| Austria | 3242–4282 | 1041 | 761 | ⬜ not started |
| Belgium | 4283–6096 | 1814 | 1327 | ⬜ not started |
| Brazil | 6097–8182 | 2086 | 1564 | ✅ **COMPLETE** (row 8182) — 1346 PASS / 218 FAIL |
| Cabo Verde | 8183–9573 | 1391 | 696 | ⬜ not started |
| Cameroon | 9574–10745 | 1172 | 738 | ⬜ not started |
| Canada | 10746–12428 | 1683 | 1003 | ⬜ not started |
| Chile | 12429–13847 | 1419 | 960 | ⬜ not started |
| Colombia | 13848–15527 | 1680 | 1132 | ⬜ not started |
| Costa Rica | 15528–16571 | 1044 | 734 | ⬜ not started |
| Côte d'Ivoire | 16572–17486 | 915 | 542 | ⬜ not started |
| Croatia | 17487–19101 | 1615 | 1188 | ⬜ not started |
| Denmark | 19102–20581 | 1480 | 1041 | ⬜ not started |
| DR Congo | 20582–21579 | 998 | 586 | ⬜ not started |
| Ecuador | 21580–22765 | 1186 | 782 | ⬜ not started |
| Egypt | 22766–23686 | 921 | 636 | ⬜ not started |
| England | 23687–25401 | 1715 | 1315 | ⬜ not started |
| France | 25402–27324 | 1923 | 1413 | ⬜ not started |
| Germany | 27325–29165 | 1841 | 1356 | ⬜ not started |
| Ghana | 29166–30309 | 1144 | 855 | ⬜ not started |
| Iran | 30310–31698 | 1389 | 926 | ⬜ not started |
| Iraq | 31699–32567 | 869 | 537 | ⬜ not started |
| Italy | 32568–34327 | 1760 | 1286 | ⬜ not started |
| Jamaica | 34328–34953 | 626 | 424 | ⬜ not started |
| Japan | 34954–36397 | 1444 | 997 | ⬜ not started |
| Jordan | 36398–37773 | 1376 | 850 | ⬜ not started |
| Mexico | 37774–39364 | 1591 | 1074 | ⬜ not started |
| Morocco | 39365–40186 | 822 | 558 | ⬜ not started |
| Netherlands | 40187–41273 | 1087 | 878 | ⬜ not started |
| New Zealand | 41274–42086 | 813 | 564 | ⬜ not started |
| Nigeria | 42087–42203 | 117 | 93 | ⬜ not started |
| Paraguay | 42204–42927 | 724 | 505 | ⬜ not started |
| Senegal | 42928–43782 | 855 | 661 | ⬜ not started |
| Switzerland | 43783–44756 | 974 | 832 | ⬜ not started |
| Tunisia | 44757–45514 | 758 | 573 | ⬜ not started |
| USA | 45515–46518 | 1004 | 689 | ⬜ not started |

## 5. How to run the loop (exact procedure, per batch ~25–90 candidate rows)

1. **Print the next batch from `QA_PASSED.md`** — parse it for `### Row N` within your country's
   range and read each entry's Q / Answer / Options straight from `QA_PASSED.md`. Then, for those
   same `Row N`, look up the **`explanation`** field in `Pre-worldcup-clean.csv` (QA_PASSED.md
   omits it). So each candidate ends up with Q, Answer, Options (from QA_PASSED.md) + explanation
   (from the CSV). Never check a row that isn't in `QA_PASSED.md`. (See the `python3` snippets in
   `QA_TC06_LIVE.md` for the pattern.)
2. **Build a per-country fact base first** (squad/results/qualification history), then adjudicate.
   Only run new `WebSearch`/`WebFetch` for facts not already established this session.
3. For each candidate decide **PASS / FAIL / UNVERIFIED→FAIL** per §6.
4. Append: PASS → `QA_PASSED_ALL.md`; FAIL → `QA_FAILED_LIVENESS_PASSED_OTHERS.md` (group per
   fact-cluster to stay concise; always cite a source URL; for fails give a concrete remedy).
5. **Update state:** the `Total …` lines in both files, the §3 totals + §4 row here, and the
   cursor + a batch table in `QA_TC06_LIVE.md`.
6. Report the batch result to the user. **Before they push, confirm §3/§4 here are updated.**

## 6. Judgment rules (be consistent — these are what Algeria was graded on)

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

## 7. Recurring defect patterns found in Algeria (likely repeat per country — watch for them)

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
