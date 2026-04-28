# AI-Tells and Substitutions

LLM-generated prose carries a distinct fingerprint — a vocabulary and rhythm shaped by the patterns the model was trained to imitate. Once you can name the fingerprint, you can edit it out. This reference catalogs the specific words, phrases, and structural patterns that signal "AI wrote this" — and the concrete substitutions that bring the prose back to a human register.

## Why this matters

Modern technical readers can spot AI prose in seconds. The cost of getting caught is high: the article reads as effortless to produce, which means it reads as un-earned. Every banned phrase below is a small leak; collectively they tell the reader they're consuming generic content instead of a specific person's thinking.

The discipline is not "avoid AI words because AI bad." It's: **specific language carries voice; generic language carries nothing.** The catalog isn't an arbitrary blacklist — every banned phrase is banned because it was *picked* by the model to sound smart, and the cost of "sounding smart" is "sounding like every other article on the topic."

## The four categories

AI prose leaks through four categories of vocabulary. Catch them in revision.

### 1. High-frequency AI words

Words that LLMs reach for to signal sophistication. They are not wrong; they are *overused* to the point of being a tell.

| AI word | What it means | Plain alternative |
|---|---|---|
| **delve** | to investigate or explore | explore, dig into, examine |
| **underscore** | to emphasize or highlight | highlight, emphasize, make clear |
| **pivotal** | extremely important | important, decisive, central |
| **realm** | a field, domain, area | area, field, world |
| **harness** | to make use of | use, take advantage of |
| **illuminate** | to clarify | explain, clarify, show |
| **leverage** (verb) | to use to advantage | use, apply, exploit |
| **navigate** (figurative) | to move through complexity | work through, handle, manage |
| **myriad** | a great number | many, dozens of, hundreds of |
| **plethora** | an abundance | a lot of, many, an excess of |
| **landscape** (figurative) | environment, field | field, world, situation |
| **paradigm** | a typical example or model | model, approach, framework |
| **ecosystem** (figurative) | a system of interrelated things | system, network, environment |

**Detection rule:** if the word appears more than twice in a 2000-word piece, the prose is leaking. Most can be cut entirely.

### 2. AI transition phrases

LLMs love structured connectives. A few are useful in moderation; most are filler that signal a model is performing "essay shape."

| AI transition | Plain alternative |
|---|---|
| **That being said…** | However…  /  Even so…  /  But… |
| **At its core…** | Fundamentally…  /  Essentially…  /  At root… |
| **To put it simply…** | In simpler terms…  /  Simply put…  /  Plain version: |
| **This underscores the importance of…** | This shows…  /  This means… |
| **A key takeaway is…** | The main point is…  /  One thing to remember: |
| **From a broader perspective…** | When you zoom out…  /  Stepping back… |
| **It's important to note that…** | Note: …  /  Worth flagging: …  /  *(usually deletable)* |
| **In today's fast-paced world…** | *(always deletable)* |
| **In the rapidly evolving landscape of…** | *(always deletable)* |
| **Moreover…  /  Furthermore…** | Also…  /  And…  /  *(often deletable)* |
| **In conclusion…  /  To summarize…** | *(usually deletable — a strong close doesn't need a label)* |

**Detection rule:** "Moreover," "Furthermore," and "It's important to note that" should appear at most once each per article. "That being said," "At its core," and "From a broader perspective" should appear zero times.

### 3. Hedging and softening phrases

LLM RLHF rewards safe, qualified statements. The result: prose that hedges by reflex, conveying caution where commitment would have been right.

| Hedge | When it's earned | When to cut |
|---|---|---|
| **Generally speaking** | When making a real generalization with stated exceptions | When followed by a confident claim — just make the claim |
| **Typically** | When citing actual statistics | When the writer doesn't know if it's typical |
| **Tends to** | When describing a real tendency you observed | When substituting for "is" or "does" |
| **Arguably** | When previewing a contested claim you're about to defend | When used as filler to sound balanced |
| **To some extent** | When the claim has a clear partial truth you'll quantify | When used to avoid commitment |
| **Broadly speaking** | When introducing a true generalization | When followed by specifics that contradict the breadth |
| **It seems** | When you're genuinely uncertain | When you're certain — drop it |
| **It's worth considering** | Almost never | Almost always — cut |
| **Could potentially** | When stacking modal force is intended | Usually one of "could" or "potentially" suffices |
| **May or may not** | When the disjunction is genuinely informative | Almost never |

**Detection rule:** count hedges per paragraph. More than one hedge per 100 words signals reflex hedging. Cut hedges that don't earn their position; commit to the claim.

### 4. Academic and analytical filler

LLMs reach for academic-register verbs to sound rigorous. The verbs are real; their *frequency* is the tell.

| AI verb | Plain alternative |
|---|---|
| **shed light on** | explain, clarify, show |
| **facilitate** | help, enable, make easier |
| **refine** | improve, polish, sharpen |
| **bolster** | strengthen, support, reinforce |
| **differentiate** | distinguish, tell apart, separate |
| **streamline** | simplify, optimize, smooth out |
| **navigate** (figurative) | work through, handle |
| **encompass** | include, cover, span |
| **demonstrate** | show, prove |
| **utilize** | use *(always; "utilize" is "use" with extra syllables)* |
| **ascertain** | find out, determine, check |
| **endeavor** (verb) | try, attempt |
| **commence** | start, begin |

**Detection rule:** the simpler verb is almost always correct. "Utilize" and "leverage" (as a verb) are particularly strong tells — neither has any meaning the simpler word lacks.

### 5. Buzzwords and AI-flavored superlatives

These were once meaningful; LLMs have worn them out.

| Buzzword | Plain alternative |
|---|---|
| **revolutionize** | change, transform, replace |
| **innovative** | new *(or a specific feature, or cut entirely)* |
| **cutting-edge** | new, advanced *(or cut)* |
| **state-of-the-art** | current *(or cut)* |
| **game-changing** | significant *(or cut, often)* |
| **transformative** | impactful, influential *(or cut)* |
| **seamless integration** | works with X *(name the integration)* |
| **scalable solution** | grows with the system *(name the dimension)* |
| **robust** | reliable, well-tested *(or specify)* |
| **comprehensive** | complete *(or specify what's covered)* |
| **leverage synergies** | *(always cut; this phrase has been a parody for 15 years)* |
| **best-in-class** | *(usually cut; substitute a benchmark)* |
| **industry-leading** | *(usually cut; substitute a position)* |
| **mission-critical** | *(usually cut; substitute the consequence of failure)* |

**Detection rule:** if you can replace the buzzword with the word "important" without losing meaning, the buzzword is filler.

## The six AI-prose structural patterns

Beyond vocabulary, AI prose has structural fingerprints.

### Pattern 1: balanced-everything

LLM RLHF favors symmetric prose. Every claim has a counterclaim. Every advantage has a disadvantage. Every paragraph has a topic sentence and an exit sentence.

| Symptom | Fix |
|---|---|
| Every paragraph follows topic-evidence-mini-summary | Break the rhythm. Paragraphs of 1 sentence; paragraphs of 6 sentences; paragraphs that don't summarize. |
| Every claim is paired with "however" | Cut some "howevers." Pick a side. |
| Discussion always leads to "it depends" | Decide what depends. Be specific about the conditions. |

### Pattern 2: the smooth gradient

AI prose flows. Every sentence connects to the next. Every paragraph builds on the previous. There are no jolts, no breaks, no unexpected pivots.

| Symptom | Fix |
|---|---|
| Reads like a single 2000-word stream | Insert hard cuts. Section breaks. Paragraph fragments. |
| Every transition is signaled ("Moreover," "Furthermore") | Cut the signals. Let logic do the bridging. |
| No surprise sentences | Plant one or two off-rhythm sentences per section. |

### Pattern 3: list-of-three syndrome

LLMs love three-item lists. Three benefits, three challenges, three considerations.

| Symptom | Fix |
|---|---|
| Every list has exactly three items | Vary list length. Use 2, 4, 7. |
| Three items are all parallel grammatical structure | Break parallelism for the third item if it carries different weight. |

### Pattern 4: the executive summary tone

AI defaults to a "summarizing intelligent observer" voice. No personal stake. No lived experience. The writer is reporting on the topic from above, not inside it.

| Symptom | Fix |
|---|---|
| First-person pronouns absent | Add "I" / "we" / "our team" where it's true |
| No anecdotes | Add a specific named scene, even if 2 sentences |
| Voice is "balanced expert" with no personality | Pick a voice axis and commit (see voice-and-tonality.md) |

### Pattern 5: the polite hedge cascade

AI adds hedges in stacks. Each one alone is fine; together they signal lack of commitment.

| Symptom | Fix |
|---|---|
| "It might be worth considering whether perhaps in some cases…" | Cut all the hedges; commit to the claim |
| Multiple hedges per sentence | One hedge maximum, only when truly earned |

### Pattern 6: the predictable formatting

AI wraps content in clean structure. Title-case headings. Numbered subsections. Tidy bullet points. Every section ends with a smooth pivot to the next.

| Symptom | Fix |
|---|---|
| All headings are title-case noun phrases | Mix in sentence-case headings, action headings, occasional questions |
| Every list is bullet-formatted | Use prose where the items aren't truly parallel |
| Sections always end with a one-sentence transition | Sometimes just stop |

## The sniff test

Before publishing, scan the draft and check:

1. **Word-frequency tells.** Does any of {delve, underscore, pivotal, realm, harness, illuminate, leverage, navigate, myriad, plethora, landscape, paradigm, ecosystem} appear more than twice? Cut.
2. **Transition tells.** Does {That being said, At its core, From a broader perspective, In today's fast-paced, It's important to note} appear at all? Cut all instances.
3. **Hedge density.** More than one hedge per 100 words? Cut at least half.
4. **Buzzword count.** Any of {revolutionize, innovative, cutting-edge, game-changing, transformative, seamless integration, scalable solution} appear? Replace with a specific descriptor or cut.
5. **First-person count.** Zero first-person pronouns in a piece that should have them? Add stake.
6. **List-length distribution.** Are all your lists three items long? Vary.
7. **Opener.** Does the opening sentence resemble "In today's…" / "In the rapidly evolving…" / "In recent years…"? Rewrite.

## Worked transformation

### Before (AI-prose)

> In today's rapidly evolving software landscape, performance optimization has emerged as a pivotal concern for engineering teams looking to deliver seamless user experiences. To put it simply, the importance of streamlined database queries cannot be overstated. Generally speaking, teams that leverage modern caching strategies tend to facilitate significantly improved response times. That being said, it's important to note that there are myriad approaches, and the cutting-edge solutions of today may not be the best fit for every use case. From a broader perspective, the key takeaway is that businesses must carefully navigate this complex realm to harness the full potential of their infrastructure.

Word count: 105. Information density: low. Specific claims: zero.

AI tells found:
- "In today's rapidly evolving" — opener anti-pattern
- "emerged as a pivotal concern" — pivotal + filler verb
- "looking to deliver seamless" — buzzword
- "To put it simply" — AI transition
- "the importance of … cannot be overstated" — generic emphasis
- "Generally speaking" — hedge
- "leverage" — AI verb
- "tend to facilitate significantly" — hedge + AI verb + filler intensifier
- "That being said" — AI transition
- "it's important to note" — AI transition
- "myriad approaches" — AI word
- "cutting-edge solutions" — buzzword
- "From a broader perspective" — AI transition
- "The key takeaway is" — AI transition
- "navigate this complex realm" — AI verb + AI word
- "harness the full potential" — AI verb + buzzword

The paragraph carries no specific information.

### After (humanized)

> Two of our four busiest endpoints had P99 latencies over 800ms last quarter. We added Redis as a read-through cache in front of the largest two queries — the user feed and the search results page. P99 dropped to 110ms within a week. The cost was one new piece of infrastructure to monitor, plus a cache-invalidation bug we shipped to production twice before we got the TTL strategy right.

Word count: 64. Information density: high. Specific claims: 6 (4 endpoints, 800ms, Redis, 2 queries named, 110ms, 1 week, 2 bug shipments).

The "after" version is shorter, says more, and carries voice. The reader knows what the team did, what worked, and what hurt.

## Substitution by example

Quick substitution table for common AI sentences:

| AI version | Human version |
|---|---|
| "AI is revolutionizing the industry." | "Three of the five teams I talked to are now using GPT-4 for first-draft code review." |
| "We leveraged cutting-edge ML algorithms." | "We used a fine-tuned BERT model from 2019." |
| "This approach offers seamless integration with existing systems." | "It plugged into our Postgres setup with one connection-pool change." |
| "The framework provides robust performance at scale." | "It handled 80k requests/second on a single c5.2xlarge in our load test." |
| "Streamlined workflows facilitate enhanced productivity." | "Removing the approval step shaved 30 minutes off every PR." |
| "It's important to note that there are myriad considerations." | "Three things matter here: latency, cost, and operational simplicity." |
| "From a broader perspective, this represents a paradigm shift." | "If this works, we'll re-architect the next two services the same way." |

## When the AI vocabulary is correct

Not every word on these lists is wrong every time. Some legitimate uses:

- **"Underscore"** as a literal verb in a quote, citation, or annotation context.
- **"Pivotal"** when describing a genuine inflection point (the *pivotal moment* something changed).
- **"Comprehensive"** in titles of works that are comprehensive (e.g., a published reference book).
- **"Demonstrate"** when describing a literal product demo.
- **"Robust"** when contrasting with a known fragile alternative ("our robust retry policy beats the previous best-effort approach").

The discipline isn't "never use these words" — it's "don't reach for them by reflex." When you find one in a draft, ask: did I pick this word because it's the precise word, or because it sounded sophisticated?

## The catalog isn't complete

This list captures the highest-frequency tells. New ones emerge as models update. Two practices help you keep the list current:

1. **Save your own catches.** When you cut an AI-tell from a draft, note it. Over time you build a personal blacklist that matches your model and your topic.
2. **Read prose you wish you'd written.** Track which words and rhythms appear. The gap between "what I admire" and "what I produce" is where editing happens.

## The deeper principle

AI prose isn't bad because of any single word. It's bad because every word is *plausible* but no word is *specific*. The fix isn't to swap synonyms — it's to replace generic claims with specific evidence. The catalog above is just the surface symptom. The structural fix is everywhere else in this skill: concrete-over-abstract, voice-and-tonality, hooks-and-openers. Use this reference for the line-level pass; use the others for the structural one.

The single best diagnostic question, when you suspect AI prose: **Could this paragraph be in any article on this topic written by anyone?** If yes, it's leaking.
