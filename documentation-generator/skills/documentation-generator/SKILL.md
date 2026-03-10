---
name: documentation-generator
description: >-
  Generate comprehensive documentation for repositories of any size, from small libraries
  to large monorepos. Use when creating documentation, generating docs, writing READMEs,
  producing API docs, architecture docs, or technical references for a repository.
  NOT for UX copy or microcopy (use ux-writing).
---

# Repository Documentation Generator

Generate comprehensive documentation for repositories of any size - from small libraries to large monorepos. Creates both non-technical overviews and detailed technical references.

---

## Workflow Overview

Documentation generation follows this sequence:

```
1. ANALYSIS PHASE
   └─ Run scripts, understand repo structure

2. PLANNING PHASE
   └─ Load: persona-definition, persona-mapping, prioritization
   └─ Define audiences, prioritize doc types

3. STRUCTURE PHASE
   └─ Load: systems-thinking, ontology-design, navigation-design
   └─ Map system, define concepts, plan navigation

4. WRITING PHASE
   └─ Load: ux-writing, example-design, consistency-standards
   └─ Write content using templates

5. COVERAGE PHASE
   └─ Load: edge-case-coverage, user-journey-design
   └─ Ensure completeness, validate flows

6. VALIDATION PHASE
   └─ Load: outcome-orientation, risk-management
   └─ Measure quality, identify gaps
```

---

## Phase 1: Analysis

Run the analysis script first:

```bash
SKILL_DIR="{SKILL_DIR}"
python "$SKILL_DIR/scripts/doc-gen.py" analyze /path/to/repo --output analysis.json --pretty
```

---

## Phase 2: Planning - Load Supporting Skills

**MANDATORY: Load these skills before planning documentation:**

### Step 2.1: Define Target Personas
```
Load skill: persona-definition
```
Create 2-4 personas for documentation audiences:
- New developers (onboarding)
- Senior developers (architecture)
- DevOps/SRE (operations)
- External developers (API consumers)
- Non-technical stakeholders (overview)

### Step 2.2: Map Stakeholder Priority
```
Load skill: persona-mapping
```
Use Power-Interest matrix to prioritize:
- Who needs docs most urgently?
- Who has decision-making power?
- What's the communication strategy per persona?

### Step 2.3: Prioritize Documentation Types
```
Load skill: prioritization
```
Use RICE or ICE scoring to decide:
- Which docs to create first?
- What's the minimum viable documentation?
- What can wait for later iterations?

---

## Phase 3: Structure - Load Supporting Skills

**MANDATORY: Load these skills before structuring:**

### Step 3.1: Analyze System Architecture
```
Load skill: systems-thinking
```
Apply to architecture documentation:
- Identify feedback loops in the system
- Map component dependencies
- Find leverage points for understanding
- Document system archetypes

### Step 3.2: Define Domain Concepts
```
Load skill: ontology-design
```
Apply to domain documentation:
- Define core entities and relationships
- Create glossary of terms
- Establish taxonomy for concepts
- Map entity relationships

### Step 3.3: Plan Documentation Navigation
```
Load skill: navigation-design
```
Apply to doc site structure:
- Design information architecture
- Plan breadcrumb structure
- Create sitemap
- Ensure wayfinding clarity

---

## Phase 4: Writing - Load Supporting Skills

**MANDATORY: Load these skills during content creation:**

### Step 4.1: Write Interface Text
```
Load skill: ux-writing
```
Apply to all user-facing content:
- Error messages in troubleshooting docs
- Button/action labels in UI docs
- Empty states and loading states
- Confirmation dialogs

### Step 4.2: Create Code Examples
```
Load skill: example-design
```
Apply to API docs and tutorials:
- Progressive complexity (simple → advanced)
- Runnable, copy-paste ready
- Cover common use cases
- Include error handling

### Step 4.3: Ensure Consistency
```
Load skill: consistency-standards
```
Apply across all documentation:
- Naming conventions
- Terminology standardization
- Style guide adherence
- Content reuse patterns

---

## Phase 5: Coverage - Load Supporting Skills

**MANDATORY: Load these skills before finalizing:**

### Step 5.1: Cover Edge Cases
```
Load skill: edge-case-coverage
```
Apply to troubleshooting and API docs:
- Boundary conditions
- Error scenarios
- Corner cases
- Validation requirements

### Step 5.2: Validate User Journeys
```
Load skill: user-journey-design
```
Apply to getting started and tutorials:
- Map touchpoints through docs
- Identify emotional states (confusion, success)
- Find friction points
- Ensure smooth flow from awareness → mastery

---

## Phase 6: Validation - Load Supporting Skills

**MANDATORY: Load these skills for quality assurance:**

### Step 6.1: Measure Documentation Effectiveness
```
Load skill: outcome-orientation
```
Define success metrics:
- Time to first success (quickstart)
- Support ticket reduction
- Documentation coverage %
- User satisfaction scores

### Step 6.2: Identify Documentation Gaps
```
Load skill: risk-management
```
Create documentation risk register:
- What's missing?
- What's outdated?
- What causes confusion?
- Mitigation plan for gaps

---

## Template Portfolio

This skill includes **24 comprehensive templates**:

### Core Documentation
| Template | Location | Required Skills |
|----------|----------|-----------------|
| README | `templates/readme/standard.md` | ux-writing |
| Quickstart | `templates/getting-started/quickstart.md` | user-journey-design, example-design |
| Installation | `templates/getting-started/installation.md` | edge-case-coverage |
| User Guide | `templates/guides/user-guide.md` | persona-definition, example-design |
| Configuration | `templates/guides/configuration.md` | edge-case-coverage |
| Deployment | `templates/guides/deployment.md` | edge-case-coverage, risk-management |
| Contributing | `templates/contributing/CONTRIBUTING.md` | consistency-standards |
| Changelog | `templates/changelog/CHANGELOG.md` | - |

### API Documentation
| Template | Location | Required Skills |
|----------|----------|-----------------|
| API Overview | `templates/api/api-overview.md` | example-design, edge-case-coverage |
| REST Endpoint | `templates/api/rest-endpoint.md` | example-design, ux-writing |
| GraphQL Schema | `templates/api/graphql-schema.md` | ontology-design, example-design |

### Architecture Documentation
| Template | Location | Required Skills |
|----------|----------|-----------------|
| System Design | `templates/architecture/system-design.md` | systems-thinking |
| Repository Structure | `templates/architecture/repository-structure.md` | navigation-design |
| Ownership Map | `templates/architecture/ownership-map.md` | persona-mapping |
| Component Spec | `templates/architecture/component-spec.md` | systems-thinking |
| Data Flow | `templates/architecture/data-flow.md` | systems-thinking, ontology-design |
| ADR Template | `templates/architecture/adr-template.md` | risk-management |

### Domain Documentation
| Template | Location | Required Skills |
|----------|----------|-----------------|
| Domain Spec | `templates/domain/domain-spec.md` | ontology-design |
| Ontology | `templates/domain/ontology.md` | ontology-design |

### Specifications
| Template | Location | Required Skills |
|----------|----------|-----------------|
| Product Spec | `templates/specs/product-spec.md` | persona-definition, outcome-orientation |
| Feature Spec | `templates/specs/feature-spec.md` | user-journey-design, edge-case-coverage |

### Integrations
| Template | Location | Required Skills |
|----------|----------|-----------------|
| External Integration | `templates/integrations/external-integration.md` | edge-case-coverage, example-design |

### Operations
| Template | Location | Required Skills |
|----------|----------|-----------------|
| Runbook | `templates/operations/runbook.md` | edge-case-coverage, risk-management |
| Troubleshooting | `templates/operations/troubleshooting.md` | edge-case-coverage, ux-writing |

---

## Quick Reference: Which Skills to Load When

| Documentation Type | Load These Skills |
|--------------------|-------------------|
| **README** | ux-writing, persona-definition |
| **Getting Started** | user-journey-design, example-design |
| **API Reference** | example-design, edge-case-coverage, ux-writing |
| **Architecture** | systems-thinking, ontology-design |
| **Domain Model** | ontology-design |
| **Troubleshooting** | edge-case-coverage, ux-writing |
| **Operations** | risk-management, edge-case-coverage |
| **Full Doc Audit** | All skills in sequence |

---

## Script Commands

### Full Workflow
```bash
python "$SKILL_DIR/scripts/doc-gen.py" full /path/to/repo
```

### Individual Commands
```bash
# Analyze
python "$SKILL_DIR/scripts/doc-gen.py" analyze /path/to/repo --output analysis.json

# Generate
python "$SKILL_DIR/scripts/doc-gen.py" generate /path/to/repo --output ./docs

# Validate
python "$SKILL_DIR/scripts/doc-gen.py" validate /path/to/docs --min-score 70

# Check Links
python "$SKILL_DIR/scripts/doc-gen.py" check-links /path/to/docs

# Detect Drift
python "$SKILL_DIR/scripts/doc-gen.py" drift /path/to/repo --docs-path /path/to/docs
```

---

## Rules

1. **Load skills per phase** - Don't skip skill loading steps
2. **Run scripts first** - They handle initial analysis
3. **Use templates** - Don't reinvent document structures
4. **Apply skills to templates** - Each template has required skills
5. **Validate with outcome-orientation** - Measure doc effectiveness
6. **Audit with risk-management** - Identify and track gaps





