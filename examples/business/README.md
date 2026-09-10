# Demo — Business: end-to-end company analysis

**Prompt**

> Run a full strategic analysis of Abridge, the ambient clinical documentation company.
> I'm evaluating whether to compete with them.

**Which skill fires:** `company-deep-dive` (matches "full strategic analysis of [company]")

**Chain it orchestrates**

| Phase | Skill invoked | Produces |
|---|---|---|
| 1 | `field-understanding` | 8 grounding outputs: submarket, value chain, suppliers, buyers, competitive structure, substitution threats, commoditization line, named competitors |
| 2 | `ai-product-forces-and-powers` Part I | Porter's Five Forces, each citing a Phase 1 output |
| 3 | `business-model-canvas` | 9 blocks + coherence check |
| 4 | *(inline)* | Competitive landscape: tiers, rival mini-canvases, binding competitor |
| 5 | `ai-product-forces-and-powers` Part II | 7 Powers vs. named rivals; power stack; critical vulnerability |
| 6 | *(inline)* | Financial reality check |
| 7 | *(inline)* | Integrated verdict |
| — | `sl` (optional) | Iterative research loop when evidence is thin or contested |

**What to check in the output**
- [ ] Every Porter force cites a specific Phase 1 output, not a generic claim
- [ ] Every one of the 7 Powers is rated *against named competitors*, never an abstraction
- [ ] A single **critical vulnerability** is named, with the competitor positioned to exploit it
- [ ] An **evidence cutoff date** appears (strategic analysis ages fast)

**Expected shape:** Parts 0–7, roughly 3,000–5,000 words, tables in Parts 2–5.
