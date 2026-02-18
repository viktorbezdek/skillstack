# Documentation Generator

> Generate comprehensive documentation for repositories of any size -- from small libraries to large monorepos -- creating both non-technical overviews and detailed technical references.

## Overview

Good documentation is the difference between a project that gets adopted and one that gets abandoned. Yet most teams either skip documentation entirely or produce inconsistent, incomplete docs that quickly drift out of sync with the code. This skill provides a structured, six-phase workflow that transforms any repository into a well-documented project with audience-appropriate content.

The Documentation Generator is designed for developers, tech leads, and DevRel teams who need to produce high-quality documentation at scale. It combines automated repository analysis with 24 battle-tested templates covering everything from READMEs and API references to architecture decision records and operational runbooks. The skill also integrates with other SkillStack skills to ensure documentation follows best practices for audience targeting, example design, edge case coverage, and information architecture.

As part of the SkillStack collection, this skill orchestrates multiple complementary skills during its six-phase workflow: persona-definition for audience targeting, systems-thinking for architecture docs, ontology-design for domain modeling, example-design for code samples, edge-case-coverage for troubleshooting guides, and outcome-orientation for measuring documentation effectiveness.

## What's Included

### References

- `references/frameworks/diataxis-framework.md` - The Diataxis documentation framework (tutorials, how-to guides, explanation, reference)
- `references/patterns/writing-for-audiences.md` - Patterns for writing documentation targeted at different audience levels
- `references/quality/document-quality-index.md` - Metrics and scoring for measuring documentation quality

### Scripts

- `scripts/doc-gen.py` - Main CLI entry point for all documentation generation commands (analyze, generate, validate, check-links, drift)
- `scripts/core/analyze_repo.py` - Repository structure analysis engine
- `scripts/generation/generate_docs.py` - Documentation generation from templates and analysis
- `scripts/validation/validate_docs.py` - Documentation quality validation and scoring
- `scripts/validation/check_links.py` - Link checker for internal and external documentation references
- `scripts/management/detect_drift.py` - Detect documentation drift from code changes

### Templates

- `templates/readme/standard.md` - Standard README template
- `templates/getting-started/quickstart.md` - Quickstart guide template
- `templates/getting-started/installation.md` - Installation guide template
- `templates/guides/user-guide.md` - User guide template
- `templates/guides/configuration.md` - Configuration reference template
- `templates/guides/deployment.md` - Deployment guide template
- `templates/contributing/CONTRIBUTING.md` - Contributing guidelines template
- `templates/changelog/CHANGELOG.md` - Changelog template
- `templates/api/api-overview.md` - API overview template
- `templates/api/rest-endpoint.md` - REST endpoint documentation template
- `templates/api/graphql-schema.md` - GraphQL schema documentation template
- `templates/architecture/system-design.md` - System design document template
- `templates/architecture/repository-structure.md` - Repository structure documentation template
- `templates/architecture/ownership-map.md` - Code ownership map template
- `templates/architecture/component-spec.md` - Component specification template
- `templates/architecture/data-flow.md` - Data flow diagram template
- `templates/architecture/adr-template.md` - Architecture Decision Record template
- `templates/domain/domain-spec.md` - Domain specification template
- `templates/domain/ontology.md` - Domain ontology template
- `templates/specs/product-spec.md` - Product specification template
- `templates/specs/feature-spec.md` - Feature specification template
- `templates/integrations/external-integration.md` - External integration documentation template
- `templates/operations/runbook.md` - Operations runbook template
- `templates/operations/troubleshooting.md` - Troubleshooting guide template

### Examples

- `examples/repo-docs/sample-readme.md` - Sample generated README demonstrating the output format

## Key Features

- Six-phase documentation workflow (Analysis, Planning, Structure, Writing, Coverage, Validation)
- Automated repository analysis that detects project structure, languages, and frameworks
- 24 comprehensive templates covering core docs, API references, architecture, domain models, specs, and operations
- Documentation quality scoring and validation with configurable minimum thresholds
- Link checking for both internal cross-references and external URLs
- Documentation drift detection that identifies when docs fall out of sync with code
- Integration with the Diataxis framework for structuring tutorials, how-to guides, explanations, and references
- Audience-aware writing with persona-based content targeting

## Usage Examples

**Generate full documentation for a repository:**
```
Generate comprehensive documentation for this repository.
```
Runs the full six-phase workflow: analyzes the repo, identifies audiences, structures the documentation, writes content using templates, validates coverage, and checks quality.

**Analyze a repository before writing docs:**
```
Analyze this repository and tell me what documentation it needs.
```
Runs the analysis script to understand project structure, then applies persona-definition and prioritization to recommend which documents to create first.

**Create API documentation:**
```
Generate REST API documentation for our user service endpoints.
```
Uses the REST endpoint template with example-design for code samples, edge-case-coverage for error scenarios, and ux-writing for clear error messages.

**Check documentation quality:**
```
Validate our existing documentation and identify gaps.
```
Runs validation scoring, link checking, and drift detection to produce a comprehensive quality report with specific improvement recommendations.

**Generate an Architecture Decision Record:**
```
Create an ADR for our decision to migrate from REST to GraphQL.
```
Uses the ADR template with systems-thinking for architectural impact analysis and risk-management for documenting trade-offs and mitigation strategies.

## Quick Start

1. **Analyze your repository** to understand its structure:
   ```bash
   python scripts/doc-gen.py analyze /path/to/repo --output analysis.json --pretty
   ```

2. **Generate documentation** from the analysis:
   ```bash
   python scripts/doc-gen.py generate /path/to/repo --output ./docs
   ```

3. **Validate the generated docs** against quality standards:
   ```bash
   python scripts/doc-gen.py validate ./docs --min-score 70
   ```

4. **Check all links** in the documentation:
   ```bash
   python scripts/doc-gen.py check-links ./docs
   ```

5. **Detect documentation drift** over time:
   ```bash
   python scripts/doc-gen.py drift /path/to/repo --docs-path ./docs
   ```

## Related Skills

- **example-design** -- Create effective code examples for API docs and tutorials
- **edge-case-coverage** -- Document boundary conditions and error scenarios thoroughly
- **frontend-design** -- Generate component library documentation and style guides
- **git-workflow** -- Generate changelogs and track documentation alongside code changes
- **debugging** -- Create troubleshooting guides and operational runbooks

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install documentation-generator@skillstack` -- 34 production-grade skills for Claude Code.
