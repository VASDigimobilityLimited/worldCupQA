# QA Review Prompt — World Cup Trivia Question Set

You are a **QA reviewer for a competitive World Cup trivia app**. Your job is to
check every question in the dataset against the test battery below, decide
**PASS or FAIL**, and write the results into **two Markdown files**:

- `QA_PASSED.md` — every question that passes, with the reason(s) it passed.
- `QA_FAILED.md` — every question that fails, with the reason(s) it failed **and**
  a remedy (the corrected / right version of the question, or a recommendation to
  drop it if it cannot be salvaged).

A question **PASSES only if it clears every applicable test**. If it fails even one
test, it goes in `QA_FAILED.md` (list *all* failing tests, not just the first).

---

## 1. Inputs

- **Dataset:** `Pre-worldcup-clean.csv` (columns: `category_id, country, question,
  answer, options, difficulty, explanation`). `options` is a JSON array of the **3
  distractors**; the correct choice is `answer`, stored separately. The four
  rendered choices = `answer` + the 3 distractors (shuffled at runtime).
- **Deterministic validator:** `tc_validate.py` — already implements the mechanical
  tests (TC-01, 04, 05, 08, 09, 10, 11, 13, 15, 16). **Run it first** and use its
  row-level flags as the mechanical layer; you supply judgment for the rest.
- **Sources** used to generate the questions (for factual cross-referencing, TC-06):
  mlssoccer.com, intermiamicf.com, wikipedia.org, aljazeera.com, coachesvoice.com,
  cbssports.com, 365scores.com, theguardian.com. Treat Wikipedia + official FIFA
  records as the tie-breaker.
- **Generation context** (Section 3) — the prompts the questions were written
  against. Several generation rules are themselves QA criteria; enforce them.

---

## 2. Test battery

### A. Mechanical tests (from `tc_validate.py` — verify, don't re-derive by hand)

- **TC-01 — Duplicate Questions:** identical text (exact) or near-duplicate (token
  similarity ≥ 85% within the same country + answer). Near-dups: keep the best-worded
  one, fail the rest as duplicates.
- **TC-04 — Question Coherence:** blank, under 10 characters, or no question word
  (who/what/when/where/which/how).
- **TC-05 — Incomplete Options:** not exactly **3 distractors**, any blank distractor,
  or two identical distractors.
- **TC-08 — Difficulty Validity:** blank, or not one of easy/medium/hard.
- **TC-09 — Category Validity:** blank `country` (the real category; `category_id` is a
  constant `12` and is ignored).
- **TC-10 — Encoding & Whitespace:** leading/trailing spaces, unrendered HTML entities
  (`&amp;`), or hidden control characters in any field.
- **TC-11 — Numeric Plausibility:** a year **presented as a World Cup edition**
  (`<year> World Cup` / `World Cup <year>`, excluding "… qualifiers") that is not a
  real men's or women's edition (e.g. "2024 World Cup", "2021 World Cup cycle").
  Incidental years (FA founded 1863, "2019 AFCON", "2021 Copa") are **not** flagged.
- **TC-13 — Letter Reference:** text like "see option B" / "choose answer A".
- **TC-15 — Time Span:** any World Cup edition referenced in the question or correct
  answer that falls outside **2006–2026**.
- **TC-16 — Distractor Equals Answer:** a distractor equal to the answer — exactly, by
  alias/synonym (USA ≡ United States, Group stage ≡ Group phase), or by filler word
  (2018 World Cup ≡ 2018 FIFA World Cup). Do **not** fail distractors that merely look
  similar but differ in the key fact (2022 vs 2026).

### B. Judgment tests (you decide — this is the core of your value)

- **TC-03 — Mismatched / Irrelevant Options:** Do all four choices make sense as
  answers to *this* question? Fail if a distractor is the wrong type or off-topic
  (e.g. a stadium among players, a manager among years).
- **TC-06 — Factual Accuracy:** Is `answer` actually correct, and is `explanation`
  true? Cross-reference the sources above + FIFA records. Fail if the answer is wrong,
  the explanation is wrong, or the question asserts an event that did not happen.
  **Men's-vs-women's nuance:** a year can be a valid edition yet wrong for the subject
  (e.g. a male player asked about "the 2023 World Cup", which was the Women's edition).
  That is a TC-06 failure even though TC-11 passes.
- **TC-14 — Tip-Off Language:** Can a player guess without knowing football? Fail if one
  option is grammatically/structurally a giveaway, or if the distractors aren't equally
  plausible (the "obviousness" check from the generation pipeline).

### C. Generation-rule compliance (derived from Section 3 — enforce as QA criteria)

Map each violation to the closest test ID in the failure report, or label it
`GEN-RULE`:

1. **Self-contained / nation named** — the question must explicitly name the nation or
   its nationality adjective (e.g. "Which **Argentina** player…"). A question that
   needs external category context to make sense fails (relates to TC-03/TC-04).
2. **Tournament anchor** — must reference a specific year or tournament edition; never
   "currently"/"recently".
3. **No negative framing** — no "did NOT", "never", "which is NOT".
4. **Answer length** — `answer` ≤ 4 words, no explanation embedded.
5. **Format uniformity** — all four choices share one format/type/word-count (all bare
   names, all years, all "Name + action", etc.) (relates to TC-14/TC-03).
6. **Ends with a question mark.**
7. **Explanation quality** — one natural sentence; must NOT say "the dataset",
   "according to the data", "as recorded", etc.
8. **Distractors real & wrong** — every distractor must be a real football entity and
   verifiably incorrect for this question (relates to TC-06/TC-16).
9. **Temporal boundary 2006–2026** (reinforces TC-15).

---

## 3. How the questions were generated (context for judgment)

Questions were produced by an LLM constrained to **VERIFIED REFERENCE DATA** (it was
told to invent nothing), then distractors were generated and an "obviousness" check
was run. The key writer rules: under 14–18 words; answer ≤ 4 words; all distractors
the same type/word-count/format as the answer and **actually wrong**; positive framing
only; must name the nation; must anchor to a 2006–2026 tournament; explanation is one
natural sentence. The distractor prompt required wrong answers to be real entities that
are never also correct. The obviousness prompt failed any set where one option is a
category or visual-format outlier.

**Use these as the standard the questions were meant to meet.** A question that breaks
its own generation rules is a QA failure even if it is factually true.

---

## 4. Procedure

1. **Run** `python3 tc_validate.py` to get the mechanical row-level flags.
2. **Iterate every row.** For each, collect mechanical flags, then apply the judgment
   tests (TC-03, TC-06, TC-14) and the generation-rule checks.
3. **Decide:** PASS if zero failing tests; otherwise FAIL.
4. **Write** the two files (formats below). Process in batches and **append** so the
   run is resumable; keep rows in dataset order and cite the CSV row number.
5. For **TC-06**, when you cannot verify a fact from the sources or reliable records,
   do **not** assert it is correct — mark it `UNVERIFIED` under TC-06 and place it in
   `QA_FAILED.md` with a note that it needs source confirmation. Be conservative:
   a competitive quiz must not ship unverified facts.

---

## 5. Output format

### `QA_PASSED.md`

```markdown
# QA — Passed Questions

Total passed: <N>

---

### Row <row#> — <country> (<difficulty>)
**Q:** <question>
**Answer:** <answer>
**Options:** <answer> | <d1> | <d2> | <d3>
**Why it passed:** Clears all tests. Coherent and self-contained (names <country>),
answer is factually correct per <source>, distractors are real, same-type, and
plausible (TC-03/14 ok), edition is in-range (TC-11/15 ok), no duplicates (TC-01 ok).
```

### `QA_FAILED.md`

```markdown
# QA — Failed Questions

Total failed: <N>

---

### Row <row#> — <country> (<difficulty>)
**Q:** <question>
**Answer:** <answer>
**Options:** <answer> | <d1> | <d2> | <d3>
**Failed:** TC-06, TC-14   <!-- list every failing test -->
**Why it failed:**
- TC-06: <answer> is incorrect — <correct fact> per <source>.
- TC-14: distractor "<x>" is a structural giveaway (only one with a year).
**Remedy (corrected version):**
- **Q:** <fixed question, or "same">
- **Answer:** <corrected answer>
- **Options:** <answer> | <fixed d1> | <fixed d2> | <fixed d3>
- **Difficulty:** <fixed if needed>
- *If unsalvageable* (e.g. asserts a non-existent event with no source support):
  **Recommend removal** — <one-line reason>.
```

**Rules for the remedy:** keep the original intent and the same answer type; obey all
generation rules in the rewrite (≤ 4-word answer, real same-type distractors, 2006–2026
anchor, names the nation, positive framing, ends with "?"). If a near-duplicate (TC-01),
the remedy is "drop — duplicate of row <#>". If a fact cannot be verified, the remedy is
"hold for source confirmation", not a guessed correction.

---

## 6. Quality bar

- Every failure entry must name the **specific** problem and a **concrete** fix — never
  "looks wrong".
- Prefer correcting over deleting, but never invent facts to make a question pass.
- When multiple tests fail, fix all of them in the single remedy.
- Be consistent: the same issue gets the same TC label and the same style of fix
  everywhere.
