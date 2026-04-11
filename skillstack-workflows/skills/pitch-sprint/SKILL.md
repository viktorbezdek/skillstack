---
name: pitch-sprint
description: Parallel-merge workflow for producing a pitch (investor deck, board proposal, internal funding request, customer sales narrative) in roughly a week. Runs three parallel streams (deep interviews via elicitation, market dynamics via systems-thinking, audience sharpening via persona-definition), merges them into a single storytelling spine, audits via critical-intuition, and polishes every line with ux-writing. Use when you have one week to produce a pitch that must actually land with a specific, named audience and every claim must be grounded in something real. Not for internal status updates, factual reports, or quick sales emails — use plain writing for those.
---

# Pitch Sprint

> Most pitches fail at one of two points: the claims are abstract because nobody ran real interviews, or the draft ships without a self-audit because "we're out of time". This workflow stops both by running the research and audit stages as non-negotiable gates around the writing stage.

A pitch is only as strong as the specific detail underneath it. Abstract claims ("our users love it") signal that no one has done the work. This workflow forces you to do the work.

---

## When to use this workflow

- Investor deck with ≤2 weeks until the meeting
- Board proposal asking for a real decision (funding, strategy shift, reorg)
- Internal funding request competing against other teams
- Customer sales narrative for a named account, not a template
- Founder story refresh ahead of a hiring or fundraising push

## When NOT to use this workflow

- **Routine status updates** — use plain writing
- **Factual reports** where narrative would be distortion — use the `data-storytelling` skill directly
- **Quick sales emails** — one scenario + one call-to-action is enough, no sprint needed
- **You already have the research** — skip to the storytelling merge phase; don't re-interview
- **Audience is vague** — stop, run `persona-definition` first, come back when you can name a specific person

---

## Prerequisites

Install these SkillStack plugins first — the workflow references them explicitly and they provide the depth Claude will draw on in each phase:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install elicitation@skillstack
/plugin install systems-thinking@skillstack
/plugin install persona-definition@skillstack
/plugin install storytelling@skillstack
/plugin install critical-intuition@skillstack
/plugin install ux-writing@skillstack
```

The workflow still gives useful guidance without these installed, but the depth collapses into generic advice. Install them for real sprint use.

---

## Core principle

**Every claim in the pitch must survive the question "where did that come from?"** If the answer is "we think so" or "it feels right", the claim is fiction and will collapse under hostile questioning. If the answer is "we interviewed 12 people last week and 9 of them described this exact situation in their own words", the claim is evidence and stands up.

The sprint structure exists to make sure every major claim has that second kind of answer by the time you write.

---

## The sprint (5 days, compressible to 3)

### Day 1 (parallel streams begin)

Three streams start on day 1 and run in parallel. They do NOT wait for each other.

**Stream A — deep interviews (elicitation skill)**

Run 6-12 interviews with people who are either the target audience of the pitch or who represent the audience the pitch describes (users, customers, internal stakeholders).

From the `elicitation` skill, apply:
- **OARS framework** (Motivational Interviewing): 2:1 reflection-to-question ratio. Most pitch-research interviews fail because they're 100% questions, which produces surface answers.
- **Self-defining memory frames**: "Is there a moment that keeps coming back to you when you think about [problem]?" — this surfaces concrete stories you can quote.
- **Values elicitation techniques**: role model ("who do you admire for handling this well?"), anger-as-signal ("what makes you genuinely angry about the current state?"), decision archaeology ("tell me about a hard choice you made around this").

Output: a notebook of verbatim quotes, specific moments, real numbers, and emotional pivots. Not a summary — actual quotes with attribution.

**Stream B — systems and market dynamics (systems-thinking skill)**

While the interviews are happening, map the system the pitch is intervening in.

From the `systems-thinking` skill, apply:
- **Feedback loops**: what reinforcing loops make the current state persist? what balancing loops slow change down?
- **Leverage points**: where would a small intervention have outsized effect? (Meadows' hierarchy — rules of the system > information flows > delays > parameters)
- **Stocks and flows**: what accumulates, and what drains it?

Output: a one-page diagram or written description of the system, the loops, and the two or three highest-leverage intervention points.

**Stream C — audience sharpening (persona-definition skill)**

In parallel, sharpen who the pitch is for. Not "investors" — which investor? Not "customers" — which customer? The specificity matters because the storytelling phase will write to one specific person.

From the `persona-definition` skill, apply:
- **Goals and pain points**: not generic. For this specific audience member, what are they trying to accomplish this quarter? what keeps them up at night?
- **Empathy map**: what do they hear, see, say, do? what are they thinking that they wouldn't say out loud?
- **Decision criteria**: how do they actually decide "yes" vs "no"? this is the shape of the pitch's ending.

Output: a one-page profile of the specific audience member the pitch is written for.

### Day 2-3 (merge into storytelling spine)

The three streams converge on day 2 or 3. Apply the `storytelling` skill's `business-storytelling` reference to select a structure:

- **StoryBrand 7-part framework** (Donald Miller) — the default choice. Especially important: the audience is the hero, the pitcher is the guide. Almost every weak pitch violates this.
- **Pixar Spine** — use this as a pre-writing prompt to check coherence: "Once upon a time ___. Every day ___. Until one day ___. Because of that ___. Because of that ___. Until finally ___. And ever since ___." If you can't fill every blank with something concrete, the story has a hole.
- **Before-After-Bridge** — for short sections (one slide, one paragraph).
- **Founder story structure** — crucible → search → insight → bet. Use when the pitch depends on personal credibility.

Every beat in the chosen structure should pull from the streams:
- Concrete quotes from Stream A ("Aisha, a nurse manager in Cleveland, told us: [exact quote]")
- System insight from Stream B ("The reason this problem persists isn't awareness — it's that every existing tool optimizes for X, which creates a feedback loop against Y")
- Audience-specific framing from Stream C ("For a VP of Operations evaluating this, the question isn't features — it's whether we can integrate without a six-month implementation")

Output: a draft of the pitch (deck, memo, script) with every claim traceable to a stream.

### Day 4 (audit, do not polish yet)

Run the draft through the `critical-intuition` skill before touching language. The audit asks:

**Specificity audit** — walk through the pitch one sentence at a time. For each sentence, ask: "if a skeptic asked 'says who?', what's the answer?" Flag every sentence where the answer is "we think so". These get rewritten with Stream A material or cut entirely.

**Hero check** — does the pitch treat the audience as the hero, or the company? If the company is the hero, it will land as self-promotion. Rewrite to cast the audience as the hero facing the problem, with the company as the guide who offers the plan. See the `business-storytelling` reference for the full guide vs. hero principle.

**Stakes check** — what happens if the audience does nothing? If you can't answer concretely, the pitch has no urgency and will be deferred. Add the cost-of-inaction — from Stream A quotes, not from speculation.

**Obligatory scene check** — is there a moment in the pitch where the audience feels "okay, yes, this is my problem, I'm in"? If no, the draft is structurally incomplete. This usually goes near the end of the setup, before the reveal of the solution.

**Anti-pattern audit** — check against:
- The company-as-hero anti-pattern
- The feature dump (lists what the product does instead of what the audience gets)
- The vague customer ("enterprises trust us" without naming anyone)
- The unearned transformation ("we saved them $2M" with no narrative arc explaining how)

Output: a marked-up draft with specific fixes, not "this is weak" generalities.

### Day 5 (polish, line by line)

Only now bring in the `ux-writing` skill to tighten every sentence.

- Cut every "we", "our", and "us" you can — replace with a second-person sentence or the audience's name where concrete
- Replace every passive verb with an active one
- Every adjective must be earning its place — delete anything decorative
- Read the whole thing out loud; rewrite every sentence where you stumble
- For decks: each slide's title must stand alone as a headline (the slide's argument in one line)
- For memos: the first sentence of each paragraph must carry the argument for that paragraph — an executive skimming only first sentences should still get the shape

Output: final pitch.

---

## Compressed 3-day version

If you have three days, not five, run this sequence instead:

- Day 1 morning — Stream A (6 interviews, 45 min each)
- Day 1 afternoon — Stream B + Stream C (2 hours each)
- Day 2 — Merge + draft (full day)
- Day 3 morning — Audit (critical-intuition)
- Day 3 afternoon — Polish (ux-writing), final review, ship

The sacrifice: fewer interviews means less quote density. You can still win on quality if the 6 interviews are with the right people.

## Compressed 1-day version (emergency only)

Not recommended, but:

- 2 hours — 3 interviews with the sharpest people you can reach
- 1 hour — System + audience sketch (written, not full frameworks)
- 3 hours — Draft
- 1 hour — Audit
- 1 hour — Polish

The one-day version is a last resort. Warn stakeholders that depth suffers.

---

## Gates and failure modes

**Gate 1: the research gate.** You cannot start writing until Stream A has produced at least 3 concrete, specific quotes you intend to use verbatim. If you don't have quotes, you have opinions.

**Gate 2: the hero gate.** Before day 4 audit, re-read the draft looking ONLY for who the hero is. If the company is the hero, stop and rewrite. A pitch where the company is the hero cannot pass the audit no matter how good the language.

**Gate 3: the stakes gate.** Before polish, the pitch must have a clear, specific answer to "what happens if the audience does nothing?". If the answer is vague, the pitch will not move anyone to action.

**Failure mode: interview fatigue on day 1** — do not let interviewees' phrases bleed into your mental model before the merge. Write exact quotes in the notebook. Paraphrases destroy the specificity you came for.

**Failure mode: loving your draft too much** — if you resist the audit because "it's already good", the audit is catching something real. The resistance IS the signal. Do the audit anyway.

**Failure mode: polish before audit** — if you polish language before the audit, you'll end up polishing the wrong sentences and having to throw them away. Audit first.

---

## Output artifacts

A successful pitch sprint produces:

1. **The pitch itself** (deck / memo / script)
2. **An interview notebook** — reusable for future pitches, marketing copy, and product decisions
3. **A system diagram** — reusable for strategy conversations
4. **A specific persona profile** — reusable for all future communications with this audience
5. **A decision trace** — for each major claim in the pitch, which stream/quote/insight it came from (useful when the audience asks follow-up questions in Q&A)

The by-products are often more valuable long-term than the pitch itself. The sprint forces research work that teams rarely make time for otherwise.

---

## Related workflows and skills

- For data-only presentations (no narrative arc), use `data-storytelling` directly from the `storytelling` skill
- For speeches rather than written pitches, use `speech-and-presentation` from the `storytelling` skill
- For the research methodology alone (not the pitch), use the `elicitation` skill on its own
- For stakeholder mapping beyond a single persona, add the `persona-mapping` skill to Stream C

---

> *Workflow part of [skillstack-workflows](../../../README.md) by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
