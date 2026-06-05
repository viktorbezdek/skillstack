# Phase 2: Deduplication & Taxonomy

**Date:** 2026-06-05  **Status:** PENDING APPROVAL  **Source:** `docs/audit/01-inventory.md` + trigger-evals comparison

## Summary

- Merge candidates from Phase 1: **2**
- Merge candidates confirmed after trigger-evals: **0** (both rejected — see evidence below)
- Final verdict: **59 keep, 0 merge, 0 split, 0 rename, 0 deprecate**
- Domain map: finalized — no changes from Phase 1 proposals
- Action log: no migrations required this phase

---

## Merge Candidate Resolutions

### MC-1: `filesystem-context` — REJECTED (keep distinct)

**Phase 1 concern:** trigger "use filesystem for agent memory" overlaps memory-systems "implement agent memory".

**Trigger-evals comparison:**

| Plugin | Positive triggers (sample) | Scope |
|--------|---------------------------|-------|
| `filesystem-context` | "offload context to files", "implement scratch pads", "persist agent plans", "use filesystem for agent memory" | **Mechanism**: the file system AS the context store during a Claude Code session |
| `memory-systems` | "implement agent memory", "persist state across sessions", "build knowledge graph", "track entities over time", "add long-term memory" | **Frameworks**: production memory systems (Mem0, Zep, GraphRAG) for deployed agents |

**Decisive evidence:**

1. `filesystem-context` NOT-for excludes KV-cache, summarization, context theory — these are context-engineering exclusions, not memory exclusions. The skill is scoped to Claude Code session management via the OS filesystem.
2. `memory-systems` NOT-for excludes "hosted agent infrastructure or sandboxed VMs" — scoped to software architecture, not CC session tooling.
3. Skill descriptions confirm different output: `filesystem-context` → scratch pad patterns, plan persistence files, dynamic SKILL.md loading. `memory-systems` → framework comparison (Mem0 vs Zep), vector store selection, knowledge graph schemas.

**Verdict: KEEP both.** Different levels of abstraction (CC session tool vs production architecture framework). A merge would conflate Claude Code meta-skills with application engineering advice.

---

### MC-2: `outcome-orientation` — REJECTED (keep distinct)

**Phase 1 concern:** trigger wording mirrors `product-thinking/outcome-oriented-thinking` skill.

**Trigger-evals comparison:**

| Plugin/skill | Positive triggers (sample) | Scope |
|-------------|---------------------------|-------|
| `outcome-orientation` | "help me with outcome orientation", "reframe work around measurable outcomes", "OKRs", "KPIs" | **Mechanics**: write OKRs, define KPIs, operationalize outcome-vs-output distinction |
| `product-thinking/outcome-oriented-thinking` | "Is shipping this feature really an outcome?", "What should our North Star metric be?", "Write the outcome hypothesis for a redesigned onboarding flow" | **Validation**: product decision framing — is this thing an outcome at all? |

**Decisive evidence:**

`product-thinking/outcome-oriented-thinking` trigger-evals FALSE entry: `"Write OKRs for the engineering team this quarter."` — explicitly NOT this skill. This query routes to `outcome-orientation`. The two skills are complementary in a handoff design: outcome-orientation handles operational mechanics (write the OKR), product-thinking handles philosophical validation (should this be an OKR at all?).

**Verdict: KEEP both.** The handoff is intentional and documented in trigger-evals. Merging removes the routing clarity.

---

## Granularity Rule (formalized)

| Class | Condition | Disposition |
|-------|-----------|-------------|
| **nano** | 1 skill, single clearly-bounded topic | Default — no action |
| **multi** | 2–9 skills, related area | Review for internal coherence; acceptable if skills serve distinct sub-problems |
| **large** | 10+ skills | Flag for split review — not mandatory, but requires justification |

**Current distribution:**

| Class | Plugins | Notes |
|-------|---------|-------|
| nano | 49 | Healthy — marketplace favors focused plugins |
| multi | 8 | `brainstorm-swarm` (4sk+12ag), `communication` (5), `deslop` (3), `plugin-dev` (8), `product-thinking` (5), `technical-copywriting` (5), `skillstack-workflows` (20-see large) |
| large | 1 | `skillstack-workflows` (20sk) — flagged, see below |

**`skillstack-workflows` flag:** 20 skills spans multiple domains (workflow orchestration, git, code review, CI/CD, verification). Post-Phase-5 candidate for split into a `spec-workflow` core plugin + contributions to E-domain plugins. Deferred — splitting requires updating 2 cross-refs and 20 SKILL.md files. Out of scope for this restructure pass.

---

## Final Domain Map

**Domains:**

| Code | Name | Plugin count | Skill count |
|------|------|-------------|-------------|
| E | Engineering | 24 | 35 |
| I | Meta-Infra | 17 | 41 |
| P | Managerial-Product | 13 | 20 |
| M | Marketing-Comms | 5 | 14 |

**Full assignment table:**

| Plugin | Domain | Rationale |
|--------|--------|-----------|
| `agent-evaluation` | Meta-Infra | Evaluates LLM agent quality — a CC meta-skill, not an app engineering topic |
| `agent-project-development` | Engineering | Builds agent systems — software engineering lifecycle |
| `api-design` | Engineering | REST/GraphQL/gRPC design — dev tooling |
| `bdi-mental-states` | Engineering | Agent reasoning architecture — applied to software agents |
| `brainstorm-swarm` | Managerial-Product | Ideation and decision-making runtime — PM/strategy use case |
| `cicd-pipelines` | Engineering | DevOps — unambiguously E |
| `cloud-finops` | Managerial-Product | Cost governance — managerial/financial, not engineering implementation |
| `code-review` | Engineering | Dev workflow — unambiguously E |
| `coding-discipline` | Engineering | Production coding behavioral contract — dev practice |
| `communication` | Marketing-Comms | Writing, editing, messaging — 5 communication skills |
| `consistency-standards` | Meta-Infra | Naming/taxonomy enforcement — CC convention management |
| `content-modelling` | Managerial-Product | CMS information architecture — product/editorial design |
| `context-compression` | Meta-Infra | CC session context management |
| `context-degradation` | Meta-Infra | CC session context management |
| `context-fundamentals` | Meta-Infra | CC session context management |
| `context-optimization` | Meta-Infra | CC session context management |
| `creative-problem-solving` | Managerial-Product | Ideation methodology — SCAMPER, lateral thinking, PM/strategy use |
| `critical-intuition` | Meta-Infra | Reasoning/stress-testing — meta-cognitive CC skill |
| `debugging` | Engineering | Bug investigation — core dev workflow |
| `deslop` | Marketing-Comms | AI-slop removal from editorial/marketing copy |
| `docker-containerization` | Engineering | Container infra — DevOps |
| `documentation-generator` | Engineering | Codebase docs generation — dev tooling |
| `edge-case-coverage` | Engineering | Boundary condition analysis — test/dev practice |
| `elicitation` | Meta-Infra | Deep-interview and requirements elicitation — CC meta-skill |
| `example-design` | Meta-Infra | Pedagogically effective code examples — plugin/skill authoring meta-skill |
| `filesystem-context` | Meta-Infra | CC session context via OS filesystem — CC-specific tooling |
| `frontend-design` | Engineering | UI/CSS/design systems — dev |
| `git-workflow` | Engineering | VCS workflow — dev |
| `gws-cli` | Engineering | Google Workspace CLI automation — scripting/tooling |
| `hindsight` | Meta-Infra | Session memory persistence + hook — CC operational plugin |
| `hosted-agents` | Engineering | Cloud agent deployment (sandboxed VMs) — infra engineering |
| `mcp-server` | Engineering | MCP server development — dev |
| `memory-systems` | Meta-Infra | Agent memory architecture frameworks — CC/agent meta-skill |
| `multi-agent-patterns` | Engineering | Multi-agent system architecture — software engineering |
| `navigation-design` | Engineering | Information architecture / wayfinding — UX engineering |
| `nextjs-development` | Engineering | Next.js framework — dev |
| `ontology-design` | Managerial-Product | Knowledge modeling — product/data architecture |
| `osint` | Meta-Infra | Intelligence gathering methodology — research meta-skill (see note) |
| `outcome-orientation` | Managerial-Product | OKR/KPI mechanics — PM tooling |
| `persona-definition` | Managerial-Product | User personas — UX/product research |
| `persona-mapping` | Managerial-Product | Stakeholder mapping — org/product design |
| `plugin-dev` | Meta-Infra | Claude Code plugin authoring — marketplace meta-skill |
| `prioritization` | Managerial-Product | RICE/MoSCoW — PM tooling |
| `product-thinking` | Managerial-Product | Product strategy suite — PM |
| `prompt-engineering` | Meta-Infra | LLM prompt design — CC/LLM meta-skill |
| `python-development` | Engineering | Python dev — language tooling |
| `react-development` | Engineering | React dev — framework tooling |
| `risk-management` | Managerial-Product | Risk registers, probability-impact matrices — PM/strategy |
| `skill-foundry` | Meta-Infra | SKILL.md authoring quality — marketplace meta-skill |
| `skillstack-workflows` | Meta-Infra | CC workflow orchestration — CC meta-skill |
| `storytelling` | Marketing-Comms | Narrative craft — writing/content |
| `systems-thinking` | Managerial-Product | Feedback loops, causal maps — strategic analysis |
| `technical-copywriting` | Marketing-Comms | Long-form technical article structure — content/writing |
| `test-driven-development` | Engineering | TDD methodology — dev practice |
| `testing-framework` | Engineering | Test infrastructure setup — dev tooling |
| `tool-design` | Engineering | Agent tool/function design — software engineering |
| `typescript-development` | Engineering | TypeScript dev — language tooling |
| `user-journey-design` | Managerial-Product | Journey maps, touchpoints — UX/product design |
| `ux-writing` | Marketing-Comms | Microcopy, error messages, interface text — content/writing |

---

## Domain Boundary Notes

### E/I boundary: where to classify "agent" plugins

Multi-agent-patterns, bdi-mental-states, agent-project-development → **E** (building software systems).
agent-evaluation, memory-systems, prompt-engineering → **I** (meta-skills for evaluating or enhancing how Claude Code operates).

Rule: if the plugin helps you *build* something (code, agent, API), it's E. If it helps Claude Code or LLM agents *operate better* (evaluate, remember, reason, compress context), it's I.

### P/I boundary: where to classify "thinking" plugins

creative-problem-solving, systems-thinking, critical-intuition — creative-problem-solving and systems-thinking → **P** (used in PM/strategy contexts). critical-intuition → **I** (stress-testing reasoning — more meta-cognitive than strategic).

### osint note

`osint` is I (meta-skill for information research) despite potential P use (competitive intelligence). Zero inbound refs from other plugins. Low usage signal — monitor. If a "competitive-intelligence" cluster forms in P later, reassign.

### gws-cli note

Assigned E (scripting/automation). Could be P (workspace productivity for non-dev users). Trigger surface is CLI-centric ("managing 18 Workspace APIs from the terminal") — E assignment holds until a non-dev usage pattern emerges.

---

## Action Log

No renames, merges, splits, or deprecations this phase. All 59 plugins keep current directory names and SKILL.md content.

| Action | Plugin | Status | Reason |
|--------|--------|--------|--------|
| Assign domain tag `Engineering` | 24 plugins | Phase 5 | `category` field update in plugin.json + marketplace + registry |
| Assign domain tag `Meta-Infra` | 17 plugins | Phase 5 | Same |
| Assign domain tag `Managerial-Product` | 13 plugins | Phase 5 | Same |
| Assign domain tag `Marketing-Comms` | 5 plugins | Phase 5 | Same |
| Flag `skillstack-workflows` for split | 1 plugin | Post-Phase-5 | Deferred — out of scope |
| Monitor `osint` usage | 1 plugin | Ongoing | 0 inbound refs; reassign if P cluster forms |

---

## Open Questions for Phase 3 (Gap Analysis)

1. **Marketing-Comms is thin (5 plugins, 14 skills).** Is this a real gap or correct? Skills exist: communication, deslop, technical-copywriting, ux-writing, storytelling. Missing candidates: social-media, brand-voice, SEO, email-marketing. Phase 3 will assess.
2. **No `data-engineering` or `database-design` plugin in E.** Large sub-domain absent from 24 E plugins. Gap or out of scope?
3. **No `security` plugin in E.** `code-review` has security checks but no dedicated security plugin. Real gap?
4. **`osint` is the only I plugin touching research methodology.** Is there a gap in "research + synthesis" as a meta-skill?
5. **`cloud-finops` is the only P plugin touching infrastructure.** No "infrastructure planning" or "capacity planning" peer.
6. **Plugin-to-domain ratio (M=5) vs expected user population.** If marketing/content users are 20%+ of the user base, M needs 10+ plugins. Phase 3 evidence needed.

---

*Decisions D-008 through D-010 logged in `hindsight/DECISIONS.md`*

---
*Generated manually from trigger-evals comparison + domain analysis · Pending Phase 3 approval*
