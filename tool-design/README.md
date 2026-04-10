# Tool Design

> **v1.0.4** | Agent Architecture | 5 iterations

Design tools optimized for LLM agents rather than human developers. Consolidation principle, architectural reduction, tool description engineering, MCP naming, and the file system agent pattern.

## What Problem Does This Solve

Tools are the primary mechanism through which agents interact with the world. They define the contract between deterministic systems and non-deterministic agents. Unlike traditional software APIs designed for developers, tool APIs must be designed for language models that reason about intent, infer parameter values, and generate calls from natural language requests. Poor tool design creates failure modes that no amount of prompt engineering can fix. Effective tool design follows specific principles that account for how agents perceive and use tools.

## When to Use This Skill

This skill should be used when the user asks to "design agent tools", "create tool descriptions", "reduce tool complexity", "implement MCP tools", or mentions tool consolidation, architectural reduction, tool naming conventions, or agent-tool interfaces.

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

- **When to Activate**
- **Core Concepts**
- **Detailed Topics**
- **Practical Guidance**
- **Examples**
- **Guidelines**
- **Integration**
- **References**

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
