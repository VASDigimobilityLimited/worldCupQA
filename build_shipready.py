#!/usr/bin/env python3
"""Combine all PASSED (ship-ready) questions from the three QA tracks into one CSV,
in the original 7-column dataset format:
    category_id,country,question,answer,options,difficulty,explanation

Source of truth = the three "passed-all" markdown files (mechanical + TC-06 liveness).
Each entry references a Row N which equals line N of that track's dataset CSV.
Batch-2 uses a mix of `### Row N` headers and grouped `- **Row N/M-P**` bullets.
"""
import csv, re, sys

# (passed-all file, dataset CSV, liveness-fail file, label)
TRACKS = [
    ("QA_PASSED_ALL.md",        "Pre-worldcup-clean.csv", "QA_FAILED_LIVENESS_PASSED_OTHERS.md", "batch1"),
    ("QA_PASSED_ALL_b2.md",     "Pre-worldcup2.csv",      "QA_FAILED_LIVENESS_b2.md",            "batch2"),
    ("QA_PASSED_ALL_cleaned.md","QA_CLEANED_dataset.csv", "QA_FAILED_LIVENESS_cleaned.md",       "cleaned"),
]
OUT = "WorldCup_ShipReady_ALL.csv"

# ranges like 179–186 / 179-186 ; singles like 166 ; slash lists 171/173/175
RANGE_RE = re.compile(r"(\d+)\s*[–‒—-]\s*(\d+)")
NUM_RE   = re.compile(r"\d+")

def parse_spec(spec):
    """Expand a row spec (the text right after 'Row ' up to the closing '**' / '—')."""
    rows = set()
    # First pull out any A-B ranges and expand them, blanking them out as we go.
    def _range(m):
        a, b = int(m.group(1)), int(m.group(2))
        if b >= a and b - a < 500:        # sanity guard
            rows.update(range(a, b + 1))
        return " "
    leftover = RANGE_RE.sub(_range, spec)
    # Any remaining bare numbers are individual rows.
    for m in NUM_RE.finditer(leftover):
        rows.add(int(m.group()))
    return rows

def extract_rows(md_path):
    rows = set()
    with open(md_path, encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s.startswith("### Row"):
                m = re.match(r"### Row\s+(\d+)", s)
                if m:
                    rows.add(int(m.group(1)))
            elif s.startswith("- **Row") or s.startswith("- *(Row"):
                # spec = text between 'Row ' and the closing '**' (or ')')
                m = re.search(r"Row\s+(.*?)(?:\*\*|\)\*|\s+—|\s+-\s)", s)
                spec = m.group(1) if m else s.split("Row", 1)[1]
                rows |= parse_spec(spec)
    return rows

def load_csv(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.reader(f))   # row[0] = header, line N = data[N-1]

def main():
    out_rows = []
    summary = []
    for md, csv_path, fail_md, label in TRACKS:
        passed = extract_rows(md)
        failed = extract_rows(fail_md)
        excluded = passed & failed          # fail takes precedence — never ship a flagged row
        rownums = sorted(passed - failed)
        data = load_csv(csv_path)
        nlines = len(data)
        added = 0
        missing = []
        for n in rownums:
            if n < 2 or n > nlines:
                missing.append(n)
                continue
            rec = data[n - 1]            # line N (1-based) -> index N-1
            if len(rec) < 7:
                missing.append(n)
                continue
            out_rows.append(rec[:7])
            added += 1
        summary.append((label, md, len(passed), len(excluded), added, missing))

    with open(OUT, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        w.writerow(["category_id","country","question","answer","options","difficulty","explanation"])
        w.writerows(out_rows)

    print(f"Wrote {len(out_rows)} ship-ready rows to {OUT}\n")
    for label, md, passed, excluded, added, missing in summary:
        print(f"  {label:8s} {md:28s} passed={passed:6d}  also-failed(excluded)={excluded:3d}  written={added:6d}  missing={len(missing)}")
        if missing:
            print(f"           missing/out-of-range rows: {missing[:20]}{' …' if len(missing)>20 else ''}")

if __name__ == "__main__":
    main()
