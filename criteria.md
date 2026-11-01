# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

<!-- Your criterion. It must name a number. -->
Of 5 pieces I wrote myself (including 1 written in deliberately plain, simple English), none gets the "ai" label, in all 3 trials.


**Why this target:**
I do not want a humans writing to be marked as AI, and I
want to have the model do that as little as possible. A 
wrong accusations hurts a real person, while a missed AI text would cost the site a little.


---

## 2.

<!-- Your criterion. -->
The average combined_score of 5 clearly-AI texts is at least 0.5 higher than the average of 5 clearly-human texts, in all 3 trials.


**Why this target:**
Human is ≤ 0.35 and AI is ≥ 0.65, so the bands are 0.3 apart. A spread of 0.5 is big enough so each score should fall into their own baskets in each label.


---

## 3.

<!-- Your criterion. -->
Of my test texts, at least one gets ai, one human, and one unsure, in all 3 trials.


**Why this target:**
Human is ≤ 0.35 and AI is ≥ 0.65 and unsure is inbetween, so the three labels should be reachable in different trials from each other.


---

## 4.

<!-- Your criterion. -->
All 5 appeals with a real content_id are written to the log and change status to under_review. An appeal with a made-up content_id returns 404 and writes nothing.


**Why this target:**
The appeal is the only thing between a wrong accusation and nothing at all, so it can't fail even once.


---

## 5.

<!-- Your criterion. -->
If text is missing, empty, or enormous, it must go through
0 out of 5 test trials. missing text, empty "", only spaces, and over 20,000 characters are cases where this should happen, and should return an error message with code 400, and never get a score or label.


**Why this target:**
Empty text would get a meaningless score, enormous text slows the detector for everyone, and a crash on bad input is one of the most common real failures.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
