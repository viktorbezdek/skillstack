# Context Degradation

> **v1.0.4** | Context Engineering | 5 iterations

Patterns for recognizing and mitigating context failures in LLM agents. Covers lost-in-middle, context poisoning, distraction, confusion, clash, and empirical degradation thresholds by model.

## What Problem Does This Solve

Agent and LLM failures are frequently misdiagnosed as model capability problems when the actual cause is context degradation — a predictable set of failure modes that emerge as context grows. Information buried in the middle of a long conversation gets ignored (lost-in-middle), an early hallucination compounds through repeated reference (context poisoning), or irrelevant retrieved documents drown out the relevant ones (context distraction). This skill names these patterns precisely, provides empirical thresholds by model, and maps each pattern to mitigation strategies.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "My agent gives wrong answers after long conversations" | Model-specific degradation onset and severe degradation thresholds (e.g. Claude Sonnet 4.5 degrades at ~80K tokens) |
| "The agent ignores information I put in the middle of the prompt" | Lost-in-middle pattern: U-shaped attention curve, 10-40% recall loss, and placement strategies to counter it |
| "An early error is polluting all my agent's subsequent reasoning" | Context poisoning detection: compounding feedback loop symptoms, entry pathways, and recovery techniques |
| "My agent uses the wrong tool or addresses the wrong task" | Context confusion and context clash patterns with architectural isolation solutions |
| "Adding more context seems to make responses worse" | Non-linear degradation curves, cost implications, and the cognitive load limits that make larger contexts counterproductive |
| "Which model handles long contexts best for my use case?" | Comparative model behavior table: GPT-5.2, Claude Opus/Sonnet 4.5, Gemini 3 Pro/Flash with failure mode characteristics |

## When NOT to Use This Skill

- learning context basics or theory -- use [context-fundamentals](../context-fundamentals/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install context-degradation@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the context-degradation skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `context-degradation`
- `lost-in-middle`
- `context-poisoning`
- `attention-patterns`

## What's Inside

- **When to Activate** -- Conditions signaling context degradation: unexpected agent performance drops, incorrect outputs in long conversations, and design considerations for large-context systems.
- **Core Concepts** -- Five named degradation patterns (lost-in-middle, poisoning, distraction, confusion, clash) with brief definitions and the four mitigation buckets (write, select, compress, isolate).
- **Detailed Topics** -- Deep coverage of each pattern's mechanics, empirical evidence, detection symptoms, and recovery/mitigation strategies, plus RULER benchmark data and model-specific thresholds.
- **Practical Guidance** -- The four-bucket approach (Write, Select, Compress, Isolate) with specific architectural patterns for each strategy.
- **Examples** -- Concrete context growth progression showing when degradation begins, and a structured placement example for lost-in-middle mitigation.
- **Guidelines** -- Eight prioritized rules for designing systems that degrade gracefully rather than catastrophically.
- **Integration** -- How this skill connects to context-optimization (mitigation techniques), multi-agent-patterns (isolation), and evaluation (detection and measurement).
- **References** -- Internal references to degradation pattern details and external research on attention mechanisms and the lost-in-middle phenomenon.

## Version History

- `1.0.4` fix(context-engineering): optimize descriptions with cross-references and NOT clauses (7881054)
- `1.0.3` fix(context-degradation): add standard keywords and expand README to full format (39ba542)
- `1.0.2` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.1` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.0` Initial release (697ea68)

## Related Skills

- **[Context Compression](../context-compression/)** -- Production strategies for compressing LLM context windows. Anchored iterative summarization, opaque compression, tokens-...
- **[Context Fundamentals](../context-fundamentals/)** -- Foundational understanding of context engineering for AI agent systems. Covers context anatomy, attention mechanics, pro...
- **[Context Optimization](../context-optimization/)** -- Techniques for extending effective context capacity through compaction, observation masking, KV-cache optimization, and ...
- **[Filesystem Context](../filesystem-context/)** -- Filesystem-based context engineering patterns for LLM agents. Scratch pads, plan persistence, sub-agent communication, d...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
