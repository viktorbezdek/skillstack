# SkillStack Workflows

> **v2.2.0** | Twenty playbooks that chain SkillStack plugins into multi-stage workflows for real problems -- from debugging a three-hour bug to shipping an API to production.
> 20 workflow skills, no references | 234 trigger evals + 54 output evals (288 total)

## The Problem

Individual skills handle focused tasks well -- writing an API, debugging a race condition, designing a persona. But real projects are rarely one skill deep. Shipping a product needs research, design, build, test, deploy, and monitor. Debugging a complex issue needs hypothesis formation, tests as oracles, blast-radius assessment, and rollback planning. Making a strategic decision needs outcome definition, option generation, risk analysis, and a check that the criteria did not drift during deliberation.

Without workflow guidance, teams face two failure modes. The first is skipping stages: jumping straight from problem to solution without research, building without tests, shipping without review. Each skipped stage creates a debt that surfaces later as a production incident, a wasted sprint, or a decision that looked right at the time but was never stress-tested. The second is stage confusion: doing the right steps in the wrong order (optimizing code before profiling, building an agent before asking "is this even an agent task?"), which wastes effort on work that gets thrown away.

Single skills cannot solve this because they do not know about each other. The API design skill does not know it should hand off to TDD. The debugging skill does not know it should assess blast radius before fixing. The pitch-writing skill does not know it should audit via critical intuition before polishing. Each skill is a chapter; nobody wrote the book.

## Context to Provide

Workflows activate on natural language problem descriptions -- not workflow names. The more context you provide about your situation, the more precisely the right workflow activates and the more useful the phase-by-phase guidance becomes.

**What information to include in your prompt:**
- **What you are trying to accomplish** -- describe the goal, not the process. "I need to ship a REST API" activates `api-to-production`; "I need to run the api workflow" is less effective.
- **Your current state** -- are you starting from scratch or partway through? Workflows can start mid-phase. "I have the design done, now I need tests and deployment" skips to the right starting point.
- **What has already failed or been tried** -- for debugging workflows, include how long you have been stuck and what you have already attempted. For cost optimization, include what optimizations you already made. History determines where to start.
- **Constraints and stakes** -- hard deadlines, compliance requirements, team size, production traffic levels. These affect which gates are strict, which can be skipped, and how much caution to apply.
- **Underlying plugins installed** -- workflows draw on specific SkillStack skills for domain depth. If you know which skills you have installed, mention it; the workflow adapts its depth accordingly.

**What makes results better across workflows:**
- Describing the failure mode you are most worried about (not just what you want to achieve)
- Providing artifact descriptions (API contract, bug description, research notes, existing code) as context rather than abstract descriptions
- Indicating whether you need a full walkthrough or targeted help with a specific phase

**Workflow-specific context:**

| Workflow | Most important context to provide |
|---|---|
| `debug-complex-issue` | How long you've been stuck, what you've already tried, what makes the bug unusual (intermittent, environment-dependent, multi-system) |
| `api-to-production` | API purpose, auth requirements, expected load, existing test infrastructure, deployment target |
| `build-ai-agent` | What problem the agent solves, what tools it needs access to, what "good" output looks like, what failure looks like |
| `llm-cost-optimization` | Current monthly spend, which agents/features drive cost, what quality you cannot compromise |
| `strategic-decision` | The specific options on the table, who makes the final call, what constraints are non-negotiable |
| `product-story-to-ship` | Number of interviews conducted, what you learned, team capacity, timeline to ship |
| `legacy-rescue` | Why the codebase is scary to touch, what happened last time someone changed it, what you need to change now |
| `security-hardening-audit` | What data the system handles, compliance requirements, any known vulnerabilities or past incidents |
| `evaluate-plugin-or-skill` | Whether the input is a plugin or a single SKILL.md, the path or GitHub URL, whether trigger/output evals already exist, who the audience is (you, your team, public marketplace) |

**Template prompt:**
```
I need help with [multi-stage problem description].

Current state: [where you are now -- starting fresh, mid-project, stuck at a specific phase]
What I've already tried / done: [previous attempts, completed phases, decisions already made]
The stakes: [what failure looks like, hard deadlines, compliance requirements, production impact]
My constraints: [team size, timeline, technology choices that are locked in]
Goal: [what done looks like -- shipped to production, risk register ready, decision made, backlog prioritized]

Walk me through the full process.
```

## The Solution

This plugin provides twenty composable workflow playbooks that orchestrate existing SkillStack plugins for multi-stage problems. Each workflow is a self-contained playbook with phase-by-phase guidance, explicit gates (conditions that must be met before proceeding), loops (steps that repeat until a quality bar is met), and references to the underlying skills by name.

The workflows are not programmatic chains -- they are playbooks Claude reads and follows. When you describe a problem that matches a workflow, Claude loads the playbook, follows the phases in order, draws on the underlying skills you have installed for domain depth, respects the gates, and produces the expected output artifacts.

The twenty workflows span engineering (API to production, debugging, legacy rescue, security audit), product (user research to insight, product stories, design review), AI (build an agent, improve an agent, LLM cost optimization, context engineering), strategy (strategic decisions, pitch sprints, stakeholder storytelling), content (content platform build), and meta (build a plugin, update a plugin, evaluate a plugin or skill, write a skill, codebase onboarding).

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Jump from problem to solution, skip research and testing stages | Each workflow enforces the right stages in the right order with gates that prevent skipping |
| Debug for hours with trial-and-error fixes | `debug-complex-issue` enforces observation-before-hypothesis, multi-hypothesis differentiation, and blast-radius assessment |
| Build an agent, iterate on prompts, realize it should not have been an agent | `build-ai-agent` starts with "is this even an agent task?" filter before writing any code |
| Ship an API without tests, reviews, or CI/CD | `api-to-production` gates: contract frozen, tests green, pipeline green before deployment |
| Optimize LLM costs by cutting context, product quality degrades | `llm-cost-optimization` mandatory quality gate rolls back any optimization that degrades output |
| Inherit a legacy codebase, make changes, break production | `legacy-rescue` builds a codemap, adds characterization tests, makes rollback-planned atomic commits |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install skillstack-workflows@skillstack
```

### Prerequisites

The workflows reference specific SkillStack skills by name. Without those skills installed, you get process guidance but not domain depth. Install the underlying plugins for full functionality:

```
/plugin install debugging@skillstack
/plugin install agent-evaluation@skillstack
/plugin install cloud-finops@skillstack
/plugin install code-review@skillstack
/plugin install test-driven-development@skillstack
/plugin install api-design@skillstack
/plugin install tool-design@skillstack
/plugin install memory-systems@skillstack
```

Or install the full SkillStack collection for complete coverage across all 20 workflows.

### Verify installation

After installing, test with:

```
I've been stuck on this race condition for 3 hours -- help me debug it systematically. The bug: our order processing service occasionally creates duplicate orders. It only happens under concurrent load (50+ req/s), never in local or staging. I've checked the database transactions and they look correct. I've already tried adding a unique index but it still happens about 1 in 10,000 requests.
```

## Quick Start

1. Install the plugin with the commands above
2. Describe your problem naturally: `I need to ship a new user management REST API endpoint from design to production deployment. It needs CRUD operations, JWT auth, rate limiting, and must be containerized for our Kubernetes cluster. 2-week deadline, 3-engineer team.`
3. The `api-to-production` workflow activates and walks you through five phases: API design, TDD, code review, CI/CD pipeline, and containerized deployment
4. Follow each phase -- the workflow gates prevent you from deploying before tests pass or skipping code review
5. Next, try: `Our Claude API costs tripled last month -- help me fix it without degrading quality`

---

## System Overview

```
User prompt (multi-stage problem description)
        |
        v
   Skill activation: matches against 20 workflow descriptions
        |
        v
+------------------------------------------------------------------+
|                    Workflow Playbook (SKILL.md)                    |
|  Phase 1 ──gate──> Phase 2 ──gate──> Phase 3 ──gate──> Phase N   |
|     |                 |                 |                 |       |
|     v                 v                 v                 v       |
|  [Skill A]         [Skill B]         [Skill C]         [Skill D] |
|  (installed)       (installed)       (installed)       (installed)|
+------------------------------------------------------------------+

Workflow Types:
  Sequential gates .... linear phases with checkpoints (api-to-production)
  Diagnostic loops .... hypothesis-test-fix cycles (debug-complex-issue)
  Funnels ............. wide intake, successive filtering (build-ai-agent)
  Funnel + gate ....... funnel with mandatory quality gate (llm-cost-optimization)
  Parallel-merge ...... parallel streams that converge (pitch-sprint)
  Layered build ....... load-bearing layer order (content-platform-build)
  Multi-pass audit .... audit everything, then fix (security-hardening-audit)
```

Each workflow is a standalone SKILL.md with its own activation triggers. There are no shared references -- every workflow is self-contained. When activated, the workflow tells Claude to follow phases in order, draw on the underlying skills by name, respect gates, and produce output artifacts at each phase.

## What's Inside

### The 20 Workflows

#### Engineering

| Workflow | Type | What it does |
|---|---|---|
| `api-to-production` | Sequential gates | Design, TDD, code review, CI/CD, containerized deployment. Three gates: contract frozen, tests green, pipeline green. |
| `debug-complex-issue` | Diagnostic loop | Observation-before-hypothesis, family classification, multi-hypothesis differentiation, blast-radius assessment, TDD as debugging oracle. |
| `legacy-rescue` | Safety-net loop | Codemap generation, feedback-center identification, characterization test safety net, rollback-planned atomic commits. |
| `security-hardening-audit` | Multi-pass audit | Threat surface mapping, security-focused code review, edge case analysis, test hardening, remediation. Audit all before fixing any. |
| `onboard-to-codebase` | Ramp-up sequence | Auto-generate codemap, build system model, trace key flows, build context strategy for ongoing work. |

#### Product & Design

| Workflow | Type | What it does |
|---|---|---|
| `user-research-to-insight` | Research funnel | Depth-tiered interview design, pattern-based persona synthesis, stakeholder mapping, journey mapping, narrative presentation. |
| `product-story-to-ship` | PM funnel | Deep interviews, journey mapping, persona definition, measurable outcomes, RICE/MoSCoW prioritized backlog with provenance chains. |
| `design-review-sprint` | Sequential audit | Visual audit, navigation review, copy audit, journey validation, consistency check. Audit top-down, fix bottom-up. |
| `content-platform-build` | 7-layer build | Content model, ontology, consistency standards, navigation, UX copy, examples, tooling. Order is load-bearing. |

#### AI & Agents

| Workflow | Type | What it does |
|---|---|---|
| `build-ai-agent` | 9-phase funnel | "Is this even an agent task?" filter, tool-surface minimization, evaluation pipeline before prompt iteration, production monitoring. |
| `evaluate-and-improve-agent` | Diagnostic loop | Baseline evaluation, architecture diagnosis, pattern redesign, memory integration, re-evaluation against baseline. |
| `llm-cost-optimization` | Funnel + gate | Diagnoses six AI cost anti-patterns, reduces context, compresses, rightsizes models. Non-negotiable quality gate rolls back degrading optimizations. |
| `context-engineering-pipeline` | Diagnostic-fix | Understand context mechanics, optimize capacity, compress, diagnose degradation patterns (lost-in-middle, poisoning), persist to filesystem. |

#### Strategy & Communication

| Workflow | Type | What it does |
|---|---|---|
| `strategic-decision` | Gate-driven | Define outcomes measurably, generate options widely, stress-test for bias, assess downside, rank on original criteria, outcome-gate catches criteria drift. |
| `pitch-sprint` | Parallel-merge | Three parallel streams (interviews, system mapping, persona sharpening) merge into a story spine, audited via critical intuition. 5/3/1-day variants. |
| `storytelling-for-stakeholders` | Narrative build | Structure (3-act, SparkLines, SCR), find the angle, anchor to outcomes, craft and polish. Every beat passes the "so what?" test. |

#### Meta (Building Skills & Plugins)

| Workflow | Type | What it does |
|---|---|---|
| `build-a-plugin` | End-to-end lifecycle | Ideation (7-criteria check), research (marketplace survey), architecture (component decomposition), build (hooks + composition + skills), validation, evaluation. |
| `update-a-plugin` | Five-phase change cycle | Audit current state, classify the change, implement with the right plugin-dev skill, regression-check via re-validation and re-evaluation, version bump and docs update. |
| `evaluate-plugin-or-skill` | Multi-pass audit + verdict | Structural validation, content audit (skill-foundry anti-patterns), trigger and output evals (plugin-evaluation), documentation completeness — aggregated into a single verdict: SHIP, IMPROVE, or REWORK. |
| `write-your-own-skill` | Meta-workflow | Spec first, elicit domain depth, design examples before prose, validate against anti-patterns, ship with structural tests. |

### Component Spotlights

#### debug-complex-issue (workflow skill)

**What it does:** A systematic debugging workflow for bugs that have defeated a first-pass attempt. Enforces observation-before-hypothesis discipline, classifies the bug family (race condition, state machine, environment, LLM, etc.), generates and differentiates multiple hypotheses, assesses blast radius, and uses TDD as a debugging oracle.

**Input -> Output:** You describe a bug you have been stuck on -> You get a phased debugging process with hypothesis ranking, differentiation tests, blast-radius assessment, and a verified fix with regression test.

**When to use:** You have been debugging for more than 30 minutes with no progress, or the bug is intermittent, environment-dependent, or multi-system.
**When NOT to use:** Simple bugs with obvious causes -- just fix them directly.

**Try these prompts:**

```
I've been stuck on this race condition for 3 hours -- help me debug it systematically
```

```
This test passes locally but fails in CI and I can't figure out why
```

```
Users report intermittent 500 errors but I can't reproduce them
```

```
My agent loops forever on certain inputs and I don't know where the cycle starts
```

#### build-ai-agent (workflow skill)

**What it does:** A 9-phase funnel from "I want an agent that does X" to a deployed, evaluated, cost-monitored agent. Critical gate: evaluation pipeline must be in place before prompt iteration begins. Includes the "is this even an agent task?" filter that prevents over-engineering.

**Input -> Output:** You describe what you want an agent to do -> You get a phased build process with task-model fit assessment, tool-surface minimization, evaluation pipeline, prompt iteration with data, and deployment with monitoring.

**When to use:** Building a new agent, or rebuilding an agent that is not performing well.
**When NOT to use:** A simple deterministic script would suffice -- the "is this even an agent task?" filter in Phase 1 will tell you.

**Try these prompts:**

```
I want to build an agent that automates our support ticket triage
```

```
Help me design a coding assistant agent with file access, test running, and git operations
```

```
We need an agent that monitors our production logs and alerts on anomalies
```

```
Should this automation be an agent or a simple script? Help me decide and build it
```

#### llm-cost-optimization (workflow skill)

**What it does:** A funnel-with-gate workflow for reducing LLM costs without degrading quality. Diagnoses six AI cost anti-patterns, optimizes in priority order (prompt caching, context compression, model routing, etc.), and enforces a non-negotiable quality gate that rolls back any optimization that degrades output.

**Input -> Output:** You describe your LLM cost problem -> You get a diagnosis of where money is going, prioritized optimizations, and verified cost reduction with quality preserved.

**When to use:** LLM costs have increased significantly and you need to reduce them without degrading the product.
**When NOT to use:** Costs are reasonable and you want to optimize for performance or capability instead of cost.

**Try these prompts:**

```
Our Claude API costs tripled last month -- help me cut costs without degrading quality
```

```
Which of our agents is the biggest cost driver and what can we do about it?
```

```
We need to reduce LLM spend by 50% before the next board meeting -- where do we start?
```

```
Our agent sends full documents as context on every call -- how do we fix this cost-efficiently?
```

#### strategic-decision (workflow skill)

**What it does:** A gate-driven workflow for high-stakes decisions under uncertainty. Defines outcomes measurably first, generates options widely, stress-tests for bias and hidden assumptions, assesses downside, ranks on original criteria, and uses the outcome-gate to catch criteria drift during deliberation.

**Input -> Output:** You describe a decision with multiple viable options -> You get a structured evaluation with measurable criteria, stress-tested options, and a documented recommendation with rationale.

**Try these prompts:**

```
We need to decide whether to build our own auth system or use a third-party provider
```

```
Should we pivot from B2C to B2B? Help me think through this systematically
```

```
We have three architecture options and strong opinions on each -- help us decide objectively
```

```
Our team is split on whether to rewrite or refactor -- what's the right framework for deciding?
```

#### api-to-production (workflow skill)

**What it does:** Takes an API from design through TDD, code review, CI/CD, and containerized deployment. Three gates: contract frozen before implementation, tests green before review, pipeline green before deployment.

**Input -> Output:** You describe an API you need to ship -> You get a phased build with design, tests, review, pipeline, and deployment -- each gated.

**Try these prompts:**

```
I need to build and ship a new REST API endpoint for user management -- take me from design to production
```

```
Design, build, test, and deploy a GraphQL API for our product catalog
```

```
Help me take this API from prototype to production-ready with proper CI/CD and containerization
```

```
We need a new microservice endpoint -- walk me through the full lifecycle
```

#### legacy-rescue (workflow skill)

**What it does:** A safety-net workflow for making real progress on legacy code without breaking production. Generates a codemap first, identifies feedback centers, adds characterization tests as a safety net, makes rollback-planned atomic commits.

**Input -> Output:** You describe a legacy codebase you need to modify -> You get a codemap, safety net of characterization tests, and a structured approach to making changes with rollback plans.

**Try these prompts:**

```
I inherited a legacy codebase and I'm terrified to touch it -- help me make changes safely
```

```
We need to add a feature to a 10-year-old monolith with no tests
```

```
Help me understand and safely modify this undocumented legacy system
```

```
Our legacy code has no tests and we need to refactor the payment module without downtime
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, may not activate the right workflow) | Good (specific, activates the right workflow) |
|---|---|
| "Help me with my API" | "I need to ship a new REST API from design to production -- walk me through the full lifecycle" |
| "Fix this bug" | "I've been stuck on this race condition for 3 hours -- help me debug it systematically" |
| "Build me an agent" | "I want to build an agent that automates support ticket triage -- walk me from idea to deployed" |
| "Our costs are too high" | "Our Claude API costs tripled after adding three agent features -- help me cut costs without degrading quality" |
| "Review our security" | "Run a systematic security audit across our codebase -- threat surface, code review, edge cases, then remediation" |

### Structured Prompt Templates

**For engineering workflows:**
```
I need to [build / ship / debug / secure / onboard to] [what] -- [context about constraints, timeline, or current state]. Walk me through the full process.
```

**For product workflows:**
```
We [ran N user interviews / have research notes / need to prioritize features]. Help me turn [raw input] into [deliverable: prioritized backlog / personas / journey maps].
```

**For AI/agent workflows:**
```
[I want to build / Our agent is underperforming / Our LLM costs are too high]. [Describe the situation]. Help me [build it right / diagnose and improve / cut costs without degrading quality].
```

**For strategy workflows:**
```
We need to decide between [options]. [Describe the stakes and constraints]. Help me evaluate this systematically so we make the right call.
```

**For meta workflows:**
```
I want to [build a Claude Code plugin / create a skill] for [what it does]. Walk me through the full process from idea to validated artifact.
```

### Prompt Anti-Patterns

- **Asking for a workflow by name instead of describing the problem:** Saying "run the api-to-production workflow" is less effective than describing what you need. The skill activates from natural language problem descriptions, not workflow names.
- **Describing a single-skill problem as a multi-stage workflow:** If the problem fits entirely within one skill (e.g., "design a REST API"), use that skill directly. Workflows add value when the problem spans multiple domains -- design + build + test + deploy.
- **Skipping context about your current state:** "Help me debug this" activates debug-complex-issue, but the workflow is much more effective when you include how long you have been stuck, what you have tried, and what makes the bug unusual. Context determines which phase to start in.
- **Expecting programmatic execution:** These workflows are playbooks Claude follows, not automated chains. If you need programmatic multi-step orchestration (scripts, state machines), use the workflow-automation plugin instead.

## Real-World Walkthrough

You are an engineering manager at a startup. Your team's Claude API bill went from $2,000/month to $6,800/month after adding three new agent features. The CEO asks you to cut costs without degrading product quality.

**Step 1 -- Diagnose the cost surface.** You describe the problem:

```
Our Claude API costs tripled last month after adding three new agent features. Help me cut costs without degrading product quality.
```

The `llm-cost-optimization` workflow activates. It draws on `cloud-finops` to break down costs by agent, model, and token type. You discover Agent C (document analysis) accounts for 60% of cost because it sends entire documents as context on every call. Agent A (search) costs 15% but runs 10x more calls. Agent B (chat) costs 25% with reasonable per-call costs but high volume.

**Step 2 -- Identify anti-patterns.** The workflow checks for six AI cost anti-patterns:
1. Stuffing full documents into context (Agent C -- guilty)
2. Using the most expensive model for everything (all three use Sonnet when Haiku suffices for classification)
3. No prompt caching (Agent A repeats the same system prompt thousands of times)
4. Redundant tool calls (Agent C calls the same tool 3x per conversation)
5. No context compression (Agent B sends full history every turn)
6. No model routing (all tasks go to the same model)

**Step 3 -- Optimize in priority order.** The workflow prioritizes by cost impact:

First: prompt caching for Agent A. The `context-optimization` skill guides cache control headers. Agent A costs drop 75% ($1,020 to $255).

Second: context compression for Agent C. Chunked retrieval with summarization via `context-compression`. Per-call cost drops 80%.

Third: model routing. Classification steps use Haiku. The `agent-project-development` skill provides routing logic. Simple step costs drop 90%.

**Step 4 -- Quality gate (non-negotiable).** Before deploying any optimization, the workflow requires running the test suite and comparing output quality against the pre-optimization baseline using `agent-evaluation`. Prompt caching passes -- responses identical. Context compression passes for 95% of documents but degrades on 50+ page documents -- rolled back for those. Model routing passes for classification but fails for multi-step reasoning -- those stay on Sonnet.

**Step 5 -- Result.** Monthly cost drops from $6,800 to $2,400 (65% reduction). Two sub-optimizations were automatically rolled back by the quality gate. Cost savings validated without degrading product quality.

**Gotchas discovered:** The quality gate caught two optimizations that would have degraded output. Without it, you would have deployed all optimizations and discovered the quality regression from user complaints weeks later.

## Usage Scenarios

### Scenario 1: Shipping an API from scratch to production

**Context:** You need to build a new user management API and ship it to production with proper testing, review, and CI/CD.

**You say:** `I need to build a user management API and ship it to production -- walk me through the full lifecycle`

**The workflow provides:**
- Phase 1: API design with `api-design` -- resource naming, status codes, error contracts
- Phase 2: TDD with `test-driven-development` -- failing tests first, then implementation
- Phase 3: Code review with `code-review` -- security, performance, style, coverage
- Phase 4: CI/CD with `cicd-pipelines` -- build, test, deploy pipeline
- Phase 5: Containerization with `docker-containerization`
- Three gates: contract frozen, tests green, pipeline green

**You end up with:** A production-deployed API with tests, review, CI/CD, and containerized deployment.

### Scenario 2: Onboarding to an unfamiliar codebase

**Context:** You just joined a team and cloned a 200+ file repository with no documentation.

**You say:** `I just cloned this repo and I have no idea how it works -- help me understand it fast`

**The workflow provides:**
- Auto-generated codemap showing structure, dependencies, and entry points
- System model identifying critical paths and high-connectivity modules
- End-to-end trace of 2-3 key flows
- Context strategy for ongoing work

**You end up with:** A mental model compressed from weeks of exploration into one session.

### Scenario 3: Making a high-stakes technical decision

**Context:** Your team needs to choose between PostgreSQL, DynamoDB, and CockroachDB for a new product.

**You say:** `We need to choose our primary database and each option has strong advocates -- help us decide objectively`

**The workflow provides:**
- Measurable criteria definition (latency p99, ops cost, developer velocity)
- Option generation ensuring nothing was prematurely eliminated
- Stress testing of each option's assumptions
- Downside assessment per option
- Criteria-locked ranking that catches drift during discussion

**You end up with:** A documented decision with rationale the team can align behind.

### Scenario 4: Building a Claude Code skill from scratch

**Context:** You want to turn a repeatable workflow into a reusable skill but have never written one.

**You say:** `I want to create a Claude Code skill for database migration reviews`

**The workflow provides:**
- Spec definition (what it does, who uses it, triggers)
- Domain depth elicitation (your migration review methodology)
- Example design before prose (examples become test cases)
- Anti-pattern validation
- Structural tests (frontmatter, trigger evals, output quality)

**You end up with:** A skill that activates reliably with evals that prove it works.

### Scenario 5: Turning user research into a prioritized backlog

**Context:** You completed 12 user interviews and need to go from notes to sprint-ready stories.

**You say:** `We ran 12 user interviews and I need to turn them into a prioritized backlog`

**The workflow provides:**
- Pattern extraction from interviews via `elicitation`
- Journey mapping via `user-journey-design`
- Persona synthesis via `persona-definition`
- Outcome definition via `outcome-orientation`
- RICE/MoSCoW prioritization via `prioritization` with provenance chains

**You end up with:** A prioritized backlog where every story traces to specific research findings.

---

## Decision Logic

**How does the right workflow get activated?**

Each of the 20 workflows has its own SKILL.md with distinct activation triggers in the frontmatter description. When you describe a problem, Claude matches your description against all active skill descriptions. The match is based on natural language similarity, not keywords. Describe the problem you face, not the workflow name.

**When multiple workflows could apply:**

| Your situation | Workflow | Why this one |
|---|---|---|
| Stuck on a bug for 30+ minutes | `debug-complex-issue` | The diagnostic loop with hypothesis differentiation |
| Need to ship an API end-to-end | `api-to-production` | Sequential gates from design to deployment |
| Need to build a new agent | `build-ai-agent` | 9-phase funnel with "is this an agent task?" filter |
| Agent exists but underperforms | `evaluate-and-improve-agent` | Diagnostic loop with baseline comparison |
| LLM costs too high | `llm-cost-optimization` | Funnel with mandatory quality gate |
| Legacy code scares you | `legacy-rescue` | Safety-net with characterization tests |
| Inherited a new codebase | `onboard-to-codebase` | Ramp-up sequence, not safety-net (different from legacy-rescue) |
| High-stakes decision | `strategic-decision` | Gate-driven with criteria-drift detection |
| Need a pitch/deck | `pitch-sprint` | Parallel-merge with time-boxed variants |
| Security review needed | `security-hardening-audit` | Multi-pass: audit all, then fix all |

**What is the difference between `debug-complex-issue` and just using the debugging skill directly?**

The debugging skill provides methodology for systematic root cause analysis. The `debug-complex-issue` workflow wraps that methodology in a structured loop with additional stages: it enforces multi-hypothesis generation (not just the first plausible cause), requires differentiation tests between hypotheses, assesses blast radius before applying fixes, and loops back if the fix does not resolve the issue. Use the skill for straightforward bugs; use the workflow when you have been stuck for 30+ minutes.

**What is the difference between `onboard-to-codebase` and `legacy-rescue`?**

`onboard-to-codebase` is for understanding a codebase you have just joined -- read-only exploration that produces a mental model. `legacy-rescue` is for modifying a codebase you are afraid to touch -- it adds characterization tests and makes rollback-planned changes. If you need to understand but not yet modify, use onboard. If you need to modify safely, use rescue.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Workflow activated but underlying skills not installed | Claude follows the process structure but provides generic guidance instead of domain-depth recommendations | Install the specific SkillStack plugins referenced by the workflow. Each workflow's SKILL.md names the skills it draws on. Install the full SkillStack collection for complete coverage. |
| Wrong workflow activated for the problem | You asked about debugging but the strategic-decision workflow activated, or vice versa | Be more specific in your problem description. Include domain signals: "debugging a race condition" vs "deciding between two architectures." If the wrong workflow persists, explicitly name the workflow: "use the debug-complex-issue workflow." |
| Quality gate in llm-cost-optimization blocks all optimizations | Every optimization degrades output quality and gets rolled back, leaving costs unchanged | The quality gate is working correctly -- it prevents shipping degraded quality. The problem is that your current approach requires expensive processing. Look for structural changes (different architecture, different prompting strategy) rather than surface-level cost cuts. |
| Workflow feels too rigid for the problem | The phased structure does not match how the problem actually unfolds -- some phases are irrelevant or the order needs adjustment | Workflows are playbooks, not chains. Tell Claude "skip Phase 3 -- we already have tests" or "start at Phase 4 -- the design is done." The gates still apply, but phases can be reordered or skipped when the situation warrants it. |
| Diagnostic loop does not converge | debug-complex-issue or evaluate-and-improve-agent keeps looping without resolving the issue after 3+ iterations | The loop should converge within 3 iterations. If it does not, the problem is likely misclassified. Step back and re-classify: is this really a race condition, or is it a state machine bug? Is the agent architecture fundamentally wrong, or is it a prompt issue? Reclassification often unlocks the solution. |

## Ideal For

- **Teams facing multi-stage problems** -- the workflows enforce the right stages in the right order, preventing the "skip testing and ship" impulse
- **Engineers debugging complex issues** -- the diagnostic loop prevents trial-and-error fixes by enforcing hypothesis formation and blast-radius assessment
- **Product managers turning research into action** -- the funnel workflows connect user interviews to prioritized backlogs with provenance chains
- **AI engineers building and optimizing agents** -- the agent workflows include critical gates (evaluation before iteration, quality gates on cost optimization) that prevent common mistakes
- **Leaders making high-stakes decisions** -- the gate-driven decision workflow prevents criteria drift and stress-tests hidden assumptions
- **Anyone inheriting an unfamiliar codebase** -- the onboarding workflow compresses weeks of exploration into one structured session

## Not For

- **Single-skill tasks** -- if the problem fits cleanly inside one skill's domain, use that skill directly. Workflows are for problems that span multiple domains.
- **Reversible experiments** -- if you can try something cheaply and see what happens, just experiment. Workflows add structure for when the stakes are high.
- **You have not installed the underlying plugins** -- the workflows reference specific skills by name. Without them, you get process guidance but not domain depth.
- **Programmatic multi-step orchestration** -- these are playbooks Claude follows, not automated chains. For programmatic orchestration, use the [workflow-automation](../workflow-automation/) plugin.

## Version History

- `2.0.0` Added 9 new workflows: build-a-plugin, api-to-production, security-hardening-audit, onboard-to-codebase, product-story-to-ship, context-engineering-pipeline, design-review-sprint, evaluate-and-improve-agent, storytelling-for-stakeholders
- `1.0.0` Initial release with 9 composition workflows

## Related Plugins

- **[Plugin Dev](../plugin-dev/)** -- Full plugin authoring toolkit referenced by `build-a-plugin`
- **[Workflow Automation](../workflow-automation/)** -- Programmatic multi-step orchestration (not playbook-style)
- **[Debugging](../debugging/)** -- Single debugging skill that `debug-complex-issue` wraps in a structured loop
- **[Agent Evaluation](../agent-evaluation/)** -- Evaluation framework that `build-ai-agent` and `evaluate-and-improve-agent` draw on
- **[Cloud FinOps](../cloud-finops/)** -- Cost analysis that `llm-cost-optimization` uses for diagnosing spend
- All 32+ SkillStack skills referenced by the workflows -- install them for domain depth

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
