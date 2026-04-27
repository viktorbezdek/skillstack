---
name: strategic-decision
description: Gate workflow for making a strategic decision under uncertainty when multiple options have merit and the stakes are high. Defines the success criteria first (outcome-orientation), maps what actually drives the outcome (systems-thinking), generates options including uncomfortable ones (creative-problem-solving), stress-tests each for blind spots and hidden assumptions (critical-intuition), assesses downside per option (risk-management), ranks using the original criteria (prioritization), and uses outcome-orientation as an end gate — does the top-ranked option actually achieve the outcome we defined? Use for irreversible bets, resource allocation across competing priorities, pivot/persevere decisions, hire-for-speed vs hire-for-quality choices. NOT for reversible decisions with cheap experimentation — just experiment.
---

# Strategic Decision Under Uncertainty

> Most strategic decisions go sideways not because of bad ranking but because the criteria drifted between when the decision was framed and when it was made. This workflow's gate at the end catches that drift.

A high-stakes decision is one where the cost of reversing it is large (time, money, trust, reputation) and the options have meaningfully different futures. Those decisions deserve structure. Reversible decisions don't — just experiment.

---

## When to use this workflow

- Irreversible bets: funding allocation, major hires, platform choices, pivot vs persevere, build vs buy, strategic partnerships
- Decisions under active disagreement where stakeholders are anchored
- Decisions where the "obvious" answer feels off but you can't articulate why
- Decisions that will be judged in retrospect by people who weren't in the room

## When NOT to use this workflow

- **Reversible decisions** — if you can change your mind next week at low cost, just pick one and learn
- **Decisions with clear criteria and clear winners** — don't manufacture complexity
- **Tactical execution decisions** — use `prioritization` directly
- **Decisions where experimentation is cheap** — run the experiment, don't analyze

---

## Prerequisites

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install outcome-orientation@skillstack
/plugin install systems-thinking@skillstack
/plugin install creative-problem-solving@skillstack
/plugin install critical-intuition@skillstack
/plugin install risk-management@skillstack
/plugin install prioritization@skillstack
```

---

## Core principle

**The criteria you set at the start must be the criteria you judge the top-ranked option against at the end.** Criteria drift is the dominant failure mode in strategic decisions. People start with one set of priorities, get attached to an option, and quietly shift the criteria to justify it. The gate at the end of this workflow is a check against that drift.

Secondary principle: **the best option you can imagine in the first 20 minutes is probably not the best option available.** Generate options before you evaluate them. Evaluating early kills creative options.

---

## The phases

### Phase 1 — define success measurably (outcome-orientation)

Load the `outcome-orientation` skill.

Before generating options, answer:

- **What outcome would make this a good decision in 12 months?** Not a feeling ("we'll be in a better place") — a measurable state ("revenue up 30%", "team shipping weekly", "customer retention above 90%").
- **What outcome would make it clearly a bad decision?** This is often more useful than the success definition because it's harder to fool yourself about failure.
- **What are the non-negotiables?** Legal constraints, ethical constraints, existing commitments. Any option that violates these is disqualified regardless of how well it scores elsewhere.
- **What's the time horizon?** A decision that's right in 3 months might be wrong in 3 years, and vice versa. Name the horizon explicitly.

Write these down. You'll return to them at the gate at the end. If you can't articulate them clearly now, you're not ready to decide — you're ready to think more.

### Phase 2 — understand what actually drives the outcome (systems-thinking)

Load the `systems-thinking` skill.

Before generating options, map the system:

- **Feedback loops** — what reinforcing loops make the current state persist? What balancing loops slow change down? Any option that ignores these will underperform.
- **Leverage points** — where in the system would a small intervention have outsized effect? (Meadows' hierarchy: paradigms > goals > power structures > rules > information flows > delays > parameters.) Options that act on high-leverage points are inherently more powerful than options that act on parameters.
- **Delays** — where are the time lags between action and result? Decisions that don't account for delays often look like they're failing when they're just waiting.
- **Stocks and flows** — what accumulates? A one-time fix to a flow problem leaves the stock unchanged.

The system map isn't a pretty artifact — it's a working hypothesis about what actually determines whether any option succeeds. Options will be judged against this map, not against a simpler mental model.

### Phase 3 — generate options, widely (creative-problem-solving)

Load the `creative-problem-solving` skill.

**Generate more options than you need.** If you only have 2-3 options, you haven't generated, you've pre-evaluated. Aim for 6-10 options including ones you don't like. Uncomfortable options are often the most valuable — they reveal what you're protecting.

Techniques from `creative-problem-solving`:
- **Lateral thinking** — what's a reframe that makes the problem look different?
- **SCAMPER** — Substitute, Combine, Adapt, Modify, Put to other use, Eliminate, Reverse. Apply each to the "obvious" option.
- **First principles** — strip the problem to its components and rebuild. The options you thought were the only choices usually turn out to be one of many.
- **Inversion** — what if we did the opposite of our first instinct? What option would someone who strongly disagrees with us generate?
- **The 10th option** — force yourself to generate at least one more option even when you think you're done. The 10th is usually where the insight hides.

Don't evaluate yet. Resist the urge to rank. The goal of Phase 3 is a list of legitimately different options, not a short list.

### Phase 4 — stress-test each option (critical-intuition)

Load the `critical-intuition` skill.

For each option, run:

- **Hidden assumptions audit** — what does this option assume is true that might not be? Assumptions become load-bearing when stress increases.
- **Blind spots check** — what does this option not address? A good option doesn't solve everything, but it should name what it's leaving aside.
- **Red flag identification** — what would make this option dangerous? Unknown unknowns, reversibility concerns, concentration risks.
- **Bias check** — which option do you want to be the answer? That's the one most at risk from motivated reasoning. Stress-test it extra hard.
- **Steelman the alternatives** — construct the strongest possible case for each option you don't prefer. If you can't make a strong case for any alternative, either the alternatives are actually weak or your analysis is shallow. Usually the latter.

Output: for each option, a list of "what would have to be true for this to work" and "what would break this".

### Phase 5 — assess downside systematically (risk-management)

Load the `risk-management` skill.

For each option:

- **Worst realistic outcome** — not catastrophic, just realistic downside. What does failure look like?
- **Probability distribution** — is this 90% works / 10% fails, or 50/50? Don't mask uncertainty with point estimates.
- **Recoverability** — if this option fails, how hard is it to recover? Expensive failures with fast recovery are often better than cheap failures with slow recovery.
- **Insurance mechanisms** — can you hedge? Options with partial hedging dominate otherwise-equal options without hedging.
- **Cost of waiting** — not deciding is also a decision. Map the cost of delay.

Plot the options on a 2x2: expected value on one axis, downside severity on the other. Options in the top-left (high expected value, low downside) dominate. Options in the bottom-right (low expected value, high downside) are easy rejects. The interesting options are in the top-right (high expected value, high downside) — these need explicit risk tolerance.

### Phase 6 — rank using the original criteria (prioritization)

Load the `prioritization` skill.

Score each option against the criteria you set in Phase 1. Not new criteria you came up with during Phases 2-5 — the ORIGINAL criteria. If you're tempted to change the criteria now, that's criteria drift; go back to Phase 1 and articulate what changed.

Pick a scoring method from `prioritization`:
- **RICE** (Reach × Impact × Confidence / Effort) — good for product prioritization but adaptable
- **Weighted scoring matrix** — when criteria have different importance, weight them
- **MoSCoW** — when criteria split cleanly into must-have / should-have / nice-to-have
- **ICE** (Impact × Confidence × Ease) — simpler than RICE when you don't have reach data

The scoring method is less important than the discipline of applying the same scores to all options.

### Phase 7 — the gate: does the top option achieve the outcome? (outcome-orientation, loop)

Return to the `outcome-orientation` skill's Phase 1 criteria.

For the top-ranked option, ask:

- **Would this option, if executed, actually achieve the outcome we defined?** Be concrete. Trace the logic: action → expected effect → does that produce the measurable outcome?
- **If the top option is a no, why did it rank highest?** Usually because the ranking weighted factors that don't drive the outcome.
- **If yes, is the risk acceptable given the worst realistic outcome from Phase 5?**

Three possible answers at the gate:

1. **Yes to both** — decide. Move to execution.
2. **Yes on outcome, no on risk** — look at the second-ranked option; often it's only slightly worse on expected value and significantly better on risk.
3. **No on outcome** — loop back to Phase 3. You don't have the right options yet, or Phase 6 weighted the wrong things.

This loop is the most important part of the workflow. It catches the most common strategic failure: picking the option that ranks best on the criteria you used, when the criteria you used weren't the criteria that actually matter.

### Phase 8 — decide, document, commit

When the gate is cleared:

- **Write down the decision** in one sentence
- **Write down the alternative you rejected** in one sentence — the runner-up
- **Write down the criteria** you used (copied from Phase 1)
- **Write down the trigger for reversal** — what would make you change your mind? What evidence would you need to see? If nothing could reverse it, the decision is faith, not analysis.
- **Commit publicly** to the people who need to know. Waffling after deciding is worse than a suboptimal decision.

This document becomes the postmortem artifact if the decision is judged later. It also makes you a better decider over time — reviewing old decisions against their documented criteria is how calibration actually improves.

---

## Gates and failure modes

**Gate 1: the criteria gate.** Phase 3 cannot start until Phase 1 has produced measurable criteria. If you don't know what success looks like, you don't know what options to generate.

**Gate 2: the generation gate.** Phase 4 cannot start until Phase 3 has produced at least 6 options. Two or three options is pre-evaluation, not generation.

**Gate 3: the outcome gate** (the workflow's main gate). Phase 8 cannot start until Phase 7 has explicitly traced the top option to the Phase 1 outcome. Hand-waving the gate defeats the workflow.

**Failure mode: criteria drift.** The top-ranked option doesn't actually achieve the Phase 1 outcome, but the team has fallen in love with it. They rationalize that "the criteria were always a guide, not a rule". This is the failure the workflow exists to prevent. Mitigation: the gate. Non-negotiable.

**Failure mode: analysis paralysis.** The team loops through Phases 3-7 forever because each cycle reveals new options. Mitigation: time-box. One week for strategic decisions of medium stakes, three weeks for large ones. If you haven't decided by then, the team's bottleneck is commitment, not information.

**Failure mode: sunk cost in options.** Options generated early carry emotional weight by Phase 6, regardless of merit. Mitigation: blind-score Phase 6. Score each option on criteria without looking at what option it is.

**Failure mode: the "obvious" option that isn't.** The team's favorite option from Phase 1 survives every phase because nobody stress-tests it hard enough. Mitigation: Phase 4's steelman-alternatives step. Deliberately construct the strongest case for options you don't like.

---

## Output artifacts

A completed decision produces:

1. **A decision statement** — one sentence, specific
2. **The rejected runner-up** — one sentence, with the reason
3. **The criteria document** — Phase 1's measurable outcome definition
4. **The system map** — Phase 2's mental model of what drives the outcome
5. **A reversal trigger** — what evidence would change the decision
6. **A followup schedule** — when to review whether the decision is working

---

## Related workflows and skills

- For executing the decided option, move to whichever domain workflow fits (pitch-sprint for selling it, zero-to-launch for building it, etc.)
- For team alignment on the decision, use the `pitch-sprint` workflow to produce the internal narrative
- For risk-specific deep-dive, use `risk-management` directly after the gate
- For regular decision-making practice (not just high-stakes), use `prioritization` alone

---

> *Workflow part of [skillstack-workflows](../../../README.md) by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
