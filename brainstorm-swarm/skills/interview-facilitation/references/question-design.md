# Question Design

Prompt patterns for the orchestrator constructing the spawn prompts each persona receives. Get this right and the swarm's contributions are sharp; get it wrong and they're generic.

## The phase-1 prompt template (divergent opening)

```
Topic: [one-sentence framing]

Context:
- [What the team is working on / system being modified]
- [What's already known or decided]
- [Constraints — budget, timeline, team size, technical limits]
- [The specific question the user wants help thinking through]

Your job: Contribute your perspective in your characteristic voice.
Length budget: under 400 words.
```

This template, with persona-specific subagent type, generates a focused contribution from each persona. The template is intentionally minimal — the persona's own system prompt does the rest.

### Variants

**Variant A: with persona-specific question (optional)**

Add one paragraph after the standard prompt, persona-specific:

```
Specifically: [persona-specific question]
```

Examples:

- For **Operator**: "Specifically: what's the on-call burden if this fails at 3 AM?"
- For **Veteran**: "Specifically: what past patterns does this match?"

Use sparingly. Most of the time, the standard prompt + persona's voice is enough.

**Variant B: with constraint reminder**

If a key constraint is non-obvious, repeat it explicitly:

```
Critical constraint: [the constraint]
```

Example: "Critical constraint: this must ship before Q3 board meeting (8 weeks)."

## The phase-2 prompt template (probing)

When you've identified a specific tension from Phase 1, spawn 2-3 personas with this template:

```
Round 1 surfaced this tension:
- [Persona A] said: "[their position]"
- [Persona B] said: "[their position]"

Your job (you are [Persona A or B]):
1. Defend your position with specifics
2. Steelman the other side — what's the strongest version of their case
3. Name the conditions under which the other side would be right
4. Identify the evidence that would settle this
```

This forces engagement with the specific disagreement, not generic perspective-giving.

### Phase-2 variants

**Variant A: introduce a new persona to break the deadlock**

If A and B are stuck, sometimes a third perspective helps:

```
Round 1: A said X, B said Y. Round 2: spawn A, B, AND First-Principles
Thinker — to reframe whether the X-vs-Y framing itself is right.
```

**Variant B: ask both sides to propose a hybrid**

```
Your job (you are A or B):
1. Defend your position
2. Propose a hybrid that captures 70% of your value AND 70% of the
   other side's value
3. Identify what specifically is lost in the hybrid
```

## The phase-3 prompt template (convergent closing)

When the user has a tentative direction:

```
Proposed decision: [the tentative decision]

Your job:
1. Strongest argument FOR this decision (one paragraph, specific)
2. Strongest argument AGAINST (one paragraph, specific — actually steelmanned, not strawmanned)
3. The decisive consideration in your view (one sentence)

You can support or oppose the decision in your "decisive consideration."
Just be clear which side you land on and why.
```

Tight, focused, produces actionable output.

## Question design rules

### Rule 1: open-ended in Phase 1

Phase 1 prompts should be neutral and open. Don't bias the personas toward any answer.

| Bad (leading) | Good (neutral) |
|---|---|
| "Why is this important?" | "What's your perspective on this?" |
| "What are the risks?" | "What are the relevant considerations?" |
| "How should we ship this default-on?" | "How should we approach the rollout?" |

### Rule 2: specific in Phase 2 and 3

Phase 2 and 3 prompts should be specific. Reference the prior round's actual output.

| Bad (vague) | Good (specific) |
|---|---|
| "Go deeper on the disagreement" | "PM said 'ship default-on'; Skeptic said 'opt-in is safer.' Each defend your position with specific evidence and conditions for the other being right." |
| "Pressure-test the decision" | "Decision is 'opt-in offline mode for paid users only.' Each: strongest FOR (paragraph), strongest AGAINST (paragraph), decisive consideration (sentence)." |

### Rule 3: include just enough context

Each persona is a fresh subagent. Give them what they need to be specific to the situation.

Aim for 100-300 words of context. Not more (dilutes the prompt), not less (forces generic contributions).

### Rule 4: trust the persona's voice

Don't overprescribe the contribution. The persona's own subagent definition handles the format and voice. Just give them the topic and context; let them produce.

| Over-prescribed | Trust the persona |
|---|---|
| "PM, give me 5 questions, 3 concerns, a proposed scope cut, and a stakeholder map" | "PM, your perspective on this." |
| "Skeptic, list every possible failure mode in alphabetical order" | "Skeptic, your perspective on this." |

### Rule 5: don't echo the user's bias

If the user has framed the topic with bias ("We MUST add offline mode"), neutralize it in the persona prompts:

```
User's framing: 'We're considering adding offline mode.'
[Not: 'We've decided to add offline mode.' — that constrains the personas]
```

The orchestrator's job is to steel-frame the topic so personas can critique freely.

## Worked example — Phase 1 prompt

User says: "I'm thinking about adding offline mode to our mobile app."

Orchestrator constructs the Phase 1 prompt:

```
Topic: Should we add offline mode to our mobile app?

Context:
- We make a project management mobile app for small teams (2-15 people).
- 80% of usage is on wifi; 20% is on cellular. Real offline use (no
  connectivity) is unmeasured but anecdotally rare.
- Engineering team is 4 mobile devs. Current backlog is full for Q3.
- The ask comes from one enterprise customer who sometimes works on planes.
- Tentative scope: read-only offline for the next quarter; sync for next year.

Your job: Contribute your perspective in your characteristic voice.
Length budget: under 400 words.
```

Spawned to all 6 chosen personas in one message.

## Worked example — Phase 2 probing prompt

After Phase 1, synthesis reveals tension:
- **PM** said: "The single enterprise customer doesn't justify the eng cost."
- **User Advocate** said: "Power users (the 20% on cellular) hit connectivity issues regularly. The enterprise customer is the visible voice; the cellular cohort is the silent one."

Orchestrator constructs the Phase 2 prompt:

```
Round 1 surfaced this tension:
- PM said: "The single enterprise customer doesn't justify the eng cost. We're
  building infrastructure for a request set of one."
- User Advocate said: "Power users on cellular hit connectivity issues regularly.
  The enterprise customer is the visible voice; the cellular cohort is the silent
  one with similar pain."

Your job (you are PM or User Advocate):
1. Defend your position with specifics
2. Steelman the other side
3. Name the conditions under which the other side would be right
4. Identify the evidence that would settle this — what data would convince you?
```

Spawned to JUST PM and User Advocate (2 personas). Tighter focus, deeper engagement.

## Worked example — Phase 3 convergent prompt

After Phase 2, user has a tentative direction: "Read-only offline for power users (Pro plan), shipped behind feature flag for Q3 with explicit opt-in."

Orchestrator constructs the Phase 3 prompt:

```
Proposed decision: Read-only offline for Pro plan users, shipped behind feature
flag for Q3 with explicit opt-in.

Your job:
1. Strongest argument FOR (one paragraph, specific)
2. Strongest argument AGAINST (one paragraph, specific — steelmanned)
3. The decisive consideration in your view (one sentence)

You can support or oppose. Just be clear which side and why.
```

Spawn to 4 personas: Engineer + Operator + Skeptic + User Advocate. The personas form the final pressure-test on the proposed direction.

## Question design anti-patterns

### Stuffing the prompt with prior synthesis

Don't dump 1500 words of "here's everything from Phase 1" into the Phase 2 prompt. The persona doesn't need it. Pull out the specific tension; reference 2-3 prior contributions; leave the rest.

### Generic Phase 2 prompts

"Go deeper" isn't a Phase 2 prompt. It's a vibe. The Phase 2 prompt MUST reference the specific Phase 1 contributions and the specific tension being probed.

### Ignoring the persona's structured format

Don't ask "give me bullet points." The persona's subagent definition already specifies their output format. Trust it.

### Asking for consensus

Phase 3 prompts that say "everyone, agree on the right answer" defeat the swarm. Each persona should be able to land in a different place. The user does the final synthesis.

## Calibration

Iterate on prompt design over multiple swarms. After each brainstorm, reflect:

- Were the contributions specific to the topic, or generic?
- Did the personas surface different angles, or did they converge?
- Did Phase 2 actually deepen the disagreement, or restate Phase 1?

If contributions were generic → context was too thin or too leading.
If personas converged → single-message rule was violated, or the prompt biased toward consensus.
If Phase 2 restated Phase 1 → the Phase 2 prompt didn't tighten the question.

Each pass calibrates the orchestrator's question-design instinct.
