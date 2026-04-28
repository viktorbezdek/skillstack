---
name: swarm-protocol
description: >-
  Orchestration logic for running a parallel persona-swarm brainstorm — when
  to invoke, which subset of the 12 canonical personas to spawn (PM, Engineer,
  Designer, Skeptic, User Advocate, Pre-Mortem Specialist, Junior, Veteran,
  First-Principles Thinker, Constraint-Setter, Optimist, Operator), how to
  spawn them in parallel via the Task() tool with persona-specific subagent
  types, how to handle their outputs, and when to do a second round. Use when
  the user asks to brainstorm with multiple perspectives, run a persona swarm,
  get a virtual roundtable, workshop an idea from PM/engineer/designer/skeptic
  angles, pre-mortem a decision, or invoke the brainstorm-swarm. NOT for code
  review (use code-review). NOT for single-perspective interviews (use
  elicitation or deep-interview). NOT for executing or building things (use
  team or autopilot). NOT for designing custom personas — that's the
  custom-personas skill. NOT for the synthesis output formatting — that's
  the swarm-synthesis skill.
---

# Swarm Protocol

> A persona swarm is parallel by design. Spawning 6 subagents one at a time defeats the point — they all see each other's work and converge. The value is in the dissent that emerges when each sees only the topic.

This skill owns the orchestration logic. It teaches when to invoke a swarm, how to choose the right persona subset, how to spawn them in true parallel via the Task() tool, and how to handle the returned outputs (with the synthesis handed off to `swarm-synthesis`).

## Core principle

**Spawn in parallel. Synthesize sequentially.** Each persona is a real subagent — separate context, separate prompt, separate output. The orchestrator's job is to launch them all in one message (so they truly run in parallel), then wait for all returns before synthesizing.

## When to invoke a swarm

The swarm is the right tool when:

- The decision is non-trivial and the team would benefit from multiple perspectives
- You're early enough in thinking that disagreement is useful (not yet committed)
- The topic touches multiple disciplines (design, eng, business, security, etc.)
- You sense you might be missing a perspective and want to surface it

The swarm is NOT the right tool when:

- The task is execution (use `team` / `autopilot`)
- The decision is already made and you just need a doc
- The topic is narrow enough for a single perspective (just talk to one persona, not the swarm)
- The team would benefit more from depth than breadth (use `deep-interview` instead)

## The 12 personas (canonical set)

| Persona | Subagent type | When to include |
|---|---|---|
| **PM** | `brainstorm-swarm:pm` | Always include for product/feature decisions |
| **Engineer** | `brainstorm-swarm:engineer` | Always include for anything technical |
| **Designer** | `brainstorm-swarm:designer` | Include when there's a user-facing surface |
| **Skeptic** | `brainstorm-swarm:skeptic` | Include unless the user explicitly opts out |
| **User Advocate** | `brainstorm-swarm:user-advocate` | Include when end-users are downstream |
| **Pre-Mortem Specialist** | `brainstorm-swarm:pre-mortem-specialist` | Include for high-stakes / hard-to-reverse decisions |
| **Junior** | `brainstorm-swarm:junior` | Include when the team has shared assumptions worth surfacing |
| **Veteran** | `brainstorm-swarm:veteran` | Include when pattern-matching against past failures helps |
| **First-Principles Thinker** | `brainstorm-swarm:first-principles-thinker` | Include for "are we solving the right problem?" decisions |
| **Constraint-Setter** | `brainstorm-swarm:constraint-setter` | Include for scope-prone decisions |
| **Optimist** | `brainstorm-swarm:optimist` | Include when the room is too pessimistic |
| **Operator** | `brainstorm-swarm:operator` | Include for anything that runs in production |

See `references/persona-catalog.md` for the full descriptions, voices, and selection guidance.

## Choosing a subset

Don't always spawn all 12 — that produces noise and burns tokens. Pick a subset of 4-8 personas based on the decision type.

### Default subsets by decision type

| Decision type | Default subset (5-7 personas) |
|---|---|
| **Feature design** | PM, Engineer, Designer, Skeptic, User Advocate, Pre-Mortem |
| **Architecture decision** | Engineer, Operator, Skeptic, Veteran, First-Principles, Constraint-Setter |
| **Product strategy** | PM, User Advocate, Skeptic, Optimist, First-Principles, Pre-Mortem |
| **Technical migration** | Engineer, Operator, Veteran, Pre-Mortem, Constraint-Setter, Skeptic |
| **Content / writing** | First-Principles, Skeptic, User Advocate, Optimist, Junior |
| **Process / org change** | Skeptic, Veteran, User Advocate (= the affected team), Pre-Mortem, Constraint-Setter |
| **Greenfield exploration** | Optimist, First-Principles, User Advocate, Junior, Skeptic |

See `references/invocation-patterns.md` for full subset rationale.

## How to invoke (the parallel-spawn pattern)

### ⛔ The single-message rule

Spawn all subagents **in a single message** with multiple Task() tool uses. This is what makes them parallel. Spawning them sequentially across multiple messages defeats the purpose.

```python
# Single message, multiple Task() calls — TRUE PARALLEL:
Task(subagent_type="brainstorm-swarm:pm", description="PM perspective on offline mode", prompt="...")
Task(subagent_type="brainstorm-swarm:engineer", description="Engineer perspective on offline mode", prompt="...")
Task(subagent_type="brainstorm-swarm:designer", description="Designer perspective on offline mode", prompt="...")
Task(subagent_type="brainstorm-swarm:skeptic", description="Skeptic perspective on offline mode", prompt="...")
Task(subagent_type="brainstorm-swarm:user-advocate", description="User Advocate perspective on offline mode", prompt="...")
Task(subagent_type="brainstorm-swarm:pre-mortem-specialist", description="Pre-mortem of offline mode", prompt="...")
```

### The prompt template each persona receives

Every persona gets the SAME core prompt (the topic + context), but their persona-specific subagent type loads the persona's voice. Template:

```
Topic: [one-sentence framing of what's being brainstormed]

Context:
- [What the team is working on]
- [What's already known / decided]
- [Constraints — budget, timeline, team size if relevant]
- [Specific questions the user wants answered]

Your job:
Contribute your perspective in your characteristic voice. Follow your output
format exactly. Don't try to be all the personas — be your one.

Length budget: under 400 words.
```

The personas will produce structured Markdown contributions per their output format (see each persona's SKILL/agent file).

## Workflow

The end-to-end flow:

1. **Frame the topic.** Get a one-sentence statement of what's being brainstormed. If vague, ask 1-2 clarifying questions.
2. **Pick a subset.** Use the default-by-decision-type table; explicitly add/remove personas based on the topic. Show the user the subset and get sign-off.
3. **Build the shared prompt.** One prompt template, used for all spawned subagents. Include topic + context + length budget.
4. **Spawn in parallel.** ⛔ Single message, multiple Task() calls. All spawning happens at once.
5. **Wait for all returns.** Don't synthesize until every persona has contributed.
6. **Hand off to swarm-synthesis.** Let that skill produce the consensus / dissent / open-questions output.
7. **Optional: second round.** If synthesis surfaces a critical disagreement worth deepening, spawn just the 2-3 personas in tension for a second-round response to the specific dissent.

See `references/invocation-patterns.md` for handling edge cases and `references/parallel-spawn-rules.md` for the parallelism mechanics.

## ✅ Use for

- Invoking the brainstorm-swarm on any topic
- Picking the right persona subset for a decision type
- Spawning personas in true parallel (single message, multiple Task() calls)
- Handling persona outputs and routing them to synthesis
- Deciding whether to do a second-round deepening

## ❌ NOT for

- **Code review** — use `code-review` (different swarm, locked to code analysis)
- **Single-perspective interviews** — use `elicitation` or `deep-interview`
- **Executing or building** — use `team`, `autopilot`, or `multi-agent-patterns`
- **Designing custom personas** — use `custom-personas` (sibling skill)
- **The synthesis output format** — use `swarm-synthesis` (sibling skill)
- **The interview structure / question design** — use `interview-facilitation` (sibling skill)

## Anti-patterns

### Sequential spawning

**What it looks like:** spawning Task() #1, waiting for the return, spawning Task() #2.

**Why it's wrong:** the second persona sees what the first wrote (in your context), and you the orchestrator unconsciously bias the prompt. The personas converge instead of diverging.

**What to do instead:** single message, all Task() calls at once. They run in parallel and don't see each other.

### All-12-always

**What it looks like:** spawning every canonical persona on every topic.

**Why it's wrong:** burns tokens; produces noise; harder to synthesize.

**What to do instead:** pick the 4-8 most relevant personas for the decision type. The default-by-decision-type table is your guide.

### Skipping the framing

**What it looks like:** invoking the swarm on "what should we do about onboarding" without further framing.

**Why it's wrong:** vague topic → vague outputs from every persona → un-actionable synthesis.

**What to do instead:** ask 1-2 clarifying questions to tighten the topic before spawning. "What specifically about onboarding — the first-run experience, the activation funnel, the trial-to-paid conversion?"

### Skipping synthesis

**What it looks like:** spawning the swarm, dumping all 6 outputs back to the user, declaring done.

**Why it's wrong:** the user gets 6 walls of text and has to do the synthesis themselves. The whole point is the cross-persona pattern recognition.

**What to do instead:** always run swarm-synthesis after collection. The synthesis IS the deliverable.

### Forced consensus

**What it looks like:** orchestrator's synthesis hides the disagreement to "give a clear answer."

**Why it's wrong:** the dissent IS the value. Hiding it loses the swarm's main contribution.

**What to do instead:** swarm-synthesis explicitly preserves dissent in a Dissent section. Disagreement is a feature.

## References

| File | Contents |
|---|---|
| `references/persona-catalog.md` | Full descriptions of all 12 canonical personas — voice, contribution shape, when to include |
| `references/invocation-patterns.md` | Default subsets by decision type with rationale; subset selection edge cases |
| `references/parallel-spawn-rules.md` | The single-message rule, prompt template construction, what to do with returns |

## Related skills

- **interview-facilitation** — how to structure the interview arc and design questions
- **swarm-synthesis** — how to combine the parallel outputs into a useful artifact
- **custom-personas** — how to design ad-hoc personas when the canonical 12 don't fit
- **deep-interview** (skillstack) — single-agent socratic alternative
- **elicitation** (skillstack) — single-agent psychological deep-interview
- **multi-agent-patterns** (skillstack) — theory of multi-agent architectures (this skill is the runnable version of the swarm pattern)
