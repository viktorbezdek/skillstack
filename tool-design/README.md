# Tool Design

> **v1.0.4** | Agent Architecture | 5 iterations

Design tools optimized for LLM agents rather than human developers. Consolidation principle, architectural reduction, tool description engineering, MCP naming, and the file system agent pattern.

## What Problem Does This Solve

When agent systems underperform, the culprit is often the tool interface, not the model. Overlapping tool descriptions cause agents to pick the wrong tool; vague parameter names force agents to guess; missing error context leaves agents unable to recover; and growing tool collections consume context budget with redundant descriptions. This skill applies the Consolidation Principle and Architectural Reduction to shrink tool sets, sharpen descriptions, and design error messages that give agents enough information to self-correct — producing measurable gains in task completion without changing the underlying model.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "My agent keeps calling the wrong tool when there are multiple options" | The Consolidation Principle — merging overlapping tools into single comprehensive tools with unambiguous scopes |
| "How should I write tool descriptions so the model uses them correctly?" | Description structure covering what the tool does, when to use it, parameter constraints, return format, and error conditions |
| "I have 30 tools and the agent seems confused about which to pick" | Namespacing strategy, the 10-20 tool guideline, and hierarchy patterns with umbrella routing tools |
| "My tool errors give the agent no way to fix its mistake" | Error message design patterns that include retry guidance, corrected format examples, and actionable recovery steps |
| "Should I use MCP tools and how do I reference them correctly?" | MCP fully-qualified naming requirements (`ServerName:tool_name`) and why unqualified names fail in multi-server setups |
| "Is it better to give the agent file system access or build custom tools?" | The File System Agent Pattern and Architectural Reduction case study showing when primitive tools outperform specialized wrappers |

## When NOT to Use This Skill

- building MCP servers or MCP protocol implementation -- use [mcp-server](../mcp-server/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/tool-design
```

## How to Use

**Direct invocation:**

```
Use the tool-design skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `tool-design`
- `mcp`
- `consolidation-principle`
- `architectural-reduction`

## What's Inside

- **When to Activate** -- Specific conditions for using this skill: new tool creation, debugging tool failures, optimizing existing tool sets, or standardizing tool conventions.
- **Core Concepts** -- The foundational ideas: tools as contracts between deterministic systems and non-deterministic agents, the Consolidation Principle, and tool descriptions as prompt engineering.
- **Detailed Topics** -- Deep dives into the tool-agent interface, namespacing strategies, Architectural Reduction (including the File System Agent Pattern), description engineering, response format optimization, and error message design.
- **Practical Guidance** -- Anti-patterns to avoid (vague descriptions, cryptic parameters, missing error handling) and a 5-step tool selection framework.
- **Examples** -- Annotated well-designed vs. poorly-designed tool side-by-side, with failure mode analysis for the bad example.
- **Guidelines** -- 12 actionable rules covering descriptions, consolidation, token efficiency, naming conventions, tool count limits, and iterating on failure data.
- **Integration** -- How this skill connects to context-fundamentals, multi-agent-patterns, and evaluation.
- **References** -- Links to the Best Practices reference and the Architectural Reduction case study with production evidence.

## Version History

- `1.0.4` fix(agent-architecture): add NOT clauses to disambiguate 7 agent plugins (f25da8a)
- `1.0.3` fix(tool-design): add standard keywords and expand README to full format (4502e00)
- `1.0.2` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.1` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.0` Initial release (697ea68)

## Related Skills

- **[Agent Evaluation](../agent-evaluation/)** -- Comprehensive evaluation framework for LLM agent systems. Multi-dimensional rubrics, LLM-as-judge with bias mitigation, ...
- **[Agent Project Development](../agent-project-development/)** -- Methodology for LLM-powered project development. Task-model fit analysis, pipeline architecture (acquire-prepare-process...
- **[Bdi Mental States](../bdi-mental-states/)** -- Belief-Desire-Intention cognitive architecture for LLM agents. Formal BDI ontology, T2B2T paradigm, RDF integration, SPA...
- **[Hosted Agents](../hosted-agents/)** -- Infrastructure patterns for hosted background agents. Sandbox environments, image registry pattern, self-spawning agents...
- **[Memory Systems](../memory-systems/)** -- Production memory architectures for LLM agents. Compares Mem0, Zep/Graphiti, Letta, Cognee, LangMem with benchmarks. Cov...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
