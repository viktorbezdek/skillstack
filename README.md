# SkillStack

**Battle-tested skills for Claude Code.**

**55** expert plugins covering development, DevOps, testing, design, strategy, context engineering, and agent architecture.

**[Browse the catalog](https://viktorbezdek.github.io/skillstack/)** · **[Install](#quick-start)** · **[Contribute](https://github.com/viktorbezdek/skillstack/issues)**

> **55** plugins · **8** categories · **10** collections · MIT License

---

## Quick Start

```bash
# Install the full SkillStack collection
claude plugin add viktorbezdek/skillstack

# Or install individual plugins
claude plugin add viktorbezdek/skillstack --plugin api-design
```

---

## Collections

<details>
<summary><strong>SkillStack</strong> — 55 plugins</summary>

> The complete SkillStack library — 55 expert skills for Claude Code covering development, DevOps, quality, context engineering, agent architecture, strategic thinking, design, documentation, and meta-skills.

Plugins: `agent-evaluation`, `agent-project-development`, `api-design`, `bdi-mental-states`, `cicd-pipelines`, `cloud-finops`, `code-review`, `communication`, `consistency-standards`, `content-modelling`, `context-compression`, `context-degradation`, `context-fundamentals`, `context-optimization`, `creative-problem-solving`, `critical-intuition`, `debugging`, `docker-containerization`, `documentation-generator`, `edge-case-coverage`, `elicitation`, `example-design`, `filesystem-context`, `frontend-design`, `git-workflow`, `gws-cli`, `hosted-agents`, `mcp-server`, `memory-systems`, `multi-agent-patterns`, `navigation-design`, `nextjs-development`, `ontology-design`, `outcome-orientation`, `persona-definition`, `persona-mapping`, `plugin-dev`, `prioritization`, `product-thinking`, `prompt-engineering`, `python-development`, `react-development`, `risk-management`, `skill-foundry`, `skillstack-workflows`, `storytelling`, `systems-thinking`, `technical-copywriting`, `test-driven-development`, `testing-framework`, `tool-design`, `typescript-development`, `user-journey-design`, `ux-writing`, `workflow-automation`
</details>

<details>
<summary><strong>Development Core</strong> — 10 plugins</summary>

> Core development skills for writing and shipping code: API design, debugging, frontend design, Google Workspace CLI, MCP server development, Next.js, prompt engineering, Python, React, and TypeScript.

Plugins: `api-design`, `debugging`, `frontend-design`, `gws-cli`, `mcp-server`, `nextjs-development`, `prompt-engineering`, `python-development`, `react-development`, `typescript-development`
</details>

<details>
<summary><strong>DevOps & Infrastructure</strong> — 5 plugins</summary>

> Ship and operate software in production: CI/CD pipelines, cloud FinOps, Docker containerization, Git workflow management, and workflow automation.

Plugins: `cicd-pipelines`, `cloud-finops`, `docker-containerization`, `git-workflow`, `workflow-automation`
</details>

<details>
<summary><strong>Quality & Testing</strong> — 5 plugins</summary>

> Ship reliable software: code review, test-driven development, testing frameworks, edge case coverage, and consistency standards.

Plugins: `code-review`, `consistency-standards`, `edge-case-coverage`, `test-driven-development`, `testing-framework`
</details>

<details>
<summary><strong>Context Engineering</strong> — 5 plugins</summary>

> Master LLM context windows: fundamentals, degradation patterns, compression, optimization, and filesystem-based context management.

Plugins: `context-compression`, `context-degradation`, `context-fundamentals`, `context-optimization`, `filesystem-context`
</details>

<details>
<summary><strong>Agent Architecture</strong> — 7 plugins</summary>

> Build production LLM agents: multi-agent patterns, memory systems, tool design, hosted agents, BDI mental states, agent evaluation, and project development methodology.

Plugins: `agent-evaluation`, `agent-project-development`, `bdi-mental-states`, `hosted-agents`, `memory-systems`, `multi-agent-patterns`, `tool-design`
</details>

<details>
<summary><strong>Strategic Thinking</strong> — 7 plugins</summary>

> Think better about problems: creative problem-solving, critical intuition, systems thinking, prioritization, risk management, outcome orientation, and product thinking.

Plugins: `creative-problem-solving`, `critical-intuition`, `outcome-orientation`, `prioritization`, `product-thinking`, `risk-management`, `systems-thinking`
</details>

<details>
<summary><strong>Design & UX</strong> — 9 plugins</summary>

> Design products and experiences: content modelling, elicitation, navigation design, ontology design, persona definition/mapping, storytelling, user journey design, and UX writing.

Plugins: `content-modelling`, `elicitation`, `navigation-design`, `ontology-design`, `persona-definition`, `persona-mapping`, `storytelling`, `user-journey-design`, `ux-writing`
</details>

<details>
<summary><strong>Documentation & Communication</strong> — 4 plugins</summary>

> Write, structure, and communicate: documentation generation, example design, communication craft (structured writing, stakeholder alignment, ADRs, runbooks, diagram-as-code), and long-form technical copywriting (research, structure, engaging craft, polish, distribution).

Plugins: `communication`, `documentation-generator`, `example-design`, `technical-copywriting`
</details>

<details>
<summary><strong>Meta-Skills</strong> — 3 plugins</summary>

> Build skills and plugins for Claude Code: skill engineering framework, plugin authoring toolkit, and composable workflow playbooks.

Plugins: `plugin-dev`, `skill-foundry`, `skillstack-workflows`
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
| [Plugin Dev](plugin-dev/README.md) | `1.1.0` | End-to-end Claude Code plugin authoring toolkit. 8 skills covering the full lifecycle: ideation, research, architecture, hooks, composition, validation, evaluation, and documentation generation. Plus 4 runnable scripts: plugin scaffolder, structural validator, eval harness, and hook tester. Document any plugin by URL or local path with comprehensive README generation. |
| [Prompt Engineering](prompt-engineering/README.md) | `1.1.15` | Comprehensive prompt optimization system for LLMs. Design effective AI interactions, evaluate prompt quality, and perform iterative refinement for any LLM platform. |
| [Python Development](python-development/README.md) | `1.1.24` | Comprehensive Python development skill covering modern tooling (uv, ruff, mypy, pytest), best practices, coding standards, library architecture, functional patterns, async programming, MicroPython, and production-grade development workflows. |
| [React Development](react-development/README.md) | `1.1.20` | Build production-grade React applications with Next.js App Router, shadcn/ui components, optimized hooks, and Bulletproof React architecture. |
| [Skill Foundry](skill-foundry/README.md) | `2.0.0` | Advanced skill engineering framework with 8-phase methodology, 20+ scripts, 59 references, 13 example skills, and progressive disclosure architecture. Distinct from Anthropic's bundled skill-creator — this is the full production toolkit for philosophy-first design, evidence-based prompting, anti-pattern prevention, shibboleths, eval-driven iteration, and enterprise-grade workflows. |
| [Typescript Development](typescript-development/README.md) | `1.1.20` | Comprehensive TypeScript development skill covering type system mastery, runtime validation (Zod, TypeBox, Valibot), framework integration (React 19, Next.js 16, NestJS, React Native), architecture patterns, security, tsconfig optimization, and testing strategies. |

### ⚙️ Devops (5)

| Plugin | Version | Description |
|--------|---------|-------------|
| [CI/CD Pipelines](cicd-pipelines/README.md) | `1.1.23` | Comprehensive CI/CD pipeline design, DevOps automation, infrastructure as code, container orchestration, and enterprise release management. |
| [Cloud FinOps](cloud-finops/README.md) | `2.1.0` | Expert Cloud FinOps guidance covering AI cost management, GenAI capacity planning, AI-powered FinOps automation, cloud billing (AWS, Azure, GCP, OCI), Kubernetes/container FinOps, serverless FinOps, data platform FinOps (Kafka, OpenSearch, Redis/Valkey), multi-cloud normalization (FOCUS spec), commitment strategy, tagging governance, SaaS asset management, ITAM, and GreenOps. Includes 26 domain-specific reference files grounded in enterprise delivery experience. Built by OptimNow and Viktor Bezdek, licensed CC BY-SA 4.0. |
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

### 💡 Thinking (8)

| Plugin | Version | Description |
|--------|---------|-------------|
| [Creative Problem Solving](creative-problem-solving/README.md) | `1.0.15` | Generate breakthrough solutions through lateral thinking, first principles reasoning, game theory, and strategic reframing. |
| [Critical Intuition](critical-intuition/README.md) | `1.0.15` | Detect hidden patterns, expose blind spots, and deliver rigorous critical analysis with intuition-level depth. |
| [Outcome Orientation](outcome-orientation/README.md) | `1.0.10` | Focus on measurable outcomes using OKRs, results-driven thinking, and outcome vs output distinction. |
| [Prioritization](prioritization/README.md) | `1.0.10` | Apply prioritization frameworks including RICE, MoSCoW, ICE scoring, and effort-impact matrices for decision-making. |
| [Product Thinking](product-thinking/README.md) | `1.0.0` | Five composable product-thinking skills: frame the real problem (JTBD, 5-whys), identify user needs (functional/emotional/social jobs), design value propositions (VPC, Kano), apply outcome-over-output thinking (North Star, leading/lagging metrics), and analyze trade-offs (cost-benefit, opportunity cost, reversibility, second-order effects). |
| [Risk Management](risk-management/README.md) | `1.0.10` | Apply risk assessment frameworks, mitigation strategies, risk registers, and monitoring practices. |
| [Skillstack Workflows](skillstack-workflows/README.md) | `2.2.0` | Twenty composable workflow playbooks that orchestrate existing SkillStack plugins for real multi-stage problems: plugin authoring, plugin updating, plugin/skill evaluation, API-to-production, security hardening, codebase onboarding, product stories, context engineering, design review, agent improvement, stakeholder storytelling, pitch sprints, complex debugging, AI agent building, strategic decisions, content platforms, user research, legacy rescue, LLM cost optimization, and skill authoring. Each workflow is a self-contained playbook with phase-by-phase guidance, gates/loops, and explicit references to the underlying SkillStack skills. |
| [Systems Thinking](systems-thinking/README.md) | `1.0.10` | Apply systems thinking principles including feedback loops, leverage points, and system dynamics to analyze complex problems. |

### 🎨 Design (9)

| Plugin | Version | Description |
|--------|---------|-------------|
| [Content Modelling](content-modelling/README.md) | `1.0.11` | Design content models with types, fields, relationships, and governance rules for structured content systems. |
| [Elicitation](elicitation/README.md) | `2.0.0` | Psychological elicitation and deep-interview design using narrative identity (McAdams), self-defining memories (Singer), Motivational Interviewing (OARS), values elicitation (Schwartz), schema detection (Young), life review (Haight/Birren), and linguistic analysis (Pennebaker/LIWC). Progressive-disclosure structure with 8 domain references. |
| [Navigation Design](navigation-design/README.md) | `1.0.10` | Design information architecture, wayfinding systems, breadcrumbs, and navigation patterns for documentation and applications. |
| [Ontology Design](ontology-design/README.md) | `1.0.10` | Design knowledge models with classes, properties, relationships, and taxonomies for structured data representation. |
| [Persona Definition](persona-definition/README.md) | `1.0.10` | Create detailed user personas with demographics, goals, pain points, behaviors, and empathy maps. |
| [Persona Mapping](persona-mapping/README.md) | `1.0.10` | Map stakeholders and personas using Power-Interest matrices, RACI charts, and influence analysis. |
| [Storytelling](storytelling/README.md) | `1.0.0` | Storytelling craft and application across fiction, business, data, speech, UX, and interactive narrative. Covers structural frameworks (3-act, Hero's Journey, Story Circle, Kishōtenketsu, Save the Cat, StoryBrand, Pixar Spine, Monroe's Motivated Sequence), narrative craft (character design, scene construction, dialogue, POV, pacing), domain applications, narrative theory (Propp, Polti, Booker, Tobias, Campbell), and anti-patterns. Progressive-disclosure structure with 12 domain references. |
| [User Journey Design](user-journey-design/README.md) | `1.0.10` | Design user journey maps with touchpoints, emotional states, pain points, and opportunities. |
| [UX Writing](ux-writing/README.md) | `1.0.10` | Write effective microcopy, error messages, button labels, and interface text using UX writing principles. |

### 📚 Documentation (4)

| Plugin | Version | Description |
|--------|---------|-------------|
| [Communication](communication/README.md) | `1.0.0` | Five composable communication skills for people who write for work: structure a written piece (BLUF, Minto Pyramid), edit for clarity and conciseness (active voice, hedge removal), align stakeholders (RFCs, proposals, decision docs with DACI/RAPID roles), apply documentation discipline (ADRs, runbooks, decision logs), and communicate visually (Mermaid flowcharts, sequence diagrams, C4, diagram-as-code). |
| [Documentation Generator](documentation-generator/README.md) | `1.1.15` | Generate comprehensive documentation for repositories of any size - from small libraries to large monorepos. Creates both non-technical overviews and detailed technical references. |
| [Example Design](example-design/README.md) | `1.0.10` | Design effective code examples, tutorials, and runnable samples with progressive complexity. |
| [Technical Copywriting](technical-copywriting/README.md) | `1.0.0` | Five composable skills for writing long-form technical content for an audience — articles, deep-dives, tutorials, newsletters, whitepapers, technical essays. Covers research before craft (audience profiling, source tiering, triangulation, citation), long-form structure (article templates, hook-promise-payoff contract, transitions, length strategy), engaging craft (AIDA, PAS, Bencivenga, Sugarman, Schwartz awareness, hooks, voice, concrete-over-abstract), long-form polish (pacing, scan-ability, the 30% cut, read-aloud test), and distribution craft (titles, dek/meta, social pull-quotes, channel framing). Grounded in proven copywriting techniques and evidence-based research workflow. |

---

## How It Works

Each plugin is a self-contained skill that teaches Claude Code domain expertise:

```
You describe a task        Claude loads the right skill     Expert-level output
  (natural language)   →   (automatic activation)       →   (guided by SKILL.md)
```

Skills activate automatically based on your request, or you can invoke them directly:

```
Use the api-design skill to design a REST API for user management
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) or [open an issue](https://github.com/viktorbezdek/skillstack/issues).

---

*Auto-generated from [registry.json](.claude-plugin/registry.json) · Last updated: 2026-04-16*
