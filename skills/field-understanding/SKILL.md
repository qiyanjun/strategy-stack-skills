---
name: field-understanding
description: >
  Use this skill whenever a user wants to deeply understand a new industry, domain, or field of
  knowledge — including scientific disciplines, academic fields, and emerging technology areas,
  not just traditional business industries. Trigger when users ask things like "help me understand
  X", "explain the [field] landscape", "I want to learn about [domain] like an insider",
  "break down [field] for me", "how does [industry] work", "teach me about [domain]", or
  "give me an overview of [field]". Also trigger when a user provides a field + audience
  combination (e.g. "explain genomics to a bioinformatics student" or "walk me through
  fintech as if I'm a policy maker"). Always use this skill when the request involves
  comprehensively understanding or mapping out an entire domain — even if the user's phrasing
  is casual or short.
---

# Field Understanding Skill

Deliver a **structured, multi-lens orientation** to any field, industry, or domain.
Works for any audience — students, executives, investors, researchers, policy makers.

---

## Step 1 — Identify Field, Audience, and Mode

Before generating output, determine:

- **Field**: What domain are we mapping? (e.g., synthetic biology, hedge funds, NLP, logistics)
- **Audience**: Who is this for? (undergraduate, industry practitioner, investor, executive, etc.)
  — If unclear, infer from context or ask. Audience drives which lenses to emphasize.
- **Mode**: Choose based on how the user framed the request:
  - **Quick Overview** — casual phrasing ("how does X work?", "give me a sense of X"), limited time implied, or user seems to want orientation, not a deep dive. Cover 3–4 lenses most relevant to the audience.
  - **Full Briefing** — explicit ask for comprehensive coverage, user says "deep dive", "full breakdown", "map the field", or "explain everything about X". Cover all 7 lenses.

When in doubt, default to **Quick Overview** and offer to go deeper.

---

## Step 2 — Select and Sequence Lenses

Work through lenses that are most relevant given audience and mode.
Each lens can stand alone — they do not need to be covered in order, though the default order works well.

Use the **Audience Calibration** table below to decide which lenses to emphasize and which to trim.

| Audience | Primary lenses | Secondary lenses | Skip or skim |
|---|---|---|---|
| Undergraduate student | Subfields, Technology | Academic/Technical | Investor, Org Structure |
| Graduate / PhD | Academic/Technical, Subfields | Technology, Money Flow | Investor, Org Structure |
| Industry practitioner | Org Structure, Products | Technology, Money Flow | Academic, Investor |
| Executive / MBA | Money Flow, Products | Investor, Org Structure | Academic |
| Investor / VC | Investor, Money Flow | Products, Technology | Academic, Org Structure |
| Policy maker | Money Flow, Org Structure | Subfields, Products | Investor, Technology |
| General curiosity | Subfields, Technology | Products | Org Structure, Investor |

Calibrate **depth and language** to audience too:
- Undergrad / general: accessible language, define jargon, concrete analogies
- Grad / PhD: technical terminology, methods, frontier debates
- Practitioner: operational detail, insider vocabulary
- Executive / MBA: strategic framing, business metrics
- Investor / VC: financial language, market sizing, moats
- Policy maker: plain language, risk framing, societal impact

---

## Step 3 — The 7 Lenses

---

### Lens 1 — Subfields

Give the user a mental map of the field's internal structure.

Cover:
- 4–8 core subfields or disciplines, each with a one-sentence description
- How subfields relate to or depend on each other
- Which are emerging vs. mature vs. foundational
- Where the user's background fits (if known)

---

### Lens 2 — Enterprise Org Structure

Show how a typical organization *inside this field* is structured.

Cover:
- C-suite / leadership roles and what they own
- Core functional departments (R&D, Ops, Commercial, Regulatory, etc.)
- Roles unique to this field (e.g., Medical Affairs in pharma, Quant in finance)
- How decisions flow between departments
- Structural differences between large incumbents vs. startups

---

### Lens 3 — Product Structure

Understand what the field makes, sells, or delivers.

Cover:
- Core product/service categories
- Product lifecycle: how products are created, validated, launched, retired
- Key product metrics (clinical endpoints, ARR, throughput, etc.)
- How products differ across customer segments
- Flagship real-world examples from leading organizations

---

### Lens 4 — Money Flow & Value Chain

Understand where money enters the system, how it moves, and who captures value.

Cover:
- Primary revenue models (subscription, fee-for-service, licensing, etc.)
- End-to-end value chain: raw inputs → end customer
- Key players at each stage of the value chain
- Where margin is concentrated and why
- How money flows differently for incumbents vs. disruptors
- Key cost drivers

---

### Lens 5 — Technology Landscape

Map the enabling technologies and infrastructure of the field.

Cover:
- Core enabling technologies (platforms, tools, infrastructure)
- Technology stack layers (data, compute, algorithms, applications — adapt to field)
- Key vendors and open-source ecosystems
- What is differentiating vs. commoditized
- Emerging tech trends likely to reshape the field
- Data standards and interoperability considerations (where relevant)

---

### Lens 6 — Investor Perspective

See the field through the lens of value creation, risk, and market dynamics.

Cover:
- Market size and growth trajectory (TAM/SAM where applicable)
- Dominant investment theses currently driving capital into the field
- Major public players and their market positions
- VC/PE activity and where capital is concentrating
- Key business model risks (regulatory, reimbursement, commoditization, etc.)
- Competitive moats: what makes companies defensible
- Leading indicators investors track (KPIs, milestones, pipeline metrics)
- Exit landscape (IPO, M&A trends)

---

### Lens 7 — Academic & Technical Foundations

Understand the field's intellectual roots and research frontier.

Cover:
- Core academic disciplines that underpin the field
- Landmark papers, books, or discoveries that shaped it
- Key journals, conferences, and preprint servers
- Open research questions and active debates
- Methodological approaches and common study designs
- How academic output translates into commercial or policy impact
- Career pathways: from academia into industry or policy

---

## Step 4 — Synthesize Across Lenses

After covering the selected lenses, close with a brief synthesis that:

- Names 2–3 key tensions or dynamics that cut across multiple lenses (e.g., "the org structure reflects where the money is, which explains why R&D is underfunded relative to commercial")
- Highlights what is most counterintuitive or surprising about the field
- Notes where the field is likely to change or be disrupted in the near term

This cross-lens synthesis is what distinguishes a real expert orientation from a list of facts.

---

## Step 5 — Closing Package

End every briefing with:

1. **Cheat sheet** — 5–8 bullet points: the most important things to know, distilled
2. **3 resources** — one book, one paper/report, one practitioner blog/podcast/newsletter
3. **3 starter questions** — the most interesting questions to explore next, calibrated to audience

For **Quick Overview**, include only the cheat sheet and 2 starter questions — skip the full resource list unless the user asks.

---

## Output Format

- **Quick Overview**: conversational in-chat prose, organized by lens with clear headings. No artifact needed unless the user asks to save it.
- **Full Briefing**: create an artifact (markdown) so the user can save and reference it. Use clear section headers, cheat sheet, and resources at the end.

Always use **concrete examples** — name real companies, tools, journals, metrics, and people. Generic explanations are far less useful than specific ones.

---

## Mode Selection Examples

| User says | Mode | Notes |
|---|---|---|
| "How does NLP work?" | Quick Overview | Casual phrasing; 3 lenses max |
| "Explain the hedge fund industry" | Quick Overview | Default to overview; offer to go deeper |
| "Give me a full breakdown of synthetic biology" | Full Briefing | Explicit "full breakdown" |
| "Teach me genomics like I'm a bioinformatics PhD student" | Full Briefing | PhD + specific audience = depth expected |
| "I'm pitching to biotech VCs next week — help me understand the field" | Full Briefing | High-stakes context implies depth needed |
| "What's the deal with logistics tech?" | Quick Overview | Conversational and casual |
