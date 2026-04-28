---
name: long-form-polish
description: >-
  Polish a long-form technical draft for pacing, scan-ability, and tightness.
  Cover paragraph and sentence rhythm, the scan reader's experience (headings,
  callouts, pull quotes, white space, lists, tables), the 30% cut discipline
  for removing filler, and the read-aloud test for finding bumps. Distinct
  from short-form line-level editing — this skill works at the paragraph
  and section level for pieces of 1500-5000+ words. Use when the user asks
  to polish a long article, fix pacing, improve scan-ability, run a cut pass,
  do a read-aloud test, tighten a draft, fix uneven sections, or prepare a
  draft for publication. NOT for short-form clarity editing of memos / RFCs /
  emails (use communication/clarity-editing). NOT for sentence-level craft
  techniques like AIDA / PAS (use engaging-craft). NOT for outlining or
  structural changes (use long-form-structure). NOT for code documentation
  cleanup (use documentation-generator).
---

# Long-form Polish

> Polish is what separates a draft a reader can finish from a draft that *anyone* can finish. Most long-form pieces fail in the polish phase, not the drafting phase — the substance is there but the experience of reading it is friction-heavy.

This skill covers paragraph- and section-level polish: pacing, scan-ability, the cut, the read-aloud test. It's distinct from line-level clarity editing (which works on individual sentences for active voice, hedge removal, jargon strip — that's communication/clarity-editing's job). Long-form polish is about how the *whole* reads.

## Core principle

**Polish for the skim reader without abandoning the deep reader.** A 3000-word piece is read by two readers at once: the skimmer scanning headings and bold text in 90 seconds, and the careful reader committing 12 minutes. Both need to leave with value. Polish is the discipline of serving both.

## Pacing and rhythm

Pacing is how the prose feels in time. Drafted prose tends to be monotone — same sentence length, same paragraph length, same energy throughout. Polished prose varies deliberately.

### Sentence length variation

| Pattern | Effect |
|---|---|
| Long, long, long | Slows the reader; appropriate for absorbing complex models |
| Short, short, short | Accelerates; appropriate for delivering payoffs and emphasis |
| Long, short | Long sentence builds; short sentence punches |
| Short, long | Short sentence sets up; long sentence develops |

The reliable polish move: find sequences of three or more sentences with similar length. Break the pattern by inserting a sentence of contrasting length.

```
Drafted (monotone):
"The migration was painful for several reasons. The schema change required updating multiple
 services. The data backfill took over a week. The team had to coordinate with downstream
 consumers."

Polished (varied):
"The migration was painful — three reasons. The schema change cascaded through eight services.
 The backfill took nine days. And every downstream consumer needed coordination, which meant
 daily syncs with three teams.

 It was tedious."
```

The varied version is less words but more presence. The two-word sentence ("It was tedious.") punches because the surrounding sentences set it up.

### Paragraph length variation

Paragraphs work the same way. A page of identical-length paragraphs reads flat; varied lengths breathe.

| Length | Use |
|---|---|
| One sentence | Punch. Emphasis. Pivot. |
| 2-3 sentences | Workhorse paragraph. Most prose lives here. |
| 4-5 sentences | Developing an idea; technical setup. |
| 6+ sentences | Complex argument; rare; risks losing the skim reader. |

Avoid the 200-word paragraph wall. The reader's eye sees a wall and bounces.

### Section length variation

Sections within a long article should also vary. A 3000-word piece with six 500-word sections is monotonous; one with sections of 200 / 600 / 800 / 400 / 700 / 300 reads as deliberately paced.

The reliable check: tally each section's word count. Variance is good. Uniformity is suspicious.

See `references/pacing-and-rhythm.md` for the full pacing toolbox and worked examples.

## Scan-ability

The skim reader scans:

1. The title and dek.
2. Section headings (H2s).
3. The first sentence of each paragraph.
4. Bold text within paragraphs.
5. Lists, tables, and callouts.
6. Closing paragraph.

A piece optimized for scan-ability lets the skim reader leave with the article's main points in 90 seconds. A piece that ignores scan-ability requires linear reading or the skimmer leaves with nothing.

### Scan-ability moves

| Move | Purpose |
|---|---|
| Section headings every 200-500 words | The skimmer's table of contents |
| Sub-headings (H3) when sections have parts | Hierarchy without long sections |
| Topic sentences first | First-sentence-of-paragraph carries the meaning |
| Bold key claims sparingly | Highlight the load-bearing assertion |
| Tables for comparisons | Structured data scans faster than prose |
| Lists for enumerable items | Parallel structure aids scanning |
| Callout boxes for tangents | Removes interrupters from the main flow |
| Pull quotes for memorable lines | Visual anchors; quotable content |

See `references/scannability.md` for the complete scan-ability toolkit and the skim-reader audit.

### Scan-ability anti-patterns

- **Long unbroken sections** (1000+ words without a heading).
- **Topic sentences buried** (first sentence of paragraph is throat-clearing; the actual point is sentence 4).
- **Bold inflation** (everything is bold; nothing stands out).
- **Lists for everything** (three-item lists where prose would carry better).
- **Headings that don't preview content** ("Some thoughts" doesn't tell the skimmer what's there).

## The 30% cut

Every drafted long-form piece can lose 20-40% without changing its meaning. Cut for tightness; the reader feels the difference.

### What to cut

| Category | Examples |
|---|---|
| **Hedges** | "It might be worth considering whether perhaps" → "Consider" |
| **Throat-clearing** | "Now we'll discuss…" → start with the discussion |
| **Recap padding** | "As we saw in the previous section…" → trust the reader |
| **Filler transitions** | "It's important to note that…" → just note it |
| **Redundant adjectives** | "comprehensive, robust, scalable solution" → name the specific quality |
| **Self-conscious meta** | "I'm aware this is a complex topic, but" → just write it |
| **The "in this article we will" preface** | Cut entirely; let the title and hook do the work |
| **Restated points** | A point made twice in the same section; cut one |
| **Generic examples** | Swap for specific ones (and if no specific exists, cut) |
| **Defensive overqualification** | "of course there are exceptions, this isn't always true, you know your context best, but" → trust the reader |

### What not to cut

| Category | Why keep |
|---|---|
| Concrete examples | These are the article's substance |
| Citations | Load-bearing for credibility |
| Voice markers | Personality is hard-won; preserve it |
| Specific numbers and names | The article's grip |
| Genuine qualifications | Real "unless" / "except when" / "limited to" |
| Counter-arguments addressed | Earned credibility |

### The cut in three passes

1. **Pass 1: hedge and filler removal.** Quick. Cut every "I think," "perhaps," "it seems," "in some sense," "kind of," "sort of," "really" that doesn't earn its position.
2. **Pass 2: throat-clearing and meta.** Cut every "in this section," "as we discussed," "now let's look at." The reader can see structure from the headings.
3. **Pass 3: redundancy.** Sentences that say what previous sentences already said. Paragraphs that recap rather than develop. Cut.

After three passes, the draft is typically 30% shorter and reads twice as fast.

See `references/cut-discipline.md` for full cut protocols and examples of well-cut prose.

## The read-aloud test

The single most reliable polish technique. Read the draft aloud, paying attention to where you stumble.

### What you find

| Stumble | What it means |
|---|---|
| Tongue-twisters | Awkward consonant combinations; word order to fix |
| Run-on sentences | Need to break |
| Run-out-of-breath sentences | Same; needs breaks |
| Sentences you can't parse aloud | Reader can't parse silently either |
| Sentences with no rhythm | Add or remove syllables until they sing |
| Flat paragraphs | Need a punch sentence |
| "Wait, what?" moments | Logic break or unstated transition |

### Why it works

Reading silently lets the reader's brain auto-correct. Reading aloud forces the prose to actually work syllable by syllable. Bumps become audible.

### Practical approach

1. Read aloud, slowly.
2. Mark every stumble with a margin note.
3. After the read-through, fix each marked stumble.
4. Re-read the fixed passages aloud.
5. Iterate until the read is smooth.

A 3000-word piece takes 25-40 minutes to read aloud. The polish gain is enormous.

See `references/read-aloud-test.md` for the full protocol, what to do about specific stumble types, and when to delegate the read-aloud to a tool.

## ✅ Use for

- Polishing a long-form draft before publication
- Fixing pacing problems (monotone sentences, monotone paragraphs)
- Improving scan-ability (the skim reader experience)
- Running a 30% cut pass on a bloated draft
- Doing a read-aloud test on a piece
- Tightening a draft that "feels long"
- Equalizing pacing across uneven sections
- Adding callouts, pull quotes, and visual hierarchy

## ❌ NOT for

- **Short-form clarity editing** (RFCs, memos, emails) — use communication/clarity-editing
- **Sentence-level craft techniques** (AIDA, PAS, hooks, voice calibration) — use engaging-craft
- **Outlining or structural changes** — use long-form-structure
- **Code documentation cleanup** — use documentation-generator
- **UI microcopy** — use ux-writing
- **Pre-writing research / sourcing** — use technical-research

## Anti-patterns

### The polish bypass

**What it looks like:** "It's done — let me just publish." The draft goes live without a polish pass.

**Why it's wrong:** Drafted prose is *first-pass* prose. It carries the writer's thinking-out-loud, the half-finished sentences they meant to fix, the hedges they forgot to cut. The reader gets the cost.

**What to do instead:** Treat polish as a non-negotiable phase. Budget 30-60 minutes per 1000 words for polish. The piece nearly always improves dramatically.

### The infinite polish

**What it looks like:** Eight polish passes, each making smaller changes. The piece stays in editorial purgatory.

**Why it's wrong:** After 2-3 polish passes, you're rearranging deck chairs. The piece is done; ship it.

**What to do instead:** Limit polish to 2-3 passes. After that, ship and let real readers reveal the next round of improvements.

### Over-bolding

**What it looks like:** Every other sentence has a bold phrase. The page looks like a highlighter exploded.

**Why it's wrong:** When everything is emphasized, nothing is. The reader's eye stops noticing the bold.

**What to do instead:** Bold sparingly — 1-2 phrases per major section, marking the load-bearing claim. Use other tools (lists, tables, callouts) for visual variety.

### Over-listification

**What it looks like:** Three-item lists where prose would carry better. Lists nested inside lists. Lists of one-word items.

**Why it's wrong:** Lists fragment continuous reasoning. A list of "X, Y, Z" reads as parallel options when the actual claim is "X because Y, which leads to Z."

**What to do instead:** Use lists when items are genuinely parallel (steps, options, items). Use prose when items have logical relationships among themselves.

### The "improvement" that's just rewording

**What it looks like:** Polishing pass that swaps "utilize" for "use" but doesn't actually change the prose's clarity, pacing, or scan-ability.

**Why it's wrong:** Cosmetic rewording isn't polish; it's rearranging. The reader gets no benefit.

**What to do instead:** Polish must change something the reader experiences. Cut a hedge, vary a sentence length, break a long paragraph, surface a buried point. If the change isn't perceptible to a reader, skip it.

### Polish without re-reading

**What it looks like:** A flurry of edits, then publishing. No final read-through.

**Why it's wrong:** Polish edits frequently *introduce* new bumps (broken transitions, inconsistent tense, leftover words from a half-revised sentence). Without a re-read, those ship.

**What to do instead:** After polishing, re-read the piece end-to-end one more time. Fix what you find. Then ship.

### Polish that drifts the voice

**What it looks like:** A conversational draft polished into "professional" prose. The reader notices the voice change.

**Why it's wrong:** Polish should *clarify* the voice, not change it. A piece that started colloquial and ended formal feels like the writer was insecure about the original voice.

**What to do instead:** Decide on the voice (see engaging-craft/references/voice-and-tonality.md). Polish toward the voice you committed to.

## Workflow

1. **Confirm the draft is structurally complete.** If sections are missing or out of order, fix structure first (long-form-structure). Polish doesn't fix structure problems.
2. **Cut pass 1 — hedges and filler.** Fast. Removes ~10%.
3. **Cut pass 2 — throat-clearing and meta.** Fast. Removes another ~10%.
4. **Cut pass 3 — redundancy.** Slower. Removes ~10-20%.
5. **Pacing pass — sentence length variation.** Find monotone sequences; vary.
6. **Pacing pass — paragraph length variation.** Break walls; insert short paragraphs at pivots.
7. **Scan-ability pass.** Audit headings, topic sentences, bold usage, list usage, callouts.
8. **Read-aloud pass.** Mark stumbles; fix; re-read marked passages.
9. **Final end-to-end read.** Catch anything the polish passes broke.
10. **Hand off to distribution-craft** for title, dek, social pulls.

## References

| File | Contents |
|---|---|
| `references/pacing-and-rhythm.md` | Sentence and paragraph rhythm; the variation toolbox; common pacing failures |
| `references/scannability.md` | The skim reader's experience; headings, callouts, lists, tables; visual hierarchy audit |
| `references/cut-discipline.md` | The 30% cut; three-pass cut protocol; what to keep, what to lose; example transformations |
| `references/read-aloud-test.md` | The read-aloud protocol; what stumbles mean; how to revise; when to use TTS |

## Related skills

- **long-form-structure** — fix structural problems before polishing.
- **engaging-craft** — sentence-level craft techniques (AIDA, PAS, hooks, voice).
- **technical-research** — load-bearing claims should already be sourced before polish.
- **distribution-craft** — title, dek, social pull-quotes after the body is polished.
- **communication/clarity-editing** (skillstack) — line-level editing for short-form work writing.
- **storytelling** (skillstack) — narrative pacing for non-technical pieces.
