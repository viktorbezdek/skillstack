# Context Compression

> **v1.0.4** | Context Engineering | 5 iterations

Production strategies for compressing LLM context windows. Anchored iterative summarization, opaque compression, tokens-per-task optimization, and probe-based evaluation.

## What Problem Does This Solve

When coding agents run long sessions, naive compression destroys the information they need most — file paths, error messages, and decisions made earlier — forcing expensive re-exploration that costs more tokens than the compression saved. The real optimization target is not tokens-per-request but tokens-per-task: the total cost from start to completion, including re-fetching. This skill provides structured compression strategies that preserve artifact trails and task context across compression cycles.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "My agent keeps forgetting which files it modified" | Anchored iterative summarization with explicit file-tracking sections that survive repeated compression |
| "How do I compress context without losing critical details?" | Three production-ready compression methods with quality tradeoffs: anchored iterative, opaque, and regenerative |
| "When should I trigger context compaction?" | Compression trigger strategies — fixed threshold, sliding window, importance-based, and task-boundary — with tradeoffs |
| "How do I know if my compression is working well?" | Probe-based evaluation framework with four probe types (recall, artifact, continuation, decision) that measures functional quality |
| "My agent session is approaching the context limit at 70%+" | Three-phase compression workflow for large codebases: research, planning, and implementation phases |
| "I'm seeing 99%+ compression ratios but quality seems wrong" | Six-dimension evaluation scoring (accuracy, context awareness, artifact trail, completeness, continuity, instruction following) with benchmarks |

## When NOT to Use This Skill

- diagnosing context failures or degradation patterns -- use [context-degradation](../context-degradation/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install context-compression@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the context-compression skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `context-compression`
- `summarization`
- `compaction`
- `token-optimization`

## What's Inside

- **When to Activate** -- Conditions that signal compression is needed: session length, codebase size, agents forgetting file modifications.
- **Core Concepts** -- Three compression approaches (anchored iterative, opaque, regenerative) with compression ratios and quality score tradeoffs.
- **Detailed Topics** -- Deep coverage of tokens-per-task optimization, the artifact trail problem, structured summary sections, trigger strategies, probe-based evaluation, and six evaluation dimensions.
- **Session Intent** -- Template section for capturing the user's goal at the start of each compression summary.
- **Files Modified** -- Template section for tracking which files were created, changed, or read-only during the session.
- **Decisions Made** -- Template section for preserving architectural and implementation decisions across compression cycles.
- **Current State** -- Template section for capturing test status, progress markers, and in-flight work at compression time.
- **Next Steps** -- Template section for preserving the planned continuation so agents can resume without re-exploration.

## Version History

- `1.0.4` fix(context-engineering): optimize descriptions with cross-references and NOT clauses (7881054)
- `1.0.3` fix(context-compression): add standard keywords and expand README to full format (4005434)
- `1.0.2` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.1` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.0` Initial release (697ea68)

## Related Skills

- **[Context Degradation](../context-degradation/)** -- Patterns for recognizing and mitigating context failures in LLM agents. Covers lost-in-middle, context poisoning, distra...
- **[Context Fundamentals](../context-fundamentals/)** -- Foundational understanding of context engineering for AI agent systems. Covers context anatomy, attention mechanics, pro...
- **[Context Optimization](../context-optimization/)** -- Techniques for extending effective context capacity through compaction, observation masking, KV-cache optimization, and ...
- **[Filesystem Context](../filesystem-context/)** -- Filesystem-based context engineering patterns for LLM agents. Scratch pads, plan persistence, sub-agent communication, d...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
