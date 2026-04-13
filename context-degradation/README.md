> **v1.0.4** | Context Engineering | 5 iterations

# Context Degradation

> Diagnose and fix the predictable failure patterns that cause LLM agents to produce incorrect, irrelevant, or contradictory outputs as context grows.

## The Problem

When a coding agent works through a long session and suddenly starts producing wrong answers, most teams blame the model. They retry the prompt, restart the session, or switch models -- all of which waste time and tokens without addressing the root cause. The real problem is context degradation: predictable, measurable failure patterns that emerge as context length increases.

These failures are not random. Information placed in the middle of context receives 10-40% less attention than information at the beginning or end. A single irrelevant document loaded into context reduces performance on relevant documents -- not proportionally, but as a step function where any distractor triggers degradation. Errors from tool outputs or hallucinated intermediate results compound through repeated reference, creating poisoning feedback loops that reinforce incorrect assumptions. And when accumulated context contains contradictions from different sources or different points in time, the model cannot determine which information to trust.

Without understanding these patterns, teams build agents that work beautifully in demos (short context, clean inputs) and fail unpredictably in production (long context, noisy inputs, accumulated contradictions). They spend weeks debugging "model quality issues" that are actually architectural problems with how context is assembled and maintained.

## The Solution

This plugin maps the five distinct context degradation patterns -- lost-in-middle, poisoning, distraction, confusion, and clash -- with empirical thresholds showing exactly when each pattern triggers for specific models. Instead of treating context failures as mysterious model behavior, you get diagnostic frameworks that identify which pattern is causing your agent's failures and architectural patterns that prevent each one.

The skill provides model-specific degradation thresholds: Claude Opus 4.5 begins degrading around 100K tokens with severe degradation at 180K; GPT-5.2 starts at 64K but resists severe degradation until 200K in thinking mode; Gemini 3 Pro handles 500K before onset. These numbers inform concrete architectural decisions about context budgets, compaction triggers, and when to split work across sub-agents.

You also get the four-bucket mitigation framework -- Write (save context externally), Select (filter what enters context), Compress (reduce tokens while preserving information), and Isolate (split across sub-agents) -- with guidance on which strategies address which degradation patterns.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Agent produces wrong answers in long sessions and you blame the model | You identify the specific degradation pattern (lost-in-middle, poisoning, distraction, confusion, or clash) and apply the targeted fix |
| No idea when context length starts hurting performance for your model | Model-specific thresholds tell you exactly when degradation begins and becomes severe |
| Irrelevant retrieved documents silently degrade performance on relevant ones | You understand the distractor effect and apply relevance filtering before loading context |
| Hallucinations from early tool outputs compound into persistent incorrect beliefs | You detect context poisoning symptoms and know the three recovery approaches |
| Multi-source retrieval loads contradictory information and the agent picks randomly | You apply conflict marking, priority rules, and version filtering to prevent clash |
| Critical information buried in the middle of context gets ignored | You place critical info at attention-favored positions (beginning and end) using U-shaped attention awareness |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install context-degradation@skillstack
```

### Verify installation

After installing, test with:

```
My agent produces good results for the first 50 messages but starts giving wrong answers around message 80 -- help me diagnose what's going wrong
```

## Quick Start

1. Install the plugin using the commands above
2. Describe your agent's failure: `My agent starts hallucinating file paths after long debugging sessions -- it references files that don't exist`
3. The skill identifies the likely degradation pattern (context poisoning from hallucinated intermediate results) and walks you through detection and recovery
4. Apply the recommended mitigation: context validation checkpoints, explicit poisoning markers, or sub-agent isolation
5. Use the empirical thresholds to set compaction triggers before your model's degradation onset point

## What's Inside

| Component | Description |
|---|---|
| `context-degradation` skill | Core skill covering five degradation patterns with detection criteria, empirical model thresholds, the four-bucket mitigation framework, architectural patterns, and counterintuitive research findings |
| `patterns.md` reference | Technical reference with attention distribution analysis, measurement code, and detailed diagnostic procedures |
| 13 trigger eval cases | Validates correct skill activation and near-miss rejection |
| 3 output eval cases | Tests degradation diagnosis, pattern identification, and mitigation guidance |

### context-degradation

**What it does:** Activates when your agent's performance degrades unexpectedly, when you are debugging incorrect or irrelevant outputs in long sessions, when you need to understand why larger context windows are not improving results, or when you are designing systems that must handle large contexts reliably. Provides diagnostic frameworks for five distinct failure patterns with empirical data and concrete mitigation strategies.

**Try these prompts:**

```
My coding agent works fine for short tasks but produces increasingly wrong answers during long debugging sessions -- what's happening and how do I fix it?
```

```
I'm loading 20 retrieved documents into context for my RAG agent but quality is worse than with 5 documents -- help me understand the distraction effect
```

```
My agent keeps referencing a wrong assumption from 30 messages ago even though I corrected it -- is this context poisoning?
```

```
I need to pick between Claude, GPT, and Gemini for a task that requires processing 150K tokens of context reliably -- what are the degradation thresholds?
```

```
We're seeing contradictory outputs when our agent pulls information from multiple knowledge bases -- how do we prevent context clash?
```

**Key references:**

| Reference | Topic |
|---|---|
| `patterns.md` | Technical reference with attention distribution analysis, U-shaped curve measurement code, and detailed diagnostic procedures for each degradation pattern |

## Real-World Walkthrough

You are building a code review agent that reads pull requests, loads relevant source files, and produces review comments. During testing, you notice a pattern: reviews of small PRs (under 10 files, under 5K tokens of diff) are excellent -- thorough, specific, and accurate. But reviews of large PRs (30+ files, 50K+ tokens of diff) produce generic comments, miss obvious issues, and sometimes reference code from the wrong file.

You open Claude Code and describe the problem:

```
My code review agent produces great reviews for small PRs but the quality drops significantly for large PRs. Reviews become generic, miss issues, and sometimes reference the wrong file. What's going on?
```

The context-degradation skill activates and walks you through a systematic diagnosis. It identifies three degradation patterns likely at play in your situation.

First, **lost-in-middle**: your agent loads all PR files sequentially into context. The files in the middle of the context receive 10-40% less attention than files at the beginning and end. Critical changes buried in the middle of a 30-file PR are being under-attended. The skill recommends placing the most-changed files at the beginning and end of context, and loading less-changed files in the middle where lower attention is acceptable.

Second, **context distraction**: loading 30 source files means the agent is attending to massive amounts of code that is not part of the diff. Every line of context competes for attention budget. Even clearly irrelevant boilerplate code consumes attention that should go to the actual changes. The skill recommends applying relevance filtering -- load only the functions and classes that are directly modified or called by modified code, not entire files.

Third, the wrong-file references suggest **context confusion**: with 30 files loaded, the agent is mixing up which code belongs to which file. Similar function names across different files, shared interfaces, and common patterns create confusion about what context applies to what. The skill recommends explicit file boundaries with clear headers and namespacing in context.

You implement the recommendations in stages. First, you reorder context loading to place the highest-impact files at attention-favored positions. You measure the improvement: review accuracy on files at position 15-25 (previously the "lost middle") improves from 62% to 78%.

Second, you add relevance filtering. Instead of loading entire files, you extract only the modified functions plus their immediate callers and callees. This reduces context from 50K tokens to 18K tokens for the same 30-file PR. Review quality jumps dramatically -- the agent now catches issues it previously missed because it has more attention budget for relevant code.

Third, you add explicit file boundary markers with full file paths and clear separators. The wrong-file references drop from 15% to 2%.

But you notice one more issue: when the agent encounters a complex file early in the review, it sometimes generates an incorrect assessment that it then references when reviewing related files later. This is **context poisoning** -- the wrong assessment becomes "ground truth" in context and compounds through subsequent references. You add a validation checkpoint: after each file review, the agent re-checks its assessment against the actual code before moving to the next file. This breaks the poisoning feedback loop.

The final result: your code review agent now handles 50+ file PRs with quality comparable to its small-PR performance. Total context usage dropped 65% from relevance filtering, and the remaining context is organized for optimal attention distribution. The fixes were entirely architectural -- the model did not change, the prompts did not change, only the context assembly strategy changed.

## Usage Scenarios

### Scenario 1: Diagnosing agent performance degradation in long sessions

**Context:** You have a debugging agent that works well for the first hour but produces increasingly wrong suggestions as the session continues. By message 100, it is proposing fixes that contradict its own earlier analysis.

**You say:** `My debugging agent starts contradicting itself after about 100 messages -- earlier it correctly identified a race condition but now it's suggesting single-threaded approaches that would break the fix`

**The skill provides:**
- Diagnosis of likely context clash (earlier analysis contradicts later accumulated context)
- Model-specific degradation threshold check (is 100 messages exceeding your model's reliable range?)
- Four-bucket mitigation: Write (save the race condition finding to a scratchpad), Compress (compact resolved investigation threads), Isolate (split the debugging into sub-agent phases)
- Compaction trigger recommendation based on your model's degradation onset

**You end up with:** A concrete diagnosis of why the agent contradicts itself and an architectural plan to prevent it.

### Scenario 2: RAG quality decreasing with more retrieved documents

**Context:** You built a documentation Q&A agent with retrieval. Quality was excellent with top-5 retrieval but drops when you increase to top-20 to improve recall.

**You say:** `I increased my RAG retrieval from top-5 to top-20 documents and answer quality got worse, not better -- how is more context hurting?`

**The skill provides:**
- Explanation of the distractor effect: irrelevant retrieved documents compete for attention budget
- Evidence that a single distractor triggers a step-function degradation, not proportional noise
- Relevance filtering strategies to apply before loading into context
- Guidance on balancing recall (more documents) vs precision (less distraction)

**You end up with:** A retrieval strategy that maintains high recall without degrading answer quality.

### Scenario 3: Selecting a model for large-context processing

**Context:** You need to process a 200K-token codebase for architectural analysis. You want to pick the model least likely to degrade at that context length.

**You say:** `I need to process 200K tokens of code for architectural analysis -- which model handles that context length best without degradation?`

**The skill provides:**
- Model-specific degradation thresholds: onset and severe degradation points for Claude 4.5, GPT-5.2, and Gemini 3
- Behavioral patterns under pressure: Claude 4.5 refuses rather than fabricates, GPT-5.2 benefits from thinking mode, Gemini 3 Pro handles the longest contexts
- Cost implications of large-context processing (non-linear cost growth)
- Architectural alternative: split the 200K tokens across sub-agents rather than processing in one window

**You end up with:** A model selection decision backed by empirical degradation data, with a fallback architecture if single-context processing is too unreliable.

### Scenario 4: Detecting and recovering from context poisoning

**Context:** Your agent generated an incorrect API response format early in a session. Now every subsequent API design decision references this wrong format and the agent resists correction.

**You say:** `My agent hallucinated an incorrect API format early in the session and now every new endpoint follows the wrong pattern -- even when I correct it, the next endpoint reverts to the wrong format`

**The skill provides:**
- Identification as context poisoning with compounding feedback loop
- Three recovery approaches: truncate context to before the poisoning point, explicitly mark the poisoned content with correction, or restart with clean context preserving only verified decisions
- Prevention strategies: validate intermediate outputs before they enter persistent context, use explicit checkpoints for critical design decisions
- Architectural pattern: isolate design decisions in a separate state document that can be edited independently of conversation context

**You end up with:** A recovery plan for the current session and architectural changes to prevent poisoning in future sessions.

## Ideal For

- **Agent developers** debugging unexplained quality drops in production -- the five degradation patterns provide a diagnostic checklist instead of guessing
- **RAG system builders** who need to understand why more retrieved context is not producing better answers
- **Teams selecting models** for large-context workloads -- empirical thresholds replace vendor claims with measured reality
- **Architects designing multi-agent systems** who need to understand when context isolation becomes necessary
- **Anyone running long agent sessions** (100+ messages) where performance degrades over time

## Not For

- **Learning foundational context theory** (what context is, how attention works) -- use [context-fundamentals](../context-fundamentals/) instead
- **Compressing or summarizing context** to reduce token usage -- use [context-compression](../context-compression/) instead
- **KV-cache optimization, observation masking, or context partitioning** -- use [context-optimization](../context-optimization/) instead
- **Offloading context to the file system** via scratch pads -- use [filesystem-context](../filesystem-context/) instead

## How It Works Under the Hood

The plugin is a single-skill architecture with one technical reference document.

The **core skill** (`SKILL.md`) covers five degradation patterns in depth: lost-in-middle (U-shaped attention curves, attention sink mechanics), context poisoning (three pathways, compounding effects, detection symptoms, recovery approaches), context distraction (the distractor step-function, attention budget competition), context confusion (task-context mismatches, multi-source interference), and context clash (contradictory information from multiple sources, resolution approaches). It includes model-specific degradation thresholds with empirical data, counterintuitive research findings (shuffled haystacks outperform coherent ones, single distractors have outsized impact), the four-bucket mitigation framework (Write, Select, Compress, Isolate), and architectural patterns for prevention.

The **patterns reference** (`patterns.md`) provides the technical depth layer with attention distribution measurement code, U-shaped curve analysis procedures, and detailed diagnostic workflows for each pattern. This reference activates when you need to measure degradation quantitatively rather than just identify and mitigate patterns.

The skill explicitly routes to sibling plugins: context-fundamentals for theory, context-compression for summarization strategies, and context-optimization for KV-cache and partitioning techniques.

## Related Plugins

- **[Context Compression](../context-compression/)** -- Reducing context size: summarization strategies, anchored iterative summarization, and probe-based evaluation
- **[Context Fundamentals](../context-fundamentals/)** -- Foundational theory: what context is, how attention works, progressive disclosure, and context budgeting
- **[Context Optimization](../context-optimization/)** -- Extending effective context capacity: KV-cache optimization, observation masking, and retrieval strategies
- **[Filesystem Context](../filesystem-context/)** -- Using the file system for context: scratch pads, plan persistence, and sub-agent file workspaces

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
