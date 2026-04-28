---
name: engaging-craft
description: >-
  Apply proven copywriting techniques to long-form technical content so it
  holds attention from sentence to sentence — and humanize prose that reads
  AI-generated. Covers AIDA, PAS, Before-After-Bridge, Bencivenga's pyramid,
  Sugarman's slippery slide, Schwartz's awareness levels, hook engineering,
  voice and tonality calibration, the concrete-over-abstract discipline, and
  the AI-prose-tell catalog (banned high-frequency AI words like delve /
  underscore / pivotal / leverage; AI transitions like "that being said" /
  "at its core"; reflex hedges; academic filler verbs; buzzwords like
  revolutionize / cutting-edge / seamless integration; the six structural
  fingerprints; the sniff test). Use when the user asks to make an article
  more engaging, write a hook, calibrate voice, humanize AI-generated prose,
  remove AI tells, fix robotic or generic copy, replace abstract claims with
  concrete examples, or apply a copywriting formula. NOT for outlining or
  section structure (use long-form-structure). NOT for line-level clarity
  editing of short-form work writing (use communication/clarity-editing).
  NOT for research or sourcing (use technical-research). NOT for narrative
  storytelling craft (use storytelling).
---

# Engaging Craft

> Engagement is earned sentence by sentence. The reader's attention is renewed every paragraph; if a paragraph doesn't earn the next one, the reader leaves. Most technical articles fail not because the structure is wrong, but because the prose is generic enough that any paragraph could be cut without loss.

This skill covers the sentence-and-paragraph-level craft of long-form technical writing — the proven copywriting techniques that translate to technical content, and the disciplines that distinguish prose written *to be read* from prose written *to be archived*.

## Core principle

**Engagement is concrete, specific, and earned.** Abstract assertions need to be paid for in concrete examples. Named things beat generic things. Demonstrated claims beat asserted ones. Sentences that could appear in any article about anything will be skipped.

## The proven formulas

Copywriters spent the 20th century cataloging what makes prose hold attention. Most of that craft transfers to technical content; almost none of it is taught to engineers.

The five formulas worth learning:

### AIDA — Attention, Interest, Desire, Action

The oldest formula. Originated in advertising; widely applied to long-form persuasion.

| Phase | Reader's state | Your job |
|---|---|---|
| **Attention** | "Why should I look at this?" | A hook that creates curiosity |
| **Interest** | "Why should I read more?" | A promise that the topic affects the reader |
| **Desire** | "Why should I want this?" | The payoff matters; the reader sees themselves benefiting |
| **Action** | "What should I do now?" | A clear next step |

In technical content: Attention is the hook. Interest is the promise. Desire is the development that builds the case. Action is the close.

### PAS — Problem, Agitate, Solve

The high-conversion direct-response formula. Especially useful in opinion pieces and case studies.

| Phase | Move |
|---|---|
| **Problem** | Name the problem the reader has |
| **Agitate** | Make the cost of the problem visible — what it's costing them now, what it'll cost in 6 months, what it's *already* cost |
| **Solve** | Present the solution as the relief |

In technical content: works for "your CI is slow" → "compounded across your team it's costing N engineer-weeks per quarter" → "here's how to halve it."

Caution: agitation must be honest. Manufactured urgency feels manipulative; real cost-naming feels like the writer respects the reader's situation.

### BAB — Before, After, Bridge

A gentler cousin of PAS. Useful for tutorials and case studies.

| Phase | Move |
|---|---|
| **Before** | The reader's current state |
| **After** | What life looks like after applying this |
| **Bridge** | The path from Before to After (the article's content) |

### Bencivenga's pyramid (skepticism gradient)

Gary Bencivenga's insight: every reader starts skeptical. Each claim spends a little credibility; each piece of evidence earns it back. Sequence matters — claims that seem outlandish on first read can land if you've earned credibility first.

| Position in piece | What lands |
|---|---|
| **Opening** | Hyper-specific, verifiable claims (low credibility cost) |
| **Early development** | Conventionally believable claims with strong evidence |
| **Mid-development** | Conventionally believable claims with mixed evidence |
| **Late development** | Outlandish-seeming claims that follow from accumulated evidence |
| **Payoff** | The reframing that wouldn't have worked if stated up front |

Practical: don't lead with your most controversial claim. Lead with the verifiable observation that *implies* the controversial claim, build the case, then state the controversial claim where the reader is ready for it.

### Sugarman's slippery slide

Joseph Sugarman: every sentence has one job — to get the reader to read the next sentence. The reader is on a slide; you're greasing it.

Practical implications:

- Short, punchy openers hold attention better than long, balanced ones.
- Curiosity gaps (questions, partial reveals) pull the reader forward.
- Concrete language is grippier than abstract.
- White space and short paragraphs are part of the slide — long unbroken text adds friction.

For technical writing, Sugarman's discipline is corrective: technical writers tend to over-pack sentences. Sugarman trains you to break sentences open, give the reader breathing room, and let the slide carry them.

### Schwartz's awareness levels

Eugene Schwartz: the reader's awareness of the problem and the solution determines how you frame the piece. Five levels:

| Level | Reader's awareness | Frame your hook around |
|---|---|---|
| **Unaware** | Doesn't know the problem exists | The symptom; the cost; "here's what's happening" |
| **Problem-aware** | Knows the problem; doesn't know solutions | The problem named precisely; "you've felt this; here's why it happens" |
| **Solution-aware** | Knows solutions exist; doesn't know yours | The differentiator; "here's a different way" |
| **Product-aware** | Knows your specific solution; not convinced | The objection-handling; "here's why this is different / better" |
| **Most aware** | Already convinced; needs the next step | The action; "here's what to do this week" |

Most technical articles are pitched at Problem-aware or Solution-aware readers. A common failure is pitching to Most-aware (assuming the reader already cares deeply about the problem); the article reads as preaching to a choir that isn't listening.

See `references/proven-formulas.md` for full applications of each formula with worked examples.

## Hook engineering

Hooks are the highest-leverage 200 words in any article. A weak hook loses readers who would have valued the rest.

### Eight hook types

| Type | When it works | Example pattern |
|---|---|---|
| **Misconception** | Reader has a wrong model | "Most engineers think X. The reality is more interesting." |
| **Surprising fact** | Specific, citable | "In 2023, the average X was Y. Not Z. Y." |
| **In-medias-res** | Narrative, case study | "At 02:47 AM on a Sunday, our database stopped accepting writes." |
| **Question** | The reader has implicitly wondered | "You know X is bad. Have you ever looked at exactly *why*?" |
| **Artifact** | Code, output, chart that creates curiosity | A terminal output showing the surprising number |
| **Failed expectation** | Story-shaped | "We did X. We expected Y. We got Z." |
| **Consequential question** | High stakes | "If your CI is 12 minutes, what does that cost you per quarter?" |
| **Intellectual provocation** | Opinion | "There is no such thing as X. There is only Y being paid by Z." |

See `references/hooks-and-openers.md` for the full library with selection guidance and worked examples.

### Hooks that don't work

- "In today's fast-paced digital landscape…"
- "Have you ever wondered…" (rhetorical and presumptuous)
- "We all know that…"
- "It's no secret that…"
- "Picture this:" (followed by something unmemorable)
- "Imagine you're a [role] who…"
- "Once upon a time…" (in a non-narrative piece)

These signal generic content. Readers notice within three seconds and bounce.

## Voice and tonality

Voice is the consistent personality the writing presents. Tonality is its register at a given moment. Both are choices, not happenstance.

### Voice axes

Decide where your piece sits on each axis. Pick deliberately; commit consistently.

| Axis | Pole A | Pole B |
|---|---|---|
| **Formality** | Academic | Conversational |
| **Authority signal** | Confident | Hedged |
| **Distance** | Detached | Personal |
| **Stake** | Observed | Lived |
| **Pace** | Patient | Urgent |
| **Affect** | Neutral | Opinionated |

A "patient, conversational, lived" voice produces in-the-trenches engineering blog. A "confident, detached, neutral" voice produces a whitepaper. Neither is right or wrong; mismatched voice is wrong.

### Mid-piece voice drift

A common failure: the hook is conversational, the body switches to academic. The reader feels the seam. Fix in revision: pick the voice the *body* wants and rewrite the hook to match.

See `references/voice-and-tonality.md` for the voice calibration framework, register-shifting techniques, and worked examples.

## Concrete over abstract

The single most important sentence-level discipline.

### The principle

| Abstract | Concrete |
|---|---|
| "Performance was significantly improved." | "P99 dropped from 480ms to 120ms." |
| "Many engineers struggle with this." | "I've watched four teams hit this in the last year." |
| "The migration was challenging." | "The migration broke 47 tests; we fixed 41 in two weeks; the remaining 6 took six months." |
| "Code quality matters." | "We had three production incidents in Q3 attributable to a single function nobody had reread since 2021." |
| "Modern systems are complex." | "Our microservices stack has 12 services; tracing a single user request touches 8." |

Concrete prose grips. Abstract prose washes over. The discipline is to *find* the concrete equivalent of every abstract sentence — and almost always there is one.

### Three substitutions

1. **Numbers replace adjectives.** "Significantly faster" → "3x faster" or "40ms faster on P99."
2. **Names replace categories.** "A modern framework" → "Next.js 14" or "the Phoenix LiveView team."
3. **Demonstrations replace assertions.** "X is hard to debug" → "Here's a 20-line repro that fails in three different ways depending on timing."

### When abstract is right

Abstract has its place — when generalizing across many specifics. "Many production systems exhibit this pattern" is appropriate after you've shown three. The discipline is to *earn* the abstract by paying for it in concrete.

See `references/concrete-over-abstract.md` for substitution patterns, the "why this not that" diagnostic, and the abstract-to-concrete revision pass.

## AI-prose tells (the humanization pass)

Modern technical readers can spot LLM-generated prose in seconds. The cost of getting caught is high — the article reads as effortless to produce, which means it reads as un-earned. Five categories of leak:

| Category | Examples (cut these) |
|---|---|
| **High-frequency AI words** | delve, underscore, pivotal, realm, harness, illuminate, leverage, navigate (figurative), myriad, plethora, landscape (figurative), paradigm, ecosystem |
| **AI transitions** | "That being said…", "At its core…", "From a broader perspective…", "It's important to note that…", "In today's fast-paced…", "Moreover", "Furthermore" |
| **Reflex hedges** | "Generally speaking", "Typically", "Tends to", "Arguably", "To some extent", "Broadly speaking", "It seems", "It's worth considering" |
| **Academic filler verbs** | shed light on, facilitate, refine, bolster, differentiate, streamline, encompass, demonstrate, utilize, ascertain |
| **Buzzwords** | revolutionize, innovative, cutting-edge, state-of-the-art, game-changing, transformative, seamless integration, scalable solution, robust, comprehensive |

The discipline is not "avoid AI words because AI bad." It's: **specific language carries voice; generic language carries nothing.** Every banned phrase above is banned because it was *picked* by the model to sound smart, and the cost of "sounding smart" is "sounding like every other article on the topic."

### Six structural AI fingerprints

Beyond vocabulary, AI prose has structural tells:

1. **Balanced everything** — every claim has a counterclaim; every advantage paired with disadvantage.
2. **Smooth gradient** — no jolts, no breaks, no surprise sentences.
3. **List-of-three syndrome** — every list has exactly three parallel items.
4. **Executive summary tone** — no first-person, no anecdotes, no stake.
5. **Polite hedge cascade** — multiple hedges stacked per sentence.
6. **Predictable formatting** — title-case headings, three-bullet lists, every section closes with a smooth transition.

### The sniff test (run before publishing)

1. Does {delve, underscore, pivotal, realm, harness, illuminate, leverage, navigate, myriad, plethora} appear more than twice? Cut.
2. Does {That being said, At its core, From a broader perspective, In today's fast-paced, It's important to note} appear at all? Cut all instances.
3. More than one hedge per 100 words? Cut at least half.
4. Any of {revolutionize, innovative, cutting-edge, game-changing, transformative} appear? Replace with a specific descriptor or cut.
5. Zero first-person pronouns in a piece that should have them? Add stake.
6. All your lists three items long? Vary.
7. Opening sentence resembles "In today's…" / "In recent years…" / "In the rapidly evolving…"? Rewrite.

The single best diagnostic question, when you suspect AI prose: **Could this paragraph appear in any article on this topic written by anyone?** If yes, it's leaking.

See `references/ai-tells-and-substitutions.md` for the full catalog with concrete substitutions, worked transformations, and structural-pattern fixes.

## Sentence-level pacing

Long sentences are slow; short sentences are fast. Vary deliberately.

### The slow-down

Long sentences with multiple clauses slow the reader. Use them when introducing complexity, when the reader needs to absorb a model, or when the prose itself benefits from rhythm.

```
"VACUUM, the maintenance operation that exists because Postgres uses MVCC and MVCC means dead
 tuples accumulate, runs in two modes — autovacuum, the background daemon that triggers based on
 thresholds, and manual VACUUM, the one you run when autovacuum couldn't keep up — and the
 distinction matters for diagnosing the failure mode we're about to walk through."
```

That sentence introduces three concepts. The length signals "absorb this."

### The speed-up

Short sentences accelerate. Use them at section breaks, in transitions, when delivering payoffs, and when emphasizing.

```
"VACUUM didn't run.

That was the bug."
```

Two sentences, eight words. Maximum velocity.

### The varied paragraph

Mix in the same paragraph. Long-then-short is satisfying; short-then-long takes a deeper breath.

```
"Postgres MVCC keeps both versions of an updated row, so concurrent readers see consistent
 snapshots even as writes happen — that's the elegant part. Then come the dead tuples.
 They accumulate. VACUUM cleans them up, but only if it can run. And when can it not run?
 When a transaction stays open."
```

Long-then-short. The reader absorbs the model in the long sentence; the short sentences underline the punchline.

## Callbacks and motifs

A motif is an image, phrase, or example that recurs through the piece. Callbacks reward the careful reader.

```
Section 1:  "...like a librarian shelving books that nobody can read until they're catalogued."
Section 4:  "...so the librarian is still shelving, but nobody's catalogued anything since
            yesterday."
Section 7:  "Find the librarian. Free the librarian."
```

The same image, three times, takes on meaning each time. The reader who's been paying attention feels rewarded; the reader who hasn't still gets the point.

Motif rules:

- Earn the first instance with concrete utility (it explains something).
- Don't force callbacks just because. The third instance must do work.
- Keep the motif's vocabulary stable. "The librarian" each time, not "the librarian / the cataloger / the bookshelf-keeper."

## ✅ Use for

- Making an existing article more engaging (sentence-level)
- Engineering a hook for a piece in progress
- Calibrating voice and tonality
- Replacing abstract claims with concrete examples
- Applying AIDA / PAS / BAB / Bencivenga / Sugarman / Schwartz to a draft
- Fixing prose that feels generic or asserted
- **Humanizing AI-generated prose** — removing the high-frequency AI words (delve, underscore, pivotal), AI transitions ("that being said"), reflex hedges, academic filler, and buzzwords (revolutionize, cutting-edge) that signal generic LLM output
- Adding callbacks and motifs

## ❌ NOT for

- **Outlining or section-level structure** — use long-form-structure
- **Line-level clarity editing** (active voice, hedge removal) — use long-form-polish or communication/clarity-editing
- **Research, sourcing, or citation** — use technical-research
- **Narrative storytelling craft** (character arcs, scene construction) — use storytelling
- **UI microcopy, button labels** — use ux-writing

## Anti-patterns

### The AI-prose tell

**What it looks like:** Smooth, balanced, hedge-laden prose. Every sentence has equal weight. Every claim is qualified. The piece reads as if it were averaging across all possible articles on the topic.

**Why it's wrong:** The reader feels that no specific person wrote this. Engagement requires a *voice*, and AI-by-default writing lacks one.

**What to do instead:** Read the draft aloud. Where does it sound like a human? Where does it sound like a press release? Rewrite the press-release sentences with stake, opinion, and specific details. Cut hedges. Use first-person where appropriate. Pick a voice and commit.

### The asserted authority

**What it looks like:** "It's well-known that…" "Most experts agree…" "Industry best practice is…" — claims about consensus that the reader can't check.

**Why it's wrong:** Authority should be demonstrated, not asserted. Each "well-known" claim spends credibility without earning it.

**What to do instead:** Replace authority claims with specific evidence. "Three Postgres committers I asked separately said…" beats "well-known among Postgres experts." Or remove the framing entirely and just make the claim with evidence.

### Abstract everywhere

**What it looks like:** Three pages of generic prose. "Performance," "complexity," "tradeoffs," "modern systems," "engineering teams." No numbers, no names, no specific examples.

**Why it's wrong:** The reader could replace any noun with any other noun and the article would still parse. That means none of the nouns are doing real work.

**What to do instead:** Run the abstract-to-concrete pass. For every abstract noun, find the concrete equivalent. If you can't, the prose may be hiding that you don't have the specifics.

### Listicle prose

**What it looks like:** "First, X is important. Second, Y is also important. Third, Z is important too." Each "point" gets a paragraph; the paragraphs don't build on each other.

**Why it's wrong:** Looks like development; actually accumulation. The reader collects items rather than absorbing an argument.

**What to do instead:** Decide which point is the *thesis* and which are *evidence for the thesis.* Restructure so the thesis is stated and the others support.

### The deflated payoff

**What it looks like:** A 3000-word build-up that lands on "...so the answer is, it depends."

**Why it's wrong:** The reader spent 15 minutes for a non-answer.

**What to do instead:** If the answer really is "it depends," promise *a framework for thinking about it* up front. Then deliver the framework. The reader who wanted "depends on what?" is satisfied; the reader who wanted a single answer was misaligned with the article from the start.

### Voice drift

**What it looks like:** A conversational hook gives way to a corporate-academic body that gives way to a punchy close. The piece feels like three different writers.

**Why it's wrong:** The reader unconsciously feels the seams. Trust erodes; engagement drops.

**What to do instead:** Pick the voice the body wants (it's hardest to change). Rewrite the hook and close to match.

### Sugarman violation: the long unbroken paragraph

**What it looks like:** A 200-word paragraph with no break, no list, no breathing room.

**Why it's wrong:** The reader's eye sees a wall and bounces. Even if the content is excellent, the visual signal is "this is going to be hard."

**What to do instead:** Break long paragraphs at logical pivots. Aim for 50-100 word paragraphs in the development sections. Use short paragraphs to deliver punch lines.

## Workflow

1. **Confirm voice.** Before drafting, decide the six voice axes.
2. **Engineer the hook.** Pick a hook type; draft 2-3 candidates; pick the best.
3. **Pick a formula** if relevant (AIDA, PAS, BAB) and lay out the moves.
4. **Draft with concrete bias.** When you reach for an abstract noun, ask "what's the concrete?"
5. **Sentence-level pass** — vary length, break long unbroken paragraphs, deliver short punch lines at key beats.
6. **Callback engineering** — identify a motif; reuse it across sections.
7. **Read aloud.** Find the bumps. Rewrite the bumps.
8. **Hand off to long-form-polish** for pacing, scan-ability, and the cut.

## References

| File | Contents |
|---|---|
| `references/proven-formulas.md` | AIDA, PAS, BAB, Bencivenga's pyramid, Sugarman's slippery slide, Schwartz's awareness levels — full applications with technical-content examples |
| `references/hooks-and-openers.md` | Eight hook types with selection guidance and worked openers |
| `references/voice-and-tonality.md` | Voice calibration framework (six axes), register-shifting, mid-piece drift detection |
| `references/concrete-over-abstract.md` | The substitution disciplines, the abstract-to-concrete revision pass, when abstract is correct |
| `references/ai-tells-and-substitutions.md` | Full catalog of AI-prose vocabulary tells (high-frequency words, transitions, hedges, academic filler, buzzwords) plus the six structural AI fingerprints, the sniff test, and worked humanization transformations |

## Related skills

- **technical-research** — concrete examples come from research; you can't write specific without sourcing specific.
- **long-form-structure** — engagement at sentence level depends on structural payoff at article level.
- **long-form-polish** — pacing across paragraphs and sections after the draft exists.
- **distribution-craft** — title and dek inherit voice from the body.
- **storytelling** (skillstack) — narrative craft for non-technical pieces; engaging-craft is the technical-content cousin.
- **communication/clarity-editing** (skillstack) — line-level clarity editing for short-form work writing.
