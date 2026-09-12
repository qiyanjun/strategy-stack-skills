---
name: personal-career-deep-dive
description: Run a complete end-to-end strategic analysis of a person's career, orchestrating multiple frameworks in dependency order — target market understanding, labor market forces, Business Model You canvas, peer landscape mapping, personal 7 Powers defensibility, compensation reality, and an integrated verdict with a staged action plan. Use whenever someone wants thorough multi-framework career analysis rather than a single-framework answer. Trigger on "full career analysis", "deep dive on my career", "analyze my career end to end", "complete strategic picture of my career", "should I stay or leave", "am I positioned well for [role or market]", "analyze my career from scratch", "run the career pipeline on me", or a request combining a profile, CV, or homepage with comprehensive strategic intent. For a single framework only, use the narrower skill directly (business-model-you for the model, personal-power-analysis for defensibility). For a company rather than a person, use company-deep-dive.
---

# Personal Career Deep Dive — End-to-End Orchestrator

Runs a full career analysis by sequencing frameworks so each feeds the next. It does not re-implement them — **it loads and follows them.**

This is the personal counterpart to `company-deep-dive`, with the same dependency architecture: understand the market, then the structural forces, then the individual's model, then the competition, then defensibility, then the money, then a verdict.

## Critical mechanic: you must actually read the component skills

Skills are not callable functions. Naming a skill does nothing. At each phase you MUST `view` the referenced SKILL.md and follow it. Skipping the read means improvising a framework from memory — which yields output that looks structured but is generic. If a path fails to resolve, say so explicitly rather than silently substituting your own version.

**Running under Codex or another host with no `${CLAUDE_PLUGIN_ROOT}`:** that variable is a Claude Code plugin convention and won't be set. Resolve any `${CLAUDE_PLUGIN_ROOT}/skills/<name>/SKILL.md` reference below as `<name>/SKILL.md` in the directory next to this skill's own directory instead.

**When a phase's analysis already exists earlier in the session**, you may carry it forward instead of re-deriving it — but state explicitly what was carried and from where, and re-verify anything later phases depend on. Do not silently compress a phase to a summary; a reader cannot tell the difference between a phase that was run and one that was skipped, and neither can you on review.

---

## Why this order

| # | Phase | Requires | Because |
|---|---|---|---|
| 0 | Scope & evidence | Nothing | The decision being made determines every emphasis downstream |
| 1 | Target market understanding | The arena | Market forces are generic without it |
| 2 | Labor market forces | Phase 1 outputs | Person-agnostic — what anyone in this market faces |
| 3 | Business Model You | Profile + market context | Maps how *this person* creates and captures value |
| 4 | Peer landscape | Phase 1 + Phase 3 | Supplies the named foils; without them, 7 Powers rates against an abstraction |
| 5 | Personal 7 Powers | Phases 3 + 4 | Tests defensibility of the mapped model against real competing profiles |
| 6 | Compensation reality | Phases 3 + 5 | Tests whether powers actually show up in what's captured |
| 7 | Integrated verdict + plan | All | The deliverable |

**Note on ordering:** Business Model You precedes 7 Powers because the latter tests the defensibility of a model that must first be mapped. The peer landscape precedes 7 Powers because `personal-power-analysis` explicitly requires named foils, not abstractions.

---

## Phase 0 — Scope and evidence

**Establish the decision first.** The same person yields a different analysis depending on the question:

| Decision | Emphasis shifts toward |
|---|---|
| **Stay or leave** | Opportunity cost, portability, what's non-transferable |
| **Target a specific role/market** | Value proposition legibility, foil comparison, gap to requirements |
| **Pivot fields** | Which resources transfer, which must be rebuilt, re-earned segments |
| **Increase leverage in place** | Scale economies, switching costs, activity allocation |
| **Negotiate or re-price** | Powers vs. captured value, comp benchmarks |
| **General "where am I"** | Run balanced; say explicitly that no decision was specified |

Ask at most 2–3 questions and only for load-bearing unknowns — people find being interviewed about themselves tedious, and much is inferable from a CV, homepage, or prior conversation.

**Gather evidence once; reuse it in every phase.** Sources: CV or résumé, personal site, LinkedIn, Google Scholar, GitHub, publication or project record, prior conversation. Where relevant, web-search the person's public artifacts to see what's independently visible — that visibility is itself Phase 5 evidence. For complex research, `view ${CLAUDE_PLUGIN_ROOT}/skills/sl/SKILL.md`.

Record the **evidence date** and note what was unavailable.

**Verification rule for load-bearing claims.** Any claim that becomes the analysis's binding constraint, anchor power, or critical vulnerability must be independently checked before it is allowed to carry that weight — not asserted from plausibility. Framework reasoning generates confident-sounding claims very easily, and the most consequential one is the most dangerous to leave unverified. If a check isn't possible, label the claim explicitly as unverified and say what would confirm or refute it.

**Absence of evidence rule.** Not finding something in a search is weak evidence that it doesn't exist. Never write "the person is not present in X" when the evidence supports only "no presence in X surfaced in this search." Distinguish carefully between *an artifact being visible* (their work is cited, used, referenced) and *the person being visible* (they participate, publish, appear in that community's venues) — these are different claims with different implications, and conflating them produces a wrong diagnosis with a plausible surface.

---

## Phase 1 — Target market understanding

`view ${CLAUDE_PLUGIN_ROOT}/skills/field-understanding/SKILL.md` and apply it to the **market the person is selling into** — not their discipline in general, but the specific hiring or client market ("AI safety research roles at frontier labs," not "machine learning").

Extract and record these 6 outputs; Phase 2 requires them:

1. **Market definition** — which roles, which employers or client types, what geography
2. **Who buys and what they pay for** — the outcomes purchased, not the titles
3. **Value chain** — where in the workflow this person sits, and where leverage accrues
4. **Supply side** — where competing candidates come from (academia, industry, adjacent fields, bootcamps, career changers)
5. **Commoditization line** — what is becoming abundant versus what remains scarce, with explicit attention to AI-driven shifts
6. **Named competing profile types** — 2–4 realistic archetypes, which become the Phase 4 peer set

---

## Phase 2 — Labor market forces

An adaptation of Porter's Five Forces to a labor or client market. No skill covers this; run it inline using the structure below. Keep it **person-agnostic** — describe what anyone in this market faces, not this individual. Each force must cite a Phase 1 output.

| Force | Personal-market translation |
|---|---|
| **Rivalry among candidates** | How many credible people compete for the same roles? Is competition on credentials, portfolio, referral, or price? Fierce credential-based rivalry compresses returns; referral-based rivalry rewards network |
| **Buyer power (employers/clients)** | How concentrated are the buyers? A handful of frontier labs is high buyer power; thousands of mid-market firms is low. Concentrated buyers set terms |
| **Supplier power (your inputs)** | What do you depend on that others control — credentials, platform access, employer affiliation, tooling, a visa, a licence? Dependencies others gate are leverage against you |
| **Threat of substitutes** | What replaces this role rather than competing within it — AI tooling, offshoring, automation, an adjacent function absorbing the work? Usually the most consequential force right now |
| **Threat of new entrants** | How hard is it to become credible here? Low barriers mean continuous new supply and eroding returns; high barriers (long training, scarce access, regulation) protect incumbents |

Close with a **structural verdict**: is this market favorable or hostile to sellers of this kind of labor, and where does the value pool actually sit? Then a transition sentence setting up what defensibility must overcome.

---

## Phase 3 — Business Model You

`view ${CLAUDE_PLUGIN_ROOT}/skills/business-model-you/SKILL.md` and follow Steps 0–3: the nine blocks, the archetype, and the coherence critique. Apply its sector calibration (academia, public sector, regulated professions) and its soft-revenue test (deliberate trade vs. undeliberate subsidy).

**Do not run its Step 4** — the integrated plan in Phase 7 replaces it, informed by everything downstream.

Carry forward for later phases: the strongest and weakest blocks, the archetype, the value-capture assessment, and any resources flagged as appreciating or depreciating.

---

## Phase 4 — Peer landscape

Phase 1 *named* competing profile types. This phase *analyzes* them, so Phase 5 compares against real profiles rather than labels.

**This is about profile archetypes, not named individuals.** Do not build dossiers on specific private people. Where public figures are genuinely instructive as reference points, use only public professional information and stay respectful.

### 4a. Tier the competition

- **Direct peers** — same background, competing for the same roles
- **Adjacent profiles** — different route, same destination (industry→academia, research→product, self-taught→credentialed)
- **Over-qualified entrants** — people moving down-market who compete on credibility
- **Insurgents** — newer, cheaper, faster-moving profiles enabled by tooling or changed norms

### 4b. Profile the 2–4 that matter

For each: typical background, what they offer that this person doesn't, what they lack, and how a buyer perceives them. Keep it to a few lines each — the goal is a usable comparison basis, not a study.

### 4c. Comparison table

| Dimension | **[Person]** | Peer type A | Peer type B | Peer type C |
|---|---|---|---|---|
| Typical background | | | | |
| Core offer | | | | |
| Scarcest asset | | | | |
| Legibility to buyers | | | | |
| Main weakness | | | | |

### 4d. Name the binding comparison

Which peer type most constrains this person's opportunities — and why. Usually not the most credentialed, but the one buyers find **easiest to evaluate**. Legibility beats quality in markets where buyers can't assess deeply. State what that peer would have to do to win the same opportunity, and what this person must do to be chosen instead.

---

## Phase 5 — Personal 7 Powers

`view ${CLAUDE_PLUGIN_ROOT}/skills/personal-power-analysis/SKILL.md` and follow it.

Phase 0 supplied the arena; **Phase 4 supplied the foils** — use those, and do not re-derive them. Run the full Benefit × Barrier test on all seven powers, the strength-vs-power audit including commoditization reclassification, and the portability × legibility overlays.

Produce: the power stack, the anchor power, the compounding check, and the critical vulnerability.

---

## Phase 6 — Compensation and market reality

Powers that don't show up in captured value are hypotheses. Test them.

`view /mnt/skills/plugins/human-resources:comp-analysis/SKILL.md` for benchmarking structure. Where an Indeed connector or similar job-market tool is available, use it to ground demand in actual postings rather than impression.

Assess:
- **Benchmark position** — where does current compensation sit against the market for this profile and geography? Use ranges and name the uncertainty; do not present point estimates as precise.
- **Powers-to-capture gap** — if Phase 5 found real powers but compensation sits at median, the powers are illegible, mis-aimed, or unexercised. Which?
- **Demand evidence** — how many real openings exist for this profile? Thin demand changes the whole strategy regardless of how strong the powers are.
- **Non-cash capture** — equity, autonomy, learning, flexibility, security. Apply the deliberate-trade test from Phase 3; do not treat a chosen trade as underpayment.
- **The falsifier** — what compensation or demand evidence would show the strategic read is wrong?

If data is unavailable, say so plainly rather than estimating from impression.

---

## Phase 6b — Widen the option space before verdict

**Mandatory checkpoint. Do not skip.** Career analyses default to binary framing — stay or leave, this role or that role — because the decision was stated that way in Phase 0. For senior people especially, the binary is usually false, and the best option often sits between the poles.

Before writing the verdict, explicitly enumerate:

- **Warm internal channels first.** Does the person already hold a relationship with an organization in the target market — an advisory role, a scholar or affiliate appointment, a former employer, a consulting client, a co-author? **An existing relationship is a warmer channel than any external application**, and is systematically underweighted because it feels like the status quo rather than a move. Check this before recommending any cold path.
- **Non-binary structures:** advisory or affiliate roles, part-time or fractional arrangements, sabbatical placements, visiting researcher terms, contract or consulting engagements, joint appointments, secondments, board or committee positions. Seniority buys access to these; junior candidates rarely have the option.
- **Sequenced entry:** a low-commitment arrangement that converts later — visiting or sabbatical first, permanent second. This resolves the reversibility problem that makes the structural move hard.
- **Stay-and-change:** renegotiating the current role — scope, allocation, affiliation, external time — is a genuine option and must be analyzed with the same rigor as leaving, not treated as the null case.

**Then analyze the stay branch as seriously as the leave branch.** If Phase 0's decision was framed as a departure, that framing came from the person's current mood as much as from the evidence. State what staying would have to look like to be the right answer, and what would make it wrong. An analysis that only builds the case for change is advocacy, not analysis.

Carry the widened option set into Phase 7's move table so the plan is not artificially narrowed.

---

## Phase 7 — Integrated verdict and plan

Answer the three questions the frameworks were chosen to separate:

1. **Is the model coherent?** (Phase 3) — does value creation match value capture?
2. **Is the market favorable?** (Phases 1–2) — structural forces, and where the value pool sits.
3. **Is the position defensible?** (Phase 5) — what stops someone else being chosen instead?

Resolve into a single judgment answering the Phase 0 decision, and **name the binding constraint** — the one thing most limiting outcomes. The strongest analyses find that the model is fine but the market is hostile, or the market is good but the position is illegible, rather than rating everything equally.

Then produce the plan, following `business-model-you` Step 4's structure:

**Scored moves**

| Move | What it fixes | Effort | Payoff | Reversible? | Depends on |
|---|---|---|---|---|---|

**Three horizons** — Now (0–30 days, cheap, reversible, information-generating) · Near (1–6 months, build or open something) · Structural (6–18 months, changes the model's shape, downstream of evidence from earlier horizons).

**The first move** — one, with why it dominates.

**What NOT to do** — moves that address a non-binding block, strengths not to trade away, and what the analysis does not support.

**Decision triggers** — 2–3 observable events that would change the recommendation.

---

## Output format

**Citations in files must be real links.** Never write `<cite index="...">` citation markup into a file. That markup only resolves inside the chat interface, where it is matched against search results in context; written to a document it becomes inert text with nothing to resolve against, and it survives conversion to .docx or .pdf as visible junk. In files, cite with ordinary markdown links — `[the claim text](https://url)` — and close the document with a numbered **Sources** list mapping each externally-sourced claim to its URL. Chat responses use citation markup normally; files never do.


Length makes this a file. If `/mnt/user-data/outputs/` exists (the claude.ai convention), write `[name]-career-deep-dive.md` there and present it. In any other environment (Claude Code, Codex, etc.), ask the user where to save the file before writing it — do not assume a path silently. If asking isn't practical, default to the current working directory, name the file `[name]-career-deep-dive.md`, and state the exact path you used. Either way, follow the write with a tight summary in chat (5–8 sentences: the verdict, the binding constraint, the first move).

```
# [Name] — Career Deep Dive
[Evidence date + decision being analyzed + career stage + sector calibration]

## Part 0 — Scope
## Part 1 — Target Market            (6 outputs)
## Part 2 — Labor Market Forces      (person-agnostic + verdict)
## Part 3 — Business Model You       (9 blocks, archetype, coherence)
## Part 4 — Peer Landscape           (tiers, profiles, comparison, binding peer)
## Part 5 — Personal 7 Powers        (stack, anchor, critical vulnerability)
## Part 6 — Compensation & Demand Reality
## Part 6b — Option Space (warm channels, non-binary structures, the stay branch)
## Part 7 — Verdict + Staged Plan
## Sources & confidence notes
```

---

## Depth calibration

- **Early career**: Phase 5 assesses only powers *achievable at this stage* — counter-positioning and early cornered resources, not brand or process power. A thin power stack is normal, not a failing. Weight Phases 1–2 heavily; market choice matters more than differentiation this early.
- **Mid career**: the fullest run. Coherence and defensibility both carry real signal.
- **Senior**: emphasize leverage, portability, and opportunity cost. Powers exist; the question is whether they're exercised and whether they transfer.
- **Pivot/transition**: run Phase 3 as *two* canvases, current and target, and Phase 5 twice — powers in the current arena versus powers in the target arena. The gap between them is the analysis.
- **In a hurry**: Phases 3, 5, and 7 only; state what's skipped.

---

## Guardrails

- **Wellbeing precedes framework.** If someone describes burnout, distress, or crisis rather than a strategy problem, respond to the person first. A structured career analysis is the wrong instrument for distress and can make it worse. The pipeline can wait; say so plainly and kindly.
- **This is a strategic lens, not life advice or therapy.** Career dissatisfaction sometimes has causes no canvas can see.
- **Respect deliberate trades.** Lower capture chosen for autonomy, mission, family, or stability is a valid design. Name trade-offs; do not diagnose choices as errors.
- **Be direct when the subject is the reader.** They can verify every claim against their own experience and will detect hedging or flattery instantly. Do not soften the weakest finding — locating it is why they asked. Keep observation and inference visibly separate so they can reject a conclusion without discarding the evidence.
- **Don't manufacture powers or pad thin evidence.** An honest "no power here yet, and here's what's buildable" beats an inflated moat.
- **Privacy.** For a third party, use only public professional information. Do not compile personal details, and do not build comparison dossiers on private individuals — Phase 4 profiles archetypes, not people.
- **Compensation is guidance, not advice.** Present ranges and sources so the person decides; note you are not a financial or legal advisor.
- **Don't narrow the option space to the question as asked.** The person's framing reflects where their thinking currently is, not the full set of available moves. Phase 6b exists to correct this and is not optional.
- **Don't let the pipeline agree with itself.** If frameworks conflict — a strong model in a hostile market, real powers with no captured value — surface the conflict. Uniform agreement across all phases usually means one wasn't run honestly.
