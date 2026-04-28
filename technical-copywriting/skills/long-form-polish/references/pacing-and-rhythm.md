# Pacing and Rhythm

Pacing is how the prose feels in time. Most drafts are monotone — same sentence length, same paragraph length, same energy across thousands of words. Polished prose varies deliberately. The variation is what makes the piece feel composed instead of typed.

## Sentence-length rhythm

### The default failure: monotone

Drafted prose has rhythm patterns the writer doesn't consciously notice. Two common ones:

**The 12-word train**

Most engineers' default sentence length lands around 12-18 words. A draft of all-12-word sentences feels flat:

```
"Postgres uses MVCC for concurrency control. MVCC keeps both versions of updated rows.
 Concurrent readers see consistent snapshots without blocking writers. The cost is dead tuples
 that accumulate over time. VACUUM cleans up dead tuples in the background."
```

Five sentences, each around 10-13 words. Each says one thing. The reader feels no pulse.

**The 30-word breath-killer**

Or, the opposite — long sentences strung together:

```
"The MVCC mechanism in Postgres, which exists primarily to allow concurrent readers and writers
 to operate without blocking each other, accomplishes this by keeping multiple versions of
 each row, with each version tagged by the transaction that created or modified it, and this
 design means that updates create new tuples rather than overwriting existing ones, leading
 directly to the situation where dead tuples accumulate in the heap and require cleanup."
```

One sentence. 80 words. The reader runs out of breath.

### The variation toolbox

Five reliable rhythm patterns:

#### 1. Long-then-short

The long sentence builds a model; the short sentence punches.

```
"Postgres uses MVCC, which means that every UPDATE creates a new tuple while leaving the old
 tuple in place, so that readers running in older snapshots can still see the row as it was
 before the update.

 That's the elegant part."
```

The 45-word sentence does the explaining. The 5-word sentence does the framing.

#### 2. Short-then-long

The short sentence sets up; the long sentence develops.

```
"VACUUM didn't run. The reason was a single hung psql session that an engineer had left open
 over lunch, which kept a transaction with an old xmin alive, which prevented VACUUM from
 cleaning up any tuples newer than that xmin."
```

Two sentences, 6 + 38 words. The short opener creates the tension; the long sentence releases it.

#### 3. Three-short cascade

A sequence of short sentences accelerates toward a payoff.

```
"We checked the logs. Nothing. We checked the metrics. Nothing. We checked the database. There
 it was."
```

Each sentence ends fully; the cumulative effect is acceleration.

#### 4. Long-long-short

Two long sentences set up; one short sentence closes.

```
"Most teams adopt strict mode incrementally because the alternative — a big-bang migration with
 hundreds of broken type errors all at once — is operationally indistinguishable from chaos.
 The incremental approach lets the team fix errors in batches, with each batch landed and
 verified before the next, so progress is visible and reversible at every step.

 It's the only approach that works."
```

The two long sentences give the reasoning. The short closes the case.

#### 5. The em-dash compress

Em dashes — used sparingly — let you compress two sentences into one rhythmic unit.

```
"VACUUM does the work; the question is when it can run. The answer — surprisingly — is 'when
 no transaction is older than the oldest dead tuple.'"
```

The dashes create a pulse without the longer pause of a full stop.

### Sentence-length audit

Run this on a finished draft:

1. Pick a section.
2. Count words per sentence.
3. Plot the lengths in your head.
4. Look for:
   - Three or more sentences with similar length in a row → break the pattern.
   - A sequence of all-long sentences → insert a short.
   - A sequence of all-short sentences → insert a long for breath.
   - An over-50-word sentence that's not doing complex work → split.

The audit takes 5 minutes per section. It's the highest-leverage rhythm pass.

## Paragraph-length rhythm

The same principle, scaled up. A 2000-word piece with all 100-word paragraphs reads flat. Variety carries the reader.

### Paragraph-length effects

| Length | Effect |
|---|---|
| **One sentence** (5-30 words) | Punch. Pivot. Emphasis. Maximum velocity. |
| **2-3 sentences** (40-80 words) | Workhorse paragraph. Most prose. |
| **4-5 sentences** (80-150 words) | Develops a single idea fully. |
| **6+ sentences** (150-300 words) | Complex argument. Risks losing the skim reader. |
| **300+ words** | Rare. Almost always should be broken. |

### The single-sentence paragraph

The most underused tool in technical writing. Use it for:

- A pivot ("But there's a catch.")
- A payoff ("It's the index that's killing us.")
- A summary of a complex section ("Two systems, one root cause.")
- An emphasis ("This is the bug.")

A single-sentence paragraph signals to the reader: *stop here, this matters.* Don't overuse — the effect dilutes.

### Long paragraph repair

A 250-word paragraph almost always wants to be three 80-word paragraphs. Repair patterns:

**Pattern 1: split at logical pivots**

Find where the paragraph shifts topic, claim, or example. Insert a paragraph break.

**Pattern 2: extract the punch**

If the paragraph ends with the most important sentence, extract that sentence into its own paragraph for emphasis.

**Pattern 3: convert to a list**

If the paragraph is enumerating items, switch to a list. The list scans better.

### Paragraph-length audit

Same as sentences: pick a section, eyeball paragraph lengths, fix monotony.

## Section-length rhythm

The biggest-scale pacing decision. A 3000-word piece with six 500-word sections reads monotone; one with sections of 200 / 600 / 800 / 400 / 700 / 300 reads composed.

### Reasons sections vary

- **Setup sections are short.** You're establishing common ground; don't overstay.
- **Development sections are mid-to-long.** Substantial moves take space.
- **Synthesis / payoff sections vary.** Sometimes short and punchy; sometimes long and detailed.
- **Closes are short.** Resolution doesn't need much.

### Section-length warning signs

| Signal | Likely problem |
|---|---|
| Section over 1000 words | Trying to do too much; needs splitting or scoping |
| Section under 100 words | Too thin to deserve its own H2; merge or expand |
| Five consecutive sections all 400-500 words | Monotony; intentional variation needed |
| Wildly uneven (one section 200, next 1500) | Unintentional bloat; reader's attention will break |

## Energy pacing

Pacing isn't only about length; it's about *energy*. Energy comes from concrete language, vivid examples, voice intensity, and rhythm.

### The energy curve

A well-paced article has an energy curve:

```
ENERGY
   ^
   |        Hook ───┐
   |               ╲           ┌─── Payoff
   |   Setup ─────╲╲          ╱
   |                ╲╲    ╱──╱
   |                 ╲╲╱──╲
   |                            ╲─── Close
   |
   +────────────────────────────────────────> TIME
```

Hook starts high (curiosity). Setup dips slightly (necessary information without much energy). Development climbs through specifics, evidence, and examples. Payoff peaks. Close settles.

A piece with flat energy reads boring even if every sentence is fine. A piece with chaotic energy reads disorganized.

### Where to inject energy

- **Specific examples** raise energy.
- **Dialogue / quotes** raise energy.
- **Surprising facts** raise energy.
- **Voice intensity (opinion, stake)** raises energy.
- **Short paragraphs at key beats** raise energy.

### Where energy can sit lower

- Setup paragraphs (necessary; reader knows it's groundwork).
- Caveats and disclaimers (the reader expects these to be lower-energy).
- Tables and lists (content over voice).
- Methodology sections in whitepapers.

The pattern: invest energy where the article needs to grip; allow it to dip where the reader can ride lower.

## The breath test

A useful synthesis: read a paragraph aloud and count the breaths you take.

| Breaths per 100 words | Effect |
|---|---|
| 0-1 | Run-on; reader can't breathe |
| 2-3 | Tight, paced |
| 4-6 | Natural for technical prose |
| 7+ | Choppy; too many short sentences |

If a paragraph forces you to take 0-1 breaths, split sentences. If it makes you take 7+, combine.

## Pacing across genres

Different genres have different pacing norms:

| Genre | Typical pacing |
|---|---|
| Tutorial | Even pacing; readers reading for procedure |
| Deep-dive | Slower opening (model-building); faster development; punchy synthesis |
| Opinion | Punchy throughout; short paragraphs; high energy |
| Case study | Mixed; setup slow, journey punchy, retrospective slower |
| Whitepaper | Patient throughout; designed for non-linear reading |
| Technical narrative | High variation; narrative pacing matches story arc |

Match pacing to genre. A whitepaper paced like an opinion piece reads frantic; an opinion piece paced like a whitepaper reads dull.

## The pacing pass

Practical workflow:

1. **Read each section** marking sentences that feel monotonous.
2. **Vary sentence length** at the marked spots.
3. **Audit paragraph lengths** — break walls, insert short paragraphs at pivots.
4. **Audit section lengths** — note any wildly long or short sections; address.
5. **Energy check** — does the energy curve match the genre's expected shape?
6. **Read aloud** — final test (see `read-aloud-test.md`).

The pacing pass takes 30-60 minutes per 2000 words. It's the difference between prose that reads like a transcript and prose that reads like writing.

## Anti-patterns

### The exhaustion paragraph

A paragraph so long the reader runs out of attention before it ends. Symptoms: 200+ words, 5+ ideas, no white space.

**Fix:** find the logical pivots; insert paragraph breaks. If there are no pivots, the paragraph is doing too many things.

### The choppy section

A sequence of short paragraphs in a row, none over 30 words. Looks like notes.

**Fix:** combine paragraphs that develop the same idea. Reserve short paragraphs for pivots and emphasis.

### Pacing-by-headings

Using heading frequency to artificially "pace" a piece — H2 every 200 words regardless of structure.

**Fix:** headings should mark structural moves, not just provide visual breaks. Use other rhythm tools (paragraph length, callouts) for pure pacing.

### The em-dash overdose

Em dashes are seductive but burn out fast. A piece with three em dashes per page reads as overwritten.

**Fix:** limit to one em-dash construction per 500 words. Use commas, parentheses, or new sentences for the others.

### The same opener six times

Five paragraphs in a row that start with "But" or "Now" or "However."

**Fix:** vary openers. Mix sentence-start words, occasional inverted constructions, occasional dialogue or quotes.

### Pacing without purpose

Variation for its own sake — random short sentences inserted for rhythm without logical reason.

**Fix:** pacing should *serve* the content. The short sentence at the end of a long paragraph punches because the long paragraph set it up; the short sentence inserted at random feels like a tic.
