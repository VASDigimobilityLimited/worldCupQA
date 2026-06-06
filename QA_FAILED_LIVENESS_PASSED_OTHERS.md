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

Total failed-liveness-passed-others so far: **286** (Algeria 176 + Argentina 110; ARGENTINA COMPLETE through row 2160)

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
