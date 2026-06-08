import csv, re, sys, json

# Build row -> (country, q, answer, options, difficulty, explanation) from dataset
rows = {}
with open('QA_CLEANED_dataset.csv', newline='', encoding='utf-8') as f:
    r = csv.reader(f)
    header = next(f)  # skip but keep line numbering: line 2 = first data row
    # csv.reader consumed header via next(f)? careful: mixing. redo properly.
with open('QA_CLEANED_dataset.csv', newline='', encoding='utf-8') as f:
    r = csv.reader(f)
    for i, rec in enumerate(r, start=1):
        if i == 1:
            continue
        if len(rec) < 7:
            continue
        cat, country, q, ans, opts, diff, expl = rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6]
        try:
            distractors = json.loads(opts)
        except Exception:
            distractors = [opts]
        rows[i] = dict(country=country, q=q, ans=ans, distractors=distractors, diff=diff, expl=expl)

# Parse pool to get the set of rows in scope (and confirm Q/Answer/Options)
pool = set()
with open('QA_PASSED_cleaned.md', encoding='utf-8') as f:
    for line in f:
        m = re.match(r'^### Row (\d+) — (.+) \((.*)\)', line)
        if m:
            pool.add(int(m.group(1)))

target = sys.argv[1] if len(sys.argv) > 1 else None
out = []
for n in sorted(pool):
    if n not in rows:
        continue
    rec = rows[n]
    if target and rec['country'].lower() != target.lower():
        continue
    out.append((n, rec))

for n, rec in out:
    choices = [rec['ans']] + rec['distractors']
    print(f"### Row {n} — {rec['country']} ({rec['diff']})")
    print(f"Q: {rec['q']}")
    print(f"ANSWER: {rec['ans']}")
    print(f"OPTIONS: {' | '.join(choices)}")
    print(f"EXPL: {rec['expl']}")
    print()
print(f"--- {len(out)} rows for {target or 'ALL'} ---")
