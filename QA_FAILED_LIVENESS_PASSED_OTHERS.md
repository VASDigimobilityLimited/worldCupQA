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

Total failed-liveness-passed-others so far: **119** (last verified row 810)

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
