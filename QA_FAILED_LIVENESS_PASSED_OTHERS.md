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

Total failed-liveness-passed-others so far: **2287** (Algeria 176 · Argentina 110 [✅ COMPLETE] · Australia 121 [✅ COMPLETE] · Austria 135 [✅ COMPLETE] · Belgium 192 [✅ COMPLETE] · Brazil 6097–6760 so far: 73 · Cabo Verde 73 [✅ COMPLETE] · Canada 41 [✅ COMPLETE] · Chile 191 [✅ COMPLETE] · Costa Rica 80 [✅ COMPLETE] · Côte d'Ivoire 79 [✅ COMPLETE] · Croatia 154 [✅ COMPLETE] · Denmark 182 [✅ COMPLETE] · DR Congo 127 [✅ COMPLETE] · Egypt 104 [✅ COMPLETE] · England 87 [✅ COMPLETE] · Germany 65 [✅ COMPLETE] · Ghana 72 [✅ COMPLETE] · Italy 225 [✅ COMPLETE])

---

## Rows 231–275 (Algeria)

### Row 242 — Algeria (medium) — FAIL: wrong explanation (mislabeled play-off)
**Q:** In which World Cup year did Algeria qualify via a playoff against Egypt?
**Answer:** 2010
**Why it fails:** The answer year (2010) is correct, but the explanation calls it an
"intercontinental playoff." It was a **CAF play-off vs Egypt** (1-0, Khartoum, 18 Nov 2009) —
intra-confederation, not intercontinental. Recurring dataset error (defect pattern #2).
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round
**Remedy:** Replace "intercontinental playoff" with "CAF play-off against Egypt."

### Row 243 — Algeria (medium) — FAIL: wrong explanation (goal count)
**Q:** In which World Cup year did Algeria's Islam Slimani become their all-time top scorer?
**Answer:** 2022
**Why it fails:** Explanation says Slimani "scored his record-breaking 41st goal." He broke
the record by passing **Abdelhafid Tasfaout's 36** on **8 Oct 2021**, so the record-breaker
was his **37th** goal, not his 41st. (He passed the mark in the 2022 WC-qualifying cycle, so
the year answer is defensible, but the explanation's count is wrong.)
**Source:** https://en.wikipedia.org/wiki/Islam_Slimani
**Remedy:** Change "record-breaking 41st goal" to "record-breaking 37th goal (passing Tasfaout's 36, on 8 Oct 2021)."

### Row 244 — Algeria (medium) — FAIL: wrong answer
**Q:** In which World Cup year did Riyad Mahrez debut for Algeria after his 2016 Premier League win?
**Answer:** 2018
**Why it fails:** Mahrez's **only** World Cup, and his World Cup debut, was **2014** — before
his 2016 Premier League title, not after. Algeria failed to qualify for 2018, so the answer
2018 is impossible. The question's "after his 2016 PL win" premise is also contradictory.
**Source:** https://en.wikipedia.org/wiki/Riyad_Mahrez
**Remedy:** This question is unsalvageable as posed (Mahrez's WC debut predates the 2016 title);
drop it or rewrite without the "after 2016" framing, with answer 2014.

### Row 245 — Algeria (medium) — FAIL: wrong explanation (mislabeled play-off)
**Q:** In which year did Algeria beat Egypt in a World Cup playoff?
**Answer:** 2009
**Why it fails:** Answer year correct (18 Nov 2009), but the explanation again calls it an
"intercontinental playoff." It was a **CAF play-off** (Algeria 1-0 Egypt, Khartoum). Same
recurring error as row 242.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round
**Remedy:** Replace "intercontinental playoff" with "CAF play-off."

### Row 246 — Algeria (medium) — FAIL: wrong answer
**Q:** In which year did Algeria qualify for the 2026 World Cup?
**Answer:** 2026
**Why it fails:** Algeria **sealed 2026 qualification on 9 Oct 2025** (3-0 v Somalia, Oran;
Amoura 2, Mahrez). The year they qualified is **2025**, not 2026 — and 2025 is not even among
the four choices (2026/2022/2018/2014), so no option is correct.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Change the answer to **2025** and add it as a choice (replace a distractor).

### Row 247 — Algeria (medium) — FAIL: false/unverifiable premise
**Q:** In which year did Algeria qualify for the World Cup with players from Ligue 1 clubs like MC Alger?
**Answer:** 2014
**Why it fails:** The 2014 squad was **overwhelmingly Europe-based**; the claim that "many
players developed in the domestic Ligue 1" at clubs "like MC Alger" is false/unsupported (only
a couple of reserve goalkeepers were domestic). The "MC Alger" hook is unverifiable, and 2010
was also a year Algeria qualified, making the year non-unique without the dubious clause.
**Source:** https://en.wikipedia.org/wiki/Algeria_at_the_2014_FIFA_World_Cup
**Remedy:** Drop the false "domestic Ligue 1 / MC Alger" framing; the 2014 squad was Europe-based.

### Row 275 — Algeria (easy) — FAIL: wrong explanation + misleading premise
**Q:** Unlike their 2010 playoff, how did Algeria qualify for the 2014 World Cup?
**Answer:** Through CAF qualification
**Why it fails:** Explanation says Algeria "qualified **directly** through the CAF qualification
process" — but 2014 qualification came via a **two-legged CAF play-off vs Burkina Faso** (1-0
Blida, through on away goals after 3-3 agg), i.e. not directly. The question's framing also
implies the 2010 play-off was *not* CAF, reinforcing the "intercontinental" myth; the 2010
play-off vs Egypt was **also** a CAF play-off.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round
**Remedy:** Reword: 2014 was a CAF play-off vs Burkina Faso (not "directly"); note 2010 was
also a CAF play-off (vs Egypt), not intercontinental.

---

## Rows 276–320 (Algeria)

### Row 314 — Algeria (medium) — FAIL: corrupted answer (date auto-conversion)
**Q:** What was the score when Algeria lost to Germany in the 2014 World Cup round of 16?
**Answer:** 02-Jan
**Why it fails:** The answer cell is **`02-Jan`** — a spreadsheet date-corruption of the
scoreline **"2-1"** (Excel read `2-1` as 2 January). The rendered correct choice is unreadable
garbage, so the question has no valid answer even though the explanation correctly states 2-1.
Classic "looks clean but ships broken" row.
**Source:** https://en.wikipedia.org/wiki/Algeria_at_the_2014_FIFA_World_Cup
**Remedy:** Restore the answer to **"2-1"** (and audit the dataset for other `DD-Mon`
date-mangled scorelines).

---

## Rows 321–385 (Algeria)

### Row 336 — Algeria (medium) — FAIL: wrong qualification year
**Q:** When did Algeria qualify for the 2014 FIFA World Cup through CAF?
**Answer:** 2014
**Why it fails:** Algeria **completed** 2014 qualification via the two-legged CAF play-off vs
Burkina Faso in **November 2013** (1-0 in Blida, 19 Nov 2013, through on away goals). The
dataset's own row 337 correctly answers **2013**, so "2014" is internally inconsistent and
factually the wrong year; 2013 is not among the choices.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round
**Remedy:** Change answer to **2013** (and add it as a choice), or reword to "for which World Cup."

### Row 338 — Algeria (medium) — FAIL: wrong qualification year
**Q:** When did Algeria qualify for the 2014 World Cup via CAF?
**Answer:** 2014
**Why it fails:** Same as row 336 — qualification was sealed in **November 2013**, not 2014.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round
**Remedy:** Change answer to **2013**, or reword to "for which World Cup."

### Row 339 — Algeria (medium) — FAIL: wrong qualification year
**Q:** When did Algeria qualify for the 2026 FIFA World Cup?
**Answer:** 2026
**Why it fails:** Algeria **sealed 2026 qualification on 9 Oct 2025** (3-0 v Somalia, Oran).
The year was **2025**, not 2026 (same defect as row 246); 2025 is not among the choices.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Change answer to **2025** (and add it as a choice), or reword to "for which World Cup."

### Row 358 — Algeria (hard) — FAIL: wrong timing
**Q:** When did Algeria's Islam Slimani break his team's all-time scoring record?
**Answer:** Before the 2022 qualifiers
**Why it fails:** Slimani passed Tasfaout's record on **8 Oct 2021** — in Algeria's **6-1 win
over Niger, which was itself a 2022 FIFA World Cup qualifier**. So he broke the record **during**
the 2022 qualifiers, not before them. The explanation ("prior to the 2022 ... qualifiers") is
likewise wrong.
**Source:** https://en.wikipedia.org/wiki/Islam_Slimani
**Remedy:** Change to "**During** the 2022 qualifiers" (8 Oct 2021, v Niger).

### Row 363 — Algeria (medium) — FAIL: wrong qualification year
**Q:** When did Algeria's national team qualify for the 2026 FIFA World Cup?
**Answer:** 2026
**Why it fails:** Qualification was sealed in **October 2025**, not 2026 (duplicate of the
row 246/339 defect).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Change answer to **2025**, or reword to "for which World Cup."

### Row 365 — Algeria (hard) — FAIL: unverifiable "squad rebuild" claim
**Q:** When did Algeria's post-2019 AFCON rebuild start affecting FIFA World Cup squad selections?
**Answer:** 2022 World Cup qualifiers
**Why it fails:** The "post-2019 squad rebuild" is a soft narrative with no authoritative source
pinning when it "started affecting" selections. UNVERIFIED → FAIL (conservative; same basis as
the earlier squad-rebuild fails, old-method rows 5/6).
**Source:** none located (narrative claim).
**Remedy:** Drop, or replace with a crisp sourced fact.

### Row 367 — Algeria (medium) — FAIL: unverifiable "squad rebuild" claim
**Q:** When did Algeria's squad rebuild begin after their AFCON win?
**Answer:** After 2019 AFCON
**Why it fails:** "Squad rebuild" start date is an unsourced narrative claim (UNVERIFIED → FAIL).
**Source:** none located.
**Remedy:** Drop, or anchor to a verifiable event.

### Row 369 — Algeria (medium) — FAIL: unverifiable "squad rebuild" claim
**Q:** When did Algeria's World Cup squad rebuild begin after their AFCON win?
**Answer:** After 2019
**Why it fails:** Same unsourced "squad rebuild" narrative as rows 365/367 (UNVERIFIED → FAIL).
**Source:** none located.
**Remedy:** Drop, or anchor to a verifiable event.

---

## Rows 386–460 (Algeria)

> This range is dominated by a generated **"Which Algeria attacker…"** template that produced
> many flawed near-variants. Grouped by defect below. Shared source for the squad/2022 facts:
> https://en.wikipedia.org/wiki/Algeria_national_football_team (Algeria **failed to qualify**
> for the 2022 World Cup — lost the CAF play-off to Cameroon).

### Rows 430, 434, 441, 442, 447 — FAIL: false premise (Algeria was NOT at the 2022 World Cup)
- **430:** "Which Algeria attacker from Manchester City **played at the 2022 World Cup**? → Mahrez"
- **434:** "Which Algeria attacker **played at the 2022 FIFA World Cup**? → Benrahma"
- **441:** "Which Algeria attacker was in the **2022 World Cup squad** …? → Bounedjah"
- **442:** "Which Algeria attacker was in their **2022 FIFA World Cup squad**? → Benrahma"
- **447:** "Which Algeria attacker … played at the **2014 and 2022 World Cups**? → Mahrez"
**Why they fail:** Algeria did **not** qualify for the 2022 World Cup, so no Algerian played at
it and there was no 2022 World Cup squad. Every one of these asserts an event that didn't happen.
**Remedy:** Re-anchor to the **2022 World Cup *qualifying* campaign** (which did happen), or to
the 2014 World Cup.

### Rows 433, 438, 439, 440, 443 — FAIL: non-unique answer ("key modern attacker" = Benrahma)
All ask which Algeria attacker is "a key player for the modern era" / "a key figure in 2022 WC
qualifying," with **Benrahma** keyed as the answer and **Mahrez / Slimani / Bounedjah** as
distractors. Mahrez (captain, 2019 AFCON best-XI, talisman) fits the description **at least as
well as Benrahma**, so the answer is not unique. (Explanations are also circular: "Benrahma is
described as a key attacker…".)
**Source:** https://en.wikipedia.org/wiki/Riyad_Mahrez
**Remedy:** Make the discriminator unique (e.g. a club, a cap/goal figure, a specific match), or drop.

### Rows 435, 436 — FAIL: non-unique answer (caps/goals description)
- **435:** "attacker with **over 90 caps and 25+ goals** → Mahrez" (distractor **Slimani** also has 90+ caps and 40+ goals)
- **436:** "attacker who **scored over 25 international goals by 2022** → Mahrez" (Slimani had 40+ by 2022)
**Why they fail:** Islam Slimani — a listed distractor and Algeria's all-time top scorer — also
satisfies the description, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Islam_Slimani
**Remedy:** Add a unique discriminator (row 446's "Manchester City" works); otherwise drop.

### Row 428 — FAIL: non-unique answer
**Q:** Which Algeria 2026 qualifier starter was also a 2019 AFCON final starter? **A:** Mahrez
**Why it fails:** Other 2019 AFCON-final starters (e.g. **Ismaël Bennacer**, **Youcef Belaïli**)
also featured as starters in 2026 qualifying, so Mahrez is not the unique answer. (Soft squad-
composition claim — UNVERIFIED for uniqueness → FAIL.)
**Source:** https://en.wikipedia.org/wiki/2019_Africa_Cup_of_Nations_Final
**Remedy:** Drop or rebuild with a uniquely-identifying clue.

### Row 448 — FAIL: non-unique / incoherent answer
**Q:** Which Algeria attacker's team topped their 2022 WC qualification group? **A:** Mahrez
**Why it fails:** All four options (Mahrez, Slimani, Bounedjah, Feghouli) are **Algeria** players,
so "their team" topped the group for every choice — the question can't single one out.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Drop; the construction is logically non-discriminating.

### Row 396 — FAIL: non-unique answer + wrong explanation
**Q:** Which 2014 World Cup knockout team did Algeria NOT face? **A:** Costa Rica
**Why it fails:** The distractor **France** is **also** a team Algeria did not face (Algeria's group
was Belgium, South Korea, Russia; R16 was Germany), so two options are correct → non-unique. The
explanation ("faced Belgium **and France** in the group stage") is also false — Algeria never
played France in 2014.
**Source:** https://en.wikipedia.org/wiki/Algeria_at_the_2014_FIFA_World_Cup
**Remedy:** Replace distractors so only one option is a team Algeria avoided; fix the explanation.

### Row 417 — FAIL: wrong answer
**Q:** Which AFCON-winning nation did Algeria's 2014 World Cup coach NOT manage? **A:** Ivory Coast
**Why it fails:** Vahid Halilhodžić **did** manage Ivory Coast (2008–2010) — the explanation even
says so — so "Ivory Coast" is the one he *did* manage, making it the wrong answer. Nigeria, Egypt
and Cameroon (the distractors) are all nations he did **not** manage, so three options are valid.
**Source:** https://en.wikipedia.org/wiki/Vahid_Halilhod%C5%BEi%C4%87
**Remedy:** Question is broken; drop or fully rebuild.

### Row 423 — FAIL: self-referential / incoherent answer
**Q:** Which African nation matched Algeria's 2019 AFCON title count? **A:** Algeria
**Why it fails:** The answer is the subject nation itself ("Algeria matched Algeria") — incoherent,
same defect as old-method row 10. (Also, none of the distractors Egypt/Nigeria/Cameroon has exactly
two AFCON titles anyway.)
**Source:** https://en.wikipedia.org/wiki/Africa_Cup_of_Nations
**Remedy:** Drop — the answer restates the subject.

---

## Rows 461–540 (Algeria)

### Row 462 — Algeria (easy) — FAIL: unverified / likely-false debut claim
**Q:** Which Algeria defender debuted at the 2021 Africa Cup of Nations? **A:** Ilyes Chetti
**Why it fails:** Chetti's senior breakthrough came at the **FIFA Arab Cup (Dec 2021)**, which
**preceded** the 2021 AFCON (played Jan 2022) — so "debuted at the 2021 AFCON" is not supported
and is likely wrong. Obscure squad-composition claim → UNVERIFIED → FAIL.
**Source:** https://en.wikipedia.org/wiki/Ilyes_Chetti
**Remedy:** Verify and restate his actual debut competition/date, or drop.

### Row 507 — Algeria (easy) — FAIL: false premise
**Q:** Which Algeria manager's AFCON win was later: Vahid Halilhodžić's or Djamel Belmadi's? **A:** Belmadi
**Why it fails:** The question presupposes **Halilhodžić won an AFCON** — he never did (with Algeria
or anyone). Only Belmadi (2019) has an AFCON title, so the comparison is built on a non-event.
**Source:** https://en.wikipedia.org/wiki/Vahid_Halilhod%C5%BEi%C4%87
**Remedy:** Drop the false comparison; Halilhodžić has no AFCON title.

### Row 508 — Algeria (easy) — FAIL: wrong timing (false premise)
**Q:** Which Algeria player became his nation's all-time top scorer during the 2019 AFCON? **A:** Slimani
**Why it fails:** Slimani is the right player, but he passed Tasfaout's record on **8 Oct 2021**
(a 2022 WC qualifier v Niger) — **not** "during the 2019 AFCON." The question's timing is false.
**Source:** https://en.wikipedia.org/wiki/Islam_Slimani
**Remedy:** Change "during the 2019 AFCON" to "during 2022 World Cup qualifying (Oct 2021)."

### Row 512 — Algeria (easy) — FAIL: false premise + non-Algerian distractors
**Q:** Which Algeria player emerged after the 2019 AFCON squad rebuild? **A:** Ismaël Bennacer
**Why it fails:** Bennacer was the **breakout star of the 2019 AFCON itself** (named in the team
of the tournament) — he did not "emerge after." The premise is false, the "squad rebuild" is an
unsourced narrative, and the distractors (Pépé, Ziyech, Zaha) aren't even Algerian.
**Source:** https://en.wikipedia.org/wiki/2019_Africa_Cup_of_Nations_Final
**Remedy:** Drop; re-anchor to a genuine post-2019 debutant with valid distractors.

### Row 513 — Algeria (medium) — FAIL: false (Djabou did not force extra time)
**Q:** Which Algeria player equalized to force extra time against Germany in 2014? **A:** Djabou
**Why it fails:** The 2014 R16 was **0-0 after 90 minutes** and went to extra time goalless;
Germany then scored (Schürrle 92', Özil 120') and Djabou's goal came at **120'+1'**, making it
**2-1** — a late consolation, **not** a stoppage-time equalizer to "make it 2-2 / force ET."
Recurring Djabou error (cf. old-method rows 133, 190).
**Source:** https://en.wikipedia.org/wiki/Algeria_at_the_2014_FIFA_World_Cup
**Remedy:** Rewrite: no one forced ET (0-0 at 90'); Djabou scored Algeria's only goal at 120'+1'.

### Row 515 — Algeria (easy) — FAIL: non-unique answer
**Q:** Which Algeria player from their 2019 AFCON triumph also played in the 2022 WC qualifiers? **A:** Mahrez
**Why it fails:** Distractors **Ismaël Bennacer** and **Youcef Belaïli** were also 2019 AFCON
winners who featured in 2022 WC qualifying — so several options are valid, not just Mahrez.
**Source:** https://en.wikipedia.org/wiki/2019_Africa_Cup_of_Nations_Final
**Remedy:** Add a unique discriminator, or drop.

### Row 527 — Algeria (easy) — FAIL: wrong (no such retirement)
**Q:** Which Algeria player retired after the 2019 AFCON triumph? **A:** Adlène Guedioura
**Why it fails:** Guedioura did **not** retire after 2019 — his final cap was **25 March 2022**
(the 1-0 CAF play-off second leg v Cameroon), ending an 11-year international career.
**Source:** https://en.wikipedia.org/wiki/Adl%C3%A8ne_Guedioura
**Remedy:** Correct to 2022, or drop the "retired after 2019" framing.

### Row 540 — Algeria (medium) — FAIL: non-unique / unsupported answer
**Q:** Which Algeria player scored in the 2023 AFCON before their 2026 qualification? **A:** Mahrez
**Why it fails:** **Baghdad Bounedjah** — a listed distractor — scored for Algeria at the 2023
AFCON (a brace v Burkina Faso, including a 90'+5' equalizer), so the answer is non-unique; Mahrez
scoring there is not clearly supported.
**Source:** https://en.wikipedia.org/wiki/Algeria_national_football_team
**Remedy:** Make the scorer unique (Bounedjah is the safer key fact), or drop.

---

## Rows 541–620 (Algeria)

### Rows 558, 565 — FAIL: false "Djabou equalizer" (no such goal)
- **558:** "Djabou scored the **88th-minute equalizer** vs Germany in 2014 … to level at 2-2 and force extra time"
- **565:** "Djabou scored the **late equalizer** … in the 91st minute to make it 2-2 before Germany won in ET"
**Why they fail:** The 2014 R16 was **0-0 after 90 minutes** and went to extra time goalless;
Germany scored (Schürrle 92', Özil 120') and Djabou's goal came at **120'+1'**, making it **2-1**.
There was no 88th/91st-minute equalizer and the score was never 2-2. Recurring Djabou error.
**Source:** https://en.wikipedia.org/wiki/Algeria_at_the_2014_FIFA_World_Cup
**Remedy:** Remove the "equalizer/2-2/forced ET" framing; Djabou scored a 120'+1' consolation (2-1).

### Row 547 — FAIL: wrong scorer
**Q:** Which Algeria player scored in their 2014 World Cup round of 16 defeat? **A:** Islam Slimani
**Why it fails:** Algeria's only goal in the 2-1 R16 loss to Germany was scored by **Abdelmoumene
Djabou** (120'+1'), **not Slimani**. The explanation repeats the error.
**Source:** https://en.wikipedia.org/wiki/Algeria_at_the_2014_FIFA_World_Cup
**Remedy:** Change the answer to **Djabou**.

### Row 561 — FAIL: wrong scorer
**Q:** Which Algeria player scored the decisive goal in their 2014 World Cup qualifier? **A:** Slimani
**Why it fails:** The goal that sealed 2014 qualification — **Algeria 1-0 Burkina Faso in Blida**
(through on away goals after 3-3 agg) — was scored by **Madjid Bougherra**, not Slimani.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round
**Remedy:** Change the answer to **Bougherra**.

### Row 574 — FAIL: false premise (Algeria did NOT qualify for 2022)
**Q:** Which Algeria player scored their qualifying winner against Cameroon for Qatar 2022? **A:** Slimani
**Why it fails:** Algeria **lost** the 2022 CAF play-off to **Cameroon** (agg 2-2, out on away
goals) — there was no "qualifying winner against Cameroon" and Algeria did not reach Qatar 2022.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Drop — the event never happened.

### Rows 545, 577 — FAIL: non-unique answer (2014 squad)
- **545:** "Which Algeria player **scored in their 2014 World Cup group stage** match? → Slimani"
  (distractors **Feghouli** and **Brahimi** also scored in the 2014 group stage)
- **577:** "Which Algeria player **started** their 2014 World Cup match against Germany? → Bougherra"
  (distractors **Feghouli** and **Slimani** also started the R16)
**Why they fail:** Multiple listed options satisfy the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Algeria_at_the_2014_FIFA_World_Cup
**Remedy:** Add a unique discriminator, or replace the over-broad distractors.

### Row 589 — FAIL: false timing
**Q:** Which Algeria player was their all-time top scorer **at the 2014 World Cup**? **A:** Slimani
**Why it fails:** Slimani only became Algeria's all-time top scorer on **8 Oct 2021**; at the 2014
World Cup the record-holder was still **Abdelhafid Tasfaout**. The phrasing pins the record to 2014.
**Source:** https://en.wikipedia.org/wiki/Islam_Slimani
**Remedy:** Drop "at the 2014 World Cup," or reword to "who is now their all-time top scorer."

### Row 599 — FAIL: false premise
**Q:** Which Algeria player, their all-time top scorer, faced Tunisia in 2018 World Cup qualifying? **A:** Slimani
**Why it fails:** Algeria's 2018 WC qualifying third-round group was **Nigeria, Cameroon, Zambia** —
**not Tunisia** (who were in a different group). Algeria did not face Tunisia in 2018 qualifying.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Replace Tunisia with an actual 2018 opponent, or drop.

### Row 610 — FAIL: false (retirement date off by ~17 years)
**Q:** Which Algeria player's international retirement preceded their 2010 World Cup group stage exit? **A:** Rabah Madjer
**Why it fails:** Rabah Madjer (1987 European Cup backheel fame) ended his international career in the
early **1990s**, not "2009." All the distractors (Bencheikh, Belloumi, Zidane) are likewise 1980s-era
players — the whole premise of a "2009 retirement before 2010" is false.
**Source:** https://en.wikipedia.org/wiki/Rabah_Madjer
**Remedy:** Drop — the question is built on a fabricated retirement date.

### Row 611 — FAIL: wrong answer
**Q:** Which Algeria players were not part of their 2019 AFCON winning squad? **A:** Youcef Atal
**Why it fails:** **Youcef Atal was in the 2019 AFCON-winning squad** (starting right-back until
injured mid-tournament). The explanation's "Atal broke into the team after 2019" is false.
**Source:** https://en.wikipedia.org/wiki/2019_Africa_Cup_of_Nations_Final
**Remedy:** Pick a genuine non-2019 player (e.g. Aouar, as in row 587); Atal was in the squad.

### Row 620 — FAIL: false premise
**Q:** Which Algeria star attacker scored twice in 2014 World Cup qualifiers? **A:** Riyad Mahrez
**Why it fails:** Mahrez **debuted for Algeria in 2014, after** qualification had already been
secured (Nov 2013) — he played **no** matches in the 2014 qualifying campaign, so he could not have
scored in it.
**Source:** https://en.wikipedia.org/wiki/Riyad_Mahrez
**Remedy:** The intended scorer is likely Slimani; fix the answer or drop.

### Rows 613, 615, 617, 618 — FAIL: unverifiable "squad rebuild / squad age" narrative
- **613:** "Which Algeria squad **era followed** their 2019 AFCON triumph? → A rebuild phase"
- **615:** "Which Algeria squad was **older**, the 2019 winners or the 2026 qualifiers? → 2019 winners"
- **617:** "Which Algeria squad was **younger**, the 2019 winners or the 2022 qualifiers? → 2022 qualifiers"
- **618:** "Which Algeria squad's **rebuild** was evident at the 2022 qualifiers? → Post-2019 AFCON squad"
**Why they fail:** All rest on the unsourced "post-2019 squad rebuild" narrative and on squad-age
comparisons with no authoritative data; 618's explanation is also self-referential ("The reference
fact states…"). UNVERIFIED → FAIL (consistent with the earlier squad-rebuild fails).
**Source:** none located (narrative/editorial claims).
**Remedy:** Replace with crisp, sourceable facts (specific debutants, named ages), or drop.

---

## Rows 621–710 (Algeria)

> A heavily-flawed stretch: fabricated Algerian club histories, the "Benrahma = key modern
> attacker" template, "2022 World Cup squad" false premises (Algeria did **not** qualify for
> 2022), and non-unique club/caps/scorer questions. 41 fails — grouped by defect.

### Rows 704, 705, 706, 707, 693 — FAIL: fabricated Algerian club histories
- **704, 705:** "Which Algerian Ligue 1 club did **Riyad Mahrez** play for before 2014? → USM Alger"
- **706, 707:** "Which Algerian Ligue 1 club did **Yacine Brahimi** play for before 2014? → USM Alger"
- **693:** "Which Algerian club's player scored vs Russia in 2014? → USM Alger (Slimani 'played for USM Alger')"
**Why they fail:** **Mahrez** (Sarcelles→Quimper→Le Havre→Leicester) and **Brahimi** (Rennes
academy→Clermont→Granada→Porto) came up entirely through **French** football and **never played
for any Algerian club**. **Slimani**'s Algerian club was **CR Belouizdad**, and by the 2014 World
Cup he was at **Sporting CP** — not USM Alger. All five answers are invented.
**Source:** https://en.wikipedia.org/wiki/Riyad_Mahrez , https://en.wikipedia.org/wiki/Yacine_Brahimi , https://en.wikipedia.org/wiki/Islam_Slimani
**Remedy:** Drop — none of these players played for USM Alger.

### Rows 644, 645, 646, 647, 648, 663, 666, 670, 672, 674, 701 — FAIL: non-unique "key modern attacker = Benrahma"
All key Benrahma as "the key modern attacker" / "key figure in 2022 WC qualifying" with
**Mahrez / Slimani / Bounedjah** as distractors. Mahrez (captain, talisman) fits the description
at least as well, so the answer is not unique; explanations are circular ("Benrahma is described as…").
**Source:** https://en.wikipedia.org/wiki/Riyad_Mahrez
**Remedy:** Add a unique discriminator (club, caps, a specific match/goal), or drop.

### Rows 628, 636, 637, 658, 664, 680, 684 — FAIL: "2022 World Cup squad/finals" false premise
Each asserts an Algerian was **in the 2022 World Cup squad / played or scored at the 2022 World
Cup** (628 Bounedjah, 636 Slimani "for the 2022 WC squad", 637 Benrahma "debuted for the 2022 WC
squad", 658 "scored in both the 2014 and 2022 WCs", 664/684 Benrahma "in the 2022 WC squad",
680 "started at the 2022 WC"). Algeria **failed to qualify for 2022** — none of this happened.
(658 is doubly wrong: Mahrez scored in neither 2014 nor 2022.)
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Re-anchor to the 2022 *qualifying* campaign or to 2014/2026.

### Rows 639, 642, 702 — FAIL: non-unique "over 90 caps"
"Over 90 caps" alone (639, 642 "before 2022 WC", 702 "by the 2022 WC") → keyed to Mahrez, but
**Slimani** (≈98 caps) also has 90+ caps, so the descriptor doesn't single Mahrez out.
**Source:** https://en.wikipedia.org/wiki/Islam_Slimani
**Remedy:** Add a unique discriminator (Man City works, as in rows 641/682), or drop.

### Rows 626, 659, 660, 661 — FAIL: non-unique answer
- **626:** "scored in 2014 group stage → Slimani" (Djabou & Feghouli also scored in the group stage)
- **659:** "scored in 2022 WC qualifiers → Mahrez" (Slimani/Bounedjah also scored in 2022 qualifying)
- **660:** "scored in 2022 WC qualifiers → Benrahma" (Mahrez/Slimani/Bounedjah also scored)
- **661:** "modern attacker with **fewer than 40** goals → Benrahma" (Mahrez ~30 and Bounedjah ~20s also have <40)
**Why they fail:** Multiple listed options satisfy the criterion.
**Source:** https://en.wikipedia.org/wiki/Algeria_at_the_2014_FIFA_World_Cup
**Remedy:** Add a unique discriminator, or drop.

### Rows 688, 690, 692 — FAIL: broken / non-unique club questions
- **688:** "Which Algerian **club** did NOT compete in the 2022 World Cup qualifiers? → MC Alger" —
  **incoherent**: clubs don't play in World Cup qualifying; the criterion is true of every option.
- **690:** "Which Algerian club is a top team in the Algerian Ligue 1? → MC Alger" — distractors
  **JS Kabylie, USM Alger, CR Belouizdad** are **all** top Algerian Ligue 1 clubs → non-unique.
- **692:** "founding member … based in **Algiers** → MC Alger" — **USM Alger** and **CR Belouizdad**
  (distractors) are also Algiers clubs → non-unique geography.
**Source:** https://en.wikipedia.org/wiki/Algerian_Ligue_Professionnelle_1
**Remedy:** Use non-Algerian distractors (as rows 687/689 do), or drop.

### Row 629 — FAIL: false premise + non-unique nickname
**Q:** Which Algeria team qualified for the 2022 World Cup after winning the 2019 AFCON? **A:** The Desert Foxes
**Why it fails:** Algeria did **not** qualify for 2022. Also the distractor **"The Greens"** (Les
Verts) is **also** a genuine Algeria nickname, so the nickname answer isn't unique either.
**Source:** https://en.wikipedia.org/wiki/Algeria_national_football_team
**Remedy:** Drop the false premise; if testing the nickname, remove "The Greens" as a distractor.

### Row 699 — FAIL: wrong debut date
**Q:** Which Algerian key attacker debuted after the 2018 World Cup? **A:** Benrahma (E: "debuted in 2020")
**Why it fails:** Benrahma's senior Algeria debut was **13 Oct 2015** (v Senegal) — before, not
after, the 2018 World Cup. Contradicts the dataset's own row 638 ("debuted in 2015").
**Source:** https://en.wikipedia.org/wiki/Sa%C3%AFd_Benrahma
**Remedy:** Correct the debut year to 2015, or drop.

### Row 662 — FAIL: overstated/false role
**Q:** Which Algerian attacker was a key creative force during their 2014 World Cup campaign? **A:** Mahrez
**Why it fails:** Mahrez was a **fringe substitute** at the 2014 World Cup (newly called up); the
creative forces were Feghouli and Brahimi. Calling him "a key creative force" in 2014 is false.
**Source:** https://en.wikipedia.org/wiki/Algeria_at_the_2014_FIFA_World_Cup
**Remedy:** Change to Feghouli/Brahimi, or drop.

### Row 656 — FAIL: faulty/false comparison
**Q:** Who played more World Cup matches before 2022, Mahrez or Slimani? **A:** Mahrez
**Why it fails:** Both only ever played the **2014** World Cup (Algeria missed 2018 & 2022), and
Slimani was a **starter** in 2014 while Mahrez was a **substitute** — so Mahrez did not play more.
The explanation's "more total caps ⇒ more WC matches" reasoning is a non-sequitur.
**Source:** https://en.wikipedia.org/wiki/Algeria_at_the_2014_FIFA_World_Cup
**Remedy:** Drop — the comparison is unfounded.

### Rows 623, 630, 708, 710 — FAIL: unverifiable narrative / false descriptor
- **623:** "star part of the squad **before its rebuild** → Mahrez" — Slimani/Feghouli were also
  pre-rebuild stars (non-unique), resting on the unsourced rebuild narrative.
- **630:** "which qualification group saw **squad transition** after 2019 → 2022 CAF Group A" —
  the "transition/rebuild" is unsourced editorializing (UNVERIFIED → FAIL).
- **708:** "which Algerian club had the **most players** in the 2010 World Cup squad → MC Alger" —
  obscure squad-composition count with no authoritative source (UNVERIFIED → FAIL).
- **710:** "which **Algerian Ligue 1 club manager** led the 2022 qualifiers → Belmadi" — Belmadi
  managed **Qatari** clubs (Lekhwiya/Al-Duhail), never an Algerian Ligue 1 club; the descriptor is
  false (the explanation itself says "managed in Qatar").
**Source:** https://en.wikipedia.org/wiki/Djamel_Belmadi
**Remedy:** Replace narrative/false descriptors with verifiable facts, or drop.

---

## Rows 711–810 (Algeria)

### Rows 712, 713, 714, 715, 717 — FAIL: fabricated / false club facts
- **712:** "club that provided the **most** players to the 2010 squad → JS Kabylie" — directly
  **contradicts row 708** (which said MC Alger); both are unsourced "most players" guesses.
- **713:** "club that provided the **most** players to the 2014 squad → USM Alger" — the 2014 squad
  was overwhelmingly Europe-based; an unverifiable "most" count.
- **714:** "USM Alger's academy produced the 2014 goalscorer (Slimani)" — **false**: Slimani came
  through **JSM Chéraga / CR Belouizdad**, never USM Alger.
- **715:** "club's player scored in the 2014 World Cup **penalty shootout** → Feghouli (USM Alger)"
  — **there was no shootout**: Germany won 2-1 **in extra time**; and Feghouli never played for USM Alger.
- **717:** "Stade du 5 Juillet, **home to USM Alger**, hosted a 2022 qualifier" — it's a national/
  multi-club stadium (not "USM Alger's"), and Algeria's 2022 home qualifiers were based in **Blida**.
**Source:** https://en.wikipedia.org/wiki/Islam_Slimani , https://en.wikipedia.org/wiki/Algeria_at_the_2014_FIFA_World_Cup
**Remedy:** Drop the invented club attributions; correct the "no shootout" error.

### Rows 731, 732, 733 — FAIL: wrong debut facts
- **731:** "debuted after the 2019 AFCON → Adam Ounas (E: debuted 2022)" — Ounas debuted ~**2017**
  and was **in the 2019 AFCON squad**.
- **732:** "debuted after 2026 qualification → Titraoui (E: debuted 2024)" — internally contradictory:
  Algeria secured 2026 in **Oct 2025**, so a **2024** debut is *before*, not after.
- **733:** "debuted in 2022 after playing for **MC Alger** → Tougai" — Tougai came through **ES Sétif**
  (then Espérance de Tunis), not MC Alger.
**Source:** https://en.wikipedia.org/wiki/Adam_Ounas
**Remedy:** Fix the debut years/clubs, or drop.

### Rows 759, 770, 778 — FAIL: non-unique answer
- **759:** "missed the 2018 and 2022 World Cups → Mahrez" — **all** Algeria players did (the team
  didn't qualify); the explanation says so itself.
- **770:** "scored in the 2014 group stage → Slimani" — Feghouli and Djabou (distractors) also scored.
- **778:** "scored more World Cup goals than Mahrez → Slimani" — Mahrez scored **0** WC goals, so
  Feghouli (1) and Brahimi (1), both distractors, also scored more.
**Source:** https://en.wikipedia.org/wiki/Algeria_at_the_2014_FIFA_World_Cup
**Remedy:** Add a unique discriminator, or drop.

### Row 718 — FAIL: wrong answer
**Q:** Which Algerian manager failed to qualify for **both** the 2018 and 2022 World Cups? **A:** Georges Leekens
**Why it fails:** Leekens managed only during the **2018** campaign; the **2022** failure (play-off
loss to Cameroon) was under **Belmadi**. No single manager failed "both," so Leekens is wrong.
**Source:** https://en.wikipedia.org/wiki/Georges_Leekens
**Remedy:** Restrict to 2018 only (as the correct row 473 does), or drop.

### Row 720 — FAIL: wrong explanation ("intercontinental playoff")
**Q:** Which Algerian manager led the 2010 World Cup playoff win? **A:** Rabah Saâdane
**Why it fails:** Saâdane is correct, but the explanation again calls the decider an
"**intercontinental** playoff" — it was a **CAF** play-off vs Egypt (Khartoum, 18 Nov 2009).
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round
**Remedy:** Replace "intercontinental playoff" with "CAF play-off vs Egypt."

### Rows 726, 760 — FAIL: false qualification/timing
- **726:** "became all-time top scorer **during the 2014 qualifiers** → Slimani" — he passed the
  record on **8 Oct 2021** (a 2022 qualifier), not in 2014.
- **760:** "qualified for 2014 **directly via CAF, unlike 2010's playoff** → Slimani" — 2014 also
  required a **playoff** (vs Burkina Faso), and Slimani wasn't even in the 2010 squad (debuted 2012).
**Source:** https://en.wikipedia.org/wiki/Islam_Slimani
**Remedy:** Fix the timing/"directly" framing, or drop.

### Rows 762, 764 — FAIL: unverified goal stats
- **762:** "scored **7 goals** in 2018 World Cup qualifying → Slimani" — unconfirmed (his known
  campaign tallies are 5 in 2014 and 8 in 2022; no source supports 7 in 2018).
- **764:** "scored a **crucial brace** in a 2014 qualifier → Slimani" — unverified for any specific match.
**Source:** https://en.wikipedia.org/wiki/List_of_international_goals_scored_by_Islam_Slimani
**Remedy:** Verify the exact tally/match, or drop. UNVERIFIED → FAIL.

### Row 735 — FAIL: false explanation (cap count)
**Q:** Which Algerian player debuted internationally before his Manchester City move? **A:** Mahrez
**Why it fails:** The answer is fine (debuted 2014, joined City 2018), but the explanation claims he
had "**over 90 caps before joining Manchester City**" — he had roughly **35** caps in 2018.
**Source:** https://en.wikipedia.org/wiki/Riyad_Mahrez
**Remedy:** Remove the false cap figure.

### Row 739 — FAIL: false premise (cap count)
**Q:** Which Algerian player has over 40 goals **but fewer than 90 caps**? **A:** Slimani
**Why it fails:** Slimani has **~98 caps** (more than 90, and more than Mahrez), so "fewer than 90
caps" is false; the explanation also wrongly implies Slimani has fewer caps than Mahrez.
**Source:** https://en.wikipedia.org/wiki/Islam_Slimani
**Remedy:** Drop the false cap qualifier.

### Row 767 — FAIL: wrong venue
**Q:** Which Algerian player scored at the 2014 World Cup **in Belo Horizonte**? **A:** Slimani
**Why it fails:** Slimani's goal vs **Russia** was in **Curitiba** (Arena da Baixada), not Belo
Horizonte. Algeria's Belo Horizonte match was vs **Belgium**, where **Feghouli** (not Slimani) scored.
**Source:** https://en.wikipedia.org/wiki/Algeria_at_the_2014_FIFA_World_Cup
**Remedy:** Correct the venue (Curitiba), or drop the city reference.

### Row 805 — FAIL: false explanation
**Q:** Which Algerian player was their top scorer during the 2014 group stage? **A:** Slimani
**Why it fails:** Slimani (2 goals) being Algeria's top group-stage scorer is fine, but the
explanation says he scored "**Algeria's only two goals in the 2014 group stage**" — Algeria scored
**six** in the group stage (1 v Belgium, 4 v South Korea, 1 v Russia).
**Source:** https://en.wikipedia.org/wiki/Algeria_at_the_2014_FIFA_World_Cup
**Remedy:** Fix the explanation (Algeria scored 6 group-stage goals; Slimani got 2 of them).

---

## Rows 811–920 (Algeria)

### Rows 815, 821, 852, 857, 880, 883, 854 — FAIL: 2018/2022 World Cup false premise
Each places an Algerian **at the 2018 or 2022 World Cup** (which Algeria did **not** reach):
- **815, 821:** Slimani "all-time top scorer **at the 2022 World Cup** / during the 2022 tournament"
- **852:** Mahrez "in the **2018 World Cup squad**"; **880:** Mahrez "**played at the 2018 World Cup**"
- **883:** Mahrez "earned his **2018 World Cup call-up**"; **857:** Mahrez "captain **at the 2022 World Cup**"
- **854:** Bounedjah "**playing at the 2014 World Cup's** Estádio Beira-Rio" — he didn't play in 2014 (debuted ~2018)
**Source:** https://en.wikipedia.org/wiki/Algeria_national_football_team
**Remedy:** Re-anchor to qualifying campaigns / 2014 / 2019, or drop.

### Rows 818, 822, 892, 895, 896, 915 — FAIL: Slimani "top scorer" wrong timing
All claim Slimani was the all-time top scorer **at the 2014 WC** (818, 915) or **became** top scorer
**during 2014 / 2018 qualifying** (822, 892, 895, 896). He passed Tasfaout's record on **8 Oct 2021**
(a 2022 qualifier); at the 2014 WC the record-holder was still Tasfaout.
**Source:** https://en.wikipedia.org/wiki/Islam_Slimani
**Remedy:** Use "during 2022 qualifying (Oct 2021)" or a present-tense appositive instead.

### Rows 879, 887, 919 — FAIL: temporal contradiction
All have the 2016 Premier League win **preceding** a 2014 event:
- **879:** "won PL 2016, **before** his 2014 World Cup debut"
- **887:** "2016 PL win **preceded** the 2014 World Cup qualification"
- **919:** "in the 2014 squad **after winning the 2016** Premier League"
The 2016 title came **after** 2014 — the explanations themselves say "later/after," contradicting the questions.
**Source:** https://en.wikipedia.org/wiki/Riyad_Mahrez
**Remedy:** Drop the impossible ordering.

### Row 811 — FAIL: false (Mahrez didn't score in 2014)
**Q:** …key to 2019 AFCON **and also scored at the 2014 World Cup**? **A:** Mahrez (E: "scored against South Korea")
**Why it fails:** Mahrez scored **0** goals at the 2014 World Cup; Algeria's South Korea scorers were
Slimani, Halliche, Djabou and Brahimi.
**Source:** https://en.wikipedia.org/wiki/Algeria_at_the_2014_FIFA_World_Cup
**Remedy:** Drop the "scored at 2014" clause (or change the player).

### Row 840 — FAIL: false (Algeria did not top the 2018 group)
**Q:** …2016 PL win preceded his **2018 World Cup qualification group top spot**? **A:** Mahrez
**Why it fails:** Algeria finished **bottom** of their 2018 qualifying group (Group B; Nigeria topped it,
Algeria last with 1 point) — they did not top it.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Drop — the premise is false.

### Row 868 — FAIL: false (Mahrez played no 2014 qualifiers)
**Q:** …star attacker **scored in the 2014 World Cup qualifiers**? **A:** Mahrez
**Why it fails:** Mahrez debuted for Algeria in 2014, **after** qualification ended (Nov 2013), so he
played in none of the 2014 qualifiers (same defect as row 620). The intended scorer is Slimani.
**Source:** https://en.wikipedia.org/wiki/Riyad_Mahrez
**Remedy:** Change the answer to Slimani, or drop.

### Rows 855, 905 — FAIL: unverifiable narrative / non-unique
- **855:** "which squad was younger, 2014 or 2026 qualifiers? → 2026" — unsourced squad-age/rebuild claim.
- **905:** "which striker missed the 2018 and 2022 World Cups? → Slimani" — the **whole team** missed both,
  so all options (Mahrez, Feghouli, Brahimi) are equally valid → non-unique.
**Source:** https://en.wikipedia.org/wiki/Algeria_national_football_team
**Remedy:** Replace with verifiable/uniquely-answerable facts, or drop.

---

## Rows 921–1228 (Algeria)

### Rows 935, 1013, 1017, 1020, 1024, 1094, 1097, 1144, 1218 — FAIL: "intercontinental playoff" mislabel
All describe Algeria's **2010 qualification play-off vs Egypt** (Omdurman, 18 Nov 2009) as an
"**intercontinental** playoff" (in the question and/or explanation). It was an intra-**CAF** play-off
(the CAF third-round decider), not intercontinental. Answers ("Egypt" / "2010") are correct; the label is the defect.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round
**Remedy:** Replace "intercontinental playoff" with "CAF play-off vs Egypt."

### Rows 954, 966, 1037, 1042, 1053, 1058 — FAIL: self-referential answer
Each asks "which CAF/other nation, **like Algeria**, …" but the keyed answer is **Algeria itself**
(954/966 "nearly beat Germany 2014", 1037/1058 "best result = R16", 1042/1053 "qualified for 2026 via CAF").
A "which other nation like X" question cannot be answered "X."
**Source:** https://en.wikipedia.org/wiki/Algeria_national_football_team
**Remedy:** Supply a genuine other nation, or rephrase to drop "like Algeria."

### Rows 929, 930, 1139, 1142, 1143 — FAIL: "qualified via CAF" non-unique / false "directly"
Algeria — being a CAF nation — reached **2010, 2014 and 2026 all through CAF**. So:
- **929, 930:** "achieved/secured through CAF (→ 2014)" with **2010** as a distractor — 2010 was also CAF → non-unique.
- **1139:** "two World Cups via CAF → 2014 and 2026" — but **2010** was also via CAF → distractor "2010 and 2014" equally valid.
- **1143:** "qualified through CAF → 2026" with 2010/2014 distractors (both also CAF) → non-unique.
- **1142:** "qualified **directly through CAF, not a playoff** → 2014" — **false**: 2014 was a CAF **play-off** vs Burkina Faso; the only direct qualification was **2026**.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round
**Remedy:** Use a unique discriminator ("not a play-off" → 2026, as row 631 does), or drop.

### Rows 1052, 1067, 1043, 1107, 956, 1054 — FAIL: non-unique answer
- **1052:** "like Algeria, qualified via CAF for 2014 → Nigeria" — **Ghana** and **Cameroon** (distractors) also qualified for 2014 via CAF.
- **1067:** "like Algeria, eliminated in the 2010 group stage → South Africa" — **Nigeria** and **Ivory Coast** also group-exited in 2010 (only Ghana advanced).
- **1043:** "reached the 2010 QF, unlike Algeria → Germany" — **Spain** (distractor) won 2010, so also reached the QF.
- **1107:** "did NOT face in the 2014 **knockout** stage → Argentina" — **Russia** and **South Korea** (distractors) were group opponents, so also not faced in the knockout.
- **956:** "unlike Algeria, qualified for **both** 2018 and 2022 → Tunisia" — **Morocco** (distractor) also qualified for both.
- **1054:** "like Algeria, won AFCON in both the 1990s and 2010s → Egypt" — **Nigeria** (1994, 2013) and **Ivory Coast** (1992, 2015) also did.
**Source:** https://en.wikipedia.org/wiki/Africa_Cup_of_Nations
**Remedy:** Replace the over-broad distractors so only one option fits.

### Row 955 — FAIL: wrong fact
**Q:** Which CAF nation, like Algeria in 2019, also won its second AFCON title? **A:** Egypt (E: "Egypt won its second in 1998")
**Why it fails:** 1998 was Egypt's **fourth** AFCON title (after 1957, 1959, 1986); their second was **1959**.
**Source:** https://en.wikipedia.org/wiki/Egypt_national_football_team
**Remedy:** Pick a nation whose *second* title is the hook, or fix the Egypt fact.

### Rows 922, 927, 1147 — FAIL: 2022 World Cup false premise
- **922:** "winger with 90+ caps in their **2022 World Cup squad** → Mahrez" — no 2022 WC squad (Algeria didn't qualify).
- **927:** "Algerian **World Cup 2022 player** also won the 2016 PL → Mahrez" — there were no Algerian 2022 WC players.
- **1147:** "won the AFCON before qualifying → 2019 (E: 'then **qualified for the 2022 World Cup**')" — Algeria **failed** to qualify for 2022.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Re-anchor to qualifying / 2014 / 2026.

### Row 1039 — FAIL: false contrast
**Q:** Which nation qualified for the 2014 WC via a playoff, **unlike Algeria**? **A:** Uruguay
**Why it fails:** Uruguay's was an **intercontinental** play-off, but Algeria **also** qualified via a
play-off (the CAF play-off vs Burkina Faso) — so "unlike Algeria" is false; the explanation's "Algeria
qualified directly" repeats the recurring error.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_qualification_%E2%80%93_CAF_Third_Round
**Remedy:** Reword to "intercontinental play-off, unlike Algeria's CAF play-off," or drop.

### Rows 1219, 1221, 1222, 1223, 1224 — FAIL: unverifiable "squad rebuild" narrative
All answer a "why did the squad change / look different after 2019" question with "**a squad rebuild**"
(1219 is also circular: "because of their AFCON triumph"). The "post-2019 rebuild" is unsourced
editorializing, and Belmadi remained manager throughout (so the "new manager" framing elsewhere is wrong too).
**Source:** none located (narrative claim).
**Remedy:** Replace with concrete, sourceable facts (named retirements/debutants), or drop.

---

# ARGENTINA (rows 1229–2160)

## Rows 1229–1300 (Argentina)

### Rows 1244, 1246, 1259, 1277 — FAIL: corrupted answer (spreadsheet date-mangling)
The `answer` cell is an Excel date-conversion of a scoreline (the explanation has the real score):
- **1244 / 1259:** `02-Jan` = **"2-1"** (Argentina 2-1 Chile, 2019 Copa third-place match)
- **1246:** `04-Feb` = **"4-2"** (Argentina beat France 4-2 on penalties, 2022 final)
- **1277:** `02-Feb` = **"2-2"** (Argentina 2-2 Netherlands a.e.t., 2022 quarter-final)
**Source:** https://en.wikipedia.org/wiki/Argentina_at_the_2022_FIFA_World_Cup
**Remedy:** Restore the real scoreline strings; sweep the whole dataset for `DD-Mon` answers.

### Rows 1268, 1278 — FAIL: non-unique answer (2008 Olympic gold)
Both ask which Argentine (at the 2014 / 2022 WC) had won **2008 Olympic gold → Messi**, but
**Ángel Di María** *and* **Sergio Agüero** (listed distractors) were also in the gold-winning
2008 squad. (At 2022, Di María was in the squad too, so still non-unique.)
**Source:** https://en.wikipedia.org/wiki/Football_at_the_2008_Summer_Olympics_%E2%80%93_Men%27s_tournament
**Remedy:** Use a discriminator unique to Messi, or drop.

### Row 1276 — FAIL: false premise (no such match)
**Q:** …Which team did Argentina beat 1-0 in the **2024 Copa América group stage**? **A:** Brazil
**Why it fails:** Argentina (Group A) and Brazil (Group D) were in **different groups** and did
**not** meet at the 2024 Copa América at all (Brazil went out in the quarter-finals to Uruguay).
**Source:** https://en.wikipedia.org/wiki/2024_Copa_Am%C3%A9rica
**Remedy:** Drop — the match never happened.

### Row 1279 — FAIL: wrong explanation (goal breakdown)
**Q:** …which Argentine had 13 total World Cup goals? **A:** Messi
**Why it fails:** The total (13) is right, but the explanation says they came "across the **2014,
2018, and 2022** tournaments" — those three sum to **12** (4+1+7). Messi's 13th is his **2006**
goal vs Serbia & Montenegro.
**Source:** https://en.wikipedia.org/wiki/Lionel_Messi
**Remedy:** Fix the breakdown (include the 2006 goal), or drop the enumeration.

### Row 1281 — FAIL: non-unique / overstated
**Q:** …who partnered Otamendi in central defence [at 2022]? **A:** Cristian Romero ("throughout the campaign")
**Why it fails:** **Lisandro Martínez** (a distractor) also started at CB next to Otamendi (vs
Mexico and Poland after the Saudi loss); Romero was not the partner "throughout." Two valid answers.
**Source:** https://en.wikipedia.org/wiki/Argentina_at_the_2022_FIFA_World_Cup
**Remedy:** Drop "throughout," or make the answer unique to one match.

### Row 1300 — FAIL: wrong fact
**Q:** For the 2022 World Cup, which facility was Argentina's main training base? **A:** AFA complex in Ezeiza
**Why it fails:** Argentina's 2022 World Cup base camp was **Qatar University** in Doha (hotel +
training in one place). Ezeiza is their permanent home base in Argentina, not their tournament base
— and "University of Qatar" is even offered as a distractor.
**Source:** https://www.gulf-times.com/story/714557/Argentina-to-stay-and-train-at-Qatar-University-during-World-Cup
**Remedy:** Change the answer to the Qatar University base.

### Row 1298 — FAIL: false (did not win every home qualifier)
**Q:** During which World Cup qualifiers did Argentina win **every home match**? **A:** 2022 qualifiers
**Why it fails:** Argentina **drew 0-0 at home vs Brazil** (San Juan, 16 Nov 2021) during 2022
CONMEBOL qualifying — so they did not win every home match (they were unbeaten, not all-winning).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Reword to "unbeaten in qualifying," or drop.

### Rows 1248, 1299, 1264, 1296 — FAIL: unverified / unsupported claims
- **1248:** "Argentina fell to **10th** in early 2018 under Sampaoli" — unconfirmed and implausible
  (they were ranked **5th** by June 2018 with few intervening matches; no source supports a 10th-place dip).
- **1299:** "used **Estadio Monumental multiple times** during 2022 qualifying" — unsupported; the
  Monumental was under renovation and Argentina used provincial venues (San Juan, Santiago del Estero) for many qualifiers.
- **1264:** "2022 squad featured players from **thirteen** different leagues" — unverifiable exact count.
- **1296:** "**over 100** Argentine players in Europe's top-five leagues" — explanation is self-referential
  ("The reference fact states…") and the count is unverified.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking , https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Verify each figure against a source, or drop. UNVERIFIED → FAIL.

---

## Rows 1301–1390 (Argentina)

### Rows 1341, 1342 — FAIL: false (Argentina were unbeaten in 2022 qualifying)
Both claim Argentina's "only defeat" in 2022 CONMEBOL qualifying was a **2-0 loss to Brazil**.
Argentina went **unbeaten** through the entire 2022 qualifying campaign (11 W, 6 D, **0 L** — part of
their 36-match unbeaten run). There was no 2-0 loss to Brazil; the two Brazil games were an abandoned
match and a 0-0 draw.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop — Argentina had no defeats in 2022 qualifying.

### Row 1352 — FAIL: corrupted answer (formation → date)
**Q:** …what primary formation number did Scaloni use? **A:** `04/03/2003`
**Why it fails:** `04/03/2003` is a spreadsheet date-mangling of **"4-3-3"** (the explanation says
4-3-3). The rendered answer is unusable.
**Source:** https://en.wikipedia.org/wiki/Argentina_at_the_2022_FIFA_World_Cup
**Remedy:** Restore the answer to **"4-3-3"** (add `4-3-3`-style formations to the date-corruption sweep).

### Rows 1355, 1361 — FAIL: false detail ("four goals in 23 minutes")
Both say Germany scored **four goals in 23 minutes** vs Argentina (2010 QF). Germany's four goals
came at **3', 67', 74', 89'** — spanning 86 minutes (and the last three span ~22 min, i.e. *three*
goals, not four). The "four goals in 23 minutes" claim is false.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_knockout_stage
**Remedy:** Drop the "four in 23 minutes" detail (true score was 4-0).

### Row 1369 — FAIL: wrong (Man of the Match)
**Q:** In which World Cup final was **Ángel Di María** named Man of the Match? **A:** 2022
**Why it fails:** The 2022 final's official Player of the Match was **Lionel Messi**, not Di María
(Messi won 5 POTM awards at the tournament, including the final). Di María scored but didn't win it.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_final
**Remedy:** Drop — Di María was not named MOTM of any World Cup final.

### Row 1378 — FAIL: non-unique answer
**Q:** In which World Cup did Messi win the **Golden Ball**? **A:** 2014 FIFA World Cup
**Why it fails:** Messi won the World Cup Golden Ball in **both 2014 and 2022**, and **2022** is a
listed distractor — so two options are correct.
**Source:** https://en.wikipedia.org/wiki/Lionel_Messi
**Remedy:** Make the answer unique (e.g. add a distinguishing clue), or drop.

### Row 1373 — FAIL: non-unique answer
**Q:** In which two World Cups did Argentina top their group? **A:** 2022 and 2014
**Why it fails:** Argentina also topped their groups in **1998 (Group H) and 2006 (Group C)** — and
"1998 and 2006" is a listed option — so the answer isn't unique. (They topped 2010's group too.)
**Source:** https://en.wikipedia.org/wiki/Argentina_national_football_team
**Remedy:** Replace the distractor pairs so only one is fully correct, or drop.

### Row 1335 — FAIL: non-unique answer
**Q:** Estadio Monumental had a larger capacity than which other Argentine stadium? **A:** Estadio Único Madre
**Why it fails:** The Monumental (~84,000) is larger than **all four** options — Único Madre (~30k),
Bombonera (~54k), Kempes (~57k) and Amalfitani (~49k) — so every choice is "correct."
**Source:** https://en.wikipedia.org/wiki/Estadio_Monumental_(Buenos_Aires)
**Remedy:** Use one stadium that is actually *larger* than the Monumental (none in Argentina is), or rewrite.

### Rows 1332, 1333 — FAIL: wrong WC-goal breakdown
Both ask how many WC goals Messi scored "**from 2014 to 2022**" / "in **2014, 2018, 2022** combined"
and answer **13**. Those three tournaments sum to **12** (4+1+7); Messi's 13th WC goal was in **2006**.
**Source:** https://en.wikipedia.org/wiki/Lionel_Messi
**Remedy:** Either answer **12** for 2014–2022, or include 2006 to reach 13.

### Rows 1302, 1303, 1313 — FAIL: unverifiable squad-league count
All assert Argentina's 2022 squad came from "**13** different club leagues" (same unverified claim as
row 1264). No authoritative source confirms the exact figure.
**Source:** https://en.wikipedia.org/wiki/Argentina_at_the_2022_FIFA_World_Cup
**Remedy:** Verify the exact count against the official squad list, or drop. UNVERIFIED → FAIL.

### Row 1334 — FAIL: wrong figure
**Q:** In 2018 and 2022 qualifying, Argentina scored over how many combined goals? **A:** 50
**Why it fails:** Argentina scored ~**27** in 2022 CONMEBOL qualifying and ~**19** in 2018 — about
**46** combined, not "over 50."
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Recompute the combined total (~46), or drop.

### Rows 1336, 1339 — FAIL: unsupported venue claims
- **1336:** "won **every home match in Buenos Aires**" in 2022 qualifying — unverified narrowing (and
  the broad version, row 1298, is false; Argentina rotated venues and drew at home in San Juan).
- **1339:** "Estadio Monumental was their **primary home venue** for 2022 qualifying" — Argentina rotated
  venues (opener at La Bombonera; a Venezuela qualifier was moved **off** the Monumental), so "primary" isn't supported.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Verify the venue breakdown, or drop. UNVERIFIED → FAIL.

---

## Rows 1391–1480 (Argentina)

### Rows 1444, 1448, 1452 — FAIL: corrupted answer (date-mangling)
- **1444:** `03-Mar` = **"3-3"** (2022 final after extra time)
- **1448:** `03-Jan` = **"3-1"** (beat Ecuador to qualify for 2018)
- **1452:** `02-Jan` = **"2-1"** (beat Chile, 2019 Copa third place)
**Source:** https://en.wikipedia.org/wiki/Argentina_national_football_team
**Remedy:** Restore the real scorelines; part of the dataset-wide `DD-Mon` corruption.

### Rows 1451, 1455 — FAIL: false premise (no Argentina–Brazil 2024 Copa match)
Both assert Argentina beat Brazil 1-0 in the **2024 Copa América group stage**. They were in
different groups and never met at the 2024 Copa (cf. row 1276).
**Source:** https://en.wikipedia.org/wiki/2024_Copa_Am%C3%A9rica
**Remedy:** Drop — the match never happened.

### Rows 1473, 1397 — FAIL: false (2022 qualifying record)
- **1473:** "won **all** home qualifiers for the 2022 World Cup" — false; Argentina drew 0-0 at home
  vs Brazil (San Juan). (cf. row 1298.)
- **1397:** "2022 qualifying record **11 W, 5 D, 1 L**" — false; Argentina were **unbeaten**: 11 W,
  **6 D, 0 L** (39 pts).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Correct to unbeaten (11-6-0); they did not win every home match.

### Row 1415 — FAIL: wrong (2023 U-20 World Cup)
**Q:** In which year did Argentina's U-20 team win the FIFA U-20 World Cup? **A:** 2023
**Why it fails:** **Uruguay** won the 2023 U-20 World Cup (beat Italy 1-0). Argentina **hosted** it
but were eliminated in the round of 16 (lost to Nigeria). Argentina's last U-20 title was 2007.
**Source:** https://en.wikipedia.org/wiki/2023_FIFA_U-20_World_Cup
**Remedy:** Drop, or change to a year Argentina actually won (e.g. 2007).

### Row 1476 — FAIL: wrong (2014 Fair Play Award)
**Q:** When did Argentina win the FIFA Fair Play Award at the World Cup? **A:** 2014
**Why it fails:** The 2014 World Cup FIFA Fair Play Award went to **Colombia**, not Argentina.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup
**Remedy:** Drop — Argentina did not win the 2014 Fair Play Award.

### Rows 1414, 1395 — FAIL: non-unique answer
- **1414:** "year Emiliano Martínez won the Copa América **Golden Glove** → 2024" — he also won it in
  **2021** (a listed distractor), so two options are correct.
- **1395:** "qualifying campaign in which Messi was Argentina's **top scorer** → 2022" — Messi was also
  Argentina's top scorer in **2018** qualifying (7 goals incl. the decisive Ecuador hat-trick), a listed option.
**Source:** https://en.wikipedia.org/wiki/Lionel_Messi
**Remedy:** Make the answer unique, or drop.

### Rows 1428, 1429, 1431 — FAIL: unverified ranking ("10th in early 2018")
All claim Argentina fell to **10th** in the FIFA rankings in early 2018 under Sampaoli (cf. row 1248).
Unconfirmed and implausible — they were **5th** by June 2018 with few intervening matches; no source
supports a 10th-place dip.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Verify the exact low, or drop. UNVERIFIED → FAIL.

### Rows 1396, 1472 — FAIL: unverified venue claim (Monumental in 2022 qualifying)
Both say Estadio Monumental hosted **multiple** of Argentina's 2022 qualifiers (cf. rows 1299/1339).
Argentina rotated venues (opener at La Bombonera; a Venezuela qualifier was moved **off** the Monumental,
which was undergoing renovation); the "multiple matches at the Monumental" claim is unsupported.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Verify the venue list, or drop. UNVERIFIED → FAIL.

### Row 1417 — FAIL: unverified / likely-wrong year
**Q:** In which year did Messi surpass Mascherano as Argentina's most-capped player? **A:** 2022
**Why it fails:** Messi passed Mascherano's 147-cap record around **2021** (he already had ~158 caps by
the end of 2021, and ~169 by the 2022 World Cup), so "2022" is not supported.
**Source:** https://en.wikipedia.org/wiki/Lionel_Messi
**Remedy:** Verify the exact date (≈2021), or drop. UNVERIFIED → FAIL.

---

## Rows 1481–1570 (Argentina)

### Rows 1483, 1504 — FAIL: wrong (2023 U-20 World Cup)
Both say Argentina's U-20 team **won** the 2023 FIFA U-20 World Cup "on home soil." **Uruguay** won
it; Argentina hosted but went out in the round of 16 (cf. row 1415).
**Source:** https://en.wikipedia.org/wiki/2023_FIFA_U-20_World_Cup
**Remedy:** Drop, or use Argentina's actual last U-20 title (2007).

### Rows 1484, 1496 — FAIL: non-unique answer
- **1484:** "year Emiliano Martínez won the Copa América Golden Glove → 2024" — he also won it in
  **2021** (a listed option). (cf. row 1414.)
- **1496:** "qualifying campaign in which Messi was Argentina's top scorer → 2022" — also true of
  **2018** qualifying (a listed option). (cf. row 1395.)
**Source:** https://en.wikipedia.org/wiki/Lionel_Messi
**Remedy:** Make the answer unique, or drop.

### Row 1521 — FAIL: non-unique answer
**Q:** Which 2022 World Cup group stage opponent did Argentina NOT lose to? **A:** Poland
**Why it fails:** Argentina lost only to Saudi Arabia in the group; they did **not** lose to **Mexico**
either (a listed option), so two answers are valid. (Australia, also listed, was a round-of-16 opponent,
not a group opponent.)
**Source:** https://en.wikipedia.org/wiki/Argentina_at_the_2022_FIFA_World_Cup
**Remedy:** Leave only one not-lost-to group opponent among the options.

### Row 1548 — FAIL: non-unique answer
**Q:** Which Argentina defender started in the 2022 World Cup final? **A:** Cristian Romero
**Why it fails:** Argentina's final back four was Molina, Romero, **Otamendi**, Tagliafico — so
**Nicolás Otamendi** and **Nahuel Molina** (both listed options) also started. Only Lisandro Martínez (the 4th option) didn't.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_final
**Remedy:** Use defenders who did *not* start as the distractors.

### Row 1566 — FAIL: wrong figure
**Q:** Which Argentina forward scored **42 goals in 101 appearances** before retiring in 2021? **A:** Sergio Agüero
**Why it fails:** Agüero scored **41** goals (not 42) in his 101 Argentina caps.
**Source:** https://en.wikipedia.org/wiki/Sergio_Ag%C3%BCero
**Remedy:** Correct to **41** goals.

### Row 1529 — FAIL: wrong figure
**Q:** Which Argentina campaign scored **over 50 goals** in 2018 & 2022 qualifiers combined? **A:** World Cup qualifying
**Why it fails:** Argentina scored ~27 (2022) + ~19 (2018) ≈ **46** combined — not over 50 (cf. row 1334).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Recompute (~46), or drop.

### Row 1486 — FAIL: unverified venue claim
**Q:** When did Estadio Monumental host Argentina's 2022 World Cup qualifiers? **A:** 2022 qualifying matches
**Why it fails:** Same unsupported "Monumental hosted multiple 2022 qualifiers" claim as rows
1299/1339/1396/1472 — Argentina rotated venues and the Monumental was under renovation.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Verify the venue list, or drop. UNVERIFIED → FAIL.

### Row 1482 — FAIL: vague/unverifiable + self-referential
**Q:** When did Argentina's rivalry with Brazil become South America's most-played international fixture? **A:** Before 2022
**Why it fails:** "Before 2022" is not a meaningful answer to "when did it become the most-played," and
the explanation is self-referential ("The fact states…"). No verifiable milestone is given.
**Source:** https://en.wikipedia.org/wiki/Argentina%E2%80%93Brazil_football_rivalry
**Remedy:** Drop, or replace with a concrete, sourceable date.

---

## Rows 1571–1670 (Argentina)

### Rows 1666, 1668 — FAIL: wrong year (Messi passed Mascherano in 2021)
Both say Messi surpassed Mascherano's caps record "**in 2022**." Messi broke the 147-cap record on
**29 June 2021** (his 148th cap, vs Bolivia at the 2021 Copa América). The answer (Mascherano) is
right but the year is wrong. (cf. row 1417.)
**Source:** https://en.wikipedia.org/wiki/Lionel_Messi
**Remedy:** Change "2022" to **2021**.

### Row 1658 — FAIL: wrong explanation (goal total / timing)
**Q:** Which Argentina player became their all-time top scorer before the 2022 World Cup? **A:** Messi
**Why it fails:** Messi is correctly the answer, but the explanation says he "had already scored **116
goals** … before the 2022 tournament" — 116 is his **2026** total. Before the 2022 World Cup he had ~91.
**Source:** https://en.wikipedia.org/wiki/Lionel_Messi
**Remedy:** Fix the figure (~91 before 2022; 116 as of 2026).

### Row 1613 — FAIL: built on unverified premise
**Q:** Which Argentina manager oversaw their drop to **10th** in the FIFA rankings in early 2018? **A:** Jorge Sampaoli
**Why it fails:** Sampaoli was indeed the manager, but the premise (a drop to **10th** in early 2018) is
the same unverified/implausible claim failed at rows 1248/1428/1429/1431 (Argentina were 5th by June 2018).
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Verify the ranking premise, or rewrite without the "10th" figure.

---

## Rows 1671–1780 (Argentina)

### Rows 1748, 1749, 1750 — FAIL: non-unique (2008 Olympic gold)
All ask which player was in Argentina's 2008 Olympic gold squad → Messi, but **Sergio Agüero** and
**Ángel Di María** (listed options) were also in that squad. Only Higuaín (4th option) wasn't. (cf. 1268/1278.)
**Source:** https://en.wikipedia.org/wiki/Football_at_the_2008_Summer_Olympics_%E2%80%93_Men%27s_tournament
**Remedy:** Use distractors who were NOT in the 2008 squad.

### Rows 1718, 1720 — FAIL: wrong scorer
Both say **Cristián Pavón** scored in Argentina's 4-3 round-of-16 loss to France (2018). Argentina's
three scorers were **Di María, Gabriel Mercado, and Sergio Agüero** — not Pavón.
**Source:** https://en.wikipedia.org/wiki/Argentina_at_the_2018_FIFA_World_Cup
**Remedy:** Change to a real scorer (Di María / Mercado / Agüero); cf. correct row 1721 (Agüero).

### Row 1686 — FAIL: non-unique answer
**Q:** Which Argentina player partnered Otamendi in central defence at the 2022 World Cup? **A:** Cristian Romero
**Why it fails:** **Lisandro Martínez** (a listed option) also partnered Otamendi (he started at CB vs
Mexico and Poland after the Saudi loss). Two valid answers. (cf. row 1281.)
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_final
**Remedy:** Use defenders who never partnered Otamendi as distractors.

### Row 1755 — FAIL: wrong (Man of the Match)
**Q:** Which Argentina player was named Man of the Match in the 2022 World Cup final? **A:** Ángel Di María
**Why it fails:** The 2022 final's Player of the Match was **Messi**, not Di María (cf. row 1369).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_final
**Remedy:** Change to Messi, or drop.

### Row 1695 — FAIL: wrong goal breakdown
**Q:** Which Argentina player scored 13 World Cup goals across 2014, 2018, and 2022? **A:** Messi
**Why it fails:** Messi is the player with 13 WC goals, but those three tournaments total **12** (4+1+7);
his 13th was in **2006** (cf. rows 1332/1333).
**Source:** https://en.wikipedia.org/wiki/Lionel_Messi
**Remedy:** Either say "12 across 2014–2022" or include 2006.

### Row 1722 — FAIL: wrong figure in explanation
**Q:** Which Argentina player scored more than 40 international goals? **A:** Sergio Agüero
**Why it fails:** Agüero is the only 40+ scorer among the options (so the answer is right), but the
explanation states he scored "**42** goals" — he scored **41** (cf. row 1566).
**Source:** https://en.wikipedia.org/wiki/Sergio_Ag%C3%BCero
**Remedy:** Correct the explanation to 41 goals.

---

## Rows 1781–1900 (Argentina)

### Rows 1835, 1836, 1893 — FAIL: non-unique answer
- **1835, 1836:** "which star was in the 2008 Olympic gold squad → Messi" — Agüero & Di María (options) were too.
- **1893:** "appeared in every World Cup 2010–2022 → Messi" — **Di María** (an option) also played 2010, 2014, 2018 and 2022.
**Source:** https://en.wikipedia.org/wiki/%C3%81ngel_Di_Mar%C3%ADa
**Remedy:** Use distractors who don't satisfy the criterion.

### Row 1884 — FAIL: non-unique answer
**Q:** Which Argentine midfielder was key in both the 2021 Copa América and 2022 World Cup? **A:** Leandro Paredes
**Why it fails:** **Rodrigo De Paul** (a listed option, and the dataset's own answer in rows 1645/1887)
was also key in both — two valid answers.
**Source:** https://en.wikipedia.org/wiki/Argentina_at_the_2022_FIFA_World_Cup
**Remedy:** Make the discriminator unique, or drop.

### Rows 1873, 1900 — FAIL: wrong year (Mascherano record)
Both say Messi surpassed Mascherano's caps record "**in 2022**" — it was **29 June 2021** (cf. rows 1417/1666/1668).
The answer (Mascherano) is right; the year is wrong.
**Source:** https://en.wikipedia.org/wiki/Lionel_Messi
**Remedy:** Change 2022 → 2021.

### Row 1795 — FAIL: wrong (Man of the Match)
**Q:** …Di María's 2022 final performance earned him Man of the Match? **A:** Di María
**Why it fails:** Messi was the 2022 final's Player of the Match, not Di María (cf. 1369/1755).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_final
**Remedy:** Change to Messi, or drop.

### Row 1807 — FAIL: wrong scorers
**Q:** Which Argentina players scored in their 4-3 2018 loss to France? **A:** Pavón, Agüero, Mercado
**Why it fails:** The scorers were **Di María, Mercado, Agüero** — **Pavón did not score** (cf. 1718/1720).
**Source:** https://en.wikipedia.org/wiki/Argentina_at_the_2018_FIFA_World_Cup
**Remedy:** Replace Pavón with Di María.

### Row 1808 — FAIL: wrong figures
**Q:** Which Argentina qualifying campaign had over 25 goals: 2018 or 2022? **A:** Both (E: "over 50 combined")
**Why it fails:** 2022 had ~27 (over 25 ✓) but **2018 had ~19** (under 25); the combined total is ~46, not
over 50 (cf. rows 1334/1529).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Only 2022 cleared 25 goals; fix the figures.

### Row 1849 — FAIL: wrong (2014 Fair Play Award)
**Q:** Which Argentina team won the FIFA Fair Play Award in 2014? **A:** Argentina national team
**Why it fails:** **Colombia** won the 2014 World Cup Fair Play Award, not Argentina (cf. row 1476).
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup
**Remedy:** Drop — Argentina did not win it.

### Rows 1822, 1827, 1830 — FAIL: unsupported Monumental claims
- **1822:** "Monumental hosted 2022 qualifiers **before La Bombonera**" — false; Argentina's **opening**
  2022 qualifier (vs Ecuador) was at **La Bombonera**.
- **1827, 1830:** "Monumental hosted **multiple** 2022 qualifiers" — unsupported; several Argentina home
  qualifiers were relocated **away** from the Monumental (Venezuela moved off it; Colombia to Kempes), it
  was under renovation, and only the Uruguay game is clearly confirmed there (cf. rows 1299/1396/1472/1486).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Verify the Monumental's actual 2022-qualifier matches, or drop the "multiple/first" claims.

---

## Rows 1901–2010 (Argentina)

### Rows 1963, 1985, 2002 — FAIL: false (Argentina unbeaten in 2022 qualifying)
All claim Argentina's "only 2022 World Cup qualifying defeat" was a **2-0 loss to Brazil** (one cites
"Nov 2019"). Argentina were **unbeaten** in 2022 CONMEBOL qualifying (0 losses), and Nov 2019 predates
the campaign (it began Oct 2020); the Nov 2019 Brazil match was a **friendly** (lost 1-0). (cf. 1341/1342.)
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop — Argentina had no qualifying defeat. (Brazil did finish *ahead* of them, as rows 1960/2000 correctly say.)

### Rows 1904, 1950 — FAIL: wrong (2014 Fair Play Award)
Both credit Argentina with the **FIFA Fair Play Award at the 2014 World Cup**. It went to **Colombia**.
(Argentina's 2014 award was Messi's Golden Ball.) (cf. rows 1476/1849.)
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup
**Remedy:** Change the award to the Golden Ball, or drop.

### Rows 1905, 1930 — FAIL: wrong goal breakdown
Both say Messi scored **13** World Cup goals "across 2014, 2018, 2022." Those three total **12** (4+1+7);
the 13th was 2006. (cf. 1332/1333/1695.)
**Source:** https://en.wikipedia.org/wiki/Lionel_Messi
**Remedy:** Say 12 for 2014–2022, or include 2006.

### Row 1901 — FAIL: wrong year
**Q:** Which Argentine held the national caps record until 2022? **A:** Mascherano
**Why it fails:** Messi passed Mascherano on **29 June 2021**, so the record stood "until 2021," not 2022
(answer Mascherano is right). (cf. 1417/1666/1668/1873/1900.)
**Source:** https://en.wikipedia.org/wiki/Lionel_Messi
**Remedy:** Change 2022 → 2021.

### Row 1966 — FAIL: non-unique answer
**Q:** Which Copa América final did Argentina NOT win? **A:** 2016 Copa América
**Why it fails:** Argentina also lost the **2007** final (to Brazil) and the **2015** final (to Chile) —
both listed options — so three answers are valid.
**Source:** https://en.wikipedia.org/wiki/Argentina_national_football_team
**Remedy:** Leave only one not-won final among the options.

---

## Rows 2011–2160 (Argentina) — FINAL ARGENTINA BATCH

### Rows 2054, 2093, 2149 — FAIL: false (Argentina unbeaten in 2022 qualifying)
Repeat of the false "Argentina lost 2-0 to Brazil in 2022 qualifying (Nov 2019)" claim. Argentina were
**unbeaten** in 2022 CONMEBOL qualifying; Nov 2019 predates the campaign and was a friendly (lost 1-0).
(cf. 1341/1342/1963/1985/2002.) 2149 is a "why did they lose" question built on the non-event.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop — no qualifying defeat.

### Rows 2042, 2043, 2045, 2047, 2124 — FAIL: unsupported "Monumental hosted multiple 2022 qualifiers"
Same overstated/unverified claim as 1299/1396/1472/1486/1827/1830 — Argentina rotated venues and several
home qualifiers were moved away from the Monumental (which was under renovation).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Verify the Monumental's actual 2022-qualifier matches, or drop "multiple/primary."

### Rows 2096, 2097 — FAIL: false ("four goals in 23 minutes")
Germany's four 2010 QF goals came at 3', 67', 74', 89' (86-minute span), not "four in 23 minutes"
(cf. 1355/1361). Answer (Germany) is right; the timing detail is false.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_knockout_stage
**Remedy:** Drop the "23 minutes" detail.

### Row 2037 — FAIL: false premise (no Argentina–Brazil 2024 Copa match)
"Argentina beat Brazil 1-0 in the 2024 Copa América group stage" — they were in different groups and
never met (cf. 1276/1451/1455).
**Source:** https://en.wikipedia.org/wiki/2024_Copa_Am%C3%A9rica
**Remedy:** Drop.

### Row 2121 — FAIL: wrong (2014 Fair Play Award)
"Argentina won the FIFA Fair Play Award at the 2014 World Cup" — it went to **Colombia** (cf. 1476/1849/1904/1950).
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup
**Remedy:** Drop.

### Row 2110 — FAIL: fabricated name
**Q:** Which two Argentine legends assisted Scaloni at the 2022 World Cup? **A:** Matelán and Ayala
**Why it fails:** Scaloni's assistants were **Roberto Ayala, Walter Samuel, Pablo Aimar** (and Diego
Placente). There is no "Aníbal Matelán" on the staff — the name is fabricated.
**Source:** https://en.wikipedia.org/wiki/Lionel_Scaloni
**Remedy:** Replace with a real assistant (Samuel / Aimar).

### Rows 2082 — FAIL: non-unique answer
**Q:** Which team did NOT beat Argentina in a 2022 World Cup group match? **A:** Mexico
**Why it fails:** Argentina lost only to Saudi Arabia in the group; **Poland** (and Australia, a R16
opponent) also did not beat them in a group match — multiple valid options (cf. 1521).
**Source:** https://en.wikipedia.org/wiki/Argentina_at_the_2022_FIFA_World_Cup
**Remedy:** Leave only one not-beaten-by group opponent among the options.

### Row 2152 — FAIL: wrong figure
"Argentina scored **over 50 goals** in 2018 & 2022 qualifiers combined" — it was ~46 (cf. 1334/1529/1808).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Recompute (~46).

### Row 2160 — FAIL: built on unverified premise
**Q:** Why was Argentina ranked 5th for the 2018 World Cup? **A:** Poor qualifying results (E: "including a drop to **10th** in early 2018")
**Why it fails:** Rests on the unverified "10th in early 2018" claim (cf. 1248/1428/1429/1431/1613); and a
"poor campaign" wouldn't explain a high 5th-place ranking.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop the "10th" premise.

---

### Row 6097 — Brazil (hard) — FAIL
**Q:** After beating Argentina in the 2019 Copa América, when did Brazil next face them?
**Answer:** 2021 Copa América final
**Why it fails:** After the 2019 Copa semi-final (Brazil 2-0 Argentina), Brazil's NEXT meeting with Argentina was a friendly in Riyadh on 15 Nov 2019 (Argentina 1-0, Messi), not the 2021 Copa final. The answer ignores the intervening friendly.
**Source:** https://en.wikipedia.org/wiki/2019_Supercl%C3%A1sico_de_las_Am%C3%A9ricas
**Remedy:** Reword to 'next competitive meeting' (2021 Copa final) or change answer to the Nov 2019 friendly.

### Row 6102 — Brazil (easy) — FAIL
**Q:** After Brazil's 2019 Copa Libertadores win, which club did NOT spark a resurgence?
**Answer:** Corinthians
**Why it fails:** Non-unique: among the options, Santos also did NOT spark a post-2019 resurgence (no Libertadores since 2011), so 'Corinthians' is not the unique answer; Palmeiras (2020/21) and Flamengo (2019) both did.
**Source:** https://en.wikipedia.org/wiki/Copa_Libertadores
**Remedy:** Drop — negative-framed and non-unique.

### Row 6108 — Brazil (easy) — FAIL
**Q:** After scoring in Brazil's 5-1 win over Bolivia in September 2023, which player then surpassed Pelé's goal record?
**Answer:** Neymar
**Why it fails:** Explanation is wrong: Neymar EQUALED Pelé's 77 against Croatia at the 2022 World Cup, not against Bolivia; and he scored his 78th AND 79th in the SAME 5-1 Bolivia match (8 Sep 2023), not 'days later'.
**Source:** https://www.aljazeera.com/sports/2023/9/9/i-have-no-words-neymar-breaks-peles-brazil-goal-scoring-record
**Remedy:** Keep answer Neymar; rewrite explanation: 'Neymar scored twice against Bolivia on 8 Sep 2023 to pass Pelé's 77 and become Brazil's all-time top scorer.'

### Row 6119 — Brazil (medium) — FAIL
**Q:** Against which nation did Brazil draw 0-0 in the 2018 World Cup group stage?
**Answer:** Mexico
**Why it fails:** False premise: Brazil did NOT draw 0-0 with Mexico in the 2018 group stage (Mexico was not in Brazil's group). Brazil's only 2018 group draw was 1-1 v Switzerland; they beat Mexico 2-0 in the Round of 16.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_E
**Remedy:** Change answer to Switzerland and the score to 1-1, or drop.

### Row 6120 — Brazil (easy) — FAIL
**Q:** Against which nation did Brazil record a 0-0 draw and a 2-0 win at the 2018 World Cup?
**Answer:** Mexico
**Why it fails:** False premise: Brazil played Mexico only once at the 2018 World Cup (R16, won 2-0). There was no 0-0 group-stage draw with Mexico.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_E
**Remedy:** Drop — conflates a non-existent group game with the R16 win.

### Row 6122 — Brazil (easy) — FAIL
**Q:** Against which nation did Neymar equal Pelé's Brazil scoring record in September 2023?
**Answer:** Bolivia
**Why it fails:** Wrong: Neymar EQUALED Pelé's record (77) against Croatia at the 2022 World Cup, not against Bolivia. Against Bolivia (Sep 2023) he SURPASSED it with his 78th and 79th goals. The explanation's '77th vs Bolivia' is false.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Change answer to Croatia (and year 2022), or reframe the question to 'surpassed' → Bolivia.

### Row 6126 — Brazil (medium) — FAIL
**Q:** As of 2023, how many Copa Libertadores titles have Brazilian clubs won?
**Answer:** 24 titles
**Why it fails:** Wrong count: as of 2023 Brazilian clubs had won 23 Copa Libertadores titles (Fluminense's 2023 win was the 23rd). The figure '24' is reached only in 2024 (Botafogo); Brazil tied Argentina at 25 in 2025.
**Source:** https://en.wikipedia.org/wiki/Copa_Libertadores
**Remedy:** Change answer to 23 titles (as of 2023).

### Row 6147 — Brazil (medium) — FAIL
**Q:** At the 2022 World Cup in Qatar, Brazil scored how many total goals?
**Answer:** 15 goals
**Why it fails:** Wrong number: Brazil scored 8 goals at the 2022 World Cup (2 v Serbia, 1 v Switzerland, 0 v Cameroon, 4 v South Korea, 1 v Croatia), not 15.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Change answer to 8 goals.

### Row 6148 — Brazil (easy) — FAIL
**Q:** At the 2022 World Cup qualifiers, Brazil hosted matches at which stadium?
**Answer:** Arena Corinthians
**Why it fails:** Non-unique/ambiguous: Brazil hosted 2022 World Cup qualifiers at several stadiums (the explanation itself says 'multiple venues'), so 'Arena Corinthians' is not a uniquely correct single answer.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Anchor to a specific qualifier match/date, or drop.

### Row 6149 — Brazil (easy) — FAIL
**Q:** At the 2022 World Cup, Brazil beat South Korea by what score in the round of 16?
**Answer:** 04-Jan
**Why it fails:** Corrupted answer: '04-Jan' is an Excel-mangled '4-1'. Brazil beat South Korea 4-1 (as the explanation correctly states); the answer cell is unusable.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Fix the answer cell to '4-1' and flag a dataset-wide date-corruption sweep.

### Row 6150 — Brazil (medium) — FAIL
**Q:** At the 2022 World Cup, Brazil scored how many total goals?
**Answer:** 15 goals
**Why it fails:** Wrong number: Brazil scored 8 goals at the 2022 World Cup, not 15.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Change answer to 8 goals.

### Row 6157 — Brazil (easy) — FAIL
**Q:** At what age did Brazilian Endrick score in a World Cup qualifier?
**Answer:** 17 years old
**Why it fails:** False premise: Endrick's goals at age 17 were all friendlies (England and Spain, Mar 2024; Mexico, Jun 2024). He played 2026 WC qualifiers at 17 but did not score in one.
**Source:** https://en.wikipedia.org/wiki/Endrick_(footballer,_born_2006)
**Remedy:** Reword to 'friendly' (his England goal at 17), or drop.

### Row 6197 — Brazil (medium) — FAIL
**Q:** Brazil averaged how many goals per match at the 2022 World Cup?
**Answer:** 3 goals
**Why it fails:** False premise: Brazil scored 8 goals in 5 matches at 2022 (~1.6/match), not 15 → not 3 goals/match.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Recompute: 8 goals in 5 matches ≈ 1.6/match; reword or drop.

### Row 6212 — Brazil (medium) — FAIL
**Q:** Brazil dropped to 22nd in FIFA rankings in 2012. Which ranking did they NOT fall to?
**Answer:** 15th
**Why it fails:** Non-unique negative: Brazil fell to 22nd in 2012, so they did NOT fall to 15th — but they also did not fall to 18th, 20th or 25th. No unique answer.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men's_World_Ranking
**Remedy:** Drop — negative-framed and non-unique.

### Row 6242 — Brazil (easy) — FAIL
**Q:** Brazil lost to Belgium by what scoreline in the 2018 World Cup quarter-finals?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer: '02-Jan' is an Excel-mangled '2-1'. Brazil lost 2-1 to Belgium (as the explanation states); the answer cell is unusable.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2018_FIFA_World_Cup
**Remedy:** Fix the answer cell to '2-1' and flag a date-corruption sweep.

### Row 6243 — Brazil (easy) — FAIL
**Q:** Brazil prepared for the 2014 World Cup at which national team training centre in Teresópolis?
**Answer:** CBF Training Centre
**Why it fails:** Non-unique/TC-16: the distractor 'Granja Comary' is the SAME venue as the answer 'CBF Training Centre' (the explanation says so), so two options are correct.
**Source:** https://en.wikipedia.org/wiki/Brazil_national_football_team
**Remedy:** Replace 'Granja Comary' with a genuinely different distractor, or drop.

### Row 6244 — Brazil (medium) — FAIL
**Q:** Brazil reached the quarter-finals in how many World Cups from 2010 to 2022?
**Answer:** Three
**Why it fails:** Ambiguous/non-unique: Brazil REACHED the quarter-finals in all four 2010-2022 World Cups (in 2014 they advanced to the SF), so 'reached the QF' = four, not three. The intended count (eliminated AT the QF) is three, but the wording supports the 'Four' distractor too.
**Source:** https://en.wikipedia.org/wiki/Brazil_national_football_team
**Remedy:** Reword to 'eliminated in the quarter-finals' (as in row 6255).

### Row 6246 — Brazil (medium) — FAIL
**Q:** Brazil scored 15 goals in 5 matches at which FIFA World Cup?
**Answer:** 2022 World Cup
**Why it fails:** False premise: Brazil scored 8 goals at the 2022 World Cup, not 15.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Drop or correct the goal count to 8.

### Row 6247 — Brazil (hard) — FAIL
**Q:** Brazil scored 15 goals in 5 matches at which World Cup?
**Answer:** The 2022 World Cup
**Why it fails:** False premise: Brazil scored 8 goals at the 2022 World Cup, not 15.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Drop or correct the goal count to 8.

### Row 6248 — Brazil (medium) — FAIL
**Q:** Brazil scored 15 goals in how many matches at the 2022 World Cup?
**Answer:** 5 matches
**Why it fails:** False premise: the question asserts Brazil scored 15 goals at 2022 (the asked-for '5 matches' is right, but they scored 8, not 15).
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Drop — built on the false 15-goal figure.

### Row 6256 — Brazil (hard) — FAIL
**Q:** Brazil were FIFA's top-ranked team entering the 2022 World Cup. Which other nation also entered a World Cup as FIFA's #1?
**Answer:** Brazil in 2010
**Why it fails:** Non-unique: Germany also entered a World Cup (2018) ranked FIFA No.1, so the 'Germany in 2018' option is equally correct. Also self-referential (answer is Brazil again).
**Source:** https://en.wikipedia.org/wiki/FIFA_Men's_World_Ranking
**Remedy:** Drop — multiple correct options.

### Row 6265 — Brazil (easy) — FAIL
**Q:** Brazil's 2-0 win over Mexico in 2018 was in which World Cup stage?
**Answer:** Round of 16
**Why it fails:** Explanation is false: it claims Brazil drew Mexico 0-0 in the 2018 group stage, but Brazil never played Mexico in the group (only the R16, won 2-0). The R16 answer is right; the explanation tail is wrong.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_E
**Remedy:** Remove the false '0-0 group stage draw' clause.

### Row 6271 — Brazil (medium) — FAIL
**Q:** Brazil's 2018 World Cup knockout win over Mexico followed what group stage result?
**Answer:** A 0-0 draw
**Why it fails:** False premise: Brazil's R16 win over Mexico did NOT follow a 0-0 group draw — they never met Mexico in the 2018 group stage.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_E
**Remedy:** Drop — non-existent group game.

### Row 6277 — Brazil (medium) — FAIL
**Q:** Brazil's 2018 World Cup qualifying record under Tite was 12 wins, 5 draws, and how many defeats?
**Answer:** 0 defeats
**Why it fails:** Wrong record: Brazil's 2018 CONMEBOL campaign was 12W-5D-1L (41 pts) — one defeat (to Chile), not zero. The 12W/5D figures are the full-campaign totals, which include that loss.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change answer to 1 defeat.

### Row 6305 — Brazil (hard) — FAIL
**Q:** Brazil's main creative force Neymar was nominated for the Ballon d'Or in which years?
**Answer:** 2015 and 2017
**Why it fails:** Non-unique: Neymar received nine Ballon d'Or nominations (not just 2015 & 2017); his two PODIUM finishes were 2015 and 2017, but he was also nominated in 2014, 2016 and 2018, so the 'nominated in which years' framing has multiple correct options.
**Source:** https://en.wikipedia.org/wiki/Neymar
**Remedy:** Reword to 'finished 3rd in the Ballon d'Or' (2015 and 2017), or drop.

### Row 6316 — Brazil (medium) — FAIL
**Q:** Brazil's Neymar won the Bronze Ball in 2014 after scoring how many goals?
**Answer:** Four goals
**Why it fails:** False premise: Neymar did NOT win the 2014 World Cup Bronze Ball — that went to Arjen Robben (Golden Messi, Silver Müller). Neymar was injured before the semis. The '4 goals' is right, but he won no 2014 award.
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup_awards
**Remedy:** Drop the Bronze Ball claim; reword to his 4 goals before injury.

### Row 6320 — Brazil (medium) — FAIL
**Q:** Brazilian clubs had won the most Copa Libertadores titles of any country by 2023. How many?
**Answer:** 24 titles
**Why it fails:** Wrong count: Brazilian clubs had 23 Copa Libertadores titles as of 2023 (Fluminense's 2023 win = the 23rd), not 24.
**Source:** https://en.wikipedia.org/wiki/Copa_Libertadores
**Remedy:** Change answer to 23 titles.

### Row 6325 — Brazil (medium) — FAIL
**Q:** For Brazil's 2022 World Cup squad, how many different nations' club leagues were represented?
**Answer:** Six nations
**Why it fails:** Explanation wrong: the 2022 squad's sixth league was Mexico (Dani Alves at Pumas), NOT Germany — no 2022 Brazil player was Bundesliga-based. The count 'six' (England, Spain, France, Italy, Mexico, Brazil) is right, but the explanation lists Germany falsely.
**Source:** https://en.wikipedia.org/wiki/Template:Brazil_squad_2022_FIFA_World_Cup
**Remedy:** Replace 'Germany' with 'Mexico' in the explanation.

### Row 6339 — Brazil (medium) — FAIL
**Q:** From how many different national leagues were Brazil's 2022 World Cup squad players drawn?
**Answer:** Six
**Why it fails:** Explanation wrong: the sixth league was Mexico (Dani Alves/Pumas), not Germany. The count 'six' is correct but the listed nations are wrong.
**Source:** https://en.wikipedia.org/wiki/Template:Brazil_squad_2022_FIFA_World_Cup
**Remedy:** Replace 'Germany' with 'Mexico'.

### Row 6353 — Brazil (medium) — FAIL
**Q:** How many Copa Libertadores titles had Brazilian clubs won as of 2023?
**Answer:** 24 titles
**Why it fails:** Wrong count: Brazilian clubs had 23 Copa Libertadores titles as of 2023, not 24.
**Source:** https://en.wikipedia.org/wiki/Copa_Libertadores
**Remedy:** Change answer to 23 titles.

### Row 6357 — Brazil (medium) — FAIL
**Q:** How many goals did Brazil score at the 2022 FIFA World Cup?
**Answer:** 15 goals
**Why it fails:** Wrong number: Brazil scored 8 goals at the 2022 World Cup, not 15.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Change answer to 8 goals.

### Row 6358 — Brazil (medium) — FAIL
**Q:** How many goals did Brazil score in total at the 2022 World Cup?
**Answer:** 15 goals
**Why it fails:** Wrong number: Brazil scored 8 goals at the 2022 World Cup, not 15.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Change answer to 8 goals.

### Row 6363 — Brazil (medium) — FAIL
**Q:** How many goals did Brazil's Richarlison score at the 2022 FIFA World Cup?
**Answer:** 4
**Why it fails:** Wrong number: Richarlison scored 3 goals at the 2022 World Cup (2 v Serbia, 1 v South Korea), not 4.
**Source:** https://en.wikipedia.org/wiki/Richarlison
**Remedy:** Change answer to 3.

### Row 6391 — Brazil (easy) — FAIL
**Q:** In a 2022 World Cup qualifier, Brazil beat which South American rival 2-0 in Manaus?
**Answer:** Uruguay
**Why it fails:** Wrong score/venue: Brazil beat Uruguay 4-1 in Manaus (Oct 2021). The 2-0 win was away in Montevideo (Nov 2020), not Manaus.
**Source:** https://www.espn.com/soccer/report/_/gameId/561042
**Remedy:** Change answer/score to 4-1, or move the 2-0 to Montevideo.

### Row 6392 — Brazil (easy) — FAIL
**Q:** In a 2023 Brazil 5-1 win over Bolivia, which player scored his 77th goal to equal Pelé's record?
**Answer:** Neymar
**Why it fails:** False premise: Neymar EQUALED Pelé's 77 against Croatia (2022 WC). In the 2023 Bolivia 5-1 he scored his 78th and 79th to SURPASS the record — he did not score 'his 77th to equal Pelé' in that match.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed Pelé' or move the 'equal' to the Croatia game.

### Row 6412 — Brazil (medium) — FAIL
**Q:** In Brazil's 2022 World Cup squad, how many players were based in European leagues?
**Answer:** 26 players
**Why it fails:** Wrong number: of Brazil's 26-man 2022 squad, ~22 were European-league based — three were Brazil-based (Weverton, Pedro, Everton Ribeiro) and Dani Alves was in Mexico. Not all 26 were in Europe.
**Source:** https://en.wikipedia.org/wiki/Template:Brazil_squad_2022_FIFA_World_Cup
**Remedy:** Change answer to ~22, or reword to total squad size.

### Row 6413 — Brazil (medium) — FAIL
**Q:** In Brazil's 2022 World Cup squad, players' clubs were based in how many different countries?
**Answer:** Six countries
**Why it fails:** Explanation wrong: the six countries were England, Spain, France, Italy, Mexico (Dani Alves/Pumas) and Brazil — NOT Germany. The count 'six' is right but the listed nations are wrong.
**Source:** https://en.wikipedia.org/wiki/Template:Brazil_squad_2022_FIFA_World_Cup
**Remedy:** Replace 'Germany' with 'Mexico'.

### Row 6422 — Brazil (easy) — FAIL
**Q:** In the 2018 World Cup quarter-final, what score did Brazil lose by to Belgium?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer: '02-Jan' is a mangled '2-1'. Brazil lost 2-1 to Belgium (as the explanation states); the answer cell is unusable.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2018_FIFA_World_Cup
**Remedy:** Fix answer to '2-1'.

### Row 6428 — Brazil (easy) — FAIL
**Q:** In the 2022 World Cup qualifiers, Brazil beat which CONMEBOL rival 2-0 in Manaus?
**Answer:** Uruguay
**Why it fails:** Wrong score/venue: Brazil beat Uruguay 4-1 in Manaus (Oct 2021). The 2-0 win was away in Montevideo (Nov 2020).
**Source:** https://www.espn.com/soccer/report/_/gameId/561042
**Remedy:** Change score to 4-1, or relocate the 2-0 to Montevideo.

### Row 6429 — Brazil (easy) — FAIL
**Q:** In the 2022 World Cup qualifiers, which team did Brazil beat 2-0 in Manaus?
**Answer:** Uruguay
**Why it fails:** Wrong score: the Manaus qualifier v Uruguay was 4-1, not 2-0 (the 2-0 was in Montevideo).
**Source:** https://www.espn.com/soccer/report/_/gameId/561042
**Remedy:** Change score to 4-1.

### Row 6441 — Brazil (easy) — FAIL
**Q:** In which 2018 World Cup stage did Brazil first face Mexico?
**Answer:** Group stage
**Why it fails:** False premise: Brazil did NOT first face Mexico in the 2018 group stage — Mexico was not in Brazil's group. They met only in the R16 (Brazil won 2-0).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_E
**Remedy:** Drop — non-existent group meeting.

### Row 6450 — Brazil (medium) — FAIL
**Q:** In which Copa América did Brazil win their group but lose to Uruguay on penalties?
**Answer:** 2024 Copa América
**Why it fails:** False premise: Brazil did NOT win their 2024 Copa group — they finished 2nd in Group D behind Colombia (5 pts vs 7). They did lose to Uruguay on pens in the QF, but the group claim is wrong.
**Source:** https://en.wikipedia.org/wiki/2024_Copa_Am%C3%A9rica
**Remedy:** Reword to 'finished second in their group', or drop the group claim.

### Row 6456 — Brazil (medium) — FAIL
**Q:** In which month of 2023 did Neymar equal Pelé's Brazil goal record?
**Answer:** Sep-23
**Why it fails:** False premise: Neymar EQUALED Pelé's record in 2022 (v Croatia), not 2023 — so 'which month of 2023 did he equal it' is invalid; v Bolivia in Sept 2023 he surpassed it (78th/79th, not a 77th). (Answer 'Sep-23' also date-mangled.)
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed' → September 2023, or move 'equal' to 2022.

### Row 6468 — Brazil (medium) — FAIL
**Q:** In which World Cup did Brazil score 15 goals across 5 matches?
**Answer:** 2022 World Cup
**Why it fails:** Wrong number: Brazil scored 8 goals (not 15) in 5 matches at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Change to 8 goals.

### Row 6480 — Brazil (medium) — FAIL
**Q:** In which World Cup did Brazil's Neymar win the Bronze Ball award?
**Answer:** 2014 World Cup
**Why it fails:** False premise: Neymar did NOT win the 2014 Bronze Ball — Arjen Robben won it. Neymar was injured before the knockouts and won no 2014 award.
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup_awards
**Remedy:** Drop — false award claim.

### Row 6486 — Brazil (hard) — FAIL
**Q:** In which World Cup did Brazilian Neymar win the Bronze Ball?
**Answer:** 2014 FIFA World Cup
**Why it fails:** False premise: Neymar did not win the 2014 Bronze Ball (Robben did).
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup_awards
**Remedy:** Drop — false award claim.

### Row 6503 — Brazil (hard) — FAIL
**Q:** In which World Cup year did Brazil draw with Mexico in the group stage?
**Answer:** 2018
**Why it fails:** False premise: Brazil did NOT draw Mexico in the 2018 group stage (Mexico was not in their group). They met only in the R16.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_E
**Remedy:** Drop — non-existent group game.

### Row 6504 — Brazil (medium) — FAIL
**Q:** In which World Cup year did Brazil first draw 0-0 with Mexico before later beating them?
**Answer:** 2018
**Why it fails:** False premise: there was no 0-0 group draw with Mexico in 2018 — Brazil played Mexico only once (R16, won 2-0).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_E
**Remedy:** Drop — non-existent group game.

### Row 6522 — Brazil (medium) — FAIL
**Q:** In which year did Brazil beat Uruguay 2-0 in a World Cup qualifier in Manaus?
**Answer:** 2022
**Why it fails:** False premise: there was no Brazil 2-0 win over Uruguay in Manaus. Manaus (Oct 2021) was 4-1; the 2-0 was away in Montevideo (Nov 2020).
**Source:** https://www.espn.com/soccer/report/_/gameId/561042
**Remedy:** Correct the score to 4-1 (Manaus) or move the 2-0 to Montevideo.

### Row 6523 — Brazil (medium) — FAIL
**Q:** In which year did Brazil beat Uruguay 2-0 in World Cup qualifying?
**Answer:** 2022
**Why it fails:** False premise: the Manaus qualifier v Uruguay was 4-1, not 2-0 (the 2-0 was in Montevideo).
**Source:** https://www.espn.com/soccer/report/_/gameId/561042
**Remedy:** Correct the score/venue.

### Row 6538 — Brazil (medium) — FAIL
**Q:** In which year did Brazil score 15 goals in 5 World Cup matches?
**Answer:** 2022
**Why it fails:** Wrong number: Brazil scored 8 goals (not 15) in 5 matches at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Change to 8 goals.

### Row 6556 — Brazil (medium) — FAIL
**Q:** In which year did Endrick first join Brazil's senior World Cup squad?
**Answer:** 2024
**Why it fails:** Wrong year: Endrick's first senior call-up was November 2023 (debut 16 Nov 2023 v Colombia), not 2024.
**Source:** https://en.wikipedia.org/wiki/Endrick_(footballer,_born_2006)
**Remedy:** Change answer to 2023.

### Row 6557 — Brazil (medium) — FAIL
**Q:** In which year did Endrick receive his first Brazil senior call-up?
**Answer:** 2024
**Why it fails:** Wrong year: Endrick's first senior call-up was November 2023, not 2024.
**Source:** https://en.wikipedia.org/wiki/Endrick_(footballer,_born_2006)
**Remedy:** Change answer to 2023.

### Row 6568 — Brazil (hard) — FAIL
**Q:** In which years was Brazil's Neymar nominated for the Ballon d'Or?
**Answer:** 2015 and 2017
**Why it fails:** Non-unique: Neymar had nine Ballon d'Or nominations (incl. 2014, 2016, 2018), not just 2015 & 2017 — multiple option pairs are true. His PODIUM (3rd) finishes were 2015 and 2017.
**Source:** https://en.wikipedia.org/wiki/Neymar
**Remedy:** Reword to '3rd-place finishes', or drop.

### Row 6569 — Brazil (hard) — FAIL
**Q:** In which years was Brazilian star Neymar nominated for the Ballon d'Or?
**Answer:** 2015 and 2017
**Why it fails:** Non-unique: Neymar had nine Ballon d'Or nominations, so 'nominated in 2015 and 2017' is not the unique answer (he was also nominated in 2014, 2016, 2018).
**Source:** https://en.wikipedia.org/wiki/Neymar
**Remedy:** Reword to '3rd-place finishes', or drop.

### Row 6586 — Brazil (easy) — FAIL
**Q:** What was Brazil's average goals per match at the 2022 FIFA World Cup?
**Answer:** 3 goals
**Why it fails:** False premise: the '3 goals/match' figure rests on a false 15-goal total — Brazil scored 8 goals in 5 matches at 2022 (~1.6/match).
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Recompute from 8 goals.

### Row 6597 — Brazil (easy) — FAIL
**Q:** What was Brazil's scoreline against Uruguay in the 2022 World Cup qualifier in Manaus?
**Answer:** 2-0
**Why it fails:** Wrong score: the Manaus qualifier v Uruguay was 4-1, not 2-0 (the 2-0 was away in Montevideo).
**Source:** https://www.espn.com/soccer/report/_/gameId/561042
**Remedy:** Change score to 4-1.

### Row 6598 — Brazil (easy) — FAIL
**Q:** What was Brazil's scoreline in their 2014 World Cup semi-final loss to Germany?
**Answer:** 01-Jul
**Why it fails:** Corrupted answer: '01-Jul' is an Excel-mangled scoreline. Brazil lost 7-1 to Germany (per the explanation); the answer cell is unusable.
**Source:** https://en.wikipedia.org/wiki/Brazil_v_Germany_(2014_FIFA_World_Cup)
**Remedy:** Fix answer to '7-1' (loss).

### Row 6604 — Brazil (easy) — FAIL
**Q:** What was Brazil's winning score against South Korea in the 2022 World Cup round of 16?
**Answer:** 04-Jan
**Why it fails:** Corrupted answer: '04-Jan' is a mangled '4-1'. Brazil beat South Korea 4-1 (per the explanation); the answer cell is unusable.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Fix answer to '4-1'.

### Row 6607 — Brazil (medium) — FAIL
**Q:** What was the exact score when Brazil lost to Germany in the 2014 World Cup semi-final?
**Answer:** 07-Jan
**Why it fails:** Corrupted answer: '07-Jan' is a mangled '7-1'. Brazil lost 7-1 to Germany (per the explanation).
**Source:** https://en.wikipedia.org/wiki/Brazil_v_Germany_(2014_FIFA_World_Cup)
**Remedy:** Fix answer to '7-1'.

### Row 6610 — Brazil (easy) — FAIL
**Q:** What was the final score when Brazil beat South Korea in the 2022 World Cup round of 16?
**Answer:** 04-Jan
**Why it fails:** Corrupted answer: '04-Jan' is a mangled '4-1'. Brazil beat South Korea 4-1 (per the explanation).
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Fix answer to '4-1'.

### Row 6612 — Brazil (easy) — FAIL
**Q:** What was the final score when Brazil lost to Belgium in the 2018 World Cup quarter-final?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer: '02-Jan' is a mangled '2-1'. Brazil lost 2-1 to Belgium (per the explanation).
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2018_FIFA_World_Cup
**Remedy:** Fix answer to '2-1'.

### Row 6622 — Brazil (medium) — FAIL
**Q:** When did Brazil beat Uruguay 2-0 in a World Cup qualifier?
**Answer:** 2022
**Why it fails:** Explanation wrong: Brazil's 2-0 win over Uruguay was in Montevideo (Nov 2020), not Manaus (Manaus was 4-1).
**Source:** https://www.espn.com/soccer/report/_/gameId/561042
**Remedy:** Correct the venue to Montevideo, or the score to 4-1 for Manaus.

### Row 6623 — Brazil (medium) — FAIL
**Q:** When did Brazil beat Uruguay 2-0 in World Cup qualifiers in Manaus?
**Answer:** 2022
**Why it fails:** False premise: the Manaus qualifier v Uruguay was 4-1, not 2-0 (the 2-0 was in Montevideo).
**Source:** https://www.espn.com/soccer/report/_/gameId/561042
**Remedy:** Correct the score/venue.

### Row 6625 — Brazil (medium) — FAIL
**Q:** When did Brazil draw 0-0 with Mexico at the World Cup?
**Answer:** 2018 group stage
**Why it fails:** False premise: Brazil never drew 0-0 with Mexico at a World Cup — Mexico was not in their 2018 group; they met only in the R16 (Brazil won 2-0).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_E
**Remedy:** Drop — non-existent group game.

### Row 6648 — Brazil (medium) — FAIL
**Q:** When did Brazil score 15 goals in five World Cup matches?
**Answer:** 2022 World Cup
**Why it fails:** Wrong number: Brazil scored 8 goals (not 15) in 5 matches at 2022.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Change to 8 goals.

### Row 6675 — Brazil (medium) — FAIL
**Q:** When did Brazil's Neymar equal Pelé's national team goal record in 2023?
**Answer:** 08-Sep-23
**Why it fails:** False: Neymar EQUALED Pelé's 77 against Croatia (Dec 2022), not in 2023. The 8 Sep 2023 Bolivia match was where he SURPASSED it (78th/79th), not equaled with a 77th.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed', or move the 'equal' to the 2022 Croatia game.

### Row 6689 — Brazil (medium) — FAIL
**Q:** When did Brazilian forward Richarlison score 4 World Cup goals?
**Answer:** 2022
**Why it fails:** Wrong number: Richarlison scored 3 World Cup goals at 2022 (2 v Serbia, 1 v South Korea), not 4 — the premise is false.
**Source:** https://en.wikipedia.org/wiki/Richarlison
**Remedy:** Change to 3 goals.

### Row 6703 — Brazil (medium) — FAIL
**Q:** When did Neymar equal Pelé's Brazil scoring record in a 5-1 win over Bolivia?
**Answer:** 08-Sep-23
**Why it fails:** False: Neymar did NOT equal Pelé's record in the Bolivia match — he scored his 78th and 79th there to SURPASS it (he equaled at 77 v Croatia in 2022).
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed', or move 'equal' to the 2022 Croatia game.

### Row 6704 — Brazil (medium) — FAIL
**Q:** When did Neymar equal Pelé's Brazil scoring record in a World Cup qualifier?
**Answer:** 08-Sep-23
**Why it fails:** False: in the Bolivia qualifier Neymar surpassed (not equaled) Pelé — his 78th/79th. He equaled at 77 v Croatia in 2022.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 6705 — Brazil (medium) — FAIL
**Q:** When did Neymar first equal Pelé's Brazilian scoring record?
**Answer:** 08-Sep-23
**Why it fails:** False: Neymar FIRST equaled Pelé's record v Croatia (Dec 2022), not on 8 Sep 2023 (when he surpassed it).
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Change to the 2022 Croatia game for 'equal'.

### Row 6746 — Brazil (easy) — FAIL
**Q:** Which 2014 Brazil World Cup stadium had a larger capacity than Mineirão?
**Answer:** Arena Castelão
**Why it fails:** Non-unique: more than one option had a larger 2014 capacity than the Mineirão (~58k) — the Maracanã (~74k) and Arena Corinthians (~62k) also exceed it, so 'Arena Castelão' is not the unique answer.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup
**Remedy:** Drop — multiple larger venues among the options.

### Row 6752 — Brazil (medium) — FAIL
**Q:** Which 2018 World Cup group stage opponent did Brazil later beat 2-0 in the round of 16?
**Answer:** Mexico
**Why it fails:** False premise: Mexico was NOT a 2018 group-stage opponent of Brazil (their group was Switzerland/Costa Rica/Serbia). They met only in the R16. The explanation also repeats the false 0-0 group draw.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_E
**Remedy:** Reword: Mexico was an R16 opponent, not a group opponent.

## Australia (rows 2161–3241) — batch 2161–2240

### Row 2235 — FAIL: spreadsheet date-corruption
**Q:** Australia's 2015 Asian Cup final win over South Korea was by what score? **A:** `02-Jan`
**Why it fails:** `02-Jan` is a corrupted "2-1" (Australia won 2-1 AET).
**Source:** https://en.wikipedia.org/wiki/2015_AFC_Asian_Cup_Final
**Remedy:** Restore answer to "2-1".

### Row 2238 — FAIL: wrong year / false premise
**Q:** Australia's 2018 playoff win over Honduras followed which other AFC playoff success? **A:** 2010 vs Uruguay (E: "also qualified for 2010 via intercontinental playoff vs Uruguay")
**Why it fails:** Australia's Uruguay intercontinental playoff was for **2006** (Nov 2005, won on penalties), not 2010. They qualified for **2010 directly via AFC** — no playoff.
**Source:** https://en.wikipedia.org/wiki/2006_FIFA_World_Cup_qualification_(AFC%E2%80%93CONMEBOL_play-off)
**Remedy:** Change to "2006 vs Uruguay".

### Row 2168 — FAIL: wrong date for ranking
**Q:** After which FIFA World Cup did Australia reach 14th? **A:** After 2022 World Cup (E: "highest FIFA ranking 14th in April 2023")
**Why it fails:** Australia's all-time-high 14th ranking was **September 2009**, not after the 2022 WC. They peaked around 25th–27th after 2022.
**Source:** https://en.wikipedia.org/wiki/Australia_men%27s_national_soccer_team
**Remedy:** Remove the false 2022/April-2023 attribution.

### Row 2228 — FAIL: non-unique answer
**Q:** Australia qualified for 2010 via AFC. Which later tournament required an intercontinental playoff? **A:** 2022 World Cup **Options:** 2022 | 2014 | 2018 | 2026
**Why it fails:** Both **2018** (vs Honduras) and **2022** (vs Peru) required intercontinental playoffs, and 2018 is an option → two correct answers.
**Source:** https://en.wikipedia.org/wiki/Australia_men%27s_national_soccer_team
**Remedy:** Remove the 2018 distractor.

### Row 2216 — FAIL: undercount (stale + wrong)
**Q:** Australia in 2015 is one of how many AFC Asian Cup host nations to win the tournament? **A:** Four **Options:** Four | Two | Three | Five
**Why it fails:** Host nations that won at home: South Korea (1960), Israel (1964), Iran (1968 & 1976), **Kuwait (1980)**, Australia (2015) = **5 even at 2015**; Qatar (2023) makes **6 now**. "Four" omits Kuwait.
**Source:** https://en.wikipedia.org/wiki/AFC_Asian_Cup
**Remedy:** Correct the count (≥5).

### Row 2175 — FAIL: wrong (understated) stage
**Q:** At the 2011 Asian Cup, Australia reached which tournament stage? **A:** Semi-finals
**Why it fails:** Australia reached the **final** of the 2011 Asian Cup (lost 1-0 AET to Japan), not the semi-finals — "semi-finals" is not their furthest stage.
**Source:** https://en.wikipedia.org/wiki/2011_AFC_Asian_Cup
**Remedy:** Change to "final / runners-up".

### Row 2230 — FAIL: non-unique answer
**Q:** Australia reached the 2011 Asian Cup semi-finals. Which AFC nation did the same? **A:** South Korea **Options:** South Korea | Japan | Iran | Saudi Arabia
**Why it fails:** The 2011 semi-finalists were Japan, Australia, **South Korea AND Uzbekistan** — so both South Korea *and* Japan (both options) "did the same", giving two correct answers.
**Source:** https://en.wikipedia.org/wiki/2011_AFC_Asian_Cup
**Remedy:** Remove the Japan distractor (or re-scope).

### Rows 2170 vs 2196 — FAIL: wrong "first R16" (2196)
**Q (2196):** At which World Cup did Australia first reach the round of 16? **A:** 2022 World Cup
**Why it fails:** Australia first reached the R16 in **2006** (lost to Italy). 2022 was their *second* R16 — and their first **as an AFC nation** (which is the correct framing used by row 2170, kept as PASS). Unqualified "first R16 = 2022" is false.
**Source:** https://en.wikipedia.org/wiki/2006_FIFA_World_Cup
**Remedy:** Add the "as an AFC member" qualifier or change to 2006.

### Row 2227 — FAIL: AFC-join year ≠ first qualifier
**Q:** Australia played their first AFC World Cup qualifier in which year? **A:** 2006 **Options:** 2006 | 2002 | 2010 | 2014
**Why it fails:** Australia *joined* the AFC in 2006 but played their first AFC **World Cup qualifier** in **2008** (2010 campaign, 3rd round, Feb 2008). No option matches the true year; "2006" conflates membership with qualifying.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_(AFC)
**Remedy:** Fix to the actual qualifier year (2008) and option set.

### Row 2164 — FAIL: self-referential / incoherent
**Q:** After Australia's 2022 World Cup, which nation saw a similar football interest surge? **A:** Australia (E: "Australia's own 2022 success uniquely boosted domestic interest")
**Why it fails:** The question asks which *other* nation saw a *similar* surge; answering "Australia" is self-referential (the explanation even says "Australia's own"). No valid comparator.
**Source:** n/a (malformed question)
**Remedy:** Rewrite to name a genuine comparator nation, or drop.

---

## Australia — batch 2241–2320

### Rows 2307, 2315, 2317 — FAIL: spreadsheet date-corruption
- **2307:** 2010 vs Ghana scoreline `01-Jan` → "1-1".
- **2315:** 2015 Asian Cup final vs South Korea `02-Jan` → "2-1".
- **2317:** 2022 R16 vs Argentina `02-Jan` → "2-1".
**Source:** https://en.wikipedia.org/wiki/Australia_men%27s_national_soccer_team
**Remedy:** Restore real scorelines.

### Rows 2270, 2272, 2273 — FAIL: non-unique answer (direct AFC qualification)
**2270** opts 2026|2010|2014|2022; **2272** opts 2010|2006|2014|2026; **2273** opts 2026|2010|2014|2018.
**Why they fail:** Australia qualified **directly via AFC for 2010, 2014 and 2026** — so each question has ≥2 correct options (e.g. 2010 & 2014 & 2026 are all "direct AFC qualification").
**Source:** https://en.wikipedia.org/wiki/Australia_men%27s_national_soccer_team
**Remedy:** Re-scope so only one answer is correct.

### Rows 2259, 2261, 2303 — FAIL: wrong date for the 14th ranking
**2259** ("reached 14th during 2022 qualifying"), **2261** ("first reached 14th during 2006 cycle"), **2303** ("Australia's 14th was *in 2022*, higher than South Korea's 17th *in 2022*").
**Why they fail:** Australia's all-time-high 14th was **September 2009** (the 2010 cycle). South Korea's best ranking (17th) was **December 1998**, not 2022.
**Source:** https://en.wikipedia.org/wiki/Australia_men%27s_national_soccer_team
**Remedy:** Attribute the 14th to 2009 / 2010-cycle; fix the SK comparison.

### Row 2260 — FAIL: wrong cycle for the scoring record
**Q:** During which World Cup cycle did Australia's Tim Cahill become their all-time top scorer? **A:** 2018 qualification cycle
**Why it fails:** Cahill became Australia's all-time top scorer on **5 March 2014** (vs Ecuador), surpassing Damian Mori's 29 — i.e. the **2014** cycle, not 2018.
**Source:** https://en.wikipedia.org/wiki/List_of_international_goals_scored_by_Tim_Cahill
**Remedy:** Change to the 2014 cycle.

### Row 2289 — FAIL: stale undercount
**Q:** How many FIFA World Cups has Australia qualified for since joining AFC in 2006? **A:** Four (2010,2014,2018,2022)
**Why it fails:** Australia has since also qualified for **2026** → **five** AFC-era World Cups, not four.
**Source:** https://en.wikipedia.org/wiki/Australia_men%27s_national_soccer_team
**Remedy:** Update to five.

### Row 2255 — FAIL: non-unique / wrong framing
**Q:** Australia's six straight World Cups (2006-2026) matches which other AFC nation's streak? **A:** South Korea
**Why it fails:** **Japan** also qualified for all of 2006–2026, so the answer is non-unique; and South Korea's actual streak (every WC since 1986) is far longer than six, so it does not "match".
**Source:** https://en.wikipedia.org/wiki/Japan_national_football_team
**Remedy:** Remove ambiguity; no AFC side has a streak of *exactly* six.

### Row 2250 — FAIL: false premise ("2006 debut")
**Q:** Which World Cup followed Australia's 2006 debut? **A:** 2010 (E: "Australia's first World Cup was in 2006")
**Why it fails:** Australia's World Cup **debut was 1974** (West Germany); 2006 was their second appearance. The "2006 debut" premise is false.
**Source:** https://en.wikipedia.org/wiki/1974_FIFA_World_Cup
**Remedy:** Drop "debut" (or change year to 1974).

### Row 2314 — FAIL: answer contradicts the facts (and its own explanation)
**Q:** In the 2010 World Cup, which two nations did Australia lose to? **A:** Germany and Ghana
**Why it fails:** Australia **lost only to Germany (4-0)**; they **drew 1-1 with Ghana** (and beat Serbia 2-1). The explanation itself says "drew 1-1 with Ghana", contradicting the answer.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup
**Remedy:** Only Germany; the Ghana match was a draw.

### Row 2296 — FAIL: unverifiable precise figure
**Q:** How many players from Australia's 2022 World Cup squad returned for the 2023 Asian Cup? **A:** 10 players
**Why it fails:** The exact "10" cannot be verified from reliable sources; precise unverifiable counts are treated as FAIL (conservative).
**Source:** n/a (unverifiable)
**Remedy:** Verify against both squad lists or drop the precise number.

---

## Australia — batch 2321–2400

### Rows 2328, 2334 — FAIL: wrong venue / wrong cycle (AAMI Park)
**2328:** "Which 2022 WC qualifier did Australia host at Melbourne Rectangular Stadium? vs Saudi Arabia" — the 2022-cycle Australia v Saudi Arabia match (11 Nov 2021, 0-0) was at **CommBank Stadium, Sydney**, not AAMI Park.
**2334:** "First hosted a qualifier at AAMI Park in the 2018 cycle" — Australia's first WC qualifier at AAMI Park was **February 2012 (the 2014 cycle)**, vs Saudi Arabia.
**Source:** https://www.socceroos.com.au/news/our-previous-matches-aami-park
**Remedy:** Fix venue (2328 = Sydney) and cycle (2334 = 2014).

### Row 2360 — FAIL: wrong competition (friendly, not a qualifier)
**Q:** In which year did Australia host a 2018 World Cup qualifier at AAMI Park? **A:** 2016 (E: "vs Greece at AAMI Park, June 2016")
**Why it fails:** The June 2016 Australia–Greece matches were **friendlies**, not 2018 World Cup qualifiers. The explanation's premise is false.
**Source:** https://en.wikipedia.org/wiki/Australia_men%27s_national_soccer_team
**Remedy:** Replace with a genuine 2018-cycle qualifier (and correct year/opponent).

### Row 2340 — FAIL: player did not score
**Q:** In which World Cup did Australia's Ajdin Hrustic score? **A:** 2022 World Cup
**Why it fails:** Hrustic did **not** score at the 2022 World Cup finals. Australia's finals scorers were Duke (vs Tunisia), Leckie (vs Denmark), Goodwin (vs France) + an own goal vs Argentina. (Hrustic's notable goal was vs UAE in the June-2022 *qualifying* playoff, not the finals.)
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Remove the false scoring claim.

### Row 2342 — FAIL: first WC goal ≠ first international goal
**Q:** In which World Cup did Tim Cahill score his first international goal? **A:** 2006 World Cup
**Why it fails:** Cahill's **first international goal was 31 May 2004 vs Tahiti** (2004 OFC Nations Cup). 2006 was his first **World Cup** goal, not his first international goal.
**Source:** https://en.wikipedia.org/wiki/List_of_international_goals_scored_by_Tim_Cahill
**Remedy:** Change "international goal" to "World Cup goal".

### Rows 2376, 2377, 2381 — FAIL: stale undercount (now five)
All three answer "**Four**" WC qualifications since the 2006 AFC move (2010/2014/2018/2022). Australia has since also qualified for **2026** → **five**.
**Source:** https://en.wikipedia.org/wiki/Australia_men%27s_national_soccer_team
**Remedy:** Update to five.

### Row 2394 — FAIL: unverifiable precise figure
**Q:** What was Australia's average squad age at the 2022 World Cup? **A:** 26.8 years old
**Why it fails:** The precise "26.8" cannot be confirmed from reliable sources; conservative grading treats unverifiable precise stats as FAIL.
**Source:** n/a (unverifiable)
**Remedy:** Verify against the official squad list or drop the precise figure.

---

## Australia — batch 2401–2480

### Rows 2408, 2410, 2411, 2413 — FAIL: spreadsheet date-corruption
- **2408 / 2411:** 2015 Asian Cup final vs South Korea `02-Jan` → "2-1".
- **2410:** 2022 opener loss to France `04-Jan` → "4-1".
- **2413:** 2022 R16 loss to Argentina `02-Jan` → "2-1".
**Source:** https://en.wikipedia.org/wiki/Australia_men%27s_national_soccer_team
**Remedy:** Restore real scorelines.

### Rows 2429, 2432 — FAIL: wrong venue (AAMI Park / COVID relocations)
- **2429:** "Hosted a 2022 qualifier vs China at AAMI Park, Sep-2021" — the Sept-2021 window was played abroad; the Socceroos were **"763 days away from home" until Nov-2021** (first home game back was vs Saudi Arabia in Sydney). The China game was not at AAMI Park.
- **2432:** "Hosted Japan at AAMI Park during the 2022 cycle" — the 2022-cycle home match vs Japan (24 Mar 2022, Japan won 2-0) was in **Sydney**, not AAMI Park.
**Source:** https://www.espn.com/soccer/report?gameId=611253
**Remedy:** Correct the venues.

### Row 2426 — FAIL: not their first WC meeting
**Q:** When did Australia first play Chile at a FIFA World Cup? **A:** 2014
**Why it fails:** Australia first met Chile at the **1974 World Cup** (0-0 draw, group stage), not 2014.
**Source:** https://en.wikipedia.org/wiki/1974_FIFA_World_Cup
**Remedy:** Change to 1974.

### Row 2443 — FAIL: wrong year (qualified in 2013)
**Q:** When did Australia qualify for the 2014 World Cup through AFC qualification? **A:** 2014
**Why it fails:** Australia secured 2014 qualification on **18 June 2013** (1-0 vs Iraq). (Cf. row 2442, which correctly says 2013.)
**Source:** https://en.wikipedia.org/wiki/Australia_men%27s_national_soccer_team
**Remedy:** Change to 2013.

### Row 2451 — FAIL: wrong year (qualified in 2025)
**Q:** When did Australia qualify for the 2026 World Cup via AFC qualification? **A:** 2026 **Options:** 2026 | 2022 | 2018 | 2014
**Why it fails:** Australia secured 2026 qualification on **10 June 2025** (2-1 away at Saudi Arabia) — their first direct qualification since 2014. The answer year (and option set) is wrong; 2025 isn't even offered.
**Source:** https://www.espn.com/soccer/report/_/gameId/710521
**Remedy:** Change to 2025 and fix the options.

### Rows 2452, 2467, 2471 — FAIL: non-unique answer
**Q:** When did Australia reach the Asian Cup semi-finals? **A:** 2011 **Options:** 2011 | 2007 | 2015 | 2019
**Why they fail:** Australia reached the semi-finals in **both 2011 and 2015** (they won the 2015 edition, so passed through the SF), and 2015 is an option → two correct answers.
**Source:** https://en.wikipedia.org/wiki/2015_AFC_Asian_Cup
**Remedy:** Re-scope (e.g. "before 2015", as row 2435 correctly does).

---

## Australia — batch 2481–2560

### Row 2488 — FAIL: wrong (understated) finish
**Q:** Where did Australia finish in the 2011 Asian Cup? **A:** Semi-finals
**Why it fails:** Australia finished **runners-up** (reached the final, lost 1-0 AET to Japan), not the semi-finals.
**Source:** https://en.wikipedia.org/wiki/2011_AFC_Asian_Cup
**Remedy:** Change to "final / runners-up".

### Rows 2498, 2513 — FAIL: wrong about Mathew Leckie
- **2498:** "Which 2022 player is NOT in the 2026 squad? Leckie (retired after 2022)" — Leckie **never retired** ("I'll never retire from the national team") and **is named in Australia's 2026 World Cup squad** (his 4th WC). Premise false.
- **2513:** "Which A-League club did Leckie play for? Melbourne Victory" — Leckie played for **Melbourne City** (joined 2021), not Melbourne Victory.
**Source:** https://en.wikipedia.org/wiki/Mathew_Leckie
**Remedy:** 2498 = pick a player who actually left (e.g. a retiree); 2513 = Melbourne City.

### Row 2508 — FAIL: wrong player (2015 squad)
**Q:** Which 2022 World Cup scorer for Australia also won the 2015 Asian Cup? **A:** Craig Goodwin
**Why it fails:** Goodwin (debut July 2013, barely capped by 2015, not at the 2014 WC) was **not** in the 2015 Asian Cup-winning squad. The 2022 scorer who *did* win the 2015 Asian Cup is **Mathew Leckie** (he assisted the winning goal in the 2015 final).
**Source:** https://en.wikipedia.org/wiki/2015_AFC_Asian_Cup_squads
**Remedy:** Change answer to Mathew Leckie.

### Rows 2518, 2555 — FAIL: non-unique / "only other" false
- **2518:** "Which AFC nation also reached the 2022 R16 like Australia? Japan (the only other)" — **three** AFC sides reached the 2022 R16: Japan, **South Korea** and Australia. So "only other" is false and the answer is non-unique.
- **2555:** "Which AFC team matched Australia's R16 feat in 2010? South Korea" (opts incl Japan) — **both** South Korea and Japan reached the 2010 R16 → non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Re-scope so only one AFC side qualifies.

### Row 2536 — FAIL: wrong year / wrong host
**Q:** Which AFC nation, like Australia in 2015, last won the Asian Cup as host? **A:** Qatar (E: "Qatar won the 2019 Asian Cup as host")
**Why it fails:** The **2019** Asian Cup was hosted by the **UAE** — Qatar won it *away*. Qatar's host-and-win was the **2023** edition (played Jan 2024). The explanation is false.
**Source:** https://en.wikipedia.org/wiki/2019_AFC_Asian_Cup
**Remedy:** Fix to "Qatar, 2023".

### Row 2538 — FAIL: garbled / false premise
**Q:** Which AFC nation's 2022 World Cup qualifier was NOT hosted at Stadium Australia? **A:** Saudi Arabia (E: "Stadium Australia hosted qualifiers for Japan, South Korea and UAE, but not Saudi Arabia")
**Why it fails:** **South Korea and the UAE were not in Australia's 2022 qualifying group** (Group B: Australia, Japan, Saudi Arabia, China, Oman, Vietnam), so the explanation's premise is false.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(AFC)
**Remedy:** Rewrite around the actual Group B opponents.

---

## Australia — batch 2561–2640

### Rows 2626, 2627, 2628 — FAIL: player did not score (Hrustic, 2022 finals)
All three say Ajdin Hrustic scored at the 2022 World Cup. He did **not** score at the finals (Australia's scorers: Duke, Leckie, Goodwin + an own goal). Cf. row 2340.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Remove the false scoring claim.

### Row 2591 — FAIL: wrong timing / false premise
**Q:** Which Australia manager left his post before their 2018 World Cup qualifying campaign? **A:** Ange Postecoglou (E: "resigned in late 2017, before the final phase of 2018 qualification")
**Why it fails:** Postecoglou coached the **entire** 2018 qualifying campaign (incl. the Nov-2017 intercontinental playoff vs Honduras) and resigned **after** Australia had qualified — not before. (Van Marwijk then took the finals.)
**Source:** https://en.wikipedia.org/wiki/Ange_Postecoglou
**Remedy:** Rephrase to "left before the 2018 finals", or name a manager who actually left earlier.

### Row 2609 — FAIL: wrong manager (2014 qualification)
**Q:** Which Australia manager was in charge when they qualified for the 2014 World Cup? **A:** Ange Postecoglou
**Why it fails:** Australia secured 2014 qualification on **18 June 2013 under Holger Osieck**. Postecoglou was appointed in **October 2013**, after qualification. (Cf. row 2597, which correctly credits Osieck.)
**Source:** https://en.wikipedia.org/wiki/Australia_men%27s_national_soccer_team
**Remedy:** Change answer to Holger Osieck.

### Row 2637 — FAIL: wrong opponent/venue for debut
**Q:** Which Australia player debuted for the Socceroos at the 2018 World Cup in Melbourne? **A:** Daniel Arzani (E: "debuted vs Hungary at AAMI Park in 2018")
**Why it fails:** Arzani debuted on **1 June 2018 vs the Czech Republic** (as a sub, at a neutral pre-WC venue in Austria). His first goal — not debut — came vs Hungary, in **Budapest**, not AAMI Park / Melbourne.
**Source:** https://en.wikipedia.org/wiki/Daniel_Arzani
**Remedy:** Fix the opponent (Czech Republic) and venue.

---

## Australia — batch 2641–2720

### Rows 2652, 2662, 2673, 2697 — FAIL: that goal was an own goal, not Goodwin
All four credit Craig Goodwin with scoring against Argentina in the 2022 R16. Goodwin's shot deflected in off **Enzo Fernández and is officially an own goal** (77'). Goodwin's only 2022 goal was vs France. (2662 also wrongly says he scored in both the group stage and R16.)
**Source:** https://www.espn.com/soccer/report/_/gameId/633836
**Remedy:** Australia's R16 goal = Enzo Fernández own goal; Goodwin scored only vs France.

### Rows 2646, 2655 — FAIL: player did not score (Hrustic)
Both say Ajdin Hrustic scored at the 2022 World Cup; he did not (cf. 2340, 2626-2628).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Remove the false scoring claim.

### Row 2666 — FAIL: wrong player (2015 squad)
**Q:** Which Australia player scored in the 2022 World Cup and also won the 2015 Asian Cup? **A:** Craig Goodwin
**Why it fails:** Goodwin was not in the 2015 Asian Cup-winning squad; the correct answer is **Mathew Leckie** (cf. 2508).
**Source:** https://en.wikipedia.org/wiki/2015_AFC_Asian_Cup_squads
**Remedy:** Change to Mathew Leckie.

### Row 2679 — FAIL: wrong/overstated qualifying goal
**Q:** Which Australia player scored the decisive goal in their 2010 World Cup qualifier? **A:** Josh Kennedy (E: "vs Uzbekistan, secured 2010 qualification")
**Why it fails:** Kennedy's *decisive* qualification goal was the header vs **Iraq on 18 June 2013** (for 2014). His April-2009 goal vs Uzbekistan did not secure 2010 qualification (clinched later).
**Source:** https://en.wikipedia.org/wiki/Joshua_Kennedy
**Remedy:** Either change to the 2014 vs Iraq goal, or drop "decisive/secured".

### Row 2683 — FAIL: impossible venue
**Q:** Which Australia player scored the first World Cup goal at Stadium Australia? **A:** Tim Cahill (E: "3-1 win over Japan at the 2006 World Cup")
**Why it fails:** The **2006 World Cup was in Germany** (Cahill's goals vs Japan were in Kaiserslautern), not Stadium Australia (Sydney). The men's WC has never been played there.
**Source:** https://en.wikipedia.org/wiki/2006_FIFA_World_Cup
**Remedy:** Remove the false venue premise.

### Row 2696 — FAIL: saved, did not score
**Q:** Which Australia player scored the winning penalty against Peru in the 2022 playoff? **A:** Andrew Redmayne
**Why it fails:** Redmayne (the "grey wiggle") **saved** Alex Valera's penalty to win the shootout — he did not score the winning penalty.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(AFC%E2%80%93CONMEBOL_play-off)
**Remedy:** Change to "saved the decisive penalty".

---

## Australia — batch 2721–2800

### Rows 2765, 2767, 2768, 2756 — FAIL: Hrustic scoring claim
- **2765 / 2767:** "Hrustic scored at the 2022 World Cup" — he did not (cf. 2340, 2626-2628, 2646/2655).
- **2768:** "Hrustic scored at the 2022 WC and the 2023 Asian Cup" — false (no 2022 finals goal).
- **2756:** answer "Aaron Mooy didn't score" is fine, but the explanation claims "unlike **Hrustic, Irvine** and Leckie" — Hrustic and Irvine did **not** score at the 2022 WC; only Leckie did.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Remove the false scoring claims.

### Row 2721 — FAIL: fabricated squad member
**Q:** Which A-League club had a player in the 2022 World Cup squad? **A:** Western Sydney Wanderers (E: "WSW goalkeeper Lawrence Thomas")
**Why it fails:** Lawrence Thomas was **not** in Australia's 2022 squad (GKs were Ryan, Redmayne, Vukovic). No WSW player was in the squad.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_squads
**Remedy:** Use an A-League club that actually had a 2022 squad player (e.g. Central Coast Mariners — Kuol/Cummings).

### Row 2746 — FAIL: not his first-choice debut
**Q:** Which goalkeeper debuted as first-choice at the 2018 World Cup? **A:** Mat Ryan
**Why it fails:** Ryan was already Australia's first-choice keeper at the **2014 World Cup** (started all three games). 2018 was not his first-choice debut.
**Source:** https://en.wikipedia.org/wiki/Mathew_Ryan
**Remedy:** Change to 2014, or drop "debuted".

### Rows 2779, 2782 — FAIL: false premise (Irvine in 2018)
Both say Jackson Irvine was in the 2022 squad "but not in 2018". **Irvine was named in Australia's 2018 World Cup squad** in Russia.
**Source:** https://en.wikipedia.org/wiki/Jackson_Irvine
**Remedy:** Remove the "not in 2018" contrast.

### Row 2798 — FAIL: wrong debut venue
**Q:** Which player debuted for the Socceroos at AAMI Park before the 2018 World Cup? **A:** Daniel Arzani
**Why it fails:** Arzani debuted vs the **Czech Republic** at a neutral venue (Austria), not AAMI Park (cf. 2637).
**Source:** https://en.wikipedia.org/wiki/Daniel_Arzani
**Remedy:** Fix the venue/opponent.

### Row 2800 — FAIL: 2004 is not a World Cup year
**Q:** Which Australian player debuted internationally in a World Cup year? **A:** Tim Cahill (E: "debuted in 2004, a World Cup qualifying year")
**Why it fails:** Cahill debuted in **2004**, which is **not** a World Cup year (the WCs were 2002 and 2006). The explanation quietly swaps in "qualifying year", contradicting the question.
**Source:** https://en.wikipedia.org/wiki/Tim_Cahill
**Remedy:** Use a player who debuted in an actual WC year (2002/2006/…), or rephrase.

---

## Australia — batch 2801–2880

### Rows 2835, 2864 — FAIL: own goal, not Goodwin
Both credit Goodwin with scoring vs Argentina in the 2022 R16; that goal was an **Enzo Fernández own goal** (cf. 2652/2662/2673/2697).
**Source:** https://www.espn.com/soccer/report/_/gameId/633836
**Remedy:** Australia's R16 goal = own goal.

### Rows 2852, 2853 — FAIL: wrong tournament count for Cahill
- **2852:** explanation says Cahill's 5 WC goals came "across 2006, 2010, 2014 **and 2018**" — he scored **0 in 2018**.
- **2853:** "five World Cup goals in **four tournaments**" — Cahill scored in **three** (2006, 2010, 2014).
**Source:** https://en.wikipedia.org/wiki/Tim_Cahill
**Remedy:** Three tournaments (2006/2010/2014).

### Row 2806 — FAIL: wrong figure (Viduka)
**Q:** Which Australian player scored more World Cup goals than Mark Viduka? **A:** Tim Cahill (E: "Cahill 5, Viduka 2")
**Why it fails:** Mark Viduka scored **0** World Cup goals (no goals at the 2006 WC). The comparison still holds, but the stated "2" is false.
**Source:** https://en.wikipedia.org/wiki/Mark_Viduka
**Remedy:** Viduka = 0 WC goals.

### Row 2825 — FAIL: saved, did not score
**Q:** Which Australian player scored a crucial penalty against Peru in the 2022 playoff? **A:** Mathew Leckie (E: "scored the decisive penalty")
**Why it fails:** The decisive act was goalkeeper **Andrew Redmayne saving** Alex Valera's penalty (cf. 2696). Leckie did not score the decisive penalty.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(AFC%E2%80%93CONMEBOL_play-off)
**Remedy:** Redmayne, and he *saved* the decisive penalty.

---

## Australia — batch 2881–2960 (venue cluster)

### Rows 2932, 2933, 2940, 2941, 2945, 2946 — FAIL: Peru playoff was in Qatar
All claim the 2022 intercontinental playoff vs Peru was at an Australian stadium (Melbourne Rectangular / Stadium Australia). The single-leg AFC–CONMEBOL playoff was played on **13 June 2022 at Ahmad bin Ali Stadium, Al Rayyan, QATAR** (neutral venue) — not in Australia.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(AFC%E2%80%93CONMEBOL_play-off)
**Remedy:** Venue = Ahmad bin Ali Stadium, Qatar (or drop the "in Australia" premise).

### Rows 2934, 2948, 2950 — FAIL: wrong Australian venue (Saudi/Japan, 2022 cycle)
- **2934:** Saudi Arabia 2022 qualifier (11 Nov 2021) was at **CommBank Stadium, Sydney**, not AAMI Park.
- **2948 / 2950:** the 2022-cycle home match vs Japan (24 Mar 2022) was at **Stadium Australia, Sydney**, not AAMI Park.
**Source:** https://www.espn.com/soccer/report?gameId=611253
**Remedy:** Fix venues (Sydney, not AAMI Park).

### Row 2928 — FAIL: wrong venue (2015 Asian Cup QF)
**Q:** Which stadium hosted a 2015 Asian Cup quarter-final? **A:** Melbourne Rectangular Stadium (E: "Australia vs China QF")
**Why it fails:** The Australia–China QF (22 Jan 2015) was at **Brisbane Stadium** (~52,000), not AAMI Park.
**Source:** https://en.wikipedia.org/wiki/2015_AFC_Asian_Cup
**Remedy:** Brisbane Stadium.

### Row 2929 — FAIL: wrong venue (2017 Saudi qualifier)
**Q:** Which stadium hosted a 2017 World Cup qualifier? **A:** AAMI Park (E: "vs Saudi Arabia in 2017")
**Why it fails:** Australia 3-2 Saudi Arabia (8 June 2017) was at **Adelaide Oval**, not AAMI Park.
**Source:** https://www.espn.com/soccer/match/_/gameId/463999
**Remedy:** Adelaide Oval.

### Row 2953 — FAIL: 2023 Asian Cup was in Qatar
**Q:** Which Australian stadium hosts Socceroos matches for the 2023 Asian Cup? **A:** AAMI Park
**Why it fails:** The 2023 AFC Asian Cup (played Jan 2024) was hosted entirely by **Qatar**; no Australian stadium hosted those matches.
**Source:** https://en.wikipedia.org/wiki/2023_AFC_Asian_Cup
**Remedy:** Remove the false premise.

---

## Australia — batch 2961–3040

### Row 3011 — FAIL: wrong manager (2026 qualification)
**Q:** Which manager led Australia's 2026 World Cup qualification? **A:** Graham Arnold (E: "Arnold secured qualification for 2026")
**Why it fails:** Arnold **resigned in Sept 2024** mid-campaign; **Tony Popovic** took over and *secured* 2026 qualification (2-1 at Saudi Arabia, 10 June 2025).
**Source:** https://www.espn.com/soccer/report/_/gameId/710521
**Remedy:** Tony Popovic secured 2026 qualification.

### Row 3016 — FAIL: false premise (2014 qualification succeeded)
**Q:** Which manager led Australia's unsuccessful qualifying campaign for the 2014 World Cup? **A:** Holger Osieck (E: "the failed 2014 World Cup qualification attempt")
**Why it fails:** Australia **successfully qualified** for the 2014 World Cup under Osieck (clinched 18 June 2013 vs Iraq). It was not unsuccessful/failed.
**Source:** https://en.wikipedia.org/wiki/Australia_men%27s_national_soccer_team
**Remedy:** Remove "unsuccessful/failed".

### Row 2971 — FAIL: false premise ("2006 debut")
**Q:** Which Australian tournament win came after their 2006 World Cup debut? **A:** 2015 Asian Cup (E: "their first World Cup appearance in 2006")
**Why it fails:** Australia's World Cup **debut was 1974**, not 2006 (cf. 2250). The answer (2015) is fine, but the "2006 debut/first appearance" premise is false.
**Source:** https://en.wikipedia.org/wiki/1974_FIFA_World_Cup
**Remedy:** Drop "debut/first appearance".

### Row 2992 — FAIL: wrong timing (OFC / 2006)
**Q:** Which confederation did Australia leave before their 2006 World Cup qualification? **A:** OFC
**Why it fails:** Australia qualified for the 2006 World Cup **as an OFC member** (OFC route + Nov-2005 playoff vs Uruguay) and only joined the AFC in **January 2006** — i.e. *after* qualifying. They did not leave OFC before 2006 qualification. (Cf. row 2993, which correctly says they represented OFC in 2006 qualifying.)
**Source:** https://en.wikipedia.org/wiki/Australia_men%27s_national_soccer_team
**Remedy:** Fix the timing (left OFC after 2006 qualification).

---

## Australia — batch 3042–3140

### Rows 3093, 3095 — FAIL: Peru playoff was in Qatar
Both place the 2022 Peru playoff at "Stadium Australia, Sydney". It was at **Ahmad bin Ali Stadium, Al Rayyan, Qatar** (cf. 2932/2933/etc.; rows 3092 & 3098 get this right).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(AFC%E2%80%93CONMEBOL_play-off)
**Remedy:** Qatar venue.

### Row 3096 — FAIL: wrong venue (Saudi 2022)
**Q:** Which stadium hosted Australia's 2022 qualifier vs Saudi Arabia? **A:** Melbourne Rectangular Stadium
**Why it fails:** That match (11 Nov 2021) was at **CommBank Stadium, Sydney**, not AAMI Park.
**Source:** https://www.austadiums.com/sport/event/25664
**Remedy:** CommBank Stadium, Sydney.

### Rows 3083, 3100 — FAIL: wrong (understated) stage
Both ask which round/stage Australia *reached* at the 2011 Asian Cup, answering "semi-finals". They reached the **final** (runners-up) — the SF was not their furthest stage (cf. 2175/2488).
**Source:** https://en.wikipedia.org/wiki/2011_AFC_Asian_Cup
**Remedy:** Final / runners-up.

### Row 3049 — FAIL: wrong first opponent
**Q:** Which nation did Australia face first in their six consecutive World Cup runs? **A:** Brazil (E: "2006, first group match vs Brazil")
**Why it fails:** Australia's first 2006 group match was vs **Japan** (3-1 win, 12 June 2006). Brazil was their second match.
**Source:** https://en.wikipedia.org/wiki/2006_FIFA_World_Cup
**Remedy:** Japan.

### Row 3081 — FAIL: non-unique answer
**Q:** Which other World Cup did Australia also qualify for through AFC qualification? **A:** 2014 **Options:** 2014 | 2018 | 2022 | 2010
**Why it fails:** Both **2010 and 2014** were direct AFC qualifications (2018/2022 needed intercontinental playoffs), and 2010 is an option → two correct answers.
**Source:** https://en.wikipedia.org/wiki/Australia_men%27s_national_soccer_team
**Remedy:** Remove the 2010 option.

### Row 3097 — FAIL: no AFC qualifier in 2006
**Q:** Which stadium hosted Australia's first AFC World Cup qualifier in 2006? **A:** Sydney Football Stadium
**Why it fails:** Australia's first AFC World Cup **qualifier was in 2008** (2010 campaign); there was no AFC WC qualifier in 2006 (cf. 2227). The premise is false.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_(AFC)
**Remedy:** Fix to the actual 2008 qualifier/venue.

### Row 3124 — FAIL: false premise (South Korea)
**Q:** Which team did Australia beat in the 2022 World Cup group stage? **A:** Denmark (E: "Argentina, France, and **South Korea** all defeated Australia")
**Why it fails:** South Korea was **not** an Australia opponent at the 2022 WC (group D: France, Tunisia, Denmark; then Argentina in R16). The answer "Denmark" is correct, but the explanation is false.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Remove the South Korea claim.

---

## Australia — batch 3141–3241 (AUSTRALIA COMPLETE)

### Rows 3161, 3162, 3163 — FAIL: non-unique (direct AFC qualification)
**3161** (ans 2026, opts incl 2010 & 2014), **3162** (ans 2010, opts incl 2014), **3163** (ans 2014, opts incl 2026). Australia qualified **directly via AFC for 2010, 2014 and 2026** — each of these has ≥2 correct options. (Row 3164, scoped "before 2014", is fine.)
**Source:** https://en.wikipedia.org/wiki/Australia_men%27s_national_soccer_team
**Remedy:** Re-scope so exactly one answer is correct.

### Rows 3213, 3239 — FAIL: 2006 was an OFC qualification
Both claim Australia qualified for the 2006 World Cup *via the AFC*. They qualified through the **OFC** (+ Nov-2005 playoff vs Uruguay) and only joined the AFC in January 2006 (cf. 2993).
**Source:** https://en.wikipedia.org/wiki/2006_FIFA_World_Cup_qualification_(AFC%E2%80%93CONMEBOL_play-off)
**Remedy:** 2006 = OFC route.

### Rows 3155, 3156 — FAIL: drew Ghana, didn't lose
Both say Australia *lost to / was defeated by* "Germany and Ghana" in 2010. Australia **drew 1-1 with Ghana** (lost only to Germany 4-0; beat Serbia 2-1). (Cf. 2314; note row 3152 "eliminated by" with an accurate explanation is kept as PASS.)
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup
**Remedy:** Only Germany was a loss.

### Row 3150 — FAIL: Peru playoff was in Qatar
**Q:** Which two nations contested a 2022 qualifier at Stadium Australia? **A:** Australia and Peru
**Why it fails:** The Australia–Peru playoff was at **Ahmad bin Ali Stadium, Qatar**, not Stadium Australia.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(AFC%E2%80%93CONMEBOL_play-off)
**Remedy:** Qatar venue.

### Row 3159 — FAIL: non-unique "best finish"
**Q:** Which was Australia's best World Cup finish: 2006, 2010, 2014, or 2022? **A:** 2022
**Why it fails:** Australia reached the round of 16 in **both 2006 and 2022** (joint best), and 2006 is an option → two correct answers.
**Source:** https://en.wikipedia.org/wiki/2006_FIFA_World_Cup
**Remedy:** Remove the 2006 option, or accept "2006 & 2022".

### Row 3178 — FAIL: wrong year (qualified 2017)
**Q:** Which year did Australia qualify for the 2018 World Cup via an intercontinental playoff? **A:** 2018
**Why it fails:** Australia beat Honduras in the playoff in **November 2017** (cf. 2444/2445, correctly 2017).
**Source:** https://en.wikipedia.org/wiki/Australia_men%27s_national_soccer_team
**Remedy:** 2017.

---

## Rows 16572–17486 (Côte d'Ivoire) — 79 FAIL-liveness

### Row 16587 — Côte d'Ivoire (medium) — FAIL: false premise (not at 2018 WC)
**Q:** At the 2018 World Cup, when had Côte d'Ivoire last won the AFCON? **A:** 2015
**Options:** 2015 | 2012 | 2017 | 2019
**Why it fails:** Côte d'Ivoire did not qualify for the 2018 World Cup, so 'At the 2018 World Cup' asserts a tournament appearance that never happened. (Answer 2015 is itself correct as their last AFCON win before 2018.)
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to a real edition, e.g. 'As of 2018, when had Côte d'Ivoire last won the AFCON?' → 2015.

### Row 16614 — Côte d'Ivoire (easy) — FAIL: date corruption (02-Jan = 2-1)
**Q:** Côte d'Ivoire's 2023 AFCON final win over Nigeria was by what scoreline? **A:** 02-Jan
**Options:** 02-Jan | 1-0 | 3-1 | 2-0
**Why it fails:** Answer cell '02-Jan' is an Excel-mangled '2-1'. CIV beat Nigeria 2-1 in the 2023 final.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_final
**Remedy:** Restore answer to '2-1'.

### Row 16617 — Côte d'Ivoire (medium) — FAIL: non-unique (stadium predates 2022 WC too)
**Q:** Côte d'Ivoire's 60,000-seat Stade Alassane Ouattara was built before which World Cup? **A:** 2026 World Cup
**Options:** 2026 World Cup | 2022 World Cup | 2018 World Cup | 2014 World Cup
**Why it fails:** Stade Alassane Ouattara opened 3 Oct 2020, i.e. before BOTH the 2022 and 2026 World Cups — so distractor '2022 World Cup' is also a correct answer.
**Source:** https://en.wikipedia.org/wiki/Alassane_Ouattara_Stadium
**Remedy:** Reword to 'built for which 2023 tournament?' → 2023 AFCON, or drop the 2022 option.

### Row 16627 — Côte d'Ivoire (hard) — FAIL: non-unique (CAF qual also 2010/2014)
**Q:** For which FIFA World Cup did Côte d'Ivoire qualify through CAF qualification? **A:** The 2026 World Cup
**Options:** The 2026 World Cup | The 2010 World Cup | The 2014 World Cup | The 2018 World Cup
**Why it fails:** Côte d'Ivoire qualified via CAF for 2006, 2010, 2014 AND 2026; options 2010 and 2014 are therefore also correct.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Make it specific, e.g. 'For which World Cup did CIV first qualify via CAF?' → 2006 (not an option here).

### Row 16645 — Côte d'Ivoire (medium) — FAIL: wrong — first WC was 2006
**Q:** How many World Cups did Côte d'Ivoire qualify for via CAF by 2010? **A:** One
**Options:** One | Two | Three | Four
**Why it fails:** CIV's first World Cup was 2006 (qualified Oct 2005), not 2010. By 2010 they had qualified for two World Cups (2006 and 2010), not one; the explanation falsely calls 2010 their first.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Answer: Two. Or reword to 'How many WCs had CIV qualified for by 2006?' → One.

### Row 16648 — Côte d'Ivoire (medium) — FAIL: wrong/non-unique — not CAF's largest
**Q:** In 2023, which Côte d'Ivoire stadium built for the AFCON is that confederation's largest? **A:** Stade Alassane Ouattara
**Options:** Stade Alassane Ouattara | Stade Félix Houphouët-Boigny | Cairo International Stadium | Stade Olympique de Radès
**Why it fails:** Stade Alassane Ouattara (60,000) is the largest stadium in Côte d'Ivoire, but NOT the largest in CAF — Cairo International Stadium (~75,000), which is itself a listed option, is larger.
**Source:** https://en.wikipedia.org/wiki/Alassane_Ouattara_Stadium
**Remedy:** Reword to 'Côte d'Ivoire's largest stadium' and drop the CAF-largest claim, or remove the Cairo option.

### Row 16649 — Côte d'Ivoire (hard) — FAIL: false premise (not at 2022 WC)
**Q:** In a 2022 World Cup group stage match, Côte d'Ivoire's 2015 AFCON victory preceded it by how many years? **A:** 7 years
**Options:** 7 years | 8 years | 6 years | 9 years
**Why it fails:** CIV failed to qualify for the 2022 World Cup, so 'In a 2022 World Cup group stage match' references a match that never happened.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Drop — built on a non-existent 2022 appearance.

### Row 16650 — Côte d'Ivoire (easy) — FAIL: false premise (no 2022 WC squad)
**Q:** In Côte d'Ivoire's 2022 World Cup squad, which player was the key striker? **A:** Sébastien Haller
**Options:** Sébastien Haller | Franck Kessié | Simon Adingra | Wilfried Zaha
**Why it fails:** CIV did not qualify for the 2022 World Cup, so there was no '2022 World Cup squad'. (Haller is correctly their key striker otherwise.)
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON squad or the 2026 World Cup squad.

### Row 16654 — Côte d'Ivoire (hard) — FAIL: date corruption (09-Aug = 9-8)
**Q:** In the 2015 AFCON final, Côte d'Ivoire beat Ghana in a penalty shootout by what score? **A:** 09-Aug
**Options:** 09-Aug | 7-6 | 5-4 | 6-5
**Why it fails:** Answer cell '09-Aug' is a mangled '9-8'. CIV beat Ghana 9-8 on penalties in the 2015 AFCON final.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_Africa_Cup_of_Nations
**Remedy:** Restore answer to '9-8'.

### Row 16659 — Côte d'Ivoire (easy) — FAIL: date corruption (02-Jan = 2-1)
**Q:** In the 2023 AFCON final, what was Côte d'Ivoire's winning scoreline? **A:** 02-Jan
**Options:** 02-Jan | 1-0 | 3-2 | 2-0
**Why it fails:** Answer '02-Jan' is a mangled '2-1' (2023 final v Nigeria).
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_final
**Remedy:** Restore answer to '2-1'.

### Row 16660 — Côte d'Ivoire (medium) — FAIL: date corruption (02-Jan = 2-1)
**Q:** In the 2023 AFCON final, what was the exact score Côte d'Ivoire beat Nigeria by? **A:** 02-Jan
**Options:** 02-Jan | 1-0 | 3-2 | 2-0
**Why it fails:** Answer '02-Jan' is a mangled '2-1' (2023 final v Nigeria).
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_final
**Remedy:** Restore answer to '2-1'.

### Row 16661 — Côte d'Ivoire (easy) — FAIL: date corruption (02-Jan = 2-1)
**Q:** In the 2023 AFCON final, what was the final score when Côte d'Ivoire beat Nigeria? **A:** 02-Jan
**Options:** 02-Jan | 1-0 | 3-1 | 2-0
**Why it fails:** Answer '02-Jan' is a mangled '2-1' (2023 final v Nigeria).
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_final
**Remedy:** Restore answer to '2-1'.

### Row 16695 — Côte d'Ivoire (hard) — FAIL: non-unique (also out in groups 2010 & 2006)
**Q:** In which year were Côte d'Ivoire eliminated in the World Cup group stage? **A:** 2014
**Options:** 2014 | 2010 | 2018 | 2022
**Why it fails:** CIV were eliminated in the group stage in 2006, 2010 AND 2014; option 2010 is therefore also correct.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Remove the 2010 option, or ask 'last WC group-stage exit' → 2014.

### Row 16698 — Côte d'Ivoire (easy) — FAIL: date corruption (02-Jan = 2-1)
**Q:** What scoreline did Côte d'Ivoire achieve in the 2023 AFCON final? **A:** 02-Jan
**Options:** 02-Jan | 1-0 | 3-2 | 2-0
**Why it fails:** Answer '02-Jan' is a mangled '2-1' (2023 final v Nigeria).
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_final
**Remedy:** Restore answer to '2-1'.

### Row 16699 — Côte d'Ivoire (easy) — FAIL: date corruption (02-Jan = 2-1)
**Q:** What scoreline did Côte d'Ivoire beat Nigeria by in the 2023 AFCON final? **A:** 02-Jan
**Options:** 02-Jan | 1-0 | 3-1 | 2-0
**Why it fails:** Answer '02-Jan' is a mangled '2-1' (2023 final v Nigeria).
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_final
**Remedy:** Restore answer to '2-1'.

### Row 16700 — Côte d'Ivoire (easy) — FAIL: date corruption (02-Jan = 2-1)
**Q:** What was Côte d'Ivoire's winning score against Nigeria in the 2023 AFCON final? **A:** 02-Jan
**Options:** 02-Jan | 1-0 | 3-2 | 2-0
**Why it fails:** Answer '02-Jan' is a mangled '2-1' (2023 final v Nigeria).
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_final
**Remedy:** Restore answer to '2-1'.

### Row 16702 — Côte d'Ivoire (easy) — FAIL: date corruption (02-Jan = 2-1)
**Q:** What was the final score when Côte d'Ivoire won the 2023 AFCON final? **A:** 02-Jan
**Options:** 02-Jan | 1-0 | 3-1 | 2-0
**Why it fails:** Answer '02-Jan' is a mangled '2-1' (2023 final v Nigeria).
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_final
**Remedy:** Restore answer to '2-1'.

### Row 16738 — Côte d'Ivoire (easy) — FAIL: non-unique time reference
**Q:** When did Ivorian Didier Drogba set his 65-goal national record? **A:** Upon his retirement
**Options:** Upon his retirement | After the 2014 WC | Before the -2010 WC | During the 2015 AFCON
**Why it fails:** Answer 'Upon his retirement' and distractor 'After the 2014 WC' denote the same moment — Drogba retired right after the 2014 World Cup — so two options are equally correct.
**Source:** https://en.wikipedia.org/wiki/List_of_international_goals_scored_by_Didier_Drogba
**Remedy:** Drop the 'After the 2014 WC' option, or ask a concrete fact (e.g. how many goals → 65).

### Row 16761 — Côte d'Ivoire (easy) — FAIL: broken — no shared 2010/2014 opponent
**Q:** Which 2014 World Cup opponent did Côte d'Ivoire also face in 2010? **A:** Portugal
**Options:** Portugal | Colombia | Greece | North Korea
**Why it fails:** CIV's 2010 opponents (Brazil, Portugal, North Korea) and 2014 opponents (Colombia, Greece, Japan) have NO overlap, so no option can be a '2014 opponent also faced in 2010'. The answer Portugal was a 2010 opponent only — the explanation even admits 'not in 2014'.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Drop — the premise (a shared opponent) is false.

### Row 16764 — Côte d'Ivoire (hard) — FAIL: false premise (no 2022 WC squad)
**Q:** Which 2022 Côte d'Ivoire squad had many players from top European leagues? **A:** 2022 World Cup squad
**Options:** 2022 World Cup squad | 2021 Africa Cup squad | 2023 Africa Cup squad | 2014 World Cup squad
**Why it fails:** CIV failed to qualify for the 2022 World Cup, so there was no '2022 World Cup squad'.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON squad.

### Row 16783 — Côte d'Ivoire (medium) — FAIL: self-referential answer
**Q:** Which 2023 AFCON winner, like Côte d'Ivoire, nearly exited in the group stage? **A:** Côte d'Ivoire
**Options:** Côte d'Ivoire | Nigeria | Senegal | Algeria
**Why it fails:** The 2023 AFCON winner that nearly exited the group stage IS Côte d'Ivoire, so the question's answer is its own subject.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_final
**Remedy:** Drop — self-referential. Ask instead which stage they nearly exited (group stage).

### Row 16832 — Côte d'Ivoire (easy) — FAIL: non-unique (multiple 2010 CAF qualifiers)
**Q:** Which CAF nation qualified for the 2010 World Cup alongside Côte d'Ivoire? **A:** Ghana
**Options:** Ghana | Nigeria | Cameroon | Senegal
**Why it fails:** Ghana, Nigeria AND Cameroon all qualified for the 2010 World Cup alongside CIV — three of the four options are correct (only Senegal didn't).
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup
**Remedy:** Keep one CAF qualifier and replace the others with non-qualifiers, or ask for the host (South Africa).

### Row 16840 — Côte d'Ivoire (medium) — FAIL: non-unique (all options qualified for 2010)
**Q:** Which CAF team qualified for the 2010 FIFA World Cup through the same continental qualification as Côte d'Ivoire? **A:** Ghana
**Options:** Ghana | Nigeria | Cameroon | Algeria
**Why it fails:** Ghana, Nigeria, Cameroon AND Algeria all qualified for the 2010 World Cup — every option is correct.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup
**Remedy:** Replace three options with nations that missed 2010.

### Row 16846 — Côte d'Ivoire (easy) — FAIL: non-unique (all options missed 2018 & 2022)
**Q:** Which Côte d'Ivoire captain missed the 2018 and 2022 World Cups? **A:** Didier Drogba
**Options:** Didier Drogba | Yaya Touré | Salomon Kalou | Kolo Touré
**Why it fails:** CIV failed to qualify for both 2018 and 2022, so Drogba, Yaya Touré, Kalou and Kolo Touré all 'missed' them; several (Drogba, Yaya, Kolo) also captained the side, so the answer isn't unique.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Ask a specific, unique fact (e.g. captain at the 2010/2014 WC → Drogba).

### Row 16863 — Côte d'Ivoire (easy) — FAIL: false premise (no 2014 WC goal)
**Q:** Which Côte d'Ivoire legend scored his final World Cup goal in 2014? **A:** Didier Drogba
**Options:** Didier Drogba | Yaya Touré | Salomon Kalou | Gervinho
**Why it fails:** Drogba did NOT score at the 2014 World Cup (CIV's goals came from Bony and Gervinho). His final World Cup goal was in 2010 v Brazil.
**Source:** https://en.wikipedia.org/wiki/List_of_international_goals_scored_by_Didier_Drogba
**Remedy:** Answer: 2010. Or reword to 'final World Cup appearance in 2014'.

### Row 16867 — Côte d'Ivoire (easy) — FAIL: non-unique (two managers had no WC)
**Q:** Which Côte d'Ivoire manager did not lead them at a FIFA World Cup? **A:** Emerse Faé
**Options:** Emerse Faé | Patrice Beaumelle | Henri Michel | Sabri Lamouchi
**Why it fails:** Both Emerse Faé and Patrice Beaumelle managed CIV without ever leading them at a World Cup; meanwhile Henri Michel (2006) and Lamouchi (2014) did. Two options are correct.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_national_football_team
**Remedy:** Replace Beaumelle with a manager who did coach at a WC (e.g. Henri Michel is fine; swap in another WC coach).

### Row 16888 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Côte d'Ivoire midfielder provided key quality at the 2022 FIFA World Cup? **A:** Franck Kessié
**Options:** Franck Kessié | Sébastien Haller | Simon Adingra | Wilfried Zaha
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup match/squad/campaign for them. (Kessié was indeed a key CIV midfielder, but not at a 2022 World Cup.)
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup squad.

### Row 16890 — Côte d'Ivoire (medium) — FAIL: false premise (not at 2022 WC)
**Q:** Which Côte d'Ivoire midfielder provided key quality in their 2022 World Cup group stage? **A:** Franck Kessié
**Options:** Franck Kessié | Seko Fofana | Serge Aurier | Maxwel Cornet
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup match/squad/campaign for them. (Kessié was indeed a key CIV midfielder, but not at a 2022 World Cup.)
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup squad.

### Row 16892 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Côte d'Ivoire midfielder was a key figure at the 2022 FIFA World Cup? **A:** Franck Kessié
**Options:** Franck Kessié | Wilfried Zaha | Serge Aurier | Nicolas Pépé
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup match/squad/campaign for them. (Kessié was indeed a key CIV midfielder, but not at a 2022 World Cup.)
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup squad.

### Row 16899 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Côte d'Ivoire midfielder was a key quality provider at the 2022 World Cup? **A:** Franck Kessié
**Options:** Franck Kessié | Sébastien Haller | Simon Adingra | Wilfried Zaha
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup match/squad/campaign for them. (Kessié was indeed a key CIV midfielder, but not at a 2022 World Cup.)
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup squad.

### Row 16900 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Côte d'Ivoire midfielder was a key squad selection for the 2022 FIFA World Cup? **A:** Franck Kessié
**Options:** Franck Kessié | Sébastien Haller | Simon Adingra | Wilfried Zaha
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup match/squad/campaign for them. (Kessié was indeed a key CIV midfielder, but not at a 2022 World Cup.)
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup squad.

### Row 16907 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Côte d'Ivoire midfielder was key in their 2022 World Cup squad? **A:** Franck Kessié
**Options:** Franck Kessié | Wilfred Ndidi | Thomas Partey | Mohamed Elneny
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup match/squad/campaign for them. Also the distractors (Ndidi, Partey, Elneny) are non-Ivorian (TC-03).
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup squad.

### Row 16912 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Côte d'Ivoire player at the 2022 World Cup was not a midfielder? **A:** Sébastien Haller
**Options:** Sébastien Haller | Serge Aurier | Franck Kessié | Wilfried Zaha
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup match/squad/campaign for them. Haller is correctly a striker among midfielders, but the 2022 framing is invalid.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup squad.

### Row 16945 — Côte d'Ivoire (easy) — FAIL: false premise (no 2022 WC squad)
**Q:** Which Côte d'Ivoire player in the 2022 World Cup squad was from a top European league? **A:** Sébastien Haller
**Options:** Sébastien Haller | Sadio Mané | Mohamed Salah | Riyad Mahrez
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup match/squad/campaign for them. Distractors Mané/Salah/Mahrez are also non-Ivorian.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON squad; replace non-Ivorian distractors.

### Row 16947 — Côte d'Ivoire (easy) — FAIL: false premise (no 2022 WC squad)
**Q:** Which Côte d'Ivoire player in their 2022 World Cup squad was based in a top European league? **A:** Sébastien Haller
**Options:** Sébastien Haller | Wilfried Zaha | Jean Michaël Seri | Max Gradel
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup match/squad/campaign for them. The explanation's Dortmund detail can't rescue a non-existent 2022 squad.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON squad.

### Row 16950 — Côte d'Ivoire (easy) — FAIL: non-unique (all options missed 2018 & 2022)
**Q:** Which Côte d'Ivoire player missed the 2018 and 2022 FIFA World Cups? **A:** Didier Drogba
**Options:** Didier Drogba | Salomon Kalou | Yaya Touré | Wilfried Zaha
**Why it fails:** CIV failed to qualify for both 2018 and 2022, so Drogba, Kalou, Yaya Touré and Zaha all missed them — every option is correct.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Ask a unique fact, e.g. captain at the 2010/2014 WC (Drogba).

### Row 16952 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Côte d'Ivoire player provided midfield quality at the 2022 FIFA World Cup? **A:** Franck Kessié
**Options:** Franck Kessié | Sébastien Haller | Simon Adingra | Wilfried Zaha
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup match/squad/campaign for them. (Kessié was indeed a key CIV midfielder, but not at a 2022 World Cup.)
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup squad.

### Row 16954 — Côte d'Ivoire (easy) — FAIL: invalid edition / false premise (no 2023 men's WC)
**Q:** Which Côte d'Ivoire player provides midfield quality at the 2023 World Cup? **A:** Franck Kessié
**Options:** Franck Kessié | Sébastien Haller | Simon Adingra | Wilfried Zaha
**Why it fails:** There is no 2023 men's FIFA World Cup (2023 was the Women's edition), and CIV anyway weren't at a 2022/2023 men's WC.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_national_football_team
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup.

### Row 16973 — Côte d'Ivoire (easy) — FAIL: non-unique (two CIV players scored in the 2023 final)
**Q:** Which Côte d'Ivoire player scored in their 2023 AFCON final win? **A:** Sébastien Haller
**Options:** Sébastien Haller | Nicolas Pépé | Franck Kessié | Max Gradel
**Why it fails:** Both Sébastien Haller (81') AND Franck Kessié (62') scored in CIV's 2-1 win in the 2023 final; Kessié is a listed option, so two answers are correct.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_final
**Remedy:** Ask who scored the WINNING goal (Haller), or drop the Kessié option.

### Row 17023 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Côte d'Ivoire player's midfield quality was key for their 2022 World Cup squad? **A:** Franck Kessié
**Options:** Franck Kessié | Sébastien Haller | Simon Adingra | Yaya Touré
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup squad/match for them.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup (or to the real 2022 qualifying campaign).

### Row 17053 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Côte d'Ivoire striker featured in their 2022 World Cup squad? **A:** Sébastien Haller
**Options:** Sébastien Haller | Didier Drogba | Yaya Touré | Wilfried Zaha
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup squad/match for them.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup (or to the real 2022 qualifying campaign).

### Row 17071 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Côte d'Ivoire striker was their key attacker at the 2022 FIFA World Cup? **A:** Sébastien Haller
**Options:** Sébastien Haller | Wilfried Zaha | Nicolas Pépé | Max Gradel
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup squad/match for them.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup (or to the real 2022 qualifying campaign).

### Row 17072 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Côte d'Ivoire striker was their key attacking figure for the 2022 World Cup? **A:** Sébastien Haller
**Options:** Sébastien Haller | Wilfried Zaha | Nicolas Pépé | Jean-Philippe Krasso
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup squad/match for them.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup (or to the real 2022 qualifying campaign).

### Row 17073 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Côte d'Ivoire striker was their key attacking threat at the 2022 FIFA World Cup? **A:** Sébastien Haller
**Options:** Sébastien Haller | Wilfried Zaha | Nicolas Pépé | Maxwel Cornet
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup squad/match for them.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup (or to the real 2022 qualifying campaign).

### Row 17075 — Côte d'Ivoire (hard) — FAIL: non-unique / self-referential
**Q:** Which Côte d'Ivoire team nearly exited in the 2023 AFCON group stage? **A:** The 2023 champions
**Options:** The 2023 champions | The 2015 champions | The 2012 runners-up | The 2023 hosts
**Why it fails:** CIV were BOTH the 2023 AFCON champions AND the 2023 hosts, and both descriptions refer to the same side that nearly exited the group stage — so 'The 2023 champions' and 'The 2023 hosts' are both correct.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_final
**Remedy:** Drop one of the two CIV descriptors.

### Row 17078 — Côte d'Ivoire (easy) — FAIL: false premise (40 caps 'for the 2022 WC')
**Q:** Which Côte d'Ivoire winger had over 40 caps for the 2022 World Cup? **A:** Nicolas Pépé
**Options:** Nicolas Pépé | Simon Adingra | Franck Kessié | Sébastien Haller
**Why it fails:** Pépé does have 40+ caps (53), but 'for the 2022 World Cup' anchors to a tournament CIV did not reach.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor: '...by the 2023 AFCON' or 'in 2022 World Cup qualifying'.

### Row 17112 — Côte d'Ivoire (easy) — FAIL: non-unique (several Ivorian Ligue 1 clubs)
**Q:** Which Ivorian club features in the country's top domestic Ligue 1? **A:** ASEC Mimosas
**Options:** ASEC Mimosas | Africa Sports | Stade d'Abidjan | SC Gagnoa
**Why it fails:** ASEC Mimosas, Africa Sports, Stade d'Abidjan and SC Gagnoa are ALL Ivorian Ligue 1 clubs, so 'which features in Ligue 1' has multiple correct answers.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_national_football_team
**Remedy:** Ask 'most Ligue 1 titles' (ASEC Mimosas) to make it unique.

### Row 17113 — Côte d'Ivoire (easy) — FAIL: non-unique (several Ivorian Ligue 1 clubs)
**Q:** Which Ivorian club features in the top domestic Ligue 1? **A:** ASEC Mimosas
**Options:** ASEC Mimosas | Africa Sports | Stade d'Abidjan | SC Gagnoa
**Why it fails:** All four options are Ivorian Ligue 1 clubs, so the answer isn't unique.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_national_football_team
**Remedy:** Ask 'most Ligue 1 titles' (ASEC Mimosas).

### Row 17128 — Côte d'Ivoire (easy) — FAIL: wrong — Gasset selected the 2023 squad
**Q:** Which Ivorian manager selected the squad for the 2023 AFCON as hosts? **A:** Emerse Faé
**Options:** Emerse Faé | Sven-Göran Eriksson | Sabri Lamouchi | Patrice Beaumelle
**Why it fails:** The AFCON-2023 squad was named by Jean-Louis Gasset; Emerse Faé was his assistant and only took charge after matchday 3 (Gasset sacked). Faé did not select the squad, and Gasset isn't even an option.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_final
**Remedy:** Reword to 'managed CIV to the 2023 AFCON title' (Faé), or add Gasset as the squad-selector answer.

### Row 17134 — Côte d'Ivoire (easy) — FAIL: non-unique (Henri Michel also pre-2014)
**Q:** Which Ivorian manager's World Cup appearance came before Sabri Lamouchi's in 2014? **A:** Sven-Göran Eriksson
**Options:** Sven-Göran Eriksson | Henri Michel | Patrice Beaumelle | Hervé Renard
**Why it fails:** Both Sven-Göran Eriksson (2010) AND Henri Michel (2006) coached CIV at a World Cup before Lamouchi (2014); Henri Michel is a listed option.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Remove the Henri Michel option, or specify the 2010 edition.

### Row 17142 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Ivorian midfielder was a key player at the 2022 FIFA World Cup? **A:** Franck Kessié
**Options:** Franck Kessié | Thomas Partey | Ismaël Bennacer | André-Frank Zambo Anguissa
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup squad/match for them.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup (or to the real 2022 qualifying campaign).

### Row 17145 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Ivorian midfielder was included for his quality in the 2022 World Cup squad? **A:** Franck Kessié
**Options:** Franck Kessié | Seko Fofana | Ibrahim Sangaré | Jean Michaël Seri
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup squad/match for them.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup (or to the real 2022 qualifying campaign).

### Row 17149 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Ivorian midfielder was key in their 2022 World Cup squad? **A:** Franck Kessié
**Options:** Franck Kessié | Sébastien Haller | Simon Adingra | Wilfried Zaha
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup squad/match for them.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup (or to the real 2022 qualifying campaign).

### Row 17152 — Côte d'Ivoire (easy) — FAIL: wrong — Yaya's first WC was 2006
**Q:** Which Ivorian midfielder's first FIFA World Cup was in 2010? **A:** Yaya Touré
**Options:** Yaya Touré | Franck Kessié | Nicolas Pépé | Sébastien Haller
**Why it fails:** Yaya Touré's first World Cup was 2006 (he was in CIV's debut squad), not 2010, so the explanation is false.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Answer: 2006. Or ask who was key 'at the 2010 WC' without the 'first' claim.

### Row 17165 — Côte d'Ivoire (easy) — FAIL: non-unique (Kessié also scored 2023 final)
**Q:** Which Ivorian player scored in the 2023 AFCON final against Nigeria? **A:** Sébastien Haller
**Options:** Sébastien Haller | Nicolas Pépé | Franck Kessié | Wilfried Zaha
**Why it fails:** Both Haller (81') and Kessié (62') scored in the 2023 final; Kessié is a listed option.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_final
**Remedy:** Ask for the winning goal (Haller) or drop the Kessié option.

### Row 17169 — Côte d'Ivoire (easy) — FAIL: non-unique (Kessié also scored 2023 final)
**Q:** Which Ivorian player scored in the 2023 Africa Cup of Nations final? **A:** Sébastien Haller
**Options:** Sébastien Haller | Nicolas Pépé | Franck Kessié | Wilfried Zaha
**Why it fails:** Both Haller and Kessié scored in the 2-1 final; Kessié is a listed option.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_final
**Remedy:** Ask for the winning goal (Haller) or drop the Kessié option.

### Row 17213 — Côte d'Ivoire (easy) — FAIL: false premise (no 2014 WC goal)
**Q:** Which Ivorian striker cried after scoring at the 2014 FIFA World Cup? **A:** Didier Drogba
**Options:** Didier Drogba | Salomon Kalou | Yaya Touré | Gervinho
**Why it fails:** Drogba did NOT score at the 2014 World Cup, so he couldn't have 'cried after scoring' there. CIV's 2014 goals came from Bony and Gervinho.
**Source:** https://en.wikipedia.org/wiki/List_of_international_goals_scored_by_Didier_Drogba
**Remedy:** Drop the 'after scoring' clause, or re-anchor to 2010 (he scored v Brazil).

### Row 17216 — Côte d'Ivoire (easy) — FAIL: false premise (final WC goal was 2010)
**Q:** Which Ivorian striker scored his final World Cup goal in 2014? **A:** Didier Drogba
**Options:** Didier Drogba | Wilfried Zaha | Salomon Kalou | Gervinho
**Why it fails:** Drogba's final World Cup goal was in 2010 (v Brazil); he didn't score at the 2014 World Cup.
**Source:** https://en.wikipedia.org/wiki/List_of_international_goals_scored_by_Didier_Drogba
**Remedy:** Answer: 2010.

### Row 17221 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Ivorian striker was the key attacker for the 2022 FIFA World Cup squad? **A:** Sébastien Haller
**Options:** Sébastien Haller | Wilfried Zaha | Nicolas Pépé | Jean-Philippe Krasso
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup squad/match for them.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup.

### Row 17222 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Ivorian striker was the key forward at the 2022 FIFA World Cup? **A:** Sébastien Haller
**Options:** Sébastien Haller | Wilfried Zaha | Nicolas Pépé | Maxwel Cornet
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup squad/match for them.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup.

### Row 17225 — Côte d'Ivoire (easy) — FAIL: false anchor (CIV not at 2022 WC)
**Q:** Which Ivorian winger had over 40 caps by the 2022 World Cup? **A:** Nicolas Pépé
**Options:** Nicolas Pépé | Wilfried Zaha | Maxwel Cornet | Jérémie Boga
**Why it fails:** Pépé does have 40+ caps (53), but 'by the 2022 World Cup' anchors an Ivorian fact to a tournament CIV didn't reach.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor: '...by the 2023 AFCON' or 'in 2022 World Cup qualifying'.

### Row 17229 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which Ivorian winger was a key starter for Côte d'Ivoire at the 2022 FIFA World Cup? **A:** Nicolas Pépé
**Options:** Nicolas Pépé | Simon Adingra | Sébastien Haller | Franck Kessié
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup squad/match for them.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup.

### Row 17242 — Côte d'Ivoire (easy) — FAIL: non-unique (Kessié also scored 2023 final)
**Q:** Which Ivory Coast player scored in the 2023 AFCON final? **A:** Sébastien Haller
**Options:** Sébastien Haller | Wilfried Zaha | Franck Kessié | Nicolas Pépé
**Why it fails:** Both Haller and Kessié scored in the 2-1 final; Kessié is a listed option.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_final
**Remedy:** Ask for the winning goal (Haller) or drop the Kessié option.

### Row 17246 — Côte d'Ivoire (easy) — FAIL: non-unique (3 managers didn't coach 2010)
**Q:** Which manager did not coach Côte d'Ivoire at the 2010 World Cup? **A:** Sabri Lamouchi
**Options:** Sabri Lamouchi | Sven-Göran Eriksson | Vahid Halilhodžić | Hervé Renard
**Why it fails:** Only Eriksson coached CIV at the 2010 WC, so Lamouchi, Halilhodžić AND Renard all 'did not' — three correct answers to a negatively-framed question.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Ask positively: who DID coach at 2010 (Eriksson).

### Row 17248 — Côte d'Ivoire (easy) — FAIL: non-unique (none of the 4 led AFCON as hosts)
**Q:** Which manager did NOT lead Côte d'Ivoire to an AFCON title as hosts? **A:** Sabri Lamouchi
**Options:** Sabri Lamouchi | Hervé Renard | François Zahoui | Patrice Beaumelle
**Why it fails:** Only Emerse Faé led CIV to an AFCON title as hosts; all four options (Lamouchi, Renard, Zahoui, Beaumelle) 'did not', so every option is correct.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_final
**Remedy:** Ask positively: who DID (Faé).

### Row 17333 — Côte d'Ivoire (easy) — FAIL: wrong — Zambia were 2012 champions
**Q:** Which nation, like Côte d'Ivoire in 2012, were AFCON runners-up on penalties? **A:** Zambia
**Options:** Zambia | Nigeria | Ghana | Egypt
**Why it fails:** Zambia WON the 2012 AFCON final on penalties; they were not runners-up like CIV. The answer contradicts the premise (it should name a different nation that finished runner-up on penalties).
**Source:** https://en.wikipedia.org/wiki/2012_Africa_Cup_of_Nations_Final
**Remedy:** Drop — Zambia were champions; pick an actual penalty-shootout runner-up, or rephrase to 'who beat CIV on penalties' (Zambia).

### Row 17334 — Côte d'Ivoire (easy) — FAIL: non-unique (Chile also missed 2018 & 2022)
**Q:** Which nation, like Côte d'Ivoire, missed the 2018 and 2022 World Cups? **A:** Italy
**Options:** Italy | Netherlands | Chile | Ghana
**Why it fails:** Both Italy AND Chile failed to qualify for the 2018 and 2022 World Cups; Chile is a listed option, so two answers are correct.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Replace Chile with a nation that made one of those tournaments.

### Row 17351 — Côte d'Ivoire (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which player provided midfield quality for Côte d'Ivoire's 2022 World Cup squad? **A:** Franck Kessié
**Options:** Franck Kessié | Serge Aurier | Maxwel Cornet | Jean Michaël Seri
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup squad/match for them.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup.

### Row 17375 — Côte d'Ivoire (easy) — FAIL: non-unique (two teams not lost to)
**Q:** Which team did Côte d'Ivoire not lose to at the 2014 World Cup? **A:** Japan
**Options:** Japan | Colombia | Greece | Costa Rica
**Why it fails:** CIV beat Japan and never played Costa Rica, so they 'did not lose to' BOTH — two correct options.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Replace Costa Rica with another team CIV lost to, or restrict to actual group opponents.

### Row 17376 — Côte d'Ivoire (medium) — FAIL: non-unique (two teams not lost to)
**Q:** Which team did Côte d'Ivoire not lose to in the 2014 World Cup group stage? **A:** Japan
**Options:** Japan | Colombia | Greece | Uruguay
**Why it fails:** CIV beat Japan and never played Uruguay (Uruguay wasn't in Group C), so both are teams they 'did not lose to'.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Replace Uruguay with a team CIV actually lost to.

### Row 17401 — Côte d'Ivoire (medium) — FAIL: flawed/non-unique (three CAF quals after 2008)
**Q:** Which two World Cups did Côte d'Ivoire qualify for through CAF after 2008? **A:** 2014 and 2026
**Options:** 2014 and 2026 | 2010 and 2014 | 2010 and 2026 | 2018 and 2022
**Why it fails:** CIV qualified via CAF for 2010, 2014 AND 2026 after 2008 — three, not two — so the distractor '2010 and 2014' is also a correct pair and the answer arbitrarily omits 2010.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Ask for all qualifications, or fix the time anchor.

### Row 17406 — Côte d'Ivoire (hard) — FAIL: non-unique (CAF qual also 2010/2014)
**Q:** Which World Cup did Côte d'Ivoire qualify for through CAF qualification? **A:** 2026 World Cup
**Options:** 2026 World Cup | 2010 World Cup | 2014 World Cup | 2018 World Cup
**Why it fails:** CIV qualified via CAF for 2010, 2014 AND 2026; options 2010 and 2014 are also correct.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Make it specific (first CAF qualification → 2006).

### Row 17409 — Côte d'Ivoire (medium) — FAIL: non-unique (CAF qual also 2010/2014)
**Q:** Which World Cup did the Côte d'Ivoire team qualify for via CAF? **A:** 2026
**Options:** 2026 | 2010 | 2014 | 2018
**Why it fails:** CIV qualified via CAF for 2010, 2014 AND 2026; options 2010 and 2014 are also correct.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Make it specific.

### Row 17411 — Côte d'Ivoire (hard) — FAIL: wrong — ignores 2006 (it's the 4th)
**Q:** Which World Cup was Côte d'Ivoire's third CAF qualification after 2010 and 2014? **A:** 2026 World Cup
**Options:** 2026 World Cup | 2018 World Cup | 2022 World Cup | 2030 World Cup
**Why it fails:** CIV's first World Cup (2006) was also a CAF qualification, so 2026 is their 4th CAF qualification, not the 3rd; the explanation falsely lists only 2010/2014/2026.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Answer reframed: 2026 is the most recent (4th) CAF qualification, counting 2006.

### Row 17412 — Côte d'Ivoire (medium) — FAIL: wrong — ignores 2006 (it's the 4th)
**Q:** Which World Cup was the third Côte d'Ivoire qualified for via CAF? **A:** 2026 World Cup
**Options:** 2026 World Cup | 2010 World Cup | 2014 World Cup | 2018 World Cup
**Why it fails:** 2006 (their debut) was also a CAF qualification, so the CAF set is 2006/2010/2014/2026 and 2026 is the 4th, not the 3rd.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Count 2006; 2026 is the 4th.

### Row 17448 — Côte d'Ivoire (easy) — FAIL: false premise (no 2022 WC squad)
**Q:** Who provided midfield quality for Côte d'Ivoire's 2022 World Cup squad? **A:** Franck Kessié
**Options:** Franck Kessié | Sébastien Haller | Simon Adingra | Wilfried Zaha
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup squad for them.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup squad.

### Row 17471 — Côte d'Ivoire (easy) — FAIL: false premise (no 2022 WC squad)
**Q:** Why did Côte d'Ivoire's 2022 World Cup squad have strong depth? **A:** Top European league players
**Options:** Top European league players | Excellent youth academy | Strong domestic league | Experienced African-based core
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup squad for them.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup squad.

### Row 17472 — Côte d'Ivoire (easy) — FAIL: false premise (no 2022 WC squad)
**Q:** Why did Côte d'Ivoire's 2022 World Cup squad have such high quality? **A:** Top European league players
**Options:** Top European league players | Excellent youth academy graduates | Long-term domestic league focus | Veteran African-based core
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup squad for them.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup squad.

### Row 17484 — Côte d'Ivoire (easy) — FAIL: false premise (no 2022 WC squad)
**Q:** Why was the 2022 Côte d'Ivoire World Cup squad considered strong? **A:** Top European league players
**Options:** Top European league players | Experienced domestic players | Top African league players | Strong youth academy products
**Why it fails:** false premise — CIV did not qualify for the 2022 World Cup, so there was no 2022 World Cup squad for them.
**Source:** https://en.wikipedia.org/wiki/Ivory_Coast_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2023 AFCON or 2026 World Cup squad.

## Rows 17487–19101 (Croatia) — 154 FAIL-liveness

Recurring Croatia defect clusters: (1) **false 2023 Nations League 'win'** — Croatia LOST the final to Spain (beat the Netherlands only in the semi); (2) **fabricated 2010 playoff loss to Ukraine** — Croatia missed 2010 by finishing 3rd, no playoff; (3) **'lost to Cameroon' in 2014** — they beat Cameroon 4-0; (4) **Euro 2024 'beat Albania / lost to Italy'** — both were draws, only loss was Spain; (5) **Gvardiol 2022 Best Young Player** — that was Enzo Fernández; (6) **Modrić age/caps** (37 at 2022 not 39; ~160 caps not 175+); (7) date/formation corruption (`02-Jan`=2-1, `04/03/2003`=4-3-3); (8) 'only team to win all 3 groups in 2018' (Belgium & Uruguay also did).

### Row 17497 — Croatia (medium) — FAIL: wrong — Croatia lost the 2023 NL final
**Q:** After reaching the Euro 2020 last 16, when did Croatia next win a UEFA trophy? **A:** 2023
**Options:** 2023 | 2021 | 2022 | 2024
**Why it fails:** Croatia did NOT win a UEFA trophy in 2023 — they LOST the 2022–23 Nations League final to Spain on penalties (0–0, 5–4). They have never won a senior UEFA trophy.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Drop — Croatia were NL runners-up; they have no UEFA title.

### Row 17502 — Croatia (easy) — FAIL: date corruption (03-Mar = 3-3)
**Q:** After trailing 3-1, what score did Croatia equalise to against Spain at Euro 2020? **A:** 03-Mar
**Options:** 03-Mar | 2-2 | 4-4 | 5-5
**Why it fails:** Answer '03-Mar' is a mangled '3-3' (Croatia equalised to 3-3 v Spain at Euro 2020).
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Restore answer to '3-3'.

### Row 17507 — Croatia (hard) — FAIL: date corruption (03-Jan = 3-1)
**Q:** At Euro 2008, Croatia lost a quarter-final penalty shootout by what score? **A:** 03-Jan
**Options:** 03-Jan | 2-1 | 4-2 | 5-3
**Why it fails:** Answer '03-Jan' is a mangled '3-1' (lost 3-1 on pens to Türkiye, Euro 2008).
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Restore answer to '3-1'.

### Row 17516 — Croatia (easy) — FAIL: non-unique + wrong explanation
**Q:** At Euro 2020, Croatia lost 5-3 to Spain. Which nation did Croatia NOT face in a Euro knockout match? **A:** Netherlands
**Options:** Netherlands | Portugal | Türkiye | Italy
**Why it fails:** Croatia have NOT faced Italy in a Euro knockout match either (only group meetings), so both 'Netherlands' AND 'Italy' are correct; the explanation falsely claims an Italy knockout meeting.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Replace Italy with a team Croatia did meet in a Euro knockout.

### Row 17517 — Croatia (easy) — FAIL: date corruption (03-Mar = 3-3)
**Q:** At Euro 2020, Croatia's Mislav Oršić scored to make it what score vs Spain? **A:** 03-Mar
**Options:** 03-Mar | 2-2 | 4-4 | 1-1
**Why it fails:** Answer '03-Mar' is a mangled '3-3' (Oršić levelled it 3-3 v Spain, Euro 2020).
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Restore answer to '3-3'.

### Row 17539 — Croatia (easy) — FAIL: non-unique (Modrić also fits)
**Q:** At the 2022 World Cup, which Croatia midfielder provided experience and quality? **A:** Mateo Kovačić
**Options:** Mateo Kovačić | Luka Modrić | Marcelo Brozović | Lovro Majer
**Why it fails:** 'Midfielder who provided experience and quality' applies at least as much to Luka Modrić (the captain, a listed option) as to Kovačić.
**Source:** https://en.wikipedia.org/wiki/Croatia_national_football_team
**Remedy:** Make it specific (e.g. the Chelsea/Man City midfielder Kovačić), or drop Modrić.

### Row 17554 — Croatia (medium) — FAIL: wrong — Enzo Fernández won 2022 BYP
**Q:** At which FIFA World Cup did Croatian defender Joško Gvardiol win the Best Young Player award? **A:** 2022 World Cup
**Options:** 2022 World Cup | 2018 World Cup | 2014 World Cup | 2010 World Cup
**Why it fails:** The 2022 World Cup Best Young Player was Enzo Fernández (Argentina), not Joško Gvardiol.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Drop — Gvardiol did not win the award (re-anchor to Modrić's Bronze Ball).

### Row 17560 — Croatia (medium) — FAIL: wrong explanation (not the only team)
**Q:** At which World Cup did Croatia win all three group matches? **A:** 2018 World Cup
**Options:** 2018 World Cup | 2014 World Cup | 2022 World Cup | 2010 World Cup
**Why it fails:** Croatia did win all three 2018 group games, but the explanation's 'the only team to do so' is false — Belgium also won all three group matches in 2018.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Remove 'the only team to do so'.

### Row 17569 — Croatia (hard) — FAIL: false premise (beat Cameroon 4-0)
**Q:** At which World Cup was Croatia eliminated in the group stage by Brazil, Mexico, and Cameroon? **A:** 2014 FIFA World Cup
**Options:** 2014 FIFA World Cup | 2010 FIFA World Cup | 2018 FIFA World Cup | 2022 FIFA World Cup
**Why it fails:** Croatia did NOT lose to Cameroon in 2014 — they beat Cameroon 4-0 (their biggest WC win); they lost only to Brazil and Mexico.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_2014_FIFA_World_Cup
**Remedy:** List Brazil and Mexico as the teams that beat them, not Cameroon.

### Row 17579 — Croatia (medium) — FAIL: false premise (lost the 2018 final)
**Q:** Croatia beat Argentina 3-0 in the 2018 World Cup group stage. Which nation did they then defeat in the final? **A:** France
**Options:** France | Brazil | England | Spain
**Why it fails:** Croatia LOST the 2018 final to France 4-2 — they did not 'defeat' anyone in the final.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_final
**Remedy:** Reword to 'lost the final to' France.

### Row 17581 — Croatia (hard) — FAIL: non-unique (all four went to ET)
**Q:** Croatia beat Brazil on penalties in the 2022 World Cup quarter-final. Which other World Cup knockout win also went to extra time? **A:** Beat England 2018
**Options:** Beat England 2018 | Beat Japan 2022 | Beat Denmark 2018 | Beat Russia 2018
**Why it fails:** Croatia's wins over Denmark (R16), Russia (QF) and England (SF) in 2018 AND over Japan (R16) in 2022 all went to extra time — every option is a correct 'other knockout win that went to ET'.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Keep one ET win and replace the rest with non-ET results.

### Row 17584 — Croatia (easy) — FAIL: wrong/non-unique (no 2010 playoff v Ukraine)
**Q:** Croatia beat Greece 4-1 in a 2018 World Cup playoff. Which team did they NOT beat in a UEFA playoff? **A:** Ukraine
**Options:** Ukraine | Iceland | Greece | Sweden
**Why it fails:** Croatia never played a 2010 WC playoff against Ukraine (they finished 3rd in their group and missed out without a playoff). Both 'Ukraine' and 'Sweden' are teams Croatia never beat in a WC playoff, so the answer isn't unique and the explanation is fabricated.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Croatia's only WC playoffs were 2014 (Iceland) and 2018 (Greece), both won — rebuild the options around that.

### Row 17585 — Croatia (hard) — FAIL: date corruption (04-Jan = 4-1)
**Q:** Croatia beat Greece in a 2018 World Cup playoff by what aggregate score? **A:** 04-Jan
**Options:** 04-Jan | 3-1 | 2-0 | 5-2
**Why it fails:** Answer '04-Jan' is a mangled '4-1' (beat Greece 4-1 on aggregate, 2018 playoff).
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Restore answer to '4-1'.

### Row 17591 — Croatia (easy) — FAIL: wrong — lost 2023 NL final to Spain
**Q:** Croatia beat which nation in the 2023 Nations League final? **A:** the Netherlands
**Options:** the Netherlands | Portugal | Spain | Italy
**Why it fails:** Croatia did NOT beat the Netherlands in the 2023 Nations League final — they beat the Netherlands in the SEMI-final (4-2 AET) and then LOST the final to Spain on penalties.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Answer: they reached the final but lost to Spain; they beat the Netherlands in the semi-final.

### Row 17596 — Croatia (hard) — FAIL: false premise (no Euro 2020 shootout)
**Q:** Croatia lost 3-1 on penalties at Euro 2008. What was their penalty shootout score at Euro 2020? **A:** 05-Mar
**Options:** 05-Mar | 3-1 | 1-0 | 4-2
**Why it fails:** Croatia's Euro 2020 loss to Spain was 5-3 after extra time, NOT a penalty shootout, so there was no shootout score; '05-Mar' is also a mangled '5-3'.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Drop — no penalty shootout occurred; the 5-3 was in extra time.

### Row 17608 — Croatia (hard) — FAIL: false premise (beat Cameroon 4-0)
**Q:** Croatia lost to Brazil, Mexico, and Cameroon in which FIFA World Cup group stage? **A:** 2014 FIFA World Cup
**Options:** 2014 FIFA World Cup | 2010 FIFA World Cup | 2018 FIFA World Cup | 2022 FIFA World Cup
**Why it fails:** Croatia beat Cameroon 4-0 in 2014; they lost only to Brazil and Mexico.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_2014_FIFA_World_Cup
**Remedy:** List Brazil and Mexico, not Cameroon.

### Row 17609 — Croatia (easy) — FAIL: date corruption (04-Feb = 4-2)
**Q:** Croatia lost to France by what score in the 2018 World Cup final? **A:** 04-Feb
**Options:** 04-Feb | 3-1 | 2-0 | 1-0
**Why it fails:** Answer '04-Feb' is a mangled '4-2' (lost the 2018 final 4-2 to France).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_final
**Remedy:** Restore answer to '4-2'.

### Row 17620 — Croatia (easy) — FAIL: wrong — NL final was v Spain (lost)
**Q:** Croatia won the 2022-23 Nations League final against which nation? **A:** the Netherlands
**Options:** the Netherlands | Spain | Italy | Portugal
**Why it fails:** Croatia did NOT win the 2022–23 Nations League — they beat the Netherlands in the SEMI-final (4-2 AET) and then LOST the FINAL to Spain on penalties (0-0, 5-4). The 'final win over the Netherlands' framing conflates the semi-final with the final and reverses the result.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Croatia beat the Netherlands in the semi-final, then lost the final to Spain.

### Row 17621 — Croatia (easy) — FAIL: wrong — NL final was v Spain (lost)
**Q:** Croatia won the 2022-23 Nations League final by beating which team? **A:** Netherlands
**Options:** Netherlands | Portugal | Spain | Italy
**Why it fails:** Croatia did NOT win the 2022–23 Nations League — they beat the Netherlands in the SEMI-final (4-2 AET) and then LOST the FINAL to Spain on penalties (0-0, 5-4). The 'final win over the Netherlands' framing conflates the semi-final with the final and reverses the result.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 17623 — Croatia (easy) — FAIL: fabricated — no 2010 playoff v Ukraine
**Q:** Croatia's 2010 World Cup exit was sealed by a playoff loss to which nation? **A:** Ukraine
**Options:** Ukraine | Greece | Iceland | Turkey
**Why it fails:** Croatia did not lose a 2010 World Cup qualifying playoff to Ukraine — they finished 3rd in their group (behind England and Ukraine) and missed the playoff entirely. The 'playoff loss to Ukraine' is invented.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Drop — Croatia simply finished 3rd in qualifying; there was no playoff.

### Row 17637 — Croatia (easy) — FAIL: wrong — 0-0 was the final v Spain
**Q:** Croatia's 2022-23 Nations League final win over the Netherlands ended with what score? **A:** 0-0
**Options:** 0-0 | 1-0 | 2-1 | 3-2
**Why it fails:** Croatia did NOT win the 2022–23 Nations League — they beat the Netherlands in the SEMI-final (4-2 AET) and then LOST the FINAL to Spain on penalties (0-0, 5-4). The 'final win over the Netherlands' framing conflates the semi-final with the final and reverses the result.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** The 0-0 (lost on pens) was the final v Spain; the Netherlands game was the 4-2 AET semi-final.

### Row 17660 — Croatia (medium) — FAIL: wrong — not their first group win
**Q:** For which World Cup did Croatia first win their UEFA qualifying group? **A:** 2022 World Cup
**Options:** 2022 World Cup | 2018 World Cup | 2014 World Cup | 2010 World Cup
**Why it fails:** Croatia had already won UEFA qualifying groups for 2002 and 2006; 2022 was not their first group win.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Drop the 'first' claim, or ask which recent WC they qualified for by topping the group.

### Row 17714 — Croatia (easy) — FAIL: date corruption (03-Mar = 3-3)
**Q:** In Croatia's 5-3 Euro 2020 loss to Spain, what score did they equalise to? **A:** 03-Mar
**Options:** 03-Mar | 2-2 | 4-4 | 1-1
**Why it fails:** Answer '03-Mar' is a mangled '3-3' (Croatia equalised to 3-3 v Spain, Euro 2020).
**Source:** https://en.wikipedia.org/wiki/Croatia_national_football_team
**Remedy:** Restore answer to '3-3'.

### Row 17727 — Croatia (easy) — FAIL: wrong — NL final was v Spain (lost)
**Q:** In the 2023 Nations League final, how did Croatia beat the Netherlands? **A:** On penalties
**Options:** On penalties | In extra time | In regulation time | By forfeit
**Why it fails:** Croatia did NOT win the 2022–23 Nations League — they beat the Netherlands in the SEMI-final (4-2 AET) and then LOST the FINAL to Spain on penalties (0-0, 5-4). The 'final win over the Netherlands' framing conflates the semi-final with the final and reverses the result.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Croatia lost the final to Spain on penalties; they beat the Netherlands in the semi-final.

### Row 17740 — Croatia (medium) — FAIL: self-referential answer
**Q:** In which 2022 World Cup squad did Croatia's efficient talent-to-population ratio shine? **A:** Croatia's 2022 squad
**Options:** Croatia's 2022 squad | Uruguay's 2022 squad | Morocco's 2022 squad | Denmark's unreachable 2022 squad
**Why it fails:** The question names Croatia and the answer is 'Croatia's 2022 squad' — the answer is its own subject (and a distractor is malformed: 'Denmark's unreachable 2022 squad').
**Source:** https://en.wikipedia.org/wiki/Croatia_national_football_team
**Remedy:** Drop — self-referential; ask a concrete squad fact instead.

### Row 17754 — Croatia (easy) — FAIL: wrong — drew Albania & Italy at Euro 2024
**Q:** In which order did Croatia lose at Euro 2024 before beating Albania? **A:** Spain then Italy
**Options:** Spain then Italy | Italy then Spain | Spain then Germany | Italy then Netherlands
**Why it fails:** At Euro 2024 Croatia went W0 D2 L1: lost to Spain (0-3), DREW Albania 2-2 and DREW Italy 1-1. They did not beat Albania and did not lose to Italy.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Croatia lost only to Spain; both Albania and Italy were draws.

### Row 17755 — Croatia (easy) — FAIL: wrong — drew Albania & Italy at Euro 2024
**Q:** In which order did Croatia lose to Spain, Italy, then beat Albania at Euro 2024? **A:** Spain, Italy, Albania
**Options:** Spain, Italy, Albania | Italy,  Spain,  Albania | Spain, Albania, Italy | Italy, Spain
**Why it fails:** At Euro 2024 Croatia went W0 D2 L1: lost to Spain (0-3), DREW Albania 2-2 and DREW Italy 1-1. They did not beat Albania and did not lose to Italy.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Sequence was Spain (loss), Albania (draw), Italy (draw) — no win.

### Row 17785 — Croatia (hard) — FAIL: false premise (beat Cameroon 4-0)
**Q:** In which World Cup did Croatia lose group games to Brazil, Mexico, and Cameroon? **A:** 2014 FIFA World Cup
**Options:** 2014 FIFA World Cup | 2010 FIFA World Cup | 2018 FIFA World Cup | 2022 FIFA World Cup
**Why it fails:** Croatia beat Cameroon 4-0 in 2014; they lost only to Brazil and Mexico.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_2014_FIFA_World_Cup
**Remedy:** List Brazil and Mexico, not Cameroon.

### Row 17788 — Croatia (medium) — FAIL: wrong explanation (not the only team)
**Q:** In which World Cup did Croatia win all three group matches? **A:** 2018 World Cup
**Options:** 2018 World Cup | 2014 World Cup | 2022 World Cup | 2010 World Cup
**Why it fails:** Belgium also won all three group matches at the 2018 World Cup, so 'the only team' is false.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Remove 'the only team'.

### Row 17798 — Croatia (medium) — FAIL: wrong — Kovačić's first WC was 2014
**Q:** In which World Cup did Croatia's Mateo Kovačić make his tournament debut? **A:** 2018
**Options:** 2018 | 2014 | 2010 | 2022
**Why it fails:** Mateo Kovačić was in Croatia's 2014 World Cup squad, so 2018 was not his first World Cup tournament.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_2014_FIFA_World_Cup
**Remedy:** Answer: 2014 (or drop the 'first tournament' claim).

### Row 17819 — Croatia (medium) — FAIL: wrong — beat Netherlands in semi, not final
**Q:** In which year did Croatia beat the Netherlands in a Nations League final? **A:** 2023
**Options:** 2023 | 2022 | 2021 | 2020
**Why it fails:** Croatia did NOT win the 2023 Nations League final — they beat the Netherlands in the SEMI-final and LOST the FINAL to Spain on penalties.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** They beat the Netherlands in the semi-final; the final (lost) was v Spain.

### Row 17830 — Croatia (medium) — FAIL: wrong — lost NL final to Spain
**Q:** In which year did Croatia win the UEFA Nations League final against the Netherlands? **A:** 2023
**Options:** 2023 | 2022 | 2021 | 2024
**Why it fails:** Croatia did NOT win the 2023 Nations League final — they beat the Netherlands in the SEMI-final and LOST the FINAL to Spain on penalties.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Croatia lost the NL final to Spain.

### Row 17831 — Croatia (medium) — FAIL: wrong — Croatia didn't win the NL
**Q:** In which year did Croatia win the UEFA Nations League final? **A:** 2023
**Options:** 2023 | 2021 | 2020 | 2022
**Why it fails:** Croatia did NOT win the 2023 Nations League final — they beat the Netherlands in the SEMI-final and LOST the FINAL to Spain on penalties.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Croatia were NL runners-up (lost final to Spain).

### Row 17842 — Croatia (medium) — FAIL: wrong explanation (2026 was a group win)
**Q:** Under Zlatko Dalić, which World Cup did Croatia qualify for by winning their group? **A:** 2022 World Cup
**Options:** 2022 World Cup | 2018 World Cup | 2026 World Cup | 2014 World Cup
**Why it fails:** Croatia qualified for 2026 by WINNING their group (7W-1D), not via a playoff; the explanation's '2018 and 2026 via playoffs' is false for 2026.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Only 2014 and 2018 were playoffs; 2022 and 2026 were group wins.

### Row 17863 — Croatia (easy) — FAIL: date corruption (02-Jan = 2-1)
**Q:** What was Croatia's final score against Morocco in the 2022 third-place play-off? **A:** 02-Jan
**Options:** 02-Jan | 1-0 | 3-1 | 2-0
**Why it fails:** Answer '02-Jan' is a mangled '2-1' (beat Morocco 2-1 for 3rd, 2022).
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Restore '2-1'.

### Row 17867 — Croatia (easy) — FAIL: wrong explanation (final was v Spain)
**Q:** What was Croatia's score after 120 minutes in the 2023 Nations League final? **A:** 0-0
**Options:** 0-0 | 1-0 | 1-1 | 2-1
**Why it fails:** The 0-0 final was against Spain, not the Netherlands; the Netherlands match was the 4-2 AET semi-final.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Name Spain as the final opponent.

### Row 17868 — Croatia (medium) — FAIL: date corruption (01-Jan = 1-1)
**Q:** What was Croatia's score after extra time vs Denmark at the 2018 World Cup? **A:** 01-Jan
**Options:** 01-Jan | 2-1 | 0-0 | 2-2
**Why it fails:** Answer '01-Jan' is a mangled '1-1' (v Denmark AET, 2018 R16).
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Restore '1-1'.

### Row 17875 — Croatia (easy) — FAIL: date corruption (02-Jan = 2-1)
**Q:** What was Croatia's winning scoreline against England in the 2018 World Cup semi-final? **A:** 02-Jan
**Options:** 02-Jan | 1-0 | 3-2 | 2-0
**Why it fails:** Answer '02-Jan' is a mangled '2-1' (beat England 2-1, 2018 SF).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_final
**Remedy:** Restore '2-1'.

### Row 17876 — Croatia (medium) — FAIL: wrong explanation (final was v Spain)
**Q:** What was the final score after Croatia's 2023 Nations League final? **A:** 0-0 after extra time
**Options:** 0-0 after extra time | 1-0 after extra time | 1-1 after extra time | 2-1 after extra time
**Why it fails:** The 0-0 AET final was against Spain; the Netherlands was the semi-final.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Name Spain as the final opponent.

### Row 17877 — Croatia (medium) — FAIL: date corruption (01-Jan = 1-1)
**Q:** What was the final score after extra time when Croatia beat Brazil on penalties in the 2022 World Cup quarter-final? **A:** 01-Jan
**Options:** 01-Jan | 0-0 | 2-1 | 2-2
**Why it fails:** Answer '01-Jan' is a mangled '1-1' (v Brazil AET, 2022 QF).
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Restore '1-1'.

### Row 17879 — Croatia (easy) — FAIL: date corruption (05-Mar = 5-3)
**Q:** What was the final score of Croatia's Euro 2020 loss to Spain? **A:** 05-Mar
**Options:** 05-Mar | 4-2 | 3-1 | 2-0
**Why it fails:** Answer '05-Mar' is a mangled '5-3' (lost 5-3 to Spain, Euro 2020).
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Restore '5-3'.

### Row 17880 — Croatia (easy) — FAIL: date corruption (02-Jan = 2-1)
**Q:** What was the final score when Croatia beat England in the 2018 World Cup semi-final? **A:** 02-Jan
**Options:** 02-Jan | 1-0 | 3-1 | 2-0
**Why it fails:** Answer '02-Jan' is a mangled '2-1' (beat England 2-1, 2018 SF).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_final
**Remedy:** Restore '2-1'.

### Row 17881 — Croatia (easy) — FAIL: date corruption (02-Jan = 2-1)
**Q:** What was the final score when Croatia beat Morocco for third place in 2022? **A:** 02-Jan
**Options:** 02-Jan | 1-0 | 3-1 | 2-0
**Why it fails:** Answer '02-Jan' is a mangled '2-1' (beat Morocco 2-1, 2022 3rd place).
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Restore '2-1'.

### Row 17902 — Croatia (medium) — FAIL: wrong — Croatia lost the 2023 NL final to Spain
**Q:** When did Croatia beat the Netherlands in a Nations League final? **A:** 2022-23
**Options:** 2022-23 | 2020-21 | 2018-19 | 2021-22
**Why it fails:** Croatia did NOT win the 2022–23 Nations League — they beat the Netherlands in the SEMI-final and LOST the FINAL to Spain on penalties (0-0, 5-4). They hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** They beat the Netherlands in the semi-final; the final (lost) was v Spain.

### Row 17903 — Croatia (medium) — FAIL: wrong — Croatia lost the 2023 NL final to Spain
**Q:** When did Croatia beat the Netherlands in the Nations League final? **A:** 2023
**Options:** 2023 | 2021 | 2022 | 2024
**Why it fails:** Croatia did NOT win the 2022–23 Nations League — they beat the Netherlands in the SEMI-final and LOST the FINAL to Spain on penalties (0-0, 5-4). They hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** They beat the Netherlands in the semi-final; the final (lost) was v Spain.

### Row 17904 — Croatia (medium) — FAIL: wrong — Croatia lost the 2023 NL final to Spain
**Q:** When did Croatia beat the Netherlands on penalties in a Nations League final? **A:** 2022-23
**Options:** 2022-23 | 2020-21 | 2018-19 | 2021-22
**Why it fails:** Croatia did NOT win the 2022–23 Nations League — they beat the Netherlands in the SEMI-final and LOST the FINAL to Spain on penalties (0-0, 5-4). They hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** They beat the Netherlands in the semi-final; the final (lost) was v Spain.

### Row 17933 — Croatia (medium) — FAIL: wrong explanation (not the only team)
**Q:** When did Croatia win all three World Cup group matches? **A:** 2018
**Options:** 2018 | 2014 | 2022 | 2010
**Why it fails:** Three teams won all three group games in 2018 — Croatia, Belgium AND Uruguay — so 'the only team' is false.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Remove 'the only team'.

### Row 17935 — Croatia (medium) — FAIL: wrong — Croatia lost the 2023 NL final to Spain
**Q:** When did Croatia win the Nations League final on penalties? **A:** 2023
**Options:** 2023 | 2022 | 2021 | 2024
**Why it fails:** Croatia did NOT win the 2022–23 Nations League — they beat the Netherlands in the SEMI-final and LOST the FINAL to Spain on penalties (0-0, 5-4). They hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** They beat the Netherlands in the semi-final; the final (lost) was v Spain.

### Row 17936 — Croatia (medium) — FAIL: wrong — Croatia lost the 2023 NL final to Spain
**Q:** When did Croatia win the UEFA Nations League final against the Netherlands? **A:** 2023
**Options:** 2023 | 2021 | 2022 | 2024
**Why it fails:** Croatia did NOT win the 2022–23 Nations League — they beat the Netherlands in the SEMI-final and LOST the FINAL to Spain on penalties (0-0, 5-4). They hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** They beat the Netherlands in the semi-final; the final (lost) was v Spain.

### Row 17937 — Croatia (medium) — FAIL: wrong — Croatia lost the 2023 NL final to Spain
**Q:** When did Croatia win the UEFA Nations League final? **A:** 2022-23
**Options:** 2022-23 | 2018-19 | 2020-21 | 2024-25
**Why it fails:** Croatia did NOT win the 2022–23 Nations League — they beat the Netherlands in the SEMI-final and LOST the FINAL to Spain on penalties (0-0, 5-4). They hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** They beat the Netherlands in the semi-final; the final (lost) was v Spain.

### Row 17939 — Croatia (medium) — FAIL: wrong — Croatia lost the 2023 NL final to Spain
**Q:** When did Croatia win their first UEFA Nations League title? **A:** 2022-23
**Options:** 2022-23 | 2018-19 | 2020-21 | 2021-22
**Why it fails:** Croatia did NOT win the 2022–23 Nations League — they beat the Netherlands in the SEMI-final and LOST the FINAL to Spain on penalties (0-0, 5-4). They hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** They beat the Netherlands in the semi-final; the final (lost) was v Spain.

### Row 17962 — Croatia (hard) — FAIL: wrong explanation (not the only team)
**Q:** When was Croatia's perfect 3-win group stage? **A:** 2018
**Options:** 2018 | 2014 | 2010 | 2022
**Why it fails:** Croatia, Belgium and Uruguay all won their three group games in 2018.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Remove 'the only team'.

### Row 17991 — Croatia (medium) — FAIL: fabricated — no 2010 playoff v Ukraine
**Q:** Which 2010 playoff opponent caused Croatia's first World Cup qualification failure? **A:** Ukraine
**Options:** Ukraine | Greece | Iceland | Turkey
**Why it fails:** Croatia did not lose a 2010 qualifying playoff to Ukraine — they finished 3rd in their group and never reached a playoff.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Drop — there was no 2010 playoff.

### Row 18005 — Croatia (easy) — FAIL: wrong explanation (Argentina 2022 was 3-0, not pens)
**Q:** Which 2018 World Cup opponent did Croatia beat on penalties, unlike in 2022? **A:** Denmark
**Options:** Denmark | Brazil | Argentina | Russia
**Why it fails:** Croatia lost the 2022 semi-final to Argentina 3-0 in regulation, NOT on penalties; in 2022 Croatia actually WON their shootouts (Japan, Brazil).
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Re-anchor: Croatia beat Denmark on penalties in 2018; the 2022 Argentina loss was 3-0 in normal time.

### Row 18006 — Croatia (easy) — FAIL: non-unique (three options not faced in 2018 playoff)
**Q:** Which 2018 World Cup playoff opponent did Croatia NOT face? **A:** Ukraine
**Options:** Ukraine | Greece | Iceland | Sweden
**Why it fails:** Croatia's only 2018 playoff was v Greece, so Ukraine, Iceland AND Sweden were all 'not faced' in the 2018 playoff.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Ask which team Croatia DID face in the 2018 playoff (Greece).

### Row 18014 — Croatia (easy) — FAIL: wrong — Dalić didn't win the 2022-23 NL
**Q:** Which 2022 tournament did Croatia's manager Dalić win? **A:** UEFA Nations League
**Options:** UEFA Nations League | FIFA World Cup | UEFA European Championship | FIFA Confederations Cup
**Why it fails:** Croatia reached the 2022-23 Nations League final but LOST it to Spain on penalties; Dalić did not win the title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Drop — Croatia were NL runners-up.

### Row 18026 — Croatia (easy) — FAIL: wrong — Croatia lost the 2023 NL final to Spain
**Q:** Which 2022-23 Nations League final did Croatia win on penalties? **A:** Netherlands
**Options:** Netherlands | Portugal | Spain | France
**Why it fails:** Croatia did NOT win the 2022–23 Nations League — they beat the Netherlands in the SEMI-final and LOST the FINAL to Spain on penalties (0-0, 5-4). They hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** They beat the Netherlands in the semi-final; the final (lost) was v Spain.

### Row 18028 — Croatia (medium) — FAIL: wrong — Croatia didn't win the NL
**Q:** Which 2023 achievement boosted Croatia's FIFA ranking? **A:** Winning the Nations League
**Options:** Winning the Nations League | Reaching the World Cup final | Winning the European Championship | Topping their qualifying group
**Why it fails:** Croatia lost the 2023 NL final to Spain, so 'winning the Nations League' is false.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Their ranking rose from reaching the final, not winning it.

### Row 18036 — Croatia (easy) — FAIL: wrong — Croatia didn't win the NL
**Q:** Which Croatia achievement in 2023 helped them qualify for the 2024 Euros? **A:** Won UEFA Nations League
**Options:** Won UEFA Nations League | Reached World Cup final | Topped their qualifying group | Won a friendly tournament
**Why it fails:** Croatia did not win the 2022–23 Nations League (lost the final to Spain), and they qualified for Euro 2024 via the normal qualifying group, not via the NL.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Drop — false achievement.

### Row 18041 — Croatia (easy) — FAIL: wrong age — Modrić was 37 at 2022 WC
**Q:** Which Croatia captain was 39 at the 2022 FIFA World Cup? **A:** Luka Modrić
**Options:** Luka Modrić | Ivan Perišić | Mateo Kovačić | Domagoj Vida
**Why it fails:** Modrić (b. 9 Sept 1985) was 37 at the 2022 World Cup, not 39.
**Source:** https://en.wikipedia.org/wiki/Luka_Modri%C4%87
**Remedy:** Answer identity (Modrić) is right; fix the age to 37.

### Row 18042 — Croatia (easy) — FAIL: wrong age — Modrić is 40 at 2026 WC
**Q:** Which Croatia captain was 39 at the 2026 FIFA World Cup? **A:** Luka Modrić
**Options:** Luka Modrić | Ivan Perišić | Mateo Kovačić | Andrej Kramarić
**Why it fails:** Modrić turns 40 in Sept 2025, so he is 40 (not 39) at the June 2026 World Cup.
**Source:** https://en.wikipedia.org/wiki/Luka_Modri%C4%87
**Remedy:** Fix the age to 40.

### Row 18043 — Croatia (easy) — FAIL: wrong age — Modrić was 37 at 2022 WC
**Q:** Which Croatia captain, aged 39, led his team at the 2022 FIFA World Cup? **A:** Luka Modrić
**Options:** Luka Modrić | Ivan Rakitić | Mario Mandžukić | Darijo Srna
**Why it fails:** Modrić was 37 (not 39) at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/Luka_Modri%C4%87
**Remedy:** Fix the age to 37.

### Row 18053 — Croatia (easy) — FAIL: wrong — no 2023 NL title
**Q:** Which Croatia coach's tactical decisions led to their 2023 UEFA Nations League title? **A:** Zlatko Dalić
**Options:** Zlatko Dalić | Igor Štimac | Slaven Bilić | Ante Čačić
**Why it fails:** Croatia LOST the 2022–23 Nations League final to Spain on penalties; they hold no NL title (they beat the Netherlands only in the semi-final).
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Croatia were NL runners-up.

### Row 18057 — Croatia (easy) — FAIL: wrong — Enzo Fernández won 2022 BYP
**Q:** Which Croatia defender earned the 2022 World Cup Best Young Player award? **A:** Joško Gvardiol
**Options:** Joško Gvardiol | Dejan Lovren | Domagoj Vida | Borna Sosa
**Why it fails:** The 2022 World Cup Best Young Player was Enzo Fernández, not Gvardiol.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Drop — Gvardiol did not win the award.

### Row 18071 — Croatia (easy) — FAIL: wrong — Croatia lost the 2023 NL final
**Q:** Which Croatia final win was decided on penalties in 2023? **A:** Nations League final
**Options:** Nations League final | World Cup final | European Championship final | Confederations Cup final
**Why it fails:** The 2023 NL final was not a Croatia win — they lost to Spain on penalties (the Netherlands was the semi-final).
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Drop — Croatia lost the final.

### Row 18136 — Croatia (easy) — FAIL: wrong — no NL title
**Q:** Which Croatia manager led them to a World Cup final and a Nations League title? **A:** Zlatko Dalić
**Options:** Zlatko Dalić | Slaven Bilić | Niko Kovač | Ante Čačić
**Why it fails:** Croatia LOST the 2022–23 Nations League final to Spain on penalties; they hold no NL title (they beat the Netherlands only in the semi-final).
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Dalić led them to the 2018 WC final but NOT an NL title.

### Row 18139 — Croatia (easy) — FAIL: wrong — no NL title
**Q:** Which Croatia manager led them to the 2022-23 Nations League title? **A:** Zlatko Dalić
**Options:** Zlatko Dalić | Slaven Bilić | Niko Kovač | Ante Čačić
**Why it fails:** Croatia LOST the 2022–23 Nations League final to Spain on penalties; they hold no NL title (they beat the Netherlands only in the semi-final).
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Croatia lost the 2022–23 NL final to Spain.

### Row 18153 — Croatia (easy) — FAIL: non-unique (Čačić also fits)
**Q:** Which Croatia manager reached a major tournament finals but not a World Cup playoff? **A:** Slaven Bilić
**Options:** Slaven Bilić | Zlatko Dalić | Niko Kovač | Ante Čačić
**Why it fails:** Both Bilić (Euro 2008) AND Čačić (Euro 2016) reached major-tournament finals without ever managing a World Cup playoff — two correct answers.
**Source:** https://en.wikipedia.org/wiki/Croatia_national_football_team
**Remedy:** Replace Čačić with a manager who did lead a WC playoff (Kovač/Dalić).

### Row 18192 — Croatia (easy) — FAIL: wrong explanation (Kovač led 2014 WC)
**Q:** Which Croatia manager was NOT appointed mid-World Cup qualifying? **A:** Niko Kovač
**Options:** Niko Kovač | Zlatko Dalić | Slaven Bilić | Ante Čačić
**Why it fails:** The explanation claims Kovač 'began his tenure after the 2014 World Cup cycle' — false; Kovač was appointed in Oct 2013 and managed the 2014 WC qualifying playoff and the 2014 finals.
**Source:** https://en.wikipedia.org/wiki/Croatia_national_football_team
**Remedy:** Fix the explanation; the Kovač distinction is wrong.

### Row 18193 — Croatia (easy) — FAIL: wrong — no 2022-23 NL title
**Q:** Which Croatia manager won the 2022-23 Nations League after two World Cup podiums? **A:** Zlatko Dalić
**Options:** Zlatko Dalić | Slaven Bilić | Niko Kovač | Ante Čačić
**Why it fails:** Croatia LOST the 2022–23 Nations League final to Spain on penalties; they hold no NL title (they beat the Netherlands only in the semi-final).
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Drop the NL-title claim.

### Row 18194 — Croatia (easy) — FAIL: wrong — no 2022-23 NL title
**Q:** Which Croatia manager won the 2022-23 Nations League title? **A:** Zlatko Dalić
**Options:** Zlatko Dalić | Slaven Bilić | Niko Kovač | Ante Čačić
**Why it fails:** Croatia LOST the 2022–23 Nations League final to Spain on penalties; they hold no NL title (they beat the Netherlands only in the semi-final).
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Croatia were NL runners-up.

### Row 18195 — Croatia (easy) — FAIL: wrong — lost the 2023 NL final to Spain
**Q:** Which Croatia manager won the 2023 Nations League final? **A:** Zlatko Dalić
**Options:** Zlatko Dalić | Slaven Bilić | Niko Kovač | Ivica Olić
**Why it fails:** Croatia LOST the 2022–23 Nations League final to Spain on penalties; they hold no NL title (they beat the Netherlands only in the semi-final).
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** They lost the final to Spain on penalties.

### Row 18229 — Croatia (hard) — FAIL: wrong answer — NL final was a loss
**Q:** Which Croatia penalty win came after their 2018 World Cup semi-final? **A:** 2023 Nations League final
**Options:** 2023 Nations League final | 2022 World Cup quarter-final | 2022 World Cup third-place | Euro   2016 quarter-final
**Why it fails:** The penalty win after the 2018 semi-final was the 2022 World Cup QUARTER-FINAL v Brazil (a listed option); the 2023 NL final was a penalty LOSS to Spain, not a win.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Answer: 2022 World Cup quarter-final.

### Row 18243 — Croatia (easy) — FAIL: wrong stat — ~160 caps at 2022 WC
**Q:** Which Croatia player had over 175 caps by the 2022 World Cup? **A:** Luka Modrić
**Options:** Luka Modrić | Ivan Rakitić | Mario Mandžukić | Dejan Lovren
**Why it fails:** Modrić had roughly 160 caps at the 2022 World Cup (he reached 196 only by 2026), so 'over 175 caps by the 2022 World Cup' is an overstatement.
**Source:** https://en.wikipedia.org/wiki/Luka_Modri%C4%87
**Remedy:** He was most-capped, but not yet over 175 in 2022.

### Row 18267 — Croatia (easy) — FAIL: asserts false 2023 NL title
**Q:** Which Croatia player scored a World Cup semi-final winner before their 2023 Nations League title? **A:** Mario Mandžukić
**Options:** Mario Mandžukić | Luka Modrić | Joško Gvardiol | Dominik Livaković
**Why it fails:** Mandžukić did score the 2018 SF winner, but the clause 'before their 2023 Nations League title' asserts a title Croatia never won (they lost the final to Spain).
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Remove the false NL-title reference.

### Row 18298 — Croatia (medium) — FAIL: malformed + Croatia didn't beat Albania
**Q:** Which Croatia player scored their only Euro 2024 group stage win? **A:** Albania
**Options:** Albania | Spain | Italy | Germany
**Why it fails:** Asks 'which player' but answers 'Albania' (a nation), and Croatia did NOT win v Albania at Euro 2024 — that match was a 2-2 draw (Croatia went W0 D2 L1).
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Drop — there was no Euro 2024 group win.

### Row 18309 — Croatia (easy) — FAIL: wrong — Enzo Fernández won 2022 BYP
**Q:** Which Croatia player was named Best Young Player at the 2022 World Cup? **A:** Joško Gvardiol
**Options:** Joško Gvardiol | Luka Modrić | Dominik Livaković | Mario Mandžukić
**Why it fails:** The 2022 World Cup Best Young Player was Enzo Fernández, not Gvardiol.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Drop — Gvardiol didn't win the award.

### Row 18347 — Croatia (hard) — FAIL: self-referential + false 'only'
**Q:** Which Croatia team won all three 2018 World Cup group matches? **A:** The 2018 Croatia team
**Options:** The 2018 Croatia team | The -2014 Croatia team | The 2022 Croatia team | The 2010 Croatia team
**Why it fails:** The question names 'which Croatia team' and answers 'The 2018 Croatia team' (its own subject); also three teams (Croatia, Belgium, Uruguay) won all three group games in 2018, so 'only' is false.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Reframe; remove the self-reference and 'only'.

### Row 18348 — Croatia (hard) — FAIL: wrong — Croatia lost the 2023 NL final
**Q:** Which Croatia tournament win in 2023 ended with a penalty shootout? **A:** UEFA Nations League
**Options:** UEFA Nations League | European Championship | World Cup Qualifiers | FIFA World Cup
**Why it fails:** Croatia LOST the 2022–23 Nations League final to Spain on penalties (the Netherlands was the SEMI-final); they hold no UEFA title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** The 2023 final shootout was lost to Spain, not won.

### Row 18349 — Croatia (hard) — FAIL: wrong — Croatia lost the 2023 NL final
**Q:** Which Croatia tournament win in 2023 required a penalty shootout after 0-0? **A:** Nations League final
**Options:** Nations League final | Euro quarter-final | World Cup qualifier | Euro round of 16
**Why it fails:** Croatia LOST the 2022–23 Nations League final to Spain on penalties (the Netherlands was the SEMI-final); they hold no UEFA title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** The 2023 final shootout was lost to Spain, not won.

### Row 18350 — Croatia (hard) — FAIL: wrong — Croatia lost the 2023 NL final
**Q:** Which Croatia trophy win in 2023 was secured via a penalty shootout? **A:** UEFA Nations League
**Options:** UEFA Nations League | FIFA World Cup | European Championship | FIFA Confederations Cup
**Why it fails:** Croatia LOST the 2022–23 Nations League final to Spain on penalties (the Netherlands was the SEMI-final); they hold no UEFA title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** The 2023 final shootout was lost to Spain, not won.

### Row 18351 — Croatia (easy) — FAIL: wrong — Croatia have no UEFA title
**Q:** Which Croatia trophy win in 2023 was their first UEFA title? **A:** UEFA Nations League
**Options:** UEFA Nations League | UEFA Euro 2024 | FIFA World Cup 2022 | UEFA Euro 2016
**Why it fails:** Croatia did not win their 'first UEFA title' in 2023 — they lost the Nations League final to Spain on penalties.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Drop — Croatia hold no senior UEFA trophy.

### Row 18353 — Croatia (easy) — FAIL: wrong age — Modrić is 40 at 2026 WC
**Q:** Which Croatia veteran was 39 years old at the 2026 FIFA World Cup? **A:** Luka Modrić
**Options:** Luka Modrić | Ivan Perišić | Domagoj Vida | Marcelo Brozović
**Why it fails:** Modrić turns 40 in Sept 2025, so he is 40 (not 39) at the June 2026 World Cup.
**Source:** https://en.wikipedia.org/wiki/Luka_Modri%C4%87
**Remedy:** Fix the age to 40.

### Row 18354 — Croatia (medium) — FAIL: wrong — NL final was v Spain (lost)
**Q:** Which Croatia victory was a UEFA Nations League final, not a Euro final? **A:** 2022-23 vs Netherlands
**Options:** 2022-23 vs Netherlands | 2018 vs Argentina | 2022 vs Belgium | 2016 vs Spain
**Why it fails:** Croatia LOST the 2022–23 Nations League final to Spain on penalties (the Netherlands was the SEMI-final); they hold no UEFA title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** The 2022-23 final (lost) was v Spain; the Netherlands was the semi-final.

### Row 18363 — Croatia (medium) — FAIL: fabricated WC playoff losses
**Q:** Which Croatia World Cup qualifying playoff loss happened first? **A:** 2010 to Ukraine
**Options:** 2010 to Ukraine | 2014 to Iceland | 2018 to Greece | 2022 to Russia
**Why it fails:** Croatia have NO World Cup playoff losses: they won the 2014 (Iceland) and 2018 (Greece) playoffs and never reached a 2010 playoff. '2010 to Ukraine' is invented.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Drop — none of the listed playoff 'losses' happened.

### Row 18368 — Croatia (easy) — FAIL: wrong age — Modrić was 37 at 2022 WC
**Q:** Which Croatian captain was 39 years old at the 2022 FIFA World Cup? **A:** Luka Modrić
**Options:** Luka Modrić | Ivan Perišić | Mateo Kovačić | Domagoj Vida
**Why it fails:** Modrić was 37 at the 2022 World Cup, not 39.
**Source:** https://en.wikipedia.org/wiki/Luka_Modri%C4%87
**Remedy:** Fix the age to 37.

### Row 18423 — Croatia (easy) — FAIL: wrong — Enzo Fernández won 2022 BYP
**Q:** Which Croatian defender was named Best Young Player at the 2022 FIFA World Cup? **A:** Joško Gvardiol
**Options:** Joško Gvardiol | Dejan Lovren | Josip Šutalo | Martin Erlić
**Why it fails:** The 2022 World Cup Best Young Player was Enzo Fernández, not Gvardiol.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Drop — Gvardiol didn't win the award.

### Row 18425 — Croatia (easy) — FAIL: wrong — Enzo Fernández won 2022 BYP
**Q:** Which Croatian defender was selected as the 2022 World Cup's Best Young Player? **A:** Joško Gvardiol
**Options:** Joško Gvardiol | Dejan Lovren | Domagoj Vida | Borna Sosa
**Why it fails:** The 2022 World Cup Best Young Player was Enzo Fernández, not Gvardiol.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Drop — Gvardiol didn't win the award.

### Row 18430 — Croatia (easy) — FAIL: wrong — Enzo Fernández won 2022 BYP
**Q:** Which Croatian defender won the Best Young Player award at Qatar 2022? **A:** Joško Gvardiol
**Options:** Joško Gvardiol | Luka Modrić | Dejan Lovren | Mateo Kovačić
**Why it fails:** The 2022 World Cup Best Young Player was Enzo Fernández, not Gvardiol.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Drop — Gvardiol didn't win the award.

### Row 18539 — Croatia (easy) — FAIL: wrong stat — ~160 caps at 2022 WC
**Q:** Which Croatian player had over 175 caps by the 2022 World Cup? **A:** Luka Modrić
**Options:** Luka Modrić | Ivan Perišić | Mateo Kovačić | Marcelo Brozović
**Why it fails:** Modrić had ~120 caps at the 2018 WC and ~160 at the 2022 WC; he only passed 175 around 2024 (196 by 2026). Anchoring '175+ caps' to 2018/2022 is an overstatement.
**Source:** https://en.wikipedia.org/wiki/Luka_Modri%C4%87
**Remedy:** He was most-capped, but not over 175 by 2022.

### Row 18549 — Croatia (easy) — FAIL: wrong stat — ~160 caps before 2022
**Q:** Which Croatian player reached 175 caps before the 2022 World Cup? **A:** Luka Modrić
**Options:** Luka Modrić | Ivan Rakitić | Dejan Lovren | Domagoj Vida
**Why it fails:** Modrić had ~120 caps at the 2018 WC and ~160 at the 2022 WC; he only passed 175 around 2024 (196 by 2026). Anchoring '175+ caps' to 2018/2022 is an overstatement.
**Source:** https://en.wikipedia.org/wiki/Luka_Modri%C4%87
**Remedy:** He reached 175+ only c.2024.

### Row 18565 — Croatia (easy) — FAIL: wrong — Perišić scored once in 2018 final
**Q:** Which Croatian player scored twice in the 2018 World Cup final? **A:** Ivan Perišić
**Options:** Ivan Perišić | Luka Modrić | Mario Mandžukić | Domagoj Vida
**Why it fails:** Perišić scored only ONE goal in the 2018 final (28'); Mandžukić scored Croatia's other goal (69'). No Croatian scored twice.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_final
**Remedy:** Answer: nobody scored twice; Perišić and Mandžukić each scored once.

### Row 18593 — Croatia (easy) — FAIL: wrong — Enzo Fernández won 2022 BYP
**Q:** Which Croatian player won the Best Young Player award at the 2022 FIFA World Cup? **A:** Joško Gvardiol
**Options:** Joško Gvardiol | Luka Modrić | Dominik Livaković | Mario Mandžukić
**Why it fails:** The 2022 World Cup Best Young Player was Enzo Fernández, not Gvardiol.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Drop — Gvardiol didn't win the award.

### Row 18602 — Croatia (easy) — FAIL: wrong stat — ~120 caps at 2018 WC
**Q:** Which Croatian player's 175+ caps helped them win all 2018 group matches? **A:** Luka Modrić
**Options:** Luka Modrić | Ivan Rakitić | Mario Mandžukić | Dejan Lovren
**Why it fails:** Modrić had ~120 caps at the 2018 WC and ~160 at the 2022 WC; he only passed 175 around 2024 (196 by 2026). Anchoring '175+ caps' to 2018/2022 is an overstatement.
**Source:** https://en.wikipedia.org/wiki/Luka_Modri%C4%87
**Remedy:** In 2018 he had ~120 caps, not 175+.

### Row 18609 — Croatia (easy) — FAIL: wrong stat — ~160 caps by 2022
**Q:** Which Croatian player's longevity led to a record 175+ caps by 2022? **A:** Luka Modrić
**Options:** Luka Modrić | Ivan Rakitić | Mario Mandžukić | Dejan Lovren
**Why it fails:** Modrić had ~120 caps at the 2018 WC and ~160 at the 2022 WC; he only passed 175 around 2024 (196 by 2026). Anchoring '175+ caps' to 2018/2022 is an overstatement.
**Source:** https://en.wikipedia.org/wiki/Luka_Modri%C4%87
**Remedy:** Not 175+ by 2022.

### Row 18610 — Croatia (easy) — FAIL: wrong explanation — not 175 by 2022
**Q:** Which Croatian player's longevity made them the nation's most-capped at the 2022 World Cup? **A:** Luka Modrić
**Options:** Luka Modrić | Ivan Perišić | Dejan Lovren | Mateo Kovačić
**Why it fails:** Modrić was the most-capped in 2022 (true), but the explanation's 'over 175 appearances by the 2022 tournament' is false — he had ~160 then.
**Source:** https://en.wikipedia.org/wiki/Luka_Modri%C4%87
**Remedy:** He was most-capped but not yet over 175 in 2022.

### Row 18675 — Croatia (easy) — FAIL: wrong — NL final was v Spain (lost)
**Q:** Which final did Croatia win on penalties in 2023? **A:** Nations League final
**Options:** Nations League final | World Cup final | European Championship final | Confederations Cup final
**Why it fails:** The 2023 Nations League FINAL was Croatia v Spain (lost on penalties); Croatia beat the Netherlands only in the SEMI-final. So 'beat the Netherlands in the final / won the NL' is false.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 18676 — Croatia (easy) — FAIL: date corruption (04/03/2003 = 4-3-3)
**Q:** Which formation did Croatia use under Zlatko Dalić at the 2018 FIFA World Cup? **A:** 04/03/2003
**Options:** 04/03/2003 | 3-5-2 | 4-4-2 | 4-2-3-1
**Why it fails:** Answer '04/03/2003' is a mangled '4-3-3' formation.
**Source:** https://en.wikipedia.org/wiki/Croatia_national_football_team
**Remedy:** Restore answer to '4-3-3'.

### Row 18677 — Croatia (easy) — FAIL: date corruption (04/03/2003 = 4-3-3)
**Q:** Which formation did Zlatko Dalić use for Croatia's 2018 World Cup run? **A:** 04/03/2003
**Options:** 04/03/2003 | 3-5-2 | 4-4-2 | 4-2-3-1
**Why it fails:** Answer '04/03/2003' is a mangled '4-3-3' formation.
**Source:** https://en.wikipedia.org/wiki/Croatia_national_football_team
**Remedy:** Restore answer to '4-3-3'.

### Row 18681 — Croatia (easy) — FAIL: non-unique (Kovač also fits)
**Q:** Which manager did NOT lead Croatia at a major tournament from 2016 to 2022? **A:** Slaven Bilić
**Options:** Slaven Bilić | Ante Čačić | Zlatko Dalić | Niko Kovač
**Why it fails:** Both Bilić (last major tournament Euro 2008) AND Kovač (2014 WC) did NOT lead Croatia at a major tournament during 2016–2022 — two correct answers.
**Source:** https://en.wikipedia.org/wiki/Croatia_national_football_team
**Remedy:** Replace Kovač with a manager who did lead a 2016–2022 tournament.

### Row 18724 — Croatia (easy) — FAIL: fabricated — no 2010 playoff v Ukraine
**Q:** Which nation beat Croatia in a 2010 World Cup qualifying playoff? **A:** Ukraine
**Options:** Ukraine | Iceland | Greece | Russia
**Why it fails:** Croatia did not play (or lose) a 2010 World Cup qualifying playoff against Ukraine — they finished 3rd in their group and never reached a playoff. The Ukraine playoff is fabricated.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Drop — there was no 2010 playoff.

### Row 18730 — Croatia (easy) — FAIL: fabricated — no 2010 playoff v Ukraine
**Q:** Which nation defeated Croatia in the 2010 World Cup qualifying playoff? **A:** Ukraine
**Options:** Ukraine | Iceland | Greece | Russia
**Why it fails:** Croatia did not play (or lose) a 2010 World Cup qualifying playoff against Ukraine — they finished 3rd in their group and never reached a playoff. The Ukraine playoff is fabricated.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Drop — there was no 2010 playoff.

### Row 18748 — Croatia (easy) — FAIL: wrong — NL final was v Spain (lost)
**Q:** Which nation did Croatia beat in the 2022-23 Nations League final? **A:** Netherlands
**Options:** Netherlands | Spain | Portugal | Italy
**Why it fails:** The 2023 Nations League FINAL was Croatia v Spain (lost on penalties); Croatia beat the Netherlands only in the SEMI-final. So 'beat the Netherlands in the final / won the NL' is false.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 18750 — Croatia (easy) — FAIL: wrong — NL final was v Spain (lost)
**Q:** Which nation did Croatia beat in the 2023 UEFA Nations League final? **A:** Netherlands
**Options:** Netherlands | Spain | Portugal | Italy
**Why it fails:** The 2023 Nations League FINAL was Croatia v Spain (lost on penalties); Croatia beat the Netherlands only in the SEMI-final. So 'beat the Netherlands in the final / won the NL' is false.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 18751 — Croatia (easy) — FAIL: wrong — Croatia drew Albania 2-2
**Q:** Which nation did Croatia beat in their final Euro 2024 group match? **A:** Albania
**Options:** Albania | Italy | Spain | Netherlands
**Why it fails:** Croatia did NOT beat Albania at Euro 2024 (it was a 2-2 draw), and their final group match was v Italy (1-1). Croatia had no Euro 2024 group win.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Drop — there was no Euro 2024 group win.

### Row 18754 — Croatia (easy) — FAIL: wrong — NL final was v Spain (lost)
**Q:** Which nation did Croatia beat on penalties in the 2023 Nations League final? **A:** Netherlands
**Options:** Netherlands | Portugal | Spain | Italy
**Why it fails:** The 2023 Nations League FINAL was Croatia v Spain (lost on penalties); Croatia beat the Netherlands only in the SEMI-final. So 'beat the Netherlands in the final / won the NL' is false.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 18756 — Croatia (easy) — FAIL: wrong — NL final was v Spain (lost)
**Q:** Which nation did Croatia beat to win the 2022-23 UEFA Nations League? **A:** Netherlands
**Options:** Netherlands | Portugal | Spain | Italy
**Why it fails:** The 2023 Nations League FINAL was Croatia v Spain (lost on penalties); Croatia beat the Netherlands only in the SEMI-final. So 'beat the Netherlands in the final / won the NL' is false.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 18757 — Croatia (easy) — FAIL: wrong — NL final was v Spain (lost)
**Q:** Which nation did Croatia beat to win the 2023 UEFA Nations League? **A:** The Netherlands
**Options:** The Netherlands | Portugal | Spain | Italy
**Why it fails:** The 2023 Nations League FINAL was Croatia v Spain (lost on penalties); Croatia beat the Netherlands only in the SEMI-final. So 'beat the Netherlands in the final / won the NL' is false.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 18763 — Croatia (easy) — FAIL: wrong — NL final was v Spain (lost)
**Q:** Which nation did Croatia defeat in the 2022-23 Nations League final? **A:** Netherlands
**Options:** Netherlands | Spain | Portugal | Italy
**Why it fails:** The 2023 Nations League FINAL was Croatia v Spain (lost on penalties); Croatia beat the Netherlands only in the SEMI-final. So 'beat the Netherlands in the final / won the NL' is false.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 18768 — Croatia (easy) — FAIL: wrong — NL final was v Spain (lost)
**Q:** Which nation did Croatia defeat to win a tournament final in 2023? **A:** Netherlands
**Options:** Netherlands | Portugal | Spain | France
**Why it fails:** The 2023 Nations League FINAL was Croatia v Spain (lost on penalties); Croatia beat the Netherlands only in the SEMI-final. So 'beat the Netherlands in the final / won the NL' is false.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 18769 — Croatia (easy) — FAIL: wrong — NL final was v Spain (lost)
**Q:** Which nation did Croatia defeat to win the 2023 Nations League final? **A:** Netherlands
**Options:** Netherlands | Spain | Portugal | Italy
**Why it fails:** The 2023 Nations League FINAL was Croatia v Spain (lost on penalties); Croatia beat the Netherlands only in the SEMI-final. So 'beat the Netherlands in the final / won the NL' is false.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 18779 — Croatia (easy) — FAIL: non-unique (France also not beaten)
**Q:** Which nation did Croatia NOT defeat in a major tournament knockout match? **A:** Spain
**Options:** Spain | France | England | Brazil
**Why it fails:** Croatia also never beat France in a knockout — they LOST the 2018 final to France — so both 'Spain' and 'France' are nations Croatia didn't defeat in a knockout.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Replace France with a team Croatia beat in a knockout (England/Brazil).

### Row 18781 — Croatia (easy) — FAIL: fabricated — no 2010 playoff v Ukraine
**Q:** Which nation eliminated Croatia in the 2010 World Cup qualifying playoff? **A:** Ukraine
**Options:** Ukraine | Greece | Iceland | Turkey
**Why it fails:** Croatia did not play (or lose) a 2010 World Cup qualifying playoff against Ukraine — they finished 3rd in their group and never reached a playoff. The Ukraine playoff is fabricated.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Drop — there was no 2010 playoff.

### Row 18791 — Croatia (easy) — FAIL: wrong — NL final was v Spain (lost)
**Q:** Which nation lost to Croatia in the 2023 Nations League final? **A:** The Netherlands
**Options:** The Netherlands | Spain | Portugal | Italy
**Why it fails:** Croatia LOST the 2023 Nations League final to Spain on penalties (the Netherlands was the semi-final); they hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 18814 — Croatia (easy) — FAIL: self-referential answer
**Q:** Which nation, like Croatia at Euro 2020, equalised after trailing 3-1? **A:** Croatia
**Options:** Croatia | Portugal | Italy | Germany
**Why it fails:** 'Which nation, like Croatia at Euro 2020, equalised after trailing 3-1?' answers 'Croatia' — the subject itself.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Drop — self-referential.

### Row 18816 — Croatia (easy) — FAIL: false premise (Croatia didn't win the NL)
**Q:** Which nation, like Croatia in 2023, won a UEFA Nations League title? **A:** Portugal
**Options:** Portugal | Spain | France | Netherlands
**Why it fails:** The comparison 'like Croatia in 2023, won a Nations League title' is false — Croatia lost the 2023 NL final and have no NL title. (Portugal did win the 2019 NL.)
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Remove the false Croatia comparison.

### Row 18881 — Croatia (easy) — FAIL: fabricated — no 2010 playoff v Ukraine
**Q:** Which team beat Croatia in a 2010 World Cup qualifying playoff? **A:** Ukraine
**Options:** Ukraine | Iceland | Greece | Sweden
**Why it fails:** Croatia never played a 2010 World Cup qualifying playoff against Ukraine — they finished 3rd in their group and missed the playoff entirely. Fabricated.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Drop — there was no 2010 playoff.

### Row 18882 — Croatia (easy) — FAIL: fabricated — no 2010 playoff v Ukraine
**Q:** Which team beat Croatia in a playoff for the 2010 World Cup? **A:** Ukraine
**Options:** Ukraine | Greece | Iceland | Portugal
**Why it fails:** Croatia never played a 2010 World Cup qualifying playoff against Ukraine — they finished 3rd in their group and missed the playoff entirely. Fabricated.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Drop — there was no 2010 playoff.

### Row 18884 — Croatia (easy) — FAIL: fabricated — no 2010 playoff v Ukraine
**Q:** Which team beat Croatia in the 2010 World Cup playoff? **A:** Ukraine
**Options:** Ukraine | Greece | Iceland | Turkey
**Why it fails:** Croatia never played a 2010 World Cup qualifying playoff against Ukraine — they finished 3rd in their group and missed the playoff entirely. Fabricated.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Drop — there was no 2010 playoff.

### Row 18886 — Croatia (easy) — FAIL: fabricated — no 2010 playoff v Ukraine
**Q:** Which team defeated Croatia in a 2010 World Cup qualifying playoff? **A:** Ukraine
**Options:** Ukraine | Iceland | Greece | Turkey
**Why it fails:** Croatia never played a 2010 World Cup qualifying playoff against Ukraine — they finished 3rd in their group and missed the playoff entirely. Fabricated.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Drop — there was no 2010 playoff.

### Row 18896 — Croatia (easy) — FAIL: wrong — Croatia drew Albania 2-2
**Q:** Which team did Croatia beat at Euro 2024? **A:** Albania
**Options:** Albania | Spain | Italy | Portugal
**Why it fails:** At Euro 2024 Croatia went W0 D2 L1 (lost Spain 0-3, drew Albania 2-2, drew Italy 1-1) — they had no group win and did not beat Albania; the final group match was v Italy.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Drop — no Euro 2024 group win.

### Row 18897 — Croatia (easy) — FAIL: wrong — Croatia beat Cameroon 4-0
**Q:** Which team did Croatia beat at the 2014 World Cup? **A:** None
**Options:** None | Cameroon | Australia | Mexico
**Why it fails:** Croatia did beat a team at the 2014 WC — they beat Cameroon 4-0. The answer 'None' is wrong.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_2014_FIFA_World_Cup
**Remedy:** Answer: Cameroon (4-0).

### Row 18911 — Croatia (easy) — FAIL: wrong — NL final was v Spain (lost)
**Q:** Which team did Croatia beat in the 2023 UEFA Nations League final? **A:** Netherlands
**Options:** Netherlands | Portugal | Spain | Italy
**Why it fails:** Croatia LOST the 2023 Nations League final to Spain on penalties (the Netherlands was the semi-final); they hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 18914 — Croatia (medium) — FAIL: wrong — last group game was Italy (draw)
**Q:** Which team did Croatia beat last in the Euro 2024 group stage? **A:** Albania
**Options:** Albania | Spain | Italy | Netherlands
**Why it fails:** At Euro 2024 Croatia went W0 D2 L1 (lost Spain 0-3, drew Albania 2-2, drew Italy 1-1) — they had no group win and did not beat Albania; the final group match was v Italy. The Albania game (a draw) was the second match, not the last.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Final group match was a 1-1 draw v Italy.

### Row 18919 — Croatia (easy) — FAIL: wrong — NL final was v Spain (lost)
**Q:** Which team did Croatia beat on penalties in the 2022-23 Nations League final? **A:** The Netherlands
**Options:** The Netherlands | Portugal | Spain | France
**Why it fails:** Croatia LOST the 2023 Nations League final to Spain on penalties (the Netherlands was the semi-final); they hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 18922 — Croatia (medium) — FAIL: wrong — Croatia drew Albania 2-2
**Q:** Which team did Croatia defeat in the Euro 2024 group stage? **A:** Albania
**Options:** Albania | Spain | Italy | Portugal
**Why it fails:** At Euro 2024 Croatia went W0 D2 L1 (lost Spain 0-3, drew Albania 2-2, drew Italy 1-1) — they had no group win and did not beat Albania; the final group match was v Italy.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Drop — no Euro 2024 group win.

### Row 18930 — Croatia (medium) — FAIL: wrong/non-unique — beat Cameroon
**Q:** Which team did Croatia NOT lose to in their 2014 World Cup group stage? **A:** Argentina
**Options:** Argentina | Brazil | Mexico | Cameroon
**Why it fails:** Croatia BEAT Cameroon 4-0 in 2014; they lost only to Brazil and Mexico. So among the options, Croatia did NOT lose to Argentina (didn't play) AND did NOT lose to Cameroon (beat them) — two correct answers, and the explanation falsely says they lost to Cameroon.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_2014_FIFA_World_Cup
**Remedy:** Replace Cameroon; the only teams Croatia lost to were Brazil and Mexico.

### Row 18932 — Croatia (easy) — FAIL: wrong — Portugal DID eliminate them in a Euro R16
**Q:** Which team did NOT eliminate Croatia in a Euro round of 16? **A:** Portugal
**Options:** Portugal | Spain | Türkiye | Netherlands
**Why it fails:** Portugal eliminated Croatia in the Euro 2016 round of 16 (1-0 AET), so 'Portugal did not' is false; the teams that never knocked Croatia out of a Euro R16 are Türkiye (2008 was a QF) and the Netherlands.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Answer should be Netherlands (or Türkiye).

### Row 18937 — Croatia (easy) — FAIL: fabricated — no 2010 playoff v Ukraine
**Q:** Which team eliminated Croatia in the 2010 World Cup playoff? **A:** Ukraine
**Options:** Ukraine | Greece | Iceland | Sweden
**Why it fails:** Croatia never played a 2010 World Cup qualifying playoff against Ukraine — they finished 3rd in their group and missed the playoff entirely. Fabricated.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Drop — there was no 2010 playoff.

### Row 18960 — Croatia (medium) — FAIL: wrong — Croatia beat Cameroon
**Q:** Which three teams beat Croatia in the 2014 World Cup group stage? **A:** Brazil, Mexico, Cameroon
**Options:** Brazil, Mexico, Cameroon | Brazil,  Netherlands,  Chile | Argentina, Nigeria, Iran | Netherlands, Chile
**Why it fails:** Croatia BEAT Cameroon 4-0 in 2014; they lost only to Brazil and Mexico.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_2014_FIFA_World_Cup
**Remedy:** Only Brazil and Mexico beat Croatia in 2014.

### Row 18962 — Croatia (medium) — FAIL: non-unique (3 tournaments not a final)
**Q:** Which tournament did Croatia NOT reach the final under Zlatko Dalić? **A:** 2022 World Cup
**Options:** 2022 World Cup | 2018 World Cup | 2020 Euros | 2024 Euros
**Why it fails:** Under Dalić, Croatia reached the final only at the 2018 WC; they did NOT reach the final at the 2022 WC, Euro 2020 OR Euro 2024 — three correct answers.
**Source:** https://en.wikipedia.org/wiki/Croatia_national_football_team
**Remedy:** Ask which one they DID reach (2018 WC).

### Row 18963 — Croatia (medium) — FAIL: wrong — Croatia didn't win the NL
**Q:** Which tournament did Croatia win under Zlatko Dalić? **A:** 2022-23 Nations League
**Options:** 2022-23 Nations League | 2018 FIFA World Cup | 2020 European Championship | 2022 FIFA World Cup
**Why it fails:** Croatia lost the 2022-23 Nations League final to Spain; Dalić did not win that title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Drop — Croatia were NL runners-up.

### Row 18964 — Croatia (medium) — FAIL: non-unique + false NL-win
**Q:** Which tournament did Croatia's Zlatko Dalić NOT reach the final under his management? **A:** 2022 World Cup
**Options:** 2022 World Cup | 2018 World Cup | 2020 Euros | 2023 Nations League
**Why it fails:** Both the 2022 WC (3rd) and Euro 2020 (R16) were not finals, so the answer isn't unique; the explanation also falsely says Croatia 'won the 2022-23 Nations League' (they lost the final).
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Make the answer unique and remove the NL-win claim.

### Row 18975 — Croatia (medium) — FAIL: wrong — Croatia drew Italy at Euro 2024
**Q:** Which two nations beat Croatia in the Euro 2024 group stage? **A:** Spain and Italy
**Options:** Spain and Italy | Germany and Italy | Spain and Albania | Italy and Albania
**Why it fails:** At Euro 2024 Croatia lost ONLY to Spain (0-3); the Italy match was a 1-1 DRAW (Zaccagni's stoppage-time equaliser) and Albania was a 2-2 draw. They did not lose to Italy.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Croatia lost only to Spain; Italy and Albania were draws.

### Row 18976 — Croatia (medium) — FAIL: wrong — Croatia drew Italy at Euro 2024
**Q:** Which two nations defeated Croatia in the Euro 2024 group stage? **A:** Spain and Italy
**Options:** Spain and Italy | Italy and Albania | Spain and Albania | Netherlands and Italy
**Why it fails:** At Euro 2024 Croatia lost ONLY to Spain (0-3); the Italy match was a 1-1 DRAW (Zaccagni's stoppage-time equaliser) and Albania was a 2-2 draw. They did not lose to Italy.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Croatia lost only to Spain; Italy and Albania were draws.

### Row 18979 — Croatia (medium) — FAIL: wrong — Croatia drew Italy at Euro 2024
**Q:** Which two teams beat Croatia in the Euro 2024 group stage? **A:** Spain and Italy
**Options:** Spain and Italy | Spain and Albania | Italy and Albania | Netherlands and Italy
**Why it fails:** At Euro 2024 Croatia lost ONLY to Spain (0-3); the Italy match was a 1-1 DRAW (Zaccagni's stoppage-time equaliser) and Albania was a 2-2 draw. They did not lose to Italy.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Croatia lost only to Spain; Italy and Albania were draws.

### Row 18980 — Croatia (medium) — FAIL: wrong — Croatia drew Italy at Euro 2024
**Q:** Which two teams defeated Croatia in the Euro 2024 group stage? **A:** Spain and Italy
**Options:** Spain and Italy | Spain and Portugal | Italy and Türkiye | Albania and Italy
**Why it fails:** At Euro 2024 Croatia lost ONLY to Spain (0-3); the Italy match was a 1-1 DRAW (Zaccagni's stoppage-time equaliser) and Albania was a 2-2 draw. They did not lose to Italy.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Croatia lost only to Spain; Italy and Albania were draws.

### Row 18981 — Croatia (easy) — FAIL: wrong — Croatia drew Italy at Euro 2024
**Q:** Which two teams did Croatia lose to at Euro 2024? **A:** Spain and Italy
**Options:** Spain and Italy | Germany and Italy | Spain and Portugal | Italy and Albania
**Why it fails:** At Euro 2024 Croatia lost ONLY to Spain (0-3); the Italy match was a 1-1 DRAW (Zaccagni's stoppage-time equaliser) and Albania was a 2-2 draw. They did not lose to Italy.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Croatia lost only to Spain; Italy and Albania were draws.

### Row 18982 — Croatia (medium) — FAIL: wrong — Croatia drew Italy at Euro 2024
**Q:** Which two teams did Croatia lose to in the Euro 2024 group stage? **A:** Spain and Italy
**Options:** Spain and Italy | Spain and Albania | Italy and Albania | Netherlands and Spain
**Why it fails:** At Euro 2024 Croatia lost ONLY to Spain (0-3); the Italy match was a 1-1 DRAW (Zaccagni's stoppage-time equaliser) and Albania was a 2-2 draw. They did not lose to Italy.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Croatia lost only to Spain; Italy and Albania were draws.

### Row 18983 — Croatia (easy) — FAIL: wrong — Croatia lost the 2023 NL final to Spain
**Q:** Which UEFA competition did Croatia win in 2023? **A:** Nations League
**Options:** Nations League | European Championship | Champions League | Europa League
**Why it fails:** Croatia LOST the 2023 Nations League final to Spain on penalties (the Netherlands was the semi-final); they hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 19006 — Croatia (easy) — FAIL: wrong — last group game was Italy (draw)
**Q:** Which UEFA team did Croatia beat in their final Euro 2024 group match? **A:** Albania
**Options:** Albania | Spain | Italy | Netherlands
**Why it fails:** At Euro 2024 Croatia lost ONLY to Spain (0-3); the Italy match was a 1-1 DRAW (Zaccagni's stoppage-time equaliser) and Albania was a 2-2 draw. They did not lose to Italy. The final group match was v Italy, not a win over Albania.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_UEFA_European_Championship
**Remedy:** Final group match was a 1-1 draw v Italy.

### Row 19007 — Croatia (easy) — FAIL: wrong — Croatia lost the 2023 NL final to Spain
**Q:** Which UEFA team did Croatia beat on penalties in the 2022-23 Nations League final? **A:** Netherlands
**Options:** Netherlands | Spain | Portugal | France
**Why it fails:** Croatia LOST the 2023 Nations League final to Spain on penalties (the Netherlands was the semi-final); they hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 19008 — Croatia (easy) — FAIL: wrong — Croatia lost the 2023 NL final to Spain
**Q:** Which UEFA team did Croatia beat on penalties in the 2023 Nations League final? **A:** the Netherlands
**Options:** the Netherlands | Portugal | Spain | England
**Why it fails:** Croatia LOST the 2023 Nations League final to Spain on penalties (the Netherlands was the semi-final); they hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 19016 — Croatia (hard) — FAIL: wrong — Croatia lost the 2023 NL final to Spain
**Q:** Which UEFA tournament did Croatia win in 2023 after a penalty shootout? **A:** Nations League
**Options:** Nations League | European Championship | World Cup | Champions League
**Why it fails:** Croatia LOST the 2023 Nations League final to Spain on penalties (the Netherlands was the semi-final); they hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 19026 — Croatia (medium) — FAIL: fabricated — no 2010 playoff v Ukraine
**Q:** Which World Cup did Croatia miss by losing a playoff to Ukraine? **A:** 2010 World Cup
**Options:** 2010 World Cup | 2014 World Cup | 2018 World Cup | 2022 World Cup
**Why it fails:** Croatia never lost a 2010 World Cup qualifying playoff to Ukraine — they finished 3rd in their group and missed the playoff entirely. Fabricated.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Drop — there was no 2010 playoff; Croatia simply finished 3rd.

### Row 19029 — Croatia (medium) — FAIL: non-unique + wrong explanation
**Q:** Which World Cup did Croatia qualify for directly under coach Dalić? **A:** 2026 World Cup
**Options:** 2026 World Cup | 2018 World Cup | 2022 World Cup | 2014 World Cup
**Why it fails:** Under Dalić, Croatia qualified DIRECTLY (group win) for BOTH 2022 and 2026, so the answer isn't unique; the explanation's claim that 'the other tournaments required playoffs' is false for 2022.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** 2022 and 2026 were both direct; only 2014/2018 were playoffs.

### Row 19030 — Croatia (easy) — FAIL: wrong explanation (beat Cameroon)
**Q:** Which World Cup group did Croatia exit in 2014? **A:** Group A
**Options:** Group A | Group B | Group C | Group D
**Why it fails:** Answer 'Group A' is correct, but the explanation's 'lost to Brazil, Mexico and Cameroon' is false — Croatia beat Cameroon 4-0.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_2014_FIFA_World_Cup
**Remedy:** Fix the explanation: Croatia lost only to Brazil and Mexico.

### Row 19033 — Croatia (hard) — FAIL: fabricated — no 2010 playoff v Ukraine
**Q:** Which World Cup qualifying playoff did Croatia lose to Ukraine? **A:** 2010 World Cup playoff
**Options:** 2010 World Cup playoff | 2014 World Cup playoff | 2018 World Cup playoff | 2022 World Cup playoff
**Why it fails:** Croatia never lost a 2010 World Cup qualifying playoff to Ukraine — they finished 3rd in their group and missed the playoff entirely. Fabricated.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Drop — there was no 2010 playoff; Croatia simply finished 3rd.

### Row 19039 — Croatia (medium) — FAIL: wrong — Croatia lost the 2023 NL final to Spain
**Q:** Which year did Croatia win the UEFA Nations League title? **A:** 2023
**Options:** 2023 | 2021 | 2022 | 2024
**Why it fails:** Croatia LOST the 2023 Nations League final to Spain on penalties (the Netherlands was the semi-final); they hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 19043 — Croatia (easy) — FAIL: wrong — Croatia lost the 2023 NL final to Spain
**Q:** Who did Croatia beat in the 2023 Nations League final? **A:** Netherlands
**Options:** Netherlands | Spain | Italy | Portugal
**Why it fails:** Croatia LOST the 2023 Nations League final to Spain on penalties (the Netherlands was the semi-final); they hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 19044 — Croatia (easy) — FAIL: wrong — Croatia lost the 2023 NL final to Spain
**Q:** Who did Croatia beat to win the 2023 Nations League final? **A:** The Netherlands
**Options:** The Netherlands | Spain | Portugal | Italy
**Why it fails:** Croatia LOST the 2023 Nations League final to Spain on penalties (the Netherlands was the semi-final); they hold no NL title.
**Source:** https://en.wikipedia.org/wiki/2023_UEFA_Nations_League_Final
**Remedy:** Netherlands was the semi-final; the final (lost) was v Spain.

### Row 19078 — Croatia (easy) — FAIL: fabricated — no 2010 playoff v Ukraine
**Q:** Why did Croatia miss the 2010 FIFA World Cup? **A:** Lost playoff to Ukraine
**Options:** Lost playoff to Ukraine | Lost playoff to Iceland | Lost playoff to Greece | Lost playoff to Russia
**Why it fails:** Croatia never lost a 2010 World Cup qualifying playoff to Ukraine — they finished 3rd in their group and missed the playoff entirely. Fabricated.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Drop — there was no 2010 playoff; Croatia simply finished 3rd.

### Row 19079 — Croatia (easy) — FAIL: fabricated — no 2010 playoff v Ukraine
**Q:** Why did Croatia miss the 2010 World Cup after the 2008 Euros? **A:** Lost playoff to Ukraine
**Options:** Lost playoff to Ukraine | Lost playoff to Greece | Lost playoff to Iceland | Lost playoff to Russia
**Why it fails:** Croatia never lost a 2010 World Cup qualifying playoff to Ukraine — they finished 3rd in their group and missed the playoff entirely. Fabricated.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Drop — there was no 2010 playoff; Croatia simply finished 3rd.

### Row 19096 — Croatia (easy) — FAIL: false premise (not the only team)
**Q:** Why was Croatia the only team to win all group matches at the 2018 World Cup? **A:** They won all three
**Options:** They won all three | They won all four | They won all five | They won all six
**Why it fails:** Croatia, Belgium AND Uruguay all won their three group games in 2018, so 'the only team to win all group matches' is false.
**Source:** https://en.wikipedia.org/wiki/Croatia_at_the_FIFA_World_Cup
**Remedy:** Remove the 'only team' framing.

## Rows 19102–20581 (Denmark) — 182 FAIL-liveness

Recurring Denmark defect clusters: (1) **DBU HQ 'in Copenhagen'** — it's in BRØNDBY (~40 rows; Brøndby is often even a distractor); (2) **'Telia Parken' distractor** = Parken Stadium (alias → non-unique, ~35 rows); (3) **'Denmark qualified for 2026'** — FALSE, they lost the playoff to Czechia (parallel to a fake-tournament cluster); (4) **'Hjulmand leads the 2026 cycle'** — he resigned in 2024; Brian Riemer leads it (~35 rows); (5) **'Eriksen 2nd-highest scorer'** — he's 5th (~25 rows); (6) **'40+ goals' non-unique** when Tomasson (52) is a distractor; (7) **'peak/highest FIFA ranking 10th'** — their peak was 6th (1996); (8) **Højlund 'plays for Manchester United'** — he moved to Napoli/Serie A (permanent 3 Jun 2026); (9) date corruption (`02-Jan`=2-1, `04-Jan`=4-1, `01-Jan`=1-1); (10) wrong cap stats (Kjær ~115 not 130+ in 2022; Poulsen ~35 not 70 in 2018) and self-referential/non-unique items.

### Row 19119 — Denmark (easy) — FAIL: date corruption (02-Jan = 2-1)
**Q:** At Euro 2020, Denmark lost to England in the semi-final by what score? **A:** 02-Jan
**Options:** 02-Jan | 1-0 | 2-0 | 3-1
**Why it fails:** Answer '02-Jan' is a mangled '2-1' (lost 2-1 to England, Euro 2020 semi).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Restore '2-1'.

### Row 19145 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** At the 2022 FIFA World Cup, Denmark's football federation headquarters were in which city? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Herning
**Why it fails:** The Danish Football Association (DBU) headquarters are at Fodboldens Hus in BRØNDBY, not Copenhagen.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19173 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** At which stadium did Denmark host its 2022 World Cup qualifiers? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadion | Aalborg Portland Park
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (Telia was the stadium's sponsor name 2014-2020), so the answer is non-unique — two options name the same venue.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option — it's the same stadium as Parken.

### Row 19178 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** At which stadium do Denmark host all their World Cup qualifiers? **A:** Parken Stadium
**Options:** Parken Stadium | Brøndby Stadium | Telia Parken | Aalborg Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (Telia was the stadium's sponsor name 2014-2020), so the answer is non-unique — two options name the same venue.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option — it's the same stadium as Parken.

### Row 19188 — Denmark (easy) — FAIL: date corruption (04-Jan = 4-1)
**Q:** By what score did Denmark beat Russia at Euro 2020? **A:** 04-Jan
**Options:** 04-Jan | 3-1 | 2-0 | 3-0
**Why it fails:** Answer '04-Jan' is a mangled '4-1' (beat Russia 4-1, Euro 2020).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Restore '4-1'.

### Row 19191 — Denmark (easy) — FAIL: date corruption (04-Jan = 4-1)
**Q:** Denmark beat Russia by what scoreline at Euro 2020? **A:** 04-Jan
**Options:** 04-Jan | 3-1 | 2-0 | 3-0
**Why it fails:** Answer '04-Jan' is a mangled '4-1' (beat Russia 4-1, Euro 2020).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Restore '4-1'.

### Row 19201 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Denmark hosted their 2022 World Cup qualifier vs Scotland at which stadium? **A:** Parken Stadium
**Options:** Parken Stadium | Brøndby Stadium | Aalborg Stadion | Telia Parken
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (Telia was the stadium's sponsor name 2014-2020), so the answer is non-unique — two options name the same venue.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option — it's the same stadium as Parken.

### Row 19205 — Denmark (easy) — FAIL: self-referential answer
**Q:** Denmark lost 2-0 to Germany in the Euro 2024 round of 16. Which nation lost 2-1 to England in the Euro 2020 semi-final? **A:** Denmark
**Options:** Denmark | Czech Republic | Wales | Russia
**Why it fails:** The question (in a Denmark category) asks 'which nation lost 2-1 to England in the Euro 2020 semi-final?' and the answer is Denmark itself — a giveaway derivable from the category.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Drop — self-referential.

### Row 19210 — Denmark (easy) — FAIL: date corruption (01-Jan = 1-1)
**Q:** Denmark lost to Croatia on penalties in the 2018 World Cup round of 16 after what final score? **A:** 01-Jan
**Options:** 01-Jan | 0-0 | 2-1 | 2-2
**Why it fails:** Answer '01-Jan' is a mangled '1-1' (v Croatia 1-1, 2018 R16).
**Source:** https://en.wikipedia.org/wiki/Denmark_at_the_FIFA_World_Cup
**Remedy:** Restore '1-1'.

### Row 19213 — Denmark (easy) — FAIL: non-unique (Switzerland also qualified 2010)
**Q:** Denmark qualified for the 2010 FIFA World Cup via UEFA. Which nation also qualified through UEFA for 2010? **A:** England
**Options:** England | Republic of Ireland | Switzerland | Scotland
**Why it fails:** England AND Switzerland both qualified via UEFA for the 2010 World Cup, so two options are correct (Ireland and Scotland did not).
**Source:** https://en.wikipedia.org/wiki/Denmark_at_the_FIFA_World_Cup
**Remedy:** Replace Switzerland with a UEFA team that missed 2010.

### Row 19227 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Denmark's 2022 World Cup qualifying campaign was based at which stadium? **A:** Parken Stadium
**Options:** Parken Stadium | Brøndby Stadion | Telia Parken | Aalborg Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (Telia was the stadium's sponsor name 2014-2020), so the answer is non-unique — two options name the same venue.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option — it's the same stadium as Parken.

### Row 19229 — Denmark (hard) — FAIL: false premise — Denmark missed 2026
**Q:** Denmark's 2026 World Cup qualification came after which earlier successful UEFA playoff? **A:** The 2018 playoff
**Options:** The 2018 playoff | The 2010 playoff | The 2022 playoff | The 2014 playoff
**Why it fails:** Denmark did NOT qualify for the 2026 World Cup — they lost the UEFA playoff final to Czechia (2-2, 3-1 pens, 31 Mar 2026). There was no '2026 World Cup qualification' to follow up the 2018 playoff.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_C
**Remedy:** Drop — Denmark failed to reach the 2026 World Cup.

### Row 19247 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** For 2022 World Cup qualifiers, where did Denmark host all home matches? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadion | Odense Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (Telia was the 2014-2020 sponsor name), so two options name the same venue — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19248 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** For 2022 World Cup qualifiers, which stadium hosted all Denmark's home matches? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadion | Odense Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (Telia was the 2014-2020 sponsor name), so two options name the same venue — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19249 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** For a 2026 World Cup qualifier, which Danish stadium with a 38,065 capacity hosts the match? **A:** Parken Stadium
**Options:** Parken Stadium | Brøndby Stadium | Aalborg Portland Park | Telia Parken
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (Telia was the 2014-2020 sponsor name), so two options name the same venue — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19252 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** For Denmark's 2022 World Cup qualifiers, where were all home matches played? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadion | Odense Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (Telia was the 2014-2020 sponsor name), so two options name the same venue — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19256 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** For the 2022 FIFA World Cup, where were the Danish FA (DBU) headquarters located? **A:** Copenhagen
**Options:** Copenhagen | Brøndby | Aarhus | Odense
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus, DBU Allé 1), not Copenhagen — and several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19258 — Denmark (easy) — FAIL: outdated — Højlund now plays for Napoli
**Q:** For the 2026 cycle, which Danish striker plays for Manchester United? **A:** Rasmus Højlund
**Options:** Rasmus Højlund | Yussuf Poulsen | Martin Braithwaite | Mikkel Damsgaard
**Why it fails:** As of 2026 Rasmus Højlund plays for NAPOLI (Serie A) — he moved on loan in summer 2025, made permanent on 3 June 2026 — not Manchester United.
**Source:** https://en.wikipedia.org/wiki/Rasmus_H%C3%B8jlund
**Remedy:** Answer/clue should say Napoli (Serie A), not Manchester United.

### Row 19259 — Denmark (easy) — FAIL: outdated — Højlund now plays for Napoli
**Q:** For the 2026 cycle, which Denmark striker plays for Manchester United? **A:** Rasmus Højlund
**Options:** Rasmus Højlund | Yussuf Poulsen | Martin Braithwaite | Mikkel Damsgaard
**Why it fails:** As of 2026 Rasmus Højlund plays for NAPOLI (Serie A) — he moved on loan in summer 2025, made permanent on 3 June 2026 — not Manchester United.
**Source:** https://en.wikipedia.org/wiki/Rasmus_H%C3%B8jlund
**Remedy:** Answer/clue should say Napoli (Serie A), not Manchester United.

### Row 19260 — Denmark (easy) — FAIL: outdated — Højlund (Napoli) is in Serie A
**Q:** For the 2026 cycle, which league does NOT supply Denmark's main squad? **A:** Serie A
**Options:** Serie A | Premier League | La Liga | Bundesliga
**Why it fails:** Højlund moved to Napoli (Serie A) by 2026, so Serie A IS represented in Denmark's squad — the 'not Serie A' answer is now false.
**Source:** https://en.wikipedia.org/wiki/Rasmus_H%C3%B8jlund
**Remedy:** Serie A is now represented (Højlund).

### Row 19262 — Denmark (medium) — FAIL: wrong — Hjulmand isn't the 2026 manager
**Q:** For which FIFA World Cup cycle is Kasper Hjulmand Denmark's manager? **A:** The 2026 cycle
**Options:** The 2026 cycle | The 2022 cycle | The 2030 cycle | The 2018 cycle
**Why it fails:** Kasper Hjulmand RESIGNED in July 2024 after Euro 2024; Brian Riemer (from Oct 2024) leads Denmark's 2026 cycle.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer manages the 2026 cycle.

### Row 19279 — Denmark (easy) — FAIL: false premise — Denmark missed 2026
**Q:** How did Denmark qualify for the 2026 FIFA World Cup? **A:** Through UEFA qualification
**Options:** Through UEFA qualification | Winning a playoff | Via inter-confederation playoff | As host nation
**Why it fails:** Denmark did NOT qualify for the 2026 World Cup (lost the UEFA playoff final to Czechia on penalties).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_C
**Remedy:** Drop — Denmark failed to qualify for 2026.

### Row 19293 — Denmark (hard) — FAIL: wrong — Russia was the group stage
**Q:** How many goals did Denmark score in the Euro 2020 knockout stage? **A:** 10 goals
**Options:** 10 goals | 6 goals | 8 goals | 12 goals
**Why it fails:** Denmark's Euro 2020 KNOCKOUT goals were 4 (Wales) + 2 (Czechia) + 1 (England) = 7; the 4 v Russia came in the GROUP stage, so '10' is wrong (and 7 isn't even an option).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Answer: 7 (Wales 4, Czechia 2, England 1).

### Row 19310 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** In 2018, which city was the DBU headquarters based in for Denmark's World Cup campaign? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Aalborg
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus, DBU Allé 1), not Copenhagen — and several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19313 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** In 2022 World Cup qualifying, where did Denmark host all their home matches? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadion | Aarhus Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (Telia was the 2014-2020 sponsor name), so two options name the same venue — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19314 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** In 2022 World Cup qualifying, which stadium hosted all Denmark's home matches? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadion | Aarhus Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (Telia was the 2014-2020 sponsor name), so two options name the same venue — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19325 — Denmark (easy) — FAIL: wrong — Denmark had 5 points in 2018
**Q:** In Denmark's 2018 World Cup group, what was their points total? **A:** 4 points
**Options:** 4 points | 3 points | 5 points | 6 points
**Why it fails:** Denmark earned 5 points in the 2018 group (beat Peru 1-0, drew Australia 1-1 AND France 0-0) — one win and TWO draws, not 4 points.
**Source:** https://en.wikipedia.org/wiki/Denmark_at_the_FIFA_World_Cup
**Remedy:** Answer: 5 points.

### Row 19330 — Denmark (medium) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** In Denmark's 2022 World Cup group stage, which player is their second-highest all-time scorer? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Poul Nielsen
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer; the top two are Tomasson and Poul Nielsen (52 each, joint), ahead of Pauli Jørgensen and Ole Madsen.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 19333 — Denmark (easy) — FAIL: outdated — Højlund now plays for Napoli
**Q:** In Denmark's 2026 World Cup cycle, which striker plays for Manchester United? **A:** Rasmus Højlund
**Options:** Rasmus Højlund | Yussuf Poulsen | Martin Braithwaite | Mikkel Damsgaard
**Why it fails:** As of 2026 Rasmus Højlund plays for NAPOLI (Serie A) — he moved on loan in summer 2025, made permanent on 3 June 2026 — not Manchester United.
**Source:** https://en.wikipedia.org/wiki/Rasmus_H%C3%B8jlund
**Remedy:** Answer/clue should say Napoli (Serie A), not Manchester United.

### Row 19345 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** In the 2018 World Cup, where were Denmark's FA headquarters compared to Germany's? **A:** Copenhagen
**Options:** Copenhagen | Berlin | Munich | Frankfurt
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus, DBU Allé 1), not Copenhagen — and several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19348 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** In the 2022 FIFA World Cup qualifiers, Denmark's FA headquarters were in which city? **A:** Copenhagen
**Options:** Copenhagen | Brøndby | Odense | Aalborg
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus, DBU Allé 1), not Copenhagen — and several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19349 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** In the 2022 FIFA World Cup qualifiers, where did Denmark play all their home matches? **A:** Parken Stadium
**Options:** Parken Stadium | Brøndby Stadion | Arena Nord | Telia Parken
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (Telia was the 2014-2020 sponsor name), so two options name the same venue — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19353 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** In the 2022 World Cup qualifiers, where did the Danish FA base its operations? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Herning
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus, DBU Allé 1), not Copenhagen — and several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19356 — Denmark (medium) — FAIL: wrong — Germany's result was better
**Q:** In the 2022 World Cup, which nation had a worse group stage result than Denmark? **A:** Germany
**Options:** Germany | Australia | France | Belgium
**Why it fails:** In 2022 Germany finished 3rd with 4 points; Denmark finished last with 1 point. Germany's group result was BETTER than Denmark's, not worse (no listed nation did worse than Denmark).
**Source:** https://en.wikipedia.org/wiki/Denmark_at_the_FIFA_World_Cup
**Remedy:** Drop — none of the options had a worse group result than Denmark.

### Row 19368 — Denmark (hard) — FAIL: wrong — Denmark's peak was 6th, not 10th
**Q:** In what year did Denmark reach their peak FIFA ranking of 10th? **A:** 2022
**Options:** 2022 | 2021 | 2023 | 2018
**Why it fails:** Denmark's highest-EVER FIFA ranking is 6th (reached in 1993 and 1996); the 10th in 2022 was a recent high, not their all-time peak. 'Highest/peak ranking of 10th' is false.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** 10th (2022) was a recent high; their all-time best was 6th in the 1990s.

### Row 19372 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** In which city are the DBU headquarters for the Danish national team? **A:** Copenhagen
**Options:** Copenhagen | Århus | Odense | Aalborg
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus, DBU Allé 1), not Copenhagen — and several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19373 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** In which city are the DBU's headquarters for Denmark's World Cup campaigns? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Herning
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus, DBU Allé 1), not Copenhagen — and several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19375 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** In which city did Denmark's FA plan their 2022 World Cup qualifying campaign? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Aalborg
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus, DBU Allé 1), not Copenhagen — and several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19376 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** In which city does the Danish FA base its World Cup qualifier operations? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Herning
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus, DBU Allé 1), not Copenhagen — and several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19377 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** In which city does the Danish FA plan its World Cup campaigns? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Aalborg
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus, DBU Allé 1), not Copenhagen — and several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19378 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** In which city have Denmark's World Cup campaigns been planned since 2008? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Aalborg
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus, DBU Allé 1), not Copenhagen — and several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19379 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** In which city is the DBU based when Denmark plays at a World Cup? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Aalborg
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus, DBU Allé 1), not Copenhagen — and several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19428 — Denmark (hard) — FAIL: wrong — Denmark's peak was 6th, not 10th
**Q:** In which year did Denmark achieve their highest FIFA ranking of 10th? **A:** 2022
**Options:** 2022 | 2018 | 2020 | 2021
**Why it fails:** Denmark's highest-EVER FIFA ranking is 6th (reached in 1993 and 1996); the 10th in 2022 was a recent high, not their all-time peak. 'Highest/peak ranking of 10th' is false.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** 10th (2022) was a recent high; their all-time best was 6th in the 1990s.

### Row 19439 — Denmark (hard) — FAIL: wrong — Denmark's peak was 6th, not 10th
**Q:** In which year did Denmark's men's team reach its peak FIFA ranking of 10th? **A:** 2022
**Options:** 2022 | 2018 | 2020 | 2024
**Why it fails:** Denmark's highest-EVER FIFA ranking is 6th (reached in 1993 and 1996); the 10th in 2022 was a recent high, not their all-time peak. 'Highest/peak ranking of 10th' is false.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** 10th (2022) was a recent high; their all-time best was 6th in the 1990s.

### Row 19446 — Denmark (medium) — FAIL: wrong — Hjulmand isn't the 2026-cycle manager
**Q:** In which year did Kasper Hjulmand begin managing Denmark for the 2026 World Cup cycle? **A:** 2020
**Options:** 2020 | 2016 | 2018 | 2022
**Why it fails:** Hjulmand resigned in July 2024; he did not manage Denmark's 2026 World Cup cycle (Brian Riemer does). The '2026 World Cup cycle' framing is false for Hjulmand.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Drop the 2026-cycle framing; Hjulmand managed 2020-2024.

### Row 19449 — Denmark (hard) — FAIL: wrong — highest ranking (6th) was in the 1990s
**Q:** In which year did the Denmark national team reach its highest FIFA ranking? **A:** 2022
**Options:** 2022 | 2018 | 2020 | 2024
**Why it fails:** Denmark's HIGHEST FIFA ranking was 6th (1993/1996), reached in the 1990s — not 2022. The 10th in 2022 was only a recent high.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Answer for 'highest ever' would be 1996 (6th), not 2022.

### Row 19457 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Since 2008, Denmark's home World Cup qualifiers have all been at which stadium? **A:** Parken Stadium
**Options:** Parken Stadium | Brøndby Stadion | Telia Parken | Aalborg Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19459 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Since 2022, where do Denmark play all FIFA World Cup home qualifiers? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadium | Odense Stadium
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19468 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** What is Denmark's national stadium for 2022 World Cup qualifiers? **A:** Parken Stadium
**Options:** Parken Stadium | Brøndby Stadion | Telia Parken | Odense Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19478 — Denmark (medium) — FAIL: date corruption (04-Jan = 4-1)
**Q:** What was Denmark's exact scoreline against Russia at Euro 2020? **A:** 04-Jan
**Options:** 04-Jan | 3-1 | 2-0 | 3-0
**Why it fails:** Answer '04-Jan' is a mangled '4-1' (beat Russia 4-1, Euro 2020).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Restore '4-1'.

### Row 19479 — Denmark (medium) — FAIL: date corruption (02-Jan = 2-1)
**Q:** What was Denmark's exact scoreline against the Czech Republic in the Euro 2020 quarter-final? **A:** 02-Jan
**Options:** 02-Jan | 3-1 | 1-0 | 2-0
**Why it fails:** Answer '02-Jan' is a mangled '2-1' (beat Czechia 2-1, Euro 2020 QF).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Restore '2-1'.

### Row 19481 — Denmark (medium) — FAIL: date corruption (02-Jan = 2-1)
**Q:** What was Denmark's exact scoreline in their Euro 2020 quarter-final win? **A:** 02-Jan
**Options:** 02-Jan | 1-0 | 3-1 | 2-0
**Why it fails:** Answer '02-Jan' is a mangled '2-1' (beat Czechia 2-1, Euro 2020 QF).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Restore '2-1'.

### Row 19482 — Denmark (easy) — FAIL: date corruption (02-Jan = 2-1)
**Q:** What was Denmark's final score in their Euro 2020 semi-final loss? **A:** 02-Jan
**Options:** 02-Jan | 1-0 | 3-2 | 2-0
**Why it fails:** Answer '02-Jan' is a mangled '2-1' (lost 2-1 to England, Euro 2020 semi).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Restore '2-1'.

### Row 19492 — Denmark (medium) — FAIL: date corruption (02-Jan = 2-1)
**Q:** What was the score when Denmark beat Czech Republic in the Euro 2020 quarter-final? **A:** 02-Jan
**Options:** 02-Jan | 1-0 | 3-1 | 2-0
**Why it fails:** Answer '02-Jan' is a mangled '2-1' (beat Czechia 2-1, Euro 2020 QF).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Restore '2-1'.

### Row 19509 — Denmark (hard) — FAIL: wrong — Denmark's peak was 6th, not 10th
**Q:** When did Denmark achieve their highest FIFA ranking of 10th? **A:** In 2022
**Options:** In 2022 | In 2018 | In 2020 | In 2021
**Why it fails:** Denmark's highest-EVER FIFA ranking is 6th (reached in 1993 and 1996); the 10th in 2022 was a recent high, not their all-time peak. 'Highest/peak ranking of 10th' is false.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** 10th (2022) was a recent high; their all-time best was 6th in the 1990s.

### Row 19542 — Denmark (medium) — FAIL: false premise — Denmark missed 2026
**Q:** When did Denmark qualify for the 2026 FIFA World Cup? **A:** 2026
**Options:** 2026 | 2022 | 2018 | 2014
**Why it fails:** Denmark did NOT qualify for the 2026 World Cup (lost the UEFA playoff final to Czechia on penalties, 31 Mar 2026).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_C
**Remedy:** Drop — Denmark failed to qualify for 2026.

### Row 19575 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Where are Denmark's football federation headquarters located for the 2026 World Cup? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Brøndby
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19576 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Where are Denmark's World Cup team headquarters based? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Aalborg
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19577 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Where are the Danish FA (DBU) headquarters based? **A:** Copenhagen
**Options:** Copenhagen | Århus | Odense | Herning
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19579 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Where are the Danish Football Association (DBU) headquarters located? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Herning
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19580 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Where are the DBU headquarters for Denmark's World Cup team? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Aalborg
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19582 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Where did Denmark host all their 2018 FIFA World Cup qualifiers? **A:** Parken Stadium
**Options:** Parken Stadium | Brøndby Stadion | Telia Parken | Aarhus Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19583 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Where did Denmark host all their 2022 FIFA World Cup qualifiers? **A:** Parken Stadium
**Options:** Parken Stadium | Brøndby Stadion | Aalborg Portland Park | Telia Parken
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19587 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Where did Denmark host France in their 2022 World Cup qualifier? **A:** Parken Stadium
**Options:** Parken Stadium | Brøndby Stadion | Telia Parken | Aalborg Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19588 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Where did Denmark host its 2022 World Cup qualifiers? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadion | Aarhus Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19590 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Where did Denmark host their 2022 World Cup qualifier against Scotland? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadion | Arena Nord
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19591 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Where did Denmark host their 2022 World Cup qualifier against Sweden? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadion | Arena Nordvest
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19593 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Where did Denmark host their 2022 World Cup qualifying matches? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadion | Aalborg Portland Park
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19594 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Where did Denmark play all their 2022 FIFA World Cup home qualifiers? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadion | Odense Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19596 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Where did Denmark play their 2022 World Cup qualifying home matches? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadion | Aalborg Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19598 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Where do Denmark host all home 2022 FIFA World Cup qualifiers? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadion | Odense Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19600 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Where do Denmark play all their 2026 World Cup qualifying home matches? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadion | Odense Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19602 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Where do Denmark play all their FIFA World Cup qualifying home matches? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadion | MCH Arena
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 19604 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Where is the Danish FA (DBU) headquarters for the 2026 World Cup cycle? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Herning
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19605 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Where is the Danish FA's headquarters for World Cup planning? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Herning
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19606 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Where is the Danish Football Association (DBU) headquarters located? **A:** Copenhagen
**Options:** Copenhagen | Brøndby | Aarhus | Odense
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19607 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Where was Denmark's 2022 World Cup squad officially selected? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Herning
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19608 — Denmark (medium) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Where was Denmark's FA based during their 2018 World Cup qualification group win? **A:** Copenhagen
**Options:** Copenhagen | Århus | Odense | Aalborg
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19609 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Where was the DBU based when Denmark qualified for the 2018 World Cup? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Aalborg
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19610 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Where were the Danish FA (DBU) headquarters located during the 2018 World Cup? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Aalborg
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19611 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Where were the Danish FA (DBU) headquarters located during the 2022 World Cup? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Brøndby | Herning
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19612 — Denmark (medium) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Where were the DBU headquarters during Denmark's 2018 World Cup group stage? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Herning
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19616 — Denmark (hard) — FAIL: non-unique (two 2022 results listed)
**Q:** Which 2022 World Cup group stage result was Denmark's? **A:** Drew 0-0 with Tunisia
**Options:** Drew 0-0 with Tunisia | Beat Peru 1-0 | Drew 1-1 with Australia | Lost 1-0 to Australia
**Why it fails:** Both 'Drew 0-0 with Tunisia' AND 'Lost 1-0 to Australia' were Denmark's 2022 group results (the Australia loss was 2022, not 2018), so two options are correct; the explanation wrongly assigns the Australia loss to 2018.
**Source:** https://en.wikipedia.org/wiki/Denmark_at_the_FIFA_World_Cup
**Remedy:** Keep only one 2022 result among the options.

### Row 19627 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Which city did Denmark's 2018 World Cup squad selection originate from? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Aalborg
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19628 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Which city hosts the Danish FA (DBU) headquarters for World Cup planning? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Brøndby
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19629 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Which city hosts the Danish FA (DBU) headquarters? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Brondby
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19630 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Which city hosts the Danish FA headquarters for World Cup qualifiers? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Herning
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19631 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Which city hosts the Danish FA's headquarters for World Cup operations? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Aalborg
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19632 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Which city housed the Danish FA during the 2022 World Cup? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Herning
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19643 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Which Danish city hosts the DBU headquarters for FIFA World Cup planning? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Aalborg
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19644 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Which Danish city hosts the DBU headquarters for their World Cup campaigns? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Aalborg
**Why it fails:** The DBU's headquarters are in BRØNDBY (Fodboldens Hus), not Copenhagen — several of these rows even list Brøndby as a distractor.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19665 — Denmark (easy) — FAIL: wrong stat — Poulsen had ~35 caps in 2018
**Q:** Which Danish forward had over 70 caps at the 2018 World Cup? **A:** Yussuf Poulsen
**Options:** Yussuf Poulsen | Martin Braithwaite | Christian Eriksen | Mikkel Damsgaard
**Why it fails:** Yussuf Poulsen (debut 2013) had roughly 35 caps at the 2018 World Cup, not 70+ (he passed ~70 only years later). No forward had 70+ caps in 2018.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team
**Remedy:** Drop the '70 caps' claim, or it describes his later total.

### Row 19710 — Denmark (easy) — FAIL: non-unique (Tomasson also 40+)
**Q:** Which Danish player scored 40+ goals by the 2022 World Cup? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Brian Laudrup
**Why it fails:** Both Eriksen (~40) and Tomasson (52, a listed option) scored 40+ goals by 2022, so the answer isn't unique.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Replace Tomasson, or specify a current player.

### Row 19720 — Denmark (easy) — FAIL: wrong — Eriksen is the squad's TOP scorer
**Q:** Which Danish player was their second-highest scorer in the 2022 World Cup squad? **A:** Christian Eriksen
**Options:** Christian Eriksen | Kasper Dolberg | Martin Braithwaite | Yussuf Poulsen
**Why it fails:** Among the 2022 squad Eriksen (~40 goals) was the HIGHEST scorer, not second; and all-time he is 5th, not 2nd.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** He was the leading scorer in that squad.

### Row 19721 — Denmark (easy) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** Which Danish player, with 40+ goals, is their second-highest scorer? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Brian Laudrup
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer; Tomasson and Poul Nielsen (52, joint) lead, then Pauli Jørgensen and Ole Madsen.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 19748 — Denmark (medium) — FAIL: non-unique (failed to beat all three)
**Q:** Which Denmark 2022 World Cup group stage opponent did they fail to beat? **A:** Tunisia
**Options:** Tunisia | Peru | Australia | France
**Why it fails:** Denmark won zero 2022 group games — they failed to beat Tunisia (drew), France (lost) AND Australia (lost), so three options are correct.
**Source:** https://en.wikipedia.org/wiki/Denmark_at_the_FIFA_World_Cup
**Remedy:** Keep only one 2022 opponent among the options.

### Row 19751 — Denmark (easy) — FAIL: wrong stat — Kjær had ~115 caps in 2022
**Q:** Which Denmark captain had over 130 caps at the 2022 World Cup? **A:** Simon Kjær
**Options:** Simon Kjær | Christian Eriksen | Kasper Schmeichel | Yussuf Poulsen
**Why it fails:** Simon Kjær reached 125 caps only in June 2023, so at the 2022 World Cup he had ~115 — not over 130 (he finished his career on 132).
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team
**Remedy:** He passed 130 only at the very end of his career.

### Row 19752 — Denmark (easy) — FAIL: wrong stat — Kjær had ~115 caps in 2022
**Q:** Which Denmark captain had over 130 caps by the 2022 World Cup? **A:** Simon Kjær
**Options:** Simon Kjær | Christian Eriksen | Kasper Schmeichel | Yussuf Poulsen
**Why it fails:** Simon Kjær reached 125 caps only in June 2023, so at the 2022 World Cup he had ~115 — not over 130 (he finished his career on 132).
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team
**Remedy:** He passed 130 only at the very end of his career.

### Row 19785 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Which Denmark city hosts DBU headquarters for 2022 World Cup qualifiers? **A:** Copenhagen
**Options:** Copenhagen | Århus | Odense | Esbjerg
**Why it fails:** The DBU's headquarters are in BRØNDBY, not Copenhagen.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19786 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Which Denmark city hosts DBU headquarters for World Cup planning? **A:** Copenhagen
**Options:** Copenhagen | Aarhus | Odense | Aalborg
**Why it fails:** The DBU's headquarters are in BRØNDBY, not Copenhagen.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 19813 — Denmark (easy) — FAIL: wrong stat — Poulsen had ~35 caps in 2018
**Q:** Which Denmark forward had over 70 caps at the 2018 World Cup? **A:** Yussuf Poulsen
**Options:** Yussuf Poulsen | Martin Braithwaite | Mikkel Damsgaard | Joakim Mæhle
**Why it fails:** Yussuf Poulsen had roughly 35 caps at the 2018 World Cup, not 70+.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team
**Remedy:** Drop the '70 caps' claim.

### Row 19840 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads the 2026 cycle
**Q:** Which Denmark manager began his tenure for the 2026 World Cup cycle? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Kasper Hjulmand resigned in July 2024 after Euro 2024; Brian Riemer (appointed Oct 2024) leads Denmark's 2026 cycle, not Hjulmand.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer.

### Row 19847 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads the 2026 cycle
**Q:** Which Denmark manager is leading the team for the 2026 FIFA World Cup cycle? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Kasper Hjulmand resigned in July 2024 after Euro 2024; Brian Riemer (appointed Oct 2024) leads Denmark's 2026 cycle, not Hjulmand.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer.

### Row 19848 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads the 2026 cycle
**Q:** Which Denmark manager is leading the team for the 2026 World Cup? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | John Jensen
**Why it fails:** Kasper Hjulmand resigned in July 2024 after Euro 2024; Brian Riemer (appointed Oct 2024) leads Denmark's 2026 cycle, not Hjulmand.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer.

### Row 19849 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads the 2026 cycle
**Q:** Which Denmark manager is leading the team's 2026 World Cup campaign? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Kasper Hjulmand resigned in July 2024 after Euro 2024; Brian Riemer (appointed Oct 2024) leads Denmark's 2026 cycle, not Hjulmand.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer.

### Row 19850 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads the 2026 cycle
**Q:** Which Denmark manager is leading their 2026 FIFA World Cup qualifying campaign? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Kasper Hjulmand resigned in July 2024 after Euro 2024; Brian Riemer (appointed Oct 2024) leads Denmark's 2026 cycle, not Hjulmand.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer.

### Row 19852 — Denmark (medium) — FAIL: wrong — Riemer (not Hjulmand) leads the 2026 cycle
**Q:** Which Denmark manager is leading their 2026 World Cup qualification campaign? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Kasper Hjulmand resigned in July 2024 after Euro 2024; Brian Riemer (appointed Oct 2024) leads Denmark's 2026 cycle, not Hjulmand.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer.

### Row 19854 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads the 2026 cycle
**Q:** Which Denmark manager is set to lead the team for the 2026 FIFA World Cup cycle? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Kasper Hjulmand resigned in July 2024 after Euro 2024; Brian Riemer (appointed Oct 2024) leads Denmark's 2026 cycle, not Hjulmand.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer.

### Row 19859 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which Denmark manager led the team for the 2026 World Cup cycle? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer (Oct 2024) leads Denmark's 2026 cycle — Hjulmand does not manage 2026.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer for the 2026 cycle.

### Row 19860 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which Denmark manager led the team into the 2026 World Cup cycle? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Olsen
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer (Oct 2024) leads Denmark's 2026 cycle — Hjulmand does not manage 2026.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer for the 2026 cycle.

### Row 19861 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which Denmark manager led the team through the 2026 World Cup cycle? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | John Jensen
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer (Oct 2024) leads Denmark's 2026 cycle — Hjulmand does not manage 2026.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer for the 2026 cycle.

### Row 19862 — Denmark (medium) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which Denmark manager led their 2026 World Cup qualification campaign? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | John Jensen
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer (Oct 2024) leads Denmark's 2026 cycle — Hjulmand does not manage 2026.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer for the 2026 cycle.

### Row 19865 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which Denmark manager led them to Euro 2020 and is aiming for 2026? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | John Jensen
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer (Oct 2024) leads Denmark's 2026 cycle — Hjulmand does not manage 2026.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer for the 2026 cycle.

### Row 19876 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which Denmark manager oversaw their 2026 World Cup qualifying campaign? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer (Oct 2024) leads Denmark's 2026 cycle — Hjulmand does not manage 2026.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer for the 2026 cycle.

### Row 19886 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which Denmark manager was appointed for the 2026 World Cup cycle? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer (Oct 2024) leads Denmark's 2026 cycle — Hjulmand does not manage 2026.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer for the 2026 cycle.

### Row 19887 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which Denmark manager was appointed in 2020 for the 2026 World Cup? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer (Oct 2024) leads Denmark's 2026 cycle — Hjulmand does not manage 2026.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer for the 2026 cycle.

### Row 19889 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which Denmark manager was appointed to lead their 2026 World Cup campaign? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer (Oct 2024) leads Denmark's 2026 cycle — Hjulmand does not manage 2026.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer for the 2026 cycle.

### Row 19891 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which Denmark manager was in charge for the 2026 World Cup cycle? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer (Oct 2024) leads Denmark's 2026 cycle — Hjulmand does not manage 2026.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer for the 2026 cycle.

### Row 19893 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which Denmark manager will lead the team in 2026 World Cup qualifiers? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer (Oct 2024) leads Denmark's 2026 cycle — Hjulmand does not manage 2026.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer for the 2026 cycle.

### Row 19894 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which Denmark manager will lead the team in the 2026 World Cup cycle? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer (Oct 2024) leads Denmark's 2026 cycle — Hjulmand does not manage 2026.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer for the 2026 cycle.

### Row 19895 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which Denmark manager will lead them in the 2026 World Cup? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | John Jensen
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer (Oct 2024) leads Denmark's 2026 cycle — Hjulmand does not manage 2026.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer for the 2026 cycle.

### Row 19904 — Denmark (easy) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** Which Denmark midfielder became their second-highest scorer by 2022? **A:** Christian Eriksen
**Options:** Christian Eriksen | Michael Laudrup | Brian Laudrup | Jon Dahl Tomasson
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer; Tomasson and Poul Nielsen (52, joint) lead, then Pauli Jørgensen and Ole Madsen — Eriksen is not second.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 19907 — Denmark (easy) — FAIL: non-unique (Eriksen also a midfielder with 80+)
**Q:** Which Denmark midfielder had over 80 caps by the 2022 World Cup? **A:** Pierre-Emile Højbjerg
**Options:** Pierre-Emile Højbjerg | Christian Eriksen | Simon Kjær | Yussuf Poulsen
**Why it fails:** Eriksen (a listed midfielder) had ~147 caps — well over 80 — so 'which midfielder had over 80 caps by 2022' has two correct answers; Højbjerg himself had only ~73 by 2022.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team
**Remedy:** Replace Eriksen, or pick a unique cap threshold.

### Row 19938 — Denmark (easy) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** Which Denmark player at the 2022 FIFA World Cup is their second-highest all-time scorer? **A:** Christian Eriksen
**Options:** Christian Eriksen | Kasper Dolberg | Yussuf Poulsen | Andreas Cornelius
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer; Tomasson and Poul Nielsen (52, joint) lead, then Pauli Jørgensen and Ole Madsen — Eriksen is not second.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 19939 — Denmark (easy) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** Which Denmark player at the 2022 World Cup is their second-highest scorer? **A:** Christian Eriksen
**Options:** Christian Eriksen | Kasper Dolberg | Yussuf Poulsen | Thomas Delaney
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer; Tomasson and Poul Nielsen (52, joint) lead, then Pauli Jørgensen and Ole Madsen — Eriksen is not second.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 19944 — Denmark (easy) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** Which Denmark player became their second-highest scorer by 2022? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Allan Simonsen
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer; Tomasson and Poul Nielsen (52, joint) lead, then Pauli Jørgensen and Ole Madsen — Eriksen is not second.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 19960 — Denmark (easy) — FAIL: non-unique (Tomasson also 40+)
**Q:** Which Denmark player had over 40 international goals by 2023? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Brian Laudrup
**Why it fails:** Both Eriksen (~41) and Tomasson (52, a listed option) had 40+ goals, so the answer isn't unique.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Replace Tomasson, or specify a current player.

### Row 19961 — Denmark (easy) — FAIL: non-unique (Tomasson also 40+)
**Q:** Which Denmark player had scored 40+ international goals by the 2022 FIFA World Cup? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Brian Laudrup
**Why it fails:** Both Eriksen (~41) and Tomasson (52, a listed option) had 40+ goals, so the answer isn't unique.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Replace Tomasson, or specify a current player.

### Row 19971 — Denmark (easy) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** Which Denmark player is the nation's second-highest all-time scorer with over 40 goals? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Brian Laudrup
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer; Tomasson and Poul Nielsen (52, joint) lead, then Pauli Jørgensen and Ole Madsen — Eriksen is not second.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 19972 — Denmark (easy) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** Which Denmark player is the nation's second-highest scorer with 40+ goals? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Brian Laudrup
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer; Tomasson and Poul Nielsen (52, joint) lead, then Pauli Jørgensen and Ole Madsen — Eriksen is not second.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 19980 — Denmark (easy) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** Which Denmark player is their second-highest all-time scorer with 40+ goals? **A:** Christian Eriksen
**Options:** Christian Eriksen | Michael Laudrup | Jon Dahl Tomasson | Brian Laudrup
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer; Tomasson and Poul Nielsen (52, joint) lead, then Pauli Jørgensen and Ole Madsen — Eriksen is not second.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 19981 — Denmark (easy) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** Which Denmark player is their second-highest scorer entering Euro 2024? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Brian Laudrup
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer; Tomasson and Poul Nielsen (52, joint) lead, then Pauli Jørgensen and Ole Madsen — Eriksen is not second.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 19982 — Denmark (easy) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** Which Denmark player is their second-highest scorer with 40+ goals? **A:** Christian Eriksen
**Options:** Christian Eriksen | Michael Laudrup | Jon Dahl Tomasson | Brian Laudrup
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer; Tomasson and Poul Nielsen (52, joint) lead, then Pauli Jørgensen and Ole Madsen — Eriksen is not second.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 19986 — Denmark (easy) — FAIL: wrong — Eriksen's WC debut was 2010
**Q:** Which Denmark player made his World Cup debut in 2022 after a major Euro 2020 health incident? **A:** Christian Eriksen
**Options:** Christian Eriksen | Daley Blind | Mario Götze | Sergio Agüero
**Why it fails:** Eriksen did not 'make his World Cup debut in 2022' — he debuted at the 2010 World Cup and also played in 2018; 2022 was a RETURN.
**Source:** https://en.wikipedia.org/wiki/Denmark_at_the_FIFA_World_Cup
**Remedy:** Reword to 'returned at' the 2022 World Cup.

### Row 19997 — Denmark (easy) — FAIL: non-unique (Tomasson also 40+)
**Q:** Which Denmark player reached 40+ goals before the 2022 World Cup? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Nicklas Bendtner
**Why it fails:** Both Eriksen (~41) and Tomasson (52, a listed option) had 40+ goals, so the answer isn't unique.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Replace Tomasson, or specify a current player.

### Row 20022 — Denmark (easy) — FAIL: non-unique (Tomasson also 40+)
**Q:** Which Denmark player scored 40+ goals before the 2022 World Cup? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Brian Laudrup
**Why it fails:** Both Eriksen (~41) and Tomasson (52, a listed option) had 40+ goals — non-unique.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Replace Tomasson, or specify a current player.

### Row 20024 — Denmark (easy) — FAIL: non-unique (Tomasson also 40+)
**Q:** Which Denmark player scored 40+ goals for his country? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Nicklas Bendtner
**Why it fails:** Both Eriksen (~41) and Tomasson (52, a listed option) had 40+ goals — non-unique.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Replace Tomasson, or specify a current player.

### Row 20025 — Denmark (easy) — FAIL: non-unique (Tomasson also 40+)
**Q:** Which Denmark player scored 40+ goals for the national team? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Nicklas Bendtner
**Why it fails:** Both Eriksen (~41) and Tomasson (52, a listed option) had 40+ goals — non-unique.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Replace Tomasson, or specify a current player.

### Row 20026 — Denmark (easy) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** Which Denmark player scored 40+ goals to become their second-highest scorer? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Brian Laudrup
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer (behind Tomasson & Poul Nielsen 52, Pauli Jørgensen, Ole Madsen) — not second.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 20027 — Denmark (easy) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** Which Denmark player scored 40+ goals, becoming their second-highest scorer? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Nicklas Bendtner
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer (behind Tomasson & Poul Nielsen 52, Pauli Jørgensen, Ole Madsen) — not second.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 20090 — Denmark (easy) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** Which Denmark player was their second-highest scorer entering the 2022 FIFA World Cup? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Dennis Rommedahl
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer (behind Tomasson & Poul Nielsen 52, Pauli Jørgensen, Ole Madsen) — not second.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 20091 — Denmark (easy) — FAIL: wrong — Mæhle didn't score v England
**Q:** Which Denmark player, like Joakim Mæhle, scored at Euro 2020 against England? **A:** Mikkel Damsgaard
**Options:** Mikkel Damsgaard | Martin Braithwaite | Yussuf Poulsen | Christian Eriksen
**Why it fails:** Mæhle scored at Euro 2020 (v Russia, Wales) but NOT against England; Denmark's only goal v England was Damsgaard's free kick (the other was a Kjær own goal). The 'like Mæhle' premise is false.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Damsgaard scored v England; Mæhle didn't.

### Row 20092 — Denmark (easy) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** Which Denmark player, with 40+ goals, is their second-highest scorer entering the 2022 FIFA World Cup? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Brian Laudrup
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer (behind Tomasson & Poul Nielsen 52, Pauli Jørgensen, Ole Madsen) — not second.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 20107 — Denmark (easy) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** Which Denmark player's 40+ goals made him their second-highest scorer before the 2022 World Cup? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Nicklas Bendtner
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer (behind Tomasson & Poul Nielsen 52, Pauli Jørgensen, Ole Madsen) — not second.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 20108 — Denmark (easy) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** Which Denmark player's 40+ goals make him their second-highest scorer? **A:** Christian Eriksen
**Options:** Christian Eriksen | Nicklas Bendtner | Michael Laudrup | Jon Dahl Tomasson
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer (behind Tomasson & Poul Nielsen 52, Pauli Jørgensen, Ole Madsen) — not second.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 20115 — Denmark (easy) — FAIL: wrong — Eriksen is 5th, not 2nd
**Q:** Which Denmark player's goals in FIFA World Cup qualifiers made him the nation's second-highest scorer? **A:** Christian Eriksen
**Options:** Christian Eriksen | Jon Dahl Tomasson | Michael Laudrup | Martin Braithwaite
**Why it fails:** Eriksen (~41 goals) is Denmark's FIFTH-highest scorer (behind Tomasson & Poul Nielsen 52, Pauli Jørgensen, Ole Madsen) — not second.
**Source:** https://en.wikipedia.org/wiki/Denmark_national_football_team_records_and_statistics
**Remedy:** Eriksen is not the second-highest scorer.

### Row 20122 — Denmark (easy) — FAIL: wrong — confused + Riemer leads 2026
**Q:** Which Denmark rival's manager was appointed for the 2026 World Cup cycle? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | John Jensen
**Why it fails:** Hjulmand is (was) Denmark's own manager, not a 'rival's', and he doesn't lead the 2026 cycle (Riemer does).
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Reword; Riemer manages the 2026 cycle.

### Row 20124 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Which Denmark stadium has a 38,065 capacity for FIFA World Cup qualifiers? **A:** Parken Stadium
**Options:** Parken Stadium | Brøndby Stadion | Telia Parken | Aarhus Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 20127 — Denmark (easy) — FAIL: outdated — Højlund now plays for Napoli
**Q:** Which Denmark striker for the 2026 World Cup cycle plays for Manchester United? **A:** Rasmus Højlund
**Options:** Rasmus Højlund | Kasper Dolberg | Yussuf Poulsen | Andreas Skov Olsen
**Why it fails:** As of 2026 Rasmus Højlund plays for NAPOLI (Serie A) — he moved on loan in summer 2025, made permanent on 3 June 2026 — not Manchester United.
**Source:** https://en.wikipedia.org/wiki/Rasmus_H%C3%B8jlund
**Remedy:** Answer/clue should say Napoli (Serie A), not Manchester United.

### Row 20142 — Denmark (easy) — FAIL: outdated — Højlund now plays for Napoli
**Q:** Which Denmark striker, playing for Manchester United, is a key forward for the 2026 World Cup cycle? **A:** Rasmus Højlund
**Options:** Rasmus Højlund | Yussuf Poulsen | Martin Braithwaite | Mikkel Damsgaard
**Why it fails:** As of 2026 Rasmus Højlund plays for NAPOLI (Serie A) — he moved on loan in summer 2025, made permanent on 3 June 2026 — not Manchester United.
**Source:** https://en.wikipedia.org/wiki/Rasmus_H%C3%B8jlund
**Remedy:** Answer/clue should say Napoli (Serie A), not Manchester United.

### Row 20143 — Denmark (easy) — FAIL: outdated — Højlund now plays for Napoli
**Q:** Which Denmark striker, playing for Manchester United, is emerging for the 2026 World Cup cycle? **A:** Rasmus Højlund
**Options:** Rasmus Højlund | Martin Braithwaite | Yussuf Poulsen | Mikkel Damsgaard
**Why it fails:** As of 2026 Rasmus Højlund plays for NAPOLI (Serie A) — he moved on loan in summer 2025, made permanent on 3 June 2026 — not Manchester United.
**Source:** https://en.wikipedia.org/wiki/Rasmus_H%C3%B8jlund
**Remedy:** Answer/clue should say Napoli (Serie A), not Manchester United.

### Row 20160 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Which Euro 2020 host staged all Denmark's home World Cup qualifiers? **A:** Parken Stadium
**Options:** Parken Stadium | Brøndby Stadion | Telia Parken | Arena Națională
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 20172 — Denmark (easy) — FAIL: outdated — Højlund (Napoli) is in Serie A
**Q:** Which major European league did Denmark's 2026 World Cup squad NOT draw players from? **A:** Serie A
**Options:** Serie A | Premier League | La Liga | Bundesliga
**Why it fails:** Højlund moved to Napoli (Serie A) by 2026, so Serie A IS represented in Denmark's squad — the 'not Serie A' answer is now false.
**Source:** https://en.wikipedia.org/wiki/Rasmus_H%C3%B8jlund
**Remedy:** Serie A is now represented (Højlund).

### Row 20173 — Denmark (easy) — FAIL: outdated — Højlund (Napoli) is in Serie A
**Q:** Which major league was not represented in Denmark's 2026 World Cup squad? **A:** Serie A
**Options:** Serie A | Premier League | La Liga | Bundesliga
**Why it fails:** Højlund moved to Napoli (Serie A) by 2026, so Serie A IS represented in Denmark's squad — the 'not Serie A' answer is now false.
**Source:** https://en.wikipedia.org/wiki/Rasmus_H%C3%B8jlund
**Remedy:** Serie A is now represented (Højlund).

### Row 20175 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which manager is leading Denmark for the 2026 FIFA World Cup? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Åge Hareide | Morten Olsen | Lars Lagerbäck
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer leads Denmark's 2026 cycle, not Hjulmand.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer.

### Row 20176 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which manager is leading Denmark in their 2026 World Cup qualifying campaign? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer leads Denmark's 2026 cycle, not Hjulmand.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer.

### Row 20178 — Denmark (medium) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which manager is leading Denmark's 2026 FIFA World Cup qualification campaign? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Åge Hareide | Morten Olsen | Lars Lagerbäck
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer leads Denmark's 2026 cycle, not Hjulmand.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer.

### Row 20188 — Denmark (medium) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which manager led Denmark's 2026 FIFA World Cup qualification campaign? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer leads Denmark's 2026 cycle, not Hjulmand.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer.

### Row 20189 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which manager led Denmark's 2026 World Cup qualifying campaign? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Åge Hareide | Morten Olsen | Lars Lagerbäck
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer leads Denmark's 2026 cycle, not Hjulmand.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer.

### Row 20193 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Which manager will lead Denmark at the 2026 FIFA World Cup? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer leads Denmark's 2026 cycle, not Hjulmand.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer.

### Row 20282 — Denmark (medium) — FAIL: wrong — Tunisia won a 2022 group game
**Q:** Which nation, like Denmark in 2022, also failed to win a World Cup group stage match? **A:** Tunisia
**Options:** Tunisia | Australia | Peru | Croatia
**Why it fails:** Tunisia did NOT fail to win in 2022 — they beat France 1-0 in their final group match (they drew Denmark 0-0, lost to Australia). So they are not 'like Denmark' (0 wins).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_D
**Remedy:** None of the listed options went winless like Denmark.

### Row 20283 — Denmark (easy) — FAIL: self-referential + false premise
**Q:** Which nation, like Denmark, qualified for the 2026 World Cup via UEFA? **A:** Denmark
**Options:** Denmark | Germany | France | Spain
**Why it fails:** The answer is 'Denmark' (the subject — self-referential), and the premise that Denmark 'qualified for the 2026 World Cup' is false (they lost the playoff to Czechia).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_C
**Remedy:** Drop — Denmark did not qualify for 2026.

### Row 20302 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Which stadium hosted all Denmark's 2022 World Cup qualifier home matches? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadion | Aalborg Portland Park
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 20304 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Which stadium hosted Denmark's 2022 FIFA World Cup qualifiers? **A:** Parken Stadium
**Options:** Parken Stadium | Telia Parken | Brøndby Stadium | Aalborg Stadium
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 20307 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Which stadium hosted Denmark's 2022 World Cup qualifiers with a capacity near 38,000? **A:** Parken Stadium
**Options:** Parken Stadium | Brøndby Stadion | Telia Parken | Aalborg Portland Park
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 20316 — Denmark (easy) — FAIL: non-unique (Telia Parken = Parken)
**Q:** Which stadium hosts all of Denmark's home FIFA World Cup qualifiers? **A:** Parken Stadium
**Options:** Parken Stadium | Brøndby Stadion | Telia Parken | Odense Stadion
**Why it fails:** The option 'Telia Parken' IS Parken Stadium (2014-2020 sponsor name) — non-unique.
**Source:** https://en.wikipedia.org/wiki/Parken_Stadium
**Remedy:** Remove the 'Telia Parken' option.

### Row 20393 — Denmark (easy) — FAIL: non-unique (Croatia also not a Euro KO loss)
**Q:** Which team did Denmark NOT lose to in a Euro knockout match? **A:** Russia
**Options:** Russia | England | Croatia | Germany
**Why it fails:** Denmark never lost to Croatia in a EURO knockout (that loss was the 2018 World Cup), so both 'Russia' and 'Croatia' fit 'not lost to in a Euro knockout'.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Replace Croatia with a team Denmark beat in a Euro knockout.

### Row 20437 — Denmark (easy) — FAIL: wrong — France 2-1 was a group game
**Q:** Which two nations eliminated Denmark by a 2-1 scoreline in knockout matches? **A:** England and France
**Options:** England and France | England and Croatia | Germany and France | Croatia and Germany
**Why it fails:** Denmark's 2-1 loss to France (2022) was in the GROUP stage and did NOT eliminate them (Australia did); only England (Euro 2020 SF) was a 2-1 knockout elimination.
**Source:** https://en.wikipedia.org/wiki/Denmark_at_the_FIFA_World_Cup
**Remedy:** France didn't eliminate Denmark in a knockout.

### Row 20451 — Denmark (medium) — FAIL: false premise — Denmark missed 2026
**Q:** Which two World Cups did Denmark qualify for after reaching Euro 2020? **A:** 2022 and 2026
**Options:** 2022 and 2026 | 2018 and 2022 | 2014 and 2018 | 2010 and 2014
**Why it fails:** Denmark qualified for 2022 but NOT 2026 — they lost the playoff to Czechia.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_C
**Remedy:** Only 2022; 2026 was a failed playoff.

### Row 20453 — Denmark (medium) — FAIL: false premise — Denmark missed 2026
**Q:** Which two World Cups did Denmark qualify for via UEFA group wins? **A:** 2022 and 2026
**Options:** 2022 and 2026 | 2010 and 2018 | 2014 and 2022 | 2018 and 2026
**Why it fails:** Denmark did NOT qualify for the 2026 World Cup — they lost the UEFA playoff final to Czechia (2-2, 3-1 pens, 31 Mar 2026). They also finished 2nd in their 2026 group (Scotland won it), not a group win.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_C
**Remedy:** Only 2022 was a group win; 2026 failed.

### Row 20469 — Denmark (medium) — FAIL: self-referential + wrong peak
**Q:** Which UEFA nation matched Denmark's 2022 FIFA ranking peak of 10th? **A:** Denmark
**Options:** Denmark | Switzerland | Croatia | Netherlands
**Why it fails:** Answer is 'Denmark' (self-referential); also Denmark's all-time peak ranking is 6th (1996), not 10th — the 10th was only a 2022 high.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop; 10th wasn't Denmark's peak.

### Row 20484 — Denmark (easy) — FAIL: non-unique (Switzerland also qualified 2010)
**Q:** Which UEFA nation, like Denmark, qualified for the 2010 FIFA World Cup? **A:** Netherlands
**Options:** Netherlands | Switzerland | Republic of Ireland | Sweden
**Why it fails:** Both the Netherlands AND Switzerland qualified for the 2010 World Cup, so two options are correct.
**Source:** https://en.wikipedia.org/wiki/Denmark_at_the_FIFA_World_Cup
**Remedy:** Replace Switzerland with a UEFA team that missed 2010.

### Row 20485 — Denmark (easy) — FAIL: self-referential answer
**Q:** Which UEFA nation, like Denmark, won its 2022 World Cup qualifying group? **A:** Denmark
**Options:** Denmark | Germany | England | Spain
**Why it fails:** 'Which UEFA nation, like Denmark, won its 2022 qualifying group?' answers 'Denmark' — the subject itself.
**Source:** https://en.wikipedia.org/wiki/Denmark_at_the_FIFA_World_Cup
**Remedy:** Name a different group winner.

### Row 20489 — Denmark (easy) — FAIL: self-referential + wrong (DBU in Brøndby)
**Q:** Which UEFA nation's FA headquarters are in Copenhagen, like Denmark's DBU? **A:** Denmark
**Options:** Denmark | Sweden | Norway | Finland
**Why it fails:** Answer is 'Denmark' (self-referential), and the premise that the DBU HQ is in Copenhagen is false — it's in Brøndby.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Drop; DBU HQ is in Brøndby.

### Row 20501 — Denmark (easy) — FAIL: non-unique (Switzerland also qualified 2014)
**Q:** Which UEFA team qualified for the 2014 World Cup, unlike Denmark? **A:** Netherlands
**Options:** Netherlands | Sweden | Switzerland | Turkey
**Why it fails:** Both the Netherlands AND Switzerland qualified for the 2014 World Cup, so two options are correct.
**Source:** https://en.wikipedia.org/wiki/Denmark_at_the_FIFA_World_Cup
**Remedy:** Replace Switzerland with a team that missed 2014.

### Row 20508 — Denmark (hard) — FAIL: false premise — Denmark missed 2026
**Q:** Which World Cup did Denmark qualify for after the 2022 tournament? **A:** The 2026 World Cup
**Options:** The 2026 World Cup | The 2018 World Cup | The 2014 World Cup | The 2010 World Cup
**Why it fails:** Denmark did NOT qualify for the 2026 World Cup — they lost the UEFA playoff final to Czechia (2-2, 3-1 pens, 31 Mar 2026).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_C
**Remedy:** Denmark did not qualify for the WC after 2022.

### Row 20529 — Denmark (medium) — FAIL: false premise — Denmark missed 2026
**Q:** Which year did Denmark qualify for the 2026 FIFA World Cup? **A:** 2026
**Options:** 2026 | 2022 | 2018 | 2014
**Why it fails:** Denmark did NOT qualify for the 2026 World Cup — they lost the UEFA playoff final to Czechia (2-2, 3-1 pens, 31 Mar 2026).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_C
**Remedy:** Drop — no 2026 qualification.

### Row 20530 — Denmark (medium) — FAIL: non-unique (qualified 2010, 2018 & 2022)
**Q:** Which year did Denmark qualify for the World Cup? **A:** 2010
**Options:** 2010 | 2014 | 2018 | 2022
**Why it fails:** Denmark qualified for the 2010, 2018 AND 2022 World Cups, so three of the four year options are correct.
**Source:** https://en.wikipedia.org/wiki/Denmark_at_the_FIFA_World_Cup
**Remedy:** Ask which year they did NOT qualify (2014), or make it specific.

### Row 20535 — Denmark (easy) — FAIL: wrong — Riemer (not Hjulmand) leads 2026
**Q:** Who is Denmark's manager for the 2026 FIFA World Cup cycle? **A:** Kasper Hjulmand
**Options:** Kasper Hjulmand | Morten Olsen | Åge Hareide | Lars Lagerbäck
**Why it fails:** Hjulmand resigned in July 2024; Brian Riemer leads Denmark's 2026 cycle.
**Source:** https://en.wikipedia.org/wiki/Kasper_Hjulmand
**Remedy:** Answer: Brian Riemer.

### Row 20571 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Why did Denmark's 2022 World Cup squad hold a key pre-tournament meeting in Copenhagen? **A:** DBU headquarters are there
**Options:** DBU headquarters are there | Team hotel was there | Stadium training there | Sponsor event there
**Why it fails:** The DBU's headquarters are in BRØNDBY, not Copenhagen.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 20574 — Denmark (easy) — FAIL: wrong — DBU HQ is in Brøndby
**Q:** Why did Denmark's coach hold a key 2022 World Cup tactical briefing in Copenhagen? **A:** DBU headquarters are there
**Options:** DBU headquarters are there | Aarhus stadium hosted it | Parken Stadium is there | National team trained there
**Why it fails:** The DBU's headquarters are in BRØNDBY, not Copenhagen.
**Source:** https://en.wikipedia.org/wiki/Danish_Football_Association
**Remedy:** Answer: Brøndby.

### Row 20576 — Denmark (easy) — FAIL: false premise — Denmark missed 2026
**Q:** Why did Denmark's national team qualify for the 2026 FIFA World Cup? **A:** UEFA qualification campaign
**Options:** UEFA qualification campaign | UEFA Nations League | UEFA inter-confederation playoff | UEFA final tournament
**Why it fails:** Denmark did NOT qualify for the 2026 World Cup — they lost the UEFA playoff final to Czechia (2-2, 3-1 pens, 31 Mar 2026).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_C
**Remedy:** Drop — Denmark failed to qualify for 2026.

## Rows 20582–21579 (DR Congo) — 127 FAIL-liveness

Recurring DR Congo defect clusters: (1) **2023 AFCON = 'quarter-finals'** — they actually reached the **SEMI-finals** (4th place); (2) **self-referential** 'which nation/team, like DR Congo, …? → DR Congo' (~30); (3) **2018/2022 World Cup false premises** — DR Congo were not at those finals; (4) **outdated clubs** — Wissa now at Newcastle (not Brentford), Mbemba now at Lille (not Marseille); (5) **outdated 'never qualified under current name'** — DR Congo HAVE now qualified (2026); (6) qualified via the **intercontinental playoff**, not directly through CAF; (7) misc — Desabre (not Ibenge) managed the 2023 AFCON; Bundesliga IS represented (Silas/Stuttgart); DR Congo don't 'consistently struggle' at AFCON (2 titles); non-unique items. **NOTE:** squad-composition '2026 cycle/squad' facts and the 'first WC under current name = 2026 / first in 52 years' framing were PASSED as correct.

### Row 20590 — DR Congo (easy) — FAIL: false premise (not at 2018 WC)
**Q:** At 2018 World Cup, who played for DR Congo? **A:** Ligue 1 players
**Options:** Ligue 1 players | La Liga players | Bundesliga players | Serie A players
**Why it fails:** false premise — DR Congo did NOT qualify for the 2018 World Cup, so there was no DR Congo squad/match there.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 World Cup squad or 2026 qualifying.

### Row 20592 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** At 2022 World Cup, which DR Congo key defender? **A:** Arthur Masuaku
**Options:** Arthur Masuaku | Cédric Bakambu | Chancel Mbemba | Yoane Wissa
**Why it fails:** false premise — DR Congo did NOT qualify for the 2022 World Cup, so there was no DR Congo squad/match there.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 World Cup squad.

### Row 20593 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** At 2022 World Cup, which DR Congo player? **A:** Yoane Wissa
**Options:** Yoane Wissa | Chancel Mbemba | Dieumerci Mbokani | Cedric Bakambu
**Why it fails:** false premise — DR Congo did NOT qualify for the 2022 World Cup, so there was no DR Congo squad/match there.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 World Cup squad.

### Row 20594 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** At 2022 World Cup, which league did DR Congo's squad not feature? **A:** Bundesliga
**Options:** Bundesliga | Ligue 1 | Premier League | Serie A
**Why it fails:** false premise — DR Congo did NOT qualify for the 2022 World Cup, so there was no DR Congo squad/match there.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 World Cup squad.

### Row 20595 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** At 2022 World Cup, which league has DR Congo players? **A:** Ligue 1
**Options:** Ligue 1 | Bundesliga | Serie A | La Liga
**Why it fails:** false premise — DR Congo did NOT qualify for the 2022 World Cup, so there was no DR Congo squad/match there.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 World Cup squad.

### Row 20598 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** At 2022 World Cup, who leads DR Congo's attack? **A:** Yoane Wissa
**Options:** Yoane Wissa | Chancel Mbemba | Dieumerci Mbokani | Cedric Bakambu
**Why it fails:** false premise — DR Congo did NOT qualify for the 2022 World Cup, so there was no DR Congo squad/match there.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 World Cup squad.

### Row 20602 — DR Congo (easy) — FAIL: false premise (not at 2018 WC)
**Q:** At the 2018 World Cup, who provides defensive experience for DR Congo? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Yoane Wissa | Dieumerci Mbokani | Cedric Bakambu
**Why it fails:** false premise — DR Congo did NOT qualify for the 2018 World Cup, so there was no DR Congo squad/match there.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 World Cup squad or 2026 qualifying.

### Row 20607 — DR Congo (easy) — FAIL: wrong — 2023 AFCON was the SEMIS, not QF
**Q:** At the 2023 AFCON, which stage did DR Congo reach? **A:** The quarter-finals
**Options:** The quarter-finals | The semi-finals | The group stage | The final
**Why it fails:** DR Congo reached the SEMI-FINALS of the 2023 AFCON (4th place — lost the SF 1-0 to Ivory Coast, then the 3rd-place playoff to South Africa on pens), NOT the quarter-finals.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** Answer: the semi-finals (4th place).

### Row 20620 — DR Congo (hard) — FAIL: non-unique (failed all of 2010-2022)
**Q:** Before 2026, which World Cup did DR Congo fail to qualify for? **A:** The 2022 World Cup
**Options:** The 2022 World Cup | The 2018 World Cup | The 2014 World Cup | The 2010 World Cup
**Why it fails:** DR Congo failed to qualify for 2010, 2014, 2018 AND 2022 — all four options are correct.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Make it specific (e.g. the most recent miss before 2026 → 2022).

### Row 20640 — DR Congo (easy) — FAIL: self-referential answer
**Q:** DR Congo qualified for the 2026 World Cup. Which nation also qualified for their first World Cup under a new name in 2026? **A:** DR Congo
**Options:** DR Congo | Ivory Coast | Nigeria | Senegal
**Why it fails:** 'Which nation also qualified for their first WC under a new name in 2026?' answers 'DR Congo' — the subject itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Drop — self-referential.

### Row 20657 — DR Congo (medium) — FAIL: wrong/non-unique — 2023 was the SEMIS
**Q:** DR Congo reached AFCON quarter-finals in what year? **A:** 2023
**Options:** 2023 | 2015 | 2019 | 2021
**Why it fails:** DR Congo reached the SEMI-FINALS of the 2023 AFCON (4th place — lost the SF 1-0 to Ivory Coast, then the 3rd-place playoff to South Africa on pens), NOT the quarter-finals. They reached the QF in both 2015 and 2023 en route to the semis.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** 2023 result was the semi-finals.

### Row 20660 — DR Congo (medium) — FAIL: wrong — 2023 was also a semi-final
**Q:** DR Congo reached the 2023 AFCON quarter-finals, but in which year did they last reach the semi-finals? **A:** 2015
**Options:** 2015 | 2019 | 2021 | 2017
**Why it fails:** DR Congo reached the SEMI-FINALS of the 2023 AFCON (4th place — lost the SF 1-0 to Ivory Coast, then the 3rd-place playoff to South Africa on pens), NOT the quarter-finals. So '2015 was the last semi before a 2023 QF run' is false — 2023 was itself a semi.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** Both 2015 and 2023 were semi-final runs.

### Row 20665 — DR Congo (easy) — FAIL: wrong — 2023 AFCON was the SEMIS, not QF
**Q:** DR Congo reached which AFCON stage in 2023? **A:** Quarter finals
**Options:** Quarter finals | Semi finals | Group stage | Finals
**Why it fails:** DR Congo reached the SEMI-FINALS of the 2023 AFCON (4th place — lost the SF 1-0 to Ivory Coast, then the 3rd-place playoff to South Africa on pens), NOT the quarter-finals.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** Answer: the semi-finals (4th place).

### Row 20666 — DR Congo (easy) — FAIL: wrong — 2023 AFCON was the SEMIS, not QF
**Q:** DR Congo reached which round of the 2023 AFCON? **A:** Quarter-finals
**Options:** Quarter-finals | Round of 16 | Semi-finals | Final
**Why it fails:** DR Congo reached the SEMI-FINALS of the 2023 AFCON (4th place — lost the SF 1-0 to Ivory Coast, then the 3rd-place playoff to South Africa on pens), NOT the quarter-finals.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** Answer: the semi-finals (4th place).

### Row 20673 — DR Congo (medium) — FAIL: wrong — 2023 was a semi-final too
**Q:** DR Congo's 2015 AFCON semi-final finish was better than their result at which 2023 tournament? **A:** 2023 AFCON quarter-finals
**Options:** 2023 AFCON quarter-finals | 2023 AFCON final | 2023 AFCON group stage | 2023 AFCON third place
**Why it fails:** 2015 (semi/3rd) was NOT a stage further than 2023: DR Congo also reached the SEMI-FINALS in 2023 (4th).
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** Both were semi-final finishes.

### Row 20678 — DR Congo (medium) — FAIL: wrong — 2023 was a semi, matching 2015
**Q:** DR Congo's 2023 AFCON quarter-final matched their best run since which prior tournament? **A:** 2015 AFCON
**Options:** 2015 AFCON | 2017 AFCON | 2019 AFCON | 2021 AFCON
**Why it fails:** DR Congo's 2023 run reached the SEMI-FINALS (not QF), matching — not falling short of — their 2015 semi.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** 2023 equalled the 2015 semi-final run.

### Row 20718 — DR Congo (easy) — FAIL: wrong — qualified via intercontinental playoff
**Q:** How did DR Congo qualify for the 2026 FIFA World Cup? **A:** Through CAF qualification
**Options:** Through CAF qualification | Via intercontinental playoff | As a host nation | Via a wildcard entry
**Why it fails:** DR Congo did NOT qualify 'through CAF qualification' directly — they finished 2nd in CAF Group B, won the CAF playoff (v Nigeria), then won the FIFA INTERCONTINENTAL playoff (v Jamaica) to qualify. The listed distractor 'Via intercontinental playoff' is the correct answer.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Answer: via the intercontinental playoff.

### Row 20726 — DR Congo (medium) — FAIL: outdated — DR Congo qualified for 2026
**Q:** How many FIFA World Cups has DR Congo qualified for under its current name? **A:** Zero
**Options:** Zero | One | Two | Three
**Why it fails:** As of 2026 DR Congo HAVE qualified for a World Cup under their current name — they reached the 2026 finals (via the intercontinental playoff). 'Never/zero under current name' is now false.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Answer: once (2026).

### Row 20728 — DR Congo (medium) — FAIL: outdated — DR Congo qualified for 2026
**Q:** How many times have DR Congo qualified for a FIFA World Cup under their current name? **A:** Zero times
**Options:** Zero times | One time | Two times | Three times
**Why it fails:** As of 2026 DR Congo HAVE qualified for a World Cup under their current name — they reached the 2026 finals (via the intercontinental playoff). 'Never/zero under current name' is now false.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Answer: once (2026).

### Row 20747 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** In a 2022 World Cup group, which DR Congo attacker was a key Premier League forward? **A:** Yoane Wissa
**Options:** Yoane Wissa | Mohamed Salah | Sadio Mané | Riyad Mahrez
**Why it fails:** false premise — DR Congo did NOT qualify for the 2022 World Cup, so there was no DR Congo squad/match there.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 World Cup squad.

### Row 20749 — DR Congo (easy) — FAIL: outdated — Mbemba now at Lille
**Q:** In a 2026 World Cup qualifier, which DR Congo centre-back anchored the defense for Marseille? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Issa Diop | Willy Boly | Axel Disasi
**Why it fails:** Chancel Mbemba moved from Marseille to Lille in 2025; he no longer plays for Marseille.
**Source:** https://en.wikipedia.org/wiki/Chancel_Mbemba
**Remedy:** Mbemba plays for Lille.

### Row 20750 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** In DR Congo's 2026 qualifier, which key attacker plays for Brentford? **A:** Yoane Wissa
**Options:** Yoane Wissa | Chancel Mbemba | Cédric Bakambu | Gaël Kakuta
**Why it fails:** Yoane Wissa moved from Brentford to Newcastle United (2025); he no longer plays for Brentford.
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle (still the Premier League).

### Row 20767 — DR Congo (medium) — FAIL: wrong — 2023 AFCON was the SEMIS, not QF
**Q:** In which year did DR Congo reach the AFCON quarter-finals? **A:** 2023
**Options:** 2023 | 2015 | 2019 | 2021
**Why it fails:** DR Congo reached the SEMI-FINALS of the 2023 AFCON (4th place), not the quarter-finals.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** Answer: the semi-finals (4th).

### Row 20773 — DR Congo (medium) — FAIL: outdated — DR Congo qualified for 2026
**Q:** Under their current name, how many FIFA World Cups have DR Congo qualified for? **A:** Zero
**Options:** Zero | One | Two | Three
**Why it fails:** DR Congo HAVE now qualified for a World Cup under their current name — they reached the 2026 finals (intercontinental playoff). 'Zero under current name' is false.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Answer: once (2026).

### Row 20798 — DR Congo (medium) — FAIL: wrong — DR Congo are long-standing AFCON regulars
**Q:** When did DR Congo become regular AFCON participants? **A:** After 2006
**Options:** After 2006 | Before 2006 | After 2010 | After 2014
**Why it fails:** DR Congo have been AFCON regulars since the 1960s-70s (champions 1968 & 1974), not 'after 2006'.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_national_football_team
**Remedy:** Answer: well before 2006.

### Row 20809 — DR Congo (medium) — FAIL: wrong — DR Congo also reached the 2023 semis
**Q:** When did DR Congo last reach the AFCON semi-finals? **A:** 2015
**Options:** 2015 | 2013 | 2017 | 2019
**Why it fails:** DR Congo's LAST AFCON semi-final was 2023 (4th place), not 2015 — they reached the semis in both 2015 and 2023.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** Answer: 2023 (also 2015).

### Row 20810 — DR Congo (medium) — FAIL: non-unique (AFCON regular — many years)
**Q:** When did DR Congo play AFCON matches? **A:** At 2019
**Options:** At 2019 | At 2006 | At 2010 | At 2012
**Why it fails:** DR Congo played AFCON matches in 2006 AND 2019 (among the options), so the answer isn't unique (they're regular participants).
**Source:** https://en.wikipedia.org/wiki/DR_Congo_national_football_team
**Remedy:** Specify a unique year/fact.

### Row 20811 — DR Congo (medium) — FAIL: non-unique (N-African rivals across many AFCONs)
**Q:** When did DR Congo play North African rivals at AFCON? **A:** 2019 AFCON
**Options:** 2019 AFCON | 2015 AFCON | 2013 AFCON | 2017 AFCON
**Why it fails:** DR Congo played North-African opponents at several AFCONs (e.g. Tunisia 2015, Morocco 2017, Egypt 2019, Morocco 2023), so a single year isn't unique.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_national_football_team
**Remedy:** Specify a unique fact, not a year.

### Row 20812 — DR Congo (medium) — FAIL: non-unique (N-African rivals across many AFCONs)
**Q:** When did DR Congo play North African rivals? **A:** At 2019
**Options:** At 2019 | At 2015 | At 2021 | At 2023
**Why it fails:** DR Congo played North-African opponents at several AFCONs (e.g. Tunisia 2015, Morocco 2017, Egypt 2019, Morocco 2023), so a single year isn't unique.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_national_football_team
**Remedy:** Specify a unique fact, not a year.

### Row 20824 — DR Congo (medium) — FAIL: wrong — 2023 AFCON was the SEMIS, not QF
**Q:** When did DR Congo reach the 2023 AFCON quarter-finals? **A:** 2023
**Options:** 2023 | 2022 | 2024 | 2021
**Why it fails:** DR Congo reached the SEMI-FINALS of the 2023 AFCON (4th place), not the quarter-finals.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** Answer: the semi-finals (4th).

### Row 20836 — DR Congo (medium) — FAIL: wrong — Stade des Martyrs didn't host the 2015 AFCON
**Q:** When did DR Congo's Stade des Martyrs host AFCON? **A:** 2015 AFCON
**Options:** 2015 AFCON | 2017 AFCON | 2019 AFCON | 2021 AFCON
**Why it fails:** The 2015 AFCON was hosted by Equatorial Guinea, not DR Congo; Stade des Martyrs did not host it.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_national_football_team
**Remedy:** Drop — DR Congo didn't host the 2015 AFCON.

### Row 20875 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Which 2026 World Cup qualifier, like DR Congo, ended a 50+ year wait? **A:** DR Congo
**Options:** DR Congo | Egypt | Ghana | Nigeria
**Why it fails:** The answer is the subject (DR Congo / TP Mazembe) itself — self-referential. 'Which nation, like DR Congo, …?' → DR Congo.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different nation.

### Row 20893 — DR Congo (medium) — FAIL: self-referential answer
**Q:** Which African nation's 2026 World Cup qualification ended a 50+ year wait, like DR Congo's? **A:** DR Congo
**Options:** DR Congo | Morocco | Senegal | Nigeria
**Why it fails:** The answer is the subject (DR Congo / TP Mazembe) itself — self-referential. 'Which nation, like DR Congo, …?' → DR Congo.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different nation.

### Row 20899 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Which African team reached 2010 FIFA Club World Cup final like DR Congo's TP Mazembe? **A:** TP Mazembe
**Options:** TP Mazembe | Al Ahly | Espérance | Wydad
**Why it fails:** 'Which African team reached the 2010 Club World Cup final like DR Congo's TP Mazembe?' answers 'TP Mazembe' — the subject.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_national_football_team
**Remedy:** Name a different club, or drop.

### Row 20934 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Which CAF nation, like DR Congo, failed to qualify for multiple World Cups? **A:** DR Congo
**Options:** DR Congo | Egypt | Nigeria | Cameroon
**Why it fails:** The answer is the subject (DR Congo / TP Mazembe) itself — self-referential. 'Which nation, like DR Congo, …?' → DR Congo.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different nation.

### Row 20957 — DR Congo (easy) — FAIL: false premise (no 2023 WC)
**Q:** Which defender provided DR Congo's 2023 World Cup squad with defensive experience? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Arthur Masuaku | Gédéon Kalulu | Brian Bayeye
**Why it fails:** There is no 2023 men's World Cup and DR Congo were not at one; '2023 World Cup squad' is invalid (re-anchor to the 2026 squad).
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 World Cup squad.

### Row 20958 — DR Congo (easy) — FAIL: outdated — Mbemba now at Lille
**Q:** Which DR Congo 2026 WC defender has over 60 caps and plays for Marseille? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Cédric Bakambu | Arthur Masuaku | Silas Katompa
**Why it fails:** Chancel Mbemba moved from Marseille to Lille in 2025; 'plays for Marseille' is outdated.
**Source:** https://en.wikipedia.org/wiki/Chancel_Mbemba
**Remedy:** Mbemba plays for Lille, not Marseille.

### Row 20963 — DR Congo (medium) — FAIL: wrong — 2023 AFCON was the SEMIS, not QF
**Q:** Which DR Congo achievement in 2023 mirrored their historic 2026 World Cup qualification? **A:** Reaching AFCON quarter-finals
**Options:** Reaching AFCON quarter-finals | Winning AFCON bronze medal | Qualifying for AFCON semi-finals | Winning a World Cup qualifier
**Why it fails:** DR Congo reached the SEMI-FINALS of the 2023 AFCON (4th place), not the quarter-finals.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** Answer: the semi-finals (4th).

### Row 20966 — DR Congo (hard) — FAIL: wrong — 2023 AFCON was the SEMIS, not QF
**Q:** Which DR Congo AFCON run preceded their historic 2026 World Cup qualification? **A:** 2023 quarter-finals
**Options:** 2023 quarter-finals | 2015 semi-finals | 2022 group stage | 2019 round of 16
**Why it fails:** DR Congo reached the SEMI-FINALS of the 2023 AFCON (4th place), not the quarter-finals.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** Answer: the semi-finals (4th).

### Row 20968 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo attacker for 2026 World Cup qualifying plays for Brentford? **A:** Yoane Wissa
**Options:** Yoane Wissa | Cédric Bakambu | Gaël Kakuta | Dieumerci Mbokani
**Why it fails:** Yoane Wissa moved from Brentford to Newcastle United (2025); 'plays for Brentford' is outdated (he's still a Premier League player, now at Newcastle).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle, not Brentford.

### Row 20970 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo attacker from Brentford was a key player for their 2026 World Cup squad? **A:** Yoane Wissa
**Options:** Yoane Wissa | Chancel Mbemba | Cédric Bakambu | Gaël Kakuta
**Why it fails:** Yoane Wissa moved from Brentford to Newcastle United (2025); 'plays for Brentford' is outdated (he's still a Premier League player, now at Newcastle).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle, not Brentford.

### Row 20971 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo attacker from Brentford was a key squad selection for the 2026 FIFA World Cup qualifiers? **A:** Yoane Wissa
**Options:** Yoane Wissa | Meschack Elia | Cédric Bakambu | Gradel Diangana
**Why it fails:** Yoane Wissa moved from Brentford to Newcastle United (2025); 'plays for Brentford' is outdated (he's still a Premier League player, now at Newcastle).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle, not Brentford.

### Row 20972 — DR Congo (easy) — FAIL: outdated club + false premise (no 2022 WC)
**Q:** Which DR Congo attacker from Brentford was in the 2022 World Cup squad? **A:** Yoane Wissa
**Options:** Yoane Wissa | Cédric Bakambu | Dieumerci Mbokani | Benik Afobe
**Why it fails:** Wissa now plays for Newcastle (not Brentford), AND DR Congo did not play at the 2022 World Cup (no '2022 World Cup squad').
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 squad; Wissa is at Newcastle.

### Row 20980 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo attacker is key for Brentford in the 2026 World Cup qualifiers? **A:** Yoane Wissa
**Options:** Yoane Wissa | Cédric Bakambu | Dieumerci Mbokani | Benik Afobe
**Why it fails:** Yoane Wissa moved from Brentford to Newcastle United (2025); 'plays for Brentford' is outdated (he's still a Premier League player, now at Newcastle).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle, not Brentford.

### Row 20982 — DR Congo (easy) — FAIL: outdated club + false premise (no 2022 WC)
**Q:** Which DR Congo attacker played for Brentford during the 2022 World Cup? **A:** Yoane Wissa
**Options:** Yoane Wissa | Cedric Bakambu | Dieumerci Mbokani | Benik Afobe
**Why it fails:** Wissa now plays for Newcastle (not Brentford), AND DR Congo did not play at the 2022 World Cup (no '2022 World Cup squad').
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 squad; Wissa is at Newcastle.

### Row 20983 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo attacker plays for Brentford and is a key figure for the 2026 World Cup qualifiers? **A:** Yoane Wissa
**Options:** Yoane Wissa | Cédric Bakambu | Dieumerci Mbokani | Benik Afobe
**Why it fails:** Yoane Wissa moved from Brentford to Newcastle United (2025); 'plays for Brentford' is outdated (he's still a Premier League player, now at Newcastle).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle, not Brentford.

### Row 20985 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo attacker plays for Brentford in the 2026 World Cup qualifiers? **A:** Yoane Wissa
**Options:** Yoane Wissa | Chancel Mbemba | Cédric Bakambu | Gaël Kakuta
**Why it fails:** Yoane Wissa moved from Brentford to Newcastle United (2025); 'plays for Brentford' is outdated (he's still a Premier League player, now at Newcastle).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle, not Brentford.

### Row 20986 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo attacker plays for Brentford in the Premier League? **A:** Yoane Wissa
**Options:** Yoane Wissa | Michy Batshuayi | Bryan Mbeumo | Maxwel Cornet
**Why it fails:** Yoane Wissa moved from Brentford to Newcastle United (2025); 'plays for Brentford' is outdated (he's still a Premier League player, now at Newcastle).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle, not Brentford.

### Row 20990 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo attacker, a Brentford forward, is a key player for the 2026 World Cup qualifiers? **A:** Yoane Wissa
**Options:** Yoane Wissa | Cédric Bakambu | Dieumerci Mbokani | Benik Afobe
**Why it fails:** Yoane Wissa moved from Brentford to Newcastle United (2025); 'plays for Brentford' is outdated (he's still a Premier League player, now at Newcastle).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle, not Brentford.

### Row 21000 — DR Congo (easy) — FAIL: outdated — Mbemba now at Lille
**Q:** Which DR Congo centre-back has over 60 caps and plays for Marseille? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Arthur Masuaku | Marcel Tisserand | Christian Luyindama
**Why it fails:** Chancel Mbemba moved from Marseille to Lille in 2025; 'plays for Marseille' is outdated.
**Source:** https://en.wikipedia.org/wiki/Chancel_Mbemba
**Remedy:** Mbemba plays for Lille, not Marseille.

### Row 21002 — DR Congo (easy) — FAIL: outdated — Mbemba now at Lille
**Q:** Which DR Congo centre-back plays for Marseille for the 2026 World Cup cycle? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Cédric Bakambu | Yoane Wissa | Arthur Masuaku
**Why it fails:** Chancel Mbemba moved from Marseille to Lille in 2025; 'plays for Marseille' is outdated.
**Source:** https://en.wikipedia.org/wiki/Chancel_Mbemba
**Remedy:** Mbemba plays for Lille, not Marseille.

### Row 21003 — DR Congo (easy) — FAIL: outdated — Mbemba now at Lille
**Q:** Which DR Congo centre-back started the 2026 World Cup qualifier for Marseille? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Cédric Bakambu | Arthur Masuaku | Silas Katompa
**Why it fails:** Chancel Mbemba moved from Marseille to Lille in 2025; 'plays for Marseille' is outdated.
**Source:** https://en.wikipedia.org/wiki/Chancel_Mbemba
**Remedy:** Mbemba plays for Lille, not Marseille.

### Row 21006 — DR Congo (easy) — FAIL: outdated — Mbemba now at Lille
**Q:** Which DR Congo centre-back with over 60 caps plays for Marseille in the 2026 World Cup cycle? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Cédric Bakambu | Arthur Masuaku | Silas Katompa
**Why it fails:** Chancel Mbemba moved from Marseille to Lille in 2025; 'plays for Marseille' is outdated.
**Source:** https://en.wikipedia.org/wiki/Chancel_Mbemba
**Remedy:** Mbemba plays for Lille, not Marseille.

### Row 21007 — DR Congo (easy) — FAIL: outdated — Mbemba now at Lille
**Q:** Which DR Congo centre-back with over 60 caps plays for Marseille? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Cédric Bakambu | Arthur Masuaku | Silas Katompa
**Why it fails:** Chancel Mbemba moved from Marseille to Lille in 2025; 'plays for Marseille' is outdated.
**Source:** https://en.wikipedia.org/wiki/Chancel_Mbemba
**Remedy:** Mbemba plays for Lille, not Marseille.

### Row 21009 — DR Congo (easy) — FAIL: outdated — Mbemba now at Lille
**Q:** Which DR Congo centre-back, playing for Marseille, aims for the 2026 World Cup? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Cédric Bakambu | Arthur Masuaku | Silas Katompa
**Why it fails:** Chancel Mbemba moved to Lille in 2025; the present-tense 'plays for Marseille' is outdated.
**Source:** https://en.wikipedia.org/wiki/Chancel_Mbemba
**Remedy:** Mbemba plays for Lille (he was at Marseille until 2025).

### Row 21041 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which DR Congo defender debuted at 2022 World Cup? **A:** Arthur Masuaku
**Options:** Arthur Masuaku | Cédric Bakambu | Chancel Mbemba | Yoane Wissa
**Why it fails:** DR Congo did not play at the 2022 World Cup, so no defender 'debuted at the 2022 World Cup'.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 squad.

### Row 21051 — DR Congo (easy) — FAIL: outdated — Mbemba now at Lille
**Q:** Which DR Congo defender plays for Marseille in 2026? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Arthur Masuaku | Cédric Bakambu | Silas Katompa
**Why it fails:** Chancel Mbemba moved to Lille in 2025; the present-tense 'plays for Marseille' is outdated.
**Source:** https://en.wikipedia.org/wiki/Chancel_Mbemba
**Remedy:** Mbemba plays for Lille (he was at Marseille until 2025).

### Row 21054 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which DR Congo defender provided experience at the 2022 FIFA World Cup? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Yoane Wissa | Dieumerci Mbokani | Cédric Bakambu
**Why it fails:** false premise — DR Congo did NOT play at the 2022 World Cup, so there was no DR Congo squad/debut/player there.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 squad (Mbemba did provide experience there).

### Row 21080 — DR Congo (easy) — FAIL: outdated — Mbemba now at Lille
**Q:** Which DR Congo defender, with over 60 caps, plays for Marseille? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Arthur Masuaku | Dylan Batubinsika | Christian Luyindama
**Why it fails:** Chancel Mbemba moved to Lille in 2025; the present-tense 'plays for Marseille' is outdated.
**Source:** https://en.wikipedia.org/wiki/Chancel_Mbemba
**Remedy:** Mbemba plays for Lille (he was at Marseille until 2025).

### Row 21104 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo forward for the 2026 cycle plays for Brentford? **A:** Yoane Wissa
**Options:** Yoane Wissa | Cédric Bakambu | Chancel Mbemba | Arthur Masuaku
**Why it fails:** Yoane Wissa moved to Newcastle United in 2025; the present-tense 'plays for Brentford' is outdated (he's still a Premier League player, now at Newcastle).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle, not Brentford.

### Row 21119 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo forward plays for Brentford in the 2026 World Cup cycle? **A:** Yoane Wissa
**Options:** Yoane Wissa | Cédric Bakambu | Chancel Mbemba | Silas Katompa
**Why it fails:** Yoane Wissa moved to Newcastle United in 2025; the present-tense 'plays for Brentford' is outdated (he's still a Premier League player, now at Newcastle).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle, not Brentford.

### Row 21127 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo forward, key for 2026 World Cup cycle, plays for Brentford? **A:** Yoane Wissa
**Options:** Yoane Wissa | Cédric Bakambu | Chancel Mbemba | Arthur Masuaku
**Why it fails:** Yoane Wissa moved to Newcastle United in 2025; the present-tense 'plays for Brentford' is outdated (he's still a Premier League player, now at Newcastle).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle, not Brentford.

### Row 21128 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo forward, playing for Brentford, is key for 2026 World Cup qualifiers? **A:** Yoane Wissa
**Options:** Yoane Wissa | Cédric Bakambu | Chancel Mbemba | Arthur Masuaku
**Why it fails:** Yoane Wissa moved to Newcastle United in 2025; the present-tense 'plays for Brentford' is outdated (he's still a Premier League player, now at Newcastle).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle, not Brentford.

### Row 21129 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo forward, playing for Brentford, was key for the 2026 World Cup cycle? **A:** Yoane Wissa
**Options:** Yoane Wissa | Cédric Bakambu | Chancel Mbemba | Silas Katompa
**Why it fails:** Yoane Wissa moved to Newcastle United in 2025; the present-tense 'plays for Brentford' is outdated (he's still a Premier League player, now at Newcastle).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle, not Brentford.

### Row 21130 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo forward's 2026 World Cup cycle preparation is with Brentford? **A:** Yoane Wissa
**Options:** Yoane Wissa | Cédric Bakambu | Chancel Mbemba | Silas Katompa
**Why it fails:** Yoane Wissa moved to Newcastle United in 2025; the present-tense 'plays for Brentford' is outdated (he's still a Premier League player, now at Newcastle).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle, not Brentford.

### Row 21133 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo key attacker in 2026 World Cup qualifying plays for Brentford? **A:** Yoane Wissa
**Options:** Yoane Wissa | Cédric Bakambu | Dieumerci Mbokani | Benik Afobe
**Why it fails:** Yoane Wissa moved to Newcastle United in 2025; the present-tense 'plays for Brentford' is outdated (he's still a Premier League player, now at Newcastle).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle, not Brentford.

### Row 21150 — DR Congo (easy) — FAIL: false premise (not at 2022 WC) + outdated club
**Q:** Which DR Congo player at 2022 World Cup plays for Brentford? **A:** Yoane Wissa
**Options:** Yoane Wissa | Christian Eriksen | Bryan Mbeumo | Romain Faivre
**Why it fails:** false premise — DR Congo did NOT play at the 2022 World Cup, so there was no DR Congo squad/debut/player there. (Wissa is also now at Newcastle, not Brentford.)
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 squad / 2023 AFCON; Wissa is at Newcastle.

### Row 21152 — DR Congo (easy) — FAIL: false premise (not at 2022 WC) + outdated club
**Q:** Which DR Congo player at the 2022 World Cup came from England's Premier League? **A:** Yoane Wissa
**Options:** Yoane Wissa | Chancel Mbemba | Cédric Bakambu | Gaël Kakuta
**Why it fails:** false premise — DR Congo did NOT play at the 2022 World Cup, so there was no DR Congo squad/debut/player there. (Wissa is also now at Newcastle, not Brentford.)
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 squad / 2023 AFCON; Wissa is at Newcastle.

### Row 21153 — DR Congo (easy) — FAIL: false premise (not at 2022 WC) + outdated club
**Q:** Which DR Congo player at the 2022 World Cup did NOT play in Ligue 1? **A:** Yoane Wissa
**Options:** Yoane Wissa | Chancel Mbemba | Cédric Bakambu | Gaël Kakuta
**Why it fails:** false premise — DR Congo did NOT play at the 2022 World Cup, so there was no DR Congo squad/debut/player there. (Wissa is also now at Newcastle, not Brentford.)
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 squad / 2023 AFCON; Wissa is at Newcastle.

### Row 21154 — DR Congo (easy) — FAIL: false premise (not at 2022 WC) + outdated club
**Q:** Which DR Congo player at the 2022 World Cup played for a Premier League club? **A:** Yoane Wissa
**Options:** Yoane Wissa | Chancel Mbemba | Cédric Bakambu | Gaël Kakuta
**Why it fails:** false premise — DR Congo did NOT play at the 2022 World Cup, so there was no DR Congo squad/debut/player there. (Wissa is also now at Newcastle, not Brentford.)
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 squad / 2023 AFCON; Wissa is at Newcastle.

### Row 21166 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo player from Brentford is a key attacker in their 2026 World Cup qualifiers? **A:** Yoane Wissa
**Options:** Yoane Wissa | Cédric Bakambu | Gaël Kakuta | Dieumerci Mbokani
**Why it fails:** Wissa moved from Brentford to Newcastle (2025); the present-tense Brentford reference is outdated (he's still in the Premier League).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle.

### Row 21170 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo player in their 2026 squad plays for Brentford? **A:** Yoane Wissa
**Options:** Yoane Wissa | Cédric Bakambu | Gaël Kakuta | Chancel Mbemba
**Why it fails:** Wissa moved from Brentford to Newcastle (2025); the present-tense Brentford reference is outdated (he's still in the Premier League).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle.

### Row 21179 — DR Congo (easy) — FAIL: false premise (not at 2018 WC)
**Q:** Which DR Congo player played at 2018 World Cup? **A:** Cédric Bakambu
**Options:** Cédric Bakambu | Chancel Mbemba | Yoane Wissa | Arthur Masuaku
**Why it fails:** DR Congo did not play at the 2018 World Cup, so Bakambu didn't 'play at the 2018 World Cup'.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor; Bakambu's first WC will be 2026.

### Row 21180 — DR Congo (easy) — FAIL: outdated — Mbemba now at Lille
**Q:** Which DR Congo player played for Marseille in 2026? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Cédric Bakambu | Yoane Wissa | Arthur Masuaku
**Why it fails:** Mbemba moved to Lille in 2025; 'plays for Marseille in 2026' is outdated.
**Source:** https://en.wikipedia.org/wiki/Chancel_Mbemba
**Remedy:** Mbemba plays for Lille.

### Row 21181 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Which DR Congo player plays for Brentford in 2026? **A:** Yoane Wissa
**Options:** Yoane Wissa | Cédric Bakambu | Chancel Mbemba | Arthur Masuaku
**Why it fails:** Wissa moved from Brentford to Newcastle (2025); the present-tense Brentford reference is outdated (he's still in the Premier League).
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle.

### Row 21182 — DR Congo (easy) — FAIL: outdated — Mbemba now at Lille
**Q:** Which DR Congo player plays for Marseille in 2026? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Cédric Bakambu | Yoane Wissa | Arthur Masuaku
**Why it fails:** Mbemba moved to Lille in 2025; 'plays for Marseille in 2026' is outdated.
**Source:** https://en.wikipedia.org/wiki/Chancel_Mbemba
**Remedy:** Mbemba plays for Lille.

### Row 21183 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which DR Congo player plays in Premier League at 2022 World Cup? **A:** Yoane Wissa
**Options:** Yoane Wissa | Chancel Mbemba | Dieumerci Mbokani | Cedric Bakambu
**Why it fails:** false premise — DR Congo did NOT play at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 squad / 2023 AFCON.

### Row 21204 — DR Congo (hard) — FAIL: self-referential / confused
**Q:** Which DR Congo squad featured players from an AFCON regular that missed the 2022 World Cup? **A:** DR Congo 2026 qualifiers
**Options:** DR Congo 2026 qualifiers | DR Congo 2022 qualifiers | DR Congo 2018 qualifiers | DR Congo 2014 qualifiers
**Why it fails:** The 'AFCON regular that missed the 2022 World Cup' IS DR Congo, so the answer ('DR Congo 2026 qualifiers') is self-referential.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_national_football_team
**Remedy:** Reword to avoid the self-reference.

### Row 21207 — DR Congo (medium) — FAIL: non-unique (all those squads failed)
**Q:** Which DR Congo squad has never qualified for the FIFA World Cup? **A:** The 2022 squad
**Options:** The 2022 squad | The 2018 squad | The 2014 squad | The 2010 squad
**Why it fails:** DR Congo's 2010, 2014, 2018 AND 2022 squads all failed to qualify, so every option is correct.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Make it specific.

### Row 21250 — DR Congo (medium) — FAIL: wrong — 2023 was a semi-final
**Q:** Which DR Congo team matched its 2023 AFCON quarter-final run in the 2010s? **A:** 2015 AFCON semi-finalists
**Options:** 2015 AFCON semi-finalists | 2013 AFCON quarter-finalists | 2017 AFCON quarter-finalists | 2019 AFCON quarter-finalists
**Why it fails:** DR Congo also reached the SEMIS in 2023, so it didn't merely 'match a 2015 QF' — both were semi-final runs.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** Both 2015 and 2023 were semis.

### Row 21251 — DR Congo (medium) — FAIL: wrong — both 2015 and 2023 were semis
**Q:** Which DR Congo team progressed further in AFCON, their 2015 or 2023 side? **A:** The 2015 team
**Options:** The 2015 team | The 2023 team | They progressed equally | The 2013 team
**Why it fails:** DR Congo reached the semi-finals in BOTH 2015 and 2023, so 2015 did not progress further than 2023.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** They went equally far (both semis).

### Row 21252 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Which DR Congo team qualified for its first FIFA World Cup in 2026? **A:** DR Congo
**Options:** DR Congo | Zambia | Uganda | Tanzania
**Why it fails:** Self-referential: in a DR Congo category, 'which nation, like DR Congo, …?' answers DR Congo itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different nation.

### Row 21254 — DR Congo (easy) — FAIL: self-referential + 2023 was the semis
**Q:** Which DR Congo team reached the 2023 AFCON quarter-finals? **A:** DR Congo
**Options:** DR Congo | Côte d'Ivoire | Morocco | Senegal
**Why it fails:** Answer 'DR Congo' is self-referential, and DR Congo reached the 2023 AFCON SEMI-finals (4th), not the quarter-finals.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** Name another QF team and fix the stage.

### Row 21272 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which league does DR Congo's Yoane Wissa play in at 2022 World Cup? **A:** Premier League
**Options:** Premier League | Bundesliga | Serie A | La Liga
**Why it fails:** false premise — DR Congo did NOT play at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 squad / 2023 AFCON.

### Row 21280 — DR Congo (easy) — FAIL: wrong — Bundesliga IS represented
**Q:** Which league was not represented in DR Congo's 2026 World Cup qualifying squad? **A:** Bundesliga
**Options:** Bundesliga | Ligue 1 | Premier League | La Liga
**Why it fails:** Silas Katompa plays for VfB Stuttgart (Bundesliga), so the Bundesliga IS represented in DR Congo's squad.
**Source:** https://en.wikipedia.org/wiki/Silas_Katompa_Mvumpa
**Remedy:** Pick a league genuinely absent.

### Row 21285 — DR Congo (easy) — FAIL: false premise (no 2018 WC squad)
**Q:** Which leagues did DR Congo's 2018 World Cup squad draw from? **A:** Ligue 1 Premier
**Options:** Ligue 1 Premier | Bundesliga Pro | Serie A Elite | La Liga Premier
**Why it fails:** DR Congo did not qualify for the 2018 World Cup, so there was no '2018 World Cup squad'.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to a real campaign.

### Row 21319 — DR Congo (easy) — FAIL: wrong — not the most Europe-based
**Q:** Which nation has most players in 2022 European leagues, DR Congo, Morocco, Egypt, or Senegal? **A:** DR Congo
**Options:** DR Congo | Morocco | Egypt | Senegal
**Why it fails:** DR Congo do NOT have the most Europe-based players among DR Congo/Morocco/Egypt/Senegal — Morocco and Senegal field almost entirely European-based squads.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_national_football_team
**Remedy:** Drop the comparative claim.

### Row 21329 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Which nation qualified for 2026 like DR Congo? **A:** DR Congo
**Options:** DR Congo | Senegal | Egypt | Morocco
**Why it fails:** Self-referential: in a DR Congo category, 'which nation, like DR Congo, …?' answers DR Congo itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different nation.

### Row 21332 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Which nation qualified for its first World Cup under the name DR Congo in 2026? **A:** DR Congo
**Options:** DR Congo | Ivory Coast | Tanzania | Zimbabwe
**Why it fails:** Self-referential: in a DR Congo category, 'which nation, like DR Congo, …?' answers DR Congo itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different nation.

### Row 21336 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Which nation qualified for the 2026 World Cup like DR Congo? **A:** DR Congo
**Options:** DR Congo | Morocco | Tunisia | Algeria
**Why it fails:** Self-referential: in a DR Congo category, 'which nation, like DR Congo, …?' answers DR Congo itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different nation.

### Row 21338 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Which nation qualified for their first FIFA World Cup as DR Congo in 2026? **A:** DR Congo
**Options:** DR Congo | Côte d'Ivoire | Bosnia-Herzegovina | North Macedonia
**Why it fails:** Self-referential: in a DR Congo category, 'which nation, like DR Congo, …?' answers DR Congo itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different nation.

### Row 21339 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Which nation qualified in 2026 like DR Congo? **A:** DR Congo
**Options:** DR Congo | Senegal | Morocco | Egypt
**Why it fails:** Self-referential: in a DR Congo category, 'which nation, like DR Congo, …?' answers DR Congo itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different nation.

### Row 21351 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Which nation, like DR Congo in 2026, ended a 50+ year World Cup drought? **A:** DR Congo
**Options:** DR Congo | Cameroon | Nigeria | Senegal
**Why it fails:** Self-referential: in a DR Congo category, 'which nation, like DR Congo, …?' answers DR Congo itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different nation.

### Row 21352 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Which nation, like DR Congo in 2026, last qualified for a World Cup over 50 years ago? **A:** DR Congo
**Options:** DR Congo | Cameroon | Senegal | Morocco
**Why it fails:** Self-referential: in a DR Congo category, 'which nation, like DR Congo, …?' answers DR Congo itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different nation.

### Row 21363 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which player is DR Congo's key attacker at 2022 FIFA World Cup? **A:** Yoane Wissa
**Options:** Yoane Wissa | Chancel Mbemba | Dieumerci Mbokani | Cedric Bakambu
**Why it fails:** false premise — DR Congo did NOT play at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 squad / 2023 AFCON.

### Row 21372 — DR Congo (easy) — FAIL: wrong — 2023 AFCON was the SEMIS
**Q:** Which round did DR Congo reach at the 2023 AFCON? **A:** Quarter-finals
**Options:** Quarter-finals | Semi-finals | Final | Round of 16
**Why it fails:** DR Congo reached the SEMI-FINALS of the 2023 AFCON (4th), not the quarter-finals.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** Answer: the semi-finals (4th).

### Row 21379 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Which stadium hosts DR Congo at 2022 World Cup? **A:** Stade des Martyrs
**Options:** Stade des Martyrs | Stade Tata Raphaël | Stade Frederic Kibassa | Stade du 20 Mai
**Why it fails:** DR Congo were not at the 2022 World Cup, and the WC isn't hosted at their home stadium — 'hosts DR Congo at 2022 World Cup' is a false premise.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to home qualifiers.

### Row 21385 — DR Congo (easy) — FAIL: wrong — 2023 AFCON was the SEMIS
**Q:** Which stage did DR Congo reach at the 2023 Africa Cup of Nations? **A:** Quarter-finals
**Options:** Quarter-finals | Semi-finals | Round of 16 | Final
**Why it fails:** DR Congo reached the SEMI-FINALS of the 2023 AFCON (4th place), not the quarter-finals.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** Answer: the semi-finals (4th).

### Row 21387 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Which team debuted at 2026 FIFA World Cup like DR Congo? **A:** DR Congo
**Options:** DR Congo | Ghana | Senegal | Morocco
**Why it fails:** Self-referential: in a DR Congo category, 'which team/nation/who, like DR Congo, …?' answers DR Congo itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different team.

### Row 21392 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Which team failed to qualify for multiple World Cups like DR Congo? **A:** DR Congo
**Options:** DR Congo | China | Canada | Bolivia
**Why it fails:** Self-referential: in a DR Congo category, 'which team/nation/who, like DR Congo, …?' answers DR Congo itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different team.

### Row 21395 — DR Congo (medium) — FAIL: self-referential answer
**Q:** Which team had a historic 2026 World Cup qualification like DR Congo? **A:** DR Congo
**Options:** DR Congo | Senegal | Egypt | Morocco
**Why it fails:** Self-referential: in a DR Congo category, 'which team/nation/who, like DR Congo, …?' answers DR Congo itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different team.

### Row 21403 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Which team qualified for 2026 like DR Congo? **A:** DR Congo
**Options:** DR Congo | South Africa | Egypt | Morocco
**Why it fails:** Self-referential: in a DR Congo category, 'which team/nation/who, like DR Congo, …?' answers DR Congo itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different team.

### Row 21405 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Which team qualified for 2026 World Cup like DR Congo? **A:** DR Congo
**Options:** DR Congo | Ghana | Senegal | Morocco
**Why it fails:** Self-referential: in a DR Congo category, 'which team/nation/who, like DR Congo, …?' answers DR Congo itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different team.

### Row 21413 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Which team reached 2015 AFCON semi-finals like DR Congo? **A:** DR Congo
**Options:** DR Congo | Ghana | Ivory Coast | Cameroon
**Why it fails:** Self-referential: in a DR Congo category, 'which team/nation/who, like DR Congo, …?' answers DR Congo itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different team.

### Row 21415 — DR Congo (easy) — FAIL: self-referential + 2023 was the semis
**Q:** Which team reached 2023 AFCON quarter-finals like DR Congo? **A:** DR Congo
**Options:** DR Congo | Egypt | Morocco | Senegal
**Why it fails:** Answer 'DR Congo' is self-referential, and DR Congo reached the 2023 AFCON SEMIS (4th), not the quarter-finals.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** Name another team and fix the stage.

### Row 21420 — DR Congo (easy) — FAIL: non-unique (all options are AFCON regulars)
**Q:** Which teams are regular AFCON participants like DR Congo? **A:** Egypt
**Options:** Egypt | Ghana | Nigeria | Morocco
**Why it fails:** Egypt, Ghana, Nigeria AND Morocco are all regular AFCON participants like DR Congo — every option is correct.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_national_football_team
**Remedy:** Pick a non-regular as the distractor set.

### Row 21446 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Who benefits from DR Congo's European leagues talent in 2026? **A:** DR Congo
**Options:** DR Congo | Morocco | Egypt | Senegal
**Why it fails:** Self-referential: in a DR Congo category, 'which team/nation/who, like DR Congo, …?' answers DR Congo itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different team.

### Row 21451 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Who defends DR Congo at 2022 World Cup? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Yoane Wissa | Dieumerci Mbokani | Cedric Bakambu
**Why it fails:** false premise — DR Congo did NOT play at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 squad / 2023 AFCON.

### Row 21464 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Who is DR Congo's key attacker at 2022 FIFA World Cup? **A:** Yoane Wissa
**Options:** Yoane Wissa | Chancel Mbemba | Dieumerci Mbokani | Cedric Bakambu
**Why it fails:** false premise — DR Congo did NOT play at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 squad / 2023 AFCON.

### Row 21467 — DR Congo (easy) — FAIL: false premise (DR Congo missed AFCON 2021)
**Q:** Who is DR Congo's key defender at AFCON 2021? **A:** Arthur Masuaku
**Options:** Arthur Masuaku | Chancel Mbemba | Cédric Bakambu | Yoane Wissa
**Why it fails:** DR Congo did not qualify for the 2021 AFCON, so there was no 'key defender at AFCON 2021'.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_national_football_team
**Remedy:** Re-anchor to 2023 (or 2015).

### Row 21475 — DR Congo (easy) — FAIL: wrong — Desabre (not Ibenge) led the 2023 AFCON
**Q:** Who led DR Congo at 2023 AFCON? **A:** Florent Ibengé
**Options:** Florent Ibengé | Héctor Cúper | Patrice Beaumelle | Sven Vandenbroeck
**Why it fails:** Sébastien Desabre managed DR Congo at the 2023 AFCON (to the semis/4th); Florent Ibenge led the 2015 edition, not 2023.
**Source:** https://en.wikipedia.org/wiki/S%C3%A9bastien_Desabre
**Remedy:** Answer: Sébastien Desabre (and the stage was the semis).

### Row 21480 — DR Congo (easy) — FAIL: false premise (not at 2018 WC)
**Q:** Who led DR Congo's defense at 2018 World Cup? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Yoane Wissa | Dieumerci Mbokani | Cedric Bakambu
**Why it fails:** false premise — DR Congo did NOT play at the 2018 World Cup.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to a real campaign.

### Row 21481 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Who led DR Congo's defense at 2022 World Cup? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Cédric Bakambu | Yoane Wissa | Arthur Masuaku
**Why it fails:** false premise — DR Congo did NOT play at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 squad / 2023 AFCON.

### Row 21483 — DR Congo (easy) — FAIL: wrong — Desabre managed the 2023 AFCON
**Q:** Who managed DR Congo at 2023 AFCON? **A:** Florent Ibenge
**Options:** Florent Ibenge | Hector Cuper | Patrice Beaumelle | Sven Vandenbroeck
**Why it fails:** The 2023 AFCON manager was Desabre, not Ibenge (who left in 2018); DR Congo also reached the semis, not the QF.
**Source:** https://en.wikipedia.org/wiki/S%C3%A9bastien_Desabre
**Remedy:** Answer: Sébastien Desabre.

### Row 21502 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Who played for DR Congo at 2022 World Cup? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Cédric Bakambu | Yoane Wissa | Arthur Masuaku
**Why it fails:** false premise — DR Congo did NOT play at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 squad / 2023 AFCON.

### Row 21505 — DR Congo (easy) — FAIL: outdated — Wissa now at Newcastle
**Q:** Who plays for Brentford in 2026 for DR Congo? **A:** Yoane Wissa
**Options:** Yoane Wissa | Cédric Bakambu | Chancel Mbemba | Arthur Masuaku
**Why it fails:** Wissa moved to Newcastle in 2025; 'plays for Brentford in 2026' is outdated.
**Source:** https://en.wikipedia.org/wiki/Yoane_Wissa
**Remedy:** Wissa plays for Newcastle.

### Row 21507 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Who plays in Ligue 1 for DR Congo at 2022 World Cup? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Yoane Wissa | Other players | No one
**Why it fails:** false premise — DR Congo did NOT play at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 squad / 2023 AFCON.

### Row 21517 — DR Congo (easy) — FAIL: false premise (not at 2022 WC)
**Q:** Who provides defensive experience in DR Congo's squad at 2022 World Cup? **A:** Chancel Mbemba
**Options:** Chancel Mbemba | Yoane Wissa | Dieumerci Mbokani | Cedric Bakambu
**Why it fails:** false premise — DR Congo did NOT play at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Re-anchor to the 2026 squad / 2023 AFCON.

### Row 21519 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Who qualified DR Congo for 2026 World Cup? **A:** DR Congo
**Options:** DR Congo | Ghana | Senegal | Morocco
**Why it fails:** Self-referential: in a DR Congo category, 'which team/nation/who, like DR Congo, …?' answers DR Congo itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different team.

### Row 21520 — DR Congo (easy) — FAIL: self-referential answer
**Q:** Who qualified DR Congo for 2026? **A:** DR Congo
**Options:** DR Congo | Ghana | Morocco | Senegal
**Why it fails:** Self-referential: in a DR Congo category, 'which team/nation/who, like DR Congo, …?' answers DR Congo itself.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** Name a different team.

### Row 21547 — DR Congo (easy) — FAIL: nonsensical + outdated
**Q:** Why did DR Congo not qualify in 2018? **A:** New Name
**Options:** New Name | New Kit | New Coach | New Style
**Why it fails:** 'New Name' is not a reason DR Congo failed to qualify in 2018, and the 'never qualified under current name' premise is now outdated (they qualified for 2026).
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Drop — incoherent reason.

### Row 21548 — DR Congo (easy) — FAIL: nonsensical + outdated
**Q:** Why did DR Congo not qualify in 2022? **A:** New Name
**Options:** New Name | New Coach | New Sponsor | New Stadium
**Why it fails:** 'New Name' is not why DR Congo missed 2022, and they have since qualified for 2026.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_at_the_FIFA_World_Cup
**Remedy:** Drop — incoherent reason.

### Row 21552 — DR Congo (easy) — FAIL: wrong — 2023 AFCON was the SEMIS
**Q:** Why did DR Congo reach the 2023 AFCON quarter-finals? **A:** Reached the quarter-finals
**Options:** Reached the quarter-finals | Won the tournament | Reached the final | Were eliminated in group stage
**Why it fails:** DR Congo reached the SEMI-FINALS of the 2023 AFCON (4th place), not the quarter-finals. (And the question is tautological.)
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations_knockout_stage
**Remedy:** They reached the semi-finals.

### Row 21561 — DR Congo (easy) — FAIL: wrong — DR Congo don't 'consistently struggle' at AFCON
**Q:** Why do DR Congo consistently struggle at the AFCON? **A:** Strong North African teams
**Options:** Strong North African teams | Weak domestic league | Poor youth development | Lack of experienced coaches
**Why it fails:** DR Congo have WON the AFCON twice (1968, 1974) and reached the semi-finals as recently as 2015 and 2023 — the 'consistently struggle' premise is false.
**Source:** https://en.wikipedia.org/wiki/DR_Congo_national_football_team
**Remedy:** Drop — false premise.

### Row 21566 — DR Congo (easy) — FAIL: outdated — DR Congo qualified for 2026
**Q:** Why has DR Congo never played at a FIFA World Cup under their current name? **A:** They have never qualified
**Options:** They have never qualified | They withdrew from qualifying | They were disqualified | They lost a playoff
**Why it fails:** DR Congo HAVE now qualified for a World Cup under their current name (2026, via the intercontinental playoff), so 'never qualified / failed to qualify under current name' is outdated.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** They qualified for 2026 (first under the name DR Congo).

### Row 21567 — DR Congo (easy) — FAIL: outdated — DR Congo qualified for 2026
**Q:** Why has DR Congo never reached a FIFA World Cup under its current name? **A:** Failed to qualify
**Options:** Failed to qualify | Boycotted tournaments | Were suspended by FIFA | Lost a playoff
**Why it fails:** DR Congo HAVE now qualified for a World Cup under their current name (2026, via the intercontinental playoff), so 'never qualified / failed to qualify under current name' is outdated.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** They qualified for 2026 (first under the name DR Congo).

### Row 21568 — DR Congo (easy) — FAIL: outdated — DR Congo qualified for 2026
**Q:** Why has DR Congo not qualified for a FIFA World Cup under their current name? **A:** They have never qualified
**Options:** They have never qualified | They withdrew from qualifiers | They were disqualified | They lost a playoff
**Why it fails:** DR Congo HAVE now qualified for a World Cup under their current name (2026, via the intercontinental playoff), so 'never qualified / failed to qualify under current name' is outdated.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(inter-confederation_play-offs)
**Remedy:** They qualified for 2026 (first under the name DR Congo).
<!-- ===== Austria (rows 3242+) — NEW METHOD ===== -->

### Row 3251 — FAIL: spreadsheet date-corruption
**Q:** At Euro 2024, Austria beat the Netherlands by what scoreline? **A:** 03-Feb (E: "ended 3-2")
**Why it fails:** The answer cell `03-Feb` is an Excel-mangled `3-2`. The correct scoreline (per the
explanation and live sources) is **3-2**, but the rendered answer is a corrupted date string.
**Source:** https://www.cbc.ca/sports/soccer/european-championship-soccer-roundup-july2-1.7252081
**Remedy:** Restore the answer to `3-2`; flag for a dataset-wide date-corruption sweep.

### Row 3270 — FAIL: 2022 World Cup false premise
**Q:** At the 2022 World Cup, which Austria player was their star but faced injury problems? **A:** David Alaba
**Why it fails:** Austria **did not qualify** for the 2022 World Cup, so there was no Austria player "at
the 2022 World Cup." The premise asserts an event that did not happen. (Alaba is indeed Austria's star,
but the framing is false.)
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Re-anchor to Euro 2024 (or to qualifying), e.g. "Austria's star at Euro 2024 who faced injury problems."

### Rows 3276, 3277 — FAIL: wrong answer (first Euro group stage was 2008, not 2016)
- **3276:** "At which European Championship did Austria first reach the group stage? → Euro 2016"
- **3277:** "At which Euros did Austria's men's team first reach the group stage? → Euro 2016"
**Why they fail:** Austria's **first** UEFA European Championship appearance (and group stage) was **Euro
2008**, as co-hosts with Switzerland — not Euro 2016. Worse, **Euro 2008 is offered as a distractor** in
both rows, so the keyed answer is wrong while a correct option is present.
**Source:** https://en.wikipedia.org/wiki/Austria_at_the_UEFA_European_Championship
**Remedy:** Change the answer to **Euro 2008**, or reword to "first *qualified on merit*" (Euro 2016) and remove the 2008 distractor.

<!-- ===== Austria batch 3291-3460 ===== -->

### Rows 3291, 3292, 3373, 3450, 3451, 3454, 3455, 3459, 3460 — FAIL: corrupted answer "03-Feb" (= 3-2)
All ask Austria's scoreline in the Euro 2024 win over the Netherlands; the answer cell is the
Excel-mangled date **`03-Feb`** instead of **`3-2`** (the explanations all correctly say 3-2).
**Source:** https://www.skysports.com/football/news/26806/13157522/euro-2024-netherlands-2-3-austria
**Remedy:** Restore the answer to `3-2`; sweep the dataset for `DD-Mon` date-corrupted scorelines.

### Rows 3319, 3320, 3321 — FAIL: corrupted answer "02-Jan" (= 2-1)
Ask Austria's scoreline vs Italy (Euro 2020) / Türkiye (Euro 2024); the answer cell is the
Excel-mangled date **`02-Jan`** instead of **`2-1`**.
**Source:** https://en.wikipedia.org/wiki/Austria_at_the_UEFA_European_Championship
**Remedy:** Restore the answer to `2-1`.

### Row 3310 — FAIL: false premise + wrong answer
**Q:** ...Which team beat them 2-1 at the 2018 World Cup? **A:** Croatia (E: "Austria did not qualify for the 2018 World Cup, so no team beat them 2-1")
**Why it fails:** Austria didn't play at the 2018 WC, so the premise is false and the keyed answer
"Croatia" directly contradicts the explanation. No option can be correct.
**Source:** https://en.wikipedia.org/wiki/Austria_at_the_FIFA_World_Cup
**Remedy:** Drop, or re-anchor to a real match.

### Row 3315 — FAIL: non-unique answer
**Q:** Which nation did Austria NOT face in a Euro knockout stage? **A:** The Netherlands (O: Netherlands | Germany | Italy | Turkey)
**Why it fails:** Austria's only Euro knockout opponents are **Italy** (2020) and **Türkiye** (2024).
So **both** "Netherlands" and "Germany" are correct ("not faced") — the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/Austria_at_the_UEFA_European_Championship
**Remedy:** Replace one of the unfaced-nation distractors so only one option fits.

### Rows 3341, 3427, 3431 — FAIL: wrong year (Euro 2020 was played in 2021)
- **3341:** "In which year did Austria reach the Euro 2020 R16? → 2020" (no 2021 option)
- **3427:** "In which year did Austria lose 2-1 to Italy in extra time? → 2020" (2021 *was* an option)
- **3431:** "In which year did Austria reach the Euro 2020 round of 16? → 2020"
**Why they fail:** All Austria's Euro 2020 matches (incl. the R16 loss to Italy) were played in
**June 2021** (tournament postponed). The dataset's own rows 3307/3317/3426 correctly answer 2021;
keying 2020 here is internally inconsistent and factually wrong.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Change the answer to **2021**.

### Rows 3344, 3348 — FAIL: 2022 World Cup false premise
- **3344:** "Austria's **2022 World Cup** midfield quality was provided by which player? → Sabitzer"
- **3348:** "Austria's **2022 World Cup squad** featured many Bundesliga players. Which year? → 2022"
**Why they fail:** Austria **did not play at the 2022 World Cup** (failed to qualify), so there was
no 2022 WC squad/midfield. (Sabitzer and the Bundesliga point are true of the *qualifiers*, but the
WC framing is a false premise — cf. the parallel "qualifiers" rows which pass.)
**Source:** https://en.wikipedia.org/wiki/Austria_at_the_FIFA_World_Cup
**Remedy:** Reword to "2022 World Cup **qualifiers**."

### Rows 3376, 3377 — FAIL: wrong fact (top-scorer timing)
**Q:** Before/by the 2022 World Cup, which Austrian had become the nation's all-time top scorer? **A:** Marko Arnautović
**Why it fails:** Arnautović became Austria's all-time top scorer on **9 Oct 2025** (passing Toni
Polster). Before/by 2022 he was **not** yet the record holder — **Polster** still held it. (He did
become most-*capped* in Sep 2022, but that's caps, not goals.) Also a 2022-WC false premise.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Re-anchor to 2025 (when he became top scorer), or change to most-capped (Sep 2022).

### Rows 3415, 3434, 3436, 3437, 3438 — FAIL: wrong year (Rangnick rejected Bayern in 2024, not 2022)
All ask the year Rangnick turned down Bayern Munich to stay with Austria; all key **2022** (with
explanations claiming he did so "that same year" as his appointment). He was appointed in 2022 but
**rejected Bayern in May 2024** (after Tuchel's exit). 3434/3436 even offer **2024** as a distractor.
**Source:** https://www.espn.co.uk/football/story/_/id/40067631/rangnick-turns-bayern-munich-stay-austria
**Remedy:** Change the answer to **2024**; fix the "same year as appointment" explanations.

### Rows 3430, 3439 — FAIL: wrong qualification year (2025, not 2026)
**Q:** In which year did Austria / Rangnick's Austria qualify for the 2026 World Cup? **A:** 2026
**Why they fail:** Austria sealed 2026 qualification on **18 Nov 2025** (1-1 v Bosnia in Vienna,
group winners of UEFA Group H). The year is **2025**, not 2026 — and 2025 isn't even an option.
**Source:** https://www.nbcsports.com/soccer/news/austria-qualify-for-first-world-cup-in-28-years
**Remedy:** Change the answer to **2025** (add it as a choice).

### Row 3441 — FAIL: self-referential answer
**Q:** Under Koller, Austria's peak FIFA ranking was 10th. Which nation also peaked at 10th? **A:** Austria
**Why it fails:** The answer restates the subject nation — Austria can't be the "other" nation that
"also" peaked at 10th. Logically broken.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Drop, or supply a genuine other nation whose peak was 10th.

### Rows 3356, 3360 — FAIL: non-unique answer
- **3356:** "2026 qualification compares to which **earlier Euros qualification**? → Euro 2016" — but
  Austria also qualified for **Euro 2020** and **Euro 2024** (both offered), so the answer isn't unique.
- **3360:** "The 3-2 win over the Netherlands occurred **after** which other finals? → Euro 2020" — it
  occurred after *all* the offered finals (2020, 2016, 2008, 2012), so "after" is satisfied by several.
**Source:** https://en.wikipedia.org/wiki/Austria_at_the_UEFA_European_Championship
**Remedy:** Tighten the comparison so exactly one option fits (e.g. "most recent" / "immediately preceding").

---

## Austria batch rows 3461-3660 — 45 FAIL

### Rows 3461, 3462, 3463, 3465, 3468 — FAIL: Excel date-corruption of the scoreline
- **3461, 3462, 3463, 3465:** answer **"03-Feb"** is a mangled **"3-2"** (Austria beat the Netherlands 3-2 at Euro 2024).
- **3468:** answer **"02-Jan"** is a mangled **"2-1"** (Austria lost 2-1 to Türkiye).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024
**Remedy:** Store scorelines as text (e.g. `'3-2`) so Excel does not auto-convert them to dates.

### Rows 3480, 3498 — FAIL: Euro 2020 keyed "2020" though the match was played in 2021
- **3480:** "lose 2-1 to Italy in the Euro 2020 round of 16 → 2020" but the match was June 2021, and **2021 is among the options** — so the keyed answer is wrong/non-unique.
- **3498:** "reach the round of 16 at Euro 2020 → 2020" — self-referential and the R16 tie was played in 2021.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Key postponed Euro 2020 events to 2021, or drop the self-referential year question.

### Rows 3491, 3496, 3500, 3508, 3523 — FAIL: non-unique / wrong tournament-year answer
- **3491, 3496:** "qualify for / reach a Euro group stage → Euro 2016 / 2016" — Austria reached the group stage at **2008, 2016, 2020 and 2024** (several offered), so not unique.
- **3500:** "reach the UEFA Euro round of 16 → Euro 2020" — Austria reached the R16 at **both Euro 2020 and Euro 2024** (both offered).
- **3508:** "**last** reach the Euro group stage → 2016" — their most recent was **Euro 2024**.
- **3523:** "which **2010s** World Cup did Austria fail to qualify for → 2014" — they missed **2010, 2014 and 2018** (all offered), so not unique.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Rewrite so exactly one option is correct (e.g. "first" / "most recent").

### Row 3497 — FAIL: first Euro was 2008, not 2016
- "qualify for their **first** UEFA European Championship → Euro 2016" — Austria's first Euro finals was **Euro 2008** (as co-hosts).
**Source:** https://en.wikipedia.org/wiki/Austria_at_the_UEFA_European_Championship
**Remedy:** Change answer to Euro 2008, or reword to "first qualified-on-merit" if that is the intent.

### Rows 3493, 3494, 3495 — FAIL: Austria qualified in 2025, not 2026
- "When did Austria qualify for the 2026 FIFA World Cup → 2026" — qualification was secured on **18 Nov 2025**; "2026" is the tournament year, not the year they qualified. The correct year (2025) is not even offered.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Key the qualification year as 2025, or reword to "for which World Cup did Austria qualify".

### Rows 3505, 3518, 3519, 3547, 3548, 3549, 3554, 3583, 3584, 3586, 3591, 3592, 3593, 3594 — FAIL: Rangnick rejected Bayern in 2024, not 2022
- All key Rangnick's rejection of Bayern Munich to **2022** (in the answer and/or explanation). He was *appointed* Austria manager in 2022, but he **turned down Bayern in 2024**. Rows whose answer is literally "In 2022" (3505, 3518, 3519) have a wrong answer; the rest carry the wrong year in the explanation.
**Source:** https://en.wikipedia.org/wiki/Ralf_Rangnick
**Remedy:** Separate the 2022 appointment from the 2024 Bayern rejection; key the rejection to 2024.

### Row 3557 — FAIL: Rangnick was not in charge for 2022 WC qualifying
- "introduced a pressing style **for 2022 World Cup qualifying** → Rangnick" — the 2022 WC qualifiers were run by **Franco Foda**; Rangnick was appointed only after that campaign ended.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Tie Rangnick's pressing to the 2026 cycle / Euro 2024, not the 2022 qualifiers.

### Rows 3545, 3623, 3625, 3638, 3644 — FAIL: Arnautović became all-time top scorer in 2025
- These claim Marko Arnautović was/became Austria's **all-time top scorer "by/before the 2022 World Cup"** (3545, 3623, 3625, 3644) or **"at the 2024 Euros"** (3638). He overtook Toni Polster's record only in **2025**. (3644 additionally has a false premise — Austria did not play the 2022 World Cup.)
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Drop the "by 2022 / at 2024" time-bounding, or use present-tense "is the all-time top scorer".

### Rows 3615, 3622, 3629, 3635, 3636 — FAIL: wrong/non-unique player-club facts
- **3615:** "midfielder who played for **Borussia Dortmund at the 2022 World Cup** → Sabitzer" — Sabitzer was at **Bayern** then (he joined Dortmund in 2023), and Austria did not play the 2022 WC.
- **3622, 3635:** "player **NOT based in the Bundesliga** → Alaba" — not unique: **Arnautović** (Bologna, Serie A) was also non-Bundesliga in that period.
- **3629:** "had **over 100 caps** for the 2022 WC qualifiers → Alaba" — not unique (**Arnautović** also has 100+ caps) and neither had reached 100 caps yet in 2021.
- **3636:** "player **based in the Bundesliga** → Baumgartner" — not unique: **Schlager** (Wolfsburg) and **Schöpf** (Arminia Bielefeld) were also Bundesliga-based.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Pick a discriminator that singles out exactly one player, and fix the club/era facts.

### Rows 3654, 3655, 3656, 3657 — FAIL: false premise — Austria did not play the 2022 World Cup
- These frame David Alaba's injury around the **2022 World Cup** itself ("ahead of / availability for / hopes for the 2022 FIFA World Cup"). Austria failed to qualify for the 2022 World Cup, so a finals-participation framing is a false premise.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Reframe to the **2022 World Cup qualifiers** (which Austria did contest) rather than the finals.

---

## Austria batch rows 3661-3860 — 23 FAIL

### Rows 3719, 3747, 3773 — FAIL: wrong manager name "Franz Koller"
- All key the answer to **"Franz Koller"** for Austria's peak FIFA ranking (10th). The manager was **Marcel Koller**; "Franz Koller" is not a real Austria manager. (In 3747 the correct name is not even an option.)
**Source:** https://en.wikipedia.org/wiki/Marcel_Koller
**Remedy:** Correct the name to Marcel Koller.

### Row 3785 — FAIL: Rangnick rejected Bayern in 2024, not 2022
- "rejected Bayern Munich before 2026 WC qualifiers → Rangnick" but the explanation dates the rejection to **2022**; he was *appointed* in 2022 and **turned down Bayern in 2024**.
**Source:** https://en.wikipedia.org/wiki/Ralf_Rangnick
**Remedy:** Key the Bayern rejection to 2024.

### Rows 3742, 3858 — FAIL: Arnautović became all-time top scorer in 2025
- **3742:** "holds the all-time scoring record **entering the 2022 WC qualifiers**" and **3858:** "became their all-time top scorer **before the 2022 World Cup**". Arnautović overtook Toni Polster's record only on **9 Oct 2025** (45 goals); Polster held it through 2021.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Drop the pre-2022 time-bounding, or use present tense.

### Rows 3661, 3679, 3682, 3683, 3720, 3839, 3843 — FAIL: false premise — Austria did not play the 2022 World Cup
- These frame players around the **2022 World Cup finals / squad / availability** (3661 Alaba's "2022 World Cup availability"; 3679/3682/3683 Baumgartner "at/in the 2022 World Cup squad"; 3720 "defender at the 2022 World Cup"; 3839/3843 Sabitzer "2022 World Cup squad"). Austria **failed to qualify** for the 2022 World Cup, so a finals/squad framing is a false premise.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Reframe to the 2022 World Cup **qualifiers**, which Austria contested.

### Rows 3672, 3673, 3857, 3859 — FAIL: non-unique "not based in the Bundesliga"
- All key "not based in the Bundesliga → David Alaba" (Real Madrid), but **Marko Arnautović** (Bologna in 2021, Inter Milan by 2024 — both Serie A) was also not Bundesliga-based, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Replace Arnautović as a distractor, or add a discriminator unique to Alaba.

### Row 3826 — FAIL: Sabitzer was at Bayern, not Dortmund, during the 2022 cycle
- "played for Borussia Dortmund **during the 2022 World Cup cycle** → Sabitzer" — he was at **Bayern Munich** then; he only joined Borussia Dortmund in 2023.
**Source:** https://en.wikipedia.org/wiki/Marcel_Sabitzer
**Remedy:** Tie the Dortmund spell to 2023 onward (e.g. the 2026 cycle), not 2022.

### Rows 3732, 3734 — FAIL: non-unique tournament/opponent answer
- **3732:** "Euro 2024 group opponent that **also played at the 2022 World Cup** → Netherlands" — Austria's Euro 2024 group also contained **France and Poland**, both of which also played the 2022 World Cup (3 of 4 options qualify).
- **3734:** "Euro 2024 opponent they **defeated** → Netherlands" — Austria also **beat Poland 3-1** at Euro 2024, so two offered options are correct.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024
**Remedy:** Rewrite so exactly one option satisfies the condition.

### Rows 3675, 3807 — FAIL: internal temporal contradiction
- **3675:** "2024 achievement that **followed their 2026 World Cup qualification** → beat Netherlands 3-2" — the win was June 2024, *before* qualification was secured (Nov 2025), so it could not have followed it.
- **3807:** "manager whose tenure **ended before the 2022 World Cup qualifiers** → Foda" — Foda *oversaw* the 2022 qualifiers (2018-2022); even the explanation says his tenure ended "during" that cycle, contradicting the stem.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Fix the ordering so the stem matches the timeline.

### Row 3751 — FAIL: false premise — Austria did not face Germany in 2022 WC qualifying
- "manager who **faced Germany in a 2022 World Cup qualifier** → Foda" — Austria and Germany were in **different qualifying groups**; they did not meet in 2022 WC qualifying.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Use a genuine 2022-qualifying opponent (e.g. Denmark, Scotland, Israel).

---

## Austria batch rows 3861-4060 — 21 FAIL

### Rows 3862 — FAIL: Alaba did not have 100+ caps before the 2022 World Cup
- "had over 100 caps **before the 2022 World Cup** → David Alaba". Alaba reached his 100th cap only on **17 June 2023** (vs Belgium, Euro 2024 qualifying), so he was below 100 caps before the 2022 WC.
**Source:** https://en.wikipedia.org/wiki/David_Alaba
**Remedy:** Use present tense ("has over 100 caps"), or anchor to Arnautović (100 caps from 6 June 2022).

### Rows 3867 — FAIL: non-unique "based in the Bundesliga"
- "player in the 2022 WC qualifiers **based in the Bundesliga** → Baumgartner (Hoffenheim)" — not unique: **Marcel Sabitzer** (Bayern Munich from Aug 2021) was also Bundesliga-based during that campaign.
**Source:** https://en.wikipedia.org/wiki/Marcel_Sabitzer
**Remedy:** Add a discriminator unique to Baumgartner, or replace Sabitzer as a distractor.

### Rows 3868, 3941 — FAIL: false premise — "2022 World Cup squad/player"
- **3868:** "Austrian player **in the 2022 World Cup squad** who won the CL with two clubs → Alaba"; **3941:** "Austrian **World Cup 2022 player** who won the CL with Bayern and Real → Alaba". Austria **failed to qualify** for the 2022 World Cup, so a finals-squad/player framing is a false premise.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Drop the "2022 World Cup squad/player" framing (use "2022 WC qualifiers" or no year).

### Rows 3875, 3878 — FAIL: Arnautović became all-time top scorer in 2025
- **3875:** "all-time top scorer **at the 2022 World Cup** → Arnautović" (also a false premise — Austria did not play it); **3878:** "all-time top scorer, **a status he held during the 2022 World Cup qualifiers**". Arnautović overtook Toni Polster's record only on **9 Oct 2025** (45 goals); Polster held it through 2021-22.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Use present tense ("is the all-time top scorer"); drop the 2022 time-bounding.

### Rows 3881, 3902 — FAIL: Arnautović has never scored a World Cup goal
- **3881:** "**scored a World Cup goal** and is the nation's all-time top scorer → Arnautović"; **3902:** "**World Cup goal tally** made him their all-time leading scorer → Arnautović". Arnautović has **never played at a World Cup** (Austria last appeared in 1998); his goals come from qualifiers, friendlies and the Euros.
**Source:** https://en.wikipedia.org/wiki/Marko_Arnautovi%C4%87
**Remedy:** Remove the "World Cup goal" claim; his record is from international goals overall.

### Row 3908 — FAIL: Ernst-Happel-Stadion / Vienna was not a Euro 2020 host
- "Austrian stadium, **a 2020 Euro host** → Ernst-Happel-Stadion". Euro 2020's host cities were London, Munich, Rome, Baku, Saint Petersburg, Amsterdam, Bucharest, Budapest, Copenhagen, Glasgow and Seville — **Vienna was not among them**.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Anchor the stadium to Euro 2008 (which Vienna did host) or to its capacity, not Euro 2020.

### Rows 3914, 3918, 3920, 3927 — FAIL: false premise — Alaba injury framed around the 2022 World Cup finals
- These tie David Alaba's injury to the **2022 World Cup** itself: 3914 "injured **before the 2022 FIFA World Cup**", 3918 "**2022 World Cup preparation**", 3920 "**2022 World Cup hopes**", 3927 "**2022 FIFA World Cup squad availability**". Austria did not qualify for the 2022 finals, so a finals/squad-preparation framing is a false premise.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Reframe to the **2022 World Cup qualifiers** (which Austria contested).

### Row 3944 — FAIL: Austria Wien IS a main Austrian Bundesliga club
- "Which club is **NOT** a main Austrian Bundesliga team? → Austria Wien". **FK Austria Wien** is one of Austria's biggest top-flight clubs (24-time champions) and plays in the Austrian Bundesliga, so it is not the odd one out.
**Source:** https://en.wikipedia.org/wiki/FK_Austria_Wien
**Remedy:** Replace the answer with a club that is genuinely not in the Austrian Bundesliga.

### Rows 3945, 4026 — FAIL: Rangnick rejected Bayern in 2024, not 2022
- Both tie Rangnick's rejection of Bayern Munich to **2022** ("reject to remain Austria manager **in 2022**" / "turned down Bayern to coach Austria **in 2022**"). He was *appointed* Austria manager in 2022 but **turned down Bayern in 2024**.
**Source:** https://en.wikipedia.org/wiki/Ralf_Rangnick
**Remedy:** Separate the 2022 appointment from the 2024 Bayern rejection; key the rejection to 2024.

### Row 3950 — FAIL: the Netherlands win was a group game, and Austria's only knockout match was a loss
- "Euro 2024 **only knockout win** → Beat Netherlands 3-2". The 3-2 win over the Netherlands was the final **group-stage** match; Austria's only knockout game at Euro 2024 was the **R16 loss (2-1) to Türkiye** — they had no knockout win.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024
**Remedy:** Reframe as a group-stage result, or remove the false "knockout win" claim.

### Rows 3955, 3960 — FAIL: non-unique answer
- **3955:** "Which Euros did Austria reach the **group stage** in? → Euro 2016" — Austria reached the group stage at **Euro 2008, 2016, 2020 and 2024** (all four offered), so not unique.
- **3960:** "manager who did **NOT** lead Austria to World Cup qualification → Koller" — **Foda** (failed 2022) and **Constantini** also never led a WC qualification, so three options qualify.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Rewrite so exactly one option satisfies the condition (e.g. "first" / "only").

### Rows 3969, 4027 — FAIL: Rangnick was not in charge of the 2022 World Cup cycle
- **3969:** "implemented a pressing style **for Austria in 2022 World Cup qualifying** → Rangnick"; **4027:** "appointed to lead Austria **in the 2022 World Cup cycle** → Rangnick". The 2022 WC qualifiers were run by **Franco Foda** (ended Nov 2021); Rangnick was appointed only afterwards for the Euro 2024 / 2026 cycle, so keying the 2022 WC campaign to him is wrong (Foda is the correct manager for that cycle).
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Tie Rangnick to the 2026 cycle / Euro 2024, not the 2022 World Cup campaign.

---

## Austria batch rows 4061-4282 — 11 FAIL

### Rows 4105, 4204 — FAIL: self-referential answer
- **4105:** "Which nation, **like Austria** under Koller, also reached its best FIFA ranking of 10th? → **Austria**"; **4204:** "Which UEFA nation, **like Austria**, failed to qualify for the 2010/2014/2018/2022 World Cups? → **Austria**". The stem asks for a nation *comparable to* Austria, but the keyed answer is Austria itself — circular and unanswerable as posed.
**Source:** https://en.wikipedia.org/wiki/Austria_national_football_team
**Remedy:** Either name a genuine peer nation as the answer, or drop the "like Austria" framing and ask about Austria directly.

### Rows 4140 — FAIL: the Netherlands win was a group game, not a knockout win
- "Which team did Austria beat in the Euro 2024 **knockout stage**? → Netherlands" — the 3-2 win over the Netherlands was a **group-stage** match. Austria's only knockout game at Euro 2024 was the R16 **loss** to Türkiye, so they beat no one in the knockout stage. (The explanation also wrongly says Austria lost to Italy — they did not face Italy at Euro 2024.)
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024
**Remedy:** Reframe as a group-stage result, or remove the false "knockout" premise.

### Rows 4147, 4148, 4241 — FAIL: non-unique answer
- **4147:** "team Austria did **NOT** beat at Euro 2024 → Türkiye" — Austria also **lost 0-1 to France** (and beat only the Netherlands and Poland), so France is equally a correct answer.
- **4148:** "team Austria did **NOT** beat in a group-stage upset → Italy" — their only group-stage upset was over the Netherlands, so Germany and France (also offered) are equally "not beaten."
- **4241:** "year Austria qualified for the Euro **group stage** → 2016" — Austria reached the group stage at **2008, 2016 and 2020** (all offered), so not unique.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024
**Remedy:** Rewrite so exactly one option satisfies the condition.

### Rows 4203 — FAIL: false premise (Austria's first Euros was 2008) and non-unique
- "Which UEFA nation, **like Austria at Euro 2016, also qualified for their first Euros in 2016**? → Iceland". Austria's **first** Euros was **2008** (as co-host), not 2016 — so the comparison is false. Moreover Iceland, **Wales, Slovakia and Northern Ireland** (all offered) all made their Euro debut in 2016, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2016
**Remedy:** Drop the false Austria comparison and ensure only one option debuted in 2016.

### Rows 4233, 4238, 4240 — FAIL: Austria qualified in 2025, not 2026
- All ask **which year** Austria qualified and key **2026** ("end their 28-year absence by qualifying", "qualify for the 2026 World Cup under Rangnick", "qualify after a 28-year absence"). Qualification was secured on **18 Nov 2025**; 2026 is the tournament year, and the correct year (2025) is not even offered.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Key the qualification year as 2025, or reword to "for which World Cup did Austria qualify".

### Rows 4276 — FAIL: answer is a consequence, not a reason
- "**Why** did Austria qualify for the 2026 FIFA World Cup? → Ended a 28-year absence". Ending the absence is a *result* of qualifying, not its cause. Austria qualified by **winning their qualifying group** — an option offered ("Won their qualifying group"), which is the correct causal answer.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Key the answer to "Won their qualifying group", or reword the stem to ask about significance rather than cause.

---

## Cabo Verde batch rows 8183–8530 — 16 FAIL

### Rows 8191, 8368, 8404, 8405 — FAIL: wrong AFCON 2023 stage (it was the quarter-finals)
- All key the 2023 AFCON exit as the **round of 16**. Cabo Verde actually **won** their round-of-16 tie (1-0 v Mauritania) and were eliminated by **South Africa in the quarter-finals** (0-0, lost 2-1 on penalties). **8191** ("reached which knockout stage → Round of 16") and **8368** ("eliminated in which round → round of 16") have a wrong answer; **8404/8405** ("which 2023 AFCON round did they lose to South Africa → round of 16") are wrong — that loss was the quarter-final.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations
**Remedy:** Key the stage as the quarter-finals.

### Rows 8222, 8223, 8366, 8367, 8450, 8459 — FAIL: false premise / wrong explanation ("lost to South Africa in the 2023 round of 16")
- **8222/8223** build the stem on "Cabo Verde lost to South Africa in the 2023 AFCON **round of 16**" — false (it was the quarter-final). **8222** also keys "tournament ended → 2023" although the 2023 edition was played Jan–Feb **2024**. **8366/8367** ask who beat/eliminated them "in the 2023 AFCON round of 16 → South Africa" — South Africa beat them in the QF, not the R16. **8450/8459** have correct answers (2023) but explanations that state they "lost to South Africa in the round of 16," which is false.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations
**Remedy:** Drop/replace the round-of-16 premise with the quarter-final; for 8222 reconcile the 2023 vs 2024 dating.

### Rows 8237, 8250 — FAIL: self-referential answer
- **8237:** "Cabo Verde secured its first World Cup… **which nation also qualified?** → Cabo Verde"; **8250:** "Cabo Verde's 2026 qualification was historic. **Which nation also qualified for its first World Cup?** → Cabo Verde." The stem asks for another nation, but the keyed answer is Cabo Verde itself — circular. (8237 is also non-unique on the looser reading, since Egypt and Senegal also qualified for 2026.)
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Name a genuine other first-time 2026 qualifier (e.g. Jordan or Uzbekistan), or reframe to ask about Cabo Verde directly.

### Rows 8245, 8246, 8289 — FAIL: false premise ("2022 World Cup squad")
- All reference Cabo Verde's "**2022 World Cup squad**." Cabo Verde did **not** qualify for the 2022 World Cup, so there was no 2022 World Cup (finals) squad. The underlying diaspora fact (many Portugal-based players) is true, but the premise is false.
**Source:** https://en.wikipedia.org/wiki/Cape_Verde_national_football_team
**Remedy:** Reframe as the "2022 World Cup **qualifying** squad" or drop the tournament reference.

### Row 8402 — FAIL: false geographic premise (Angola is not a West African rival)
- "In which 2013 AFCON match did Cabo Verde face a **West African rival**? → Group stage vs Angola." Angola is a **Central/Southern** African nation, not West African, and the explanation asserts a "verified West African rivalry fixture," which is false.
**Source:** https://en.wikipedia.org/wiki/2013_Africa_Cup_of_Nations
**Remedy:** Remove the "West African" descriptor, or pick a genuine West African opponent.

---

## Cabo Verde batch rows 8531–8880 — 11 FAIL

### Rows 8536, 8689 — FAIL: wrong AFCON 2023 stage (reached the quarter-finals)
- **8536** ("lost to South Africa in the 2023 knockout stage → Round of 16") and **8689** ("which AFCON 2023 stage did Cabo Verde reach → Round of 16") are wrong. Cabo Verde **won** their 2023 round-of-16 tie and were eliminated by **South Africa in the quarter-finals** (0-0, 2-1 on penalties), the furthest stage they reached. Quarter-finals is an offered option in both.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations
**Remedy:** Key the stage as the quarter-finals.

### Rows 8535, 8618, 8870 — FAIL: false premise / wrong explanation ("lost to South Africa in the 2023 round of 16")
- **8535** keys the correct year (2023) but its explanation says they "lost to South Africa in the 2023 AFCON round of 16" — false (that loss was the quarter-final). **8618** ("which 2023 round-of-16 opponent did Cabo Verde lose to → South Africa") and **8870** ("which opponent eliminated them in the 2023 round of 16 → South Africa") both rest on the false premise that South Africa beat them in the round of 16.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations
**Remedy:** Replace "round of 16" with "quarter-finals."

### Rows 8667, 8719 — FAIL: self-referential answer
- **8667:** "Which 2026 World Cup qualifier is Cabo Verde's greatest sporting achievement? → Cabo Verde"; **8719:** "Which African nation's World Cup qualifying rise mirrors Cabo Verde's? → Cabo Verde" (its explanation even states "the question asks which nation mirrors itself"). Both key the subject nation as the answer — circular.
**Source:** https://en.wikipedia.org/wiki/Cape_Verde_national_football_team
**Remedy:** Name a genuine comparator nation, or reframe to ask about Cabo Verde directly.

### Row 8620 — FAIL: non-unique / wrong answer (multiple players raised in Portugal)
- "Which 2026 Cabo Verde World Cup player was raised in Portugal? → Ryan Mendes." The squad is built on the Portugal-raised diaspora, and option **Bebé** (Tiago Correia) was unambiguously born and raised in Portugal — so the condition is not unique to Ryan Mendes (himself Praia-born).
**Source:** https://en.wikipedia.org/wiki/Cape_Verde_national_football_team
**Remedy:** Reword so exactly one option fits, or name a player uniquely tied to Portugal.

### Row 8740 — FAIL: unverified captaincy + ambiguous position
- "Which Cabo Verde **centre-back captained** the team during 2022 World Cup qualifying? → Stopira." Stopira's primary position is **left-back**, and option **Varela** (Fernando Varela) is the squad's recognised centre-back, making "centre-back" non-unique; the specific captaincy claim is unverified.
**Source:** https://en.wikipedia.org/wiki/Fernando_Varela_(Cape_Verdean_footballer)
**Remedy:** Drop the "centre-back" qualifier and confirm/replace the captaincy claim.

### Row 8865 — FAIL: wrong club (Kenny Rocha Santos never played for Moreirense)
- "Which Cabo Verde midfielder … played for Moreirense in Europe? → Kenny Rocha Santos." Rocha Santos's European career is in **France** (Saint-Étienne, Rouen) and **Cyprus** (AEZ Zakakiou); there is no Moreirense spell.
**Source:** https://en.wikipedia.org/wiki/Kenny_Rocha_Santos
**Remedy:** Remove the Moreirense reference, or name the club he actually played for.

### Row 8875 — FAIL: wrong diaspora (Jamiro Monteiro is Dutch-born)
- "Which Cabo Verde player qualified … through Portuguese diaspora? → Jamiro Monteiro." Monteiro was born and raised in the **Netherlands**, so he qualifies via the Dutch diaspora, not the Portuguese one; the explanation's "especially from Portugal" is wrong for him.
**Source:** https://en.wikipedia.org/wiki/Jamiro_Monteiro
**Remedy:** Pick a genuinely Portugal-raised player, or correct the diaspora.

---

## Cabo Verde batch rows 8881–9230 — 26 FAIL

### Rows 8886, 8902, 9003, 9004, 9005, 9006, 9024, 9146, 9163, 9169, 9173, 9179, 9181, 9184, 9210, 9220 — FAIL: self-referential answer (names the subject nation itself)
- Each of these asks which *other* nation/team matches, mirrors, or shares a trait with Cabo Verde, but keys **"Cabo Verde"** as the answer — the subject restated. Examples: **9003/9004/9005/9006** ("which CAF nation's ranking rise mirrors Cabo Verde's → Cabo Verde"); **9024** ("which CAF nation's stadium capacity is closest to Cabo Verde's → Cabo Verde"); **9146** ("which nation matched Cabo Verde's 2014 peak of 27th → Cabo Verde"); **9169/9173/9179/9181/9184/9210/9220** ("which nation, like Cabo Verde, … → Cabo Verde"); **8886/8902** likewise key the subject team. Several explanations even admit it ("the question asks which nation's trajectory mirrors its own"). **9163** additionally rests on a false premise — Cabo Verde did **not** qualify for the 2015 AFCON (their AFCON appearances are 2013, 2021, 2023).
**Source:** https://en.wikipedia.org/wiki/Cape_Verde_national_football_team
**Remedy:** Name a genuine comparator nation (e.g. Iceland for the "tiny debutant" framing), or reframe to ask about Cabo Verde directly.

### Rows 8881, 8942, 9087, 9096 — FAIL: non-unique answer
- **8881** ("which Cabo Verde player, eligible via Portuguese diaspora, played at AFCON tournaments → Garry Rodrigues"): the condition fits **all four** options — Ryan Mendes, Kenny Rocha Santos and Stopira all featured at AFCON via the same diaspora, so the answer is not unique.
- **8942** ("which Cabo Verdean team qualified for the 2026 World Cup → The national team"): the distractors **"Cape Verde," "Cabo Verde," "Cape Verde Islands"** are the same nation, so multiple options are equally correct.
- **9087** ("which manager did **NOT** lead Cabo Verde during early 2026 qualification → Lucio Antunes"): a negative question where **Hervé Renard and Carlos Queiroz** also never led Cabo Verde — only Bubista did — so three options satisfy "did not lead."
- **9096** ("which manager led Cabo Verde during their 2023 AFCON campaign → Bubista"): option **"Pedro Brito"** is the same man — *Bubista* is the nickname of **Pedro Leitão Brito** — so two options name the correct manager.
**Source:** https://en.wikipedia.org/wiki/Cape_Verde_national_football_team
**Remedy:** Reword so exactly one option is correct (distinct managers, distinct players, a single spelling of the nation).

### Row 9048 — FAIL: wrong answer (World Cup squad is Europe-based, not the domestic league)
- "Which domestic league do most Cabo Verde World Cup squad players compete in? → Campeonato Caboverdiano de Futebol." Cabo Verde's 2026 squad is built almost entirely on the Portugal-based diaspora and other European leagues; very few (if any) of the World Cup squad play in the domestic **Campeonato Caboverdiano**. Option **Liga Portugal** is the realistic answer.
**Source:** https://en.wikipedia.org/wiki/Cape_Verde_national_football_team
**Remedy:** Change the answer to the Portuguese top flight, or reword to ask which league is Cabo Verde's *top domestic* competition (then the Campeonato answer is fine).

### Rows 9127, 9129 — FAIL: wrong explanation (2023 AFCON exit was the quarter-final, not the round of 16)
- **9127** ("which nation did Cabo Verde face in a 2023 AFCON knockout round → South Africa") and **9129** ("which nation eliminated Cabo Verde from the 2023 AFCON → South Africa"): the keyed answer South Africa is correct, but both explanations say the loss came in the **round of 16**. Cabo Verde won their round-of-16 tie and were eliminated by South Africa in the **quarter-finals** (0-0, 2-1 on penalties).
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations
**Remedy:** Replace "round of 16" with "quarter-finals" in the explanation.

### Row 9131 — FAIL: false premise (no round-of-16 loss to South Africa)
- "Which nation eliminated Cabo Verde in the 2023 Africa Cup of Nations **round of 16**? → South Africa." The premise is false: South Africa beat Cabo Verde in the **quarter-finals**, not the round of 16.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations
**Remedy:** Change "round of 16" to "quarter-finals."

### Rows 9206, 9219 — FAIL: false premise (Iceland's debut was 2018, not 2026)
- **9206** ("which nation's **2026** World Cup qualification is compared to Cabo Verde's → Iceland") and **9219** ("which nation's **2026** World Cup qualification was compared to Cabo Verde's historic first → Iceland"): Iceland did **not** qualify for 2026; the valid comparison is to Iceland's **2018** debut (the explanations themselves say 2018). The "2026" framing of Iceland's qualification is false.
**Source:** https://en.wikipedia.org/wiki/Iceland_national_football_team
**Remedy:** Drop "2026" from the Iceland framing — compare Cabo Verde's 2026 debut to Iceland's 2018 debut.

---

## Cabo Verde batch rows 9231–9573 — 20 FAIL

### Rows 9286, 9287 — FAIL: wrong answer (2023 AFCON best stage was the quarter-finals)
- Both ask which round Cabo Verde **reached** at the 2023 AFCON and key **"Round of 16."** Cabo Verde won their round-of-16 tie and reached the **quarter-finals** (lost to South Africa 0-0, 2-1 on penalties) — and "Quarter-finals" is an offered option in both.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations
**Remedy:** Change the answer to the quarter-finals.

### Rows 9344, 9388, 9423 — FAIL: false premise (no round-of-16 loss to South Africa)
- **9344** ("which team beat Cabo Verde in the 2023 AFCON **round of 16** → South Africa"), **9388** ("which West African nation did Cabo Verde lose to in the 2023 AFCON **round of 16** → South Africa") and **9423** ("who eliminated Cabo Verde in the 2023 AFCON **round of 16** → South Africa") all embed the false premise that South Africa beat Cabo Verde in the round of 16 — that loss came in the **quarter-finals**. (9388 also mislabels South Africa, a Southern-African side, as "West African.")
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations
**Remedy:** Replace "round of 16" with "quarter-finals."

### Rows 9353, 9356, 9411, 9454 — FAIL: wrong explanation (states "round of 16" for the quarter-final exit)
- The keyed answers are right — South Africa (9353, 9356), the year 2023 (9411), "lost in knockout stage" (9454) — but each explanation says Cabo Verde lost in the **round of 16**. Their 2023 AFCON elimination by South Africa was in the **quarter-finals**.
**Source:** https://en.wikipedia.org/wiki/2023_Africa_Cup_of_Nations
**Remedy:** Correct the explanation to "quarter-finals."

### Row 9341 — FAIL: false premise (Cabo Verde did not play the 2015 AFCON)
- "Which stage did Cabo Verde reach at the **2015** Africa Cup of Nations? → Group stage." Cabo Verde failed to qualify for the 2015 AFCON; their AFCON appearances are 2013, 2021 and 2023. The premise is false.
**Source:** https://en.wikipedia.org/wiki/Cape_Verde_national_football_team
**Remedy:** Re-anchor to a tournament Cabo Verde actually contested (2013, 2021 or 2023).

### Row 9375 — FAIL: wrong answer (squad is Europe-based, not the domestic league)
- "Which top domestic league do Cabo Verde's 2022 World Cup squad players compete in? → Campeonato Caboverdiano de Futebol." Cabo Verde's squad is built on the Portugal-based diaspora and other European leagues; option **Liga Portugal** is the realistic answer. (Same defect as row 9048 in the previous batch.)
**Source:** https://en.wikipedia.org/wiki/Cape_Verde_national_football_team
**Remedy:** Change the answer to the Portuguese top flight, or reword to ask which league is Cabo Verde's *top domestic* competition.

### Rows 9263, 9305 — FAIL: self-referential answer (names the subject nation)
- **9263** ("which nation's most popular sport is football, like Cabo Verde's → Cabo Verde") and **9305** ("which small nation qualified for its first World Cup in 2026 like Cabo Verde → Cabo Verde") both ask which *other* nation is "like Cabo Verde" yet key Cabo Verde itself.
**Source:** https://en.wikipedia.org/wiki/Cape_Verde_national_football_team
**Remedy:** Name a genuine comparator nation (e.g. Iceland), or reframe to ask about Cabo Verde directly.

### Row 9320 — FAIL: false premise (Iceland's debut was 2018, not 2026)
- "Which small nation's **2026** World Cup qualification is compared to Cabo Verde's? → Iceland." Iceland did not qualify for 2026; the valid comparison is to Iceland's **2018** debut (the explanation itself says 2018).
**Source:** https://en.wikipedia.org/wiki/Iceland_national_football_team
**Remedy:** Drop "2026" from the Iceland framing — compare Cabo Verde's 2026 debut to Iceland's 2018 debut.

### Rows 9453, 9462, 9475, 9559 — FAIL: false premise (Cabo Verde never qualified for the 2018 or 2022 World Cup)
- **9453** ("why did Cabo Verde **join Iceland as a 2018 World Cup qualifier** → tiny population"), **9462** ("why did Cabo Verde **qualify for the 2022 World Cup** as a tiny nation"), **9475** ("why did Cabo Verde's **2022 qualification** join Iceland as a World Cup feat") and **9559** ("why was Cabo Verde's **2022 World Cup qualification** so remarkable") all assert a 2018 or 2022 *qualification*. Cabo Verde's first-ever World Cup qualification is **2026** — they reached no earlier finals. (9453's explanation also wrongly gives Iceland a ~500,000 population; it is ~370,000. 9462 additionally ships an empty explanation.)
**Source:** https://en.wikipedia.org/wiki/Cape_Verde_national_football_team
**Remedy:** Re-anchor to the 2026 qualification, or reframe as the 2022 *qualifying campaign* (which they contested but did not win).

### Rows 9280, 9389 — FAIL: non-unique answer
- **9280** ("which of these nations has a larger population than Cabo Verde? → Uruguay"): Cabo Verde's population (~525,000) is also smaller than **Trinidad and Tobago** (~1.5M) and **Slovenia** (~2.1M), so three of the four options are larger — not unique. (Only Iceland is smaller.)
- **9389** ("which West African nation did Cabo Verde **NOT** face in a 2013 or 2023 AFCON match? → Nigeria"): Cabo Verde also did not face **Senegal** in either tournament, so two options satisfy "not faced." (Cabo Verde played Angola in 2013 and South Africa in 2023.)
**Source:** https://en.wikipedia.org/wiki/Cape_Verde_national_football_team
**Remedy:** Reword so exactly one option fits.

---

## Canada batch rows 10746–11085 — 17 FAIL

### Rows 10753, 10755, 10756, 10757, 10758, 10815, 10839, 10843, 10846, 11028, 11067 — FAIL: stale superlative ("highest/peak FIFA ranking = 33rd")
- Each keys Canada's **highest / peak / best** FIFA ranking as **33rd** (or asks the year of that peak → 2022). Canada did reach 33rd in **February 2022**, but that is no longer their high-water mark: they climbed to **31st (Dec 2024)** and peaked at **26th (September 2025)**. So "33rd = highest-ever" and "highest ranking after 2022 qualification = 33rd / reached in 2022" are now false. (Year-bounded variants like "highest ranking *in 2022* → 33rd" remain correct and PASS.)
**Source:** https://en.wikipedia.org/wiki/Canada_men%27s_national_soccer_team
**Remedy:** Re-anchor to "33rd in 2022" without the all-time superlative, or update the peak to 26th (2025).

### Rows 11071, 11072, 11079 — FAIL: Excel date-mangled scoreline
- The keyed answers are spreadsheet-corrupted dates: **11071 "04-Jan"** = the 4-1 loss to Croatia; **11072 / 11079 "02-Jan"** = the 2-1 loss to Morocco. The scoreline was mangled into a date by Excel.
**Source:** https://en.wikipedia.org/wiki/Canada_men%27s_national_soccer_team
**Remedy:** Restore the scorelines ("4-1", "2-1").

### Row 10747 — FAIL: internal temporal contradiction + false premise
- "After Canada's **2020 Olympic gold**, which World Cup did they co-host? → **2015 Women's World Cup**." The answer (2015) predates the stem's anchor event (2020), and the explanation even says "before their gold medal win" — a self-contradiction. (The 2020 Olympic gold was the **women's** team; this is a men's-team item.)
**Source:** https://en.wikipedia.org/wiki/Canada_women%27s_national_soccer_team
**Remedy:** Drop the "after 2020 gold" framing; ask plainly which Women's World Cup Canada co-hosted (2015).

### Row 10805 — FAIL: false premise (2-0 is not a "three-goal margin")
- "Canada lost 2-0 to Argentina in the 2024 Copa semi-final. Which 2022 group opponent **also** beat them by a **three-goal margin**? → Croatia." Croatia (4-1) was indeed a three-goal margin, but Argentina's 2-0 is a **two-goal** margin, so the "also … three-goal" premise (and the explanation "matching Argentina's 2-0 win") is false.
**Source:** https://en.wikipedia.org/wiki/Canada_men%27s_national_soccer_team
**Remedy:** Drop the false equivalence; ask which 2022 opponent beat Canada by three goals (Croatia).

### Row 10995 — FAIL: misleading premise (BMO Field did not host 2022 World Cup matches)
- "In which two World Cup years will Canada's BMO Field host matches? → **2022 and 2026**." BMO Field hosted a 2022 **qualifier** (the Jamaica clincher), not 2022 World Cup matches — the 2022 finals were in Qatar. BMO Field hosts World Cup matches only in **2026**.
**Source:** https://en.wikipedia.org/wiki/Canada_men%27s_national_soccer_team
**Remedy:** Reword to distinguish the 2022 qualifier from 2026 finals, or key 2026 only.

## Canada batch rows 11086–11425 — 11 FAIL

### Rows 11090, 11184, 11186 — FAIL: wrong Marsch appointment year (2024, not 2023)
- Each keys Jesse Marsch's appointment as Canada manager to **2023**. Marsch was actually appointed in **May 2024** (the first American to coach Canada, for the 2026 cycle). John Herdman left for Toronto FC in 2023, after which Canada ran an interim before hiring Marsch in 2024.
**Source:** https://en.wikipedia.org/wiki/Canada_men%27s_national_soccer_team
**Remedy:** Correct the appointment year to 2024.

### Rows 11089, 11125, 11126, 11128, 11134 — FAIL: stale superlative ("highest/peak FIFA ranking = 33rd")
- Same defect as the batch-1 ranking cluster: these key Canada's **highest / peak / best-ever** FIFA ranking as **33rd**, or ask the year of that peak. 33rd was their February 2022 mark only; they later climbed to **31st (Dec 2024)** and peaked at **26th (Sept 2025)**. Year-bounded "in 2022 → 33rd" variants remain correct and PASS.
**Source:** https://en.wikipedia.org/wiki/Canada_men%27s_national_soccer_team
**Remedy:** Drop the all-time superlative or update the peak to 26th (2025).

### Rows 11154, 11402, 11409 — FAIL: "Jonathan David 25+ goals by/in 2022" premature
- Each credits **Jonathan David** with **25+ international goals by (or in) 2022**. David did not reach 25 international goals until **2023**; at the 2022 World Cup his tally was lower. (Present-tense "David is Canada's top scorer" and "by 2023" variants PASS; Cyle Larin "25+ by 2022" also PASS, as he was the record scorer at ~25 by then.)
**Source:** https://en.wikipedia.org/wiki/Canada_men%27s_national_soccer_team
**Remedy:** Re-anchor David's 25-goal milestone to 2023, or attribute the 2022 record to Larin.

## Canada batch rows 11426–11765 — 5 FAIL

### Rows 11663, 11664, 11710 — FAIL: false premise (Ismael Koné debuted in 2022, not after)
- Each claims **Ismael Koné** debuted **for the 2026 cycle / 2026 squad** or **after the 2022 World Cup**: 11663 ("debuted for the 2026 cycle, **not** the 2022 World Cup"), 11664 ("debuted for the 2026 FIFA World Cup squad"), 11710 ("debuted for the national team **after** the 2022 World Cup"). Koné actually debuted in **January 2022** and **played all three group games at the 2022 World Cup** — a fact the same dataset confirms elsewhere (rows 11500 and 11682 in this very pool place Koné in the 2022 squad). Calling him a "2026 prospect" is fine; claiming his debut post-dates 2022 is false.
**Source:** https://en.wikipedia.org/wiki/Canada_men%27s_national_soccer_team
**Remedy:** Reword to "emerging/next-generation" without asserting a post-2022 debut.

### Row 11711 — FAIL: non-unique answer
- "Which Canadian player did **NOT** have 25+ goals in 2022 World Cup qualifying? → Alphonso Davies." Options are Davies | Jonathan David | Cyle Larin | **Atiba Hutchinson**. Hutchinson (a defensive midfielder with ~9 career international goals) also did **not** have 25+ goals, so two options satisfy the stem — not unique.
**Source:** https://en.wikipedia.org/wiki/Canada_men%27s_national_soccer_team
**Remedy:** Replace Hutchinson with a genuine 25+-goal distractor, or reword.

### Row 11717 — FAIL: "Jonathan David 25+ goals by the 2022 World Cup" premature
- "Which Canadian player had **25+ international goals by the 2022 World Cup**? → Jonathan David." David did not reach 25 international goals until **2023**; his tally at the 2022 finals was lower. (Same defect as the batch-2 David cluster; present-tense "David has 25+ goals" and "Larin 25+ by 2022" variants PASS.)
**Source:** https://en.wikipedia.org/wiki/Canada_men%27s_national_soccer_team
**Remedy:** Re-anchor David's 25-goal milestone to 2023, or attribute the 2022 figure to Larin.

## Canada batch rows 11766–12105 — 5 FAIL

### Row 11810 — FAIL: stale superlative ("highest FIFA ranking = 33rd")
- "Which Canadian player's 2022 World Cup goal preceded their highest FIFA ranking? → Alphonso Davies," with explanation "the same year they reached their **highest FIFA ranking of 33rd**." 33rd was Canada's February 2022 mark only; they later climbed to **31st (Dec 2024)** and peaked at **26th (Sept 2025)**, so "highest = 33rd" is no longer true.
**Source:** https://en.wikipedia.org/wiki/Canada_men%27s_national_soccer_team
**Remedy:** Drop the all-time superlative (say "their 2022 ranking of 33rd") or update the peak to 26th.

### Rows 11791, 11890 — FAIL: "Jonathan David 25+ goals by/during 2022" premature
- **11791** ("leading scorer with over 25 goals **prior to the 2022 tournament**") and **11890** ("scored over 25 goals **during 2022 World Cup qualifying**") both place David's 25+ international goals in the 2022 window. David did not reach 25 international goals until **2023**. (Present-tense "David has 25+ goals" variants PASS; Larin 25+ by 2022 PASS.)
**Source:** https://en.wikipedia.org/wiki/Canada_men%27s_national_soccer_team
**Remedy:** Re-anchor the 25-goal milestone to 2023, or attribute the 2022 figure to Larin.

### Row 11823 — FAIL: non-unique answer
- "Which Canadian Premier League club joined before the 2022 World Cup qualifiers? → Forge FC." Options are Forge FC | Pacific FC | Cavalry FC | Valour FC — **all four** are 2019 CPL founding members, so every option "joined before the 2022 qualifiers." Not unique.
**Source:** https://en.wikipedia.org/wiki/Canadian_Premier_League
**Remedy:** Use three distractors that post-date 2022, or reword.

### Row 11787 — FAIL: non-unique answer
- "Which Canadian player was **NOT** a top scorer in 2022 World Cup qualifying? → Alphonso Davies." Options are Davies | Jonathan David | Cyle Larin | **Tajon Buchanan**. The explanation names David and Larin as the top scorers, leaving **both Davies and Buchanan** as "not a top scorer" — two valid answers.
**Source:** https://en.wikipedia.org/wiki/Canada_men%27s_national_soccer_team
**Remedy:** Replace Buchanan with one of the actual top scorers so exactly one option fits.

## Canada batch rows 12106–12428 — 3 FAIL

### Rows 12391, 12403, 12404 — FAIL: stale superlative ("FIFA ranking peak = 33rd")
- Each frames **33rd as Canada's FIFA-ranking peak** tied to 2022: 12403's stem ("Why did Canada's FIFA ranking **peak at 33rd** in 2022?"), and the explanations of 12391 ("Canada's FIFA ranking **peak of 33rd** in 2022") and 12404 ("Canada's ranking **peaked** after they qualified"). 33rd was their February 2022 mark only; they later climbed to **31st (Dec 2024)** and peaked at **26th (Sept 2025)**, so "33rd = peak" is no longer true. (The "why" answer — that the rise followed World Cup qualification — is itself fine; the defect is the all-time-peak framing.)
**Source:** https://en.wikipedia.org/wiki/Canada_men%27s_national_soccer_team
**Remedy:** Reword to "rose to 33rd in 2022" without the all-time-peak claim, or update the peak to 26th (2025).

---

# ✅ COSTA RICA (rows 15528–16571) — TC-06 liveness fails

**Two systematic, web-verified dataset errors recur throughout Costa Rica:**
1. **FIFA-ranking peak.** The dataset uniformly asserts Costa Rica's highest/best-ever FIFA ranking was **15th (in 2014)**. The actual all-time peak is **13th, reached in February 2015** ([MLSSoccer](https://www.mlssoccer.com/news/fifa-world-rankings-no-13-costa-rica-achieve-highest-rank-ever-us-slip-no-31), [Tico Times 12 Feb 2015](https://ticotimes.net/2015/02/12/costa-ricas-sele-reaches-its-highest-position-ever-in-fifa-world-ranking)). Any claim that 15th was their highest/peak/best-ever ranking is false.
2. **2026 World Cup qualification.** The dataset asserts Costa Rica **qualified for the 2026 World Cup directly via CONCACAF**. In reality Costa Rica was **ELIMINATED on 19 Nov 2025** (0-0 draw with Honduras, 3rd in CONCACAF Group C) and is **NOT at the 2026 World Cup** for the first time since 2006 ([Tico Times 19 Nov 2025](https://ticotimes.net/2025/11/19/costa-rica-eliminated-from-2026-world-cup-after-honduras-draw), [Tico Times 5 Jun 2026](https://ticotimes.net/2026/06/05/6-things-to-know-as-the-2026-world-cup-kicks-off-without-costa-rica)). Any "qualified for 2026" claim is false.

## Costa Rica batch rows 15528–15750 — 33 FAIL

### Rows 15530, 15533, 15534, 15535, 15539, 15540, 15541, 15546, 15547, 15548, 15633, 15649, 15658 — FAIL: false FIFA-ranking peak ("highest = 15th")
- Each presents **15th** as Costa Rica's highest/peak/best-ever FIFA ranking (most tie it to 2014). Their actual all-time peak is **13th, reached February 2015**. So "highest/peaked at 15th" is false; the correct best ranking is 13th.
- 15540 compounds the error: "Which CONCACAF nation **also** peaked at 15th? → **Costa Rica**" is both false (peak 13th) and self-referential (names Costa Rica itself as the "other" nation).
**Source:** https://www.mlssoccer.com/news/fifa-world-rankings-no-13-costa-rica-achieve-highest-rank-ever-us-slip-no-31
**Remedy:** Change the peak ranking to 13th (Feb 2015), or reword to a non-superlative "rose into the mid-teens after 2014."

### Rows 15615, 15625, 15626, 15628, 15629, 15630, 15669, 15670, 15700, 15708, 15714, 15715, 15719 — FAIL: false 2026 World Cup qualification
- Each asserts Costa Rica **qualified for the 2026 World Cup** (directly via CONCACAF). Costa Rica was **eliminated on 19 Nov 2025** and did **not** qualify for 2026. Rows whose answer *is* "2026 / CONCACAF qualification" (15625, 15626, 15629, 15630, 15714, 15715, 15719) have a directly false answer; rows that merely use 2026 qualification as a premise (15615, 15628, 15669, 15670, 15700, 15708) rest on a false premise.
**Source:** https://ticotimes.net/2025/11/19/costa-rica-eliminated-from-2026-world-cup-after-honduras-draw
**Remedy:** Remove all claims that Costa Rica reached the 2026 World Cup.

### Rows 15601, 15729 — FAIL: Excel date-mangled scoreline
- Both give the Costa Rica 3-1 win over Uruguay as the corrupt answer "**03-Jan**" (Excel mis-parse of "3-1"). The scoreline is correct (3-1) but the rendered answer string is wrong.
**Source:** https://en.wikipedia.org/wiki/Costa_Rica_national_football_team
**Remedy:** Store scorelines as text so "3-1" is not converted to a date.

### Row 15595 — FAIL: non-unique answer
- "Costa Rica are regular CONCACAF Gold Cup participants. Which **other** nation is? → United States." Options are United States | Mexico | Canada | Panama — **all four** are regular Gold Cup participants, so every option satisfies the stem.
**Source:** https://en.wikipedia.org/wiki/CONCACAF_Gold_Cup
**Remedy:** Use three non-CONCACAF distractors so only one option is a regular Gold Cup nation.

### Row 15624 — FAIL: wrong answer (New Zealand did not qualify)
- "Costa Rica qualified for 2022 via a playoff. Which **other** nation qualified via a playoff in 2022? → New Zealand." New Zealand **lost** the intercontinental playoff to Costa Rica and did **not** qualify. (The other intercontinental playoff was won by Australia, not listed.)
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification
**Remedy:** Replace the answer with Australia (the actual other intercontinental playoff winner).

### Row 15636 — FAIL: non-unique answer
- "Costa Rica topped their 2014 group. Which opponent did they **NOT** beat? → England." Options are England | Uruguay | Italy | **Netherlands**. They drew England (not beaten) **and** lost to the Netherlands on penalties (also not beaten), so two options satisfy the stem.
**Source:** https://en.wikipedia.org/wiki/Costa_Rica_national_football_team
**Remedy:** Replace Netherlands with a team Costa Rica actually beat (e.g. Greece).

### Row 15672 — FAIL: non-unique answer
- "Costa Rica's CONCACAF qualification secured their spot for which World Cup? → 2018 World Cup." Options are 2018 | 2014 | 2022 | **2006**. Costa Rica qualified directly via CONCACAF for **2006, 2014 and 2018** — three of the four options are valid; only 2022 (playoff) is excluded.
**Source:** https://en.wikipedia.org/wiki/Costa_Rica_national_football_team
**Remedy:** Use distractors that were not CONCACAF-direct qualifications.

### Row 15727 — FAIL: self-referential answer
- "In 2022 qualifying, Costa Rica's primary stadium capacity was closest to which **other** CONCACAF venue? → **Estadio Nacional (CR)**." The answer is Costa Rica's own stadium, not another venue. (The real distractors — Azteca ~87k, BC Place ~54k, NRG ~72k — are all far from Estadio Nacional's ~35,175.)
**Source:** https://en.wikipedia.org/wiki/Estadio_Nacional_(Costa_Rica)
**Remedy:** Offer a genuinely separate venue of similar capacity, or reword to drop "other."

## Costa Rica batch rows 15751–15980 — 17 FAIL

### Rows 15793, 15854, 15855 — FAIL: false FIFA-ranking peak ("highest = 15th")
- All three state Costa Rica's highest FIFA ranking was **15th** (in 2014). Actual all-time peak is **13th, February 2015**.
**Source:** https://www.mlssoccer.com/news/fifa-world-rankings-no-13-costa-rica-achieve-highest-rank-ever-us-slip-no-31
**Remedy:** Change peak ranking to 13th (Feb 2015).

### Rows 15790, 15851, 15852, 15853 — FAIL: false 2026 World Cup qualification
- Each states Costa Rica **qualified for the 2026 World Cup** (in 2026 / via CONCACAF). Costa Rica was **eliminated on 19 Nov 2025** and is not at the 2026 tournament.
**Source:** https://ticotimes.net/2025/11/19/costa-rica-eliminated-from-2026-world-cup-after-honduras-draw
**Remedy:** Remove all claims that Costa Rica reached the 2026 World Cup.

### Rows 15821, 15822, 15824, 15830, 15832 — FAIL: Excel date-mangled scoreline
- Corrupt date-formatted answers: 15821 "**03-Apr**" and 15832/15822/15824 "**03-Jan**" (for the 3-1 win over Uruguay), and 15830 "**04-Mar**" (for the 4-3 shootout loss to the Netherlands). The underlying facts (3-1, 3-4/4-3) are right; the rendered answer strings are corrupt.
**Source:** https://en.wikipedia.org/wiki/Costa_Rica_national_football_team
**Remedy:** Store scorelines as text so "3-1" / "4-3" are not converted to dates.

### Row 15788 — FAIL: non-unique answer
- "In which year did Costa Rica **NOT** qualify for a World Cup via CONCACAF qualification? → 2022." Options 2022 | 2014 | 2018 | **2026**. 2022 was a playoff (not CONCACAF) — but Costa Rica also **failed CONCACAF qualification for 2026** (eliminated), so 2026 equally satisfies "did not qualify via CONCACAF." Two valid answers.
**Source:** https://ticotimes.net/2025/11/19/costa-rica-eliminated-from-2026-world-cup-after-honduras-draw
**Remedy:** Replace the 2026 option with a year Costa Rica did qualify via CONCACAF.

### Row 15878 — FAIL: contradictory/false explanation
- "Which 2014 group opponent did Costa Rica not defeat? → England." Correct (they drew England 0-0), but the explanation states they "**did not face England**" — false and self-contradictory, since England was in their group.
**Source:** https://en.wikipedia.org/wiki/Costa_Rica_national_football_team
**Remedy:** Fix the explanation to "drew 0-0 with England."

### Row 15881 — FAIL: non-unique answer
- "Which 2014 group stage result was a Costa Rica win? → Costa Rica 1-0 Italy." Options also include **Costa Rica 3-1 Uruguay**, which is equally a genuine Costa Rica 2014 group win. Two valid answers.
**Source:** https://en.wikipedia.org/wiki/Costa_Rica_national_football_team
**Remedy:** Replace the Uruguay option with a non-win so only one option is a real Costa Rica victory.

### Row 15894 — FAIL: non-unique answer
- "Which 2018 World Cup qualifier, Costa Rica or Panama, reached via CONCACAF? → Costa Rica." **Both** Costa Rica and Panama qualified for the 2018 World Cup directly through CONCACAF (Panama's debut), so both options are valid.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONCACAF)
**Remedy:** Drop Panama from the options or reword so exactly one nation fits.

### Row 15902 — FAIL: self-referential answer
- "Which 2022 World Cup team lost by a larger margin than Costa Rica? → **Costa Rica**." The answer is Costa Rica itself; the stem asks for a different team that lost by a larger margin (and none of the listed teams did).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Reword to ask for Costa Rica's loss margin, or supply a team with a genuinely larger-margin defeat.

## Costa Rica batch rows 15981–16200 — 10 FAIL

### Rows 16088, 16113, 16155, 16157, 16163 — FAIL: false FIFA-ranking peak ("15th") in stem/explanation
- Each ties Costa Rica's post-2014 FIFA-ranking rise to **15th** as their peak (16157 stem/explanation "peak FIFA ranking of 15th"; 16088 "rise to 15th"; 16113/16155/16163 explanations "rise to 15th"). The actual all-time peak is **13th, February 2015**. (The "what caused the rise" answers — the quarter-final run — are themselves correct; the defect is the false 15th figure.) 16088 additionally misattributes the post-WC rise to manager Jorge Luis Pinto, who left in August 2014 before the Feb-2015 peak.
**Source:** https://www.mlssoccer.com/news/fifa-world-rankings-no-13-costa-rica-achieve-highest-rank-ever-us-slip-no-31
**Remedy:** Replace 15th with 13th (Feb 2015).

### Rows 16159, 16160 — FAIL: non-unique answer (multiple CONCACAF years)
- 16159 ("Which CR World Cup qualification was **NOT** via CONCACAF? → 2022," options include **2026**): Costa Rica also failed to qualify via CONCACAF for 2026 (eliminated 19 Nov 2025), so both 2022 and 2026 satisfy the stem.
- 16160 ("Which CR qualification was via CONCACAF, 2018 or 2022? → 2018," options include **2014**): both 2018 and 2014 were direct CONCACAF qualifications, so two options are valid.
**Source:** https://en.wikipedia.org/wiki/Costa_Rica_national_football_team
**Remedy:** Use option sets where exactly one year matches the stem.

### Row 16119 — FAIL: anachronistic cap count
- "Which Costa Rica player had **over 150 caps at the 2018 World Cup**? → Celso Borges." At the 2018 World Cup Borges had roughly **110** caps; no Costa Rica player had 150 caps in 2018. Borges only later became the record-holder (164 career caps). (Career-descriptor variants — "the midfielder with over 150 caps" — PASS; this one binds 150 to 2018.)
**Source:** https://en.wikipedia.org/wiki/Celso_Borges
**Remedy:** Drop the cap figure or re-anchor it to his later career.

### Row 16179 — FAIL: non-unique answer
- "Which Costa Rican **forward** debuted before the 2014 World Cup? → Joel Campbell." Bryan Ruiz (a forward, debuted 2005) is also an option and likewise debuted before 2014, so two forward options satisfy the stem.
**Source:** https://en.wikipedia.org/wiki/Costa_Rica_national_football_team
**Remedy:** Replace Ruiz with a forward who debuted after 2014, or reword.

### Row 16053 — FAIL: self-referential answer
- "Which Costa Rica goalkeeper's 2014 World Cup run is most comparable to **Keylor Navas's**? → Keylor Navas." The answer is Navas himself (the explanation even concedes "the question asks for the Costa Rican goalkeeper, which is Keylor Navas himself").
**Source:** https://en.wikipedia.org/wiki/Keylor_Navas
**Remedy:** Reword to ask which goalkeeper starred in 2014 (drop the self-comparison).

## Costa Rica batch rows 16201–16400 — 6 FAIL

### Rows 16272, 16294 — FAIL: false 2026 World Cup qualification
- 16272 ("Which CR qualification path for the **2026 World Cup** matched their 2014 method? → CONCACAF qualification," explanation "qualified for both 2014 and 2026 directly through CONCACAF") and 16294 (explanation "direct CONCACAF qualification for 2014, 2018, **and 2026**") both assert Costa Rica qualified for 2026. Costa Rica was eliminated on 19 Nov 2025 and did not qualify.
**Source:** https://ticotimes.net/2025/11/19/costa-rica-eliminated-from-2026-world-cup-after-honduras-draw
**Remedy:** Remove the 2026 qualification claims. (Rows merely noting Navas's aging as a challenge "for the 2026 cycle/transition" — 16227, 16283, 16287, 16289 — PASS, since they do not assert qualification.)

### Row 16304 — FAIL: false FIFA-ranking figure ("15th")
- "Which FIFA ranking did Costa Rica achieve after the 2014 World Cup? → 15th." Their actual post-2014 peak was **13th (Feb 2015)**.
**Source:** https://www.mlssoccer.com/news/fifa-world-rankings-no-13-costa-rica-achieve-highest-rank-ever-us-slip-no-31
**Remedy:** Change the answer to 13th.

### Rows 16367, 16368, 16399 — FAIL: non-unique answer
- 16367 ("Which nation did Costa Rica **NOT** beat at the 2014 World Cup? → Spain"): they also did not beat the **Netherlands** (lost on penalties), and Netherlands is an option — two valid answers.
- 16368 ("Which nation did Costa Rica **NOT** face in the 2014 knockout rounds? → Germany"): **Uruguay** (an option) was also not a knockout opponent (group stage only), so two options fit.
- 16399 ("Which nation, like Costa Rica in 2014, qualified via CONCACAF's direct path? → United States"): **Honduras** (an option) also qualified directly for 2014 via the CONCACAF Hexagonal (only Mexico went via playoff), so two options are valid.
**Source:** https://en.wikipedia.org/wiki/Costa_Rica_national_football_team
**Remedy:** Replace the colliding distractor (Netherlands / Uruguay / Honduras) so exactly one option satisfies each stem.

## Costa Rica batch rows 16401–16571 — 14 FAIL

### Rows 16461, 16465, 16466, 16473, 16538, 16559 — FAIL: false 2026 World Cup qualification
- Each asserts Costa Rica **qualified for the 2026 World Cup** directly via CONCACAF: 16461 ("2014 **and 2026**"), 16465/16466/16473 (answer = 2026), 16538 ("Why did CR qualify for the 2026 WC?"), and 16559 (presupposes a "2026 World Cup squad"). Costa Rica was eliminated on 19 Nov 2025 and is not at the 2026 tournament.
**Source:** https://ticotimes.net/2025/11/19/costa-rica-eliminated-from-2026-world-cup-after-honduras-draw
**Remedy:** Remove the 2026-qualification answers/premises. (Rows about Navas being phased out "for the 2026 cycle" — 16498, 16548, 16570 — PASS, as they assert no qualification.)

### Rows 16464, 16467, 16468, 16471 — FAIL: non-unique CONCACAF-qualification answer
- 16464 ("Which WC did CR **NOT** qualify for via CONCACAF? → 2022," option 2026): CR also failed CONCACAF qualification for 2026, so 2022 and 2026 both fit.
- 16467 ("through CONCACAF, **not a playoff**? → 2014"), 16468 ("through CONCACAF? → 2014"), 16471 ("via CONCACAF direct placement? → 2018"): both 2014 and 2018 were direct CONCACAF qualifications, so two options are valid in each. (16469/16472, pinned to "via playoff" / "in 2018", PASS.)
**Source:** https://en.wikipedia.org/wiki/Costa_Rica_national_football_team
**Remedy:** Use option sets where exactly one year matches.

### Row 16470 — FAIL: false 2026 claim in explanation
- "Which World Cup did Costa Rica qualify for via an intercontinental playoff? → 2022" — answer is correct, but the explanation adds "unlike their direct CONCACAF qualification for 2014, 2018, **and 2026**," which is false (no 2026 qualification).
**Source:** https://ticotimes.net/2025/11/19/costa-rica-eliminated-from-2026-world-cup-after-honduras-draw
**Remedy:** Drop "and 2026" from the explanation.

### Rows 16543, 16557 — FAIL: false FIFA-ranking peak ("15th")
- 16543 ("Why did Costa Rica rise to **15th** in the 2014 FIFA rankings?") and 16557 ("Why did Costa Rica's FIFA ranking **peak at 15th** in 2014?") embed 15th as their ranking. Actual all-time peak is **13th (Feb 2015)**. (The graded answers — "their World Cup performance" — are correct; the 15th figure is the defect.)
**Source:** https://www.mlssoccer.com/news/fifa-world-rankings-no-13-costa-rica-achieve-highest-rank-ever-us-slip-no-31
**Remedy:** Replace 15th with 13th.

### Row 16434 — FAIL: non-unique answer
- "Which team did Costa Rica **NOT** concede seven goals to at the 2022 World Cup? → Germany." Costa Rica conceded seven only to Spain; the other three options (Germany, Netherlands, Brazil) are all teams they did not concede seven to (and did not even play), so three options satisfy the stem.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_E
**Remedy:** Make Spain the only "conceded 7" team and use distractors Costa Rica actually faced, or reword.

---

# ✅ ENGLAND (rows 23687–25401) — TC-06 liveness fails

**Web-verified fact anchors used throughout England:** highest FIFA ranking = **3rd** (2012 and 2017–18); England qualified for the **2026 World Cup with a perfect 8-win, 0-goals-conceded record** (UEFA Group K) — so "perfect 2026 qualification" and "3rd in 2012 and 2018" claims **PASS**. Recurring dataset error: England's post-2014-World-Cup ranking is stated as **17th**, but they actually fell to **20th (July 2014)** and were **18th by Sept 2014** — 17th is unsupported.

## England batch rows 23687–23920 — 18 FAIL

### Rows 23690, 23692, 23693, 23713, 23714, 23715, 23719, 23720, 23721 — FAIL: wrong FIFA ranking ("fell to 17th in 2014")
- Each states that after their 2014 World Cup group-stage exit England "fell to **17th**." Post-exit they actually dropped to **20th (July 2014)**, recovering to **18th by September 2014** — 17th does not match the verifiable figures.
- 23692 also self-references: "which nation **also** fell to 17th? → **England**" names England itself.
**Source:** http://www.englandfootballonline.com/teamrank/rankfifa.html (England fell to 20th in July 2014)
**Remedy:** Replace 17th with 20th (July 2014), and give 23692 a genuine second nation.

### Row 23689 — FAIL: Excel date-mangled scoreline
- England's 2018 World Cup semi-final loss margin is given as the corrupt answer "**02-Jan**" (Excel mis-parse of "2-1"). The scoreline (2-1 to Croatia) is right; the rendered string is corrupt.
**Source:** https://en.wikipedia.org/wiki/England_national_football_team
**Remedy:** Store scorelines as text so "2-1" is not converted to a date.

### Rows 23857, 23894 — FAIL: wrong answer (a 2022 squad player was based abroad)
- Both claim **all 26** of England's 2022 World Cup squad were at Premier League clubs / **zero** based abroad. **Jude Bellingham** was a Borussia Dortmund (Bundesliga) player at the 2022 World Cup, so at least one was based abroad.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_squads
**Remedy:** Correct the count (≥1 abroad), or reword.

### Row 23748 — FAIL: temporal error (Rooney WAS top scorer during the 2022 WC)
- "At the 2022 World Cup, which England player was **NOT** the all-time top scorer? → Wayne Rooney." Harry Kane did not overtake Rooney until **March 2023**, so during the Nov–Dec 2022 World Cup Rooney **was** still the record holder. The answer/explanation invert the timeline.
**Source:** https://en.wikipedia.org/wiki/Harry_Kane
**Remedy:** Re-anchor to a player who genuinely was not the record holder, or move the timeframe past March 2023.

### Row 23787 — FAIL: non-unique answer
- "At which World Cup year was Wayne Rooney still England's all-time top scorer? → 2018." Rooney was the record holder at **both 2018 and 2022** (Kane broke it March 2023), and 2022 is an option, so two answers are valid.
**Source:** https://en.wikipedia.org/wiki/Wayne_Rooney
**Remedy:** Remove 2022 from the options.

### Row 23807 — FAIL: non-unique answer
- "England finished 1st in which FIFA World Cup qualifying group? → 2018 World Cup group." England topped their qualifying group for **2010, 2014, 2018 and 2022** — all four options are groups they won.
**Source:** https://en.wikipedia.org/wiki/England_national_football_team
**Remedy:** Use distractor years where England did not finish first.

### Row 23812 — FAIL: non-unique answer
- "Which other World Cup knockout loss was by a 2-1 scoreline? → 2022 quarter-final." The **2018 semi-final** (also an option) was likewise a **2-1** World Cup knockout defeat (to Croatia), so two options fit.
**Source:** https://en.wikipedia.org/wiki/England_national_football_team
**Remedy:** Replace the 2018-semi-final option with a non-2-1 result.

### Rows 23792, 23793 — FAIL: non-unique answer (same song)
- "Which anthem did England fans famously sing? → Football's Coming Home," with **Three Lions** as a separate option. "Three Lions" *is* the song whose chorus is "Football's coming home" — both options name the same anthem.
**Source:** https://en.wikipedia.org/wiki/Three_Lions
**Remedy:** Drop one of the two identical options.

## England batch rows 23921–24170 — 29 FAIL

### Rows 23937, 23940, 23957, 23979, 24142, 24151, 24152, 24157, 24158, 24160, 24161, 24165, 24168, 24169, 24170 — FAIL: Excel date-mangled scoreline
- Each answer is a corrupt date-formatted score: "06-Feb"=6-2 (Iran, 23937/24151), "04-Jan"=4-1 (Germany 2010, 23940/24170), "02-Jan"=2-1 (Poland 23957/24158/24169; Denmark 23979/24152/24157; Iceland 24142; France 24165), "02-Feb"=2-2 (Scotland, 24160), "03-Jan"=3-1 (Netherlands 2019 NL, 24161), "03-Feb"=3-2 (Euro 2020 shootout, 24168). The underlying scores are correct; the rendered answer strings are corrupt.
**Source:** https://en.wikipedia.org/wiki/England_national_football_team
**Remedy:** Store scorelines as text so e.g. "6-2" is not converted to a date.

### Rows 23986, 24080, 24137, 24138 — FAIL: wrong FIFA ranking ("fell to 17th in 2014")
- Each gives England's post-2014-World-Cup ranking as **17th**; they actually fell to **20th (July 2014)**. Notably 24137 and 24138 even list **20th** as an option but mark 17th correct.
**Source:** http://www.englandfootballonline.com/teamrank/rankfifa.html
**Remedy:** Change the answer to 20th.

### Rows 24092, 24100 — FAIL: non-unique answer (and false "17th" premise)
- "In which year did England NOT reach / NOT peak at 3rd in the FIFA rankings? → 2014," options including **2022**. England were ~5th in 2022 (not 3rd), so 2022 also satisfies "did not reach 3rd" — two valid answers. Both explanations also repeat the false "17th in 2014" figure.
**Source:** https://en.wikipedia.org/wiki/England_national_football_team
**Remedy:** Replace 2022 with a year England did reach 3rd (2012 or 2018 are already used), or reword.

### Rows 23969, 23972, 23973 — FAIL: wrong answer (a 2022 squad player was based abroad)
- All claim England's entire 26-man 2022 World Cup squad was at English/Premier League clubs (zero abroad). **Jude Bellingham** played for Borussia Dortmund (Germany) at that tournament.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_squads
**Remedy:** Correct the claim (≥1 player abroad).

### Row 23927 — FAIL: wrong answer (2010 qualifying had no draws)
- "England's 2010 UEFA group record was 9 wins and how many draws? → 1 draw." England's record was **9 wins, 0 draws, 1 loss** (they lost the dead-rubber away to Ukraine). The correct answer "0 draws" is even an option.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change the answer to 0 draws (and fix the "9 wins and 1 draw" explanations elsewhere to "9 wins, 1 loss").

### Row 23970 — FAIL: wrong answer (count of English Champions League titles)
- "How many Champions League titles did English clubs win between 2008 and 2023? → Six." English clubs won **five**: Man United (2008), Chelsea (2012), Liverpool (2019), Chelsea (2021), Man City (2023).
**Source:** https://en.wikipedia.org/wiki/List_of_European_Cup_and_UEFA_Champions_League_finals
**Remedy:** Change the answer to five.

### Row 24060 — FAIL: wrong answer (Henderson's World Cup debut)
- "In which World Cup did England's Jordan Henderson make his tournament debut? → 2018." Henderson was in (and played at) the **2014** World Cup, so 2018 was not his World Cup debut.
**Source:** https://en.wikipedia.org/wiki/Jordan_Henderson
**Remedy:** Change the answer to the 2014 World Cup.

### Row 24103 — FAIL: wrong answer (Euro 2024 Young Player)
- "In which year did England's Jude Bellingham win the Euro Young Player award? → 2024." The **Euro 2024 Young Player of the Tournament was Lamine Yamal (Spain)**, not Bellingham.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024
**Remedy:** Remove the claim; Bellingham did not win the Euro 2024 young-player award.

### Row 24003 — FAIL: non-unique / nonsensical answer
- "In which World Cup host nation did England's Leicester City NOT win their 2016 title? → South Africa." Leicester won the title in **England**, so they did not win it in **any** of the listed host nations (South Africa, Germany, Brazil, Russia) — all four options satisfy the stem.
**Source:** https://en.wikipedia.org/wiki/2015%E2%80%9316_Premier_League
**Remedy:** Reword; the premise makes every option correct.

## England batch rows 24171–24420 — 5 FAIL

### Row 24192 — FAIL: wrong FIFA ranking ("fell to 17th in 2014")
- "When did England fall to **17th** in the FIFA rankings after a World Cup group-stage exit? → In 2014." England actually fell to **20th** (July 2014).
**Source:** http://www.englandfootballonline.com/teamrank/rankfifa.html
**Remedy:** Change 17th to 20th.

### Rows 24237, 24238, 24259 — FAIL: wrong answer (Euro 2024 Young Player)
- Each states Jude Bellingham was **Young Player of the Tournament at Euro 2024**. The award went to **Lamine Yamal (Spain)**.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024
**Remedy:** Remove the claim; Bellingham did not win the Euro 2024 young-player award.

### Row 24320 — FAIL: anachronistic/false statistic
- "Which England captain had **78 goals in 112 caps before the 2022 World Cup**? → Harry Kane." Those are much-later career figures; **before the 2022 World Cup Kane had ~51 goals** (he passed Rooney's 53 only in March 2023). (The sibling row 24321, which compares Kane's career ratio 78/112 to Rooney's 53/120 with no false time anchor, PASSES.)
**Source:** https://en.wikipedia.org/wiki/Harry_Kane
**Remedy:** Drop "before the 2022 World Cup" or use Kane's actual pre-2022 tally.

## England batch rows 24421–24700 — 7 FAIL

### Rows 24560, 24561, 24562 — FAIL: wrong answer (Euro 2024 Young Player)
- Each names Jude Bellingham as **Euro 2024 Young Player of the Tournament**. The award went to **Lamine Yamal (Spain)**.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024
**Remedy:** Remove the claim.

### Row 24593 — FAIL: temporal error (Kane became top scorer in 2023, not "by 2022")
- "Which England player became their all-time top scorer **by 2022**? → Harry Kane." Kane only passed Wayne Rooney's record in **March 2023**; through 2022 Rooney was still the record holder.
**Source:** https://en.wikipedia.org/wiki/Harry_Kane
**Remedy:** Change the timeframe to 2023, or reword.

### Row 24687 — FAIL: temporal error (record holder during the 2014 WC was Charlton)
- "Which England player held the national goalscoring record **during the 2014 World Cup**? → Wayne Rooney." During the 2014 World Cup the record holder was still **Bobby Charlton (49)**; Rooney only passed him in **September 2015**. (Sibling rows anchoring Rooney's record to Euro 2016, the 2018 qualifiers, or "before Kane" PASS, since he held it 2015–2023.)
**Source:** https://en.wikipedia.org/wiki/Wayne_Rooney
**Remedy:** Re-anchor to 2016 onward, or change the answer to Bobby Charlton.

### Row 24631 — FAIL: non-unique answer
- "Which England player did **NOT** score a late equalizer at a major tournament? → Harry Kane." Only Bellingham (Euro 2024) scored a late equalizer among the options, so **Kane, Luke Shaw and Frank Lampard** all "did not" — three valid answers.
**Source:** https://en.wikipedia.org/wiki/England_national_football_team
**Remedy:** Make three of the four options genuine late-equalizer scorers, or reword.

### Row 24648 — FAIL: non-unique answer
- "Which England player featured at the 2022 World Cup and Euro 2024 while also earning individual award nominations? → Phil Foden." **Saka and Bellingham** (both options) equally featured at both tournaments and earned individual award nominations, so the criteria fit three options.
**Source:** https://en.wikipedia.org/wiki/England_national_football_team
**Remedy:** Add a criterion unique to one player, or change the distractors.

## England — CORRECTION: "Pickford in the Euro 2020 Team of the Tournament" (13 rows, batches 2–5)

**Web-verified:** the official UEFA Euro 2020 Team of the Tournament goalkeeper was **Gianluigi Donnarumma** (Italy), and England's representatives were **Kyle Walker, Harry Maguire and Raheem Sterling** — **Jordan Pickford was NOT in it**. Every row asserting Pickford made the Euro 2020 Team of the Tournament is therefore a wrong answer. (Pickford *did* save penalties in the Euro 2020 final shootout — those rows remain PASS.)

- **Rows 24028, 24029, 24123 (batch 2), 24278, 24376, 24388, 24390, 24391, 24392 (batch 3), 24696 (batch 4)** were initially mis-passed and have been **removed from `QA_PASSED_ALL.md`** and counted as FAIL here (batch PASS/FAIL totals corrected accordingly: B2 182P/32F, B3 194P/11F, B4 225P/8F).
- **Rows 24854, 24906, 24932 (batch 5)** likewise FAIL. 24696/24854/24932 are aggravated: their distractors (Maguire, Walker, Sterling) are the players who *actually* made the Team of the Tournament.
**Source:** https://www.uefa.com/uefaeuro/history/news/0286-1932cbd2ce99-96c5a8fb4205-1000--uefa-euro-2020-team-of-the-tournament/
**Remedy:** Change the answer to Donnarumma/Walker/Maguire/Sterling as appropriate, or reword to Pickford's actual Euro 2020 achievement (penalty saves in the final shootout).

## England batch rows 24701–25050 — 13 FAIL (incl. 3 Pickford-ToT above: 24854, 24906, 24932)

### Rows 24884, 24898, 24933 — FAIL: wrong answer (Euro 2024 Young Player)
- Each names Jude Bellingham as **Euro 2024 Young Player of the Tournament**; the award went to **Lamine Yamal (Spain)**.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024
**Remedy:** Remove the claim.

### Rows 24996, 25017 — FAIL: wrong FIFA ranking ("dropped to 17th in 2014")
- Both give England's post-2014-group-exit ranking as **17th**; it was **20th** (July 2014). 24996 even lists 20th as an option.
**Source:** http://www.englandfootballonline.com/teamrank/rankfifa.html
**Remedy:** Change 17th to 20th.

### Row 25024 — FAIL: wrong answer (a 2022 squad player was based abroad)
- "Which England World Cup squad had **all 26 players based in England**? → The 2022 squad." **Jude Bellingham** was at Borussia Dortmund (Germany) at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_squads
**Remedy:** Correct the claim; not all 26 were England-based.

### Row 24878 — FAIL: temporal error (Rooney, not Kane, was record holder at the 2022 WC)
- "Which England player was their **all-time top scorer at the 2022 World Cup**? → Harry Kane." Kane only passed Rooney's record in **March 2023**; at the Nov–Dec 2022 World Cup Rooney was still the all-time top scorer.
**Source:** https://en.wikipedia.org/wiki/Harry_Kane
**Remedy:** Change the answer to Wayne Rooney, or move the timeframe to 2023+.

### Row 24764 — FAIL: wrong context (Kane's 54th goal came in a Euro 2024 qualifier)
- "Which England player scored his 54th international goal in **2023 World Cup qualifying**? → Harry Kane." Kane's record-breaking 54th goal (23 March 2023 vs Italy) came in a **UEFA Euro 2024 qualifier**; there was no World Cup qualifying in 2023 (2026 qualifying began in 2025).
**Source:** https://en.wikipedia.org/wiki/Harry_Kane
**Remedy:** Change "2023 World Cup qualifying" to "a Euro 2024 qualifier."

### Row 24781 — FAIL: false premise (England did not play a 2018 World Cup final)
- "Which England player scored in the Euro 2024 final, **unlike Kane in 2018**? → Cole Palmer," explained as "Kane did not score in the **2018 World Cup final**." England did not reach the 2018 World Cup final (they lost the semi-final and the third-place play-off).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Drop the false 2018-final comparison.

### Row 24905 — FAIL: non-unique answer
- "Which England player, unlike Marcus Rashford, scored in the 2022 World Cup but **not against Wales**? → Bukayo Saka." **Kane** (vs Senegal/France) and **Sterling** (vs Iran), both options, also scored in the 2022 World Cup and not against Wales.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_B
**Remedy:** Use distractors who did not score in the 2022 World Cup.

## England batch rows 25051–25401 — 5 FAIL

### Row 25074 — FAIL: Excel date-mangled formation
- England's 2018 World Cup semi-final formation is given as the corrupt answer "**03/05/2002**" (Excel mis-parse of "3-5-2"). The formation (3-5-2 / 3-4-3) is right; the rendered string is corrupt.
**Source:** https://en.wikipedia.org/wiki/England_national_football_team
**Remedy:** Store formations as text so "3-5-2" is not converted to a date.

### Row 25116 — FAIL: non-unique answer
- "Which manager was **NOT** in charge of England at the 2010 World Cup? → Gareth Southgate." Only **Fabio Capello** managed England in 2010; the other three options (Southgate, Roy Hodgson, Sven-Göran Eriksson) were all not in charge then, so three options satisfy the stem.
**Source:** https://en.wikipedia.org/wiki/England_national_football_team
**Remedy:** Make three options the 2010 manager-era figures, or reword so exactly one was not in charge.

### Row 25165 — FAIL: wrong answer (England did beat Hungary)
- "Which nation did England **NOT defeat** in their 2022 World Cup qualifying campaign? → Hungary." England **beat Hungary 4-0** away (Sept 2021) in that campaign (and drew 1-1 at home); they defeated every group opponent at least once, so no option is correct as stated. (England's *dropped points* — the recurring fact — were draws with Hungary and Poland, which is a different claim.)
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA_Group_I)
**Remedy:** Reword to "drew with" / "dropped points to," or use an opponent England genuinely never beat.

### Row 25374 — FAIL: false FIFA-ranking premise ("dropped to 17th in 2014")
- "Why did England **drop to 17th** in the FIFA rankings in 2014? → Group-stage elimination." The cause (group-stage exit) is right, but England fell to **20th**, not 17th.
**Source:** http://www.englandfootballonline.com/teamrank/rankfifa.html
**Remedy:** Change 17th to 20th.

### Row 25399 — FAIL: false premise (2022 squad not entirely Premier League-based)
- "Why was England's 2022 World Cup squad **entirely Premier League-based**? → all 26 players selected … based at English clubs." **Jude Bellingham** played for Borussia Dortmund (Germany) at that tournament, so the squad was not entirely Premier League-based.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_squads
**Remedy:** Correct the premise; not all 26 were Premier League-based.

---

# ✅ GHANA (rows 29166–30309) — TC-06 liveness fails

**Web-verified fact anchors:** Ghana **drew Germany 2-2** in the 2014 group stage (and lost to USA and Portugal) — so "lost to USA and Germany" claims FAIL. Ghana reached the **2010 AFCON FINAL** (lost 1-0 to Egypt), not the semi-finals. Ghana **DID qualify for the 2026 World Cup** (topped CAF Group I under Otto Addo, secured 13 Oct 2025) — so "qualified for 2026" claims PASS. 2010 WC QF lost to Uruguay on penalties after the Suárez handball; Gyan (51 goals) is the all-time top scorer; 2022 group exit (beat South Korea 3-2 via Kudus brace, lost Portugal 3-2 & Uruguay 2-0).

## Ghana batch rows 29166–29420 — 26 FAIL

### Rows 29172, 29237, 29331, 29339, 29380, 29411 — FAIL: wrong result ("lost to USA and Germany" in 2014)
- Each says Ghana **lost to USA and Germany** in the 2014 group stage. Ghana **drew Germany 2-2**; their two defeats were to the **USA (1-2) and Portugal (2-1)**. (29172's answer "USA and Germany" is directly wrong; 29237/29331/29339/29380/29411 carry the false result as a premise.)
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_G
**Remedy:** Replace "Germany" with "Portugal."

### Rows 29279, 29351, 29409 — FAIL: wrong stage (2010 AFCON final, not semi-finals)
- Each states Ghana reached the **2010 AFCON semi-finals**; Ghana actually reached the **final** (lost 1-0 to Egypt). 29279 even offers "the final" as an option; 29351/29409 are also non-unique (Ghana reached the AFCON semis in 2008 and 2012 too).
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations
**Remedy:** Change the answer to "the final" / a year where the semi-final was their actual endpoint.

### Rows 29229, 29253, 29278, 29361, 29362, 29363, 29367, 29368, 29372 — FAIL: Excel date-mangled scoreline
- Corrupt date-formatted answers: "02-Jan" = 2-1 (Ghana 2-1 USA, 2010 — 29229/29363/29368/29372), "03-Feb" = 3-2 (Ghana 3-2 South Korea, 2022 — 29253/29278/29362/29367), "01-Jan" = 1-1 (1-1 aggregate vs Nigeria — 29361). Underlying scores correct; rendered strings corrupt.
**Source:** https://en.wikipedia.org/wiki/Ghana_national_football_team
**Remedy:** Store scorelines as text.

### Rows 29271, 29275, 29277 — FAIL: wrong count (managers AT World Cups)
- Each answers **Four** for the number of managers who led Ghana **at** the 2010/2014/2022 World Cups. Only **three** managed at those tournaments — Rajevac (2010), Appiah (2014), Addo (2022). Avram Grant managed Ghana between tournaments but at **no** World Cup (Ghana missed 2018). (Sibling row 29232 correctly answers "Three.")
**Source:** https://en.wikipedia.org/wiki/Ghana_national_football_team
**Remedy:** Change the answer to three, or reword to "managers in 2010-2022" (which excludes the "at World Cups" qualifier).

### Row 29292 — FAIL: wrong club (Kudus was at Ajax in 2022, not West Ham)
- "Which star attacker played for **West Ham** during the 2022 World Cup? → Mohammed Kudus." Kudus was an **Ajax** player at the 2022 World Cup; he only joined West Ham in August 2023.
**Source:** https://en.wikipedia.org/wiki/Mohammed_Kudus
**Remedy:** Change "West Ham" to "Ajax."

### Rows 29242, 29419 — FAIL: non-unique answer (multiple qualification years)
- 29242 ("Ghana qualified for the FIFA World Cup in which year? → 2026," options 2026/2010/2014/2022): Ghana qualified for **all four** of those World Cups, so every option is valid.
- 29419 ("Which 2020s FIFA World Cup did Ghana qualify for? → 2022," option 2026): Ghana qualified for **both** 2022 and 2026.
**Source:** https://en.wikipedia.org/wiki/Ghana_at_the_FIFA_World_Cup
**Remedy:** Use option sets where exactly one year fits.

### Row 29283 — FAIL: non-unique answer (all options are Ghana Premier League clubs)
- "Which Ghanaian club plays in the Ghana Premier League? → Hearts of Oak." All four options — **Hearts of Oak, Asante Kotoko, Medeama SC, Ashanti Gold** — have played in the Ghana Premier League.
**Source:** https://en.wikipedia.org/wiki/Ghana_Premier_League
**Remedy:** Use three non-GPL distractors.

### Row 29417 — FAIL: self-referential answer
- "Which 2017 AFCON semi-finalist matched Ghana's tournament performance? → **Ghana**." The answer is Ghana itself; **Egypt** (an option) was also a 2017 semi-finalist (and finalist).
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations
**Remedy:** Make the answer a different semi-finalist, or reword to drop the self-comparison.

## Ghana batch rows 29421–29700 — 9 FAIL

### Rows 29423, 29424 — FAIL: false explanation / non-unique (Ghana had no 2022 draws; scored 0 vs Uruguay)
- 29423 ("Which 2022 opponent did Ghana NOT play to a draw? → Uruguay") claims Ghana "drew 3-3 with Portugal and 2-2 with South Korea" — false; Ghana **lost 3-2 to Portugal, beat South Korea 3-2, and lost 2-0 to Uruguay** (no draws), so all three options satisfy "not a draw."
- 29424 ("Which match saw Ghana score more than against Uruguay? → South Korea") says Ghana scored "2 against Uruguay" — they scored **0** (2-0 loss); both the South Korea (3) and Portugal (2) matches exceed 0, so the answer is non-unique.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_H
**Remedy:** Fix the results (no draws; 0 vs Uruguay) and the option sets.

### Rows 29514, 29524 — FAIL: wrong club (Kudus was at Ajax in 2022, not the Premier League / West Ham)
- 29514 ("Which 2022 squad member did NOT play in the Premier League? → Inaki Williams") claims Kudus, Partey and Salisu "were Premier League players" — **Kudus was at Ajax** (Eredivisie) in 2022, so he also was not a PL player (non-unique with Williams).
- 29524 ("Which attacker starred for **West Ham** at the 2022 World Cup? → Kudus") — Kudus was an **Ajax** player then; he joined West Ham only in August 2023. (Present-tense "Kudus plays for West Ham" rows PASS.)
**Source:** https://en.wikipedia.org/wiki/Mohammed_Kudus
**Remedy:** Use Kudus's 2022 club (Ajax); reserve West Ham for present-tense statements.

### Rows 29489, 29490, 29503 — FAIL: self-referential answer
- Each asks which CAF nation "**like Ghana**" did something, and answers **Ghana** itself: 29489 (qualified for 2014 — Nigeria, Côte d'Ivoire and Cameroon also did), 29490 (failed to qualify for 2018), 29503 (reached the 2010 AFCON semi-finals — and Ghana actually reached the **final**; Nigeria was a genuine 2010 semi-finalist).
**Source:** https://en.wikipedia.org/wiki/Ghana_national_football_team
**Remedy:** Make the answer a different nation, not Ghana.

### Row 29533 — FAIL: non-unique answer
- "Which Ghana campaign was identical to their 2010 route? → 2014 qualification." Ghana also qualified directly through CAF for **2026** (an option), so 2026 is equally "identical to 2010."
**Source:** https://en.wikipedia.org/wiki/Ghana_at_the_FIFA_World_Cup
**Remedy:** Remove the 2026 option or specify the distinguishing detail.

### Row 29698 — FAIL: false explanation
- "Which 2010 Ghana opponent was NOT faced again in 2022? → United States" (correct), but the explanation claims "Ghana faced Uruguay **and South Korea** in both tournaments." Ghana did **not** play South Korea in 2010 (their 2010 opponents were Serbia, Australia, Germany, USA, Uruguay).
**Source:** https://en.wikipedia.org/wiki/Ghana_at_the_FIFA_World_Cup
**Remedy:** Drop the false "South Korea in both" claim from the explanation.

## Ghana — CORRECTION: non-unique "~40,000-capacity stadium" rows (batches 1–2)

**Both Accra Sports Stadium (~40,000, capital) and Baba Yara Stadium (~40,000, Kumasi) are ~40k Ghana venues** (the dataset itself calls Baba Yara "the *other* ~40,000 stadium"). Any "which Ghana stadium holds ~40,000?" item that lists **both** as options without a capital/Kumasi disambiguator is non-unique.
- **Row 29281 (batch 1)** ("which Ghana stadium with 40,000 seats? → Baba Yara"; options also include Accra Sports and "Kumasi Sports Stadium" = Baba Yara's own alias) and **Row 29432 (batch 2)** ("which 40,000-capacity stadium hosts qualifiers? → Baba Yara"; options include Accra Sports) were initially mis-passed and have been **removed from `QA_PASSED_ALL.md`** and counted FAIL here (corrected batch totals: B1 163P/27F, B2 186P/10F).
- Rows that *do* disambiguate (e.g. "in the capital" → Accra, "in Kumasi"/"like Accra" → Baba Yara) remain PASS.
**Source:** https://en.wikipedia.org/wiki/Baba_Yara_Stadium
**Remedy:** Drop one of the two 40k stadiums from the options, or add a city qualifier.

## Ghana batch rows 29701–29970 — 10 FAIL

### Rows 29912, 29915, 29916, 29917 — FAIL: non-unique answer (two ~40,000 stadiums)
- Each asks which Ghana stadium holds ~40,000 with **both Accra Sports Stadium and Baba Yara Stadium** offered (no city qualifier), so two options are valid. 29915 additionally has a false premise — "Cape Town Stadium's 2010 World Cup capacity of 40,000" (it held ~64,000).
**Source:** https://en.wikipedia.org/wiki/Baba_Yara_Stadium
**Remedy:** Offer only one 40k Ghana stadium, or disambiguate by city.

### Rows 29919, 29961, 29970 — FAIL: wrong 2010 AFCON stage (Ghana reached the FINAL)
- 29919 ("Which stage did Ghana reach at the 2010 AFCON? → the semi-finals") asks their endpoint, which was the **final** (runners-up to Egypt) — and "the final" is an option.
- 29961 ("Which team reached the 2010 AFCON semi-finals? → Ghana") is non-unique: **Nigeria** (an option, 3rd place) was also a 2010 semi-finalist.
- 29970 ("Which tournament matched their 2017 AFCON semi-final finish? → 2010 AFCON"): in 2010 Ghana reached the **final**, not a semi-final finish; the matching tournament is **2013** (also a semi-final/4th-place finish).
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations
**Remedy:** Use "the final" for 2010; pick 2013 for a semi-final-finish match.

### Row 29712 — FAIL: non-unique answer (Kudus also not in the Premier League in 2022)
- "Which 2022 squad player did NOT play in the Premier League? → Inaki Williams." **Mohammed Kudus** (an option) was at **Ajax** in 2022 (Eredivisie), so he too was not a Premier League player.
**Source:** https://en.wikipedia.org/wiki/Mohammed_Kudus
**Remedy:** Replace Kudus with a genuine Premier League player.

### Row 29747 — FAIL: non-unique answer
- "Which Ghana player had over 25 caps after the 2022 World Cup? → Mohammed Kudus." All four options (Kudus, Partey, André Ayew, Jordan Ayew) had **well over 25 caps**, so every option satisfies the stem.
**Source:** https://en.wikipedia.org/wiki/Ghana_national_football_team
**Remedy:** Raise the threshold so only one player qualifies.

### Row 29892 — FAIL: non-unique / nonsensical answer
- "Which Ghana Premier League club is NOT a national team at the 2021 AFCON? → Asante Kotoko." All four options (Asante Kotoko, Hearts of Oak, Ashanti Gold, Medeama SC) are **clubs, not national teams**, so every option satisfies the (confused) stem.
**Source:** https://en.wikipedia.org/wiki/Ghana_Premier_League
**Remedy:** Reword; the premise makes all options correct.

## Ghana — CORRECTION: "Kudus plays for West Ham" (10 rows, batches 1–4)

**Web-verified:** Mohammed Kudus was an **Ajax** player at the 2022 World Cup (not West Ham), and he transferred from West Ham to **Tottenham Hotspur in July 2025** — so *every* "Kudus + West Ham" claim is wrong, whether it places him at West Ham during the 2022 World Cup (he was at Ajax) or states he currently plays for West Ham (he's now at Tottenham).
- **Rows 29292 (B1), 29524 (B2)** already FAIL (Ajax-in-2022). **Rows 29532 (B2), 29838, 29924, 29931 (B3)** were initially mis-passed and are now **removed from `QA_PASSED_ALL.md`** and counted FAIL (corrected totals: B2 185P/11F, B3 203P/13F). **Rows 29985, 29986, 29987, 30028 (B4)** likewise FAIL.
- (By contrast, "Thomas Partey plays for Arsenal" rows PASS: Arsenal was correct during the 2022 World Cup that those questions reference, even though Partey later moved to Villarreal in Aug 2025.)
**Source:** https://en.wikipedia.org/wiki/Mohammed_Kudus
**Remedy:** Use Kudus's 2022 club (Ajax) for World-Cup-era questions; update present-tense club to Tottenham.

## Ghana batch rows 29971–30240 — 20 FAIL (incl. 4 Kudus-West Ham above: 29985, 29986, 29987, 30028)

### Rows 30185, 30196, 30197, 30205, 30206, 30210 — FAIL: wrong result ("USA and Germany" in 2014)
- Each says Ghana **lost to USA and Germany** in the 2014 group stage. Ghana **drew Germany 2-2** and lost to **USA and Portugal**. 30185 ("which team did Ghana NOT lose to? → Portugal") is doubly wrong — they *did* lose to Portugal. 30206 even offers the correct "USA and Portugal" as an option.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_Group_G
**Remedy:** Replace "Germany" with "Portugal."

### Rows 29991, 29992, 29993, 29995 — FAIL: non-unique answer (all options are Ghana Premier League clubs)
- Each asks which club plays in the Ghana Premier League while listing **multiple GPL clubs** (Hearts of Oak, Asante Kotoko, Ashanti Gold, Great Olympics, Medeama SC, Accra Lions), so several options are valid. (Rows asking specifically for Asante Kotoko's *rival* — Hearts of Oak — are unique and PASS.)
**Source:** https://en.wikipedia.org/wiki/Ghana_Premier_League
**Remedy:** Use three non-GPL distractors.

### Row 30029 — FAIL: non-unique answer
- "Which Ghanaian star had over 25 caps by the 2022 World Cup? → Mohammed Kudus." Partey, Jordan Ayew and Daniel Amartey (all options) also had well over 25 caps.
**Source:** https://en.wikipedia.org/wiki/Ghana_national_football_team
**Remedy:** Raise the threshold so only one player qualifies.

### Rows 30108, 30130, 30192, 30193 — FAIL: self-referential answer
- Each asks which nation/team "**like Ghana**" did something and answers **Ghana** itself: 30108/30130 (won four AFCON titles), 30192 (matched Ghana's "2010 AFCON semi-final run" — which was actually the final), 30193 (reached the 2010 World Cup quarter-finals in South Africa — **Uruguay and Paraguay**, both options, also did).
**Source:** https://en.wikipedia.org/wiki/Ghana_national_football_team
**Remedy:** Make the answer a different team, not Ghana.

### Row 30123 — FAIL: wrong answer (Costa Rica did not qualify for 2010)
- "Which nation, like Ghana, qualified for the 2010, 2014 and 2022 World Cups? → Costa Rica." Costa Rica **failed to qualify for 2010** (lost the playoff to Uruguay). The other options — **Mexico, Uruguay and Portugal** — all qualified for 2010, 2014 and 2022, so the marked answer is wrong and the distractors are correct.
**Source:** https://en.wikipedia.org/wiki/Costa_Rica_at_the_FIFA_World_Cup
**Remedy:** Replace Costa Rica with a nation that missed one of those tournaments, or change the answer.

## Ghana batch rows 30241–30309 — 1 FAIL

### Row 30279 — FAIL: wrong dates (Chris Hughton's Ghana role)
- "Who was Ghana's technical adviser **during the 2014 World Cup cycle**? → Chris Hughton," explained as "Hughton served from 2014 to 2017." Hughton's Ghana involvement began in **2022** (technical adviser, then head coach 2023–2024); 2014–2017 was **Avram Grant's** tenure. (Rows placing Hughton as adviser at/around the 2022 World Cup PASS.)
**Source:** https://en.wikipedia.org/wiki/Chris_Hughton
**Remedy:** Re-anchor Hughton to 2022, or change the answer to Avram Grant for the 2014 cycle.

### Row 4283 — Belgium (easy) — FAIL
**Q:** After Belgium's 2018 group win, which UEFA player had their nation's best goalscoring record?
**Answer:** Romelu Lukaku
**Why it fails:** Non-unique: 'which UEFA player had their nation's best goalscoring record?' - Ronaldo (Portugal) and Lewandowski (Poland) were also their nations' all-time top scorers in 2018, so Lukaku is not the unique answer.
**Source:** https://en.wikipedia.org/wiki/List_of_men%27s_footballers_with_50_or_more_international_goals
**Remedy:** Anchor to Belgium ('which Belgian...') or replace the record-holder distractors.

### Row 4296 — Belgium (easy) — FAIL
**Q:** At Euro 2016, what score did Belgium lose by to Wales?
**Answer:** 03-Jan
**Why it fails:** Corrupted answer: '03-Jan' is an Excel-mangled '3-1' (Belgium lost 3-1 to Wales at Euro 2016). The correct score appears only as the corrupted cell.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2016
**Remedy:** Restore answer to '3-1'; flag for a dataset date-corruption sweep.

### Row 4304 — Belgium (easy) — FAIL
**Q:** At the 2018 FIFA World Cup, Belgium beat Brazil by what scoreline?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer: '02-Jan' is an Excel-mangled '2-1' (Belgium beat Brazil 2-1).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Restore answer to '2-1'; flag for a dataset sweep.

### Row 4305 — Belgium (easy) — FAIL
**Q:** At the 2018 World Cup, Belgium beat Brazil in the quarter-finals by what scoreline?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer: '02-Jan' is an Excel-mangled '2-1' (Belgium beat Brazil 2-1, 2018 QF).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Restore answer to '2-1'; flag for a dataset sweep.

### Row 4310 — Belgium (medium) — FAIL
**Q:** At the 2018 World Cup, how many goals did Belgium's Golden Generation score?
**Answer:** 9 goals
**Why it fails:** Wrong: Belgium scored 16 goals at the 2018 World Cup (the tournament's top-scoring team), not 9. '9' was only their group-stage tally.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Change answer/explanation to 16 goals.

### Row 4312 — Belgium (easy) — FAIL
**Q:** At the 2018 World Cup, which Belgian midfielder was a key starter?
**Answer:** Axel Witsel
**Why it fails:** Non-unique: De Bruyne was also a key starting midfielder in Belgium's 2018 double pivot (with Witsel), so 'Axel Witsel' is not the unique answer.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Remove De Bruyne as a distractor or specify the role.

### Row 4345 — Belgium (medium) — FAIL
**Q:** At which FIFA World Cup did Belgium win the Fair Play Award?
**Answer:** 2018 World Cup
**Why it fails:** Wrong: Spain won the 2018 World Cup Fair Play Award, not Belgium.
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup_awards
**Remedy:** Belgium did not win it in 2018 - drop or change to Spain.


### Row 4363 — Belgium (hard) — FAIL
**Q:** At which World Cup did Belgium reach the quarter-finals?
**Answer:** 2014 FIFA World Cup
**Why it fails:** Non-unique: Belgium also reached the quarter-finals in 2018 (and went further, to 3rd), so '2014' is not the unique answer to 'which World Cup did Belgium reach the QF'.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Reword to 'at which World Cup were the QF Belgium's ceiling' or drop 2018 as a distractor.

### Row 4371 — Belgium (medium) — FAIL
**Q:** At which World Cup was Belgian Eden Hazard named to the All-Star Team?
**Answer:** 2018 World Cup
**Why it fails:** False premise: FIFA did not name an official All-Star Team in 2018 (it was discontinued after 2010). Hazard won the Silver Ball and topped media teams-of-the-tournament, but 'All-Star Team' is not a real 2018 award.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Re-anchor to the Silver Ball (which Hazard did win) or drop.

### Row 4373 — Belgium (easy) — FAIL
**Q:** Before Belgium's 2018 World Cup run, which club had already won 35 Belgian titles?
**Answer:** Anderlecht
**Why it fails:** Wrong: Anderlecht has 34 Belgian league titles (their record 34th came in May 2017), not 35.
**Source:** https://en.wikipedia.org/wiki/R.S.C._Anderlecht
**Remedy:** Change to 34 titles.

### Row 4385 — Belgium (easy) — FAIL
**Q:** Belgium first reached FIFA #1 in 2015; what was their 2018 World Cup goal total?
**Answer:** 9 goals
**Why it fails:** Wrong: Belgium scored 16 goals at the 2018 WC (tournament top scorers), not 9. '9' was only their group-stage tally.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Change answer/explanation to 16 goals.

### Row 4389 — Belgium (medium) — FAIL
**Q:** Belgium held the FIFA number 1 ranking for a record duration starting in which year?
**Answer:** 2018
**Why it fails:** False premise: Belgium's 2018-2022 No.1 reign was NOT a record duration - Brazil and Spain both had longer continuous reigns at No.1.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop 'record', or reframe as 'a long reign starting in 2018'.

### Row 4433 — Belgium (easy) — FAIL
**Q:** Belgium's FA headquarters is in Brussels. Which city does NOT host another UEFA nation's FA?
**Answer:** Tubize
**Why it fails:** Incoherent / non-unique: all four options (Tubize, Genk, Mechelen, Waregem) are Belgian cities that do not host another UEFA nation's FA, so no option is uniquely correct.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Drop - the question's logic is broken.

### Row 4435 — Belgium (easy) — FAIL
**Q:** Belgium's Golden Generation held FIFA's top ranking but never won what?
**Answer:** A major trophy
**Why it fails:** Non-unique: Belgium also never won the World Cup, the Euros, or the Nations League, so all four options are equally valid 'never won' answers.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Drop or restrict to one specific trophy.

### Row 4439 — Belgium (easy) — FAIL
**Q:** During 2026 World Cup qualifying, Belgium's planned new national stadium faced what?
**Answer:** Delays
**Why it fails:** UNVERIFIED -> FAIL: a soft claim with no authoritative source tying a 'planned new national stadium facing delays' to the 2026 qualifying period (the Eurostadium project was abandoned years earlier).
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Drop, or replace with a sourced, dated stadium fact.

### Row 4442 — Belgium (medium) — FAIL
**Q:** During which Euro tournament was Belgium's record FIFA number 1 streak ongoing?
**Answer:** Euro 2020
**Why it fails:** False/unverified: Belgium's No.1 reign was the 3rd-longest continuous run (Brazil and Spain longer), not a 'record', and the specific 1,735-day figure is unsupported.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop the 'record 1,735-day' framing.

### Row 4449 — Belgium (easy) — FAIL
**Q:** For 2026 World Cup qualifiers, which stadium hosts all Belgian home matches?
**Answer:** King Baudouin Stadium
**Why it fails:** Non-unique: 'King Baudouin Stadium' and 'Stade Roi Baudouin' are the same venue (English vs French name), so two options are identical and correct.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Replace the duplicate distractor with a genuinely different stadium.


### Row 4458 — Belgium (easy) — FAIL
**Q:** For the 2010 World Cup, Belgium finished behind which two nations?
**Answer:** Spain and Türkiye
**Why it fails:** 2010 WC qualifying: Belgium finished 4th in UEFA Group 5, behind Spain, Bosnia & Herzegovina AND Turkey - not just Spain and Turkiye (Bosnia finished 2nd, above Belgium).
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_5
**Remedy:** Reword to include Bosnia, or ask a different question.

### Row 4468 — Belgium (medium) — FAIL
**Q:** From 2014 to 2022, how many consecutive major tournaments did Belgium qualify for?
**Answer:** Four consecutive tournaments
**Why it fails:** Wrong count: Belgium qualified for FIVE consecutive major tournaments 2014-2022 (2014 WC, Euro 2016, 2018 WC, Euro 2020, 2022 WC), not four - the dataset omits Euro 2020.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_UEFA_European_Championship
**Remedy:** Change answer to five.

### Row 4480 — Belgium (medium) — FAIL
**Q:** From which year did Belgium's record FIFA #1 ranking begin?
**Answer:** 2018
**Why it fails:** Explanation wrong: Belgium's No.1 reign was NOT a 'record 1,735-day run' - Brazil and Spain had longer continuous reigns at No.1.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop the 'record 1,735-day' framing (the start year 2018 is fine).

### Row 4481 — Belgium (medium) — FAIL
**Q:** From which year was Thibaut Courtois Belgium's first-choice goalkeeper?
**Answer:** 2014
**Why it fails:** Wrong: Courtois was Belgium's first-choice GK from ~2011-2012 (he played every minute of the 2014 qualifying campaign in 2012-13), not 'from 2014' - '2012' is the better option.
**Source:** https://en.wikipedia.org/wiki/Thibaut_Courtois
**Remedy:** Change answer to 2012.

### Row 4486 — Belgium (medium) — FAIL
**Q:** How many caps did Belgian defender Jan Vertonghen retire with in 2024?
**Answer:** 154 caps
**Why it fails:** Wrong: Vertonghen retired in 2024 with 157 caps (Belgium's most-capped player), not 154.
**Source:** https://en.wikipedia.org/wiki/Jan_Vertonghen
**Remedy:** Change answer to 157.

### Row 4491 — Belgium (medium) — FAIL
**Q:** How many consecutive FIFA World Cups did Belgium's Golden Generation qualify for?
**Answer:** Four tournaments
**Why it fails:** Wrong count: it was FIVE consecutive major tournaments (2014-2022), not four - Euro 2020 is omitted.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_UEFA_European_Championship
**Remedy:** Change answer to five.

### Row 4492 — Belgium (medium) — FAIL
**Q:** How many consecutive major tournaments did Belgium qualify for from 2014 to 2022?
**Answer:** Four
**Why it fails:** Wrong count: Belgium qualified for FIVE consecutive major tournaments 2014-2022, not four (Euro 2020 omitted).
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_UEFA_European_Championship
**Remedy:** Change answer to five.

### Row 4493 — Belgium (medium) — FAIL
**Q:** How many consecutive major tournaments did Belgium's Golden Generation qualify for from 2014?
**Answer:** Four tournaments
**Why it fails:** Wrong count: five consecutive major tournaments from 2014 (incl. Euro 2020), not four.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_UEFA_European_Championship
**Remedy:** Change answer to five.

### Row 4495 — Belgium (medium) — FAIL
**Q:** How many goals did Belgium score at the 2018 FIFA World Cup?
**Answer:** 9 goals
**Why it fails:** Wrong: Belgium scored 16 goals at the 2018 WC (the tournament's top-scoring team), not 9.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Change answer to 16.

### Row 4496 — Belgium (medium) — FAIL
**Q:** How many goals did Belgium score in 7 matches at the 2018 FIFA World Cup?
**Answer:** 9 goals
**Why it fails:** Wrong: Belgium scored 16 goals in 7 matches at the 2018 WC, not 9.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Change answer to 16.

### Row 4497 — Belgium (medium) — FAIL
**Q:** How many goals did Belgium score in the 2018 World Cup?
**Answer:** 9 goals
**Why it fails:** Wrong: Belgium scored 16 goals at the 2018 WC, not 9.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Change answer to 16.

### Row 4509 — Belgium (easy) — FAIL
**Q:** In 2010 World Cup qualifying, which two teams finished above Belgium?
**Answer:** Spain and Türkiye
**Why it fails:** 2010 qualifying: THREE teams finished above Belgium (Spain, Bosnia & Herzegovina, Turkey), not two - the answer omits Bosnia.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_5
**Remedy:** Reword - Belgium finished 4th behind three nations.

### Row 4512 — Belgium (easy) — FAIL
**Q:** In 2018, Belgium's 9 goals in 7 matches gave them what goals-per-game average?
**Answer:** 1.29
**Why it fails:** False premise: Belgium scored 16 goals (not 9) in 7 matches at 2018, so the average was ~2.29 per game, not 1.29.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Recompute from 16 goals (~2.29 gpg).

### Row 4516 — Belgium (medium) — FAIL
**Q:** In a 2018 World Cup group stage match, which Belgian goalkeeper did NOT make match-winning saves?
**Answer:** Simon Mignolet
**Why it fails:** Non-unique negative: Mignolet, Casteels AND Sels all did NOT make match-winning saves (only Courtois did), so 'Simon Mignolet' is not the unique answer.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Drop - three options satisfy the 'did NOT' condition.


### Row 4548 — Belgium (medium) — FAIL
**Q:** In what World Cup tournament did Belgium score 9 goals in 7 matches?
**Answer:** 2018 World Cup
**Why it fails:** Wrong: Belgium scored 16 goals at the 2018 WC (tournament top scorers), not 9.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Change answer to 16.

### Row 4549 — Belgium (medium) — FAIL
**Q:** In what year did Belgium's Eden Hazard retire from international football?
**Answer:** 2023
**Why it fails:** Wrong: Hazard retired from INTERNATIONAL football in December 2022 (after the 2022 WC), not 2023. His 2023 retirement was from all football. '2022' is the correct option.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Change answer to 2022 for international retirement.

### Row 4567 — Belgium (medium) — FAIL
**Q:** In which FIFA World Cup did the Belgian team score 9 goals across 7 matches?
**Answer:** 2018 World Cup
**Why it fails:** Wrong: Belgium scored 16 goals in 7 matches at the 2018 WC, not 9.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Change answer to 16.

### Row 4595 — Belgium (medium) — FAIL
**Q:** In which World Cup did Belgium score 9 goals in 7 matches?
**Answer:** 2018 World Cup
**Why it fails:** Wrong: Belgium scored 16 goals in 7 matches at the 2018 WC, not 9.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Change answer to 16.

### Row 4596 — Belgium (medium) — FAIL
**Q:** In which World Cup did Belgium score 9 goals?
**Answer:** 2018 World Cup
**Why it fails:** Wrong: Belgium scored 16 goals at the 2018 WC, not 9.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Change answer to 16.

### Row 4597 — Belgium (medium) — FAIL
**Q:** In which World Cup did Belgium score nine goals across seven matches?
**Answer:** 2018 World Cup
**Why it fails:** Wrong: Belgium scored 16 goals in 7 matches at the 2018 WC, not 9.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Change answer to 16.

### Row 4605 — Belgium (hard) — FAIL
**Q:** In which World Cup group stage did Belgium's 3-2 comeback against Japan occur?
**Answer:** 2018 World Cup
**Why it fails:** False premise: Belgium's 3-2 comeback v Japan occurred in the Round of 16, NOT the group stage.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Reword - it was the R16, not the group stage.

### Row 4626 — Belgium (medium) — FAIL
**Q:** In which year did Belgium lose 2-1 to Italy in a Euro quarter-final?
**Answer:** 2020
**Why it fails:** Wrong year: the Belgium-Italy Euro 2020 QF was played on 2 July 2021, so the year was 2021, not 2020 ('2021' is an option, and row 4638 correctly answers 2021).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Change answer to 2021.

### Row 4631 — Belgium (medium) — FAIL
**Q:** In which year did Belgium qualify for the 2014 FIFA World Cup?
**Answer:** 2014
**Why it fails:** Wrong: Belgium sealed 2014 World Cup qualification in October 2013, not 2014.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Change answer to 2013.

### Row 4634 — Belgium (medium) — FAIL
**Q:** In which year did Belgium's record 1,735-day FIFA number 1 ranking begin?
**Answer:** 2018
**Why it fails:** Explanation/premise wrong: Belgium's No.1 run was not a 'record 1,735-day' reign - Brazil and Spain had longer continuous reigns at No.1.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop the 'record 1,735-day' framing (start year 2018 is fine).


### Row 4644 — Belgium (medium) — FAIL
**Q:** Under which coach did Belgium's 2026 World Cup qualification succeed?
**Answer:** Domenico Tedesco
**Why it fails:** False: Belgium's 2026 WC qualifying was led by Rudi Garcia (appointed Jan 2025), not Tedesco (sacked 17 Jan 2025).
**Source:** https://en.wikipedia.org/wiki/List_of_Belgium_national_football_team_managers
**Remedy:** Change manager to Rudi Garcia.

### Row 4646 — Belgium (easy) — FAIL
**Q:** Under which manager did Belgium qualify for the 2026 World Cup?
**Answer:** Domenico Tedesco
**Why it fails:** False: the 2026 qualifying campaign was under Rudi Garcia, not Tedesco (sacked Jan 2025).
**Source:** https://en.wikipedia.org/wiki/List_of_Belgium_national_football_team_managers
**Remedy:** Change manager to Rudi Garcia.

### Row 4657 — Belgium (easy) — FAIL
**Q:** What was Belgium's final score after trailing Japan 2-0 in the 2018 World Cup round of 16?
**Answer:** 03-Feb
**Why it fails:** Corrupted answer: '03-Feb' is an Excel-mangled '3-2' (Belgium beat Japan 3-2).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Restore '3-2'.

### Row 4658 — Belgium (easy) — FAIL
**Q:** What was Belgium's final score in their 2018 World Cup comeback win vs Japan?
**Answer:** 03-Feb
**Why it fails:** Corrupted answer: '03-Feb' = '3-2' (beat Japan).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Restore '3-2'.

### Row 4664 — Belgium (easy) — FAIL
**Q:** What was the final score in Belgium's 2018 World Cup comeback win against Japan?
**Answer:** 03-Feb
**Why it fails:** Corrupted answer: '03-Feb' = '3-2' (beat Japan).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Restore '3-2'.

### Row 4666 — Belgium (easy) — FAIL
**Q:** What was the final score when Belgium beat Japan at the 2018 World Cup?
**Answer:** 03-Feb
**Why it fails:** Corrupted answer: '03-Feb' = '3-2' (beat Japan).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Restore '3-2'.

### Row 4671 — Belgium (medium) — FAIL
**Q:** What was the score when Belgium beat Brazil in the 2018 World Cup quarter-final?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer: '02-Jan' = '2-1' (beat Brazil).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Restore '2-1'.

### Row 4677 — Belgium (medium) — FAIL
**Q:** What was the score when Belgium lost to Wales at Euro 2016?
**Answer:** 03-Jan
**Why it fails:** Corrupted answer: '03-Jan' = '3-1' (lost to Wales).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2016
**Remedy:** Restore '3-1'.

### Row 4694 — Belgium (medium) — FAIL
**Q:** When did Belgium begin their record 1,735-day streak as FIFA's number-one ranked team?
**Answer:** Sep-18
**Why it fails:** 'record 1,735-day' streak claim false: Belgium's No.1 reign was not a record (Brazil & Spain held it longer); Sep 2018-Mar 2022 is also ~1,280 days, not 1,735.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop the 'record 1,735-day' framing.

### Row 4714 — Belgium (medium) — FAIL
**Q:** When did Belgium lose 2-1 to Italy in the Euro quarter-finals?
**Answer:** 2020
**Why it fails:** Wrong year: the Belgium-Italy Euro 2020 QF was played on 2 July 2021, so the year was 2021, not 2020 (cf. row 4638).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Change answer to 2021.

### Row 4721 — Belgium (medium) — FAIL
**Q:** When did Belgium qualify for the 2026 World Cup under Domenico Tedesco?
**Answer:** 2026
**Why it fails:** False premise: Belgium's 2026 qualifying campaign was under Rudi Garcia, not Tedesco (sacked Jan 2025).
**Source:** https://en.wikipedia.org/wiki/List_of_Belgium_national_football_team_managers
**Remedy:** Change manager to Rudi Garcia.

### Row 4725 — Belgium (medium) — FAIL
**Q:** When did Belgium reach the quarter-finals of the FIFA World Cup?
**Answer:** 2014
**Why it fails:** Non-unique: Belgium also reached the QF in 2018 (and went to 3rd), so '2014' is not the unique answer.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Reword or drop the 2018 distractor.

### Row 4729 — Belgium (medium) — FAIL
**Q:** When did Belgium start its record FIFA number 1 streak?
**Answer:** 2018
**Why it fails:** 'record 1,735-day' run claim false: Belgium's No.1 reign was not a record (Brazil & Spain longer).
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop the 'record 1,735-day' framing.

### Row 4730 — Belgium (medium) — FAIL
**Q:** When did Belgium start their record FIFA #1 ranking streak?
**Answer:** 2018
**Why it fails:** 'record FIFA #1 streak' false: Belgium's reign was not a record (Brazil & Spain longer).
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop 'record'.

### Row 4734 — Belgium (medium) — FAIL
**Q:** When did Belgium win the FIFA Fair Play Award?
**Answer:** 2018 World Cup
**Why it fails:** Wrong: Spain won the 2018 World Cup Fair Play Award, not Belgium.
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup_awards
**Remedy:** Belgium did not win it in 2018.


### Row 4748 — Belgium (medium) — FAIL
**Q:** When did Belgium's men's team first reach the FIFA number 1 ranking?
**Answer:** 2018
**Why it fails:** Wrong: Belgium first reached FIFA No.1 in November 2015, not 2018 (the correct year is not even an option).
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Change answer to 2015.

### Row 4753 — Belgium (medium) — FAIL
**Q:** When did Belgium's number 1 ranked 'Golden Generation' fail to win a World Cup?
**Answer:** 2018 World Cup
**Why it fails:** Non-unique/imprecise: Belgium failed to win the WC at 2010/2014/2022 too, and they were NOT ranked No.1 during the 2018 WC (3rd, rising to No.1 that September).
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Reword - premise and answer aren't unique.

### Row 4754 — Belgium (medium) — FAIL
**Q:** When did Belgium's record 1,735-day FIFA number 1 ranking begin?
**Answer:** Sep-18
**Why it fails:** 'record 1,735-day' ranking claim false - Belgium's No.1 reign was not a record (Brazil & Spain longer).
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop the 'record 1,735-day' framing (Sep 2018 start is fine).

### Row 4755 — Belgium (medium) — FAIL
**Q:** When did Belgium's record 1,735-day FIFA number 1 ranking end?
**Answer:** 2022
**Why it fails:** 'record 1,735-day' claim false - not a record (Brazil & Spain held No.1 longer).
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop the 'record 1,735-day' framing.

### Row 4756 — Belgium (medium) — FAIL
**Q:** When did Belgium's record 1,735-day run as FIFA number 1 end?
**Answer:** Mar-22
**Why it fails:** 'record 1,735-day' claim false - not a record (Brazil & Spain longer); end Mar 2022 is otherwise correct.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop the 'record 1,735-day' framing.

### Row 4757 — Belgium (medium) — FAIL
**Q:** When did Belgium's record FIFA number 1 ranking start?
**Answer:** 2018
**Why it fails:** 'record FIFA No.1 ranking' claim false - Belgium's reign was not a record (Brazil & Spain longer).
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop the 'record 1,735-day' framing.

### Row 4781 — Belgium (easy) — FAIL
**Q:** Where did Belgium host all their 2022 World Cup qualifiers?
**Answer:** King Baudouin Stadium
**Why it fails:** Non-unique: 'King Baudouin Stadium' and 'Stade Roi Baudouin' are the same venue (English vs French name), so two options are identical and correct.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Replace the duplicate distractor.

### Row 4810 — Belgium (easy) — FAIL
**Q:** Which 2014 World Cup rival did Belgium NOT face in a quarter-final?
**Answer:** Italy
**Why it fails:** Non-unique negative: Belgium's only 2014 QF opponent was Argentina, so they did NOT face Italy, Brazil OR France in a QF - three options satisfy 'not faced'.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Drop - multiple options qualify.

### Row 4811 — Belgium (easy) — FAIL
**Q:** Which 2018 World Cup award did the Belgian national team win?
**Answer:** FIFA Fair Play Award
**Why it fails:** Wrong: Spain won the 2018 Fair Play Award, not Belgium. Belgium DID win the 2018 Golden Glove (Courtois), which is a distractor here - so the answer is also non-unique.
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup_awards
**Remedy:** Change answer to the Golden Glove (Courtois).

### Row 4812 — Belgium (easy) — FAIL
**Q:** Which 2018 World Cup comeback is often compared to Belgium's 3-2 win over Japan?
**Answer:** Belgium vs Japan
**Why it fails:** Self-referential: the question asks which comeback is compared to Belgium's win over Japan, and the answer names the Belgium-Japan game itself.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Replace with a genuinely comparable comeback, or drop.

### Row 4819 — Belgium (easy) — FAIL
**Q:** Which 2018 World Cup match was NOT a famous comeback win for Belgium?
**Answer:** Belgium vs England
**Why it fails:** Non-unique negative: the Brazil win (2-1) and the France game (1-0 loss) were also NOT 'famous comeback wins' (only Japan was a comeback), so 'Belgium vs England' is not unique.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Drop - multiple options qualify.


### Row 4843 — Belgium (easy) — FAIL
**Q:** Which Belgian association is responsible for organizing World Cup qualifiers from Brussels?
**Answer:** The Belgian Football Association
**Why it fails:** Non-unique: all four options ('Belgian Football Association', 'Royal Belgian FA', 'Belgian FA', "Belgium's FA") name the same organisation.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Replace the distractors with genuinely different bodies.

### Row 4844 — Belgium (easy) — FAIL
**Q:** Which Belgian association organizes World Cup logistics from its Brussels HQ?
**Answer:** Belgian Football Association
**Why it fails:** Non-unique: 'Belgian Football Association' and 'Royal Belgian FA' are the same organisation, so two options are correct.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Replace the duplicate.

### Row 4845 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker debuted in 2008 and retired in 2024?
**Answer:** Eden Hazard
**Why it fails:** Wrong: Hazard retired from international football in Dec 2022 (all football in 2023), not 2024 - the '2024' detail is false (Vertonghen, a defender, retired in 2024).
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Fix the retirement year.

### Row 4851 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker had over 100 caps and 20+ goals by 2022?
**Answer:** Dries Mertens
**Why it fails:** Non-unique: Hazard (126 caps / 33 goals) also had 100+ caps and 20+ goals by 2022.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten the criteria.

### Row 4854 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker played at both the 2018 and 2022 World Cups?
**Answer:** Yannick Carrasco
**Why it fails:** Non-unique: Hazard and Mertens also played at both the 2018 and 2022 WCs.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - several attackers fit.

### Row 4855 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker played at Euro 2016 and two World Cups?
**Answer:** Yannick Carrasco
**Why it fails:** Non-unique: Mertens also played at Euro 2016 and the 2018 & 2022 WCs.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - Mertens also fits.

### Row 4856 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker played at Euro 2016, the 2018 World Cup, and the 2022 World Cup?
**Answer:** Yannick Carrasco
**Why it fails:** Non-unique: Mertens also featured at Euro 2016, the 2018 WC and the 2022 WC.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - Mertens also fits.

### Row 4858 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker played at the 2018 and 2022 FIFA World Cups?
**Answer:** Yannick Carrasco
**Why it fails:** Non-unique: Mertens also played at both the 2018 and 2022 WCs.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - Mertens also fits.

### Row 4860 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker played in 2018 World Cup qualifiers from 2013 onward?
**Answer:** Dries Mertens
**Why it fails:** Non-unique: Hazard, Lukaku and De Bruyne were also key attackers in the 2018 qualifiers from 2013.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten the criteria.

### Row 4862 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker retired from international football in 2024?
**Answer:** Eden Hazard
**Why it fails:** Wrong: Hazard retired from international football in Dec 2022, not 2024 (Vertonghen retired in 2024).
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Fix the year to 2022.

### Row 4863 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker retired from internationals in 2024 after 126 caps?
**Answer:** Eden Hazard
**Why it fails:** Wrong: Hazard retired from internationals in Dec 2022, not 2024.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Fix the year to 2022.

### Row 4866 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker retired in 2024 after earning 126 caps?
**Answer:** Eden Hazard
**Why it fails:** Wrong: Hazard retired from international football in Dec 2022, not 2024.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Fix the year to 2022.

### Row 4867 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker retired in 2024 after playing from 2008?
**Answer:** Eden Hazard
**Why it fails:** Wrong: Hazard retired in 2022 (internationals)/2023 (all football), not 2024.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Fix the year.

### Row 4868 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker retired in 2024 with 126 caps?
**Answer:** Eden Hazard
**Why it fails:** Wrong: Hazard retired from internationals in Dec 2022, not 2024.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Fix the year to 2022.

### Row 4871 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker was a key creative force from 2008 to 2024?
**Answer:** Eden Hazard
**Why it fails:** Wrong span: Hazard's international career ran 2008-2022 (retired Dec 2022), not 'to 2024'.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Fix the end year.

### Row 4872 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker was a key figure in their 2018 World Cup qualifying campaign?
**Answer:** Dries Mertens
**Why it fails:** Non-unique: Hazard, Lukaku and De Bruyne were all key figures in the 2018 qualifying campaign.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten the criteria.

### Row 4876 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker was in the squad for the 2022 FIFA World Cup?
**Answer:** Dries Mertens
**Why it fails:** Non-unique: Hazard and Vertonghen were also in the 2022 WC squad.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - several players fit.

### Row 4877 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker was key from 2013 to 2022?
**Answer:** Dries Mertens
**Why it fails:** Non-unique: Hazard, Lukaku and De Bruyne were also key attackers from 2013 to 2022.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten the criteria.

### Row 4878 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker was not at the 2022 World Cup?
**Answer:** Eden Hazard
**Why it fails:** False premise: Hazard DID play at the 2022 WC (he retired Dec 2022, after it). All four options were at the 2022 WC, so none was 'not at' it.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** The premise is false - all options played in 2022.

### Row 4879 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker was selected for the 2018 FIFA World Cup squad?
**Answer:** Yannick Carrasco
**Why it fails:** Non-unique: Mertens was also in Belgium's 2018 WC squad.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - Mertens also fits.

### Row 4881 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker, key from 2013 to 2022, earned over 100 caps?
**Answer:** Dries Mertens
**Why it fails:** Non-unique: Hazard (126 caps) was also a key attacker 2013-2022 with 100+ caps.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten the criteria.

### Row 4882 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker, with over 70 caps, played at the 2018 World Cup?
**Answer:** Yannick Carrasco
**Why it fails:** Non-unique: Mertens (100+ caps) also had over 70 caps and played at the 2018 WC.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten the criteria.

### Row 4883 — Belgium (easy) — FAIL
**Q:** Which Belgian attacker's international career spanned from 2008 to 2024?
**Answer:** Eden Hazard
**Why it fails:** Wrong span: Hazard's international career ran 2008-2022 (retired Dec 2022), not 2008-2024.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Fix the end year.

### Row 4897 — Belgium (easy) — FAIL
**Q:** Which Belgian club had 35 domestic league titles by 2024?
**Answer:** Anderlecht
**Why it fails:** Wrong: Anderlecht has 34 Belgian league titles (record 34th in 2017), not 35.
**Source:** https://en.wikipedia.org/wiki/R.S.C._Anderlecht
**Remedy:** Change to 34.

### Row 4898 — Belgium (easy) — FAIL
**Q:** Which Belgian club had 35 domestic league titles by the 2022 World Cup?
**Answer:** Anderlecht
**Why it fails:** Wrong: Anderlecht has 34 titles, not 35.
**Source:** https://en.wikipedia.org/wiki/R.S.C._Anderlecht
**Remedy:** Change to 34.

### Row 4899 — Belgium (easy) — FAIL
**Q:** Which Belgian club had 35 domestic titles before the 2018 World Cup?
**Answer:** Anderlecht
**Why it fails:** Wrong: Anderlecht had 34 titles (their 34th came in 2017), not 35.
**Source:** https://en.wikipedia.org/wiki/R.S.C._Anderlecht
**Remedy:** Change to 34.

### Row 4901 — Belgium (easy) — FAIL
**Q:** Which Belgian club had 35 league titles before the 2022 World Cup?
**Answer:** Anderlecht
**Why it fails:** Wrong: Anderlecht has 34 titles, not 35.
**Source:** https://en.wikipedia.org/wiki/R.S.C._Anderlecht
**Remedy:** Change to 34.

### Row 4905 — Belgium (easy) — FAIL
**Q:** Which Belgian club has 35 league titles, the most in their history?
**Answer:** Anderlecht
**Why it fails:** Wrong: Anderlecht has 34 league titles, not 35.
**Source:** https://en.wikipedia.org/wiki/R.S.C._Anderlecht
**Remedy:** Change to 34.

### Row 4906 — Belgium (easy) — FAIL
**Q:** Which Belgian club has won 35 domestic league titles?
**Answer:** Anderlecht
**Why it fails:** Wrong: Anderlecht has won 34 league titles, not 35.
**Source:** https://en.wikipedia.org/wiki/R.S.C._Anderlecht
**Remedy:** Change to 34.


### Row 4944 — Belgium (easy) — FAIL
**Q:** Which Belgian defender retired after the 2024 World Cup qualifiers with 154 caps?
**Answer:** Jan Vertonghen
**Why it fails:** False premise: there were no '2024 World Cup qualifiers' (no 2024 WC); Vertonghen retired after Euro 2024 with 157 caps, not 154.
**Source:** https://en.wikipedia.org/wiki/Jan_Vertonghen
**Remedy:** Fix the framing (Euro 2024 / 2026 qualifiers) and the cap count (157).

### Row 4960 — Belgium (easy) — FAIL
**Q:** Which Belgian earned a spot in the 2018 World Cup All-Star Team?
**Answer:** Eden Hazard
**Why it fails:** False premise: FIFA named no official All-Star Team in 2018 (discontinued after 2010). Hazard won the Silver Ball.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Re-anchor to the Silver Ball or drop.

### Row 4964 — Belgium (easy) — FAIL
**Q:** Which Belgian forward debuted as a key player at Euro 2024?
**Answer:** Leandro Trossard
**Why it fails:** Non-unique: Doku was also a key forward for Belgium at Euro 2024.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024
**Remedy:** Tighten - Doku also fits.

### Row 5016 — Belgium (medium) — FAIL
**Q:** Which Belgian manager oversaw their 2026 World Cup qualification?
**Answer:** Domenico Tedesco
**Why it fails:** False: Belgium's 2026 qualifying was under Rudi Garcia (appointed Jan 2025), not Tedesco (sacked 17 Jan 2025).
**Source:** https://en.wikipedia.org/wiki/List_of_Belgium_national_football_team_managers
**Remedy:** Change to Rudi Garcia.

### Row 5017 — Belgium (easy) — FAIL
**Q:** Which Belgian manager qualified them for the 2026 World Cup?
**Answer:** Domenico Tedesco
**Why it fails:** False: the 2026 qualifying campaign was under Rudi Garcia, not Tedesco (sacked Jan 2025).
**Source:** https://en.wikipedia.org/wiki/List_of_Belgium_national_football_team_managers
**Remedy:** Change to Rudi Garcia.

### Row 5024 — Belgium (easy) — FAIL
**Q:** Which Belgian midfielder emerged as key for the post-Golden Generation era at the 2026 World Cup?
**Answer:** Amadou Onana
**Why it fails:** Non-unique: Youri Tielemans is also a key midfielder for Belgium's post-Golden-Generation era.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - Tielemans also fits.

### Row 5036 — Belgium (easy) — FAIL
**Q:** Which Belgian midfielder is central to their 2026 World Cup qualifying rebuild?
**Answer:** Amadou Onana
**Why it fails:** Non-unique: Tielemans is also central to Belgium's 2026 midfield.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - Tielemans also fits.

### Row 5038 — Belgium (easy) — FAIL
**Q:** Which Belgian midfielder is central to their 2026 World Cup transition plans?
**Answer:** Amadou Onana
**Why it fails:** Non-unique: Tielemans is also central to Belgium's 2026 transition.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - Tielemans also fits.

### Row 5039 — Belgium (easy) — FAIL
**Q:** Which Belgian midfielder is central to their post-Golden Generation future?
**Answer:** Amadou Onana
**Why it fails:** Non-unique: Tielemans is also central to Belgium's post-Golden-Generation midfield.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - Tielemans also fits.

### Row 5040 — Belgium (easy) — FAIL
**Q:** Which Belgian midfielder is central to their squad after their Golden Generation?
**Answer:** Amadou Onana
**Why it fails:** Non-unique: Tielemans is also central to Belgium's post-Golden-Generation squad.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - Tielemans also fits.


### Row 5041 — Belgium (easy) — FAIL
**Q:** Which Belgian midfielder is considered key for the post-Golden Generation era?
**Answer:** Amadou Onana
**Why it fails:** Non-unique: Tielemans is also a key midfielder for Belgium's post-Golden-Generation era.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - Tielemans also fits.

### Row 5044 — Belgium (easy) — FAIL
**Q:** Which Belgian midfielder is key for the post-2022 World Cup era?
**Answer:** Amadou Onana
**Why it fails:** Non-unique: Tielemans is also a key post-2022 midfielder for Belgium.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - Tielemans also fits.

### Row 5049 — Belgium (easy) — FAIL
**Q:** Which Belgian midfielder is key for their post-Golden Generation era?
**Answer:** Amadou Onana
**Why it fails:** Non-unique: Tielemans is also a key post-Golden-Generation midfielder.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - Tielemans also fits.

### Row 5052 — Belgium (easy) — FAIL
**Q:** Which Belgian midfielder played at both the 2014 and 2022 World Cups?
**Answer:** Axel Witsel
**Why it fails:** Non-unique: De Bruyne also played at both the 2014 and 2022 World Cups.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - De Bruyne also fits.

### Row 5054 — Belgium (easy) — FAIL
**Q:** Which Belgian midfielder was a key part of their 2022 World Cup squad?
**Answer:** Amadou Onana
**Why it fails:** Non-unique: De Bruyne and Witsel were the key midfielders in Belgium's 2022 WC squad.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - others fit better.

### Row 5057 — Belgium (easy) — FAIL
**Q:** Which Belgian midfielder was not a key creative fulcrum at the 2018 World Cup?
**Answer:** Amadou Onana
**Why it fails:** Non-unique negative: Tielemans and Thorgan Hazard were also NOT the 2018 creative fulcrum (only De Bruyne was).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Drop - multiple options qualify.

### Row 5079 — Belgium (easy) — FAIL
**Q:** Which Belgian player debuted for the national team after 2008, a product of the 2000s academy investment?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: both De Bruyne (2010) and Lukaku (2010) debuted after 2008 as academy products.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - Lukaku also fits.

### Row 5083 — Belgium (easy) — FAIL
**Q:** Which Belgian player did NOT win the Silver Ball at the 2018 World Cup?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique negative: De Bruyne, Lukaku AND Courtois all did NOT win the 2018 Silver Ball (only Hazard did).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Drop - multiple options qualify.

### Row 5088 — Belgium (easy) — FAIL
**Q:** Which Belgian player ended his international career in 2023 with 126 caps?
**Answer:** Eden Hazard
**Why it fails:** Wrong: Hazard's international career ended in Dec 2022, not 2023 (his all-football retirement was 2023). 126 caps is correct.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Fix to 2022 for the international retirement.

### Row 5090 — Belgium (easy) — FAIL
**Q:** Which Belgian player featured in their 2014-2022 tournament streak?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Courtois, Hazard and Lukaku also featured across 2014-2022 (and the streak was five tournaments, not four).
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - all options fit.

### Row 5104 — Belgium (medium) — FAIL
**Q:** Which Belgian player has received multiple Ballon d'Or nominations?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard also received multiple Ballon d'Or nominations.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.

### Row 5124 — Belgium (easy) — FAIL
**Q:** Which Belgian player is NOT their nation's all-time top scorer?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique negative: De Bruyne, Hazard AND Vertonghen are all NOT Belgium's top scorer (only Lukaku is).
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Drop - multiple options qualify.


### Row 5143 — Belgium (easy) — FAIL
**Q:** Which Belgian player made the 2018 All-Star Team and won the Silver Ball?
**Answer:** Eden Hazard
**Why it fails:** False premise: FIFA named no official 2018 All-Star Team (discontinued after 2010). Hazard won the Silver Ball.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Drop the All-Star Team claim.

### Row 5144 — Belgium (easy) — FAIL
**Q:** Which Belgian player made the 2018 World Cup All-Star Team?
**Answer:** Eden Hazard
**Why it fails:** False premise: no official 2018 World Cup All-Star Team existed.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Drop or re-anchor to the Silver Ball.

### Row 5152 — Belgium (easy) — FAIL
**Q:** Which Belgian player retired from international football in 2023 with 126 caps?
**Answer:** Eden Hazard
**Why it fails:** Wrong: Hazard retired from international football in Dec 2022, not 2023 (his all-football retirement was 2023). 126 caps is correct.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Fix to 2022.

### Row 5153 — Belgium (easy) — FAIL
**Q:** Which Belgian player retired from international football in 2023?
**Answer:** Eden Hazard
**Why it fails:** Wrong: Hazard retired from international football in Dec 2022, not 2023.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Fix to 2022.

### Row 5163 — Belgium (easy) — FAIL
**Q:** Which Belgian player scored a hat-trick at the 2018 World Cup?
**Answer:** Romelu Lukaku
**Why it fails:** Wrong: Lukaku did NOT score a hat-trick at the 2018 WC - he scored braces v Panama (2) and Tunisia (2), 4 total, no single-match hat-trick.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Drop the hat-trick claim.

### Row 5166 — Belgium (easy) — FAIL
**Q:** Which Belgian player scored against Japan at the 2018 World Cup?
**Answer:** Divock Origi
**Why it fails:** Wrong: Origi did not score v Japan in 2018 - Belgium's scorers were Vertonghen, Fellaini and Chadli.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Change to Chadli (an option).

### Row 5170 — Belgium (easy) — FAIL
**Q:** Which Belgian player scored in their 2018 World Cup round of 16 win over Japan?
**Answer:** Divock Origi
**Why it fails:** Wrong: Origi did not score v Japan in 2018 - the scorers were Vertonghen, Fellaini and Chadli.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Change to Chadli (an option).

### Row 5194 — Belgium (easy) — FAIL
**Q:** Which Belgian player was a key part of their Golden Generation from 2014 to 2022?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard, Courtois and Lukaku were also key Golden-Generation players 2014-2022 (and the streak was five tournaments, not four).
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - all options fit.

### Row 5199 — Belgium (easy) — FAIL
**Q:** Which Belgian player was in the 2018 World Cup All-Star Team and won the Silver Ball?
**Answer:** Eden Hazard
**Why it fails:** False premise: no official 2018 All-Star Team (Hazard won the Silver Ball).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Drop the All-Star Team claim.

### Row 5204 — Belgium (easy) — FAIL
**Q:** Which Belgian player was named to the All-Star Team at the 2018 FIFA World Cup?
**Answer:** Eden Hazard
**Why it fails:** False premise: no official 2018 World Cup All-Star Team existed.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Drop or re-anchor.

### Row 5207 — Belgium (easy) — FAIL
**Q:** Which Belgian player was selected for the 2018 World Cup All-Star Team?
**Answer:** Eden Hazard
**Why it fails:** False premise: no official 2018 World Cup All-Star Team existed.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Drop or re-anchor.

### Row 5215 — Belgium (easy) — FAIL
**Q:** Which Belgian player won both the Silver Ball and made the All-Star Team at the 2018 FIFA World Cup?
**Answer:** Eden Hazard
**Why it fails:** False premise: no official 2018 All-Star Team (the Silver Ball is real, the All-Star Team is not).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Drop the All-Star Team part.

### Row 5230 — Belgium (easy) — FAIL
**Q:** Which Belgian player, developed in Belgium's youth system, became a Premier League star?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Lukaku was also developed in Belgium's youth system (Anderlecht) and became a Premier League star.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - Lukaku also fits.


### Row 5242 — Belgium (medium) — FAIL
**Q:** Which Belgian player's World Cup performances earned multiple Ballon d'Or nominations?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard also received multiple Ballon d'Or nominations.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.

### Row 5249 — Belgium (easy) — FAIL
**Q:** Which Belgian Pro League club did Kevin De Bruyne play for before his 2010 World Cup debut?
**Answer:** Genk
**Why it fails:** False premise: De Bruyne had no '2010 World Cup debut' - Belgium didn't play the 2010 WC and his WC debut was 2014 (his senior debut was 2010, not at a WC).
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Reword to 'his 2010 senior debut'.

### Row 5251 — Belgium (easy) — FAIL
**Q:** Which Belgian Pro League club had 35 titles before the 2018 World Cup?
**Answer:** Anderlecht
**Why it fails:** Wrong: Anderlecht had 34 league titles (their 34th came in 2017), not 35.
**Source:** https://en.wikipedia.org/wiki/R.S.C._Anderlecht
**Remedy:** Change to 34.

### Row 5253 — Belgium (easy) — FAIL
**Q:** Which Belgian Pro League club won 35 domestic titles historically?
**Answer:** Anderlecht
**Why it fails:** Wrong: Anderlecht has won 34 league titles, not 35.
**Source:** https://en.wikipedia.org/wiki/R.S.C._Anderlecht
**Remedy:** Change to 34.

### Row 5274 — Belgium (hard) — FAIL
**Q:** Which Belgian squad held the world's top FIFA ranking for a record 1,735 days?
**Answer:** 2018-2022 Golden Generation
**Why it fails:** 'record 1,735 days' false: Belgium's No.1 reign was not a record (Brazil & Spain longer); Sep 2018-Mar 2022 is ~1,280 days.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop the '1,735-day record' framing.

### Row 5276 — Belgium (easy) — FAIL
**Q:** Which Belgian squad's consistent results caused their 1,735-day FIFA top ranking from 2018?
**Answer:** The Golden Generation
**Why it fails:** '1,735-day' record framing false (not a record; ~1,280 days).
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop the '1,735-day record' framing.

### Row 5295 — Belgium (easy) — FAIL
**Q:** Which Belgian stadium with a 50,093 capacity hosts their 2022 World Cup qualifiers?
**Answer:** King Baudouin Stadium
**Why it fails:** Non-unique: 'King Baudouin Stadium' and 'Stade Roi Baudouin' are the same venue, so two options are identical and correct.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Replace the duplicate distractor.

### Row 5303 — Belgium (easy) — FAIL
**Q:** Which Belgian star ended his international career in 2023 with 126 caps?
**Answer:** Eden Hazard
**Why it fails:** Wrong: Hazard's international career ended in Dec 2022, not 2023 (his all-football retirement was 2023). 126 caps is correct.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Fix to 2022.

### Row 5310 — Belgium (medium) — FAIL
**Q:** Which Belgian star from the 2018 World Cup Golden Generation has multiple Ballon d'Or nominations?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard also received multiple Ballon d'Or nominations.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.

### Row 5311 — Belgium (medium) — FAIL
**Q:** Which Belgian star from their Golden Generation era was a multiple Ballon d'Or nominee?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard was also a multiple Ballon d'Or nominee from that era.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.

### Row 5320 — Belgium (medium) — FAIL
**Q:** Which Belgian star received multiple Ballon d'Or nominations from 2015 to 2023?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard also received multiple Ballon d'Or nominations 2015-2023.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.

### Row 5326 — Belgium (medium) — FAIL
**Q:** Which Belgian star was a 2022 Ballon d'Or nominee?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard was also a Ballon d'Or nominee.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.

### Row 5327 — Belgium (medium) — FAIL
**Q:** Which Belgian star was Ballon d'Or nominated multiple times by 2022?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard also received multiple Ballon d'Or nominations by 2022.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.

### Row 5333 — Belgium (easy) — FAIL
**Q:** Which Belgian star won both the Silver Ball and made the All-Star Team in 2018?
**Answer:** Eden Hazard
**Why it fails:** False premise: no official 2018 All-Star Team (Hazard won the Silver Ball).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Drop the All-Star Team claim.


### Row 5353 — Belgium (medium) — FAIL
**Q:** Which Belgian star's Ballon d'Or nominations define their Golden Generation?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard also received multiple Ballon d'Or nominations.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.

### Row 5357 — Belgium (easy) — FAIL
**Q:** Which Belgian star's three Chelsea awards preceded his 2018 World Cup All-Star selection?
**Answer:** Eden Hazard
**Why it fails:** False premise: no official 2018 World Cup All-Star Team (Hazard won the Silver Ball).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Drop the All-Star Team claim.

### Row 5387 — Belgium (easy) — FAIL
**Q:** Which Belgian team conduct earned the 2018 FIFA Fair Play Award?
**Answer:** Lowest disciplinary points tally
**Why it fails:** False premise: Belgium did NOT win the 2018 Fair Play Award - Spain did.
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup_awards
**Remedy:** Belgium didn't win it in 2018.

### Row 5390 — Belgium (easy) — FAIL
**Q:** Which Belgian tournament streak began with the 2014 World Cup?
**Answer:** Four consecutive qualifications
**Why it fails:** Wrong count: it was FIVE consecutive qualifications 2014-2022 (incl. Euro 2020), not four.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_UEFA_European_Championship
**Remedy:** Change answer to five.

### Row 5395 — Belgium (easy) — FAIL
**Q:** Which Belgian was top scorer in 2022 WC qualifying, but not in 2018?
**Answer:** Romelu Lukaku
**Why it fails:** False contrast: Lukaku was ALSO Belgium's top scorer in 2018 qualifying (~11 goals), so 'but not in 2018' is wrong.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Drop the 'not in 2018' clause.

### Row 5403 — Belgium (easy) — FAIL
**Q:** Which Belgian winger retired from international football in 2023 with 126 caps?
**Answer:** Eden Hazard
**Why it fails:** Wrong: Hazard's international retirement was Dec 2022, not 2023 (all-football 2023). 126 caps is correct.
**Source:** https://en.wikipedia.org/wiki/Eden_Hazard
**Remedy:** Fix to 2022.

### Row 5432 — Belgium (medium) — FAIL
**Q:** Which Belgium coach's 2026 World Cup qualification mirrored their 2014 group-winning success?
**Answer:** Domenico Tedesco
**Why it fails:** False: Belgium's 2026 qualifying was under Rudi Garcia (Jan 2025), not Tedesco (sacked Jan 2025).
**Source:** https://en.wikipedia.org/wiki/List_of_Belgium_national_football_team_managers
**Remedy:** Change to Rudi Garcia.


### Row 5513 — Belgium (medium) — FAIL
**Q:** Which Belgium manager oversaw their qualification for the 2026 World Cup?
**Answer:** Domenico Tedesco
**Why it fails:** False: Belgium's 2026 qualifying was under Rudi Garcia (appointed Jan 2025), not Tedesco (sacked Jan 2025).
**Source:** https://en.wikipedia.org/wiki/List_of_Belgium_national_football_team_managers
**Remedy:** Change to Rudi Garcia.


### Row 5559 — Belgium (medium) — FAIL
**Q:** Which Belgium player earned multiple Ballon d'Or nominations by 2022?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard also received multiple Ballon d'Or nominations.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.

### Row 5561 — Belgium (easy) — FAIL
**Q:** Which Belgium player from their 2022 group-stage exit also starred in their 2018 semi-final run?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Lukaku, Courtois and Hazard also played in both the 2018 SF run and the 2022 group stage.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Tighten - several players fit.

### Row 5563 — Belgium (medium) — FAIL
**Q:** Which Belgium player had multiple Ballon d'Or nominations by 2022?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard also received multiple Ballon d'Or nominations.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.

### Row 5564 — Belgium (medium) — FAIL
**Q:** Which Belgium player had multiple Ballon d'Or nominations by the 2022 World Cup?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard also received multiple Ballon d'Or nominations.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.

### Row 5568 — Belgium (medium) — FAIL
**Q:** Which Belgium player has been nominated for the Ballon d'Or multiple times?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard also received multiple Ballon d'Or nominations.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.

### Row 5569 — Belgium (medium) — FAIL
**Q:** Which Belgium player has multiple Ballon d'Or nominations since 2018?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard also received multiple Ballon d'Or nominations.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.

### Row 5570 — Belgium (medium) — FAIL
**Q:** Which Belgium player has received multiple Ballon d'Or nominations?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard also received multiple Ballon d'Or nominations.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.

### Row 5578 — Belgium (easy) — FAIL
**Q:** Which Belgium player made the 2018 World Cup All-Star Team?
**Answer:** Eden Hazard
**Why it fails:** False premise: no official 2018 World Cup All-Star Team (Hazard won the Silver Ball).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Drop the All-Star Team claim.

### Row 5596 — Belgium (easy) — FAIL
**Q:** Which Belgium player scored against Japan in the 2018 World Cup round of 16?
**Answer:** Divock Origi
**Why it fails:** Wrong: Origi did not score v Japan in 2018 - Belgium's scorers were Vertonghen, Fellaini and Chadli.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Change to Chadli (an option).

### Row 5623 — Belgium (easy) — FAIL
**Q:** Which Belgium player was top scorer in their 2022 World Cup qualifying, but not in 2018?
**Answer:** Romelu Lukaku
**Why it fails:** False contrast: Lukaku was ALSO Belgium's top scorer in 2018 qualifying, so 'but not in 2018' is wrong.
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** Drop the 'not in 2018' clause.

### Row 5625 — Belgium (medium) — FAIL
**Q:** Which Belgium player, active in 2022 World Cup group stage, has multiple Ballon d'Or nominations?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard also received multiple Ballon d'Or nominations.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.

### Row 5637 — Belgium (medium) — FAIL
**Q:** Which Belgium star was a Ballon d'Or nominee at the 2022 World Cup?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard also received multiple Ballon d'Or nominations.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.

### Row 5638 — Belgium (medium) — FAIL
**Q:** Which Belgium star was nominated for multiple Ballon d'Or awards by 2022?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard also received multiple Ballon d'Or nominations.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.

### Row 5639 — Belgium (medium) — FAIL
**Q:** Which Belgium star's World Cup performances earned multiple Ballon d'Or nominations?
**Answer:** Kevin De Bruyne
**Why it fails:** Non-unique: Hazard also received multiple Ballon d'Or nominations.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Specify 'midfielder' or tighten.


### Row 5647 — Belgium (medium) — FAIL
**Q:** Which Belgium team held the FIFA number 1 spot for a record 1,735 days?
**Answer:** The 2018-2022 side
**Why it fails:** 'record 1,735 days' false: Belgium's No.1 reign was not a record (Brazil & Spain longer; ~1,280 days).
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop the '1,735-day record' framing.

### Row 5682 — Belgium (medium) — FAIL
**Q:** Which manager guided Belgium to 2026 FIFA World Cup qualification?
**Answer:** Domenico Tedesco
**Why it fails:** False: Belgium's 2026 qualifying was under Rudi Garcia (Jan 2025), not Tedesco (sacked Jan 2025).
**Source:** https://en.wikipedia.org/wiki/List_of_Belgium_national_football_team_managers
**Remedy:** Change to Rudi Garcia.

### Row 5684 — Belgium (medium) — FAIL
**Q:** Which manager guided Belgium's qualification for the 2026 FIFA World Cup?
**Answer:** Domenico Tedesco
**Why it fails:** False: Belgium's 2026 qualifying was under Rudi Garcia (Jan 2025), not Tedesco (sacked Jan 2025).
**Source:** https://en.wikipedia.org/wiki/List_of_Belgium_national_football_team_managers
**Remedy:** Change to Rudi Garcia.

### Row 5687 — Belgium (medium) — FAIL
**Q:** Which manager led Belgium to 2026 World Cup qualification, unlike their 2010 failure?
**Answer:** Domenico Tedesco
**Why it fails:** False: Belgium's 2026 qualifying was under Rudi Garcia (Jan 2025), not Tedesco (sacked Jan 2025).
**Source:** https://en.wikipedia.org/wiki/List_of_Belgium_national_football_team_managers
**Remedy:** Change to Rudi Garcia.

### Row 5689 — Belgium (medium) — FAIL
**Q:** Which manager led Belgium to 2026 World Cup UEFA qualification?
**Answer:** Domenico Tedesco
**Why it fails:** False: Belgium's 2026 qualifying was under Rudi Garcia (Jan 2025), not Tedesco (sacked Jan 2025).
**Source:** https://en.wikipedia.org/wiki/List_of_Belgium_national_football_team_managers
**Remedy:** Change to Rudi Garcia.

### Row 5699 — Belgium (easy) — FAIL
**Q:** Which manager led Belgium to qualify for the 2026 FIFA World Cup?
**Answer:** Domenico Tedesco
**Why it fails:** False: Belgium's 2026 qualifying was under Rudi Garcia (Jan 2025), not Tedesco (sacked Jan 2025).
**Source:** https://en.wikipedia.org/wiki/List_of_Belgium_national_football_team_managers
**Remedy:** Change to Rudi Garcia.

### Row 5713 — Belgium (medium) — FAIL
**Q:** Which manager led Belgium's successful 2026 World Cup qualification?
**Answer:** Domenico Tedesco
**Why it fails:** False: Belgium's 2026 qualifying was under Rudi Garcia (Jan 2025), not Tedesco (sacked Jan 2025).
**Source:** https://en.wikipedia.org/wiki/List_of_Belgium_national_football_team_managers
**Remedy:** Change to Rudi Garcia.

### Row 5719 — Belgium (easy) — FAIL
**Q:** Which manager qualified Belgium for both the 2026 and 2024 tournaments?
**Answer:** Domenico Tedesco
**Why it fails:** False: Tedesco qualified Belgium for Euro 2024 but NOT the 2026 WC (that was under Rudi Garcia).
**Source:** https://en.wikipedia.org/wiki/List_of_Belgium_national_football_team_managers
**Remedy:** Tedesco did not do the 2026 qualification.

### Row 5722 — Belgium (easy) — FAIL
**Q:** Which manager qualified Belgium for the 2026 FIFA World Cup?
**Answer:** Domenico Tedesco
**Why it fails:** False: Belgium's 2026 qualifying was under Rudi Garcia (Jan 2025), not Tedesco (sacked Jan 2025).
**Source:** https://en.wikipedia.org/wiki/List_of_Belgium_national_football_team_managers
**Remedy:** Change to Rudi Garcia.

### Row 5734 — Belgium (medium) — FAIL
**Q:** Which manager was in charge of Belgium during their 2018-2022 record FIFA ranking?
**Answer:** Roberto Martínez
**Why it fails:** Question asserts a 'record' FIFA ranking, which is false (Belgium's No.1 reign was not a record). Martinez was the manager, but the premise is wrong.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop 'record'.


### Row 5790 — Belgium (easy) — FAIL
**Q:** Which nation eliminated Belgium from two consecutive major tournaments?
**Answer:** France
**Why it fails:** False: France's eliminations of Belgium were NOT consecutive - Italy eliminated them at Euro 2020 and they group-exited 2022, between the 2018 SF and the Euro 2024 R16.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Drop 'consecutive'.

### Row 5836 — Belgium (easy) — FAIL
**Q:** Which nation's FA headquarters are in Brussels, like Belgium's?
**Answer:** Belgium
**Why it fails:** Self-referential: the question asks which nation's FA is in Brussels 'like Belgium's' and answers Belgium itself.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Reword - the answer restates the subject.


### Row 5860 — Belgium (easy) — FAIL
**Q:** Which stadium did Belgium NOT use for their 2026 World Cup qualifiers?
**Answer:** Eurostadium
**Why it fails:** Non-unique negative: Belgium used only the King Baudouin Stadium for 2026 qualifiers, so they also did not use Jan Breydel or Lotto Park - not just the Eurostadium.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Drop - multiple options qualify.

### Row 5868 — Belgium (easy) — FAIL
**Q:** Which stadium hosts all Belgium home World Cup qualifiers?
**Answer:** King Baudouin Stadium
**Why it fails:** Non-unique: 'King Baudouin Stadium' and 'Stade Roi Baudouin' are the same venue, so two options are identical and correct.
**Source:** https://en.wikipedia.org/wiki/Belgium_national_football_team
**Remedy:** Replace the duplicate.

### Row 5911 — Belgium (easy) — FAIL
**Q:** Which team did Belgium not face in the 2021 Nations League semi-finals?
**Answer:** Portugal
**Why it fails:** Non-unique negative: Belgium faced only France in the 2021 NL SF, so they also did not face Italy or Spain - not just Portugal.
**Source:** https://en.wikipedia.org/wiki/2021_UEFA_Nations_League_Finals
**Remedy:** Drop - multiple options qualify.

### Row 5912 — Belgium (easy) — FAIL
**Q:** Which team did not eliminate Belgium in a Euro quarter-final?
**Answer:** Italy
**Why it fails:** Wrong: Italy DID eliminate Belgium in a Euro QF (2-1 at Euro 2020). The correct 'did not' answer is France or Germany.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Change answer - Italy did eliminate them.


### Row 5943 — Belgium (medium) — FAIL
**Q:** Which two Euro quarter-finals did Belgium lose by a 1-goal margin?
**Answer:** 2020 and 2024
**Why it fails:** False: Belgium's Euro 2024 loss (1-0 to France) was in the ROUND OF 16, not a quarter-final. Their only 1-goal Euro QF loss was 2020 (2-1 to Italy); 2016 was 3-1.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024
**Remedy:** Drop '2024' - it wasn't a QF.

### Row 5947 — Belgium (easy) — FAIL
**Q:** Which two nations finished above Belgium in 2010 World Cup qualifying?
**Answer:** Spain and Türkiye
**Why it fails:** 2010 qualifying: THREE nations finished above Belgium (Spain, Bosnia & Herzegovina, Turkey), not two - the answer omits Bosnia.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_5
**Remedy:** Reword - Belgium finished 4th.

### Row 5949 — Belgium (easy) — FAIL
**Q:** Which two nations finished ahead of Belgium in their 2010 World Cup qualifying group?
**Answer:** Spain and Türkiye
**Why it fails:** 2010 qualifying: THREE nations finished above Belgium (Spain, Bosnia & Herzegovina, Turkey), not two - the answer omits Bosnia.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_5
**Remedy:** Reword - Belgium finished 4th.

### Row 5955 — Belgium (medium) — FAIL
**Q:** Which two World Cups did Belgium qualify for by winning their UEFA group?
**Answer:** 2014 and 2022
**Why it fails:** Non-unique: Belgium also won their 2018 UEFA qualifying group, so the pair is wrong - they won 2014, 2018 AND 2022 (the '2018 and 2022' distractor is equally valid).
**Source:** https://en.wikipedia.org/wiki/Belgium_at_the_FIFA_World_Cup
**Remedy:** At least three qualify - reword.

### Row 6045 — Belgium (easy) — FAIL
**Q:** Who led Belgium to qualify for the 2026 World Cup?
**Answer:** Domenico Tedesco
**Why it fails:** False: Belgium's 2026 qualifying was under Rudi Garcia (Jan 2025), not Tedesco (sacked Jan 2025).
**Source:** https://en.wikipedia.org/wiki/List_of_Belgium_national_football_team_managers
**Remedy:** Change to Rudi Garcia.

### Row 6049 — Belgium (easy) — FAIL
**Q:** Who managed Belgium to qualify for the 2026 World Cup?
**Answer:** Domenico Tedesco
**Why it fails:** False: Belgium's 2026 qualifying was under Rudi Garcia (Jan 2025), not Tedesco (sacked Jan 2025).
**Source:** https://en.wikipedia.org/wiki/List_of_Belgium_national_football_team_managers
**Remedy:** Change to Rudi Garcia.

### Row 6068 — Belgium (easy) — FAIL
**Q:** Why did Belgium hold the FIFA #1 ranking from 2018 to 2022?
**Answer:** Record 1,735-day streak
**Why it fails:** 'Record 1,735-day streak' false: Belgium's No.1 reign was not a record (Brazil & Spain longer; ~1,280 days).
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop the '1,735-day record' framing.

### Row 6072 — Belgium (medium) — FAIL
**Q:** Why did Belgium only average 1.3 goals per game at the 2018 World Cup?
**Answer:** Scored 9 in 7
**Why it fails:** False premise: Belgium scored 16 goals (not 9) in 7 matches at 2018, so they did NOT average 1.3 per game (actual ~2.29).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Recompute from 16 goals.

### Row 6095 — Belgium (easy) — FAIL
**Q:** Why was Belgium ranked FIFA #1 from 2018 to 2022?
**Answer:** Record duration at top
**Why it fails:** 'Record duration at top' false: Belgium's No.1 reign was not a record (Brazil & Spain held it longer).
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Drop 'record'.


## Chile — rows 12429–13845 (new method) — 191 failed-liveness

### Row 12429 — Chile (easy) — FAIL
**Q:** A 2014 Chile win over Spain preceded which player's dual Copa América final heroics?
**Answer:** Alexis Sánchez
**Why it fails:** False: the 2016 Copa America Centenario final winning penalty was scored by Francisco Silva, not Alexis Sanchez. Alexis scored only the 2015 final winner (Bravo saved in both shootouts).
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica_Centenario_final
**Remedy:** Restrict the claim to the 2015 final, or change the 2016 scorer to Francisco Silva.

### Row 12431 — Chile (easy) — FAIL
**Q:** After Chile failed to qualify for the 2022 FIFA World Cup, which era ended?
**Answer:** Their golden era
**Why it fails:** Non-unique: 'golden era / golden generation / golden age / golden period' are synonyms — there is no single distinct correct answer.
**Source:** https://en.wikipedia.org/wiki/Chile_national_football_team
**Remedy:** Replace the distractors with genuinely distinct options.

### Row 12465 — Chile (easy) — FAIL
**Q:** At the 2014 World Cup, what was Chile's score after 90 minutes vs Brazil?
**Answer:** 01-Jan
**Why it fails:** Corrupted answer (Excel date mangling): the cell shows a date in place of the scoreline.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup
**Remedy:** Restore the real scoreline as the answer (e.g. 1-1 after 90', or 3-2 on penalties).

### Row 12466 — Chile (easy) — FAIL
**Q:** At the 2014 World Cup, which Chile forward had over 80 caps and 40+ goals?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 12509 — Chile (easy) — FAIL
**Q:** Chile beat Spain 2-0 in 2014. Who scored their Copa América 2015 & 2016 winning penalties?
**Answer:** Alexis Sánchez
**Why it fails:** False: the 2016 Copa America Centenario final winning penalty was scored by Francisco Silva, not Alexis Sanchez. Alexis scored only the 2015 final winner (Bravo saved in both shootouts).
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica_Centenario_final
**Remedy:** Restrict the claim to the 2015 final, or change the 2016 scorer to Francisco Silva.

### Row 12567 — Chile (easy) — FAIL
**Q:** Chile qualified for the 2026 FIFA World Cup under which manager?
**Answer:** Ricardo Gareca
**Why it fails:** False: Chile did NOT qualify for the 2026 World Cup. They finished last (10th) in CONMEBOL and Ricardo Gareca resigned; it is Chile's 3rd straight World Cup missed.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop/rewrite — Gareca's 2026 campaign failed; do not state Chile qualified.

### Row 12569 — Chile (medium) — FAIL
**Q:** Chile qualified for the 2026 World Cup. Which CONMEBOL campaign did they fail?
**Answer:** 2022 qualification
**Why it fails:** False: Chile did NOT qualify for the 2026 World Cup. They finished last (10th) in CONMEBOL and Ricardo Gareca resigned; it is Chile's 3rd straight World Cup missed.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop/rewrite — Gareca's 2026 campaign failed; do not state Chile qualified.

### Row 12570 — Chile (hard) — FAIL
**Q:** Chile qualified for which FIFA World Cup through CONMEBOL?
**Answer:** The 2014 World Cup
**Why it fails:** Non-unique: Chile also qualified for the 2010 World Cup via CONMEBOL, so the distractor '2010' is equally correct.
**Source:** https://en.wikipedia.org/wiki/Chile_national_football_team
**Remedy:** Remove 2010 as a distractor.

### Row 12583 — Chile (hard) — FAIL
**Q:** Chile's 2014 World Cup qualification was their last before which tournament?
**Answer:** The 2026 World Cup
**Why it fails:** False: Chile did NOT qualify for the 2026 World Cup. They finished last (10th) in CONMEBOL and Ricardo Gareca resigned; it is Chile's 3rd straight World Cup missed.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop/rewrite — Gareca's 2026 campaign failed; do not state Chile qualified.

### Row 12592 — Chile (easy) — FAIL
**Q:** Chile's 2022 qualifying failure under Martín Lasarte mirrored which other manager's failed campaign?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 12594 — Chile (medium) — FAIL
**Q:** Chile's 2026 World Cup qualification under Ricardo Gareca ended which consecutive cycle of CONMEBOL failures?
**Answer:** Two consecutive cycles
**Why it fails:** False: Chile did NOT qualify for the 2026 World Cup. They finished last (10th) in CONMEBOL and Ricardo Gareca resigned; it is Chile's 3rd straight World Cup missed.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop/rewrite — Gareca's 2026 campaign failed; do not state Chile qualified.

### Row 12602 — Chile (medium) — FAIL
**Q:** Chile's Alexis Sánchez scored Copa América winning penalties in which two years?
**Answer:** 2015 and 2016
**Why it fails:** False: the 2016 Copa America Centenario final winning penalty was scored by Francisco Silva, not Alexis Sanchez. Alexis scored only the 2015 final winner (Bravo saved in both shootouts).
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica_Centenario_final
**Remedy:** Restrict the claim to the 2015 final, or change the 2016 scorer to Francisco Silva.

### Row 12606 — Chile (easy) — FAIL
**Q:** Chile's Estadio Nacional has a capacity near 48,665. Which CONMEBOL nation's main World Cup qualifier stadium also holds about 48,000?
**Answer:** Chile
**Why it fails:** Self-referential/circular: the explanation says 'the question states...', the ~48,000 stadium premise is non-unique, and the answer just restates the subject.
**Source:** https://en.wikipedia.org/wiki/Chile_national_football_team
**Remedy:** Drop — circular and non-unique.

### Row 12617 — Chile (medium) — FAIL
**Q:** During which World Cup qualifying campaign did Reinaldo Rueda manage Chile?
**Answer:** The 2018 campaign
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 12658 — Chile (easy) — FAIL
**Q:** In Chile's 2-0 win over Spain in 2014, who later scored both Copa América winning penalties?
**Answer:** Alexis Sánchez
**Why it fails:** False: the 2016 Copa America Centenario final winning penalty was scored by Francisco Silva, not Alexis Sanchez. Alexis scored only the 2015 final winner (Bravo saved in both shootouts).
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica_Centenario_final
**Remedy:** Restrict the claim to the 2015 final, or change the 2016 scorer to Francisco Silva.

### Row 12660 — Chile (hard) — FAIL
**Q:** In Chile's 2014 round of 16 loss to Brazil, what was the penalty shootout score?
**Answer:** 03-Feb
**Why it fails:** Corrupted answer (Excel date mangling): the cell shows a date in place of the scoreline.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup
**Remedy:** Restore the real scoreline as the answer (e.g. 1-1 after 90', or 3-2 on penalties).

### Row 12661 — Chile (easy) — FAIL
**Q:** In Chile's 2014 World Cup squad, which midfielder had over 80 caps by 2023?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 12692 — Chile (medium) — FAIL
**Q:** In which two years did Chile's Alexis Sánchez score Copa América final-winning penalties?
**Answer:** 2015 and 2016
**Why it fails:** False: the 2016 Copa America Centenario final winning penalty was scored by Francisco Silva, not Alexis Sanchez. Alexis scored only the 2015 final winner (Bravo saved in both shootouts).
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica_Centenario_final
**Remedy:** Restrict the claim to the 2015 final, or change the 2016 scorer to Francisco Silva.

### Row 12713 — Chile (medium) — FAIL
**Q:** In which year did Chile qualify for the World Cup under manager Ricardo Gareca?
**Answer:** 2026
**Why it fails:** False: Chile did NOT qualify for the 2026 World Cup. They finished last (10th) in CONMEBOL and Ricardo Gareca resigned; it is Chile's 3rd straight World Cup missed.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop/rewrite — Gareca's 2026 campaign failed; do not state Chile qualified.

### Row 12726 — Chile (medium) — FAIL
**Q:** Under Reinaldo Rueda, Chile failed to qualify for which World Cup?
**Answer:** 2018 World Cup
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 12727 — Chile (easy) — FAIL
**Q:** Under which manager did Chile fail to qualify for the 2018 FIFA World Cup?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 12728 — Chile (easy) — FAIL
**Q:** Under which manager did Chile qualify for the 2026 World Cup?
**Answer:** Ricardo Gareca
**Why it fails:** False: Chile did NOT qualify for the 2026 World Cup. They finished last (10th) in CONMEBOL and Ricardo Gareca resigned; it is Chile's 3rd straight World Cup missed.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop/rewrite — Gareca's 2026 campaign failed; do not state Chile qualified.

### Row 12744 — Chile (hard) — FAIL
**Q:** What was Chile's penalty shootout score against Brazil in 2014?
**Answer:** 03-Feb
**Why it fails:** Corrupted answer (Excel date mangling): the cell shows a date in place of the scoreline.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup
**Remedy:** Restore the real scoreline as the answer (e.g. 1-1 after 90', or 3-2 on penalties).

### Row 12797 — Chile (medium) — FAIL
**Q:** When did Reinaldo Rueda manage Chile's failed World Cup qualifying campaign?
**Answer:** 2018 qualifying
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 12802 — Chile (medium) — FAIL
**Q:** When will Chile's new generation debut at a FIFA World Cup?
**Answer:** 2026
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 12856 — Chile (easy) — FAIL
**Q:** Which aging Chile star could still play at the 2026 World Cup?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 12880 — Chile (easy) — FAIL
**Q:** Which Chile forward at the 2026 World Cup provides Premier League pedigree?
**Answer:** Ben Brereton Díaz
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 12882 — Chile (easy) — FAIL
**Q:** Which Chile forward brought Premier League experience to their 2026 World Cup squad?
**Answer:** Ben Brereton Díaz
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 12885 — Chile (easy) — FAIL
**Q:** Which Chile forward could feature at his fifth World Cup in 2026?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 12886 — Chile (easy) — FAIL
**Q:** Which Chile forward could feature at the 2026 FIFA World Cup?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 12887 — Chile (easy) — FAIL
**Q:** Which Chile forward could make a 2026 World Cup his last?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 12888 — Chile (easy) — FAIL
**Q:** Which Chile forward could play at the 2026 World Cup despite his veteran status?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 12890 — Chile (easy) — FAIL
**Q:** Which Chile forward debuted in the 2026 World Cup qualifiers?
**Answer:** Ben Brereton Díaz
**Why it fails:** False: Ben Brereton Diaz debuted for Chile in 2021 (during the 2022 qualifying cycle), not in the 2026 World Cup qualifiers.
**Source:** https://en.wikipedia.org/wiki/Ben_Brereton_D%C3%ADaz
**Remedy:** Change to 2021 / the 2022 cycle, or drop the '2026' debut claim.

### Row 12900 — Chile (easy) — FAIL
**Q:** Which Chile forward had over 40 goals and played at the 2014 World Cup?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 12901 — Chile (easy) — FAIL
**Q:** Which Chile forward had over 80 caps and 40+ goals by 2022?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 12906 — Chile (easy) — FAIL
**Q:** Which Chile forward has scored over 40 international goals?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 12910 — Chile (easy) — FAIL
**Q:** Which Chile forward may feature at the 2026 FIFA World Cup?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 12913 — Chile (easy) — FAIL
**Q:** Which Chile forward scored 40+ goals and played at the 2014 World Cup?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 12914 — Chile (easy) — FAIL
**Q:** Which Chile forward scored over 40 goals for his country?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 12915 — Chile (easy) — FAIL
**Q:** Which Chile forward scored over 40 goals, including at the 2014 World Cup?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 12916 — Chile (medium) — FAIL
**Q:** Which Chile forward started all three group stage matches at the 2014 World Cup?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 12919 — Chile (easy) — FAIL
**Q:** Which Chile forward was a key starter at the 2014 World Cup?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 12921 — Chile (easy) — FAIL
**Q:** Which Chile forward was in their 2014 FIFA World Cup squad?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 12923 — Chile (easy) — FAIL
**Q:** Which Chile forward was key at both the 2014 World Cup and the 2015 Copa América?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 12924 — Chile (easy) — FAIL
**Q:** Which Chile forward was key at the 2014 FIFA World Cup?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 12926 — Chile (easy) — FAIL
**Q:** Which Chile forward was key for their 2014 FIFA World Cup campaign?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 12927 — Chile (easy) — FAIL
**Q:** Which Chile forward was key for them at the 2014 FIFA World Cup?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 12928 — Chile (easy) — FAIL
**Q:** Which Chile forward was key in the 2014 World Cup qualifiers?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 12932 — Chile (easy) — FAIL
**Q:** Which Chile forward with Premier League pedigree debuted in 2026 World Cup qualifiers?
**Answer:** Ben Brereton Díaz
**Why it fails:** False: Ben Brereton Diaz debuted for Chile in 2021 (during the 2022 qualifying cycle), not in the 2026 World Cup qualifiers.
**Source:** https://en.wikipedia.org/wiki/Ben_Brereton_D%C3%ADaz
**Remedy:** Change to 2021 / the 2022 cycle, or drop the '2026' debut claim.

### Row 12938 — Chile (easy) — FAIL
**Q:** Which Chile forward, with over 80 caps and 40 goals, was key at the 2014 FIFA World Cup?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 12954 — Chile (easy) — FAIL
**Q:** Which Chile manager beat Argentina on penalties in the 2015 and 2016 Copa América finals?
**Answer:** Jorge Sampaoli
**Why it fails:** False: no single manager won both finals — Jorge Sampaoli won the 2015 Copa America, but the 2016 Copa Centenario was won under Juan Antonio Pizzi.
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica_Centenario_final
**Remedy:** Restrict to 2015 (Sampaoli) or 2016 (Pizzi).

### Row 12955 — Chile (easy) — FAIL
**Q:** Which Chile manager defeated Argentina in two consecutive Copa América finals?
**Answer:** Jorge Sampaoli
**Why it fails:** False: no single manager won both finals — Jorge Sampaoli won the 2015 Copa America, but the 2016 Copa Centenario was won under Juan Antonio Pizzi.
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica_Centenario_final
**Remedy:** Restrict to 2015 (Sampaoli) or 2016 (Pizzi).

### Row 12956 — Chile (easy) — FAIL
**Q:** Which Chile manager failed in 2018 WC qualifying, unlike Gareca in 2026?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 12958 — Chile (easy) — FAIL
**Q:** Which Chile manager failed in the 2018 World Cup qualifiers?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 12964 — Chile (easy) — FAIL
**Q:** Which Chile manager failed to qualify them for the 2018 FIFA World Cup?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 12965 — Chile (easy) — FAIL
**Q:** Which Chile manager led the 2018 World Cup qualifying failure?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 12978 — Chile (medium) — FAIL
**Q:** Which Chile manager oversaw the failed 2018 World Cup qualification campaign?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 12981 — Chile (medium) — FAIL
**Q:** Which Chile manager oversaw their failed 2018 World Cup qualification?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 12982 — Chile (easy) — FAIL
**Q:** Which Chile manager oversaw their failed 2018 World Cup qualifying campaign?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 12996 — Chile (easy) — FAIL
**Q:** Which Chile manager won a Copa América after Marcelo Bielsa's tenure?
**Answer:** Jorge Sampaoli
**Why it fails:** Non-unique: both Sampaoli (2015) and Pizzi (2016, a distractor) won a Copa America during/after the relevant period, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Chile_national_football_team
**Remedy:** Remove Juan Antonio Pizzi from the options.

### Row 12997 — Chile (easy) — FAIL
**Q:** Which Chile manager won a Copa América title but did not manage a World Cup qualifying campaign?
**Answer:** Juan Antonio Pizzi
**Why it fails:** False: Juan Antonio Pizzi DID manage a World Cup qualifying campaign — he oversaw Chile's failed 2018 CONMEBOL qualifying (6th).
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop — the premise that Pizzi never managed a qualifying campaign is wrong.

### Row 13006 — Chile (easy) — FAIL
**Q:** Which Chile manager's 2018 World Cup qualifying failure was repeated by Martín Lasarte in 2022?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 13007 — Chile (easy) — FAIL
**Q:** Which Chile manager's Copa América win came during his tenure?
**Answer:** Jorge Sampaoli
**Why it fails:** Non-unique: both Sampaoli (2015) and Pizzi (2016, a distractor) won a Copa America during/after the relevant period, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Chile_national_football_team
**Remedy:** Remove Juan Antonio Pizzi from the options.

### Row 13008 — Chile (easy) — FAIL
**Q:** Which Chile manager's failed qualifying campaign came after Reinaldo Rueda's?
**Answer:** Martín Lasarte
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 13017 — Chile (easy) — FAIL
**Q:** Which Chile midfielder had over 80 caps during the 2015 Copa América victory?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13018 — Chile (easy) — FAIL
**Q:** Which Chile midfielder had over 80 caps during their golden era?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13020 — Chile (easy) — FAIL
**Q:** Which Chile midfielder reached 80+ caps during their golden era?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13021 — Chile (easy) — FAIL
**Q:** Which Chile midfielder was a key starter in their 2014 World Cup round of 16 run?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13023 — Chile (easy) — FAIL
**Q:** Which Chile midfielder was key during their 2014 World Cup golden era?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13025 — Chile (medium) — FAIL
**Q:** Which Chile midfielder, with over 80 caps, played in the 2014 World Cup group stage?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13026 — Chile (easy) — FAIL
**Q:** Which Chile midfielder, with over 80 caps, was key during their golden era World Cup qualifiers?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13035 — Chile (easy) — FAIL
**Q:** Which Chile player could feature at the 2026 World Cup?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13036 — Chile (easy) — FAIL
**Q:** Which Chile player could make his last World Cup appearance in 2026?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13041 — Chile (easy) — FAIL
**Q:** Which Chile player for the 2026 World Cup squad has a Premier League pedigree?
**Answer:** Ben Brereton Díaz
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13043 — Chile (easy) — FAIL
**Q:** Which Chile player from the 2014 squad is least likely to start at the 2026 World Cup?
**Answer:** Gary Medel
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13055 — Chile (easy) — FAIL
**Q:** Which Chile player is part of their 2026 World Cup veteran core?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13060 — Chile (easy) — FAIL
**Q:** Which Chile player may feature at the 2026 FIFA World Cup despite nearing retirement?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13061 — Chile (easy) — FAIL
**Q:** Which Chile player may feature at the 2026 World Cup despite his age?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13073 — Chile (easy) — FAIL
**Q:** Which Chile player scored the decisive penalty in consecutive Copa América finals?
**Answer:** Alexis Sánchez
**Why it fails:** False: the 2016 Copa America Centenario final winning penalty was scored by Francisco Silva, not Alexis Sanchez. Alexis scored only the 2015 final winner (Bravo saved in both shootouts).
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica_Centenario_final
**Remedy:** Restrict the claim to the 2015 final, or change the 2016 scorer to Francisco Silva.

### Row 13082 — Chile (easy) — FAIL
**Q:** Which Chile player scored winning penalties in both 2015 and 2016 Copa América finals?
**Answer:** Alexis Sánchez
**Why it fails:** False: the 2016 Copa America Centenario final winning penalty was scored by Francisco Silva, not Alexis Sanchez. Alexis scored only the 2015 final winner (Bravo saved in both shootouts).
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica_Centenario_final
**Remedy:** Restrict the claim to the 2015 final, or change the 2016 scorer to Francisco Silva.

### Row 13104 — Chile (easy) — FAIL
**Q:** Which Chile player, with over 50 goals, is CONMEBOL's 3rd-highest active international scorer?
**Answer:** Alexis Sánchez
**Why it fails:** False/unverifiable ranking: Alexis Sanchez is not CONMEBOL's 3rd-highest active international scorer (Messi, Neymar and Suarez all rank above him).
**Source:** https://en.wikipedia.org/wiki/Alexis_S%C3%A1nchez
**Remedy:** Drop the specific '3rd-highest active' claim.

### Row 13118 — Chile (easy) — FAIL
**Q:** Which Chile players will feature in the 2026 World Cup squad?
**Answer:** A new generation
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13123 — Chile (easy) — FAIL
**Q:** Which Chile squad will mark a generational shift at the 2026 FIFA World Cup?
**Answer:** A new generation
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13127 — Chile (easy) — FAIL
**Q:** Which Chile star could make his final World Cup appearance in 2026?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13129 — Chile (easy) — FAIL
**Q:** Which Chile star could play his last World Cup in 2026?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13138 — Chile (easy) — FAIL
**Q:** Which Chile star will lead their new generation at the 2026 World Cup?
**Answer:** Ben Brereton Díaz
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13146 — Chile (easy) — FAIL
**Q:** Which Chile veteran could play his final World Cup in 2026?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13147 — Chile (easy) — FAIL
**Q:** Which Chile veteran could still play at the 2026 World Cup?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13148 — Chile (easy) — FAIL
**Q:** Which Chile veteran may still feature at the 2026 World Cup?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13155 — Chile (easy) — FAIL
**Q:** Which Chilean 2026 World Cup veteran was part of the aging golden generation?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13189 — Chile (easy) — FAIL
**Q:** Which Chilean forward could become one of the oldest outfield players at the 2026 FIFA World Cup?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13190 — Chile (easy) — FAIL
**Q:** Which Chilean forward could play in his fifth World Cup in 2026?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13196 — Chile (easy) — FAIL
**Q:** Which Chilean forward for the 2026 World Cup squad has Premier League experience?
**Answer:** Ben Brereton Díaz
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13204 — Chile (easy) — FAIL
**Q:** Which Chilean forward may feature at the 2026 FIFA World Cup?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13205 — Chile (easy) — FAIL
**Q:** Which Chilean forward provided goals and Premier League pedigree for the 2026 World Cup squad?
**Answer:** Ben Brereton Díaz
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13208 — Chile (easy) — FAIL
**Q:** Which Chilean forward was a key player at the 2014 FIFA World Cup?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 13209 — Chile (easy) — FAIL
**Q:** Which Chilean forward was key at the 2014 World Cup?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 13210 — Chile (easy) — FAIL
**Q:** Which Chilean forward was key to their attack at the 2014 FIFA World Cup?
**Answer:** Eduardo Vargas
**Why it fails:** Non-unique: Alexis Sanchez (a forward with 166+ caps and 50 goals who also started up front at the 2014 World Cup) equally satisfies the criterion, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Add a detail unique to Vargas, or remove Alexis Sanchez from the options.

### Row 13213 — Chile (easy) — FAIL
**Q:** Which Chilean forward with Premier League experience debuted in the 2026 World Cup qualifiers?
**Answer:** Ben Brereton Díaz
**Why it fails:** False: Ben Brereton Diaz debuted for Chile in 2021 (during the 2022 qualifying cycle), not in the 2026 World Cup qualifiers.
**Source:** https://en.wikipedia.org/wiki/Ben_Brereton_D%C3%ADaz
**Remedy:** Change to 2021 / the 2022 cycle, or drop the '2026' debut claim.

### Row 13215 — Chile (easy) — FAIL
**Q:** Which Chilean forward with Premier League pedigree played at the 2026 World Cup?
**Answer:** Ben Brereton Díaz
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13218 — Chile (easy) — FAIL
**Q:** Which Chilean forward, part of the new generation, has Premier League pedigree for the 2026 World Cup?
**Answer:** Ben Brereton Díaz
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13224 — Chile (easy) — FAIL
**Q:** Which Chilean generation will dominate the 2026 FIFA World Cup squad?
**Answer:** A new generation
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13225 — Chile (easy) — FAIL
**Q:** Which Chilean generation will lead the squad at the 2026 FIFA World Cup?
**Answer:** A new generation
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13236 — Chile (easy) — FAIL
**Q:** Which Chilean golden generation star played in the 2026 World Cup qualifiers?
**Answer:** Alexis Sánchez
**Why it fails:** Non-unique: Arturo Vidal and Gary Medel also featured for Chile in the 2026 qualifying campaign, so the golden-generation answer is not unique.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Remove Vidal/Medel from the options or pick a uniquely identifying fact.

### Row 13249 — Chile (easy) — FAIL
**Q:** Which Chilean manager's qualifying failure preceded Martín Lasarte's 2022 failure?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 13250 — Chile (easy) — FAIL
**Q:** Which Chilean manager's tenure ended before the 2018 World Cup qualifiers?
**Answer:** Jorge Sampaoli
**Why it fails:** False/non-unique: Sampaoli's tenure did not end before the 2018 qualifiers — the 2018 CONMEBOL qualifying began Oct 2015 and Sampaoli managed its first matches before resigning Jan 2016; Bielsa (a distractor) also pre-dates it.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Rephrase; the premise is inaccurate and the answer non-unique.

### Row 13252 — Chile (easy) — FAIL
**Q:** Which Chilean midfielder earned over 80 caps during the 2010s golden era?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13256 — Chile (easy) — FAIL
**Q:** Which Chilean midfielder had over 80 caps by the 2018 World Cup qualifiers?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13257 — Chile (easy) — FAIL
**Q:** Which Chilean midfielder had over 80 caps during the golden era?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13258 — Chile (easy) — FAIL
**Q:** Which Chilean midfielder had over 80 caps during their golden era?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13259 — Chile (easy) — FAIL
**Q:** Which Chilean midfielder was a key squad inclusion for the 2014 FIFA World Cup?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13261 — Chile (easy) — FAIL
**Q:** Which Chilean midfielder was key during the golden era of World Cup qualifying?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13262 — Chile (easy) — FAIL
**Q:** Which Chilean midfielder was key during their golden era before the 2014 World Cup?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13263 — Chile (easy) — FAIL
**Q:** Which Chilean midfielder was key during their golden era World Cup campaigns?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13264 — Chile (easy) — FAIL
**Q:** Which Chilean midfielder was key during their golden era?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13267 — Chile (easy) — FAIL
**Q:** Which Chilean midfielder was selected for their 2014 World Cup squad?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13269 — Chile (easy) — FAIL
**Q:** Which Chilean midfielder with over 80 caps played a key role during their golden era?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13272 — Chile (easy) — FAIL
**Q:** Which Chilean midfielder, with over 80 caps, was a key starter during their 2014 World Cup campaign?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13273 — Chile (easy) — FAIL
**Q:** Which Chilean midfielder, with over 80 caps, was a key starter in their 2014 World Cup golden era?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13274 — Chile (easy) — FAIL
**Q:** Which Chilean midfielder, with over 80 caps, was a key tactical component in their 2014 World Cup midfield?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13280 — Chile (easy) — FAIL
**Q:** Which Chilean player could appear at the 2026 World Cup after 2010?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13281 — Chile (easy) — FAIL
**Q:** Which Chilean player could be in both the 2014 and 2026 World Cup squads?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13282 — Chile (easy) — FAIL
**Q:** Which Chilean player could feature at both the 2014 and 2026 World Cups?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13283 — Chile (easy) — FAIL
**Q:** Which Chilean player could feature at the 2026 FIFA World Cup?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13289 — Chile (easy) — FAIL
**Q:** Which Chilean player from the 2014 squad could also feature at the 2026 World Cup?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13290 — Chile (easy) — FAIL
**Q:** Which Chilean player from the 2014 World Cup is unlikely to be in the 2026 squad?
**Answer:** Alexis Sánchez
**Why it fails:** Non-unique/false premise: all four golden-generation players are equally 'unlikely' for a 2026 squad, and Chile failed to qualify for 2026 so no such squad exists.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop.

### Row 13291 — Chile (easy) — FAIL
**Q:** Which Chilean player from the 2026 World Cup squad is a new-generation forward?
**Answer:** Ben Brereton Díaz
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13295 — Chile (easy) — FAIL
**Q:** Which Chilean player has NOT scored 40+ goals for their national team?
**Answer:** Arturo Vidal
**Why it fails:** Non-unique/wrong explanation: it claims Ben Brereton Diaz has scored 40+ goals (he has ~5); both Vidal and Brereton fail the 40+ criterion.
**Source:** https://en.wikipedia.org/wiki/Eduardo_Vargas
**Remedy:** Fix the explanation — only Sanchez and Vargas have 40+ goals.

### Row 13305 — Chile (easy) — FAIL
**Q:** Which Chilean player provides goals and Premier League pedigree for the 2026 World Cup squad?
**Answer:** Ben Brereton Díaz
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13308 — Chile (easy) — FAIL
**Q:** Which Chilean player represents the new 2026 World Cup generation?
**Answer:** Ben Brereton Díaz
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13309 — Chile (easy) — FAIL
**Q:** Which Chilean player scored the decisive penalty in both the 2015 and 2016 Copa América finals?
**Answer:** Alexis Sánchez
**Why it fails:** False: the 2016 Copa America Centenario final winning penalty was scored by Francisco Silva, not Alexis Sanchez. Alexis scored only the 2015 final winner (Bravo saved in both shootouts).
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica_Centenario_final
**Remedy:** Restrict the claim to the 2015 final, or change the 2016 scorer to Francisco Silva.

### Row 13314 — Chile (easy) — FAIL
**Q:** Which Chilean player secured both their 2015 and 2016 Copa América final wins?
**Answer:** Alexis Sánchez
**Why it fails:** False: the 2016 Copa America Centenario final winning penalty was scored by Francisco Silva, not Alexis Sanchez. Alexis scored only the 2015 final winner (Bravo saved in both shootouts).
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica_Centenario_final
**Remedy:** Restrict the claim to the 2015 final, or change the 2016 scorer to Francisco Silva.

### Row 13329 — Chile (easy) — FAIL
**Q:** Which Chilean player will be part of the new generation at the 2026 World Cup?
**Answer:** Ben Brereton Díaz
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13330 — Chile (easy) — FAIL
**Q:** Which Chilean player will lead their new generation at the 2026 World Cup?
**Answer:** Ben Brereton Díaz
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13332 — Chile (easy) — FAIL
**Q:** Which Chilean player will represent the new generation at the 2026 World Cup?
**Answer:** Ben Brereton Díaz
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13337 — Chile (easy) — FAIL
**Q:** Which Chilean player's 2026 World Cup squad would be his last?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13340 — Chile (easy) — FAIL
**Q:** Which Chilean player's penalty kicks secured their 2015 and 2016 Copa América titles?
**Answer:** Alexis Sánchez
**Why it fails:** False: the 2016 Copa America Centenario final winning penalty was scored by Francisco Silva, not Alexis Sanchez. Alexis scored only the 2015 final winner (Bravo saved in both shootouts).
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica_Centenario_final
**Remedy:** Restrict the claim to the 2015 final, or change the 2016 scorer to Francisco Silva.

### Row 13356 — Chile (easy) — FAIL
**Q:** Which Chilean star could play his last World Cup in 2026?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13357 — Chile (easy) — FAIL
**Q:** Which Chilean star could still play at the 2026 World Cup?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13360 — Chile (easy) — FAIL
**Q:** Which Chilean star from Copa America 2015 may play at the 2026 World Cup?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13361 — Chile (easy) — FAIL
**Q:** Which Chilean star from the 2010s could play at the 2026 FIFA World Cup?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13367 — Chile (easy) — FAIL
**Q:** Which Chilean star's final World Cup appearance could be in 2026?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13373 — Chile (easy) — FAIL
**Q:** Which Chilean striker debuted for the 2026 World Cup squad?
**Answer:** Ben Brereton Díaz
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13376 — Chile (easy) — FAIL
**Q:** Which Chilean veteran could appear at his final World Cup in 2026?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13378 — Chile (easy) — FAIL
**Q:** Which Chilean veteran could still play at the 2026 FIFA World Cup?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13379 — Chile (easy) — FAIL
**Q:** Which Chilean veteran from the 2014 World Cup could still feature at the 2026 tournament?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13381 — Chile (easy) — FAIL
**Q:** Which Chilean veteran is from the aging generation, not the new 2026 one?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13382 — Chile (easy) — FAIL
**Q:** Which Chilean veteran may be included in their 2026 World Cup squad?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13384 — Chile (easy) — FAIL
**Q:** Which Chilean veteran may feature in the 2026 FIFA World Cup squad?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13386 — Chile (easy) — FAIL
**Q:** Which Chilean veteran of the 2014 World Cup could still play at the 2026 finals?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13391 — Chile (easy) — FAIL
**Q:** Which Chilean veteran's career longevity may allow him to play at the 2026 World Cup?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13392 — Chile (easy) — FAIL
**Q:** Which Chilean veteran's Copa America 2024 form could earn him a 2026 World Cup spot?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13394 — Chile (medium) — FAIL
**Q:** Which coach led Chile to 2026 World Cup qualification?
**Answer:** Ricardo Gareca
**Why it fails:** False: Chile did NOT qualify for the 2026 World Cup. They finished last (10th) in CONMEBOL and Ricardo Gareca resigned; it is Chile's 3rd straight World Cup missed.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop/rewrite — Gareca's 2026 campaign failed; do not state Chile qualified.

### Row 13395 — Chile (easy) — FAIL
**Q:** Which coach led Chile to qualify for the 2026 FIFA World Cup?
**Answer:** Ricardo Gareca
**Why it fails:** False: Chile did NOT qualify for the 2026 World Cup. They finished last (10th) in CONMEBOL and Ricardo Gareca resigned; it is Chile's 3rd straight World Cup missed.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop/rewrite — Gareca's 2026 campaign failed; do not state Chile qualified.

### Row 13443 — Chile (medium) — FAIL
**Q:** Which CONMEBOL nation qualified for the 2014 World Cup after Chile's 2010 qualification?
**Answer:** Chile
**Why it fails:** Non-unique/self-referential: Uruguay and Colombia (distractors) also qualified for 2014, and the answer 'Chile' restates the subject of the question.
**Source:** https://en.wikipedia.org/wiki/Chile_national_football_team
**Remedy:** Drop or rephrase to a unique fact.

### Row 13466 — Chile (easy) — FAIL
**Q:** Which CONMEBOL nation, like Chile, qualified for the 2010 FIFA World Cup?
**Answer:** Brazil
**Why it fails:** Non-unique: Argentina, Uruguay and Paraguay all also qualified for the 2010 World Cup, so multiple distractors are correct.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup
**Remedy:** Use a distractor set where only one nation qualified for 2010.

### Row 13547 — Chile (medium) — FAIL
**Q:** Which manager guided Chile to 2026 World Cup qualification?
**Answer:** Ricardo Gareca
**Why it fails:** False: Chile did NOT qualify for the 2026 World Cup. They finished last (10th) in CONMEBOL and Ricardo Gareca resigned; it is Chile's 3rd straight World Cup missed.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop/rewrite — Gareca's 2026 campaign failed; do not state Chile qualified.

### Row 13550 — Chile (easy) — FAIL
**Q:** Which manager led Chile during 2018 World Cup qualifying?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 13552 — Chile (medium) — FAIL
**Q:** Which manager led Chile during their failed 2018 FIFA World Cup qualification?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 13553 — Chile (easy) — FAIL
**Q:** Which manager led Chile during their failed 2018 World Cup qualifying campaign?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 13556 — Chile (easy) — FAIL
**Q:** Which manager led Chile in the 2018 World Cup qualifiers?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 13559 — Chile (medium) — FAIL
**Q:** Which manager led Chile to 2026 World Cup qualification?
**Answer:** Ricardo Gareca
**Why it fails:** False: Chile did NOT qualify for the 2026 World Cup. They finished last (10th) in CONMEBOL and Ricardo Gareca resigned; it is Chile's 3rd straight World Cup missed.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop/rewrite — Gareca's 2026 campaign failed; do not state Chile qualified.

### Row 13560 — Chile (easy) — FAIL
**Q:** Which manager led Chile to fail in 2018 World Cup qualifying?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 13561 — Chile (easy) — FAIL
**Q:** Which manager led Chile to qualify for the 2026 FIFA World Cup?
**Answer:** Ricardo Gareca
**Why it fails:** False: Chile did NOT qualify for the 2026 World Cup. They finished last (10th) in CONMEBOL and Ricardo Gareca resigned; it is Chile's 3rd straight World Cup missed.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop/rewrite — Gareca's 2026 campaign failed; do not state Chile qualified.

### Row 13573 — Chile (medium) — FAIL
**Q:** Which manager led Chile's failed 2018 World Cup qualification?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 13574 — Chile (easy) — FAIL
**Q:** Which manager led Chile's failed 2018 World Cup qualifying campaign?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 13581 — Chile (easy) — FAIL
**Q:** Which manager qualified Chile for the 2026 World Cup after two failed campaigns?
**Answer:** Ricardo Gareca
**Why it fails:** False: Chile did NOT qualify for the 2026 World Cup. They finished last (10th) in CONMEBOL and Ricardo Gareca resigned; it is Chile's 3rd straight World Cup missed.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop/rewrite — Gareca's 2026 campaign failed; do not state Chile qualified.

### Row 13583 — Chile (medium) — FAIL
**Q:** Which manager secured Chile's 2026 World Cup qualification?
**Answer:** Ricardo Gareca
**Why it fails:** False: Chile did NOT qualify for the 2026 World Cup. They finished last (10th) in CONMEBOL and Ricardo Gareca resigned; it is Chile's 3rd straight World Cup missed.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop/rewrite — Gareca's 2026 campaign failed; do not state Chile qualified.

### Row 13589 — Chile (easy) — FAIL
**Q:** Which manager was in charge of Chile during the 2018 World Cup qualifiers?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 13592 — Chile (medium) — FAIL
**Q:** Which manager was in charge of Chile's unsuccessful 2018 World Cup qualification?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 13595 — Chile (easy) — FAIL
**Q:** Which manager's Chile failed to qualify for the 2018 World Cup?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 13628 — Chile (medium) — FAIL
**Q:** Which nation did Chile not face in the 2010 FIFA World Cup knockout stage?
**Answer:** Netherlands
**Why it fails:** Non-unique: Chile's only 2010 knockout match was the R16 vs Brazil, so they faced none of Netherlands/Spain/Portugal in the knockout — several distractors are equally 'not faced'.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup
**Remedy:** Rephrase; only Brazil was faced in the knockout.

### Row 13656 — Chile (medium) — FAIL
**Q:** Which nation's 2010 World Cup qualification campaign directly competed with Chile's?
**Answer:** Uruguay
**Why it fails:** Non-unique: Paraguay (a distractor) also qualified for 2010, and every CONMEBOL side 'competed' in the same campaign.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup
**Remedy:** Rephrase to a uniquely identifying fact.

### Row 13661 — Chile (easy) — FAIL
**Q:** Which player's penalties secured Chile's 2015 and 2016 Copa América titles?
**Answer:** Alexis Sánchez
**Why it fails:** False: the 2016 Copa America Centenario final winning penalty was scored by Francisco Silva, not Alexis Sanchez. Alexis scored only the 2015 final winner (Bravo saved in both shootouts).
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica_Centenario_final
**Remedy:** Restrict the claim to the 2015 final, or change the 2016 scorer to Francisco Silva.

### Row 13664 — Chile (easy) — FAIL
**Q:** Which Premier League forward debuted for Chile during 2026 World Cup qualifying?
**Answer:** Ben Brereton Díaz
**Why it fails:** False: Ben Brereton Diaz debuted for Chile in 2021 (during the 2022 qualifying cycle), not in the 2026 World Cup qualifiers.
**Source:** https://en.wikipedia.org/wiki/Ben_Brereton_D%C3%ADaz
**Remedy:** Change to 2021 / the 2022 cycle, or drop the '2026' debut claim.

### Row 13665 — Chile (easy) — FAIL
**Q:** Which Premier League forward is in Chile's 2026 World Cup squad?
**Answer:** Ben Brereton Díaz
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13666 — Chile (easy) — FAIL
**Q:** Which Premier League forward was in Chile's 2026 World Cup squad?
**Answer:** Ben Brereton Díaz
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13702 — Chile (easy) — FAIL
**Q:** Which team did Chile beat 2-0 at the 2014 World Cup, eliminating Spain?
**Answer:** Chile
**Why it fails:** Broken: the answer 'Chile' is self-referential; the team Chile beat 2-0 to eliminate the defending champions was Spain.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup
**Remedy:** Change the answer to Spain.

### Row 13748 — Chile (easy) — FAIL
**Q:** Which veteran Chile forward could feature at the 2026 World Cup?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13749 — Chile (easy) — FAIL
**Q:** Which veteran Chile forward may play at the 2026 World Cup?
**Answer:** Alexis Sánchez
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13758 — Chile (medium) — FAIL
**Q:** Which World Cup did Chile qualify for under manager Ricardo Gareca?
**Answer:** 2026 World Cup
**Why it fails:** False: Chile did NOT qualify for the 2026 World Cup. They finished last (10th) in CONMEBOL and Ricardo Gareca resigned; it is Chile's 3rd straight World Cup missed.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop/rewrite — Gareca's 2026 campaign failed; do not state Chile qualified.

### Row 13778 — Chile (easy) — FAIL
**Q:** Who managed Chile during their failed 2018 World Cup qualifiers?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 13779 — Chile (easy) — FAIL
**Q:** Who managed Chile during their failed 2018 World Cup qualifying campaign?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 13786 — Chile (easy) — FAIL
**Q:** Who scored Chile's winning penalties in both 2015 and 2016 Copa América finals?
**Answer:** Alexis Sánchez
**Why it fails:** False: the 2016 Copa America Centenario final winning penalty was scored by Francisco Silva, not Alexis Sanchez. Alexis scored only the 2015 final winner (Bravo saved in both shootouts).
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica_Centenario_final
**Remedy:** Restrict the claim to the 2015 final, or change the 2016 scorer to Francisco Silva.

### Row 13789 — Chile (easy) — FAIL
**Q:** Who scored Chile's winning penalty in the 2016 Copa América Centenario final?
**Answer:** Alexis Sánchez
**Why it fails:** False: the 2016 Copa America Centenario final winning penalty was scored by Francisco Silva, not Alexis Sanchez. Alexis scored only the 2015 final winner (Bravo saved in both shootouts).
**Source:** https://en.wikipedia.org/wiki/Copa_Am%C3%A9rica_Centenario_final
**Remedy:** Restrict the claim to the 2015 final, or change the 2016 scorer to Francisco Silva.

### Row 13795 — Chile (easy) — FAIL
**Q:** Who was Chile's key midfielder during their golden era at the 2014 World Cup?
**Answer:** Charles Aránguiz
**Why it fails:** Non-unique: Arturo Vidal (a midfielder with 140+ caps from the same golden era) equally satisfies '80+ caps / key golden-era midfielder', so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Charles_Ar%C3%A1nguiz
**Remedy:** Remove Vidal from the options, or add a detail unique to Aranguiz.

### Row 13797 — Chile (easy) — FAIL
**Q:** Who was Chile's manager when they qualified for the 2026 World Cup?
**Answer:** Ricardo Gareca
**Why it fails:** False: Chile did NOT qualify for the 2026 World Cup. They finished last (10th) in CONMEBOL and Ricardo Gareca resigned; it is Chile's 3rd straight World Cup missed.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop/rewrite — Gareca's 2026 campaign failed; do not state Chile qualified.

### Row 13798 — Chile (easy) — FAIL
**Q:** Who was the Chile manager during their failed 2018 FIFA World Cup qualifying campaign?
**Answer:** Reinaldo Rueda
**Why it fails:** Wrong manager: the failed 2018 qualifying (6th in CONMEBOL) was under Juan Antonio Pizzi. Reinaldo Rueda was appointed Jan 2018 — AFTER that campaign — and led the start of the 2022 cycle.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Change the manager to Juan Antonio Pizzi (or re-anchor Rueda to the 2022 cycle).

### Row 13841 — Chile (easy) — FAIL
**Q:** Why might Chile's Alexis Sánchez play at the 2026 FIFA World Cup?
**Answer:** End of his career
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13843 — Chile (easy) — FAIL
**Q:** Why will Chile's 2026 World Cup squad differ from its 2014 team?
**Answer:** Aging golden generation
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

### Row 13845 — Chile (easy) — FAIL
**Q:** Why will Chile's 2026 World Cup squad look so different?
**Answer:** A new generation
**Why it fails:** False premise: Chile failed to qualify for the 2026 World Cup (finished last in CONMEBOL), so no Chilean player will feature at it and there is no 2026 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Re-anchor to the 2026 qualifying campaign (which happened) or drop the claim of playing at the tournament.

## Egypt — rows 22766–23686 (new method) — 104 failed-liveness

### Row 22779 — Egypt (medium) — FAIL
**Q:** At the 2022 World Cup, which Egyptian star had previously won two Premier League Golden Boots?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 22781 — Egypt (hard) — FAIL
**Q:** At which FIFA World Cup did Egypt fail to qualify, unlike these other tournaments?
**Answer:** 2022 FIFA World Cup
**Why it fails:** Non-unique/false framing: Egypt also failed to qualify for 2010 and 2014 (distractors), so '2022, unlike these other tournaments' is broken.
**Source:** https://en.wikipedia.org/wiki/Egypt_national_football_team
**Remedy:** Use distractors Egypt qualified for (e.g. 2018, 1990, 1934).

### Row 22807 — Egypt (easy) — FAIL
**Q:** Egypt lost the 2017 AFCON final by what score?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer (Excel date mangling): the cell shows a date in place of the scoreline (e.g. '02-Jan' = 2-1).
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations_Final
**Remedy:** Restore the real scoreline (the 2017 AFCON final was Cameroon 2-1 Egypt).

### Row 22809 — Egypt (easy) — FAIL
**Q:** Egypt lost the 2021 AFCON final to which nation on penalties?
**Answer:** Senegal
**Why it fails:** False: Egypt did NOT host the 2021 AFCON - Cameroon hosted it (played Jan-Feb 2022). Egypt hosted the 2019 AFCON. Egypt did lose the 2021 final to Senegal, but not as hosts.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** Remove the 'host/as hosts' framing for 2021 (Egypt hosted 2019, not 2021).

### Row 22824 — Egypt (medium) — FAIL
**Q:** Egypt's Al Ahly had how many CAF Champions League wins by the 2022 World Cup?
**Answer:** 12 titles
**Why it fails:** False/stale: Al Ahly reached 12 CAF Champions League titles only in 2024 (9th 2020, 10th 2021, 11th 2023, 12th 2024). They had NOT won 12 by the 2022 World Cup (10) or by 2023 (11).
**Source:** https://en.wikipedia.org/wiki/Al_Ahly_SC
**Remedy:** Drop the date qualifier or correct the count for that date.

### Row 22853 — Egypt (easy) — FAIL
**Q:** How did Egypt beat Ghana in the 2010 AFCON final?
**Answer:** On penalties
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 22854 — Egypt (easy) — FAIL
**Q:** How did Egypt lose the 2021 AFCON final as hosts?
**Answer:** On penalties
**Why it fails:** False: Egypt did NOT host the 2021 AFCON - Cameroon hosted it (played Jan-Feb 2022). Egypt hosted the 2019 AFCON. Egypt did lose the 2021 final to Senegal, but not as hosts.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** Remove the 'host/as hosts' framing for 2021 (Egypt hosted 2019, not 2021).

### Row 22867 — Egypt (medium) — FAIL
**Q:** How many CAF Champions League titles had Egypt's Al Ahly won by the 2022 World Cup?
**Answer:** 12 titles
**Why it fails:** False/stale: Al Ahly reached 12 CAF Champions League titles only in 2024 (9th 2020, 10th 2021, 11th 2023, 12th 2024). They had NOT won 12 by the 2022 World Cup (10) or by 2023 (11).
**Source:** https://en.wikipedia.org/wiki/Al_Ahly_SC
**Remedy:** Drop the date qualifier or correct the count for that date.

### Row 22869 — Egypt (medium) — FAIL
**Q:** How many CAF Champions Leagues had Egypt's Al Ahly won by 2023?
**Answer:** 12 titles
**Why it fails:** False/stale: Al Ahly reached 12 CAF Champions League titles only in 2024 (9th 2020, 10th 2021, 11th 2023, 12th 2024). They had NOT won 12 by the 2022 World Cup (10) or by 2023 (11).
**Source:** https://en.wikipedia.org/wiki/Al_Ahly_SC
**Remedy:** Drop the date qualifier or correct the count for that date.

### Row 22874 — Egypt (hard) — FAIL
**Q:** How many Premier League Golden Boots had Egypt's Mohamed Salah won by the 2022 World Cup?
**Answer:** Two
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 22875 — Egypt (hard) — FAIL
**Q:** How many Premier League Golden Boots has Egypt's Mohamed Salah won with Liverpool?
**Answer:** Two
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 22877 — Egypt (hard) — FAIL
**Q:** How many times did Egypt's Mohamed Salah win the Premier League Golden Boot with Liverpool?
**Answer:** Twice
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 22878 — Egypt (hard) — FAIL
**Q:** How many times had Egypt's Mohamed Salah won the Premier League Golden Boot by 2022?
**Answer:** Twice
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 22887 — Egypt (easy) — FAIL
**Q:** In Egypt's 2010 AFCON final win, who did they beat on penalties?
**Answer:** Ghana
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 22888 — Egypt (medium) — FAIL
**Q:** In Egypt's 2018 World Cup group stage match against Saudi Arabia, which Egyptian attacker was a key AFCON performer?
**Answer:** Trézéguet
**Why it fails:** Non-unique: Mohamed Salah (a distractor) is also a key Egypt attacker at the AFCON, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mahmoud_Hassan_(footballer)
**Remedy:** Remove Mohamed Salah from the options or specify a trait unique to Trezeguet.

### Row 22895 — Egypt (easy) — FAIL
**Q:** In the 2017 AFCON final, what was Cameroon's winning score against Egypt?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer (Excel date mangling): the cell shows a date in place of the scoreline (e.g. '02-Jan' = 2-1).
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations_Final
**Remedy:** Restore the real scoreline (the 2017 AFCON final was Cameroon 2-1 Egypt).

### Row 22896 — Egypt (easy) — FAIL
**Q:** In the 2017 AFCON final, what was Egypt's final score against Cameroon?
**Answer:** 01-Feb
**Why it fails:** Corrupted answer (Excel date mangling): the cell shows a date in place of the scoreline (e.g. '02-Jan' = 2-1).
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations_Final
**Remedy:** Restore the real scoreline (the 2017 AFCON final was Cameroon 2-1 Egypt).

### Row 22904 — Egypt (medium) — FAIL
**Q:** In what year did Egypt win the AFCON by beating Ghana on penalties?
**Answer:** 2010
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 22924 — Egypt (medium) — FAIL
**Q:** In which year did Carlos Queiroz manage the Egypt national team?
**Answer:** 2022
**Why it fails:** False: Carlos Queiroz was appointed Egypt manager in September 2021 (he led the 2021 AFCON in Jan 2022 and the March 2022 WC playoff), not 'appointed in 2022'.
**Source:** https://en.wikipedia.org/wiki/Carlos_Queiroz
**Remedy:** Change to 2021 (appointed), or rephrase.

### Row 22927 — Egypt (medium) — FAIL
**Q:** In which year did Egypt host and lose the AFCON final?
**Answer:** 2021
**Why it fails:** False: Egypt did NOT host the 2021 AFCON - Cameroon hosted it (played Jan-Feb 2022). Egypt hosted the 2019 AFCON. Egypt did lose the 2021 final to Senegal, but not as hosts.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** Remove the 'host/as hosts' framing for 2021 (Egypt hosted 2019, not 2021).

### Row 22928 — Egypt (medium) — FAIL
**Q:** In which year did Egypt host the AFCON final they lost to Senegal?
**Answer:** 2021
**Why it fails:** False: Egypt did NOT host the 2021 AFCON - Cameroon hosted it (played Jan-Feb 2022). Egypt hosted the 2019 AFCON. Egypt did lose the 2021 final to Senegal, but not as hosts.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** Remove the 'host/as hosts' framing for 2021 (Egypt hosted 2019, not 2021).

### Row 22933 — Egypt (medium) — FAIL
**Q:** In which year did Egypt lose the AFCON final as hosts?
**Answer:** 2021
**Why it fails:** False: Egypt did NOT host the 2021 AFCON - Cameroon hosted it (played Jan-Feb 2022). Egypt hosted the 2019 AFCON. Egypt did lose the 2021 final to Senegal, but not as hosts.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** Remove the 'host/as hosts' framing for 2021 (Egypt hosted 2019, not 2021).

### Row 22942 — Egypt (medium) — FAIL
**Q:** In which year did Egypt reach the AFCON final as hosts?
**Answer:** 2021
**Why it fails:** False: Egypt did NOT host the 2021 AFCON - Cameroon hosted it (played Jan-Feb 2022). Egypt hosted the 2019 AFCON. Egypt did lose the 2021 final to Senegal, but not as hosts.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** Remove the 'host/as hosts' framing for 2021 (Egypt hosted 2019, not 2021).

### Row 22947 — Egypt (medium) — FAIL
**Q:** In which year were Egypt AFCON hosts and finalists?
**Answer:** 2021
**Why it fails:** False: Egypt did NOT host the 2021 AFCON - Cameroon hosted it (played Jan-Feb 2022). Egypt hosted the 2019 AFCON. Egypt did lose the 2021 final to Senegal, but not as hosts.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** Remove the 'host/as hosts' framing for 2021 (Egypt hosted 2019, not 2021).

### Row 22966 — Egypt (medium) — FAIL
**Q:** When did Egypt beat Ghana in an AFCON final on penalties?
**Answer:** 2010
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 22967 — Egypt (medium) — FAIL
**Q:** When did Egypt beat Ghana in an AFCON final?
**Answer:** 2010
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 22969 — Egypt (medium) — FAIL
**Q:** When did Egypt host and lose the AFCON final to Senegal?
**Answer:** 2021
**Why it fails:** False: Egypt did NOT host the 2021 AFCON - Cameroon hosted it (played Jan-Feb 2022). Egypt hosted the 2019 AFCON. Egypt did lose the 2021 final to Senegal, but not as hosts.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** Remove the 'host/as hosts' framing for 2021 (Egypt hosted 2019, not 2021).

### Row 22970 — Egypt (medium) — FAIL
**Q:** When did Egypt host the AFCON final they lost to Senegal?
**Answer:** 2021
**Why it fails:** False: Egypt did NOT host the 2021 AFCON - Cameroon hosted it (played Jan-Feb 2022). Egypt hosted the 2019 AFCON. Egypt did lose the 2021 final to Senegal, but not as hosts.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** Remove the 'host/as hosts' framing for 2021 (Egypt hosted 2019, not 2021).

### Row 22986 — Egypt (medium) — FAIL
**Q:** When did Egypt win the Africa Cup of Nations by beating Ghana on penalties?
**Answer:** 2010
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 22987 — Egypt (medium) — FAIL
**Q:** When did Egypt, as hosts, reach the AFCON final?
**Answer:** 2021
**Why it fails:** False: Egypt did NOT host the 2021 AFCON - Cameroon hosted it (played Jan-Feb 2022). Egypt hosted the 2019 AFCON. Egypt did lose the 2021 final to Senegal, but not as hosts.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** Remove the 'host/as hosts' framing for 2021 (Egypt hosted 2019, not 2021).

### Row 23008 — Egypt (easy) — FAIL
**Q:** Where did Egypt's Mohamed Salah score his 2018 World Cup goal?
**Answer:** Against Saudi Arabia
**Why it fails:** False: Salah scored TWO goals at the 2018 World Cup (a penalty vs Russia and one vs Saudi Arabia), so 'his only goal of the tournament, vs Saudi Arabia' is wrong.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** He scored vs Russia and vs Saudi Arabia - drop 'only'.

### Row 23012 — Egypt (easy) — FAIL
**Q:** Which 2021 AFCON final did Egypt lose as hosts?
**Answer:** Final vs Senegal
**Why it fails:** False: Egypt did NOT host the 2021 AFCON - Cameroon hosted it (played Jan-Feb 2022). Egypt hosted the 2019 AFCON. Egypt did lose the 2021 final to Senegal, but not as hosts.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** Remove the 'host/as hosts' framing for 2021 (Egypt hosted 2019, not 2021).

### Row 23028 — Egypt (easy) — FAIL
**Q:** Which African nation did Egypt defeat in the 2010 AFCON final?
**Answer:** Ghana
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 23086 — Egypt (easy) — FAIL
**Q:** Which CAF nation, like Egypt in 2026, qualified for the 2018 World Cup?
**Answer:** Egypt
**Why it fails:** Self-referential/non-unique: the answer 'Egypt' restates the subject, and Senegal/Nigeria/Morocco (distractors) all also qualified for 2018.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Drop or rephrase.

### Row 23097 — Egypt (medium) — FAIL
**Q:** Which CAF team qualified for the 2026 World Cup through CAF qualification like Egypt?
**Answer:** Egypt
**Why it fails:** Self-referential/non-unique: the answer 'Egypt' restates the subject, and Morocco/Senegal (distractors) also qualified for 2026.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Drop or rephrase.

### Row 23102 — Egypt (easy) — FAIL
**Q:** Which Egypt attacker was a key AFCON player before his 2018 World Cup debut?
**Answer:** Trézéguet
**Why it fails:** Non-unique: Mohamed Salah (a distractor) is also a key Egypt attacker at the AFCON, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mahmoud_Hassan_(footballer)
**Remedy:** Remove Mohamed Salah from the options or specify a trait unique to Trezeguet.

### Row 23104 — Egypt (easy) — FAIL
**Q:** Which Egypt attacker was a key player in the 2021 Africa Cup of Nations?
**Answer:** Trézéguet
**Why it fails:** Non-unique: Mohamed Salah (a distractor) is also a key Egypt attacker at the AFCON, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mahmoud_Hassan_(footballer)
**Remedy:** Remove Mohamed Salah from the options or specify a trait unique to Trezeguet.

### Row 23105 — Egypt (easy) — FAIL
**Q:** Which Egypt attacker was key at AFCON before 2018 World Cup qualifying?
**Answer:** Trézéguet
**Why it fails:** Non-unique: Mohamed Salah (a distractor) is also a key Egypt attacker at the AFCON, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mahmoud_Hassan_(footballer)
**Remedy:** Remove Mohamed Salah from the options or specify a trait unique to Trezeguet.

### Row 23106 — Egypt (easy) — FAIL
**Q:** Which Egypt attacker was key at AFCON before the 2018 World Cup?
**Answer:** Trézéguet
**Why it fails:** Non-unique: Mohamed Salah (a distractor) is also a key Egypt attacker at the AFCON, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mahmoud_Hassan_(footballer)
**Remedy:** Remove Mohamed Salah from the options or specify a trait unique to Trezeguet.

### Row 23107 — Egypt (easy) — FAIL
**Q:** Which Egypt attacker was key at AFCON tournaments?
**Answer:** Trézéguet
**Why it fails:** Non-unique: Mohamed Salah (a distractor) is also a key Egypt attacker at the AFCON, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mahmoud_Hassan_(footballer)
**Remedy:** Remove Mohamed Salah from the options or specify a trait unique to Trezeguet.

### Row 23108 — Egypt (easy) — FAIL
**Q:** Which Egypt attacker was key at the 2019 AFCON?
**Answer:** Trézéguet
**Why it fails:** Non-unique: Mohamed Salah (a distractor) is also a key Egypt attacker at the AFCON, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mahmoud_Hassan_(footballer)
**Remedy:** Remove Mohamed Salah from the options or specify a trait unique to Trezeguet.

### Row 23109 — Egypt (easy) — FAIL
**Q:** Which Egypt attacker was key at the 2019 Africa Cup of Nations?
**Answer:** Trézéguet
**Why it fails:** Non-unique: Mohamed Salah (a distractor) is also a key Egypt attacker at the AFCON, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mahmoud_Hassan_(footballer)
**Remedy:** Remove Mohamed Salah from the options or specify a trait unique to Trezeguet.

### Row 23111 — Egypt (medium) — FAIL
**Q:** Which Egypt attacker was key in AFCON knockout stages before the 2022 World Cup?
**Answer:** Trézéguet
**Why it fails:** Non-unique: Mohamed Salah (a distractor) is also a key Egypt attacker at the AFCON, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mahmoud_Hassan_(footballer)
**Remedy:** Remove Mohamed Salah from the options or specify a trait unique to Trezeguet.

### Row 23113 — Egypt (easy) — FAIL
**Q:** Which Egypt attacker was key in the 2017 and 2021 AFCON tournaments?
**Answer:** Trézéguet
**Why it fails:** Non-unique: Mohamed Salah (a distractor) is also a key Egypt attacker at the AFCON, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mahmoud_Hassan_(footballer)
**Remedy:** Remove Mohamed Salah from the options or specify a trait unique to Trezeguet.

### Row 23114 — Egypt (easy) — FAIL
**Q:** Which Egypt attacker was key in their 2019 AFCON run?
**Answer:** Trézéguet
**Why it fails:** Non-unique: Mohamed Salah (a distractor) is also a key Egypt attacker at the AFCON, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mahmoud_Hassan_(footballer)
**Remedy:** Remove Mohamed Salah from the options or specify a trait unique to Trezeguet.

### Row 23115 — Egypt (easy) — FAIL
**Q:** Which Egypt attacker was key to their 2019 AFCON final run?
**Answer:** Trézéguet
**Why it fails:** Non-unique: Mohamed Salah (a distractor) is also a key Egypt attacker at the AFCON, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mahmoud_Hassan_(footballer)
**Remedy:** Remove Mohamed Salah from the options or specify a trait unique to Trezeguet.

### Row 23117 — Egypt (easy) — FAIL
**Q:** Which Egypt club is NOT one of Africa's two biggest, per their league?
**Answer:** Pyramids FC
**Why it fails:** Non-unique: two of the four options are NOT among Egypt's two biggest clubs (Al Ahly & Zamalek), so more than one answer is correct.
**Source:** https://en.wikipedia.org/wiki/Egypt_national_football_team
**Remedy:** Leave only one non-(Ahly/Zamalek) club among the options.

### Row 23120 — Egypt (medium) — FAIL
**Q:** Which Egypt forward won the Premier League Golden Boot twice before the 2022 World Cup?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23121 — Egypt (medium) — FAIL
**Q:** Which Egypt forward won the Premier League Golden Boot twice with Liverpool?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23122 — Egypt (medium) — FAIL
**Q:** Which Egypt forward won the Premier League Golden Boot twice?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23132 — Egypt (easy) — FAIL
**Q:** Which Egypt manager did NOT win the AFCON title in 2008?
**Answer:** Carlos Queiroz
**Why it fails:** Non-unique: three of the four managers did not win the 2008 AFCON (only Hassan Shehata did), so the 'did NOT win' answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Hassan_Shehata
**Remedy:** Make the distractors all 2008 winners except one.

### Row 23144 — Egypt (easy) — FAIL
**Q:** Which Egypt midfielder earned over 100 caps before the 2022 World Cup?
**Answer:** Mohamed Elneny
**Why it fails:** Non-unique: Ahmed Hassan (a distractor) is a midfielder with 184 caps - also 'over 100 caps' - so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Elneny
**Remedy:** Remove Ahmed Hassan, or add a qualifier (e.g. 'played for Arsenal') that uniquely identifies Elneny.

### Row 23145 — Egypt (easy) — FAIL
**Q:** Which Egypt midfielder earned over 100 caps for his country?
**Answer:** Mohamed Elneny
**Why it fails:** Non-unique: Ahmed Hassan (a distractor) is a midfielder with 184 caps - also 'over 100 caps' - so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Elneny
**Remedy:** Remove Ahmed Hassan, or add a qualifier (e.g. 'played for Arsenal') that uniquely identifies Elneny.

### Row 23146 — Egypt (easy) — FAIL
**Q:** Which Egypt midfielder had over 100 caps before the 2022 FIFA World Cup?
**Answer:** Mohamed Elneny
**Why it fails:** Non-unique: Ahmed Hassan (a distractor) is a midfielder with 184 caps - also 'over 100 caps' - so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Elneny
**Remedy:** Remove Ahmed Hassan, or add a qualifier (e.g. 'played for Arsenal') that uniquely identifies Elneny.

### Row 23147 — Egypt (easy) — FAIL
**Q:** Which Egypt midfielder had over 100 caps by 2024?
**Answer:** Mohamed Elneny
**Why it fails:** Non-unique: Ahmed Hassan (a distractor) is a midfielder with 184 caps - also 'over 100 caps' - so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Elneny
**Remedy:** Remove Ahmed Hassan, or add a qualifier (e.g. 'played for Arsenal') that uniquely identifies Elneny.

### Row 23148 — Egypt (easy) — FAIL
**Q:** Which Egypt midfielder had over 100 caps for his national team?
**Answer:** Mohamed Elneny
**Why it fails:** Non-unique: Ahmed Hassan (a distractor) is a midfielder with 184 caps - also 'over 100 caps' - so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Elneny
**Remedy:** Remove Ahmed Hassan, or add a qualifier (e.g. 'played for Arsenal') that uniquely identifies Elneny.

### Row 23158 — Egypt (easy) — FAIL
**Q:** Which Egypt opponent lost the 2010 AFCON final on penalties?
**Answer:** Ghana
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 23225 — Egypt (medium) — FAIL
**Q:** Which Egypt player won the Premier League Golden Boot twice before 2022 World Cup qualifiers?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23226 — Egypt (medium) — FAIL
**Q:** Which Egypt player won the Premier League Golden Boot twice with Liverpool?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23227 — Egypt (medium) — FAIL
**Q:** Which Egypt player won the Premier League Golden Boot twice?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23229 — Egypt (medium) — FAIL
**Q:** Which Egypt player won two Premier League Golden Boots with Liverpool?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23246 — Egypt (medium) — FAIL
**Q:** Which Egypt star won more Premier League Golden Boots before the 2022 World Cup?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23248 — Egypt (medium) — FAIL
**Q:** Which Egypt star won the Premier League Golden Boot twice?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23249 — Egypt (medium) — FAIL
**Q:** Which Egypt star won two Premier League Golden Boots?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23252 — Egypt (medium) — FAIL
**Q:** Which Egypt star's two Premier League Golden Boots are a World Cup-era record for an African player?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23253 — Egypt (medium) — FAIL
**Q:** Which Egypt star's two Premier League Golden Boots preceded the 2018 World Cup?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23254 — Egypt (easy) — FAIL
**Q:** Which Egypt team lost a 2021 final to Senegal on penalties?
**Answer:** The host nation
**Why it fails:** False: Egypt did NOT host the 2021 AFCON - Cameroon hosted it (played Jan-Feb 2022). Egypt hosted the 2019 AFCON. Egypt did lose the 2021 final to Senegal, but not as hosts.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** Remove the 'host/as hosts' framing for 2021 (Egypt hosted 2019, not 2021).

### Row 23258 — Egypt (easy) — FAIL
**Q:** Which Egyptian attacker was a key player at AFCON tournaments during 2010s World Cup cycles?
**Answer:** Trézéguet
**Why it fails:** Non-unique: Mohamed Salah (a distractor) is also a key Egypt attacker at the AFCON, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mahmoud_Hassan_(footballer)
**Remedy:** Remove Mohamed Salah from the options or specify a trait unique to Trezeguet.

### Row 23259 — Egypt (easy) — FAIL
**Q:** Which Egyptian attacker was a key player at AFCON tournaments?
**Answer:** Trézéguet
**Why it fails:** Non-unique: Mohamed Salah (a distractor) is also a key Egypt attacker at the AFCON, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mahmoud_Hassan_(footballer)
**Remedy:** Remove Mohamed Salah from the options or specify a trait unique to Trezeguet.

### Row 23260 — Egypt (easy) — FAIL
**Q:** Which Egyptian attacker was crucial in AFCONs before their 2018 World Cup qualifiers?
**Answer:** Trézéguet
**Why it fails:** Non-unique: Mohamed Salah (a distractor) is also a key Egypt attacker at the AFCON, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mahmoud_Hassan_(footballer)
**Remedy:** Remove Mohamed Salah from the options or specify a trait unique to Trezeguet.

### Row 23263 — Egypt (easy) — FAIL
**Q:** Which Egyptian attacker was key at AFCON tournaments before the 2018 World Cup?
**Answer:** Trézéguet
**Why it fails:** Non-unique: Mohamed Salah (a distractor) is also a key Egypt attacker at the AFCON, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mahmoud_Hassan_(footballer)
**Remedy:** Remove Mohamed Salah from the options or specify a trait unique to Trezeguet.

### Row 23266 — Egypt (easy) — FAIL
**Q:** Which Egyptian club had the most CAF Champions League wins before the 2022 World Cup?
**Answer:** Al Ahly
**Why it fails:** False/stale: Al Ahly reached 12 CAF Champions League titles only in 2024 (9th 2020, 10th 2021, 11th 2023, 12th 2024). They had NOT won 12 by the 2022 World Cup (10) or by 2023 (11).
**Source:** https://en.wikipedia.org/wiki/Al_Ahly_SC
**Remedy:** Drop the date qualifier or correct the count for that date.

### Row 23267 — Egypt (easy) — FAIL
**Q:** Which Egyptian club had won 12 CAF Champions League titles by 2022?
**Answer:** Al Ahly
**Why it fails:** False/stale: Al Ahly reached 12 CAF Champions League titles only in 2024 (9th 2020, 10th 2021, 11th 2023, 12th 2024). They had NOT won 12 by the 2022 World Cup (10) or by 2023 (11).
**Source:** https://en.wikipedia.org/wiki/Al_Ahly_SC
**Remedy:** Drop the date qualifier or correct the count for that date.

### Row 23268 — Egypt (easy) — FAIL
**Q:** Which Egyptian club had won the most CAF Champions League titles by the 2019 AFCON?
**Answer:** Al Ahly
**Why it fails:** False/stale: Al Ahly reached 12 CAF Champions League titles only in 2024 (9th 2020, 10th 2021, 11th 2023, 12th 2024). They had NOT won 12 by the 2022 World Cup (10) or by 2023 (11).
**Source:** https://en.wikipedia.org/wiki/Al_Ahly_SC
**Remedy:** Drop the date qualifier or correct the count for that date.

### Row 23270 — Egypt (easy) — FAIL
**Q:** Which Egyptian club has NOT won the CAF Champions League a record 12 times?
**Answer:** Zamalek
**Why it fails:** Non-unique: every club except Al Ahly has NOT won 12 CAF Champions League titles, so multiple options are correct.
**Source:** https://en.wikipedia.org/wiki/Al_Ahly_SC
**Remedy:** Rephrase to a uniquely identifying fact.

### Row 23297 — Egypt (medium) — FAIL
**Q:** Which Egyptian forward won the Premier League Golden Boot twice?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23319 — Egypt (easy) — FAIL
**Q:** Which Egyptian midfielder had over 100 caps before the 2022 World Cup?
**Answer:** Mohamed Elneny
**Why it fails:** Non-unique: Ahmed Hassan (a distractor) is a midfielder with 184 caps - also 'over 100 caps' - so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mohamed_Elneny
**Remedy:** Remove Ahmed Hassan, or add a qualifier (e.g. 'played for Arsenal') that uniquely identifies Elneny.

### Row 23333 — Egypt (medium) — FAIL
**Q:** Which Egyptian player had also won the Premier League Golden Boot by the 2022 World Cup?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23336 — Egypt (medium) — FAIL
**Q:** Which Egyptian player had won two Premier League Golden Boots before the 2018 World Cup?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23360 — Egypt (easy) — FAIL
**Q:** Which Egyptian player was a key attacker at the 2019 Africa Cup of Nations?
**Answer:** Trézéguet
**Why it fails:** Non-unique: Mohamed Salah (a distractor) is also a key Egypt attacker at the AFCON, so the answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Mahmoud_Hassan_(footballer)
**Remedy:** Remove Mohamed Salah from the options or specify a trait unique to Trezeguet.

### Row 23365 — Egypt (medium) — FAIL
**Q:** Which Egyptian player won the Premier League Golden Boot twice with Liverpool?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23366 — Egypt (medium) — FAIL
**Q:** Which Egyptian player won the Premier League Golden Boot twice?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23367 — Egypt (medium) — FAIL
**Q:** Which Egyptian player won two Premier League Golden Boots before the 2022 World Cup?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23371 — Egypt (medium) — FAIL
**Q:** Which Egyptian player's club form earned him two Premier League Golden Boots?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23398 — Egypt (easy) — FAIL
**Q:** Which Egyptian stadium was NOT the primary venue for the 2019 Africa Cup of Nations?
**Answer:** Borg El Arab Stadium
**Why it fails:** Non-unique: Cairo International was the primary 2019 AFCON venue; the other three options were all 'not primary', so more than one answer fits.
**Source:** https://en.wikipedia.org/wiki/2019_Africa_Cup_of_Nations
**Remedy:** Leave only one non-primary venue among the options.

### Row 23410 — Egypt (medium) — FAIL
**Q:** Which Egyptian star twice won the Premier League Golden Boot?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23414 — Egypt (medium) — FAIL
**Q:** Which Egyptian star won the Premier League Golden Boot twice with Liverpool before the 2022 World Cup?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23417 — Egypt (medium) — FAIL
**Q:** Which Egyptian's club achievements include two Premier League Golden Boots?
**Answer:** Mohamed Salah
**Why it fails:** False/stale count: Mohamed Salah has won the Premier League Golden Boot FOUR times (2017-18, 2018-19, 2021-22, 2024-25) - three of them by the 2022 World Cup - not 'twice'.
**Source:** https://en.wikipedia.org/wiki/Premier_League_Golden_Boot
**Remedy:** Update the count (4 total; 3 by 2022) or drop the 'twice/two' framing.

### Row 23475 — Egypt (easy) — FAIL
**Q:** Which nation beat host nation Egypt in the 2021 AFCON final?
**Answer:** Senegal
**Why it fails:** False: Egypt did NOT host the 2021 AFCON - Cameroon hosted it (played Jan-Feb 2022). Egypt hosted the 2019 AFCON. Egypt did lose the 2021 final to Senegal, but not as hosts.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations_final
**Remedy:** Remove the 'host/as hosts' framing for 2021 (Egypt hosted 2019, not 2021).

### Row 23485 — Egypt (easy) — FAIL
**Q:** Which nation did Egypt beat in the 2010 AFCON final?
**Answer:** Ghana
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 23486 — Egypt (easy) — FAIL
**Q:** Which nation did Egypt beat in the 2010 Africa Cup of Nations final?
**Answer:** Ghana
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 23488 — Egypt (easy) — FAIL
**Q:** Which nation did Egypt beat on penalties in the 2010 AFCON final?
**Answer:** Ghana
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 23490 — Egypt (easy) — FAIL
**Q:** Which nation did Egypt defeat on penalties in the 2010 AFCON final?
**Answer:** Ghana
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 23526 — Egypt (easy) — FAIL
**Q:** Which nation lost the 2010 AFCON final to Egypt on penalties?
**Answer:** Ghana
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 23537 — Egypt (easy) — FAIL
**Q:** Which nation, like Egypt, qualified for the 2018 World Cup via CAF?
**Answer:** Nigeria
**Why it fails:** Non-unique: Nigeria, Senegal, Morocco and Tunisia ALL qualified for the 2018 World Cup via CAF, so every option is correct.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Use a distractor set where only one nation qualified for 2018.

### Row 23550 — Egypt (easy) — FAIL
**Q:** Which of these AFCON winners, unlike Egypt, has not won it seven times?
**Answer:** Nigeria
**Why it fails:** Non-unique: none of Nigeria/Cameroon/Ghana/Ivory Coast has won the AFCON seven times, so multiple options fit 'not seven'.
**Source:** https://en.wikipedia.org/wiki/Egypt_at_the_Africa_Cup_of_Nations
**Remedy:** Rephrase to a unique fact.

### Row 23552 — Egypt (easy) — FAIL
**Q:** Which of these clubs is NOT one of the two biggest in Egypt's top league?
**Answer:** Ismaily SC
**Why it fails:** Non-unique: two of the four options are NOT among Egypt's two biggest clubs (Al Ahly & Zamalek), so more than one answer is correct.
**Source:** https://en.wikipedia.org/wiki/Egypt_national_football_team
**Remedy:** Leave only one non-(Ahly/Zamalek) club among the options.

### Row 23599 — Egypt (easy) — FAIL
**Q:** Which team did Egypt beat in the 2010 AFCON final?
**Answer:** Ghana
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 23600 — Egypt (easy) — FAIL
**Q:** Which team did Egypt beat on penalties in the 2010 AFCON final?
**Answer:** Ghana
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 23601 — Egypt (easy) — FAIL
**Q:** Which team did Egypt defeat in the 2010 Africa Cup of Nations final?
**Answer:** Ghana
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 23602 — Egypt (easy) — FAIL
**Q:** Which team did Egypt defeat on penalties in the 2010 AFCON final?
**Answer:** Ghana
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 23619 — Egypt (easy) — FAIL
**Q:** Which team lost to Egypt in the 2010 Africa Cup of Nations final on penalties?
**Answer:** Ghana
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

### Row 23633 — Egypt (hard) — FAIL
**Q:** Which World Cup did Egypt's CAF qualification not secure?
**Answer:** 2022 World Cup
**Why it fails:** Non-unique: Egypt's CAF qualification also failed for 2010 and 2014 (distractors), not only 2022, so more than one option is correct.
**Source:** https://en.wikipedia.org/wiki/Egypt_national_football_team
**Remedy:** Use distractors Egypt actually qualified for.

### Row 23648 — Egypt (easy) — FAIL
**Q:** Who did Egypt beat on penalties in the 2010 AFCON final?
**Answer:** Ghana
**Why it fails:** False: Egypt beat Ghana 1-0 in the 2010 AFCON final (Gedo, 85'), NOT on penalties. Egypt's penalty-shootout AFCON final win was 2006 vs Cote d'Ivoire.
**Source:** https://en.wikipedia.org/wiki/2010_Africa_Cup_of_Nations_Final
**Remedy:** Drop 'on penalties' (the 2010 final was 1-0); use 2006 vs Cote d'Ivoire for a penalty-shootout final.

## Germany — rows 27325–29161 (new method) — 65 failed-liveness

### Row 27367 — Germany (easy) — FAIL
**Q:** At Euro 2012, Germany lost to Italy by what score?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27374 — Germany (medium) — FAIL
**Q:** At Euro 2024, Germany set a record for a host nation's biggest opening win. What was the score?
**Answer:** 05-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27384 — Germany (easy) — FAIL
**Q:** At the 2010 FIFA World Cup, Germany beat England in the round of 16 by what score?
**Answer:** 04-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27389 — Germany (easy) — FAIL
**Q:** At the 2014 FIFA World Cup, what was Germany's semi-final score against Brazil?
**Answer:** 07-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27406 — Germany (easy) — FAIL
**Q:** At the 2022 World Cup, Germany led Japan at half-time but lost what final score?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27409 — Germany (easy) — FAIL
**Q:** At the 2022 World Cup, what was the final score when Germany lost to Japan?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27470 — Germany (easy) — FAIL
**Q:** Germany beat Argentina 4-0 in 2010. Which rival did they NOT beat 4-0 in a World Cup quarter-final?
**Answer:** Brazil
**Why it fails:** Non-unique: Germany did not beat England, France OR Spain 4-0 in a World Cup quarter-final either, so several options equally fit 'not beaten 4-0 in a QF' (only Argentina, 2010).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Pick distractors Germany actually beat 4-0 in a QF.

### Row 27474 — Germany (easy) — FAIL
**Q:** Germany beat Scotland by what scoreline in the Euro 2024 opener?
**Answer:** 05-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27475 — Germany (easy) — FAIL
**Q:** Germany beat Scotland in their Euro 2024 opener by what score?
**Answer:** 05-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27476 — Germany (easy) — FAIL
**Q:** Germany beat Uruguay in the 2010 World Cup third-place play-off by what score?
**Answer:** 03-Feb
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27516 — Germany (hard) — FAIL
**Q:** Germany won the 2017 Confederations Cup, but which tournament did they also win between 2008 and 2026?
**Answer:** 2017 Confederations Cup
**Why it fails:** False/non-unique: Germany also won the 2014 World Cup (a distractor) within 2008-2026, so '2017 Confederations Cup was their only win' is wrong.
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Remove the 2014 World Cup option / fix the premise.

### Row 27523 — Germany (easy) — FAIL
**Q:** Germany's 2016 semi-final loss to France was 2-0. What was their 2010 World Cup win over England?
**Answer:** 04-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27539 — Germany (medium) — FAIL
**Q:** Germany's Bayern Munich won the UEFA Champions League in which two years?
**Answer:** 2013 and 2020
**Why it fails:** Non-unique: Bayern Munich also won the Champions League in 2001, so the distractor pair '2001 and 2013' is equally correct.
**Source:** https://en.wikipedia.org/wiki/FC_Bayern_Munich
**Remedy:** Use a distractor set with no Bayern UCL-winning year.

### Row 27543 — Germany (medium) — FAIL
**Q:** Germany's Euro 2020 exit was earlier than their Euro 2024 exit by how many rounds?
**Answer:** Two rounds
**Why it fails:** False: the round of 16 (Euro 2020) and the quarter-final (Euro 2024) are ONE round apart, not two.
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Change the answer to 'one round'.

### Row 27606 — Germany (easy) — FAIL
**Q:** In Germany's 2026 World Cup campaign, which veteran midfielder did manager Julian Nagelsmann recall to the squad?
**Answer:** Toni Kroos
**Why it fails:** False: Toni Kroos retired from football after Euro 2024 and was NOT part of Germany's 2026 World Cup squad/campaign (he came back only for Euro 2024).
**Source:** https://en.wikipedia.org/wiki/Toni_Kroos
**Remedy:** Re-anchor Kroos to Euro 2024, or name a player actually in the 2026 squad.

### Row 27609 — Germany (easy) — FAIL
**Q:** In Germany's Euro 2024 quarter-final loss, which scorer's goal came later?
**Answer:** Niclas Füllkrug
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 27610 — Germany (easy) — FAIL
**Q:** In Germany's Euro 2024 quarter-final, who scored the winner after Füllkrug's equaliser?
**Answer:** Mikel Oyarzabal
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 27612 — Germany (easy) — FAIL
**Q:** In the 2010 World Cup round of 16, Germany beat England by what scoreline?
**Answer:** 04-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27617 — Germany (easy) — FAIL
**Q:** In the 2014 World Cup semi-final, what was Germany's final score against Brazil?
**Answer:** 07-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27633 — Germany (easy) — FAIL
**Q:** In which Euro 2024 match did Germany's Niclas Füllkrug score a late equaliser?
**Answer:** Quarter-final vs Spain
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 27659 — Germany (medium) — FAIL
**Q:** In which tournament's quarter-final did Germany lose to Spain after a late Füllkrug equaliser?
**Answer:** Euro 2024
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 27740 — Germany (easy) — FAIL
**Q:** What was Germany's margin of victory over England in the 2010 World Cup round of 16?
**Answer:** 04-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27745 — Germany (easy) — FAIL
**Q:** What was Germany's winning score against Scotland in Euro 2024's opening match?
**Answer:** 05-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27746 — Germany (easy) — FAIL
**Q:** What was Germany's winning scoreline against England in the 2010 World Cup round of 16?
**Answer:** 04-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27747 — Germany (easy) — FAIL
**Q:** What was Germany's winning scoreline in their record-breaking Euro 2024 opener?
**Answer:** 05-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27749 — Germany (easy) — FAIL
**Q:** What was the final score when Germany beat England in the 2010 World Cup?
**Answer:** 04-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27752 — Germany (easy) — FAIL
**Q:** What was the final score when Germany lost to Italy in the Euro 2012 semi-final?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27753 — Germany (medium) — FAIL
**Q:** What was the final score when Germany lost to Japan in the 2022 World Cup group stage?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27758 — Germany (medium) — FAIL
**Q:** What was the score in Germany's Euro 2024 opening win over Scotland?
**Answer:** 05-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27760 — Germany (medium) — FAIL
**Q:** What was the score when Germany beat England in the 2010 World Cup round of 16?
**Answer:** 04-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27766 — Germany (medium) — FAIL
**Q:** What was the score when Germany lost to Spain at Euro 2024?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer (Excel date mangling): a scoreline is shown as a date (e.g. '07-Jan'=7-1, '02-Jan'=2-1, '04-Jan'=4-1, '05-Jan'=5-1, '03-Feb'=3-2).
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Restore the real scoreline as the answer.

### Row 27816 — Germany (easy) — FAIL
**Q:** When did Germany's Niclas Füllkrug equalise against Spain at Euro 2024?
**Answer:** In the quarter-final
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 28093 — Germany (easy) — FAIL
**Q:** Which German manager recalled Toni Kroos for the 2026 World Cup campaign?
**Answer:** Julian Nagelsmann
**Why it fails:** False: Toni Kroos retired from football after Euro 2024 and was NOT part of Germany's 2026 World Cup squad/campaign (he came back only for Euro 2024).
**Source:** https://en.wikipedia.org/wiki/Toni_Kroos
**Remedy:** Re-anchor Kroos to Euro 2024, or name a player actually in the 2026 squad.

### Row 28124 — Germany (easy) — FAIL
**Q:** Which German midfielder did Nagelsmann recall to build his 2026 World Cup team around?
**Answer:** Toni Kroos
**Why it fails:** False: Toni Kroos retired from football after Euro 2024 and was NOT part of Germany's 2026 World Cup squad/campaign (he came back only for Euro 2024).
**Source:** https://en.wikipedia.org/wiki/Toni_Kroos
**Remedy:** Re-anchor Kroos to Euro 2024, or name a player actually in the 2026 squad.

### Row 28229 — Germany (easy) — FAIL
**Q:** Which German player equalised late against Spain in the Euro 2024 quarter-final?
**Answer:** Niclas Füllkrug
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 28231 — Germany (easy) — FAIL
**Q:** Which German player equalised late versus Spain at Euro 2024?
**Answer:** Niclas Füllkrug
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 28235 — Germany (easy) — FAIL
**Q:** Which German player had fewer World Cup goals than Miroslav Klose's 16?
**Answer:** Thomas Müller
**Why it fails:** Non-unique: every German except Klose scored fewer than his 16 World Cup goals, so Gotze, Podolski and Schweinsteiger all fit 'fewer than 16' too.
**Source:** https://en.wikipedia.org/wiki/Miroslav_Klose
**Remedy:** Rephrase to a uniquely identifying fact.

### Row 28291 — Germany (easy) — FAIL
**Q:** Which German player scored a late Euro 2024 equaliser, like Khedira did in 2014?
**Answer:** Niclas Füllkrug
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 28304 — Germany (easy) — FAIL
**Q:** Which German player scored in the Euro 2024 quarter-final?
**Answer:** Niclas Füllkrug
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 28321 — Germany (easy) — FAIL
**Q:** Which German player scored the late equaliser against Spain at Euro 2024?
**Answer:** Niclas Füllkrug
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 28322 — Germany (easy) — FAIL
**Q:** Which German player scored the late equaliser against Spain in the Euro 2024 quarter-final?
**Answer:** Niclas Füllkrug
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 28480 — Germany (easy) — FAIL
**Q:** Which German stadium was not a Euro 2024 host venue?
**Answer:** Veltins-Arena Gelsenkirchen
**Why it fails:** False: the Veltins-Arena in Gelsenkirchen WAS one of the 10 Euro 2024 host venues.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024
**Remedy:** Pick a stadium that genuinely was not a Euro 2024 host.

### Row 28503 — Germany (easy) — FAIL
**Q:** Which German striker equalised late against Spain at Euro 2024?
**Answer:** Niclas Füllkrug
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 28509 — Germany (easy) — FAIL
**Q:** Which German striker scored a late equaliser vs Spain in Euro 2024?
**Answer:** Niclas Füllkrug
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 28571 — Germany (easy) — FAIL
**Q:** Which Germany forward scored an equaliser vs Spain at Euro 2024?
**Answer:** Niclas Füllkrug
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 28609 — Germany (easy) — FAIL
**Q:** Which Germany manager recalled Toni Kroos for the 2026 World Cup campaign?
**Answer:** Julian Nagelsmann
**Why it fails:** False: Toni Kroos retired from football after Euro 2024 and was NOT part of Germany's 2026 World Cup squad/campaign (he came back only for Euro 2024).
**Source:** https://en.wikipedia.org/wiki/Toni_Kroos
**Remedy:** Re-anchor Kroos to Euro 2024, or name a player actually in the 2026 squad.

### Row 28684 — Germany (easy) — FAIL
**Q:** Which Germany player scored a late equaliser against Spain at Euro 2024?
**Answer:** Niclas Füllkrug
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 28696 — Germany (easy) — FAIL
**Q:** Which Germany player scored the late equaliser vs Spain at Euro 2024?
**Answer:** Niclas Füllkrug
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 28793 — Germany (easy) — FAIL
**Q:** Which nation beat Germany in the 2010 World Cup round of 16?
**Answer:** Germany
**Why it fails:** Broken/self-referential: Germany were not beaten in the 2010 World Cup round of 16 - they beat England 4-1 - so the answer 'Germany' is nonsensical.
**Source:** https://en.wikipedia.org/wiki/2010_FIFA_World_Cup
**Remedy:** Fix: Germany beat England in the 2010 R16.

### Row 28838 — Germany (easy) — FAIL
**Q:** Which nation did Germany not defeat in a World Cup semi-final?
**Answer:** Argentina
**Why it fails:** Non-unique: Germany did not beat Spain or England in a World Cup semi-final either (they beat only Brazil, 2014), so several options fit 'not beaten in a WC SF'.
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Rephrase to a unique fact.

### Row 28839 — Germany (easy) — FAIL
**Q:** Which nation did Germany NOT finish behind in their 2022 World Cup group?
**Answer:** Costa Rica
**Why it fails:** Non-unique: Germany did not finish behind Costa Rica OR Brazil in their 2022 group (Brazil was not in Group E), so more than one option fits.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup
**Remedy:** Use only in-group teams as distractors.

### Row 28840 — Germany (easy) — FAIL
**Q:** Which nation did Germany NOT lose to in a knockout match at Euro 2016?
**Answer:** Argentina
**Why it fails:** Non-unique: at Euro 2016 Germany lost a knockout only to France; they did not lose to Italy or Spain either, so several options fit 'not lost to'.
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Rephrase to a unique fact.

### Row 28867 — Germany (easy) — FAIL
**Q:** Which nation has won more World Cup titles than Germany's four?
**Answer:** Brazil and Italy
**Why it fails:** False: Italy has 4 World Cup titles (equal to Germany, not more); only Brazil (5) has more, so 'Brazil and Italy' is wrong.
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** The only nation with more than Germany's 4 is Brazil (5).

### Row 28906 — Germany (easy) — FAIL
**Q:** Which opponent did Germany NOT face in a 2024 quarter-final?
**Answer:** Italy
**Why it fails:** Non-unique: Germany did not face France or England in the Euro 2024 quarter-final either (only Spain), so several options fit 'did NOT face'.
**Source:** https://en.wikipedia.org/wiki/Germany_national_football_team
**Remedy:** Rephrase to a unique fact.

### Row 28916 — Germany (easy) — FAIL
**Q:** Which Spain player scored the late winner against Germany in the Euro 2024 quarter-final?
**Answer:** Mikel Oyarzabal
**Why it fails:** False: Spain's Euro 2024 quarter-final winner v Germany was Mikel Merino (119'), not Mikel Oyarzabal (the equaliser was Wirtz, not Fullkrug).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Change the scorer to Mikel Merino.

### Row 28920 — Germany (easy) — FAIL
**Q:** Which Spain player scored the winning goal in the Euro 2024 quarter-final against Germany?
**Answer:** Mikel Oyarzabal
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 28981 — Germany (easy) — FAIL
**Q:** Which team did Germany NOT beat 8-0 in 2022 World Cup qualifying?
**Answer:** San Marino
**Why it fails:** Non-unique: Germany's only 8-0 win in 2022 qualifying was over Liechtenstein, so San Marino, Armenia and Iceland all equally fit 'not beaten 8-0'.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Rephrase to a unique fact.

### Row 28982 — Germany (easy) — FAIL
**Q:** Which team did Germany not beat by 8+ goals in their 2022 World Cup qualifying campaign?
**Answer:** North Macedonia
**Why it fails:** Non-unique: Germany beat only Liechtenstein 8-0 in 2022 qualifying, so Armenia and Iceland (and North Macedonia) all fit 'not beaten by 8+'.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Rephrase to a unique fact.

### Row 28983 — Germany (easy) — FAIL
**Q:** Which team did Germany NOT beat in a 2014 World Cup semi-final?
**Answer:** Argentina
**Why it fails:** Non-unique: Germany's only 2014 WC semi-final win was over Brazil, so Argentina, France and Italy all equally fit 'not beaten in a 2014 SF'.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup
**Remedy:** Rephrase to a unique fact.

### Row 28985 — Germany (easy) — FAIL
**Q:** Which team did Germany NOT defeat by 6+ goals at the 2014 World Cup?
**Answer:** Argentina
**Why it fails:** Non-unique: at the 2014 World Cup Germany beat only Brazil by 6+ (7-1), so Argentina, Portugal and France all fit 'not beaten by 6+'.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup
**Remedy:** Rephrase to a unique fact.

### Row 28986 — Germany (medium) — FAIL
**Q:** Which team did Germany NOT lose to in their 2018 World Cup group stage?
**Answer:** Sweden
**Why it fails:** Non-unique: Germany beat Sweden in the 2018 group but also did not face Japan there (Japan was 2022), so more than one option fits 'not lost to'.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Use only 2018 group opponents as distractors.

### Row 29071 — Germany (easy) — FAIL
**Q:** Which veteran did Julian Nagelsmann recall for Germany's 2026 World Cup squad?
**Answer:** Toni Kroos
**Why it fails:** False: Toni Kroos retired from football after Euro 2024 and was NOT part of Germany's 2026 World Cup squad/campaign (he came back only for Euro 2024).
**Source:** https://en.wikipedia.org/wiki/Toni_Kroos
**Remedy:** Re-anchor Kroos to Euro 2024, or name a player actually in the 2026 squad.

### Row 29072 — Germany (easy) — FAIL
**Q:** Which veteran midfielder did Julian Nagelsmann recall for Germany's 2026 World Cup campaign?
**Answer:** Toni Kroos
**Why it fails:** False: Toni Kroos retired from football after Euro 2024 and was NOT part of Germany's 2026 World Cup squad/campaign (he came back only for Euro 2024).
**Source:** https://en.wikipedia.org/wiki/Toni_Kroos
**Remedy:** Re-anchor Kroos to Euro 2024, or name a player actually in the 2026 squad.

### Row 29119 — Germany (easy) — FAIL
**Q:** Who scored Germany's late goal in their Euro 2024 quarter-final?
**Answer:** Niclas Füllkrug
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 29123 — Germany (easy) — FAIL
**Q:** Who scored Spain's winning goal against Germany in the Euro 2024 quarter-final?
**Answer:** Mikel Oyarzabal
**Why it fails:** False: in the Euro 2024 quarter-final (Spain 2-1 Germany, a.e.t.) Germany's equaliser was scored by Florian Wirtz (89'), NOT Niclas Fullkrug; Spain's winner was Mikel Merino (119'), not Oyarzabal.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2024_knockout_phase
**Remedy:** Correct the scorer - Wirtz equalised, Merino won it.

### Row 32570 — Italy (medium) — FAIL
**Q:** After Euro 2020, Italy's FIFA ranking was what number?
**Answer:** 7th
**Why it fails:** Wrong answer: after winning Euro 2020 Italy rose to 5th in the FIFA ranking (Aug 2021), not 7th. 7th was their PRE-tournament rank.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Change answer to 5th.

### Row 32571 — Italy (medium) — FAIL
**Q:** After failing in 2018 and 2022, which manager led Italy to 2026 World Cup qualification?
**Answer:** Luciano Spalletti
**Why it fails:** False premise: Italy did NOT qualify for the 2026 World Cup (lost the UEFA playoff final to Bosnia 1-1, 4-1 pens, Mar 2026 - third straight WC missed). Also Spalletti was sacked in June 2025; Gattuso led the failed playoff.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026; no manager led them there.

### Row 32575 — Italy (medium) — FAIL
**Q:** After Italy won Euro 2020, what FIFA ranking did they achieve?
**Answer:** 7th
**Why it fails:** Wrong answer: Italy reached 5th after Euro 2020 (Aug 2021), not 7th.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Change answer to 5th.

### Row 32576 — Italy (medium) — FAIL
**Q:** After Italy won Euro 2020, what was their new FIFA ranking?
**Answer:** 7th
**Why it fails:** Wrong answer: Italy's new ranking after Euro 2020 was 5th, not 7th.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Change answer to 5th.

### Row 32586 — Italy (medium) — FAIL
**Q:** After Italy's Euro 2024, when did Roberto Mancini resign?
**Answer:** Aug-23
**Why it fails:** Temporal contradiction: Mancini resigned in August 2023 - BEFORE Euro 2024 (June 2024), which he did not even manage. The 'After Italy's Euro 2024' framing is false.
**Source:** https://en.wikipedia.org/wiki/Roberto_Mancini
**Remedy:** Drop the 'after Euro 2024' framing (resignation was Aug 2023).

### Row 32592 — Italy (medium) — FAIL
**Q:** After which major tournament did Italy's Bonucci and Chiellini retire?
**Answer:** Euro 2020/2022
**Why it fails:** Inaccurate: Chiellini retired internationally after the June 2022 Finalissima, but Bonucci kept playing for Italy until June 2023 (Nations League). They did not both retire 'after Euro 2020/2022'.
**Source:** https://en.wikipedia.org/wiki/Leonardo_Bonucci
**Remedy:** Separate the two - Bonucci's last cap was June 2023, not after Euro 2020.

### Row 32594 — Italy (medium) — FAIL
**Q:** After which tournament did Italy's Bonucci & Chiellini retire internationally?
**Answer:** After Euro 2020/2022
**Why it fails:** Inaccurate: Bonucci continued for Italy until June 2023 (his last cap, Nations League v Spain); only Chiellini retired after the 2022 Finalissima. The pair did not both retire after Euro 2020/2022.
**Source:** https://en.wikipedia.org/wiki/Leonardo_Bonucci
**Remedy:** Don't group them; Bonucci retired in 2023.

### Row 32597 — Italy (medium) — FAIL
**Q:** After winning Euro 2020, Italy reached which FIFA ranking?
**Answer:** 7th
**Why it fails:** Wrong answer: Italy reached 5th after Euro 2020, not 7th.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Change answer to 5th.

### Row 32598 — Italy (medium) — FAIL
**Q:** After winning Euro 2020, Italy's FIFA ranking rose to which position?
**Answer:** 7th
**Why it fails:** Wrong answer: Italy rose to 5th after Euro 2020, not 7th.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Change answer to 5th.

### Row 32599 — Italy (medium) — FAIL
**Q:** After winning Euro 2020, what FIFA ranking did Italy reach?
**Answer:** 7th
**Why it fails:** Wrong answer: Italy reached 5th after Euro 2020, not 7th.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Change answer to 5th.

### Row 32600 — Italy (hard) — FAIL
**Q:** After winning Euro 2020, when did Italy's FIFA ranking climb to 7th?
**Answer:** After Euro 2020
**Why it fails:** False premise: after Euro 2020 Italy climbed to 5th, not 7th (7th was the pre-tournament rank), so the 'climb to 7th' the question asks about did not happen post-Euro 2020.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Fix the rank to 5th.

### Row 32606 — Italy (medium) — FAIL
**Q:** At Euro 2020, how many clean sheets did Italy keep?
**Answer:** 4
**Why it fails:** Wrong answer: Italy kept 3 clean sheets at Euro 2020 (Turkey, Switzerland, Wales), not 4 - they conceded in all four knockout matches.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Change answer to 3.

### Row 32607 — Italy (medium) — FAIL
**Q:** At Euro 2020, how many goals did Italy concede in total?
**Answer:** Three goals
**Why it fails:** Wrong answer: Italy conceded 4 goals across Euro 2020 (Austria, Belgium, Spain, England), not three.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Change answer to four goals.

### Row 32610 — Italy (hard) — FAIL
**Q:** At Euro 2020, Italy's penalty shootout win over Spain ended with what score?
**Answer:** 04-Feb
**Why it fails:** Excel date-corruption: the answer renders as '04-Feb' instead of the score 4-2. The cell no longer reads as a scoreline.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Restore answer to '4-2 on penalties' and store as text; flag for a dataset date-corruption sweep.

### Row 32622 — Italy (easy) — FAIL
**Q:** At the 2026 FIFA World Cup qualifiers, which Italian stadium used has the smallest capacity?
**Answer:** Juventus Stadium
**Why it fails:** False premise: Italy did NOT use the Juventus Stadium for 2026 qualifiers. Their 2026 home matches were at Reggio Emilia, Bergamo and Udine (playoff also Bergamo/Rome). The stadium list is fabricated.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use Italy's actual 2026 venues (Bergamo, Udine, Reggio Emilia).

### Row 32627 — Italy (medium) — FAIL
**Q:** At which 2021 tournament did Italy concede only 3 goals?
**Answer:** Euro 2020
**Why it fails:** Wrong: Italy conceded 4 goals at Euro 2020 (Austria, Belgium, Spain, England), not 3. The 'only 3 goals' premise/explanation is false.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct the figure to 4 goals conceded.

### Row 32636 — Italy (medium) — FAIL
**Q:** At which tournament did Italy concede just three goals?
**Answer:** Euro 2020
**Why it fails:** Wrong: Italy conceded 4 goals at Euro 2020, not 3.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to 4 goals conceded.

### Row 32638 — Italy (medium) — FAIL
**Q:** At which tournament did Italy's defense concede only 3 goals?
**Answer:** Euro 2020
**Why it fails:** Wrong: Italy conceded 4 goals at Euro 2020, not 3.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to 4 goals conceded.

### Row 32639 — Italy (medium) — FAIL
**Q:** At which tournament did Italy's Jorginho miss two penalties?
**Answer:** Euro 2020
**Why it fails:** Wrong tournament: Jorginho missed only ONE penalty at Euro 2020 (the final shootout v England) - he scored the SF winner v Spain. His TWO costly misses were against Switzerland in 2022 WC qualifying, which contributed to Italy missing the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change answer to the 2022 World Cup qualifiers.

### Row 32651 — Italy (easy) — FAIL
**Q:** During Italy's Euro 2020 run, when did they keep their fourth clean sheet?
**Answer:** In the final
**Why it fails:** False: Italy kept only 3 clean sheets at Euro 2020 (all in the group stage); the final v England was 1-1, NOT a clean sheet, so there was no 'fourth clean sheet in the final'.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Remove - Italy had 3 clean sheets and conceded in the final.

### Row 32652 — Italy (easy) — FAIL
**Q:** During Juventus's nine-year Serie A reign, which Italian club did NOT win the title?
**Answer:** AC Milan
**Why it fails:** Non-unique: during Juventus's nine straight titles NONE of Inter, Roma, Napoli or AC Milan won Serie A, so every option satisfies 'did NOT win'. The answer is not unique.
**Source:** https://en.wikipedia.org/wiki/Serie_A
**Remedy:** Rework so only one option is a non-winner.

### Row 32653 — Italy (hard) — FAIL
**Q:** During which World Cup qualifying campaign did Italy play home matches at multiple venues?
**Answer:** 2026 World Cup qualifiers
**Why it fails:** Non-unique/soft: Italy rotates home venues nearly every campaign, so 'multiple venues' is not unique to 2026. (Their actual 2026 venues were Bergamo, Udine, Reggio Emilia, not a distinguishing trait.)
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Make the venue fact specific and unique.

### Row 32658 — Italy (medium) — FAIL
**Q:** For how many consecutive World Cups did Italy fail to qualify starting in 2018?
**Answer:** Two
**Why it fails:** Outdated as of 2026: starting in 2018 Italy have now missed THREE consecutive World Cups (2018, 2022, 2026) after losing the playoff final to Bosnia. The answer 'Two' is no longer correct.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Change answer to Three.

### Row 32663 — Italy (easy) — FAIL
**Q:** For Italy's 2026 World Cup qualifiers, in which four cities have they played home matches?
**Answer:** Rome, Milan, Turin, Naples
**Why it fails:** False: Italy's 2026 qualifying home matches were NOT in Rome, Milan, Turin and Naples - they were played in Reggio Emilia, Bergamo and Udine (with Rome only for the playoff). The four-city list is fabricated.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use the real host cities (Bergamo, Udine, Reggio Emilia).

### Row 32666 — Italy (easy) — FAIL
**Q:** For Italy's 2026 World Cup qualifiers, which four cities have hosted home matches?
**Answer:** Rome, Milan, Turin, Naples
**Why it fails:** False: Italy's 2026 qualifier home cities were Bergamo, Udine and Reggio Emilia, not Rome/Milan/Turin/Naples.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use the real host cities.

### Row 32667 — Italy (easy) — FAIL
**Q:** For Italy's 2026 World Cup qualifiers, which stadium had the smallest capacity?
**Answer:** Juventus Stadium
**Why it fails:** False premise: the Juventus Stadium was not a 2026-qualifier venue for Italy (they used Bergamo, Udine, Reggio Emilia).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use Italy's actual 2026 venues.

### Row 32671 — Italy (easy) — FAIL
**Q:** For Italy's 2026 World Cup squad, which league does goalkeeper Gianluigi Donnarumma play in?
**Answer:** Ligue 1
**Why it fails:** Outdated: Donnarumma left PSG for Manchester City in September 2025, so he plays in the Premier League, not Ligue 1.
**Source:** https://en.wikipedia.org/wiki/Gianluigi_Donnarumma
**Remedy:** Change answer to Premier League (Manchester City).

### Row 32675 — Italy (easy) — FAIL
**Q:** For the 2010 World Cup, how did Italy qualify compared to 2014?
**Answer:** As European champions
**Why it fails:** False: Italy did NOT qualify for 2010 'as European champions' - they were 2006 WORLD champions (and were knocked out of Euro 2008 in the QF). There was no automatic berth; they qualified by winning their UEFA group.
**Source:** https://en.wikipedia.org/wiki/Italy_national_football_team
**Remedy:** Correct to 'by winning their qualifying group' (defending WORLD champions, not auto-qualified).

### Row 32681 — Italy (hard) — FAIL
**Q:** For which FIFA World Cup qualifiers has Italy used Juventus Stadium?
**Answer:** 2026 World Cup qualifiers
**Why it fails:** False premise: Italy did not use the Juventus Stadium for the 2026 qualifiers (home games were Bergamo, Udine, Reggio Emilia).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Remove the Juventus Stadium claim for 2026.

### Row 32688 — Italy (medium) — FAIL
**Q:** For which World Cup did Italy use multiple home venues like Rome and Milan?
**Answer:** 2026 World Cup
**Why it fails:** False: Italy's 2026 home venues were Bergamo, Udine and Reggio Emilia - not 'Rome and Milan'. The example cities are wrong.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use the real host cities.

### Row 32693 — Italy (easy) — FAIL
**Q:** How did Italy qualify for the 2010 FIFA World Cup?
**Answer:** As European champions
**Why it fails:** False: Italy were not 'reigning European champions from Euro 2008' (they were eliminated in the Euro 2008 QF). They were the 2006 World champions and qualified for 2010 by winning their group - there is no auto-qualification for past champions.
**Source:** https://en.wikipedia.org/wiki/Italy_national_football_team
**Remedy:** Correct to 'by winning their qualifying group'.

### Row 32705 — Italy (medium) — FAIL
**Q:** How many cities host Italy's FIFA World Cup qualifiers?
**Answer:** Four
**Why it fails:** False: the named host cities (Rome, Milan, Turin, Naples) are wrong for the 2026 qualifiers - Italy played home games in Bergamo, Udine and Reggio Emilia.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use the real host cities.

### Row 32708 — Italy (medium) — FAIL
**Q:** How many consecutive FIFA World Cups did Italy fail to qualify for after 2014?
**Answer:** Two World Cups
**Why it fails:** Outdated as of 2026: after 2014 Italy have now missed THREE consecutive World Cups (2018, 2022, 2026), not two.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Change answer to Three.

### Row 32710 — Italy (medium) — FAIL
**Q:** How many consecutive FIFA World Cups did Italy miss after 2014?
**Answer:** Two
**Why it fails:** Outdated as of 2026: after 2014 Italy have now missed three consecutive World Cups (2018, 2022, 2026), not two.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Change answer to Three.

### Row 32712 — Italy (hard) — FAIL
**Q:** How many consecutive Serie A titles had Juventus won by Italy's 2018 World Cup qualification?
**Answer:** Seven consecutive titles
**Why it fails:** Wrong count: by Italy's 2018 WC qualifying campaign (ending Nov 2017) Juventus had won SIX straight Serie A titles (2011-12 to 2016-17); the seventh (2017-18) was not clinched until May 2018.
**Source:** https://en.wikipedia.org/wiki/Serie_A
**Remedy:** Change answer to six consecutive titles.

### Row 32713 — Italy (medium) — FAIL
**Q:** How many consecutive World Cups did Italy fail to qualify for?
**Answer:** Two consecutive World Cups
**Why it fails:** Outdated as of 2026: Italy have now failed to qualify for THREE consecutive World Cups (2018, 2022, 2026), not two.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Change answer to three consecutive World Cups.

### Row 32716 — Italy (medium) — FAIL
**Q:** How many goals did Italy concede at Euro 2020?
**Answer:** Three goals
**Why it fails:** Wrong: Italy conceded 4 goals at Euro 2020 (Austria, Belgium, Spain, England), not three.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Change answer to four goals.

### Row 32717 — Italy (medium) — FAIL
**Q:** How many goals did Italy concede in 7 Euro 2020 matches?
**Answer:** Three goals
**Why it fails:** Wrong: Italy conceded 4 goals across their 7 Euro 2020 matches, not three.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Change answer to four goals.

### Row 32718 — Italy (medium) — FAIL
**Q:** How many goals did Italy concede in their seven Euro 2020 matches?
**Answer:** Three
**Why it fails:** Wrong: Italy conceded 4 goals at Euro 2020, not three.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Change answer to four.

### Row 32722 — Italy (medium) — FAIL
**Q:** How many goals has Italian striker Ciro Immobile scored for his national team?
**Answer:** 14 goals
**Why it fails:** Wrong total: Immobile scored 17 goals for Italy (in 57 caps), not 14.
**Source:** https://en.wikipedia.org/wiki/Ciro_Immobile
**Remedy:** Change answer to 17 goals.

### Row 32732 — Italy (medium) — FAIL
**Q:** How many of Italy's Euro 2020 heroes retired internationally by 2022?
**Answer:** Two
**Why it fails:** Inaccurate: only Chiellini retired by 2022 (Finalissima, June 2022); Bonucci kept playing for Italy until June 2023. They did not both retire 'by 2022'.
**Source:** https://en.wikipedia.org/wiki/Leonardo_Bonucci
**Remedy:** Don't group them; Bonucci's last cap was June 2023.

### Row 32752 — Italy (hard) — FAIL
**Q:** In Euro 2020, what was Italy's penalty shootout score vs Spain?
**Answer:** 04-Feb
**Why it fails:** Excel date-corruption: answer renders as '04-Feb' instead of the score 4-2.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Restore '4-2' as text; flag for a date-corruption sweep.

### Row 32754 — Italy (medium) — FAIL
**Q:** In Italy's 2016 Euro quarter-final, what was the final score after extra time?
**Answer:** 01-Jan
**Why it fails:** Excel date-corruption: answer renders as '01-Jan' instead of the score 1-1 (Italy 1-1 Germany, Euro 2016 QF).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2016
**Remedy:** Restore '1-1' as text; flag for a date-corruption sweep.

### Row 32762 — Italy (easy) — FAIL
**Q:** In Italy's 2026 World Cup qualifiers, which manager chose the 3-5-2 formation?
**Answer:** Luciano Spalletti
**Why it fails:** Unsupported/false: Spalletti managed only Italy's OPENING 2026 qualifier before being sacked (June 2025); Gattuso ran the rest of the campaign. Spalletti is associated with 4-3-3, not a 3-5-2.
**Source:** https://en.wikipedia.org/wiki/Luciano_Spalletti
**Remedy:** Drop - no clear 3-5-2 manager ran Italy's 2026 qualifiers; Conte (the 3-5-2 example) was not involved.

### Row 32764 — Italy (easy) — FAIL
**Q:** In Italy's 2026 World Cup qualifiers, which stadium had a capacity near 41,500?
**Answer:** Juventus Stadium
**Why it fails:** False premise: the ~41,500-capacity Juventus Stadium was NOT one of Italy's 2026 qualifier venues. Italy used Reggio Emilia (~21k), Bergamo (~21k), Udine (~25k) and San Siro Milan (~75k).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use an actual 2026 venue.

### Row 32766 — Italy (easy) — FAIL
**Q:** In Italy's Euro 2020 quarter-final win over Belgium, what was the final score?
**Answer:** 02-Jan
**Why it fails:** Excel date-corruption: answer renders as '02-Jan' instead of the score 2-1 (Italy 2-1 Belgium, Euro 2020 QF).
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Restore '2-1' as text; flag for a date-corruption sweep.

### Row 32770 — Italy (easy) — FAIL
**Q:** In the Euro 2020 final shootout, Italy beat England by what penalty score?
**Answer:** 03-Feb
**Why it fails:** Excel date-corruption: answer renders as '03-Feb' instead of the score 3-2.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020_final
**Remedy:** Restore '3-2' as text; flag for a date-corruption sweep.

### Row 32771 — Italy (easy) — FAIL
**Q:** In the Euro 2020 final, Italy beat England on penalties by what score?
**Answer:** 03-Feb
**Why it fails:** Excel date-corruption: answer renders as '03-Feb' instead of the score 3-2.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020_final
**Remedy:** Restore '3-2' as text; flag for a date-corruption sweep.

### Row 32773 — Italy (hard) — FAIL
**Q:** In the Euro 2020 semi-final, what was Italy's penalty shootout score against Spain?
**Answer:** 04-Feb
**Why it fails:** Excel date-corruption: answer renders as '04-Feb' instead of the score 4-2 (Italy beat Spain 4-2 on pens).
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Restore '4-2' as text; flag for a date-corruption sweep.

### Row 32779 — Italy (easy) — FAIL
**Q:** In which city did Italy NOT host a 2026 World Cup qualifier?
**Answer:** Florence
**Why it fails:** Non-unique and wrong explanation: Italy hosted 2026 qualifiers in Reggio Emilia, Bergamo, Udine and Milan - NOT Rome or Turin, so Rome and Turin (as well as Florence) all satisfy 'did NOT host'. The explanation that they played in Rome/Milan/Turin is false.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Make the non-hosting city unique and fix the host list.

### Row 32780 — Italy (easy) — FAIL
**Q:** In which city did Italy play a 2026 World Cup qualifier in 2023?
**Answer:** Rome
**Why it fails:** False premise: there were no 2026 World Cup qualifiers in 2023 (UEFA's began in 2025; Italy's first was June 2025). Rome was also not a group-stage host.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Remove - no 2026 qualifier was played in 2023.

### Row 32791 — Italy (hard) — FAIL
**Q:** In which FIFA World Cup qualifying campaign did Italy's Gianluigi Buffon earn his record 176th cap?
**Answer:** 2018 World Cup qualifiers
**Why it fails:** False: Buffon's record-setting final cap was a 2018 friendly under Mancini, NOT during the 2018 WC qualifying campaign. His last competitive game was the Nov-2017 Sweden playoff, but he added friendly caps in 2018.
**Source:** https://en.wikipedia.org/wiki/Gianluigi_Buffon
**Remedy:** Re-anchor to his 2018 friendlies, or reword.

### Row 32792 — Italy (hard) — FAIL
**Q:** In which FIFA World Cup qualifying cycle did Italy use venues in Rome, Milan, Turin, and Naples?
**Answer:** 2026 World Cup qualifiers
**Why it fails:** False: Italy's 2026 qualifier venues were Reggio Emilia, Bergamo, Udine and San Siro Milan - not Rome, Turin and Naples.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use the real host cities.

### Row 32795 — Italy (easy) — FAIL
**Q:** In which Italian city do Italy NOT play FIFA World Cup home matches?
**Answer:** Florence
**Why it fails:** False/non-unique: Italy do not have a fixed Rome/Milan/Turin/Naples home policy - they rotate widely (recently Bergamo, Udine, Reggio Emilia, and they have used Florence's Stadio Franchi too). The 'not Florence' answer is not uniquely correct.
**Source:** https://en.wikipedia.org/wiki/Italy_national_football_team
**Remedy:** Drop the false four-city premise.

### Row 32796 — Italy (medium) — FAIL
**Q:** In which major tournament did Italy host their opener at Rome's Stadio Olimpico?
**Answer:** UEFA Euro 2020
**Why it fails:** Non-unique: Italy also opened the 1990 World Cup at Rome's Stadio Olimpico (1-0 v Austria), so both 'Euro 2020' and 'FIFA World Cup 1990' satisfy the question.
**Source:** https://en.wikipedia.org/wiki/1990_FIFA_World_Cup
**Remedy:** Make the answer unique (only one tournament should fit).

### Row 32802 — Italy (medium) — FAIL
**Q:** In which tournament did Italy keep 4 clean sheets including the final?
**Answer:** Euro 2020
**Why it fails:** False: Italy kept 3 clean sheets at Euro 2020 (all in the group), and the final v England was 1-1 - NOT a clean sheet. There were not 4 clean sheets 'including the final'.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to 3 clean sheets (none in the final).

### Row 32803 — Italy (medium) — FAIL
**Q:** In which tournament did Italy's defense concede only three goals in seven matches?
**Answer:** Euro 2020
**Why it fails:** False: Italy conceded 4 goals at Euro 2020, not three.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to 4 goals.

### Row 32807 — Italy (medium) — FAIL
**Q:** In which tournament did Italy's Jorginho miss two penalties but still win?
**Answer:** Euro 2020
**Why it fails:** False: Jorginho missed only ONE penalty at Euro 2020 (the final shootout); he scored the SF winner v Spain. His TWO misses were v Switzerland in 2022 WC qualifying (which Italy did NOT win).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Re-anchor the two misses to 2022 qualifying (and that campaign was a failure).

### Row 32808 — Italy (medium) — FAIL
**Q:** In which tournament did Italy's Jorginho miss two penalties?
**Answer:** Euro 2020
**Why it fails:** False: Jorginho missed only one penalty at Euro 2020 (the final). His two penalty misses were against Switzerland in 2022 WC qualifying.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Change answer to the 2022 WC qualifiers.

### Row 32858 — Italy (medium) — FAIL
**Q:** In which year did Italy use Rome, Milan, Turin, and Naples for World Cup qualifiers?
**Answer:** 2026 qualifiers
**Why it fails:** False: Italy's 2026 qualifier venues were Reggio Emilia, Bergamo, Udine and San Siro Milan - not Rome, Turin and Naples.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use the real host cities.

### Row 32901 — Italy (easy) — FAIL
**Q:** Italy beat Spain on penalties in the Euro 2020 semi-final by what score?
**Answer:** 04-Feb
**Why it fails:** Excel date-corruption: answer renders as '04-Feb' instead of the score 4-2.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Restore '4-2' as text; flag for a date-corruption sweep.

### Row 32902 — Italy (easy) — FAIL
**Q:** Italy beat Türkiye 3-0 to open Euro 2020. Which other Euro 2020 knockout match ended 3-0?
**Answer:** Italy vs Türkiye
**Why it fails:** Broken/self-referential: the question asks for another KNOCKOUT match that ended 3-0, but the answer 'Italy vs Türkiye' is the group-stage opener already named in the stem (and not a knockout match). No other Euro 2020 match Italy played ended 3-0.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Remove - the premise has no valid unique answer.

### Row 32906 — Italy (medium) — FAIL
**Q:** Italy conceded how many goals in their 7 Euro 2020 matches?
**Answer:** 3 goals
**Why it fails:** False: Italy conceded 4 goals across their 7 Euro 2020 matches, not 3.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to 4 goals.

### Row 32911 — Italy (easy) — FAIL
**Q:** Italy hosted a 2026 World Cup qualifier at which Turin stadium?
**Answer:** Allianz Stadium
**Why it fails:** False premise: Italy did NOT host any 2026 qualifier in Turin/Allianz Stadium. Their venues were Reggio Emilia, Bergamo, Udine and San Siro Milan.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Remove the Turin/Allianz claim.

### Row 32925 — Italy (medium) — FAIL
**Q:** Italy reached what FIFA ranking after winning Euro 2020?
**Answer:** 7th
**Why it fails:** Wrong: Italy rose to 5th after Euro 2020 (Aug 2021), not 7th (7th was the pre-tournament rank).
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Change answer to 5th.

### Row 32932 — Italy (hard) — FAIL
**Q:** Italy's 2021 Euro final penalty shootout win over England finished what score?
**Answer:** 03-Feb
**Why it fails:** Excel date-corruption: answer renders as '03-Feb' instead of the score 3-2.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020_final
**Remedy:** Restore '3-2' as text; flag for a sweep.

### Row 32934 — Italy (medium) — FAIL
**Q:** Italy's 2022 playoff loss followed a 2018 failure. How many consecutive World Cups did Italy miss?
**Answer:** Two World Cups
**Why it fails:** Outdated as of 2026: Italy have now missed THREE consecutive World Cups (2018, 2022, 2026), not two.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Change answer to three.

### Row 32939 — Italy (medium) — FAIL
**Q:** Italy's 2026 World Cup qualifiers have been played across how many different cities?
**Answer:** Four
**Why it fails:** Wrong explanation: although Italy did use four cities, they were Reggio Emilia, Bergamo, Udine and Milan - NOT Rome, Milan, Turin, Naples as the explanation states.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Fix the explanation's city list (keep the count of four).

### Row 32942 — Italy (medium) — FAIL
**Q:** Italy's 37-match unbeaten run ended before which UEFA tournament?
**Answer:** UEFA Euro 2020
**Why it fails:** False: the 37-match run did NOT end before Euro 2020 - it continued THROUGH Euro 2020 (won July 2021) and ended in October 2021 (1-2 loss to Spain in the Nations League). It ended before Euro 2024, not Euro 2020.
**Source:** https://en.wikipedia.org/wiki/Italy_national_football_team
**Remedy:** Change answer to UEFA Euro 2024.

### Row 32953 — Italy (medium) — FAIL
**Q:** Italy's Gianluigi Buffon retired after 2018 qualification failure. Which goalkeeper also retired after a World Cup qualification failure?
**Answer:** Gianluigi Buffon
**Why it fails:** Self-referential: the stem already names Buffon as the keeper who retired after the 2018 failure, then the answer is Buffon again. The 'other goalkeeper' answer should not be the same player.
**Source:** https://en.wikipedia.org/wiki/Gianluigi_Buffon
**Remedy:** Replace with a genuinely different keeper, or rework the question.

### Row 32957 — Italy (medium) — FAIL
**Q:** To which FIFA ranking did Italy climb after winning Euro 2020?
**Answer:** 7th
**Why it fails:** Wrong: Italy climbed to 5th after Euro 2020, not 7th.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Change answer to 5th.

### Row 32958 — Italy (easy) — FAIL
**Q:** To which ranking did Italy rise after winning Euro 2020?
**Answer:** 7th
**Why it fails:** Wrong: Italy rose to 5th after Euro 2020, not 7th.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Change answer to 5th.

### Row 32959 — Italy (easy) — FAIL
**Q:** Under which manager did Italy qualify for the 2026 World Cup?
**Answer:** Luciano Spalletti
**Why it fails:** False premise: Italy did NOT qualify for the 2026 World Cup (lost the playoff final to Bosnia, 4-1 pens). No manager 'led them to 2026 qualification'; Spalletti was also sacked in June 2025.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 32970 — Italy (easy) — FAIL
**Q:** What scoreline did Italy beat Belgium by at Euro 2020?
**Answer:** 02-Jan
**Why it fails:** Excel date-corruption: answer renders as '02-Jan' instead of the score 2-1.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Restore '2-1' as text; flag for a sweep.

### Row 32972 — Italy (medium) — FAIL
**Q:** What was Italy's exact score against Belgium in the Euro 2020 quarter-final?
**Answer:** 02-Jan
**Why it fails:** Excel date-corruption: answer renders as '02-Jan' instead of the score 2-1.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Restore '2-1'; flag for a sweep.

### Row 32973 — Italy (hard) — FAIL
**Q:** What was Italy's exact scoreline against England in the 2014 World Cup group stage?
**Answer:** 02-Jan
**Why it fails:** Excel date-corruption: answer renders as '02-Jan' instead of the score 2-1 (Italy 2-1 England, 2014).
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_FIFA_World_Cup
**Remedy:** Restore '2-1'; flag for a sweep.

### Row 32974 — Italy (medium) — FAIL
**Q:** What was Italy's FIFA ranking after winning Euro 2020?
**Answer:** 7th
**Why it fails:** Wrong: Italy's ranking after Euro 2020 was 5th, not 7th.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Change answer to 5th.

### Row 32978 — Italy (easy) — FAIL
**Q:** What was Italy's penalty score in the Euro 2020 final shootout?
**Answer:** 03-Feb
**Why it fails:** Excel date-corruption: answer renders as '03-Feb' instead of the score 3-2.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020_final
**Remedy:** Restore '3-2'; flag for a sweep.

### Row 32981 — Italy (easy) — FAIL
**Q:** What was Italy's quarter-final score against Belgium at Euro 2020?
**Answer:** 02-Jan
**Why it fails:** Excel date-corruption: answer renders as '02-Jan' instead of the score 2-1.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Restore '2-1'; flag for a sweep.

### Row 32988 — Italy (easy) — FAIL
**Q:** What was the final score when Italy beat Belgium in the Euro 2020 quarter-final?
**Answer:** 02-Jan
**Why it fails:** Excel date-corruption: answer renders as '02-Jan' instead of the score 2-1.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Restore '2-1'; flag for a sweep.

### Row 33004 — Italy (medium) — FAIL
**Q:** When did Italy concede only three goals in seven matches?
**Answer:** At Euro 2020
**Why it fails:** False: Italy conceded 4 goals in their seven Euro 2020 matches, not three.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to four goals.

### Row 33010 — Italy (medium) — FAIL
**Q:** When did Italy first host a FIFA World Cup qualifier at Juventus Stadium?
**Answer:** In 2026 qualifying
**Why it fails:** False premise: Italy did NOT host a 2026 qualifier at the Juventus Stadium (venues were Reggio Emilia, Bergamo, Udine, San Siro Milan).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Remove the Juventus Stadium claim.

### Row 33011 — Italy (medium) — FAIL
**Q:** When did Italy keep 4 clean sheets at a major tournament?
**Answer:** Euro 2020
**Why it fails:** False: Italy kept 3 clean sheets at Euro 2020, not 4.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to 3 clean sheets.

### Row 33012 — Italy (medium) — FAIL
**Q:** When did Italy keep 4 clean sheets at Euro 2020?
**Answer:** 2020
**Why it fails:** False premise: Italy kept 3 clean sheets at Euro 2020, not 4.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to 3 clean sheets.

### Row 33013 — Italy (medium) — FAIL
**Q:** When did Italy keep 4 clean sheets in a European Championship?
**Answer:** Euro 2020
**Why it fails:** False: Italy kept 3 clean sheets at Euro 2020, not 4.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to 3 clean sheets.

### Row 33014 — Italy (medium) — FAIL
**Q:** When did Italy keep four clean sheets at the European Championship?
**Answer:** 2020
**Why it fails:** False: Italy kept 3 clean sheets at Euro 2020, not 4.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to 3 clean sheets.

### Row 33015 — Italy (medium) — FAIL
**Q:** When did Italy keep four clean sheets, including the final?
**Answer:** Euro 2020
**Why it fails:** False: Italy kept 3 clean sheets at Euro 2020 (none in the final, which was 1-1), not 4 including the final.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to 3 clean sheets (none in the final).

### Row 33016 — Italy (medium) — FAIL
**Q:** When did Italy last lose a knockout match to a European rival?
**Answer:** Euro 2024
**Why it fails:** Outdated: Italy's most recent knockout loss to a European rival is the March 2026 WC playoff final v Bosnia (1-1, 4-1 pens), not the Euro 2024 R16. 'Last' is no longer Euro 2024.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Update to the 2026 playoff loss to Bosnia (or scope the question to major-tournament knockouts).

### Row 33034 — Italy (medium) — FAIL
**Q:** When did Italy qualify for the 2026 FIFA World Cup under Luciano Spalletti?
**Answer:** 2026
**Why it fails:** False premise: Italy did NOT qualify for the 2026 World Cup (lost the playoff final to Bosnia); and Spalletti was sacked in June 2025.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 33035 — Italy (medium) — FAIL
**Q:** When did Italy qualify for the 2026 World Cup under Spalletti?
**Answer:** 2026
**Why it fails:** False premise: Italy did not qualify for 2026 (lost to Bosnia in the playoff final); Spalletti had also been sacked.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 33036 — Italy (hard) — FAIL
**Q:** When did Italy reach 7th in the FIFA rankings after Euro 2020?
**Answer:** After Euro 2020
**Why it fails:** False premise: after Euro 2020 Italy reached 5th, not 7th (7th was the pre-tournament rank).
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Fix the rank to 5th.

### Row 33038 — Italy (medium) — FAIL
**Q:** When did Italy use multiple stadiums for their World Cup qualifiers?
**Answer:** For 2026 qualifiers
**Why it fails:** Non-unique: Italy rotate home venues nearly every qualifying campaign, so 'multiple stadiums' is not unique to 2026.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Make the venue fact specific/unique.

### Row 33039 — Italy (hard) — FAIL
**Q:** When did Italy use multiple stadiums for World Cup qualifiers?
**Answer:** 2026 World Cup qualifiers
**Why it fails:** Non-unique: using multiple stadiums is not unique to the 2026 qualifiers (Italy do this most campaigns).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Make the venue fact unique.

### Row 33040 — Italy (medium) — FAIL
**Q:** When did Italy use Rome, Milan, Turin, and Naples venues for FIFA World Cup qualifiers?
**Answer:** 2026 qualifiers
**Why it fails:** False: Italy's 2026 qualifier venues were Reggio Emilia, Bergamo, Udine and Milan - not Rome, Turin, Naples.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use the real host cities.

### Row 33048 — Italy (hard) — FAIL
**Q:** When did Italy's Allianz Stadium first host a World Cup qualifier?
**Answer:** In the 2026 cycle
**Why it fails:** False premise: the Allianz Stadium (Turin) did NOT host a 2026 qualifier - Italy used Reggio Emilia, Bergamo, Udine and San Siro Milan.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Remove the Allianz/Turin claim.

### Row 33057 — Italy (medium) — FAIL
**Q:** When did Italy's Jorginho miss a penalty in the Euro 2020 semi-final?
**Answer:** In 2021
**Why it fails:** False premise: Jorginho did NOT miss in the Euro 2020 semi-final - he scored the winning penalty in the SF shootout v Spain. His miss came in the FINAL v England.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Re-anchor the missed penalty to the final, not the semi-final.

### Row 33108 — Italy (easy) — FAIL
**Q:** Which 2014 World Cup opponent did Italy fail to beat?
**Answer:** Costa Rica
**Why it fails:** Non-unique: Italy failed to beat BOTH Costa Rica and Uruguay in 2014 (lost 0-1 to each), so two options satisfy 'failed to beat'.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_FIFA_World_Cup
**Remedy:** Leave only one valid non-beaten opponent among the options.

### Row 33112 — Italy (easy) — FAIL
**Q:** Which 2022 World Cup qualifying rival did not force Italy into a playoff?
**Answer:** Bulgaria
**Why it fails:** Non-unique: only Switzerland forced the playoff; Bulgaria, Northern Ireland AND Lithuania all 'did not force' it, so three options fit.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Keep only one non-forcing rival among the options.

### Row 33114 — Italy (easy) — FAIL
**Q:** Which city has NOT hosted Italy's 2026 World Cup qualifiers?
**Answer:** Florence
**Why it fails:** Non-unique/false: Italy's 2026 hosts were Reggio Emilia, Bergamo, Udine, Milan - so Rome and Turin (and Florence) all did NOT host; the explanation that they played Rome/Turin is false.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Fix the host list and make the answer unique.

### Row 33115 — Italy (easy) — FAIL
**Q:** Which city hosted an Italy 2026 World Cup qualifier?
**Answer:** Naples
**Why it fails:** False: Naples did NOT host a 2026 Italy qualifier - none of the options (Naples, Florence, Bologna, Genoa) did. Italy used Reggio Emilia, Bergamo, Udine and Milan.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use an actual host city (e.g. Bergamo).

### Row 33123 — Italy (easy) — FAIL
**Q:** Which Euro 2020 opponent did Italy's Federico Chiesa NOT score against?
**Answer:** England
**Why it fails:** Non-unique: Chiesa scored v Austria and Spain at Euro 2020, so he did NOT score against England OR Belgium - two options fit 'did NOT score against'.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Leave only one option Chiesa failed to score against.

### Row 33134 — Italy (medium) — FAIL
**Q:** Which FIFA ranking did Italy achieve after winning Euro 2020?
**Answer:** 7th
**Why it fails:** Wrong: Italy reached 5th after Euro 2020, not 7th.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Change answer to 5th.

### Row 33141 — Italy (easy) — FAIL
**Q:** Which formation did Italy's Luciano Spalletti use at the 2026 World Cup?
**Answer:** 3-5-2 or 4-3-3
**Why it fails:** False premise: Italy did NOT play at the 2026 World Cup (failed to qualify), and Spalletti was sacked in June 2025 - he had no formation 'at the 2026 World Cup'.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not feature at the 2026 World Cup.

### Row 33145 — Italy (easy) — FAIL
**Q:** Which four cities host Italy's FIFA World Cup qualifying matches?
**Answer:** Rome, Milan, Turin, Naples
**Why it fails:** False: Italy's 2026 qualifier host cities were Reggio Emilia, Bergamo, Udine and Milan - not Rome, Milan, Turin, Naples.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use the real host cities.

### Row 33146 — Italy (easy) — FAIL
**Q:** Which four Italian cities host Italy's FIFA World Cup qualifiers?
**Answer:** Rome, Milan, Turin, Naples
**Why it fails:** False: the four host cities were Reggio Emilia, Bergamo, Udine and Milan, not Rome/Milan/Turin/Naples.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use the real host cities.

### Row 33150 — Italy (easy) — FAIL
**Q:** Which Italian 2026 squad players are based at clubs in England?
**Answer:** Sandro Tonali
**Why it fails:** Non-unique as of 2025-26: both Tonali (Newcastle) AND Donnarumma (Manchester City, since Sept 2025) are based in England, so two options fit. (Chiesa is also in England, at Liverpool.)
**Source:** https://en.wikipedia.org/wiki/Gianluigi_Donnarumma
**Remedy:** Leave only one England-based player among the options.

### Row 33153 — Italy (easy) — FAIL
**Q:** Which Italian 2026 World Cup player is based at PSG?
**Answer:** Gianluigi Donnarumma
**Why it fails:** Outdated: Donnarumma left PSG for Manchester City in September 2025 - he is no longer at PSG.
**Source:** https://en.wikipedia.org/wiki/Gianluigi_Donnarumma
**Remedy:** Update club to Manchester City, or change the question.

### Row 33155 — Italy (easy) — FAIL
**Q:** Which Italian 2026 World Cup squad player is based abroad?
**Answer:** Gianluigi Donnarumma
**Why it fails:** Non-unique and wrong explanation: Donnarumma (Man City) AND Chiesa (Liverpool, since 2024) are BOTH based abroad, and the explanation that Donnarumma plays for PSG / the others are all Serie A is false.
**Source:** https://en.wikipedia.org/wiki/Federico_Chiesa
**Remedy:** Fix the clubs and leave only one abroad-based player.

### Row 33156 — Italy (easy) — FAIL
**Q:** Which Italian 2026 World Cup squad player is based at French club PSG?
**Answer:** Gianluigi Donnarumma
**Why it fails:** Outdated: Donnarumma moved from PSG to Manchester City (Premier League) in September 2025; he is not at the French club PSG.
**Source:** https://en.wikipedia.org/wiki/Gianluigi_Donnarumma
**Remedy:** Update to Manchester City.

### Row 33158 — Italy (easy) — FAIL
**Q:** Which Italian centre-back pair retired after Euro 2020, aging the 2026 World Cup squad?
**Answer:** Bonucci and Chiellini
**Why it fails:** Inaccurate: Chiellini retired after the June 2022 Finalissima, but Bonucci kept playing for Italy until June 2023. They did not both retire after Euro 2020.
**Source:** https://en.wikipedia.org/wiki/Leonardo_Bonucci
**Remedy:** Don't group them; Bonucci's last cap was June 2023.

### Row 33159 — Italy (easy) — FAIL
**Q:** Which Italian city hosted a 2026 World Cup qualifier for Italy?
**Answer:** Rome
**Why it fails:** False: Rome did NOT host a 2026 Italy qualifier - none of the options did. Italy's 2026 home games were in Reggio Emilia, Bergamo, Udine and Milan; the playoff final was away in Zenica, Bosnia.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use an actual host city (e.g. Bergamo).

### Row 33180 — Italy (easy) — FAIL
**Q:** Which Italian club features in Serie A, Italy's top league?
**Answer:** AC Milan
**Why it fails:** Non-unique: all four options (AC Milan, AS Roma, Juventus, Inter Milan) are Serie A clubs, so every option satisfies 'features in Serie A'.
**Source:** https://en.wikipedia.org/wiki/Serie_A
**Remedy:** Include non-Serie-A distractors.

### Row 33181 — Italy (easy) — FAIL
**Q:** Which Italian club is a top team in Serie A, Italy's domestic league?
**Answer:** Inter Milan
**Why it fails:** Non-unique/subjective: all four (Inter, Lazio, Fiorentina, Atalanta) are Serie A clubs and 'a top team' is undefined (Atalanta/Lazio also qualify).
**Source:** https://en.wikipedia.org/wiki/Serie_A
**Remedy:** Make the criterion objective and unique.

### Row 33183 — Italy (easy) — FAIL
**Q:** Which Italian club last won Serie A before the 2022 World Cup?
**Answer:** Juventus
**Why it fails:** False: the last Serie A title decided before the Nov-2022 World Cup was 2021-22, won by AC MILAN (May 2022), not Juventus (whose last was 2019-20). Inter (2020-21) also came after Juventus.
**Source:** https://en.wikipedia.org/wiki/Serie_A
**Remedy:** Change answer to AC Milan.

### Row 33205 — Italy (easy) — FAIL
**Q:** Which Italian club won Serie A in the World Cup year 2022?
**Answer:** Napoli
**Why it fails:** False: the Serie A title won in calendar 2022 (2021-22) went to AC Milan; Napoli's win was 2022-23, decided in May 2023, not 2022.
**Source:** https://en.wikipedia.org/wiki/Serie_A
**Remedy:** Change answer to AC Milan (or fix the year).

### Row 33223 — Italy (easy) — FAIL
**Q:** Which Italian defender did NOT retire internationally after Euro 2020/2022?
**Answer:** Alessandro Bastoni
**Why it fails:** Non-unique: both Bastoni (still active) AND Barzagli (retired in 2017, before Euro 2020) satisfy 'did NOT retire after Euro 2020/2022'.
**Source:** https://en.wikipedia.org/wiki/Andrea_Barzagli
**Remedy:** Replace Barzagli with a player who retired after Euro 2020.

### Row 33227 — Italy (easy) — FAIL
**Q:** Which Italian defender from Euro 2020 is NOT in the 2026 World Cup squad?
**Answer:** Leonardo Bonucci
**Why it fails:** Non-unique: both Bonucci AND Chiellini are retired and not in the 2026 setup, so two options satisfy 'NOT in the 2026 squad'.
**Source:** https://en.wikipedia.org/wiki/Giorgio_Chiellini
**Remedy:** Leave only one retired defender among the options.

### Row 33240 — Italy (easy) — FAIL
**Q:** Which Italian defender retired internationally after Euro 2020?
**Answer:** Giorgio Chiellini
**Why it fails:** Non-unique: both Chiellini (2022) and Bonucci (2023) retired after Euro 2020, so two options fit.
**Source:** https://en.wikipedia.org/wiki/Leonardo_Bonucci
**Remedy:** Leave only one post-Euro-2020 retiree among the options.

### Row 33259 — Italy (easy) — FAIL
**Q:** Which Italian defenders retired after the 2020 Euros?
**Answer:** Bonucci and Chiellini
**Why it fails:** Inaccurate: Chiellini retired after the June 2022 Finalissima, but Bonucci played for Italy until June 2023 - they did not both retire after Euro 2020.
**Source:** https://en.wikipedia.org/wiki/Leonardo_Bonucci
**Remedy:** Bonucci's last cap was June 2023; don't pair them as retiring after Euro 2020.

### Row 33260 — Italy (easy) — FAIL
**Q:** Which Italian defensive duo retired after Euro 2020, ending an era?
**Answer:** Bonucci and Chiellini
**Why it fails:** Inaccurate: Bonucci kept playing for Italy until June 2023; only Chiellini retired around Euro 2020/2022.
**Source:** https://en.wikipedia.org/wiki/Leonardo_Bonucci
**Remedy:** Separate the two; Bonucci retired in 2023.

### Row 33261 — Italy (easy) — FAIL
**Q:** Which Italian defensive legends retired before the 2022 World Cup?
**Answer:** Bonucci and Chiellini
**Why it fails:** False: Bonucci did NOT retire before the 2022 World Cup - his last Italy cap was June 2023 (after the Nov-2022 WC). Only Chiellini retired before it.
**Source:** https://en.wikipedia.org/wiki/Leonardo_Bonucci
**Remedy:** Don't group them; Bonucci retired in 2023.

### Row 33262 — Italy (easy) — FAIL
**Q:** Which Italian defensive pair retired after Euro 2020?
**Answer:** Bonucci and Chiellini
**Why it fails:** Inaccurate: Bonucci played for Italy until June 2023, not 'after Euro 2020'. Only Chiellini fits.
**Source:** https://en.wikipedia.org/wiki/Leonardo_Bonucci
**Remedy:** Separate the two; Bonucci retired in 2023.

### Row 33291 — Italy (easy) — FAIL
**Q:** Which Italian left-sided centre-back did NOT start their 2026 World Cup qualifier vs. Ukraine?
**Answer:** Giorgio Chiellini
**Why it fails:** False premise: Italy did NOT play Ukraine in 2026 WC qualifying (their Group I opponents were Norway, Israel, Estonia, Moldova). Also Chiellini retired in 2022.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Remove the fictional Ukraine qualifier.

### Row 33303 — Italy (easy) — FAIL
**Q:** Which Italian manager ended their World Cup absence by qualifying for the 2026 tournament?
**Answer:** Luciano Spalletti
**Why it fails:** False: Italy did NOT qualify for the 2026 World Cup (lost the playoff final to Bosnia, 4-1 pens); no manager ended the absence, and Spalletti was sacked in June 2025.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 33313 — Italy (easy) — FAIL
**Q:** Which Italian manager selected a 3-5-2 squad for the 2026 World Cup qualifiers?
**Answer:** Luciano Spalletti
**Why it fails:** Inaccurate: Spalletti is a 4-3-3 manager, not a 3-5-2 one, and he managed only Italy's opening 2026 qualifier before being sacked (June 2025); Gattuso ran the campaign.
**Source:** https://en.wikipedia.org/wiki/Luciano_Spalletti
**Remedy:** Drop the specific 3-5-2 claim for Spalletti's 2026 qualifiers.

### Row 33316 — Italy (easy) — FAIL
**Q:** Which Italian manager was NOT in charge during 2026 World Cup qualifying?
**Answer:** Roberto Mancini
**Why it fails:** Non-unique and false: Mancini, Ventura AND Conte were all NOT in charge of 2026 qualifying (three options fit). The explanation that 'only Spalletti' managed the 2026 campaign is also wrong - Gattuso ran most of it.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Leave only one manager who was not involved; note Gattuso.

### Row 33328 — Italy (easy) — FAIL
**Q:** Which Italian midfielder was in the Euro 2012 Team of the Tournament?
**Answer:** Andrea Pirlo
**Why it fails:** Non-unique: BOTH Pirlo and De Rossi were in the Euro 2012 Team of the Tournament (which had four Italians: Buffon, De Rossi, Pirlo, Balotelli).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2012
**Remedy:** Remove De Rossi as a distractor.

### Row 33336 — Italy (easy) — FAIL
**Q:** Which Italian midfielder was selected for the Euro 2012 Team of the Tournament?
**Answer:** Andrea Pirlo
**Why it fails:** Non-unique: both Pirlo and De Rossi were in the Euro 2012 Team of the Tournament.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2012
**Remedy:** Remove De Rossi as a distractor.

### Row 33340 — Italy (easy) — FAIL
**Q:** Which Italian midfielder, in Euro 2012's Team of the Tournament, played in the 2014 World Cup?
**Answer:** Andrea Pirlo
**Why it fails:** Non-unique: both Pirlo and De Rossi were in the Euro 2012 Team of the Tournament AND both played at the 2014 World Cup.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2012
**Remedy:** Remove De Rossi as a distractor.

### Row 33341 — Italy (easy) — FAIL
**Q:** Which Italian midfielder, unlike Xavi, was in the Euro 2012 Team of the Tournament?
**Answer:** Andrea Pirlo
**Why it fails:** False premise + non-unique: Xavi WAS in the Euro 2012 Team of the Tournament (so the 'unlike Xavi' contrast is wrong), and De Rossi (also Italian) was in it too.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2012
**Remedy:** Drop the false Xavi contrast and the De Rossi distractor.

### Row 33360 — Italy (easy) — FAIL
**Q:** Which Italian player made the Euro 2012 Team of the Tournament?
**Answer:** Andrea Pirlo
**Why it fails:** Non-unique: both Pirlo AND Buffon were in the Euro 2012 Team of the Tournament.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2012
**Remedy:** Remove Buffon as a distractor.

### Row 33361 — Italy (easy) — FAIL
**Q:** Which Italian player made the Euro 2020 Team of the Tournament?
**Answer:** Federico Chiesa
**Why it fails:** Non-unique: both Chiesa AND Bonucci were in the Euro 2020 Team of the Tournament (which had five Italians: Donnarumma, Bonucci, Spinazzola, Jorginho, Chiesa).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Remove Bonucci as a distractor.

### Row 33371 — Italy (easy) — FAIL
**Q:** Which Italian player scored at Euro 2020 vs Austria, Belgium, and Spain?
**Answer:** Federico Chiesa
**Why it fails:** False: Chiesa scored v Austria and Spain at Euro 2020 but NOT v Belgium (Barella and Insigne scored in the QF).
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Drop Belgium - Chiesa scored only v Austria and Spain.

### Row 33375 — Italy (easy) — FAIL
**Q:** Which Italian player scored in Euro 2020 knockout matches against Austria, Belgium, and Spain?
**Answer:** Federico Chiesa
**Why it fails:** False: Chiesa did NOT score v Belgium at Euro 2020 - only v Austria (R16) and Spain (SF).
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Drop Belgium.

### Row 33376 — Italy (easy) — FAIL
**Q:** Which Italian player scored in Euro 2020 knockout wins over Austria, Belgium, and Spain?
**Answer:** Federico Chiesa
**Why it fails:** False: Chiesa scored v Austria and Spain, not Belgium, in the Euro 2020 knockouts.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Drop Belgium.

### Row 33379 — Italy (easy) — FAIL
**Q:** Which Italian player scored in three consecutive Euro 2020 knockout matches?
**Answer:** Federico Chiesa
**Why it fails:** False: Chiesa did NOT score in three consecutive knockout matches - he scored in the R16 and SF but NOT the QF v Belgium.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to two (non-consecutive) knockout goals.

### Row 33393 — Italy (easy) — FAIL
**Q:** Which Italian player was named in the Euro 2020 Team of the Tournament?
**Answer:** Federico Chiesa
**Why it fails:** Non-unique: Chiesa, Bonucci AND Donnarumma were all in the Euro 2020 Team of the Tournament.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Leave only one Euro 2020 ToT Italian among the options.

### Row 33395 — Italy (easy) — FAIL
**Q:** Which Italian player was part of the 2018 World Cup qualifying playoff loss to Sweden?
**Answer:** Gianluigi Buffon
**Why it fails:** Non-unique: both Buffon AND Insigne played in the 2018 WC qualifying playoff v Sweden (Insigne started the 2nd leg).
**Source:** https://en.wikipedia.org/wiki/Italy_national_football_team
**Remedy:** Leave only one squad member among the options.

### Row 33403 — Italy (easy) — FAIL
**Q:** Which Italian player, besides Andrea Pirlo in 2012, made the Euro 2020 Team of the Tournament?
**Answer:** Federico Chiesa
**Why it fails:** Non-unique and false: Chiesa, Bonucci and Donnarumma were ALL in the Euro 2020 ToT, so Chiesa was not 'the only other Italian'.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Fix the false claim and leave one ToT Italian.

### Row 33404 — Italy (easy) — FAIL
**Q:** Which Italian player, like Andrea Pirlo in 2012, was in the Euro 2020 Team of the Tournament?
**Answer:** Federico Chiesa
**Why it fails:** Non-unique: Chiesa, Bonucci and Donnarumma were all in the Euro 2020 ToT.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Leave only one ToT Italian among the options.

### Row 33405 — Italy (easy) — FAIL
**Q:** Which Italian player, like Spain's Xavi in 2012, made the Euro 2020 Team of the Tournament?
**Answer:** Federico Chiesa
**Why it fails:** Non-unique: both Chiesa, Bonucci AND Donnarumma were in the Euro 2020 ToT.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Leave only one ToT Italian among the options.

### Row 33427 — Italy (easy) — FAIL
**Q:** Which Italian stadium held Italy matches with a 41,507 capacity?
**Answer:** Juventus Stadium Turin
**Why it fails:** Non-unique: 'Juventus Stadium Turin' and 'Allianz Stadium Turin' are the SAME stadium (~41,507), so two options are identical.
**Source:** https://en.wikipedia.org/wiki/Allianz_Stadium_(Turin)
**Remedy:** Remove the duplicate stadium option.

### Row 33428 — Italy (easy) — FAIL
**Q:** Which Italian stadium hosted a 2026 World Cup qualifier for Italy?
**Answer:** Juventus Stadium
**Why it fails:** False: the Juventus Stadium did NOT host a 2026 Italy qualifier (venues were Reggio Emilia, Bergamo, Udine, San Siro Milan).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use an actual 2026 venue.

### Row 33429 — Italy (easy) — FAIL
**Q:** Which Italian stadium hosted a 2026 World Cup qualifier?
**Answer:** Stadio Olimpico
**Why it fails:** False: the Stadio Olimpico did NOT host a 2026 Italy qualifier - the group games were in Reggio Emilia, Bergamo, Udine and Milan, and the playoff final was away in Zenica.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use an actual 2026 venue (e.g. San Siro).

### Row 33436 — Italy (easy) — FAIL
**Q:** Which Italian stadium used for 2026 World Cup qualifiers has the smallest capacity?
**Answer:** Allianz Stadium
**Why it fails:** False premise: the Allianz Stadium (Turin) was NOT a 2026 Italy qualifier venue; the smallest venue actually used was Bergamo/Reggio Emilia (~21,000).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use the real smallest venue (Bergamo or Reggio Emilia).

### Row 33475 — Italy (easy) — FAIL
**Q:** Which Italian veteran retired before the 2026 World Cup qualifying cycle?
**Answer:** Leonardo Bonucci
**Why it fails:** Non-unique: all four (Bonucci 2023, Chiellini 2022, Buffon 2018, Pirlo 2015) retired before the 2026 qualifying cycle.
**Source:** https://en.wikipedia.org/wiki/Italy_national_football_team
**Remedy:** Leave only one pre-2026 retiree among the options.

### Row 33479 — Italy (easy) — FAIL
**Q:** Which Italian was named in the Team of the Tournament at Euro 2020, not Euro 2012?
**Answer:** Federico Chiesa
**Why it fails:** Non-unique: Chiesa, Bonucci AND Donnarumma were all in the Euro 2020 ToT (and not the 2012 one).
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Leave only one 2020-ToT Italian among the options.

### Row 33494 — Italy (easy) — FAIL
**Q:** Which Italian's Euro 2012 displays earned him a Team of the Tournament spot?
**Answer:** Andrea Pirlo
**Why it fails:** Non-unique: Pirlo, Buffon AND Balotelli were all in the Euro 2012 Team of the Tournament.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2012
**Remedy:** Leave only one 2012-ToT Italian among the options.

### Row 33504 — Italy (easy) — FAIL
**Q:** Which Italy centre-back played in all three Euro finals from 2012 to 2020?
**Answer:** Giorgio Chiellini
**Why it fails:** Flawed: Italy reached only TWO Euro finals in 2012-2020 (2012 and 2020; they exited Euro 2016 in the QF), so 'all three Euro finals' is false. If read as the three tournaments, both Chiellini AND Bonucci played all three (non-unique).
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Fix the premise; Italy had two Euro finals in that span.

### Row 33511 — Italy (easy) — FAIL
**Q:** Which Italy coach qualified them for the 2026 World Cup?
**Answer:** Luciano Spalletti
**Why it fails:** False: Italy did NOT qualify for the 2026 World Cup (lost the playoff final to Bosnia); Spalletti was also sacked in June 2025.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 33513 — Italy (easy) — FAIL
**Q:** Which Italy coach's tactics led to 4 clean sheets at Euro 2020?
**Answer:** Roberto Mancini
**Why it fails:** False premise: Italy kept 3 clean sheets at Euro 2020, not 4 (the coach, Mancini, is right, but the '4 clean sheets' figure is wrong).
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to 3 clean sheets.

### Row 33541 — Italy (easy) — FAIL
**Q:** Which Italy forward scored in three Euro 2020 knockout games?
**Answer:** Federico Chiesa
**Why it fails:** False: Chiesa scored in TWO Euro 2020 knockout games (Austria, Spain), not three - he did not score v Belgium.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to two knockout goals.

### Row 33542 — Italy (easy) — FAIL
**Q:** Which Italy forward scored in three separate Euro 2020 knockout matches?
**Answer:** Federico Chiesa
**Why it fails:** False: Chiesa scored in two knockout matches (Austria, Spain), not three.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to two.

### Row 33600 — Italy (easy) — FAIL
**Q:** Which Italy manager favoured a 3-5-2 or 4-3-3 formation at the 2026 World Cup?
**Answer:** Luciano Spalletti
**Why it fails:** False premise: Italy did NOT play at the 2026 World Cup (failed to qualify), and Spalletti was sacked in June 2025 - he used no formation 'at the 2026 World Cup'.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Reframe to the qualifying cycle, not the tournament.

### Row 33608 — Italy (easy) — FAIL
**Q:** Which Italy manager is leading their 2026 FIFA World Cup qualifying campaign?
**Answer:** Luciano Spalletti
**Why it fails:** False as of 2026: Spalletti is NOT leading the 2026 qualifying campaign - he was sacked in June 2025, Gattuso ran the campaign, and it ended with the playoff loss to Bosnia.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Credit Gattuso (and note Italy failed to qualify).

### Row 33609 — Italy (easy) — FAIL
**Q:** Which Italy manager leads their 2026 World Cup qualifying campaign?
**Answer:** Luciano Spalletti
**Why it fails:** False as of 2026: Spalletti does not lead the 2026 qualifying campaign; he was sacked in June 2025 and Gattuso ran it.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Credit Gattuso.

### Row 33616 — Italy (easy) — FAIL
**Q:** Which Italy manager led their 2026 World Cup qualifying campaign?
**Answer:** Luciano Spalletti
**Why it fails:** False as of 2026: Spalletti did NOT lead the 2026 qualifying campaign - he was sacked in June 2025 after the opening qualifiers; Gattuso led the campaign, which ended in the playoff loss to Bosnia.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Credit Gattuso with leading the campaign.

### Row 33640 — Italy (medium) — FAIL
**Q:** Which Italy manager oversaw their 2026 World Cup qualification?
**Answer:** Luciano Spalletti
**Why it fails:** False: Italy did NOT qualify for the 2026 World Cup (lost the playoff final to Bosnia); Spalletti was sacked in June 2025.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 33650 — Italy (easy) — FAIL
**Q:** Which Italy manager qualified them for the 2026 FIFA World Cup?
**Answer:** Luciano Spalletti
**Why it fails:** False: Italy did NOT qualify for the 2026 World Cup; Spalletti was also sacked in June 2025.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 33667 — Italy (medium) — FAIL
**Q:** Which Italy manager secured 2026 World Cup qualification after their 2022 failure?
**Answer:** Luciano Spalletti
**Why it fails:** False: Italy did NOT secure 2026 qualification - they lost the playoff final to Bosnia; Spalletti was sacked in June 2025.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026 (a third straight miss).

### Row 33668 — Italy (medium) — FAIL
**Q:** Which Italy manager secured 2026 World Cup qualification through UEFA?
**Answer:** Luciano Spalletti
**Why it fails:** False: Italy did NOT qualify for 2026 through UEFA; they lost the playoff final to Bosnia.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 33670 — Italy (medium) — FAIL
**Q:** Which Italy manager secured their 2026 FIFA World Cup qualification?
**Answer:** Spalletti
**Why it fails:** False: Italy did not secure 2026 qualification; Spalletti was also sacked in June 2025.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 33671 — Italy (medium) — FAIL
**Q:** Which Italy manager secured their 2026 World Cup qualification?
**Answer:** Luciano Spalletti
**Why it fails:** False: Italy did NOT qualify for 2026 (lost to Bosnia in the playoff final).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 33694 — Italy (easy) — FAIL
**Q:** Which Italy manager will lead their 2026 FIFA World Cup qualifying campaign?
**Answer:** Luciano Spalletti
**Why it fails:** False as of 2026: Spalletti did NOT lead the 2026 qualifying campaign - he was sacked in June 2025; Gattuso led it and Italy failed to qualify.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Credit Gattuso (and note the campaign is over and failed).

### Row 33706 — Italy (easy) — FAIL
**Q:** Which Italy manager's tactics conceded just 3 goals at Euro 2020?
**Answer:** Roberto Mancini
**Why it fails:** False premise: Italy conceded 4 goals at Euro 2020, not 3 (the manager, Mancini, is right).
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to 4 goals.

### Row 33720 — Italy (easy) — FAIL
**Q:** Which Italy midfielder made the Euro 2012 Team of the Tournament?
**Answer:** Andrea Pirlo
**Why it fails:** Non-unique: both Pirlo AND De Rossi were in the Euro 2012 Team of the Tournament.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2012
**Remedy:** Remove De Rossi as a distractor.

### Row 33722 — Italy (easy) — FAIL
**Q:** Which Italy midfielder missed two penalties at Euro 2020?
**Answer:** Jorginho
**Why it fails:** False: Jorginho missed only ONE penalty at Euro 2020 (the final); his two penalty misses were v Switzerland in 2022 WC qualifying.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Re-anchor the two misses to 2022 qualifying.

### Row 33730 — Italy (easy) — FAIL
**Q:** Which Italy midfielder was honored in the Euro 2012 Team of the Tournament?
**Answer:** Andrea Pirlo
**Why it fails:** Non-unique: both Pirlo AND De Rossi were in the Euro 2012 Team of the Tournament.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2012
**Remedy:** Remove De Rossi as a distractor.

### Row 33734 — Italy (easy) — FAIL
**Q:** Which Italy midfielder was key at Euro 2020 despite missing two penalties?
**Answer:** Jorginho
**Why it fails:** False: Jorginho missed only one penalty at Euro 2020 (the final). His two misses were v Switzerland in 2022 WC qualifying.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Re-anchor the two misses to 2022 qualifying.

### Row 33746 — Italy (easy) — FAIL
**Q:** Which Italy player for the 2026 World Cup is based at PSG?
**Answer:** Gianluigi Donnarumma
**Why it fails:** Outdated: Donnarumma left PSG for Manchester City in September 2025; he is no longer at PSG.
**Source:** https://en.wikipedia.org/wiki/Gianluigi_Donnarumma
**Remedy:** Update to Manchester City.

### Row 33747 — Italy (easy) — FAIL
**Q:** Which Italy player for the 2026 World Cup squad is based abroad?
**Answer:** Gianluigi Donnarumma
**Why it fails:** Non-unique/false: Donnarumma (Man City) AND Chiesa (Liverpool) are both based abroad, and the explanation that the others are all Serie A is wrong.
**Source:** https://en.wikipedia.org/wiki/Federico_Chiesa
**Remedy:** Fix the clubs and leave one abroad-based player.

### Row 33764 — Italy (easy) — FAIL
**Q:** Which Italy player made the Euro 2020 Team of the Tournament?
**Answer:** Federico Chiesa
**Why it fails:** Non-unique: both Chiesa AND Bonucci were in the Euro 2020 Team of the Tournament.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Remove Bonucci as a distractor.

### Row 33765 — Italy (easy) — FAIL
**Q:** Which Italy player missed a penalty in the Euro 2020 semi-final shootout?
**Answer:** Jorginho
**Why it fails:** False: Jorginho did NOT miss in the Euro 2020 semi-final shootout - he SCORED the winning penalty v Spain. His miss came in the final.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Re-anchor the miss to the final.

### Row 33766 — Italy (easy) — FAIL
**Q:** Which Italy player missed a penalty in their Euro 2020 semi-final shootout win?
**Answer:** Jorginho
**Why it fails:** False: Jorginho scored the winning penalty in the Euro 2020 SF shootout v Spain - he did not miss it. His miss was in the final.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Re-anchor the miss to the final.

### Row 33767 — Italy (easy) — FAIL
**Q:** Which Italy player missed two penalties at Euro 2020, but his team still reached the final?
**Answer:** Jorginho
**Why it fails:** False: Jorginho missed only one penalty at Euro 2020 (the final), and he SCORED the SF shootout winner v Spain. The 'two penalties including the SF' claim is wrong.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to one miss (the final); the two misses were in 2022 qualifying.

### Row 33768 — Italy (easy) — FAIL
**Q:** Which Italy player missed two penalties at Euro 2020?
**Answer:** Jorginho
**Why it fails:** False: Jorginho missed one penalty at Euro 2020 (the final); the two misses were v Switzerland in 2022 qualifying.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Re-anchor the two misses to 2022 qualifying.

### Row 33769 — Italy (easy) — FAIL
**Q:** Which Italy player missed two penalties during Euro 2020?
**Answer:** Jorginho
**Why it fails:** False: Jorginho missed only one penalty at Euro 2020 (the final).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_qualification_(UEFA)
**Remedy:** Re-anchor the two misses to 2022 qualifying.

### Row 33800 — Italy (easy) — FAIL
**Q:** Which Italy player scored at Euro 2020 against Austria, Belgium, and Spain?
**Answer:** Federico Chiesa
**Why it fails:** False: Chiesa scored v Austria and Spain at Euro 2020 but NOT v Belgium.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Drop Belgium.

### Row 33803 — Italy (medium) — FAIL
**Q:** Which Italy player scored in the 2020 Euros knockout stages against Austria, Belgium, and Spain?
**Answer:** Federico Chiesa
**Why it fails:** False: Chiesa scored v Austria and Spain, not Belgium, in the Euro 2020 knockouts.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Drop Belgium.

### Row 33813 — Italy (medium) — FAIL
**Q:** Which Italy player scored in three different Euro 2020 knockout stage matches?
**Answer:** Federico Chiesa
**Why it fails:** False: Chiesa scored in TWO Euro 2020 knockout matches (Austria, Spain), not three (he did not score v Belgium).
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to two.

### Row 33848 — Italy (easy) — FAIL
**Q:** Which Italy player was in the Euro 2020 Team of the Tournament?
**Answer:** Federico Chiesa
**Why it fails:** Non-unique: Chiesa, Bonucci AND Donnarumma were all in the Euro 2020 Team of the Tournament.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Leave only one 2020-ToT Italian among the options.

### Row 33852 — Italy (easy) — FAIL
**Q:** Which Italy player was named in the Euro 2012 Team of the Tournament?
**Answer:** Andrea Pirlo
**Why it fails:** Non-unique: both Pirlo AND Buffon were in the Euro 2012 Team of the Tournament.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2012
**Remedy:** Remove Buffon as a distractor.

### Row 33864 — Italy (easy) — FAIL
**Q:** Which Italy player's Euro 2020 performance earned him a Team of the Tournament spot?
**Answer:** Federico Chiesa
**Why it fails:** Non-unique: both Chiesa AND Bonucci were in the Euro 2020 Team of the Tournament.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Remove Bonucci as a distractor.

### Row 33866 — Italy (easy) — FAIL
**Q:** Which Italy player's Euro Team of Tournament inclusion came after Andrea Pirlo's?
**Answer:** Federico Chiesa
**Why it fails:** Non-unique: the Italian named in the Euro 2020 ToT (after Pirlo's 2012 inclusion) was not only Chiesa - Bonucci (also an option) was in it too.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020
**Remedy:** Remove Bonucci as a distractor.

### Row 33878 — Italy (easy) — FAIL
**Q:** Which Italy striker had over 50 caps and 14 goals?
**Answer:** Ciro Immobile
**Why it fails:** Wrong: Immobile scored 17 goals for Italy, not 14.
**Source:** https://en.wikipedia.org/wiki/Ciro_Immobile
**Remedy:** Change to 17 goals.

### Row 33879 — Italy (easy) — FAIL
**Q:** Which Italy striker had over 50 caps but under 15 goals?
**Answer:** Ciro Immobile
**Why it fails:** Wrong: Immobile has 17 Italy goals - not 'under 15'.
**Source:** https://en.wikipedia.org/wiki/Ciro_Immobile
**Remedy:** Correct the goal count to 17.

### Row 33902 — Italy (easy) — FAIL
**Q:** Which Italy winger, a Juventus player, was in their 2026 World Cup squad?
**Answer:** Federico Chiesa
**Why it fails:** Outdated criterion: Chiesa left Juventus for Liverpool in 2024, so 'a Juventus player' is wrong; and Italy had no 2026 World Cup squad (they failed to qualify).
**Source:** https://en.wikipedia.org/wiki/Federico_Chiesa
**Remedy:** Update his club to Liverpool and drop the 2026-squad framing.

### Row 33903 — Italy (easy) — FAIL
**Q:** Which Italy winger, fit for the 2026 World Cup, plays for Juventus?
**Answer:** Federico Chiesa
**Why it fails:** Outdated: Chiesa plays for Liverpool (since 2024), not Juventus.
**Source:** https://en.wikipedia.org/wiki/Federico_Chiesa
**Remedy:** Update his club to Liverpool.

### Row 33909 — Italy (medium) — FAIL
**Q:** Which manager guided Italy to 2026 FIFA World Cup qualification?
**Answer:** Luciano Spalletti
**Why it fails:** False: Italy did NOT qualify for the 2026 World Cup (lost the playoff final to Bosnia); Spalletti was sacked in June 2025.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 33911 — Italy (easy) — FAIL
**Q:** Which manager is leading Italy in the 2026 FIFA World Cup qualifiers?
**Answer:** Luciano Spalletti
**Why it fails:** False as of 2026: Spalletti is not leading the 2026 qualifiers - he was sacked in June 2025 and Gattuso ran the (failed) campaign.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Credit Gattuso.

### Row 33913 — Italy (easy) — FAIL
**Q:** Which manager is leading Italy's 2026 World Cup qualifying campaign?
**Answer:** Luciano Spalletti
**Why it fails:** False as of 2026: Spalletti does not lead the 2026 qualifying campaign; Gattuso ran it after Spalletti's June 2025 sacking.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Credit Gattuso.

### Row 33914 — Italy (easy) — FAIL
**Q:** Which manager leads Italy in 2026 World Cup qualifying?
**Answer:** Luciano Spalletti
**Why it fails:** False as of 2026: Gattuso, not Spalletti, ran the 2026 qualifying campaign (Spalletti was sacked June 2025).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Credit Gattuso.

### Row 33918 — Italy (easy) — FAIL
**Q:** Which manager led Italy in the 2026 World Cup qualifiers?
**Answer:** Luciano Spalletti
**Why it fails:** False as of 2026: Spalletti did not run the 2026 qualifiers - he managed only the opening games before being sacked in June 2025; Gattuso led the campaign, which failed.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Credit Gattuso.

### Row 33919 — Italy (medium) — FAIL
**Q:** Which manager led Italy to 2026 World Cup qualification?
**Answer:** Luciano Spalletti
**Why it fails:** False: Italy did NOT qualify for 2026 (lost to Bosnia in the playoff final); Spalletti was also sacked in June 2025.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 33923 — Italy (easy) — FAIL
**Q:** Which manager led Italy to qualify for the 2026 World Cup?
**Answer:** Luciano Spalletti
**Why it fails:** False: Italy did NOT qualify for the 2026 World Cup; Spalletti was sacked in June 2025.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 33926 — Italy (easy) — FAIL
**Q:** Which manager led Italy's 2026 World Cup qualifying campaign?
**Answer:** Luciano Spalletti
**Why it fails:** False as of 2026: Gattuso (not Spalletti) led the 2026 qualifying campaign; Spalletti was sacked in June 2025.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Credit Gattuso.

### Row 33932 — Italy (easy) — FAIL
**Q:** Which manager qualified Italy for the 2026 World Cup via UEFA qualifiers?
**Answer:** Luciano Spalletti
**Why it fails:** False: Italy did NOT qualify for 2026 via UEFA - they lost the playoff final to Bosnia; Spalletti was also sacked in June 2025.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 33944 — Italy (easy) — FAIL
**Q:** Which nation also missed two consecutive World Cups before Italy?
**Answer:** No European nation
**Why it fails:** False: a major European nation did miss two consecutive World Cups before Italy - the Netherlands (an option here) missed both 1982 and 1986 (and England missed 1974 & 1978).
**Source:** https://en.wikipedia.org/wiki/Netherlands_national_football_team
**Remedy:** Change answer to the Netherlands (or fix the premise).

### Row 34057 — Italy (easy) — FAIL
**Q:** Which nation's 2018 World Cup playoff loss matched Italy's failure to qualify?
**Answer:** Sweden
**Why it fails:** False premise: Sweden did NOT lose a 2018 playoff - they WON it (beating Italy). The 'Sweden's playoff loss' framing is wrong.
**Source:** https://en.wikipedia.org/wiki/Italy_national_football_team
**Remedy:** Reword: Sweden won; Italy lost the playoff.

### Row 34082 — Italy (easy) — FAIL
**Q:** Which stadium hosted an Italy 2026 World Cup qualifier?
**Answer:** Stadio Olimpico
**Why it fails:** False: the Stadio Olimpico did NOT host a 2026 Italy qualifier (venues were Reggio Emilia, Bergamo, Udine, San Siro Milan); the foreign distractors are also implausible, so no option is correct.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use an actual 2026 venue (e.g. San Siro).

### Row 34083 — Italy (easy) — FAIL
**Q:** Which stadium hosted Italy's 2026 World Cup qualifier played in Turin?
**Answer:** Allianz Stadium
**Why it fails:** False premise: Italy did NOT play a 2026 qualifier in Turin/Allianz Stadium (their venues were Reggio Emilia, Bergamo, Udine, San Siro Milan).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Remove the Turin 2026-qualifier claim.

### Row 34090 — Italy (easy) — FAIL
**Q:** Which stadium in Turin hosted Italy's 2026 World Cup qualifiers?
**Answer:** Juventus Stadium
**Why it fails:** False + duplicate options: Italy did NOT host a 2026 qualifier in Turin, and 'Juventus Stadium' and 'Allianz Stadium' are the SAME stadium.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Remove the duplicate and the Turin claim.

### Row 34139 — Italy (easy) — FAIL
**Q:** Which team did Italy keep a clean sheet against in the Euro 2020 final?
**Answer:** England
**Why it fails:** False: Italy did NOT keep a clean sheet in the Euro 2020 final - it finished 1-1 (they conceded, then won on penalties). They had 3 clean sheets total, not 4.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2020_final
**Remedy:** Remove - the final was not a clean sheet.

### Row 34144 — Italy (easy) — FAIL
**Q:** Which team did Italy NOT eliminate in a major tournament semi-final?
**Answer:** Germany
**Why it fails:** False: Italy DID eliminate Germany in a semi-final - they beat Germany 2-1 in the Euro 2012 SF. (They also beat Spain in the 2020 SF.) Germany is not a team Italy failed to eliminate in a SF.
**Source:** https://en.wikipedia.org/wiki/UEFA_Euro_2012
**Remedy:** Pick a team Italy never beat in a SF (e.g. England or Belgium).

### Row 34145 — Italy (easy) — FAIL
**Q:** Which team did Italy NOT lose to at the 2014 FIFA World Cup?
**Answer:** England
**Why it fails:** Non-unique: Italy did not lose to England (they beat them) NOR to Brazil (whom they did not even play) at the 2014 World Cup, so two options fit 'did NOT lose to'.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_FIFA_World_Cup
**Remedy:** Use only actual 2014 opponents as distractors.

### Row 34191 — Italy (easy) — FAIL
**Q:** Which two Italian defenders retired after Euro 2020, enabling a squad evolution?
**Answer:** Bonucci and Chiellini
**Why it fails:** Inaccurate: Bonucci played for Italy until June 2023, so he did not retire 'after Euro 2020' (2021). Only Chiellini fits.
**Source:** https://en.wikipedia.org/wiki/Leonardo_Bonucci
**Remedy:** Bonucci's last cap was June 2023; don't pin him to Euro 2020.

### Row 34195 — Italy (easy) — FAIL
**Q:** Which two Italian defenders retired before the 2022 FIFA World Cup?
**Answer:** Bonucci and Chiellini
**Why it fails:** False: Bonucci did NOT retire before the 2022 World Cup - his last Italy cap was June 2023 (after the Nov-2022 WC). Only Chiellini retired before it.
**Source:** https://en.wikipedia.org/wiki/Leonardo_Bonucci
**Remedy:** Bonucci retired in 2023.

### Row 34196 — Italy (easy) — FAIL
**Q:** Which two Italian defenders retired internationally after Euro 2020?
**Answer:** Bonucci and Chiellini
**Why it fails:** Inaccurate: Bonucci played for Italy until June 2023; he did not retire after Euro 2020. Only Chiellini fits.
**Source:** https://en.wikipedia.org/wiki/Leonardo_Bonucci
**Remedy:** Bonucci's last cap was June 2023.

### Row 34199 — Italy (easy) — FAIL
**Q:** Which two Italy defenders retired after Euro 2020?
**Answer:** Bonucci and Chiellini
**Why it fails:** Inaccurate: Bonucci played for Italy until June 2023, not retiring after Euro 2020. Only Chiellini fits.
**Source:** https://en.wikipedia.org/wiki/Leonardo_Bonucci
**Remedy:** Bonucci retired in 2023.

### Row 34244 — Italy (hard) — FAIL
**Q:** Which World Cup did Italy qualify for under Luciano Spalletti?
**Answer:** 2026 FIFA World Cup
**Why it fails:** False: Italy did NOT qualify for the 2026 World Cup under Spalletti - they failed to qualify (lost the playoff final to Bosnia) and Spalletti was sacked in June 2025.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 34253 — Italy (medium) — FAIL
**Q:** Which year did Italy qualify for the 2026 FIFA World Cup?
**Answer:** 2026
**Why it fails:** False: Italy did NOT qualify for the 2026 World Cup (lost the playoff final to Bosnia, March 2026).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 34257 — Italy (easy) — FAIL
**Q:** Who is Italy's manager for the 2026 FIFA World Cup qualifiers?
**Answer:** Luciano Spalletti
**Why it fails:** False as of 2026: Spalletti was not Italy's manager for the 2026 qualifiers - he was sacked in June 2025 and Gattuso ran the (failed) campaign.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Credit Gattuso.

### Row 34258 — Italy (easy) — FAIL
**Q:** Who is leading Italy's 2026 World Cup qualifying campaign?
**Answer:** Luciano Spalletti
**Why it fails:** False as of 2026: Gattuso, not Spalletti, ran the 2026 qualifying campaign (Spalletti sacked June 2025).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Credit Gattuso.

### Row 34259 — Italy (easy) — FAIL
**Q:** Who is managing Italy for the 2026 FIFA World Cup qualifiers?
**Answer:** Luciano Spalletti
**Why it fails:** False as of 2026: Spalletti is not managing the 2026 qualifiers - he was sacked June 2025 and the campaign (run by Gattuso) is over.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Credit Gattuso.

### Row 34261 — Italy (easy) — FAIL
**Q:** Who managed Italy to qualify for the 2026 FIFA World Cup?
**Answer:** Luciano Spalletti
**Why it fails:** False: Italy did NOT qualify for the 2026 World Cup; Spalletti was sacked in June 2025.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 34265 — Italy (medium) — FAIL
**Q:** Who managed Italy's successful 2026 World Cup qualification?
**Answer:** Luciano Spalletti
**Why it fails:** False: Italy did NOT qualify for the 2026 World Cup (lost the playoff final to Bosnia); Spalletti was also sacked in June 2025 and Gattuso ran the failed campaign.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 34275 — Italy (medium) — FAIL
**Q:** Who was Italy's manager for their 2026 World Cup qualification?
**Answer:** Luciano Spalletti
**Why it fails:** False: Italy did NOT qualify for 2026; Spalletti was sacked in June 2025 and Gattuso led the failed campaign.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_second_round
**Remedy:** Remove - Italy did not qualify for 2026.

### Row 34279 — Italy (easy) — FAIL
**Q:** Why did Italy concede only 3 goals at Euro 2020?
**Answer:** Their defense was excellent
**Why it fails:** False premise: Italy conceded 4 goals at Euro 2020, not 3.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to 4 goals.

### Row 34287 — Italy (easy) — FAIL
**Q:** Why did Italy host a 2026 World Cup qualifier at Allianz Stadium?
**Answer:** Multiple venues used
**Why it fails:** False premise: Italy did NOT host a 2026 qualifier at the Allianz Stadium (Turin) - their venues were Reggio Emilia, Bergamo, Udine, San Siro Milan.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_UEFA_Group_I
**Remedy:** Use an actual 2026 venue.

### Row 34302 — Italy (hard) — FAIL
**Q:** Why did Italy rise to 7th in the FIFA rankings in 2021?
**Answer:** Winning Euro 2020
**Why it fails:** False premise: after Euro 2020 Italy rose to 5th, not 7th (7th was the pre-tournament rank).
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Fix the rank to 5th.

### Row 34305 — Italy (medium) — FAIL
**Q:** Why did Italy win the European Championship in 2020?
**Answer:** Conceded only 3 goals
**Why it fails:** False premise: Italy conceded 4 goals at Euro 2020, not 3.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to 4 goals.

### Row 34312 — Italy (medium) — FAIL
**Q:** Why did Italy's defense concede only 3 goals at Euro 2020?
**Answer:** Kept 4 clean sheets
**Why it fails:** False on both counts: Italy conceded 4 goals (not 3) and kept 3 clean sheets (not 4) at Euro 2020.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to 4 goals and 3 clean sheets.

### Row 34313 — Italy (easy) — FAIL
**Q:** Why did Italy's defense concede so few goals at Euro 2020?
**Answer:** Kept four clean sheets
**Why it fails:** False: Italy kept 3 clean sheets (not 4) and conceded 4 goals (not 3) at Euro 2020.
**Source:** https://en.wikipedia.org/wiki/Italy_at_the_UEFA_European_Championship
**Remedy:** Correct to 3 clean sheets / 4 goals.

### Row 34315 — Italy (hard) — FAIL
**Q:** Why did Italy's FIFA ranking improve to 7th in 2021?
**Answer:** Won Euro 2020
**Why it fails:** False premise: Italy improved to 5th after Euro 2020, not 7th.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Fix the rank to 5th.

### Row 34316 — Italy (hard) — FAIL
**Q:** Why did Italy's FIFA ranking rise to 7th in 2021?
**Answer:** Winning Euro 2020
**Why it fails:** False premise: Italy rose to 5th after Euro 2020, not 7th.
**Source:** https://en.wikipedia.org/wiki/FIFA_Men%27s_World_Ranking
**Remedy:** Fix the rank to 5th.
