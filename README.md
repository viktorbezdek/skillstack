<div align="center">
<img src="assets/hero.svg" alt="SkillStack" width="100%" />
</div>

# SkillStack

34 individually installable expert skills for AI coding assistants. First-class support for Claude Code with one-command install. Works with Cursor, Windsurf, Copilot, Cline, aider, and any AI tool that reads project files.

```bash
claude plugin add github:viktorbezdek/skillstack/python-development
```

<div align="center">

**[Install](#installation)** &nbsp;&middot;&nbsp; **[Browse Skills](#skill-catalog)** &nbsp;&middot;&nbsp; **[Examples](#usage-examples)** &nbsp;&middot;&nbsp; **[Other AI Tools](#using-with-other-ai-tools)** &nbsp;&middot;&nbsp; **[Contributing](#contributing)**

</div>

---

## Installation

### Claude Code (one command per skill)

```bash
claude plugin add github:viktorbezdek/skillstack/api-design
claude plugin add github:viktorbezdek/skillstack/debugging
claude plugin add github:viktorbezdek/skillstack/react-development
```

Skills activate automatically — mention "REST API" and the `api-design` skill loads. Say "pytest fixtures" and `testing-framework` kicks in. No special syntax.

### Install everything

```bash
git clone https://github.com/viktorbezdek/skillstack.git
claude plugin add /path/to/skillstack
```

---

## Using with Other AI Tools

Every skill is standard markdown with scripts and templates. The knowledge works with any AI coding assistant that reads project context.

### Cursor

Copy a skill's `SKILL.md` into your project or reference it in `.cursorrules`:

```bash
cp skillstack/python-development/SKILL.md .cursorrules
```

### Windsurf / Codeium

Add skill directories to your project workspace. Windsurf indexes markdown files automatically.

### GitHub Copilot

Copy skill content into `.github/copilot-instructions.md`:

```bash
cat skillstack/api-design/SKILL.md >> .github/copilot-instructions.md
```

### Cline / Continue.dev / aider

Add skill directories to your project. These tools read project files for context and will pick up the patterns, templates, and examples.

### What's universal vs Claude-specific

| Feature | Works everywhere | Claude Code only |
|---------|-----------------|-----------------|
| 785+ markdown guides and references | Yes | Yes |
| 500+ templates and scripts | Yes | Yes |
| Code examples and patterns | Yes | Yes |
| Automatic trigger-based activation | — | Yes |
| One-command plugin install | — | Yes |

---

## Usage Examples

```
"Design a REST API for a multi-tenant SaaS billing system"
→ api-design skill: REST patterns, auth strategies, pagination

"My Next.js app hydration fails only in production"
→ debugging skill: systematic root cause analysis

"Review this PR for security issues"
→ code-review skill: multi-agent analysis (security + performance + style)

"Create a production Docker setup for my FastAPI app"
→ docker-containerization skill: optimized multi-stage Dockerfiles

"Write pytest tests for this auth service with edge cases"
→ test-driven-development skill: Red-Green-Refactor test suites
```

---

## Skill Catalog

> Click any skill name for detailed documentation, file listings, and usage examples.

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

Each skill is a standalone plugin:

```
skill-name/
├── plugin.json                 # Plugin manifest
├── SKILL.md                    # Core instructions (AI reads this)
├── README.md                   # Human documentation
├── references/                 # Deep-dive guides
├── templates/                  # Copy-paste boilerplates
├── scripts/                    # Automation utilities
└── examples/                   # Runnable code
```

---

## Contributing

1. Create a directory with `plugin.json`, `SKILL.md`, and `README.md`
2. Add references, templates, scripts, and examples
3. Submit a pull request

### Quality Checklist

- [ ] `plugin.json` has name, version, description
- [ ] `SKILL.md` has valid YAML frontmatter with triggers
- [ ] Examples are complete and runnable
- [ ] `README.md` documents all included files

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">

**34 skills. Install what you need. Works with any AI coding assistant.**

</div>
