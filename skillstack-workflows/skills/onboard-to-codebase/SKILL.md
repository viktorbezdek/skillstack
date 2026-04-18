---
name: onboard-to-codebase
description: Ramp-up workflow for understanding a new codebase fast — onboard to codebase, understand a repo, grok a project, ramp up on code. Generates a codemap so the structure is visible before you read any implementation (documentation-generator), then builds a system model of dependencies, feedback loops, and critical paths so you know which parts matter (systems-thinking), then traces key flows end-to-end through the code so you see how the pieces connect in practice (debugging), and finally builds a context strategy so you know what to keep in working memory and what to look up on demand (context-fundamentals). Use when joining a new team, inheriting a codebase, onboarding an AI agent to a repo, or switching projects and needing productive orientation in hours instead of weeks. NOT for codebases you already know well — skip straight to the relevant skill instead.
---

# Onboard to Codebase

> Understanding a codebase is not reading files from top to bottom. It's building a mental model that lets you predict where a change should go and what it will affect — before you read the implementation.

New developers read code. Effective developers build models. The difference between "I've read the code" and "I understand the system" is the difference between having a map and having a mental simulation. This workflow builds the simulation.

---

## When to use this workflow

- You just cloned a repo and need to be productive fast
- Joining a new team and inheriting an existing codebase
- Onboarding an AI agent to a project it hasn't seen before
- Switching projects after months away and needing to rebuild context
- Preparing to make your first meaningful contribution to an open-source project

## When NOT to use this workflow

- **You already know the codebase** — skip to the specific skill you need
- **The codebase is trivial** — a 200-line script doesn't need four phases
- **You're doing a code review, not onboarding** — use `code-review` directly
- **You need to fix a specific bug right now** — use `debug-complex-issue`; onboarding can wait

---

## Prerequisites

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install documentation-generator@skillstack
/plugin install systems-thinking@skillstack
/plugin install debugging@skillstack
/plugin install context-fundamentals@skillstack
```

---

## Core principle

**Structure before detail.** The single biggest time-sink in onboarding is diving into implementation before understanding architecture. A developer who spends 30 minutes building a codemap before reading any function will outperform a developer who starts reading `main.ts` line by line — because the first developer knows which functions matter and the second doesn't.

Secondary principle: **trace flows, don't catalog files.** A file listing tells you what exists. A traced flow tells you how things work. The flow is what you need to make changes safely.

---

## The phases

### Phase 1 — generate the codemap (documentation-generator)

Load the `documentation-generator` skill with codemap intent. Before reading any implementation code, produce a structural map:

- **Module inventory** — what major modules/packages exist, what each one owns
- **Entry points** — where does execution start? HTTP handlers, CLI commands, event consumers, scheduled jobs, main functions
- **Dependency graph** — which modules depend on which. Direction matters: A imports B is different from B imports A
- **External boundaries** — what APIs does this system call? What databases, queues, caches, third-party services?
- **Configuration surface** — environment variables, config files, feature flags. These are often the hidden inputs that change behavior
- **Build and deploy** — how is this thing built, tested, and shipped? CI config, Dockerfile, deploy scripts

Output: a codemap document. Not a full documentation set — just the structural skeleton that makes Phase 2 possible.

The codemap is an investment. Every minute spent here saves ten minutes of confused file-hopping later.

### Phase 2 — build the system model (systems-thinking)

Load the `systems-thinking` skill. Using the codemap from Phase 1, build a model of the system as a living thing, not a static structure:

- **Dependency analysis** — which modules are structural hubs (high in-degree)? Which are leaves? Hubs are where changes ripple; leaves are where changes stay local.
- **Feedback loops** — does the system have loops where output feeds back as input? Examples: caching layers that affect what gets cached, retry logic that amplifies failures, auto-scaling that responds to its own load.
- **Critical paths** — for the main use cases, what's the end-to-end path from user action to system response? Which modules are on every critical path (and therefore the riskiest to change)?
- **Failure modes** — where does the system fail gracefully? Where does it cascade? A database timeout that brings down the whole service is a cascade; one that shows a fallback is graceful.
- **Bottlenecks** — what constrains throughput? Database queries, external API rate limits, single-threaded processing, shared locks.

Output: a system model — a mental picture of how the parts interact, not just what the parts are.

The key insight: modules with high in-degree AND on critical paths are the ones you must understand deeply. Everything else you can learn on demand.

### Phase 3 — trace key flows (debugging)

Load the `debugging` skill — not to fix bugs, but to use its trace-and-observe discipline for understanding.

Pick the 3-5 most important flows in the system (the critical paths from Phase 2) and trace each one end-to-end:

- **Follow the data** — for each flow, start at the entry point and follow the data through every function, transformation, and storage operation until it reaches the output. Note where data is transformed, validated, enriched, cached, or dropped.
- **Identify the seams** — where are the boundaries between modules? Where does control pass from one concern to another? These seams are where bugs tend to live and where changes tend to be needed.
- **Note the surprising parts** — every codebase has at least one "wait, why does it do THAT?" moment. Write these down. They're either bugs, historical workarounds, or domain logic you don't understand yet. All three are important.
- **Run it** — if possible, run the system and trigger each flow while watching logs, debugger, or network traffic. Reading code tells you what should happen; running it tells you what actually happens.

Output: a traced-flows document — for each major flow, the path through the code with annotations on seams, surprises, and failure points.

This is the phase that transforms "I've seen the files" into "I know how it works."

### Phase 4 — build a context strategy (context-fundamentals)

Load the `context-fundamentals` skill. Now that you have the codemap, system model, and traced flows, decide what to keep in working memory and what to look up on demand:

- **Always-loaded context** — the codemap, the system model, the critical-path traces. These are your orientation anchors. If you lose these, you lose your bearings.
- **On-demand context** — implementation details of specific modules. You don't need to remember how the auth middleware works until you're changing it.
- **Disposable context** — one-off explorations, dead-end investigations, historical code that's been replaced. Let these go.
- **Context entry points** — for each major area of the codebase, know the ONE file to start reading. Not the whole module — just the entry file. From there, you can navigate.

For AI agents specifically:
- **What goes in the system prompt** — the codemap and system model (structure, not implementation)
- **What goes in retrieval** — implementation details, pulled in when relevant
- **What gets summarized** — long explorations that yielded a conclusion (keep the conclusion, drop the exploration)

Output: a context strategy — what to keep close, what to retrieve, what to forget. This is the mental model that makes you productive, not the code itself.

---

## Decision Tree

```
Why are you onboarding?
│
├─ Joining a new team / inherited a codebase
│   └─ Run all 4 phases sequentially
│
├─ Switching back after months away
│   └─ Phase 1 (codemap) → Phase 2 (model) only — skip if prior model exists
│
├─ Onboarding an AI agent to the repo
│   └─ Phase 1 → Phase 4 (context strategy) — agent needs structure, not flows
│
├─ Preparing to contribute to open source
│   └─ Phase 1 → Phase 3 (trace the contribution flow) → Phase 4
│
└─ The codebase is trivial (<200 lines)
    └─ Skip this workflow — read the code directly
```

## Anti-Patterns

| # | Anti-Pattern | Symptom | Fix |
|---|---|---|---|
| 1 | **Reading files top-to-bottom** | You've read 50 files but can't explain how a request flows through the system | Build the codemap first (Phase 1), then trace flows (Phase 3). Structure before detail. |
| 2 | **Diving into the most complex module first** | Deep knowledge of one module, zero context on the rest | Phase 1 forces breadth. Only go deep in Phase 3 on critical-path modules. |
| 3 | **Building the model from static code only** | Your model misses feature flags, dynamic dispatch, config-driven behavior | Phase 3 includes "run it." Execute the system and observe actual behavior. |
| 4 | **Trying to learn everything** | A week passes with no contribution | Phase 4's context strategy explicitly identifies what to forget. Ship what matters. |
| 5 | **Skipping the codemap and going straight to tracing** | You trace flows but miss that the most important module wasn't on your list | Gate 1 enforces: no Phase 2 without Phase 1 output. |

## Gates and failure modes

**Gate 1: the codemap gate.** Phase 2 cannot start until Phase 1's codemap exists. Building a system model without knowing what modules exist is speculation.

**Gate 2: the model gate.** Phase 3 cannot start until Phase 2 has identified the critical paths. Tracing random flows is busywork; tracing critical paths is understanding.

**Gate 3: the trace gate.** Phase 4 cannot start until at least 3 key flows have been traced. A context strategy built on untested assumptions about how the code works is a context strategy that will mislead.

**Failure mode: premature depth.** You start reading the most complex module first because it looks interesting. Three hours later you understand one module deeply and the rest not at all. Mitigation: Phase 1 forces breadth before depth.

**Failure mode: passive reading.** You read files sequentially without building a model. After reading 50 files you can't explain how a request flows through the system. Mitigation: Phase 3 forces active tracing.

**Failure mode: ignoring the runtime.** You build a model from static code analysis. The code has feature flags, dynamic dispatch, or configuration that changes behavior at runtime. Your model is wrong. Mitigation: Phase 3's "run it" step.

**Failure mode: trying to learn everything.** You spend a week reading every file before making any change. Mitigation: Phase 4's context strategy explicitly identifies what to forget.

---

## Output artifacts

A completed onboarding produces:

1. **A codemap** — module inventory, dependency graph, entry points, external boundaries
2. **A system model** — feedback loops, critical paths, bottlenecks, failure modes
3. **Traced flows** — 3-5 critical paths traced end-to-end with annotations
4. **A context strategy** — what to keep loaded, what to retrieve, what to forget
5. **A surprises list** — things that were unexpected, for follow-up investigation

The context strategy is the real deliverable. Everything else feeds into it.

---

## Related workflows and skills

- For making changes to a legacy codebase after onboarding, use the `legacy-rescue` workflow
- For debugging a specific issue you found during onboarding, use the `debug-complex-issue` workflow
- For presenting what you learned to the team, use `documentation-generator` to turn the codemap into permanent docs
- For optimizing context when onboarding an AI agent, use the `context-engineering-pipeline` workflow after this one

---

> *SkillStack Workflows by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
