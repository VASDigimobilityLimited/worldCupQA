#!/usr/bin/env python3
"""Adapt QA_CLEANED.csv (the programmatically-rectified ex-QA_FAILED rows) into the
7-column dataset schema that qa_review.py consumes, so the fixes can be re-checked.

QA_CLEANED.csv schema:
    Row, Country, Difficulty, Question, Answer, Options, Failed, Why it failed, Remedy
  - Options is a pipe-joined string (answer is NOT always first).
  - There is NO explanation column.

Output (QA_CLEANED_dataset.csv) schema (matches Pre-worldcup-clean.csv):
    category_id, country, question, answer, options(JSON 3 distractors), difficulty, explanation

Rules:
  - category_id -> constant 12.
  - distractors = the pipe parts with `answer` removed once (NOT parts[1:]). If `answer`
    is absent or the result isn't exactly 3 distinct distractors, we keep it malformed on
    purpose so the mechanics re-check (TC-05/TC-16) flags it — we do not silently repair.
  - explanation is spliced back from Pre-worldcup-clean.csv by the original Row number.
    (Caveat: if the answer was changed during cleaning, this explanation may be stale —
    a liveness-stage concern, flagged below, not blocked here.)
"""
import csv, json

CLEANED = "QA_CLEANED.csv"
MASTER = "Pre-worldcup-clean.csv"
OUT = "QA_CLEANED_dataset.csv"


def load_explanations(path):
    """row-number (line N, header = line 1) -> explanation."""
    expl = {}
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.reader(f); next(r)
        for n, row in enumerate(r, start=2):
            expl[n] = row[6]
    return expl


def main():
    expl_by_row = load_explanations(MASTER)
    n_no_answer = n_bad_count = n_no_expl = 0
    out_rows = []
    with open(CLEANED, newline="", encoding="utf-8") as f:
        r = csv.reader(f); next(r)
        for x in r:
            rownum, country, diff, q, ans, opts = x[0], x[1], x[2], x[3], x[4], x[5]
            parts = [p.strip() for p in opts.split("|")]
            distractors = list(parts)
            if ans.strip() in distractors:
                distractors.remove(ans.strip())
            else:
                n_no_answer += 1  # answer not among rendered options -> will fail re-check
            if len(distractors) != 3 or len(set(distractors)) != len(distractors):
                n_bad_count += 1
            try:
                expl = expl_by_row[int(rownum)]
            except (ValueError, KeyError):
                expl = ""
                n_no_expl += 1
            out_rows.append(["12", country, q, ans, json.dumps(distractors), diff, expl])

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["category_id", "country", "question", "answer",
                    "options", "difficulty", "explanation"])
        w.writerows(out_rows)

    print("wrote %s: %d rows" % (OUT, len(out_rows)))
    print("  answer not in options (expect TC-05/TC-16 fail): %d" % n_no_answer)
    print("  distractor count != 3 distinct (expect TC-05 fail): %d" % n_bad_count)
    print("  no explanation found by Row number: %d" % n_no_expl)


if __name__ == "__main__":
    main()
