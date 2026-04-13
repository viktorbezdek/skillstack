# Hosted Agents

> **v1.0.4** | Agent Architecture | 5 iterations

> Infrastructure patterns for running AI coding agents in the cloud -- sandbox environments, image pre-building, warm pools, self-spawning, multiplayer sessions, and multi-client integration.

## The Problem

Running AI coding agents locally works for a single developer on a single task, but breaks down in every other scenario. The agent competes with the developer's IDE, browser, and build tools for CPU and memory. Each team member has a different local environment, so the agent produces inconsistent results. Only one person can use a session at a time -- when the PM wants to watch the agent work or the designer wants to describe a UI change, they have to take turns or screen-share.

Moving agents to hosted infrastructure solves these problems but introduces new ones. Spinning up a development environment from scratch takes 30-90 seconds (clone the repo, install dependencies, run the build), which is an eternity when users expect near-instant responses. Per-session state isolation is straightforward for one user but becomes complex at scale -- hundreds of concurrent sessions each need their own database, filesystem, and process space without interfering with each other. Multi-client synchronization (a user starts a session in Slack, continues it on the web, and reviews the PR in VS Code) requires a real-time state layer that most teams have never built.

The deeper problem is that most teams building hosted agents solve each of these challenges independently, discovering the same patterns through trial and error: image pre-building to reduce startup time, warm pools for predictive sandbox allocation, per-session SQLite for state isolation, WebSocket hibernation for idle connections. These patterns are well-established in production systems but not documented in a form that a new team can adopt systematically.

## The Solution

This plugin documents the architectural patterns that production teams (including Ramp's background agent system) have used to build reliable hosted agent infrastructure. It covers the full three-layer architecture: sandbox infrastructure for isolated execution, API layer for state management and client coordination, and client interfaces for user interaction across platforms.

The sandbox layer covers the image registry pattern (pre-build environment images every 30 minutes so sessions start from a recent snapshot instead of from scratch), filesystem snapshots for instant restore, Git configuration for background agents (app tokens for clone, user identity for commits), and warm pool strategy with predictive warm-up (start warming a sandbox when the user begins typing, not when they submit).

The API layer covers per-session SQLite for state isolation at scale, WebSocket hibernation for idle connections, cross-client synchronization, and real-time streaming of tool execution and model output. The client layer covers Slack bot integration (with a repository classifier and virality loop design), web interface (with hosted VS Code and before/after screenshots), and Chrome extension (with DOM extraction instead of raw screenshots for token efficiency).

The skill also covers self-spawning agents (tools for starting and checking sub-sessions, prompt engineering for when to spawn), multiplayer support (per-prompt authorship, shared session links), and metrics (merged PR rate as the primary KPI).

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Agent sessions take 45-90 seconds to start because the environment builds from scratch each time | Image registry pre-builds every 30 minutes; warm pool has sandboxes ready before the user types -- startup limited only by model time-to-first-token |
| Each session re-clones the repo and reinstalls all dependencies, wasting compute and time | Pre-built images contain the cloned repo, installed dependencies, and cached build artifacts from running the test suite once |
| Per-session state isolation is ad-hoc, leading to sessions that interfere with each other at scale | Per-session SQLite provides isolation by default; no session can impact another's performance |
| Only one person can use an agent session at a time -- collaboration means screen-sharing | Multiplayer support with per-prompt authorship, shared session links, and real-time sync across clients |
| Agent is only accessible through the CLI -- non-engineers cannot use it | Multi-client architecture: Slack bot for natural-language interaction, web interface for visual work, Chrome extension for non-engineers |
| Large tasks run sequentially in one session, taking hours | Self-spawning agents break large tasks into parallel sub-sessions, each producing its own PR |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install hosted-agents@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when your prompts mention hosted agents, background agents, sandboxed execution, agent infrastructure, multiplayer agents, or remote coding environments.

## Quick Start

1. Install the plugin using the commands above
2. Open a Claude Code session
3. Type: `Design the sandbox infrastructure for a hosted coding agent that needs to start sessions in under 5 seconds`
4. Claude produces the three-layer architecture with image registry pattern, warm pool strategy, predictive warm-up, and per-session state isolation
5. Next, try: `How do I add multiplayer support so multiple team members can collaborate in the same agent session?` to get the data model changes, WebSocket sync architecture, and shared session link design

## What's Inside

Single-skill plugin with one SKILL.md and one reference file, 13 trigger eval cases, and 3 output eval cases.

| Topic | What It Covers |
|---|---|
| **Sandbox Infrastructure** | Image registry pattern (30-min pre-build cadence), filesystem snapshots, Git config for background agents, warm pool with predictive warm-up |
| **Agent Framework Selection** | Server-first architecture, code-as-source-of-truth principle, plugin system requirements (event listeners, conditional tool blocking, runtime context injection) |
| **Speed Optimizations** | Parallel file reads before git sync, predictive sandbox warm-up, maximizing build-time work |
| **Self-Spawning Agents** | Tools for starting/checking sub-sessions, prompt engineering for spawn-vs-inline decisions |
| **API Layer** | Per-session SQLite, WebSocket hibernation, cross-client sync, real-time streaming |
| **Multiplayer Support** | Per-prompt authorship data model, shared session links, concurrent editing patterns |
| **Client Integration** | Slack bot (repository classifier, virality loop), web interface, Chrome extension (DOM extraction) |
| **Metrics** | Merged PR rate as primary KPI, follow-up message handling strategies, adoption patterns |

### Reference

| Reference | Topic |
|---|---|
| `infrastructure-patterns.md` | Detailed implementation patterns from Ramp's background agent, Modal Sandboxes, Cloudflare Durable Objects, and OpenCode |

### hosted-agents

**What it does:** Activates when you ask about building background coding agents, designing sandbox environments, implementing multiplayer sessions, creating multi-client interfaces, scaling agent infrastructure, or building self-spawning agent systems. Provides the three-layer architecture (sandbox, API, client) with specific patterns for each layer and production-tested guidance from teams that have already shipped these systems.

**Try these prompts:**

```
Design the infrastructure for a hosted coding agent platform that serves 50 concurrent users with sub-5-second session startup
```

```
How do I pre-build environment images for my agent's sandbox so sessions don't have to clone and install from scratch?
```

```
Add multiplayer support to our agent -- I want team members to share a session link and see each other's prompts in real time
```

```
Build a Slack bot interface for our coding agent so product managers can use it without leaving Slack
```

```
Our agent needs to handle a 30-file refactoring task -- how do I implement self-spawning so it can parallelize the work?
```

## Real-World Walkthrough

You are the engineering lead at a 200-person company that has been using AI coding agents locally. Adoption is strong among senior engineers, but three problems keep coming up: sessions take over a minute to start (clone, install, build), only one person can work with the agent at a time, and non-engineers (PMs, designers) cannot use it at all because it requires a CLI. Your CTO asks you to build a hosted version.

You start by asking Claude: **"Design the infrastructure for a hosted coding agent that starts sessions in under 5 seconds and supports multiplayer."**

Claude activates the hosted-agents skill and begins with the **sandbox layer**. The key insight: session speed should be limited only by model time-to-first-token, with all infrastructure setup completed before the user starts their session.

Claude designs the **image registry pattern**. A background job runs every 30 minutes for each active repository. It clones the repo, installs all dependencies, runs the build, executes the test suite once (to populate caches), and saves the result as a snapshot image. When a user starts a session, the sandbox spins up from the latest image -- the repo is at most 30 minutes old, so syncing with the current HEAD is a fast `git pull` of recent commits, not a full clone.

On top of this, Claude adds the **warm pool strategy**. For your top 10 most-used repositories, the system maintains a pool of 3 pre-warmed sandboxes each. These are already running, already synced, and ready to accept a session. When a user starts typing (not when they submit), the system starts warming a sandbox predictively. By the time they hit Enter, the sandbox is ready. Session startup drops from 60+ seconds to under 3 seconds.

Claude also adds a **speed optimization for file reads**: allow the agent to start reading files immediately even if the `git pull` from the latest branch has not completed. In large repositories, the files the user is asking about are rarely the ones that changed in the last 30 minutes. File reads proceed immediately; only file writes are blocked until synchronization completes.

Next, Claude designs the **API layer**. Each session gets its own SQLite database for state isolation -- no session can impact another's performance, and the system handles hundreds of concurrent sessions without a shared database bottleneck. Real-time updates (token streaming from the model, tool execution status, file change notifications) flow through WebSocket connections. Claude recommends WebSocket hibernation (Cloudflare Durable Objects pattern) to reduce compute costs during idle periods while maintaining open connections.

For **multiplayer**, Claude explains the data model changes. The session model must not tie sessions to a single author. Each prompt carries its own authorship information: who sent it, when, and from which client. When the agent commits code, it uses the prompting user's Git identity (`user.name` and `user.email`), not the app's identity. This ensures correct commit attribution and prevents users from approving their own agent-generated PRs.

Shared session links are simple: generate a unique URL for each session, and any authenticated user with the link can view and contribute. The WebSocket sync layer already handles real-time updates, so multiplayer is "nearly free" once the synchronization architecture is in place.

For **client integration**, Claude designs three surfaces. The **Slack bot** is the highest-priority client because it creates a virality loop: when a team member uses the agent in a public Slack channel, other team members see it working and want to try it. The bot uses a fast model (like Haiku) to classify which repository the user is referring to based on the message text, thread context, and channel name. The **web interface** provides a richer experience: real-time streaming of agent work, a hosted VS Code instance running inside the sandbox for live code editing, and before/after screenshots for PR review. The **Chrome extension** serves non-engineers: a sidebar chat interface with a screenshot tool that extracts DOM structure and React component tree instead of sending raw screenshots (reducing token usage while maintaining precision).

Finally, Claude covers **metrics and adoption**. The primary KPI is sessions resulting in merged PRs -- not sessions started, not PRs created, but PRs that were actually merged. This measures real value delivered. The adoption strategy: work in public Slack channels for visibility, let the product create its own virality loop, and build to people's actual needs rather than hypothetical requirements.

You ship the hosted agent over two months. Session startup drops from 60 seconds to 3 seconds. The Slack bot drives adoption among non-engineers -- within a month, PMs are using the agent to update copy, designers are using it to adjust CSS, and the agent-written code percentage across repositories climbs to 15%. The multiplayer feature becomes the surprise hit: pair debugging sessions where an engineer and a PM look at the same agent conversation become a daily occurrence.

## Usage Scenarios

### Scenario 1: Designing sandbox infrastructure from scratch

**Context:** You are building a hosted agent platform and need the sandbox architecture that supports fast session startup and clean isolation.

**You say:** "Design the sandbox infrastructure for our coding agent -- we need fast startup, clean isolation, and support for 100 concurrent sessions"

**The skill provides:**
- Image registry pattern with 30-minute pre-build cadence
- Warm pool strategy with predictive warm-up
- Per-session filesystem and process isolation
- Git configuration for background agent commits
- Snapshot and restore for session continuity

**You end up with:** A complete sandbox architecture document with build pipeline, warm pool sizing, and isolation model.

### Scenario 2: Reducing agent session startup time

**Context:** Users complain that agent sessions take 45 seconds to start. You need to get this under 5 seconds.

**You say:** "Our agent sessions take 45 seconds to start -- how do I reduce this to under 5 seconds?"

**The skill provides:**
- Image pre-building to move clone/install/build to background jobs
- Warm pool with predictive warm-up (start warming when user types, not when they submit)
- Parallel file reads before git sync completes
- Metrics for measuring startup time breakdown

**You end up with:** A prioritized optimization plan with expected time savings for each technique, targeting sub-5-second startup.

### Scenario 3: Adding a Slack bot for non-engineer access

**Context:** Your agents work well for engineers via CLI, but PMs and designers cannot use them. You want a Slack interface.

**You say:** "Build a Slack bot interface so our PMs and designers can use the coding agent without learning the CLI"

**The skill provides:**
- Repository classifier using a fast model to route requests to the right repo
- Natural-language command interface with no syntax required
- Virality loop design (public channel usage drives organic adoption)
- Session linking so a Slack conversation can continue on the web interface

**You end up with:** A Slack bot architecture that classifies repositories, creates agent sessions, and streams results back to the channel.

### Scenario 4: Implementing self-spawning for large tasks

**Context:** A user asks the agent to refactor authentication across 30 files. Running sequentially would take hours.

**You say:** "How do I make my agent spawn sub-agents to parallelize a large refactoring task?"

**The skill provides:**
- Self-spawning tool design: start session, check status, retrieve results
- Prompt engineering for when to spawn vs. handle inline
- Work decomposition strategy (group independent files into parallel sub-tasks)
- PR strategy (one PR per sub-agent or consolidated PR from coordinator)

**You end up with:** A self-spawning architecture where the agent breaks large tasks into parallel sub-sessions, each producing independent results.

## Ideal For

- **Teams building hosted coding agent platforms** -- the three-layer architecture (sandbox, API, client) provides the complete infrastructure blueprint
- **Engineering leads scaling beyond local agent execution** -- image pre-building, warm pools, and predictive warm-up solve the startup time problem that blocks adoption
- **Companies wanting non-engineer access to coding agents** -- Slack bot, web interface, and Chrome extension patterns serve different user types without requiring CLI skills
- **Teams building collaborative AI workflows** -- multiplayer support with per-prompt authorship enables pair debugging, collaborative code review, and teaching sessions
- **Organizations tracking agent ROI** -- merged PR rate as primary KPI and adoption strategy guidance for measuring and growing real value

## Not For

- **Agent coordination patterns or multi-agent design** -- this plugin covers the infrastructure for hosting agents, not the patterns for how agents coordinate with each other. Use [multi-agent-patterns](../multi-agent-patterns/) for supervisor, swarm, and pipeline architectures
- **Agent memory and persistence across sessions** -- use [memory-systems](../memory-systems/) for production memory frameworks (Mem0, Zep, Letta, Cognee, LangMem)
- **Designing tools and tool interfaces for agents** -- use [tool-design](../tool-design/) for tool description optimization, parameter design, and error handling patterns

## How It Works Under the Hood

The plugin is a single-skill architecture with one SKILL.md and one reference file. The SKILL.md covers eight topics organized around the three-layer architecture:

**Sandbox Layer:**
1. Image registry pattern (pre-build cadence, snapshot contents, sync strategy)
2. Warm pool strategy (pool sizing, predictive warm-up, expiration)
3. Speed optimizations (parallel reads, build-time maximization)

**API Layer:**
4. Per-session state isolation (SQLite per session)
5. Real-time streaming (WebSocket with hibernation)
6. Self-spawning agents (tool design, prompt engineering)

**Client Layer:**
7. Slack bot (repository classifier, virality loop)
8. Web interface and Chrome extension

The reference file (`infrastructure-patterns.md`) provides detailed implementation patterns drawn from production systems: Ramp's background agent architecture, Modal Sandboxes for compute isolation, Cloudflare Durable Objects for per-session state, and OpenCode as a server-first agent framework reference.

## Related Plugins

- **[Multi-Agent Patterns](../multi-agent-patterns/)** -- Supervisor, peer-to-peer, swarm, and hierarchical multi-agent architectures -- complements hosted agents with coordination logic
- **[Memory Systems](../memory-systems/)** -- Production memory architectures for persistent agent memory across sessions
- **[Agent Evaluation](../agent-evaluation/)** -- Evaluation frameworks for measuring agent quality with rubrics and LLM-as-judge
- **[Agent Project Development](../agent-project-development/)** -- Task-model fit analysis and pipeline architecture for LLM projects
- **[BDI Mental States](../bdi-mental-states/)** -- Belief-Desire-Intention cognitive architecture for LLM agents

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
