# Technical Copywriting

> **v1.0.0** | Long-form technical content | 5 skills

---

## The Problem

Technical writing for an audience — blog posts, tutorials, deep-dives, newsletters, whitepapers, technical essays — is a different discipline from the technical writing most engineers have practiced. Code docs explain something the reader has already chosen to use. Long-form technical content has to *earn* the reader's attention, hold it across thousands of words, and leave them with an idea they can use.

Most technical articles fail in predictable ways:

- **Buried thesis.** The interesting claim is in paragraph nine. The reader leaves at paragraph two.
- **Asserted authority.** The piece claims expertise instead of demonstrating it.
- **Generic prose.** Every sentence could have been written by anyone about anything.
- **Unsourced claims.** "Studies show…" with no study cited; benchmarks with no methodology.
- **Listicle disease.** Five disconnected tips presented as a structured argument.
- **No hook.** The article opens with "In today's fast-paced digital landscape…" and the reader is gone.
- **Weak titles.** A piece worth reading dies because the title gives the reader no reason to click.

These failures are well-studied. Copywriters have spent a century cataloging what works: hooks, promise-payoff contracts, AIDA, PAS, Bencivenga's pyramid, Sugarman's slippery slide, Schwartz's awareness levels, the inverted pyramid, the read-aloud test, the 30% cut. The techniques are proven; most technical writers have never been taught them.

## The Solution

The technical-copywriting plugin gives Claude five composable skills, each scoped to one phase of the long-form workflow:

1. **technical-research** — Research before craft. Profile the audience, tier the sources, triangulate facts across three sources before citing, manage evidence types (data, expert quotes, demonstrations, case studies), and apply citation discipline so claims survive scrutiny.

2. **long-form-structure** — Structure the piece around the hook → promise → payoff contract. Pick the right template (deep-dive, tutorial, opinion, case study, whitepaper, technical narrative). Engineer transitions that pull the reader from section to section. Match length to ambition.

3. **engaging-craft** — Apply proven copywriting formulas (AIDA, PAS, BAB, Bencivenga's pyramid, Sugarman's slippery slide) to technical content. Engineer hooks. Tune voice and tonality. Replace abstract claims with concrete examples. Build callbacks that reward the careful reader.

4. **long-form-polish** — The polish phase that's distinct from line-level clarity editing. Manage pacing and rhythm. Engineer scan-ability for the skim reader without abandoning the deep reader. Apply the 30% cut. Read aloud to find every bump.

5. **distribution-craft** — The article doesn't end at the last paragraph. Engineer titles that survive a noisy feed. Write deks and meta descriptions that get the click. Pull social quotes that travel. Reframe for each channel (X/LinkedIn/HN/Reddit/newsletter) without writing five articles.

## Why these five

Each skill maps to a phase of the workflow that has its own techniques, anti-patterns, and craft tradition:

| Phase | Skill | What it produces |
|---|---|---|
| **Pre-writing** | technical-research | A research brief: audience, sources, evidence inventory, claim-evidence map |
| **Architecture** | long-form-structure | An outline with hook, promise, sections, payoff |
| **Drafting** | engaging-craft | A draft that holds attention from sentence to sentence |
| **Revision** | long-form-polish | A polished piece that scans cleanly and reads aloud well |
| **Launch** | distribution-craft | A title, dek, social pulls, and channel-specific frames |

## Installation

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install technical-copywriting@skillstack
```

## Usage

Each skill auto-activates on relevant queries. Common patterns:

- "Research and outline a deep-dive on incremental adoption of strict mode" → activates `technical-research` then `long-form-structure`
- "Make this article more engaging" → activates `engaging-craft`
- "Polish this draft for pacing and scan-ability" → activates `long-form-polish`
- "Suggest titles and a dek for this piece" → activates `distribution-craft`

You can also chain them explicitly: research → structure → craft → polish → distribute.

## What this plugin is NOT

- **NOT for code documentation, READMEs, or API references** — use `documentation-generator`.
- **NOT for UX microcopy** (button labels, error messages) — use `ux-writing`.
- **NOT for short-form work writing** (RFCs, ADRs, design docs, emails) — use `communication` (especially `structured-writing` and `clarity-editing`).
- **NOT for fiction or narrative craft** — use `storytelling` (the storytelling plugin explicitly defers technical content here).
- **NOT for CMS content models or information architecture** — use `content-modelling`.
- **NOT for interface text or onboarding copy** — use `ux-writing`.

The five skills inside this plugin are also clearly bounded — see each `SKILL.md` for its `NOT for` clause.

## Conventions

The plugin follows the skill-foundry house style:

- Each skill description includes a literal `NOT for` clause for activation discipline.
- Every skill has an anti-patterns block.
- Every skill has both `✅ Use for:` and `❌ NOT for:` lists in the body.
- References are progressive — `SKILL.md` is the entry point; reference files cover one topic each.

## Author

Viktor Bezdek — https://github.com/viktorbezdek

## License

MIT.
