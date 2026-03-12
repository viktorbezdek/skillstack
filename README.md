<div align="center">
<img src="assets/hero.svg" alt="SkillStack" width="100%" />
</div>

# SkillStack

34 individually installable skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Browse the catalog, install only what you need, and extend Claude with deep domain expertise.

<div align="center">

**[Install a Skill](#installation)** &nbsp;&middot;&nbsp; **[Browse Catalog](#skill-catalog)** &nbsp;&middot;&nbsp; **[Usage Examples](#usage-examples)** &nbsp;&middot;&nbsp; **[Create Your Own](#contributing)**

</div>

---

## Installation

Each skill is an independent plugin. Install individually:

```bash
# Install a single skill
claude plugin add github:viktorbezdek/skillstack/api-design
claude plugin add github:viktorbezdek/skillstack/debugging
claude plugin add github:viktorbezdek/skillstack/python-development

# Install several at once
claude plugin add github:viktorbezdek/skillstack/react-development
claude plugin add github:viktorbezdek/skillstack/testing-framework
claude plugin add github:viktorbezdek/skillstack/typescript-development
```

Or install everything:

```bash
# Clone the full marketplace
git clone https://github.com/viktorbezdek/skillstack.git

# Install all skills at once
claude plugin add /path/to/skillstack
```

### How it works

Skills activate automatically based on your conversation. When you mention "REST API design", the `api-design` skill loads. When you say "pytest fixtures", the `testing-framework` skill kicks in. No special syntax needed.

---

## Usage Examples

```
"Design a REST API for a multi-tenant SaaS billing system"
→ api-design skill activates with REST patterns, auth strategies, pagination

"My Next.js app hydration fails only in production"
→ debugging skill activates with systematic root cause analysis

"Review this PR for security issues"
→ code-review skill runs multi-agent analysis (security + performance + style)

"Create a production Docker setup for my FastAPI app"
→ docker-containerization skill generates optimized multi-stage Dockerfiles

"Write pytest tests for this auth service with edge cases"
→ test-driven-development skill generates Red-Green-Refactor test suites
```

---

## Skill Catalog

> Click any skill name to view its detailed documentation, file listings, and usage examples.

### Development

| Skill | Install | Description |
|-------|---------|-------------|
| **[python-development](python-development/)** | `claude plugin add github:viktorbezdek/skillstack/python-development` | Modern Python with uv, ruff, mypy, pytest, FastAPI, async patterns |
| **[typescript-development](typescript-development/)** | `claude plugin add github:viktorbezdek/skillstack/typescript-development` | Zod/TypeBox validation, Clean Architecture, branded types, strict tsconfig |
| **[react-development](react-development/)** | `claude plugin add github:viktorbezdek/skillstack/react-development` | React 19, hooks optimization, Bulletproof React, accessibility |
| **[nextjs-development](nextjs-development/)** | `claude plugin add github:viktorbezdek/skillstack/nextjs-development` | Next.js 16 App Router, Server Components, caching strategies |
| **[frontend-design](frontend-design/)** | `claude plugin add github:viktorbezdek/skillstack/frontend-design` | Tailwind/shadcn/Radix, WCAG 2.1 AA, design tokens |
| **[prompt-engineering](prompt-engineering/)** | `claude plugin add github:viktorbezdek/skillstack/prompt-engineering` | 4-D optimization framework, A/B testing, eval rubrics |
| **[skill-creator](skill-creator/)** | `claude plugin add github:viktorbezdek/skillstack/skill-creator` | Create your own skills with progressive disclosure and validation |

### DevOps & Infrastructure

| Skill | Install | Description |
|-------|---------|-------------|
| **[cicd-pipelines](cicd-pipelines/)** | `claude plugin add github:viktorbezdek/skillstack/cicd-pipelines` | GitHub Actions, GitLab CI, Terraform, DevSecOps, semantic versioning |
| **[docker-containerization](docker-containerization/)** | `claude plugin add github:viktorbezdek/skillstack/docker-containerization` | Multi-stage builds, Docker Compose, worktree isolation |
| **[git-workflow](git-workflow/)** | `claude plugin add github:viktorbezdek/skillstack/git-workflow` | Conventional commits, changelog generation, worktree management |

### Quality & Testing

| Skill | Install | Description |
|-------|---------|-------------|
| **[test-driven-development](test-driven-development/)** | `claude plugin add github:viktorbezdek/skillstack/test-driven-development` | Red-Green-Refactor for pytest, Vitest, Playwright |
| **[testing-framework](testing-framework/)** | `claude plugin add github:viktorbezdek/skillstack/testing-framework` | Unit, E2E, component, accessibility, mutation, fuzz testing |
| **[debugging](debugging/)** | `claude plugin add github:viktorbezdek/skillstack/debugging` | Chrome DevTools automation, systematic root cause analysis |
| **[code-review](code-review/)** | `claude plugin add github:viktorbezdek/skillstack/code-review` | Multi-agent swarm review (security + performance + style) |

### API & Architecture

| Skill | Install | Description |
|-------|---------|-------------|
| **[api-design](api-design/)** | `claude plugin add github:viktorbezdek/skillstack/api-design` | REST, GraphQL, gRPC, OpenAPI, auth, pagination, rate limiting |
| **[mcp-server](mcp-server/)** | `claude plugin add github:viktorbezdek/skillstack/mcp-server` | Build MCP servers with FastMCP (Python) or TypeScript |

### Documentation & Automation

| Skill | Install | Description |
|-------|---------|-------------|
| **[documentation-generator](documentation-generator/)** | `claude plugin add github:viktorbezdek/skillstack/documentation-generator` | 6-phase doc generation, 24 templates, drift detection |
| **[workflow-automation](workflow-automation/)** | `claude plugin add github:viktorbezdek/skillstack/workflow-automation` | CI/CD automation, FABER state machine, release management |

### Strategic Thinking

| Skill | Install | Description |
|-------|---------|-------------|
| **[creative-problem-solving](creative-problem-solving/)** | `claude plugin add github:viktorbezdek/skillstack/creative-problem-solving` | Game theory, first principles, lateral thinking, SCAMPER |
| **[critical-intuition](critical-intuition/)** | `claude plugin add github:viktorbezdek/skillstack/critical-intuition` | Pattern recognition, Bayesian reasoning, bias detection |

### Helper Skills

Focused frameworks for specific tasks. Install individually or as companions to the skills above.

| Skill | Install | What it Does |
|-------|---------|-------------|
| **[consistency-standards](consistency-standards/)** | `claude plugin add github:viktorbezdek/skillstack/consistency-standards` | Naming conventions, style guides |
| **[content-modelling](content-modelling/)** | `claude plugin add github:viktorbezdek/skillstack/content-modelling` | CMS schemas, content types |
| **[edge-case-coverage](edge-case-coverage/)** | `claude plugin add github:viktorbezdek/skillstack/edge-case-coverage` | Boundary conditions, error scenarios |
| **[example-design](example-design/)** | `claude plugin add github:viktorbezdek/skillstack/example-design` | Progressive complexity examples |
| **[navigation-design](navigation-design/)** | `claude plugin add github:viktorbezdek/skillstack/navigation-design` | Information architecture, wayfinding |
| **[ontology-design](ontology-design/)** | `claude plugin add github:viktorbezdek/skillstack/ontology-design` | Knowledge models, taxonomies |
| **[outcome-orientation](outcome-orientation/)** | `claude plugin add github:viktorbezdek/skillstack/outcome-orientation` | OKRs, success metrics |
| **[persona-definition](persona-definition/)** | `claude plugin add github:viktorbezdek/skillstack/persona-definition` | User personas, empathy maps |
| **[persona-mapping](persona-mapping/)** | `claude plugin add github:viktorbezdek/skillstack/persona-mapping` | Stakeholder analysis, RACI |
| **[prioritization](prioritization/)** | `claude plugin add github:viktorbezdek/skillstack/prioritization` | RICE, MoSCoW, ICE scoring |
| **[risk-management](risk-management/)** | `claude plugin add github:viktorbezdek/skillstack/risk-management` | Risk registers, mitigation strategies |
| **[systems-thinking](systems-thinking/)** | `claude plugin add github:viktorbezdek/skillstack/systems-thinking` | Feedback loops, leverage points |
| **[user-journey-design](user-journey-design/)** | `claude plugin add github:viktorbezdek/skillstack/user-journey-design` | Journey maps, touchpoints |
| **[ux-writing](ux-writing/)** | `claude plugin add github:viktorbezdek/skillstack/ux-writing` | Microcopy, error messages |

---

## Skill Structure

Each skill is a standalone plugin with this structure:

```
skill-name/
├── plugin.json                 # Plugin manifest (name, version, description)
├── SKILL.md                    # Core skill instructions for Claude
├── README.md                   # Human-readable documentation
├── references/                 # Deep-dive guides
├── templates/                  # Copy-paste boilerplates
├── scripts/                    # Automation utilities
└── examples/                   # Runnable code examples
```

### Frontmatter

Every SKILL.md starts with YAML frontmatter for automatic activation:

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

---

## Contributing

### Creating a New Skill

1. Create a directory with `plugin.json` and `SKILL.md`
2. Add references, templates, scripts, and examples
3. Write a `README.md` documenting what's included
4. Submit a pull request

### Skill Quality Checklist

- [ ] `plugin.json` has name, version, description
- [ ] `SKILL.md` has valid frontmatter with triggers
- [ ] Examples are complete and runnable
- [ ] Templates are copy-paste ready
- [ ] `README.md` documents all included files

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">

**34 skills. Install what you need. Extend Claude your way.**

</div>
