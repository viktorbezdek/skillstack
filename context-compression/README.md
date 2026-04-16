> **v1.0.4** | Context Engineering | 5 iterations

# Context Compression

> Reduce agent context size without losing the information that matters -- structured summarization, anchored iterative compression, tokens-per-task optimization, and probe-based quality evaluation.
> Single skill + 1 reference document | 13 trigger evals, 3 output evals

## The Problem

Long-running AI agent sessions generate enormous conversation histories. A debugging session might reach 89,000 tokens across 178 messages. A codebase exploration might accumulate millions of tokens of tool output. When the context window fills up, something must be compressed or discarded -- and naive approaches destroy the information agents need most.

The default compression strategy is aggressive token reduction: summarize everything, keep it short, move on. This looks efficient on paper. In practice, it causes agents to forget which files they modified, lose track of error messages they already diagnosed, and re-explore approaches they already tried. The agent spends 20% more tokens recovering context that compression threw away. The "savings" cost more than they saved.

The deeper failure is measurement. Teams optimize for tokens-per-request (how small is each API call?) when the real metric is tokens-per-task (total tokens consumed to complete a piece of work). A compression strategy that saves 0.5% more tokens per request but causes agents to re-fetch information three times is a net loss. Without probe-based evaluation to measure what compression actually preserved, teams cannot distinguish good compression from bad.

## The Solution

This plugin provides a single skill that teaches Claude how to compress context intelligently using three production-tested approaches: anchored iterative summarization (structured summaries that force preservation of critical information), opaque compression (maximum token savings for short sessions), and regenerative full summaries (readable output at phase boundaries). The skill includes a probe-based evaluation framework that measures compression quality across six dimensions -- accuracy, context awareness, artifact trail, completeness, continuity, and instruction following.

The core insight is that structure forces preservation. When summaries have explicit sections for session intent, files modified, decisions made, and next steps, the summarizer must populate each section. Silent information drift becomes structurally impossible. The plugin also teaches when to trigger compression (70-80% context utilization), how to merge summaries incrementally rather than regenerating from scratch, and how to handle the artifact trail problem -- the weakest dimension across all compression methods.

## Context to Provide

Compression strategy depends on your session characteristics -- what the agent does, how long sessions run, and which specific information types get lost. Generic compression advice rarely fits; specific session context produces immediately applicable strategy.

**What information to include in your prompt:**

- **Agent type and task**: What does the agent do? (debugging, code migration, research synthesis, code generation) -- the critical information types differ by task
- **Typical session length**: Approximate turns and token count (e.g., "150 turns, 80-100K tokens for a debugging session")
- **Information that must survive compression**: What does the agent forget that causes problems? (file paths it modified, error messages it diagnosed, approaches it already tried, decisions it made)
- **Re-fetch cost**: How expensive is it when the agent loses something and has to redo work? (re-reading a 10K-line file, re-running a slow API call, re-exploring an already-diagnosed error)
- **Current compression approach**: What do you do now? (nothing, aggressive summarization, sliding window, full regeneration)
- **Quality measurement problem**: How do you currently know if compression is working? Do you have any way to detect when critical information was silently lost?
- **Phase structure**: Does the work have clear phases (research, planning, implementation) or is it continuous and unpredictable?

**What makes results better:**
- Describing a specific failure case ("after turn 80, the agent proposes fixes it already tried -- it forgets which approaches failed") maps directly to the decision-probe design and the decisions-made section of the summary template
- Specifying what information is most expensive to re-fetch ("re-reading the codebase takes 20K tokens each time") quantifies the cost of compression failure and justifies a higher-quality compression strategy
- Describing your current approach ("we use aggressive summarization, keeping summaries under 500 tokens") enables before/after comparison and specific improvement recommendations
- Mentioning whether you need to audit compression quality ("regulators require traceability, so I need to verify the summary is accurate") drives the probe-based evaluation design

**What makes results worse:**
- "Summarize this conversation" -- the skill designs compression systems, not one-off summaries
- Focusing on tokens-per-request reduction without describing what the agent does with recovered context -- the right metric is tokens-per-task
- Omitting what specifically gets lost -- "the agent forgets things" is not enough to design the right summary structure

**Template prompt:**
```
Design a context compression strategy for a [type of agent] that [what it does]. Sessions typically run [N turns / N tokens]. The critical information it must preserve across compressions: [list: file paths modified / error messages / decisions made / approaches tried / etc.]. Re-fetch cost when this is lost: [describe]. Current compression approach: [none / aggressive summarization / describe]. Phase structure: [phased research-plan-implement / continuous / other]. I also need to [evaluate compression quality / detect when information is silently lost].
```

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Agent forgets which files it modified after context compaction | Structured summary sections force file tracking through explicit "Files Modified" sections |
| Compression optimizes for tokens-per-request, ignoring re-fetch costs | Optimizes for tokens-per-task -- total cost including recovery when information is lost |
| No way to measure what compression preserved or destroyed | Probe-based evaluation asks targeted questions to verify functional compression quality |
| Full regeneration summaries lose details across repeated compression cycles | Anchored iterative summarization merges incrementally, preserving details from earlier cycles |
| Agent re-explores approaches it already tried because decisions were lost | Explicit "Decisions Made" section preserves reasoning chains across compressions |
| Compression triggers at arbitrary points, disrupting active reasoning | Strategic trigger points at 70-80% utilization or logical task boundaries |

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install context-compression@skillstack
```

### Prerequisites

No additional dependencies. Pairs well with `context-degradation` (understanding what compression prevents), `context-optimization` (broader optimization strategies), and `filesystem-context` (file-based offloading).

### Verify installation

After installing, test with:

```
How should I implement context compression for a long-running coding agent that keeps forgetting which files it modified?
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `"My agent session is hitting context limits -- what compression strategy should I use for a debugging workflow?"`
3. The skill activates and walks you through anchored iterative summarization with explicit sections for your use case
4. Follow up with: `"How do I test whether my compression is actually preserving the right information?"`
5. The skill provides probe-based evaluation templates you can apply to your compressed summaries

---

## System Overview

```
context-compression (plugin)
└── context-compression (skill)
    ├── Core methodology
    │   ├── Anchored Iterative Summarization (best quality)
    │   ├── Opaque Compression (best ratio)
    │   └── Regenerative Full Summary (best readability)
    ├── Compression triggers & decision logic
    ├── Three-phase workflow (Research → Planning → Implementation)
    ├── Probe-based evaluation framework
    └── references/
        └── evaluation-framework.md (probe types & scoring rubrics)
```

## What's Inside

| Component | Type | Description |
|---|---|---|
| `context-compression` | Skill | Core compression methodology, trigger strategies, and evaluation |
| `evaluation-framework.md` | Reference | Detailed probe types and scoring rubrics for measuring compression quality |
| Trigger evals | Test suite | 13 trigger evaluation cases |
| Output evals | Test suite | 3 output quality evaluation cases |

### Component Spotlights

#### context-compression (skill)

**What it does:** Activates when users need to reduce context size for LLM agents. Provides three compression approaches ranked by quality vs. compression ratio trade-offs, structured summary templates, trigger strategies, and a probe-based evaluation framework for measuring compression quality.

**Input -> Output:** A description of your agent's context pressure (session length, what information matters, re-fetch costs) -> Specific compression strategy with structured summary sections, trigger configuration, evaluation probes, and compression ratio guidance.

**When to use:**
- Agent sessions exceed context window limits
- Codebases exceed context windows (5M+ token systems)
- Designing conversation summarization strategies
- Debugging cases where agents "forget" what files they modified
- Building evaluation frameworks for compression quality

**When NOT to use:**
- Diagnosing why context is degrading (use `context-degradation`)
- KV-cache optimization or context partitioning (use `context-optimization`)
- Learning foundational context theory (use `context-fundamentals`)
- File-based offloading or scratch pads (use `filesystem-context`)

**Try these prompts:**

```
How should I compress a 90K-token debugging session without losing track of which files were modified and what the root cause was? The agent reads many files but only modifies a few. When context gets compressed, it forgets which files it already diagnosed and re-reads them. Re-reading a file costs 2-8K tokens. I need a summary structure that forces file-state tracking.
```

```
I'm building a coding agent that runs for 200+ turns on complex refactoring tasks. After about turn 100, it starts proposing approaches it already tried and abandoned. What summarization strategy prevents this? Sessions average 120K tokens. The agent works on a single codebase but touches 20-40 files per session.
```

```
My agent compresses at 70% context utilization using a simple summarize-everything approach. Sometimes it loses information it still needs mid-investigation, other times it waits too long. The agent does unpredictable debugging -- no clear phase structure. How should I tune the trigger strategy and what should the summary preserve?
```

```
How do I evaluate whether my compression strategy is actually preserving the right information? ROUGE scores are high (0.85+) but the agent still loses critical information after compression. I need a way to detect when specific information types -- file paths, error messages, decisions -- have been silently dropped. What probe questions should I run after each compression?
```

**Key references:**

| Reference | Topic |
|---|---|
| `evaluation-framework.md` | Probe types (recall, artifact, continuation, decision), scoring rubrics, and the six evaluation dimensions for compression quality |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate) | Good (specific, activates reliably) |
|---|---|
| "Make my context smaller" | "How should I compress a long debugging session while preserving file modification history?" |
| "Summarize this conversation" | "Design a structured summary format for a coding agent that needs to track files, decisions, and next steps across compressions" |
| "Use context-compression skill" | "My agent keeps forgetting which files it modified after compaction -- what summarization approach prevents this?" |
| "Help with tokens" | "How do I measure whether my compression strategy is losing critical information? Traditional metrics like ROUGE aren't working." |

### Structured Prompt Templates

**For designing a compression strategy:**
```
I'm building a [type of agent] that typically runs for [N turns/tokens]. The critical information it must preserve across compressions is [files modified / decisions made / error messages / etc.]. What compression approach and summary structure should I use?
```

**For evaluating compression quality:**
```
After compressing my agent's context, how do I test whether it preserved [specific information type]? I need probe questions that detect when compression has silently lost critical details.
```

**For optimizing trigger points:**
```
My agent compresses at [current threshold]. Sometimes it loses information it still needs, other times it compresses too late and hits the wall. How should I tune the trigger strategy for [workload type]?
```

### Prompt Anti-Patterns

- **Asking for generic summarization:** "Summarize this conversation" does not activate context-compression. The skill targets systematic compression strategy, not one-off summaries.
- **Focusing on tokens-per-request:** "How do I use fewer tokens per API call?" misses the point. The skill optimizes tokens-per-task, which may mean using slightly more tokens per request to avoid costly re-fetching.
- **Expecting automatic compression:** The skill teaches compression methodology and evaluation -- it does not automatically compress your current conversation. It helps you design and evaluate compression systems.

## Real-World Walkthrough

**Starting situation:** You are building a coding agent that helps developers debug issues. The agent routinely runs 150+ turn sessions, accumulating 80,000-100,000 tokens of conversation history. Users report that after about turn 80, the agent starts re-reading files it already examined and proposing fixes it already tried. You need a compression strategy.

**Step 1: Identify the core problem.** You ask: "My coding agent forgets what it already tried after long sessions. It re-reads files and proposes duplicate fixes. How should I handle context compression?"

The skill activates and immediately reframes the problem: you are optimizing for the wrong metric. Your current system probably uses aggressive summarization triggered by token count, which minimizes tokens-per-request. The right optimization target is tokens-per-task. The re-reading and duplicate proposals mean compression is destroying file tracking and decision history, forcing expensive re-exploration.

**Step 2: Choose a compression approach.** Based on your description (long sessions, file tracking critical, debugging workflow), the skill recommends anchored iterative summarization. It provides a structured summary template with sections for Session Intent, Root Cause, Files Modified (distinguishing read-only from modified), Decisions Made, Test Status, and Next Steps. Each section acts as a preservation checklist -- the summarizer must populate every section, preventing silent drift.

**Step 3: Configure compression triggers.** The skill walks you through trigger strategy selection. For debugging sessions with unpredictable flow, a sliding window approach works best: keep the last N turns in full plus the structured summary. Trigger compression at 70-80% context utilization. At task boundaries (when the agent shifts from diagnosis to implementation), perform a full summary refresh. This gives predictable context size without interrupting active reasoning.

**Step 4: Handle the artifact trail problem.** The skill warns about the weakest dimension in all compression methods: artifact trail integrity (2.2-2.5 out of 5.0 in evaluations). Even with structured summaries, file tracking degrades across long sessions. The recommendation is a separate artifact index -- a dedicated data structure outside the summary that tracks file paths, modification types, and timestamps. This index supplements the summary and survives multiple compression cycles.

**Step 5: Build evaluation probes.** To verify compression quality, the skill provides four probe types. Recall probes test factual retention ("What was the original error message?"). Artifact probes test file tracking ("Which files have we modified?"). Continuation probes test task planning ("What should we do next?"). Decision probes test reasoning chains ("What did we decide about the Redis issue?"). You run these probes after each compression cycle and compare answers against ground truth.

**Step 6: Measure and iterate.** You implement the strategy and measure results. Anchored iterative summarization achieves 98.6% compression ratio with a 3.70 quality score. The previous aggressive approach was getting 99.3% compression with a 3.35 quality score. The 0.7% additional tokens retained buy 0.35 quality points -- which translates to 40% fewer re-fetch cycles. Total tokens-per-task drops by 15%.

**Gotchas discovered:** The biggest surprise was that full regeneration summaries (rewriting the entire summary on each compression) scored lower than incremental merging despite being more readable. Repeated regeneration introduces subtle drift where each cycle loses a few details. Incremental merging preserves earlier details because it only summarizes newly-truncated content.

## Usage Scenarios

### Scenario 1: Long-running debugging agent

**Context:** Your debugging agent runs 200+ turn sessions investigating production issues. After turn 100, it starts proposing fixes it already tried.

**You say:** "Design a compression strategy for a debugging agent that needs to preserve error messages, file paths, and the diagnostic reasoning chain across 200+ turns."

**The skill provides:**
- Anchored iterative summarization template with debugging-specific sections
- Sliding window trigger at 75% utilization
- Separate artifact index recommendation for file tracking
- Four probe types to verify compression quality

**You end up with:** A compression system that preserves diagnostic history, reduces tokens-per-task by 15-25%, and includes automated quality checks.

### Scenario 2: Codebase migration at scale

**Context:** You are using an agent to migrate a 5M-token codebase from one framework to another. The agent cannot fit the entire codebase in context.

**You say:** "How do I compress a massive codebase exploration into something an agent can actually work with for a migration project?"

**The skill provides:**
- Three-phase workflow: Research (explore and document), Planning (compress to specification), Implementation (execute against spec)
- Structured research document template
- Example artifact seed strategy using a manual migration PR as reference

**You end up with:** A 2,000-word implementation specification compressed from 5M tokens of codebase, with the agent executing against the spec rather than raw exploration.

### Scenario 3: Evaluating a compression system

**Context:** You built a compression pipeline but have no way to measure whether it works. ROUGE scores are high but agents still forget things.

**You say:** "How do I evaluate my context compression system? ROUGE says summaries are good but agents still lose information."

**The skill provides:**
- Explanation of why ROUGE/embedding similarity fail for functional quality
- Probe-based evaluation with specific question types
- Six evaluation dimensions with scoring rubrics
- Benchmark data comparing compression methods

**You end up with:** An evaluation framework that measures what actually matters -- can the agent answer questions about its compressed history?

---

## Decision Logic

**When does anchored iterative summarization activate vs. opaque compression vs. regenerative summaries?**

The skill selects based on session characteristics:
- Sessions with 100+ messages where file tracking matters: anchored iterative (best quality, slightly less compression at 98.6%)
- Short sessions where maximum token savings are needed and re-fetch costs are low: opaque compression (99.3% compression, sacrifices interpretability)
- Sessions with clear phase boundaries where full-context review is acceptable: regenerative summaries (readable output, moderate quality at 3.44)

**What happens when compression loses critical information?**

The probe-based evaluation framework detects this. If artifact probes fail (agent cannot name modified files) or decision probes fail (agent cannot recall key choices), the evaluation signals quality degradation. Recovery involves adjusting summary sections to force preservation of the missing information type, or switching to a higher-quality compression method.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Artifact trail loss after multiple compression cycles | Agent cannot name files it modified 50+ turns ago | Implement a separate artifact index outside the summary; supplement structured summaries with dedicated file-state tracking |
| Compression triggers during active reasoning | Agent loses the thread of its current investigation mid-compression | Switch from fixed-threshold triggers to task-boundary triggers; compress only at logical completion points |
| Opaque compression destroys interpretability | Cannot verify what the compressed representation contains; debugging compression failures is impossible | Switch to anchored iterative summarization for any session where you need to audit compression quality |
| Incremental merge drift | Over many cycles, merged sections grow stale or contradictory | Periodically perform a full regeneration pass (every 5-10 compression cycles) to reset accumulated drift |

## Ideal For

- **Agent platform engineers** building long-running coding agents who need their agents to maintain coherent file tracking and decision history across 100+ turn sessions
- **AI infrastructure teams** optimizing LLM costs who want to reduce tokens-per-task rather than just tokens-per-request, achieving real savings without quality degradation
- **Evaluation engineers** building quality frameworks for compression who need probe-based evaluation methods that measure functional quality rather than lexical overlap
- **Teams migrating large codebases** with AI agents who need to compress millions of tokens of codebase exploration into actionable implementation specifications

## Not For

- **Diagnosing why context is degrading** -- if your agent is producing worse outputs and you do not know why, use `context-degradation` to identify the failure pattern first
- **KV-cache optimization or partitioning** -- if you need to optimize cache hit rates or split work across sub-agents, use `context-optimization`
- **File-based context offloading** -- if you want to use scratch pads or the file system to manage context, use `filesystem-context`

## Related Plugins

- **context-degradation** -- Understand what failure patterns compression prevents; compression is a mitigation strategy for degradation
- **context-fundamentals** -- Foundational context theory; understand context anatomy and attention mechanics before optimizing compression
- **context-optimization** -- Broader optimization techniques including KV-cache, observation masking, and partitioning
- **memory-systems** -- Compression relates to scratchpad and summary memory patterns in agent architectures
- **multi-agent-patterns** -- Context isolation through sub-agents as an alternative to compression

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
