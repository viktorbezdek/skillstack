# Filesystem Context

> **v1.0.4** | Context Engineering | 5 iterations

Filesystem-based context engineering patterns for LLM agents. Scratch pads, plan persistence, sub-agent communication, dynamic skill loading, terminal persistence, and self-modification patterns.

## What Problem Does This Solve

LLM agents operating on long-horizon tasks accumulate tool outputs, plans, and intermediate results in their context window until it fills up and performance degrades. The usual workarounds -- summarisation and truncation -- lose information. This skill treats the filesystem as an unlimited external memory layer: large outputs are written to files and referenced by pointer, plans are persisted and re-read on each turn, and sub-agents share state through a shared workspace rather than message chains. The core insight is that files enable dynamic context discovery -- agents pull relevant context on demand rather than carrying everything in the window.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install filesystem-context@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## What's Inside

Single-skill plugin with one SKILL.md and one reference file:

| Component | What It Provides |
|---|---|
| **Scratch Pad Pattern** | Write large tool outputs (above a 2000-token threshold) to files, return a summary + file reference, then use grep or targeted reads for retrieval |
| **Plan Persistence** | YAML schema for objective, steps, and status that the agent re-reads each turn -- "manipulating attention through recitation" |
| **Sub-Agent Workspaces** | Per-agent file directories so a coordinator can read results directly instead of routing through message chains |
| **Dynamic Skill Loading** | Store skills as files, include only names and descriptions statically, load full content on demand -- scales to dozens of skills without context bloat |
| **Terminal Log Persistence** | Sync stdout to dated files so agents can grep for error patterns rather than loading full build logs |
| **Self-Modification** | Agents write learned preferences and patterns to files, evolving their own behavior across sessions |
| **`implementation-patterns.md`** | Reference file with worked examples showing before/after token counts, recommended directory structure, and ten implementation rules |

## How to Use

**Direct invocation:**

```
Use the filesystem-context skill to design a scratch pad system for our agent's tool outputs
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

`filesystem` · `context-management` · `scratch-pad` · `dynamic-loading`

## Usage Scenarios

**1. Reducing token bloat from web search results.** Your agent calls a web search tool that returns 10,000+ tokens of raw content per query. Use the scratch pad pattern to write the full results to a file, return a 200-token summary to the context, and then use grep to extract only the relevant paragraphs when the agent needs specific details.

**2. Keeping a long-running refactoring task on track.** A multi-step refactoring task takes 30+ turns and the agent keeps losing track of which files have been updated. Use plan persistence to write a YAML plan file with each step's status, re-reading it at the start of every turn so the agent always knows exactly where it left off.

**3. Coordinating parallel sub-agents.** You have three sub-agents working on different parts of a feature (frontend, backend, database migration). Instead of passing results through message chains, each agent writes its output to a designated directory and the coordinator reads the files directly -- eliminating information loss from summarisation.

**4. Scaling from 5 skills to 50 without degrading performance.** Your agent has accumulated 50 skills but loading all of them into the system prompt wastes tokens and confuses the model. Use dynamic skill loading to include only a one-line index of each skill name and description, then load the full SKILL.md on demand when a query matches.

**5. Debugging a CI failure from agent context.** A build that ran for 8 minutes produced 50,000 lines of output. Instead of dumping that into context, use terminal persistence to write the output to a dated log file and have the agent grep for "ERROR", "FAILED", or stack trace patterns to extract only the relevant lines.

## When to Use / When NOT to Use

**Use when:** Tool outputs are bloating the context window, agents need to persist state across long trajectories, sub-agents must share information, you need to scale the number of skills without degrading performance, or terminal output needs to be accessible without overwhelming the context.

**Do NOT use for:**
- **In-context optimization** (KV-cache, observation masking) -- use [context-optimization](../context-optimization/)
- **Summarisation or compression techniques** -- use [context-compression](../context-compression/)
- **Understanding context theory or fundamentals** -- use [context-fundamentals](../context-fundamentals/)

## Related Plugins in SkillStack

- **[Context Compression](../context-compression/)** -- Anchored iterative summarization, opaque compression, tokens-per-task optimization
- **[Context Degradation](../context-degradation/)** -- Recognizing and mitigating context failures: lost-in-middle, poisoning, distraction
- **[Context Fundamentals](../context-fundamentals/)** -- Foundational theory of context engineering for AI agent systems
- **[Context Optimization](../context-optimization/)** -- Extending effective context capacity through compaction, KV-cache, and retrieval strategies

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
