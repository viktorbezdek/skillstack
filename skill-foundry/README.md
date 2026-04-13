# Skill Foundry

> **v2.0.0** | Development | 21 iterations

> Advanced skill engineering framework for Claude Code -- philosophy-first design, evidence-based prompting, progressive disclosure architecture, anti-pattern prevention, shibboleths, eval-driven iteration, and enterprise-grade workflows.
> Single skill + 59 references + 26 scripts + 23 templates + 13 example skills

## The Problem

Most Claude Code skills are checklists dressed up as expertise. They list steps to follow, templates to fill in, and rules to obey -- and the output converges to the same generic pattern regardless of context. The skill activates when it should not, stays silent when it should trigger, and when it does fire, it produces rigid, templated responses that do not adapt to the user's actual situation.

The deeper problem is that skill creators focus on procedure before philosophy. They write "Step 1: Do X, Step 2: Do Y" without establishing the mental framework that guides judgment when the steps do not apply. They stuff 800 lines of instructions into SKILL.md without progressive disclosure, burning through context tokens and degrading the model's attention. They reference scripts and files that do not exist, causing silent failures. They write descriptions that are either too vague ("Helps with development") or too narrow ("Use when running Docker Compose on Kubernetes"), missing the activation window entirely.

The result is a skill ecosystem where most skills are either over-engineered (an "Everything Skill" that tries to handle an entire domain) or under-designed (a thin wrapper around a template with no expert knowledge). Teams that want to encode their real domain expertise into reusable skills have no systematic methodology for doing it well.

## The Solution

This plugin provides a complete skill engineering framework built on four pillars: Philosophy Before Procedure (establish "how to think" before "what to do"), Anti-Patterns as Guidance (what NOT to do is as important as what to do), Progressive Disclosure (core instructions in SKILL.md under 500 lines, details in references), and Shibboleths (encode the deep expert knowledge that separates novices from experts).

The skill offers two tracks based on complexity. The Minimal Workflow gets a simple skill from idea to working state in six steps: define scope, initialize with `init_skill.py`, write the description with keywords and NOT clauses, add anti-patterns, test activation, and validate. The Full Workflow uses an 8-phase methodology (Schema Definition through Metrics Tracking) for production-grade skills that need rigorous I/O contracts, adversarial testing, and enterprise validation.

Beyond the methodology, the plugin ships with 26 utility scripts (initialization, validation, analysis, documentation extraction, packaging), 59 reference files covering every aspect of skill design, 23 templates for SKILL.md files, helper scripts, and configuration, and 13 example skills showing the transformation from basic to effective. This is the full production toolkit -- distinct from Anthropic's bundled skill-creator.

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
/plugin install skill-foundry@skillstack
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

---

## System Overview

```
User wants to create / review / improve a skill
    │
    ▼
┌───────────────────────────────────────────────────────────┐
│                 skill-foundry (skill)                       │
│                                                             │
│  Four Pillars:                                              │
│  1. Philosophy Before Procedure                             │
│  2. Anti-Patterns as Guidance                               │
│  3. Progressive Disclosure (<500 lines)                     │
│  4. Shibboleths (expert knowledge encoding)                 │
│                                                             │
│  Two Tracks:                                                │
│  ├── Minimal (6 steps) ─── Simple skills                   │
│  │   Scope → Init → Description → Anti-patterns →          │
│  │   Test activation → Validate                             │
│  │                                                          │
│  └── Full (8 phases) ──── Production skills                │
│      Schema → Cognitive Frame → Intent Archaeology →        │
│      Use Cases → Architecture → Metadata →                  │
│      Instruction Crafting → Validation → Metrics            │
│                                                             │
│  ┌────────────────────────────────────────────────────────┐ │
│  │           59 Reference Files (on-demand)                │ │
│  │                                                         │ │
│  │  Core: skill-foundry (8-phase), skill_creation,         │ │
│  │        progressive_disclosure, core_principles          │ │
│  │  Quality: anti-patterns, shibboleths, validation,       │ │
│  │           best_practices, scoring-rubric                │ │
│  │  Advanced: evidence-based-prompting, composability,     │ │
│  │            variation-patterns, output-patterns           │ │
│  │  Enterprise: skill-factory-workflow, audit-protocol,    │ │
│  │              enterprise-checklist, migration-guide       │ │
│  │  Agents: agent-creator, agent-patterns                  │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │  26 Scripts   │  │ 23 Templates │  │  13 Examples      │  │
│  │  init, valid- │  │ SKILL.md,    │  │  document skills, │  │
│  │  ate, analyze,│  │ scripts,     │  │  algorithmic art, │  │
│  │  test, pack-  │  │ configs,     │  │  before/after,    │  │
│  │  age, extract,│  │ metrics,     │  │  annotated,       │  │
│  │  upgrade      │  │ adversarial  │  │  good-skills      │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  │
└───────────────────────────────────────────────────────────┘
```

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `skill-foundry` | skill | Core methodology: four pillars, description engineering, two workflow tracks, anti-pattern format, quality heuristics, review checklist |
| 59 reference files | reference | Deep guidance on methodology, anti-patterns, quality, composability, enterprise workflows, agent patterns |
| 26 utility scripts | script | Initialization, validation, analysis, documentation extraction, packaging, activation testing |
| 23 templates | template | SKILL.md starters, script boilerplate, configuration, metrics tracking, adversarial testing, skeleton projects |
| 13 example skills | example | Document skills (PDF/DOCX/PPTX/XLSX), algorithmic art, internal comms, before/after transformations, annotated analysis |
| 6 flowchart templates | asset | Decision tree, approval workflow, parallel execution, system architecture swimlane, onboarding |

**Eval coverage:** 13 trigger evaluation cases, 3 output evaluation cases.

### Component Spotlights

#### skill-foundry (skill)

**What it does:** Activates when you want to create, review, improve, or debug Claude Code skills. Guides you through philosophy-first design, description engineering for correct activation, anti-pattern encoding, progressive disclosure architecture, and validation. Provides both a minimal workflow (6 steps for simple skills) and a full 8-phase methodology for production-grade skills.

**Input -> Output:** A description of the expertise you want to encode (or an existing skill to review) -> A complete skill with SKILL.md, description, anti-patterns, decision trees, references, scripts, and validation results.

**When to use:** Creating new skills from scratch or from documentation. Reviewing or auditing existing skills for quality. Improving skill activation rates and precision. Encoding domain expertise and shibboleths. Building agent-powered skill workflows. Debugging why skills do not activate correctly.

**When NOT to use:** General prompt engineering (use prompt-engineering). Building Claude Code plugins as complete packages (use plugin-dev). Agent runtime and multi-agent orchestration (use multi-agent-patterns). Simple script writing that does not need skill abstraction.

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
| `skill-foundry.md` | Complete 8-phase methodology with detailed phase descriptions |
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
| `scoring-rubric.md` | Quality scoring criteria and thresholds |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, misses the skill's depth) | Good (specific, leverages the full framework) |
|---|---|
| "Help me make a skill" | "Create a skill for PostgreSQL query optimization -- I want it to encode index selection heuristics and common N+1 anti-patterns for Django ORM" |
| "My skill doesn't work" | "My container skill triggers for basic docker commands when it should only fire for Dockerfile optimization and multi-stage builds -- fix the activation" |
| "Write a SKILL.md" | "My SKILL.md is 900 lines and quality has dropped -- refactor it with progressive disclosure into a lean core with reference files" |
| "Make it better" | "This skill scores 45/100 on analyze_skill.py -- the anti-patterns are missing and there's no philosophy section. Help me get above 70." |
| "Create a skill from docs" | "I have API documentation at docs.internal.com/api -- extract the authentication patterns, error codes, and common pitfalls and turn them into a skill" |

### Structured Prompt Templates

**For creating a new skill:**
```
Create a Claude Code skill for [domain expertise]. The skill should encode
[specific knowledge: patterns, anti-patterns, decision trees]. Target users
are [who]. It should NOT handle [exclusions]. Top mistakes to prevent:
[list 2-3 common mistakes].
```

**For improving activation precision:**
```
My skill [name] triggers [too broadly / too narrowly]. It should activate for
[target queries] but currently [what happens instead]. Here's the current
description: [paste]. Fix the activation with proper keywords and NOT clauses.
```

**For refactoring an oversized skill:**
```
My SKILL.md is [N] lines. Help me split it using progressive disclosure.
Keep [what should stay in core: decision trees, anti-patterns, philosophy]
in SKILL.md and move [what should become references: detailed patterns,
examples, deep dives] to reference files.
```

**For enterprise skill creation:**
```
We need to create [N] skills for our [team/org]. Set up a factory workflow
with quality gates. Minimum score: [threshold]. Each skill needs
[requirements: peer review, activation testing, metrics tracking].
```

### Prompt Anti-Patterns

- **Asking to "create a skill" without specifying the expertise:** The skill needs to know what domain knowledge you want to encode, what mistakes you want to prevent, and who the target users are. Without this, it produces a generic skeleton.
- **Treating skill creation as template filling:** Saying "fill in the SKILL.md template" misses the point. The skill's value is the philosophy-first design process -- scope definition, description engineering, anti-pattern extraction, shibboleth encoding. The template is the output, not the process.
- **Ignoring the NOT clause in descriptions:** Asking to "add more trigger keywords" without also defining exclusions leads to broad activation. The NOT clause is as important as the keywords for precision.
- **Requesting skills for one-time tasks:** If the expertise is needed once and will not repeat, just do the task directly. Skills are for encoding knowledge that benefits from repeated application across projects.

## Real-World Walkthrough

You are a senior DevOps engineer who has spent five years managing Kubernetes clusters. Your team keeps making the same mistakes: overly permissive RBAC roles, missing resource limits, pods running as root, and Helm charts with hardcoded values. You want to encode this expertise into a Claude Code skill so the entire team benefits every time they work with Kubernetes manifests.

You open Claude Code and say:

```
I want to create a skill for Kubernetes best practices -- focusing on security, resource management, and Helm chart quality
```

The skill activates and starts with **scope definition**. It asks three focused questions: (1) Which Kubernetes versions? (2) What should this skill NOT handle -- cluster provisioning, networking CNI choices, service mesh configuration? (3) What are the top 3 mistakes your team makes?

You answer: Kubernetes 1.28+, NOT for cluster setup or CNI configuration, top mistakes are running as root, missing resource limits, and overly broad RBAC.

The skill runs `python scripts/init_skill.py kubernetes-security --path ./skills/` to create the directory structure. Next comes **description engineering**. The skill applies the formula: [What] [Use for] [Keywords] NOT for [Exclusions]. It produces a description with specific trigger keywords (`kubectl`, `helm`, `pod`, `deployment`, `RBAC`) and clear exclusions, explaining why this matters: the description is the activation trigger, and vague descriptions cause either false activations (wasting tokens) or missed activations (skill never fires).

Now the skill guides you through **philosophy before procedure**. Instead of starting with "Step 1: Add resource limits", it helps you write a philosophy section establishing "Defense in Depth" as the mental framework: each security layer assumes the layers above it have failed. This guides the model's judgment in situations the explicit rules do not cover.

The skill then helps you **encode anti-patterns** -- the mistakes you listed. Each anti-pattern follows the format: What it looks like / Why it's wrong / What to do instead / How to detect. For example, "Root Runner": no `securityContext` in pod spec leads to container escape + root = full node access. Fix: `runAsNonRoot: true` with specific UID. This format teaches the model to catch these patterns proactively.

You add a **validation script** and connect it from SKILL.md. After writing the core at 380 lines, you run validation:

```bash
python scripts/quick_validate.py ./skills/kubernetes-security/
# Structure valid, all references exist, description has keywords and NOT clause, under 500 lines
```

Then quality analysis:

```bash
python scripts/analyze_skill.py ./skills/kubernetes-security/
# Score: 78/100
# Philosophy section present, anti-patterns with detection criteria, decision trees
# Missing: temporal knowledge (what changed between K8s versions), variation guidance
```

Based on the feedback, you add a temporal section ("Pre-1.25: PodSecurityPolicy, 1.25+: Pod Security Admission") and variation guidance ("Dev: warn mode, Staging: enforce with exceptions, Production: enforce strict"). The score rises to 85/100.

The final skill has a clear philosophy, five encoded anti-patterns, a decision tree for RBAC scope selection, a validation script, and progressive disclosure with two reference files. It activates correctly for Kubernetes security questions and stays silent for cluster provisioning and networking.

## Usage Scenarios

### Scenario 1: Creating a skill from API documentation

**Context:** Your team uses a complex internal API with 40+ endpoints. New developers keep making the same authentication and pagination mistakes.

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
- Explicit triggers in SKILL.md for each reference file
- Validation that all references are connected and no orphaned sections exist

**You end up with:** A 400-line SKILL.md with focused core content and 4-5 reference files loaded on demand, improving both activation precision and output quality.

### Scenario 4: Enterprise skill factory workflow

**Context:** Your organization wants to create 15 skills encoding team expertise across infrastructure, security, and development.

**You say:** `We need to create 15 skills for our engineering org -- set up a factory workflow with quality gates`

**The skill provides:**
- Enterprise skill factory workflow from `skill-factory-workflow.md`
- Quality scoring rubric from `scoring-rubric.md` with minimum thresholds
- Audit protocol from `SKILL-AUDIT-PROTOCOL.md` for peer review
- Metrics tracking template for measuring skill effectiveness over time

**You end up with:** A repeatable process where each skill goes through scope definition, creation, validation (score >= 70), peer audit, and metrics tracking before deployment.

---

## Decision Logic

**When should I create a new skill vs extend an existing one?**

Create a new skill when: you have domain expertise not covered by existing skills, a pattern repeats across 3+ projects, or you have anti-patterns you want to prevent proactively. Extend an existing skill when: the expertise fits within an existing skill's scope and adding it would not push SKILL.md over 500 lines. Do not create a skill for one-time tasks -- just do the task directly.

**When should I use the Minimal vs Full workflow?**

The Minimal Workflow (6 steps) is for skills with clear scope, simple I/O, and internal use. The Full Workflow (8 phases) is for production-grade skills that will be shared across teams, need adversarial testing, or require strict I/O contracts. If you are not sure, start with Minimal and upgrade to Full when the skill proves its value.

**Skill vs Subagent vs MCP -- which extension type?**

- **Skill**: Domain expertise, decision trees, anti-patterns. No runtime state needed. The model reads instructions and applies them.
- **Subagent**: Multi-step workflows needing tool orchestration, parallel execution, or complex state management.
- **MCP**: External API connections, authentication, stateful sessions, or real-time data access.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Skill activates for everything in its domain | Description is too vague -- "Helps with Python" triggers on every `.py` file | Rewrite description with the formula: [What] [Use for] [Specific keywords] NOT for [Exclusions]. Test with `test_activation.py` against target and non-target queries. |
| Skill never activates when it should | Description is too narrow or uses jargon the model does not recognize as triggers | Add natural language trigger phrases alongside technical terms. Include "Use when..." clauses with common ways users describe the need. |
| Output is rigid and templated despite good design | SKILL.md is procedure-heavy with no philosophy section and no variation guidance | Add a philosophy section establishing the mental framework. Add variation guidance: "Outputs should vary based on [context dimension 1], [context dimension 2]." |
| Referenced files do not exist -- silent failures | Skill was edited but references were not updated, or files were moved without updating SKILL.md | Run `check_self_contained.py` to identify broken references. Fix by either creating the missing files or removing the references. |
| Quality score is low despite comprehensive content | Content is thorough but lacks structure: no anti-patterns, no decision trees, no progressive disclosure | Focus on the four pillars: add philosophy section, extract anti-patterns with the standard format, add decision trees for key choices, split content exceeding 500 lines into references. |

## Ideal For

- **Engineers encoding team expertise into reusable skills** -- the philosophy-first approach produces skills that adapt to context rather than outputting rigid templates
- **Skill authors who want activation precision** -- description engineering with the [What] [Use for] [Keywords] NOT for [Exclusions] formula eliminates false activations
- **Teams building skill libraries at scale** -- the enterprise factory workflow, quality scoring, and audit protocol ensure consistent quality across dozens of skills
- **Anyone improving an existing skill** -- `analyze_skill.py` produces a score with specific improvement suggestions, and `upgrade_skill.py` generates code changes
- **Documentation-to-skill converters** -- `doc_extractor.py` and `doc_analyzer.py` transform API docs, tool references, and internal wikis into structured skills

## Not For

- **General prompt engineering** -- use [prompt-engineering](../prompt-engineering/) for optimizing prompts that are not Claude Code skills
- **Building Claude Code plugins** -- use [plugin-dev](https://github.com/viktorbezdek/skillstack/tree/main/plugin-dev) for plugin architecture, composition, and validation; this skill focuses on the SKILL.md component
- **Agent runtime and orchestration** -- use [multi-agent-patterns](../multi-agent-patterns/) for designing multi-agent systems; this skill creates individual skills, not agent architectures

## Related Plugins

- **[Prompt Engineering](../prompt-engineering/)** -- Optimize prompts for LLMs through systematic design and evaluation
- **[Agent Evaluation](../agent-evaluation/)** -- Build evaluation frameworks to measure skill and agent performance
- **[Hosted Agents](../hosted-agents/)** -- Create hosted coding agents for sandboxed execution
- **[Multi-Agent Patterns](../multi-agent-patterns/)** -- Design multi-agent systems that compose multiple skills

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
