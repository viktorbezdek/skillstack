# Voice and Tonality

Voice is the consistent personality the writing presents. Tonality is its register at a given moment. Both are choices, not happenstance — and both are perceptible to readers even when they can't name what they're perceiving.

## The six axes

Decide where your piece sits on each axis. Pick deliberately; commit consistently.

### 1. Formality (academic ←→ conversational)

| Academic | Conversational |
|---|---|
| "The implications of this design decision are significant" | "This design decision matters more than it looks" |
| "It is recommended that practitioners…" | "You probably want to…" |
| Passive voice common | Active voice dominant |
| Latinate vocabulary | Anglo-Saxon vocabulary |

Academic suits whitepapers, reference docs, peer-reviewed material. Conversational suits blog posts, tutorials, op-eds. Pick one and stay there — drift is jarring.

### 2. Authority signal (confident ←→ hedged)

| Confident | Hedged |
|---|---|
| "X is wrong" | "X may not always be the right choice in some cases" |
| "Here's what works" | "Here's something that has worked for some teams in some situations" |
| "Don't do this" | "You might consider being cautious about this" |

Excessive hedging is a tell of unconfident writing. Hedge for things you actually want to qualify; don't hedge by reflex. A confident sentence followed by a real qualification ("X is wrong, *unless* Y") is stronger than a hedged sentence ("X might be wrong sometimes").

### 3. Distance (detached ←→ personal)

| Detached | Personal |
|---|---|
| "One observes that…" | "I noticed that…" |
| "The team migrated…" | "We migrated…" |
| Third-person, abstract subjects | First-person, named subjects |
| No personal anecdotes | Personal anecdotes prominent |

Personal voice earns trust through stake. Detached voice earns trust through neutrality. Both work; pick by genre.

### 4. Stake (observed ←→ lived)

Related to but distinct from distance:

| Observed | Lived |
|---|---|
| Writer is reporting | Writer was there |
| Other people's experience | Writer's own experience |
| Synthesis from research | Synthesis from doing |

A piece can be detached *and* lived ("we, our team, the bugs we found") or personal *and* observed ("I researched this; I haven't done it"). The reader notices the combination.

### 5. Pace (patient ←→ urgent)

| Patient | Urgent |
|---|---|
| Long sentences | Short sentences |
| Setup before payoff | Payoff first, setup after |
| Builds the model | Hits the point and moves on |
| Reader takes 30 seconds to process | Reader processes in real-time |

Patient voice fits deep-dives and explainers. Urgent voice fits opinion and calls-to-action. Tutorials are usually somewhere in between (urgent for the steps, patient for the explanations).

### 6. Affect (neutral ←→ opinionated)

| Neutral | Opinionated |
|---|---|
| Reports tradeoffs | Recommends a side |
| Shows multiple views | Argues for one |
| Avoids the writer's preferences | Foregrounds the writer's preferences |

Neutral fits whitepapers and reference docs. Opinionated fits opinion pieces and case studies. The choice should be deliberate: a piece advertised as a comparison that turns out to be opinionated reads as biased; an opinion piece that pretends to be neutral feels evasive.

## Voice profiles

Common voice profiles and where they fit:

### "Engineering blog" voice

| Axis | Position |
|---|---|
| Formality | Conversational |
| Authority | Confident, with calibrated hedges |
| Distance | Personal ("we") |
| Stake | Lived |
| Pace | Mixed — patient for setup, urgent for the lessons |
| Affect | Opinionated within their lane |

Examples: Cloudflare blog, Stripe blog, GitHub Engineering. The voice signals "engineers writing for engineers about real work."

### "Whitepaper" voice

| Axis | Position |
|---|---|
| Formality | Academic |
| Authority | Confident |
| Distance | Detached |
| Stake | Observed |
| Pace | Patient |
| Affect | Neutral |

Examples: NIST publications, ACM reports, McKinsey-style consulting reports. The voice signals "this was rigorous; trust the methodology."

### "Indie hacker" voice

| Axis | Position |
|---|---|
| Formality | Conversational, sometimes informal |
| Authority | Confident, sometimes overconfident |
| Distance | Personal ("I") |
| Stake | Lived |
| Pace | Urgent |
| Affect | Strongly opinionated |

Examples: Pieter Levels, Justin Jackson, certain Hacker News personalities. The voice signals "this is one person's experience and they're not pretending otherwise."

### "Academic blog" voice

| Axis | Position |
|---|---|
| Formality | Mid-academic |
| Authority | Confident with explicit uncertainty |
| Distance | Detached but writerly |
| Stake | Observed (or "lived" for the writer's research) |
| Pace | Patient |
| Affect | Mostly neutral, some opinion |

Examples: Tim Bray's blog, Bret Victor's writing, Nate Soares' writing. The voice signals "this person thinks carefully and isn't trying to sell you anything."

### "Trade publication" voice

| Axis | Position |
|---|---|
| Formality | Mid-formal (journalistic) |
| Authority | Confident, externally cited |
| Distance | Detached (third-person) |
| Stake | Observed |
| Pace | Mid (depends on outlet) |
| Affect | Mostly neutral, with editorial slant |

Examples: Wired, The Information, Stratechery. The voice signals "we're reporting; the analysis is editorial but careful."

## Voice calibration: the four-question test

If you're unsure about voice, answer:

1. **What's the venue?** Personal blog, company blog, journal, magazine?
2. **Who's the reader?** Practitioner, decision-maker, generalist, expert?
3. **What's your relationship to the topic?** Did this, watched this, researched this?
4. **What's the piece's purpose?** Persuade, teach, inform, entertain?

The answers determine the voice. A practitioner reader on a company blog about something the team did to teach others wants Engineering Blog voice. A decision-maker on a trade publication about a research study to inform wants Trade Publication voice.

## Mid-piece voice drift

The most common voice failure: starting in one voice and switching to another mid-piece. Symptoms:

- Hook is conversational; body switches to academic.
- First section uses "I"; later sections use "one."
- Early sections are urgent; later sections are patient (or vice versa).
- Opening is opinionated; body becomes neutral (the writer hedged in revision).

The reader feels the seam without naming it. Trust drops.

### Detecting drift

Read the piece aloud, paying attention to:

- **Pronoun shifts.** "I" → "we" → "one" → "the team" → "you" inside one piece.
- **Register shifts.** "rad" in paragraph 3, "salient" in paragraph 7.
- **Confidence shifts.** Bold claims early, hedged claims late.
- **Subject shifts.** Personal anecdotes give way to abstract observations and vice versa.

### Fixing drift

Pick the voice the *body* wants. The hook is easier to rewrite than 3000 words of body. If hook and body diverge, change the hook to match.

## Register shifts within a single voice

Even with a consistent voice, the *register* shifts within a piece:

| Section | Register |
|---|---|
| Hook | Highest energy; punchiest sentences |
| Setup | Calmer, explanatory |
| Development | Working register; explains, demonstrates |
| Climax / payoff | Higher energy; shorter sentences; punch |
| Close | Settled; provides resolution |

Within "engineering blog" voice, the hook is *more conversational* than the development; the close is *more reflective* than the payoff. Same voice, different registers.

## Voice in collaborative writing

When two people co-write, voice fragmentation is the default failure mode. Three strategies:

1. **Single primary author.** One person writes; the other reviews and suggests. Voice stays unified.
2. **Voice matching.** Co-authors agree on a voice profile up front; each writes their sections in it; one person edits the final pass for consistency.
3. **Acknowledged different voices.** Frame the piece as a dialogue or anthology. "Section 1, by X; Section 2, by Y." This works for some genres (interviews, debates) and badly for most.

Voice fragmentation reads to readers as disorganization, even when the underlying content is good.

## Voice and AI-assisted drafting

A note on the failure mode of AI-by-default writing:

LLMs default to a particular voice — formal, balanced, hedge-heavy, neutral, smooth. It's not bad voice; it's *generic* voice. Pieces drafted with no voice intervention sound like every other piece.

Three corrections:

1. **Pick a voice profile up front** and instruct deliberately (or rewrite to match).
2. **Insert specific voice markers.** First-person where appropriate, opinions where appropriate, sentence-length variation, vocabulary outside the LLM's mid-distribution.
3. **Read aloud.** AI-default prose reads smooth-but-flat aloud. Where it sounds like a press release, rewrite for the human voice you want.

## Voice and authority

Different voices project different kinds of authority:

| Voice | Authority signal |
|---|---|
| Engineering blog | "We did this and it worked" |
| Whitepaper | "We measured this rigorously" |
| Indie hacker | "I tried this and learned this" |
| Academic blog | "I thought carefully about this" |
| Trade publication | "We talked to people and synthesized" |

Mismatched voice and authority reads as posturing. An indie hacker voice making claims about industry-wide patterns ("everyone is doing X") feels presumptuous; an academic voice making claims about lived experience ("we observed") feels detached. Match the voice to the kind of authority the piece actually has.

## Voice anti-patterns

### The unmarked switch

```
Paragraph 1: "We were three engineers, two months in, and we were stuck."
Paragraph 2: "It is well-established in the literature that complex systems exhibit emergent
              properties that may not be predicted from local interactions."
```

The voice flips from personal/lived to academic/observed without acknowledgment. Reader disorientation.

### The hedge accumulation

```
"It might be worth considering whether perhaps in some cases X could potentially be a useful
 approach for some teams under certain circumstances."
```

Each hedge spends authority. By the third hedge, the writer sounds afraid of their own claim. If the claim is uncertain, name the uncertainty crisply ("X works for teams over 50; smaller teams should hold off").

### The borrowed voice

A writer copying another writer's voice. Sometimes works for a while; usually wears thin. The reader senses the imitation.

### The voice-from-nowhere

A piece with no voice at all — neither this nor that — that reads as if the writer didn't decide. The reader feels nothing about the writer; the piece doesn't stick.

### Mismatched voice and venue

Indie-hacker voice on a whitepaper feels unprofessional. Whitepaper voice on a personal blog feels stiff. The venue carries voice expectations; honor or subvert them deliberately.

## Calibrating voice over time

Writers develop voice by writing and revising. Two practices:

1. **Read writers whose voice you admire and analyze it.** Run their prose through the six-axis framework. What makes it work?
2. **Save your own best paragraphs.** Build a "voice canon" of your own work. When drafting, read your canon to recalibrate.

Voice gets better with deliberate practice. It's not a personality trait; it's a craft.
