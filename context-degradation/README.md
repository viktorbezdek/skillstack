> **v1.0.4** | Context Engineering | 5 iterations

# Context Degradation

> Diagnose and fix the predictable failure patterns that cause LLM agents to produce incorrect, irrelevant, or contradictory outputs as context grows -- lost-in-middle, poisoning, distraction, confusion, and clash patterns with empirical thresholds by model.
> Single skill + 1 reference document | 13 trigger evals, 3 output evals

## The Problem

AI agents degrade in predictable but invisible ways as their context grows. A coding agent that works flawlessly at turn 10 starts producing irrelevant outputs at turn 60. A retrieval system that finds the right answer in short documents misses it when the document grows to 30 pages. An agent that correctly follows instructions with one task loses track when juggling three. These failures are not random -- they follow specific, documented patterns -- but most teams treat them as mysterious quality problems.

The core issue is that context degradation is a continuum, not a binary state. Performance does not suddenly drop from "works" to "broken." It erodes gradually: 10-40% lower recall for information placed in the middle of context. A single irrelevant document reducing performance by a measurable step function. Hallucinations that persist because poisoned context creates feedback loops reinforcing incorrect beliefs. Teams that do not understand these patterns cannot diagnose them, and resort to cargo-cult solutions like "just use a bigger context window" -- which often makes things worse.

The cost of undiagnosed degradation compounds. An agent operating at 60% of its potential wastes 40% of the tokens spent on it. A team that does not recognize context poisoning spends hours debugging symptoms while the root cause -- a single hallucinated fact early in the conversation -- continues to corrupt every subsequent output.

## The Solution

This plugin provides a systematic taxonomy of five context degradation patterns -- lost-in-middle, context poisoning, context distraction, context confusion, and context clash -- with empirical benchmarks, model-specific degradation thresholds, and concrete architectural mitigations for each pattern. Rather than treating degradation as a vague quality problem, it gives you a diagnostic framework: observe the symptom, match it to a pattern, apply the specific fix.

The skill includes empirical data from the RULER benchmark and model-specific thresholds showing where degradation begins and where it becomes severe for Claude 4.5, GPT-5.2, and Gemini 3. It provides a four-bucket mitigation strategy (Write, Select, Compress, Isolate) and counterintuitive research findings -- like shuffled haystacks outperforming coherent ones, and single distractors having outsized impact. This turns degradation diagnosis from guesswork into engineering.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Agent quality drops at turn 60 and nobody knows why | Recognize lost-in-middle pattern: critical info placed in attention dead zone; reposition to beginning or end |
| Hallucinations persist despite corrections and compound over turns | Identify context poisoning: a single hallucinated fact early in conversation creates feedback loop; truncate to before poisoning point |
| Adding retrieved documents makes the agent worse, not better | Understand distraction: even one irrelevant document triggers a step-function performance drop; filter before loading |
| "Just use a bigger context window" is the default fix for everything | Know that larger contexts often hurt: degradation onset varies by model (64K for GPT-5.2, 100K for Claude Opus 4.5) |
| Agent mixes up instructions from different tasks in the same session | Recognize context confusion: multi-task sessions require explicit task segmentation and context isolation |
| No way to tell if context quality is degrading until outputs are clearly wrong | Monitor degradation thresholds: model-specific onset points and the four-bucket mitigation strategy |

## Context to Provide

The more precisely you describe your degradation symptoms, the more targeted the diagnosis. Vague descriptions ("my agent is getting worse") activate the skill but produce generic guidance. Specific descriptions activate pattern-matching against the five degradation types and generate concrete mitigations.

**What to include in your prompt:**
- **The model you are using** (Claude Sonnet 4.5, GPT-5.2, Gemini 3 Pro) -- degradation thresholds differ significantly by model
- **Approximate context size when symptoms appear** (in tokens or number of turns) -- this is the single most useful diagnostic signal
- **The specific symptom** (wrong outputs, ignored information, persistent errors, contradictory answers, wrong task context applied)
- **What has been tried** (if you have already attempted fixes, say what they were and why they did not work)
- **The context composition** (what fills the context: retrieved documents, tool outputs, conversation history, system prompt)

**What makes results better:**
- Describing *when* the problem starts (turn 30? after 80K tokens?) rather than just that it exists
- Specifying whether the symptom is consistent or intermittent
- Naming the agent type (coding agent, RAG system, customer support bot, multi-task agent)
- Sharing whether you have multiple tasks in one session or a single long conversation

**What makes results worse:**
- "My agent is broken" or "make my context better" -- too vague to match a pattern
- Assuming the model needs a larger context window -- this is frequently backwards
- Treating all degradation as one problem -- the five patterns have different causes and mitigations

**Template prompt:**
```
My [agent type] shows [specific symptom: irrelevant outputs / persistent hallucinations / wrong-task context / contradictory answers] after approximately [N turns or K tokens]. I am using [model name]. The context contains [describe composition: retrieved docs, tool outputs, history]. Approaches I have already tried: [list]. What degradation pattern matches this and how do I fix it?
```

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install context-degradation@skillstack
```

### Prerequisites

No additional dependencies. For maximum value, install `context-fundamentals` first (foundational theory) and pair with `context-optimization` (mitigation techniques) and `context-compression` (one specific mitigation strategy).

### Verify installation

After installing, test with:

```
My coding agent works great for the first 50 turns but starts producing irrelevant suggestions after that. How do I diagnose what's going wrong with the context?
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `"My agent's outputs are getting worse as conversations get longer -- what degradation pattern is this?"`
3. The skill walks you through symptom analysis and matches your situation to a specific degradation pattern
4. Follow up with: `"What are the degradation thresholds for Claude Sonnet 4.5?"`
5. The skill provides empirical benchmarks showing onset and severe degradation points for your model

---

## System Overview

```
context-degradation (plugin)
└── context-degradation (skill)
    ├── Five degradation patterns
    │   ├── Lost-in-middle (U-shaped attention)
    │   ├── Context poisoning (error feedback loops)
    │   ├── Context distraction (irrelevant info overwhelms)
    │   ├── Context confusion (wrong context applied)
    │   └── Context clash (contradictory information)
    ├── Empirical benchmarks & model thresholds
    ├── Four-bucket mitigation strategy
    ├── Counterintuitive research findings
    └── references/
        └── patterns.md (attention distribution analysis & technical detail)
```

## What's Inside

| Component | Type | Description |
|---|---|---|
| `context-degradation` | Skill | Degradation pattern taxonomy, empirical benchmarks, mitigation strategies |
| `patterns.md` | Reference | Attention distribution analysis, detailed technical reference for all five patterns |
| Trigger evals | Test suite | 13 trigger evaluation cases |
| Output evals | Test suite | 3 output quality evaluation cases |

### Component Spotlights

#### context-degradation (skill)

**What it does:** Activates when users encounter context-related performance degradation in LLM agents. Provides a diagnostic taxonomy of five degradation patterns with empirical thresholds by model, symptom-to-pattern matching, and concrete architectural mitigations using the four-bucket strategy (Write, Select, Compress, Isolate).

**Input -> Output:** A description of degradation symptoms (agent quality drops, hallucinations persist, outputs become irrelevant) -> Diagnosis matching symptoms to specific patterns, model-specific threshold data, and targeted mitigation recommendations.

**When to use:**
- Agent performance degrades unexpectedly during long conversations
- Debugging cases where agents produce incorrect or irrelevant outputs
- Designing systems that must handle large contexts reliably
- Investigating "lost in middle" phenomena
- Evaluating model selection for context-sensitive tasks

**When NOT to use:**
- Learning foundational context theory (use `context-fundamentals`)
- Compressing or summarizing context (use `context-compression`)
- KV-cache optimization or partitioning performance (use `context-optimization`)

**Try these prompts:**

```
My RAG system retrieves relevant documents but the agent ignores them when there are more than 5 documents in context. It was accurate with 3 documents. I'm using Claude Sonnet 4.5 with a 200K context window. What's happening and how do I fix the retrieval strategy?
```

```
We're seeing hallucinations that persist even after explicit correction. The agent keeps referencing a function name it invented at turn 12 even when I correct it directly. This is a coding agent with 40K tokens in context. How do I diagnose and recover from this?
```

```
What are the empirical degradation thresholds for Claude Opus 4.5 and Gemini 3 Pro? I need to process 150K-token documents reliably and need to choose which model degrades more gracefully at that scale.
```

```
My customer support agent handles single-issue tickets well but produces confused outputs when customers describe two problems in one session. The agent applies context from one issue to the other. What's the pattern and what architectural change fixes it?
```

**Key references:**

| Reference | Topic |
|---|---|
| `patterns.md` | Attention distribution analysis, detailed technical reference for lost-in-middle, poisoning, distraction, confusion, and clash patterns |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate) | Good (specific, activates reliably) |
|---|---|
| "My agent is broken" | "My agent works well for 50 turns then starts giving irrelevant suggestions -- what degradation pattern is this?" |
| "Make my context better" | "I'm seeing hallucinations that persist even after correction. How do I detect and recover from context poisoning?" |
| "Help with long context" | "What are the degradation thresholds for Claude Opus 4.5? I need to know when performance starts dropping." |
| "Fix my RAG" | "Adding more retrieved documents makes my agent worse. Is this the distraction effect, and how do I filter effectively?" |

### Structured Prompt Templates

**For diagnosing degradation:**
```
My [agent type] shows [specific symptom] after approximately [N turns/tokens]. The symptom manifests as [irrelevant outputs / persistent errors / wrong task context / contradictions]. Using [model name]. What degradation pattern matches this?
```

**For model selection:**
```
I need to handle contexts of [N tokens] for [task type]. What are the degradation thresholds for [model options]? Which model degrades most gracefully for this use case?
```

**For designing mitigations:**
```
I've identified [degradation pattern] in my agent. What architectural mitigation should I apply? I currently use [current approach] and my constraints are [cost / latency / complexity limits].
```

### Prompt Anti-Patterns

- **Blaming the model without diagnosis:** "Claude just stops working after a while" does not help. Identify the specific symptom (wrong outputs, ignored information, persistent errors) so the skill can match it to a pattern.
- **Assuming bigger context fixes everything:** "I need a model with a larger context window" is often backwards. The skill teaches when larger contexts hurt (degradation onset data shows this for each model).
- **Treating all degradation the same:** "My agent degrades" could be five different patterns, each with different mitigations. The skill requires symptom specificity to provide the right fix.

## Real-World Walkthrough

**Starting situation:** You have deployed a customer support agent that handles complex multi-step issues. It uses a 128K-token context window with Claude Sonnet 4.5. For the first few months, quality was excellent. Now, as conversations get longer (customers with complex account issues generate 50-80 turn conversations), support quality has dropped. The agent sometimes answers questions about the wrong account, references features the customer does not have, and occasionally repeats suggestions that the customer already tried.

**Step 1: Gather symptoms.** You ask: "My support agent's quality is dropping on long conversations. It confuses customer accounts, references wrong features, and repeats suggestions. What degradation pattern is this?"

The skill identifies multiple overlapping patterns. The wrong-account references suggest context confusion -- the agent is applying context from one part of the conversation to a different part. The wrong-feature references suggest context poisoning -- an incorrect detail entered context early and has been reinforced. The repeated suggestions suggest lost-in-middle -- earlier conversation turns where the customer rejected suggestions are buried in the attention dead zone.

**Step 2: Apply model-specific thresholds.** The skill provides Claude Sonnet 4.5's degradation profile: onset at approximately 80K tokens, severe degradation at approximately 150K tokens. Your 50-80 turn conversations are likely hitting 60-90K tokens, right at the onset boundary. This explains why degradation appeared gradually as conversations grew longer.

**Step 3: Diagnose the distraction pattern.** You mention that the agent retrieves customer account data, product documentation, and previous ticket history into context. The skill identifies this as context distraction compounding the other patterns -- the agent must attend to all retrieved documents even when they are irrelevant to the current question. Each irrelevant document competes for attention budget, worsening the lost-in-middle effect.

**Step 4: Apply the four-bucket mitigation strategy.** The skill recommends a layered approach:
- **Select:** Filter retrieved documents to only those relevant to the current question, not the entire conversation. Remove previous ticket history unless explicitly referenced.
- **Write:** Save resolved sub-topics to external storage and remove them from context. The customer's account data should be re-fetched per question, not carried through the entire conversation.
- **Compress:** Summarize resolved portions of the conversation into structured summaries with explicit customer-state sections.
- **Isolate:** For conversations exceeding 60K tokens, consider sub-agent architecture where each question gets a fresh context with only the customer state summary and relevant retrieved documents.

**Step 5: Address the poisoning vector.** The skill highlights that context poisoning requires specific intervention. If the agent hallucinated an incorrect account detail at turn 15, every subsequent turn reinforces that error. The fix is proactive validation: after retrieving account data, explicitly compare it against the structured summary to detect contradictions. When found, flag and correct rather than allowing the poisoned detail to propagate.

**Step 6: Verify with counterintuitive findings.** The skill shares that shuffled (incoherent) haystacks outperform coherent ones in retrieval tasks. This means your well-organized conversation history may actually create false associations that confuse retrieval. Consider interleaving context sections rather than presenting them chronologically.

**Gotchas discovered:** The most actionable finding was that a single irrelevant retrieved document has a step-function impact -- it does not degrade proportionally to the noise. Removing just the lowest-relevance document from each retrieval set produced a measurable quality improvement.

## Usage Scenarios

### Scenario 1: RAG system producing worse results with more documents

**Context:** Your retrieval-augmented generation system retrieves 10 documents per query. Quality was better when you only retrieved 3.

**You say:** "Adding more retrieved documents is making my agent worse. With 3 documents it's accurate, with 10 it gives wrong answers. What's happening?"

**The skill provides:**
- Diagnosis of context distraction pattern with step-function impact
- Explanation of why even one irrelevant document degrades performance
- Relevance filtering strategies before loading into context
- Model-specific thresholds for how much retrieved context different models handle

**You end up with:** A filtered retrieval strategy that loads only high-relevance documents, improving quality while using fewer tokens.

### Scenario 2: Choosing a model for long-context tasks

**Context:** You need to process documents of 100K-200K tokens and are evaluating models.

**You say:** "What are the empirical degradation thresholds for Claude Opus 4.5, GPT-5.2, and Gemini 3 Pro? I need reliable performance at 150K tokens."

**The skill provides:**
- Model-specific degradation onset and severe degradation thresholds
- Behavior patterns under context pressure (Claude refuses rather than fabricates, GPT-5.2 thinking mode reduces hallucination)
- RULER benchmark data showing only 50% of models claiming 32K+ actually maintain performance
- Recommendation based on task characteristics

**You end up with:** An evidence-based model selection decision with known degradation boundaries.

### Scenario 3: Persistent hallucinations in a coding agent

**Context:** Your coding agent hallucinated a function name at turn 12 and now references it in every subsequent suggestion despite corrections.

**You say:** "My agent made up a function name early in the session and keeps using it even when I correct it. The hallucination won't go away."

**The skill provides:**
- Diagnosis of context poisoning with compounding feedback loop
- Three recovery strategies: truncate to before poisoning, explicit correction with re-evaluation, restart with clean context preserving only verified information
- Prevention patterns: validate generated facts against codebase, detect contradiction between agent claims and tool outputs

**You end up with:** A recovery plan for the current session and prevention patterns to stop future poisoning.

---

## Decision Logic

**Which degradation pattern is causing the problem?**

The skill matches symptoms to patterns:
- Agent ignores information that exists in context -> Lost-in-middle (check information position)
- Errors persist despite correction and compound over turns -> Context poisoning (check when the error first appeared)
- More retrieved documents make outputs worse -> Context distraction (check relevance of retrieved content)
- Agent applies wrong context to current task -> Context confusion (check task segmentation)
- Agent produces contradictory outputs referencing conflicting facts -> Context clash (check for multiple conflicting sources)

**What happens when multiple patterns overlap?**

This is common. The skill recommends addressing patterns in severity order: poisoning first (it corrupts everything), then distraction (it amplifies other patterns), then confusion/clash (structural issues), then lost-in-middle (positional optimization). Each fix reduces the impact of remaining patterns.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Misdiagnosis: treating poisoning as lost-in-middle | Repositioning information does not help because the root issue is corrupted context, not position | Check when the incorrect information first appeared; if it originated from the agent rather than the input, it is poisoning, not positional |
| Over-filtering retrieved documents to avoid distraction | Agent now lacks information it needs, producing incomplete answers | Balance relevance filtering with a minimum-context guarantee; always include the most relevant N documents regardless of score |
| Degradation thresholds do not match observed behavior | Model behavior differs from benchmarks due to task-specific factors | Thresholds are guidelines, not guarantees; profile your specific workload to find actual degradation points |

## Ideal For

- **AI platform engineers** debugging degradation in production agent systems who need a diagnostic taxonomy rather than guesswork
- **ML engineers evaluating models** for long-context tasks who need empirical degradation thresholds by model to make evidence-based selection decisions
- **RAG system architects** whose retrieval systems degrade with more documents and who need to understand the distraction and confusion patterns
- **Agent reliability engineers** who need to design monitoring and mitigation strategies for context degradation before it impacts users

## Not For

- **Learning foundational context theory** -- if you do not yet understand context windows, attention mechanics, or progressive disclosure, start with `context-fundamentals`
- **Compressing or summarizing context** -- if you know the pattern is compression-related and need specific compression strategies, use `context-compression`
- **KV-cache optimization or partitioning** -- if you need to optimize cache hit rates or implement sub-agent architectures, use `context-optimization`

## Related Plugins

- **context-fundamentals** -- Foundational theory that this skill builds on; understand context anatomy before diagnosing failures
- **context-compression** -- Compression is one mitigation strategy for degradation; use after diagnosing the pattern
- **context-optimization** -- Broader optimization techniques (observation masking, partitioning) for mitigating degradation
- **multi-agent-patterns** -- Sub-agent isolation is the strongest mitigation for degradation; partitioning prevents context from growing large enough to degrade
- **memory-systems** -- External memory systems as a "Write" strategy for keeping context lean

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
