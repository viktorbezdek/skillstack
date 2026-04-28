---
name: long-form-structure
description: >-
  Structure long-form technical articles around the hook → promise → setup →
  development → payoff contract. Pick from canonical templates (deep-dive,
  tutorial, opinion, case study, whitepaper, technical narrative). Engineer
  section transitions and signposting. Match length to ambition (when 800 vs
  1500 vs 3000 vs 5000+ words is right). Use when the user asks to outline
  a technical article, structure a deep-dive, plan a tutorial, organize a
  whitepaper, pick an article template, fix pacing across sections, or audit
  the structure of an existing draft. NOT for short-form work writing like
  RFCs or memos (use communication/structured-writing — BLUF, Pyramid). NOT
  for line-level editing or pacing within paragraphs (use long-form-polish).
  NOT for fiction or character-driven story arcs (use storytelling). NOT for
  research, sourcing, or citation (use technical-research).
---

# Long-form Structure

> A long-form article is a contract: the hook promises something, the structure delivers it, the payoff makes the contract feel honored. Most failed articles either don't promise enough to be worth reading, or promise more than they deliver.

Long-form technical content (1500-5000+ words) lives or dies on structure. Short writing tolerates loose structure because the reader's commitment is small. Long writing has to earn every additional minute of attention. Structure is how you do that.

This skill covers article-level architecture: the contract, the templates, the transitions, the length decisions.

## Core principle

**Hook makes a promise. Structure delivers it. Payoff makes it feel honored.**

Every section should advance the promise. If a section doesn't, it's tax — cut it or move it. The reader gives you their attention conditionally; the structure is what spends it well.

## The hook → promise → payoff contract

Every long-form piece is built around a contract:

| Element | Job | Length |
|---|---|---|
| **Hook** | Catch attention; create a question | 1-3 paragraphs |
| **Promise** | State what the reader will get | 1 paragraph (often blends with hook) |
| **Setup** | Common ground, definitions, scope | 5-15% of article |
| **Development** | The argument / tutorial / story unfolds | 60-75% of article |
| **Payoff** | The promised insight / capability / shift | The last 10-15% |
| **Close** | What changes for the reader; what to do next | 1-3 paragraphs |

The hook and promise create tension; the development sustains it; the payoff resolves it. A piece without a clear promise feels meandering. A piece without a payoff feels deflating. A piece whose payoff doesn't match the promise feels like a bait-and-switch.

See `references/hook-promise-payoff.md` for full templates and worked examples of each.

## Six canonical article templates

Most long-form technical articles fit one of six templates. Pick the template before outlining; mixing templates produces structural confusion.

### 1. Deep-dive ("Here's how X actually works")

**For:** Conceptual explainers; demystifying a system, protocol, or pattern.
**Skeleton:**

```
1. Hook — a misconception or surprising fact about X
2. Promise — by the end you'll understand X well enough to [predict/debug/decide]
3. Setup — the model the reader probably has now, and why it's incomplete
4. Layer 1 — the simplest accurate model
5. Layer 2 — what that model leaves out, and the next layer down
6. Layer 3+ — additional layers as needed
7. Payoff — putting the layers together; a worked example or surprising prediction
8. Close — implications; further reading
```

**Length:** 2500-5000 words.
**Example:** "How Postgres MVCC really works" or "What actually happens during a Kubernetes pod restart."

### 2. Tutorial ("Here's how to do X step by step")

**For:** Implementation guides; teaching a procedure.
**Skeleton:**

```
1. Hook — the problem this solves; what success looks like
2. Promise — by the end you'll have a working [thing]; estimated time
3. Prerequisites — what the reader needs to have/know before starting
4. Step 1 — minimal complete first step; verify it works
5. Step 2 — incremental addition; verify
6. Step N — final state
7. Common pitfalls — the predictable failures and their fixes
8. What's next — extending the tutorial; production hardening
```

**Length:** 1500-4000 words.
**Example:** "Adding row-level security to your PostgreSQL multi-tenant app" or "Building a Rust CLI from zero to ship."

### 3. Opinion ("Here's why X is wrong / right")

**For:** Argument; advocacy; reframing accepted wisdom.
**Skeleton:**

```
1. Hook — the conventional view, stated fairly
2. Promise — what's wrong with the conventional view; what the better view is
3. Strongest case for the conventional view — steelman
4. Where the conventional view breaks — your specific objections
5. The alternative view — your position
6. Anticipated objections — and your responses
7. Payoff — what changes if your view is right
8. Close — concession, scope, what you'd update if shown wrong
```

**Length:** 1500-3500 words.
**Example:** "Microservices were a mistake for most teams" or "The 100% test coverage cult."

### 4. Case study ("Here's what we did and what we learned")

**For:** Sharing experience; illustrating a pattern through one specific instance.
**Skeleton:**

```
1. Hook — the result up front (decided outcome, surprising number, key tension)
2. Promise — what the reader will learn from your specific story
3. Context — your situation, constraints, what made this case interesting
4. The decision/event/journey — what happened, in chronological order
5. The result — measurable outcomes
6. What we'd do differently — honest retrospective
7. Generalization — what the reader can take from this beyond your specifics
8. Close — caveats; what doesn't generalize
```

**Length:** 1500-4000 words.
**Example:** "How we cut latency by 80% by removing a service" or "Migrating 100k tests from Mocha to Vitest in two weeks."

### 5. Whitepaper / report ("Here's the state of X")

**For:** Survey; reference; rigorous analysis with data.
**Skeleton:**

```
1. Executive summary — the conclusions up front (one page)
2. Background — the question, why it matters, who this is for
3. Methodology — how the analysis was done; what's in/out of scope
4. Findings — section per finding, each with data and interpretation
5. Discussion — what the findings mean together; tradeoffs
6. Recommendations — actionable guidance derived from the findings
7. Limitations — what this report doesn't show
8. Appendices — methodology detail, raw data, references
```

**Length:** 5000-15000+ words; designed for sections to be read in any order.
**Example:** "State of Open Source 2024" or "A reference architecture for multi-region failover."

### 6. Technical narrative ("Here's a story that teaches a lesson")

**For:** Memorable lessons; war stories; investigations.
**Skeleton:**

```
1. Hook — the moment of crisis or discovery
2. Promise — what you'll learn from the story
3. Setup — the system, the team, what was normal
4. Inciting incident — what went wrong / what we noticed
5. Investigation — clues, false leads, the discovery
6. Resolution — how it ended
7. Lesson — what generalizes
8. Close — what we changed; what's still open
```

**Length:** 2000-4500 words.
**Example:** "The day our database stopped accepting writes" or "How a one-line change took down our pipeline for three days."

See `references/article-templates.md` for full skeletons with inline notes, length guidance, and which template fits which JTBD.

## Length strategy

Length is a decision, not a discovery. Pick the length before drafting:

| Length | Best for | Risk if wrong |
|---|---|---|
| **800-1500 (short)** | Single point, clear takeaway, one example | Reads as "should have been a tweet" |
| **1500-3000 (mid)** | One argument with two or three supporting moves; tutorial covering one workflow | Reads as bloated short or thin long |
| **3000-5000 (deep-dive)** | Multi-layered explanation; case study with retro; opinion with anticipated objections | Loses the casual reader |
| **5000-10000 (long-form)** | Whitepaper; comprehensive tutorial; investigation with full evidence | Becomes a slog if not earning every section |
| **10000+ (chapter-length)** | Reference document; multi-part series in one file | Almost always should be split |

If a piece *wants* to be 1500 words, forcing it to 4000 produces filler. If it wants to be 4000, cutting to 1500 loses the substance. Match length to scope; resist length inflation as a marker of effort.

See `references/length-strategy.md` for the full decision matrix.

## Section transitions

A long article fails if the reader doesn't make it from section to section. The transition is the bridge.

### Three transition patterns

1. **Question-pull.** End a section with a question the next section answers.
   > "But how does this hold up under load? Let's measure."

2. **Foreshadowing.** Set up a tension that resolves in a later section.
   > "We'll see in Section 4 why this innocent-looking line caused the outage."

3. **Logical bridge.** Restate the just-finished claim as the premise for the next.
   > "Given that the cache eviction is LRU, the next question is when entries become eligible for eviction."

### Common transition failures

- **Topic-jump.** Section ends, next section starts a new topic with no bridge.
- **Repetitive transitions.** Every section ends with "Let's look at…" — the reader notices.
- **Recap inflation.** Each section recaps the previous, padding length without earning it.

See `references/section-transitions.md` for the transition library and worked examples.

## Signposting and scaffolding

Long-form readers need to know where they are. Signposts help them.

| Signpost | When |
|---|---|
| **Section headings** | Every 200-500 words |
| **Sub-headings** | When a section has 3+ logical parts |
| **Numbered lists** | When order matters (steps, ranking) |
| **Bulleted lists** | When order doesn't matter (parallel options) |
| **Tables** | When comparing 2+ items across 2+ dimensions |
| **Callout boxes** | For tangential content the reader can skip |
| **TL;DR / executive summary** | Long-form (3000+ words) earning patience up front |
| **"In this article you'll learn…"** | Tutorial format only; clichéd elsewhere |

Don't over-signpost — a 2000-word piece with 12 H2 headings reads choppy. Let the prose do work where it can.

## ✅ Use for

- Outlining a new long-form technical article
- Picking the right template (deep-dive vs tutorial vs opinion etc.)
- Auditing the structure of an existing draft
- Fixing pacing problems across sections (too long, too uneven, weak transitions)
- Deciding length before drafting
- Engineering hook-promise-payoff contracts

## ❌ NOT for

- **Short-form work writing** (RFCs, memos, design docs) — use communication/structured-writing (BLUF, Pyramid)
- **Line-level editing or paragraph pacing** — use long-form-polish
- **Fiction structure / character arcs** — use storytelling
- **Research and sourcing** — use technical-research
- **Hook *language*** (sentence-level craft) — use engaging-craft

## Anti-patterns

### Promise inflation

**What it looks like:** A title and opening that promise "the definitive guide to X" — followed by 1500 words covering one corner of X.

**Why it's wrong:** The reader feels misled. Trust is spent in the first 30 seconds and never recovered.

**What to do instead:** Promise what you can deliver. "How we shaved 80ms off our P99" beats "The complete guide to performance optimization" if the article is about one specific 80ms.

### Buried thesis

**What it looks like:** The interesting claim arrives in paragraph 9. The reader leaves at paragraph 2.

**Why it's wrong:** Long-form readers are still skim-readers. They scan the first 200 words, the first sentences of each paragraph, and the closing — to decide whether to commit to the rest. If the interesting claim isn't visible in that scan, the article doesn't earn the read.

**What to do instead:** State the thesis early. The development can build the case; the thesis itself shouldn't hide. (This is *not* the same as opinion-cliché "spoiling" — see the deep-dive template, which leads with the surprising fact.)

### Listicle disease

**What it looks like:** "10 things you should know about X" — ten loosely connected sub-points presented as if they were a structured argument.

**Why it's wrong:** A listicle is a structure of last resort. It signals to the reader that you didn't synthesize — you stacked. The reader leaves with ten weak claims instead of one strong one.

**What to do instead:** If you have ten points, find the synthesizing thesis they support, and present them as evidence for the thesis. If you can't find a synthesizing thesis, you have a tweet thread, not an article.

### Genre-mixing

**What it looks like:** A tutorial that morphs into an opinion piece halfway through. A case study that suddenly becomes a whitepaper.

**Why it's wrong:** Each template sets reader expectations. Mid-article genre shift breaks the contract.

**What to do instead:** Pick one template. If you have a tutorial that needs to make an opinion-y point, embed it as a side note ("opinionated take:") so the genre stays clear. If the opinion is the actual thesis, restructure as opinion with the tutorial as supporting evidence.

### Recap padding

**What it looks like:** Each section opens with "as we saw in the previous section…" and recaps for 100 words before adding new material.

**Why it's wrong:** Inflates length without earning it. Talks down to the reader. Breaks the pacing.

**What to do instead:** Trust the reader to remember what they read 30 seconds ago. Use callbacks ("recall the LRU eviction") rather than recaps when continuity matters.

### Section bloat

**What it looks like:** Sections that go 1500 words deep on a sub-point, while the rest of the article is 500-word sections.

**Why it's wrong:** The bloated section dominates the article without being labeled as the centerpiece. The reader's pace breaks.

**What to do instead:** Either make the bloated section the article's centerpiece (and trim other sections to support it) or split the bloated section into two or three sections with their own H2 headings.

## Workflow

Use this order when structuring a new piece:

1. **Confirm the audience profile** — from technical-research.
2. **Pick the template** — one of the six.
3. **State the promise in one sentence.** If you can't, the article isn't focused enough.
4. **Sketch the payoff.** What does the reader leave with? Knowledge? A capability? A reframing? An action?
5. **List sections.** Each must move the promise toward the payoff. Aim for 5-9 sections.
6. **Pick the length.** Based on template and depth needed.
7. **Draft the hook.** First 50-100 words; gets you started.
8. **Engineer one transition per section pair.** Question-pull, foreshadow, or logical bridge.
9. **Self-test the outline:** can you defend each section's role? Cut what you can't defend.
10. **Hand off to engaging-craft** for sentence-level work.

## References

| File | Contents |
|---|---|
| `references/article-templates.md` | All six templates with full skeletons, length guidance, JTBD mapping, and worked examples |
| `references/hook-promise-payoff.md` | The hook-promise-payoff contract with templates for each kind of hook and payoff |
| `references/section-transitions.md` | Transition library — question-pull, foreshadow, logical bridge — with worked examples |
| `references/length-strategy.md` | Length decision matrix, length-by-template guidance, when to split, when to expand |

## Related skills

- **technical-research** — research before structure; the structure depends on what evidence you have.
- **engaging-craft** — sentence-level work after the structure is right.
- **long-form-polish** — pacing within paragraphs and across sections after the draft exists.
- **distribution-craft** — title and dek depend on the structure (especially the hook and promise).
- **storytelling** (skillstack) — narrative arcs for non-technical pieces.
- **communication/structured-writing** (skillstack) — short-form structure (BLUF, Pyramid) for memos and emails.
