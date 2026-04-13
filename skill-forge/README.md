# Skill Creator

> **v1.1.19** | Development | 21 iterations

> Create high-quality Claude Code skills using philosophy-first design, evidence-based prompting, progressive disclosure architecture, and anti-pattern prevention.

## The Problem

Most Claude Code skills are checklists dressed up as expertise. They list steps to follow, templates to fill in, and rules to obey -- and the output converges to the same generic pattern regardless of context. The skill activates when it should not, stays silent when it should trigger, and when it does fire, it produces rigid, templated responses that do not adapt to the user's actual situation.

The deeper problem is that skill creators focus on procedure before philosophy. They write "Step 1: Do X, Step 2: Do Y" without establishing the mental framework that guides judgment when the steps do not apply. They stuff 800 lines of instructions into SKILL.md without progressive disclosure, burning through context tokens and degrading the model's attention. They reference scripts and files that do not exist, causing silent failures. They write descriptions that are either too vague ("Helps with development") or too narrow ("Use when running Docker Compose on Kubernetes"), missing the activation window entirely.

The result is a skill ecosystem where most skills are either over-engineered (an "Everything Skill" that tries to handle an entire domain) or under-designed (a thin wrapper around a template with no expert knowledge). Teams that want to encode their real domain expertise into reusable skills have no systematic methodology for doing it well.

## The Solution

This plugin provides a complete skill creation framework built on four pillars: Philosophy Before Procedure (establish "how to think" before "what to do"), Anti-Patterns as Guidance (what NOT to do is as important as what to do), Progressive Disclosure (core instructions in SKILL.md under 500 lines, details in references), and Shibboleths (encode the deep expert knowledge that separates novices from experts).

The skill offers two tracks based on complexity. The Minimal Workflow gets a simple skill from idea to working state in six steps: define scope, initialize with `init_skill.py`, write the description with keywords and NOT clauses, add anti-patterns, test activation, and validate. The Full Workflow uses an 8-phase methodology (Schema Definition through Metrics Tracking) for production-grade skills that need rigorous I/O contracts, adversarial testing, and enterprise validation.

Beyond the methodology, the plugin ships with 26 utility scripts (initialization, validation, analysis, documentation extraction, packaging), 55 reference files covering every aspect of skill design, 23 templates for SKILL.md files, helper scripts, and configuration, and 10 example skills showing the transformation from basic to effective.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Skills are checklists that produce the same rigid output regardless of context | Philosophy-first design establishes mental frameworks that guide context-appropriate variation |
| Description field is too vague or too narrow -- skill activates incorrectly | Description engineering formula: [What] [Use for] [Keywords] NOT for [Exclusions] -- precise activation |
| SKILL.md is 800+ lines, burning context tokens and degrading model attention | Progressive disclosure: SKILL.md under 500 lines, deep content in references loaded on demand |
| Skills reference scripts and files that do not exist -- silent failures | `check_self_contained.py` validates every reference, `validate_skill.py` checks structural integrity |
| Common domain mistakes go uncaught -- skill does not encode what NOT to do | Anti-pattern sections with "What it looks like / Why it's wrong / What to do instead" teach the model to avoid mistakes |
| No way to measure skill quality or track improvement over time | `analyze_skill.py` scores skills 0-100, `skill-metrics.yaml` tracks revision gains |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install skill-creator@skillstack
```

### Verify installation

After installing, test with:

```
I want to create a Claude Code skill for Kubernetes deployment best practices
```

The skill should activate and guide you through scope definition, description engineering, and the skill creation workflow.

## Quick Start

1. **Install** the plugin using the commands above
2. **Describe what expertise you want to encode**: `Create a skill that helps with PostgreSQL query optimization`
3. The skill **asks scope questions**: What specific PostgreSQL expertise? Which versions? What should it NOT handle?
4. It **generates the skill structure** with `init_skill.py`, writes a description with keywords and NOT clause, and produces the SKILL.md with philosophy, anti-patterns, and decision trees
5. **Validate and iterate**: `python scripts/quick_validate.py <path>` checks structure and references, `python scripts/analyze_skill.py <path>` scores quality 0-100

## What's Inside

This is a single-skill plugin with an extensive supporting ecosystem of scripts, references, templates, and examples.

| Component | Purpose |
|---|---|
| `SKILL.md` | Core methodology -- four pillars, decision trees, description engineering, anti-pattern format, quality heuristics, review checklist |
| 26 utility scripts | Initialization, validation, analysis, documentation extraction, packaging, agent generation |
| 55 reference files | Deep guidance on every aspect of skill design |
| 23 templates | SKILL.md starters, script boilerplate, configuration, metrics tracking, adversarial testing |
| 10 example skills | From basic to production-grade, with before/after transformations |

**Eval coverage:** 13 trigger evaluation cases, 3 output evaluation cases.

**Key scripts:**

| Script | Purpose |
|---|---|
| `init_skill.py` | Initialize skill directory structure with proper layout |
| `quick_validate.py` | Fast validation of skill structure and references |
| `validate_skill.py` | Full validation with detailed error reporting |
| `analyze_skill.py` | Quality scoring (0-100) with dimension breakdown |
| `upgrade_skill.py` | Generate improvement suggestions for existing skills |
| `package_skill.py` | Validate and package skill to distributable zip |
| `test_activation.py` | Test whether skill triggers correctly for given queries |
| `check_self_contained.py` | Verify all referenced files actually exist |
| `doc_extractor.py` | Extract documentation from URLs for skill creation |
| `doc_analyzer.py` | Analyze documentation structure for skill design |

**Key references:**

| Reference | Topic |
|---|---|
| `skill-forge.md` | Complete 8-phase methodology with detailed phase descriptions |
| `skill_creation.md` | 6-step skill creation workflow |
| `progressive_disclosure.md` | Loading architecture and context budget management |
| `core_principles.md` | Fundamental skill design principles |
| `anti-patterns.md` | Comprehensive anti-pattern catalog with examples |
| `shibboleths.md` | Expert vs novice knowledge encoding |
| `evidence-based-prompting.md` | Research-backed prompting techniques |
| `composability.md` | Skill composition patterns |
| `variation-patterns.md` | Output diversity techniques |
| `skill-factory-workflow.md` | Enterprise-scale skill production |
| `SKILL-AUDIT-PROTOCOL.md` | Audit methodology for existing skills |
| `agent-creator.md` | Creating agent-powered skill workflows |

### skill-creator

**What it does:** Activates when you want to create, review, improve, or debug Claude Code skills. Guides you through philosophy-first design, description engineering for correct activation, anti-pattern encoding, progressive disclosure architecture, and validation. Provides both a minimal workflow (6 steps for simple skills) and a full 8-phase methodology for production-grade skills.

**Try these prompts:**

```
Create a Claude Code skill for Terraform infrastructure management -- I want it to encode our team's best practices
```

```
Review this skill I wrote -- it's supposed to activate for Docker questions but it fires for every container-related query
```

```
This skill works but the output is too generic -- how do I encode expert-level knowledge and domain shibboleths?
```

```
I have API documentation at this URL -- turn it into a Claude Code skill that helps developers use this API correctly
```

```
My SKILL.md is 900 lines -- help me refactor it with progressive disclosure into a lean core with reference files
```

```
Score this skill on quality and tell me what to improve to get above 70/100
```

## Real-World Walkthrough

You are a senior DevOps engineer who has spent five years managing Kubernetes clusters. Your team keeps making the same mistakes: overly permissive RBAC roles, missing resource limits, pods running as root, and Helm charts with hardcoded values. You want to encode this expertise into a Claude Code skill so the entire team benefits from it every time they work with Kubernetes manifests.

You open Claude Code and say:

```
I want to create a skill for Kubernetes best practices -- focusing on security, resource management, and Helm chart quality
```

The skill activates and starts with **scope definition**. It asks three focused questions: (1) Which Kubernetes versions? (2) What should this skill NOT handle -- cluster provisioning, networking CNI choices, service mesh configuration? (3) What are the top 3 mistakes your team makes?

You answer: Kubernetes 1.28+, NOT for cluster setup or CNI configuration, top mistakes are running as root, missing resource limits, and overly broad RBAC.

The skill runs `python scripts/init_skill.py kubernetes-security --path ./skills/` to create the directory structure:

```
kubernetes-security/
├── SKILL.md
├── references/
├── scripts/
└── templates/
```

Next comes **description engineering**. The skill applies the formula: [What] [Use for] [Keywords] NOT for [Exclusions]. It produces:

```yaml
description: >-
  Kubernetes security and resource management best practices. Use when writing
  K8s manifests, YAML configs, Helm charts, RBAC roles, Pod security policies,
  or reviewing Kubernetes deployments. Activate on "kubectl", "helm", "pod",
  "deployment", "RBAC". NOT for cluster provisioning (use infrastructure skills),
  NOT for CNI or service mesh configuration.
```

The description includes specific trigger keywords (`kubectl`, `helm`, `pod`, `deployment`, `RBAC`) and clear exclusions. The skill explains why this matters: the description is the activation trigger, and vague descriptions cause either false activations (wasting tokens) or missed activations (skill never fires).

Now the skill guides you through **philosophy before procedure**. Instead of starting with "Step 1: Add resource limits", it helps you write a philosophy section:

```markdown
## Philosophy: Defense in Depth

Kubernetes security is not a checklist -- it is layered defense where each
layer assumes the layers above it have failed. A pod with proper resource
limits still needs restricted RBAC. A namespace with network policies still
needs pod security standards. If you are asking "do I really need this
layer?", the answer is yes.
```

This mental framework guides the model's judgment in situations the explicit rules do not cover.

The skill then helps you **encode anti-patterns** -- the mistakes you listed:

```markdown
### Anti-Pattern: Root Runner
**What it looks like**: No `securityContext` in pod spec, or `runAsUser: 0`
**Why it's wrong**: Container escape + root = full node access
**What to do instead**: `runAsNonRoot: true` + specific UID in securityContext
**How to detect**: grep for `runAsUser: 0` or missing securityContext
```

Each anti-pattern includes recognition criteria, the fundamental reason it is wrong (not just "it's insecure"), the correct alternative, and a detection method. This format teaches the model to catch these patterns proactively.

You add a **validation script** (`scripts/check_manifest.py`) that scans Kubernetes YAML files for the anti-patterns and produces a report. The skill references this script explicitly: "Run `python scripts/check_manifest.py <manifest.yaml>` to validate against security patterns."

After writing the core SKILL.md at 380 lines, you run validation:

```bash
python scripts/quick_validate.py ./skills/kubernetes-security/
# ✅ Structure valid
# ✅ All references exist
# ✅ Description has keywords and NOT clause
# ✅ Under 500 lines
```

Then quality analysis:

```bash
python scripts/analyze_skill.py ./skills/kubernetes-security/
# Score: 78/100
# ✅ Philosophy section present
# ✅ Anti-patterns with detection criteria
# ✅ Decision trees for common choices
# ⚠️ Missing temporal knowledge (what changed between K8s versions)
# ⚠️ No variation guidance for different environments (dev vs prod)
```

Based on the feedback, you add a temporal section ("Pre-1.25: PodSecurityPolicy, 1.25+: Pod Security Admission") and variation guidance ("Dev clusters: warn mode, Staging: enforce mode with exceptions, Production: enforce strict"). The score rises to 85/100.

The final skill has a clear philosophy, five encoded anti-patterns, a decision tree for RBAC scope selection, a validation script, and progressive disclosure with two reference files for Helm chart patterns and RBAC templates. It activates correctly for Kubernetes security questions and stays silent for cluster provisioning and networking.

## Usage Scenarios

### Scenario 1: Creating a skill from API documentation

**Context:** Your team uses a complex internal API with 40+ endpoints. New developers keep making the same mistakes: wrong authentication headers, missing pagination parameters, and incorrect error handling.

**You say:** `I have our API documentation at docs.internal.com/api -- turn it into a skill that helps developers use the API correctly`

**The skill provides:**
- Documentation extraction using `doc_extractor.py`
- Analysis of common patterns, authentication requirements, and error codes
- A SKILL.md with API usage patterns, anti-patterns (wrong auth, missing pagination), and decision trees
- Helper scripts for common API operations

**You end up with:** A skill that activates whenever a developer works with your API, proactively suggesting correct patterns and catching common mistakes before they ship.

### Scenario 2: Improving a skill that activates incorrectly

**Context:** You wrote a skill for "container development" but it fires for every Docker-related query, including basic `docker run` commands that do not need it.

**You say:** `My container skill triggers too broadly -- it fires for simple docker commands when it should only activate for Dockerfile optimization and multi-stage builds`

**The skill provides:**
- Diagnosis of the description field (too vague, missing NOT clauses)
- Rewritten description with specific activation keywords and exclusions
- `test_activation.py` results showing activation scores for target and non-target queries
- Suggestions for splitting the skill if scope is genuinely too broad

**You end up with:** A skill with precise activation: fires for Dockerfile optimization and multi-stage builds, stays silent for basic Docker commands.

### Scenario 3: Refactoring an over-engineered skill

**Context:** Your SKILL.md is 900 lines and tries to handle everything about database management. Quality has degraded because the context is too large.

**You say:** `My database skill is 900 lines and the output quality has dropped -- help me split it properly`

**The skill provides:**
- Progressive disclosure analysis: which content is core (needed every time) and which is reference (needed sometimes)
- Refactoring plan: keep decision trees and anti-patterns in SKILL.md, move detailed patterns to reference files
- Explicit triggers in SKILL.md for each reference file ("See `references/indexing-patterns.md` for index design")
- Validation that all references are connected and no orphaned sections exist

**You end up with:** A 400-line SKILL.md with focused core content and 4-5 reference files loaded on demand, improving both activation precision and output quality.

### Scenario 4: Enterprise skill factory workflow

**Context:** Your organization wants to create 15 skills encoding team expertise across infrastructure, security, and development. You need a repeatable, quality-controlled process.

**You say:** `We need to create 15 skills for our engineering org -- set up a factory workflow with quality gates`

**The skill provides:**
- Enterprise skill factory workflow from `skill-factory-workflow.md`
- Quality scoring rubric from `scoring-rubric.md` with minimum thresholds
- Audit protocol from `SKILL-AUDIT-PROTOCOL.md` for peer review
- Metrics tracking template for measuring skill effectiveness over time

**You end up with:** A repeatable process where each skill goes through scope definition, creation, validation (score >= 70), peer audit, and metrics tracking before deployment.

## Ideal For

- **Engineers encoding team expertise into reusable skills** -- the philosophy-first approach produces skills that adapt to context rather than outputting rigid templates
- **Skill authors who want activation precision** -- description engineering with the [What] [Use for] [Keywords] NOT for [Exclusions] formula eliminates false activations
- **Teams building skill libraries at scale** -- the enterprise factory workflow, quality scoring, and audit protocol ensure consistent quality across dozens of skills
- **Anyone improving an existing skill** -- `analyze_skill.py` produces a score with specific improvement suggestions, and `upgrade_skill.py` generates code changes

## Not For

- **General prompt engineering** -- use [prompt-engineering](../prompt-engineering/) for optimizing prompts that are not Claude Code skills
- **Building Claude Code plugins** -- use [plugin-dev](https://github.com/viktorbezdek/skillstack/tree/main/plugin-dev) for plugin architecture, composition, and validation; this skill focuses on the SKILL.md component
- **Agent runtime and orchestration** -- use [multi-agent-patterns](../multi-agent-patterns/) for designing multi-agent systems; this skill creates individual skills, not agent architectures

## How It Works Under the Hood

The plugin is a single skill with an extensive supporting ecosystem. The SKILL.md body (500 lines) contains the complete creation methodology: the four pillars (Philosophy, Anti-Patterns, Progressive Disclosure, Shibboleths), both workflow tracks (Minimal and Full), description engineering formula, anti-pattern format, quality heuristics, and review checklist. This is enough to create effective skills without loading any references.

When deeper guidance is needed, 55 reference files provide specialized content organized into four categories:

- **Core methodology (4 files):** skill-forge (8-phase), skill creation workflow, progressive disclosure, core principles
- **Anti-patterns and quality (6 files):** comprehensive anti-pattern catalogs, best practices checklists, shibboleths, validation
- **Advanced techniques (5 files):** evidence-based prompting, composability, variation patterns, output patterns, prompting principles
- **Enterprise and workflows (5 files):** factory workflows, audit protocols, enterprise checklists, step-by-step guides

Twenty-six utility scripts handle every operational aspect: initialization (`init_skill.py`), structural validation (`validate_skill.py`, `check_self_contained.py`), quality analysis (`analyze_skill.py`), activation testing (`test_activation.py`), documentation extraction (`doc_extractor.py`, `doc_analyzer.py`), and packaging (`package_skill.py`). Twenty-three templates provide starting points for SKILL.md files, helper scripts, configuration, metrics tracking, and adversarial testing protocols.

## Related Plugins

- **[Prompt Engineering](../prompt-engineering/)** -- Optimize prompts for LLMs through systematic design and evaluation
- **[Agent Evaluation](../agent-evaluation/)** -- Build evaluation frameworks to measure skill and agent performance
- **[Hosted Agents](../hosted-agents/)** -- Create hosted coding agents for sandboxed execution
- **[Multi-Agent Patterns](../multi-agent-patterns/)** -- Design multi-agent systems that compose multiple skills

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
