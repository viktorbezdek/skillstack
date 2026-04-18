---
name: hosted-agents
description: Build and deploy hosted background coding agents with sandboxed VM execution, multiplayer sessions, and multi-client interfaces. Use when the user asks to "build background agent", "create hosted coding agent", "set up sandboxed execution", "implement multiplayer agent", or mentions background agents, sandboxed VMs, agent infrastructure, Modal sandboxes, self-spawning agents, or remote coding environments. NOT for agent coordination patterns or multi-agent design (use multi-agent-patterns), NOT for agent memory or persistence (use memory-systems), NOT for tool design or tool interfaces (use tool-design).
---

# Hosted Agent Infrastructure

Hosted agents run in remote sandboxed environments rather than on local machines. When designed well, they provide unlimited concurrency, consistent execution environments, and multiplayer collaboration. The critical insight is that session speed should be limited only by model provider time-to-first-token, with all infrastructure setup completed before the user starts their session.

## When to Use

- Building background coding agents that run independently of user devices
- Designing sandboxed execution environments for agent workloads
- Implementing multiplayer agent sessions with shared state
- Creating multi-client agent interfaces (Slack, Web, Chrome extensions)
- Scaling agent infrastructure beyond local machine constraints
- Building systems where agents spawn sub-agents for parallel work

## When NOT to Use

- Coordinating multiple agents with handoffs or supervisor patterns (use multi-agent-patterns)
- Persisting agent state or memory across sessions (use memory-systems)
- Designing individual tools or tool interfaces for agents (use tool-design)
- Running agents locally on a user's machine (not a hosting problem)

## Decision Tree

```
What are you building?
│
├─ Agent runs remotely in sandboxed environment
│  ├─ Need pre-built environment images? → Image Registry Pattern
│  ├─ Need instant session start? → Warm Pool + Predictive Warm-Up
│  └─ Need multiple users in same session? → Multiplayer Support
│
├─ Agent needs to spawn sub-agents
│  ├─ Sub-agents work on same repo? → Self-Spawning with shared state
│  └─ Sub-agents work across repos? → Self-Spawning with API coordination
│
├─ Need multiple client interfaces
│  ├─ Internal team adoption priority? → Slack Integration
│  ├─ Need visual verification? → Web Interface with VS Code
│  └─ Non-engineering users? → Chrome Extension
│
└─ Not sure if hosted or local
   ├─ Need unlimited concurrency? → Hosted
   ├─ Need reproducible environments? → Hosted
   └─ Single user, local dev only? → Local agent (not this skill)
```

## Core Concepts

Hosted agents address the fundamental limitation of local agent execution: resource contention, environment inconsistency, and single-user constraints. By moving agent execution to remote sandboxed environments, teams gain unlimited concurrency, reproducible environments, and collaborative workflows.

The architecture consists of three layers: sandbox infrastructure for isolated execution, API layer for state management and client coordination, and client interfaces for user interaction across platforms. Each layer has specific design requirements that enable the system to scale.

## Detailed Topics

### Sandbox Infrastructure

**The Core Challenge**
Spinning up full development environments quickly is the primary technical challenge. Users expect near-instant session starts, but development environments require cloning repositories, installing dependencies, and running build steps.

**Image Registry Pattern**
Pre-build environment images on a regular cadence (every 30 minutes works well). Each image contains:
- Cloned repository at a known commit
- All runtime dependencies installed
- Initial setup and build commands completed
- Cached files from running app and test suite once

When starting a session, spin up a sandbox from the most recent image. The repository is at most 30 minutes out of date, making synchronization with the latest code much faster.

**Snapshot and Restore**
Take filesystem snapshots at key points:
- After initial image build (base snapshot)
- When agent finishes making changes (session snapshot)
- Before sandbox exit for potential follow-up

This enables instant restoration for follow-up prompts without re-running setup.

**Git Configuration for Background Agents**
Since git operations are not tied to a specific user during image builds:
- Generate GitHub app installation tokens for repository access during clone
- Update git config's `user.name` and `user.email` when committing and pushing changes
- Use the prompting user's identity for commits, not the app identity

**Warm Pool Strategy**
Maintain a pool of pre-warmed sandboxes for high-volume repositories:
- Sandboxes are ready before users start sessions
- Expire and recreate pool entries as new image builds complete
- Start warming sandbox as soon as user begins typing (predictive warm-up)

### Agent Framework Selection

**Server-First Architecture**
Choose an agent framework structured as a server first, with TUI and desktop apps as clients. This enables:
- Multiple custom clients without duplicating agent logic
- Consistent behavior across all interaction surfaces
- Plugin systems for extending functionality
- Event-driven architectures for real-time updates

**Code as Source of Truth**
Select frameworks where the agent can read its own source code to understand behavior. This is underrated in AI development: having the code as source of truth prevents hallucination about the agent's own capabilities.

**Plugin System Requirements**
The framework should support plugins that:
- Listen to tool execution events (e.g., `tool.execute.before`)
- Block or modify tool calls conditionally
- Inject context or state at runtime

### Speed Optimizations

**Predictive Warm-Up**
Start warming the sandbox as soon as a user begins typing their prompt:
- Clone latest changes in parallel with user typing
- Run initial setup before user hits enter
- For fast spin-up, sandbox can be ready before user finishes typing

**Parallel File Reading**
Allow the agent to start reading files immediately, even if sync from latest base branch is not complete:
- In large repositories, incoming prompts rarely modify recently-changed files
- Agent can research immediately without waiting for git sync
- Block file edits (not reads) until synchronization completes

**Maximize Build-Time Work**
Move everything possible to the image build step:
- Full dependency installation
- Database schema setup
- Initial app and test suite runs (populates caches)
- Build-time duration is invisible to users

### Self-Spawning Agents

**Agent-Spawned Sessions**
Create tools that allow agents to spawn new sessions:
- Research tasks across different repositories
- Parallel subtask execution for large changes
- Multiple smaller PRs from one major task

Frontier models are capable of containing themselves. The tools should:
- Start a new session with specified parameters
- Read status of any session (check-in capability)
- Continue main work while sub-sessions run in parallel

**Prompt Engineering for Self-Spawning**
Engineer prompts to guide when agents spawn sub-sessions:
- Research tasks that require cross-repository exploration
- Breaking monolithic changes into smaller PRs
- Parallel exploration of different approaches

### API Layer

**Per-Session State Isolation**
Each session requires its own isolated state storage:
- Dedicated database per session (SQLite per session works well)
- No session can impact another's performance
- Handles hundreds of concurrent sessions

**Real-Time Streaming**
Agent work involves high-frequency updates:
- Token streaming from model providers
- Tool execution status updates
- File change notifications

WebSocket connections with hibernation APIs reduce compute costs during idle periods while maintaining open connections.

**Synchronization Across Clients**
Build a single state system that synchronizes across:
- Chat interfaces
- Slack bots
- Chrome extensions
- Web interfaces
- VS Code instances

All changes sync to the session state, enabling seamless client switching.

### Multiplayer Support

**Why Multiplayer Matters**
Multiplayer enables:
- Teaching non-engineers to use AI effectively
- Live QA sessions with multiple team members
- Real-time PR review with immediate changes
- Collaborative debugging sessions

**Implementation Requirements**
- Data model must not tie sessions to single authors
- Pass authorship info to each prompt
- Attribute code changes to the prompting user
- Share session links for instant collaboration

With proper synchronization architecture, multiplayer support is nearly free to add.

### Authentication and Authorization

**User-Based Commits**
Use GitHub authentication to:
- Obtain user tokens for PR creation
- Open PRs on behalf of the user (not the app)
- Prevent users from approving their own changes

**Sandbox-to-API Flow**
1. Sandbox pushes changes (updating git user config)
2. Sandbox sends event to API with branch name and session ID
3. API uses user's GitHub token to create PR
4. GitHub webhooks notify API of PR events

### Client Implementations

**Slack Integration**
The most effective distribution channel for internal adoption:
- Creates virality loop as team members see others using it
- No syntax required, natural chat interface
- Classify repository from message, thread context, and channel name

Build a classifier to determine which repository to work in:
- Fast model with descriptions of available repositories
- Include hints for common repositories
- Allow "unknown" option for ambiguous cases

**Web Interface**
Core features:
- Works on desktop and mobile
- Real-time streaming of agent work
- Hosted VS Code instance running inside sandbox
- Streamed desktop view for visual verification
- Before/after screenshots for PRs

Statistics page showing:
- Sessions resulting in merged PRs (primary metric)
- Usage over time
- Live "humans prompting" count (prompts in last 5 minutes)

**Chrome Extension**
For non-engineering users:
- Sidebar chat interface with screenshot tool
- DOM and React internals extraction instead of raw images
- Reduces token usage while maintaining precision
- Distribute via managed device policy (bypasses Chrome Web Store)

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Building images on-demand per session | Users wait minutes for environment setup | Use Image Registry Pattern with 30-min cadence pre-builds |
| Blocking file reads until git sync completes | Agent idles while user waits | Allow reads immediately; block only writes until sync finishes |
| Tying sessions to a single author in the data model | Multiplayer becomes impossible | Design authorship as per-prompt metadata, not session-level |
| Attributing commits to the app identity | Audit trail breaks; users see bot commits | Use the prompting user's GitHub identity for all commits |
| Warming sandboxes only on session request | Cold start latency kills adoption | Start warming when user begins typing (predictive warm-up) |
| Supervisor paraphrasing sub-agent responses | "Telephone game" loses fidelity | Implement `forward_message` tool for direct pass-through |
| Tracking sessions or PRs created as the success metric | Volume doesn't equal value | Track merged PRs as the primary metric |
| Storing all sessions in a shared database | Cross-session interference and contention | Use per-session isolated storage (e.g., SQLite per session) |
| Skipping WebSocket hibernation | Idle connections waste compute | Use hibernation APIs to reduce costs during idle periods |

## Practical Guidance

### Follow-Up Message Handling

Decide how to handle messages sent during execution:
- **Queue approach**: Messages wait until current prompt completes
- **Insert approach**: Messages are processed immediately

Queueing is simpler to manage and lets users send thoughts on next steps while agent works. Build mechanism to stop agent mid-execution when needed.

### Metrics That Matter

Track metrics that indicate real value:
- Sessions resulting in merged PRs (primary success metric)
- Time from session start to first model response
- PR approval rate and revision count
- Agent-written code percentage across repositories

### Adoption Strategy

Internal adoption patterns that work:
- Work in public spaces (Slack channels) for visibility
- Let the product create virality loops
- Don't force usage over existing tools
- Build to people's needs, not hypothetical requirements

## Guidelines

1. Pre-build environment images on regular cadence (30 minutes is a good default)
2. Start warming sandboxes when users begin typing, not when they submit
3. Allow file reads before git sync completes; block only writes
4. Structure agent framework as server-first with clients as thin wrappers
5. Isolate state per session to prevent cross-session interference
6. Attribute commits to the user who prompted, not the app
7. Track merged PRs as primary success metric
8. Build for multiplayer from the start; it is nearly free with proper sync architecture

## Integration

This skill builds on multi-agent-patterns for agent coordination and tool-design for agent-tool interfaces. It connects to:

- multi-agent-patterns - Self-spawning agents follow supervisor patterns
- tool-design - Building tools for agent spawning and status checking
- context-optimization - Managing context across distributed sessions
- filesystem-context - Using filesystem for session state and artifacts

## References

Internal reference:
- [Infrastructure Patterns](./references/infrastructure-patterns.md) - Detailed implementation patterns

Related skills in this collection:
- multi-agent-patterns - Coordination patterns for self-spawning agents
- tool-design - Designing tools for hosted environments
- context-optimization - Managing context in distributed systems

External resources:
- [Ramp](https://builders.ramp.com/post/why-we-built-our-background-agent) - Why We Built Our Own Background Agent
- [Modal Sandboxes](https://modal.com/docs/guide/sandbox) - Cloud sandbox infrastructure
- [Cloudflare Durable Objects](https://developers.cloudflare.com/durable-objects/) - Per-session state management
- [OpenCode](https://github.com/sst/opencode) - Server-first agent framework
