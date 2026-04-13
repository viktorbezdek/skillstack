# Hosted Agents

> **v1.0.4** | Agent Architecture | 5 iterations

> Infrastructure patterns for running AI coding agents in the cloud -- sandbox environments, image pre-building, warm pools, self-spawning, multiplayer sessions, and multi-client integration.

## The Problem

Running AI coding agents on local machines hits fundamental limits quickly. A developer's laptop can run one agent at a time, competing with their IDE, build tools, and browser for CPU and memory. When the developer closes the laptop, the agent stops. When two team members want to collaborate on the same agent session, they cannot -- sessions are tied to a single machine. When the agent needs to work on a repository that requires 20 minutes of dependency installation, the user waits 20 minutes before the first useful response.

Scaling beyond one developer reveals deeper problems. Each developer has a different machine configuration, different installed tools, different environment variables. An agent that works perfectly on one machine fails silently on another because a dependency is missing or a path is different. There is no consistent, reproducible environment for agent execution, which means every "it works on my machine" bug from traditional development is amplified in the agent context.

The most critical constraint is session speed. If an agent takes 3 minutes to start (clone repository, install dependencies, run initial build), users will not wait. They will type the code themselves. The gap between "agent is ready" and "user loses patience" is measured in seconds, not minutes. Without infrastructure that brings session startup time below the model's time-to-first-token, hosted agents are a demo, not a product.

## The Solution

This plugin provides production-tested infrastructure patterns for running AI coding agents in remote sandboxed environments. The core architecture addresses the session speed problem through image pre-building: environment images are rebuilt every 30 minutes with the repository cloned, dependencies installed, and initial builds completed. When a user starts a session, the sandbox spins up from a recent image and is ready in seconds, not minutes.

The skill covers six infrastructure areas: sandbox setup (image registry pattern, snapshot and restore, git configuration for background agents), speed optimizations (predictive warm-up, parallel file reading, build-time maximization), self-spawning agents (agent-initiated sub-sessions for parallel work), API layer (per-session state isolation, real-time WebSocket streaming, multi-client synchronization), multiplayer support (shared sessions, user attribution, collaboration patterns), and client implementations (Slack integration, web interface, Chrome extension for non-engineers).

The plugin ships one SKILL.md with all patterns, one reference file with detailed implementation patterns, 13 trigger eval cases, and 3 output quality eval cases.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Agent starts by cloning, installing dependencies, and building -- 3-20 minute wait before first response | Image pre-building every 30 minutes means sandbox is at most 30 minutes stale; startup is seconds, not minutes |
| Each developer's agent runs in a different environment; behavior varies across machines | Sandboxed environments provide consistent, reproducible execution regardless of the user's machine |
| Sessions tied to one user on one machine; collaboration requires screen sharing | Multiplayer sessions with shared state; multiple users can interact with the same agent session |
| Agent works only through one interface (CLI or IDE) | Multi-client architecture: Slack, web, Chrome extension, VS Code -- all synchronized to the same session |
| Complex tasks require one agent doing everything sequentially | Self-spawning agents: an agent can create sub-sessions for parallel research or split large PRs into smaller ones |
| No visibility into whether agent work produces value | Metrics infrastructure: track sessions-to-merged-PRs as the primary success metric |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install hosted-agents@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when your prompts mention background agents, hosted agents, sandboxed execution, agent infrastructure, warm pools, multiplayer agents, or self-spawning agents.

## Quick Start

1. Install the plugin using the commands above
2. Open a Claude Code session
3. Type: `Design the sandbox infrastructure for a hosted coding agent that works on our monorepo`
4. Claude provides the image registry pattern with build cadence, snapshot strategy, and warm pool configuration
5. Next, try: `How should the agent spawn sub-sessions for parallel research across multiple repositories?`

---

## System Overview

```
User prompt (hosted agent architecture / sandbox design / multiplayer)
        |
        v
+------------------+     +-------------------------------+
|  hosted-agents   |---->| Topic routing                  |
|  skill (SKILL.md)|     | (match to infrastructure area)|
+------------------+     +-------------------------------+
        |                         |
        v                         v
  Core concepts:           6 infrastructure areas:
  - Session speed is       1. Sandbox Infrastructure
    everything               (image registry, snapshots, warm pools)
  - Pre-build everything   2. Speed Optimizations
  - Server-first             (predictive warm-up, parallel reads)
    architecture           3. Self-Spawning Agents
        |                    (sub-sessions, prompt engineering)
        v                  4. API Layer
  Practical guidance:        (state isolation, WebSocket, sync)
  - Follow-up handling     5. Multiplayer Support
  - Metrics that matter      (shared sessions, user attribution)
  - Adoption strategy      6. Client Implementations
                             (Slack, web, Chrome extension)
                                   |
                                   v
                           +----------------------------+
                           | Infrastructure Patterns    |
                           | reference (detailed code)  |
                           +----------------------------+
```

Single-skill plugin with one reference file for detailed implementation patterns. No hooks, no MCP servers, no scripts.

## What's Inside

| Component | Type | What It Provides |
|---|---|---|
| **hosted-agents** | Skill | 6 infrastructure areas, core concepts, practical guidance, adoption strategy |
| **infrastructure-patterns.md** | Reference | Detailed implementation patterns for sandbox, API layer, and client integration |
| **trigger-evals** | Eval | 13 trigger eval cases (8 positive, 5 negative) |
| **output-evals** | Eval | 3 output quality eval cases |

### Component Spotlight

#### hosted-agents (skill)

**What it does:** Activates when you ask about building hosted or background coding agents, designing sandboxed execution environments, implementing multiplayer agent sessions, creating multi-client agent interfaces, or scaling agent infrastructure. Provides production-tested patterns for each infrastructure area with specific implementation guidance.

**Input -> Output:** You describe a hosted agent architecture challenge -> The skill provides the matching infrastructure pattern(s) with implementation approach, trade-offs, and guidance on what to build first.

**When to use:**
- Building background coding agents that run independently of user devices
- Designing sandboxed execution environments for agent workloads
- Implementing multiplayer agent sessions with shared state
- Creating multi-client agent interfaces (Slack, Web, Chrome extensions)
- Scaling agent infrastructure beyond local machine constraints
- Building systems where agents spawn sub-agents for parallel work

**When NOT to use:**
- Agent coordination patterns and multi-agent design -> use [multi-agent-patterns](../multi-agent-patterns/)
- Agent memory and persistence across sessions -> use [memory-systems](../memory-systems/)
- Tool interface design for agents -> use [tool-design](../tool-design/)
- Building MCP servers -> use [mcp-server](../mcp-server/)

**Try these prompts:**

```
Design the sandbox infrastructure for a hosted coding agent that works on our 50K-file monorepo
```

```
How should I implement warm pools so agent sessions start in under 5 seconds?
```

```
Design a self-spawning pattern where the agent can create sub-sessions for parallel code research
```

```
Build a multiplayer architecture where 3 team members can collaborate on the same agent session
```

```
What's the best way to add a Slack bot interface to our hosted agent? We want team members to trigger agent sessions from a channel.
```

**Key references:**

| Reference | Topic |
|---|---|
| `infrastructure-patterns.md` | Detailed sandbox architecture, API layer, client patterns, and implementation code |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Build an agent" | "Design the sandbox infrastructure for a background coding agent that clones our repo, installs deps, and runs tasks" |
| "Make it faster" | "How should I implement warm pools and predictive warm-up to get session startup under 5 seconds?" |
| "Add multiplayer" | "Design a multiplayer architecture where team members can join an active agent session and send prompts attributed to their identity" |
| "Scale the agent" | "Our agent runs 50 concurrent sessions. How should I isolate per-session state and handle WebSocket connections efficiently?" |
| "Add Slack" | "Build a Slack bot that classifies which repository to work in based on the channel and message content, then spawns an agent session" |

### Structured Prompt Templates

**For sandbox design:**
```
Design sandbox infrastructure for a hosted agent. Repository: [size/language/build time]. Target session startup: [seconds]. Image build cadence: [frequency]. Expected concurrency: [sessions].
```

**For client integration:**
```
Add a [Slack / web / Chrome extension] client to our hosted agent. The client should: [trigger sessions / monitor progress / interact during execution]. Users: [engineers / non-engineers / mixed]. Auth: [GitHub / SSO / anonymous].
```

**For self-spawning agents:**
```
Design a self-spawning pattern where agents can: [parallel research / split PRs / cross-repo investigation]. Constraints: [max concurrent sub-sessions / coordination mechanism / how results merge].
```

### Prompt Anti-Patterns

- **Asking about agent coordination logic:** "How should agents decide who does what?" -- this plugin covers infrastructure, not coordination patterns. Use [multi-agent-patterns](../multi-agent-patterns/) for supervisor/swarm/pipeline patterns.
- **Requesting memory system design:** "How should the agent remember past sessions?" -- use [memory-systems](../memory-systems/) for Mem0, Zep, Graphiti, or custom memory.
- **Combining infrastructure with implementation:** "Build a hosted agent that does code review" -- first design the infrastructure (this plugin), then implement the code review logic (use [code-review](../code-review/)).

## Real-World Walkthrough

You are the platform engineering lead at a mid-size company. The team wants to build a hosted coding agent that developers can access from Slack. The agent should clone any of your 12 repositories, make code changes, and open PRs. Currently, developers use Claude Code locally, but adoption is limited because setup takes 15 minutes per repo and only works on the developer's machine.

**Step 1: Sandbox design.** You ask Claude: **"Design the sandbox infrastructure for a hosted agent. We have 12 repositories, the largest is 50K files with a 10-minute cold build. We want session startup under 10 seconds for the top 5 most-used repos."**

Claude activates the hosted-agents skill and provides the image registry pattern:
- Build environment images every 30 minutes for the top 5 repositories
- Each image contains: cloned repo at latest commit, all dependencies installed, initial build completed, test suite caches populated
- When a session starts, spin up a sandbox from the most recent image (at most 30 minutes stale)
- Run `git pull` to sync the last 30 minutes of changes (typically a few seconds for 1-2 commits)

For the remaining 7 less-used repos, use on-demand builds with a cache layer for dependencies.

**Step 2: Warm pool.** You ask: **"The CEO tried the agent and said '10 seconds is too slow.' How do I get it under 3 seconds?"**

Claude provides the warm pool strategy:
- Maintain 2-3 pre-warmed sandboxes per popular repository
- When a user's Slack message is classified to a repository, assign them a pre-warmed sandbox instantly
- The warm pool refills in the background as sandboxes are consumed
- Predictive warm-up: start warming a sandbox when the user begins typing in Slack (the typing indicator API)

**Step 3: Slack integration.** You ask: **"Design the Slack bot that triggers sessions."**

Claude provides the repository classification pattern:
- Build a fast classifier (small model) that maps Slack messages to repositories using channel name, message content, and thread context
- Each channel is tagged with a default repository (e.g., #frontend -> `web-app`, #api -> `backend-service`)
- If the classifier returns "unknown," ask the user which repo to use
- The bot creates a thread for the agent session, streaming updates as the agent works

**Step 4: Multiplayer.** You ask: **"Two developers want to work on the same agent session -- one reviewing while the other directs."**

Claude provides the multiplayer architecture:
- Sessions are not tied to a single user -- any team member with access can join via a shared session URL
- Each prompt is attributed to the user who sent it (using their GitHub identity for commits)
- The data model stores `prompted_by` per message, not per session
- Real-time sync via WebSocket ensures all participants see the same state

**Step 5: Metrics.** You ask: **"How do we measure if this is actually working?"**

Claude provides the metrics framework:
- Primary metric: sessions resulting in merged PRs (not sessions started, not lines generated)
- Secondary: time from session start to first model response (target: < 3 seconds)
- Secondary: PR approval rate and average revision count
- Dashboard showing "agent-written code %" per repository, tracking adoption over time

You now have a complete architecture: sandbox with warm pools, Slack integration with repository classification, multiplayer support, and a metrics framework -- ready to build incrementally.

## Usage Scenarios

### Scenario 1: Building a sandboxed execution environment

**Context:** Your team wants to run AI coding agents in isolated cloud environments. The monorepo has a 15-minute cold build that makes local execution impractical.

**You say:** "Design a sandbox environment for our monorepo agent. Cold build is 15 minutes. We need sessions to start in under 5 seconds."

**The skill provides:**
- Image registry pattern with 30-minute build cadence
- Build-time optimization: move all dependency installation and initial build to image creation
- Snapshot strategy: filesystem snapshots at key checkpoints for instant restore
- Warm pool sizing: 3-5 pre-warmed sandboxes based on expected usage patterns

**You end up with:** A sandbox architecture where session startup is decoupled from build time -- users start working in seconds regardless of how long the build takes.

### Scenario 2: Adding a Slack bot interface

**Context:** Your engineering team of 30 people uses Slack daily. You want to distribute the hosted agent through Slack so developers can trigger sessions without any new tooling.

**You say:** "Design a Slack bot for our hosted agent. 12 repositories. The bot should figure out which repo to work in from the message and channel."

**The skill provides:**
- Repository classifier using channel tags and message content
- Thread-based session management (one thread = one agent session)
- Streaming updates as the agent works (tool calls, file changes, PR creation)
- Error handling for ambiguous repository classification

**You end up with:** A Slack bot that is the easiest distribution channel for internal adoption -- team members see others using it and start naturally.

### Scenario 3: Implementing self-spawning for complex tasks

**Context:** Your agent receives requests that require changes across 3 repositories. Currently it handles them sequentially, which takes too long.

**You say:** "Design a self-spawning pattern where the agent can create sub-sessions for parallel work across multiple repos."

**The skill provides:**
- Agent tool design: `create_session(repo, prompt)`, `check_session_status(id)`, `get_session_result(id)`
- Prompt engineering for when to spawn (cross-repo changes, research tasks, PR splitting)
- Coordination pattern: main agent monitors sub-sessions and synthesizes results
- Resource limits: maximum concurrent sub-sessions and timeout handling

**You end up with:** An agent architecture that parallelizes naturally, creating sub-sessions for cross-repo work and merging results in the main session.

---

## Decision Logic

The skill matches your query to one of six infrastructure areas:

| Your situation | Infrastructure area |
|---|---|
| Need fast session startup, reproducible environments | Sandbox Infrastructure (image registry, snapshots, warm pools) |
| Startup too slow even with images | Speed Optimizations (predictive warm-up, parallel reads, build-time maximization) |
| Complex tasks need parallel work | Self-Spawning Agents (sub-session tools, prompt engineering) |
| Need multi-client support, real-time streaming | API Layer (state isolation, WebSocket, synchronization) |
| Team wants to collaborate on sessions | Multiplayer Support (shared sessions, user attribution) |
| Need Slack, web, or browser interface | Client Implementations (Slack bot, web app, Chrome extension) |

Most production systems combine multiple areas. A typical build order: sandbox first (core functionality), then Slack integration (distribution), then warm pools (speed), then multiplayer (collaboration).

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Image build fails silently | Sessions start from stale image; code is hours behind main branch | Monitor image build pipeline; alert on build failure; fall back to previous known-good image |
| Warm pool exhausted during usage spike | Session startup degrades from 3 seconds to 30+ seconds (cold start) | Auto-scale warm pool size based on usage patterns; implement queueing with estimated wait time for users |
| Self-spawned sub-session runs forever | Resource leak; cloud bill increases; main session waits indefinitely | Set timeout on all sub-sessions; main agent checks status periodically; auto-terminate stale sub-sessions |
| Multiplayer attribution wrong | Code committed under wrong user identity | Verify git `user.name` and `user.email` are set from the prompting user's identity, not the app identity |
| Slack classifier picks wrong repository | Agent starts working on the wrong codebase | Include a confirmation step: "I think this is about the `web-app` repo. Is that right?" Allow user to correct before sandbox spins up |

## Ideal For

- **Platform engineering teams** building internal developer tools that include AI coding agents
- **Startups building AI-native development products** (e.g., coding assistants, automated PR generators)
- **Enterprise teams** that need multiplayer, audit trails, and user attribution for AI-generated code
- **Teams adopting AI agents at scale** who have outgrown local CLI execution and need cloud infrastructure

## Not For

- **Agent coordination patterns** (supervisor, swarm, pipeline architectures) -- use [multi-agent-patterns](../multi-agent-patterns/)
- **Agent memory and persistence** (remembering past sessions, learning over time) -- use [memory-systems](../memory-systems/)
- **Tool interface design** (how agents call tools, tool description optimization) -- use [tool-design](../tool-design/)

## Related Plugins

- **[Multi-Agent Patterns](../multi-agent-patterns/)** -- Coordination patterns for self-spawning agents (supervisor, swarm, pipeline)
- **[Memory Systems](../memory-systems/)** -- Persistent memory for agents that need to remember across sessions
- **[Tool Design](../tool-design/)** -- Designing tools for agent spawning and status checking
- **[MCP Server](../mcp-server/)** -- Build MCP servers that agents use to interact with external systems
- **[Filesystem Context](../filesystem-context/)** -- Filesystem patterns for session state and artifacts within sandboxes

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
