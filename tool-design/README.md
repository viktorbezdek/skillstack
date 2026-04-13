# Tool Design

> **v1.0.4** | Agent Architecture | 5 iterations

Design tools optimized for LLM agents rather than human developers. Consolidation principle, architectural reduction, tool description engineering, MCP naming, and the file system agent pattern.

## What Problem Does This Solve

When agent systems underperform, the culprit is often the tool interface, not the model. Overlapping tool descriptions cause agents to pick the wrong tool. Vague parameter names force agents to guess. Missing error context leaves agents unable to recover. Growing tool collections consume context budget with redundant descriptions. Most teams approach tool design the way they approach human-facing APIs -- clear enough for a developer who can read docs and experiment. But agents infer contracts from descriptions and generate calls from natural language, so every ambiguity becomes a failure mode that no amount of prompt engineering can fix.

This skill applies the Consolidation Principle and Architectural Reduction to shrink tool sets, sharpen descriptions, and design error messages that give agents enough information to self-correct -- producing measurable gains in task completion without changing the underlying model.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install tool-design@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

**Direct invocation:**

```
Use the tool-design skill to review my agent's tool set
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `tool-design`
- `mcp`
- `consolidation-principle`
- `architectural-reduction`

## What's Inside

This is a **single-skill plugin** with two reference documents and two eval suites.

| Component | Path | Purpose |
|---|---|---|
| Skill | `skills/tool-design/SKILL.md` | Core methodology: Consolidation Principle, Architectural Reduction, description engineering, error message design, MCP naming, tool collection sizing |
| Reference | `references/best_practices.md` | Extended guidelines: description structure, naming conventions, error message schemas, response format optimization, anti-pattern catalog, design checklist |
| Reference | `references/architectural_reduction.md` | Production case study: text-to-SQL agent rebuilt from 17 specialized tools to 2 primitive tools -- 3.5x faster, 37% fewer tokens, 100% success rate |
| Evals | `evals/trigger-evals.json` | 13 trigger scenarios including 3 NOT-for boundary tests (MCP servers, multi-agent, memory) |
| Evals | `evals/evals.json` | 3 output quality scenarios for design walkthroughs, reviews, and greenfield setup |

## Usage Scenarios

**1. "My agent keeps calling the wrong tool when there are multiple options"**
The skill teaches the Consolidation Principle: if a human engineer cannot definitively say which tool to use, the agent cannot either. It walks through merging overlapping tools into single comprehensive tools with unambiguous scopes, reducing tool count from 30+ to the recommended 10-20 range.

**2. "We rebuilt our agent with fewer tools and it actually got better"**
The Architectural Reduction case study documents a production text-to-SQL agent that went from 17 specialized tools (GetEntityJoins, LoadCatalog, SearchSchema, etc.) to 2 primitive tools (ExecuteCommand, ExecuteSQL). Results: average execution time dropped from 275s to 77s, success rate went from 80% to 100%, and token usage dropped 37%. The skill explains when this pattern applies and when it does not.

**3. "How should I write tool descriptions so the model uses them correctly?"**
The description engineering section provides a four-question framework: what does the tool do, when should it be used, what inputs does it accept, and what does it return. Includes side-by-side examples of well-designed vs poorly-designed tools with failure mode analysis for the bad example.

**4. "My tool errors give the agent no way to fix its mistake"**
The error message design section covers structured error responses with actionable recovery guidance -- including retry timing for rate limits, corrected format examples for validation errors, and alternative suggestions for not-found errors. Error messages serve two audiences (developers and agents), and the skill prioritizes agent recovery.

**5. "Should I give the agent file system access or build custom tools?"**
The File System Agent Pattern shows when primitive tools (bash + SQL) outperform specialized wrappers. The skill provides prerequisites for success (high documentation quality, sufficient model capability, safe sandbox) and explicit failure conditions (messy data, specialized domain knowledge, safety constraints).

## When to Use / When NOT to Use

**Use when:**
- Creating new tools for an agent system
- Debugging tool-related failures or misuse (agent picks wrong tool, generates bad parameters)
- Optimizing an existing tool set for better agent performance
- Standardizing tool conventions across a codebase
- Evaluating whether to build custom tools or provide primitive capabilities

**Do NOT use when:**
- Building MCP servers or implementing the MCP protocol -- use [mcp-server](../mcp-server/) instead
- Designing multi-agent coordination or agent handoffs -- use [multi-agent-patterns](../multi-agent-patterns/) instead
- Implementing agent memory or persistence -- use [memory-systems](../memory-systems/) instead

## Related Plugins in SkillStack

- **[Agent Evaluation](../agent-evaluation/)** -- Evaluate agent systems including tool usage effectiveness
- **[Agent Project Development](../agent-project-development/)** -- End-to-end agent project methodology including tool selection
- **[Multi-Agent Patterns](../multi-agent-patterns/)** -- Coordination patterns where each agent has its own tool set
- **[MCP Server](../mcp-server/)** -- Build MCP servers that expose the tools this skill teaches you to design
- **[Memory Systems](../memory-systems/)** -- Agent memory architectures that complement well-designed tool interfaces

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
