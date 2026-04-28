# Title Craft

The single highest-leverage 8-12 words in any article. Most articles get a default working title that ships unchanged; this is the most common preventable distribution failure in technical writing.

## What a title must do

1. **Promise something specific** the reader values.
2. **Differentiate** from the noise around it.
3. **Honor the article** — accurate, not over-promising.

Most titles do (1) at best. Strong titles do all three.

## The 8-12 word band

Most strong titles land between 8-12 words.

| Length | Risk |
|---|---|
| 1-4 words | Vague; competes with nothing |
| 5-7 words | Tight; can work but often under-specifies |
| **8-12 words** | The safe band; room for specificity + curiosity |
| 13-15 words | Loses energy; reader's eye glazes |
| 16+ words | Reads as subtitle, not title |

Exceptions exist (a tight 5-word title with strong words can work, e.g., "Falsehoods Programmers Believe About Names"). But default to 8-12 unless you have specific reason.

## Title formula library

Each formula has a track record. Pick by article shape.

### "How [we / they] [did specific thing] [with surprising detail]"

```
"How we cut Postgres latency 80% by removing one index"
"How GitHub built Copilot's autocomplete latency under 200 ms"
"How we migrated 100k tests in 11 weeks (without breaking production)"
"How we deleted 47 microservices in one quarter"
```

**Best for:** case studies. The "how we" frame promises a story; the specific detail (80%, 11 weeks, 47) earns the click.

**Variants:**
- "How we [did X] in [time period]"
- "How [company] [did X]"
- "How we [did X] (without [side effect])"

### "Why [conventional view] is wrong (and what to do instead)"

```
"Why TDD doesn't work for the median team"
"Why microservices were a mistake for most teams"
"Why your CI is slow and how to fix it"
"Why we stopped using GraphQL"
```

**Best for:** opinion. Promises differentiation from conventional wisdom.

**Variants:**
- "Why [thing] is harder than it looks"
- "Why we [stopped doing X]"
- "Why [specific group] should [non-obvious action]"

### "The [specific thing] that [verb + consequence]"

```
"The Postgres setting that's costing you 30% of your disk"
"The deploy bug that took down our pipeline for three days"
"The TypeScript pattern that made our codebase 2x faster to type-check"
"The CSS feature that solves 80% of your layout problems"
```

**Best for:** narratives, deep-dives, "wow factor" posts. Teases a specific revelation.

**Variants:**
- "The [N] [things] that [verb]"
- "The [thing] you've never heard of"
- "The [thing] that nobody talks about"

### "[Specific number] things I learned from [specific experience]"

```
"5 things I learned from a 6-month Rust migration"
"3 lessons from running 100k experiments at GitLab"
"What 11 weeks of test migration taught us"
```

**Best for:** experience-based reflections. Listicle-shaped but anchored in specific experience.

**Variants:**
- "Lessons from [specific event]"
- "What [N years / N events] of [thing] taught me"

### "[Tool / technique] for [specific use case]"

```
"PostgreSQL row-level security for multi-tenant apps"
"Ruby's pattern matching for parsing tree-sitter output"
"Bun's test runner for incremental migration from Jest"
```

**Best for:** tutorials, how-tos. Direct, searchable, low-curiosity. The reader is already searching for this.

**Variants:**
- "[Use case] with [tool]"
- "[Tool] for [use case]: a guide"

### "[Time investment]: [specific value]"

```
"The 5-minute Postgres health check"
"A 2-hour deploy pipeline rewrite (and what we learned)"
"The 10-minute CI setup that saves you a day per week"
```

**Best for:** tutorials with clear payoff. Frames the time cost; promises proportional value.

### "What [respected source / event] taught us about [topic]"

```
"What the Slack outage taught us about distributed-system blast radius"
"What 6 months of OpenAI status pages taught us about uptime"
"What the Linux scheduler tells us about fairness"
```

**Best for:** pieces that draw insight from a public event or source. Borrows authority.

### "[Specific verb]: [thing]"

```
"Falsehoods Programmers Believe About Names"
"Considered Harmful: GoTo Statements"
"Profiling: A 10-minute introduction"
```

**Best for:** classics; works when the title is already familiar to the audience or when it borrows a known pattern.

### "A [adjective] case for [thing]"

```
"A modest case for boring databases"
"A practical case for the modular monolith"
"An honest case against my own previous post"
```

**Best for:** opinion that's measured rather than provocative.

## Anti-formulas (don't)

| Pattern | Why it fails |
|---|---|
| "The Ultimate Guide to X" | Promise inflation; reader doesn't believe it |
| "Everything You Need to Know About X" | Same |
| "X: A Complete Tutorial" | Marketing-coded; reader discounts |
| "Mastering X in N Days" | Self-help-coded |
| "The Future of X" | Generic; predicts nothing specific |
| "X is Dead" | Cliché; rarely true |
| "Why X Will Change Everything" | Hyperbole tells the reader to discount |
| "X 101" | Tells novices "this is for you"; loses everyone else |
| "Beyond X: Y" | Pretentious; the reader cares about X or Y, not the journey |
| Single-word abstract titles ("Resilience.") | Vague; competes with nothing |
| "[Buzzword] for [Buzzword]" | Both words generic; cancels itself out |
| "A Deep Dive Into X" | Tells the reader the *form*, not the *substance* |

## Title testing

### Test 1: read aloud

The title that reads cleanest aloud usually wins. Stumbles in titles are amplified — the reader's eye stumbles in milliseconds.

### Test 2: strip the curiosity

Remove every curiosity-bait element. Does the title still tell the reader what they get?

```
Before: "The shocking truth about TypeScript strict mode"
Stripped: "About TypeScript strict mode"

→ Title was relying on "shocking" + "truth" for grip; substance is missing.
```

A title that survives the strip is honest. One that doesn't is bait.

### Test 3: search the title

Search for your candidate title. If 30 articles have nearly identical titles, you're competing in noise. Differentiate.

### Test 4: show three friends

Three readers; ask which they'd click. Watch for hesitations and "what does this mean?" — those are signals.

### Test 5: imagine the article in a feed

Picture your candidate title in a Hacker News list, a Twitter feed, a LinkedIn feed, an RSS reader. Does it stand out? Or does it blend?

## Worked title transformations

### Case study transformation

```
Default working title:        "Our migration to TypeScript strict mode"
After title craft:            "How we migrated 500k lines of TypeScript to strict mode in 11 weeks (and what broke)"
```

The default title is descriptive but generic — "our migration" tells nothing specific. The crafted version carries scope (500k lines), time (11 weeks), and a hook (and what broke).

### Opinion transformation

```
Default working title:        "Some thoughts on microservices"
After title craft:            "Microservices were a mistake for most teams (and the modular monolith is the right alternative)"
```

The default reads as low-stakes. The crafted version commits to a position and previews the alternative.

### Deep-dive transformation

```
Default working title:        "Understanding Postgres VACUUM"
After title craft:            "Why VACUUM blocks during long transactions (and the alert that catches it)"
```

The default is a textbook chapter title. The crafted version is specific: why-question + actionable closer.

### Tutorial transformation

```
Default working title:        "Setting up row-level security in Postgres"
After title craft:            "Row-level security in Postgres: a working multi-tenant setup in 90 minutes"
```

The default is searchable but unspecific. The crafted version commits to scope (multi-tenant) and time investment (90 minutes).

### Narrative transformation

```
Default working title:        "A debugging story"
After title craft:            "The day our database stopped accepting writes (and the 47-character bug behind it)"
```

The default is generic; the crafted version is in-medias-res with a specific tease.

## Honesty check

Before locking the title:

1. Does the article actually deliver what the title promises?
2. Is the specific number (if any) in the title accurate?
3. Could a reader reasonably feel misled?

If any answer is uncertain, fix either the title or the article. Misleading titles burn trust permanently.

## SEO considerations

A note on SEO. Some title patterns rank better in search:

- **Specific keywords match search queries.** "PostgreSQL row-level security multi-tenant" matches what people search.
- **Long-tail titles often rank.** Specific multi-word titles match specific searches.
- **Question-format titles can rank well** for question-search behavior.
- **Title length matters.** Very long titles get truncated in SERPs.

But: SEO and engagement aren't separate. Titles that engage humans tend to engage algorithms. Don't sacrifice clarity for keyword stuffing — it ranks worse *and* engages less.

## When to A/B test

For high-stakes pieces (a paid newsletter's main piece, a launch post for a product), A/B test the title.

Most platforms (Substack, Medium, Twitter via thread vs. tweet, etc.) support some form of testing. The cost is low; the reach impact can be 2-3x.

For most articles, A/B testing is overkill. The 30-minute title-craft pass earns most of the gain.

## Title and dek as a unit

Title and dek work together. The title hooks; the dek confirms. Test them as a pair:

```
Title: "Why VACUUM blocks during long transactions"
Dek:   "How dead tuples accumulate, why a forgotten psql session can fill your disk, and the
        6-line alert that catches it before you run out of space."
```

The dek lets the title be tighter (no need to cram every detail into the title) and earns the second commitment from the reader.

## When to break the rules

Strong title craft sometimes breaks the rules deliberately. Examples:

- **Single-word titles** when the word is the article's whole frame ("Slow.").
- **Very long titles** when they're effectively the dek ("Falsehoods Programmers Believe About Names And Why Your User Onboarding Form Is Broken").
- **Question titles** when the question itself is provocative ("Did You Know Your Database Is Fine?").

The rules are defaults that work most of the time. Break them when you have a specific reason; don't break them by accident.

## The compounding payoff

Writers who learn title craft develop an ear. After a year, their working titles are 80% of the way to the final title. The polish pass is shorter; the reach is consistently better.

Like every other skill in technical copywriting, title craft compounds.
