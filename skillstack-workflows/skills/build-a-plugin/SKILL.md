---
name: build-a-plugin
description: End-to-end workflow for authoring a Claude Code plugin from idea to validated, evaluated artifact. Composes six phases — ideation with a 7-criteria kill gate (plugin-ideation), marketplace survey and build-vs-fork decision (plugin-research), skill/hook/MCP/subagent/command decomposition (plugin-architecture), component implementation (plugin-hooks + plugin-composition + skill-creator), structural validation (plugin-validation), and trigger plus output evaluation with iteration loop (plugin-evaluation). Use when building a full Claude Code plugin with multiple components, hooks, MCP servers, or composed skills. Use when converting a working prototype into a shippable plugin. NOT for writing a single SKILL.md file — use the write-your-own-skill workflow for that. NOT for one-off prompt engineering — use prompt-engineering directly.
---

# Build a Plugin

> A plugin that ships without evals ships with hope instead of evidence. A plugin that ships without validation ships with structural debt. This workflow forces both before you can call it done.

Building a Claude Code plugin is more than writing a SKILL.md file. A plugin bundles skills, hooks, MCP servers, subagents, and commands into a cohesive package with a manifest, validation, and evaluation. Teams that skip the ideation gate build plugins nobody needs. Teams that skip evaluation build plugins that don't activate reliably. This workflow prevents both.

---

## When to use this workflow

- Building a new Claude Code plugin from scratch with multiple components
- Converting a collection of loose skills into a proper plugin package
- Adding hook-based automation alongside skill-based knowledge
- Building a plugin that includes an MCP server or subagent
- Preparing a plugin for marketplace publication

## When NOT to use this workflow

- **Single SKILL.md files** — use the `write-your-own-skill` workflow
- **One-off prompts** — use `prompt-engineering` directly
- **MCP server development only** — use the `mcp-server` skill directly
- **Quick prototype not intended for distribution** — write the SKILL.md directly with `skill-foundry`

---

## Prerequisites

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install plugin-ideation@skillstack
/plugin install plugin-research@skillstack
/plugin install plugin-architecture@skillstack
/plugin install plugin-hooks@skillstack
/plugin install plugin-composition@skillstack
/plugin install skill-foundry@skillstack
/plugin install plugin-validation@skillstack
/plugin install plugin-evaluation@skillstack
```

---

## Core principle

**Kill bad ideas early, validate structure before content, evaluate activation before shipping.** The most expensive plugin failures are the ones that pass every structural check but never activate when needed — or activate when they shouldn't. The ideation gate prevents building the wrong thing; the evaluation gate prevents shipping a thing that doesn't work.

Secondary principle: **decomposition drives quality.** A plugin that tries to be one giant skill will either bloat the context window or under-serve its users. Deciding which parts are skills, which are hooks, and which are MCP tools is the architectural decision that determines everything downstream.

---

## The phases

### Phase 1 — ideation and kill gate (plugin-ideation)

Load the `plugin-ideation` skill. It provides a 7-criteria checklist for evaluating plugin ideas before investing in them.

Answer honestly:

- **Problem clarity** — can you state the problem in one sentence without using the word "comprehensive"?
- **Audience** — who specifically will use this? "Developers" is not specific enough.
- **Existing alternatives** — does this already exist in the marketplace? Can you fork instead of building?
- **Activation clarity** — can you write 5 example queries that should trigger this plugin?
- **Scope boundary** — can you name 3 things this plugin explicitly does NOT do?
- **Component count** — do you need more than one skill, or is this actually a single-skill plugin?
- **Value test** — if the plugin existed today, would you install it?

If any criterion fails, iterate on the idea or kill it. Building a plugin nobody needs is the most common failure mode.

Output: a one-page plugin brief with clear scope, audience, and component sketch.

### Phase 2 — marketplace research (plugin-research)

Load the `plugin-research` skill. Before building, survey:

- **Existing plugins** — what's already in the marketplace that overlaps?
- **Authoritative sources** — what does the official Anthropic documentation say about the extension points you'll use?
- **Build vs. fork** — is it faster to fork an existing plugin and modify it, or start fresh?
- **Gap analysis** — what specifically does your plugin add that nothing else covers?

This phase produces the evidence that justifies building. Without it, you risk duplicating existing work or misunderstanding the extension API.

Output: a research brief with marketplace survey, source inventory, and build-vs-fork decision.

### Phase 3 — architecture and decomposition (plugin-architecture)

Load the `plugin-architecture` skill. For each capability your plugin needs, decide:

- **Skill** — declarative knowledge Claude should load into context (when-to-use, how-to-think, reference material)
- **Hook** — event-driven automation that runs before/after tool calls or session events (validation, formatting, routing)
- **MCP server** — external tool access that gives Claude new capabilities (API calls, data retrieval, computation)
- **Subagent** — delegated work that runs in a separate context (parallel execution, specialized analysis)
- **Slash command** — user-invoked action that triggers a specific workflow

Map each capability to exactly one extension type. Capabilities that span two types usually need to be split. The architecture document is the blueprint for Phase 4.

Output: a component map listing every piece, its type, and its responsibility.

### Phase 4 — build the components (plugin-hooks + plugin-composition + skill-creator)

Load the skills needed for your specific components:

- **For skills:** load `skill-foundry` and follow its conventions for frontmatter, progressive disclosure, and reference files
- **For hooks:** load `plugin-hooks` for the event model, matching patterns, and hook script conventions
- **For composed plugins:** load `plugin-composition` for the manifest structure, component wiring, and cross-component communication

Build one component at a time. Each component should work independently before you wire them together. The `plugin-composition` skill covers the integration patterns — how skills reference each other, how hooks complement skills, how the manifest ties everything together.

Output: all plugin components implemented, with a valid `plugin.json` manifest.

### Phase 5 — structural validation (plugin-validation)

Load the `plugin-validation` skill. Run validation checks:

- **Manifest validity** — `plugin.json` has all required fields, paths resolve, versions are correct
- **Frontmatter validity** — every SKILL.md has `name` and `description`, name matches directory
- **Reference integrity** — every reference cited in SKILL.md exists on disk
- **Hook structure** — hook scripts are executable, event patterns are valid
- **Cross-references** — skills that reference other skills point to real targets

Fix every validation error before proceeding. Structural errors in production are embarrassing and avoidable.

Output: a clean validation report with zero errors.

### Phase 6 — evaluation and iteration (plugin-evaluation)

Load the `plugin-evaluation` skill. Build two kinds of evals:

**Trigger evals** — does the plugin activate on the right queries and stay silent on the wrong ones?
- Write 8+ positive triggers (queries that should activate the skill)
- Write 5+ negative triggers (near-miss queries that should NOT activate)
- Run them. If activation accuracy is below your threshold, revise the frontmatter descriptions.

**Output evals** — when the plugin activates, does it produce good results?
- Write 3+ scenario-based evals with expected behavior descriptions
- Run them against the actual skill content
- Iterate on content until output quality meets your bar

This is the loop: evaluate → identify weakness → fix → re-evaluate. Ship when both trigger and output evals pass.

Output: passing trigger-evals.json and evals.json for every skill in the plugin.

---

## Gates and failure modes

**Gate 1: the ideation gate.** Phase 2 cannot start until Phase 1 concludes the idea is worth building. Researching a bad idea wastes time.

**Gate 2: the architecture gate.** Phase 4 cannot start until Phase 3 has produced the component map. Building without architecture produces a tangled plugin.

**Gate 3: the validation gate.** Phase 6 cannot start until Phase 5 passes with zero errors. Evaluating a structurally broken plugin produces misleading results.

**Failure mode: single-skill plugin disguised as multi-component.** The plugin has one real skill and five empty stubs. Mitigation: Phase 1's component count criterion.

**Failure mode: hook without corresponding skill.** A hook runs validation but there's no skill that teaches Claude how to produce valid output. Mitigation: Phase 3's decomposition forces explicit pairing.

**Failure mode: perfect validation, zero activation.** The plugin passes every structural check but the frontmatter descriptions are too vague to trigger. Mitigation: Phase 6's trigger evals catch this before shipping.

---

## Output artifacts

1. **plugin.json** — valid manifest with all components declared
2. **SKILL.md files** — one per skill, lean and scoped
3. **Hook scripts** — if applicable, with event patterns and matching rules
4. **MCP server** — if applicable, with tool definitions
5. **references/** — focused domain content per skill
6. **README.md** — human-facing documentation
7. **trigger-evals.json + evals.json** — per skill, passing
8. **A decision log** — why each component exists and what type it is

---

## Related workflows and skills

- For writing a single SKILL.md (not a full plugin), use the `write-your-own-skill` workflow
- For the plugin extension API reference, see the `plugin-hooks` and `plugin-composition` skills directly
- For marketplace publication, see the skillstack README for contribution guidelines
- For debugging activation issues after shipping, use the `debug-complex-issue` workflow

---

> *SkillStack Workflows by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
