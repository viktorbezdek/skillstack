---
name: content-platform-build
description: Layering workflow for building a knowledge base, CMS, documentation site, or structured content platform from scratch. Builds the data model first (content-modelling), adds a formal knowledge-graph layer if needed (ontology-design), establishes naming and taxonomy conventions (consistency-standards), designs information architecture (navigation-design), fine-tunes voice and microcopy (ux-writing), fills the structure with examples (example-design), and adds tooling for scale (documentation-generator). Use when starting a content or docs system from scratch, migrating one to a structured model, or rescuing one that has drifted into inconsistency. NOT for small single-page docs — use documentation-generator alone.
---

# Content Platform Build

> Content platforms fail when teams skip the layers. You cannot design navigation for a content schema you haven't defined. You cannot enforce consistency on terminology that isn't named. You cannot produce examples for a structure that doesn't exist yet. This workflow enforces the order.

The layering is load-bearing. Each layer depends on the one below it. Trying to do `navigation-design` before `content-modelling` is backwards — you'd be designing navigation for a schema nobody agreed on. Similarly, adding `consistency-standards` after the content is already written produces a retrofit, not a standard.

---

## When to use this workflow

- Starting a new documentation site, knowledge base, or CMS from scratch
- Migrating ad-hoc content (wiki pages, scattered markdown) into a structured system
- Rescuing a content platform that has drifted into inconsistency
- Building a customer-facing help center or developer docs site
- Structuring internal company knowledge (handbook, wiki, playbooks)

## When NOT to use this workflow

- **Single-page README or short docs** — use `documentation-generator` alone
- **One-off blog posts or articles** — use `storytelling` for narrative and `ux-writing` for polish
- **Code comments and inline docs** — different discipline, use language-specific skill
- **Marketing copy for a landing page** — use `storytelling` + `ux-writing`

---

## Prerequisites

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install content-modelling@skillstack
/plugin install ontology-design@skillstack
/plugin install consistency-standards@skillstack
/plugin install navigation-design@skillstack
/plugin install ux-writing@skillstack
/plugin install example-design@skillstack
/plugin install documentation-generator@skillstack
```

---

## Core principle

**Structure precedes style.** Every layer in this workflow depends on the layer below it being done first. Working out of order produces content that looks right but doesn't scale, or scales but doesn't feel right. The symptoms of inverted order (shipping without content-modelling first) show up as: duplicated information, contradictory terminology, fragile navigation, and content that can't be reused across channels.

Secondary principle: **build the container before filling it.** Do not write a single piece of content until the data model, conventions, and navigation are defined. Teams that start writing too early have to rewrite everything when the structure is finalized.

---

## The layers (build strictly bottom-up)

### Layer 1 — content model (content-modelling)

Load the `content-modelling` skill.

Answer these before anything else:

- **What content types exist?** ("Article" is not a content type. "Tutorial", "API reference", "Conceptual overview", "Release note" are content types.) Each type has a different audience, different fields, and different lifecycle.
- **What fields does each type have?** Title, body, and metadata isn't enough. What structured fields do users need to filter, sort, or display differently across channels? ("Difficulty level", "Applies to version", "Author", "Last verified date".)
- **What relationships exist between types?** A tutorial references concepts. A release note references features. A troubleshooting article references error codes. Relationships are load-bearing for navigation and for reuse.
- **What's the lifecycle?** Draft → review → published → updated → archived. Each transition needs metadata and often governance.
- **COPE (Create Once, Publish Everywhere)** — can this model serve multiple channels (docs site, marketing, in-product help)? The cost of a bad model is writing the same content three times; the cost of a good model is restructuring once.

Output: a written content model document with types, fields, relationships, and lifecycles. Not a database schema (that's the implementation); a content model (that's the contract).

### Layer 2 — ontology (ontology-design) — only if needed

Load the `ontology-design` skill if your content needs a formal knowledge graph. Most content platforms do not. You need this layer when:

- Content is highly interlinked and users navigate by concept, not by document (Wikipedia, academic references)
- You plan to generate content dynamically from structured relationships
- You want semantic search that understands "product X is a type of Y" vs full-text match
- You're modeling a knowledge domain where the relationships themselves are the point (medical knowledge, legal knowledge)

If you don't need any of these, skip Layer 2 and move to Layer 3. Adding ontology you don't need adds complexity without payoff.

If you do need it, build:
- **Classes and hierarchies** — the types and their subtype relationships
- **Properties** — relationships between classes (has-part, is-a, derives-from, implements)
- **Taxonomies** — controlled vocabularies for values
- **Constraints** — cardinality, required properties

Output: a formal model document (OWL, RDF, or just a structured markdown specification).

### Layer 3 — consistency standards (consistency-standards)

Load the `consistency-standards` skill.

Now that you have types and (maybe) an ontology, establish the naming and style rules that will govern the content:

- **Terminology** — the one canonical term for each concept. "User" vs "account" vs "customer" — pick one per concept and enforce. Most platforms drift into three synonymous terms for everything, making search useless.
- **Naming conventions** — for content types (e.g., tutorials named as imperative verbs, references named as nouns, how-tos named as "How to ___")
- **Voice and tone** — formal or casual, second-person or third, active or passive. Pick one and write it down.
- **Style guide basics** — sentence case or title case in headings, Oxford commas, code formatting, abbreviations
- **Reuse rules** — when content appears in multiple places (marketing + docs), which is the source of truth? What's the propagation mechanism?

Output: a style guide document that's short enough to actually read (one page is the target, two pages is the limit) and specific enough to enforce.

### Layer 4 — information architecture (navigation-design)

Load the `navigation-design` skill.

NOW you can design how users move through the content. Notice: you cannot do this before Layer 1. If you design navigation before you know the content types, you'll design navigation for content that won't exist, and it will break when content arrives.

Apply:
- **Card-sort style grouping** — not by content type, but by user task. "Getting started", "How do I do X", "Reference", "Troubleshooting". The grouping reflects how users think, not how content is stored.
- **Breadcrumbs and location awareness** — users should always know where they are in the structure
- **Search as navigation** — for platforms above ~200 pages, search is the primary navigation; design it as a first-class feature
- **Pagination and sequencing** — for linear content (tutorials, courses), the "next" and "previous" are navigation, not decoration
- **Anti-patterns to check for**:
  - Deep hierarchies (>3 levels) that hide content
  - Homepage that's a table of contents instead of a wayfinding tool
  - Search that returns documents but not fragments
  - Cross-links broken when content moves

Output: sitemap, navigation pattern spec, and header/sidebar wireframe.

### Layer 5 — voice and microcopy (ux-writing)

Load the `ux-writing` skill.

The navigation shells, the labels, the error messages, the empty states — these need deliberate writing separate from the body content. Good body content can still fail if the UI copy around it is bad.

Apply:
- **Labels must be actions, not categories** — "Install the SDK" not "SDK"
- **Empty states** — every empty state is an opportunity to teach the user what should go there
- **Error messages** — specific, actionable, not blaming ("Could not save: your session has expired. Click here to sign in again.")
- **Button verbs** — the button label should tell the user exactly what will happen, not just "OK" or "Submit"
- **Metadata visibility** — author, date, version — presented cleanly, not as clutter

Output: UI copy specification matching the navigation structure from Layer 4.

### Layer 6 — examples (example-design)

Load the `example-design` skill.

Only now do you start producing actual content — starting with examples, because examples are the most-read content type and the most-error-prone.

Apply:
- **Progressive complexity** — start with a minimal example, build up. Don't start with "advanced production-ready".
- **Runnable, copy-pasteable** — every code example should work if copied. If it requires setup, the setup is part of the example.
- **One concept per example** — don't demonstrate five things in one snippet
- **Narrative examples** — walk through why, not just what
- **Anti-pattern examples** — sometimes showing what NOT to do is the most effective example

Output: a catalog of examples matching the content model from Layer 1, following the style from Layer 3, fitting into the navigation from Layer 4.

### Layer 7 — tooling and scale (documentation-generator)

Load the `documentation-generator` skill.

With the structure in place and seeded with examples, add the tooling that will let the content grow without drift:

- **Linter** — enforces the style guide from Layer 3 automatically
- **Link checker** — breaks when links break, before users find them
- **Deploy pipeline** — every commit builds and validates
- **Content generation** — where structured data exists (API schemas, config schemas), generate docs automatically
- **Translation pipeline** — if multi-language, structure before translation, not after
- **Analytics** — which content is read, which is searched-for-and-not-found, which has users bouncing

Output: running tooling that continuously validates the platform against its own rules.

---

## Gates and failure modes

**Gate 1: the model gate.** Layer 3 cannot start until Layer 1's content model is written down and at least informally agreed on. Working on naming conventions for types that don't exist is theater.

**Gate 2: the navigation gate.** Layer 4 cannot start until Layers 1 and 3 are both done. Designing navigation without a content model and without terminology produces navigation you'll redo.

**Gate 3: the content gate.** Layer 6 cannot start until Layers 1-5 are done. Writing content before the structure is stable means rewriting everything later.

**Failure mode: starting with Layer 4.** The most common failure. Someone wireframes the nav first because it's concrete, then backfills the content model to match. Result: a navigation that shapes the content instead of the other way around. Mitigation: strict layer order.

**Failure mode: skipping Layer 3.** Teams assume consistency will emerge. It doesn't. Six months later the platform has three terms for "user" and the search is useless. Mitigation: make Layer 3 a non-negotiable layer, not an optional one.

**Failure mode: adding Layer 2 unnecessarily.** Teams read about ontologies and decide they need one. They spend months modeling, then ship a docs site that never uses the ontology for anything. Mitigation: Layer 2's explicit "do you actually need this?" check. Most platforms don't.

**Failure mode: Layer 6 before Layer 7.** Writing 200 examples before the linting/tooling exists means 200 examples with drifting style, broken links, and un-validated code. Mitigation: Layer 7 before scaling content production.

**Failure mode: layer shortcut for speed.** "We'll fix the content model later once we have something shipped." You will not fix it later. The content written without a model becomes the de facto model, and it will be worse than a model designed up front. Mitigation: the workflow exists to prevent exactly this shortcut.

---

## Output artifacts

A completed platform build produces:

1. **Content model document** — types, fields, relationships, lifecycles
2. **Ontology** (if applicable) — formal model
3. **Style guide** — one-page terminology, voice, naming conventions
4. **Sitemap and navigation spec** — information architecture
5. **UI copy specification** — labels, buttons, errors, empty states
6. **Example catalog** — seed content following the model
7. **Tooling suite** — linter, link checker, deploy pipeline, analytics
8. **Contributor guide** — how the team will keep the standards as the platform grows

---

## Related workflows and skills

- For the individual pages within the platform, use the `storytelling` skill's `business-storytelling` or `data-storytelling` references
- For technical writing specifics (code examples, API references), use `documentation-generator` and `example-design` directly
- For UX of the platform interface (search, onboarding, empty states), use `ux-writing`
- For long-form guides and narrative documentation, use `storytelling` for the narrative structure

---

> *Workflow part of [skillstack-workflows](../../../README.md) by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
