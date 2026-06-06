# Pre-worldcup dataset — repair + validation

## 1. What was fixed

`Pre-worldcup.csv` had a broken `options` serialization (`[opt1",  "opt2",  "opt3"]"`).
Whenever an option value contained a comma (numbers like `64,000`, name-lists like
`Messi, Higuaín, Di María`, places like `Brasília, Federal District`), the comma fell
outside the quoting and an RFC-4180 parser split the record into extra columns —
corrupting `difficulty` and `explanation`. **739 rows** were affected.

`repair_worldcup.py` reverses this by re-joining the spilled columns and extracting
options with a quote-aware split. Result: **`Pre-worldcup-clean.csv`** — a clean
7-column file (`category_id, country, question, answer, options, difficulty,
explanation`) with `options` stored as a proper JSON array. All 46,517 rows now hold
exactly 3 distractors.

Data model: the 4 rendered choices = `answer` + 3 distractors (shuffled at runtime).

## 2. Test cases that WORK on this data (run by `tc_validate.py`)

| Test | What it checks | Flagged |
|------|----------------|--------:|
| **TC-01 Duplicates** | exact (normalized) + near-dup (token Jaccard ≥ 0.85, within country+answer) | 0 exact, **8,236 near-dup pairs** across 10,853 questions |
| **TC-04 Coherence** | blank / <10 chars / no question-word | **122** |
| **TC-05 Incomplete Options** *(adjusted)* | **exactly 3 distractors**, none blank, no duplicate distractor | **0** (all repaired) |
| **TC-08 Difficulty Validity** | blank or ∉ {easy, medium, hard} (case-insensitive) | **527** (genuinely blank in source) |
| **TC-09 Category Validity** *(fixed)* | checks **`country`** (the real category), not the constant `category_id=12` | **0** |
| **TC-10 Encoding & Whitespace** | leading/trailing spaces, HTML entities, control chars | **0** |
| **TC-11 Numeric Plausibility** *(adjusted)* | only years presented as **World Cup editions**; flag impossible editions (≠ any real men's/women's WC year) | **5** |
| **TC-13 Letter Reference** | "see option B" style text | **0** |
| **TC-15 Time Span** *(NEW)* | every World Cup edition referenced in question+answer must be **2006–2026** | **0** |
| **TC-16 Distractor = Answer** *(NEW)* | no distractor equals the answer — exact, alias/synonym, or filler-word match (`2018 World Cup` ≡ `2018 FIFA World Cup`) | **3** |

### Notes on the adjustments you asked for
- **TC-05 → 3 options** (not 4): the answer is stored separately, so the option list
  should contain exactly 3 distractors.
- **TC-11 → World Cup editions only**: incidental years (FA founded 1863, "2019 AFCON",
  "2021 Copa") are no longer flagged — only `<year> World Cup` / `World Cup <year>`
  phrasings, excluding "… World Cup qualifiers" (qualifiers happen in off years).
- **TC-15 → 2006–2026 span**: scoped to question + correct answer (distractors are
  intentionally wrong, so their older-edition mentions are fine).
- **TC-16 → exact + synonym**: uses normalized equality + alias groups + filler-word
  stripping. It deliberately does **not** use fuzzy string similarity, because
  plausible distractors are *meant* to look similar while differing in the key fact
  (`2022` vs `2026` World Cup). Deeper paraphrase synonyms need a semantic/LLM pass.

## 3. Test cases that do NOT work on this data model

- **TC-02 Answer Not in Options** — superseded. The answer is authoritative and stored
  separately; "is the answer among the options" is no longer meaningful. The real risk
  (a distractor coinciding with the answer) is now **TC-16**.
- **TC-07 Position Bias** — not evaluable. There is no stored A/B/C/D slot; choices are
  shuffled at runtime. Position bias can only be measured on the rendered output.
- **TC-12 Multiple Correct** — folded into **TC-16** (a distractor equal to the answer
  is the only way two choices can both be "correct" here).

## 4. Still needs a human / semantic pass

- **TC-03** mismatched options, **TC-06** factual accuracy, **TC-14** tip-off language —
  unchanged, human/LLM judgment.
- **TC-11 men's-vs-women's nuance**: a year can be a valid *edition* yet wrong for the
  subject (e.g. a male player asked about "the 2023 World Cup"). That's a **TC-06**
  factual issue, not a numeric one.
- **TC-01 / TC-16** paraphrase-level near-duplicates and synonyms beyond the alias list.

## 5. Files

- `Pre-worldcup-clean.csv` — repaired dataset (use this).
- `repair_worldcup.py` — the repair pass.
- `tc_validate.py` — the validator (runs in ~5s).
