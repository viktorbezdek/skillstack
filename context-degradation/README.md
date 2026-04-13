> **v1.0.4** | Context Engineering | 5 iterations

# Context Degradation

Diagnose and mitigate the predictable failure modes that emerge as LLM context grows -- lost-in-middle, context poisoning, distraction, confusion, and clash -- with empirical thresholds by model.

## What Problem Does This Solve

Agent and LLM failures are frequently misdiagnosed as model capability problems when the actual cause is context degradation. Information buried in the middle of a long conversation gets ignored (lost-in-middle with 10-40% recall loss). An early hallucination compounds through repeated reference until the agent's entire reasoning chain is corrupted (context poisoning). Irrelevant retrieved documents drown out the relevant ones (context distraction). The model applies constraints from a different task (context confusion). Contradictory information accumulates until reasoning derails (context clash). These are predictable, named patterns with empirical thresholds and specific mitigations -- not random failures.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install context-degradation@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## What's Inside

This is a single-skill plugin with one reference document:

| Component | Description |
|---|---|
| `skills/context-degradation/SKILL.md` | Core skill covering five degradation patterns (lost-in-middle, poisoning, distraction, confusion, clash), empirical RULER benchmark data, model-specific degradation thresholds, the four-bucket mitigation approach (Write, Select, Compress, Isolate), and counterintuitive findings from research |
| `references/patterns.md` | Technical reference with Python code for attention distribution measurement, lost-in-middle detection, hallucination tracking, error propagation analysis, context relevance scoring, a ContextHealthMonitor class with composite health scoring, alert thresholds, and strategic truncation/recovery procedures |
| `evals/trigger-evals.json` | Trigger scenarios validating correct activation and near-miss rejection |
| `evals/evals.json` | Output quality scenarios testing degradation diagnosis and guidance |

## Usage Scenarios

**1. Agent gives wrong answers after long conversations**

Your agent works well for the first 20 turns but starts hallucinating around turn 30. The skill provides model-specific degradation thresholds: Claude Sonnet 4.5 degrades at ~80K tokens (severe at ~150K), Claude Opus 4.5 at ~100K (severe at ~180K), GPT-5.2 at ~64K (severe at ~200K), Gemini 3 Pro at ~500K (severe at ~800K). Compare your conversation's token count against these thresholds to determine if degradation is the root cause.

**2. Early error pollutes all subsequent reasoning**

A tool returned malformed output in turn 5, and by turn 15 the agent is confidently building on incorrect assumptions. This is context poisoning -- the compounding feedback loop symptom. The skill maps three entry pathways (tool output errors, incorrect retrieved documents, model-generated hallucinations) and provides recovery techniques: truncate context to before the poisoning point, explicitly note the poisoning and request re-evaluation, or restart with clean context preserving only verified information.

**3. Adding more retrieved documents makes responses worse**

Counter to expectation, adding more context documents is degrading output quality. The skill explains the distractor effect: even a single irrelevant document reduces performance, and the impact follows a step function rather than scaling proportionally with noise. Mitigation: apply relevance filtering before loading documents, use namespacing, and consider whether information needs to be in context or can be accessed through tool calls instead.

**4. Agent uses the wrong tool or addresses the wrong task**

Your multi-task agent calls tools that are appropriate for a different task, or mixes requirements from multiple sources. This is context confusion -- the model cannot determine which context applies to the current situation. Architectural solutions include explicit task segmentation (different tasks get different context windows), clear transitions between task contexts, and state management that isolates context per objective.

**5. Selecting the right model for long-context workloads**

The skill provides a comparative model behavior table: Claude 4.5 series has the lowest hallucination rates and tends to refuse rather than fabricate. GPT-5.2 thinking mode reduces hallucination through step-by-step verification but increases latency. Gemini 3 Pro/Flash offers a 1M context window with strong multi-modal reasoning. Match model characteristics to your failure tolerance and latency requirements.

## How to Use

**Direct invocation:**

```
Use the context-degradation skill to diagnose why my agent degrades after long conversations
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `context-degradation`
- `lost-in-middle`
- `context-poisoning`
- `attention-patterns`

## When to Use / When NOT to Use

**Use when:**
- Agent performance degrades unexpectedly during long conversations
- Debugging incorrect or irrelevant agent outputs
- Designing systems that must handle large contexts reliably
- Investigating "lost in middle" phenomena
- Evaluating which model handles long contexts best for your use case

**Do NOT use when:**
- Learning context basics or theory -- use [context-fundamentals](../context-fundamentals/) instead
- Compressing or summarizing context -- use [context-compression](../context-compression/) instead
- Optimizing KV-cache or context partitioning -- use [context-optimization](../context-optimization/) instead

## Related Plugins

- **[Context Compression](../context-compression/)** -- Reducing context size through summarization strategies, anchored iterative summarization, and probe-based evaluation
- **[Context Fundamentals](../context-fundamentals/)** -- Foundational theory: what context is, how attention works, progressive disclosure, and context budgeting
- **[Context Optimization](../context-optimization/)** -- Extending effective context capacity: KV-cache optimization, observation masking, and context partitioning
- **[Filesystem Context](../filesystem-context/)** -- Using the file system for context: scratch pads, plan persistence, and sub-agent file workspaces

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
