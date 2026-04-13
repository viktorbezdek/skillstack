> **v1.0.4** | Context Engineering | 5 iterations

# Context Compression

> Production strategies for compressing LLM context windows without destroying the information coding agents need most.

## The Problem

Long-running coding agent sessions generate tens of thousands of tokens of conversation history. When the context window fills up, something has to go. The naive approach -- aggressive summarization to minimize tokens per request -- silently drops the exact details agents rely on: file paths they modified, error messages they diagnosed, architectural decisions they made three steps ago.

The result is brutal. After compaction, agents re-read files they already changed, re-propose fixes they already applied, and lose track of which tests are passing. Teams watch their agents burn through token budgets not because the tasks are complex, but because compression destroyed the breadcrumb trail. A session that should cost 50K tokens ends up costing 200K because the agent spends 75% of its time recovering context it already had.

Worse, there is no standard way to measure whether compression actually preserved the information that matters. Traditional metrics like ROUGE scores and embedding similarity reward lexical overlap, not functional utility. A summary can score highly on those metrics while missing the one file path the agent needs to continue working. Without probe-based evaluation, teams have no idea their compression is lossy in ways that matter until agents start hallucinating answers about their own prior work.

## The Solution

This plugin provides three production-tested compression strategies -- anchored iterative summarization, opaque compression, and regenerative summaries -- each with measured compression ratios and quality scores from evaluations across 36,000+ messages. Instead of guessing which approach works, you get empirical data: anchored iterative summarization delivers 98.6% compression at a 3.70 quality score, while opaque compression achieves 99.3% compression but drops to 3.35 quality.

The skill teaches a structured summary format with explicit sections for session intent, files modified, decisions made, current state, and next steps. These sections act as checklists that the summarizer must populate, preventing silent information drift. When compression triggers, only the newly-truncated span gets summarized and merged into the existing structure -- no full regeneration, no accumulated loss.

For measuring whether your compression actually works, the plugin includes a probe-based evaluation framework with four probe types (recall, artifact, continuation, decision) and a six-dimension scoring rubric. After compression, you ask the agent targeted questions. If it hallucinates answers about its own prior work, your compression is broken in ways that ROUGE scores will never catch.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Agents forget which files they modified after compaction and re-propose the same changes | Structured summary sections with explicit `Files Modified` tracking survive repeated compression cycles |
| Token budgets blow up from re-fetching context that compression destroyed | Tokens-per-task optimization targets total cost including re-fetching, not just per-request size |
| No way to tell if compression preserved the right information until agents hallucinate | Probe-based evaluation with recall, artifact, continuation, and decision probes catches lossy compression immediately |
| One-size-fits-all compression regardless of session type | Three methods with measured tradeoffs: pick anchored (best quality), opaque (best ratio), or regenerative (best readability) |
| Compression triggers at arbitrary points, producing messy summaries | Four trigger strategies with documented tradeoffs: fixed threshold, sliding window, importance-based, and task-boundary |
| Large codebases (5M+ tokens) overwhelm the context window with no clear strategy | Three-phase workflow compresses a 5M-token codebase into ~2,000 words of implementation specification |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install context-compression@skillstack
```

### Verify installation

After installing, test with:

```
Help me design a compression strategy for my coding agent that keeps losing track of modified files
```

## Quick Start

1. Install the plugin using the commands above
2. Start a conversation: `My agent forgets what files it changed after context compaction -- how do I fix this?`
3. The skill walks you through anchored iterative summarization with structured summary sections that explicitly track file modifications, decisions, and next steps
4. Apply the structured summary template to your agent's compaction logic and test with probe-based evaluation
5. Measure improvement: ask the agent recall and artifact probes after compression to verify it retained the details that matter

## What's Inside

| Component | Description |
|---|---|
| `context-compression` skill | Core skill covering three compression methods, tokens-per-task optimization, structured summary sections, trigger strategies, and the three-phase compression workflow |
| `evaluation-framework.md` reference | Complete evaluation framework with four probe types, six-dimension scoring rubrics, LLM judge configuration, and benchmark results across 36,000+ messages |
| 13 trigger eval cases | Validates correct skill activation and near-miss rejection |
| 3 output eval cases | Tests compression guidance quality, approach review, and greenfield setup |

### context-compression

**What it does:** Activates when you need to compress conversation history, design summarization strategies, or debug cases where agents lose track of their own work after compaction. Provides three compression methods with empirical quality scores, structured summary templates, trigger strategies, and a complete evaluation framework.

**Try these prompts:**

```
My coding agent runs 200+ message sessions and loses context after compaction -- design a compression strategy that preserves file tracking
```

```
Review my current summarization approach -- I'm using full regeneration every 50 messages but the agent keeps forgetting decisions we made earlier
```

```
What's the best compression trigger strategy for a debugging session where I need to preserve error messages and stack traces?
```

```
Set up a probe-based evaluation to measure whether my agent's compression is preserving the information it needs to continue working
```

```
I have a 5 million token codebase that exceeds the context window -- how do I compress it into something workable for implementation?
```

**Key references:**

| Reference | Topic |
|---|---|
| `evaluation-framework.md` | Four probe types (recall, artifact, continuation, decision), six-dimension scoring rubrics, LLM judge configuration, and benchmark results |

## Real-World Walkthrough

You are building a coding agent that helps developers debug production issues. The agent sessions routinely hit 150+ messages as it traces through logs, reads source files, and iterates on fixes. At around message 80, context compaction kicks in. After compaction, the agent starts re-reading files it already examined and proposes fixes for issues it already resolved. Developers are frustrated -- the agent wastes 30 minutes redoing work it already did.

You open Claude Code and describe the problem:

```
My debugging agent loses track of which files it modified after context compaction. Sessions are 150+ messages. The agent re-reads files and re-proposes fixes after compression. Help me design a compression strategy.
```

The context-compression skill activates and walks you through the tokens-per-task framing first. Your current approach optimizes for tokens-per-request -- compressing as aggressively as possible to fit more history into the window. But the re-fetching costs mean you are spending more total tokens than before compression. The real metric is tokens-per-task: total tokens consumed from the start of the debugging session to its completion, including all the re-exploration caused by lossy compression.

The skill recommends anchored iterative summarization. You define structured summary sections tailored to debugging workflows:

```markdown
## Session Intent
[What bug the user is investigating]

## Root Cause Analysis
[Current hypothesis and evidence]

## Files Examined
- [file]: [what was found, read-only or modified]

## Fixes Applied
- [file]: [what was changed and why]

## Test Status
[Current pass/fail counts, specific failing tests]

## Decisions Made
- [Decision]: [Reasoning]

## Next Steps
1. [Immediate next action]
2. [Follow-up actions]
```

You implement this template in your agent's compaction logic. When compression triggers at 75% context utilization, the summarizer must populate every section. On subsequent compressions, only the newly-truncated span gets summarized and merged into the existing sections. The `Files Examined` and `Fixes Applied` sections accumulate across compression cycles rather than being regenerated from scratch.

Now you need to verify it actually works. The skill guides you through setting up probe-based evaluation. After compression, you inject four types of probe questions:

- **Recall probe:** "What was the original error message?" -- tests whether the specific error code and stack trace survived compression
- **Artifact probe:** "Which files have we modified so far?" -- tests whether the file tracking sections are complete
- **Continuation probe:** "What should we do next?" -- tests whether the agent can continue the debugging workflow without re-exploring
- **Decision probe:** "Why did we choose connection pooling over per-request connections?" -- tests whether reasoning chains survived

You run your first evaluation across 20 debugging sessions. The recall probes score 4.1 out of 5.0 -- error messages are well preserved. The artifact probes score 2.8 -- file tracking is better than before (was 2.2 with aggressive compression) but still the weakest dimension. The continuation probes score 3.9 -- the agent can generally pick up where it left off. The decision probes score 3.5 -- reasoning chains partially survive.

The artifact trail score of 2.8 tells you that even structured summarization is not fully solving file tracking. Following the skill's guidance, you add a separate artifact index outside the summary -- a simple list of files with their modification status that persists independently of the summary. This dedicated tracking pushes artifact probe scores to 3.8.

After two weeks of running the improved compression, you measure the impact: total tokens-per-task dropped 35% because the agent stopped re-fetching files it already read. Developer satisfaction improved because the agent no longer proposes duplicate fixes. The compression ratio is 98.6% -- slightly less aggressive than your old approach (99.1%) but the 0.5% extra tokens retained buy dramatically better continuation quality.

## Usage Scenarios

### Scenario 1: Fixing agent amnesia after compaction

**Context:** You maintain a coding agent that helps with feature development. After every compaction cycle, the agent forgets which files it created and starts proposing changes that conflict with its own prior work.

**You say:** `My agent keeps forgetting which files it modified after compaction -- it re-proposes changes it already made. How do I fix this?`

**The skill provides:**
- Anchored iterative summarization with explicit `Files Modified` sections
- Incremental merging strategy that accumulates file tracking across compression cycles
- Structured summary template with session intent, files, decisions, and next steps
- Recommendation to add a separate artifact index for critical file tracking

**You end up with:** A compression strategy that preserves file tracking across compaction cycles, eliminating duplicate work.

### Scenario 2: Choosing between compression methods

**Context:** You are building an agent framework and need to pick a default compression strategy. You have usage data showing sessions range from 30 to 300+ messages with varying re-fetch costs.

**You say:** `I need to choose a default compression method for my agent framework -- walk me through the tradeoffs between the approaches`

**The skill provides:**
- Decision matrix with compression ratio vs quality score for all three methods
- Guidance on when each method fits: anchored iterative for long sessions with file tracking, opaque for short sessions with cheap re-fetching, regenerative for interpretability-critical use cases
- Benchmark data from 36,000+ messages across each approach
- Token cost analysis showing how quality score differences translate to re-fetching costs

**You end up with:** A documented decision with data backing your compression method choice, tailored to your usage patterns.

### Scenario 3: Evaluating compression quality

**Context:** You implemented a custom summarization pipeline for your agent, but you have no way to measure whether it is actually preserving the information the agent needs.

**You say:** `How do I measure whether my agent's compression is actually working? ROUGE scores don't seem to catch the failures I'm seeing`

**The skill provides:**
- Probe-based evaluation framework with four probe types (recall, artifact, continuation, decision)
- Six-dimension scoring rubric covering accuracy, context awareness, artifact trail, completeness, continuity, and instruction following
- LLM judge configuration for automated evaluation
- Benchmark scores to compare your results against

**You end up with:** A repeatable evaluation pipeline that directly measures functional compression quality rather than surface-level text similarity.

### Scenario 4: Compressing a massive codebase for implementation

**Context:** You need an agent to implement changes across a 5M+ token codebase that exceeds the context window. The agent cannot hold the entire codebase in context.

**You say:** `I have a huge codebase that doesn't fit in context -- how do I compress it so an agent can implement changes against it?`

**The skill provides:**
- Three-phase compression workflow: Research (explore and document), Planning (convert to implementation spec), Implementation (execute against spec)
- Guidance on compressing a 5M-token codebase to ~2,000 words of specification
- Strategy for using example artifacts as seeds to capture business constraints that static analysis misses

**You end up with:** A structured approach to reducing a massive codebase into an actionable implementation specification the agent can work against.

### Scenario 5: Configuring compression triggers

**Context:** Your agent's compression fires at a fixed 80% threshold, but sometimes it triggers mid-task and produces messy summaries that lose the current debugging thread.

**You say:** `My compression triggers at 80% utilization but it often fires in the middle of debugging -- the summaries lose the current thread. How should I configure the trigger?`

**The skill provides:**
- Four trigger strategies with documented tradeoffs: fixed threshold, sliding window, importance-based, and task-boundary
- Recommendation for task-boundary triggering during debugging sessions (compress at logical completions, not arbitrary thresholds)
- Sliding window approach as a pragmatic default for most coding agent use cases
- Guidance on combining strategies (e.g., task-boundary preferred, fixed threshold as safety net)

**You end up with:** A trigger configuration that fires at clean task boundaries, producing higher-quality summaries that preserve the current debugging thread.

## Ideal For

- **Agent framework developers** building compaction logic -- the three methods with empirical quality scores eliminate guesswork about which approach to implement
- **Teams running long coding sessions** (100+ messages) where agents lose track of prior work after compaction
- **Anyone measuring compression quality** -- the probe-based evaluation framework replaces unreliable metrics like ROUGE with functional testing
- **Architects working with large codebases** (5M+ tokens) that exceed context windows and need a structured compression workflow
- **DevTools teams** building developer-facing agents where re-fetching costs directly impact user experience and token budgets

## Not For

- **Diagnosing why context is degrading** (lost-in-middle, poisoning, distraction patterns) -- use [context-degradation](../context-degradation/) instead
- **Optimizing KV-cache, observation masking, or context partitioning** -- use [context-optimization](../context-optimization/) instead
- **Learning foundational context theory** (what context is, how attention works) -- use [context-fundamentals](../context-fundamentals/) instead
- **Offloading context to the file system** via scratch pads and plan persistence -- use [filesystem-context](../filesystem-context/) instead

## How It Works Under the Hood

The plugin is a single-skill architecture with one reference document providing evaluation depth.

The **core skill** (`SKILL.md`) covers the complete compression methodology: three production-ready compression methods with empirical benchmarks, the tokens-per-task optimization framework, structured summary templates with explicit sections, four compression trigger strategies, and a three-phase workflow for large codebases. It provides practical implementation guidance for anchored iterative summarization, including how to define sections, trigger compression, and merge incrementally.

The **evaluation framework reference** (`evaluation-framework.md`) provides the depth layer for measuring compression quality. It defines four probe types (recall, artifact, continuation, decision), a six-dimension scoring rubric, LLM judge configuration for automated evaluation, and benchmark results from 36,000+ messages. This reference activates when you need to build or run compression evaluations rather than just implement a compression strategy.

The skill explicitly routes to sibling plugins when the user's problem is not compression: context-degradation for failure diagnosis, context-optimization for KV-cache and partitioning strategies, context-fundamentals for theory, and filesystem-context for file-based offloading.

## Related Plugins

- **[Context Degradation](../context-degradation/)** -- Diagnosing context failures: lost-in-middle, poisoning, distraction, clash, and confusion patterns with empirical thresholds by model
- **[Context Fundamentals](../context-fundamentals/)** -- Foundational theory of context engineering: what context is, how attention works, progressive disclosure, and context budgeting
- **[Context Optimization](../context-optimization/)** -- Extending effective context capacity: KV-cache optimization, observation masking, context partitioning, and retrieval strategies
- **[Filesystem Context](../filesystem-context/)** -- Using the file system for context: scratch pads, plan persistence, dynamic skill loading, and sub-agent file workspaces

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
