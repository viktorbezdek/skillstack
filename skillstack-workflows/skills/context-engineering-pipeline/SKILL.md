---
name: context-engineering-pipeline
description: Diagnostic-and-fix pipeline for systematic context engineering — fix agent context, context engineering, context optimization pipeline, diagnose context problems. Chains context-fundamentals (attention, budgeting), context-optimization (KV-cache, partitioning, observation masking), context-compression (summarization, anchored iterative, tokens-per-task), context-degradation (lost-in-middle, poisoning, clash diagnosis), and filesystem-context (scratch pads, plan files, dynamic loading). Use when an agent's context is degrading, token costs are bloated, the agent forgets instructions mid-session, output quality drops in long conversations, or building a new agent and wanting context right from the start. NOT for prompt engineering — use prompt-engineering. NOT for agent architecture — use build-ai-agent.
---

# Context Engineering Pipeline

> Context engineering is not prompt engineering. Prompt engineering is about what you say. Context engineering is about what the model can see, how much of it fits, what it pays attention to, what degrades over time, and where it lives between sessions. This pipeline treats the context window as infrastructure, not as a text box.

Most agent failures blamed on "the model is dumb" are actually context failures: the right information was absent, buried, contradicted, or expired. This pipeline diagnoses which failure mode is active and applies the specific fix.

---

## When to use this workflow

- An agent's output quality degrades over long conversations
- Token costs are high and you suspect context bloat
- An agent forgets its instructions mid-session or contradicts itself
- You're building a new agent and want to design the context architecture before writing prompts
- An agent works on short tasks but fails on multi-step workflows
- You've tried prompt engineering and it didn't help — the problem is upstream

## When NOT to use this workflow

- **Prompt wording problems** — the model misunderstands your instruction. Use `prompt-engineering` directly.
- **Agent architecture problems** — wrong tool selection, bad routing, no eval. Use `build-ai-agent`.
- **Model capability limits** — the task exceeds the model's reasoning ability regardless of context. Test with a larger model first.
- **Cost-only optimization** — if quality is fine and you just want lower costs, use `llm-cost-optimization`.

---

## Prerequisites

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install context-fundamentals@skillstack
/plugin install context-optimization@skillstack
/plugin install context-compression@skillstack
/plugin install context-degradation@skillstack
/plugin install filesystem-context@skillstack
```

---

## Core principle

**Diagnose before optimizing.** The five context skills in this pipeline address different problems. Applying compression to a poisoning problem makes things worse (you compress the poison into a denser form). Applying optimization to a fundamentals problem wastes effort on symptoms. The pipeline enforces the diagnostic order: understand the theory, extend capacity, compress what remains, diagnose active pathologies, persist what works.

Secondary principle: **context is a budget, not a dump.** Every token in the context window competes for attention with every other token. Adding information that isn't needed for the current step doesn't just waste tokens — it actively degrades performance by diluting attention on the information that IS needed. Less is almost always more.

---

## The pipeline

### Phase 1 — understand context mechanics (context-fundamentals)

Load the `context-fundamentals` skill. Before optimizing anything, ensure the team has a shared understanding of how context actually works:

- **What context IS** — the concatenation of system prompt, conversation history, tool results, and injected documents that the model sees on each turn. It's not "memory" — it's a fresh input every time.
- **Attention mechanics** — models don't read context uniformly. Attention is strongest at the beginning and end, weakest in the middle (the "lost-in-middle" effect). Position matters.
- **Progressive disclosure** — not everything needs to be in context at all times. Load information when it's needed, not "just in case." The skill has specific patterns for when to inject vs. retrieve.
- **Context budgeting** — for each component in the context (system prompt, history, tool results, retrieved documents), assign a token budget. If the total exceeds the window, something must be cut — and the budget tells you what.
- **The attention tax** — every token added to context has a cost beyond its token price: it dilutes attention on everything else. A 1000-token document added "for reference" that the model never uses still degrades performance on the tokens it DOES use.

Output: a context budget — for the agent or system you're working on, a breakdown of what goes in the context, how many tokens each component gets, and the priority order for what gets cut when the budget is exceeded.

This phase is the foundation. Teams that skip it tend to treat context as "put everything in and hope the model figures it out," which is the root cause of most context problems.

### Phase 2 — extend effective capacity (context-optimization)

Load the `context-optimization` skill. With the budget from Phase 1, apply techniques that let you fit more useful information into the same window:

- **KV-cache optimization** — structure prompts so the stable prefix (system prompt, instructions, static context) is identical across requests. Providers cache this prefix and skip recomputation, reducing latency and cost. The key: the cached prefix must be byte-identical. Any variation — even a timestamp — breaks the cache.
- **Context partitioning** — separate "working memory" (what the agent needs for THIS step) from "reference knowledge" (what it might need for ANY step). Working memory goes in the prompt; reference knowledge goes in retrieval. This is the single highest-leverage optimization for multi-step agents.
- **Observation masking** — in multi-turn agents, tool call results from previous turns accumulate. Most are irrelevant to the current turn. Mask (remove or summarize) tool results that have been consumed and are no longer needed.
- **Retrieval strategy** — for reference knowledge, choose between embedding-based retrieval (good for semantic similarity), keyword retrieval (good for exact matches), and hybrid. The `context-optimization` skill has comparison matrices.
- **Output recycling** — when the agent's previous output contains structured results (JSON, lists, decisions), extract and reformat them rather than keeping the full conversational output in history.

Output: a set of optimization techniques applied to the context architecture, with before/after measurements of effective context utilization.

### Phase 3 — compress what remains (context-compression)

Load the `context-compression` skill. After Phase 2's optimizations, what remains in context is information that needs to be there but may be larger than necessary:

- **Conversation summarization** — replace long conversation history with a rolling summary. The `context-compression` skill covers the key challenge: summaries lose detail, and lost detail causes the agent to repeat questions or contradict earlier answers.
- **Anchored iterative summarization** — a more sophisticated approach: maintain "anchors" (key facts, decisions, user preferences) that persist through summarization cycles. The summary shrinks; the anchors don't.
- **Tokens-per-task optimization** — for each task type the agent handles, measure the actual tokens used vs. the minimum needed. This often reveals that 40% of context is boilerplate that doesn't vary between tasks.
- **Compaction triggers** — define rules for when to compact: total context exceeds N tokens, conversation exceeds M turns, tool results exceed K tokens. Reactive compaction (wait until full) loses more than proactive compaction (compact before pressure).
- **Compression validation** — after compressing, probe the agent: "Based on our conversation, what did the user ask for in step 3?" If it can't answer, the compression lost critical information. Adjust anchors.

Output: a compression policy — what gets compressed, when, how, and what anchors are preserved.

### Phase 4 — diagnose active pathologies (context-degradation)

Load the `context-degradation` skill. If the agent is still misbehaving after Phases 1-3, the problem may be a specific context pathology:

- **Lost-in-middle** — information placed in the middle of a long context is ignored. Test: move the critical information to the beginning or end. If behavior improves, this is the pathology. Fix: restructure context to place important information at attention-strong positions (beginning and end).
- **Context poisoning** — incorrect or outdated information in the context overrides correct information. Test: remove the suspected poison and check if behavior improves. Fix: actively clean context of outdated tool results, retracted statements, and superseded instructions.
- **Context clash** — two pieces of context contradict each other and the model picks the wrong one (or oscillates). Test: present only one version. Fix: resolve contradictions before they enter context; add explicit "this supersedes that" markers.
- **Context confusion** — too much unrelated information dilutes attention on relevant information. The model produces plausible but off-topic responses. Test: aggressively prune context to only the current task. Fix: Phase 2's context partitioning, applied more aggressively.
- **Instruction decay** — system prompt instructions are followed early in the conversation but gradually ignored as conversation history grows and pushes them proportionally further from the model's attention. Test: re-inject instructions mid-conversation. Fix: instruction repetition at regular intervals, or move instructions to a position that maintains attention.

The `context-degradation` skill has empirical thresholds by model for when each pathology typically manifests. Use these as diagnostic starting points.

Output: a pathology report — which degradation patterns are active, with test results and recommended fixes.

### Phase 5 — persist to the filesystem (filesystem-context)

Load the `filesystem-context` skill. Context that only lives in the conversation is context that dies when the session ends. For durable agent systems:

- **Scratch pads** — files where the agent writes intermediate work (plans, partial results, decision logs). These survive session boundaries and can be loaded into new sessions.
- **Plan persistence** — for multi-step workflows, persist the plan to a file. Each step reads the plan, executes, and updates it. The plan file is the state machine.
- **Dynamic skill loading** — instead of keeping all instructions in the system prompt, load specific skills/instructions from files when needed. This is context partitioning applied to the filesystem.
- **Sub-agent workspaces** — when using multi-agent patterns, each agent gets its own file workspace. Communication happens through files, not through shared context. This prevents context pollution between agents.
- **Terminal log persistence** — capture command outputs and tool results to files rather than keeping them in context. Reference the file when needed; discard the raw output from context.
- **Session handoff files** — when a session ends (or context compacts), write a handoff file containing: current state, key decisions, next steps, and any context the next session will need. The handoff file is the compressed memory of the session.

Output: a filesystem context architecture — what files the agent reads and writes, where they live, what format they use, and the lifecycle (created when, read when, deleted when).

---

## Gates and failure modes

**Gate 1: the budget gate.** Phase 2 cannot start until Phase 1 has produced a context budget. Optimizing without knowing what's in the context and what each component costs is guesswork.

**Gate 2: the optimization-before-compression gate.** Phase 3 cannot start until Phase 2's optimizations are applied. Compressing information that should have been removed entirely is wasted effort.

**Gate 3: the diagnosis gate.** Phase 4's pathology diagnosis should only run after Phases 1-3 have been applied. Many "pathologies" are actually just context bloat that the earlier phases fix.

**Failure mode: compressing the poison.** The context contains incorrect information. Instead of removing it (Phase 4), the team compresses it (Phase 3). Now the incorrect information is denser and harder to find. Mitigation: Phase 4 diagnoses pathologies AFTER compression, catching what compression preserved.

**Failure mode: over-optimization.** The team removes so much context that the agent doesn't have enough information to do its job. Mitigation: Phase 1's budget gives each component a minimum allocation. Phase 3's compression validation catches information loss.

**Failure mode: filesystem as dumping ground.** The team persists everything to files but never cleans up. The filesystem becomes a second context problem. Mitigation: Phase 5 requires lifecycle definitions — every file has a creation trigger and a deletion trigger.

**Failure mode: skipping to Phase 4.** The agent is misbehaving, so the team jumps straight to diagnosing pathologies without doing the fundamentals. They find "lost-in-middle" and restructure, but the real problem was a 150K-token context that should have been 30K. Mitigation: follow the phases in order.

---

## Output artifacts

A completed pipeline produces:

1. **A context budget** — what goes in, how much, and priority order for cuts
2. **An optimization report** — techniques applied with before/after measurements
3. **A compression policy** — what gets compressed, when, with what anchors
4. **A pathology report** — which degradation patterns were found and how they were fixed
5. **A filesystem architecture** — what files the agent uses, their format, and lifecycle
6. **A monitoring checklist** — what to watch for that signals context health is degrading again

The context budget and compression policy are the durable outputs. The pathology report captures point-in-time diagnosis.

---

## Related workflows and skills

- For building the agent whose context you're engineering, use the `build-ai-agent` workflow
- For reducing LLM costs after context is optimized, use the `llm-cost-optimization` workflow
- For onboarding to a codebase and building an AI agent's initial context, use the `onboard-to-codebase` workflow
- For prompt wording (not context architecture), use `prompt-engineering` directly

---

> *SkillStack Workflows by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
