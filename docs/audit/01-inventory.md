# Phase 1: Plugin Inventory

**Date:** 2026-06-05  **Status:** PENDING APPROVAL  **Source:** `docs/audit/_groundtruth.json`

## Summary

- **Total plugins:** 59
- **Total skills:** 102
- **Total agents:** 12
- **Total commands:** 8

### Domain Distribution (proposed)

| Domain | Count |
|--------|-------|
| Engineering (E) | 24 |
| Meta-Infra (I) | 17 |
| Managerial-Product (P) | 13 |
| Marketing-Comms (M) | 5 |

### Verdict Distribution

| Verdict | Count |
|---------|-------|
| keep | 57 |
| merge-candidate | 2 |

## Overlap Clusters (evidence)

### `agent-dev`

> 3 plugins: architecture patterns (multi-agent-patterns), project lifecycle (agent-project-development), interactive ideation runtime (brainstorm-swarm). Low overlap.

| Plugin | Trigger (excerpt) |
|--------|-------------------|
| `agent-project-development` | "This skill should be used when the user asks to "start an LLM project", "design batch pipe…" |
| `brainstorm-swarm` | "Design ad-hoc personas for niche domains when the canonical 12 brainstorm- swarm personas…" |
| `multi-agent-patterns` | "This skill should be used when the user asks to "design multi-agent system", "implement su…" |

### `context-suite`

> 4 plugins share 'context' namespace. Trigger surfaces are **distinct** (reduce / diagnose / theory / extend). Suite design, not duplication.

| Plugin | Trigger (excerpt) |
|--------|-------------------|
| `context-compression` | "REDUCING context size — summarization strategies, anchored iterative summarization, tokens…" |
| `context-degradation` | "Diagnosing context FAILURES — lost-in-middle, poisoning, distraction, confusion, and clash…" |
| `context-fundamentals` | "Foundational theory of context engineering — what context IS, how attention works, progres…" |
| `context-optimization` | "EXTENDING effective context capacity — KV-cache optimization, observation masking, context…" |

### `copy-quality`

> 3 plugins: editorial slop removal (deslop), technical article structure (technical-copywriting), interface microcopy (ux-writing). Trigger surfaces distinct.

| Plugin | Trigger (excerpt) |
|--------|-------------------|
| `deslop` | "Remove AI slop from marketing copy, blog posts, product descriptions, emails, and editoria…" |
| `technical-copywriting` | "Engineer the distribution layer of a long-form technical article — title, dek (subtitle)…" |
| `ux-writing` | "Write effective microcopy, error messages, button labels, and interface text using UX writ…" |

### `eval-quality`

> 3 plugins span: LLM eval (agent-evaluation), plugin authoring quality (skill-foundry), code test strategy (testing-framework). Different targets — same 'quality' concern.

| Plugin | Trigger (excerpt) |
|--------|-------------------|
| `agent-evaluation` | "This skill should be used when the user asks to "evaluate agent performance", "build test…" |
| `skill-foundry` | "Author high-quality Claude Code SKILL.md files using philosophy-first design, evidence-bas…" |
| `testing-framework` | "Test framework router and infrastructure setup across multiple languages and platforms. Us…" |

### `memory-state`

> 3 plugins handle agent state. `memory-systems` = theory, `hindsight` = session ops + hook, `filesystem-context` = workspace indexing. Partial overlap on 'track state' trigger — verify.

| Plugin | Trigger (excerpt) |
|--------|-------------------|
| `filesystem-context` | "Using the FILE SYSTEM for context — scratch pads, plan persistence, dynamic skill loading…" |
| `hindsight` | "Interact with and integrate Hindsight long-term AI memory in Claude Code via the `hindsigh…" |
| `memory-systems` | "Guides implementation of agent memory systems, compares production frameworks (Mem0, Zep/G…" |

### `outcome-product`

> 2 plugins: `outcome-orientation` trigger (goal framing, success metrics) overlaps `product-thinking` skill triggers. Merge-candidate if triggers confirm near-identity.

| Plugin | Trigger (excerpt) |
|--------|-------------------|
| `outcome-orientation` | "Reframe work around measurable outcomes using OKRs, KPIs, and the outcome-vs-output distin…" |
| `product-thinking` | "Apply outcome-over-output product thinking — separating what gets built from what actually…" |

### `persona`

> 2 plugins: user-facing personas vs stakeholder mapping. Output artifacts differ (empathy map vs RACI). Low merge risk.

| Plugin | Trigger (excerpt) |
|--------|-------------------|
| `persona-definition` | "Create individual user personas and customer archetypes — with demographics, goals, pain p…" |
| `persona-mapping` | "Map stakeholders across organizations using Power-Interest matrices, RACI charts, influenc…" |

## Plugin Inventory Table

**Column key:** Domain (E/I/P/M) · Components (sk=skills ag=agents cmd=commands) · Eval (E=evals T=trigger-evals B=benchmark) · Gran (nano=1sk multi=2-9 large=10+) · Cluster · Verdict

| Plugin | Domain | Comp | Trigger (excerpt) | Ref-by | Eval | Gran | Cluster | Verdict | Rationale |
|--------|--------|------|-------------------|--------|------|------|---------|---------|-----------|
| `agent-evaluation` | Meta-Infra | 1sk | "This skill should be used when the user asks to "evaluate agent performance", "build test…" | 4 | E+T | nano | eval-quality | **keep** | LLM-as-judge, multi-dim rubrics, bias mitigation — specialist eval. |
| `agent-project-development` | Engineering | 1sk | "This skill should be used when the user asks to "start an LLM project", "design batch pipe…" | 2 | E+T | nano | agent-dev | **keep** | End-to-end agent project lifecycle. Different scope from patterns. |
| `api-design` | Engineering | 1sk+scripts | "Design production-grade REST, GraphQL, gRPC, and Python library APIs with correct schemas…" | 7 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `bdi-mental-states` | Engineering | 1sk | "This skill should be used when the user asks to "model agent mental states", "implement BD…" | 1 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `brainstorm-swarm` | Mgmt-Product | 4sk+12ag+1cmd | "Design ad-hoc personas for niche domains when the canonical 12 brainstorm- swarm personas…" | 0 | E+T+B | multi | agent-dev | **keep** | 12 agents + 4 skills + 1 cmd — interactive ideation runtime, not a pattern reference. |
| `cicd-pipelines` | Engineering | 1sk+scripts | "CI/CD pipeline design and DevOps automation — use when the user mentions GitHub Actions, G…" | 6 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `cloud-finops` | Mgmt-Product | 1sk | "Expert FinOps guidance covering cloud, AI, SaaS, and adjacent technology spend. Includes A…" | 2 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `code-review` | Engineering | 1sk+scripts | "Reviews existing code and pull requests using multi-agent swarm analysis covering security…" | 9 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `coding-discipline` | Engineering | 1sk | "Research-grounded 5-principle behavioral contract for production LLM coding agents — Think…" | 0 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `communication` | Marketing-Comms | 5sk | "Edit written text for clarity and conciseness — active voice, hedge and weasel-word remova…" | 6 | E+T | multi | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `consistency-standards` | Meta-Infra | 1sk | "Establish and enforce uniform naming conventions, taxonomy standards, style guides, and co…" | 4 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `content-modelling` | Mgmt-Product | 1sk+scripts | "Design CMS content models — content types, fields, editorial workflows, governance rules…" | 5 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `context-compression` | Meta-Infra | 1sk | "REDUCING context size — summarization strategies, anchored iterative summarization, tokens…" | 6 | E+T | nano | context-suite | **keep** | Distinct scope: reduce size. Complements others in context-suite. |
| `context-degradation` | Meta-Infra | 1sk | "Diagnosing context FAILURES — lost-in-middle, poisoning, distraction, confusion, and clash…" | 6 | E+T | nano | context-suite | **keep** | Distinct scope: diagnose failures. No overlap with compression/optimization. |
| `context-fundamentals` | Meta-Infra | 1sk | "Foundational theory of context engineering — what context IS, how attention works, progres…" | 10 | E+T | nano | context-suite | **keep** | Theory anchor for suite. Referenced by 10 plugins — high utility. |
| `context-optimization` | Meta-Infra | 1sk | "EXTENDING effective context capacity — KV-cache optimization, observation masking, context…" | 9 | E+T | nano | context-suite | **keep** | Distinct scope: extend capacity via caching/partitioning. |
| `creative-problem-solving` | Mgmt-Product | 1sk | "Generate new ideas and breakthrough solutions using brainstorming, lateral thinking, SCAMP…" | 4 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `critical-intuition` | Meta-Infra | 1sk | "Stress-test, critique, and challenge existing ideas through pattern recognition, bias dete…" | 4 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `debugging` | Engineering | 1sk+scripts | "Finds and fixes bugs through systematic root cause analysis, stack trace interpretation, b…" | 15 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `deslop` | Marketing-Comms | 3sk | "Remove AI slop from marketing copy, blog posts, product descriptions, emails, and editoria…" | 0 | E+T+B | multi | copy-quality | **keep** | 3 skills: AI-slop removal from editorial/marketing copy. Distinct from technical writing style. |
| `docker-containerization` | Engineering | 1sk+scripts | "Docker and container development — use when the user mentions Dockerfiles, multi-stage bui…" | 3 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `documentation-generator` | Engineering | 1sk+scripts | "Generate comprehensive documentation for a codebase by reading the repository and producin…" | 8 | E+T+B | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `edge-case-coverage` | Engineering | 1sk | "Identify and document boundary conditions, corner cases, error scenarios, and validation r…" | 2 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `elicitation` | Meta-Infra | 1sk | "Psychological elicitation and deep-interview design using narrative identity (McAdams), se…" | 6 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `example-design` | Meta-Infra | 1sk | "Design pedagogically effective code examples, tutorials, and runnable samples using progre…" | 3 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `filesystem-context` | Meta-Infra | 1sk | "Using the FILE SYSTEM for context — scratch pads, plan persistence, dynamic skill loading…" | 5 | E+T | nano | memory-state | **merge-candidate** | Overlaps with memory-systems (state tracking). Merge into memory-systems or re-scope as 'workspace context'. |
| `frontend-design` | Engineering | 1sk+scripts | "Visual design systems, UI/UX styling, Tailwind CSS, CSS variables, component libraries (sh…" | 6 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `git-workflow` | Engineering | 1sk+scripts | "Git workflow management — use when the user mentions git, conventional commits, commit qua…" | 2 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `gws-cli` | Engineering | 1sk | "Google Workspace CLI (gws) for managing all 18 Workspace APIs from the terminal. Use when…" | 0 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `hindsight` | Meta-Infra | 1sk+1cmd+hook+scripts | "Interact with and integrate Hindsight long-term AI memory in Claude Code via the `hindsigh…" | 1 | E+T | nano | memory-state | **keep** | Operational memory (session persistence, hooks). Different from theory. |
| `hosted-agents` | Engineering | 1sk | "Build and deploy hosted background coding agents with sandboxed VM execution, multiplayer…" | 4 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `mcp-server` | Engineering | 1sk+scripts | "MCP (Model Context Protocol) server development — use when the user mentions MCP, Model Co…" | 6 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `memory-systems` | Meta-Infra | 1sk | "Guides implementation of agent memory systems, compares production frameworks (Mem0, Zep/G…" | 10 | E+T | nano | memory-state | **keep** | General memory theory. Referenced by 10 plugins. |
| `multi-agent-patterns` | Engineering | 1sk | "This skill should be used when the user asks to "design multi-agent system", "implement su…" | 13 | E+T | nano | agent-dev | **keep** | Architecture patterns for multi-agent systems. Referenced by 13 plugins. |
| `navigation-design` | Engineering | 1sk | "Design information architecture, wayfinding systems, and navigation structures for documen…" | 5 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `nextjs-development` | Engineering | 1sk+scripts | "Next.js framework development including App Router, Server Components, Server Actions, SSR…" | 5 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `ontology-design` | Mgmt-Product | 1sk | "Design formal knowledge models — classes, properties, relationships, hierarchies, and sema…" | 3 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `osint` | Meta-Infra | 1sk+scripts | "Conduct deep OSINT research on individuals — from name or handle to a scored dossier with…" | 0 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `outcome-orientation` | Mgmt-Product | 1sk | "Reframe work around measurable outcomes using OKRs, KPIs, and the outcome-vs-output distin…" | 6 | E+T | nano | outcome-product | **merge-candidate** | Outcome framing overlaps with product-thinking's goal-alignment skills. Merge or clearly re-scope. |
| `persona-definition` | Mgmt-Product | 1sk | "Create individual user personas and customer archetypes — with demographics, goals, pain p…" | 8 | E+T | nano | persona | **keep** | User persona creation (demographics, empathy maps). Distinct output from persona-mapping. |
| `persona-mapping` | Mgmt-Product | 1sk | "Map stakeholders across organizations using Power-Interest matrices, RACI charts, influenc…" | 7 | E+T | nano | persona | **keep** | Stakeholder mapping (RACI, Power-Interest). Different audience, different deliverable. |
| `plugin-dev` | Meta-Infra | 8sk+scripts | "Decides which Claude Code extension type to use for a given capability — skill, hook, MCP…" | 2 | E+T | multi | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `prioritization` | Mgmt-Product | 1sk | "Apply RICE, MoSCoW, ICE, and effort-impact frameworks to rank options and decide what to w…" | 10 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `product-thinking` | Mgmt-Product | 5sk | "Apply outcome-over-output product thinking — separating what gets built from what actually…" | 2 | E+T | multi | outcome-product | **keep** | 5-skill suite with depth (PRDs, roadmaps, metrics, strategy). Primary product anchor. |
| `prompt-engineering` | Meta-Infra | 1sk+scripts | "Design, evaluate, and iteratively improve prompts for LLMs — system prompts, few-shot exam…" | 4 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `python-development` | Engineering | 1sk+6cmd+scripts | "Python development — use when the user works with .py files, pyproject.toml, uv, ruff, myp…" | 3 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `react-development` | Engineering | 1sk+scripts | "React-specific development patterns including hooks (useState, useEffect, useReducer, useC…" | 5 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `risk-management` | Mgmt-Product | 1sk | "Systematically assess and mitigate risks using risk registers, probability-impact matrices…" | 8 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `skill-foundry` | Meta-Infra | 1sk+scripts | "Author high-quality Claude Code SKILL.md files using philosophy-first design, evidence-bas…" | 4 | E+T+B | nano | eval-quality | **keep** | Plugin/skill authoring quality. Distinct lifecycle from agent evaluation. |
| `skillstack-workflows` | Meta-Infra | 20sk | "End-to-end workflow for taking an API from design through TDD, code review, CI/CD, and con…" | 2 | E+T | large | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `storytelling` | Marketing-Comms | 1sk | "Expert guidance for writing, editing, and teaching stories across fiction, business, data…" | 5 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `systems-thinking` | Mgmt-Product | 1sk | "Analyze complex problems through feedback loops, system dynamics, causal relationships, an…" | 5 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `technical-copywriting` | Marketing-Comms | 5sk | "Engineer the distribution layer of a long-form technical article — title, dek (subtitle)…" | 0 | E+T+B | multi | copy-quality | **keep** | 5 skills: long-form technical article structure/distribution. Distinct audience/output. |
| `test-driven-development` | Engineering | 1sk+scripts | "Guides the Test-Driven Development methodology: the Red-Green-Refactor cycle of writing fa…" | 6 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `testing-framework` | Engineering | 1sk+scripts | "Test framework router and infrastructure setup across multiple languages and platforms. Us…" | 9 | E+T | nano | eval-quality | **keep** | Code test strategy (TDD, coverage, integration). Different from LLM eval. |
| `tool-design` | Engineering | 1sk | "This skill should be used when the user asks to "design agent tools", "create tool descrip…" | 9 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `typescript-development` | Engineering | 1sk+scripts | "TypeScript development — use when the user works with TypeScript, type system patterns, ge…" | 4 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `user-journey-design` | Mgmt-Product | 1sk | "Map user journeys with touchpoints, emotional states, pain points, and opportunities acros…" | 3 | E+T | nano | — | **keep** | No overlap cluster. Unique domain and trigger surface. |
| `ux-writing` | Marketing-Comms | 1sk | "Write effective microcopy, error messages, button labels, and interface text using UX writ…" | 9 | E+T | nano | copy-quality | **keep** | Microcopy/interface text. Different output format from both above. |

## Findings Requiring Phase 2 Decision

1. **`filesystem-context` merge candidate** — trigger surface overlaps with `memory-systems` on 'workspace state tracking'. Need trigger-level comparison in Phase 2 to confirm.
2. **`outcome-orientation` merge candidate** — trigger phrases (goal framing, success metrics) likely duplicate `product-thinking/outcome-alignment`. Confirm with full trigger-evals read.
3. **Context suite category** — 4 plugins should share a `context-engineering` sub-domain tag to aid discoverability, even if kept as-is.
4. **`gws-cli` domain ambiguity** — Google Workspace CLI sits at E/P boundary (IT admin vs productivity). Assigned Engineering; revisit if P domain grows a 'workspace-productivity' cluster.
5. **`osint` domain** — currently Meta-Infra (information gathering as a meta-capability). Could be P (competitive intelligence). Low ref-count (0) suggests low usage — flag for deprecation review.
6. **`cloud-finops` isolation** — no overlap cluster, P domain, 0 inbound refs from plugins. Useful standalone but may need a 'infrastructure-management' peer to be discoverable.
7. **`plugin-dev` size** — 8 skills, largest after skillstack-workflows (20). Consider splitting: authoring skills vs publishing/eval skills.

---
*Generated by `docs/audit/_gen_inventory.py` · All domain assignments and verdicts are proposals pending Phase 2 approval*