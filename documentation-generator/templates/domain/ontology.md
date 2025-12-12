# System Ontology: {{PROJECT_NAME}}

A comprehensive ontology defining all concepts, relationships, and classifications within {{PROJECT_NAME}}.

## Overview

This document defines the complete conceptual model of {{PROJECT_NAME}}, establishing a shared vocabulary and understanding across all stakeholders.

| Attribute | Value |
|-----------|-------|
| **Version** | {{ONTOLOGY_VERSION}} |
| **Last Updated** | {{LAST_UPDATED}} |
| **Maintainer** | @{{MAINTAINER}} |
| **Status** | {{STATUS}} |

---

## Concept Hierarchy

### Top-Level Categories

```
{{PROJECT_NAME}} Ontology
├── {{CATEGORY_1}}
│   ├── {{SUBCATEGORY_1_1}}
│   ├── {{SUBCATEGORY_1_2}}
│   └── {{SUBCATEGORY_1_3}}
├── {{CATEGORY_2}}
│   ├── {{SUBCATEGORY_2_1}}
│   └── {{SUBCATEGORY_2_2}}
├── {{CATEGORY_3}}
│   └── {{SUBCATEGORY_3_1}}
└── {{CATEGORY_4}}
    ├── {{SUBCATEGORY_4_1}}
    └── {{SUBCATEGORY_4_2}}
```

---

## Core Concepts

{{#CORE_CONCEPTS}}
### {{CONCEPT_NAME}}

| Attribute | Value |
|-----------|-------|
| **Category** | {{CATEGORY}} |
| **Parent Concept** | {{PARENT_CONCEPT}} |
| **Abstraction Level** | {{ABSTRACTION_LEVEL}} |
| **Domain** | {{DOMAIN}} |

#### Definition

{{FORMAL_DEFINITION}}

#### Informal Description

{{INFORMAL_DESCRIPTION}}

#### Properties

| Property | Type | Cardinality | Description |
|----------|------|-------------|-------------|
{{#PROPERTIES}}
| `{{PROPERTY_NAME}}` | {{TYPE}} | {{CARDINALITY}} | {{DESCRIPTION}} |
{{/PROPERTIES}}

#### Relationships

| Relationship | Target Concept | Cardinality | Description |
|--------------|----------------|-------------|-------------|
{{#RELATIONSHIPS}}
| {{RELATIONSHIP_TYPE}} | {{TARGET}} | {{CARDINALITY}} | {{DESCRIPTION}} |
{{/RELATIONSHIPS}}

#### Constraints

{{#CONSTRAINTS}}
- **{{CONSTRAINT_NAME}}:** {{CONSTRAINT_DESCRIPTION}}
{{/CONSTRAINTS}}

#### Examples

{{#EXAMPLES}}
- **{{EXAMPLE_NAME}}:** {{EXAMPLE_DESCRIPTION}}
{{/EXAMPLES}}

#### Anti-Examples (What This Is Not)

{{#ANTI_EXAMPLES}}
- {{ANTI_EXAMPLE}}
{{/ANTI_EXAMPLES}}

{{/CORE_CONCEPTS}}

---

## Relationship Types

### Structural Relationships

{{#STRUCTURAL_RELATIONSHIPS}}
#### {{RELATIONSHIP_NAME}}

| Attribute | Value |
|-----------|-------|
| **Type** | {{TYPE}} |
| **Inverse** | {{INVERSE}} |
| **Transitivity** | {{TRANSITIVITY}} |
| **Symmetry** | {{SYMMETRY}} |

**Definition:** {{DEFINITION}}

**Domain → Range:** {{DOMAIN}} → {{RANGE}}

**Examples:**
{{#EXAMPLES}}
- {{SOURCE}} {{RELATIONSHIP_NAME}} {{TARGET}}
{{/EXAMPLES}}

{{/STRUCTURAL_RELATIONSHIPS}}

### Behavioral Relationships

{{#BEHAVIORAL_RELATIONSHIPS}}
#### {{RELATIONSHIP_NAME}}

**Definition:** {{DEFINITION}}

**Participants:**
| Role | Concept | Cardinality |
|------|---------|-------------|
{{#PARTICIPANTS}}
| {{ROLE}} | {{CONCEPT}} | {{CARDINALITY}} |
{{/PARTICIPANTS}}

**Lifecycle:**
```
{{LIFECYCLE_DIAGRAM}}
```

{{/BEHAVIORAL_RELATIONSHIPS}}

---

## Taxonomies

### {{TAXONOMY_NAME}}

**Purpose:** {{TAXONOMY_PURPOSE}}

**Classification Criteria:** {{CLASSIFICATION_CRITERIA}}

```
{{TAXONOMY_NAME}}
{{TAXONOMY_TREE}}
```

#### Classification Rules

{{#CLASSIFICATION_RULES}}
| Category | Criteria | Examples |
|----------|----------|----------|
| {{CATEGORY}} | {{CRITERIA}} | {{EXAMPLES}} |
{{/CLASSIFICATION_RULES}}

---

## Entity Types

### Core Entities

| Entity | Description | Primary Key | Domain |
|--------|-------------|-------------|--------|
{{#CORE_ENTITIES}}
| {{ENTITY}} | {{DESCRIPTION}} | {{PRIMARY_KEY}} | {{DOMAIN}} |
{{/CORE_ENTITIES}}

### Supporting Entities

| Entity | Description | Related Core Entity |
|--------|-------------|---------------------|
{{#SUPPORTING_ENTITIES}}
| {{ENTITY}} | {{DESCRIPTION}} | {{RELATED_CORE}} |
{{/SUPPORTING_ENTITIES}}

### Reference Data

| Reference Type | Description | Cardinality | Mutability |
|----------------|-------------|-------------|------------|
{{#REFERENCE_DATA}}
| {{TYPE}} | {{DESCRIPTION}} | {{CARDINALITY}} | {{MUTABILITY}} |
{{/REFERENCE_DATA}}

---

## Value Types

### Primitive Value Types

| Type | Base Type | Constraints | Format |
|------|-----------|-------------|--------|
{{#PRIMITIVE_VALUES}}
| {{TYPE}} | {{BASE}} | {{CONSTRAINTS}} | {{FORMAT}} |
{{/PRIMITIVE_VALUES}}

### Complex Value Types

{{#COMPLEX_VALUES}}
#### {{VALUE_TYPE_NAME}}

**Purpose:** {{PURPOSE}}

**Structure:**
```{{CODE_LANG}}
{{STRUCTURE}}
```

**Validation Rules:**
{{#VALIDATION}}
- {{RULE}}
{{/VALIDATION}}

**Equality:** {{EQUALITY_DEFINITION}}

{{/COMPLEX_VALUES}}

### Enumerations

{{#ENUMERATIONS}}
#### {{ENUM_NAME}}

**Purpose:** {{PURPOSE}}

| Value | Code | Description |
|-------|------|-------------|
{{#VALUES}}
| {{VALUE}} | `{{CODE}}` | {{DESCRIPTION}} |
{{/VALUES}}

**Ordering:** {{ORDERING}}

**Extensible:** {{EXTENSIBLE}}

{{/ENUMERATIONS}}

---

## State Models

{{#STATE_MODELS}}
### {{ENTITY_NAME}} States

```
{{STATE_DIAGRAM}}
```

| State | Description | Entry Conditions | Exit Conditions |
|-------|-------------|------------------|-----------------|
{{#STATES}}
| {{STATE}} | {{DESCRIPTION}} | {{ENTRY}} | {{EXIT}} |
{{/STATES}}

#### Transitions

| From | To | Trigger | Guard | Action |
|------|----|---------|-------|--------|
{{#TRANSITIONS}}
| {{FROM}} | {{TO}} | {{TRIGGER}} | {{GUARD}} | {{ACTION}} |
{{/TRANSITIONS}}

{{/STATE_MODELS}}

---

## Process Models

{{#PROCESSES}}
### {{PROCESS_NAME}}

**Purpose:** {{PURPOSE}}

**Actors:**
{{#ACTORS}}
- {{ACTOR}} - {{ROLE}}
{{/ACTORS}}

**Flow:**
```
{{PROCESS_FLOW_DIAGRAM}}
```

**Steps:**

| Step | Actor | Action | Input | Output |
|------|-------|--------|-------|--------|
{{#STEPS}}
| {{STEP_NUM}} | {{ACTOR}} | {{ACTION}} | {{INPUT}} | {{OUTPUT}} |
{{/STEPS}}

**Business Rules Applied:**
{{#RULES_APPLIED}}
- {{RULE}}
{{/RULES_APPLIED}}

{{/PROCESSES}}

---

## Concept Mappings

### Internal Mappings

| Source Domain | Source Concept | Target Domain | Target Concept | Mapping Type |
|---------------|----------------|---------------|----------------|--------------|
{{#INTERNAL_MAPPINGS}}
| {{SOURCE_DOMAIN}} | {{SOURCE}} | {{TARGET_DOMAIN}} | {{TARGET}} | {{TYPE}} |
{{/INTERNAL_MAPPINGS}}

### External System Mappings

{{#EXTERNAL_MAPPINGS}}
#### {{EXTERNAL_SYSTEM}}

| Our Concept | Their Concept | Transformation | Notes |
|-------------|---------------|----------------|-------|
{{#MAPPINGS}}
| {{OUR_CONCEPT}} | {{THEIR_CONCEPT}} | {{TRANSFORMATION}} | {{NOTES}} |
{{/MAPPINGS}}

{{/EXTERNAL_MAPPINGS}}

---

## Semantic Constraints

### Integrity Constraints

{{#INTEGRITY_CONSTRAINTS}}
#### {{CONSTRAINT_NAME}}

**Type:** {{TYPE}}

**Expression:**
```
{{CONSTRAINT_EXPRESSION}}
```

**Enforcement:** {{ENFORCEMENT}}

**Violation Handling:** {{VIOLATION_HANDLING}}

{{/INTEGRITY_CONSTRAINTS}}

### Derivation Rules

{{#DERIVATION_RULES}}
#### {{DERIVED_CONCEPT}}

**Derived From:** {{SOURCE_CONCEPTS}}

**Rule:**
```
{{DERIVATION_RULE}}
```

**Caching:** {{CACHING_STRATEGY}}

{{/DERIVATION_RULES}}

---

## Temporal Aspects

### Time-Sensitive Concepts

| Concept | Temporal Type | Granularity | History Retention |
|---------|---------------|-------------|-------------------|
{{#TEMPORAL_CONCEPTS}}
| {{CONCEPT}} | {{TYPE}} | {{GRANULARITY}} | {{RETENTION}} |
{{/TEMPORAL_CONCEPTS}}

### Temporal Relationships

{{#TEMPORAL_RELATIONSHIPS}}
#### {{RELATIONSHIP_NAME}}

**Type:** {{TEMPORAL_TYPE}}

**Concepts:** {{CONCEPT_A}} ↔ {{CONCEPT_B}}

**Temporal Expression:** {{EXPRESSION}}

{{/TEMPORAL_RELATIONSHIPS}}

---

## Measurement & Metrics

### Measured Properties

| Concept | Property | Unit | Precision | Range |
|---------|----------|------|-----------|-------|
{{#MEASURED_PROPERTIES}}
| {{CONCEPT}} | {{PROPERTY}} | {{UNIT}} | {{PRECISION}} | {{RANGE}} |
{{/MEASURED_PROPERTIES}}

### Derived Metrics

| Metric | Formula | Source Data | Update Frequency |
|--------|---------|-------------|------------------|
{{#DERIVED_METRICS}}
| {{METRIC}} | {{FORMULA}} | {{SOURCE}} | {{FREQUENCY}} |
{{/DERIVED_METRICS}}

---

## Visualization

### Concept Map

```
{{CONCEPT_MAP_DIAGRAM}}
```

### Entity-Relationship Diagram

```
{{ER_DIAGRAM}}
```

### Domain Boundaries

```
{{DOMAIN_BOUNDARY_DIAGRAM}}
```

---

## Usage Guidelines

### Naming Conventions

| Category | Convention | Example |
|----------|------------|---------|
{{#NAMING_CONVENTIONS}}
| {{CATEGORY}} | {{CONVENTION}} | {{EXAMPLE}} |
{{/NAMING_CONVENTIONS}}

### Documentation Standards

{{#DOC_STANDARDS}}
- **{{STANDARD}}:** {{DESCRIPTION}}
{{/DOC_STANDARDS}}

### Common Mistakes

{{#COMMON_MISTAKES}}
#### {{MISTAKE}}

**Wrong:** {{WRONG_EXAMPLE}}

**Right:** {{RIGHT_EXAMPLE}}

**Why:** {{EXPLANATION}}

{{/COMMON_MISTAKES}}

---

## Governance

### Change Process

1. {{CHANGE_STEP_1}}
2. {{CHANGE_STEP_2}}
3. {{CHANGE_STEP_3}}
4. {{CHANGE_STEP_4}}

### Review Board

| Member | Role | Domain Expertise |
|--------|------|------------------|
{{#REVIEW_BOARD}}
| @{{MEMBER}} | {{ROLE}} | {{EXPERTISE}} |
{{/REVIEW_BOARD}}

### Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
{{#VERSION_HISTORY}}
| {{VERSION}} | {{DATE}} | @{{AUTHOR}} | {{CHANGES}} |
{{/VERSION_HISTORY}}

---

## References

### Standards

{{#STANDARDS}}
- [{{STANDARD_NAME}}]({{URL}}) - {{DESCRIPTION}}
{{/STANDARDS}}

### Related Ontologies

{{#RELATED_ONTOLOGIES}}
- [{{NAME}}]({{URL}}) - {{RELATIONSHIP}}
{{/RELATED_ONTOLOGIES}}

### Academic References

{{#ACADEMIC_REFS}}
- {{CITATION}}
{{/ACADEMIC_REFS}}

---

## Appendix

### Glossary Index

{{#GLOSSARY_INDEX}}
| Term | Definition | First Defined |
|------|------------|---------------|
{{#TERMS}}
| {{TERM}} | {{DEFINITION}} | [{{SECTION}}](#{{ANCHOR}}) |
{{/TERMS}}
{{/GLOSSARY_INDEX}}

### Symbol Legend

| Symbol | Meaning |
|--------|---------|
{{#SYMBOLS}}
| {{SYMBOL}} | {{MEANING}} |
{{/SYMBOLS}}
