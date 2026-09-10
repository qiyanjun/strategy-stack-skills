---
name: sl
description: >-
  Iterative, self-evaluated research-and-writing loop. Trigger whenever the user
  types "/sl", or asks for deep research, a thorough or comprehensive
  investigation, a rigorous analysis, a literature scan, or wants Claude to keep
  refining a hard answer until it is confident. Use it for any substantive,
  multi-part, or high-stakes question where a single pass would likely miss
  something: it makes Claude draft a take, search, self-score against a rubric,
  name its own gaps, and iterate until the answer clears a high quality bar or
  hits diminishing returns. Skip it only for trivial single-fact lookups.
---

# Self-Loop (`/sl`)

A single-pass answer to a hard question almost always leaves something out — an
unexamined sub-question, a claim asserted from memory instead of checked, a
counterargument never considered. This skill fixes that by running a disciplined
loop: **draft → score → name the gaps → close the gaps → redraft**, repeating
until the answer is genuinely strong, not just until it *feels* done.

The score is a thermometer, not the goal. The goal is a correct, well-evidenced,
honestly-calibrated answer. Never inflate a number to escape the loop — a
truthful "88, with these two open questions" is worth far more than a fake 96.

## First: calibrate effort

Before looping, gauge how much rigor the question actually warrants.

- **Trivial / single fact** ("what's the capital of X", "convert 5km to miles")
  → answer directly; don't run the loop.
- **Substantive** (multi-part questions, comparisons, "what's the state of the
  art in…", recommendations, anything where being wrong has real cost) → run the
  full loop below.

If unsure, run the loop. Under-doing a hard question is the more common failure.

## The loop

Run these steps in order. **Actually write each take** — do not collapse a round
into pure thinking. Writing the take is what exposes the gaps.

1. **Frame.** Restate the real question and break it into the concrete
   sub-questions a complete answer must resolve. List what you'd need to know.

2. **Draft a take.** Write your current best answer in full, using what you
   already know plus any searches. This is iteration 1.

3. **Search to ground it.** Use web search (or whatever retrieval tools are
   available). Favor primary and authoritative sources. Cross-check any
   surprising, load-bearing, or recency-sensitive claim against a second source.
   Note what you verified vs. what is still assumption.

4. **Score against the rubric** (below). Produce a number 0–100 *derived from the
   dimensions*, not pulled from the air.

5. **Name the specific gaps.** This is the most important step. Write down the
   exact weaknesses keeping the score below 95 — e.g. "sub-question 3 unanswered,"
   "the 2023 figure is unverified," "no counterargument to the main claim,"
   "source is a blog, need a primary one." Vague gaps ("could be better") are not
   allowed; each gap must be actionable.

6. **Close the gaps.** Think and search again, *targeting the named gaps
   specifically*. Don't re-research what's already solid.

7. **Rewrite the cumulative take.** Produce a fresh, complete version that folds
   in the new findings — not a diff or a patch. Re-score. Return to step 5.

Continue until a stop condition fires.

## Scoring rubric

Score each dimension, then let the weakest dimensions cap the overall number. An
overall ≥95 requires every dimension to be strong **and** no unresolved named gap
a careful reader would catch.

| Dimension | The question it answers |
|---|---|
| **Coverage** | Is every sub-question — and the obvious follow-ups — addressed? |
| **Evidence** | Are load-bearing claims backed by retrieval, from strong sources, with surprising ones cross-checked? |
| **Accuracy** | Are facts verified rather than recalled? Are source conflicts surfaced, not hidden? |
| **Reasoning** | Do the conclusions actually follow? Were alternatives and counterarguments considered? |
| **Calibration** | Does stated confidence match the evidence? Is genuine uncertainty flagged? |
| **Clarity** | Does it answer directly, organized, with no padding? |

A high overall score with a weak dimension is a scoring error — fix the dimension
or lower the number.

## Stop conditions

Stop as soon as **any** of these is true:

- **Threshold met** — rubric-backed score ≥ 95.
- **Max iterations** — you have completed 5 full rounds. Deliver the best take and
  state what still limits it.
- **Convergence** — a full round closed no material gap (diminishing returns).
  Don't spin; deliver and note the remaining limits.
- **Honest ceiling** — the question can't legitimately reach 95 (evidence
  genuinely conflicts, the data doesn't exist, it's irreducibly uncertain). Stop
  below threshold and say so plainly. Do **not** keep looping to manufacture
  confidence, and do **not** inflate the score to exit.

## What the user sees

Keep the per-round drafts and scores in your working/thinking. The user-facing
message is the **final cumulative take, cleaned up** — lead with the direct
answer, then supporting detail. Close with one short line: the confidence level
and any open questions or caveats. Don't dump the iteration log on the user unless
they ask to see the working.

## Anti-gaming reminders

- The number must be earned from the rubric. If you can't name *why* it's a 95,
  it isn't one.
- Closing a gap means actually resolving it, not deleting the sentence that
  exposed it.
- Reaching the ceiling honestly is a success, not a failure of the loop.

## Worked mini-example (one round)

> **Question:** "Is creatine safe for healthy adults to take daily?"
>
> **Draft take (iter 1):** Creatine monohydrate is widely regarded as safe for
> healthy adults at ~3–5g/day; the main caveat is kidney concerns. *Score: 70.*
>
> **Named gaps:** (a) "widely regarded" is unsourced; (b) the kidney claim is
> asserted, not checked; (c) no mention of long-term-study duration; (d) doesn't
> address who *shouldn't* take it.
>
> **Close gaps → search:** pull a review/meta-analysis for the safety consensus;
> check the kidney question against studies in people with normal renal function;
> find the longest follow-up duration; note contraindications.
>
> **Rewrite (iter 2):** [fuller answer citing the review, distinguishing healthy
> adults from those with pre-existing renal disease, noting the longest trials,
> stating the dose] *Score: 93 — still missing drug-interaction data → one more
> targeted round.*

That is the texture of one loop: a written take, an honest score, named gaps, a
targeted search, a rewrite — repeat until a stop condition fires.
