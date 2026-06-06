#!/usr/bin/env python3
"""Repair the malformed Pre-worldcup.csv.

Root cause: the `options` field was serialized as  [opt1",  "opt2",  "opt3"]"
with a broken quoting scheme. Whenever an option value contains a comma
(e.g. "64,000", "Brasília, Federal District"), the comma is left outside any
quote, so an RFC-4180 parser splits the record into extra columns and pushes
`difficulty` / `explanation` to the right.

Fix strategy (operates on the already-tokenised columns):
  - cat/country/question/answer (cols 0-3) are reliably quoted -> trust them.
  - The options blob spans from the first field starting with '[' to the first
    field containing ']'. Re-joining those fields with ',' exactly reverses the
    spurious split (the delimiter consumed was a single comma; spaces are
    preserved as field content).
  - Parse the blob into 3 clean distractors.
  - difficulty = first easy/medium/hard token after the options blob (else '').
  - explanation = last non-empty, non-difficulty field.
Output a clean 7-column RFC-4180 CSV with options stored as a JSON array.
"""
import csv, json, re, sys

SRC = "Pre-worldcup.csv"
OUT = "Pre-worldcup-clean.csv"
VALID_DIFF = {"easy", "medium", "hard"}

def _clean_opt(p: str) -> str:
    p = p.strip().strip("[]").strip().strip(",").strip()
    # repair thousands separators that gained a space: "50, 000" -> "50,000"
    p = re.sub(r"(\d),\s+(\d{3})\b", r"\1,\2", p)
    return p

def extract_options(blob: str):
    """Quote-aware extraction. The source serialises options as
    [opt1",  "opt2",  "opt3"]" so option boundaries are marked by the '"'
    characters, while commas *inside* an option (numbers, name-lists) are not.
    Splitting on '"' and discarding pure-separator fragments recovers the
    options for every observed corruption pattern."""
    # protect escaped quotes inside an option value, e.g. Euro \"96 final
    blob = blob.replace('\\"', "\x00")
    parts = blob.split('"')
    out = []
    for p in parts:
        c = _clean_opt(p.replace("\x00", "'"))
        if c:
            out.append(c)
    return out

def reconstruct(row):
    cat, country, question, answer = row[0], row[1], row[2], row[3]
    fields = row[4:]
    # locate options span
    start = next((k for k, f in enumerate(fields) if f.lstrip().startswith("[")), None)
    status = "ok"
    if start is None:
        start = 0
        status = "no-open-bracket"
    end = next((k for k in range(start, len(fields)) if "]" in fields[k]), None)
    if end is None:
        end = start
        status = "no-close-bracket" if status == "ok" else status
    blob = ",".join(fields[start:end + 1])
    options = extract_options(blob)
    tail = fields[end + 1:]
    difficulty = ""
    for f in tail:
        if f.strip().lower() in VALID_DIFF:
            difficulty = f.strip().lower()
            break
    expl_cands = [f.strip() for f in tail if f.strip() and f.strip().lower() not in VALID_DIFF]
    explanation = expl_cands[-1] if expl_cands else ""
    if len(options) != 3 and status == "ok":
        status = f"opts={len(options)}"
    return [cat, country, question, answer, json.dumps(options, ensure_ascii=False),
            difficulty, explanation], status

def main():
    stats = {"total": 0}
    spilled = 0
    samples = []
    with open(SRC, newline="", encoding="utf-8") as f, \
         open(OUT, "w", newline="", encoding="utf-8") as g:
        r = csv.reader(f)
        next(r)  # header
        w = csv.writer(g)
        w.writerow(["category_id", "country", "question", "answer",
                    "options", "difficulty", "explanation"])
        for row in r:
            # pad short rows
            if len(row) < 7:
                row = row + [""] * (7 - len(row))
            stats["total"] += 1
            # did this row originally spill (more than one non-empty field
            # between answer and where options closed)?
            was_spilled = "]" not in row[4]
            if was_spilled:
                spilled += 1
            new, status = reconstruct(row)
            stats[status] = stats.get(status, 0) + 1
            w.writerow(new)
            if was_spilled and len(samples) < 6:
                samples.append((row, new))
    print("=== REPAIR SUMMARY ===")
    print("rows processed:", stats.pop("total"))
    print("rows that had spilled options (comma in a value):", spilled)
    print("reconstruction status counts:", stats)
    print()
    print("=== SPOT-CHECK: 6 previously-broken rows ===")
    for old, new in samples:
        print("RAW options region :", old[4:9])
        print("  -> answer       :", new[3])
        print("  -> options      :", new[4])
        print("  -> difficulty   :", repr(new[5]))
        print("  -> explanation  :", new[6][:70])
        print()

if __name__ == "__main__":
    main()
