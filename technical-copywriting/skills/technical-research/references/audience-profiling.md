# Audience Profiling

A long-form technical article is a contract with one specific reader. Profile that reader before you outline. Vague audiences produce vague writing — every sentence has to decide what to assume, and an unprofiled audience makes those decisions inconsistently.

## The three-axis profile

Profile across three axes. Be specific.

### Axis 1: Knowledge level

| Level | Definition | Example for "TypeScript strict mode" |
|---|---|---|
| **Stranger** | Has not encountered the topic | Knows JavaScript, has never used TypeScript |
| **Novice** | Has seen it, hasn't used it | Has read TS docs, hasn't shipped TS in production |
| **Practitioner** | Uses it daily | Ships TS code, hasn't tuned strict mode flags |
| **Expert** | Has internalized the model | Has migrated codebases, debated `strictNullChecks` defaults |
| **Author** | Has shaped the topic | Contributes to the TS compiler |

A piece written for a Practitioner that explains JS basics insults them. A piece written for a Novice that assumes Practitioner knowledge loses them. The distance between the writer's level and the reader's level determines what gets explained, what gets assumed, and what gets cut.

### Axis 2: Job-to-be-done

What is the reader trying to accomplish by reading this article? Pick one:

| JTBD | Reader's question |
|---|---|
| **Decision support** | "Should we adopt this?" |
| **Implementation guide** | "How do I do this?" |
| **Conceptual model** | "How does this actually work?" |
| **Survey / orientation** | "What's the landscape here?" |
| **Validation / confirmation** | "Am I doing this right?" |
| **Entertainment / texture** | "What's an interesting story about this?" |
| **Argument / debate** | "What's the case for X over Y?" |

A piece can serve more than one JTBD, but one is dominant. Trying to serve all of them produces a piece that serves none well.

### Axis 3: Prior beliefs

What does the reader currently believe about this topic? What is your article challenging, reinforcing, or introducing?

| Stance | Article's job |
|---|---|
| **Already convinced** | Reinforce, deepen, give them ammo |
| **Curious / undecided** | Provide a clear case, walk through tradeoffs |
| **Skeptical** | Anticipate objections, address them head-on |
| **Hostile** | Reframe, find common ground, lead with shared values |
| **Has the wrong model** | Diagnose the wrong model first, then offer the right one |

A piece that doesn't engage with the reader's existing beliefs reads like it was written for someone else. The reader's first reaction is "yes but…" — and if the article never addresses the "but," it loses them.

## The audience profile template

Fill this out before outlining:

```
Title (working): [draft title]

Reader profile
--------------
Who: [specific role, company size, context — e.g., "Staff engineer at a 200-person SaaS company evaluating
     whether to enable strict mode on a 5-year-old TS codebase"]
Knowledge level: [stranger / novice / practitioner / expert / author]
Primary JTBD: [one of the seven]
Secondary JTBD (if any): [one of the seven]
Prior beliefs: [what they believe about this topic now]
What this article changes: [what they will believe / be able to do after reading]

Common ground (skip): [things the reader already knows — don't explain these]
Need to explain (cover briefly): [things the reader may not know but aren't the core]
Core contribution (the article's reason to exist): [the thing only this article gives them]
```

## Worked example 1: a deep-dive on incremental TS strict mode adoption

```
Reader profile
--------------
Who: Tech lead at a 50-200 person company that adopted TS 2-4 years ago without strict mode and now
     has 100k-500k lines of un-stricted TS.
Knowledge level: Practitioner (ships TS daily, has read the strict mode docs, hasn't done a
     large-scale migration).
Primary JTBD: Decision support ("Should we do this? At what cost?")
Secondary JTBD: Implementation guide ("If yes, how?")
Prior beliefs: Strict mode is "the right thing to do" but the migration looks too expensive to attempt.
What this article changes: They commit to a phased migration with a defined cost and timeline.

Common ground (skip):
- What strict mode is and which flags it enables
- That `any` is a code smell
- Basic TS configuration (tsconfig)

Need to explain (cover briefly):
- Per-file overrides via `// @ts-strict-ignore` or `tsconfig.json` `include`
- The four most expensive strict mode errors to fix at scale
- Why incremental beats big-bang for this kind of migration

Core contribution (the article's reason to exist):
- A four-phase migration plan with cost estimates per phase based on a real codebase migration the
  author led, with the actual numbers (lines changed, weeks elapsed, errors found and missed).
```

This profile makes drafting decisions easy: you don't explain what `strictNullChecks` does, you do explain phased rollout strategy. Every sentence has a clear test: does this serve a Practitioner deciding whether to commit?

## Worked example 2: a tutorial on PostgreSQL row-level security

```
Reader profile
--------------
Who: Backend engineer who has used PostgreSQL for years but has never set up RLS, and is now responsible
     for adding multi-tenancy to a single-tenant app.
Knowledge level: Practitioner with PG, novice with RLS.
Primary JTBD: Implementation guide.
Secondary JTBD: Conceptual model (they want to understand RLS, not just copy a recipe).
Prior beliefs: RLS is something "enterprise apps" use; their app probably needs application-layer
     authorization instead.
What this article changes: They understand RLS as a layered defense, not an alternative, and adopt it
     alongside their existing authorization.

Common ground (skip):
- SQL syntax, basic PG admin
- The difference between authentication and authorization
- That multi-tenancy can be done at multiple layers

Need to explain (cover briefly):
- The PG `current_setting('app.current_tenant')` pattern
- How RLS interacts with connection pooling
- Why bypassing RLS on admin queries is a footgun

Core contribution:
- A complete worked example: schema with RLS policies, connection-pool integration, test harness, and
  one specific bug that almost made it to production (the connection-pool / `RESET ROLE` interaction).
```

The "almost made it to production" specific bug is the article's reason to exist. Every other tutorial covers the rest.

## Profile changes during research

Audience profiles aren't fixed — research changes them. If you discover a load-bearing claim is more contested than you thought, the profile may shift from Practitioner-deciding to Practitioner-skeptical, which changes how you handle objections.

Mark the profile as a living document. Update it after each research session.

## Common profile failures

| Failure | What it looks like | Fix |
|---|---|---|
| **"For developers"** | Knowledge level unspecified; JTBD unspecified | Pick a specific role and seniority. "For developers" is for nobody. |
| **Profile-by-projection** | Writer assumes the reader is a younger version of themselves | Test: would your profile make decisions differently than you do? If no, you're writing to a mirror. |
| **Profile too narrow** | "For staff engineers at 50-100 person Series B startups using Next.js 14 with PostgreSQL" | Hyper-specific profiles still produce decisions, but check the audience exists in numbers worth writing for. |
| **Profile too broad** | "For technical leaders" without distinguishing eng managers from staff engineers from CTOs | Pick the one whose JTBD dominates. The others can read it too, but write for one. |
| **Multiple primary JTBDs** | "This piece will help readers decide AND implement" | Pick one. The other becomes an explicit "follow-up" or a separate piece. |
| **Profile drift mid-article** | Opening assumes Practitioner; later sections assume Stranger | Audit each section against the profile after drafting. |

## When the audience really is two profiles

Sometimes a piece has to work for two audiences (e.g., a "case study" that engineers read for the technical detail and managers read for the decision). Two valid options:

1. **Pick one as primary, the other as secondary.** Write for the primary; let the secondary follow along. The piece will be slightly suboptimal for the secondary but coherent for the primary.
2. **Use callouts or sections to separate the two.** "If you're an engineering manager, the takeaway is X. If you're an engineer wanting the implementation detail, see Section 3." The risk is the piece feels schizophrenic.

Option 1 wins more often. Coherence beats coverage.

## The profile and the title

The audience profile and the title are linked. The title is the audience profile compressed into a promise. If the title doesn't match the profile's JTBD, either change the title or change the profile.

A title that says "How we cut latency 80% with X" is selling a Decision Support / Survey piece to people who care about latency. A title that says "Tutorial: implementing X" is selling Implementation Guide to people who already decided. These reach different readers — pick one and commit.
