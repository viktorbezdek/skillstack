# Tool Design for Agents

> Design tools optimized for LLM agents rather than human developers. Consolidation principle, architectural reduction, tool description engineering, MCP naming, and the file system agent pattern.

## Overview

Tools are the primary mechanism through which agents interact with the world, defining the contract between deterministic systems and non-deterministic language models. Unlike traditional software APIs designed for developers who read documentation, tool APIs must be designed for models that reason about intent, infer parameter values, and generate calls from natural language. Poor tool design creates failure modes that no amount of prompt engineering can fix. This skill provides the principles and patterns for building tools that agents use correctly and efficiently.

The skill is anchored by two key principles. The consolidation principle states that if a human engineer cannot definitively say which tool should be used in a given situation, an agent cannot be expected to do better -- leading to a preference for single comprehensive tools over many narrow ones. Architectural reduction takes this further, with production evidence showing that removing most specialized tools in favor of primitives (bash + SQL) can improve success rates from 80% to 100%. Tool descriptions are not just documentation but prompt engineering that shapes agent behavior, and every ambiguity becomes a potential failure mode.

Within the SkillStack collection, Tool Design connects to Context Fundamentals (how tool definitions interact with context), Multi-Agent Patterns (specialized tools per agent), and Agent Evaluation (evaluating tool effectiveness). It provides the tool architecture guidance referenced by Agent Project Development and Hosted Agents.

## What's Included

### Skill

- `skills/tool-design/SKILL.md` -- Core design principles covering tool-agent interface, consolidation principle, architectural reduction, description engineering, response format optimization, error message design, MCP naming, and agent-powered tool optimization

### References

- **best_practices.md** -- Detailed tool design guidelines with patterns and anti-patterns
- **architectural_reduction.md** -- Production evidence for tool minimalism including the Vercel d0 case study (17 tools to 2, 80% to 100% success rate)

## Key Features

- **Consolidation principle**: if a human cannot determine which tool to use, neither can an agent -- prefer single comprehensive tools over multiple narrow overlapping ones
- **Architectural reduction** backed by production evidence: Vercel d0 achieved 100% success (up from 80%) by reducing 17 tools to 2 primitives (bash + SQL)
- **File system agent pattern** using standard Unix utilities (grep, cat, find, ls) instead of custom exploration tools, leveraging models' deep understanding of filesystem operations
- **Tool description engineering** answering four questions: what does it do, when should it be used, what inputs does it accept, what does it return
- **Response format optimization** with concise/detailed modes giving agents control over verbosity and token consumption
- **Error message design** for agent recovery with actionable guidance: what went wrong, how to correct it, retry instructions for transient errors
- **MCP naming conventions** requiring fully qualified `ServerName:tool_name` format to avoid "tool not found" errors across multiple servers
- **Agent-powered tool optimization**: using agents to analyze tool failures and improve descriptions, achieving 40% reduction in task completion time

## Usage Examples

Design tools for a new agent system:
```
I'm building an agent with access to a database, file system, and web APIs. Help me design the tool set following the consolidation principle. I currently have 25 tools and suspect many overlap.
```

Apply architectural reduction:
```
Our agent has 15 specialized tools but performance is inconsistent. Help me evaluate whether reducing to a few primitives (bash execution, file access) would improve results, following the Vercel d0 pattern.
```

Improve tool descriptions for better agent usage:
```
My agent keeps calling the wrong tool or passing incorrect parameters. Review my tool descriptions and rewrite them following the four-question pattern: what, when, inputs, returns.
```

Design error messages for agent recovery:
```
Our tools return generic error messages and the agent can't recover from failures. Help me redesign error responses to be actionable: include what went wrong, correction guidance, and retry instructions.
```

## Quick Start

1. **Audit your tool set**: List all tools and check for overlapping functionality. Apply the consolidation test: can a human definitively choose between overlapping tools?
2. **Write descriptions that answer four questions**: What does this tool do? When should it be used? What inputs does it accept? What does it return?
3. **Implement response format options**: Add concise/detailed modes so agents can choose appropriate verbosity for each situation.
4. **Design actionable errors**: Every error message should tell the agent what went wrong and how to fix it.
5. **Consider reduction**: Before adding more tools, ask whether the agent could accomplish the same thing with existing primitives (file access, command execution).

## Related Skills

- **context-fundamentals** -- How tool definitions consume context and steer agent behavior
- **multi-agent-patterns** -- Designing specialized tool sets per agent in multi-agent systems
- **agent-evaluation** -- Evaluating tool effectiveness through agent interaction testing
- **agent-project-development** -- Architectural reduction decisions within project methodology
- **hosted-agents** -- Building tools for hosted environments and agent spawning

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install tool-design@skillstack` — 46 production-grade plugins for Claude Code.
