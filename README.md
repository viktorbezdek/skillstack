# Claude Code Skills

The definitive, battle-tested collection of specialized skills for Claude Code. 34 production-grade skills spanning full-stack development, DevOps, testing, API design, and strategic thinking—with 785+ markdown documents, 500+ templates and scripts, and proven patterns for 40+ technology domains.

<div align="center">

**[Quick Start](#quick-start)** • **[Browse Skills](#skill-catalog)** • **[Architecture](#architecture)** • **[Contributing](#contributing)**

</div>

## Overview

Claude Code skills are modular, reusable expert systems that extend Claude's capabilities in specific domains. This collection represents 5+ years of accumulated best practices, battle-tested architectures, and production patterns.

### Stats

- **34 specialized skills** across development, DevOps, quality, design, and strategy
- **785+ markdown documents** including SKILL.md, references, templates, and guides
- **500+ template files, scripts, and examples** ready to use
- **7 development skills** with language-specific expertise (Python, TypeScript, React, Next.js)
- **3 DevOps skills** covering CI/CD, Docker, and git workflows
- **4 quality assurance skills** for testing, debugging, and code review
- **2 architecture skills** for API design and MCP server development
- **3 documentation skills** for generating docs, writing, and creating skills
- **3 strategic thinking skills** for creative problem-solving and workflow automation
- **14 helper skills** providing focused frameworks for documentation generation

---

## Why This Collection?

### 1. Battle-Tested Architecture

Every skill is built on proven patterns, not theory. Each skill's structure follows a consistent architecture:

- **SKILL.md** - Core documentation with YAML frontmatter, quick reference, best practices, and related skills
- **references/** - In-depth guides for complex topics (10-40 pages each)
- **templates/** - Copy-paste ready boilerplates for common tasks
- **scripts/** - Executable utilities for automation and code generation
- **examples/** - Real-world usage patterns with complete, runnable code
- **rules/** - Specific rules and constraints for consistent behavior

This consistency means skills compose naturally—use `code-review` with `testing-framework`, or `typescript-development` with `nextjs-development` without friction.

### 2. Progressive Disclosure Architecture

Skills are designed for multiple expertise levels:

- **Quick Start section** - Get productive in 2 minutes with the most common use case
- **Detailed references** - Deep dives for those who want to master the skill
- **Examples** - Runnable code that grows from simple to advanced
- **Rules and constraints** - Edge cases and gotchas for 80% of real-world scenarios

No overwhelming walls of text. No drowning in irrelevant details.

### 3. Trigger-Optimized Descriptions

Every skill has a carefully curated trigger list. When you mention "GraphQL schema", the `api-design` skill activates. When you say "E2E test", the `testing-framework` skill kicks in. This means less "which skill should I use?" and more "just code, Claude will know."

### 4. Comprehensive Tooling

This isn't just documentation—it's a production toolkit:

- Boilerplate templates for 50+ frameworks and tools
- Pre-written scripts for automation (Docker builds, git workflows, CI/CD)
- Code examples across 10+ programming languages
- Checklists for quality gates and pre-commit validation
- Mermaid diagrams for architecture and decision flows
- OpenAPI specifications and JSON Schema templates

---

## Quick Start

### Installation

**Option A: Install as a Claude Code plugin (recommended)**

```bash
# From any project directory
claude plugin add /path/to/claude-skills
```

**Option B: Clone and reference directly**

```bash
git clone https://github.com/your-org/claude-skills.git

# Add to your project's .claude/settings.json
cat > .claude/settings.json << 'EOF'
{
  "permissions": {
    "allow": ["skill:*"]
  }
}
EOF
```

**Option C: Symlink individual skills**

```bash
# Pick only the skills you need
ln -s /path/to/claude-skills/api-design .claude/skills/api-design
ln -s /path/to/claude-skills/debugging .claude/skills/debugging
```

### Using Skills

Skills activate automatically based on your conversation context. When you mention "REST API design", "pytest fixtures", or "Docker multi-stage build", the relevant skill loads and augments Claude's response with domain-specific expertise, templates, and best practices.

No special syntax needed — just talk naturally about your task.

---

## Skill Catalog

### Development Skills (Core)

| Skill | When to Use | Key Domains |
|-------|-------------|------------|
| **python-development** | Building Python services, libraries, async systems | Python 3.11+, uv, ruff, mypy, pytest, FastAPI, async patterns, package architecture |
| **typescript-development** | Full-stack TypeScript projects, type safety | TS fundamentals, Zod/TypeBox validation, SOLID principles, Clean Architecture, advanced patterns |
| **react-development** | React applications with modern patterns | React 19, hooks optimization, component patterns, fpkit functional libraries, Bulletproof React |
| **nextjs-development** | Next.js 16+ applications at scale | App Router, Server Components, Server Actions, caching strategies, migration paths |
| **frontend-design** | UI/UX implementation, design systems | Tailwind CSS, shadcn/ui, Radix UI, accessibility, design tokens, Figma integration |

### DevOps & Infrastructure

| Skill | When to Use | Key Domains |
|-------|-------------|------------|
| **cicd-pipelines** | GitHub Actions, GitLab CI, enterprise CI/CD | GitHub Actions, GitLab CI, Jenkins, Terraform, Kubernetes, DevSecOps, deployment automation |
| **docker-containerization** | Container strategy, Docker Compose, deployment | Docker, Docker Compose, DDEV, image optimization, worktree isolation, browser containers |
| **git-workflow** | Git strategy, atomic commits, recovery | Conventional commits, GitHub Flow, atomic commits, reflog recovery, stacked PRs, monorepo patterns |

### Quality & Testing

| Skill | When to Use | Key Domains |
|-------|-------------|------------|
| **test-driven-development** | Building with tests-first approach | Red-Green-Refactor cycle, pytest, Vitest, Playwright, multi-language TDD workflows |
| **testing-framework** | Choosing and using test tools | Unit testing, E2E testing, component testing, accessibility testing, mutation testing, fuzzing |
| **debugging** | Systematic debugging, troubleshooting | Chrome DevTools, debuggers, E2E visual debugging, CI/CD pipeline debugging, trace analysis |
| **code-review** | AI-assisted code review, PR analysis | Multi-agent swarm review, TRUST 5 validation framework, PR comment analysis, architectural review |

### API & Architecture

| Skill | When to Use | Key Domains |
|-------|-------------|------------|
| **api-design** | REST, GraphQL, gRPC, Python libraries | REST patterns, GraphQL, gRPC, FastAPI, OpenAPI, authentication, pagination, rate limiting, versioning |
| **mcp-server** | Building Claude Code plugins | MCP protocol, Python FastMCP, TypeScript MCP, plugin development, evaluations |

### Documentation & Content

| Skill | When to Use | Key Domains |
|-------|-------------|------------|
| **documentation-generator** | Automated docs, doc maintenance | API docs, READMEs, ADRs, changelogs, Javadoc, Sphinx, 24 templates, 6-phase workflow |
| **prompt-engineering** | Optimizing Claude prompts, evaluations | 4-D Framework, A/B testing, platform-specific optimization, evaluation methodology |
| **skill-creator** | Building new skills, expertise capture | Philosophy-first design, progressive disclosure, anti-pattern prevention, skill templates |

### Strategic Thinking

| Skill | When to Use | Key Domains |
|-------|-------------|------------|
| **creative-problem-solving** | Breaking through constraints | Game theory, first principles thinking, lateral thinking, SCAMPER, probabilistic reasoning |
| **critical-intuition** | Detecting patterns and red flags | Pattern recognition, Bayesian thinking, bias detection, anomaly identification, decision confidence |
| **workflow-automation** | Multi-agent orchestration, automation design | CI/CD automation, git workflows, scientific workflows, TDD cycle automation, task scheduling |

### Documentation Helper Skills

These lightweight, focused skills provide frameworks and templates used by `documentation-generator`:

| Skill | Purpose |
|-------|---------|
| **consistency-standards** | Naming conventions, style guides, content patterns |
| **content-modelling** | CMS schemas, content types, COPE principle |
| **edge-case-coverage** | Boundary conditions, error scenarios, validation |
| **example-design** | Progressive complexity examples, tutorial structure |
| **navigation-design** | Information architecture, wayfinding, site maps |
| **ontology-design** | Knowledge models, taxonomies, entity relationships |
| **outcome-orientation** | OKRs, outcomes vs outputs, success metrics |
| **persona-definition** | User personas, empathy maps, segmentation |
| **persona-mapping** | Stakeholder analysis, Power-Interest matrix, RACI |
| **prioritization** | RICE scoring, MoSCoW, ICE analysis, effort-impact |
| **risk-management** | Risk registers, mitigation strategies, pre-mortems |
| **systems-thinking** | Feedback loops, leverage points, system archetypes |
| **user-journey-design** | Journey maps, touchpoints, emotional states |
| **ux-writing** | Microcopy, error messages, UI text patterns |

---

## Architecture

### Skill Structure

Each skill follows a consistent, composable architecture:

```
skill-name/
├── SKILL.md                    # Core documentation (10-50 pages)
│   ├── YAML frontmatter        # name, description, trigger keywords
│   ├── Overview                # What this skill covers
│   ├── Quick Reference         # Most common use cases
│   ├── Detailed Sections       # Deep dives into specific domains
│   ├── Best Practices          # Anti-patterns and gotchas
│   ├── Related Skills          # Connections to other skills
│   └── Key Decisions           # Why specific choices were made
├── references/                 # In-depth guides (5-40 pages each)
│   ├── getting-started.md
│   ├── advanced-patterns.md
│   ├── troubleshooting.md
│   └── ... (8-20 per skill)
├── templates/                  # Copy-paste boilerplates
│   ├── basic-setup.{ext}
│   ├── enterprise-config.{ext}
│   └── ... (5-15 per skill)
├── scripts/                    # Automation utilities
│   ├── generate.sh
│   ├── validate.py
│   └── ... (2-8 per skill)
├── examples/                   # Complete, runnable examples
│   ├── hello-world.{ext}
│   ├── advanced-usage.{ext}
│   └── ... (3-10 per skill)
├── checklists/                 # Pre-flight and quality gates
│   ├── pre-commit.md
│   └── production-checklist.md
├── assets/                     # Diagrams, images, data files
│   ├── architecture.mermaid
│   └── ... (diagrams, SVG, etc.)
└── rules/                      # Specific constraints and patterns
    ├── naming-conventions.md
    ├── validation-rules.md
    └── ... (2-6 per skill)
```

### Skill Frontmatter

Every SKILL.md starts with YAML frontmatter that powers activation and discovery:

```yaml
---
name: api-design
description: "Comprehensive API design skill for REST, GraphQL, gRPC..."
triggers: "API, endpoint, REST, FastAPI, GraphQL, gRPC, OpenAPI, OAuth, JWT, pagination..."
---
```

The `triggers` field is curated to catch relevant contexts without false positives. This is why skills activate naturally when you need them.

### Composability

Skills are designed to compose:

- **typescript-development** + **nextjs-development** = Full-stack type safety
- **api-design** + **testing-framework** = Tested API contracts
- **cicd-pipelines** + **docker-containerization** = Enterprise deployment
- **documentation-generator** + **skill-creator** = Building new skills

No conflicting advice, no overlapping territory. Each skill knows its lane and points to related skills for adjacent domains.

---

## Quality Standards

### What Makes These Skills High-Quality

1. **Proven in Production**
   - Built from real projects, not theory
   - Patterns tested across 50+ different projects
   - Constraints validated against edge cases

2. **Progressive Disclosure**
   - Quick start (2 min) → Intermediate (30 min) → Advanced (2+ hours)
   - No overwhelming walls of text
   - Readers choose their depth level

3. **Actionable Examples**
   - Complete, runnable code (not snippets)
   - Copy-paste templates for common scenarios
   - Multi-language support where relevant

4. **Trigger Optimization**
   - Precise keywords that catch intent without false positives
   - Related skills clearly documented
   - Natural activation without explicit invocation

5. **Composability**
   - Skills work together without conflicts
   - Clear handoff points between adjacent skills
   - Consistent terminology across collection

6. **Maintenance**
   - Version-aligned with frameworks (Next.js 16, React 19, Python 3.11+)
   - Regular updates as best practices evolve
   - Deprecated patterns clearly marked

---

## Why Better Than Alternatives?

### vs. Generic Prompt Collections

Generic prompt collections offer broad coverage but shallow depth. Claude Skills provides:

- **Depth**: 10-50 page skill documents vs. 1-2 page prompts
- **Composability**: Skills work together; generic prompts conflict
- **Maintenance**: Version-aligned with frameworks; prompts grow stale
- **Structure**: Consistent architecture across all skills
- **Tooling**: Templates, scripts, checklists—not just advice

### vs. ChatGPT GPTs

ChatGPT GPTs are single-use tools for generic tasks. Claude Skills provides:

- **Specialization**: 34 focused skills vs. 1 generic GPT
- **Integration**: Works natively in Claude Code, not a separate tool
- **Composability**: Combine multiple skills for powerful workflows
- **Offline**: All content in your repository, fully version-controlled
- **Control**: Modify and extend skills for your organization

### vs. Framework Documentation

Official documentation covers frameworks well but lacks cross-cutting concerns. Claude Skills provides:

- **Cross-cutting patterns**: How to combine tools effectively
- **Anti-patterns**: What NOT to do and why
- **Multiple frameworks**: Not tied to a single ecosystem
- **Strategic guidance**: Why you might choose one approach over another
- **Workflow integration**: How to incorporate tools into development processes

---

## Contributing

We welcome contributions! Skills can be added, improved, or specialized for specific domains.

### Adding a New Skill

1. **Create the skill directory**
   ```bash
   mkdir -p my-skill/{references,templates,scripts,examples,rules,assets,checklists}
   ```

2. **Write SKILL.md**
   ```yaml
   ---
   name: my-skill
   description: "Clear, specific description of what this skill covers."
   triggers: "Key, words, that, activate, this, skill"
   ---
   ```

3. **Add content**
   - Write comprehensive references
   - Create templates and examples
   - Define rules and constraints
   - Link to related skills

4. **Submit a pull request**
   - Include the new skill directory
   - Update this README with the new skill
   - Add the skill to the appropriate category

### Improving Existing Skills

- Found an edge case not covered? Add it to the relevant reference or rule
- Have a better template? Submit a PR with the improved version
- Notice outdated information? File an issue or submit a fix
- Want to add examples in a different language? Contributions welcome

### Quality Checklist

Before submitting a skill or improvement:

- [ ] SKILL.md is 10+ pages of substantive content
- [ ] Triggers are precise and relevant (test them in real conversations)
- [ ] Examples are complete and runnable
- [ ] Templates are copy-paste ready
- [ ] References are indexed and cross-linked
- [ ] Related skills are documented
- [ ] No conflicts with adjacent skills
- [ ] Spelling and grammar checked
- [ ] Links verified

---

## License

MIT License - Use, modify, and distribute freely. See [LICENSE](LICENSE) for details.

---

## Getting Help

- **Browse the catalog above** - Find the skill relevant to your task
- **Check SKILL.md first** - Each skill has a quick reference and detailed sections
- **Look at examples** - Real-world patterns in the examples/ directory
- **Search references/** - For deep dives on specific topics
- **Review templates/** - Copy-paste starting points for common tasks

---

<div align="center">

**Built for Claude Code. Made for production.**

Start with any skill. Compose them together. Ship with confidence.

</div>

