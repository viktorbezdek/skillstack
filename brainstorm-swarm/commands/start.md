---
description: Run a parallel persona-swarm brainstorm on a topic. Spawns 4-8 persona-distinct subagents in parallel, synthesizes their outputs into consensus / dissent / open questions / recommended next move.
argument-hint: '<topic to brainstorm>'
allowed-tools: Read, Grep, Glob, AskUserQuestion, Task, Write, Edit
---

Run a brainstorm-swarm session on the topic provided in `$ARGUMENTS`.

If `$ARGUMENTS` is empty, ask the user what they want to brainstorm in one sentence.

## Workflow

Follow the brainstorm-swarm plugin's three skills in order:

### 1. swarm-protocol — choose the persona subset

Load `swarm-protocol` skill. Pick the persona subset (4-8 of the canonical 12) appropriate to the decision type. Use the default-by-decision-type table from `references/invocation-patterns.md`.

Show the user the proposed subset with rationale. Get sign-off before spawning. Allow the user to add/remove personas (they may also request a custom persona — invoke the `custom-personas` skill if so).

### 2. interview-facilitation — design the prompts

Load `interview-facilitation` skill. Construct the Phase 1 prompt:

- One-sentence topic framing
- 100-300 words of context (background, constraints, the specific question)
- Length budget: under 400 words per persona

Same prompt body goes to every persona; the persona's subagent type loads their voice.

### 3. swarm-protocol — spawn in parallel

⛔ **Single message, multiple Task() calls.** Sequential spawning collapses the swarm. All Task() invocations for the chosen subset go in ONE message:

```
Task(subagent_type="brainstorm-swarm:pm", description="...", prompt="...")
Task(subagent_type="brainstorm-swarm:engineer", description="...", prompt="...")
Task(subagent_type="brainstorm-swarm:designer", description="...", prompt="...")
[etc. for the chosen subset]
```

### 4. swarm-synthesis — produce the artifact

Load `swarm-synthesis` skill. Once all personas have returned, produce the standard artifact:

- Personas in the swarm (with rationale)
- Consensus (what 3+ personas agreed on)
- Dissent (substantive disagreements with underlying questions)
- Open questions (with "what evidence would resolve" notes)
- Recommended next move (with alternative)
- Per-persona contributions (collapsed)

Preserve dissent. Don't force consensus.

### 5. Optional second round (Phase 2)

After presenting the synthesis, ask the user:

- Anything to dig deeper into?
- A specific dissent worth pursuing in Phase 2?
- Or do you have enough to decide?

If deepening, use `interview-facilitation` to design the Phase 2 probing prompt and spawn just the 2-3 personas in tension.

### 6. Optional convergent closing (Phase 3)

If the user has a tentative direction, run a Phase 3 pressure-test: spawn 3-4 personas (Skeptic + relevant domain) with the convergent closing template (strongest FOR / strongest AGAINST / decisive consideration).

## Default behavior

If the user just says `/brainstorm-swarm:start <topic>` and provides no further direction:

1. Treat as Arc 1 (Divergent only) by default
2. Pick a 6-persona subset based on the topic's decision type
3. Run Phase 1 → synthesis → present
4. Ask whether to continue with Phase 2/3 or stop

Don't auto-spawn additional rounds without checking.

## Output

A markdown synthesis (in chat) covering all sections. If the user wants the artifact saved to a file, write to a path they designate. Otherwise leave in chat.

## Tip

For high-stakes decisions, consider Arc 3 (full arc): Phase 1 divergent → Phase 2 probing → Phase 3 convergent. Costs more (~30-50k tokens, 10-20 min wall) but produces a defensible decision document.

For tentative-decision pressure-tests, Arc 4 (Phase 3 only) is faster and tighter.
