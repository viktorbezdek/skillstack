# Cut Discipline

Every drafted long-form piece can lose 20-40% of its words without losing meaning. Cutting tightens prose, raises the meaning-per-word ratio, and respects the reader's time. The discipline is to *find* the cuts — most writers cling to words they don't need.

## The 30% rule

Take a finished draft. Cut 30% without changing the structure or losing meaning. The piece almost always survives, often improves. The reader feels the difference.

Why 30% is the right target:

- 10% is hedges and filler — easy to cut, almost mechanical.
- Another 10% is throat-clearing and meta — harder; requires trusting the reader.
- The last 10% is redundancy — hardest; requires recognizing that two sentences say the same thing.

Below 30%, you're leaving easy wins. Above 40%, you start cutting substance — recognizable when each cut requires real consideration.

## Three-pass cut protocol

### Pass 1: hedges and filler

Fast. Mechanical. Removes about 10%.

| Cut | Reason |
|---|---|
| "I think" / "I believe" / "I feel" | Implicit in any first-person claim |
| "perhaps" / "maybe" / "might" / "could" | Hedge by reflex; keep only when actually qualified |
| "in some sense" / "in a way" / "kind of" / "sort of" | Verbal tics |
| "really" / "very" / "quite" / "actually" / "basically" | Empty intensifiers |
| "of course" / "obviously" / "clearly" | If obvious, don't say so; if not, prove it |
| "as we know" / "as you know" / "needless to say" | If we know, don't say; if not, attribute |

### Pass 2: throat-clearing and meta

Cut every sentence that *talks about* the article instead of *being* the article.

| Cut | Reason |
|---|---|
| "In this article we will discuss…" | The title and hook do this work |
| "In this section, we will explore…" | The heading does this work |
| "Now let's look at…" | Just look at it |
| "It's important to note that…" | Just note it |
| "It's worth mentioning that…" | If worth mentioning, mention; if not, don't |
| "As we discussed earlier…" | Trust the reader to remember |
| "We'll come back to this later…" | Just come back |
| "Before we continue, let me say…" | Just say it |
| "I want to be clear that…" | Be clear; don't talk about being clear |

### Pass 3: redundancy

Slowest. Hardest. Removes 10-20%.

| Cut | Reason |
|---|---|
| Sentences that restate the previous sentence | Picked the best version |
| Paragraphs that recap earlier paragraphs | Trust the reader |
| Examples that demonstrate the same point as a previous example | Pick the best |
| Adjectives that don't add information | "comprehensive solution" — if comprehensive, prove it; otherwise cut |
| Synonym pairs ("aid and assist," "help and support") | Pick one |
| Doubled qualifiers ("very specific" → "specific") | Adverb adds nothing |
| Restatements after lists | List already enumerated; don't summarize the list back |

## Worked transformations

### Before

```
"It's important to note that, in many cases, when teams are considering whether to migrate to
 strict mode in TypeScript, there are actually several different factors that they really need
 to take into account before making a decision. These factors include things like the size of
 the codebase, the maturity of the team's TypeScript practices, the amount of any-typed code
 that exists in the codebase currently, and the overall risk tolerance of the organization."
```

74 words.

### Three-pass cut

**After Pass 1 (hedges/filler):**
```
"When teams are considering whether to migrate to strict mode in TypeScript, there are several
 factors they need to take into account before making a decision. These factors include things
 like the size of the codebase, the maturity of the team's TypeScript practices, the amount of
 any-typed code in the codebase, and the overall risk tolerance of the organization."
```
60 words. -19%.

**After Pass 2 (throat-clearing/meta):**
```
"Teams considering strict mode migration need to weigh several factors before deciding: the
 size of the codebase, the maturity of TypeScript practices, the amount of any-typed code, and
 the organization's risk tolerance."
```
33 words. -55%.

**After Pass 3 (redundancy):**
```
"Strict-mode migration depends on four factors: codebase size, TypeScript maturity, current
 any-coverage, and risk tolerance."
```
17 words. -77%.

The 17-word version carries the same information in less than a quarter of the words. It also reads tighter. Same meaning, vastly better experience.

### Another example

### Before

```
"In our experience, after we did the migration, we noticed that there were a number of issues
 that we hadn't really anticipated when we started the project, including things like
 performance regressions, increased memory usage, and unexpected behavior in our caching
 layer. These issues were challenging for our team to address because we had already moved
 past the point where we could easily roll back the migration. We ended up having to spend
 several weeks debugging and patching these issues."
```

89 words.

### Three-pass cut

**After Pass 1 (hedges/filler):**
```
"After the migration, we noticed several issues we hadn't anticipated: performance regressions,
 increased memory usage, and unexpected behavior in our caching layer. These were challenging
 to address because we'd moved past the point of easy rollback. We spent several weeks
 debugging and patching."
```
46 words. -48%.

**After Pass 2 (throat-clearing/meta):**
Already trimmed; minor:
```
"Post-migration, we hit issues we hadn't anticipated: performance regressions, increased memory,
 and caching weirdness. Rolling back wasn't easy by then. Three weeks of debugging."
```
26 words. -71% from original.

**After Pass 3 (specificity bonus):**
```
"Three weeks of post-migration debugging on issues we hadn't anticipated: 18% slower P99,
 30% more RAM, and a cache that started returning stale results 1 in 200 requests."
```
30 words. -66% from original, but each word now carries more weight (concrete numbers replace generic adjectives).

## What not to cut

The hardest part of the cut: knowing what to *keep*.

| Keep | Why |
|---|---|
| Concrete examples and specific numbers | Substance |
| Citations and source attributions | Credibility |
| Voice markers (first-person stake, opinion) | Personality |
| Genuine qualifications ("unless you're at scale X") | Real nuance |
| Counter-arguments addressed | Earned credibility |
| Setup that the reader needs | Common ground |
| Transitions between sections | Pacing |
| Pull quotes from sources | Authority signal |

The goal isn't word count for its own sake — it's meaning per word. Cutting that hurts meaning is bad cutting.

## Cut diagnostics

When considering whether to cut a sentence:

1. **Does the article still make sense without this sentence?** If yes, cut.
2. **Does the next paragraph repeat what this sentence says?** If yes, cut one.
3. **Could this sentence appear in any article on any topic?** If yes, cut.
4. **Does this sentence add information or is it elaboration?** If just elaboration, consider cutting.
5. **Could a more specific version replace this generic version?** If yes, replace; don't merely cut.

## Common cut resistance

Writers resist cuts for predictable reasons. Recognize the resistance; cut anyway.

### "But it's well-written"

Beautiful sentences that carry no information are still cuttable. The reader's experience matters more than the writer's pride.

### "But it's important context"

Often "important context" is hedge for "I want the reader to know I know this." If the article works without it, the reader doesn't need it.

### "But it took me an hour to write"

Sunk cost is irrelevant to whether a sentence belongs. A 60-second-cut sentence freed an hour of writing time only in retrospect.

### "But the reader might miss the point without it"

If the reader will miss the point without this sentence, the surrounding sentences aren't doing their job. Fix the surrounding sentences; cut the over-explanation.

### "But it's a great anecdote"

Great anecdotes still need to serve the article. A great anecdote that takes 200 words to set up for a sub-point not worth 200 words is bloat.

## Cut for pacing

Some cuts are pure pacing. A draft can be already-tight on every sentence but sluggish in aggregate. Cut for pacing:

- **Cut filler transitions.** "Now," "So," "Well," "Anyway." Most sentences don't need them.
- **Cut paragraph openers that recap.** "As we saw, …" — trust the reader.
- **Cut repeated examples.** Three examples of the same point: pick the best one.
- **Cut hedge-paragraphs.** Whole paragraphs spent qualifying a previous claim. Often the original claim was correct; the qualification is over-defense.

## Cut for honesty

Some cuts are integrity moves. Cut:

- **Claims you can't source.** Better to omit than to bluff.
- **Generalizations beyond your evidence.** "Most teams" when you've talked to three teams: cut to "the teams I've talked to."
- **Authority you haven't earned.** "It's well-established that…" — if it isn't, don't claim.
- **Specifics you've fudged.** Round numbers presented as exact, anonymous attributions you can't actually defend, etc.

## When to stop cutting

Three signals you've gone far enough:

1. **The next cut hurts.** You can't remove anything else without losing meaning, voice, or rhythm.
2. **The piece reads "tight" rather than "spare."** Tight is the goal; spare is too far.
3. **The cuts have stopped being mechanical** — every cut now requires judgment about what stays.

If you're at all three, ship.

## After cutting

Always re-read after cutting. Cuts often introduce:

- Broken transitions (the bridge sentence got cut).
- Tense inconsistencies (cuts spanned tense changes).
- Dropped antecedents (the noun got cut; later "it" no longer has a referent).
- Lost rhythm (a cut made a paragraph read flat).

A 15-minute re-read after cutting catches these. Skip it and they ship.

## The "cut by 50%" exercise

A useful exercise even if not for production: take a draft and challenge yourself to cut it by 50%.

You usually can't (without losing real substance), but the exercise reveals which sentences are *most* essential. Often the half-version is closer to the right length than the full version.

The exercise also exposes the writer's tics — the words and phrases they reach for by default. Identifying those tics speeds up future cut passes.

## Cut conventions across genres

| Genre | Cut aggressiveness |
|---|---|
| Tutorial | Aggressive — readers want the procedure, not the prose |
| Deep-dive | Moderate — explanations need space to land |
| Opinion | Aggressive — punchy reads better than padded |
| Case study | Moderate — narrative needs texture |
| Whitepaper | Lower — methodology and qualification are substance |
| Technical narrative | Moderate — narrative pacing requires breath |

The 30% target applies across genres, but *what* gets cut varies. Tutorials cut prose around code; whitepapers cut hedges and filler but keep methodology.

## The discipline pays compounding returns

Every cut pass makes the next one easier. After three articles polished with the cut discipline, the writer's drafts come in tighter — they internalize the patterns and stop drafting filler in the first place.

This is the highest-leverage long-form writing skill: it improves every future piece without additional effort once internalized.
