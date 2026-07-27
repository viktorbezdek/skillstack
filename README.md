# SkillStack

**Battle-tested skills for Claude Code.**

**66** expert plugins covering development, DevOps, testing, design, strategy, research, context engineering, and agent architecture.

**[Browse the catalog](https://viktorbezdek.github.io/skillstack/)** · **[Install](#quick-start)** · **[Contribute](https://github.com/viktorbezdek/skillstack/issues)**

> **66** plugins · **4** categories · **5** collections · MIT License

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
<summary><strong>SkillStack</strong> — 66 plugins</summary>

> The complete SkillStack library - 66 expert plugins for Claude Code spanning Engineering, Meta-Infra, Managerial-Product, and Marketing-Comms.

Plugins: `agent-evaluation`, `agent-project-development`, `api-design`, `bdi-mental-states`, `brainstorm-swarm`, `cicd-pipelines`, `cloud-finops`, `cloud-infrastructure`, `code-review`, `coding-discipline`, `communication`, `competitive-intelligence`, `consistency-standards`, `content-modelling`, `context-compression`, `context-degradation`, `context-fundamentals`, `context-optimization`, `creative-problem-solving`, `critical-intuition`, `database-design`, `debugging`, `deslop`, `docker-containerization`, `documentation-generator`, `edge-case-coverage`, `elicitation`, `email-marketing`, `example-design`, `filesystem-context`, `frontend-design`, `git-workflow`, `gws-cli`, `hindsight`, `hosted-agents`, `mcp-server`, `memory-systems`, `multi-agent-patterns`, `navigation-design`, `nextjs-development`, `ontology-design`, `osint`, `outcome-orientation`, `persona-definition`, `persona-mapping`, `plugin-dev`, `prioritization`, `product-thinking`, `prompt-engineering`, `python-development`, `react-development`, `research-synthesis`, `risk-management`, `security-engineering`, `skill-foundry`, `skillstack-workflows`, `social-media-content`, `storytelling`, `systems-thinking`, `technical-copywriting`, `test-driven-development`, `testing-framework`, `tool-design`, `typescript-development`, `user-journey-design`, `ux-writing`
</details>

<details>
<summary><strong>Engineering</strong> — 27 plugins</summary>

> Skills for building software: APIs, debugging, testing, DevOps, frontend, language tooling (Python, TypeScript, React, Next.js), containerization, MCP servers, multi-agent systems, and documentation generation.

Plugins: `agent-project-development`, `api-design`, `bdi-mental-states`, `cicd-pipelines`, `cloud-infrastructure`, `code-review`, `coding-discipline`, `database-design`, `debugging`, `docker-containerization`, `documentation-generator`, `edge-case-coverage`, `frontend-design`, `git-workflow`, `gws-cli`, `hosted-agents`, `mcp-server`, `multi-agent-patterns`, `navigation-design`, `nextjs-development`, `python-development`, `react-development`, `security-engineering`, `test-driven-development`, `testing-framework`, `tool-design`, `typescript-development`
</details>

<details>
<summary><strong>Meta-Infra</strong> — 18 plugins</summary>

> Skills for improving how Claude Code and LLM agents operate: context engineering (compression, degradation, fundamentals, optimization), memory systems, plugin authoring, prompt engineering, skill evaluation, and workflow orchestration.

Plugins: `agent-evaluation`, `consistency-standards`, `context-compression`, `context-degradation`, `context-fundamentals`, `context-optimization`, `critical-intuition`, `elicitation`, `example-design`, `filesystem-context`, `hindsight`, `memory-systems`, `osint`, `plugin-dev`, `prompt-engineering`, `research-synthesis`, `skill-foundry`, `skillstack-workflows`
</details>

<details>
<summary><strong>Managerial-Product</strong> — 14 plugins</summary>

> Skills for making decisions and shipping products: product thinking, prioritization, risk management, brainstorm facilitation, personas, user journeys, outcome orientation, ontology design, content modelling, cloud FinOps, and systems thinking.

Plugins: `brainstorm-swarm`, `cloud-finops`, `competitive-intelligence`, `content-modelling`, `creative-problem-solving`, `ontology-design`, `outcome-orientation`, `persona-definition`, `persona-mapping`, `prioritization`, `product-thinking`, `risk-management`, `systems-thinking`, `user-journey-design`
</details>

<details>
<summary><strong>Marketing-Comms</strong> — 7 plugins</summary>

> Skills for creating human-facing content: communication craft, AI-slop removal, technical copywriting, UX writing, and storytelling.

Plugins: `communication`, `deslop`, `email-marketing`, `social-media-content`, `storytelling`, `technical-copywriting`, `ux-writing`
</details>

---

## Plugin Catalog

### 📌 Engineering (27)

| Plugin | Version | Description |
|--------|---------|-------------|
| [Agent Project Development](agent-project-development/README.md) | `1.0.5` | Methodology for LLM-powered project development. Task-model fit analysis, pipeline architecture (acquire-prepare-process-parse-render), file system state machines, cost estimation, and architectural reduction. |
| [API Design](api-design/README.md) | `1.2.24` | Comprehensive API design skill for REST, GraphQL, gRPC, and Python library architectures. Design endpoints, schemas, authentication, pagination, error handling, and federation. |
| [BDI Mental States](bdi-mental-states/README.md) | `1.0.5` | Belief-Desire-Intention cognitive architecture for LLM agents. Formal BDI ontology, T2B2T paradigm, RDF integration, SPARQL competency queries, and neuro-symbolic AI integration patterns. |
| [CI/CD Pipelines](cicd-pipelines/README.md) | `1.1.24` | Comprehensive CI/CD pipeline design, DevOps automation, infrastructure as code, GitOps deployment automation, security scanning, and enterprise pipeline readiness. |
| [Cloud Infrastructure](cloud-infrastructure/README.md) | `1.0.0` | Infrastructure-as-code with Terraform and AWS CDK, cloud architecture patterns, cost optimisation, and multi-region deployment design. |
| [Code Review](code-review/README.md) | `1.1.25` | Perform thorough code reviews with multi-agent swarm analysis covering security, performance, style, tests, and documentation. Analyze PRs, extract and prioritize comments, and generate actionable fix plans. |
| [Coding Discipline](coding-discipline/README.md) | `1.0.0` | Research-grounded 5-principle behavioral contract for production LLM coding agents. Addresses named failure modes (test-gaming, phantom changes, scope creep, ego-signaling, confident hallucination) with empirical backing from SWE-bench, FeatBench, DELEGATE-52, and SE literature. Covers Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution, and Calibrated Communication — each with named anti-patterns, iteration budgets, and a structured completion schema. |
| [Database Design](database-design/README.md) | `1.0.0` | SQL schema design, ORM patterns, migration strategies, query optimisation, and data-modelling for relational databases. |
| [Debugging](debugging/README.md) | `1.1.27` | Comprehensive debugging skill combining systematic debugging methodology, browser DevTools automation, E2E testing with visual analysis, CI/CD pipeline debugging, performance profiling, and AI-powered error analysis. |
| [Docker Containerization](docker-containerization/README.md) | `1.1.23` | Comprehensive Docker and containerization skill covering Docker basics, multi-stage builds, Docker Compose orchestration, container optimization, development environment setup, and infrastructure patterns. |
| [Documentation Generator](documentation-generator/README.md) | `1.2.1` | Generate repository documentation at the right scale, from lightweight README updates to full codebase documentation sets with API, architecture, quality, and gaps coverage. |
| [Edge Case Coverage](edge-case-coverage/README.md) | `1.0.11` | Identify and document boundary conditions, error scenarios, corner cases, and validation requirements. |
| [Frontend Design](frontend-design/README.md) | `1.1.24` | Comprehensive Frontend Design (UI/UX) skill combining UI design systems, component libraries, CSS/Tailwind styling, accessibility patterns, and visual design. |
| [Git Workflow](git-workflow/README.md) | `1.1.21` | Comprehensive Git workflow management skill covering conventional commits, commit quality analysis, intelligent file grouping, worktree management with GitFlow conventions, issue tracking integration, changelog generation, semantic versioning, and hierarchical story backlog management. |
| [Gws Cli](gws-cli/README.md) | `1.0.1` | Google Workspace CLI (gws) skill for managing Drive, Gmail, Sheets, Calendar, Docs, Chat, Tasks, and 11 more Workspace APIs from the command line. Dynamic Discovery-based commands, helper shortcuts, schema introspection, and cross-service workflows. |
| [Hosted Agents](hosted-agents/README.md) | `1.0.5` | Infrastructure patterns for hosted background agents. Sandbox environments, image registry pattern, self-spawning agents, multiplayer support, warm pools, and multi-client integration (Slack, web, Chrome). |
| [MCP Server](mcp-server/README.md) | `1.2.21` | Comprehensive MCP (Model Context Protocol) server development skill. Build, configure, and manage MCP servers using Python (FastMCP) or TypeScript. Covers agent-centric design, tool creation, evaluation testing, production deployment, Claude Code integration, and plugin development. |
| [Multi Agent Patterns](multi-agent-patterns/README.md) | `1.0.5` | Architecture patterns for multi-agent LLM systems. Supervisor/orchestrator, peer-to-peer/swarm, hierarchical patterns, context isolation, consensus mechanisms, and the telephone game solution. |
| [Navigation Design](navigation-design/README.md) | `1.0.11` | Design information architecture, wayfinding systems, breadcrumbs, and navigation patterns for documentation and applications. |
| [Next.js Development](nextjs-development/README.md) | `2.0.24` | Comprehensive Next.js development skill covering App Router (13+/15/16), Server Components, Server Actions, Cache Components, data fetching patterns, and module architecture. |
| [Python Development](python-development/README.md) | `1.1.25` | Comprehensive Python development skill covering modern tooling (uv, ruff, mypy, pytest), best practices, coding standards, library architecture, functional patterns, async programming, MicroPython, and production-grade development workflows. |
| [React Development](react-development/README.md) | `1.1.21` | Build production-grade React applications and component libraries with shadcn/ui components, optimized hooks, client-side state patterns, and Bulletproof React architecture. |
| [Security Engineering](security-engineering/README.md) | `1.0.0` | Application security design, OWASP patterns, authentication architecture, secrets management, and threat-model-informed code review. |
| [Test Driven Development](test-driven-development/README.md) | `1.1.18` | Comprehensive Test-Driven Development skill implementing Red-Green-Refactor cycle across Python, TypeScript, JavaScript, and Emacs Lisp. Covers pytest, Vitest, Playwright, ERT, and Zod. |
| [Testing Framework](testing-framework/README.md) | `1.1.24` | Test framework router and infrastructure setup across multiple languages and platforms. Selects focused modules for unit, integration, E2E, accessibility, mutation, fuzz, and CI/CD test integration. |
| [Tool Design](tool-design/README.md) | `1.0.5` | Design tools optimized for LLM agents rather than human developers. Consolidation principle, architectural reduction, tool description engineering, MCP naming, and the file system agent pattern. |
| [Typescript Development](typescript-development/README.md) | `1.1.21` | Comprehensive TypeScript development skill covering type system mastery, runtime validation (Zod, TypeBox, Valibot), framework integration (React 19, Next.js 16, NestJS, React Native), architecture patterns, security, tsconfig optimization, and testing strategies. |

### 📌 Managerial Product (14)

| Plugin | Version | Description |
|--------|---------|-------------|
| [Brainstorm Swarm](brainstorm-swarm/README.md) | `1.1.0` | Run a parallel persona-swarm interview to brainstorm any complex decision — feature design, architecture choice, content piece, organizational change, product strategy. Spawns 6-12 persona-distinct subagents in parallel (PM, Engineer, Designer, Skeptic, User Advocate, Pre-Mortem Specialist, Junior, Veteran, First-Principles Thinker, Constraint-Setter, Optimist, Operator), each interviewing the user from their perspective and contributing questions, concerns, and ideas. Synthesizes the multi-perspective output into consensus, dissent, and open-questions. Use when the user asks to brainstorm with multiple perspectives, run a persona swarm, get a virtual roundtable, workshop an idea from PM/engineer/designer/skeptic angles, pre-mortem a decision, or think through something from different angles. NOT for code review (use code-review). NOT for single-perspective interviews (use elicitation or deep-interview). NOT for executing or building (use team, autopilot, or multi-agent-patterns). NOT for creating product personas as artifacts (use persona-definition). NOT for stakeholder mapping (use persona-mapping). |
| [Cloud FinOps](cloud-finops/README.md) | `2.1.2` | Expert Cloud FinOps guidance covering AI cost management, GenAI capacity planning, AI-powered FinOps automation, cloud billing (AWS, Azure, GCP, OCI), Kubernetes/container FinOps, serverless FinOps, data platform FinOps (Kafka, OpenSearch, Redis/Valkey), multi-cloud normalization (FOCUS spec), commitment strategy, tagging governance, SaaS asset management, ITAM, and GreenOps. Includes 26 domain-specific reference files grounded in enterprise delivery experience. Built by OptimNow and Viktor Bezdek, licensed CC BY-SA 4.0. |
| [Competitive Intelligence](competitive-intelligence/README.md) | `1.0.0` | Competitor analysis, market sizing, positioning maps, win/loss pattern synthesis, and battlecard creation for product and GTM decisions. |
| [Content Modelling](content-modelling/README.md) | `1.0.12` | Design content models with types, fields, relationships, and governance rules for structured content systems. |
| [Creative Problem Solving](creative-problem-solving/README.md) | `1.0.16` | Generate breakthrough solutions through lateral thinking, first principles reasoning, game theory, and strategic reframing. |
| [Ontology Design](ontology-design/README.md) | `1.0.11` | Design knowledge models with classes, properties, relationships, and taxonomies for structured data representation. |
| [Outcome Orientation](outcome-orientation/README.md) | `1.0.11` | Focus on measurable outcomes using OKRs, results-driven thinking, and outcome vs output distinction. |
| [Persona Definition](persona-definition/README.md) | `1.0.11` | Create detailed user personas with demographics, goals, pain points, behaviors, and empathy maps. |
| [Persona Mapping](persona-mapping/README.md) | `1.0.11` | Map stakeholders and personas using Power-Interest matrices, RACI charts, and influence analysis. |
| [Prioritization](prioritization/README.md) | `1.0.11` | Apply prioritization frameworks including RICE, MoSCoW, ICE scoring, and effort-impact matrices for decision-making. |
| [Product Thinking](product-thinking/README.md) | `1.0.1` | Five composable product-thinking skills: frame the real problem (JTBD, 5-whys), identify user needs (functional/emotional/social jobs), design value propositions (VPC, Kano), apply outcome-over-output thinking (North Star, leading/lagging metrics), and analyze trade-offs (cost-benefit, opportunity cost, reversibility, second-order effects). |
| [Risk Management](risk-management/README.md) | `1.0.12` | Apply risk assessment frameworks, mitigation strategies, risk registers, and monitoring practices. |
| [Systems Thinking](systems-thinking/README.md) | `1.0.11` | Apply systems thinking principles including feedback loops, leverage points, and system dynamics to analyze complex problems. |
| [User Journey Design](user-journey-design/README.md) | `1.0.11` | Design user journey maps with touchpoints, emotional states, pain points, and opportunities. |

### 📌 Marketing Comms (7)

| Plugin | Version | Description |
|--------|---------|-------------|
| [Communication](communication/README.md) | `1.0.1` | Five composable communication skills for people who write for work: structure a written piece (BLUF, Minto Pyramid), edit for clarity and conciseness (active voice, hedge removal), align stakeholders (RFCs, proposals, decision docs with DACI/RAPID roles), apply documentation discipline (ADRs, runbooks, decision logs), and communicate visually (Mermaid flowcharts, sequence diagrams, C4, diagram-as-code). |
| [Deslop](deslop/README.md) | `1.0.0` | Remove AI slop from UI copy, marketing text, and product content. Three focused skills: UI microcopy cleanup, marketing and editorial humanization, and AI-detection prevention. |
| [Email Marketing](email-marketing/README.md) | `1.0.0` | Email newsletters, drip sequences, subject line optimisation, onboarding emails, and plain-language transactional email copy. |
| [Social Media Content](social-media-content/README.md) | `1.0.0` | LinkedIn posts, Twitter/X threads, short-form social content, platform-native tone adaptation, and engagement-optimised formatting. |
| [Storytelling](storytelling/README.md) | `1.0.1` | Storytelling craft and application across fiction, business, data, speech, UX, and interactive narrative. Covers structural frameworks (3-act, Hero's Journey, Story Circle, Kishōtenketsu, Save the Cat, StoryBrand, Pixar Spine, Monroe's Motivated Sequence), narrative craft (character design, scene construction, dialogue, POV, pacing), domain applications, narrative theory (Propp, Polti, Booker, Tobias, Campbell), and anti-patterns. Progressive-disclosure structure with 12 domain references. |
| [Technical Copywriting](technical-copywriting/README.md) | `1.1.0` | Five composable skills for writing long-form technical content for an audience — articles, deep-dives, tutorials, newsletters, whitepapers, technical essays. Covers research before craft (audience profiling, source tiering, triangulation, citation), long-form structure (article templates, hook-promise-payoff contract, section transitions, length strategy), engaging craft (AIDA, PAS, Bencivenga's pyramid, Sugarman's slippery slide, Schwartz awareness levels, hooks, voice, concrete-over-abstract), long-form polish (pacing, scan-ability, the 30% cut, read-aloud test), and distribution craft (titles, dek/meta, social pull-quotes, channel framing). Grounded in proven copywriting techniques and evidence-based research workflow. Use when writing a technical blog post, deep-dive, tutorial, newsletter issue, whitepaper, or 1500-5000+ word technical essay. NOT for code documentation (use documentation-generator), UX microcopy (use ux-writing), short-form work writing like RFCs and emails (use communication), fiction or narrative craft (use storytelling), or CMS content models (use content-modelling). |
| [UX Writing](ux-writing/README.md) | `1.0.11` | Write effective microcopy, error messages, button labels, and interface text using UX writing principles. |

### 📌 Meta Infra (18)

| Plugin | Version | Description |
|--------|---------|-------------|
| [Agent Evaluation](agent-evaluation/README.md) | `1.0.5` | Comprehensive evaluation framework for LLM agent systems. Multi-dimensional rubrics, LLM-as-judge with bias mitigation, pairwise comparison, direct scoring, confidence calibration, and continuous monitoring. |
| [Consistency Standards](consistency-standards/README.md) | `1.0.11` | Establish and maintain naming conventions, taxonomy standards, style guides, and reuse patterns across documentation and code. |
| [Context Compression](context-compression/README.md) | `1.0.11` | Production strategies for compressing LLM context windows. Anchored iterative summarization, opaque compression, tokens-per-task optimization, and probe-based evaluation. |
| [Context Degradation](context-degradation/README.md) | `1.0.11` | Patterns for recognizing and mitigating context failures in LLM agents. Covers lost-in-middle, context poisoning, distraction, confusion, clash, and model-agnostic degradation measurement. |
| [Context Fundamentals](context-fundamentals/README.md) | `1.0.6` | Foundational understanding of context engineering for AI agent systems. Covers context anatomy, attention mechanics, progressive disclosure, context budgeting, and the quality-vs-quantity principle. |
| [Context Optimization](context-optimization/README.md) | `1.0.11` | Techniques for extending effective context capacity through compaction, observation masking, KV-cache optimization, and context partitioning. Double or triple effective context without larger models. |
| [Critical Intuition](critical-intuition/README.md) | `1.0.16` | Detect hidden patterns, expose blind spots, and deliver rigorous critical analysis with intuition-level depth. |
| [Elicitation](elicitation/README.md) | `2.0.1` | Psychological elicitation and deep-interview design using narrative identity (McAdams), self-defining memories (Singer), Motivational Interviewing (OARS), values elicitation (Schwartz), schema detection (Young), life review (Haight/Birren), and linguistic analysis (Pennebaker/LIWC). Progressive-disclosure structure with 8 domain references. |
| [Example Design](example-design/README.md) | `1.0.11` | Design effective code examples, tutorials, and runnable samples with progressive complexity. |
| [Filesystem Context](filesystem-context/README.md) | `1.0.14` | Filesystem-based context engineering patterns for LLM agents. Scratch pads, plan persistence, sub-agent communication, dynamic skill loading, terminal persistence, and self-modification patterns. |
| [Hindsight](hindsight/README.md) | `1.0.0` | Long-term memory for Claude Code backed by Hindsight. Hooks recall relevant memories before every prompt and retain the conversation after each turn via the installed `hindsight` CLI (external API). Includes a skill for manual recall/reflect/retain and bank management. |
| [Memory Systems](memory-systems/README.md) | `1.0.6` | Production memory architectures for LLM agents. Compares Mem0, Zep/Graphiti, Letta, Cognee, LangMem with benchmarks. Covers temporal knowledge graphs, memory consolidation, and retrieval strategies. |
| [OSINT](osint/README.md) | `1.0.1` | OSINT intelligence skill: systematic person research from name/handle to scored dossier with psychoprofile, career map, and confidence grades. 57+ Apify actors, 7 search APIs, swarm mode. |
| [Plugin Dev](plugin-dev/README.md) | `1.2.0` | End-to-end Claude Code plugin authoring toolkit. 8 skills covering the full lifecycle: ideation, research, architecture, hooks, composition, validation, evaluation, and documentation generation. Plus 4 runnable scripts: plugin scaffolder, structural validator, eval harness, and hook tester. Document any plugin by URL or local path with comprehensive README generation. |
| [Prompt Engineering](prompt-engineering/README.md) | `1.1.16` | Comprehensive prompt optimization system for LLMs. Design effective AI interactions, evaluate prompt quality, and perform iterative refinement for any LLM platform. |
| [Research Synthesis](research-synthesis/README.md) | `1.0.0` | Multi-source research coordination, evidence triangulation, competing-hypothesis analysis, and structured synthesis for knowledge-intensive tasks. |
| [Skill Foundry](skill-foundry/README.md) | `2.2.2` | Framework for creating Claude Code skills using philosophy-first design, evidence-based prompting, progressive disclosure, and anti-pattern prevention. 47 references, 25 scripts, 17 templates, 23 examples. |
| [Skillstack Workflows](skillstack-workflows/README.md) | `2.2.1` | Twenty composable workflow playbooks that orchestrate existing SkillStack plugins for real multi-stage problems: plugin authoring, plugin updating, plugin/skill evaluation, API-to-production, security hardening, codebase onboarding, product stories, context engineering, design review, agent improvement, stakeholder storytelling, pitch sprints, complex debugging, AI agent building, strategic decisions, content platforms, user research, legacy rescue, LLM cost optimization, and skill authoring. Each workflow is a self-contained playbook with phase-by-phase guidance, gates/loops, and explicit references to the underlying SkillStack skills. |

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

*Auto-generated from [registry.json](.claude-plugin/registry.json) · Last updated: 2026-07-28*
