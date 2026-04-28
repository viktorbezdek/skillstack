# Brainstorm Swarm

> **v1.0.0** | Multi-perspective brainstorming via parallel persona subagents | 4 skills + 12 personas + 1 command

---

## The problem

You're about to make a non-trivial decision — design a feature, pick an architecture, write a strategy doc, change an organizational policy, plan a migration. The right way to think about it is *from multiple perspectives*: the PM cares about scope and value, the engineer cares about complexity and rollout, the designer cares about user friction, the skeptic asks what could go wrong.

The problem: you don't have a roundtable handy. You're alone with Claude. So you either:

- Ask Claude to "think about this from different perspectives" — and get a single voice approximating multiple roles, badly
- Imagine the perspectives yourself — and miss the ones outside your habits
- Convene a real meeting — and pay the coordination cost for early-stage thinking

## The solution

Brainstorm Swarm spawns 6-12 persona-distinct subagents in parallel, each interviewing you from their perspective. Each persona is a real subagent (not Claude playing a role) — so they have isolated context, parallel execution, and genuine multi-perspective output.

After the parallel interview, the orchestrator synthesizes their contributions into:

- **Consensus** — what every persona agreed on
- **Dissent** — where personas disagreed and why
- **Open questions** — what nobody could answer; what to research next
- **Recommended next move** — the synthesized decision

## The 12 personas

| Persona | Voice |
|---|---|
| **pm** | Product Manager — value, scope, success metrics, prioritization |
| **engineer** | Implementation realism — feasibility, complexity, dependencies, rollout |
| **designer** | UX — user flow, friction, accessibility, aesthetic coherence |
| **skeptic** | Devil's Advocate — what's wrong with this, what assumption hides |
| **user-advocate** | The customer's voice in the room — what they actually want |
| **pre-mortem-specialist** | Assume failure in 6 months — what killed it |
| **junior** | Naive questioner — surfaces buried assumptions, demands explanations |
| **veteran** | War stories — "I've seen this before, here's what bit us" |
| **first-principles-thinker** | Strip back to fundamentals — what's actually true |
| **constraint-setter** | Scope discipline — what's NOT in scope, where does this stop |
| **optimist** | Yes-and energy — what's the most ambitious version of this |
| **operator** | Production reality — security, monitoring, blast radius, on-call |

## The 4 skills

| Skill | What it teaches |
|---|---|
| **swarm-protocol** | The orchestration logic — when to invoke a swarm, which subset of personas, how to spawn them in parallel, how to handle their outputs |
| **interview-facilitation** | How to structure the multi-perspective interview as a coherent arc, how to design questions, when to go deep vs broad |
| **swarm-synthesis** | How to combine multiple persona outputs into a useful artifact — consensus matrix, dissent log, decision synthesis, what to write down |
| **custom-personas** | How to design ad-hoc personas for niche domains when the canonical 12 don't fit (CFO for budget brainstorms, security engineer for threat modeling, etc.) |

## Installation

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install brainstorm-swarm@skillstack
```

## Usage

### Slash command

```
/brainstorm-swarm:start adding offline mode to our mobile app
```

The command activates the swarm-protocol skill, asks 1-2 clarifying questions about scope, proposes a persona subset, gets your sign-off, spawns the chosen subagents in parallel, collects their outputs, and synthesizes.

### Auto-activation

The skills also activate on natural-language queries:

- "Brainstorm this with multiple perspectives"
- "Get me a virtual roundtable on this design"
- "Workshop this idea from PM, engineer, designer, and skeptic angles"
- "Pre-mortem this rollout plan"
- "Run a persona swarm for [topic]"
- "I need devil's advocates on this"

### Output

A typical run produces a synthesis document with:

```
## What we brainstormed
[topic, scope, persona subset, why these personas]

## Consensus
- [point all personas agreed on, with attribution to who raised it first]

## Dissent
- PM vs Engineer on [topic]: [the disagreement]

## Open questions
- [questions nobody could answer; what to research]

## Recommended next move
- [synthesized decision with reasoning]

## Per-persona contribution (collapsible)
- PM said: [...]
- Engineer said: [...]
- ...
```

## What this plugin is NOT

- **NOT for code review** — use `code-review` (also a swarm, but locked to PR/code analysis)
- **NOT for single-perspective interviews** — use `elicitation` (psychological deep-interview techniques) or `deep-interview` (Socratic single-agent)
- **NOT for executing or building things** — use `team`, `autopilot`, or `multi-agent-patterns`
- **NOT for creating product personas as artifacts** — use `persona-definition` (creates user personas for product/UX research)
- **NOT for stakeholder mapping** — use `persona-mapping` (Power-Interest matrices, RACI charts)
- **NOT for theoretical multi-agent architecture** — use `multi-agent-patterns` (the patterns themselves, not a runnable swarm)

## Conventions

- Each persona subagent has tight scope and a focused system prompt; they don't bleed into each other's territory
- The synthesis skill explicitly preserves dissent — the swarm's value is in the disagreement, not just the consensus
- Custom personas are encouraged when a domain calls for it (the `custom-personas` skill teaches the design discipline)

## Author

Viktor Bezdek — https://github.com/viktorbezdek

## License

MIT.
