# Hosted Agents

> **v1.0.4** | Agent Architecture | 5 iterations

Infrastructure patterns for hosted background agents. Sandbox environments, image registry pattern, self-spawning agents, multiplayer support, warm pools, and multi-client integration (Slack, web, Chrome).

## What Problem Does This Solve

Running AI coding agents locally means resource contention with the developer's machine, inconsistent environments between team members, and sessions that only one person can use at a time. Moving agents to hosted sandboxed infrastructure solves all three, but introduces new challenges: slow session start-up, per-session state isolation at scale, multi-client synchronisation, and secure commit attribution. This skill documents the architectural patterns -- image registry, warm pools, per-session SQLite, WebSocket hibernation, and self-spawning -- that production teams have used to ship reliable hosted agents.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install hosted-agents@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## What's Inside

Single-skill plugin with one SKILL.md and one reference file.

### SKILL.md Structure

| Topic | What It Covers |
|---|---|
| **Sandbox Infrastructure** | Image registry pattern with 30-minute pre-build cadence, filesystem snapshots for instant restore, Git configuration for background agents (app tokens, user identity for commits), warm pool strategy with predictive warm-up |
| **Agent Framework Selection** | Server-first architecture (TUI and desktop as clients), code-as-source-of-truth principle, plugin system requirements (event listeners, conditional tool blocking, runtime context injection) |
| **Speed Optimizations** | Parallel file reads before git sync, predictive sandbox warm-up when user starts typing, making session speed limited only by model time-to-first-token |
| **Self-Spawning Agents** | Tools for starting sessions and checking status, prompt engineering for when to spawn sub-agents vs. handle inline |
| **API Layer** | Per-session SQLite for state isolation, WebSocket hibernation for idle connections, cross-client sync, real-time streaming |
| **Multiplayer Support** | Data model changes for per-prompt authorship, shared session links, concurrent editing patterns |
| **Client Integration** | Slack bot (repository classifier using fast model, virality loop design), web interface, Chrome extension |
| **Metrics** | Merged PR rate as primary KPI, follow-up message handling strategies (queue vs insert), internal adoption patterns |

### Reference File

| File | What It Covers |
|---|---|
| `infrastructure-patterns.md` | Detailed implementation patterns including Ramp's background agent architecture, Modal Sandboxes, Cloudflare Durable Objects, and OpenCode reference implementation |

## How to Use

**Direct invocation:**

```
Use the hosted-agents skill to design the sandbox infrastructure for our coding agent platform
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

`hosted-agents` · `sandbox` · `background-agents` · `multiplayer` · `infrastructure`

## Usage Scenarios

**1. Designing a hosted coding agent platform from scratch.** You want to offer coding agents as a service. The skill walks through the three-layer architecture (sandbox, API, client), explains why image pre-building on a 30-minute cadence is critical for session speed, and provides the warm pool strategy for high-volume repositories.

**2. Reducing agent session start-up time.** Users complain that sessions take 45 seconds to start. Apply the speed optimization patterns: pre-build environment images with all dependencies cached, maintain a warm pool of ready sandboxes, and start warming a sandbox predictively as soon as the user begins typing.

**3. Adding multiplayer collaboration to an existing agent.** Your single-user agent needs to support shared sessions where multiple teammates can see and contribute to the same conversation. The skill covers the data model changes needed (per-prompt authorship), the WebSocket architecture for real-time sync, and the UX patterns for shared session links.

**4. Building a Slack bot interface for non-engineers.** Your agents are used by engineers through a CLI, but product managers and designers want access too. Use the Slack integration architecture: a repository classifier that uses a fast model to route requests, natural-language command interface, and virality loop design for organic adoption.

**5. Implementing self-spawning for large tasks.** A user asks the agent to refactor 30 files. Instead of doing it sequentially, the agent spawns sub-agents to handle independent file groups in parallel. The skill provides the spawning tool design, status-checking patterns, and prompt engineering guidance for when to spawn vs. handle inline.

## When to Use / When NOT to Use

**Use when:** You are building background coding agents that run in the cloud, designing sandboxed execution environments, implementing multiplayer sessions, creating multi-client interfaces (Slack, web, Chrome), scaling beyond local machines, or building self-spawning agent systems.

**Do NOT use for:**
- **Agent coordination patterns or multi-agent design** -- use [multi-agent-patterns](../multi-agent-patterns/)
- **Agent memory or persistence** -- use [memory-systems](../memory-systems/)
- **Tool design or tool interfaces** -- use [tool-design](../tool-design/)

## Related Plugins in SkillStack

- **[Agent Evaluation](../agent-evaluation/)** -- Evaluation frameworks for LLM agent systems with rubrics and LLM-as-judge
- **[Agent Project Development](../agent-project-development/)** -- Task-model fit analysis and pipeline architecture for LLM projects
- **[BDI Mental States](../bdi-mental-states/)** -- Belief-Desire-Intention cognitive architecture for LLM agents
- **[Memory Systems](../memory-systems/)** -- Production memory architectures comparing Mem0, Zep, Letta, Cognee, LangMem
- **[Multi Agent Patterns](../multi-agent-patterns/)** -- Supervisor, peer-to-peer, swarm, and hierarchical multi-agent architectures

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
