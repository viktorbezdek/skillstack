# Filesystem-Based Context Engineering

> Filesystem-based context engineering patterns for LLM agents. Scratch pads, plan persistence, sub-agent communication, dynamic skill loading, terminal persistence, and self-modification patterns.

## Overview

The filesystem provides a single interface through which agents can flexibly store, retrieve, and update an effectively unlimited amount of context. This skill addresses the fundamental constraint that context windows are limited while tasks often require more information than fits in a single window. The core insight is that files enable dynamic context discovery: agents pull relevant context on demand rather than carrying everything in the context window.

This skill covers six practical patterns for filesystem-based context engineering. Scratch pads offload large tool outputs to files, returning compact references instead. Plan persistence writes task plans to structured files so agents can re-read them across turns. Sub-agent communication uses shared file workspaces instead of message passing to avoid the "telephone game." Dynamic skill loading stores instructions as files and loads them only when relevant. Terminal persistence syncs command output to searchable files. Self-modification lets agents write learned preferences to their own instruction files.

Within the SkillStack collection, Filesystem Context implements the "Write" strategy from Context Degradation's four-bucket approach and provides the concrete patterns for the observation masking concept in Context Optimization. It connects to Memory Systems (filesystem-as-memory is a simple memory layer), Multi-Agent Patterns (sub-agent file workspaces enable isolation), and Tool Design (tools should return file references for large outputs).

## What's Included

### Skill

- `skills/filesystem-context/SKILL.md` -- Core patterns covering scratch pads, plan persistence, sub-agent file communication, dynamic skill loading, terminal persistence, self-modification, and filesystem search techniques

### References

- **implementation-patterns.md** -- Detailed implementation patterns with code examples for each filesystem context pattern

## Key Features

- **Scratch pad pattern** writing large tool outputs (8000+ tokens) to files and returning compact references (~100 tokens), with targeted retrieval via grep and line-range reads
- **Plan persistence** storing structured task plans in YAML files that agents re-read at the start of each turn to maintain long-horizon task tracking
- **Sub-agent file communication** where agents write findings directly to shared workspace directories, bypassing message-passing degradation
- **Dynamic skill loading** keeping only skill names and descriptions in static context, loading full SKILL.md content on demand when tasks require it
- **Terminal and log persistence** syncing command output to searchable files that agents query with targeted grep instead of loading entire histories
- **Self-modification pattern** where agents write learned user preferences to their own instruction files for automatic loading in subsequent sessions
- **Static vs dynamic context trade-off** analysis with guidance on when pre-loading beats just-in-time loading
- **Filesystem search techniques** combining ls, glob, grep, and read_file with line ranges for powerful context discovery that often outperforms semantic search for technical content

## Usage Examples

Offload large tool outputs to files:
```
My agent's web search tool returns 10K tokens of results that bloat the context. Help me implement the scratch pad pattern to write results to files and return compact summaries with file references.
```

Set up plan persistence for a multi-step task:
```
I'm building an agent that refactors large codebases over many conversation turns. Implement plan persistence so the agent writes its refactoring plan to a YAML file and re-reads it each turn to stay on track.
```

Design sub-agent communication via filesystem:
```
I have a research agent and a code agent that need to share findings. Instead of passing messages through a supervisor, set up file-based communication where each agent writes to its own workspace directory.
```

Implement dynamic skill loading:
```
My agent has 20 skills but only 2-3 are relevant per task. Help me implement dynamic loading where the system prompt contains only skill summaries and the agent loads full skill files when needed.
```

## Quick Start

1. **Identify context bloat sources**: Measure which tool outputs exceed 2000 tokens and are candidates for file offloading.
2. **Implement scratch pads**: Write large outputs to `scratch/` files and return `[Output written to {path}. Summary: {key_finding}]` instead.
3. **Add plan persistence**: For multi-turn tasks, write plans to `scratch/current_plan.yaml` and have the agent re-read at the start of each turn.
4. **Set up file organization**: Structure as `scratch/` (temporary), `memory/` (persistent), `skills/` (loadable), `agents/` (sub-agent workspaces).
5. **Measure savings**: Track token usage before and after filesystem patterns to validate they reduce context consumption.

## Related Skills

- **context-optimization** -- Filesystem offloading is a concrete implementation of observation masking
- **context-compression** -- File references enable lossless "compression" by moving content out of context
- **memory-systems** -- Filesystem-as-memory is the simplest persistent memory layer
- **multi-agent-patterns** -- Sub-agent file workspaces enable context isolation without message passing
- **tool-design** -- Tools should return file references for large outputs rather than dumping content into context

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install filesystem-context@skillstack` — 46 production-grade plugins for Claude Code.
