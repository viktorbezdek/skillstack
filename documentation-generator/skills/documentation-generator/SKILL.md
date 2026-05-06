---
name: documentation-generator
description: >-
  Generate comprehensive documentation for a codebase by reading the repository and
  producing READMEs, API docs, architecture docs, and technical references. Use when the
  user asks to "document this repo", "generate docs", "write a README", "create API
  documentation", "document this codebase", "write architecture docs", or "produce
  technical references" for an existing project. NOT for UX copy, button labels, or
  interface microcopy (use ux-writing). NOT for pedagogical code examples or tutorials
  (use example-design). NOT for inline code comments. NOT for navigation or sitemap design (use navigation-design).
---

# Repository Documentation Generator

Generate comprehensive documentation for repositories of any size - from small libraries to large monorepos. Creates both non-technical overviews and detailed technical references.

Each phase produces **mandatory output artifacts** — specific named sections and files that must appear in the output. Skipping a mandatory artifact means that phase is incomplete.

---

## Workflow Overview

```
1. ANALYSIS PHASE      → analysis.json (structure map)
2. PLANNING PHASE      → Audience table + prioritized doc backlog
3. STRUCTURE PHASE     → Diátaxis classification + navigation index
4. WRITING PHASE       → Per-doc-type required sections
5. COVERAGE PHASE      → Edge cases + user journey validation
6. VALIDATION PHASE    → DQI score + Known Gaps register
```

---

## Phase 1: Analysis

Run the analysis script first:

```bash
# Locate doc-gen.py (works regardless of installation path)
DOC_GEN=$(find ~/.claude -name "doc-gen.py" -path "*/documentation-generator/scripts/*" 2>/dev/null | head -1)
[ -z "$DOC_GEN" ] && DOC_GEN=$(find . -name "doc-gen.py" -path "*/documentation-generator/scripts/*" 2>/dev/null | head -1)

python "$DOC_GEN" analyze /path/to/repo --output analysis.json --pretty
```

If the script is unavailable, manually survey: public API surface, directory structure, existing docs (even if outdated), test files (they reveal use cases), and CI/CD configuration.

---

## Phase 2: Planning

### MANDATORY DELIVERABLE 1 — Audience Analysis

Before writing any documentation, produce a `## Target Audiences` section in README.md **or** a dedicated `docs/AUDIENCES.md` file. Required table schema:

```markdown
## Target Audiences

| Persona | Role | Background | Primary Question | First Doc to Read |
|---------|------|------------|-----------------|-------------------|
| New Backend Developer | Engineer | Knows the language, never seen this repo | "How do I run this locally in 5 minutes?" | GETTING-STARTED.md |
| DevOps / SRE | Infrastructure | Owns production | "What do I need to monitor and how do I deploy?" | OPERATIONS_RUNBOOK.md |
| External API Consumer | Integrator | Knows REST, unfamiliar with this system | "What endpoints exist and what do they return?" | API_REFERENCE.md |
```

**Requirements:**
- Minimum 2 distinct named personas. "Developer" or "User" without role/background/goal does NOT count.
- Each row must have a non-empty "First Doc to Read" pointing to an actual file you will produce.
- Derive personas from the codebase: test files reveal use cases; CI config reveals deployment audience; existing issues reveal confusion points.

### MANDATORY DELIVERABLE 2 — Prioritized Documentation Backlog

Produce a `## Documentation Plan` section (in a dedicated `DOC_PLAN.md`, `HANDOFF_PLAN.md`, or the README) with this schema:

```markdown
## Documentation Plan

| Doc | Audience | Diátaxis Type | Priority | Rationale |
|-----|----------|---------------|----------|-----------|
| README.md | All | Explanation | P0 | Entry point for every reader |
| GETTING-STARTED.md | New developers | Tutorial | P0 | Blocks onboarding |
| API_REFERENCE.md | External consumers | Reference | P1 | Required for integration |
| ARCHITECTURE.md | Senior engineers | Explanation | P1 | Needed for contribution |
| RUNBOOK.md | DevOps | How-To | P1 | Required for operations |
| CONTRIBUTING.md | Contributors | How-To | P2 | Enables community |
```

**Requirements:**
- `Diátaxis Type` must be one of: **Tutorial / How-To / Reference / Explanation** (see Phase 3).
- `Priority` must be **P0** (must ship), **P1** (should ship), or **P2** (nice to have).
- Every persona from Deliverable 1 must have at least one P0 or P1 doc that answers their Primary Question.

---

## Phase 3: Structure — Diátaxis Classification

Every documentation set must cover at least two of the four Diátaxis types. Blending types in one file (e.g., a README that is simultaneously tutorial + reference + explanation) produces docs that serve no reader well.

### The four types — use these to label every doc you produce

| Type | Reader's question | Structure | Anti-pattern |
|------|------------------|-----------|--------------|
| **Tutorial** | "Can I follow this and succeed?" | Steps, prerequisites, expected outcomes | Mixing reference into tutorials |
| **How-To** | "How do I solve this specific problem?" | Goal-first, steps, troubleshooting | Explaining why when the reader needs how |
| **Reference** | "What is the exact value/syntax/behavior?" | Tables, structured lists, no narrative | Adding tutorials or how-tos into reference |
| **Explanation** | "Why does this work this way?" | Prose, rationale, tradeoffs, history | Adding steps or commands |

### MANDATORY: Label each document with its type

Add one of these comments as the **first line** of every documentation file you produce:

```markdown
<!-- Doc-Type: Tutorial -->
<!-- Doc-Type: How-To -->
<!-- Doc-Type: Reference -->
<!-- Doc-Type: Explanation -->
```

The documentation set MUST include at least one Tutorial AND one Reference. If the repo has an API, add an Explanation doc for the architecture. If the repo has operational complexity, add a How-To runbook.

### Required sections by type

**Every Tutorial must include:**
```markdown
<!-- Doc-Type: Tutorial -->

## Before You Begin
- [x] Prerequisite 1 (e.g., Node 18+ installed)
- [x] Prerequisite 2

**Estimated time:** ~N minutes

## What You Will Learn
- How to do X
- How to configure Y
- How to verify Z works

[...steps...]

## Next Steps
- [Link to How-To guide] — for solving specific problems
- [Link to Reference] — for full API details
```

**Every How-To must include:**
```markdown
<!-- Doc-Type: How-To -->

## Goal
One sentence: what problem this solves.

[...steps...]

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Error message X | Missing env var Y | Set Y=... |
| Command fails with Z | Version mismatch | Upgrade to N+ |
```

**Every Reference doc must include:**
- A working code sample (5–20 lines) **at the top**, before parameter tables
- An error/exception table: `| Code/Exception | Cause | How to Resolve |`

**Every Explanation doc must include:**
- No numbered steps, no CLI commands in primary flow
- A "Why not X?" section addressing the most obvious alternative design

---

## Phase 4: Writing

Use the templates in `templates/` as structural scaffolding. The template directory includes:
- `templates/readme/standard.md` — README structure
- `templates/architecture/adr-template.md` — ADR with `## Status` heading
- `templates/operations/runbook.md` — operational how-to
- `templates/api/rest-endpoint.md` — API reference per endpoint

### ADR heading requirement

When generating Architecture Decision Records, use `## Status` as a **heading** (not a table row):

```markdown
## Status
Accepted  <!-- or: Proposed | Deprecated | Superseded by ADR-NNN -->

## Context
[Background and problem statement]

## Decision
[What was decided and why]

## Consequences
[Results — both positive and negative]
```

⛔ **Do NOT** use `| Status | Accepted |` as a table row. The heading format is required.

### Content owner metadata

Every documentation file you create should include metadata near the top or bottom:

```markdown
<!-- Last verified: YYYY-MM-DD | Owner: [team-name] -->
```

If the owner is unknown, use `Owner: unknown` — the placeholder is better than the absence.

---

## Phase 5: Coverage

For each produced document, ask:
1. **Edge cases** — what can go wrong? Does every procedure have a Troubleshooting section?
2. **User journey** — can a reader reach mastery following only the docs? Walk the path: discovery → install → first task → advanced usage.
3. **Version accuracy** — does the doc state which version it was verified against?

Add a version note to every doc that describes behavior that may change:

```markdown
<!-- Verified against v1.2.3 — update if behavior changes -->
```

---

## Phase 6: Validation

### MANDATORY DELIVERABLE 3 — Documentation Quality Score

After completing all documentation, compute a DQI score and include it in README.md or a dedicated `docs/QUALITY.md`. Use the criteria from `references/quality/document-quality-index.md`.

Required format:

```markdown
## Documentation Quality Score

| Category | Score | Notes |
|----------|-------|-------|
| Structure (40 pts) | X/40 | [what's strong or weak] |
| Content (30 pts) | X/30 | [what's strong or weak] |
| Style (30 pts) | X/30 | [what's strong or weak] |
| **Total** | **X/100** | |

Threshold: 70/100 minimum to declare documentation complete.
```

If the score is below 70, add a P0 improvement item to the Documentation Backlog explaining what would close the gap.

### MANDATORY DELIVERABLE 4 — Known Gaps Register

Produce a `## Known Gaps` section (in the README, DOC_PLAN, or a dedicated `docs/GAPS.md`) listing what is intentionally deferred, incomplete, or undocumentable:

```markdown
## Known Gaps

| Gap | Reason | Owner | Priority |
|-----|--------|-------|----------|
| Auth flow documentation | Requires internal SSO team input | @auth-team | P1 |
| gRPC proto reference | API not stable yet | @platform | P2 |
```

If there are no gaps, write: `No known gaps as of YYYY-MM-DD.` This proves the check ran.

---

## Template Portfolio

This skill includes **24 comprehensive templates** in `templates/`:

### Core Documentation
| Template | Location |
|----------|----------|
| README | `templates/readme/standard.md` |
| Quickstart | `templates/getting-started/quickstart.md` |
| Installation | `templates/getting-started/installation.md` |
| User Guide | `templates/guides/user-guide.md` |
| Configuration | `templates/guides/configuration.md` |
| Deployment | `templates/guides/deployment.md` |
| Contributing | `templates/contributing/CONTRIBUTING.md` |
| Changelog | `templates/changelog/CHANGELOG.md` |

### API Documentation
| Template | Location |
|----------|----------|
| API Overview | `templates/api/api-overview.md` |
| REST Endpoint | `templates/api/rest-endpoint.md` |
| GraphQL Schema | `templates/api/graphql-schema.md` |

### Architecture Documentation
| Template | Location |
|----------|----------|
| System Design | `templates/architecture/system-design.md` |
| Repository Structure | `templates/architecture/repository-structure.md` |
| Ownership Map | `templates/architecture/ownership-map.md` |
| Component Spec | `templates/architecture/component-spec.md` |
| Data Flow | `templates/architecture/data-flow.md` |
| ADR Template | `templates/architecture/adr-template.md` |

### Domain / Specs / Integrations / Operations
| Template | Location |
|----------|----------|
| Domain Spec | `templates/domain/domain-spec.md` |
| Ontology | `templates/domain/ontology.md` |
| Product Spec | `templates/specs/product-spec.md` |
| Feature Spec | `templates/specs/feature-spec.md` |
| External Integration | `templates/integrations/external-integration.md` |
| Runbook | `templates/operations/runbook.md` |
| Troubleshooting | `templates/operations/troubleshooting.md` |

---

## Examples of Correct Output

The following shows what the mandatory deliverables look like in practice.

<examples>
<example>
<description>A small Python library — correct Audience Analysis + Doc Backlog + Diátaxis labels</description>
<audience-analysis>
```markdown
## Target Audiences

| Persona | Role | Background | Primary Question | First Doc to Read |
|---------|------|------------|-----------------|-------------------|
| Library Consumer | Backend engineer | Knows Python, needs to integrate this | "How do I install it and make a first call?" | GETTING-STARTED.md |
| Contributor | Open-source developer | Familiar with the language, wants to add a feature | "How do I run tests and submit a PR?" | CONTRIBUTING.md |
```
</audience-analysis>
<doc-backlog>
```markdown
## Documentation Plan

| Doc | Audience | Diátaxis Type | Priority | Rationale |
|-----|----------|---------------|----------|-----------|
| README.md | All | Explanation | P0 | Entry point |
| GETTING-STARTED.md | Consumer | Tutorial | P0 | Blocks first use |
| API_REFERENCE.md | Consumer | Reference | P0 | Required for integration |
| CONTRIBUTING.md | Contributor | How-To | P1 | Enables contribution |
| ARCHITECTURE.md | Contributor | Explanation | P2 | Helps advanced contributors |
```
</doc-backlog>
<diátaxis-label>
```markdown
<!-- Doc-Type: Tutorial -->

## Before You Begin
- [x] Python 3.9+ installed
- [x] pip available

**Estimated time:** ~10 minutes

## What You Will Learn
- How to install the library
- How to make a basic API call
- How to handle errors
```
</diátaxis-label>
<quality-score>
```markdown
## Documentation Quality Score

| Category | Score | Notes |
|----------|-------|-------|
| Structure (40 pts) | 36/40 | Clear hierarchy; navigation index present |
| Content (30 pts) | 25/30 | API covered; missing edge-case table in reference |
| Style (30 pts) | 28/30 | Consistent tone and formatting throughout |
| **Total** | **89/100** | |
```
</quality-score>
<known-gaps>
```markdown
## Known Gaps

| Gap | Reason | Owner | Priority |
|-----|--------|-------|----------|
| Russian transliteration edge cases | No native speaker review yet | @l10n-team | P2 |
```
</known-gaps>
</example>
</examples>

---

## Script Commands

```bash
# Locate doc-gen.py once
DOC_GEN=$(find ~/.claude -name "doc-gen.py" -path "*/documentation-generator/scripts/*" 2>/dev/null | head -1)
[ -z "$DOC_GEN" ] && DOC_GEN=$(find . -name "doc-gen.py" -path "*/documentation-generator/scripts/*" 2>/dev/null | head -1)

# Full workflow
python "$DOC_GEN" full /path/to/repo

# Analyze structure
python "$DOC_GEN" analyze /path/to/repo --output analysis.json

# Generate docs
python "$DOC_GEN" generate /path/to/repo --output ./docs

# Validate and score (outputs DQI score)
python "$DOC_GEN" validate /path/to/docs --min-score 70

# Detect drift
python "$DOC_GEN" drift /path/to/repo --docs-path /path/to/docs
```

---

## Decision Tree: Which Doc Type First?

```
What does the user need documented?
├─ New repo with no docs → README (Explanation) + GETTING-STARTED (Tutorial)
├─ Existing repo, docs outdated → Audit with drift detection, then update
├─ API for external consumers → API reference (Reference) + usage examples (How-To)
├─ Internal system → Architecture (Explanation) + runbooks (How-To)
├─ Onboarding problem → GETTING-STARTED (Tutorial) + user guide (How-To)
└─ Full documentation project → Run all 6 phases; produce all 4 Mandatory Deliverables
```

---

## Anti-Patterns

- **Writing docs before running analysis** — scripts surface structure you will miss manually
- **Skipping Mandatory Deliverables** — audience table, doc backlog, DQI score, and gaps register are required, not optional
- **Blending Diátaxis types** — a README that is simultaneously tutorial + reference + explanation serves no reader well; split into separate docs
- **Generic personas** — "developers" is not a persona; it must have a role, background, and primary question
- **Template structure without required sections** — producing a Tutorial without `## Before You Begin` and `## What You Will Learn` is incomplete
- **No DQI score** — undocumented documentation quality always drifts; measure it at the end
- **Omitting the Known Gaps register** — unstated gaps become invisible technical debt; list them explicitly

---

## When NOT to Use This Skill

- Writing a single README for a small project — use `ux-writing` for concise copy
- Creating navigation structure for a docs site — use `navigation-design`
- Building a tutorial with runnable code — use `example-design`
- Writing inline code comments — this is not documentation generation

---

## Rules

1. **Produce all 4 mandatory deliverables** — Audience table, Doc backlog, DQI score, Known Gaps register. These are not optional.
2. **Label every doc with its Diátaxis type** — `<!-- Doc-Type: Tutorial -->` as first line.
3. **Match required sections to type** — Tutorials need Before/Learn/NextSteps; How-Tos need Troubleshooting table; Reference needs code sample at top + error table.
4. **Use templates as scaffolding** — don't reinvent structures the templates already provide.
5. **ADR Status is a heading** — `## Status`, never `| Status | Accepted |`.
6. **Run scripts first** — they handle initial analysis and validation scoring.
7. **Score ≥ 70 before declaring done** — if below 70, add the gap to the backlog as P0.
