# Parallel Spawn Rules

The mechanics of spawning persona subagents in true parallel. Get this wrong and the swarm collapses to a sequential conversation.

## The single-message rule

⛔ **All Task() calls for one swarm round must be in ONE message.**

This is what makes the spawn parallel. Claude Code's runtime executes multiple Task() tool uses in a single message in parallel. Multiple messages = sequential = no swarm.

### Right (parallel)

```python
# Single assistant message, multiple Task() calls
Task(subagent_type="brainstorm-swarm:pm", description="PM on offline mode", prompt="...")
Task(subagent_type="brainstorm-swarm:engineer", description="Engineer on offline mode", prompt="...")
Task(subagent_type="brainstorm-swarm:designer", description="Designer on offline mode", prompt="...")
Task(subagent_type="brainstorm-swarm:skeptic", description="Skeptic on offline mode", prompt="...")
Task(subagent_type="brainstorm-swarm:user-advocate", description="User Advocate on offline mode", prompt="...")
Task(subagent_type="brainstorm-swarm:pre-mortem-specialist", description="Pre-mortem of offline mode", prompt="...")
```

All six personas get spawned at once. They run truly in parallel. None of them sees the others' output.

### Wrong (sequential — swarm collapses)

```
Message 1: Task(subagent_type="brainstorm-swarm:pm", ...)
[wait for return]
Message 2: Task(subagent_type="brainstorm-swarm:engineer", ...)
[wait for return]
...
```

This is no longer a swarm. The orchestrator's context now contains the PM's output before the Engineer runs, which biases the prompt construction (even unconsciously). The Engineer's output is influenced by what the PM said. The dissent diversity collapses.

## The shared prompt template

All spawned personas receive the same core prompt — only the subagent type changes their voice. Use this template:

```
Topic: [one-sentence framing of what's being brainstormed]

Context:
- [What the team is working on / system being modified]
- [What's already known or decided — don't make personas re-derive obvious things]
- [Constraints — budget, timeline, team size, technical limits]
- [The specific question or decision the user is trying to answer]

Your job:
Contribute your perspective in your characteristic voice. Follow your output
format exactly. Don't try to be all the personas — be your one.

Length budget: under 400 words.
```

### What to include in Context

Be generous with context. Each persona is a fresh subagent with no prior conversation history. They need:

- Enough context to make their contribution specific to your situation, not generic
- Not so much context that the prompt overflows or distracts

Aim for 100-300 words of context per spawn.

### What NOT to include in the prompt

- Don't include the personas' own output formats — those are baked into their subagent definition
- Don't include the user's questions to YOU — the persona shouldn't see the orchestrator's conversation
- Don't include other personas' anticipated takes — let each form their own view

### What to do per-persona prompt customization

Each persona gets the same prompt EXCEPT for one optional addition: a persona-specific question if you have one. Examples:

- For **Operator**: "Specifically: what's the on-call burden if this fails at 3 AM?"
- For **Veteran**: "Specifically: what past patterns does this match? Any 'I've seen this before' moments?"
- For **First-Principles**: "Specifically: is the framing 'we need offline mode' the right framing, or is the user's actual job different?"

Persona-specific questions are optional. They tighten the contribution but the persona's standard output covers most ground without them.

## Handling returns

After spawning, all personas return their structured contributions. Your orchestration job between spawn and synthesis:

### 1. Verify all returns

If a persona didn't return, decide:
- Re-spawn that one persona alone? (single new Task() call)
- Continue with the personas that returned? (synthesize what you have, note the gap)

For a 6-persona swarm, missing 1 is usually OK. Missing 3+ means re-run.

### 2. Light QA on returns

Each persona should have produced their characteristic output format. If one returned generic prose without their structured contribution, the subagent prompt didn't take. Re-spawn that persona with an even tighter prompt.

### 3. Hand off to synthesis

Pass all returned contributions to the `swarm-synthesis` skill for combining. Don't try to synthesize inline as you collect — synthesis benefits from seeing all contributions at once.

## Token budgeting

Each persona spawn costs:
- Persona's system prompt: ~600-1000 tokens
- Shared topic + context prompt: ~200-400 tokens
- Persona's output: ~400-800 tokens
- Per-spawn overhead: ~500 tokens

Total per persona ≈ 2000-2500 tokens. For a 6-persona swarm: 12-15k tokens. For a 12-persona swarm: 24-30k tokens.

This isn't cheap. The swarm's value justifies it for non-trivial decisions but don't spawn 12 personas for a tweet.

## Parallelism limits

Claude Code spawns subagents with some concurrency limit (typically 4-8 parallel). If you spawn 12, the runtime will queue some and run them in waves.

For most swarms (4-7 personas), you'll get all of them in the first wave. For 8-12, expect 1-2 waves. Total wall time is bounded by the slowest persona × number of waves.

## Idempotency

The same prompt to the same persona type produces similar but not identical outputs (model temperature). Don't expect bit-for-bit reproducibility.

If you want stricter reproducibility (for evaluation), capture each persona's output for the synthesis log so future re-runs can compare against the original.

## Spawn errors

| Error | Cause | Fix |
|---|---|---|
| `subagent type not found` | Plugin not installed, or typo in subagent name | Verify the persona files are in `agents/` and the plugin is installed |
| Persona produces wrong format | The persona's system prompt was overridden | Don't override; let the persona's subagent definition do its work |
| All personas produce identical content | Single-message rule violated; they ran sequentially | Re-do as one message with multiple Task() calls |
| Personas refuse to commit to a position | Prompt was too vague / too hedge-encouraging | Tighten the topic; remove "if you feel comfortable" framings |

## Quick checklist

Before spawning, confirm:

- [ ] Topic is a one-sentence statement (not a vague subject area)
- [ ] Context includes constraints, prior decisions, and the specific question
- [ ] Persona subset is 4-8, chosen for the decision type
- [ ] User has signed off on the subset
- [ ] You're ready to call ALL Task() in ONE message
- [ ] You have a plan for synthesis after collection
