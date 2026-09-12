---
name: company-deep-dive
description: Run a complete end-to-end strategic analysis of a company, orchestrating multiple frameworks in dependency order — industry field understanding, Porter's Five Forces, Business Model Canvas, competitive landscape mapping, Helmer's 7 Powers, financial health, and an integrated verdict. Use whenever someone wants thorough multi-framework company analysis rather than a single-framework answer. Trigger on "analyze [company] end to end", "full/complete strategic analysis of [company]", "deep dive on [company]", "analyze [company] from scratch", "should we invest in / compete with / join [company]", or "run the full pipeline on [company]". ALSO use in landscape mode for "who are the major players in [field]", "map the competitive landscape of X", or "which companies matter in [market]". For a single framework only, use the narrower skill directly (business-model-canvas, or ai-product-forces-and-powers).
---

# Company Deep Dive — End-to-End Analysis Orchestrator

This skill runs a complete company analysis by sequencing several frameworks so each one feeds the next. It does not re-implement those frameworks — **it loads and follows them.**

## Critical mechanic: you must actually read the component skills

Skills are not callable functions. Naming a skill does nothing. At each phase below you MUST `view` the referenced SKILL.md and follow its instructions. Skipping the read means improvising a framework from memory — which produces analysis that looks structured but is generic, and is the main failure mode of this pipeline. If a path does not resolve, say so explicitly in the output rather than silently substituting your own version.

**Running under Codex or another host with no `${CLAUDE_PLUGIN_ROOT}`:** that variable is a Claude Code plugin convention and won't be set. Resolve any `${CLAUDE_PLUGIN_ROOT}/skills/<name>/SKILL.md` reference below as `<name>/SKILL.md` in the directory next to this skill's own directory instead.

---

## Why this order (dependency logic)

The sequence is not arbitrary; each phase requires the previous one's outputs:

| # | Phase | Requires | Because |
|---|---|---|---|
| 0 | Scope & evidence | Nothing | Everything downstream cites this shared base |
| 1 | Field understanding | Industry name | Porter forces are generic without it |
| 2 | Porter's Five Forces | Field outputs | Product-agnostic by design — does NOT need the company's model |
| 3 | Business Model Canvas | Company facts + field context | Maps how *this* company creates and captures value |
| 4 | Competitive landscape | Field outputs + target's canvas | Profiles the rivals; without this, 7 Powers compares against labels rather than real models |
| 5 | 7 Powers | BMC + Porter + rival profiles | Assesses differentiation of the specific model against *analyzed* rivals |
| 6 | Financial reality | Company financials | Tests whether the strategy shows up in the numbers |
| 7 | Integrated verdict | All of the above | The synthesis is the deliverable |

**Note on ordering:** the Business Model Canvas sits *before* 7 Powers, not after. 7 Powers evaluates how a specific model differentiates; running it before the model is mapped produces power ratings with nothing underneath them. Porter can precede BMC because Porter is explicitly product-agnostic.

---

## Phase 0 — Scope and shared evidence base

**Establish the analytical question first.** The same company yields a different analysis depending on why you're asking. Confirm (or infer, and state your assumption):

| Lens | Emphasis shifts toward |
|---|---|
| **Investor** | Revenue quality, unit economics, moat durability, valuation logic |
| **Competitor** | Vulnerabilities, where they're exposed, what to attack |
| **Potential employee / candidate** | Trajectory, culture signals, whether the model is sustainable |
| **Partner / customer** | Reliability, lock-in risk, roadmap dependence |
| **Acquirer** | Integration fit, what's actually being bought, key-person risk |

Then gather evidence **once**, and reuse it in every phase. Web-search current facts: revenue and growth, pricing and products, recent pivots or M&A, funding or filings, litigation and regulation, named competitors, leadership. For public companies, get the latest reported quarter. For complex subjects needing iterative research, `view ${CLAUDE_PLUGIN_ROOT}/skills/sl/SKILL.md` and use that loop.

Record the **evidence cutoff date** in the output. Strategic analysis ages fast.

---

## Phase 1 — Field understanding

`view ${CLAUDE_PLUGIN_ROOT}/skills/field-understanding/SKILL.md` and run it on the **specific submarket**, not the broad industry ("AI-enabled precision oncology diagnostics," not "healthcare AI"). Use investor/executive audience framing.

Extract and explicitly record these 8 outputs — Phase 2 requires them:

1. Submarket definition and scope
2. Value chain map — who captures margin, and where
3. Key suppliers — what everyone depends on that others control
4. Key buyers — the 3–5 most powerful buyer categories
5. Competitive structure — how many credible players; concentrating or fragmenting
6. Substitution threats — what could displace the whole category
7. Technology commoditization line — what's commoditized vs. still differentiating
8. **Named competitors** — the 2–3 closest rivals, which become the 7 Powers foils

---

## Phase 2 — Porter's Five Forces

`view ${CLAUDE_PLUGIN_ROOT}/skills/ai-product-forces-and-powers/SKILL.md` and follow its Part I.

That skill mandates field understanding before Porter — Phase 1 has satisfied that requirement, so proceed without re-running it. Each of the five forces must cite at least one of the 8 outputs above as grounding.

Keep this section **product-agnostic**: describe what any player in this market faces. Do not mention the target company yet. Output a structural verdict — attractive or hostile — plus a transition sentence setting the stakes for the moat analysis.

---

## Phase 3 — Business Model Canvas

`view ${CLAUDE_PLUGIN_ROOT}/skills/business-model-canvas/SKILL.md` and follow its Steps 1–3 (nine blocks, pattern recognition, coherence check).

Do NOT re-trigger that skill's own pipeline mode — this orchestrator is already handling the composition. Take from it: the nine blocks with evidence labels, the patterns, and the coherence critique. Skip its Step 4 improvement moves; the integrated verdict in Phase 7 replaces them.

Watch for the case where a company is really **two fused businesses** (e.g., a low-margin operation that exists to generate a high-margin asset). When that's true, say so before the nine-block table — it's usually the most important structural fact about the model.

---

## Phase 4 — Competitive landscape

Phase 1 *named* the competitors. This phase *analyzes* them, so that Phase 5's power comparisons are grounded in real models rather than company names.

`view /mnt/skills/plugins/product-management:competitive-brief/SKILL.md` and follow it for the profiling structure.

### 4a. Map the field

Tier the players — this is what makes "who matters" explicit rather than assumed:

- **Direct rivals** — same buyer, same job-to-be-done. These become the 7 Powers foils.
- **Adjacent players** — overlapping capability, different primary market; the likeliest future entrants.
- **Upstream/downstream players** — suppliers or channel owners who could integrate into this market (often the most underestimated threat).
- **Insurgents** — small/new entrants attacking a specific segment or price point.

State the basis for tiering. If a well-known name is *excluded*, say why — a landscape that omits an obvious player without explanation reads as an oversight.

### 4b. Mini-canvas each key rival

For the 2–4 most important direct rivals, run an abbreviated Business Model Canvas — **the same nine blocks, compressed to the four that differentiate**: Customer Segments, Value Proposition, Revenue Streams, Key Resources. Using the same framework as Phase 3 is what makes the comparison structured rather than impressionistic.

For each rival also record: relative scale (revenue/users where known), ownership/backing (a subsidiary of a larger parent competes differently than an independent), and their single strongest asset.

### 4c. Comparative table

| Dimension | [Target] | [Rival A] | [Rival B] | [Rival C] |
|---|---|---|---|---|
| Primary segment | | | | |
| Value proposition | | | | |
| Revenue model | | | | |
| Scarcest resource | | | | |
| Scale (revenue/users) | | | | |
| Backing / parent | | | | |
| Biggest vulnerability | | | | |

### 4d. Name the binding competitor

Conclude with a judgment, not a list: **which single rival most constrains the target's future**, and why. This is usually not the largest player — it's the one whose model most directly attacks the target's scarcest resource or most profitable segment. Name what that rival would have to do to win, and what the target would have to do to stop them.

**Landscape mode (optional):** if the user wants the whole field surveyed rather than the target's rivals profiled — "who are the important companies in X" — expand 4a into a full player map with one-paragraph profiles across all tiers, and say up front that breadth is being traded for depth on any single player.

---

## Phase 5 — 7 Powers

Continue in the same skill (`ai-product-forces-and-powers`), Part II.

Assess all seven powers **comparatively against the rivals profiled in Phase 4**, never against an abstraction or a bare company name. Use the Phase 3 canvas as the description of what is being defended, and the Phase 4 mini-canvases as what it is being defended against. Produce the power stack synthesis and name the **critical vulnerability** — the weakest power that a named competitor is positioned to exploit.

---

## Phase 6 — Financial reality check

Strategy that doesn't appear in the numbers is a hypothesis, not a finding. Test the story against the financials.

- **Public companies**: `view /mnt/skills/plugins/finance:financial-statements/SKILL.md` for statement structure and variance framing.
- **Private companies**: use the private-company protocol below. Do not simply list what's missing — read the signals that *are* public.

### Private-company protocol — read the round structure as evidence

When ARR, margins, and retention are undisclosed, funding events are not a consolation prize; they are the disclosure. Investors performed diligence you cannot, and the *shape* of what they agreed to reveals what they concluded. Read these:

**Who invested, and what that buys.** Financial VCs buy expected return — their participation signals growth confidence. Corporate/strategic investors buy access, and their presence signals the company is worth embedding. **Customers investing in their own vendor is the strongest single signal in private markets** — it is diligence backed by both money and usage. But read it in both directions: a round loaded with strategic and customer money rather than financial capital can mean the company is buying distribution *because* its standalone position doesn't compound. Say which reading the rest of the analysis supports.

**Round spacing and sequence.** Rounds closing within weeks or a few months of each other mean either strong inbound demand or unplanned need — distinguish them by who led. A new outside lead at a step-up is demand; an insider-led or flat/bridge round is need. Long gaps followed by a large raise suggest a milestone was reached (or a runway wall approached).

**Valuation step-up vs. capital raised.** A large step-up on a modest raise signals investor competition; a large raise at a modest step-up signals the company needed capital more than investors needed allocation.

**Stated use of proceeds.** "Deepen engineering" means the product is still being built. "Accelerate go-to-market / international expansion" means the product is considered done and the constraint is distribution — a meaningfully later stage, and a claim that can be checked against headcount composition.

**Headcount as a revenue proxy.** Compare employee count against sector revenue-per-employee norms to bound plausible revenue, and state the assumption explicitly. Headcount growth relative to capital raised also bounds burn.

**Pricing disclosure asymmetry.** Published entry pricing with opaque enterprise pricing usually indicates a land-and-expand model where the expansion economics are the real business — and where the undisclosed number is the one that matters.

**Absence as evidence.** A company that discloses funding but never revenue at a high valuation and a mature-sounding stage is making a choice. Note it without over-reading it — non-disclosure is the private-market norm — but if a company selectively discloses *some* metrics (customer logos, test volumes) and not others, the omissions are informative.

**Then state the falsifiers.** Name the 2–3 undisclosed numbers that would confirm or break the strategic story, and say which way current evidence leans. Label all of it reported-not-audited.

Look specifically for:
- **Growth quality** — organic vs. acquired; is the reported rate flattered by M&A?
- **Margin direction** — is gross margin trending toward the strategy's promise?
- **The GAAP-vs-adjusted gap** — what's excluded, and is it a real cost to owners (e.g., stock compensation)?
- **Operating leverage** — are costs growing slower than revenue?
- **Cash position and burn** vs. committed obligations.
- **The number that would falsify the strategic story**, and what it currently says.

If financials are unavailable, state that plainly — an unverifiable model is itself a finding.

---

## Phase 7 — Integrated verdict

This is the deliverable; everything above is input. Answer the three questions the frameworks were chosen to separate:

1. **Is the model coherent?** (Canvas) — does value creation match value capture?
2. **Is the market attractive?** (Porter) — structural forces and where the profit pool sits.
3. **Is the position durable?** (7 Powers) — what prevents a well-funded rival from copying it?

Then resolve them into a single judgment, explicitly answering the Phase 0 question. State plainly which of the three is the binding constraint — the strongest analyses identify that the model is fine but the market is hostile, or the market is attractive but the moat is thin, rather than rating everything equally.

Close with:

**Watch-list table** — 3 phases over ~18 months, each row tied to a specific framework finding:

| Phase | Focus | Framework driver | Observable signal |
|---|---|---|---|

**Replan triggers** — 2–3 *named, observable* events that would invalidate the analysis (a specific competitor action, ruling, or metric threshold), not generic uncertainty.

---

## Output format

**Citations in files must be real links.** Never write `<cite index="...">` citation markup into a file. That markup only resolves inside the chat interface, where it is matched against search results in context; written to a document it becomes inert text with nothing to resolve against, and it survives conversion to .docx or .pdf as visible junk. In files, cite with ordinary markdown links — `[the claim text](https://url)` — and close the document with a numbered **Sources** list mapping each externally-sourced claim to its URL. Chat responses use citation markup normally; files never do.


Length makes this a file, not a chat response. If `/mnt/user-data/outputs/` exists (the claude.ai convention), write `[company]-deep-dive.md` there and present it. In any other environment (Claude Code, Codex, etc.), ask the user where to save the file before writing it — do not assume a path silently. If asking isn't practical, default to the current working directory, name the file `[company]-deep-dive.md`, and state the exact path you used. Either way, follow the write with a tight cited executive summary in chat (roughly 5–8 sentences covering the verdict and the binding constraint).

Structure:

```
# [Company] — End-to-End Strategic Analysis
[Pipeline note + evidence cutoff date + analytical lens]

## Part 0 — Scope
## Part 1 — Field Understanding: [Submarket]   (8 outputs)
## Part 2 — Porter's Five Forces               (product-agnostic + verdict)
## Part 3 — Business Model Canvas              (9 blocks, patterns, coherence)
## Part 4 — Competitive Landscape               (tiers, rival mini-canvases, comparison table, binding competitor)
## Part 5 — 7 Powers                            (vs. profiled rivals + critical vulnerability)
## Part 6 — Financial Reality Check
## Part 7 — Integrated Verdict + Watch-List + Replan Triggers
## Sources & confidence notes
```

**Optional extensions** — offer, don't assume:
- Sales-ready battlecard from the Phase 4 landscape → `view /mnt/skills/plugins/marketing:competitive-brief/SKILL.md`
- Structured risk register → `view /mnt/skills/plugins/operations:risk-assessment/SKILL.md`
- Slide deck → `view /mnt/skills/public/pptx/SKILL.md`; Word report → `/mnt/skills/public/docx/SKILL.md`

---

## Depth calibration

- **Well-documented public company**: run all six phases fully; financials carry real weight.
- **Private/startup**: Phase 5 compresses to disclosed metrics with heavy labeling; Phase 4 assesses only powers *achievable at the company's stage* — a pre-revenue startup cannot claim scale economies.
- **Early-stage or thin evidence**: run the pipeline but shorten each phase and say clearly which blocks are unknown. Do not pad thin evidence into confident prose.
- **User is in a hurry**: offer the compressed version — Phases 1, 3, 5 and the verdict — and say what's being skipped.
- **Competitor evidence is thin** (private rivals, no disclosed metrics): keep the Phase 4 tiering and the binding-competitor judgment, but shorten the mini-canvases and label the gaps. A named unknown is more useful than an invented profile.

---

## Guardrails

- **Evidence discipline throughout**: label claims [verified] (sourced), [inferred] (deduction), [unknown] (gap). Never invent revenue figures, market share, or valuations.
- **Sources conflict often** on private-company metrics. When they do, give the range and name the disagreement rather than picking the flattering number.
- **This is strategic analysis, not investment advice.** If the framing is investor-oriented, provide the factual basis for the person's own decision and note that you are not a financial advisor. Do not issue buy/sell recommendations.
- **Contested public figures and politics**: when a leader's public conduct materially affects a block, report the sourced business effect and attribute contested claims — do not editorialize on the underlying politics.
- **Don't flatter the subject or the pipeline.** If the frameworks disagree, surface the disagreement; if a phase produced nothing useful, say so. An analysis where every framework confirms the same conclusion usually means one of them wasn't run honestly.
