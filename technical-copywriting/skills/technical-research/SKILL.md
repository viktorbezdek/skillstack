---
name: technical-research
description: >-
  Research before craft for long-form technical content. Profile the audience
  (knowledge level, jobs-to-be-done, prior beliefs), tier sources (primary >
  peer-reviewed > authoritative > popular > vendor), triangulate every load-
  bearing claim across three sources, manage evidence types (data, expert
  quotes, demonstrations, case studies, source code), and apply citation
  discipline (when, how, link-rot mitigation, footnote vs inline). Use when
  the user asks to research a technical article, profile an audience, find
  sources for a deep-dive, fact-check a draft, build a claim-evidence map,
  or audit citations. NOT for code documentation research (use documentation-
  generator). NOT for line-level editing (use long-form-polish or
  communication/clarity-editing). NOT for the article structure itself (use
  long-form-structure). NOT for UX research or persona definition for
  product (use persona-definition).
---

# Technical Research

> A claim without a source is a guess. Three sources that copy each other are still one source. The most expensive sentence in a technical article is the one that turns out to be wrong.

The research phase is where most technical articles win or lose. Drafts written from a thin research base produce the same telltale prose: hedged claims, vague benchmarks, "studies show" with no study, anecdotes presented as evidence. Drafts written from a strong research base produce the opposite: specific numbers, named sources, claims the reader can check.

This skill covers the pre-writing research workflow: who you're writing for, where the evidence comes from, how to verify it, and how to cite it.

## Core principle

**Triangulate before you cite. Specific before you generalize. Primary before secondary.**

The discipline is asymmetric: it's cheap to verify a fact and expensive to retract one. A single wrong number in paragraph two costs the entire article's credibility. Spend the time upfront.

## Five research moves

### 1. Profile the audience

Before researching the topic, profile the reader. The same article on "incremental adoption of TypeScript strict mode" reads differently for:

- A staff engineer at a 500-person company evaluating the migration
- A solo developer maintaining a 3-year-old side project
- A platform team writing internal guidance

Audience determines what counts as common ground (skip), what needs explanation (cover briefly), and what's the actual contribution (the core).

Profile across three axes:

| Axis | Question |
|---|---|
| **Knowledge level** | What does the reader already know? What's "obvious" to them and what's "new"? |
| **Job-to-be-done** | Why are they reading? Decision support, implementation guide, conceptual model, entertainment? |
| **Prior beliefs** | What do they currently believe about this topic — and what does this article challenge or reinforce? |

A piece that gets the audience profile wrong is unsalvageable in revision. Get it right before you outline.

See `references/audience-profiling.md` for templates and worked examples.

### 2. Tier the sources

Not every source is equal. Use a strict tier hierarchy and prefer the highest tier you can find:

| Tier | Source type | Examples |
|---|---|---|
| **Tier 0 — Primary** | The thing itself | Source code, RFCs, specifications, raw data, the API you're benchmarking |
| **Tier 1 — Peer-reviewed** | Published research | ACM, IEEE, USENIX, peer-reviewed journals |
| **Tier 2 — Authoritative practitioner** | Named expert with reputation at stake | Engineering blogs from companies, named individuals with track records, conference talks with archived video |
| **Tier 3 — Quality popular** | Reputable publication, no peer review | NYT/FT/The Atlantic technology coverage, well-known tech publications with editorial standards |
| **Tier 4 — Anonymous popular** | No accountability | Reddit comments, anonymous blog posts, "I heard that…" |
| **Tier 5 — Vendor / advocacy** | Selling something | Vendor whitepapers, product blogs, sponsored content |

Rules:

- **Cite the highest tier available.** If a Tier 4 blog post and a Tier 1 paper both make the same claim, cite the paper.
- **Tier 5 is a last resort.** Vendor sources can be used for "X claims Y" but never as the sole source for a load-bearing claim.
- **Translate down.** When citing a Tier 1 paper, also link to a Tier 2/3 explainer if one exists — the reader can choose their depth.

See `references/source-tiering.md` for the full hierarchy with examples and edge cases.

### 3. Triangulate load-bearing claims

A *load-bearing claim* is one your argument depends on. If it's wrong, the article falls down.

For every load-bearing claim, find **three independent sources** that confirm it. "Independent" is the hard part:

- Three blog posts that cite the same StackOverflow answer = one source.
- A primary paper, an independent benchmark, and an experiment you ran yourself = three sources.
- The vendor's docs, the vendor's blog, and the vendor's CEO's tweet = one source.

If you can't find three independent sources for a load-bearing claim, either weaken the claim, run your own experiment, or cut it. Don't stretch a single source into a confident-sounding sentence.

See `references/triangulation-and-fact-checking.md` for the full method, the "independence test," and what to do when sources disagree.

### 4. Inventory evidence types

A persuasive technical article uses a *mix* of evidence, not just one type. Build an inventory before you outline:

| Evidence type | Best for | Failure mode |
|---|---|---|
| **Quantitative data** | Settling factual disputes; demonstrating scale | Numbers without methodology |
| **Expert quotes** | Establishing authority; introducing nuance | Quote-mining; cherry-picking |
| **Demonstrations** | Showing rather than telling; reproducible claims | Demos that work in slides only |
| **Case studies** | Showing a pattern in context; texture | One-off anecdote presented as pattern |
| **Source code** | Settling disputes about what software *actually* does | Code without commit hash or version |
| **Logical argument** | When evidence is unavailable; framing | Argument substituting for evidence |
| **Lived experience** | Texture, voice, stake | Ego in the way of insight |

The strongest articles balance two or three types. A piece that's all numbers reads cold. A piece that's all anecdote reads thin. A piece that's all logic reads detached.

See `references/evidence-types.md` for when each type pulls weight and how to combine them.

### 5. Apply citation discipline

Citations are a contract with the reader: *I claim X, here's where you can check.*

Rules:

- **Link to the most stable URL.** Prefer DOI, archived versions, permalinks. Avoid blog posts that get edited.
- **Capture link rot up front.** Save every cited page to `archive.org` while researching. The Wayback Machine is the only thing standing between your article and broken links a year from now.
- **Inline vs footnote.** Inline links for the casual reader, footnotes for the deep reader, both for important claims.
- **Quote with context.** Never quote a sentence without surrounding context if the surrounding context changes the meaning.
- **Date the source.** "As of 2024-Q3" or version numbers — software evolves, claims age.
- **Cite specifically.** "Section 3.2 of RFC 9110" not "the HTTP spec."

See `references/citation-discipline.md` for citation formats, link-rot mitigation, and worked examples.

## ✅ Use for

- Researching a technical blog post or deep-dive before drafting
- Building a claim-evidence map for an in-progress article
- Auditing an existing draft's citations and source quality
- Profiling the audience for a piece
- Fact-checking a load-bearing claim
- Choosing between competing sources

## ❌ NOT for

- **Code documentation research** — what an API does is documentation-generator's job
- **Line-level editing** — use long-form-polish (or communication/clarity-editing for short-form)
- **The article structure itself** — use long-form-structure
- **Product personas / UX research** — use persona-definition
- **Library lookup / API examples** — use the context7 docs MCP

## Anti-patterns

### "Studies show" without a study

**What it looks like:** "Studies show that developers spend 80% of their time reading code."

**Why it's wrong:** No study cited; the reader can't verify; the number is folklore. The original Robert Martin claim is anecdotal, the 80% is a guess, and "studies" plural is a fiction.

**What to do instead:** Either cite the actual study (with link, year, methodology), weaken to "anecdotally" with attribution, or cut the claim. Never use "studies show" as a magic phrase that grants authority.

### Single-source confident claims

**What it looks like:** A 3000-word article whose central thesis rests on one Hacker News comment.

**Why it's wrong:** Single sources fail. The author of the comment may be wrong; the comment may be misread; the comment may not survive scrutiny. The article's credibility is now hostage to that one link.

**What to do instead:** Triangulate. If the claim is interesting enough to anchor an article, it's interesting enough to find three independent confirmations.

### Vendor-as-authority

**What it looks like:** "AWS is the most reliable cloud provider, with 99.999% uptime according to AWS's own status page."

**Why it's wrong:** Vendors grading themselves is not evidence. The status page is a marketing document.

**What to do instead:** Cite third-party uptime monitors (e.g., StatusGator, ThousandEyes) and academic papers on cloud reliability. Treat vendor sources as "X claims Y," never as ground truth.

### Decoration citations

**What it looks like:** Three citations after a sentence that's already obviously true. Or citations to sources that don't actually support the claim.

**Why it's wrong:** Citations are a contract with the reader. If the reader clicks and the source doesn't support the sentence, every other citation in the article becomes suspect.

**What to do instead:** Cite the load-bearing claims. Don't cite the throat-clearing. And read the source you're citing — actually read it.

### Profile-by-projection

**What it looks like:** "I'm writing this for developers" without specifying which developers, what they know, or why they're reading. Or worse, "I'm writing this for myself" — and then publishing it for an audience.

**Why it's wrong:** A vague audience produces vague writing. Every sentence has to make decisions about what to assume, and an unprofiled audience makes those decisions inconsistently.

**What to do instead:** Pick a specific reader (real person if possible) and write to them. Update the profile as the piece develops.

## Workflow

Use this order for a new long-form piece:

1. **Profile the audience.** One paragraph: who, knowledge level, job-to-be-done, prior beliefs.
2. **State the thesis.** One sentence. If you can't, you're not ready to research.
3. **List load-bearing claims.** What must be true for the thesis to hold?
4. **Find sources.** For each load-bearing claim, find Tier 0–2 sources. Triangulate.
5. **Inventory evidence.** Build a map: claim → evidence type → source → link.
6. **Identify gaps.** What can't you source? Cut the claim, run your own experiment, or weaken to "anecdotally."
7. **Archive everything.** Save cited pages to archive.org. Capture screenshots of dynamic content. Note version numbers.
8. **Hand off to long-form-structure.** With the research brief in hand, structure the piece.

Skip steps at your peril. The most common failure mode is researching as you draft — which produces drafts shaped by what's *easy* to find, not what's *true*.

## References

| File | Contents |
|---|---|
| `references/audience-profiling.md` | Audience profile templates, worked examples, knowledge-level / JTBD / prior-beliefs frameworks |
| `references/source-tiering.md` | Six-tier source hierarchy with examples, edge cases, and "translate down" patterns |
| `references/triangulation-and-fact-checking.md` | The triangulation method, the independence test, sources-disagree resolution |
| `references/citation-discipline.md` | Citation formats, link-rot mitigation, inline vs footnote, dating sources, archive.org workflow |

## Related skills

- **long-form-structure** — once research is done, structure the piece.
- **engaging-craft** — proven techniques for turning research into prose that holds attention.
- **long-form-polish** — pacing and scan-ability after the draft exists.
- **distribution-craft** — title, dek, social pulls after polish.
- **persona-definition** (skillstack) — for product personas distinct from article-audience profiles.
- **storytelling** (skillstack) — for narrative arcs distinct from technical exposition.
