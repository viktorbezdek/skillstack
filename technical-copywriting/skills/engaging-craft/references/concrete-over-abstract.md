# Concrete Over Abstract

The single most important sentence-level discipline in technical writing. Abstract prose washes over readers; concrete prose grips them. Most failed technical articles fail at this level — every sentence is technically correct but specifically forgettable.

## The principle

| Abstract | Concrete |
|---|---|
| "Performance was significantly improved" | "P99 dropped from 480 ms to 120 ms" |
| "Many engineers struggle with this" | "I've watched four teams hit this in the last year" |
| "The migration was challenging" | "The migration broke 47 tests; we fixed 41 in two weeks; six took six months" |
| "Code quality matters" | "We had three production incidents in Q3 attributable to a single function nobody had reread since 2021" |
| "Modern systems are complex" | "Our microservices stack has 12 services; tracing one user request touches 8" |
| "There are tradeoffs" | "Option A trades 200 ms of P99 latency for 30 percent less RAM" |

Abstract prose lets the reader's attention wander. Concrete prose grabs it back. Abstract prose can be replaced with any other abstract prose; concrete prose can only be the prose it is.

## Three substitutions

### 1. Numbers replace adjectives

| Replace | With |
|---|---|
| "significantly faster" | "3x faster" or "40 ms faster on P99" |
| "much smaller" | "down from 1.2 GB to 340 MB" |
| "high latency" | "average 240 ms; P99 1.4 s" |
| "many tests broke" | "47 of 1,247 tests broke" |
| "long-running" | "runs for 4-7 hours" |

Numbers force precision. They also force you to *know* the number — which forces research. An article that hand-waves "significantly faster" usually didn't measure; an article with "3.2x" usually did.

### 2. Names replace categories

| Replace | With |
|---|---|
| "a modern framework" | "Next.js 14" |
| "the team" | "the Phoenix LiveView team" or "our 12-person backend team" |
| "an engineer" | "Adam Wathan" or "the staff engineer leading the migration" |
| "various clouds" | "AWS, GCP, and Azure" |
| "some industries" | "fintech, healthcare, and ad tech" |
| "the database" | "Postgres 16 (or whichever you use — we'll show Postgres examples)" |

Named things land. Categorical references slide off. The reader's brain stores "Adam Wathan" but discards "an engineer."

### 3. Demonstrations replace assertions

| Replace | With |
|---|---|
| "X is hard to debug" | "Here's a 20-line repro that fails in three different ways depending on timing" |
| "The API is confusing" | "Here are the four method names that look identical but differ in handling of nullable fields" |
| "Caching is hard to get right" | "Here's the cache invalidation bug we shipped to production three times" |
| "Microservices are complex" | "Here's the trace of a single user signup, touching 8 services" |
| "Postgres is well-engineered" | "Here's the heapam.c comment from 1996 that's still load-bearing" |

Demonstrations let the reader see the claim; assertions ask the reader to take your word.

## The "why this not that" diagnostic

When a sentence feels generic, ask: *why this and not that?*

```
"Performance was important to us."

Why important — and important compared to what? Why us — what's specific about your team?
What kind of performance — latency, throughput, capacity, cost? Compared to what — your prior
benchmarks, your competitors, the user's perception?

→ "We had a P99 latency budget of 200 ms because that's what felt instantaneous in our user
  research, and we were at 320 ms after the last release."
```

Every "important / interesting / significant / notable / relevant" is a candidate for the diagnostic. The reader cares about the *what*, not the *that-it-is*.

## When abstract is right

Abstract has a job — generalizing across many specifics. The discipline is to *earn* the abstract by paying for it in concrete first.

```
✓ "We tried the index on three different schemas — orders, sessions, audit_log. In all three,
   the index helped reads but slowed writes. The pattern is consistent enough to call it a
   law: high-write tables don't benefit from indexes on frequently-written columns."
```

Three concrete observations, then the abstract generalization. The reader trusts the abstract because it earned its position.

```
✗ "It's well-known that high-write tables don't benefit from indexes on frequently-written
   columns."
```

The abstract claim with no specifics. Even if it's true, the prose feels asserted, not demonstrated.

### The 3-then-1 pattern

A reliable structure:

1. Concrete example.
2. Concrete example.
3. Concrete example.
4. The abstract generalization the three examples support.

Use this pattern when introducing a principle. Don't lead with the principle.

## Abstract-to-concrete revision pass

Run this pass on every draft. It takes 20-40 minutes per 2000 words and dramatically improves engagement.

### Step 1: highlight every abstract noun

```
"The migration was complex. Performance varied across our environments. There were tradeoffs."

→ Abstract nouns: migration, complex, performance, environments, tradeoffs.
```

### Step 2: for each, find the concrete equivalent

| Abstract | Concrete |
|---|---|
| migration | "the move from MySQL 5.7 to Postgres 16" |
| complex | "47 incompatible queries; 12 broken triggers; one schema-comparison tool that gave wrong results half the time" |
| performance | "P99 latency on the orders endpoint" |
| environments | "staging on RDS db.r6g.xlarge; production on db.r6g.4xlarge" |
| tradeoffs | "we got 30% lower latency at the cost of 50% more RAM" |

### Step 3: rewrite with the concretes

```
"The move from MySQL 5.7 to Postgres 16 broke 47 queries, 12 triggers, and exposed two bugs in
 our schema-comparison tool. P99 on the orders endpoint dropped from 480 ms to 120 ms in
 staging (db.r6g.xlarge) but jumped back to 380 ms in production (db.r6g.4xlarge) — a tradeoff
 of 30 percent lower latency for 50 percent more RAM."
```

The revised version is longer but carries vastly more information. The reader knows what migration, what queries, what hardware, what numbers — and trusts the writer.

### Step 4: cut

After concretizing, cut sentences that *now* feel redundant. The concrete versions usually let you delete summarizing abstracts.

## When you can't find a concrete

Sometimes you reach for the concrete substitution and discover you don't have one. That's information:

| What it means | What to do |
|---|---|
| You don't actually know the specifics | Research them; the article isn't done |
| The specifics are off-record | Acknowledge ("a fintech company we worked with") |
| The claim was a vibe rather than evidence | Cut the claim or weaken to "anecdotally" |
| The specifics are too proprietary to share | Find an analogous public case ("the Slack outage of 2024 had a similar shape") |

The "I can't find a concrete" moment often catches the article making claims it isn't entitled to make.

## Concrete language for technical writing

Three patterns specific to technical content:

### 1. Specific commit hashes, version numbers, dates

```
✗ "In an older version of Postgres…"
✓ "In Postgres 9.6 (released 2016)…"

✗ "The team patched the issue."
✓ "The fix landed in commit a1b2c3d (PR #4521, merged 2024-03-15)."
```

The specific reference lets the careful reader verify. The vague reference asks them to trust.

### 2. Specific code, specific error messages

```
✗ "The error message was unhelpful."
✓ "The error message was: ERROR: deadlock detected at character 47, which doesn't tell you
   which transaction won."

✗ "We had to write some custom code."
✓ "We added 47 lines: a custom JSON serializer that handled the legacy date format."
```

### 3. Specific operational artifacts

```
✗ "Performance got worse over time."
✓ "Here's the Datadog graph: P99 climbed from 120 ms to 340 ms over six weeks. The inflection
   point is at March 14 — the day we deployed the new caching layer."
```

Operational artifacts (graphs, dashboards, log snippets, error stacks) are the most concrete possible evidence. Use them when you have them.

## Anti-patterns

### Adjective stacking

```
"This is a comprehensive, robust, scalable, performant, modern solution that addresses all the
 critical concerns of today's complex distributed systems."
```

Six unmodified adjectives, each generic. The sentence carries no information. Cut all six and replace with one specific demonstration.

### The corporate noun phrase

```
"Process improvements yielded efficiency gains."
```

Two abstract nouns ("process improvements," "efficiency gains") with no specifics. Rewrite:

```
"We deleted three CI steps; the pipeline went from 12 minutes to 8."
```

Now the sentence carries information.

### Rounded numbers as code for "I don't know"

```
"About 80% of teams" / "Roughly half" / "Most of the time"
```

Rounded numbers can be honest (you genuinely measured 80%), or they can be code for "I'm guessing." If you're guessing, either look it up or weaken to "many" / "most" with attribution.

### "Studies show" with no study

```
"Studies show that developers spend most of their time reading code."
```

Which studies? When? With what methodology? "Studies show" without citation is a verbal tic, not a citation. Either link the study or remove the framing.

### The infinite list

```
"There are many factors to consider, including performance, scalability, maintainability,
 reliability, security, cost, observability, developer experience…"
```

The list signals "I don't know which of these matters." Pick the two or three that *actually* matter for this case and develop them.

### Abstraction inflation in revision

A draft that started concrete sometimes inflates to abstract during revision (the writer rounded off specifics for "professional" tone). Catch this in late drafts; restore the specifics.

## The concreteness test

For each paragraph, ask:

1. Does any sentence have a specific number, name, or artifact?
2. If I removed those specifics, would the paragraph still parse?
3. Could the paragraph be cut from the article without changing the article's meaning?

If the answer to (1) is no and to (3) is yes, the paragraph is filler. Either concretize it or cut it.

## Concrete + voice

Concreteness is partly a voice choice. An academic voice tolerates more abstraction; a conversational voice demands more concreteness. Within any voice, however, concreteness *helps*.

A common pattern: a piece sounds smart but doesn't *feel* like the writer knew anything specific. Almost always, the fix is more concrete examples drawn from real work — not more polished prose.

## When the writer is the concrete

For lived-experience pieces, the writer's own specifics are the highest-leverage concretes:

```
"We migrated 100,234 tests in 11 weeks. Three broke production."
```

You can't be more concrete than this. The writer was there; the numbers are theirs; the claim is unfakeable. Lived-experience pieces that don't lead with the writer's specifics are leaving their best evidence on the table.

## The compounding effect

Concrete prose has a compounding effect: each concrete detail makes the next one more credible. A piece with five specific numbers, three named systems, two real code snippets, and one operational artifact reads as deeply researched even before you check the citations. A piece with no specifics reads as vibes even if the underlying research was real.

The discipline isn't optional. Cultivate it.
