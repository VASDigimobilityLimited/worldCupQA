# QA — Failed LIVENESS but Passed OTHERS

Rows that **passed the mechanical/heuristic checks** (they appear in `QA_PASSED.md`) but
**failed the live, web-sourced TC-06 factual check** — i.e. they look clean structurally
yet contain a wrong answer, a wrong explanation, a false premise, a non-unique answer, or
an unverifiable claim.

These are the **most dangerous** rows: they would otherwise ship as "passed." Each entry
lists the reason, a source URL, and a concrete remedy. `UNVERIFIED → FAIL` is used
conservatively when a claim can't be confirmed from reliable sources.

**Scope of this file:** rows **231 onward** (liveness is only run on rows already in
`QA_PASSED.md`). Rows 2–230 were verified under the earlier method (`QA_TC06_FAILED.md`).

Cursor lives in `QA_TC06_LIVE.md`.

Total failed-liveness-passed-others so far: **0** (resume at row 231)

---
