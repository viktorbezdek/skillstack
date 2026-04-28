# Social Pull-Quotes

Each channel has its own conventions, voice, and engagement patterns. The same article reframed for X, LinkedIn, Hacker News, Reddit, and a newsletter reaches dramatically different audiences. Channel-blind cross-posting (the same exact post copied everywhere) gets the worst possible result on each platform.

## The principle

The article is the substance; the channel post is the *advertisement* for the substance. The advertisement must:

1. **Match the channel's voice and conventions.**
2. **Lead with value, not the link.**
3. **Honor the article** — describe accurately, not over-promise.

Channel framing is *re-presenting* the same article, not pretending it's a different article.

## X / Twitter

X rewards punchy, specific, value-led posts. The link is the call to action; the tweet is the pitch.

### Single-tweet patterns

#### Pattern: claim + link

```
"Most Postgres databases I've audited have 18% dead tuples. Not 2%, not 5% — eighteen percent.
 Here's how that happens, why VACUUM can't always fix it, and the alert that catches it
 before you run out of disk: [link]"
```

Specific number; sets up the article's central claim; promises specific deliverables.

#### Pattern: contrarian-led

```
"Microservices were a mistake for most teams. Here's the case (with a steelman of the
 conventional view, three specific failure modes, and what to do instead): [link]"
```

Provocative claim earns the click; bullet-style preview shows substance is there.

#### Pattern: in-medias-res

```
"At 02:47 AM on a Sunday, our database stopped accepting writes. The runbook didn't have the
 error. Here's the bug, the fix, and what we changed to prevent it: [link]"
```

Specific scene; sets up curiosity; promises payoff.

### Tweet thread version

For high-stakes articles, a thread can preview the substance and earn engagement at each step.

```
1/ Most Postgres databases I've audited have 18% dead tuples. Not 2%, not 5%. Eighteen
   percent. Here's how that happens.

2/ MVCC keeps both versions of an updated row. Concurrent readers see consistent snapshots
   without blocking writers. The cost: dead tuples.

3/ VACUUM cleans them up. But VACUUM can't run while a transaction older than the dead
   tuples is still open.

4/ So one engineer's lunchtime psql session, left open for an hour, can prevent VACUUM from
   running on your entire database.

5/ Here's the alert that catches it before you fill your disk: [link to article]
```

#### Tweet thread rules

- **First tweet sells the thread.** No "1/" alone — the first tweet should pull the reader in.
- **Each tweet earns the next.** No filler.
- **Last tweet has the link.** Or links to the article in a separate context.
- **Limit threads to 5-8 tweets.** Longer threads see steep drop-off.

### X anti-patterns

| Pattern | Why it fails |
|---|---|
| "New post: [title] [link]" | Labels the article instead of selling it |
| "Just published! [link]" | No value prop; reads as broadcast |
| Tweet that's the title only | Wastes the 280 characters |
| All-caps or excessive emoji | Reads as spam |
| Quote-tweeting your own previous tweet endlessly | Algorithm penalizes; followers irritated |

### X length

| Length | Use |
|---|---|
| 1 tweet (~280 chars) | Quick value prop + link |
| 5-8 tweet thread | Substantial preview; earns engagement |
| 10+ tweet thread | Risks; only when each tweet is genuinely substantial |

## LinkedIn

LinkedIn rewards different framing — longer, more personal, more professional-toned. The algorithm favors posts that keep readers on LinkedIn (so post the substance in the LinkedIn post, with the link as supplementary).

### LinkedIn post patterns

#### Pattern: personal angle + insight

```
"I spent the last quarter auditing Postgres databases for clients. The most common operational
 issue wasn't what I expected.

 It wasn't slow queries. It wasn't bad indexes. It was dead tuples — the byproduct of
 Postgres's MVCC system that accumulate when VACUUM can't run.

 In the worst case I saw, 84% of the database was dead tuples. The team was paying for storage
 they couldn't actually read.

 The cause was almost always the same: a long-running transaction blocking VACUUM, often from
 an unrelated batch job or a forgotten psql session.

 I wrote up the mechanism, the audit query, and the alert that catches it: [link]"
```

200 words. Personal frame, specific number, concrete recommendation.

#### Pattern: lessons learned

```
"3 things I learned from migrating 100,234 tests from Mocha to Vitest in 11 weeks:

 1. The biggest cost wasn't the migration — it was deciding what to leave behind. We kept
    47k tests; the rest were duplicates of better-written ones we just hadn't noticed.

 2. Test migrations expose architectural debt. Tests that were hard to migrate were almost
    always tests of poorly-bounded code.

 3. The runtime difference (14 min → 3 min on the full suite) wasn't from Vitest's speed —
    it was from the cleanup we did along the way.

 Full writeup: [link]"
```

#### Pattern: counter-narrative

```
"Microservices were a mistake for most teams I've worked with.

 Not because the pattern is wrong — at scale, microservices solve real problems. But the
 median engineering team (under 50 people, single product) pays the distributed-systems cost
 without the organizational benefit.

 Three specific failure modes, the case for the modular monolith, and what changes if your
 team grows past the threshold: [link]"
```

### LinkedIn rules

- **Length: 100-300 words.** LinkedIn favors substantial posts; very short ones get little reach.
- **Lead with the angle.** First sentence is the hook.
- **Use line breaks.** Single block of text doesn't scan; line breaks every 1-3 sentences.
- **Don't write for "engagement bait."** "What do you think?" at the end can earn comments but reads tired.
- **Avoid Twitter-shorthand vocabulary.** "TIL," "ratio'd," "based" don't translate.

### LinkedIn anti-patterns

| Pattern | Why it fails |
|---|---|
| Twitter-length post | Algorithm doesn't promote |
| Hyphen-bullet lists for everything | Reads as listicle template |
| "Inspirational" framing on technical content | Off-tone; LinkedIn cliché |
| Engagement-bait questions ("What do you think?") | Annoys repeat readers |
| Cross-posting Twitter format | Doesn't fit; underperforms |

## Hacker News

HN rewards depth, honesty, and topic-fit. The first comment from the author often shapes the discussion.

### HN submission

The submission title:

| Pattern | When |
|---|---|
| Article title verbatim | When the title is HN-appropriate (specific, technical, not marketing-coded) |
| Adapted title | When the original title is too curiosity-led for HN |

```
Article title:        "The Postgres setting that's eating 30% of your disk"
HN-adapted title:     "Diagnosing Postgres dead tuples accumulation"
```

The HN version trades some curiosity for direct accuracy. HN readers prefer it.

### First comment

A useful first comment from the author:

- **Adds context** the article doesn't include (why I wrote this, related work).
- **Invites disagreement** on a specific point.
- **Acknowledges limits** of the article.

```
"Author here. Wrote this after the third client in a row had this exact failure mode. The
 alert query in the article works on most Postgres versions; if you're on 15+, also consider
 the new pg_visibility extension which gives you per-table dead-tuple counts directly.

 Happy to discuss disagreements on the autovacuum threshold recommendations — there's
 reasonable variation here depending on workload."
```

### HN anti-patterns

| Pattern | Why it fails |
|---|---|
| Marketing language in submission title | Downvoted; doesn't reach front page |
| Self-promotion in first comment | Ratioed; comment buried |
| Sponsored content disguised as editorial | Detected; surfaced; reputation damage |
| Submitting your own article repeatedly | Mod intervention |

### HN earns slow

HN is a long-tail channel. Articles that don't make the front page in the first 2 hours often surface later via search and back-linking. Good articles persist; bad articles vanish.

## Reddit

Reddit varies wildly per subreddit. /r/programming favors HN-style titles. /r/devops favors operational specifics. /r/PostgreSQL favors technical depth.

### Reddit rules

- **Read the subreddit's rules.** Many ban self-promotion; some require karma minimums.
- **Engage in comments substantively.** Submitting and disappearing reads as drive-by.
- **Submit infrequently.** One submission per subreddit per week max.
- **Don't title-edit after submission.** Reddit shows the original title regardless.

### Reddit submission patterns

For technical subreddits:

```
Title: "Diagnosing Postgres dead tuples accumulation in production [Link]"
```

Direct, accurate, link in title or first comment.

For broader subreddits (/r/programming):

```
Title: "Why VACUUM blocks during long transactions, and the alert that catches it"
```

Slightly more curiosity-led but still specific.

### Reddit anti-patterns

| Pattern | Why it fails |
|---|---|
| Cross-posting to 10 subreddits | Spam-flagged |
| Submitting only your own content | Auto-spam-flagged |
| Marketing-style titles | Downvoted |
| Ignoring subreddit conventions | Removed |

## Newsletters

If sending the article to a newsletter:

- **Subject line is the highest-leverage element.** Determines open rate.
- **Preview text** (the second line shown in inboxes) acts like a dek.
- **The body** can be the article itself, an excerpt, or a teaser linking to the full piece.

### Subject + preview

```
Subject: How dead tuples accumulate in Postgres
Preview: Why VACUUM doesn't always run, and the 6-line alert that catches it
```

Both visible in most inboxes. Subject hooks; preview confirms.

### Subject line patterns

| Pattern | Example |
|---|---|
| Direct from article title | "How dead tuples accumulate in Postgres" |
| Question | "Why is your Postgres disk filling up?" |
| Number + topic | "The 6-line alert every Postgres team needs" |
| Personal angle | "What I found auditing 12 Postgres databases" |

### Newsletter body strategies

#### Strategy 1: full article in the email

Reader doesn't have to click out. Best for engaged subscribers who read in the inbox.

#### Strategy 2: excerpt + link

First 300-500 words in the email; link to full article. Best for newsletters that want to drive traffic to the site.

#### Strategy 3: tease + link

A 100-word framing of the article + link. Lowest commitment; lowest conversion.

The right strategy depends on the newsletter's goal (engagement vs. traffic vs. discoverability).

## Mastodon / Bluesky / decentralized

These platforms behave more like X but with different conventions:

- **Less algorithmic amplification.** Posts reach followers; less viral potential.
- **More substantive engagement** in many communities.
- **Hashtags work** (more than on X, where hashtags are de-emphasized).

Adapt X-style posts; add 2-3 relevant hashtags; expect lower reach but higher signal-per-reader.

## Cross-posting strategies

### Strategy 1: per-channel rewrite

Highest effort; highest payoff. Each channel gets a tailored post.

Time: 15-30 minutes per channel.

### Strategy 2: per-channel template

Mid-effort. Maintain a template for each channel; fill in the specific article details.

Time: 5-15 minutes per channel.

### Strategy 3: minimal adaptation

Lowest effort. Copy the same post to all channels with minor tweaks (link format, length cap).

Time: 5 minutes total. Gets the worst result on each channel.

For high-stakes articles, use strategy 1. For routine content, strategy 2. Strategy 3 is for low-priority pieces.

## Pull quotes from the article

Beyond per-channel posts, the article often contains 2-4 pull-quote-able lines. Identify them in revision and re-use them across channels.

### What makes a good pull quote

- **Specific.** "We deleted 47 microservices" beats "we deleted some."
- **Memorable.** Short, rhythmic, quotable.
- **Self-contained.** Reads OK without context.
- **Surprising.** Earns attention.

### Where to use them

- Tweet body.
- LinkedIn post opener.
- Newsletter subject or preview.
- HN comment ("from the article: '...' ").
- The article itself, as a pull quote callout.

A reusable bank of 2-4 pull quotes per article amplifies its reach across channels.

## Timing

Each channel has timing conventions:

| Channel | Best time |
|---|---|
| X | Tuesday-Thursday, mornings (US time zones) |
| LinkedIn | Tuesday-Thursday, 8-10 AM in audience's time zone |
| Hacker News | Weekdays, 8 AM PT (gets best front-page exposure) |
| Reddit | Per subreddit; usually mid-day in audience's time zone |
| Newsletter | Per newsletter convention; consistency matters more than perfection |

Timing matters at the margin (~10-20% reach difference). Don't obsess; do post during the audience's awake hours.

## The audit

After publishing, audit:

- Which channels drove the most engagement?
- Which framing worked? Which didn't?
- What did commenters / repliers focus on? (Often surfaces what was actually interesting in the article.)

Use the audit to shape future distribution. Channels that work for your specific content keep working; channels that don't are usually a permanent mismatch.
