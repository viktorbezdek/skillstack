# Phase 3: Gap Analysis

**Date:** 2026-06-05  **Status:** PENDING APPROVAL  **Source:** skill descriptions + domain map from Phase 2

## Method

Scanned all 102 skill descriptions for coverage signals. Checked `skillstack-workflows` for partial workflow coverage before declaring a gap. Rated severity:

- **P0** — conspicuous absence; high expected demand; every comparable dev/PM/marketing toolset covers this
- **P1** — real gap with documented user demand signals (ref-counts, cross-references, workflow steps pointing nowhere)
- **P2** — legitimate gap but lower population or out-of-scope for current marketplace positioning

---

## Engineering (E) — 24 plugins, 35 skills

### E-GAP-01: Database / SQL design `P0`

**What's missing:** SQL schema design, migration management, ORM patterns (Prisma, Drizzle, SQLAlchemy, Alembic), query optimization, indexing strategy, PostgreSQL-specific guidance.

**Signal:** `api-design` handles API contracts but defers persistence to the caller. `python-development` and `typescript-development` mention ORMs in passing but have no depth. Every app-build workflow in `skillstack-workflows` implicitly requires a data layer — nothing covers it.

**Partial coverage:** None. This is a clean gap.

**Recommendation:** Build `database-design` plugin (E). Single skill covering schema design, migration patterns, ORM selection, query optimization. High ROI — referenced by every backend build workflow.

---

### E-GAP-02: Security `P1`

**What's missing:** OWASP Top 10 patterns, authentication design (JWT, OAuth, sessions), secrets management, dependency scanning, security review checklists, threat modeling.

**Signal:** `code-review` description mentions "security" as one dimension of its multi-agent swarm review. `skillstack-workflows` has a "Systematic security audit workflow for hardening a codebase through structured multi-pass analysis." But neither is a standalone security skill users can invoke directly for security-first design.

**Partial coverage:** `skillstack-workflows/security-audit` workflow covers audit use case. `code-review` covers review. Gap is in **security design and implementation guidance** (how to build secure things, not just how to audit them).

**Recommendation:** Build `security-engineering` plugin (E). Scope: auth design, OWASP patterns, secrets management, dependency hygiene. NOT audit/review (covered). NOT pentest (out of scope for a coding assistant).

---

### E-GAP-03: Cloud infrastructure / IaC `P1`

**What's missing:** Terraform, CloudFormation, Pulumi, CDK — infrastructure-as-code authoring and design patterns. AWS/GCP/Azure architecture patterns.

**Signal:** `cicd-pipelines` mentions "Terraform" in its trigger description but only in the context of pipeline configuration. `cloud-finops` covers cost optimization but not architecture or deployment patterns. `docker-containerization` covers containers but not cloud orchestration. `hosted-agents` covers Anthropic-specific agent deployment.

**Partial coverage:** `cicd-pipelines` has shallow Terraform coverage. True IaC design is uncovered.

**Recommendation:** Build `cloud-infrastructure` plugin (E). Scope: IaC patterns (Terraform, CDK), cloud architecture, deployment strategies. Distinct from `cicd-pipelines` (pipeline automation) and `cloud-finops` (cost governance).

---

### E-GAP-04: Observability / monitoring `P2`

**What's missing:** Logging strategies, metrics design, distributed tracing, alerting, OpenTelemetry, SLO/SLA design, dashboarding.

**Signal:** `debugging` covers bug investigation but not production observability. `cicd-pipelines` mentions deployment but not post-deployment monitoring. No ref in any plugin to "observability", "metrics", "tracing", or "SLO".

**Partial coverage:** None.

**Recommendation:** Build `observability` plugin (E). Lower priority than E-GAP-01/02 — good standalone when the E domain matures.

---

### E-GAP-05: Additional language plugins `P2`

**What's missing:** Go, Rust, Java/Spring, C++, mobile (iOS/Swift, Android/Kotlin, React Native, Flutter).

**Signal:** Current language coverage: Python, TypeScript, React, Next.js. No compiled languages, no mobile.

**Partial coverage:** `testing-framework` is multi-language. `cicd-pipelines` is multi-language. Core workflow skills don't require language-specific plugins.

**Recommendation:** Build on demand. Go and Rust are higher priority than mobile given current marketplace positioning. Do not bulk-create — wait for user signal.

---

## Meta-Infra (I) — 17 plugins, 41 skills

### I-GAP-01: Research and synthesis `P1`

**What's missing:** General research methodology — multi-source synthesis, fact-checking, citation management, structured note-taking from web research. Distinct from `osint` (individual profiling) and `elicitation` (interview design).

**Signal:** `skillstack-workflows` has a "ramp-up workflow for understanding a new codebase fast" and "PM funnel for turning user research into product direction" — both assume research has already been done. Nothing guides the research act itself outside of OSINT.

**Partial coverage:** `osint` covers individual research. `elicitation` covers interview design. Neither covers "synthesize information from multiple web/doc sources into structured findings."

**Recommendation:** Build `research-synthesis` plugin (I). Scope: multi-source research, evidence triangulation, structured summarization, claim confidence scoring. High utility for all domains.

---

### I-GAP-02: LLM cost and model optimization `P2`

**What's missing:** Model selection strategy (when to use Haiku vs Sonnet vs Opus), inference cost profiling, batching strategies, prompt caching optimization, token budget management.

**Signal:** `context-compression` covers context size reduction. `skillstack-workflows` has a "cost optimization workflow for reducing LLM costs without degrading quality." But no standalone skill for model selection or inference economics.

**Partial coverage:** `skillstack-workflows/cost-optimizer` workflow. `context-compression` handles one dimension.

**Recommendation:** Lower priority — workflow coverage is adequate. Build standalone skill only if the workflow proves insufficient.

---

## Managerial-Product (P) — 13 plugins, 20 skills

### P-GAP-01: Competitive and market intelligence `P1`

**What's missing:** Competitor analysis frameworks, market sizing (TAM/SAM/SOM), positioning maps, SWOT/Porter's Five Forces applied to product decisions, win/loss analysis.

**Signal:** `product-thinking` covers product strategy and value proposition but explicitly excludes competitive analysis. `brainstorm-swarm` has a skeptic/pre-mortem persona but no dedicated competitive intelligence. `osint` covers individual profiling — not market/competitive research.

**Partial coverage:** None for market intelligence.

**Recommendation:** Build `competitive-intelligence` plugin (P). Scope: competitor research frameworks, market sizing, positioning analysis. Distinct from `osint` (individual), `product-thinking` (internal product decisions), `risk-management` (risk registers).

---

### P-GAP-02: Project and sprint management `P2`

**What's missing:** Sprint planning, agile ceremonies, Jira/Linear workflow guidance, capacity planning, team velocity, retrospectives.

**Signal:** `prioritization` covers what to work on. `outcome-orientation` covers goal setting. Neither covers the operational mechanics of running a sprint or managing a backlog at the ceremony level.

**Partial coverage:** `prioritization` handles backlog ranking. `product-thinking` handles strategy. Execution layer (sprint ops) is uncovered.

**Recommendation:** Build `agile-delivery` plugin (P). Lower priority — project management is well-served by external tools and documentation. Evaluate demand before building.

---

### P-GAP-03: Executive and board communication `P2`

**What's missing:** Executive summaries, board deck narratives, investor update formats, funding pitch structure for non-technical audiences.

**Signal:** `skillstack-workflows` has a "pitch workflow" (investor deck, board proposal) and "narrative for leadership." `communication` (M domain) covers writing clarity. But no P-domain skill for the strategic framing layer executives need.

**Partial coverage:** `skillstack-workflows/pitch` workflow. Adequate for most use cases.

**Recommendation:** Defer. Workflow coverage is sufficient. Reassess if pitch/board communication becomes a frequently-invoked standalone request.

---

## Marketing-Comms (M) — 5 plugins, 14 skills

M is the thinnest domain (5 plugins, 14 skills, 8% of total plugins). Current coverage is skewed toward long-form technical writing and editorial polish. Social, email, and brand are entirely absent.

### M-GAP-01: Social media content `P0`

**What's missing:** LinkedIn posts, Twitter/X threads, short-form content, social media strategy, platform-specific format optimization.

**Signal:** `technical-copywriting` ends at article distribution strategy (meta, social pull-quotes) but doesn't cover social-native content. `deslop` handles slop removal from existing content. No social-first content creation.

**Partial coverage:** `technical-copywriting` skill 1 ("Engineer the distribution layer") briefly mentions "social pull-quotes." Not sufficient for social content creation.

**Recommendation:** Build `social-media-content` plugin (M). Scope: LinkedIn posts, Twitter threads, short-form content, platform-specific tone. High demand for developer-marketers and founders.

---

### M-GAP-02: Email marketing / newsletters `P1`

**What's missing:** Email sequence design, newsletter structure, subject line optimization, CTR-driven copywriting, subscriber segmentation narrative.

**Signal:** `communication` (M) covers general writing. `technical-copywriting` covers articles. Neither covers email-format writing conventions.

**Partial coverage:** None.

**Recommendation:** Build `email-marketing` plugin (M). Scope: newsletter writing, email sequences, subject lines, conversion-focused copy. Distinct from `communication` (general writing) and `technical-copywriting` (long-form articles).

---

### M-GAP-03: Brand voice `P2`

**What's missing:** Brand voice development, tone-of-voice guidelines, style guide creation, voice consistency across touchpoints.

**Signal:** `consistency-standards` (I) covers naming and taxonomy but not brand voice. `deslop` standardizes tone by removing slop but doesn't build a positive voice standard.

**Partial coverage:** None.

**Recommendation:** Build `brand-voice` plugin (M). Lower priority — most users reach for this after establishing a content foundation.

---

### M-GAP-04: SEO writing `P2`

**What's missing:** SEO-optimized content writing, keyword integration, search intent alignment, on-page optimization guidance for writers.

**Signal:** `technical-copywriting` skill 1 covers meta description writing. `technical-copywriting` skill 5 covers audience profiling. Neither covers keyword strategy or search-intent alignment.

**Partial coverage:** Shallow coverage in `technical-copywriting` distribution skill.

**Recommendation:** Build `seo-writing` plugin (M) or extend `technical-copywriting` with an SEO skill. Extension is simpler — add as skill 6 to existing plugin.

---

## Cross-Domain Gaps

### X-GAP-01: Accessibility `P2`

**What's missing:** WCAG compliance, screen reader patterns, keyboard navigation, color contrast, accessible component design.

**Signal:** `frontend-design` and `navigation-design` cover visual design but have no accessibility dimension. `ux-writing` covers interface text but not accessibility. No `aria-label`, `WCAG`, or `a11y` references in any skill description.

**Domain:** E (implementation) with M input (accessible copy).

**Recommendation:** Extend `frontend-design` with an accessibility skill OR build standalone `accessibility` plugin (E).

---

### X-GAP-02: Data visualization `P2`

**What's missing:** Chart selection, data viz design principles, dashboard design, Plotly/D3/Observable patterns.

**Signal:** `communication` has a Mermaid/diagram skill for systems diagrams. `storytelling` covers data storytelling at narrative level. Neither covers charting implementation or visualization design.

**Domain:** E (implementation) or M (data storytelling craft).

**Recommendation:** Defer — niche enough that demand signal should precede build.

---

## Gap Summary Table

| ID | Domain | Gap | Severity | Partial | Recommendation |
|----|--------|-----|----------|---------|----------------|
| E-GAP-01 | E | Database / SQL design | P0 | None | Build `database-design` |
| E-GAP-02 | E | Security engineering | P1 | Workflow + code-review | Build `security-engineering` |
| E-GAP-03 | E | Cloud IaC | P1 | cicd-pipelines (shallow) | Build `cloud-infrastructure` |
| E-GAP-04 | E | Observability | P2 | None | Build later |
| E-GAP-05 | E | Go, Rust, mobile | P2 | testing-framework (multi-lang) | Build on demand |
| I-GAP-01 | I | Research and synthesis | P1 | osint (partial) | Build `research-synthesis` |
| I-GAP-02 | I | LLM cost/model selection | P2 | Workflow covers it | Defer |
| P-GAP-01 | P | Competitive intelligence | P1 | None | Build `competitive-intelligence` |
| P-GAP-02 | P | Sprint/agile delivery | P2 | prioritization (partial) | Evaluate demand |
| P-GAP-03 | P | Executive communication | P2 | Workflow covers it | Defer |
| M-GAP-01 | M | Social media content | P0 | technical-copywriting (shallow) | Build `social-media-content` |
| M-GAP-02 | M | Email marketing | P1 | None | Build `email-marketing` |
| M-GAP-03 | M | Brand voice | P2 | None | Build later |
| M-GAP-04 | M | SEO writing | P2 | technical-copywriting (shallow) | Extend or build |
| X-GAP-01 | E | Accessibility | P2 | None | Extend frontend-design |
| X-GAP-02 | E/M | Data visualization | P2 | communication (mermaid only) | Defer |

---

## Phase 5 Scope Implication

Phase 5 (migration) is **domain assignment** — setting `category` fields and regenerating collections. It does NOT include building new plugins. Gap analysis here establishes the forward roadmap only.

**P0 gaps (2):** E-GAP-01 (database), M-GAP-01 (social) — recommend building these first after Phase 5 lands.

**P1 gaps (4):** E-GAP-02, E-GAP-03, I-GAP-01, P-GAP-01, M-GAP-02 — second build wave.

**P2 gaps (10):** Build on demand or defer indefinitely.

---

*Decisions D-011 logged in `hindsight/DECISIONS.md`*

---
*Pending Phase 4 approval*
