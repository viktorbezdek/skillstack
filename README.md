# SkillStack

**Battle-tested skills for Claude Code.** 52 expert plugins that give Claude deep domain knowledge across software engineering, DevOps, testing, design, strategic thinking, context engineering, agent architecture, storytelling, and composable multi-stage workflows.

**[Quick start](#quick-start)** · **[Find a skill by goal](#find-a-skill-by-goal)** · **[Full catalog](#plugin-catalog)** · **[Contribute](#contributing)**

> **52** plugins · **8** categories · **8** collections · MIT License

---

## What is a Claude Code skill?

A **skill** is a structured knowledge package that Claude Code loads on demand. Unlike a one-shot prompt, a skill includes:

- A short activation description that tells Claude when to use it
- Core instructions for how to approach the domain
- **Progressive-disclosure references** — focused files Claude only loads when relevant, so your context window doesn't fill up with content you don't need

Think of it as giving Claude a carefully organized textbook for a specific subject. When you ask about that subject, Claude reads the table of contents first and pulls in only the chapter that matters.

**Every skill in SkillStack follows the same contract**: lean activation file (≤200 lines), domain references loaded on demand, explicit "when to use / when NOT to use" boundaries, and cross-references to related skills. This keeps Claude fast and accurate even when you install dozens of plugins.

---

## Quick Start

Plugin installation in Claude Code is a two-step process: add the marketplace once, then install individual plugins by name.

**Step 1 — Add the SkillStack marketplace** (run this once, inside a Claude Code session):
```
/plugin marketplace add viktorbezdek/skillstack
```

**Step 2 — Install the plugins you want:**
```
/plugin install api-design@skillstack
/plugin install storytelling@skillstack
/plugin install debugging@skillstack
```

**Or browse and install interactively:**
```
/plugin
```
This opens the plugin browser where you can search, preview, and install any of the 52 SkillStack plugins.

After installation, the skill activates automatically when Claude detects a relevant query, or you can invoke it explicitly:
```
Use the api-design skill to design a REST API for user management.
```

---

## Find a skill by goal

Use this table to find the right plugin for what you actually want to do. Each row points to a specific skill; click through to its README for full use cases and examples.

### I want to write or ship code

| Goal | Skill |
|---|---|
| Design a REST, GraphQL, or gRPC API with pagination, auth, and versioning | [api-design](api-design/) |
| Debug a flaky test, race condition, production bug, or CI failure systematically | [debugging](debugging/) |
| Write Python/TypeScript/React/Next.js code that follows current best practices | [python-development](python-development/), [typescript-development](typescript-development/), [react-development](react-development/), [nextjs-development](nextjs-development/) |
| Style and build accessible UI with Tailwind, design tokens, WCAG compliance | [frontend-design](frontend-design/) |
| Review code with structured, severity-rated feedback | [code-review](code-review/) |
| Follow TDD with proper red-green-refactor discipline | [test-driven-development](test-driven-development/) |
| Set up a testing framework across unit, integration, and E2E | [testing-framework](testing-framework/) |
| Identify boundary conditions and edge cases I might miss | [edge-case-coverage](edge-case-coverage/) |
| Build an MCP server in Python or TypeScript | [mcp-server](mcp-server/) |
| Drive Google Workspace (Drive, Gmail, Sheets, Calendar) from the terminal | [gws-cli](gws-cli/) |
| Follow consistent naming conventions and style across my codebase | [consistency-standards](consistency-standards/) |

### I want to ship and operate

| Goal | Skill |
|---|---|
| Design a CI/CD pipeline with secrets, rollbacks, and environment promotion | [cicd-pipelines](cicd-pipelines/) |
| Optimize Dockerfiles, multi-stage builds, image size, and security | [docker-containerization](docker-containerization/) |
| Manage git worktrees, commits, branches, and changelogs at professional quality | [git-workflow](git-workflow/) |
| Reduce AWS / Azure / GCP / Kubernetes / serverless cloud costs | [cloud-finops](cloud-finops/) |
| Orchestrate complex multi-agent workflows with state machines | [workflow-automation](workflow-automation/) |

### I want to design a product or experience

| Goal | Skill |
|---|---|
| Write a pitch, founder story, case study, or data-driven presentation that actually moves people | [storytelling](storytelling/) |
| Build user personas with empathy maps, goals, and pain points from research | [persona-definition](persona-definition/) |
| Map stakeholders with Power-Interest matrices and RACI charts | [persona-mapping](persona-mapping/) |
| Design an effective user-research interview that reveals real motivations | [elicitation](elicitation/) |
| Map user journeys with touchpoints, emotional states, and friction moments | [user-journey-design](user-journey-design/) |
| Write UX microcopy, error messages, button labels, and empty states | [ux-writing](ux-writing/) |
| Design information architecture, navigation, breadcrumbs, sitemaps | [navigation-design](navigation-design/) |
| Build content models for a CMS with types, fields, and relationships | [content-modelling](content-modelling/) |
| Model a domain ontology with classes, properties, and taxonomies | [ontology-design](ontology-design/) |

### I want to think better about a problem

| Goal | Skill |
|---|---|
| Apply systems thinking — feedback loops, leverage points, stocks and flows | [systems-thinking](systems-thinking/) |
| Generate genuinely new ideas via lateral thinking, SCAMPER, first principles | [creative-problem-solving](creative-problem-solving/) |
| Critique an existing idea with pattern recognition, bias detection, red flags | [critical-intuition](critical-intuition/) |
| Prioritize a backlog with RICE, MoSCoW, ICE, or effort-impact matrices | [prioritization](prioritization/) |
| Assess and mitigate project risks systematically | [risk-management](risk-management/) |
| Define outcomes and OKRs rather than just ticking off outputs | [outcome-orientation](outcome-orientation/) |

### I want to build or evaluate AI agents

| Goal | Skill |
|---|---|
| Design a multi-agent system (supervisor, swarm, handoff patterns) | [multi-agent-patterns](multi-agent-patterns/) |
| Give an agent persistent memory across sessions | [memory-systems](memory-systems/) |
| Reduce an agent's tool surface and design better tool descriptions | [tool-design](tool-design/) |
| Build evaluation rubrics and LLM-as-judge pipelines for agent output | [agent-evaluation](agent-evaluation/) |
| Set up an LLM project with pipelines, task-model fit, and cost estimation | [agent-project-development](agent-project-development/) |
| Run background / hosted agents in sandboxed environments | [hosted-agents](hosted-agents/) |
| Model an agent's beliefs, desires, and intentions formally (BDI) | [bdi-mental-states](bdi-mental-states/) |
| Write better prompts through systematic design and evaluation | [prompt-engineering](prompt-engineering/) |

### I want to understand and engineer context

| Goal | Skill |
|---|---|
| Learn how context windows, attention, and progressive disclosure work | [context-fundamentals](context-fundamentals/) |
| Diagnose context degradation (lost-in-middle, poisoning, clash, confusion) | [context-degradation/](context-degradation/) |
| Compress context with summarization and anchored iterative techniques | [context-compression](context-compression/) |
| Extend effective context with KV-cache, partitioning, observation masking | [context-optimization](context-optimization/) |
| Use the file system as long-term context (scratch pads, dynamic loading) | [filesystem-context](filesystem-context/) |

### I want to document and create skills

| Goal | Skill |
|---|---|
| Generate repository documentation at scale (monorepo or library) | [documentation-generator](documentation-generator/) |
| Design good code examples and progressive-complexity tutorials | [example-design](example-design/) |
| Create a high-quality Claude Code skill myself | [skill-creator](skill-creator/) |
| Build a full Claude Code plugin — hooks, MCPs, multi-skill composition, validation, evals | [plugin-dev](plugin-dev/) |

### I want a playbook for a multi-stage problem

| Goal | Workflow (from [skillstack-workflows](skillstack-workflows/)) |
|---|---|
| Produce an investor / board / funding pitch in one week | `pitch-sprint` |
| Debug a complex issue that's defeated my first fix attempt | `debug-complex-issue` |
| Go from "I want an AI agent for X" to a deployed, evaluated agent | `build-ai-agent` |
| Make a high-stakes strategic decision without criteria drift | `strategic-decision` |
| Build a docs site / CMS / knowledge base from scratch | `content-platform-build` |
| Turn user research interviews into product direction that actually sticks | `user-research-to-insight` |
| Make real progress on a legacy codebase without breaking production | `legacy-rescue` |
| Cut LLM costs without degrading product quality | `llm-cost-optimization` |
| Create my own Claude Code skill that actually activates reliably | `write-your-own-skill` |
| Build a full Claude Code plugin (hooks, MCPs, multi-skill) | `build-a-plugin` |
| Build and ship an API from design to containerized deployment | `api-to-production` |
| Systematically harden a codebase's security posture | `security-hardening-audit` |
| Quickly understand a large unfamiliar codebase | `onboard-to-codebase` |
| Turn user research into a prioritized engineering backlog | `product-story-to-ship` |
| Fix an agent's degrading context window systematically | `context-engineering-pipeline` |
| Run a full UX design quality audit across an app | `design-review-sprint` |
| Diagnose and improve an underperforming AI agent | `evaluate-and-improve-agent` |
| Present data or results as a compelling stakeholder narrative | `storytelling-for-stakeholders` |

---

## Collections

<details>
<summary><strong>SkillStack</strong> — 52 plugins</summary>

> The complete SkillStack library — 52 expert skills for Claude Code covering the full software development lifecycle.

Plugins: `agent-evaluation`, `agent-project-development`, `api-design`, `bdi-mental-states`, `cicd-pipelines`, `cloud-finops`, `code-review`, `consistency-standards`, `content-modelling`, `context-compression`, `context-degradation`, `context-fundamentals`, `context-optimization`, `creative-problem-solving`, `critical-intuition`, `debugging`, `docker-containerization`, `documentation-generator`, `edge-case-coverage`, `elicitation`, `example-design`, `filesystem-context`, `frontend-design`, `git-workflow`, `gws-cli`, `hosted-agents`, `mcp-server`, `memory-systems`, `multi-agent-patterns`, `navigation-design`, `nextjs-development`, `ontology-design`, `outcome-orientation`, `persona-definition`, `persona-mapping`, `plugin-dev`, `prioritization`, `prompt-engineering`, `python-development`, `react-development`, `risk-management`, `skill-creator`, `skillstack-workflows`, `storytelling`, `systems-thinking`, `test-driven-development`, `testing-framework`, `tool-design`, `typescript-development`, `user-journey-design`, `ux-writing`, `workflow-automation`
</details>

<details>
<summary><strong>Development Core</strong> — 12 plugins</summary>

> Core development skills: Python, TypeScript, React, Next.js, API design, debugging, frontend design, and plugin authoring.

Plugins: `api-design`, `debugging`, `frontend-design`, `gws-cli`, `mcp-server`, `nextjs-development`, `plugin-dev`, `prompt-engineering`, `python-development`, `react-development`, `skill-creator`, `typescript-development`
</details>

<details>
<summary><strong>DevOps & Infrastructure</strong> — 5 plugins</summary>

> CI/CD pipelines, Docker containerization, Git workflow management, and workflow automation.

Plugins: `cicd-pipelines`, `cloud-finops`, `docker-containerization`, `git-workflow`, `workflow-automation`
</details>

<details>
<summary><strong>Quality & Testing</strong> — 5 plugins</summary>

> Code review, test-driven development, testing frameworks, edge case coverage, and consistency standards.

Plugins: `code-review`, `consistency-standards`, `edge-case-coverage`, `test-driven-development`, `testing-framework`
</details>

<details>
<summary><strong>Context Engineering</strong> — 5 plugins</summary>

> Context fundamentals, degradation patterns, compression, optimization, and filesystem-based context management.

Plugins: `context-compression`, `context-degradation`, `context-fundamentals`, `context-optimization`, `filesystem-context`
</details>

<details>
<summary><strong>Agent Architecture</strong> — 7 plugins</summary>

> Multi-agent patterns, memory systems, tool design, hosted agents, BDI mental states, agent evaluation, and project development.

Plugins: `agent-evaluation`, `agent-project-development`, `bdi-mental-states`, `hosted-agents`, `memory-systems`, `multi-agent-patterns`, `tool-design`
</details>

<details>
<summary><strong>Strategic Thinking</strong> — 7 plugins</summary>

> Creative problem-solving, critical intuition, systems thinking, prioritization, risk management, outcome orientation, and composable multi-stage workflow playbooks.

Plugins: `creative-problem-solving`, `critical-intuition`, `outcome-orientation`, `prioritization`, `risk-management`, `skillstack-workflows`, `systems-thinking`
</details>

<details>
<summary><strong>Design & UX</strong> — 8 plugins</summary>

> Content modelling, navigation design, ontology design, persona definition/mapping, storytelling, user journey design, and UX writing.

Plugins: `content-modelling`, `elicitation`, `navigation-design`, `ontology-design`, `persona-definition`, `persona-mapping`, `storytelling`, `user-journey-design`, `ux-writing`
</details>

---

## Plugin Catalog

### 💻 Development (12)

| Plugin | Version | Description |
|--------|---------|-------------|
| [API Design](api-design/README.md) | `1.2.23` | Comprehensive API design skill for REST, GraphQL, gRPC, and Python library architectures. Design endpoints, schemas, authentication, pagination, error handling, and federation. |
| [Debugging](debugging/README.md) | `1.1.26` | Comprehensive debugging skill combining systematic debugging methodology, browser DevTools automation, E2E testing with visual analysis, CI/CD pipeline debugging, performance profiling, and AI-powered error analysis. |
| [Frontend Design](frontend-design/README.md) | `1.1.23` | Comprehensive Frontend Design (UI/UX) skill combining UI design systems, component libraries, CSS/Tailwind styling, accessibility patterns, and visual design. |
| [Gws Cli](gws-cli/README.md) | `1.0.0` | Google Workspace CLI (gws) skill for managing Drive, Gmail, Sheets, Calendar, Docs, Chat, Tasks, and 11 more Workspace APIs from the command line. Dynamic Discovery-based commands, helper shortcuts, schema introspection, and cross-service workflows. |
| [MCP Server](mcp-server/README.md) | `1.2.20` | Comprehensive MCP (Model Context Protocol) server development skill. Build, configure, and manage MCP servers using Python (FastMCP) or TypeScript. Covers agent-centric design, tool creation, evaluation testing, production deployment, Claude Code integration, and plugin development. |
| [Next.js Development](nextjs-development/README.md) | `2.0.23` | Comprehensive Next.js development skill covering App Router (13+/15/16), Server Components, Server Actions, Cache Components, data fetching patterns, and module architecture. |
| [Plugin Dev](plugin-dev/README.md) | `1.0.0` | End-to-end Claude Code plugin authoring toolkit. 7 skills covering the full lifecycle (ideate → research → architect → hooks → composition → validate → evaluate) plus 4 runnable scripts (scaffold, validate, eval harness, hook tester). Fills the gap Anthropic's Complete Guide doesn't cover: hooks, multi-component composition, and plugin-level evaluation. |
| [Prompt Engineering](prompt-engineering/README.md) | `1.1.15` | Comprehensive prompt optimization system for LLMs. Design effective AI interactions, evaluate prompt quality, and perform iterative refinement for any LLM platform. |
| [Python Development](python-development/README.md) | `1.1.24` | Comprehensive Python development skill covering modern tooling (uv, ruff, mypy, pytest), best practices, coding standards, library architecture, functional patterns, async programming, MicroPython, and production-grade development workflows. |
| [React Development](react-development/README.md) | `1.1.20` | Build production-grade React applications with Next.js App Router, shadcn/ui components, optimized hooks, and Bulletproof React architecture. |
| [Skill Creator](skill-creator/README.md) | `1.1.19` | Comprehensive skill creation framework combining philosophy-first design, evidence-based prompting, progressive disclosure, anti-pattern prevention, and enterprise-grade workflows. |
| [Typescript Development](typescript-development/README.md) | `1.1.20` | Comprehensive TypeScript development skill covering type system mastery, runtime validation (Zod, TypeBox, Valibot), framework integration (React 19, Next.js 16, NestJS, React Native), architecture patterns, security, tsconfig optimization, and testing strategies. |

### ⚙️ Devops (5)

| Plugin | Version | Description |
|--------|---------|-------------|
| [CI/CD Pipelines](cicd-pipelines/README.md) | `1.1.23` | Comprehensive CI/CD pipeline design, DevOps automation, infrastructure as code, container orchestration, and enterprise release management. |
| [Cloud FinOps](cloud-finops/README.md) | `1.0.0` | Expert Cloud FinOps guidance covering AI cost management, GenAI capacity planning, cloud billing (AWS, Azure, GCP), commitment strategy, tagging governance, SaaS asset management, ITAM, and GreenOps. Includes 20 domain-specific reference files grounded in enterprise delivery experience. Built by OptimNow, licensed CC BY-SA 4.0. |
| [Docker Containerization](docker-containerization/README.md) | `1.1.22` | Comprehensive Docker and containerization skill covering Docker basics, multi-stage builds, Docker Compose orchestration, container optimization, development environment setup, and infrastructure patterns. |
| [Git Workflow](git-workflow/README.md) | `1.1.20` | Comprehensive Git workflow management skill covering conventional commits, commit quality analysis, intelligent file grouping, worktree management with GitFlow conventions, issue tracking integration, changelog generation, semantic versioning, and hierarchical story backlog management. |
| [Workflow Automation](workflow-automation/README.md) | `1.1.21` | Automate development workflows end-to-end including CI/CD pipelines, multi-agent orchestration, parallel task execution, release automation, and git workflow management. |

### ✅ Quality (5)

| Plugin | Version | Description |
|--------|---------|-------------|
| [Code Review](code-review/README.md) | `1.1.24` | Perform thorough code reviews with multi-agent swarm analysis covering security, performance, style, tests, and documentation. Analyze PRs, extract and prioritize comments, and generate actionable fix plans. |
| [Consistency Standards](consistency-standards/README.md) | `1.0.10` | Establish and maintain naming conventions, taxonomy standards, style guides, and reuse patterns across documentation and code. |
| [Edge Case Coverage](edge-case-coverage/README.md) | `1.0.10` | Identify and document boundary conditions, error scenarios, corner cases, and validation requirements. |
| [Test Driven Development](test-driven-development/README.md) | `1.1.17` | Comprehensive Test-Driven Development skill implementing Red-Green-Refactor cycle across Python, TypeScript, JavaScript, and Emacs Lisp. Covers pytest, Vitest, Playwright, ERT, and Zod. |
| [Testing Framework](testing-framework/README.md) | `1.1.23` | Comprehensive testing framework for multiple languages and platforms. Covers unit testing (Rust, TypeScript, PHP, Shell), E2E testing (Playwright), component testing (React Testing Library), accessibility testing (axe-core), mutation testing, fuzz testing, and CI/CD integration. |

### 🧠 Context Engineering (5)

| Plugin | Version | Description |
|--------|---------|-------------|
| [Context Compression](context-compression/README.md) | `1.0.4` | Production strategies for compressing LLM context windows. Anchored iterative summarization, opaque compression, tokens-per-task optimization, and probe-based evaluation. |
| [Context Degradation](context-degradation/README.md) | `1.0.4` | Patterns for recognizing and mitigating context failures in LLM agents. Covers lost-in-middle, context poisoning, distraction, confusion, clash, and empirical degradation thresholds by model. |
| [Context Fundamentals](context-fundamentals/README.md) | `1.0.5` | Foundational understanding of context engineering for AI agent systems. Covers context anatomy, attention mechanics, progressive disclosure, context budgeting, and the quality-vs-quantity principle. |
| [Context Optimization](context-optimization/README.md) | `1.0.4` | Techniques for extending effective context capacity through compaction, observation masking, KV-cache optimization, and context partitioning. Double or triple effective context without larger models. |
| [Filesystem Context](filesystem-context/README.md) | `1.0.4` | Filesystem-based context engineering patterns for LLM agents. Scratch pads, plan persistence, sub-agent communication, dynamic skill loading, terminal persistence, and self-modification patterns. |

### 🤖 Agent Architecture (7)

| Plugin | Version | Description |
|--------|---------|-------------|
| [Agent Evaluation](agent-evaluation/README.md) | `1.0.4` | Comprehensive evaluation framework for LLM agent systems. Multi-dimensional rubrics, LLM-as-judge with bias mitigation, pairwise comparison, direct scoring, confidence calibration, and continuous monitoring. |
| [Agent Project Development](agent-project-development/README.md) | `1.0.4` | Methodology for LLM-powered project development. Task-model fit analysis, pipeline architecture (acquire-prepare-process-parse-render), file system state machines, cost estimation, and architectural reduction. |
| [BDI Mental States](bdi-mental-states/README.md) | `1.0.4` | Belief-Desire-Intention cognitive architecture for LLM agents. Formal BDI ontology, T2B2T paradigm, RDF integration, SPARQL competency queries, and neuro-symbolic AI integration patterns. |
| [Hosted Agents](hosted-agents/README.md) | `1.0.4` | Infrastructure patterns for hosted background agents. Sandbox environments, image registry pattern, self-spawning agents, multiplayer support, warm pools, and multi-client integration (Slack, web, Chrome). |
| [Memory Systems](memory-systems/README.md) | `1.0.5` | Production memory architectures for LLM agents. Compares Mem0, Zep/Graphiti, Letta, Cognee, LangMem with benchmarks. Covers temporal knowledge graphs, memory consolidation, and retrieval strategies. |
| [Multi Agent Patterns](multi-agent-patterns/README.md) | `1.0.4` | Architecture patterns for multi-agent LLM systems. Supervisor/orchestrator, peer-to-peer/swarm, hierarchical patterns, context isolation, consensus mechanisms, and the telephone game solution. |
| [Tool Design](tool-design/README.md) | `1.0.4` | Design tools optimized for LLM agents rather than human developers. Consolidation principle, architectural reduction, tool description engineering, MCP naming, and the file system agent pattern. |

### 💡 Thinking (7)

| Plugin | Version | Description |
|--------|---------|-------------|
| [Creative Problem Solving](creative-problem-solving/README.md) | `1.0.15` | Generate breakthrough solutions through lateral thinking, first principles reasoning, game theory, and strategic reframing. |
| [Critical Intuition](critical-intuition/README.md) | `1.0.15` | Detect hidden patterns, expose blind spots, and deliver rigorous critical analysis with intuition-level depth. |
| [Outcome Orientation](outcome-orientation/README.md) | `1.0.10` | Focus on measurable outcomes using OKRs, results-driven thinking, and outcome vs output distinction. |
| [Prioritization](prioritization/README.md) | `1.0.10` | Apply prioritization frameworks including RICE, MoSCoW, ICE scoring, and effort-impact matrices for decision-making. |
| [Risk Management](risk-management/README.md) | `1.0.10` | Apply risk assessment frameworks, mitigation strategies, risk registers, and monitoring practices. |
| [SkillStack Workflows](skillstack-workflows/README.md) | `1.0.0` | Nine composable workflow playbooks orchestrating existing SkillStack plugins for real multi-stage problems — pitch sprints, complex debugging, AI agent builds, strategic decisions, content platform builds, user research synthesis, legacy rescue, LLM cost optimization, skill authoring. Multi-skill plugin. |
| [Systems Thinking](systems-thinking/README.md) | `1.0.10` | Apply systems thinking principles including feedback loops, leverage points, and system dynamics to analyze complex problems. |

### 🎨 Design (10)

| Plugin | Version | Description |
|--------|---------|-------------|
| [Content Modelling](content-modelling/README.md) | `1.0.11` | Design content models with types, fields, relationships, and governance rules for structured content systems. |
| [Elicitation](elicitation/README.md) | `2.0.0` | Psychological elicitation and deep-interview design using narrative identity, self-defining memories, Motivational Interviewing (OARS), values elicitation, schema detection, life review, and LIWC. |
| [Navigation Design](navigation-design/README.md) | `1.0.10` | Design information architecture, wayfinding systems, breadcrumbs, and navigation patterns for documentation and applications. |
| [Ontology Design](ontology-design/README.md) | `1.0.10` | Design knowledge models with classes, properties, relationships, and taxonomies for structured data representation. |
| [Persona Definition](persona-definition/README.md) | `1.0.10` | Create detailed user personas with demographics, goals, pain points, behaviors, and empathy maps. |
| [Persona Mapping](persona-mapping/README.md) | `1.0.10` | Map stakeholders and personas using Power-Interest matrices, RACI charts, and influence analysis. |
| [Storytelling](storytelling/README.md) | `1.0.0` | Storytelling craft across fiction, business, data, speech, UX, and interactive narrative. 9 canonical story structures, character design, scene/pacing, dialogue, POV, StoryBrand, Pixar Spine, data storytelling, speech writing, interactive narrative, and narrative theory. 12 progressive-disclosure references. |
| [User Journey Design](user-journey-design/README.md) | `1.0.10` | Design user journey maps with touchpoints, emotional states, pain points, and opportunities. |
| [UX Writing](ux-writing/README.md) | `1.0.10` | Write effective microcopy, error messages, button labels, and interface text using UX writing principles. |

### 📚 Documentation (2)

| Plugin | Version | Description |
|--------|---------|-------------|
| [Documentation Generator](documentation-generator/README.md) | `1.1.15` | Generate comprehensive documentation for repositories of any size - from small libraries to large monorepos. Creates both non-technical overviews and detailed technical references. |
| [Example Design](example-design/README.md) | `1.0.10` | Design effective code examples, tutorials, and runnable samples with progressive complexity. |

---

## How It Works

Each plugin is a self-contained skill that teaches Claude Code domain expertise using the same progressive-disclosure architecture:

```
You describe a task        Claude matches against        Lean SKILL.md loads
  (natural language)   →   skill activation descriptions  →   (<200 lines, always)
                                                              ↓
                                        Claude routes to the right reference files
                                        and loads ONLY those (no context bloat)
                                                              ↓
                                              Expert-level output
```

**Why progressive disclosure matters.** A naive skill that dumps 5,000 lines of domain content into Claude's context on every query burns tokens, slows response, and degrades quality. SkillStack skills put only routing and principles in SKILL.md, then load domain references on demand. A query about StoryBrand loads `business-storytelling.md`, not `narrative-theory.md`. A query about AWS commitment strategy loads `finops-aws.md`, not the other 25 cloud-finops references.

**Every skill in this repo is CI-validated.** The `plugin-validation` job runs on every commit and checks that:
- Every plugin has a valid `plugin.json`, `SKILL.md`, and `README.md`
- SKILL.md frontmatter matches its directory name
- Every reference file cited from SKILL.md actually exists on disk
- Versions in `plugin.json`, `registry.json`, and `marketplace.json` match
- No orphan catalog entries (plugins that don't exist) or unregistered plugins

This means when you install a plugin from this repo, you never get a half-shipped skill that references missing files.

---

## Installation details

All commands below are **slash commands** — run them from inside a Claude Code session, not from your regular shell.

### Step 1: Add the marketplace (once)

```
/plugin marketplace add viktorbezdek/skillstack
```

This registers the SkillStack marketplace with your Claude Code instance. You only need to do this once; after that, all 52 plugins become available to install by name.

### Step 2: Install individual plugins

```
/plugin install api-design@skillstack
/plugin install storytelling@skillstack
/plugin install debugging@skillstack
```

The `@skillstack` suffix is the marketplace identifier (pulled from `.claude-plugin/marketplace.json`'s `name` field). You can install as many or as few plugins as you want — each one is self-contained.

### Interactive browser

```
/plugin
```

Opens the interactive plugin browser where you can search, preview descriptions, and install any plugin with a single click. Most users find this the easiest entry point.

### Verify your installation

After install, ask Claude Code:
```
List the skills currently available.
```

Claude should include the SkillStack plugins you installed. If a plugin doesn't appear, try:
```
/plugin marketplace refresh
```

### Scope options

The `/plugin` command supports installing at user, project, or local scope. Select the scope in the interactive UI, or see Claude Code's plugin documentation for the non-interactive flags.

---

## Contributing

Contributions are welcome — bug reports, reference improvements, new skills, and fixes to existing plugins.

**Report a problem.** [Open an issue](https://github.com/viktorbezdek/skillstack/issues) with enough detail to reproduce. If you spotted a skill that misfires (activates when it shouldn't, or stays silent when it should), include the prompt you used and what you expected.

**Improve an existing skill.** Every skill has a `skills/{name}/SKILL.md` and (usually) a `skills/{name}/references/` directory. Fork, make your changes, run `python3 .github/scripts/validate_plugins.py` locally to check structure, and open a PR.

**Add a new skill.** Use the [skill-creator](skill-creator/) plugin as a starting point — it knows the repo conventions. Your new plugin needs:
- `your-skill/.claude-plugin/plugin.json` with `name`, `version`, `description`, `author`
- `your-skill/skills/your-skill/SKILL.md` with YAML frontmatter (`name` must match directory)
- `your-skill/skills/your-skill/evals/trigger-evals.json` — ≥8 positive + ≥5 negative trigger cases
- `your-skill/skills/your-skill/evals/evals.json` — ≥3 output test cases
- `your-skill/README.md` with `## What Problem Does This Solve`, `## When to Use This Skill` (scenario table), `## Installation`, `## How to Use`
- An entry in `.claude-plugin/registry.json` and `.claude-plugin/marketplace.json`
- CI will tell you what's wrong if you miss any of these

**Run evals.** Every skill has eval files. Validate structure offline or measure real activation with an API key:
```bash
# Offline smoke test (structure only, no API key needed)
python3 plugin-dev/scripts/run_eval.py --plugin-dir debugging --skill debugging --offline

# Live trigger evals (requires ANTHROPIC_API_KEY + pip install anthropic)
python3 plugin-dev/scripts/run_eval.py --plugin-dir debugging --skill debugging --mode trigger
```

**Local validation before opening a PR:**
```bash
# Check that your plugin structure is correct
python3 .github/scripts/validate_plugins.py

# Run the validator's own tests if you changed validation logic
pytest .github/scripts/tests/ -q

# Run shellcheck if you added bash scripts
find . -name "*.sh" -not -path "./.git/*" | xargs shellcheck --severity=error
```

---

## License

MIT. See [LICENSE](LICENSE).

Individual plugins may carry their own license terms when they incorporate external work — see each plugin's README. For example, `cloud-finops` is CC BY-SA 4.0 (derived from OptimNow content), and `elicitation` incorporates work from `tasteray/skills`.

---

*Catalog auto-generated from [registry.json](.claude-plugin/registry.json) · Plugin structure validated by [.github/scripts/validate_plugins.py](.github/scripts/validate_plugins.py)*
