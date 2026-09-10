# Comparison with public skills on GitHub

A search across GitHub topic pages, curated "awesome-claude-skills" lists, and the
`anthropics/skills` reference repo found no public repository that packages an
**interdependent skill cluster** (orchestrators calling components in a fixed
dependency order, validated by CI) the way this one does. This document goes one
level deeper: for each of the 9 authored skills, it names the closest existing public
skill, if one exists, and states concretely how this repo's version differs.

Searched 2026-09-10 via GitHub + web search, with direct fetches of the more promising
matches to confirm the comparison rather than judge it from a README summary alone.
**Verify before citing** — the ecosystem moves quickly and matches were found by search
terms, not an exhaustive index.

---

## Summary table

| Skill | Public counterpart found? | Verdict |
|---|---|---|
| `business-model-canvas` | **Yes, close** | Same framework, different discipline — see below |
| `ai-product-forces-and-powers` (Porter half) | **Yes, partial** | Porter alone exists publicly and in more granular detail; the 7 Powers half and the fusion into one product-level analysis does not |
| `grill-me` | **Yes, near-identical, and not original to this repo** | A community-common skill; several public forks are more elaborated than this one |
| `sl` | **Pattern known, packaging not** | Implements the academic Self-Refine / Reflexion loop pattern; no public Claude Skill packages it, and the specific 0–100 anti-gaming rubric appears original |
| `field-understanding` | No comparable skill found | Appears original |
| `business-model-you` | No comparable skill found | Appears original |
| `personal-power-analysis` | No comparable skill found | Appears original |
| `company-deep-dive` | No comparable orchestrator found | Appears original |
| `personal-career-deep-dive` | No comparable orchestrator found | Appears original |

**Net picture:** 3 of 9 authored skills (`business-model-canvas`, the Porter half of
`ai-product-forces-and-powers`, `grill-me`) implement a pattern that already exists
publicly, in one case near-verbatim. `sl` implements a known academic pattern with an
apparently original scoring mechanism on top. The remaining 5 skills, and the
cross-skill dependency architecture + CI validator itself, have no public counterpart
found.

---

## Per-skill detail

### `business-model-canvas`

**Closest match:** [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills/blob/main/project-management/strategy-frameworks/business-model-canvas/SKILL.md) (also `phuryn/pm-skills`, less detail confirmed).

Same 9-block Osterwalder framework, same core idea. Confirmed differences:

| | This repo | borghei/Claude-Skills |
|---|---|---|
| Evidence discipline | `[verified]` / `[inferred]` / `[unknown]` tags on claims | Evidence/riskiness/testability rating per *assumption*, oriented at startup validation |
| Composition | Routes to `business-model-you` for people, chains into Porter → 7 Powers for "full pipeline" requests | Composes with `lean-canvas`, `swot`, `porter-five-forces`, `value-proposition-canvas`, `north-star-metric`, `pricing-strategy` |
| Tooling | None — pure prompt skill | Ships a `canvas_validator.py` that checks completeness and segment→channel→revenue coherence programmatically |
| Iteration model | Single-pass with an honest coherence critique | Explicitly expects "3–5 revision cycles" as part of the workflow |

Neither has the other's person-vs-company routing rule or Porter/7-Powers pipeline mode
— they optimize for different things (this repo: composability into a larger strategy
stack; borghei's: iterative startup validation with a script-checked output).

### `ai-product-forces-and-powers` — Porter's Five Forces half

**Closest match:** [gnurio/porter-strategy-skills](https://github.com/gnurio/porter-strategy-skills) — 12 skills plus an orchestrator, extracted directly from Porter's *Competitive Strategy*, CC BY 4.0. Also `phuryn/pm-skills` (`porters-five-forces`) and `kannakumar/competitive-analysis-skill`, less detail confirmed.

Confirmed via direct fetch: gnurio's is **more granular on Porter alone** — it rates
all 5 forces across 32 named sub-factors (8 entry barriers, 8 rivalry drivers, 7 buyer
power factors, 6 supplier power factors, 3 substitute indicators) and adds strategic-group
mapping, industry-type diagnosis, and industry-specific playbooks (fragmented/emerging/
declining) that this repo doesn't attempt. It has no Helmer's 7 Powers and no AI-market
heuristics (model-layer vs. deployment-layer barriers, platform co-option) — it stays
strictly inside Porter's book.

### `ai-product-forces-and-powers` — Helmer's 7 Powers half

**No public skill found.** Search turned up only narrative blog/Substack applications of
7 Powers to AI moats (e.g. shipfit.ai, productstrategy.co, several Substack posts) — none
packaged as an agent skill, none with a comparative Benefit+Barrier rating scale against
named competitors. The fusion this repo does — Porter sets industry stakes, 7 Powers
rates the specific feature against 2–3 named rivals, a roadmap traces every initiative
back to a specific force or power — has no public equivalent found.

### `grill-me`

**Not original to this repo.** This is a small, terse skill (10 lines here) that is
widely circulated under the same name and near-identical wording:

- [ericgandrade/claude-superskills](https://github.com/ericgandrade/claude-superskills/blob/main/skills/grill-me/SKILL.md)
- [stevegsax/grill-me](https://github.com/stevegsax/grill-me)
- [RobMitt/grill-me-skill](https://github.com/RobMitt/grill-me-skill)
- [Jekudy/grillme-skill](https://github.com/Jekudy/grillme-skill)
- a [gist by usirin](https://gist.github.com/usirin/0f01923f7b2126b0cce817f9f8d97788)
- listed on [mcpmarket.com](https://mcpmarket.com/tools/skills/grill-me) and the [Tessl registry](https://tessl.io/registry/skills/github/belchman/claude-skills/grill-me)

Confirmed via direct fetch of ericgandrade's version: it is **more elaborated** than
this repo's — it restricts triggering to the literal word "grill" (explicitly excluding
"stress-test", "poke holes", "devil's advocate", "challenge" as *non*-triggers, to avoid
false-positive activation), and adds a decision-tree mapping step, periodic
summarization every 5–8 exchanges, and rules about completing one thread before opening
another. This repo's version is the shorter, original-form text
("interview me relentlessly... walk down each branch... ask one at a time... explore
the codebase instead") without those refinements.

**Recommendation:** treat this as a known community skill included for composability,
not a proprietary contribution — the README should say so plainly, and the more
elaborated public forks (trigger-word discipline, periodic summarization) are a
reasonable place to pull improvements from.

### `sl`

**Pattern is known; the packaging is not.** The draft → critique → revise loop is the
architecture behind two well-known agent papers: **Self-Refine: Iterative Refinement
with Self-Feedback** (Madaan et al.) and **Reflexion** (Shinn et al.), plus AWS's
"evaluator reflect-refine loop" prescriptive pattern. No public Claude Skill packages
this as a slash-command with a scoring rubric. This repo's specific contribution on top
of the known pattern: a named 0–100 rubric across 6 dimensions (Coverage, Evidence,
Accuracy, Reasoning, Calibration, Clarity), a 95-point stop threshold, a 5-round max, and
an explicit **anti-gaming / honest-ceiling** escape hatch that forbids inflating the
score to exit the loop. That specific mechanism was not found published elsewhere.

**Recommendation:** the skill's own docs should cite Self-Refine/Reflexion as the prior
art for the mechanism, which strengthens rather than weakens the skill — it signals the
loop is a validated pattern, not an invented one.

### `field-understanding`, `business-model-you`, `personal-power-analysis`, `company-deep-dive`, `personal-career-deep-dive`

**No comparable public skill found for any of these five**, despite targeted search
(industry-briefing skills with audience calibration; "Business Model You" as an agent
skill; 7 Powers applied to a person's career with Benefit/Barrier tests; end-to-end
company or career analysis orchestrators chaining 5+ frameworks in dependency order).
The closest adjacent things found were not real matches:

- For `business-model-you` / `personal-career-deep-dive`: [squerne/open-career-skills](https://github.com/squerne/open-career-skills) — a tactical job-search toolkit (CV optimizer, STAR stories, LinkedIn planner, mock interviews), structurally unrelated to a canvas/archetype/coherence-critique model.
- For `personal-power-analysis`: [Avyayalaya/pm-skills-arsenal](https://github.com/Avyayalaya/pm-skills-arsenal) encodes 7 Powers as one of 9 frameworks, but for products/companies, not individuals.
- For `company-deep-dive`: gnurio's Porter orchestrator chains skills, but only within Porter's own 12 — it doesn't cross into BMC, competitive-landscape mini-canvases, or financial reality-checking in one pipeline.

These five, along with the dependency-ordered orchestration architecture and the
CI reference validator (`tests/validate_skills.py`), are this repo's actual point of
novelty.

---

## What this means for the repo

1. **Don't claim originality for `business-model-canvas`, the Porter half of
   `ai-product-forces-and-powers`, or `grill-me`.** They implement known, publicly
   available patterns. The honest claim is: same framework, different discipline
   (evidence labeling, composition into this specific stack, AI-market heuristics on
   the Porter side).
2. **`grill-me` should credit its community origin.** It is currently presented with no
   attribution; the public forks are more developed and worth borrowing from
   (trigger-word discipline in particular avoids false-positive activation on "stress-test
   my plan" — a phrase that collides with `business-model-canvas`'s own triggers).
3. **`sl` should cite Self-Refine / Reflexion** as prior art for the loop mechanism.
4. **The real, defensible claim to originality** is: the personal-track skills
   (`business-model-you`, `personal-power-analysis`, `personal-career-deep-dive`), the
   company-track orchestrator (`company-deep-dive`), `field-understanding`, and the
   dependency-ordered, CI-validated cluster architecture itself. That's a narrower but
   more accurate claim than "10 skills, all original," and it's a stronger one to make
   publicly because it's falsifiable and held up under a search built to falsify it.
