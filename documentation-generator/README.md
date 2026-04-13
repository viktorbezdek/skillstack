> **v1.1.15** | Documentation | 17 iterations

# Documentation Generator

> Generate comprehensive documentation for repositories of any size -- from small libraries to large monorepos -- with audience-aware templates, automated analysis, and quality validation.

## The Problem

Documentation is where good intentions go to die. Every team agrees documentation matters. Few teams produce documentation that anyone actually reads. The README is either a single paragraph ("Install with npm install") or a 3,000-line dump that mixes installation, API reference, architecture decisions, and troubleshooting into an unsearchable wall of text. Neither helps the three different audiences who need it: the new developer trying to get started, the senior engineer understanding the architecture, and the DevOps engineer running it in production.

When teams do attempt comprehensive documentation, they face a blank page problem at scale. A monorepo with 50 services needs dozens of documents: READMEs, quickstart guides, API references, architecture docs, runbooks, troubleshooting guides, contributing guides, and domain specifications. Writing each from scratch produces inconsistent structure, terminology, and quality. Documentation for Service A covers error handling exhaustively while Service B does not mention it. The glossary in one guide contradicts terminology in another. And nobody validates whether the documentation actually helps users accomplish their goals or just checks a compliance box.

The result is documentation debt that compounds over time. New features ship without docs. Existing docs drift from reality. Teams answer the same questions in Slack that should be answered in documentation. Support tickets pile up for problems that are documented somewhere but unfindable. And the next person who tries to write documentation starts from scratch because there is no template, no process, and no quality standard.

## The Solution

This plugin provides a six-phase documentation workflow -- Analysis, Planning, Structure, Writing, Coverage, Validation -- with an automated analysis script, 24 document templates across 11 categories, and quality validation tooling. Instead of staring at a blank page, you run the analysis script against your repository, get a structural understanding of what needs to be documented, and fill in templates designed for specific documentation types and audiences.

The workflow integrates with 10 other SkillStack plugins at specific phases: persona-definition and persona-mapping for audience planning, prioritization for deciding what to document first, systems-thinking and ontology-design for architecture and domain documentation, navigation-design for information architecture, ux-writing for user-facing content, example-design for code samples, consistency-standards for terminology, edge-case-coverage for troubleshooting, user-journey-design for onboarding flows, outcome-orientation for measuring effectiveness, and risk-management for identifying gaps.

The result is not just documentation but a documentation system: repeatable, template-driven, audience-aware, and measurable. The same process works for a 500-line library and a 500,000-line monorepo.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Blank page paralysis -- where do you even start documenting a large repo? | Automated analysis script maps the repo structure, then templates provide starting points for every document type |
| One README tries to serve new developers, senior architects, and DevOps at the same time | Persona-driven planning creates audience-specific documents: quickstart, architecture, runbooks |
| Inconsistent documentation across services: different structure, terminology, and depth | 24 templates enforce consistent structure; consistency-standards skill standardizes terminology |
| Documentation drifts from code with no detection mechanism | Drift detection script compares docs against current code and flags discrepancies |
| No way to measure whether documentation actually helps users | Outcome-orientation phase defines success metrics: time-to-first-success, support ticket reduction |
| Code examples are outdated, incomplete, or do not run | Example-design skill ensures progressive complexity, runnable code, and error handling coverage |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install documentation-generator@skillstack
```

### Verify installation

After installing, test with:

```
Generate comprehensive documentation for this repository -- start by analyzing the codebase structure
```

## Quick Start

1. Install the plugin using the commands above
2. Ask for documentation: `Document this repository -- I need a README, quickstart guide, and API reference`
3. The skill runs the analysis script to understand repository structure, languages, frameworks, and dependencies
4. It generates documentation using the appropriate templates, tailored to your codebase
5. Validate with: `Check the documentation quality and identify any gaps`

## What's Inside

| Component | Description |
|---|---|
| `documentation-generator` skill | Core skill with the six-phase workflow (analysis, planning, structure, writing, coverage, validation), template portfolio, and supporting skill integration map |
| 3 reference documents | Diataxis framework for documentation types, writing for audiences guide, and document quality index |
| 24 document templates | README, quickstart, installation, user guide, configuration, deployment, contributing, changelog, API overview, REST endpoint, GraphQL schema, system design, repository structure, ownership map, component spec, data flow, ADR, domain spec, ontology, product spec, feature spec, external integration, runbook, troubleshooting |
| `doc-gen.py` script | Automated tooling: analyze repos, generate docs, validate quality, check links, detect drift |
| 13 trigger eval cases | Validates correct skill activation and near-miss rejection |
| 3 output eval cases | Tests documentation quality, completeness, and audience appropriateness |

### documentation-generator

**What it does:** Activates when you need to create documentation for a repository -- from a single README to a complete documentation suite. Runs automated analysis to understand the codebase, plans documentation based on audience personas, generates content using structured templates, and validates quality against measurable criteria.

**Try these prompts:**

```
Generate complete documentation for this repository -- README, quickstart, architecture docs, and API reference
```

```
I need to document our microservices monorepo -- there are 12 services with no documentation at all. Where do I start?
```

```
Write a quickstart guide that gets a new developer from clone to running the app in under 10 minutes
```

```
Create API documentation for our REST endpoints with examples, error codes, and authentication details
```

```
Audit our existing documentation -- what's missing, what's outdated, and what needs to be rewritten?
```

**Key references:**

| Reference | Topic |
|---|---|
| `frameworks/diataxis-framework.md` | Diataxis documentation framework: tutorials, how-to guides, reference, explanation -- when to use each type |
| `patterns/writing-for-audiences.md` | Audience-aware writing techniques for different personas (developers, operators, stakeholders) |
| `quality/document-quality-index.md` | Quality scoring rubric for measuring documentation effectiveness and completeness |

## Real-World Walkthrough

You just joined a company as a tech lead. The engineering team has 8 backend services, 2 frontend apps, and a shared library -- all in a monorepo with zero documentation. The README says "TODO: add docs." New developers take 2 weeks to become productive because everything is tribal knowledge passed through Slack threads and pair programming sessions. Your first mandate: document everything so the next hire ramps up in 3 days.

You open Claude Code in the monorepo root:

```
We have a monorepo with 8 backend services, 2 frontend apps, and a shared library. Zero documentation. New devs take 2 weeks to onboard. I need comprehensive docs that get the next hire productive in 3 days. Start with analysis.
```

The documentation-generator skill activates and runs the analysis phase. It executes `doc-gen.py analyze` against your repository, producing a structural map: languages (TypeScript, Go), frameworks (NestJS, React, Chi), database dependencies (PostgreSQL, Redis), build tools (Turborepo), and service boundaries. The analysis identifies 47 public API endpoints across the 8 services, 3 shared database schemas, and a message queue connecting 4 services.

**Planning phase:** The skill loads persona-definition to identify your audiences. For a 3-day onboarding goal, the primary persona is a new developer who needs to: understand the system architecture (day 1), set up a local development environment and run services (day 1), understand the service they are assigned to (day 2), and make their first contribution (day 3). Secondary personas are senior engineers reviewing architecture decisions and DevOps engineers running services in production.

The skill uses prioritization to determine document order. For the 3-day onboarding target, the minimum viable documentation is:
1. Root README with system overview and service map
2. Quickstart guide (clone to running in 30 minutes)
3. Architecture document with service interactions
4. Per-service README with API overview and ownership

**Structure phase:** The skill loads systems-thinking to map the service interactions. It identifies the request flow: API Gateway routes to services, services communicate through the message queue, all services share PostgreSQL through isolated schemas, and Redis handles caching and sessions. This map becomes the architecture document's core diagram.

It loads ontology-design to create a domain glossary. Terms like "workspace," "tenant," "project," and "environment" are used inconsistently across services. The skill establishes canonical definitions that all documentation will use, preventing the confusion that currently costs new developers days of "wait, is a workspace the same as a tenant?"

Navigation-design structures the documentation hierarchy: root README links to quickstart, quickstart links to per-service docs, per-service docs link to API references and architecture decisions. Every page has clear "next steps" so a reader never hits a dead end.

**Writing phase:** Using the templates, the skill generates the root README from `templates/readme/standard.md`, the quickstart from `templates/getting-started/quickstart.md`, the architecture doc from `templates/architecture/system-design.md`, and per-service READMEs from `templates/readme/standard.md` customized for each service. The example-design skill ensures all code examples are runnable -- the quickstart includes every command needed to go from `git clone` to seeing "Hello World" in the browser, including database setup, environment variables, and dependency installation.

The consistency-standards skill catches terminology issues: three services call the same concept "user," "account," and "profile." The documentation standardizes on "user" with a glossary entry explaining the mapping.

**Coverage phase:** Edge-case-coverage identifies common onboarding failure points: Docker not installed, wrong Node.js version, port conflicts, missing environment variables. Each gets a troubleshooting entry. User-journey-design maps the emotional arc of onboarding: excitement (day 1 quickstart works), frustration (day 2 first real task is confusing), and accomplishment (day 3 first PR merged). The documentation adds encouragement and "this is normal" notes at the frustration points.

**Validation phase:** The skill runs `doc-gen.py validate` against the generated documentation, scoring it on completeness (all services documented?), accuracy (do commands actually work?), and navigability (can you find what you need?). It identifies 3 gaps: the shared library has no documentation, the message queue schema is undocumented, and the deployment process is not covered. These go into the documentation risk register for the next iteration.

You deploy the documentation. The next hire clones the repo on Monday morning, follows the quickstart guide, has all 8 services running locally by lunch, understands the architecture by end of day, and merges their first PR on Wednesday. Onboarding time: 3 days, down from 14. The documentation paid for itself with the first hire.

## Usage Scenarios

### Scenario 1: Documenting a repository from scratch

**Context:** You have a mature codebase with hundreds of files but no documentation beyond inline comments. You need to create comprehensive docs.

**You say:** `Document this entire repository from scratch -- I need a README, architecture overview, and getting-started guide`

**The skill provides:**
- Automated analysis of repository structure, languages, frameworks, and dependencies
- Persona planning to determine audience priorities
- Template-driven generation for README, architecture docs, and quickstart guide
- Consistency validation across all generated documents

**You end up with:** A complete documentation package tailored to your repository's specific structure and technology stack.

### Scenario 2: Documenting a monorepo with multiple services

**Context:** Your monorepo has 12 services with varying levels of documentation -- some have READMEs, most have nothing, and there is no top-level overview.

**You say:** `I have a monorepo with 12 services and inconsistent documentation -- create a unified documentation structure`

**The skill provides:**
- Root-level README with service map and navigation
- Per-service README template applied consistently across all 12 services
- Architecture document showing service interactions and data flows
- Shared glossary to standardize terminology across services
- Link validation to ensure cross-references work

**You end up with:** A unified documentation structure where every service is documented to the same standard and readers can navigate between them.

### Scenario 3: Creating API documentation

**Context:** Your REST API has 30+ endpoints but the only documentation is Swagger auto-generation, which lacks examples, error descriptions, and authentication details.

**You say:** `Generate API documentation for our REST endpoints -- the Swagger output is not enough, I need real examples and error handling docs`

**The skill provides:**
- API overview document with authentication, rate limiting, and common patterns
- Per-endpoint documentation with request/response examples, error codes, and edge cases
- Progressive complexity in examples: basic request, with authentication, with pagination, with error handling
- Troubleshooting section for common API integration issues

**You end up with:** API documentation that developers can actually use to integrate with your API without reading your source code.

### Scenario 4: Auditing existing documentation

**Context:** Your team has been writing documentation for a year but nobody knows if it is complete, consistent, or up to date. You want to find and fix the gaps.

**You say:** `Audit our existing documentation -- find what's missing, what's outdated, and what needs to be rewritten`

**The skill provides:**
- Drift detection comparing documentation against current code
- Quality scoring using the document quality index
- Gap analysis identifying undocumented features, endpoints, and configuration options
- Risk register prioritizing documentation gaps by impact
- Link checking to find broken cross-references

**You end up with:** A prioritized remediation plan showing exactly which documents need updating, which are missing entirely, and which are actively misleading.

### Scenario 5: Writing operational runbooks

**Context:** Your team handles production incidents but response depends on whoever is on-call remembering the procedures. You need formal runbooks.

**You say:** `Create operational runbooks for our production services -- we need step-by-step procedures for common incidents`

**The skill provides:**
- Runbook template with severity classification, response steps, and escalation procedures
- Troubleshooting template with symptom-cause-resolution structure
- Edge case coverage for unusual failure modes
- Risk assessment for each documented procedure

**You end up with:** Step-by-step runbooks that any on-call engineer can follow during an incident, reducing mean-time-to-resolution and removing dependency on tribal knowledge.

## Ideal For

- **Teams with zero documentation** who need to go from nothing to comprehensive docs using a repeatable process
- **Monorepo maintainers** who need consistent documentation across many services with a unified navigation structure
- **Open source maintainers** who want professional-quality README, contributing guide, and API docs
- **Tech leads responsible for onboarding** who need documentation that actually reduces ramp-up time, not just checks a box
- **Organizations with documentation debt** who need to audit, prioritize, and systematically fill gaps

## Not For

- **UX copy and microcopy** (button labels, error messages, empty states) -- use [ux-writing](../ux-writing/) instead
- **API design decisions** (endpoint structure, versioning, error format) -- use [api-design](../api-design/) instead
- **Code-level documentation** (inline comments, docstrings) -- these are part of the code itself, not standalone documents

## How It Works Under the Hood

The plugin is a single-skill architecture with reference documents, 24 templates, and an automated analysis/validation script.

The **core skill** (`SKILL.md`) defines a six-phase workflow that integrates with 10 other SkillStack plugins at specific points: Analysis (automated repo scanning), Planning (persona-definition, persona-mapping, prioritization), Structure (systems-thinking, ontology-design, navigation-design), Writing (ux-writing, example-design, consistency-standards), Coverage (edge-case-coverage, user-journey-design), and Validation (outcome-orientation, risk-management). Each phase has mandatory skill-loading steps and specific application guidance.

The **reference library** provides three depth documents:
- **Diataxis framework** -- the four documentation types (tutorials, how-to guides, reference, explanation) and when each is appropriate
- **Writing for audiences** -- techniques for adapting content to different personas (developers, operators, stakeholders)
- **Document quality index** -- scoring rubric for measuring documentation completeness, accuracy, and effectiveness

The **template portfolio** (24 templates across 11 categories) provides structured starting points for every common documentation type: core docs (README, quickstart, installation, user guide, configuration, deployment, contributing, changelog), API docs (overview, REST endpoint, GraphQL schema), architecture docs (system design, repository structure, ownership map, component spec, data flow, ADR), domain docs (domain spec, ontology), specifications (product spec, feature spec), integrations (external integration), and operations (runbook, troubleshooting).

The **doc-gen.py script** automates five operations: `analyze` (scan repository structure), `generate` (create documentation from templates), `validate` (score documentation quality), `check-links` (find broken cross-references), and `drift` (detect discrepancies between code and docs).

## Related Plugins

- **[UX Writing](../ux-writing/)** -- Microcopy, error messages, and interface text used within the writing phase
- **[Example Design](../example-design/)** -- Code example methodology used for API docs and tutorials
- **[Consistency Standards](../consistency-standards/)** -- Naming conventions and terminology standardization across documentation
- **[Navigation Design](../navigation-design/)** -- Information architecture and wayfinding for documentation sites
- **[Systems Thinking](../systems-thinking/)** -- System mapping used for architecture documentation
- **[Ontology Design](../ontology-design/)** -- Domain concept modeling used for glossaries and domain docs

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
