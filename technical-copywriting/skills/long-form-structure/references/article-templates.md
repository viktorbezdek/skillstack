# Article Templates

Six canonical templates for long-form technical content. Pick one before outlining. Each has a different shape, length, and reader contract — mixing them produces structural confusion.

## Template selection matrix

| Reader's JTBD | Best template | Avoid |
|---|---|---|
| "How does X work?" | Deep-dive | Tutorial (they don't want to *do* yet) |
| "How do I do X?" | Tutorial | Deep-dive (they don't want theory) |
| "Should I adopt X?" | Opinion or Case study | Whitepaper unless data-heavy |
| "What did your team learn?" | Case study | Opinion (the story is the point) |
| "What's the state of the field?" | Whitepaper / report | Anything shorter |
| "Tell me a memorable story" | Technical narrative | Tutorial (kills the narrative) |

## 1. Deep-dive

> "Here's how X actually works."

### Skeleton

```
1. Hook — a misconception, a surprising fact, or a moment of confusion
2. Promise — by the end you'll understand X well enough to predict / debug / decide
3. The model the reader probably has now (and where it's incomplete)
4. Layer 1 — the simplest accurate model
5. Layer 2 — what Layer 1 leaves out, and what's underneath
6. Layer 3+ — keep going as needed
7. Synthesis — putting the layers together; a worked example or surprising prediction
8. Close — implications; what this changes for the reader; further reading
```

### Length

2500-5000 words. Deep-dives shorter than 2000 are usually surveys; longer than 6000 should usually become a series.

### Pacing

Each layer ~400-700 words. Synthesis ~400-800. The hook can be short (2-3 paragraphs) but must create genuine curiosity.

### Worked example outline: "How Postgres MVCC actually works"

```
1. Hook (200 words) — A common misconception: "MVCC means readers don't block writers." True
   but incomplete; it doesn't explain why long-running transactions still hurt.
2. Promise (50 words) — By the end you'll know exactly what MVCC stores, what gets cleaned up,
   and why VACUUM is the load-bearing maintenance operation.
3. The naive model (300 words) — "Each row has a timestamp; reads see only old-enough rows."
   Why this is misleading.
4. Layer 1: tuple visibility via xmin/xmax (600 words) — actual fields stored in the heap;
   the visibility check rules.
5. Layer 2: the dead tuple problem (700 words) — UPDATE creates a new tuple, leaves the old
   one in place; reads still need to skip dead tuples; this is where bloat comes from.
6. Layer 3: VACUUM and the freeze horizon (800 words) — what VACUUM does, why xid wraparound
   matters, the autovacuum thresholds.
7. Synthesis: the long-running-transaction failure mode (500 words) — why a transaction left
   open for hours can starve VACUUM and accumulate bloat. A worked example with pgstattuple.
8. Close (200 words) — what to monitor; reading list (the docs, the source files in heapam.c).
```

Total: ~3350 words. The hook earns the 30-second commitment; the layered structure earns the 15-minute commitment.

## 2. Tutorial

> "Here's how to do X step by step."

### Skeleton

```
1. Hook — the problem this solves; what success looks like (with an artifact: screenshot, code snippet, terminal output)
2. Promise — what you'll have by the end; estimated time
3. Prerequisites — what the reader needs (versions, tools, prior knowledge)
4. Step 1 — minimal complete first step. Verify it works before moving on.
5. Step 2 — incremental addition. Verify.
6. Step 3...N — final state.
7. Common pitfalls — predictable failures and their fixes
8. What's next — extending the tutorial; production hardening; further reading
```

### Length

1500-4000 words. Tutorials shorter than 1500 are usually quickstarts; longer than 5000 should be split into multi-part series.

### Pacing

Each step gets a code/config block, an explanation, and a verification step. The reader should be able to copy-paste-run at every checkpoint.

### Tutorial-specific rules

- **Always include a "verify it works" step.** A tutorial where step 4 fails because of an undisclosed prereq from step 2 wastes the reader's time.
- **State assumed versions explicitly.** "PostgreSQL 16, Node 20, macOS or Linux." Not "recent versions of…"
- **End with a working artifact.** A tutorial that ends mid-state (with TODOs) feels like an outline, not a tutorial.
- **Avoid mid-tutorial opinion.** "I think this approach is better" interrupts the procedural flow. Save opinions for the closing or a callout.

### Worked example outline: "Adding row-level security to your PostgreSQL multi-tenant app"

```
1. Hook (150 words) — Show the failure mode: a query without RLS that returns all tenants' data.
2. Promise (50 words) — By the end you'll have a working RLS setup with policies, connection-pool
   integration, and a test harness. Estimated time: 1-2 hours.
3. Prerequisites — PostgreSQL 14+, an existing multi-tenant schema with a tenant_id column.
4. Step 1: enable RLS on a single table — minimal policy; verify a tenant can only see their rows.
5. Step 2: extend to all multi-tenant tables — script + verification.
6. Step 3: integrate with the connection pool — the SET ROLE pattern + a worked Node example.
7. Step 4: write a test — a pytest/jest harness that catches RLS bypass.
8. Common pitfalls — the connection-pool RESET ROLE trap; admin queries; performance.
9. What's next — extending to row-level UPDATE/DELETE policies; auditing.
```

## 3. Opinion

> "Here's why X is wrong / right."

### Skeleton

```
1. Hook — the conventional view, stated fairly (steelman)
2. Promise — what's wrong with the conventional view; what the better view is
3. The strongest case for the conventional view (full steelman, not strawman)
4. Where the conventional view breaks — your specific objections with evidence
5. The alternative view — your position
6. Anticipated objections — and your responses
7. Payoff — what changes if your view is right (decision implications)
8. Close — concession; what would update you; scope of the argument
```

### Length

1500-3500 words. Opinion pieces shorter than 1500 are usually hot takes; longer than 4000 risk losing the casual reader.

### Opinion-specific rules

- **Steelman before objecting.** A strawman version of the view you're attacking discredits your piece. Take the strongest version of the opposing view; refute *that*.
- **Cite the conventional view.** Link to the canonical statements of the position you're arguing against. Otherwise you're arguing with a ghost.
- **Anticipate the top three objections.** Readers will mentally generate them as they read; handle them or watch the comments do it.
- **Concede honestly.** "I might be wrong if X" earns trust. "I'm definitely right" loses it.

### Worked example outline: "Microservices were a mistake for most teams"

```
1. Hook (200 words) — The 2015-era promise of microservices, fairly stated. Independent
   deployments, polyglot, scale-to-team-size.
2. Promise (50 words) — For the median engineering team (under 50 people, single product), the
   distributed-systems cost dominated the organizational benefit. Most should have stayed
   monolith with module boundaries.
3. Steelman (500 words) — The case for microservices: why Netflix and Amazon adopted, what
   problems they actually solved, why the pattern made sense in those contexts.
4. Where it breaks (700 words) — three specific failure modes: distributed tracing complexity,
   data consistency cost, hiring requirement.
5. The alternative (500 words) — modular monolith with explicit module boundaries; clear
   patterns for splitting later when needed.
6. Objections (600 words) — "but you can't scale a monolith" / "what about polyglot" / "what
   about team independence" — addressed in turn.
7. Payoff (250 words) — what teams who buy this argument should do this quarter.
8. Close (200 words) — concession: at sufficient scale (200+ engineers), the calculus flips.
```

## 4. Case study

> "Here's what we did and what we learned."

### Skeleton

```
1. Hook — the result up front (decided outcome, surprising number, key tension)
2. Promise — what the reader will learn from this story
3. Context — your specific situation; what made this case interesting
4. The journey — what happened, in chronological order, with specific details
5. The result — measurable outcomes; before/after; what worked and didn't
6. What we'd do differently — honest retrospective
7. Generalization — what generalizes beyond your specifics
8. Close — caveats; what doesn't generalize
```

### Length

1500-4000 words. Case studies shorter than 1500 are usually anecdotes; longer than 5000 lose the through-line.

### Case-study-specific rules

- **Lead with the result.** "We cut latency 80%" up front. The journey is the development.
- **Specifics over generalities.** "We migrated 100k tests from Mocha to Vitest in 11 weeks" beats "We did a major test framework migration."
- **Honest retrospective.** A case study without a "what we got wrong" section reads as marketing. Include real mistakes.
- **Distinguish what generalizes.** Your team's specific context (size, stack, constraints) shaped the decision. Tell the reader what to copy and what not to.

## 5. Whitepaper / report

> "Here's the state of X."

### Skeleton

```
1. Executive summary — the conclusions up front (one page max)
2. Background — the question, why it matters, who this is for
3. Methodology — how the analysis was done; what's in / out of scope
4. Findings — section per finding, each with data and interpretation
5. Discussion — what the findings mean together; tradeoffs
6. Recommendations — actionable guidance derived from the findings
7. Limitations — what this report doesn't show
8. Appendices — methodology detail, raw data, references
```

### Length

5000-15000+ words. Whitepapers under 5000 are usually reports; longer than 20000 should be split into a report plus appendix volumes.

### Whitepaper-specific rules

- **Designed for non-linear reading.** A reader should be able to land on Section 4.2 from a search and get value. Heavy cross-referencing.
- **Heavy citation density.** Every load-bearing claim has a citation. Methodology section is non-negotiable.
- **Executive summary is the most-read part.** Spend disproportionate effort polishing it.
- **Limitations section is the credibility move.** Honest limits earn trust; missing limits sections suggest cover-up.

## 6. Technical narrative

> "Here's a story that teaches a lesson."

### Skeleton

```
1. Hook — the moment of crisis or discovery
2. Promise — what you'll learn from this story (often implicit)
3. Setup — the system, the team, what was normal
4. Inciting incident — what went wrong / what we noticed
5. Investigation — the clues, the false leads, the discovery
6. Resolution — how it ended
7. Lesson — what generalizes
8. Close — what we changed; what's still open
```

### Length

2000-4500 words. Narratives shorter than 2000 are anecdotes; longer than 5000 risk losing the narrative thread.

### Narrative-specific rules

- **Specific details ground the story.** Times, sizes, names, screen captures. Vague stories don't read as true.
- **Show the false leads.** A narrative where you go straight from problem to solution reads invented. Show the dead ends.
- **The lesson should be one sentence.** Long narratives that end with five different lessons dilute the impact.
- **Resist the temptation to lecture mid-narrative.** Save the analysis for the lesson section.

## Anti-templates

These are common but usually wrong:

### "X tips/tricks/things you should know"

The listicle-disguised-as-article. Almost always becomes thinner than its length; rarely synthesizes. Use only if the items genuinely don't have a synthesizing thesis (e.g., "10 useful Git aliases" is fine; "10 things you should know about microservices" is not).

### "Everything you need to know about X"

Promise inflation by definition. Pick a smaller scope or pick a different framing.

### "The complete guide to X"

Same. "The complete guide" is a marketing phrase, not a content shape.

### "X vs Y: which should you choose?"

Often the right question, but a comparison piece needs a clear methodology and decision framework — otherwise it's just two summaries glued together. If you do this, define your evaluation axes up front and score against them.

## Picking length within a template

Once template is locked:

| If… | Length lands at… |
|---|---|
| The promise has one main move | Lower bound (e.g., 1500 for tutorial) |
| The promise has two main moves | Middle (e.g., 2500-3500) |
| The promise has three+ moves or significant evidence | Upper bound (e.g., 4000-5000) |
| The promise has a primary move and significant historical context or anticipated objections | Upper bound + |

If you're hitting upper bound + and still feeling cramped, split: the article wants to be two articles, or a series.

## Template for the cross-cutting case

Sometimes a piece is genuinely cross-template (e.g., a deep-dive that includes a case study). When that happens:

1. **Pick the dominant template.** The one that drives the structure.
2. **Embed the secondary** as a section with a sub-template.
3. **Signal the embedded template** with a heading ("Case in point:" or "How this looked in practice:").
4. **Don't switch midway** — once you're in the deep-dive frame, the reader expects deep-dive shape.

## Template debt

Most existing articles fail because they were drafted without a template choice. Symptoms:

- Sections that don't share a logical relationship.
- A hook that promises one thing and a body that delivers another.
- Length that doesn't match scope.
- Pacing that's uneven across sections.

Fix in revision: identify the actual template the piece is closest to, restructure to fit, cut what doesn't belong.
