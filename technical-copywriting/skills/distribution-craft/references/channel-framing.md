# Channel Framing

The same article reads differently to different audiences. A piece that converts on Hacker News may bounce on LinkedIn (and vice versa). Channel framing is the practice of presenting the same substance through the right window for each venue. It is not different articles — it's the same article, packaged for the channel.

## What changes vs. what doesn't

### What changes per channel

| Element | Adjusted per channel |
|---|---|
| Title / framing | Yes — each channel has different conventions |
| Length | Yes — X is short, LinkedIn medium, HN title-only |
| Tone | Yes — within the same voice, register adjusts |
| Hook | Yes — what hooks on X may not hook on LinkedIn |
| Visual treatment | Yes — image vs no-image varies |

### What doesn't change

| Element | Constant across channels |
|---|---|
| The article's substance | Same |
| The honesty of the framing | Same |
| The voice (in spirit) | Same |
| The promise to the reader | Same |
| Citations and sources | Same |

Channel framing is *re-presenting*, not *misrepresenting*.

## The five-channel comparison

Take one article: a deep-dive titled "The Postgres setting that's eating 30% of your disk." Frame for five channels.

### X / Twitter

```
"Most Postgres databases I've audited have 18% dead tuples. Not 2%, not 5% — eighteen percent.
 Here's how that happens, why VACUUM can't always fix it, and the alert that catches it
 before you run out of disk: [link]"
```

| Element | Choice |
|---|---|
| Length | 280 chars |
| Tone | Conversational, direct |
| Hook | Specific number (18%) |
| Promise | Three deliverables previewed |

### LinkedIn

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

| Element | Choice |
|---|---|
| Length | 200 words |
| Tone | Personal, professional |
| Hook | Personal angle (audited; expected) |
| Promise | Mechanism + audit query + alert |

### Hacker News

```
Submission title: "Diagnosing Postgres dead tuples accumulation"

First comment (from author):
"Wrote this after the third client in a row had this exact failure mode. The alert query in
 the article works on most Postgres versions; if you're on 15+, also consider the new
 pg_visibility extension which gives you per-table dead-tuple counts directly. Happy to
 discuss disagreements on the autovacuum threshold recommendations — there's reasonable
 variation here depending on workload."
```

| Element | Choice |
|---|---|
| Length | Title only + substantial first comment |
| Tone | Direct, technical |
| Hook | The accuracy of the title |
| Promise | Implicit — the title is the promise |

### Reddit (/r/PostgreSQL)

```
Title: "Diagnosing dead tuples accumulation in production Postgres"

Body (optional):
"After auditing 12 production databases, I keep finding the same operational issue: VACUUM
 not running because of long-running transactions. Wrote up the mechanism and a 6-line alert
 that catches it. Curious if /r/PostgreSQL has tuned autovacuum thresholds differently for
 high-write workloads. Article: [link]"
```

| Element | Choice |
|---|---|
| Length | Title + ~80 word body |
| Tone | Technical, peer-to-peer |
| Hook | Direct title + invitation to discuss |
| Promise | Specific to subreddit's interests |

### Newsletter

```
Subject: How dead tuples accumulate in Postgres
Preview: Why VACUUM can't always run, and the 6-line alert that catches it

Body (excerpt strategy):
"Most Postgres databases I've audited have 18% dead tuples. Not 2%, not 5% — eighteen percent.

 The mechanism is straightforward and the failure mode is preventable, but it's the most
 common operational issue I see across teams.

 Here's how dead tuples accumulate in Postgres, why VACUUM can't always clean them up, and
 the 6-line alert that catches the problem before you run out of disk:

 [Read the full article]"
```

| Element | Choice |
|---|---|
| Length | Subject + preview + ~80 word excerpt |
| Tone | Personal, focused |
| Hook | Specific number in opening |
| Promise | Stated up-front; full article via link |

## Per-channel principles

### X / Twitter

- **Lead with value, not the link.** "New post: [link]" gets ignored.
- **Specific numbers grip.** "18%" beats "many."
- **One claim per tweet.** Multi-claim tweets dilute.
- **Threads earn engagement** when each tweet is genuinely substantial.

### LinkedIn

- **Lead with personal angle.** "I spent the quarter…" beats "Here's an article."
- **Use line breaks every 1-3 sentences.** Walls of text don't scan.
- **Length: 100-300 words.** Shorter underperforms.
- **Avoid Twitter-shorthand.** "Ratio'd," "based," "TIL" don't translate.

### Hacker News

- **Title-only submission.** No image; no preview.
- **Title is the entire pitch.** Honest, specific, accurate.
- **First comment matters.** Substantive context, not promotion.
- **Engage with comments.** HN audiences expect author presence.

### Reddit

- **Per-subreddit conventions.** Read the rules; observe the tone.
- **Engage substantively.** Drive-by submissions get downvoted.
- **Don't cross-post.** Each subreddit gets its own framing.
- **Respect karma minimums** and post-frequency limits.

### Newsletter

- **Subject line is the highest-leverage element.** Determines open rate.
- **Preview text is the dek.** Most inboxes show it.
- **Body strategy varies** — full article, excerpt, or tease.

## Channel-fit detection

Not every channel fits every article. Some signals:

| Signal | Channel fit |
|---|---|
| Highly technical, specific to a tool | HN, Reddit-technical, niche newsletter |
| Career advice, professional growth | LinkedIn |
| Hot take or contrarian view | X, possibly HN |
| Tutorial or how-to | All channels; SEO-search channel works well |
| Story or case study | LinkedIn, X (if dramatic), newsletter |
| Whitepaper or report | LinkedIn, professional-research channels |
| Memes or humor | X; risky on others |

If a channel doesn't fit, skip it. Posting where you don't fit costs reputation more than it costs reach.

## Channel-time fit

Some channels reward posting at the moment of an event; others reward evergreen content.

| Channel | Evergreen vs timely |
|---|---|
| X | Strong recency bias; older posts surface less |
| LinkedIn | Some recency bias; well-engaged posts persist |
| HN | Recency bias for front page; older posts surface via search |
| Reddit | Strong recency bias on /new; subreddit search persists |
| Newsletter | Time of send is fixed; evergreen content can be re-sent |
| Substack / Medium | Long tail via search; recency for subscriber inboxes |

Evergreen articles benefit from re-promotion over time. Timely articles peak fast and decay.

## When the article fits one channel

Some articles are made for one specific channel. Examples:

- A 4-sentence observation: best as a tweet, no article needed.
- A 200-word professional reflection: best as a LinkedIn post.
- A 30-page technical investigation: best as a published article + targeted distribution.

Don't force-fit. If the substance fits one channel, publish there. Padding a tweet into an article just to have an article wastes everyone's time.

## Cross-channel echoes

A well-distributed article generates *cross-channel echoes*: someone reads it on HN, tweets about it, the tweet reaches LinkedIn, a LinkedIn user shares it in their newsletter, a newsletter subscriber posts it on Reddit. Each echo brings new readers.

Channel framing increases the chance of echoes by making the article *findable in the framing each channel's readers expect*. A tweet that links to an article that opens with a thesis matching the tweet earns higher click-through than one with a generic intro.

## Channel-fit failure modes

### Cross-posting identical text

Same exact post copied to X, LinkedIn, HN, Reddit. Each platform's algorithm and audience punishes it.

**Fix:** invest 5-10 minutes per channel.

### Channel mismatch

Posting a marketing-style title on HN. Posting a Twitter-length post on LinkedIn. Posting a hot-take on a community subreddit. Mismatches get downvoted or ignored.

**Fix:** read the venue before posting; calibrate.

### Over-distribution

Posting to 8 channels for a routine article. Most of the channels generate noise; reputation costs accumulate.

**Fix:** pick the 2-3 channels that fit the article and audience. Skip the rest.

### Under-distribution

Publishing to your blog and posting nowhere else. The article reaches RSS subscribers and search; everyone else never sees it.

**Fix:** distribute to at least one channel beyond the article's home.

### Cross-platform shilling

A single user posting their own article to /r/programming, then /r/devops, then /r/webdev within an hour. Reddit's spam filter catches this.

**Fix:** one channel per session; days between cross-posts.

## The audit

After 5-10 articles, audit which channels work for your specific content:

- Which channels generated the most clicks?
- Which channels generated the most discussion?
- Which channels generated the most secondary shares?
- Which channels were a net negative (annoyed readers, downvoted)?

The audit reveals your *channel-content fit*. Some writers do well on HN and badly on LinkedIn; others vice versa. Optimize for what works for *you*.

## When to expand or contract channels

| Signal | Action |
|---|---|
| One channel consistently outperforms others by 10x+ | Concentrate there; cut underperformers |
| All channels perform equally | Continue distributing widely |
| New channel is rising in audience | Test once or twice before committing |
| A channel turns hostile (algorithm change, audience drift) | Reduce or exit |

Channels evolve. The right channel mix in 2024 is different from 2020. Re-evaluate annually.

## The compounding pattern

Like every other element of distribution craft, channel framing pays off through compounding:

- Each well-framed channel post earns reach.
- Reach generates secondary shares.
- Secondary shares find new audiences.
- New audiences become first-readers for future articles.

A writer who consistently does channel framing well builds a multi-channel audience over years. A writer who cross-posts identical content builds a smaller, less engaged audience.

The 30 minutes per article spent on per-channel framing is the highest-ROI distribution work. Don't skip it.
