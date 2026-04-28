# Scannability

Every long-form piece is read by two readers at once: the careful reader committing 12 minutes, and the skim reader scanning in 90 seconds. Both need to leave with value. Scannability is the discipline of serving both — making the piece work top-to-bottom for the careful reader and visually-traversable for the skimmer.

## The skim reader's path

The skimmer scans, in order:

1. **Title and dek** (5 seconds)
2. **First paragraph** (10 seconds)
3. **Section headings** (15 seconds — top to bottom)
4. **First sentence of each paragraph** (variable; usually catches a third of them)
5. **Bold text and pull quotes** (5 seconds)
6. **Lists, tables, callouts** (10-15 seconds)
7. **Last paragraph** (10 seconds)
8. **Decision: read in full or close** (instant)

Total: 60-90 seconds.

If the skim doesn't deliver enough value to commit to the full read, the skimmer leaves. Scannability determines what they take.

## Scannability tools

### 1. Section headings (H2)

The skimmer's table of contents. Every 200-500 words.

**Good headings:**
- Preview the section's content ("Why VACUUM blocks during long transactions")
- Stand alone — readable without context
- Match the section's actual scope (heading promises X; section delivers X)
- Use parallel construction across siblings ("Why X happens" / "Why Y happens" / "Why Z happens")

**Bad headings:**
- Vague ("Some thoughts," "Background," "Implementation")
- Cute but uninformative ("The plot thickens," "Down the rabbit hole")
- Marketing-coded ("Unlocking the power of X")
- Mismatched scope (heading promises a deep dive; section is a paragraph)

### 2. Sub-headings (H3)

When a section has 3+ logical parts. Helps the skimmer navigate within sections.

Don't over-nest. H4 and below are usually a sign the section wants to be split into multiple H2s.

### 3. Topic sentences first

The first sentence of every paragraph should carry the paragraph's claim. The skimmer reads first sentences; if first sentences carry meaning, the skimmer extracts the article.

```
✗ Buried claim:
"After we tried the index, we ran the queries again and looked at the results. The latency
 went up across the board — the index was slowing things down."

✓ Topic-first:
"The index made queries slower, not faster. After we added the new index and re-ran our
 benchmarks, latency increased across the board."
```

The first sentence of the second version says everything the skimmer needs.

### 4. Bold text

Use sparingly. Highlights the load-bearing claim in a section.

| Pattern | Frequency |
|---|---|
| Bold the central claim of a section | 1 per section |
| Bold a key term being defined | At first use only |
| Bold a critical warning ("**Do not** run this on production") | Where it matters |

Never bold:
- Random phrases for emphasis
- Every other sentence
- Marketing-style "key benefits"
- Things the skimmer can already see (the heading already emphasizes this section)

### 5. Lists

Use lists when items are **genuinely parallel** — same kind of thing, no logical relationship beyond enumeration.

| Use list | Use prose |
|---|---|
| Steps in order | Reasoning chains |
| Options with no preference | Argument with thesis |
| Items being compared on the same dimensions | Story-shaped narrative |
| 4+ similar items | 2-3 items in a sentence |

Anti-pattern: lists for everything. A list of "X, Y, Z" reads as parallel options when the actual claim is "X because Y, which leads to Z." Prose carries causation; lists obscure it.

### 6. Tables

Use tables when comparing 2+ items across 2+ dimensions.

| Comparison | Table or prose? |
|---|---|
| Two options on three dimensions | Table |
| One option's properties | Prose or list |
| Three options on one dimension | List |
| Multiple options on multiple dimensions | Table |

Tables scan dramatically faster than prose for comparative content. The skim reader extracts entire tables in 5 seconds.

### 7. Callout boxes

For tangential content that the careful reader values but the skim reader can skip.

```
> 💡 **Aside:** The 1996 design decision still shapes how Postgres handles VACUUM today.
> See `heapam.c` line 1234 for the comment.
```

Or:

```
> ⚠️ **Pitfall:** Setting `autovacuum_vacuum_scale_factor` too low can cause autovacuum to run
> constantly on small tables, hurting throughput.
```

Callouts pull aside-content out of the main flow, keeping the through-line clean.

### 8. Pull quotes

A sentence or two extracted and visually emphasized. Used in long-form to create visual anchors.

```
> "The reason 'database administrator' was once a full-time job."
```

Pull quotes work for:
- Memorable lines that crystallize the article
- Quotes from interviewees or sources
- Provocative claims worth highlighting

Pull quotes don't work for:
- Setup or methodology sentences (no punch)
- Sentences requiring context (the skimmer won't have it)
- Generic prose (a generic pull quote is just visual clutter)

### 9. White space

Often the highest-leverage tool. Long unbroken text is daunting; white space invites the eye in.

Generated by:
- Short paragraphs
- Paragraph breaks at logical pivots
- Lists and tables
- Callout boxes
- Section breaks
- Liberal margins (in publication design)

A page of dense text has half the read-rate of the same content broken with white space.

### 10. Visual artifacts

Code blocks, screenshots, charts, terminal output. These break the prose flow and create scan-anchors.

| Artifact | Purpose |
|---|---|
| Code block | Shows the actual code; scannable in 5 seconds |
| Screenshot | Shows the actual UI; bypasses prose explanation |
| Chart | Shows trend or comparison; faster than prose |
| Terminal output | Shows actual behavior; concrete |
| Diagram | Shows structure or flow; replaces paragraphs |

Use one visual artifact per 500-1000 words for scan-friendly content. Use more for tutorials and case studies; fewer for opinion and narrative.

## The skim test

After polishing, do the skim test:

1. Set a timer for 90 seconds.
2. Skim the article — title, headings, first sentences, bold, lists, tables, last paragraph.
3. Stop at 90 seconds.
4. Write down what you got.

Did you get:
- The article's main thesis?
- Two or three supporting points?
- The intended next action?

If yes, the article scans well. If no, fix:
- **Missing thesis:** the hook isn't doing its job, or the title doesn't preview content.
- **Missing supporting points:** topic sentences aren't first; headings are vague.
- **Missing action:** the close isn't clear, or the skimmer didn't get there.

## The first-sentence-only read

A more rigorous variant: read *only* the first sentence of every paragraph. Does the article hold together?

This catches:
- Buried topic sentences (first sentences carry no claim).
- Throat-clearing openers ("Now we'll discuss…" — cut).
- Continuity gaps (first sentences don't connect logically).

Most drafts fail this test. Polishing for it is the highest-leverage scannability move.

## Scannability for different genres

| Genre | Scannability priority |
|---|---|
| Tutorial | Very high — readers often jump to step they need |
| Reference / whitepaper | Very high — designed for non-linear reading |
| Deep-dive | Medium — readers committed to linear; scan helps the curious |
| Opinion | Medium — most readers commit to linear |
| Case study | Medium-high — many readers want the result without the journey |
| Technical narrative | Lower — narrative shape requires linear reading |

Don't sacrifice narrative shape for scannability in pieces where narrative is the substance. A technical narrative with 12 H2 headings becomes a list, not a story.

## Scannability for different audiences

| Audience | Scannability priority |
|---|---|
| Decision-makers | Very high — they may not read in full |
| Practitioners doing a search | Very high — they want their answer quickly |
| Casual readers | High — low commitment, easy to bounce |
| Committed readers | Lower — they'll read in full anyway, but scanning helps re-find sections |
| Researchers | Medium — they often skim first, then commit |

Optimize scannability up when audience is decision-makers or searchers; allow lower scannability when audience is committed.

## Scannability and SEO

Search engines also "skim" — they extract structure (headings, lists, tables) for indexing. Scannable content tends to perform well in search for the same reasons it performs well with humans.

Practical: well-structured H2s, descriptive headings, and content-rich first paragraphs help both the skim reader and the search algorithm.

## Anti-patterns

### Heading inflation

Every paragraph gets an H3. The piece becomes a list of one-paragraph sections. The structural signal is lost.

**Fix:** headings should mark *structural* moves, not just visual breaks. If you have ten paragraphs each with their own H3, you have ten under-developed sections — combine.

### Bold inflation

Every other sentence has bold text. Nothing stands out.

**Fix:** bold the load-bearing claim per section. Cut the rest.

### List for non-list content

```
✗ "We made several changes:
   - The database
   - The cache
   - The application"
```

Three items, no parallel structure, no useful detail. The list adds visual fragmentation without scan value.

**Fix:** prose, with detail. "We changed three layers — the database (added an index), the cache (raised TTL from 30s to 5 min), and the application (added retry-with-backoff)."

### Callout overuse

Five callouts per page. Each one interrupts the main flow.

**Fix:** at most 2-3 callouts per 1000 words. Reserve for genuinely tangential content.

### Pull quote of nothing

```
> "We made some changes."
```

Highlights a generic sentence. Adds visual clutter.

**Fix:** pull quotes only for memorable lines.

### No white space

A wall of unbroken text. Reader's eye bounces.

**Fix:** break paragraphs at logical pivots; use lists or tables where appropriate; insert callouts or images for visual variety.

## The scannability audit

A 15-minute pass on a finished draft:

1. **Read just the headings.** Do they tell the story?
2. **Read just the first sentences.** Do they carry meaning?
3. **Look at bold usage.** Sparse and pointed? Or scattered?
4. **Look at lists.** Genuinely list-shaped content? Or fragmented prose?
5. **Look at tables.** Comparative content? Or just formatting?
6. **Look at white space.** Walls of text? Or breathing room?
7. **Look at visual artifacts.** Anchoring the prose? Or absent?

Fix what you find. The audit takes 15 minutes; it noticeably changes how the article reads.
