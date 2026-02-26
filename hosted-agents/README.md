# Hosted Agent Infrastructure

> Infrastructure patterns for hosted background agents. Sandbox environments, image registry pattern, self-spawning agents, multiplayer support, warm pools, and multi-client integration (Slack, web, Chrome).

## Overview

Hosted agents run in remote sandboxed environments rather than on local machines. When designed well, they provide unlimited concurrency, consistent execution environments, and multiplayer collaboration. The critical insight is that session speed should be limited only by model provider time-to-first-token, with all infrastructure setup (repository cloning, dependency installation, build steps) completed before the user starts their session.

This skill covers the full infrastructure stack for hosted agent systems. The sandbox layer handles pre-built environment images, snapshot/restore for instant session creation, and warm pool strategies for high-volume repositories. The API layer manages per-session state isolation, real-time streaming via WebSockets, and cross-client synchronization. The client layer implements Slack bots, web interfaces with embedded VS Code, and Chrome extensions for non-engineering users. The skill also covers self-spawning agents that create sub-sessions for parallel work.

Within the SkillStack collection, Hosted Agents builds on Multi-Agent Patterns for self-spawning agent coordination and Tool Design for agent-tool interfaces. It connects to Context Optimization for managing context across distributed sessions and Filesystem Context for using the filesystem as session state and artifact storage.

## What's Included

### Skill

- `skills/hosted-agents/SKILL.md` -- Core infrastructure patterns covering sandbox setup, image registry, warm pools, speed optimizations, self-spawning agents, API layer design, multiplayer support, authentication, and multi-client implementations

### References

- **infrastructure-patterns.md** -- Detailed implementation patterns for sandbox infrastructure, API layer, and client integration

## Key Features

- **Image registry pattern** pre-building environment images every 30 minutes with cloned repositories, installed dependencies, and cached builds, so sessions start near-instantly
- **Warm pool strategy** maintaining pre-warmed sandboxes for high-volume repositories with predictive warm-up that begins when users start typing
- **Snapshot and restore** at key points (after image build, after agent changes, before exit) enabling instant restoration for follow-up prompts
- **Self-spawning agents** with tools to start new sessions, check status, and continue work while sub-sessions run in parallel for research or large changes
- **Multiplayer support** where multiple team members collaborate in real-time on the same agent session with proper authorship attribution
- **Multi-client architecture** supporting Slack bots (virality through visibility), web interfaces (with embedded VS Code), and Chrome extensions (DOM extraction for non-engineers)
- **Speed optimizations** including parallel file reading before git sync completes, maximizing build-time work, and predictive sandbox warm-up
- **Authentication flow** using GitHub tokens so PRs are opened on behalf of users (not the app), preventing self-approval of agent-written code

## Usage Examples

Set up hosted agent infrastructure:
```
I want to build a background coding agent that runs in sandboxed environments. Help me design the infrastructure: image registry for fast startup, sandbox management, and real-time streaming to a web frontend.
```

Implement self-spawning agents:
```
My agent needs to research code across 3 repositories and then make coordinated changes. Design a self-spawning architecture where the main agent creates sub-sessions for each repository and aggregates results.
```

Add Slack integration for team adoption:
```
We want our coding agent accessible through Slack. Help me implement repository classification from channel context, threading for multi-turn sessions, and proper user attribution for commits.
```

Design multiplayer agent sessions:
```
Our team wants to collaboratively debug using a shared agent session. Implement multiplayer support where multiple users can prompt the same agent, with each user's contributions properly attributed.
```

## Quick Start

1. **Set up image registry**: Build environment images every 30 minutes containing cloned repositories, installed dependencies, and cached builds.
2. **Implement warm pools**: Maintain pre-warmed sandboxes for your most-used repositories; start warming when users begin typing.
3. **Design API layer**: Isolate state per session (SQLite per session), stream updates via WebSockets, and synchronize across clients.
4. **Add authentication**: Use GitHub app tokens for clone during build, user tokens for PR creation, and attribute commits to the prompting user.
5. **Track merged PRs** as your primary success metric -- this measures actual value delivered, not just sessions started.

## Related Skills

- **multi-agent-patterns** -- Self-spawning agents follow supervisor patterns with sub-agent coordination
- **tool-design** -- Building tools for agent spawning, status checking, and hosted environment interaction
- **context-optimization** -- Managing context across distributed sessions and parallel sub-agents
- **filesystem-context** -- Using the filesystem for session state, artifacts, and sub-agent communication
- **agent-evaluation** -- Measuring hosted agent effectiveness through merged PR rates and code quality metrics

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install hosted-agents@skillstack` — 46 production-grade plugins for Claude Code.
