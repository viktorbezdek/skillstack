# Compression Patterns

First-draft prose is roughly 30-50% waste. The waste comes from habitual phrases, redundant qualifiers, and abstract nouns. This reference catalogs the most common ones and shows how to cut.

## The 50 wordy phrases

### Length killers (most common)

| Wordy | Compressed | Savings |
|---|---|---|
| in order to | to | 2 words |
| due to the fact that | because | 3 words |
| at this point in time | now | 4 words |
| a majority of | most | 2 words |
| the reason why is that | because | 4 words |
| a number of | several / many / N | 2 words |
| on a daily basis | daily | 3 words |
| for the purpose of | to / for | 3 words |
| in the event that | if | 3 words |
| with regard to | about | 2 words |
| in spite of the fact | despite | 3 words |
| subsequent to | after | 1 word |
| prior to | before | 1 word |
| in the near future | soon | 3 words |
| at the present time | now | 3 words |

### Verb nominalizations

| Nominalized | Verb |
|---|---|
| make a decision | decide |
| perform an evaluation | evaluate |
| conduct an investigation | investigate |
| provide a solution | solve |
| give consideration to | consider |
| come to a conclusion | conclude |
| make a recommendation | recommend |
| have a discussion | discuss |
| reach an agreement | agree |
| put in place | implement |
| carry out | do |
| make reference to | refer to / cite |
| engage in a review of | review |
| undertake an analysis | analyze |
| provide an explanation | explain |

### Filler openers

| Cut | Keep |
|---|---|
| It is important to note that | (delete — or rephrase) |
| It should be pointed out that | (delete) |
| It is worth mentioning that | (delete) |
| Needless to say, | (delete — or say nothing) |
| As you may or may not know | (delete) |
| The fact of the matter is that | (delete) |
| In my honest opinion | (delete) |
| I would like to take this opportunity to | (delete) |

### Meaningless intensifiers

| Cut | Keep |
|---|---|
| very / really / quite / pretty | (usually cut) |
| extremely / incredibly / insanely | (usually cut) |
| totally / completely / absolutely | (usually cut) |
| basically / essentially / fundamentally | (usually cut) |
| literally (when not literally) | (cut) |
| actually (when not contrasting) | (cut) |

### Doublets (picking one)

| Doublet | Pick |
|---|---|
| each and every | each / every |
| full and complete | complete |
| any and all | any / all |
| first and foremost | first |
| various and sundry | various |
| null and void | void |
| over and done with | done |
| unless and until | until |

## Sentence-level compression

### Technique 1: Split at the comma

Sentences over 25 words usually have a comma that should be a period.

**Before:** "The new deploy system reduces time-to-production significantly, and it also improves reliability by allowing rollbacks, so we think the migration is worth the cost."

**After:** "The new deploy system cuts time-to-production and allows rollbacks. The migration is worth the cost."

Word count: 28 → 15. Two ideas, two sentences.

### Technique 2: Delete qualifier chains

Hedges and qualifiers stack. Cut the stack.

**Before:** "We may want to possibly consider looking into the potential for a review of our processes."

**After:** "We should review our processes." — or — "We should consider reviewing our processes."

Word count: 18 → 5 (or 6). Commitment made.

### Technique 3: Collapse redundant clauses

**Before:** "The cache layer, which is responsible for storing frequently-accessed data, was the component that caused the outage."

**After:** "The cache layer caused the outage." — or — "The cache — responsible for hot data — caused the outage."

Word count: 19 → 6 (or 11). The original adds length without adding information.

### Technique 4: Prefer concrete to abstract

**Before:** "The implementation of various optimization techniques resulted in substantial improvements in system performance metrics."

**After:** "Optimization cut p95 latency from 400ms to 120ms."

Word count: 13 → 8, plus added precision.

### Technique 5: Kill "there is / there are"

**Before:** "There are several concerns that the team has about the timeline."

**After:** "The team has several timeline concerns."

Word count: 11 → 6. The "there is/are" construction almost always hides the actor.

### Technique 6: Drop "that" when possible

**Before:** "The reviewer said that the code that we submitted had a bug that needed fixing."

**After:** "The reviewer said the code had a bug to fix."

Word count: 15 → 10. English often tolerates "that" dropping.

## When compression is wrong

Compression has diminishing returns. Stop when:

- **Meaning becomes ambiguous.** If the shorter sentence can be parsed two ways, revert.
- **Warmth is required.** A breakup email or condolence should not be minimally compressed.
- **The audience expects detail.** Academic, legal, or regulatory writing has conventions that override compression.
- **Rhythm matters.** Prose has cadence; compressing every sentence to 8 words produces choppy text.

## The 20% rule

A well-written first draft usually shrinks 20-30% after compression. Shrinking more than 40% suggests the first draft had serious bloat. Shrinking less than 10% suggests you did not actually edit.

If your compression delta is over 50% consistently, reflect on how you write first drafts — you may be padding as a habit.

## Worked example

### Before (138 words)

"I wanted to take a moment to reach out and share some thoughts regarding the upcoming deployment that is scheduled to take place next Tuesday. As you may or may not be aware, there are a number of concerns that have been raised by members of the engineering team with regard to the current state of the rollback plan. It is important to note that the rollback plan has not yet been fully documented, and there is a general feeling among the team that it would probably be a good idea to have a more comprehensive and detailed document prior to proceeding with the deployment. I would like to take this opportunity to suggest that we perhaps consider delaying the deployment by one or two days in order to provide adequate time for the plan to be completed."

### After (42 words, 70% reduction)

"Tuesday's deployment needs a documented rollback plan before we proceed. Engineering has raised the concern; the plan is drafted but not reviewed. Delaying to Wednesday or Thursday gives us time to finalize it. Proposal: push to Thursday. Thoughts?"

What was cut:
- Preamble ("I wanted to take a moment")
- Hedges ("may or may not", "probably be a good idea")
- Nominalizations ("to take place" → passive verb)
- Redundant qualifiers ("comprehensive and detailed")
- Passive voice ("concerns that have been raised" → "Engineering has raised")
- "There are / there is" constructions
- "In order to" → "to"

Nothing of substance was lost.
