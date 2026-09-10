---
name: business-model-canvas
description: Analyze a business, product, startup, or organization using the Business Model Canvas framework from Osterwalder & Pigneur's "Business Model Generation". Use this skill whenever the user wants to understand how a company makes money, map or critique a business model, compare business models, evaluate a startup idea. Trigger on phrases like "analyze [company]'s business model", "how does [company] make money", "business model canvas for X", "map my startup idea", "stress-test my business model", or any request combining a business + strategic understanding intent — even if the user never says "canvas". ALSO trigger for full-pipeline requests like "full strategic analysis of X", "deep strategy on X", or "run the strategy pipeline on X" — this skill orchestrates a composed sequence (Canvas → Porter's Five Forces → 7 Powers) for those.
---

# Business Model Canvas Analyzer

Apply the Business Model Canvas (BMC) to deeply understand a **business**. This is not a fill-in-the-boxes exercise: the value comes from evidence, coherence-checking, pattern recognition, and honest critique.

## Step 0: Scope and gather context

This skill covers companies, products, startups, nonprofits, and business ideas. For an individual's career or professional profile, hand off to `business-model-you` (see routing note below).

If the subject is a real company or public figure and current facts matter (pricing, products, recent pivots), use web search to ground the analysis in evidence rather than memory. If the subject is the user's own idea or the user themselves, ask 2–3 targeted questions ONLY if critical blocks can't be inferred from what they've shared (e.g., "Who pays, and for what?"). Don't interrogate — infer what you reasonably can and label inferences.

## Step 1: Fill the nine blocks (with evidence)

Work through the blocks in this order — it follows the logic of value creation:

1. **Customer Segments** — Who is served? Distinguish: mass market / niche / segmented / diversified / multi-sided. For multi-sided models (e.g., ad-funded), name each side and who subsidizes whom.
2. **Value Propositions** — What problem is solved, per segment? Classify the type: newness, performance, customization, design, price, cost reduction, risk reduction, accessibility, convenience, status.
3. **Channels** — How does the value reach customers? Cover the 5 phases: awareness → evaluation → purchase → delivery → after-sales. Note own vs. partner channels.
4. **Customer Relationships** — Acquisition, retention, upselling. Type: personal assistance, dedicated, self-service, automated, communities, co-creation. Note switching costs and lock-in.
5. **Revenue Streams** — For EACH segment: what do they pay for, how (asset sale, usage fee, subscription, licensing, brokerage, advertising), and what's the pricing mechanism (fixed vs. dynamic)? Estimate rough revenue mix if known.
6. **Key Resources** — Physical, intellectual (brands, patents, data), human, financial. Which are genuinely scarce/hard to copy?
7. **Key Activities** — Production, problem-solving, or platform/network management? What must the business be *excellent* at?
8. **Key Partnerships** — Strategic alliances, coopetition, joint ventures, supplier relationships. What's the motivation: optimization, risk reduction, or resource acquisition?
9. **Cost Structure** — Cost-driven vs. value-driven; biggest fixed and variable costs; economies of scale/scope.

**Evidence discipline**: mark each claim as [verified] (sourced/stated), [inferred] (reasonable deduction), or [unknown] (gap worth investigating). Never present speculation as fact.

### Analyzing a person instead of a business

For careers, professional profiles, or personal positioning, use the **`business-model-you`** skill instead (`view ${CLAUDE_PLUGIN_ROOT}/skills/business-model-you/SKILL.md` once installed) — it holds the personal adaptation (career stages, archetypes, soft revenue, burnout and opportunity cost).

Routing rule for the ambiguous case: a **solopreneur or consultant** is both. If the question is about the practice — pricing, clients, scaling — use this skill. If it's about the person's trajectory, skills, or sustainability, use `business-model-you` (which nests a business canvas for the practice where needed).

## Step 2: Pattern recognition

Check the model against the five patterns from the book, and name any that apply (models often combine several):

- **Unbundling** — separating customer-relationship, product-innovation, and infrastructure businesses (each has different economics/cultures).
- **Long Tail** — selling less of more; many niche products; low inventory cost; platform-enabled.
- **Multi-Sided Platform** — two+ interdependent groups; value grows with network effects; one side often subsidized.
- **FREE / Freemium** — free tier funded by ads, premium upgrades (watch the conversion rate), or bait-and-hook.
- **Open Business Model** — creating value via outside-in (external ideas in) or inside-out (internal assets licensed out) collaboration.

## Step 3: Coherence check and critique

This is where analysis beats description. Assess:

- **Fit**: Does each value proposition actually match a segment's real pain/gain? Do channels reach that segment? Do revenue streams reflect what customers truly value?
- **Left–right balance**: Does the cost structure (left side) plausibly support the value promise (right side)? Value-driven promise + cost-driven structure is a red flag.
- **Dependency risks**: single customer segment, single channel, single key partner, single key person — flag concentration.
- **Moat**: which key resources/activities are hard to replicate? What happens if the top competitor copies the model tomorrow?
- **Disruption exposure**: which block is most vulnerable to technology shifts, regulation, or changing customer behavior?

Give an honest verdict — name the 2–3 strongest blocks and the 2–3 weakest, with reasoning. Do not flatter.

## Step 4: Improvement directions (brief)

Offer 2–4 concrete "what if" moves drawn from canvas thinking: e.g., add a segment, change the revenue mechanism (sale → subscription), self-serve a relationship to cut costs, partner instead of build, unbundle.

## Output format

**Citations in files must be real links.** Never write `<cite index="...">` citation markup into a file. That markup only resolves inside the chat interface, where it is matched against search results in context; written to a document it becomes inert text with nothing to resolve against, and it survives conversion to .docx or .pdf as visible junk. In files, cite with ordinary markdown links — `[the claim text](https://url)` — and close the document with a numbered **Sources** list mapping each externally-sourced claim to its URL. Chat responses use citation markup normally; files never do.


Default output is a structured markdown analysis in chat:

1. **One-line model summary** (e.g., "A two-sided freemium platform monetizing the business side")
2. **The canvas** — a markdown table or 9 short labeled sections (keep each block to 1–4 bullets; density over prose)
3. **Patterns identified**
4. **Coherence check: strengths / weaknesses / risks**
5. **2–4 improvement moves**

If the user asks for a document/deck, create the appropriate file (docx/pptx via those skills). If the user asks to compare two businesses, produce side-by-side canvases and highlight the 3 most strategic differences, not all 9 blocks.

## Composing with other skills

The canvas describes the model; other frameworks test and extend it.

**How composition actually works — this is a required mechanic, not a suggestion.** Skills are not callable functions. Naming a skill does nothing on its own. To compose, you MUST `view` the other skill's SKILL.md at the path below and follow its instructions. If you skip that read, you are improvising the framework from memory, which defeats the purpose of composing.

Compose when the trigger fits; don't run all of them by default — either the trigger clearly applies, or briefly offer the extension after delivering the core canvas.

| When | Compose with | Division of labor |
|---|---|---|
| Industry/domain is unfamiliar to the user | `field-understanding` → `view ${CLAUDE_PLUGIN_ROOT}/skills/field-understanding/SKILL.md` | Run FIRST for landscape context; then BMC maps the specific player |
| User asks about defensibility, competition, or "is this a good market" | `ai-product-forces-and-powers` → `view ${CLAUDE_PLUGIN_ROOT}/skills/ai-product-forces-and-powers/SKILL.md` | BMC = internal value machine; Porter = external industry forces BMC ignores; 7 Powers = rigorous moat test replacing the shallow moat check in Step 3. Ideal sequence: BMC → Porter → 7 Powers |
| Analyzing the user's OWN idea with thin/vague blocks | `grill-me` → `view ${CLAUDE_PLUGIN_ROOT}/skills/grill-me/SKILL.md` | Interview the user to fill the canvas with real answers before critiquing |
| Comparing against named competitors | `view /mnt/skills/plugins/product-management:competitive-brief/SKILL.md` or `/mnt/skills/plugins/marketing:competitive-brief/SKILL.md` | Side-by-side canvases feed the battlecard |
| Deep evidence needed on a complex company | `sl` → `view ${CLAUDE_PLUGIN_ROOT}/skills/sl/SKILL.md` | Gathers verified facts per block before analysis |
| Deliverable output requested | `/mnt/skills/public/pptx/SKILL.md`, `/mnt/skills/public/docx/SKILL.md` | Canvas content → slide deck or document |

### Full pipeline mode ("deep strategy" invocation)

When the user asks for a **"full strategic analysis"**, **"deep strategy"**, **"complete strategic picture"**, **"BMC + Porter + 7 Powers"**, or says **"run the strategy pipeline on X"**, execute the composed sequence in one flow without asking which frameworks to use:

1. **Evidence gathering** — web-search current facts once, up front (revenue, pricing, products, recent pivots, litigation, competitors). This single evidence base serves ALL subsequent phases.
2. **Business Model Canvas** (this skill) — describe the value machine, patterns, coherence check.
3. **Porter's Five Forces + 7 Powers** — **first `view ${CLAUDE_PLUGIN_ROOT}/skills/ai-product-forces-and-powers/SKILL.md`**, then follow it: industry structure, then moat vs. the 2–3 named competitors identified during BMC.
   - **Known instruction conflict, and how to resolve it.** That skill states "Do not skip or compress Phase 1 [field understanding]" — a correct rule when it runs standalone, because Porter without field grounding produces generic force ratings. When it runs *after* BMC in this pipeline, its purpose is already served: BMC Step 1 produced the evidence base. So satisfy the requirement rather than skipping it — write an explicit **"Condensed field grounding"** paragraph covering that skill's 8 required outputs (submarket definition, value chain, key suppliers, key buyers, competitive structure, substitution threats, commoditization line, named competitors) drawn from the shared evidence. Each Porter force must still cite one of those outputs, exactly as that skill requires. Do NOT re-run the full `field-understanding` skill.
   - If the industry is genuinely unfamiliar and BMC Step 1 did *not* produce those 8 outputs, do not compress — run it properly: `view ${CLAUDE_PLUGIN_ROOT}/skills/field-understanding/SKILL.md`.
4. **Integrated verdict** — one synthesis answering: is the model coherent (BMC), is the market attractive (Porter), is the position durable (7 Powers)? Plus a compressed watch-list/roadmap with named replan triggers.

Deliver the full pipeline as a markdown report file (it exceeds chat length); give a cited executive summary in chat. For the personal equivalent, `business-model-you` carries its own composition chain.

Sequencing principle: **understand (field) → describe (this skill) → test (Porter/7 Powers, grill-me, comp-analysis) → act (content, deck, plan)**.

## Guardrails

- Don't pad: if a block is genuinely thin (e.g., a pre-revenue startup), say so — the gap IS the finding.
- For real companies, prefer recent, verifiable facts; the canvas of a company in 2020 may be obsolete.
- Never invent revenue figures or market share; use qualitative language or ranges with sources.
