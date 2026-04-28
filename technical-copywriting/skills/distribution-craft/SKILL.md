---
name: distribution-craft
description: >-
  Engineer the distribution layer of a long-form technical article — title,
  dek (subtitle), meta description, social pull-quotes, and channel-specific
  framing. Most technical articles die at the title; this skill covers the
  craft of titles that earn the click without clickbait, deks that confirm
  the promise, social pull-quotes for X / LinkedIn / Hacker News / Reddit,
  open-graph metadata, and the practice of reframing the same article
  differently per channel. Use when the user asks to write a title for an
  article, suggest titles, write a dek or subtitle, write a meta description,
  pull social quotes, prepare a launch, write a tweet thread for an article,
  reframe for LinkedIn / HN / Reddit, or audit existing distribution copy.
  NOT for the article body itself (use long-form-structure / engaging-craft /
  long-form-polish). NOT for SEO keyword research and on-page optimization
  beyond titles and meta (general SEO is out of scope). NOT for content
  marketing strategy. NOT for short-form business writing like email subject
  lines for work (use communication/structured-writing).
---

# Distribution Craft

> The article doesn't end at the last paragraph. A piece that took 20 hours to research and write often gets 2 minutes of distribution attention — and then dies in a noisy feed because the title was generic. Distribution craft is the practice of giving the article a fair chance.

This skill covers the layer between the article and its readers: title, dek, meta description, social pull-quotes, channel framing. None of this is the substance of the article — but all of it determines whether the substance ever gets read.

## Core principle

**Titles do most of the work; treat them as a discipline.** A great article with a weak title reaches a tenth of the readers a great article with a strong title would. The asymmetry is enormous; treat title craft as seriously as paragraph craft.

Secondary principle: **the same article reads differently to different audiences.** A piece that converts on Hacker News may bounce on LinkedIn (and vice versa). Channel framing isn't dishonest — it's the same substance, packaged for the venue the reader is in.

## Title craft

The single highest-leverage 8-12 words you'll write.

### Three things a title must do

1. **Promise something specific** the reader values.
2. **Differentiate** from the noise around it.
3. **Honor the article** — not over-promise, not under-promise.

A title that does all three is rare. Most titles do one (specific) at best.

### Title formulas that work

The classic patterns from a century of headline writing — adapted for technical content.

#### "How we [did specific thing] [with surprising detail]"

```
"How we cut Postgres latency 80% by removing one index"
"How we migrated 100k tests in 11 weeks (without breaking production)"
"How we deleted 47 microservices in one quarter"
```

The "how we" frame promises a story; the specific detail (80%, 11 weeks, 47) earns the click. Works for case studies.

#### "Why [conventional view] is wrong (and what to do instead)"

```
"Why TDD doesn't work for the median team (and what does)"
"Why microservices were a mistake for most teams"
"Why your CI is slow and how to fix it"
```

The contrarian frame promises differentiation; the parenthetical "and what to do" promises constructiveness. Works for opinion.

#### "The [specific kind of bug/problem/pattern] that [cost/changed/revealed something]"

```
"The Postgres setting that's costing you 30% of your disk"
"The deploy bug that took down our pipeline for three days"
"The TypeScript pattern that made our codebase 2x faster to type-check"
```

The frame teases a specific revelation. Works for narratives and deep-dives.

#### "[Specific number] things I learned from [specific experience]"

```
"5 things I learned from a 6-month Rust migration"
"3 lessons from running 100k experiments at GitLab"
"What 11 weeks of test migration taught us about test architecture"
```

Listicle-shaped but anchored in specific experience. Works when the experience is unique.

#### "[Tool/technique] for [specific use case]"

```
"PostgreSQL row-level security for multi-tenant apps"
"Ruby's pattern matching for parsing tree-sitter output"
"Bun's test runner for incremental migration from Jest"
```

Direct, searchable, low-curiosity. Works for tutorials and how-to guides where the audience is already searching.

#### "[Number]-minute [topic]: [specific value]"

```
"The 5-minute Postgres health check"
"A 2-hour deploy pipeline rewrite (and what we learned)"
```

Frames the time investment; promises proportional value.

#### "What [respected source/event] taught us about [topic]"

```
"What the Slack outage taught us about distributed-system blast radius"
"What 6 months of OpenAI's status page taught us about uptime claims"
```

Borrowed authority; specific event lends credibility.

### Anti-formulas (don't)

| Pattern | Why it's bad |
|---|---|
| "The Ultimate Guide to X" | Promise inflation; reader doesn't believe it |
| "Everything You Need to Know About X" | Same |
| "X: A Complete Tutorial" | Marketing-coded |
| "Mastering X in [N] Days" | Self-help-coded |
| "The Future of X" | Generic; predicts nothing specific |
| "X is Dead" | Cliché; rarely true |
| "Why X Will Change Everything" | Hyperbole tells the reader to discount |
| "X 101" | Tells novices "this is for you" but loses everyone else |
| "Beyond X: Y" | Pretentious; the reader cares about X or Y, not the journey |
| Single-word titles ("Resilience.") | Vague; competes with nothing |

### The 8-12 word rule

Most strong titles land between 8-12 words. Shorter often vague; longer often loses energy.

```
✗ Too short (5 words):   "Postgres performance lessons learned"
✓ Right length (10):     "The Postgres setting that's eating 30% of your disk"
✗ Too long (16):         "Lessons learned from a comprehensive Postgres performance investigation in our production environment"
```

Exceptions exist (some tight 5-word titles work), but 8-12 is the safe band.

### Title testing

If you're not sure between candidates, test:

1. **Read each aloud.** The one that reads cleanest usually wins.
2. **Show three friends.** Which would they click? Which is clearest?
3. **Search for it.** If your candidate title shows existing articles with very similar titles, you're competing in noise — differentiate.
4. **Strip the curiosity test.** Does the title still tell the reader what they get even with all curiosity-bait removed? If not, you're relying on bait.

### The honest-title constraint

A title's job is to *describe accurately what the reader will get*. Curiosity is fair; misleading is not.

| Honest curiosity | Dishonest bait |
|---|---|
| "The Postgres setting that's eating 30% of your disk" (article delivers the setting and the calc) | "The shocking truth about Postgres" (article doesn't deliver shock) |
| "How we cut latency 80% by removing one index" (we did) | "The one weird trick to cut latency 80%" (no trick; cheap framing) |
| "What 6 months of OpenAI status pages taught us" (we read 6 months of pages) | "The dark secret OpenAI doesn't want you to know" (no secret) |

The asymmetry is brutal: dishonest titles get a one-time click and zero return readers. Honest specific titles compound trust.

See `references/title-craft.md` for the full title formula library and worked transformations.

## Dek craft

The dek (subtitle, standfirst, deck) is the second sentence the reader reads. Its job: confirm the title's promise and earn the read.

### Dek formulas

| Pattern | Example |
|---|---|
| Restate + specify | Title: "Why TDD doesn't work for the median team." Dek: "TDD is a discipline that pays off at scale; for teams of 5-15 it usually adds cost without proportional benefit. A look at why, and what works instead." |
| Promise + scope | Title: "The Postgres setting that's eating 30% of your disk." Dek: "How dead tuples accumulate, why VACUUM can't always clean them up, and the alert that catches the problem before you run out of space." |
| Story setup | Title: "How we deleted 47 microservices in one quarter." Dek: "We had a distributed monolith pretending to be microservices. Here's how we noticed, what we cut, and what we kept." |
| Expectation set | Title: "The 5-minute Postgres health check." Dek: "A six-query script you can run on any database to find the most common operational problems. Designed for teams without a dedicated DBA." |

### Dek length

Usually 25-50 words. Shorter risks losing the second hook; longer competes with the article body for attention.

### Dek anti-patterns

- **Repeating the title.** "Why TDD doesn't work for the median team." Dek: "TDD doesn't work for the median team because…" Wastes the dek.
- **Hyping the dek.** "An incredible deep dive into the world of…" — adjective inflation tells the reader to discount.
- **Promising more than the article.** Dek over-promise is the same trust failure as title over-promise.

See `references/dek-and-meta.md` for the full dek and meta-description craft.

## Meta description (and open-graph)

The meta description appears in search results and social previews. Often 150-160 characters.

### Meta description formula

```
[Article promise in one sentence], [specific differentiator or detail].
```

```
"How dead tuples accumulate in Postgres, why VACUUM can't always clean them up, and the
 6-line alert that catches the problem before you run out of disk."
```

158 characters. Carries the promise and a specific detail.

### Open-graph image

The image shown in social previews. Two patterns:

1. **The article's title rendered well.** Clean typography, brand-consistent. Works when title carries the substance.
2. **A graphic / chart from the article.** Works when the article has a memorable visual.

Avoid stock photos. They tell the reader the content is generic before they read.

## Social pull-quotes

Per channel, the article needs different framing.

### X / Twitter

The tweet announcing the article should:

- Lead with a specific value-claim (not the title).
- Include the link.
- Optionally end with a hook for engagement.

```
✗ "New post: 'The Postgres setting that's eating 30% of your disk' [link]"
✓ "Most Postgres databases I've audited have 18% dead tuples. Here's how that happens, why
   VACUUM can't always fix it, and the 6-line alert that catches it before you run out of
   disk: [link]"
```

The second version sells the article in 280 characters; the first only labels it.

#### Tweet thread version

For high-stakes articles, a thread can preview the substance:

```
1/ Most Postgres databases I've audited have 18% dead tuples. Not 2%, not 5% — eighteen
   percent. Here's how that happens.

2/ MVCC keeps both versions of an updated row. Concurrent readers see consistent snapshots.
   The cost: dead tuples.

3/ VACUUM cleans them up. But VACUUM can't run while a transaction older than the dead
   tuples is still open.

4/ So one engineer's lunch-time psql session, left open for an hour, can prevent VACUUM from
   running on your entire database.

5/ Here's the alert that catches it: [link]
```

Threads earn engagement (each tweet a chance to retweet) but cost more time. Use selectively.

### LinkedIn

LinkedIn rewards different framing:

- Open with a personal angle ("I spent 6 months researching this").
- Include a takeaway readers can use.
- Avoid Twitter-shorthand vocabulary.
- Length: 100-300 words; LinkedIn favors longer posts than Twitter.

```
"I spent the last quarter auditing Postgres databases for clients. The most common
 operational issue wasn't what I expected.

 It wasn't slow queries. It wasn't bad indexes. It was dead tuples — the byproduct of
 Postgres's MVCC system that accumulate when VACUUM can't run.

 In the worst case I saw, 84% of the database was dead tuples. The team was paying for
 storage they couldn't actually read.

 The cause was almost always the same: a long-running transaction blocking VACUUM, often
 from an unrelated batch job or a forgotten psql session.

 I wrote up the mechanism, the audit query, and the alert that catches it: [link]"
```

### Hacker News

HN rewards:

- A title that signals depth (not "10 tips" but "How X works").
- An honest, specific submission title.
- A first comment from the author with context (not promotion).
- A topic that intersects with HN interests (developer tools, infrastructure, security, performance).

HN doesn't reward:

- Marketing language.
- Listicles.
- Anything that reads as content marketing.

The submission title can be the article title (preferred) or a more direct version:

```
Article title: "The Postgres setting that's eating 30% of your disk"
HN title:      "Diagnosing Postgres dead tuples accumulation"
```

The HN version trades curiosity for clarity — HN readers prefer the second.

### Reddit

Per subreddit; varies wildly. /r/programming favors HN-style titles. /r/devops favors operational specifics. /r/PostgreSQL favors technical depth.

Reddit titles must comply with subreddit rules and avoid feeling promotional. Submit infrequently; engage in comments substantively.

### Newsletter

If sending to a newsletter:

- Subject line is the highest-leverage element.
- Often the same as the article title, occasionally adapted.
- Preview text (the second line shown in inboxes) acts like the dek.

```
Subject: How dead tuples accumulate in Postgres
Preview: Why VACUUM doesn't always run, and the 6-line alert that catches it
```

See `references/social-pull-quotes.md` for per-channel patterns and worked examples.

## Channel framing

Same article, different framing per channel. Not different articles — different *windows* into the same article.

### What changes per channel

| Element | X | LinkedIn | HN | Reddit | Newsletter |
|---|---|---|---|---|---|
| Title | Curiosity-led | Personal-led | Specific / accurate | Subreddit-appropriate | Like article |
| Length | 280 chars (or thread) | 100-300 words | Title only | Title + auto-text | Subject + preview |
| Tone | Conversational | Professional | Direct | Per subreddit | Per newsletter voice |
| Hook | First 100 chars | First sentence | The title itself | The title itself | Subject line |
| Link | Always | Always | Always | Always | Always |

### What doesn't change

| Element | Across channels |
|---|---|
| The article's substance | Same |
| The honesty of the framing | Same |
| The voice | Same in spirit; adjusted to register |
| The promise to the reader | Same |

Channel framing is *re-presenting* the same article, not pretending it's a different article.

See `references/channel-framing.md` for per-channel deep-dives and worked transformations.

## ✅ Use for

- Writing a title for a finished article
- Suggesting 5-10 title candidates and picking the best
- Writing a dek / subtitle / standfirst
- Writing a meta description for SEO
- Pulling 3-5 social quotes for X / LinkedIn from the article
- Reframing the same article for HN, LinkedIn, X, Reddit
- Writing a tweet thread that previews the article
- Writing a newsletter subject line + preview text
- Auditing existing distribution copy

## ❌ NOT for

- **The article body itself** — use long-form-structure / engaging-craft / long-form-polish
- **General SEO** (keyword research, on-page optimization beyond titles and meta) — out of scope
- **Content marketing strategy** — out of scope
- **Short-form business writing** (email subject lines for work, RFC titles) — use communication/structured-writing
- **UI text or button labels** — use ux-writing
- **Paid promotion / ads copy** — different discipline; out of scope

## Anti-patterns

### The afterthought title

**What it looks like:** Article gets 30 hours of work; title gets 30 seconds. Default to the working title.

**Why it's wrong:** Title is the single highest-leverage 8-12 words. The reach asymmetry is enormous.

**What to do instead:** Generate 10 title candidates. Read each aloud. Pick the strongest; sit on it for a day; reconsider. The 30 minutes earns more readers than another 5 hours of polish.

### Clickbait

**What it looks like:** Titles that over-promise to earn the click. "The shocking truth…" "You won't believe…" "This one weird trick…"

**Why it's wrong:** The asymmetry is brutal. One bait-click, never returning. Trust burned.

**What to do instead:** Curiosity is fine; misleading is not. Make the title *specific* and *accurate*. Curiosity that pays off compounds; curiosity that doesn't burns.

### The dek that repeats the title

```
Title: "Why TDD doesn't work for the median team"
Dek:   "TDD doesn't work for the median team because…"
```

Wastes the dek. The reader who clicked the title is now reading the same content again.

**Fix:** the dek confirms the title's promise *and adds something* — scope, specificity, hook.

### Channel-blind cross-posting

The same exact post copied to X, LinkedIn, HN, Reddit. Each platform has different conventions; ignoring them costs reach on each.

**Fix:** invest 5-10 minutes per channel to reframe. The total time is small; the reach difference is large.

### Promotional first comment on HN

The author posts a first comment that reads like marketing. HN downvotes; the article never gets traction.

**Fix:** if you post a first comment, make it substantive — context the article doesn't include, or an invitation to disagree on a specific point.

### LinkedIn-as-Twitter

A 280-character LinkedIn post with a link. LinkedIn's algorithm favors longer-form; short posts get little reach.

**Fix:** write 100-300 words. Lead with personal angle. Save curiosity-style posts for X.

### Social pull-quotes that don't appear in the article

Pulling a quote that's striking but isn't actually in the article. Reader clicks expecting that line; doesn't find it; bounces.

**Fix:** pull quotes only from the actual article. If the article doesn't have a striking quote-able line, write one and add it to the article.

### Title rewriting after publication

Publishing with title A, then changing to title B based on initial signal. Fragments the article's identity (URLs already shared, screenshots floating around with title A).

**Fix:** spend the title-craft time *before* publishing. Once published, title is mostly fixed.

## Workflow

1. **Confirm the article is polished.** Don't title until the body is done — the title may need to change based on what the article actually became.
2. **List the article's promise** in one sentence. The title is a compression of this.
3. **Generate 10 title candidates.** Use the formula library.
4. **Read each aloud; eliminate weak ones.**
5. **Test the top 3.** Read to a friend; search for similar titles; verify each is accurate.
6. **Pick the winner.**
7. **Write the dek** — confirm and extend the title.
8. **Write the meta description** — 150-160 characters; promise + detail.
9. **Pull 2-4 social quotes** from the article for re-use.
10. **Reframe per channel** — X version, LinkedIn version, HN version, newsletter version.
11. **Open-graph image** — clean typography or a chart from the article.
12. **Sit on it** — review the package the next morning before publishing.

## References

| File | Contents |
|---|---|
| `references/title-craft.md` | Title formulas, anti-patterns, the 8-12 word rule, testing protocol, worked transformations |
| `references/dek-and-meta.md` | Dek formulas, meta descriptions, OG metadata, open-graph images |
| `references/social-pull-quotes.md` | Per-channel patterns for X / LinkedIn / Hacker News / Reddit / newsletter; tweet threads; first-comment strategy |
| `references/channel-framing.md` | What changes vs what doesn't per channel; worked transformations of one article across X / LinkedIn / HN / newsletter |

## Related skills

- **long-form-structure** — the article's promise (set in structure) is what the title compresses.
- **engaging-craft** — title and dek inherit voice from the body.
- **long-form-polish** — distribution comes after the body is polished.
- **technical-research** — specific numbers from research feed specific titles.
- **storytelling** (skillstack) — narrative framing for non-technical pieces.
- **communication/structured-writing** (skillstack) — work-writing structure (BLUF, Pyramid) for memos and emails.
