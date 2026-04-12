# SkillStack Workflows

> **v1.0.0** | Strategic Thinking | 1 iteration

Eighteen composable workflow playbooks that orchestrate existing SkillStack plugins for real multi-stage problems. Each workflow is a self-contained playbook with phase-by-phase guidance, explicit gates and loops, and references to the underlying skills you should install alongside it.

## What Problem Does This Solve

Single skills handle focused tasks — writing an API, debugging a race condition, designing a persona. But real projects are rarely one skill deep. Shipping a product needs research, design, build, test, deploy, monitor. Debugging a complex issue needs hypothesis formation, tests as oracles, blast-radius assessment. Making a strategic decision needs outcome definition, option generation, risk analysis, and a check that the criteria didn't drift.

This plugin provides nine **composition workflows** — sequences of existing SkillStack skills with explicit data flow between them — for the most common multi-stage problems. Each workflow is a playbook Claude can follow when activated, drawing on the underlying skills you have installed.

## When to Use This Plugin

Install this plugin alongside the underlying SkillStack plugins when you repeatedly face problems that span multiple domains. The workflows activate independently based on the kind of problem you describe:

| You say... | The workflow that activates... |
|---|---|
| "Help me write a pitch for our investor meeting in 5 days" | `pitch-sprint` — 5-day research+draft+audit+polish sprint |
| "This bug has been driving me crazy for 3 hours" | `debug-complex-issue` — hypothesis-test-fix loop with blast-radius gate |
| "I want to build an agent that automates our support triage" | `build-ai-agent` — 9-phase funnel from is-this-even-an-agent-problem to production monitoring |
| "We need to decide whether to pivot or keep going" | `strategic-decision` — gate-driven decision workflow with outcome-criteria check |
| "Help me set up a documentation platform from scratch" | `content-platform-build` — 7-layer build from content model to tooling |
| "We just ran 12 user interviews, now what?" | `user-research-to-insight` — funnel from interview design to narrative presentation |
| "I inherited a legacy codebase and I'm terrified to touch it" | `legacy-rescue` — codemap + test safety net + atomic commits + rollback plans |
| "Our Claude API bill tripled last month, help" | `llm-cost-optimization` — anti-pattern diagnosis with mandatory quality gate |
| "I want to create my own Claude Code skill that actually works" | `write-your-own-skill` — meta-workflow for skill authoring with validation |
| "I want to build a Claude Code plugin with hooks and skills" | `build-a-plugin` — full lifecycle from ideation to evaluated, validated plugin |
| "I need to build and ship a new API endpoint" | `api-to-production` — design → TDD → review → CI/CD → containerized deployment |
| "Make this codebase more secure" | `security-hardening-audit` — threat mapping → code audit → edge cases → test hardening |
| "I just cloned this repo — help me understand it" | `onboard-to-codebase` — codemap → system model → trace flows → context strategy |
| "Turn our user interviews into a prioritized backlog" | `product-story-to-ship` — elicitation → journey → personas → outcomes → prioritized stories |
| "My agent's context is a mess, it forgets things" | `context-engineering-pipeline` — diagnose → optimize → compress → fix degradation → persist |
| "Review the design quality of our whole app" | `design-review-sprint` — visual → navigation → copy → journey → consistency audit |
| "My AI agent is underperforming — help me fix it" | `evaluate-and-improve-agent` — evaluate → diagnose → redesign → add memory → re-evaluate |
| "I need to present our quarterly results to the board" | `storytelling-for-stakeholders` — structure → angle → outcomes → craft and polish |

## When NOT to Use This Plugin

- **Single-skill tasks** — if the problem fits cleanly inside one skill's domain, use that skill directly
- **Reversible experiments** — if you can try a thing cheaply and see what happens, just experiment
- **You haven't installed the underlying plugins** — the workflows reference specific SkillStack skills by name; without them installed, Claude has process guidance but no domain depth
- **You need real-time orchestration** — these workflows are playbooks for Claude to follow, not programmatic chains. If you need automated multi-step execution, look at the `workflow-automation` skill

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install skillstack-workflows@skillstack
```

**Strongly recommended:** also install the underlying SkillStack plugins that the workflows reference. Each workflow has its own prerequisites listed, but if you install the full collection, everything works:

```bash
/plugin install agent-evaluation@skillstack
/plugin install agent-project-development@skillstack
/plugin install cloud-finops@skillstack
/plugin install code-review@skillstack
/plugin install consistency-standards@skillstack
/plugin install content-modelling@skillstack
/plugin install context-compression@skillstack
/plugin install context-optimization@skillstack
/plugin install creative-problem-solving@skillstack
/plugin install critical-intuition@skillstack
/plugin install debugging@skillstack
/plugin install documentation-generator@skillstack
/plugin install elicitation@skillstack
/plugin install example-design@skillstack
/plugin install git-workflow@skillstack
/plugin install hosted-agents@skillstack
/plugin install memory-systems@skillstack
/plugin install multi-agent-patterns@skillstack
/plugin install navigation-design@skillstack
/plugin install outcome-orientation@skillstack
/plugin install persona-definition@skillstack
/plugin install persona-mapping@skillstack
/plugin install prioritization@skillstack
/plugin install prompt-engineering@skillstack
/plugin install risk-management@skillstack
/plugin install skill-creator@skillstack
/plugin install storytelling@skillstack
/plugin install systems-thinking@skillstack
/plugin install test-driven-development@skillstack
/plugin install tool-design@skillstack
/plugin install user-journey-design@skillstack
/plugin install ux-writing@skillstack
```

Or browse interactively:
```
/plugin
```

## How to Use

**Direct invocation:**

```
Use the pitch-sprint workflow to help me draft the Series A deck
```

```
Use the debug-complex-issue workflow — I've been stuck on this race condition for hours
```

```
Use the legacy-rescue workflow to help me safely add a feature to this old codebase
```

**Natural language activation** — each workflow activates automatically when you describe the matching problem. Describe what you're trying to do, and Claude will load the right workflow without you having to name it.

## What's Inside

This is a **multi-skill plugin** — one plugin containing 18 independently-activating workflow skills. Each is a self-contained playbook with frontmatter triggers specific to that problem type.

### The 18 workflows

- **`pitch-sprint`** — Parallel-merge workflow for producing a pitch in 1 week. Three parallel streams (interviews, system mapping, persona sharpening) merge into a StoryBrand / Pixar Spine / founder-story spine, audited via critical-intuition, polished via ux-writing. 5-day, 3-day, and 1-day variants.

- **`debug-complex-issue`** — Loop workflow for bugs that have defeated a first-pass attempt. Observation-before-hypothesis discipline, family classification (race, state-machine, environment, LLM, etc.), multi-hypothesis differentiation, blast-radius assessment, and the TDD loop as debugging oracle.

- **`build-ai-agent`** — 9-phase funnel from "I want an agent that does X" to deployed, evaluated, cost-monitored agent. Critical gate: evaluation pipeline before prompt iteration. Includes the is-this-even-an-agent-task filter and tool-surface minimization.

- **`strategic-decision`** — Gate workflow for high-stakes irreversible decisions. Defines outcome measurably first, generates options widely, stress-tests for bias and hidden assumptions, assesses downside, ranks on original criteria, and uses the outcome-gate to catch criteria drift.

- **`content-platform-build`** — 7-layer layering workflow for docs sites, knowledge bases, and CMS platforms. Content model → ontology (if needed) → consistency standards → navigation → UX copy → examples → tooling. Order is load-bearing; layers cannot be inverted.

- **`user-research-to-insight`** — Funnel workflow for turning interviews into product direction. Depth-tiered interview design via elicitation, pattern-based persona synthesis, stakeholder mapping, journey mapping, audit, and narrative presentation that actually moves teams to action.

- **`legacy-rescue`** — Loop workflow for making real progress on legacy code without breaking production. Codemap first, feedback-center identification, second-opinion review, characterization test safety net, rollback-planned atomic commits, and debugging loops for surprises.

- **`llm-cost-optimization`** — Funnel + gate workflow for reducing LLM costs without killing quality. Diagnoses the six AI cost anti-patterns, reduces context, compresses what can't be reduced, rightsizes models, and uses a non-negotiable quality gate to roll back optimizations that degrade the product.

- **`write-your-own-skill`** — Meta-workflow for creating Claude Code skills that actually activate and deliver value. Spec first, elicit domain depth, design examples before prose, validate against anti-patterns, ship with structural tests.

- **`build-a-plugin`** — End-to-end Claude Code plugin authoring workflow. Ideation (7-criteria check) → research (marketplace survey) → architecture (component decomposition) → build (hooks + composition + skills) → validation → evaluation. Three gates prevent wasted work.

- **`api-to-production`** — Takes an API from design to containerized deployment. API design → TDD → code review → CI/CD pipeline → Docker containerization → ship. Three gates: contract frozen, tests green, pipeline green.

- **`security-hardening-audit`** — Systematic security audit. Threat surface mapping → security-focused code review → edge case analysis → test hardening → remediation. Audit all before fixing any so systemic patterns emerge.

- **`onboard-to-codebase`** — "I just cloned this — help me understand it." Auto-generate codemap → build system model (dependencies, feedback loops) → trace key flows end-to-end → build context strategy for ongoing work.

- **`product-story-to-ship`** — PM funnel from user research to sprint-ready stories. Deep interviews → journey mapping → persona definition → measurable outcomes → RICE/MoSCoW prioritized backlog with provenance chains.

- **`context-engineering-pipeline`** — Fix agent context systematically. Understand mechanics → optimize capacity → compress remaining → diagnose degradation (lost-in-middle, poisoning) → persist to filesystem.

- **`design-review-sprint`** — Full UX quality audit. Visual audit → navigation review → copy audit → journey validation → consistency check. Audit top-down, fix bottom-up.

- **`evaluate-and-improve-agent`** — Agent improvement cycle. Baseline evaluation → architecture diagnosis → pattern redesign → memory integration → re-evaluation against baseline.

- **`storytelling-for-stakeholders`** — Turn data into compelling narratives. Structure (3-act, SparkLines, SCR) → find the angle → anchor to outcomes → craft and polish. Every beat passes the "so what?" test.

### How the workflows work

Each workflow skill has its own frontmatter with specific activation triggers. When you describe a problem, Claude matches it against all active skills' descriptions — including these workflows — and activates the best match. Once activated, the workflow's SKILL.md tells Claude to:

1. Follow the phase-by-phase process
2. Draw on the underlying skills you have installed (explicitly referenced by name)
3. Respect the gates and loops
4. Produce the expected output artifacts

The workflows do NOT programmatically chain other skills. They're playbooks Claude reads and follows. Install the underlying plugins for depth; without them, you still get process guidance but not domain expertise.

## Version History

- `2.0.0` Added 9 new workflows: build-a-plugin, api-to-production, security-hardening-audit, onboard-to-codebase, product-story-to-ship, context-engineering-pipeline, design-review-sprint, evaluate-and-improve-agent, storytelling-for-stakeholders
- `1.0.0` Initial release — 9 composition workflows

## Related Skills

- **[Skill Creator](../skill-creator/)** — Create the individual skills these workflows reference
- **[Workflow Automation](../workflow-automation/)** — For programmatic multi-step orchestration (not playbook-style)
- All 32+ SkillStack skills referenced by the workflows — install them for depth

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — 52 production-grade plugins for Claude Code.
