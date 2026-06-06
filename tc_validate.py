#!/usr/bin/env python3
"""Validator for Pre-worldcup-clean.csv.

Data model after repair: each row = category_id, country, question, answer,
options(JSON list of 3 distractors), difficulty, explanation.
The four rendered choices = answer + 3 distractors (shuffled at runtime).

Implements only the test cases that are meaningful against this data, with the
requested adjustments:
  * TC-05  -> exactly 3 distractors (not 4 options)
  * TC-11  -> only flag years presented as World Cup *editions*
  * TC-15  -> NEW: every World Cup edition referenced must be in 2006-2026
  * TC-16  -> NEW: no distractor equals the answer (exact OR synonym/near)
"""
import csv, json, re, html, unicodedata, collections, difflib

SRC = "Pre-worldcup-clean.csv"
VALID_DIFF = {"easy", "medium", "hard"}
QWORD = re.compile(r"\b(who|what|when|where|which|how|whom|whose|why)\b", re.I)
LETTERREF = re.compile(r"\b(option|answer|choice)\s+[A-D]\b", re.I)
HTMLENT = re.compile(r"&(?:[a-zA-Z]+|#\d+);")
# a year presented as a World Cup *edition* (not a qualifier played in an off year)
WC_EDITION = re.compile(
    r"\b(\d{4})\s+(?:FIFA\s+)?World Cup\b(?!\s+qualif)|\bWorld Cup\s+(\d{4})\b", re.I)
FILLER = {"fifa", "the", "a", "an"}
# men's editions (every 4 yrs from 1930, minus cancelled 1942/1946)
VALID_WC_MEN = {1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978,
                1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022, 2026}
# women's editions (a "2023 FIFA World Cup" is a real tournament)
VALID_WC_WOMEN = {1991, 1995, 1999, 2003, 2007, 2011, 2015, 2019, 2023}
VALID_WC = VALID_WC_MEN | VALID_WC_WOMEN

# minimal alias groups for synonym detection (TC-16). A full semantic pass would
# use embeddings/an LLM; this catches the common, mechanical equivalences.
ALIASES = [
    {"usa", "united states", "us", "america", "united states of america"},
    {"netherlands", "holland"},
    {"group stage", "group phase", "group round"},
    {"round of 16", "last 16", "knockout round of 16"},
    {"quarterfinal", "quarter-final", "quarter finals", "quarterfinals", "last 8"},
    {"semifinal", "semi-final", "semi finals", "semifinals"},
    {"south korea", "korea republic", "republic of korea"},
]

def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s).lower().strip()
    s = re.sub(r"\s+", " ", s)
    return s

def norm_key(s: str) -> str:
    return re.sub(r"[^a-z0-9 ]", "", norm(s)).strip()

def tokens(s: str):
    return set(re.findall(r"[a-z0-9]+", norm(s)))

def core_key(s: str) -> str:
    """Normalised key with filler words removed, so '2018 World Cup' ==
    '2018 FIFA World Cup'. Crucially this keeps distinguishing tokens (years,
    numbers, names) so distractors that differ by the key fact are NOT matched."""
    return " ".join(w for w in norm_key(s).split() if w not in FILLER)

def synonym(a: str, b: str) -> bool:
    """High-precision 'same meaning' test: exact (after normalising punctuation/
    case/filler) or a known alias group. Deliberately does NOT use fuzzy string
    similarity, because plausible distractors are *meant* to look similar while
    differing in the key fact (e.g. 2022 vs 2026 World Cup). True paraphrase
    synonyms beyond these rules need a semantic/LLM pass (see TC-06/TC-14)."""
    ka, kb = norm_key(a), norm_key(b)
    if not ka or not kb:
        return False
    if core_key(a) == core_key(b):
        return True
    for grp in ALIASES:
        if ka in grp and kb in grp:
            return True
    return False

def main():
    rows = []
    with open(SRC, newline="", encoding="utf-8") as f:
        r = csv.reader(f); next(r)
        for row in r:
            rows.append(row)
    n = len(rows)
    flags = collections.defaultdict(list)
    cat_ids = collections.Counter()

    for i, row in enumerate(rows, start=2):
        cat, country, q, ans, opts_raw, diff, expl = row
        opts = json.loads(opts_raw)
        choices = [ans] + opts
        cat_ids[cat] += 1

        # TC-04 coherence
        if not q.strip() or len(q.strip()) < 10 or not QWORD.search(q):
            flags["TC-04 coherence"].append((i, q[:60]))
        # TC-05 incomplete options (exactly 3 distractors, none blank, no dup distractor)
        if len(opts) != 3 or any(not o.strip() for o in opts) or \
           len({norm_key(o) for o in opts}) != len(opts):
            flags["TC-05 options"].append((i, opts))
        # TC-08 difficulty
        if diff.strip().lower() not in VALID_DIFF:
            flags["TC-08 difficulty"].append((i, repr(diff)))
        # TC-09 category (country)
        if not country.strip():
            flags["TC-09 category"].append((i, q[:40]))
        # TC-10 encoding / whitespace
        enc = []
        for name, val in (("question", q), ("answer", ans), ("difficulty", diff),
                          ("explanation", expl)):
            if val != val.strip():
                enc.append(f"ws:{name}")
            if HTMLENT.search(val):
                enc.append(f"html:{name}")
            if any(ord(c) < 0x20 for c in val):
                enc.append(f"ctrl:{name}")
        if enc:
            flags["TC-10 encoding"].append((i, enc))
        # TC-11 numeric plausibility (World Cup editions only)
        # TC-15 timespan (editions must be 2006-2026)
        # scope = question + correct answer (distractors are intentionally wrong)
        blob = f"{q} {ans}"
        for m in WC_EDITION.finditer(blob):
            y = int(m.group(1) or m.group(2))
            if y not in VALID_WC:
                flags["TC-11 impossible-edition"].append((i, y, q[:50]))
            elif y < 2006 or y > 2026:
                flags["TC-15 out-of-span"].append((i, y, q[:50]))
        # TC-13 letter reference
        if LETTERREF.search(q):
            flags["TC-13 letter-ref"].append((i, q[:60]))
        # TC-16 distractor equals answer (exact or synonym)
        hits = [o for o in opts if synonym(ans, o)]
        if hits:
            flags["TC-16 distractor=answer"].append((i, ans, hits))

    # TC-01 duplicates: exact (normalized, global) + near-dup within (country, answer)
    exact = collections.defaultdict(list)
    for i, row in enumerate(rows, start=2):
        exact[norm_key(row[2])].append(i)
    exact_dups = sum(len(v) - 1 for v in exact.values() if len(v) > 1)

    near_pairs = 0
    near_qids = set()
    buckets = collections.defaultdict(list)
    for i, row in enumerate(rows, start=2):
        buckets[(row[1], norm_key(row[3]))].append((i, row[2]))
    for key, items in buckets.items():
        if len(items) < 2:
            continue
        toks = [(qid, tokens(qt)) for qid, qt in items]
        inv = collections.defaultdict(list)
        for idx, (qid, ts) in enumerate(toks):
            for t in ts:
                inv[t].append(idx)
        seen_pairs = set()
        for idx, (qid, ts) in enumerate(toks):
            cand = {j for t in ts for j in inv[t] if j > idx}
            for j in cand:
                pair = (idx, j)
                if pair in seen_pairs:
                    continue
                seen_pairs.add(pair)
                tj = toks[j][1]
                jac = len(ts & tj) / len(ts | tj) if (ts | tj) else 0
                if jac >= 0.85:
                    near_pairs += 1
                    near_qids.add(toks[idx][0]); near_qids.add(toks[j][0])

    # ---- report ----
    print(f"rows validated: {n}")
    print(f"category_id values (note: constant): {dict(cat_ids)}")
    print()
    print("=== AUTOMATED TEST RESULTS ===")
    print(f"TC-01 duplicates          : {exact_dups} exact, "
          f"{near_pairs} near-dup pairs (>=0.85) across {len(near_qids)} questions")
    order = ["TC-04 coherence", "TC-05 options", "TC-08 difficulty",
             "TC-09 category", "TC-10 encoding", "TC-11 impossible-edition",
             "TC-15 out-of-span", "TC-13 letter-ref", "TC-16 distractor=answer"]
    for k in order:
        v = flags.get(k, [])
        print(f"{k:26}: {len(v)} flagged")
    print()
    print("=== SAMPLES ===")
    for k in order:
        v = flags.get(k, [])
        if v:
            print(f"\n-- {k} (showing up to 3) --")
            for ex in v[:3]:
                print("   ", ex)

if __name__ == "__main__":
    main()
