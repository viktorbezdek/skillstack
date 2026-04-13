# SkillStack Workflows

> **v2.0.0** | Strategic Thinking | Composable workflow playbooks

> Eighteen playbooks that chain SkillStack plugins into multi-stage workflows for real problems -- from debugging a three-hour bug to shipping an API to production.

## The Problem

Individual skills handle focused tasks well -- writing an API, debugging a race condition, designing a persona. But real projects are rarely one skill deep. Shipping a product needs research, design, build, test, deploy, and monitor. Debugging a complex issue needs hypothesis formation, tests as oracles, blast-radius assessment, and rollback planning. Making a strategic decision needs outcome definition, option generation, risk analysis, and a check that the criteria did not drift during deliberation.

Without workflow guidance, teams face two failure modes. The first is skipping stages: jumping straight from problem to solution without research, building without tests, shipping without review. Each skipped stage creates a debt that surfaces later as a production incident, a wasted sprint, or a decision that looked right at the time but was never stress-tested. The second is stage confusion: doing the right steps in the wrong order (optimizing code before profiling, building an agent before asking "is this even an agent task?"), which wastes effort on work that gets thrown away.

Single skills cannot solve this because they do not know about each other. The API design skill does not know it should hand off to TDD. The debugging skill does not know it should assess blast radius before fixing. The pitch-writing skill does not know it should audit via critical intuition before polishing. Each skill is a chapter; nobody wrote the book.

## The Solution

This plugin provides eighteen composable workflow playbooks that orchestrate existing SkillStack plugins for multi-stage problems. Each workflow is a self-contained playbook with phase-by-phase guidance, explicit gates (conditions that must be met before proceeding), loops (steps that repeat until a quality bar is met), and references to the underlying skills by name.

The workflows are not programmatic chains -- they are playbooks Claude reads and follows. When you describe a problem that matches a workflow, Claude loads the playbook, follows the phases in order, draws on the underlying skills you have installed for domain depth, respects the gates, and produces the expected output artifacts.

The eighteen workflows span engineering (API to production, debugging, legacy rescue, security audit), product (user research to insight, product stories, design review), AI (build an agent, improve an agent, LLM cost optimization, context engineering), strategy (strategic decisions, pitch sprints, stakeholder storytelling), content (content platform build), and meta (build a plugin, write a skill, codebase onboarding).

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

Or install the full SkillStack collection for complete coverage across all 18 workflows.

### Verify installation

After installing, test with:

```
I've been stuck on this race condition for 3 hours -- help me debug it systematically
```

## Quick Start

1. Install the plugin with the commands above
2. Describe your problem naturally: `I need to ship a new REST API endpoint from design to production deployment`
3. The `api-to-production` workflow activates and walks you through five phases: API design, TDD, code review, CI/CD pipeline, and containerized deployment
4. Follow each phase -- the workflow gates prevent you from deploying before tests pass or skipping code review
5. Next, try: `Our Claude API costs tripled last month -- help me fix it without degrading quality`

## What's Inside

This is a **multi-skill plugin** with 18 independently-activating workflow skills and 288 eval cases across all workflows. No reference documents -- each workflow is self-contained in its SKILL.md.

### The 18 Workflows

#### Engineering

| Workflow | Type | What it does |
|---|---|---|
| `api-to-production` | Sequential gates | Design, TDD, code review, CI/CD, containerized deployment. Three gates: contract frozen, tests green, pipeline green. |
| `debug-complex-issue` | Diagnostic loop | Observation-before-hypothesis, family classification, multi-hypothesis differentiation, blast-radius assessment, TDD as debugging oracle. |
| `legacy-rescue` | Safety-net loop | Codemap generation, feedback-center identification, characterization test safety net, rollback-planned atomic commits, debugging loops for surprises. |
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
| `pitch-sprint` | Parallel-merge | Three parallel streams (interviews, system mapping, persona sharpening) merge into a story spine, audited via critical intuition, polished via UX writing. 5/3/1-day variants. |
| `storytelling-for-stakeholders` | Narrative build | Structure (3-act, SparkLines, SCR), find the angle, anchor to outcomes, craft and polish. Every beat passes the "so what?" test. |

#### Meta (Building Skills & Plugins)

| Workflow | Type | What it does |
|---|---|---|
| `build-a-plugin` | End-to-end lifecycle | Ideation (7-criteria check), research (marketplace survey), architecture (component decomposition), build (hooks + composition + skills), validation, evaluation. Three gates prevent wasted work. |
| `write-your-own-skill` | Meta-workflow | Spec first, elicit domain depth, design examples before prose, validate against anti-patterns, ship with structural tests. |

### How the Workflows Work

Each workflow skill has its own frontmatter with specific activation triggers. When you describe a problem, Claude matches it against all active skills' descriptions and activates the best match. Once activated, the workflow's SKILL.md tells Claude to:

1. Follow the phase-by-phase process in order
2. Draw on the underlying skills you have installed (explicitly referenced by name in each phase)
3. Respect the gates (conditions that must be met before proceeding to the next phase)
4. Respect the loops (steps that repeat until a quality bar is met)
5. Produce the expected output artifacts at each phase

### pitch-sprint

**What it does:** A time-boxed sprint for producing a pitch -- investor deck, board proposal, internal funding request, or customer sales narrative. Three parallel streams (interviews, system mapping, persona sharpening) merge into a narrative spine using StoryBrand, Pixar Spine, or founder-story structures. Audited via critical intuition, polished via UX writing. Available in 5-day, 3-day, and 1-day variants.

**Try these prompts:**

```
Help me write a pitch for our Series A meeting next week -- we're a developer tools company
```

```
I need to present our quarterly results to the board in 3 days -- help me build the narrative
```

```
Create a compelling customer case study for our enterprise sales deck
```

```
We're pitching internally for headcount -- help me build the business case
```

### debug-complex-issue

**What it does:** A systematic debugging workflow for bugs that have defeated a first-pass attempt. Enforces observation-before-hypothesis discipline, classifies the bug family (race condition, state machine, environment, LLM, etc.), generates and differentiates multiple hypotheses, assesses blast radius, and uses TDD as a debugging oracle.

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

### build-ai-agent

**What it does:** A 9-phase funnel from "I want an agent that does X" to a deployed, evaluated, cost-monitored agent. Critical gate: evaluation pipeline before prompt iteration. Includes the "is this even an agent task?" filter and tool-surface minimization to prevent over-engineering.

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

### strategic-decision

**What it does:** A gate-driven workflow for making high-stakes decisions under uncertainty when multiple options have merit. Defines outcomes measurably first, generates options widely, stress-tests for bias and hidden assumptions, assesses downside, ranks on original criteria, and uses the outcome-gate to catch criteria drift during deliberation.

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

### api-to-production

**What it does:** Takes an API from design through TDD, code review, CI/CD, and containerized deployment. Three gates prevent premature progression: contract must be frozen before implementation, tests must be green before review, pipeline must be green before deployment.

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

### legacy-rescue

**What it does:** A safety-net workflow for making real progress on legacy code without breaking production. Generates a codemap first, identifies feedback centers (high-connectivity modules), adds characterization tests as a safety net, makes rollback-planned atomic commits, and runs debugging loops for surprises.

**Try these prompts:**

```
I inherited a legacy codebase and I'm terrified to touch it -- help me make changes safely
```

```
We need to add a feature to a 10-year-old monolith with no tests -- how do I not break everything?
```

```
Help me understand and safely modify this undocumented legacy system
```

```
Our legacy code has no tests and we need to refactor the payment module without downtime
```

## Real-World Walkthrough

You are an engineering manager at a startup. Your team's Claude API bill went from $2,000/month to $6,800/month after adding three new agent features. The CEO asks you to cut costs without degrading the product quality that users have been praising in reviews. You have no idea where to start -- cutting context might break the features, switching to a smaller model might reduce quality, and you do not know which agent is the biggest spender.

You describe the problem:

```
Our Claude API costs tripled last month after adding three new agent features. Help me cut costs without degrading product quality.
```

The `llm-cost-optimization` workflow activates. It is a funnel-with-gate design: diagnose first, optimize in priority order, and enforce a non-negotiable quality gate that rolls back any optimization that degrades output.

**Phase 1: Diagnose the cost surface.** The workflow draws on the `cloud-finops` skill to break down costs by agent, model, and token type (input vs output). You discover that Agent C (the document analysis agent) accounts for 60% of total cost because it sends entire documents as context on every call. Agent A (the search agent) costs 15% but runs 10x more calls. Agent B (the chat agent) costs 25% with reasonable per-call costs but high volume.

**Phase 2: Identify anti-patterns.** The workflow checks for six AI cost anti-patterns:
1. Stuffing full documents into context (Agent C -- guilty)
2. Using the most expensive model for everything (all three agents use Claude Sonnet when Haiku would suffice for classification steps)
3. No prompt caching (Agent A makes the same system prompt call thousands of times without caching)
4. Redundant tool calls (Agent C calls the same tool 3x per conversation due to context loss)
5. No context compression (Agent B sends full conversation history on every turn)
6. No model routing (all tasks go to the same model regardless of complexity)

**Phase 3: Optimize in priority order.** The workflow prioritizes optimizations by cost impact:

First, enable prompt caching for Agent A. The `context-optimization` skill guides you through adding cache control headers to the system prompt. This alone cuts Agent A's costs by 75% (from $1,020 to $255) because the system prompt is identical across calls.

Second, add context compression for Agent C. Instead of sending full documents, the `context-compression` skill helps you implement chunked retrieval with summarization. Agent C's per-call cost drops by 80%.

Third, implement model routing. Classification and extraction steps use Haiku instead of Sonnet. The `agent-project-development` skill provides the routing logic. This cuts per-call cost for simple steps by 90%.

**Phase 4: Quality gate (non-negotiable).** Before deploying any optimization, the workflow requires running your existing test suite and comparing output quality against the pre-optimization baseline. The gate uses the `agent-evaluation` skill to measure output quality on a held-out set of real conversations.

The prompt caching optimization passes easily -- responses are identical. The context compression optimization passes for 95% of documents but degrades quality on documents longer than 50 pages. The workflow rolls back compression for long documents and keeps it for shorter ones. The model routing passes for classification (Haiku performs identically to Sonnet on binary choices) but fails for multi-step reasoning tasks -- those stay on Sonnet.

**Result:** Your monthly cost drops from $6,800 to $2,400 -- a 65% reduction. The quality gate ensured that every optimization was validated before deployment, and two sub-optimizations were automatically rolled back because they degraded output quality. The CEO gets cost savings; users get the same product quality.

## Usage Scenarios

### Scenario 1: Shipping an API from scratch to production

**Context:** You are a backend engineer tasked with building a new user management API endpoint. You need to design, implement, test, review, and deploy it -- and you want to do every step right.

**You say:** `I need to build a user management API and ship it to production -- walk me through the full lifecycle`

**The workflow provides:**
- Phase 1: API design with `api-design` -- resource naming, status codes, error contracts
- Phase 2: TDD with `test-driven-development` -- failing tests first, then implementation
- Phase 3: Code review with `code-review` -- security, performance, style, test coverage
- Phase 4: CI/CD with `cicd-pipelines` -- pipeline configuration for build, test, deploy
- Phase 5: Containerization with `docker-containerization` -- Dockerfile, compose, deployment
- Three gates: contract frozen, tests green, pipeline green

**You end up with:** A production-deployed API with tests, code review, CI/CD pipeline, and containerized deployment -- not a prototype that "works on my machine."

### Scenario 2: Onboarding to an unfamiliar codebase

**Context:** You just joined a team and cloned a repository with 200+ files, no documentation, and a build system you have never used. You need to understand it well enough to contribute within a week.

**You say:** `I just cloned this repo and I have no idea how it works -- help me understand it fast`

**The workflow provides:**
- Phase 1: Auto-generated codemap showing file structure, dependencies, and entry points
- Phase 2: System model identifying feedback loops, critical paths, and high-connectivity modules
- Phase 3: End-to-end trace of 2-3 key flows (e.g., request lifecycle, data pipeline)
- Phase 4: Context strategy for ongoing work -- what to read first, what to keep in mind, what to look up

**You end up with:** A mental model of the codebase that would normally take 2-3 weeks of exploration, compressed into one structured session.

### Scenario 3: Making a high-stakes technical decision

**Context:** Your startup needs to decide between three database options (PostgreSQL, DynamoDB, CockroachDB) for a new product, and the decision will be expensive to reverse. Each option has vocal advocates on the team.

**You say:** `We need to choose our primary database and each option has strong advocates -- help us decide objectively`

**The workflow provides:**
- Outcome definition: what measurable criteria matter (latency p99, ops cost, developer velocity, migration effort)
- Option generation: ensures no options were prematurely eliminated
- Stress testing: challenges each option's assumptions and identifies hidden risks
- Downside assessment: what is the worst case for each option
- Criteria-locked ranking: ranks options against the original criteria, catching any drift that occurred during discussion

**You end up with:** A documented decision with rationale that the team can align behind, plus a clear record of what was considered and why alternatives were rejected.

### Scenario 4: Building a Claude Code skill from scratch

**Context:** You have a repeatable workflow that you want to turn into a reusable Claude Code skill, but you have never written one before and want it to actually activate reliably.

**You say:** `I want to create a Claude Code skill for database migration reviews -- walk me through the process`

**The workflow provides:**
- Spec first: define what the skill does, who uses it, and what triggers it
- Domain depth: elicit the migration review methodology you currently apply manually
- Example design: create examples before writing prose (the examples become the test cases)
- Anti-pattern validation: check the SKILL.md against known anti-patterns
- Structural tests: validate frontmatter, trigger evals, and output quality

**You end up with:** A skill that activates reliably for migration review queries, with evals that prove it works and a validated structure that will not break on installation.

### Scenario 5: Turning user research into a prioritized backlog

**Context:** You are a product manager who just completed 12 user interviews. You have pages of notes but no clear path from research to engineering stories.

**You say:** `We ran 12 user interviews and I need to turn them into a prioritized backlog -- help me go from notes to sprint-ready stories`

**The workflow provides:**
- Interview analysis with `elicitation` -- extract patterns, pain points, and unmet needs
- Journey mapping with `user-journey-design` -- map the end-to-end experience with friction points
- Persona synthesis with `persona-definition` -- build data-grounded personas from the interview patterns
- Outcome definition with `outcome-orientation` -- convert pain points to measurable outcomes
- Prioritization with `prioritization` -- RICE or MoSCoW scoring with provenance chains back to the original research

**You end up with:** A prioritized backlog where every story traces back to specific user research findings, not product team assumptions.

## Ideal For

- **Teams facing multi-stage problems** -- the workflows enforce the right stages in the right order, preventing the "skip testing and ship" impulse
- **Engineers debugging complex issues** -- the diagnostic loop prevents trial-and-error fixes by enforcing hypothesis formation and blast-radius assessment
- **Product managers turning research into action** -- the funnel workflows connect user interviews to prioritized backlogs with provenance chains
- **AI engineers building and optimizing agents** -- the agent workflows include critical gates (evaluation before iteration, quality gates on cost optimization) that prevent common mistakes
- **Leaders making high-stakes decisions** -- the gate-driven decision workflow prevents criteria drift and stress-tests hidden assumptions
- **Anyone inheriting an unfamiliar codebase** -- the onboarding workflow compresses weeks of exploration into one structured session

## Not For

- **Single-skill tasks** -- if the problem fits cleanly inside one skill's domain, use that skill directly. These workflows are for problems that span multiple domains.
- **Reversible experiments** -- if you can try something cheaply and see what happens, just experiment. Workflows add structure for when the stakes are high.
- **You have not installed the underlying plugins** -- the workflows reference specific SkillStack skills by name. Without them, you get process guidance but not domain depth.
- **Programmatic multi-step orchestration** -- these are playbooks Claude follows, not automated chains. For programmatic orchestration, use the [workflow-automation](../workflow-automation/) plugin.

## How It Works Under the Hood

Each of the 18 workflows is a standalone SKILL.md with its own frontmatter triggers. There are no shared reference documents -- each workflow is self-contained. When you describe a problem, Claude matches it against all active skills' descriptions and activates the best match.

The workflow types reflect different problem structures:

- **Sequential gates** (api-to-production): linear phases with checkpoints that must pass before proceeding
- **Diagnostic loops** (debug-complex-issue, evaluate-and-improve-agent): hypothesis-test-fix cycles that repeat until the issue is resolved
- **Funnels** (build-ai-agent, user-research-to-insight): wide intake that narrows through successive filtering stages
- **Funnel + gate** (llm-cost-optimization): funnel with a mandatory quality gate that can roll back optimizations
- **Parallel-merge** (pitch-sprint): parallel streams that converge into a unified output
- **Layered build** (content-platform-build): dependencies between layers where order is load-bearing
- **Multi-pass audit** (security-hardening-audit, design-review-sprint): audit everything before fixing anything, so systemic patterns emerge

The 288 eval cases across all 18 workflows test both activation (does the right workflow activate for a given query?) and output quality (does the workflow produce the correct phase structure and artifacts?).

## Version History

- `2.0.0` Added 9 new workflows: build-a-plugin, api-to-production, security-hardening-audit, onboard-to-codebase, product-story-to-ship, context-engineering-pipeline, design-review-sprint, evaluate-and-improve-agent, storytelling-for-stakeholders
- `1.0.0` Initial release with 9 composition workflows

## Related Plugins

- **[Skill Creator](../skill-creator/)** -- Create the individual skills these workflows reference
- **[Plugin Dev](../plugin-dev/)** -- Full plugin authoring toolkit referenced by `build-a-plugin`
- **[Workflow Automation](../workflow-automation/)** -- Programmatic multi-step orchestration (not playbook-style)
- All 32+ SkillStack skills referenced by the workflows -- install them for domain depth

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — production-grade plugins for Claude Code.
