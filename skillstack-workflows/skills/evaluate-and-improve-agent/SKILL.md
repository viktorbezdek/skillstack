---
name: evaluate-and-improve-agent
description: Diagnostic-loop workflow for improving an underperforming AI agent. Starts with baseline measurement using rubrics and LLM-as-judge scoring (agent-evaluation), then diagnoses architectural problems like task-model mismatch and pipeline bottlenecks (agent-project-development), redesigns the agent topology — supervisor, swarm, or specialized agents (multi-agent-patterns), adds the right memory framework when persistence is the gap (memory-systems), and re-evaluates against the original baseline to prove improvement. Use when an existing agent is underperforming, producing inconsistent results, failing on edge cases, or costing too much per interaction. NOT for building a new agent from scratch — use the build-ai-agent workflow instead. NOT for prompt-only fixes — use prompt-engineering directly.
---

# Evaluate and Improve Agent

> The most dangerous state for an agent is "it mostly works." Teams stop measuring, stop improving, and slowly accumulate failure modes that nobody notices until a customer does. This workflow breaks that plateau by forcing a baseline measurement before any changes and a comparison measurement after.

Agent improvement without measurement is hope. You change the prompt, the tools, the architecture — and you feel better about it, but you don't know if it's better. The eval harness is the difference between iterating and guessing.

---

## When to use this workflow

- An existing agent is producing inconsistent or incorrect results
- Agent accuracy has degraded over time and nobody knows why
- Agent costs are climbing without corresponding quality gains
- The agent fails on edge cases that matter to real users
- You inherited an agent codebase and need to understand what's working and what isn't
- Stakeholders ask "is the agent getting better?" and you can't answer with data

## When NOT to use this workflow

- **Building a new agent from scratch** — use the `build-ai-agent` workflow, which includes evaluation as a built-in phase
- **Prompt-only issues** — if the architecture is fine and the prompt just needs tuning, use `prompt-engineering` directly
- **The agent is working well** — don't fix what isn't broken; optimize cost with `llm-cost-optimization` instead
- **Non-agent LLM tasks** — classification, extraction, and summarization don't need agent architecture review

---

## Prerequisites

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install agent-evaluation@skillstack
/plugin install agent-project-development@skillstack
/plugin install multi-agent-patterns@skillstack
/plugin install memory-systems@skillstack
```

---

## Core principle

**Measure before you change, and measure after.** Every change to an agent should be answerable with "did this make the scores go up, go down, or stay the same?" If you can't answer that question, you don't have an evaluation pipeline — you have opinions. The baseline measurement in Phase 1 is the anchor that makes every subsequent phase meaningful.

Secondary principle: **diagnose before you redesign.** Most underperforming agents don't need new architecture — they need the existing architecture fixed. Phase 2 exists to find the actual bottleneck before Phase 3 proposes structural changes.

---

## The phases

### Phase 1 — Establish baseline (agent-evaluation)

Load the `agent-evaluation` skill. Before touching anything, measure where the agent is today.

**Build the rubric:**
- Define 4-6 evaluation dimensions relevant to this agent. Common ones: correctness, faithfulness to source material, safety/refusal accuracy, response quality, latency, cost per interaction.
- Each dimension needs a 1-5 scale with concrete anchors. "3 = partially correct, key information present but with one factual error" is useful. "3 = okay" is not.

**Build the eval set:**
- Collect 50-200 representative inputs. Pull from production logs if available — synthetic inputs miss the distribution of real usage.
- For each input, define expected behavior (exact output, expected properties, or unacceptable outputs).
- Include known failure cases. If users have reported problems, those go into the eval set first.

**Choose a scoring method:**
- **Direct scoring** — run the rubric on each output. Fast, good for clear-cut dimensions.
- **LLM-as-judge** — use a separate model to evaluate outputs. Apply bias mitigation: randomize order, use multiple judges, include reference outputs.
- **Pairwise comparison** — compare current agent vs. a reference. Useful when absolute quality is hard to define but relative quality is obvious.

**Run the baseline:**
- Score every eval set item on every dimension
- Compute aggregate scores per dimension and overall
- Identify the worst-performing dimension — this is likely where Phase 2 should focus

Output: a baseline scorecard with per-dimension scores, the eval set, and the rubric. This is the anchor for the rest of the workflow.

### Phase 2 — Diagnose architecture (agent-project-development)

Load the `agent-project-development` skill. The baseline told you WHAT is failing. This phase tells you WHY.

**Task-model fit analysis:**
- Is the underlying model appropriate for this task's difficulty? A task requiring complex reasoning on a fast/cheap model will always underperform.
- Is the task actually agent-appropriate? Some tasks that were built as agents should have been pipelines or single prompts. The `agent-project-development` skill has explicit criteria for this.

**Pipeline analysis:**
- Trace the agent's execution on 10 failing cases from the eval set. Where does it go wrong?
- Common bottlenecks: tool selection errors (wrong tool called), context overflow (too much information in the window), retrieval failures (right information not found), cascading errors (early mistake compounds through later steps).

**Prompt analysis:**
- Is the system prompt doing too much? Prompts that try to cover every case often fail on all of them.
- Are tool descriptions accurate? Agents choose tools based on descriptions. Bad descriptions cause correct tools to be ignored.
- Is the context structured or dumped? Unstructured context degrades performance as it grows.

**Cost analysis:**
- Token usage per interaction — where are the tokens going?
- Are there unnecessary round-trips? Each tool call costs tokens for the call, the response, and the agent's reasoning about the response.
- Are there agentic loops (the agent calls tools repeatedly without converging)?

Output: a diagnosis document listing the root causes of underperformance, ranked by impact on the baseline scores.

### Phase 3 — Redesign patterns (multi-agent-patterns)

Load the `multi-agent-patterns` skill. Based on the diagnosis, decide whether architectural changes are needed.

**Decision: single-agent fixes vs. multi-agent redesign**

Most of the time, the answer is to fix the existing single agent:
- Better prompt structure
- Fewer, better-described tools
- Improved context management
- Model upgrade for the hardest subtasks

Multi-agent redesign is warranted when:
- The agent has distinct subtask types that need different specializations
- A single prompt can't cover all the behavioral requirements without contradictions
- The agent needs to coordinate work across different tool sets
- Failure in one subtask should not poison the others

**If redesigning, choose a topology:**
- **Supervisor + workers** — one routing agent delegates to specialists. Best when subtasks are independent and the routing logic is clear.
- **Swarm / handoff** — agents pass control to each other based on the conversation state. Best when the flow is sequential but different phases need different capabilities.
- **Hierarchical** — supervisors of supervisors. Reserve for genuinely complex systems. The coordination overhead is real.

**Implement incrementally:**
- Change one thing at a time. Run the eval set after each change.
- If a change doesn't improve the baseline, revert it. Complexity without improvement is pure cost.

Output: the redesigned architecture (or the list of single-agent fixes), with rationale tied to specific diagnosis findings from Phase 2.

### Phase 4 — Add memory (memory-systems)

Load the `memory-systems` skill. This phase runs only if the diagnosis identified memory as a gap.

**Signs that memory is the problem:**
- The agent asks users to repeat information it should already know
- Cross-session context is lost, forcing users to re-explain their setup
- The agent makes the same mistakes repeatedly instead of learning from corrections
- Personalization is absent despite repeated interactions

**If memory IS the problem, choose a framework:**
- Compare Mem0, Zep/Graphiti, Letta, LangMem, and Cognee using the skill's comparison matrix
- Key dimensions: latency (memory retrieval adds to response time), accuracy (wrong memories are worse than no memories), cost (storage + retrieval + embedding), and operational complexity

**If memory is NOT the problem:**
- Skip this phase entirely. Memory systems add latency, cost, and debugging complexity. Adding memory to solve a non-memory problem makes the agent worse, not better.

**Implement and test:**
- Start with the simplest memory type that addresses the diagnosed gap (user preferences, conversation summaries, or factual corrections)
- Run the eval set with memory enabled. Compare against the baseline.
- Watch for memory pollution — incorrect memories that cause the agent to behave worse over time

Output: the memory implementation (or explicit decision to skip), with eval evidence showing impact.

### Phase 5 — Re-evaluate against baseline (agent-evaluation)

Load the `agent-evaluation` skill again. Run the exact same eval set with the exact same rubric against the improved agent.

**Compare dimension by dimension:**
- Which dimensions improved? By how much?
- Did any dimension regress? Regressions must be investigated — fixing one thing shouldn't break another.
- What's the overall delta?

**Analyze remaining failures:**
- Of the original failing cases, how many are now passing?
- Are there new failure modes introduced by the changes?
- What's the cost delta? Improvements that double the cost may not be worth it.

**Decision at the gate:**
- **Improvement across the board** — ship it. Set up continuous monitoring (see Phase 7 of the `build-ai-agent` workflow).
- **Mixed results** — investigate the regressions. Often they reveal a trade-off that needs explicit prioritization.
- **No improvement** — the diagnosis was wrong. Go back to Phase 2 with the new information. Do not ship changes that don't improve scores.
- **Regression** — revert all changes. The agent was better before.

Output: a comparison scorecard (before vs. after), a list of resolved failure cases, a list of remaining gaps, and a ship/no-ship recommendation.

---

## Gates and failure modes

**Gate 1: the baseline gate.** No changes until the baseline eval exists. Changing an agent without measurement is guessing, and guessing is how agents get worse while teams think they're improving.

**Gate 2: the diagnosis gate.** No redesign until the root cause is identified. "Let's try multi-agent" without a diagnosis is architecture astronautics.

**Gate 3: the improvement gate.** No shipping until the re-evaluation shows measurable improvement. "It feels better" is not evidence.

**Failure mode: eval set contamination.** The team tunes the agent to pass the eval set instead of solving the underlying problem. Mitigation: hold out 20% of the eval set that is never used during development. Test against it only at the gate.

**Failure mode: architecture enthusiasm.** The team redesigns the architecture because it's interesting, not because the diagnosis pointed there. Mitigation: Phase 2 must produce a diagnosis BEFORE Phase 3 begins. Architecture changes without a diagnosis document are rejected.

**Failure mode: memory as a band-aid.** The agent has a prompt problem, but memory feels like a more interesting fix. The agent now has a prompt problem AND a memory system. Mitigation: Phase 4 only runs when the diagnosis explicitly identifies memory gaps.

**Failure mode: ignoring cost.** The improved agent scores better but costs 3x more per interaction. Mitigation: cost is a rubric dimension. It's evaluated alongside accuracy, not after.

---

## Output artifacts

A completed improvement cycle produces:

1. **A baseline scorecard** — the agent's state before any changes
2. **A diagnosis document** — root causes ranked by impact
3. **An architecture decision record** — what changed and why (or why nothing changed)
4. **A comparison scorecard** — before vs. after on every dimension
5. **An updated eval set** — expanded with new failure modes discovered during the cycle
6. **A monitoring plan** — how to detect future regressions in production

---

## Related workflows and skills

- For building a new agent from scratch with evaluation built in, use the `build-ai-agent` workflow
- For reducing agent costs specifically, use the `llm-cost-optimization` workflow after this one
- For deep debugging of a specific agent failure, use the `debug-complex-issue` workflow
- For the memory framework comparison alone, use `memory-systems` directly

---

> *SkillStack Workflows by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
