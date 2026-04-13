# Filesystem Context

> **v1.0.4** | Context Engineering | 5 iterations

> Use the filesystem as unlimited external memory for LLM agents -- scratch pads, plan persistence, sub-agent workspaces, dynamic skill loading, and self-modification patterns.

## The Problem

LLM agents operate within a fixed context window. Every tool output, every plan step, every intermediate result consumes tokens and stays in the window for the rest of the conversation. A single web search returning 10,000 tokens of raw content occupies that space permanently, even if only 50 tokens were relevant. Over a multi-step task, the context fills with stale tool outputs, completed plan steps, and intermediary data that degrades attention to the information that actually matters now.

The consequences are predictable and systematic. Long-horizon tasks lose coherence because the plan that was clear 20 turns ago has been pushed out of effective attention by accumulated tool output. Multi-agent systems suffer "telephone effect" where findings degrade through summarization at each message-passing hop. Agents with many skills carry all their instructions in the system prompt, wasting tokens on guidance that is irrelevant to 90% of tasks. And when context windows compress or summarize, details that seemed unimportant at compression time turn out to be critical three steps later -- but they are gone.

The root issue is that most agent architectures treat the context window as the only working memory. Everything must fit, and everything competes for space. This is like trying to do knowledge work using only your short-term memory -- no notes, no files, no reference materials on your desk. It works for simple tasks. It breaks for anything with more than a few steps.

## The Solution

This plugin teaches Claude how to use the filesystem as an unlimited external memory layer for agent operations. Instead of accumulating large outputs in the context window, agents write them to files and retain only summaries and references. Plans are persisted as structured YAML so they survive context compression. Sub-agents communicate through shared file workspaces instead of message chains, preserving fidelity. Skills and instructions are loaded dynamically from files instead of being stuffed into static context.

The skill provides six concrete patterns with implementation code: filesystem as scratch pad (offload large tool outputs), plan persistence (survive context compression), sub-agent communication via filesystem (bypass telephone effect), dynamic skill loading (reduce static context bloat), terminal and log persistence (searchable output files), and learning through self-modification (agents that improve their own instructions). Each pattern includes the problem it solves, the implementation approach, and practical guidance on when to use it versus when the overhead is not justified.

The plugin ships one SKILL.md with all six patterns, one reference file with detailed implementation patterns, 13 trigger eval cases, and 3 output quality eval cases.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Web search returns 10K tokens that stay in context forever, even if only 50 tokens were relevant | Large outputs written to scratch files; only a summary and file reference enter the context window |
| Plans drift or disappear after context compression because they live only in message history | Plans persisted as structured YAML files that agents re-read at the start of each turn |
| Multi-agent findings degrade through message-passing summarization (telephone effect) | Sub-agents write findings to shared workspace files; coordinator reads originals directly |
| All skill instructions stuffed into system prompt, wasting tokens on irrelevant guidance | Skills stored as files, loaded dynamically when the task requires them |
| Terminal output from long processes must be copy-pasted or carried in context | Terminal sessions persisted as searchable files; agents grep for relevant sections |
| Agent behavior is static between sessions -- no learning from user preferences | Agents write learned preferences to instruction files that subsequent sessions load |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install filesystem-context@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when your prompts mention offloading context to files, scratch pads, plan persistence, filesystem-based agent memory, tool output persistence, or dynamic context loading.

## Quick Start

1. Install the plugin using the commands above
2. Open a Claude Code session
3. Type: `How should I implement a scratch pad pattern for my agent that makes web searches? The search results are flooding the context.`
4. Claude provides the scratch-pad implementation pattern: write outputs to files, return summaries with file references, use grep for targeted retrieval
5. Next, try: `Design a sub-agent file workspace layout for a research agent that spawns 3 parallel sub-agents`

---

## System Overview

```
User prompt (context engineering question / agent architecture design)
        |
        v
+---------------------+     +-------------------------------+
|  filesystem-context  |---->| Pattern selection              |
|  skill (SKILL.md)    |     | (match query to 1-6 patterns) |
+---------------------+     +-------------------------------+
        |                              |
        v                              v
  Core concepts:              6 implementation patterns:
  - Static vs dynamic         1. Scratch Pad (offload outputs)
  - Write once, read          2. Plan Persistence (survive compression)
    selectively               3. Sub-Agent Communication (bypass telephone)
  - Dynamic discovery         4. Dynamic Skill Loading (reduce bloat)
        |                     5. Terminal/Log Persistence (searchable)
        v                     6. Self-Modification (agent learning)
  Practical guidance:                  |
  - When to use filesystem             v
  - File organization         +----------------------------+
  - Token accounting           | Implementation Patterns    |
  - Search techniques          | reference (detailed code)  |
                               +----------------------------+
```

Single-skill plugin with one reference file for detailed implementation patterns. No hooks, no MCP servers, no external dependencies.

## What's Inside

| Component | Type | What It Provides |
|---|---|---|
| **filesystem-context** | Skill | 6 filesystem patterns, static vs dynamic context theory, practical guidance, file organization |
| **implementation-patterns.md** | Reference | Detailed code implementations for each pattern |
| **trigger-evals** | Eval | 13 trigger eval cases (8 positive, 5 negative) |
| **output-evals** | Eval | 3 output quality eval cases |

### Component Spotlight

#### filesystem-context (skill)

**What it does:** Activates when you ask about using the filesystem for agent context, offloading tool outputs, persisting plans, designing agent workspaces, or implementing dynamic skill loading. Provides six concrete implementation patterns with code examples and practical guidance on when each pattern is worth the overhead.

**Input -> Output:** You describe a context engineering challenge (bloated context, lost plans, agent coordination) -> The skill provides the matching filesystem pattern(s) with implementation code, file organization layout, and token accounting guidance.

**When to use:**
- Tool outputs are bloating the context window (search results, API responses, database queries)
- Long-horizon tasks lose coherence because plans fall out of attention
- Multi-agent systems need to share state without message-passing degradation
- System prompt is overloaded with instructions for skills that are rarely needed
- Terminal or build output needs to be accessible to agents without copy-pasting
- Building agents that learn and update their own instructions between sessions

**When NOT to use:**
- Tasks complete in a single turn with no context pressure -> filesystem overhead not justified
- In-context optimization (KV-cache tuning, observation masking) -> use [context-optimization](../context-optimization/)
- Summarization and compression techniques -> use [context-compression](../context-compression/)
- Understanding context theory and fundamentals -> use [context-fundamentals](../context-fundamentals/)

**Try these prompts:**

```
How should I implement a scratch pad for my agent? Web search results are flooding the context window with 10K+ tokens per search.
```

```
Design a file workspace layout for a coordinator agent that manages 4 parallel research sub-agents
```

```
My agent keeps losing track of its plan after context compression. How do I persist plans so they survive summarization?
```

```
I have 15 skills in my system prompt but only 2-3 are relevant per task. How do I load them dynamically from files instead?
```

```
Build a self-modification pattern where my agent remembers user preferences between sessions by writing to an instruction file
```

**Key references:**

| Reference | Topic |
|---|---|
| `implementation-patterns.md` | Detailed code implementations for all 6 filesystem patterns |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Help with context management" | "How do I offload large tool outputs to files instead of keeping them in the agent's context window?" |
| "My agent forgets things" | "My agent loses track of its multi-step plan after context compression -- how do I persist the plan as a file?" |
| "Design a multi-agent system" | "Design a file workspace layout where 3 sub-agents write findings and a coordinator reads them without message passing" |
| "Reduce token usage" | "I have 15 skill files in my system prompt consuming 8K tokens. How do I switch to dynamic loading?" |
| "Make my agent smarter" | "How should my agent write learned user preferences to an instruction file so subsequent sessions can load them?" |

### Structured Prompt Templates

**For scratch pad implementation:**
```
My agent calls [tool name] which returns [approximate token count] tokens per call. Over a [number]-step task, this accumulates to [total tokens]. How should I implement a scratch pad pattern to offload these outputs? The agent needs to [what it does with the output later].
```

**For sub-agent workspace design:**
```
Design a file workspace for [number] sub-agents coordinated by a [coordinator type]. Sub-agents perform [task type] and need to share [data types]. The coordinator needs to [synthesize / prioritize / route] findings.
```

**For dynamic skill loading:**
```
I have [number] skills totaling [token count] in my system prompt. Most tasks use [number] skills. How do I restructure for dynamic loading? Skills are currently in [current format].
```

### Prompt Anti-Patterns

- **Treating filesystem context as a silver bullet:** "Move everything to files" -- some context should stay in the window (critical rules, current task state). The skill helps you decide what to offload and what to keep.
- **Asking about in-context optimization:** "How do I optimize my KV cache?" -- this plugin is about filesystem-based context, not in-context optimization techniques. Use [context-optimization](../context-optimization/) instead.
- **No specifics about the context pressure:** "My context is too large" -- describe what is filling it (tool outputs? skill instructions? message history?) so the skill can match the right pattern.

## Real-World Walkthrough

You are building a research agent that takes a topic, searches the web for 5-10 sources, synthesizes findings, and produces a summary report. The agent works well for simple queries, but on complex topics requiring 8+ searches, the context fills with raw search results and the synthesis quality drops sharply -- the agent starts contradicting itself or forgetting earlier findings.

**Step 1: Diagnosing the context pressure.** You ask Claude: **"My research agent makes 8-10 web searches per task, each returning 5-10K tokens. By the time it tries to synthesize, the context is full of raw search results and the quality degrades. How do I fix this?"**

Claude activates the filesystem-context skill and identifies this as a classic scratch-pad pattern. The core problem: 80K+ tokens of raw search results are competing for attention with the synthesis task.

**Step 2: Implementing the scratch pad.** Claude provides the implementation: after each web search, write the full results to `scratch/search_{topic}_{n}.txt` and return only a 200-token summary to the context. The agent's message history now contains summaries like: `"[Results in scratch/search_kubernetes_1.txt. Key finding: Kubernetes HPA scales based on CPU metrics by default, custom metrics require metrics-server configuration.]"`

When the agent needs a specific detail during synthesis, it uses `grep` to search the scratch files: `grep -A 5 "metrics-server" scratch/search_kubernetes_1.txt`. Only the 5 relevant lines enter the context, not the entire 8,000-token search result.

**Step 3: Adding plan persistence.** You notice the agent sometimes loses track of which sources it has already searched. Claude adds the plan persistence pattern: the agent writes its research plan to `scratch/research_plan.yaml`:

```yaml
objective: "Research Kubernetes autoscaling patterns"
status: in_progress
sources_searched:
  - url: "https://..."
    key_finding: "HPA scales on CPU by default"
    scratch_file: "scratch/search_kubernetes_1.txt"
sources_remaining:
  - "vertical pod autoscaling"
  - "KEDA event-driven scaling"
```

The agent re-reads this file at the start of each search cycle, ensuring it never searches the same source twice and can resume after context compression.

**Step 4: Measuring the improvement.** Before the filesystem pattern, a 10-search task consumed approximately 80K tokens in context. After: the context contains 10 summaries (approximately 2K tokens total) plus the plan file reference. The agent can still access all 80K tokens of raw data through targeted grep searches, but they do not compete for attention during synthesis. Synthesis quality improves because the agent is working with a clean context containing summaries and the plan, not a wall of raw search output.

**Step 5: Extending to sub-agents.** You then parallelize: instead of one agent doing 10 sequential searches, you spawn 3 sub-agents that each search 3-4 topics. Each sub-agent writes to its own workspace:

```
workspace/
  agents/
    agent_1/findings.md
    agent_2/findings.md
    agent_3/findings.md
  coordinator/synthesis.md
```

The coordinator reads the findings files directly instead of receiving summarized messages, preserving the full fidelity of each sub-agent's research.

## Usage Scenarios

### Scenario 1: Offloading large tool outputs to scratch files

**Context:** Your agent integrates with a database that returns 500+ row query results. Carrying all results in context wastes tokens and degrades attention.

**You say:** "My agent queries a database that returns 500-row results. How do I offload these to files and use grep for targeted retrieval?"

**The skill provides:**
- Scratch pad pattern with a token threshold (write to file if output > 2000 tokens)
- Summary extraction function that returns key metrics and file reference
- Grep-based retrieval patterns for specific rows or columns
- File naming conventions with timestamps for disambiguation

**You end up with:** A working scratch pad implementation where database results are written to files and only summary statistics enter the context, with targeted retrieval when specific rows are needed.

### Scenario 2: Persisting plans across context compression

**Context:** Your agent runs multi-hour coding tasks. After context compression, it loses track of which files it modified and which tasks remain.

**You say:** "My coding agent loses its plan after context compression. How do I persist the plan so it survives summarization?"

**The skill provides:**
- YAML-based plan persistence with status tracking per task
- Re-read strategy: agent reads the plan file at the start of each turn
- Checkpoint approach: update the plan file as tasks complete
- Recovery from corrupted or stale plan files

**You end up with:** A plan persistence system where the agent writes its plan to a file, updates it as tasks complete, and re-reads it after any context interruption.

### Scenario 3: Designing a multi-agent file workspace

**Context:** You are building a code review system with 3 parallel agents (security, performance, style) that report to a coordinator.

**You say:** "Design a file workspace for a code review system with 3 specialized agents and a coordinator that synthesizes their findings."

**The skill provides:**
- Directory structure with per-agent workspaces and a coordinator synthesis directory
- Writing conventions for each agent (structured findings with severity, location, description)
- Coordinator reading strategy (read all agent findings, cross-reference, prioritize)
- Conflict resolution for overlapping findings

**You end up with:** A workspace layout that enables parallel agent execution with filesystem-based coordination, preserving full fidelity of each agent's findings.

---

## Decision Logic

The skill matches your query to one or more of its six patterns:

| Your situation | Pattern applied |
|---|---|
| Tool outputs exceeding 2000 tokens | Pattern 1: Scratch Pad |
| Plans lost after context compression | Pattern 2: Plan Persistence |
| Multi-agent coordination with information loss | Pattern 3: Sub-Agent Communication |
| System prompt overloaded with skill instructions | Pattern 4: Dynamic Skill Loading |
| Terminal/build output needs agent access | Pattern 5: Terminal/Log Persistence |
| Agent needs to remember things between sessions | Pattern 6: Self-Modification |

Multiple patterns can be combined. A research agent typically uses patterns 1 (scratch pad for search results), 2 (plan persistence for research plan), and 3 (sub-agent workspaces for parallel research).

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Over-offloading to files | Agent writes everything to files, including small outputs that fit comfortably in context. Adds file I/O latency for no token savings. | Apply the 2000-token threshold: only offload outputs that exceed this size. Small results stay in context. |
| Scratch files accumulate without cleanup | After many tasks, the scratch directory grows unbounded, confusing file discovery | Implement cleanup: delete scratch files after task completion, or use timestamped directories per session |
| Plan file becomes stale or corrupted | Agent reads an outdated plan after a crash or interrupted session | Include a `last_updated` timestamp in the plan YAML; if stale, regenerate from current state |
| Dynamic loading fails for simple models | Less capable models do not recognize when to load additional context from files | Use this pattern only with frontier models. For weaker models, keep critical instructions in static context |
| Self-modification accumulates contradictory instructions | Agent writes conflicting preferences to the instruction file over time | Implement validation: new preferences must not contradict existing ones. Periodically review and clean the preferences file |

## Ideal For

- **Agent framework developers** building long-running agents that need to survive context compression
- **Multi-agent system architects** designing coordination patterns that avoid message-passing degradation
- **Tool integrators** whose agents call high-volume APIs (search, databases, logs) that flood the context
- **Plugin developers** building skills or tools for Claude Code that need context-efficient patterns

## Not For

- **Single-turn tasks** where context pressure is not an issue -- filesystem overhead adds latency without benefit
- **In-context optimization** (KV-cache, observation masking, attention patterns) -- use [context-optimization](../context-optimization/)
- **Summarization and compression** techniques for reducing context size -- use [context-compression](../context-compression/)
- **Context theory and fundamentals** (how attention works, progressive disclosure principles) -- use [context-fundamentals](../context-fundamentals/)

## Related Plugins

- **[Context Optimization](../context-optimization/)** -- Token reduction techniques for in-context efficiency (complementary to filesystem offloading)
- **[Context Compression](../context-compression/)** -- Summarization strategies and compression triggers
- **[Context Fundamentals](../context-fundamentals/)** -- Theory of context engineering and how attention works
- **[Memory Systems](../memory-systems/)** -- Persistent storage patterns for agent memory (production frameworks like Mem0, Zep, Letta)
- **[Multi-Agent Patterns](../multi-agent-patterns/)** -- Coordination patterns for multi-agent systems (filesystem context is one coordination mechanism)
- **[Tool Design](../tool-design/)** -- Designing tools that return file references for large outputs

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
