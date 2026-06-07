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

Total failed-liveness-passed-others so far: **561** (Algeria 176 · Argentina 110 [COMPLETE through row 2160] · Brazil 6097–8182 COMPLETE: 218 · Cameroon 9574–10745 COMPLETE: 57)

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

### Row 6779 — Brazil (easy) — FAIL
**Q:** Which Brazil defender did NOT start as a first-choice centre-back at the 2022 World Cup?
**Answer:** David Luiz
**Why it fails:** Non-unique negative: besides David Luiz (not even in the squad), Éder Militão also did not start as a first-choice CENTRE-back in 2022 — he started at right-back. Two options satisfy 'did not start as first-choice CB'.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Drop — negative-framed and non-unique.

### Row 6810 — Brazil (easy) — FAIL
**Q:** Which Brazil manager oversaw the 2026 World Cup qualifiers?
**Answer:** Dorival Júnior
**Why it fails:** Non-unique: three of the four options (Dorival Júnior, Carlo Ancelotti AND Fernando Diniz) all oversaw parts of the 2026 qualification campaign, so there is no single correct answer.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop — multiple correct options (the campaign used 3 managers).

### Row 6815 — Brazil (medium) — FAIL
**Q:** Which Brazil manager oversaw their 2026 World Cup qualification campaign?
**Answer:** Dorival Júnior
**Why it fails:** Non-unique: Fernando Diniz, Dorival Júnior AND Carlo Ancelotti all oversaw parts of the 2026 qualification campaign — three of the four options are correct.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop — multiple correct options.

### Row 6887 — Brazil (easy) — FAIL
**Q:** Which Brazil player equaled Pelé's goal record in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar EQUALED Pelé's 77 against Croatia (Dec 2022). On 8 Sep 2023 v Bolivia he scored his 78th & 79th to SURPASS it — he did not 'equal with a 77th' there.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed', or move 'equal' to the 2022 Croatia game.

### Row 6888 — Brazil (easy) — FAIL
**Q:** Which Brazil player equalled Pelé's goal record in a 5-1 2023 World Cup qualifier win?
**Answer:** Neymar
**Why it fails:** False: in the Bolivia match Neymar surpassed (78th/79th), not equaled (77th) — he equaled v Croatia in 2022.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 6889 — Brazil (easy) — FAIL
**Q:** Which Brazil player equalled Pelé's goalscoring record in a 5-1 win over Bolivia in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar surpassed (not equaled) Pelé v Bolivia — he equaled at 77 v Croatia in 2022.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 6890 — Brazil (easy) — FAIL
**Q:** Which Brazil player equalled Pelé's record against Bolivia in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar surpassed Pelé v Bolivia (78th/79th); he equaled at 77 v Croatia in 2022.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 6891 — Brazil (easy) — FAIL
**Q:** Which Brazil player equalled Pelé's scoring record in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar surpassed Pelé v Bolivia; the 'equal at 77' came v Croatia in 2022.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 6899 — Brazil (easy) — FAIL
**Q:** Which Brazil player in the 2022 World Cup squad was based at Al-Hilal?
**Answer:** Neymar
**Why it fails:** Misleading premise: at the 2022 World Cup Neymar was based at PSG, NOT Al-Hilal (he joined Al-Hilal in 2023). No 2022 squad member was at Al-Hilal during the tournament.
**Source:** https://en.wikipedia.org/wiki/Neymar
**Remedy:** Drop, or reword to 'later joined Al-Hilal'.

### Row 6900 — Brazil (easy) — FAIL
**Q:** Which Brazil player is central to their 2026 World Cup cycle?
**Answer:** Rodrygo
**Why it fails:** Non-unique/subjective: Vinícius Jr. (an option) is at least as central to Brazil's 2026 cycle as Rodrygo, so 'Rodrygo' is not the unique answer.
**Source:** https://en.wikipedia.org/wiki/Brazil_national_football_team
**Remedy:** Drop — subjective and non-unique.

### Row 6907 — Brazil (easy) — FAIL
**Q:** Which Brazil player scored against Cameroon at the 2022 World Cup?
**Answer:** Raphinha
**Why it fails:** False: Brazil LOST 0-1 to Cameroon at 2022 and scored NO goal — Raphinha did not score against Cameroon (Aboubakar scored Cameroon's winner).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Drop — Brazil did not score v Cameroon.

### Row 6911 — Brazil (easy) — FAIL
**Q:** Which Brazil player scored at the 2019 Copa América?
**Answer:** Gabriel Jesus
**Why it fails:** Non-unique: besides Gabriel Jesus, both Philippe Coutinho and Richarlison (two of the other options) also scored at the 2019 Copa América.
**Source:** https://en.wikipedia.org/wiki/2019_Copa_Am%C3%A9rica
**Remedy:** Drop — multiple option-players scored.

### Row 6912 — Brazil (easy) — FAIL
**Q:** Which Brazil player scored his 77th goal, equalling Pelé's record, against Bolivia in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar's 77th (equaling Pelé) came v Croatia in 2022; v Bolivia (8 Sep 2023) he scored his 78th & 79th to surpass it.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 6923 — Brazil (easy) — FAIL
**Q:** Which Brazil player tied Pelé's goal record in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar tied Pelé's record (77) v Croatia in 2022, not v Bolivia in Sept 2023 (where he surpassed it with 78th/79th).
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 6940 — Brazil (hard) — FAIL
**Q:** Which Brazil squad first had players from six different nations' clubs?
**Answer:** 2022 World Cup squad
**Why it fails:** Explanation wrong: the 2022 squad's six countries were England, Spain, France, Italy, Mexico (Dani Alves/Pumas) and Brazil — NOT Germany.
**Source:** https://en.wikipedia.org/wiki/Template:Brazil_squad_2022_FIFA_World_Cup
**Remedy:** Replace 'Germany' with 'Mexico'.

### Row 6944 — Brazil (medium) — FAIL
**Q:** Which Brazil squad scored at a rate of 3 goals per match at the 2022 World Cup?
**Answer:** The 2022 squad
**Why it fails:** False premise: the '3 goals/match' rests on the false 15-goal figure — Brazil scored 8 in 5 matches (~1.6/match).
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Recompute from 8 goals.

### Row 6955 — Brazil (easy) — FAIL
**Q:** Which Brazil star matched Pelé's 77-goal record in a 5-1 2023 win over Bolivia?
**Answer:** Neymar
**Why it fails:** False: Neymar matched Pelé's 77 v Croatia in 2022, not in the 2023 Bolivia match (where he surpassed it with his 78th/79th).
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed', or move 'matched' to the 2022 Croatia game.

### Row 6956 — Brazil (easy) — FAIL
**Q:** Which Brazil star scored his 77th international goal in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar's 77th goal came v Croatia (Dec 2022). In September 2023 he scored his 78th & 79th, not his 77th.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Change to 78th/79th (surpassed), Sept 2023.

### Row 6960 — Brazil (easy) — FAIL
**Q:** Which Brazil training centre is in Teresópolis, Rio de Janeiro state?
**Answer:** CBF Training Centre
**Why it fails:** Non-unique/TC-16: the distractor 'Granja Comary Centre' is the SAME place as the answer 'CBF Training Centre' (the explanation says so).
**Source:** https://en.wikipedia.org/wiki/Brazil_national_football_team
**Remedy:** Replace 'Granja Comary' with a genuinely different distractor.

### Row 6961 — Brazil (medium) — FAIL
**Q:** Which Brazil winger scored at the 2022 World Cup group stage?
**Answer:** Raphinha
**Why it fails:** False: Raphinha did NOT score at the 2022 World Cup — South Korea was the R16 (not group stage) and Brazil scored nothing v Cameroon; Raphinha had 0 goals at the tournament.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Drop — Raphinha did not score at 2022.

### Row 6966 — Brazil (easy) — FAIL
**Q:** Which Brazilian 2014 World Cup stadium had a larger capacity than Arena Castelão?
**Answer:** Maracanã Stadium
**Why it fails:** Non-unique: more than one option exceeds Arena Castelão (~63,903) — the Maracanã (~74k) AND the Estádio Nacional in Brasília (~69k) are both larger.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_venues
**Remedy:** Drop — multiple larger venues among the options.

### Row 6973 — Brazil (easy) — FAIL
**Q:** Which Brazilian 2022 squad trait stemmed from their players' clubs?
**Answer:** Six different nations' leagues
**Why it fails:** Explanation wrong: the six leagues were England, Spain, France, Italy, Mexico and Brazil — NOT Germany.
**Source:** https://en.wikipedia.org/wiki/Template:Brazil_squad_2022_FIFA_World_Cup
**Remedy:** Replace 'Germany' with 'Mexico'.

### Row 6974 — Brazil (easy) — FAIL
**Q:** Which Brazilian 2022 World Cup player was based in the English Premier League?
**Answer:** Gabriel Martinelli
**Why it fails:** Non-unique: besides Gabriel Martinelli (Arsenal), Casemiro (Manchester United, an option) was also EPL-based at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/Template:Brazil_squad_2022_FIFA_World_Cup
**Remedy:** Drop — multiple EPL-based options.

### Row 6976 — Brazil (easy) — FAIL
**Q:** Which Brazilian 2022 World Cup squad member played for Liverpool?
**Answer:** Alisson
**Why it fails:** Non-unique: both Alisson AND Fabinho (an option) were Liverpool players in Brazil's 2022 squad.
**Source:** https://www.liverpoolfc.com/news/alisson-becker-and-fabinho-named-brazils-world-cup-squad
**Remedy:** Drop — two Liverpool players among the options.

### Row 6993 — Brazil (easy) — FAIL
**Q:** Which Brazilian centre-back has over 90 caps and played at both the 2018 and 2022 World Cups?
**Answer:** Marquinhos
**Why it fails:** Non-unique: Thiago Silva (an option) also has well over 90 caps and played at both the 2018 and 2022 World Cups.
**Source:** https://en.wikipedia.org/wiki/Thiago_Silva
**Remedy:** Drop — Thiago Silva equally satisfies the description.

### Row 6995 — Brazil (easy) — FAIL
**Q:** Which Brazilian centre-back partnered Thiago Silva at the 2018 and 2022 FIFA World Cups?
**Answer:** Marquinhos
**Why it fails:** Wrong for 2018: Thiago Silva's first-choice centre-back partner at the 2018 World Cup was Miranda (an option here), not Marquinhos (who featured at right-back/as backup). Marquinhos was his partner only in 2022.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2018_FIFA_World_Cup
**Remedy:** For 2018 the answer is Miranda; restrict the question to 2022.

### Row 6996 — Brazil (easy) — FAIL
**Q:** Which Brazilian centre-back partnered Thiago Silva at the 2018 World Cup?
**Answer:** Marquinhos
**Why it fails:** Wrong: at the 2018 World Cup Thiago Silva's centre-back partner was Miranda (an option), not Marquinhos.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2018_FIFA_World_Cup
**Remedy:** Change answer to Miranda for 2018.

### Row 6999 — Brazil (easy) — FAIL
**Q:** Which Brazilian centre-back played at both the 2018 and 2022 World Cups?
**Answer:** Marquinhos
**Why it fails:** Non-unique: Thiago Silva (an option) is also a centre-back who played at both the 2018 and 2022 World Cups.
**Source:** https://en.wikipedia.org/wiki/Thiago_Silva
**Remedy:** Drop — Thiago Silva equally satisfies the description.

### Row 7000 — Brazil (easy) — FAIL
**Q:** Which Brazilian city did NOT host a 2014 FIFA World Cup match?
**Answer:** Brasília
**Why it fails:** False: Brasília DID host 2014 World Cup matches — the Estádio Nacional Mané Garrincha staged 7 games (incl. a quarter-final and the third-place playoff). All four listed cities hosted.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_venues
**Remedy:** Drop — Brasília was a host city.

### Row 7001 — Brazil (easy) — FAIL
**Q:** Which Brazilian city hosted their 2-0 win over Uruguay in 2022 World Cup qualifiers?
**Answer:** Manaus
**Why it fails:** Wrong score: Brazil beat Uruguay 4-1 in Manaus (Oct 2021); the 2-0 win was away in Montevideo (Nov 2020).
**Source:** https://www.espn.com/soccer/report/_/gameId/561042
**Remedy:** Change the Manaus score to 4-1.

### Row 7003 — Brazil (easy) — FAIL
**Q:** Which Brazilian city was NOT a host for the 2014 FIFA World Cup?
**Answer:** Porto Alegre
**Why it fails:** False: Porto Alegre WAS a 2014 host city (Estádio Beira-Rio). All four listed cities hosted matches.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_venues
**Remedy:** Drop — Porto Alegre was a host city.

### Row 7092 — Brazil (easy) — FAIL
**Q:** Which Brazilian defender had over 115 caps and captained Brazil at multiple World Cups?
**Answer:** Thiago Silva
**Why it fails:** Wrong number: Thiago Silva has 113 caps, not 'over 115'. (He's still the most-capped option, but the stated criterion is false.)
**Source:** https://en.wikipedia.org/wiki/Thiago_Silva
**Remedy:** Change to 'over 110 caps' (he has 113).

### Row 7093 — Brazil (easy) — FAIL
**Q:** Which Brazilian defender had over 115 caps by 2023?
**Answer:** Thiago Silva
**Why it fails:** Wrong number: Thiago Silva has 113 caps, not over 115.
**Source:** https://en.wikipedia.org/wiki/Thiago_Silva
**Remedy:** Change to 'over 110 caps' (113).

### Row 7094 — Brazil (easy) — FAIL
**Q:** Which Brazilian defender had over 90 caps and played at the 2018 and 2022 World Cups?
**Answer:** Marquinhos
**Why it fails:** Non-unique: Thiago Silva (an option) also has 90+ caps and played at both the 2018 and 2022 World Cups, so 'Marquinhos' is not the unique answer.
**Source:** https://en.wikipedia.org/wiki/Thiago_Silva
**Remedy:** Drop — Thiago Silva equally satisfies the description.

### Row 7095 — Brazil (easy) — FAIL
**Q:** Which Brazilian defender has earned over 115 caps?
**Answer:** Thiago Silva
**Why it fails:** Wrong number: Thiago Silva has 113 caps, not over 115.
**Source:** https://en.wikipedia.org/wiki/Thiago_Silva
**Remedy:** Change to 'over 110 caps' (113).

### Row 7118 — Brazil (easy) — FAIL
**Q:** Which Brazilian defender scored against Colombia in the 2014 World Cup quarter-final?
**Answer:** Thiago Silva
**Why it fails:** Non-unique: in the 2-1 win over Colombia (2014 QF) BOTH Thiago Silva (7') and David Luiz (69', an option) scored. 'Which defender scored' has two correct answers.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2014_FIFA_World_Cup
**Remedy:** Add a discriminator (e.g. 'opening goal' → Thiago Silva, or 'free kick' → David Luiz).

### Row 7131 — Brazil (easy) — FAIL
**Q:** Which Brazilian defender was NOT part of Brazil's first-choice centre-back partnership at the 2022 World Cup?
**Answer:** Dani Alves
**Why it fails:** Non-unique negative: besides Dani Alves (a right-back), Éder Militão (an option) was also NOT part of the first-choice CB pair (Thiago Silva & Marquinhos) — he played right-back. Two options fit.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Drop — negative-framed and non-unique.

### Row 7136 — Brazil (medium) — FAIL
**Q:** Which Brazilian defender, with over 115 caps, captained the team at the 2022 World Cup group stage?
**Answer:** Thiago Silva
**Why it fails:** Wrong number: Thiago Silva has 113 caps, not 'over 115' (stated in the question stem).
**Source:** https://en.wikipedia.org/wiki/Thiago_Silva
**Remedy:** Change to 'over 110 caps' (113).

### Row 7137 — Brazil (easy) — FAIL
**Q:** Which Brazilian defender, with over 115 caps, captained them at the 2018 and 2022 World Cups?
**Answer:** Thiago Silva
**Why it fails:** Wrong number: Thiago Silva has 113 caps, not over 115.
**Source:** https://en.wikipedia.org/wiki/Thiago_Silva
**Remedy:** Change to 'over 110 caps' (113).

### Row 7144 — Brazil (medium) — FAIL
**Q:** Which Brazilian did NOT win the Confederations Cup Golden Ball in 2013?
**Answer:** Thiago Silva
**Why it fails:** Non-unique negative: three of the four options (Thiago Silva, Fred, Julio Cesar) did NOT win the 2013 Golden Ball (only Neymar did), so 'did not win' has multiple correct answers.
**Source:** https://en.wikipedia.org/wiki/2013_FIFA_Confederations_Cup
**Remedy:** Drop — negative-framed and non-unique.

### Row 7145 — Brazil (easy) — FAIL
**Q:** Which Brazilian equalled Pelé's goal record against Bolivia in 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar equaled Pelé's 77 v Croatia (2022); v Bolivia (Sept 2023) he scored his 78th & 79th to surpass it.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 7153 — Brazil (easy) — FAIL
**Q:** Which Brazilian forward equalled Pelé's goal record in a 2023 World Cup qualifier?
**Answer:** Neymar
**Why it fails:** False: Neymar surpassed (not equaled) Pelé v Bolivia in Sept 2023 (78th/79th); he equaled at 77 v Croatia in 2022.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 7155 — Brazil (easy) — FAIL
**Q:** Which Brazilian forward scored at the 2019 Copa América?
**Answer:** Gabriel Jesus
**Why it fails:** Non-unique: all four option-players (Gabriel Jesus, Richarlison, Coutinho, Firmino) scored at the 2019 Copa América.
**Source:** https://en.wikipedia.org/wiki/2019_Copa_Am%C3%A9rica
**Remedy:** Drop — multiple option-players scored.

### Row 7157 — Brazil (easy) — FAIL
**Q:** Which Brazilian forward was a 2022 World Cup squad member and is key for 2026 qualifying?
**Answer:** Rodrygo
**Why it fails:** Non-unique: Vinícius Jr. (an option) was also in the 2022 squad and is a key player for the 2026 cycle, so 'Rodrygo' is not unique.
**Source:** https://en.wikipedia.org/wiki/Brazil_national_football_team
**Remedy:** Drop — non-unique.

### Row 7161 — Brazil (easy) — FAIL
**Q:** Which Brazilian forward was in the 2022 World Cup squad?
**Answer:** Rodrygo
**Why it fails:** Non-unique: Rodrygo, Gabriel Martinelli AND Vinícius Jr. (three of the four options) were all in the 2022 World Cup squad.
**Source:** https://en.wikipedia.org/wiki/Template:Brazil_squad_2022_FIFA_World_Cup
**Remedy:** Drop — multiple option-players were in the squad.

### Row 7162 — Brazil (easy) — FAIL
**Q:** Which Brazilian forward was part of the 2022 World Cup squad?
**Answer:** Rodrygo
**Why it fails:** Non-unique: Rodrygo, Martinelli AND Vinícius Jr. were all in the 2022 squad.
**Source:** https://en.wikipedia.org/wiki/Template:Brazil_squad_2022_FIFA_World_Cup
**Remedy:** Drop — multiple option-players were in the squad.

### Row 7164 — Brazil (medium) — FAIL
**Q:** Which Brazilian goalkeeper played in their 2022 World Cup group stage match against Cameroon?
**Answer:** Alisson
**Why it fails:** False: Ederson (not Alisson) started in goal v Cameroon at 2022 — Tite made nine changes and rested Alisson.
**Source:** https://www.90min.com/posts/cameroon-vs-brazil-world-cup-team-news-lineups-prediction-02-12-22
**Remedy:** Change answer to Ederson.

### Row 7187 — Brazil (easy) — FAIL
**Q:** Which Brazilian is a key player for the 2026 World Cup cycle?
**Answer:** Rodrygo
**Why it fails:** Non-unique/subjective: Vinícius Jr. (an option) is at least as much a key 2026 player as Rodrygo.
**Source:** https://en.wikipedia.org/wiki/Brazil_national_football_team
**Remedy:** Drop — non-unique.

### Row 7195 — Brazil (easy) — FAIL
**Q:** Which Brazilian manager coached during the 2026 World Cup qualifying campaign?
**Answer:** Dorival Júnior
**Why it fails:** Non-unique: Carlo Ancelotti (an option) also coached during the 2026 qualifying campaign (he took over in May 2025).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop — Ancelotti also qualifies.

### Row 7196 — Brazil (easy) — FAIL
**Q:** Which Brazilian manager coached in the 2026 World Cup qualifiers?
**Answer:** Dorival Júnior
**Why it fails:** Non-unique: Ancelotti (an option) also coached in the 2026 qualifiers.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop — Ancelotti also qualifies.

### Row 7197 — Brazil (medium) — FAIL
**Q:** Which Brazilian manager faced Mexico in both the 2018 World Cup group stage and round of 16?
**Answer:** Tite
**Why it fails:** False premise: Brazil did NOT face Mexico in the 2018 group stage (Mexico was not in their group). They met only in the R16.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_E
**Remedy:** Drop — non-existent group meeting.

### Row 7206 — Brazil (easy) — FAIL
**Q:** Which Brazilian manager oversaw part of the 2026 World Cup qualifying campaign?
**Answer:** Dorival Júnior
**Why it fails:** Non-unique: Fernando Diniz, Dorival Júnior AND Carlo Ancelotti all oversaw parts of the 2026 campaign.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop — multiple correct options.

### Row 7209 — Brazil (medium) — FAIL
**Q:** Which Brazilian manager oversaw the 2026 World Cup qualification campaign in 2024-2025?
**Answer:** Dorival Júnior
**Why it fails:** Non-unique: Fernando Diniz and Carlo Ancelotti (options) also oversaw parts of the 2026 campaign.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop — multiple correct options.

### Row 7212 — Brazil (medium) — FAIL
**Q:** Which Brazilian manager oversaw their 2026 World Cup qualification campaign?
**Answer:** Dorival Júnior
**Why it fails:** Non-unique: Carlo Ancelotti (an option) also oversaw the 2026 qualification campaign.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop — Ancelotti also qualifies.

### Row 7248 — Brazil (easy) — FAIL
**Q:** Which Brazilian manager's tenure was part of the 2026 World Cup qualifying campaign?
**Answer:** Dorival Júnior
**Why it fails:** Non-unique: Carlo Ancelotti (an option) was also part of the 2026 qualifying campaign (from May 2025).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CONMEBOL)
**Remedy:** Drop — Ancelotti also qualifies.

### Row 7258 — Brazil (easy) — FAIL
**Q:** Which Brazilian midfielder retired in 2023 after starting at the 2018 World Cup?
**Answer:** Fred
**Why it fails:** False: Fred did NOT start at the 2018 World Cup — he was a fringe squad player (midfield trio: Casemiro/Paulinho/Coutinho). He became a starter in 2022, not 2018.
**Source:** https://en.wikipedia.org/wiki/Fred_(footballer,_born_1993)
**Remedy:** Change to 'started at the 2022 World Cup'.

### Row 7262 — Brazil (easy) — FAIL
**Q:** Which Brazilian midfielder started against Belgium in the 2018 World Cup quarter-final?
**Answer:** Fred
**Why it fails:** False: Fred did not start the 2018 QF v Belgium — Fernandinho replaced the suspended Casemiro (and scored the own goal). Fred was a fringe 2018 player.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2018_FIFA_World_Cup
**Remedy:** The 2018 QF starter was Fernandinho; reword.

### Row 7263 — Brazil (easy) — FAIL
**Q:** Which Brazilian midfielder started at the 2018 World Cup and retired in 2023?
**Answer:** Fred
**Why it fails:** False: Fred did not start at the 2018 World Cup (fringe player). He started in 2022.
**Source:** https://en.wikipedia.org/wiki/Fred_(footballer,_born_1993)
**Remedy:** Change to 'started at the 2022 World Cup'.

### Row 7264 — Brazil (easy) — FAIL
**Q:** Which Brazilian midfielder started at the 2018 World Cup and was in the 2022 squad?
**Answer:** Fred
**Why it fails:** False: Fred did not start at the 2018 World Cup (he was a fringe squad player).
**Source:** https://en.wikipedia.org/wiki/Fred_(footballer,_born_1993)
**Remedy:** Change to 2022; also non-unique (Casemiro fits 'started 2018 + 2022 squad' better).

### Row 7265 — Brazil (easy) — FAIL
**Q:** Which Brazilian midfielder started at the 2018 World Cup?
**Answer:** Fred
**Why it fails:** False: Fred did not start at the 2018 World Cup; the starters were Casemiro/Paulinho/Coutinho.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2018_FIFA_World_Cup
**Remedy:** Change to 2022.

### Row 7266 — Brazil (easy) — FAIL
**Q:** Which Brazilian midfielder started for Brazil in the 2018 World Cup?
**Answer:** Fred
**Why it fails:** False: Fred did not start at the 2018 World Cup.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2018_FIFA_World_Cup
**Remedy:** Change to 2022.

### Row 7268 — Brazil (easy) — FAIL
**Q:** Which Brazilian midfielder started in 2018 but was only a squad player in 2022?
**Answer:** Fred
**Why it fails:** Reversed: Fred was a fringe/bench player in 2018 and a STARTER in 2022 — not 'started 2018, bench 2022'.
**Source:** https://en.wikipedia.org/wiki/Fred_(footballer,_born_1993)
**Remedy:** Reverse the years.

### Row 7269 — Brazil (easy) — FAIL
**Q:** Which Brazilian midfielder started in midfield at the 2018 FIFA World Cup?
**Answer:** Fred
**Why it fails:** False: Fred did not start in midfield at the 2018 World Cup.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2018_FIFA_World_Cup
**Remedy:** Change to 2022.

### Row 7271 — Brazil (easy) — FAIL
**Q:** Which Brazilian midfielder started in the 2018 World Cup quarter-final?
**Answer:** Fred
**Why it fails:** False: Fred did not start the 2018 QF (Fernandinho replaced the suspended Casemiro).
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2018_FIFA_World_Cup
**Remedy:** Reword — Fred was not a 2018 starter.

### Row 7272 — Brazil (easy) — FAIL
**Q:** Which Brazilian midfielder started in the 2018 World Cup?
**Answer:** Fred
**Why it fails:** False: Fred did not start at the 2018 World Cup.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2018_FIFA_World_Cup
**Remedy:** Change to 2022.

### Row 7273 — Brazil (easy) — FAIL
**Q:** Which Brazilian midfielder started in the 2018 World Cup's midfield?
**Answer:** Fred
**Why it fails:** False: Fred did not start in the 2018 midfield (Casemiro/Paulinho/Coutinho did).
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2018_FIFA_World_Cup
**Remedy:** Change to 2022.

### Row 7274 — Brazil (easy) — FAIL
**Q:** Which Brazilian midfielder started matches at the 2018 FIFA World Cup?
**Answer:** Fred
**Why it fails:** False: Fred did not start matches at the 2018 World Cup (the explanation's claim is wrong); Casemiro and Paulinho were the 2018 midfield starters.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2018_FIFA_World_Cup
**Remedy:** Change to 2022.

### Row 7275 — Brazil (easy) — FAIL
**Q:** Which Brazilian midfielder started matches at the 2018 World Cup but retired before 2026?
**Answer:** Fred
**Why it fails:** False: Fred did not start at the 2018 World Cup (fringe player).
**Source:** https://en.wikipedia.org/wiki/Fred_(footballer,_born_1993)
**Remedy:** Change to 2022.

### Row 7276 — Brazil (easy) — FAIL
**Q:** Which Brazilian midfielder was in both the 2018 and 2022 World Cup squads?
**Answer:** Fred
**Why it fails:** Non-unique: Gabriel Jesus (an option) was also in both the 2018 and 2022 squads.
**Source:** https://en.wikipedia.org/wiki/Gabriel_Jesus
**Remedy:** Drop — multiple option-players were in both squads.

### Row 7284 — Brazil (easy) — FAIL
**Q:** Which Brazilian midfielder was part of the 2022 World Cup squad?
**Answer:** Fred
**Why it fails:** Non-unique: Casemiro and Lucas Paquetá (options) were also in the 2022 squad.
**Source:** https://en.wikipedia.org/wiki/Template:Brazil_squad_2022_FIFA_World_Cup
**Remedy:** Drop — multiple option-players were in the squad.

### Row 7319 — Brazil (medium) — FAIL
**Q:** Which Brazilian player did NOT score in the 2013 Confederations Cup final?
**Answer:** Thiago Silva
**Why it fails:** Non-unique negative: both Thiago Silva AND Oscar (options) did NOT score in the 2013 final (only Fred x2 and Neymar did).
**Source:** https://en.wikipedia.org/wiki/2013_FIFA_Confederations_Cup_final
**Remedy:** Drop — negative-framed and non-unique.

### Row 7328 — Brazil (easy) — FAIL
**Q:** Which Brazilian player equaled Pelé's goal record in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar equaled Pelé's 77 v Croatia (2022); v Bolivia (Sept 2023) he surpassed it (78th/79th).
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 7329 — Brazil (easy) — FAIL
**Q:** Which Brazilian player equaled Pelé's national scoring record in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar equaled Pelé v Croatia (2022), not v Bolivia (where he surpassed it).
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 7331 — Brazil (easy) — FAIL
**Q:** Which Brazilian player equalled Pelé's goal record against Bolivia in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar surpassed (not equaled) Pelé v Bolivia in Sept 2023.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 7333 — Brazil (easy) — FAIL
**Q:** Which Brazilian player equalled Pelé's goal record in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar equaled Pelé v Croatia (2022), not in Sept 2023.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 7334 — Brazil (easy) — FAIL
**Q:** Which Brazilian player equalled Pelé's goals record in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar surpassed Pelé v Bolivia (Sept 2023); he equaled at 77 v Croatia in 2022.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 7335 — Brazil (easy) — FAIL
**Q:** Which Brazilian player equalled Pelé's goalscoring record in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar surpassed Pelé v Bolivia (Sept 2023); equaled v Croatia 2022.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 7336 — Brazil (easy) — FAIL
**Q:** Which Brazilian player equalled Pelé's national team scoring record in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar matched Pelé v Croatia (2022); v Bolivia he surpassed it.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 7337 — Brazil (easy) — FAIL
**Q:** Which Brazilian player equalled Pelé's scoring record in a 2023 World Cup qualifier against Bolivia?
**Answer:** Neymar
**Why it fails:** False: Neymar surpassed (not matched) Pelé in the Bolivia qualifier (78th/79th).
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 7361 — Brazil (easy) — FAIL
**Q:** Which Brazilian player is a key part of the 2026 World Cup cycle?
**Answer:** Rodrygo
**Why it fails:** Non-unique: Vinícius Jr. (an option) was also in the 2022 squad and is a key 2026 player.
**Source:** https://en.wikipedia.org/wiki/Brazil_national_football_team
**Remedy:** Drop — non-unique.

### Row 7365 — Brazil (easy) — FAIL
**Q:** Which Brazilian player matched Pelé's international goal record in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar matched Pelé's 77 v Croatia (2022), not v Bolivia (Sept 2023, where he surpassed it).
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 7380 — Brazil (easy) — FAIL
**Q:** Which Brazilian player scored 4 goals at the 2022 FIFA World Cup?
**Answer:** Richarlison
**Why it fails:** Wrong number: Richarlison scored 3 goals at the 2022 World Cup (2 v Serbia, 1 v South Korea), not 4.
**Source:** https://en.wikipedia.org/wiki/Richarlison
**Remedy:** Change to 3 goals.

### Row 7393 — Brazil (easy) — FAIL
**Q:** Which Brazilian player scored a hat-trick at the 2022 World Cup?
**Answer:** No Brazilian player
**Why it fails:** Answer 'no Brazilian scored a hat-trick' is correct, but the explanation repeats the false 15-goal figure (Brazil scored 8 at 2022).
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Fix the explanation: 8 goals, not 15.

### Row 7406 — Brazil (easy) — FAIL
**Q:** Which Brazilian player scored at the 2019 Copa América and played in the 2018 World Cup?
**Answer:** Gabriel Jesus
**Why it fails:** Non-unique: Philippe Coutinho (an option) also scored at the 2019 Copa AND played at the 2018 World Cup.
**Source:** https://en.wikipedia.org/wiki/2019_Copa_Am%C3%A9rica
**Remedy:** Drop — non-unique.

### Row 7409 — Brazil (easy) — FAIL
**Q:** Which Brazilian player scored at the 2019 Copa América?
**Answer:** Gabriel Jesus
**Why it fails:** Non-unique: Richarlison and Coutinho (options) also scored at the 2019 Copa América.
**Source:** https://en.wikipedia.org/wiki/2019_Copa_Am%C3%A9rica
**Remedy:** Drop — non-unique.

### Row 7412 — Brazil (easy) — FAIL
**Q:** Which Brazilian player scored four goals at the 2022 FIFA World Cup?
**Answer:** Richarlison
**Why it fails:** Wrong number: Richarlison scored 3 at the 2022 World Cup, not 4.
**Source:** https://en.wikipedia.org/wiki/Richarlison
**Remedy:** Change to 3.

### Row 7414 — Brazil (easy) — FAIL
**Q:** Which Brazilian player scored his 77th international goal against Bolivia in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar's 77th goal came v Croatia (2022). Against Bolivia (Sept 2023) he scored his 78th & 79th.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Change to 78th/79th (surpassed).

### Row 7418 — Brazil (easy) — FAIL
**Q:** Which Brazilian player scored in both the 2014 7-1 loss and a 2014 World Cup quarter-final win?
**Answer:** David Luiz
**Why it fails:** False: David Luiz did NOT score in the 7-1 loss to Germany — Oscar scored Brazil's only goal. (David Luiz did score the QF free kick v Colombia.)
**Source:** https://en.wikipedia.org/wiki/Brazil_v_Germany_(2014_FIFA_World_Cup)
**Remedy:** Drop — David Luiz didn't score in the 7-1.

### Row 7426 — Brazil (easy) — FAIL
**Q:** Which Brazilian player scored in their 2022 World Cup round of 16 win?
**Answer:** Vinícius Jr.
**Why it fails:** Non-unique: Richarlison (an option) also scored in the 4-1 R16 win over South Korea (2022).
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Drop — multiple option-players scored.

### Row 7427 — Brazil (medium) — FAIL
**Q:** Which Brazilian player scored in two 2022 World Cup group stage matches?
**Answer:** Raphinha
**Why it fails:** False: Raphinha scored 0 at the 2022 World Cup — South Korea was the R16 (not group) and Brazil scored nothing v Cameroon.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Drop — Raphinha didn't score at 2022.

### Row 7457 — Brazil (easy) — FAIL
**Q:** Which Brazilian player was a 2022 squad member and key for the 2026 cycle?
**Answer:** Rodrygo
**Why it fails:** Non-unique: Vinícius Jr. (an option) was also a 2022 squad member and key for 2026.
**Source:** https://en.wikipedia.org/wiki/Brazil_national_football_team
**Remedy:** Drop — non-unique.

### Row 7468 — Brazil (easy) — FAIL
**Q:** Which Brazilian player was in the 2022 squad and is key for the 2026 cycle?
**Answer:** Rodrygo
**Why it fails:** Non-unique: Vinícius Jr. (an option) was also in the 2022 squad and is key for 2026.
**Source:** https://en.wikipedia.org/wiki/Brazil_national_football_team
**Remedy:** Drop — non-unique.

### Row 7470 — Brazil (easy) — FAIL
**Q:** Which Brazilian player was in the 2022 World Cup squad?
**Answer:** Rodrygo
**Why it fails:** Non-unique: Neymar and Casemiro (options) were also in the 2022 squad.
**Source:** https://en.wikipedia.org/wiki/Template:Brazil_squad_2022_FIFA_World_Cup
**Remedy:** Drop — multiple option-players were in the squad.

### Row 7477 — Brazil (easy) — FAIL
**Q:** Which Brazilian player was part of the 2022 FIFA World Cup squad?
**Answer:** Rodrygo
**Why it fails:** Non-unique: Gabriel Jesus and Richarlison (options) were also in the 2022 squad.
**Source:** https://en.wikipedia.org/wiki/Template:Brazil_squad_2022_FIFA_World_Cup
**Remedy:** Drop — multiple option-players were in the squad.

### Row 7479 — Brazil (easy) — FAIL
**Q:** Which Brazilian player was selected for the 2022 FIFA World Cup squad?
**Answer:** Rodrygo
**Why it fails:** Non-unique: Gabriel Jesus and Fred (options) were also in the 2022 squad.
**Source:** https://en.wikipedia.org/wiki/Template:Brazil_squad_2022_FIFA_World_Cup
**Remedy:** Drop — multiple option-players were in the squad.

### Row 7486 — Brazil (easy) — FAIL
**Q:** Which Brazilian player was the youngest to score in a World Cup qualifier?
**Answer:** Endrick
**Why it fails:** False: Endrick's age-17 goals were friendlies (England/Spain Mar 2024, Mexico Jun 2024), NOT a World Cup qualifier.
**Source:** https://en.wikipedia.org/wiki/Endrick_(footballer,_born_2006)
**Remedy:** Reword to 'friendly', or drop.

### Row 7500 — Brazil (easy) — FAIL
**Q:** Which Brazilian player won the Bronze Ball at the 2014 FIFA World Cup?
**Answer:** Neymar
**Why it fails:** False: Neymar did NOT win the 2014 Bronze Ball — Arjen Robben won it (Golden Messi, Silver Müller). Neymar was injured before the knockouts.
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup_awards
**Remedy:** Drop — false award claim.

### Row 7506 — Brazil (easy) — FAIL
**Q:** Which Brazilian player, in the 2022 World Cup squad, is a key figure for the 2026 cycle?
**Answer:** Rodrygo
**Why it fails:** Non-unique: Vinícius Jr. (an option) was also in the 2022 squad and a key 2026 figure.
**Source:** https://en.wikipedia.org/wiki/Brazil_national_football_team
**Remedy:** Drop — non-unique.

### Row 7507 — Brazil (easy) — FAIL
**Q:** Which Brazilian player, part of the 2022 squad, is a key player for the 2026 cycle?
**Answer:** Rodrygo
**Why it fails:** Non-unique: Vinícius Jr. (an option) was also a 2022 squad member and key for 2026.
**Source:** https://en.wikipedia.org/wiki/Brazil_national_football_team
**Remedy:** Drop — non-unique.

### Row 7508 — Brazil (medium) — FAIL
**Q:** Which Brazilian player, ranked highly in FIFA's Ballon d'Or voting in 2015, later won the Bronze Ball at the 2014 World Cup?
**Answer:** Neymar
**Why it fails:** False: Neymar did NOT win the 2014 Bronze Ball (Robben did). The Ballon d'Or 2015 part is true, but the award claim is wrong.
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup_awards
**Remedy:** Drop the Bronze Ball claim.

### Row 7513 — Brazil (easy) — FAIL
**Q:** Which Brazilian player's 2014 World Cup performance earned the Bronze Ball?
**Answer:** Neymar
**Why it fails:** False: Neymar did not win the 2014 Bronze Ball (Robben did).
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup_awards
**Remedy:** Drop — false award claim.

### Row 7518 — Brazil (easy) — FAIL
**Q:** Which Brazilian player's 2022 World Cup debut preceded his key role for the 2026 cycle?
**Answer:** Rodrygo
**Why it fails:** Non-unique: Vinícius Jr. (an option) was also a 2022 debutant-era squad member and key for 2026.
**Source:** https://en.wikipedia.org/wiki/Brazil_national_football_team
**Remedy:** Drop — non-unique.

### Row 7552 — Brazil (medium) — FAIL
**Q:** Which Brazilian scored in both the 2013 Confederations Cup and 2014 World Cup quarter-finals?
**Answer:** David Luiz
**Why it fails:** Unverified/false: David Luiz scored the 2014 QF free kick, but there is no record of him scoring in the 2013 Confederations Cup (he was a defender; the explanation only says he was 'part of the squad'). So 'scored in both' is not supported.
**Source:** https://en.wikipedia.org/wiki/David_Luiz
**Remedy:** Drop — the 2013 scoring claim is unsupported.

### Row 7566 — Brazil (medium) — FAIL
**Q:** Which Brazilian squad scored 15 goals in the 2022 World Cup?
**Answer:** Brazil in 2022
**Why it fails:** Wrong number: Brazil scored 8 goals at the 2022 World Cup, not 15.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Change to 8 goals.

### Row 7579 — Brazil (easy) — FAIL
**Q:** Which Brazilian stadium had a larger capacity than Arena Corinthians at the 2014 World Cup?
**Answer:** Maracanã Stadium
**Why it fails:** Non-unique: more than one option exceeds Arena Corinthians (~49,205) — Maracanã (~73k), Estádio Nacional (~70k) and Mineirão (~58k) are all larger.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_venues
**Remedy:** Drop — multiple larger venues among the options.

### Row 7614 — Brazil (easy) — FAIL
**Q:** Which Brazilian star equalled Pelé's 77-goal record in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar matched Pelé's 77 v Croatia (2022), not v Bolivia in Sept 2023 (where he surpassed it with 78th/79th).
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 7620 — Brazil (easy) — FAIL
**Q:** Which Brazilian star matched Pelé's goal tally in September 2023?
**Answer:** Neymar
**Why it fails:** False: Neymar matched Pelé v Croatia (2022); v Bolivia (Sept 2023) he surpassed it (78th/79th), not 'matched with his 77th'.
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 7638 — Brazil (easy) — FAIL
**Q:** Which Brazilian star won the 2014 World Cup Bronze Ball award?
**Answer:** Neymar
**Why it fails:** False: Neymar did NOT win the 2014 Bronze Ball — Arjen Robben won it (Neymar was injured before the knockouts).
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup_awards
**Remedy:** Drop — false award claim.

### Row 7645 — Brazil (easy) — FAIL
**Q:** Which Brazilian star's 2014 World Cup stats earned him the Bronze Ball?
**Answer:** Neymar
**Why it fails:** False: Neymar did not win the 2014 Bronze Ball (Robben did).
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup_awards
**Remedy:** Drop — false award claim.

### Row 7650 — Brazil (medium) — FAIL
**Q:** Which Brazilian team scored 15 goals in 5 matches at the 2022 World Cup?
**Answer:** Brazil 2022 squad
**Why it fails:** Wrong number: Brazil scored 8 goals (not 15) in 5 matches at the 2022 World Cup.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Change to 8 goals.

### Row 7652 — Brazil (easy) — FAIL
**Q:** Which Brazilian teen scored youngest in a World Cup qualifier?
**Answer:** Endrick
**Why it fails:** False: Endrick's age-17 goals were friendlies, not a World Cup qualifier.
**Source:** https://en.wikipedia.org/wiki/Endrick_(footballer,_born_2006)
**Remedy:** Reword to 'friendly', or drop.

### Row 7657 — Brazil (easy) — FAIL
**Q:** Which Brazilian teenager scored in a 2026 World Cup qualifier at age 17?
**Answer:** Endrick
**Why it fails:** False: Endrick's age-17 goals were friendlies, not a 2026 WC qualifier.
**Source:** https://en.wikipedia.org/wiki/Endrick_(footballer,_born_2006)
**Remedy:** Reword to 'friendly', or drop.

### Row 7666 — Brazil (easy) — FAIL
**Q:** Which Brazilian training centre in Teresópolis was used for 2014 World Cup preparation?
**Answer:** CBF Training Centre
**Why it fails:** Non-unique/TC-16: the distractor 'Granja Comary' is the SAME venue as the answer 'CBF Training Centre'.
**Source:** https://en.wikipedia.org/wiki/Brazil_national_football_team
**Remedy:** Replace 'Granja Comary' with a different distractor.

### Row 7669 — Brazil (easy) — FAIL
**Q:** Which Brazilian was 17 when scoring in a 2026 World Cup qualifier?
**Answer:** Endrick
**Why it fails:** False: Endrick's age-17 goals were friendlies, not a 2026 WC qualifier.
**Source:** https://en.wikipedia.org/wiki/Endrick_(footballer,_born_2006)
**Remedy:** Reword to 'friendly', or drop.

### Row 7676 — Brazil (easy) — FAIL
**Q:** Which Brazilian was captain and talisman for the 2018 and 2022 World Cups?
**Answer:** Neymar
**Why it fails:** False: Thiago Silva (not Neymar) was Brazil's CAPTAIN at the 2018 and 2022 World Cups. Neymar was the talisman, not the official captain.
**Source:** https://en.wikipedia.org/wiki/Thiago_Silva
**Remedy:** Change answer to Thiago Silva, or reword to 'talisman' only.

### Row 7687 — Brazil (easy) — FAIL
**Q:** Which Brazilian winger scored against both South Korea and Cameroon at the 2022 World Cup?
**Answer:** Raphinha
**Why it fails:** False: Raphinha scored 0 at the 2022 WC — South Korea was the R16 (not group) and Brazil scored nothing v Cameroon.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Drop — Raphinha didn't score at 2022.

### Row 7690 — Brazil (medium) — FAIL
**Q:** Which Brazilian winger scored goals in the 2022 World Cup group stage?
**Answer:** Raphinha
**Why it fails:** False: Raphinha did not score in the 2022 group stage (he scored 0 at the tournament).
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Drop.

### Row 7691 — Brazil (medium) — FAIL
**Q:** Which Brazilian winger scored in the 2022 World Cup group stage against Cameroon?
**Answer:** Raphinha
**Why it fails:** False: Brazil scored nothing v Cameroon (lost 0-1); Raphinha did not score.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Drop.

### Row 7692 — Brazil (medium) — FAIL
**Q:** Which Brazilian winger scored in the 2022 World Cup group stage against South Korea and Cameroon?
**Answer:** Raphinha
**Why it fails:** False: Raphinha scored 0 at 2022; South Korea was R16, not group.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Drop.

### Row 7693 — Brazil (medium) — FAIL
**Q:** Which Brazilian winger scored in two group stage matches at the 2022 FIFA World Cup?
**Answer:** Raphinha
**Why it fails:** False: Raphinha did not score in any 2022 group match (0 goals at the tournament).
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Drop.

### Row 7694 — Brazil (medium) — FAIL
**Q:** Which Brazilian winger was in the 2022 World Cup squad and scored two group stage goals?
**Answer:** Raphinha
**Why it fails:** False: Raphinha scored 0 group-stage goals at 2022.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Drop.

### Row 7704 — Brazil (medium) — FAIL
**Q:** Which Brazilian won the Bronze Ball in 2014, having won the Golden Ball in 2013?
**Answer:** Neymar
**Why it fails:** False: Neymar did not win the 2014 Bronze Ball (Robben did). He did win the 2013 Golden Ball, but not the 2014 award.
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup_awards
**Remedy:** Drop the Bronze Ball claim.

### Row 7742 — Brazil (easy) — FAIL
**Q:** Which CONMEBOL rival did Brazil beat 2-0 in Manaus during 2022 World Cup qualifying?
**Answer:** Uruguay
**Why it fails:** Wrong score: Brazil beat Uruguay 4-1 in Manaus (Oct 2021); the 2-0 was away in Montevideo.
**Source:** https://www.espn.com/soccer/report/_/gameId/561042
**Remedy:** Change the Manaus score to 4-1.

### Row 7746 — Brazil (easy) — FAIL
**Q:** Which CONMEBOL team did Brazil beat 2-0 in 2022 World Cup qualifying?
**Answer:** Uruguay
**Why it fails:** Wrong score: the Manaus qualifier v Uruguay was 4-1, not 2-0.
**Source:** https://www.espn.com/soccer/report/_/gameId/561042
**Remedy:** Change the Manaus score to 4-1.

### Row 7756 — Brazil (easy) — FAIL
**Q:** Which country's clubs had more Copa Libertadores titles than Brazil's in 2023?
**Answer:** No country
**Why it fails:** False: as of 2023 Argentina (25 titles) had MORE Copa Libertadores than Brazil (23) — so 'no country had more' is wrong (and the '24' figure is also wrong).
**Source:** https://en.wikipedia.org/wiki/Copa_Libertadores
**Remedy:** Drop — Argentina led Brazil in 2023.

### Row 7757 — Brazil (easy) — FAIL
**Q:** Which country's clubs had won 24 Copa Libertadores before Brazil's 2022 World Cup campaign?
**Answer:** Brazil
**Why it fails:** False: Brazilian clubs had ~21-22 Libertadores titles before the 2022 World Cup (23rd came with Fluminense in 2023), not 24.
**Source:** https://en.wikipedia.org/wiki/Copa_Libertadores
**Remedy:** Correct the count.

### Row 7789 — Brazil (easy) — FAIL
**Q:** Which league did NOT supply players to Brazil's 2022 World Cup squad?
**Answer:** Portugal
**Why it fails:** Non-unique negative: besides Portugal, GERMANY (an option) also did NOT supply a 2022-squad player — no Brazil 2022 player was Bundesliga-based. Two options fit 'did not supply'.
**Source:** https://en.wikipedia.org/wiki/Template:Brazil_squad_2022_FIFA_World_Cup
**Remedy:** Drop — Germany also supplied none.

### Row 7790 — Brazil (easy) — FAIL
**Q:** Which league was NOT represented by a player in Brazil's 2022 World Cup squad?
**Answer:** Netherlands Eredivisie
**Why it fails:** Non-unique negative: besides the Netherlands, the German Bundesliga (an option) also had no Brazil 2022-squad player.
**Source:** https://en.wikipedia.org/wiki/Template:Brazil_squad_2022_FIFA_World_Cup
**Remedy:** Drop — Bundesliga also unrepresented.

### Row 7872 — Brazil (easy) — FAIL
**Q:** Which nation did Brazil beat 2-0 in 2022 World Cup qualifiers to maintain dominance?
**Answer:** Uruguay
**Why it fails:** Wrong score: Brazil beat Uruguay 4-1 in Manaus (Oct 2021); the 2-0 was away in Montevideo.
**Source:** https://www.espn.com/soccer/report/_/gameId/561042
**Remedy:** Change the Manaus score to 4-1.

### Row 7886 — Brazil (medium) — FAIL
**Q:** Which nation did Brazil draw with in the 2018 World Cup group stage?
**Answer:** Mexico
**Why it fails:** False premise: Brazil did NOT draw with Mexico in the 2018 group stage (Mexico was not in their group). Their only group draw was 1-1 v Switzerland.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_E
**Remedy:** Change to Switzerland (1-1).

### Row 7887 — Brazil (easy) — FAIL
**Q:** Which nation did Brazil eliminate in a 2011 Copa América quarter-final?
**Answer:** Paraguay
**Why it fails:** Contradictory/false: Brazil did NOT eliminate Paraguay in 2011 — Paraguay eliminated Brazil on penalties (the explanation says so). The question's framing is reversed.
**Source:** https://en.wikipedia.org/wiki/2011_Copa_Am%C3%A9rica
**Remedy:** Reword: Paraguay eliminated Brazil.

### Row 7894 — Brazil (easy) — FAIL
**Q:** Which nation did Brazil's Neymar face when he equalled Pelé's goal record in September 2023?
**Answer:** Bolivia
**Why it fails:** False: Neymar EQUALED Pelé's 77 v Croatia (2022), not v Bolivia. Against Bolivia (Sept 2023) he scored his 78th & 79th to SURPASS it. (Bolivia is the right nation, but the 'equalled/77th' framing is wrong.)
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 7896 — Brazil (easy) — FAIL
**Q:** Which nation did NOT score 5 goals in under 30 minutes against Brazil at a World Cup?
**Answer:** Netherlands
**Why it fails:** Non-unique negative: only Germany scored 5 in <30 min v Brazil (2014). The Netherlands, Belgium AND Croatia (all options) did NOT — three correct answers.
**Source:** https://en.wikipedia.org/wiki/Brazil_v_Germany_(2014_FIFA_World_Cup)
**Remedy:** Drop — negative-framed and non-unique.

### Row 7938 — Brazil (easy) — FAIL
**Q:** Which nation was Brazil playing when Neymar equalled Pelé's goal record in September 2023?
**Answer:** Bolivia
**Why it fails:** False: Neymar EQUALED Pelé's 77 v Croatia (2022), not v Bolivia. Bolivia is the right Sept-2023 opponent, but there he SURPASSED it (78th/79th).
**Source:** https://www.foxsports.com/stories/soccer/world-cup-2022-neymar-ties-peles-all-time-record-for-goals-scored
**Remedy:** Reframe to 'surpassed'.

### Row 8005 — Brazil (easy) — FAIL
**Q:** Which team did Brazil beat 2-0 in Manaus during 2022 World Cup qualifying?
**Answer:** Uruguay
**Why it fails:** Wrong score: Brazil beat Uruguay 4-1 in Manaus (Oct 2021); the 2-0 was away in Montevideo.
**Source:** https://www.espn.com/soccer/report/_/gameId/561042
**Remedy:** Change the Manaus score to 4-1.

### Row 8023 — Brazil (easy) — FAIL
**Q:** Which team did Brazil NOT face in a 2022 World Cup knockout match?
**Answer:** Germany
**Why it fails:** Non-unique: Brazil faced only South Korea (R16) and Croatia (QF) in the 2022 KO, so they did NOT face Germany AND did not face Argentina (both options).
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Drop — two options (Germany, Argentina) were not faced.

### Row 8025 — Brazil (medium) — FAIL
**Q:** Which team drew 0-0 with Brazil in the 2018 World Cup group stage?
**Answer:** Mexico
**Why it fails:** False: Brazil did NOT draw 0-0 with Mexico in the 2018 group stage (Mexico was not in their group). Their group draw was 1-1 v Switzerland.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_E
**Remedy:** Change to Switzerland (1-1).

### Row 8100 — Brazil (medium) — FAIL
**Q:** Which World Cup cycles was Neymar Brazil's captain?
**Answer:** 2018 and 2022
**Why it fails:** False: Thiago Silva (not Neymar) was Brazil's CAPTAIN for the 2018 and 2022 cycles. Neymar was the talisman, not captain.
**Source:** https://en.wikipedia.org/wiki/Thiago_Silva
**Remedy:** Change to Thiago Silva, or reword to 'talisman'.

### Row 8102 — Brazil (medium) — FAIL
**Q:** Which World Cup did Brazil first draw 0-0 with Mexico in?
**Answer:** 2018 World Cup
**Why it fails:** False premise: Brazil never drew 0-0 with Mexico at a World Cup — Mexico was not in their 2018 group; they met only in the R16.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_Group_E
**Remedy:** Drop — non-existent group game.

### Row 8129 — Brazil (easy) — FAIL
**Q:** Who was Brazil's captain and talisman at the 2018 and 2022 World Cups?
**Answer:** Neymar
**Why it fails:** False: Thiago Silva (not Neymar) was Brazil's captain at 2018 and 2022. Neymar was the talisman.
**Source:** https://en.wikipedia.org/wiki/Thiago_Silva
**Remedy:** Change to Thiago Silva, or reword to 'talisman'.

### Row 8148 — Brazil (easy) — FAIL
**Q:** Why did Brazil maintain dominance over Uruguay in 2022 World Cup qualifying?
**Answer:** Beat Uruguay 2-0
**Why it fails:** Wrong score: Brazil beat Uruguay 4-1 in Manaus (Oct 2021); the 2-0 was away in Montevideo.
**Source:** https://www.espn.com/soccer/report/_/gameId/561042
**Remedy:** Change the Manaus score to 4-1.

### Row 8152 — Brazil (easy) — FAIL
**Q:** Why did Brazil score 15 goals at the 2022 World Cup?
**Answer:** Played 5 matches
**Why it fails:** False premise: Brazil scored 8 goals (not 15) in 5 matches at 2022.
**Source:** https://en.wikipedia.org/wiki/Brazil_at_the_2022_FIFA_World_Cup
**Remedy:** Correct the goal count to 8.

### Row 8165 — Brazil (easy) — FAIL
**Q:** Why did Brazil's Neymar win the 2014 World Cup Bronze Ball?
**Answer:** Scored four goals
**Why it fails:** False premise: Neymar did NOT win the 2014 Bronze Ball (Robben did); he was injured before the knockouts. He did score 4 goals.
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup_awards
**Remedy:** Drop the Bronze Ball claim.

### Row 8167 — Brazil (easy) — FAIL
**Q:** Why did Brazilian Neymar win the 2014 World Cup Bronze Ball?
**Answer:** Scored four tournament goals
**Why it fails:** False premise: Neymar did not win the 2014 Bronze Ball (Robben did).
**Source:** https://en.wikipedia.org/wiki/FIFA_World_Cup_awards
**Remedy:** Drop the Bronze Ball claim.

### Row 8169 — Brazil (medium) — FAIL
**Q:** Why do Brazilian clubs lead Copa Libertadores titles as of 2023?
**Answer:** They have 24 titles
**Why it fails:** False: Brazilian clubs had 23 Copa Libertadores titles in 2023, not 24 — and they did NOT lead, as Argentina had 25.
**Source:** https://en.wikipedia.org/wiki/Copa_Libertadores
**Remedy:** Correct the count and the 'lead' claim.

### Row 9584 — Cameroon (easy) — FAIL
**Q:** At the 2017 AFCON, Cameroon beat Egypt by what scoreline in the final?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer: '02-Jan' is a mangled '2-1'. Cameroon beat Egypt 2-1 in the 2017 AFCON final (per the explanation); the answer cell is unusable.
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations_Final
**Remedy:** Fix the answer to '2-1'.

### Row 9588 — Cameroon (easy) — FAIL
**Q:** At the 2022 FIFA World Cup, Cameroon drew what score with Serbia?
**Answer:** 03-Mar
**Why it fails:** Corrupted answer: '03-Mar' is a mangled '3-3'. Cameroon drew Serbia 3-3 (per the explanation); the answer cell is unusable.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Fix the answer to '3-3'.

### Row 9619 — Cameroon (medium) — FAIL
**Q:** Between 2010 and 2026, which World Cup did Cameroon fail to qualify for?
**Answer:** 2018 World Cup
**Why it fails:** False/non-unique: Cameroon did NOT qualify for 2026 (lost the CAF playoff to DR Congo, Nov 2025). So they failed BOTH 2018 and 2026 — 'which did they fail' is not uniquely 2018, and the explanation's 'qualified for 2026' is wrong.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Reword: Cameroon failed to qualify for both 2018 and 2026.

### Row 9628 — Cameroon (medium) — FAIL
**Q:** Cameroon won the 2017 AFCON final. What was the score?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer: '02-Jan' is a mangled '2-1'. Cameroon won the 2017 AFCON final 2-1 (per the explanation).
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations_Final
**Remedy:** Fix the answer to '2-1'.

### Row 9629 — Cameroon (easy) — FAIL
**Q:** Cameroon's Stade Ahmadou Ahidjo hosted AFCON 2021 matches. Which stadium also hosted matches?
**Answer:** Stade Olembe
**Why it fails:** Non-unique: besides Stade Olembe, Stade de Japoma (Douala, an option) also hosted AFCON 2021 matches.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations
**Remedy:** Drop — multiple option-stadiums hosted.

### Row 9652 — Cameroon (easy) — FAIL
**Q:** How did Cameroon qualify for the 2026 FIFA World Cup?
**Answer:** Through CAF qualification
**Why it fails:** False: Cameroon did NOT qualify for the 2026 World Cup — they lost the CAF playoff to DR Congo (Mbemba's late goal, Nov 2025).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Drop — Cameroon failed to qualify for 2026.

### Row 9689 — Cameroon (medium) — FAIL
**Q:** In Cameroon's 2022 World Cup group stage match against Serbia, what was the final score?
**Answer:** 03-Mar
**Why it fails:** Corrupted answer: '03-Mar' is a mangled '3-3'. Cameroon drew Serbia 3-3 (per the explanation).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Fix the answer to '3-3'.

### Row 9711 — Cameroon (medium) — FAIL
**Q:** In which FIFA World Cup did Cameroon fail to qualify during their 2008-2026 cycle?
**Answer:** 2018 World Cup
**Why it fails:** Non-unique: in the 2008-2026 span Cameroon failed to qualify for BOTH 2018 AND 2026 (lost the CAF playoff to DR Congo). 2026 is an option here, so the answer isn't uniquely 2018.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Drop — Cameroon also failed 2026.

### Row 9748 — Cameroon (hard) — FAIL
**Q:** In which year was Cameroon eliminated from the World Cup group stage after three losses?
**Answer:** 2014
**Why it fails:** Non-unique: Cameroon lost all three group games at BOTH 2010 and 2014 (both are options), so the year isn't unique.
**Source:** https://en.wikipedia.org/wiki/Cameroon_at_the_FIFA_World_Cup
**Remedy:** Drop — both 2010 and 2014 fit.

### Row 9755 — Cameroon (easy) — FAIL
**Q:** What score did Cameroon beat Egypt by in the 2017 AFCON final?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer: '02-Jan' is a mangled '2-1' (2017 AFCON final v Egypt).
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations_Final
**Remedy:** Fix the answer to '2-1'.

### Row 9756 — Cameroon (easy) — FAIL
**Q:** What was Cameroon's final score against Serbia at Qatar 2022?
**Answer:** 03-Mar
**Why it fails:** Corrupted answer: '03-Mar' is a mangled '3-3' (Serbia draw).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Fix the answer to '3-3'.

### Row 9757 — Cameroon (easy) — FAIL
**Q:** What was Cameroon's final score in their 2022 World Cup draw with Serbia?
**Answer:** 03-Mar
**Why it fails:** Corrupted answer: '03-Mar' = '3-3' (Serbia draw).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Fix the answer to '3-3'.

### Row 9758 — Cameroon (easy) — FAIL
**Q:** What was Cameroon's final scoreline against Serbia at the 2022 World Cup?
**Answer:** 03-Mar
**Why it fails:** Corrupted answer: '03-Mar' = '3-3' (Serbia draw).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Fix the answer to '3-3'.

### Row 9761 — Cameroon (easy) — FAIL
**Q:** What was Cameroon's scoreline in the 2017 AFCON final?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer: '02-Jan' = '2-1' (2017 AFCON final).
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations_Final
**Remedy:** Fix the answer to '2-1'.

### Row 9762 — Cameroon (easy) — FAIL
**Q:** What was Cameroon's winning score against Egypt in the 2017 AFCON final?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer: '02-Jan' = '2-1' (2017 AFCON final v Egypt).
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations_Final
**Remedy:** Fix the answer to '2-1'.

### Row 9765 — Cameroon (easy) — FAIL
**Q:** What was the final score in Cameroon's 2022 World Cup thriller with Serbia?
**Answer:** 03-Mar
**Why it fails:** Corrupted answer: '03-Mar' = '3-3' (Serbia draw).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Fix the answer to '3-3'.

### Row 9767 — Cameroon (easy) — FAIL
**Q:** What was the final score when Cameroon beat Egypt in the 2017 AFCON final?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer: '02-Jan' = '2-1' (2017 AFCON final).
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations_Final
**Remedy:** Fix the answer to '2-1'.

### Row 9769 — Cameroon (easy) — FAIL
**Q:** What was the final score when Cameroon drew with Serbia at the 2022 World Cup?
**Answer:** 03-Mar
**Why it fails:** Corrupted answer: '03-Mar' = '3-3' (Serbia draw).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Fix the answer to '3-3'.

### Row 9770 — Cameroon (easy) — FAIL
**Q:** What was the final score when Cameroon drew with Serbia in 2022?
**Answer:** 03-Mar
**Why it fails:** Corrupted answer: '03-Mar' = '3-3' (Serbia draw).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Fix the answer to '3-3'.

### Row 9771 — Cameroon (easy) — FAIL
**Q:** What was the final score when Cameroon faced Serbia at the 2022 FIFA World Cup?
**Answer:** 03-Mar
**Why it fails:** Corrupted answer: '03-Mar' = '3-3' (Serbia draw).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Fix the answer to '3-3'.

### Row 9776 — Cameroon (medium) — FAIL
**Q:** What was the scoreline of Cameroon's win over Egypt in the 2017 AFCON final?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer: '02-Jan' = '2-1' (2017 AFCON final).
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations_Final
**Remedy:** Fix the answer to '2-1'.

### Row 9801 — Cameroon (medium) — FAIL
**Q:** When did Cameroon lose all three group matches at a World Cup?
**Answer:** 2014
**Why it fails:** Non-unique: Cameroon lost all three group games at BOTH 2010 and 2014 (both options).
**Source:** https://en.wikipedia.org/wiki/Cameroon_at_the_FIFA_World_Cup
**Remedy:** Drop — both 2010 and 2014 fit.

### Row 9803 — Cameroon (medium) — FAIL
**Q:** When did Cameroon qualify for the 2026 FIFA World Cup?
**Answer:** 2026
**Why it fails:** False: Cameroon did NOT qualify for the 2026 World Cup (lost the CAF playoff to DR Congo, Nov 2025).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Drop — Cameroon failed to qualify for 2026.

### Row 9835 — Cameroon (easy) — FAIL
**Q:** Which 2010s AFCON champion was a notable underdog like Cameroon in 2017?
**Answer:** Cameroon
**Why it fails:** Self-referential: the question asks which underdog AFCON champion was 'like Cameroon in 2017' and the answer is Cameroon itself.
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations
**Remedy:** Drop — the answer restates the subject.

### Row 9840 — Cameroon (easy) — FAIL
**Q:** Which 2017 AFCON final score involved Cameroon beating Egypt?
**Answer:** 02-Jan
**Why it fails:** Corrupted answer: '02-Jan' = '2-1' (2017 AFCON final v Egypt).
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations_Final
**Remedy:** Fix the answer to '2-1'.

### Row 9850 — Cameroon (medium) — FAIL
**Q:** Which 2022 World Cup group stage draw did NOT involve Cameroon?
**Answer:** Brazil vs Switzerland
**Why it fails:** Broken: Brazil vs Switzerland was NOT a draw (Brazil won 1-0, as the explanation itself says). The actual non-Cameroon draw among the options was Germany 1-1 Spain.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Change the answer to Germany vs Spain (1-1).

### Row 9871 — Cameroon (easy) — FAIL
**Q:** Which African nation did Cameroon NOT beat in the 2017 AFCON final?
**Answer:** Ivory Coast
**Why it fails:** Non-unique negative: Cameroon beat Egypt in the 2017 final, so among the options they did NOT beat Ivory Coast, Senegal OR Ghana in the final — three correct answers.
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations_Final
**Remedy:** Drop — negative-framed and non-unique.

### Row 9885 — Cameroon (easy) — FAIL
**Q:** Which African nation had the most World Cup appearances before Cameroon's eighth in 2022?
**Answer:** Cameroon
**Why it fails:** Self-referential: 'which nation had the most appearances before Cameroon's 8th?' answers Cameroon itself (it held the record with 7).
**Source:** https://en.wikipedia.org/wiki/Cameroon_at_the_FIFA_World_Cup
**Remedy:** Drop — circular.

### Row 9888 — Cameroon (medium) — FAIL
**Q:** Which African nation has more World Cup qualifications than Ghana: Cameroon or Nigeria?
**Answer:** Cameroon
**Why it fails:** Non-unique: both Cameroon (8) AND Nigeria (6) have more World Cup qualifications than Ghana (4), so the 'Cameroon or Nigeria' answer isn't unique.
**Source:** https://en.wikipedia.org/wiki/Nigeria_at_the_FIFA_World_Cup
**Remedy:** Reword to 'which has the most' (Cameroon).

### Row 9917 — Cameroon (easy) — FAIL
**Q:** Which African nation, like Cameroon in 2010, qualified for the 2014 World Cup?
**Answer:** Cameroon
**Why it fails:** Self-referential + non-unique: 'which nation like Cameroon in 2010 qualified for 2014?' answers Cameroon itself, and Nigeria/Ghana/Ivory Coast (options) also qualified for 2014.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup
**Remedy:** Drop — circular and non-unique.

### Row 9918 — Cameroon (easy) — FAIL
**Q:** Which African nation, like Cameroon in 2017, won an AFCON as underdogs?
**Answer:** Cameroon
**Why it fails:** Self-referential: 'which nation, like Cameroon in 2017, won an AFCON as underdogs?' answers Cameroon itself.
**Source:** https://en.wikipedia.org/wiki/2017_Africa_Cup_of_Nations
**Remedy:** Drop — the answer restates the subject.

### Row 9984 — Cameroon (easy) — FAIL
**Q:** Which CAF team, unlike Cameroon, qualified for the 2018 World Cup?
**Answer:** Senegal
**Why it fails:** Non-unique: besides Senegal, both Nigeria AND Morocco (options) also qualified for 2018, unlike Cameroon. Only Ghana didn't.
**Source:** https://en.wikipedia.org/wiki/2018_FIFA_World_Cup
**Remedy:** Drop — multiple option-nations qualified for 2018.

### Row 9987 — Cameroon (easy) — FAIL
**Q:** Which Cameroon 2022 World Cup match did NOT end 3-3?
**Answer:** Cameroon vs Brazil
**Why it fails:** Non-unique negative: both Cameroon-Brazil (1-0) AND Cameroon-Switzerland (1-0) did NOT end 3-3, so the answer isn't unique (only the Serbia game was 3-3).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Drop — two options fit.

### Row 10031 — Cameroon (easy) — FAIL
**Q:** Which Cameroon attacker was a key part of their 2022 World Cup squad?
**Answer:** Karl Toko Ekambi
**Why it fails:** Non-unique: Aboubakar AND Choupo-Moting (options) were also key Cameroon attackers at 2022, not just Toko Ekambi.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Drop — multiple option-players were key 2022 attackers.

### Row 10033 — Cameroon (easy) — FAIL
**Q:** Which Cameroon attacker was a key player at the 2022 FIFA World Cup in Qatar?
**Answer:** Karl Toko Ekambi
**Why it fails:** Non-unique: Aboubakar and Choupo-Moting (options) were also key Cameroon attackers at 2022.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Drop — multiple option-players were key 2022 attackers.

### Row 10078 — Cameroon (easy) — FAIL
**Q:** Which Cameroon forward had over 70 caps and was a key player at the 2022 World Cup?
**Answer:** Eric Maxim Choupo-Moting
**Why it fails:** Non-unique: Aboubakar (an option) also has well over 70 caps and was a key 2022 forward, like Choupo-Moting.
**Source:** https://en.wikipedia.org/wiki/Vincent_Aboubakar
**Remedy:** Drop — Aboubakar equally fits.

### Row 10080 — Cameroon (easy) — FAIL
**Q:** Which Cameroon forward had over 70 caps at the 2022 FIFA World Cup?
**Answer:** Eric Maxim Choupo-Moting
**Why it fails:** Non-unique: Aboubakar (an option) also has 70+ caps and was a key 2022 forward.
**Source:** https://en.wikipedia.org/wiki/Vincent_Aboubakar
**Remedy:** Drop — Aboubakar equally fits.

### Row 10083 — Cameroon (easy) — FAIL
**Q:** Which Cameroon forward had over 70 caps for the 2022 World Cup?
**Answer:** Eric Maxim Choupo-Moting
**Why it fails:** Non-unique: Aboubakar (an option) also has 70+ caps and was a key 2022 forward.
**Source:** https://en.wikipedia.org/wiki/Vincent_Aboubakar
**Remedy:** Drop — Aboubakar equally fits.

### Row 10084 — Cameroon (medium) — FAIL
**Q:** Which Cameroon forward played a key role in the 2022 World Cup group stage?
**Answer:** Eric Maxim Choupo-Moting
**Why it fails:** Non-unique: Aboubakar (an option) played the key 2022 forward role (scored v Serbia & Brazil), as did Choupo-Moting.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Drop — multiple option-forwards were key.

### Row 10098 — Cameroon (easy) — FAIL
**Q:** Which Cameroon forward was a key player at the 2022 World Cup in Qatar?
**Answer:** Eric Maxim Choupo-Moting
**Why it fails:** Non-unique: Aboubakar and Toko Ekambi (options) were also key Cameroon forwards at 2022.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Drop — multiple option-forwards were key.

### Row 10099 — Cameroon (easy) — FAIL
**Q:** Which Cameroon forward was key at the 2022 FIFA World Cup?
**Answer:** Eric Maxim Choupo-Moting
**Why it fails:** Non-unique: Aboubakar and Toko Ekambi (options) were also key 2022 forwards.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Drop — multiple option-forwards were key.

### Row 10101 — Cameroon (easy) — FAIL
**Q:** Which Cameroon forward with over 70 caps was a key attacker at the 2022 FIFA World Cup?
**Answer:** Eric Maxim Choupo-Moting
**Why it fails:** Non-unique: Aboubakar (an option) also has 70+ caps and was a key 2022 attacker.
**Source:** https://en.wikipedia.org/wiki/Vincent_Aboubakar
**Remedy:** Drop — Aboubakar equally fits.

### Row 10102 — Cameroon (easy) — FAIL
**Q:** Which Cameroon forward with over 70 caps was key at the 2022 World Cup?
**Answer:** Eric Maxim Choupo-Moting
**Why it fails:** Non-unique: Aboubakar (an option) also has 70+ caps and was a key 2022 forward.
**Source:** https://en.wikipedia.org/wiki/Vincent_Aboubakar
**Remedy:** Drop — Aboubakar equally fits.

### Row 10123 — Cameroon (easy) — FAIL
**Q:** Which Cameroon key attacker at the 2022 World Cup had over 40 caps?
**Answer:** Karl Toko Ekambi
**Why it fails:** Non-unique: Aboubakar and Choupo-Moting (options) also have 40+ caps and were key 2022 attackers.
**Source:** https://en.wikipedia.org/wiki/Vincent_Aboubakar
**Remedy:** Drop — multiple option-players fit.

### Row 10150 — Cameroon (easy) — FAIL
**Q:** Which Cameroon manager faced Croatia at the 2022 FIFA World Cup?
**Answer:** Rigobert Song
**Why it fails:** False: Cameroon did NOT face Croatia at 2022 — they were in Group G (Switzerland, Serbia, Brazil). Croatia was in Group F.
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Reword — Cameroon's 2022 opponents were Switzerland/Serbia/Brazil.

### Row 10327 — Cameroon (easy) — FAIL
**Q:** Which Cameroon player was NOT in their 2014 World Cup squad?
**Answer:** Vincent Aboubakar
**Why it fails:** False: Vincent Aboubakar WAS in Cameroon's 2014 World Cup squad - he scored their only goal (v Brazil). The other options were also in the squad.
**Source:** https://en.wikipedia.org/wiki/Vincent_Aboubakar
**Remedy:** Drop - Aboubakar was in the 2014 squad.

### Row 10370 — Cameroon (hard) — FAIL
**Q:** Which Cameroon qualification cycle matched their 2026 CAF success: 2010, 2014, or 2018?
**Answer:** 2014
**Why it fails:** False premise: Cameroon did NOT qualify for 2026 (lost the CAF playoff to DR Congo), so there was no '2026 CAF success' to match.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Drop - Cameroon failed to qualify for 2026.

### Row 10496 — Cameroon (hard) — FAIL
**Q:** Which FIFA World Cup did Cameroon qualify for through CAF qualification?
**Answer:** The 2026 World Cup
**Why it fails:** False: Cameroon did NOT qualify for 2026 (lost the CAF playoff to DR Congo). They qualified via CAF for 2010, 2014 AND 2022 - so 2026 is wrong (and the other options are all correct).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Change to 2010/2014/2022; Cameroon failed 2026.

### Row 10547 — Cameroon (easy) — FAIL
**Q:** Which nation did Cameroon NOT draw with at a FIFA World Cup?
**Answer:** Switzerland
**Why it fails:** Non-unique negative: among the options Cameroon did NOT draw with Switzerland, Brazil OR Argentina at a WC (they only drew 3-3 with Serbia).
**Source:** https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_G
**Remedy:** Drop - three options fit.

### Row 10589 — Cameroon (easy) — FAIL
**Q:** Which nation, like Cameroon in 2022, qualified for the 2014 World Cup through CAF?
**Answer:** Cameroon
**Why it fails:** Self-referential + non-unique: 'which nation like Cameroon qualified for 2014 via CAF?' answers Cameroon itself, and Nigeria/Ghana/Ivory Coast also qualified for 2014.
**Source:** https://en.wikipedia.org/wiki/2014_FIFA_World_Cup
**Remedy:** Drop - circular and non-unique.

### Row 10651 — Cameroon (medium) — FAIL
**Q:** Which two World Cups did Cameroon qualify for consecutively after 2022?
**Answer:** 2022 and 2026
**Why it fails:** False: Cameroon did NOT qualify for 2026 (lost the CAF playoff to DR Congo) - so '2022 and 2026' is wrong.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Drop - Cameroon failed to qualify for 2026.

### Row 10652 — Cameroon (medium) — FAIL
**Q:** Which two World Cups did Cameroon qualify for through CAF?
**Answer:** 2022 and 2026
**Why it fails:** False: Cameroon did NOT qualify for 2026. They qualified via CAF for 2010/2014/2022, not 2026.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Drop - Cameroon failed to qualify for 2026.

### Row 10659 — Cameroon (medium) — FAIL
**Q:** Which World Cup did Cameroon not qualify for after 2010?
**Answer:** 2018 World Cup
**Why it fails:** Non-unique: Cameroon failed to qualify for BOTH 2018 and 2026 (an option), so the answer isn't uniquely 2018.
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Drop - also failed 2026.

### Row 10672 — Cameroon (medium) — FAIL
**Q:** Which World Cup was the only one Cameroon failed to qualify for between 2010 and 2026?
**Answer:** 2018 World Cup
**Why it fails:** False: 2018 was NOT the only WC Cameroon failed between 2010-2026 - they also failed 2026 (lost the CAF playoff).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Reword - Cameroon failed both 2018 and 2026.

### Row 10677 — Cameroon (medium) — FAIL
**Q:** Which year did Cameroon host the AFCON, one year after Egypt?
**Answer:** 2022
**Why it fails:** False: the 2021 AFCON (hosted by Cameroon) was the next edition after Egypt's 2019 - two years/one edition later, not 'one year after'; and it is officially the 2021 edition.
**Source:** https://en.wikipedia.org/wiki/2021_Africa_Cup_of_Nations
**Remedy:** Drop - the 'one year after Egypt' premise is wrong.

### Row 10690 — Cameroon (hard) — FAIL
**Q:** Which year did Cameroon's CAF qualification secure a World Cup spot?
**Answer:** 2010
**Why it fails:** Non-unique: Cameroon's CAF qualification secured WC spots in 2010, 2014 AND 2022 (all options), so the year isn't unique.
**Source:** https://en.wikipedia.org/wiki/Cameroon_at_the_FIFA_World_Cup
**Remedy:** Drop - multiple option-years fit.

### Row 10723 — Cameroon (easy) — FAIL
**Q:** Why did Cameroon qualify for the 2026 FIFA World Cup?
**Answer:** Through CAF qualification
**Why it fails:** False: Cameroon did NOT qualify for 2026 (lost the CAF playoff to DR Congo).
**Source:** https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_(CAF)
**Remedy:** Drop - Cameroon failed to qualify for 2026.
