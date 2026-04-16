---
name: clarity-editing
description: >-
  Edit written text for clarity and conciseness — active voice, hedge and
  weasel-word removal, jargon strip, sentence compression, nominalization
  fixes, and readability. Use when the user asks to tighten, shorten, edit,
  or clarify a paragraph or doc, remove hedges and weasel words, convert to
  active voice, cut jargon, kill passive voice, fix nominalizations, or
  improve readability. NOT for structuring the overall doc (use
  structured-writing). NOT for UI microcopy (use ux-writing). NOT for
  auto-generating docs from code (use documentation-generator). NOT for
  design-system content/tone (use consistency-standards).
---

# Clarity Editing

Good writing is rewriting. First draft: get the thought on the page. Second draft: make the thought disappear behind the sentence. This skill is the second draft.

## The four editing passes

Run in order. Each pass targets one problem.

### Pass 1 — compress

Cut every word that does not carry its weight. Typical savings: 20-40%.

| Cut | Keep |
|---|---|
| "in order to" | "to" |
| "due to the fact that" | "because" |
| "at this point in time" | "now" |
| "a number of" | "several" / "many" / a number |
| "is able to" | "can" |
| "make a decision" | "decide" |
| "in the event that" | "if" |
| "on a daily basis" | "daily" |

Sentence-level compression: if a sentence is over 25 words, look for a comma that could be a period.

### Pass 2 — active voice

Passive voice hides the actor and adds words.

| Passive | Active |
|---|---|
| "A decision was made by the team to defer the launch." | "The team deferred the launch." |
| "It has been observed that users are churning." | "Users are churning." |
| "The bug was caused by the cache layer." | "The cache layer caused the bug." |

Exceptions — use passive when:
- The actor is irrelevant ("the package was delivered").
- The actor is unknown.
- You deliberately de-emphasize the actor (accountability writing).

Default: active. Every passive sentence should be deliberate.

### Pass 3 — strip hedges

Hedges and weasel words sap authority.

| Hedge | Strip to |
|---|---|
| "I think that it might be a good idea to" | "" (delete) or "We should" |
| "It seems like there may be some concern that" | "Users worry that" |
| "We should probably consider possibly doing" | "We should do" |
| "In our opinion, it's arguably" | "" (delete) |
| "Kind of" / "sort of" / "basically" | delete |

If you are genuinely uncertain, say so with a number ("60% confidence") or a named unknown, not a pile of hedges.

Full list and the "hedge audit" technique in `references/hedge-and-jargon-removal.md`.

### Pass 4 — fix nominalizations

A nominalization is a verb disguised as a noun. They make sentences abstract and slow.

| Nominalized | Verb form |
|---|---|
| "perform an evaluation of" | "evaluate" |
| "make a recommendation" | "recommend" |
| "conduct an investigation" | "investigate" |
| "have a discussion about" | "discuss" |
| "put in place" | "implement" |

Verbs are active. Nouns-that-used-to-be-verbs are not. Prefer the verb.

## The clarity checklist

Before shipping:

- [ ] Longest sentence under 25 words
- [ ] Every passive sentence is deliberate
- [ ] No hedges except where confidence is genuinely low
- [ ] No jargon the reader does not already use
- [ ] No nominalizations that could be verbs
- [ ] Each paragraph makes one point
- [ ] The opening sentence is the most important sentence

## Readability

Aim for reader effort appropriate to the audience.

| Audience | Target grade level | Tool |
|---|---|---|
| General/executive | 8-10 | Hemingway, readability APIs |
| Engineering internal | 10-12 | Same |
| Academic / legal | 12+ | Same, but know you're excluding readers |

Readability scores are rough signals, not verdicts. A sentence can be readable and wrong, or hard-to-read and correct. Use as a sanity check, not a judge.

## Jargon

Every field has legitimate terminology. The test: does the word carry information the reader cannot get another way?

- **Retain:** terms with specific meaning in your audience's field ("idempotent", "p95", "cohort retention").
- **Cut:** corporate filler ("synergy", "leverage" as a verb, "circle back", "touch base").
- **Define:** terms the reader probably does not know on first use.

A sentence with three pieces of jargon usually needs two of them removed.

## Anti-patterns

- **Pre-editing cuts** — compressing a first draft so aggressively that meaning is lost. Write long first, cut second.
- **Sterilizing voice** — removing so much hedging and personality that the text reads like a machine. Clarity ≠ neutrality.
- **Chained compressions** — compressing a compressed sentence until it's gibberish. Stop when the sentence is clear.
- **Style over substance** — endless passes on words without fixing a structural problem. If the draft is poorly structured, use `structured-writing` first.
- **"Active voice everywhere"** — dogmatic use of active voice when passive is warranted.
- **"Readability score above 80"** — treating the score as the goal rather than the signal.

## Workflow

1. **Fix structure first.** If the doc is poorly structured, no amount of editing fixes it (use `structured-writing`).
2. **Compress.** Pass 1. Expect 20-40% shrinkage.
3. **Active voice.** Pass 2. Every passive becomes deliberate.
4. **Strip hedges.** Pass 3. Authority or explicit uncertainty, nothing in between.
5. **Fix nominalizations.** Pass 4. Verbs over nouns-pretending-to-be-verbs.
6. **Read aloud.** If you stumble, the reader stumbles. Fix the stumble.
7. **Check the checklist.** Ship.

## References

| File | Contents |
|---|---|
| `references/compression-patterns.md` | 50+ wordy phrases with their compressed form; sentence-level compression techniques |
| `references/hedge-and-jargon-removal.md` | Full hedge list, jargon audit, when to keep a hedge, domain-specific jargon guidance |
| `references/editing-examples.md` | Before/after passages showing all four passes applied to real texts |

## Related skills

- **structured-writing** — fix structure before fine editing.
- **ux-writing** — microcopy has different rules (brevity at extreme, voice matters).
- **stakeholder-alignment** — RFC prose benefits from both structure and editing.
- **visual-communication** — sometimes the edit is "replace this paragraph with a diagram."
