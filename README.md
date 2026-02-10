<div align="center">
<img src="assets/hero.svg" alt="SkillStack" width="100%" />
</div>

# SkillStack

A curated collection of 34 production-grade skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Each skill extends Claude with deep domain expertise, ready-to-use templates, and automation scripts across full-stack development, DevOps, testing, API design, and strategic thinking.

<div align="center">

**[Install](#installation)** &nbsp;&middot;&nbsp; **[Browse Skills](#skill-catalog)** &nbsp;&middot;&nbsp; **[Examples](#usage-examples)** &nbsp;&middot;&nbsp; **[Architecture](#architecture)** &nbsp;&middot;&nbsp; **[Contributing](#contributing)**

</div>

---

## The Problem

Claude Code is powerful out of the box, but it doesn't know your team's conventions, your preferred frameworks' latest patterns, or the specific anti-patterns you've been burned by. You end up repeating the same corrections across conversations.

**SkillStack fixes this.** Each skill is a focused expert system that activates automatically when relevant, giving Claude deep knowledge of specific domains — from Next.js 16 App Router patterns to pytest fixture strategies to Docker multi-stage build optimization.

---

## Installation

### Option A: Install as a plugin (recommended)

```bash
claude plugin add /path/to/skillstack
```

### Option B: Clone and configure

```bash
git clone https://github.com/viktorbezdek/skillstack.git
```

Then add to your project's `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": ["skill:*"]
  }
}
```

### Option C: Pick individual skills

```bash
# Symlink only what you need
ln -s /path/to/skillstack/api-design .claude/skills/api-design
ln -s /path/to/skillstack/debugging .claude/skills/debugging
```

### How it works

Skills activate automatically based on your conversation. No special syntax needed — when you mention "REST API design", the `api-design` skill loads. When you say "pytest fixtures", the `testing-framework` skill kicks in.

---

## Usage Examples

**API Design** — Ask Claude to design an API and it uses REST/GraphQL best practices, pagination patterns, and auth strategies from the skill:
```
"Design a REST API for a multi-tenant SaaS billing system with usage-based pricing"
```

**Debugging** — Describe a bug and Claude applies systematic debugging methodology with evidence-based root cause analysis:
```
"My Next.js app hydration fails only in production. Help me debug this systematically"
```

**Code Review** — Request a review and Claude runs a multi-agent analysis covering security, performance, and architecture:
```
"Review this PR for security issues and performance bottlenecks"
```

**Docker** — Ask about containerization and Claude generates optimized Dockerfiles with multi-stage builds and security best practices:
```
"Create a production Docker setup for my Python FastAPI app with PostgreSQL"
```

**Testing** — Describe what to test and Claude generates comprehensive test suites following TDD patterns:
```
"Write pytest tests for this authentication service with edge cases for token expiry"
```

---

## Skill Catalog

> Click any skill name to view its detailed documentation, including full file listings, usage examples, and quick start guides.

### Development (7 skills)

| Skill | Problem it Solves | What You Get |
|-------|-------------------|-------------|
| **[python-development](python-development/)** | Inconsistent Python project setup, missing type safety, outdated tooling | Modern tooling (uv, ruff, mypy), async patterns, FastAPI templates, package architecture guides |
| **[typescript-development](typescript-development/)** | Weak type safety, inconsistent validation, no architecture patterns | Zod/TypeBox runtime validation, Clean Architecture templates, branded types, strict tsconfig guides |
| **[react-development](react-development/)** | Component bloat, poor performance, accessibility gaps | React 19 patterns, hooks optimization, Bulletproof React architecture, accessibility checklists |
| **[nextjs-development](nextjs-development/)** | Confusion between App Router patterns, caching pitfalls, migration pain | Next.js 16 Server Components, Server Actions, `use cache` directive, rendering strategy decision trees |
| **[frontend-design](frontend-design/)** | Inconsistent UI, missing design tokens, poor accessibility | Tailwind/shadcn/Radix component library, WCAG 2.1 AA checklists, design token system generator |
| **[prompt-engineering](prompt-engineering/)** | Ineffective LLM prompts, no evaluation methodology | 4-D optimization framework, A/B testing templates, platform-specific tuning, eval rubrics |
| **[skill-creator](skill-creator/)** | No structured way to capture and share domain expertise | Philosophy-first skill design, progressive disclosure templates, anti-pattern prevention, validation scripts |

### DevOps & Infrastructure (3 skills)

| Skill | Problem it Solves | What You Get |
|-------|-------------------|-------------|
| **[cicd-pipelines](cicd-pipelines/)** | Manual deployments, missing security scanning, inconsistent release process | GitHub Actions/GitLab CI templates, Terraform IaC patterns, DevSecOps scanning, semantic versioning automation |
| **[docker-containerization](docker-containerization/)** | Bloated images, insecure containers, complex multi-service setups | Multi-stage build templates, Docker Compose orchestration, worktree isolation, port allocation scripts |
| **[git-workflow](git-workflow/)** | Messy commit history, manual changelogs, worktree management | Conventional commits, atomic commit strategies, changelog generators, worktree management scripts |

### Quality & Testing (4 skills)

| Skill | Problem it Solves | What You Get |
|-------|-------------------|-------------|
| **[test-driven-development](test-driven-development/)** | Writing tests after the fact, poor coverage, no TDD discipline | Red-Green-Refactor workflow for pytest/Vitest/Playwright, multi-language TDD templates |
| **[testing-framework](testing-framework/)** | Choosing the right test tool, missing test types, no CI integration | Unit/E2E/component/accessibility/mutation/fuzz testing templates, CI integration scripts |
| **[debugging](debugging/)** | Trial-and-error debugging, no systematic approach | Chrome DevTools automation, systematic root cause analysis, CI/CD pipeline debugging, trace analysis |
| **[code-review](code-review/)** | Shallow reviews that miss security and performance issues | Multi-agent swarm analysis (security + performance + style + tests), PR comment extraction, actionable fix plans |

### API & Architecture (2 skills)

| Skill | Problem it Solves | What You Get |
|-------|-------------------|-------------|
| **[api-design](api-design/)** | Inconsistent API patterns, missing pagination/auth/versioning | REST/GraphQL/gRPC design guides, OpenAPI templates, authentication patterns, rate limiting strategies |
| **[mcp-server](mcp-server/)** | No guidance for building Claude Code plugins and MCP servers | Python FastMCP + TypeScript templates, tool creation patterns, evaluation testing, deployment guides |

### Documentation (2 skills)

| Skill | Problem it Solves | What You Get |
|-------|-------------------|-------------|
| **[documentation-generator](documentation-generator/)** | Outdated or missing docs, no automated generation | 6-phase doc generation workflow, 24 templates (API docs, ADRs, changelogs), drift detection scripts |
| **[workflow-automation](workflow-automation/)** | Manual repetitive tasks, no orchestration patterns | CI/CD automation, multi-agent workflows, release automation, git workflow management scripts |

### Strategic Thinking (2 skills)

| Skill | Problem it Solves | What You Get |
|-------|-------------------|-------------|
| **[creative-problem-solving](creative-problem-solving/)** | Stuck on a problem, can't see alternatives | Game theory, first principles, lateral thinking, SCAMPER, probabilistic reasoning frameworks |
| **[critical-intuition](critical-intuition/)** | Hidden assumptions, blind spots, overconfidence | Pattern recognition, Bayesian reasoning, bias detection, anomaly identification, confidence calibration |

### Helper Skills (14 focused frameworks)

These lightweight skills provide focused frameworks used by `documentation-generator` and other skills. Each solves a specific documentation or analysis challenge:

| Skill | What it Does | Example Use |
|-------|-------------|-------------|
| **[consistency-standards](consistency-standards/)** | Naming conventions, style guides | "Establish naming conventions for our API endpoints" |
| **[content-modelling](content-modelling/)** | CMS schemas, content types | "Design a content model for a multi-language blog" |
| **[edge-case-coverage](edge-case-coverage/)** | Boundary conditions, error scenarios | "What edge cases should I test for this date parser?" |
| **[example-design](example-design/)** | Progressive complexity examples | "Create a tutorial progression for our SDK" |
| **[navigation-design](navigation-design/)** | Information architecture, wayfinding | "Design the navigation structure for our docs site" |
| **[ontology-design](ontology-design/)** | Knowledge models, taxonomies | "Model the entity relationships for our product catalog" |
| **[outcome-orientation](outcome-orientation/)** | OKRs, success metrics | "Define measurable outcomes for this feature launch" |
| **[persona-definition](persona-definition/)** | User personas, empathy maps | "Create personas for our developer platform" |
| **[persona-mapping](persona-mapping/)** | Stakeholder analysis, RACI | "Map stakeholders for this cross-team initiative" |
| **[prioritization](prioritization/)** | RICE scoring, effort-impact analysis | "Prioritize this backlog of 20 feature requests" |
| **[risk-management](risk-management/)** | Risk registers, mitigation | "Identify risks for migrating our monolith to microservices" |
| **[systems-thinking](systems-thinking/)** | Feedback loops, leverage points | "Analyze why our deploy frequency keeps dropping" |
| **[user-journey-design](user-journey-design/)** | Journey maps, touchpoints | "Map the onboarding journey for new users" |
| **[ux-writing](ux-writing/)** | Microcopy, error messages | "Write user-friendly error messages for our auth flow" |

---

## Architecture

### Skill Structure

Every skill follows a consistent, composable structure:

```
skill-name/
├── SKILL.md                    # Core documentation with quick start
├── references/                 # Deep-dive guides (5-40 pages each)
│   └── extended-patterns.md    # Detailed examples and pattern catalogs
├── templates/                  # Copy-paste boilerplates
├── scripts/                    # Automation utilities
├── examples/                   # Complete, runnable code
└── assets/                     # Diagrams and data files
```

### Frontmatter Schema

Every SKILL.md starts with YAML frontmatter that powers automatic activation:

```yaml
---
name: api-design
description: Comprehensive API design for REST, GraphQL, gRPC architectures.
triggers:
  - API
  - endpoint
  - REST
  - GraphQL
  - OpenAPI
---
```

The `triggers` array is curated to catch relevant contexts without false positives.

### Composability

Skills compose naturally — no conflicting advice, no overlapping territory:

- **typescript-development** + **nextjs-development** = Full-stack type safety
- **api-design** + **testing-framework** = Tested API contracts
- **cicd-pipelines** + **docker-containerization** = Container deployment pipeline
- **documentation-generator** + **skill-creator** = Building new skills

---

## What's Included

- **34 specialized skills** across 6 categories
- **785+ markdown documents** — guides, references, and checklists
- **500+ templates and scripts** — ready to use
- **52 automated tests** for core validation
- **CI pipeline** with shellcheck and pytest

---

## Contributing

We welcome contributions. See the [quality checklist](#quality-checklist) before submitting.

### Adding a New Skill

1. Create the directory: `mkdir -p my-skill/{references,templates,scripts,examples}`
2. Write `SKILL.md` with frontmatter (`name`, `description`, `triggers`)
3. Add references, templates, and examples
4. Submit a pull request updating this README

### Quality Checklist

- [ ] SKILL.md has substantive content (not just placeholders)
- [ ] Triggers are precise and tested in real conversations
- [ ] Examples are complete and runnable
- [ ] Templates are copy-paste ready
- [ ] Related skills are documented
- [ ] No conflicts with adjacent skills

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">

**Built for Claude Code. Made for production.**

</div>
