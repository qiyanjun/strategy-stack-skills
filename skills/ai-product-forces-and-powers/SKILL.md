---
name: ai-product-forces-and-powers
description: "Three-phase strategic analysis for an AI product feature: field understanding, then Porter's Five Forces (industry level - is this market attractive?), then Helmer's 7 Powers assessed comparatively against 2-3 named competitors (does this feature have a durable moat?), closing with an 18-month phased roadmap where every initiative traces to a Porter force or power finding. Use whenever a user wants to evaluate an AI feature or product strategically, assess defensibility, decide whether to build it, understand a competitor's moat, or turn a competitive diagnosis into a roadmap. Trigger on 'analyze [feature] strategically', 'how defensible is [feature]', 'apply Porter / 7 Powers', 'what competitive advantage does [feature] create', 'is [feature] a moat', 'roadmap for [feature]', or any AI product + competitive analysis intent, even without naming the frameworks. For a full company analysis use company-deep-dive; for the business model alone use business-model-canvas."
---

# AI Product Forces and Powers Analyzer

## Scope

This skill analyzes **one product feature** at a time - not a whole company. Its
heuristics are tuned to AI markets specifically (model layer vs. deployment layer
barriers, platform co-option, foundation-model disintermediation). For a full
multi-framework company analysis use `company-deep-dive`; for the business model alone
use `business-model-canvas`.

## How this skill works

The analysis runs in three sequential phases, each building on the last:

1. **Field Understanding** — a structured orientation to the industry and submarket the
   feature operates in, using the `/field-understanding` skill. This is not optional
   background reading; specific outputs from this phase feed directly into the Porter
   forces as grounding evidence.

2. **Porter's Five Forces** — industry-level structural analysis, grounded in what the
   field understanding revealed. Product-agnostic: characterizes what any player in this
   market faces, before naming the specific feature being analyzed.

3. **Helmer's 7 Powers + Roadmap** — product-level differentiation analysis comparing
   the specific feature against its 2–3 closest named competitors, followed by an
   18-month roadmap tracing every initiative back to a Porter force or power finding.

Do not skip or compress Phase 1. Porter analysis done without field understanding produces
generic force ratings that could apply to any market. The field understanding is what makes
the Porter analysis specific, grounded, and useful.

---

## Framework division of labor

**Porter's Five Forces → Industry level**
Maps the *structural competitive forces in the market segment* any player faces. Product-
agnostic: describes the landscape before naming any specific product. Answers: "Is this a
structurally attractive market to compete in? Where is the profit pool, and what forces
are compressing it?"

**Helmer's 7 Powers → Product/firm level**
Assesses *how this specific feature differentiates against its closest direct competitors*
within the landscape Porter mapped. Every power is assessed comparatively against named
competitors. Answers: "What makes this feature hard to displace once a customer has
adopted it?"

The two frameworks connect at the **transition**: the structural forces Porter reveals
(hostile rivalry, powerful suppliers, substitution threats) set the *stakes* for the 7
Powers analysis. A feature in a structurally hostile market needs stronger powers to
survive. A feature in a benign market can succeed with moderate powers.

---

## Phase 0 — Field Understanding

Before any competitive analysis, run the `/field-understanding` skill on the specific
industry and submarket the feature operates in. The goal is to build a factual foundation
that makes every subsequent Porter force grounded in real market knowledge rather than
generic framework patterns.

### How to run it

Invoke `/field-understanding` with:
- **Field**: the specific submarket (not the broad industry). Example: "AI prior
  authorization automation in US commercial health insurance" not "healthcare AI".
- **Audience**: investor/executive (emphasizes Money Flow, Product Structure, and
  competitive moats — the lenses most relevant to Porter and 7 Powers).
- **Mode**: Full Briefing — this analysis requires all relevant lenses.

### Which lenses to emphasize

The `/field-understanding` skill covers 7 lenses. For this analysis, the following are
essential; the others can be covered more briefly:

| Lens | Why it matters here |
|------|---------------------|
| **Lens 1 — Subfields** | Reveals how the market is segmented internally. Use this to precisely scope the Porter market segment — which specific subfield does the feature compete in? |
| **Lens 3 — Product Structure** | Maps what products exist, how they're validated, and what buyers expect. Feeds directly into Competitive Rivalry and Threat of Substitutes. |
| **Lens 4 — Money Flow & Value Chain** | The single most important lens for Porter. The value chain players become the supplier and buyer analysis. Where margin concentrates reveals which forces are most hostile. |
| **Lens 5 — Technology Landscape** | What is commoditized vs. differentiating in the technology stack. Feeds directly into Threat of New Entrants (model layer vs. deployment layer barriers). |
| **Lens 6 — Investor Perspective** | Market concentration, moat patterns, capital flow. Reveals which companies dominate and why — essential for identifying who the named competitors are in the 7 Powers section. |

Lenses 2 (Org Structure) and 7 (Academic Foundations) are lower priority unless the
competitive question specifically involves enterprise organizational dynamics or a research-
driven product category.

### Extract and record these outputs

After running `/field-understanding`, explicitly record the following before moving to
Porter. These become the evidence base for the structural analysis:

1. **Submarket definition**: the precise segment name and its scope (buyer, use case,
   geography if relevant)
2. **Value chain map**: who are the key players at each stage? Who captures the most
   margin and why?
3. **Key suppliers**: what do all players in this market depend on that others control?
4. **Key buyers**: who are the 3–5 largest or most powerful buyer categories?
5. **Current competitive structure**: how many credible players, and is the market
   concentrating or fragmenting?
6. **Substitution threats**: what existing or emerging alternatives could displace the
   entire category?
7. **Technology commoditization line**: what in the tech stack is already commoditized,
   and what remains differentiating?
8. **Named competitors for 7 Powers**: from the investor lens, identify the 2–3 most
   similar products that will serve as the foils in the 7 Powers analysis.

These 8 outputs are the direct inputs to the Porter analysis. Each Porter force section
should cite at least one of them as grounding evidence.

---

## Phase 1 — Scope

With the field understanding complete, confirm the four scoping parameters before
proceeding. Most will already be answered by the field understanding; this step just
makes them explicit:

1. **The feature**: What does it do? What is the user-facing capability?
2. **The market segment**: The precise submarket from field understanding output #1.
3. **The company and product**: Who offers this feature? What broader platform does it
   sit in?
4. **The competitive question**: What does the user need the analysis to answer?
   - *Build/invest decision*: Should we build this feature? Can we create a moat?
   - *Competitor threat assessment*: How defensible is a competitor's feature, and where
     is it vulnerable?
   - *Market entry framing*: What structural forces would we be navigating, and what
     differentiation would let us survive?

**Named direct competitors** (from field understanding output #8): confirm the 2–3
products that will serve as the comparison foils in the 7 Powers analysis.

---

## Part I — Porter's Five Forces: Industry Landscape

### What this section does (and does not do)

This section analyzes the **market segment** as an industry structure, grounded in
the field understanding from Phase 0. The specific product under analysis is not
mentioned here — this is what any player entering this market would face.

Each force must cite at least one concrete fact from the field understanding outputs
(value chain map, buyer list, technology commoditization line, competitive structure, etc.)
rather than making generic statements about the market. The field understanding is what
transforms a generic Five Forces template into a specific, credible analysis.

The output is a structural verdict on the market: attractive (few hostile forces, clear
profit pool) or hostile (multiple forces compressing margins simultaneously)?

---

For each force, write:
- **Intensity**: Very High / High / Medium / Low
- **2–3 key drivers** drawn from the field understanding — name specific players,
  pricing structures, or technology facts, not generic observations
- **One-sentence verdict**

### Force 1: Competitive Rivalry
*Draws from field understanding outputs #5 (competitive structure) and #3 (product structure)*

Map the current competitive structure of the segment. How many credible players compete
in this exact use case? Are products converging on functional parity, or is meaningful
differentiation visible? Is the market concentrating or fragmenting? Watch for platform
vendors absorbing the use case natively — the most common source of extreme rivalry in
AI markets. Name specific companies and their approximate share or scale.

### Force 2: Threat of New Entrants
*Draws from field understanding outputs #7 (technology commoditization) and #4 (value chain)*

Separate the model layer (typically low barriers — foundation models are commodity) from
the deployment layer (typically high — enterprise integrations, compliance certifications,
domain validation, procurement cycles). These are often opposite in AI markets: easy to
build a prototype, hard to reach production at scale. Rate each layer, then give a
combined intensity. Use the technology commoditization line from the field understanding
to judge where the barrier actually sits.

### Force 3: Supplier Power
*Draws from field understanding outputs #2 (value chain) and #3 (key suppliers)*

Name the specific suppliers that all players in this segment depend on. Use the value
chain map from the field understanding — the upstream players who sit above the feature
in the chain are the suppliers. Common AI supplier power sources: platform/ecosystem
gatekeepers, proprietary training data owners, foundation model providers, compute
infrastructure, and regulatory certification bodies. For each: how critical is the
dependency, and how many substitutes exist?

### Force 4: Buyer Power
*Draws from field understanding outputs #4 (key buyers) and #4 (money flow)*

Use the buyer list from the field understanding. How concentrated are they? Where does
the money flow — who pays, who decides, and are those the same entity? Assess: (a)
concentration (a few large enterprise buyers amplify buyer power enormously), (b) the
availability of platform-native substitutes that shift leverage to buyers, (c) whether
buyers can credibly self-build, and (d) budget pressure trends in this buyer segment.

### Force 5: Threat of Substitutes
*Draws from field understanding outputs #6 (substitution threats) and #5 (technology landscape)*

Use the substitution threats from the field understanding as the starting point. Two
patterns dominate AI markets: (1) *platform co-option* — the infrastructure vendor builds
this capability natively; (2) *foundation model direct access* — buyers bypass middleware
entirely. Add any category-level threats identified in the investor lens: regulatory
changes, workflow automation replacing the underlying need, or adjacent products expanding
scope to absorb this use case.

### Porter Verdict
2–3 sentences connecting all five forces to a structural verdict. Which forces are most
hostile, and what do they imply for any player in this market? Close with the transition
to the product analysis: "Given this landscape, a feature competing in [segment] must
possess [specific type of advantage] to achieve durable returns — which is what the
7 Powers analysis assesses next."

---

## Part II — Helmer's 7 Powers: Product Differentiation Analysis

### What this section does (and does not do)

This section analyzes **the specific feature** against its **2–3 closest direct
competitors** identified in Step 1. Every power assessment answers a comparative question:
does this feature have this structural advantage *relative to those specific competitors*?

A power that every product in the segment has equally is not a differentiating power —
it is table stakes. Only asymmetric advantages count.

The goal is to identify which powers make this feature hard to displace once a customer
has adopted it, and which gaps leave it exposed to a well-resourced competitor.

---

A **Power** requires both a *Benefit* (what economic advantage the power creates for the
firm) AND a *Barrier* (what specifically prevents the named competitors from replicating
it). A benefit without a barrier is a temporary advantage, not a power.

**Rating scale:**
- ★★★★★ Strong — durable, material economic benefit; replication barrier is structural
- ★★★★ Solid — real benefit and barrier; some execution or timing risk
- ★★★ Moderate — real but limited; benefit is modest or barrier is time-bounded
- ★★ Nascent — being built; not yet structurally durable
- ★ Weak / not present

For each power, write:
- **Comparative question**: Does [this feature] have this advantage *compared to
  [specific competitors]*?
- **Benefit**: What economic advantage does this power create vs. those competitors?
- **Barrier**: What specifically prevents those competitors from matching it?
- **Rating** and **Trajectory** (↑ growing / → stable / ↓ at risk)
- **Evidence**: One concrete, specific fact grounding the assessment

### Power 1: Scale Economies
Per-unit cost falls as volume grows. Compare: does this feature have meaningfully lower
unit economics than its named competitors at current or projected scale? Look for: fixed
infrastructure (data centers, model training) amortized over more customers, compliance
certification costs spread across a larger install base, or data diversity that improves
product quality with volume. Not present if cost scales roughly linearly with usage or
if all direct competitors have equivalent scale.

### Power 2: Network Economies
Each user makes the product more valuable to others. Compare: does adopting this feature
create value for other users that the named competitors cannot match? Direct (user-to-user
collaboration) and indirect (ISV/ecosystem/partner network) effects both qualify. Ask
specifically: if this feature had 10x more customers than its competitors, would the
product improve in ways competitors could not replicate? If the network effect is equally
available to all competitors, it is not a differentiating power.

### Power 3: Counter-Positioning
This feature's business model cannot be copied by key competitors without damaging their
existing profitable business. This is a power of *business model architecture*, not
product quality. Identify the specific competitor who is most threatened, then ask: why
can't they just copy this model? The answer must be a rational constraint (they would
destroy existing revenue) not a technical one. If competitors could copy the model
without self-harm, the power is absent.

### Power 4: Switching Costs
Value loss to a customer from switching to a competing product. Compare: after adopting
this feature, how much harder is it for a customer to switch to a named competitor vs.
how hard it would have been before adoption? Sources: data accumulation in proprietary
formats, deep workflow integration requiring re-training, compliance reconfiguration,
and re-validation costs. Compare specifically: do the named competitors have comparable
or lower switching costs? If so, this is not a differentiating power.

### Power 5: Branding
This feature can command a price premium from buyers who associate it with validated
quality, independent of the product's current performance. Compare: has this feature
built *more* brand trust than its named competitors through published outcome evidence,
third-party validation (analyst rankings, certifications), and track record? Branding
power is specifically about *risk aversion* in buyers who will pay a premium to avoid
an uncertain alternative.

### Power 6: Cornered Resource
Preferential access to a coveted asset unavailable to direct competitors at the same
cost. Compare: does this feature depend on or have access to something its named
competitors cannot obtain — proprietary datasets, exclusive partnerships, regulatory
clearances, unique talent, or proprietary compute? The resource must be *asymmetric* —
available to this product but not equally available to the named competitors.

### Power 7: Process Power
Embedded organizational processes that improve quality or reduce cost through accumulated
experience — invisible from outside but nearly impossible to replicate quickly. Compare:
has this feature's team built operational knowledge through production deployment that
the named competitors lack? Sources: years of edge cases improving model robustness,
clinical/domain-expert annotation pipelines, regulatory deployment experience. Process
power accumulates slowly and is most meaningful when the named competitors are younger
or less mature operationally.

---

### Power Stack Synthesis

After rating all 7 powers, identify the **power stack**: which 2–3 powers are mutually
reinforcing? Explain the compounding loop concretely:
"[Power A] → [specific mechanism] → [Power B] → [specific mechanism] → [Power C]"

Then identify the **critical vulnerability**: which power is absent or weak in a way
that the named competitors could exploit? Be specific about which competitor is best
positioned to exploit it and how.

---

## Part III — Summary Table

Always produce this table after the 7 Powers analysis:

| Power | Rating | Differentiating Advantage vs. [Competitor A, B] | Barrier | Trajectory |
|-------|--------|--------------------------------------------------|---------|------------|
| Scale Economies | ★★★ | ... | ... | ↑ |
| Network Economies | ★★ | ... | ... | → |
| Counter-Positioning | ★★★★ | ... | ... | → |
| Switching Costs | ★★★★★ | ... | ... | ↑ |
| Branding | ★★ | ... | ... | ↑ |
| Cornered Resource | ★★★ | ... | ... | ↑ |
| Process Power | ★★★ | ... | ... | → |

Note: the column header should name the actual direct competitors identified in Step 1.

---

## Part IV — Strategic Verdict

Write 3–5 paragraphs that:

1. **Connect the two frameworks**: Where does the Porter landscape make the 7 Powers
   finding *more* or *less* significant? (Example: "The Very High competitive rivalry
   Porter identified makes Switching Costs not just an advantage but a survival
   requirement — without them, functional parity among rivals means margin
   compression is inevitable.") The verdict should feel like a single integrated
   argument, not two separate summaries stapled together.

2. **Answer the competitive question** from Step 1 directly — build/invest verdict, or
   specific threat assessment, or entry framing.

3. **Name 1–2 specific strategic actions** implied by the analysis. Be concrete:
   not "deepen the moat" but "prioritize [specific integration / data agreement /
   commercial model change] in the next [timeframe] to compound [named power] before
   [named competitor] can close the gap."

4. **Identify the most important risk**: One specific competitive or structural
   development that would most undermine this feature's position. Name the early
   warning signal to watch.

---

## Part V — 18-Month Product Roadmap

This section translates the Porter and 7 Powers analysis into a phased product roadmap.
Every initiative must be explicitly tied to a finding from Part I or Part II — the roadmap
is the *operational answer* to the strategic diagnosis, not a generic feature list.

### Roadmap logic

The roadmap is driven by two inputs:

1. **From Porter**: Which forces are most hostile, and on what timeline do they intensify?
   Force movements (a supplier entering direct competition, a platform absorbing the use
   case natively, a regulatory change shifting buyer power) set the *urgency* of each
   phase. Initiatives that address an imminent force movement belong in Phase 1; those
   addressing slower-moving structural shifts belong in Phase 2 or 3.

2. **From 7 Powers**: Which powers are strong and need to be compounded? Which are weak
   or absent and represent critical vulnerabilities? Strong powers that are growing should
   be accelerated; weak powers that are exploitable by named competitors are the highest-
   priority gaps to close.

The roadmap prioritization rule: **close the most exploitable vulnerability first, then
compound the strongest power, then build toward the missing power that would complete the
stack.**

---

### Phase 1 — Foundation (Months 1–6): Close the Critical Vulnerability

Identify the single most exploitable gap from the 7 Powers analysis — the power that is
weakest AND that a named competitor is actively positioned to exploit. Phase 1 initiatives
focus entirely on closing or reducing that gap before the window closes.

For each initiative in this phase, specify:
- **Initiative name** (concrete, not abstract — e.g., "Epic App Orchard certification"
  not "improve EHR integration")
- **Framework driver**: Which Porter force or 7 Power does this address, and why now?
- **Success metric**: What observable outcome by month 6 confirms this initiative is
  working? (e.g., "signed BAA with 3 health systems", "KLAS submission submitted",
  "outcome-based pricing pilot live with 2 customers")
- **Named competitor risk mitigated**: Which competitor becomes less threatening if this
  succeeds?

Typical Phase 1 themes by competitive question:
- *Build/invest*: Prove the counter-positioning model works before the market learns to
  copy it; establish the first switching-cost seeds through production deployments
- *Threat assessment*: The vulnerability your analysis found in the competitor — what
  would a challenger need to execute in Phase 1 to make that vulnerability matter?
- *Market entry*: Achieve the minimum viable integration depth to make switching costs
  begin compounding

---

### Phase 2 — Compounding (Months 7–12): Accelerate the Power Stack

Phase 2 assumes Phase 1 succeeded. Now compound the powers that are already strong,
and begin building the second-tier powers that will complete the stack. The focus shifts
from defense (closing gaps) to offense (widening the lead on the strongest 1–2 powers).

For each initiative:
- **Initiative name**
- **Framework driver**: Which power does this compound, and what is the compounding
  mechanism? (e.g., "each new EHR integration adds to the proxy network, increasing
  switching cost for all existing customers, not just new ones")
- **Success metric** by month 12
- **Network/compounding effect**: How does completing this initiative make subsequent
  initiatives easier or faster? Roadmaps that compound are more valuable than roadmaps
  that are additive.

Typical Phase 2 themes:
- Deepen data gravity (more customer data in the system increases switching costs and
  improves product quality simultaneously)
- Expand the ISV/partner ecosystem if Counter-Positioning or Network Economies are
  primary powers
- Pursue third-party validation (KLAS rankings, FDA clearance, peer-reviewed publications)
  if Branding is a target power
- Negotiate exclusive data or partnership agreements if Cornered Resource is achievable

---

### Phase 3 — Structural Position (Months 13–18): Build the Missing Power

Phase 3 targets the power that is currently absent but would, if built, make the power
stack self-sustaining. This is typically the hardest and slowest power to build — which
is why it goes in Phase 3, after the foundation is set and compounding has begun.

For each initiative:
- **Initiative name**
- **Framework driver**: Which currently-absent power does this build, and why is it
  achievable now that Phases 1–2 are complete?
- **Success metric** by month 18
- **Long-run implication**: If this power is established by month 18, what becomes
  structurally true about this feature's competitive position that wasn't true at month 0?

---

### Roadmap Summary Table

Always produce this table after the three phases:

| Phase | Timeframe | Initiative | Framework Driver | Success Metric |
|-------|-----------|------------|-----------------|----------------|
| 1 | M1–6 | [Initiative A] | [Porter force / Power name] | [Metric] |
| 1 | M1–6 | [Initiative B] | [Porter force / Power name] | [Metric] |
| 2 | M7–12 | [Initiative C] | [Power name — compounding] | [Metric] |
| 2 | M7–12 | [Initiative D] | [Power name — compounding] | [Metric] |
| 3 | M13–18 | [Initiative E] | [Power name — building] | [Metric] |
| 3 | M13–18 | [Initiative F] | [Power name — building] | [Metric] |

---

### Roadmap risks

Close the section with 2–3 sentences on what would cause this roadmap to fail or need
replanning. The trigger to replan is always a specific observable competitive or structural
event — not generic uncertainty. Name the event (e.g., "Epic announces native [use case]
feature at HIMSS 2026", "Microsoft prices Copilot for Sales below $20/user/month") and
the specific phase it would invalidate.

---

## Output format

The full analysis is structured in this order:

```
## Field Understanding: [Submarket Name]
  [Key outputs 1–8, drawn from /field-understanding]

## Phase 1 — Scope
  [Feature, segment, competitive question, named competitors]

## Part I — Porter's Five Forces
  [Five forces, each citing field understanding outputs]
  [Porter Verdict → transition sentence to Part II]

## Part II — 7 Powers
  [Seven powers, each comparative against named competitors]
  [Power Stack Synthesis + Critical Vulnerability]

## Part III — Summary Table
  [7-row table with ratings, barriers, trajectories]

## Part IV — Strategic Verdict
  [3–5 paragraphs integrating Porter + 7 Powers + answering the competitive question]

## Part V — 18-Month Roadmap
  [Three phases, initiatives tied to Porter forces / powers]
  [Roadmap summary table]
  [Roadmap risks: named trigger events]
```

Default output format: structured markdown. If the user requests a Word document, invoke
the `docx` skill after completing the analysis. If they request slides, invoke `pptx`.

Use **bold** for framework terms on first use and for key verdicts.
Use ★ ratings exactly as specified. Use ↑ → ↓ in the summary table.
Name competitors explicitly — never "Competitor X"; always actual product names.

---

## Depth calibration

- **Build/invest decision**: The field understanding will often surface the substitution
  threats and supplier dependencies that make this market hard before the user has fully
  considered them. Don't soften a hostile Porter landscape. For 7 Powers, assess only
  powers *achievable* at the company's current stage — a pre-revenue startup cannot claim
  Scale Economies. The roadmap Phase 1 should be about survival and proving the model.
- **Competitor threat assessment**: The field understanding investor lens will identify
  the competitor's strongest structural position. Use that to make the 7 Powers assessment
  credible. The roadmap becomes "what would it take to unseat them" — Phase 1 exploits
  the vulnerability found, Phases 2–3 close the gap on their strongest power.
- **Market entry framing**: The field understanding is especially valuable here — it
  reveals the value chain dynamics and buyer concentration before the entrant has spent
  time in the market. The roadmap is the entry sequence: the order to build powers to
  survive hostile Porter forces long enough to compound a durable position.

Every Porter force must cite at least one field understanding output.
Every 7 Powers assessment must name a specific competitor as the comparison foil.
Every roadmap initiative must trace to a specific Porter force or power finding.