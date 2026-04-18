> **v1.1.16** | Documentation | 18 iterations

# Documentation Generator

> Generate comprehensive documentation for repositories of any size -- from small libraries to large monorepos -- with audience-aware personas, automated analysis, 24 templates, skill-orchestrated writing, and quality validation.
> Single skill + 6 scripts + 24 templates + 1 example | 13 trigger evals, 3 output evals

## The Problem

Documentation is where good software goes to be misunderstood. Most repositories have either no documentation, outdated documentation, or documentation written by the developer who built the system -- who is the worst person to explain it because they cannot see what is not obvious. The result: new developers take weeks to onboard, external teams misuse APIs, operations teams create runbooks from tribal knowledge, and stakeholders make decisions based on incomplete understanding.

The underlying problem is that documentation generation is a multi-disciplinary task disguised as a writing exercise. Effective documentation requires understanding your audience (persona definition), structuring information for discovery (navigation design), modeling domain concepts (ontology design), writing clear interface text (UX writing), covering edge cases (edge case coverage), and measuring effectiveness (outcome orientation). Most documentation efforts fail because they treat it as "just write it down" rather than as a design problem with its own methodology and quality metrics.

The cost of bad documentation compounds exponentially. One developer misunderstanding an API writes code that creates three support tickets. Three support tickets create a FAQ document that contradicts the official docs. The contradictory FAQ confuses the next developer more than having no documentation at all. Within a year, the team's documentation is an unreliable maze that everyone avoids and nobody trusts.

## The Solution

This plugin provides a six-phase documentation generation workflow -- Analysis, Planning, Structure, Writing, Coverage, and Validation -- that orchestrates 10+ SkillStack plugins to produce professional documentation. It ships with 24 comprehensive templates covering READMEs, quickstarts, API references, architecture documents, domain specifications, operations runbooks, and more. An analysis script examines repository structure automatically, and a validation script measures documentation quality with configurable minimum scores.

The key innovation is skill orchestration: each phase loads specific SkillStack plugins to apply domain expertise. Planning uses persona-definition and persona-mapping to identify audiences, then prioritization to decide what to write first. Structure uses systems-thinking and ontology-design to model the domain. Writing uses ux-writing for clear copy, example-design for code samples, and consistency-standards for uniform style. Coverage uses edge-case-coverage and user-journey-design to catch gaps. Validation uses outcome-orientation and risk-management to measure and improve.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Documentation written by developers who cannot see what is not obvious to newcomers | Persona-driven documentation targeting specific audiences: new developers, senior architects, DevOps, external consumers |
| No structure: docs are a flat list of markdown files with no navigation plan | Navigation design with information architecture, breadcrumbs, and sitemaps planned before writing |
| Domain concepts are undefined -- different docs use different terms for the same thing | Ontology design creates a glossary, taxonomy, and entity relationship map before any writing begins |
| Code examples are copy-pasted from tests, not designed for learning | Example design with progressive complexity: simple, realistic, advanced, error-handling |
| No way to measure documentation quality or detect drift from code | Validation script scores documentation and drift detection compares docs against current codebase |
| Documentation is a one-time effort that rots immediately | Quality tracking with minimum scores, link checking, and drift detection integrated into workflow |

## Context to Provide

The documentation generator's most valuable phase is analysis -- which requires knowing what you are documenting, who will read it, and what problem the documentation must solve. Skipping to "generate docs" without specifying audience and purpose produces well-structured documentation that addresses the wrong questions.

**What to include in your prompt:**
- **Repository path or description** of the codebase (languages, frameworks, architecture) -- the analysis script uses this; for conversational requests, describe the structure
- **Primary audience** (new developers joining the team, senior architects evaluating the system, DevOps/SRE on-call, external API consumers, open-source contributors) -- this drives which document types are highest priority
- **The specific problem** you are solving (onboarding takes 3 weeks, API consumers create wrong integrations, incidents last longer without runbooks, docs are outdated) -- this focuses the documentation effort
- **What already exists** -- existing docs, even poor ones, change the task from "generate" to "improve and fill gaps"
- **Quality constraints** -- minimum acceptable quality score, whether drift detection matters, link validation requirements

**What makes results better:**
- Running `python doc-gen.py analyze /path/to/repo --output analysis.json` first and sharing the output -- enables data-driven prioritization
- Specifying the onboarding target (new developer should be running the app in X minutes) -- gives the quickstart a concrete success criterion
- Naming the audience's assumed knowledge level ("they know Python but not our architecture")
- Stating which document types are most urgent vs. nice-to-have

**What makes results worse:**
- "Write some docs" without audience or problem -- produces documentation that is technically complete but doesn't solve the actual gap
- Skipping the analysis phase and jumping to writing -- misses the prioritization that makes the documentation effort efficient
- Expecting a single prompt to produce final documentation -- the first pass creates structure; editing passes add project-specific depth

**Template prompt:**
```
Generate documentation for [repository description or path]. Primary audience: [who will read it -- be specific]. The problem I am solving: [what fails without this documentation]. Existing documentation: [what exists and how outdated it is]. Start with the analysis phase and tell me what document types are missing and in what priority order.
```

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install documentation-generator@skillstack
```

### Prerequisites

Python 3 for the analysis and validation scripts. For maximum value, install these complementary SkillStack plugins that the generator orchestrates:
- `persona-definition` and `persona-mapping` (audience analysis)
- `systems-thinking` and `ontology-design` (domain modeling)
- `ux-writing` and `example-design` (content quality)
- `edge-case-coverage` and `user-journey-design` (completeness)
- `outcome-orientation` and `risk-management` (quality measurement)

The generator works without these plugins but produces better documentation when they are available.

### Verify installation

After installing, test with:

```
Generate documentation for this repository. Start with the analysis phase and tell me what doc types are needed.
```

## Quick Start

1. Install the plugin using the commands above
2. Run the analysis script: `python scripts/doc-gen.py analyze /path/to/repo --output analysis.json --pretty`
3. Ask: `"Based on this analysis, what documentation does this repository need? Prioritize by audience impact."`
4. The skill loads persona-definition and prioritization to recommend doc types in priority order
5. Ask: `"Generate a quickstart guide for new developers using the quickstart template."`

---

## System Overview

```
documentation-generator (plugin)
└── documentation-generator (skill)
    ├── 6-phase workflow
    │   ├── Phase 1: Analysis (repo scanning script)
    │   ├── Phase 2: Planning (persona-definition, persona-mapping, prioritization)
    │   ├── Phase 3: Structure (systems-thinking, ontology-design, navigation-design)
    │   ├── Phase 4: Writing (ux-writing, example-design, consistency-standards)
    │   ├── Phase 5: Coverage (edge-case-coverage, user-journey-design)
    │   └── Phase 6: Validation (outcome-orientation, risk-management)
    ├── Scripts
    │   ├── doc-gen.py (unified CLI: analyze, generate, validate, check-links, drift)
    │   ├── core/analyze_repo.py (repository structure analysis)
    │   ├── generation/generate_docs.py (document generation)
    │   ├── validation/validate_docs.py (quality scoring)
    │   ├── validation/check_links.py (link validation)
    │   └── management/detect_drift.py (code-docs drift detection)
    └── Templates (24)
        ├── Core: README, quickstart, installation, user guide, config, deployment, contributing, changelog
        ├── API: overview, REST endpoint, GraphQL schema
        ├── Architecture: system design, repo structure, ownership map, component spec, data flow, ADR
        ├── Domain: domain spec, ontology
        ├── Specs: product spec, feature spec
        ├── Integrations: external integration
        └── Operations: runbook, troubleshooting
```

## What's Inside

| Component | Type | Description |
|---|---|---|
| `documentation-generator` | Skill | Six-phase workflow orchestrating 10+ skills for comprehensive documentation |
| `doc-gen.py` | Script | Unified CLI for analysis, generation, validation, link checking, and drift detection |
| `analyze_repo.py` | Script | Scans repository structure, languages, frameworks, and documentation gaps |
| `generate_docs.py` | Script | Generates documentation from templates with repo-specific content |
| `validate_docs.py` | Script | Scores documentation quality against configurable thresholds |
| `check_links.py` | Script | Validates all links in documentation files |
| `detect_drift.py` | Script | Detects where documentation has drifted from current code |
| 24 templates | Templates | Complete template portfolio for every documentation type (see template table below) |
| `sample-readme.md` | Example | Reference README demonstrating the template output |
| Trigger evals | Test suite | 13 trigger evaluation cases |
| Output evals | Test suite | 3 output quality evaluation cases |

### Component Spotlights

#### documentation-generator (skill)

**What it does:** Activates when users need to create, audit, or improve repository documentation. Orchestrates a six-phase workflow that uses specialized SkillStack plugins at each phase -- from audience analysis through domain modeling, content writing, coverage checking, to quality validation.

**Input -> Output:** A repository path or documentation request -> Structured documentation following the appropriate template, with audience-aware language, progressive complexity, consistent terminology, and measurable quality scores.

**When to use:**
- Creating documentation for a new repository
- Auditing and improving existing documentation
- Generating API references, architecture docs, or quickstart guides
- Building a documentation site structure
- Measuring documentation quality and detecting drift

**When NOT to use:**
- Writing UX microcopy or interface text (use `ux-writing` directly)

**Try these prompts:**

```
Analyze this TypeScript monorepo with 4 packages and 12 microservices. We have a README and some inline comments but nothing else. Our team doubled in size and new developers take 3 weeks to onboard. Prioritize by what will most reduce onboarding time. Here is the analysis output:

[paste doc-gen.py analyze output]
```

```
Generate a quickstart guide for new developers joining our Node.js/PostgreSQL project. They know JavaScript but not our domain. Success criterion: they should have the app running locally and have made their first API call within 5 minutes. They start from cloning the repo.
```

```
Create REST API documentation for our /api/users and /api/orders endpoints. Include: authentication (JWT Bearer), request/response schemas, all error codes with explanations, pagination, and runnable code examples in Python and JavaScript. Our current API spec is missing error code documentation and examples.
```

```
Our API documentation is 6 months old and we've done two major refactors since. Run drift detection and tell me specifically which endpoint docs, response schemas, and code examples are now wrong or outdated. Repo is at /Users/me/myproject, docs are at /Users/me/myproject/docs.
```

**Template portfolio (24 templates):**

| Category | Templates | Orchestrated Skills |
|---|---|---|
| Core | README, quickstart, installation, user guide, configuration, deployment, contributing, changelog | ux-writing, persona-definition, user-journey-design |
| API | API overview, REST endpoint, GraphQL schema | example-design, edge-case-coverage, ux-writing |
| Architecture | System design, repo structure, ownership map, component spec, data flow, ADR | systems-thinking, ontology-design, navigation-design |
| Domain | Domain spec, ontology | ontology-design |
| Specs | Product spec, feature spec | persona-definition, outcome-orientation, user-journey-design |
| Integrations | External integration | edge-case-coverage, example-design |
| Operations | Runbook, troubleshooting | edge-case-coverage, risk-management, ux-writing |

#### doc-gen.py (script)

**CLI:**
```bash
python doc-gen.py analyze /path/to/repo --output analysis.json --pretty
python doc-gen.py generate /path/to/repo --output ./docs
python doc-gen.py validate /path/to/docs --min-score 70
python doc-gen.py check-links /path/to/docs
python doc-gen.py drift /path/to/repo --docs-path /path/to/docs
python doc-gen.py full /path/to/repo  # Run entire workflow
```

**What it produces:**
- `analyze`: JSON report of repository structure, languages, frameworks, existing docs, and gaps
- `generate`: Documentation files from templates, customized for the repository
- `validate`: Quality score with per-document breakdowns and improvement recommendations
- `check-links`: Report of broken internal and external links
- `drift`: List of documentation sections that no longer match the current code

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate) | Good (specific, activates reliably) |
|---|---|
| "Write some docs" | "Analyze this repo and generate a prioritized documentation plan targeting new developers and API consumers" |
| "Make a README" | "Generate a README for this TypeScript library following the standard template, with quickstart, API reference, and examples" |
| "Document the API" | "Create REST endpoint documentation for /api/users including auth, pagination, error codes, and Python/JS code examples" |
| "Update the docs" | "Run drift detection against our codebase and show me which documentation sections are outdated" |

### Structured Prompt Templates

**For full documentation generation:**
```
Generate documentation for [repo path]. Primary audience: [new developers / senior architects / DevOps / external consumers]. Priority: [onboarding speed / API accuracy / operational safety]. Start with the analysis phase.
```

**For specific document types:**
```
Create a [document type: quickstart / API reference / architecture doc / runbook] for [component/service]. Key constraints: [reader should be able to X in Y minutes / must cover Z edge cases].
```

**For documentation audit:**
```
Audit the existing documentation in [docs path]. Score quality, check links, detect drift from the codebase at [repo path]. Minimum acceptable score: [N].
```

### Prompt Anti-Patterns

- **Skipping the analysis phase:** "Just generate the docs" misses the most valuable step. The analysis phase identifies what exists, what is missing, and what to prioritize. Always start with analysis.
- **Not specifying the audience:** "Write documentation" for whom? New developers need different docs than API consumers. Specify the target audience to get properly scoped content.
- **Expecting one-shot documentation:** Documentation generation is iterative. The first pass identifies structure and gaps; subsequent passes fill in details. Do not expect a single prompt to produce final documentation.

## Real-World Walkthrough

**Starting situation:** You are a tech lead at a company with a 200K-line monorepo. The project has grown from 3 developers to 15 in the past year. Onboarding takes 3 weeks because documentation is scattered -- some in the README, some in Confluence, some in developer heads. You need to fix this systematically.

**Step 1: Analysis.** You run the analysis script: `python doc-gen.py analyze ./monorepo --output analysis.json --pretty`. The script identifies 4 main packages, 12 services, 3 API boundaries, and 47 existing markdown files. Of those, 31 are outdated (last modified before the last major refactor). The skill loads persona-definition and identifies four documentation audiences: new developers (onboarding), senior developers (architecture decisions), DevOps team (deployment and operations), and external API consumers (integration).

**Step 2: Planning.** You ask: "Based on this analysis, what documentation should I create first? We need to cut onboarding from 3 weeks to 3 days."

The skill loads prioritization and applies RICE scoring. Top priority: quickstart guide (high reach: all new hires; high impact: directly reduces onboarding time; low effort: one document). Second: architecture overview with system design document (high impact: reduces "why is this designed this way?" questions that consume senior time). Third: API documentation for external consumers (high reach: partner integrations are blocked). Fourth: operations runbooks (medium reach but high severity when missing: outages last longer without them).

**Step 3: Structure.** The skill loads systems-thinking to map the monorepo architecture: 4 packages have clear dependency relationships, 12 services form 3 clusters, and the data flows through specific paths. It loads ontology-design to create a glossary: "tenant" means X in this codebase, "workspace" means Y, "environment" has a specific technical definition different from common usage. It loads navigation-design to plan the doc site: getting-started/ for onboarding, architecture/ for system understanding, api/ for references, operations/ for runbooks.

**Step 4: Writing.** The skill generates the quickstart guide using the `templates/getting-started/quickstart.md` template, loading ux-writing for clear instructional copy and example-design for the code samples. The quickstart includes: prerequisites check (3 items), clone and install (2 commands), environment setup (copy .env.example, configure 3 values), run the application (1 command), verify it works (what you should see), next steps (links to architecture doc for deeper understanding).

**Step 5: Coverage.** The skill loads edge-case-coverage to identify what the quickstart missed: what happens if Docker is not installed? What if port 3000 is in use? What if the database migration fails? Each edge case gets a troubleshooting entry. It loads user-journey-design to trace the new developer's path: the quickstart should lead naturally to the architecture doc, which should lead to the API reference. Each document links to the next.

**Step 6: Validation.** The skill runs `python doc-gen.py validate ./docs --min-score 70`. The quickstart scores 85. The architecture doc scores 72 (missing ADR references -- needs architectural decision records). The API docs score 68 (below threshold -- missing pagination and error code documentation). The link checker finds 4 broken links to old Confluence pages. The drift detector flags 3 sections referencing an API endpoint that was renamed.

**Final outcome:** Onboarding time drops from 3 weeks to 4 days. The documentation scores above 75 across all documents. Drift detection runs monthly to catch documentation rot before it accumulates.

**Gotchas discovered:** The biggest value was not the writing but the analysis and planning phases. Knowing what documentation was missing and in what priority order prevented the team from writing the wrong docs first. The glossary from ontology-design resolved a terminology confusion ("tenant" vs "workspace") that had caused two integration bugs.

## Usage Scenarios

### Scenario 1: New open-source library needs documentation

**Context:** You are releasing a TypeScript library. It has no documentation beyond code comments.

**You say:** "Generate complete documentation for this TypeScript library. It needs a README, quickstart, API reference, and contributing guide."

**The skill provides:**
- Analysis of the library structure, exported functions, and types
- README from `templates/readme/standard.md` with project description, installation, quickstart, API summary
- Quickstart from `templates/getting-started/quickstart.md` with progressive examples
- API reference from `templates/api/api-overview.md` with each exported function documented
- Contributing guide from `templates/contributing/CONTRIBUTING.md`

**You end up with:** Publication-ready documentation that covers every audience: casual users (README), new users (quickstart), power users (API reference), and contributors.

### Scenario 2: Auditing documentation for a growing team

**Context:** Your team doubled in size. New developers keep asking questions that "should be in the docs."

**You say:** "Audit our existing documentation. Score quality, find gaps, and tell me what to fix first to reduce new-developer questions."

**The skill provides:**
- Quality scores per document with specific improvement recommendations
- Gap analysis showing what documentation types are missing
- Link validation report
- Drift detection comparing docs against current code
- Prioritized fix list based on impact on developer experience

**You end up with:** A ranked action plan that addresses the highest-impact documentation gaps first.

### Scenario 3: Operations team needs runbooks

**Context:** Your SRE team handles incidents using tribal knowledge. There are no written runbooks.

**You say:** "Generate operations runbooks for our 5 critical services. Each runbook needs incident response procedures, health checks, and recovery steps."

**The skill provides:**
- Runbook from `templates/operations/runbook.md` for each service
- Health check commands and expected outputs
- Troubleshooting decision trees from `templates/operations/troubleshooting.md`
- Edge-case coverage for unusual failure modes

**You end up with:** Structured runbooks that any on-call engineer can follow, reducing incident response time and removing dependence on specific individuals.

---

## Decision Logic

**Which phase should I start with?**

Always start with Phase 1 (Analysis). The analysis script identifies repository structure, existing documentation, and gaps. Skipping to writing produces documentation that does not match what the repository actually needs.

**Which template should I use?**

The skill selects based on document purpose:
- New users need to get started -> `quickstart.md` and `installation.md`
- Developers need to understand the system -> `system-design.md` and `component-spec.md`
- API consumers need references -> `rest-endpoint.md` or `graphql-schema.md`
- Operations needs incident response -> `runbook.md` and `troubleshooting.md`
- Decision history needs recording -> `adr-template.md`

**When should I use the orchestrated skills vs. writing directly?**

For documentation that will be read by 10+ people or maintained long-term, use the full six-phase workflow with skill orchestration. For internal one-off documents or quick READMEs, the templates alone are sufficient without loading all supporting skills.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Documentation scores high but users still confused | Quality metrics measure structure and coverage, not clarity; users may understand the words but not the concepts | Load ux-writing and user-journey-design for a clarity pass; test documentation with an actual new user and observe where they get stuck |
| Drift detection misses semantic drift | Code behavior changed but the API signature did not; docs are technically accurate but practically misleading | Supplement drift detection with user feedback; semantic drift requires human or LLM review, not just string matching |
| Template output is generic | Generated docs follow the template but lack project-specific context and nuance | Templates are starting points; every generated document needs a project-specific editing pass that adds concrete details, examples, and context |

## Ideal For

- **Tech leads** responsible for documentation at companies where the team has grown and tribal knowledge no longer scales
- **Open-source maintainers** who need publication-ready documentation covering README, quickstart, API reference, and contributing guides
- **DevOps and SRE teams** who need structured runbooks and troubleshooting guides to reduce incident response dependence on individuals
- **Documentation engineers** who want a systematic methodology with quality measurement rather than ad-hoc writing

## Not For

- **UX microcopy or interface text** -- if you need button labels, error messages, or form instructions, use `ux-writing` directly
- **Single-file documentation** -- if you just need to write one README and do not need the full analysis/planning workflow, use the README template directly without the orchestration
- **Non-repository documentation** -- this skill is designed for software repositories; for general business documentation, the templates are less applicable

## Related Plugins

- **persona-definition** -- Create audience personas that drive documentation targeting (orchestrated in Phase 2)
- **persona-mapping** -- Map stakeholder priority for documentation effort allocation (orchestrated in Phase 2)
- **systems-thinking** -- Model system architecture for architecture documentation (orchestrated in Phase 3)
- **ontology-design** -- Define domain vocabulary and relationships for glossaries (orchestrated in Phase 3)
- **navigation-design** -- Plan documentation site structure and information architecture (orchestrated in Phase 3)
- **ux-writing** -- Write clear interface text and instructional copy (orchestrated in Phase 4)
- **example-design** -- Design progressive code examples for tutorials and API docs (orchestrated in Phase 4)
- **consistency-standards** -- Maintain uniform terminology and style across all documentation (orchestrated in Phase 4)
- **edge-case-coverage** -- Identify boundary conditions and error scenarios for troubleshooting docs (orchestrated in Phase 5)
- **user-journey-design** -- Map the reader's path through documentation to ensure smooth flow (orchestrated in Phase 5)
- **outcome-orientation** -- Define success metrics for documentation effectiveness (orchestrated in Phase 6)
- **risk-management** -- Identify documentation gaps and create improvement plans (orchestrated in Phase 6)

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
