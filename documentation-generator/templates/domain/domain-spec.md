# Domain Specification: {{DOMAIN_NAME}}

A complete specification of the {{DOMAIN_NAME}} domain within {{PROJECT_NAME}}.

## Overview

| Attribute | Value |
|-----------|-------|
| **Domain** | {{DOMAIN_NAME}} |
| **Bounded Context** | {{BOUNDED_CONTEXT}} |
| **Domain Expert** | @{{DOMAIN_EXPERT}} |
| **Technical Owner** | @{{TECH_OWNER}} |
| **Status** | {{STATUS}} |

### Domain Purpose

{{DOMAIN_PURPOSE}}

### Domain Boundaries

**This domain is responsible for:**
{{#RESPONSIBILITIES}}
- {{RESPONSIBILITY}}
{{/RESPONSIBILITIES}}

**This domain is NOT responsible for:**
{{#NOT_RESPONSIBILITIES}}
- {{NOT_RESPONSIBILITY}}
{{/NOT_RESPONSIBILITIES}}

---

## Strategic Design

### Domain Classification

| Attribute | Value | Rationale |
|-----------|-------|-----------|
| **Type** | {{DOMAIN_TYPE}} | {{TYPE_RATIONALE}} |
| **Priority** | {{PRIORITY}} | {{PRIORITY_RATIONALE}} |

**Domain Types:**
- **Core:** Competitive advantage, build in-house
- **Supporting:** Necessary but not differentiating
- **Generic:** Commodity, buy or use standard solutions

### Context Map

```
{{CONTEXT_MAP_DIAGRAM}}
```

### Relationships with Other Domains

{{#DOMAIN_RELATIONSHIPS}}
#### {{RELATED_DOMAIN}}

| Attribute | Value |
|-----------|-------|
| **Relationship Type** | {{RELATIONSHIP_TYPE}} |
| **Direction** | {{DIRECTION}} |
| **Integration Pattern** | {{INTEGRATION_PATTERN}} |

**Data Exchanged:**
{{#DATA_EXCHANGED}}
- `{{DATA}}` - {{DESCRIPTION}}
{{/DATA_EXCHANGED}}

**Contract:** [{{CONTRACT_NAME}}]({{CONTRACT_URL}})

{{/DOMAIN_RELATIONSHIPS}}

---

## Ubiquitous Language

### Glossary

| Term | Definition | Example | Anti-patterns |
|------|------------|---------|---------------|
{{#GLOSSARY}}
| **{{TERM}}** | {{DEFINITION}} | {{EXAMPLE}} | {{ANTI_PATTERNS}} |
{{/GLOSSARY}}

### Language Rules

{{#LANGUAGE_RULES}}
- **{{RULE_NAME}}:** {{RULE_DESCRIPTION}}
{{/LANGUAGE_RULES}}

### Term Relationships

```
{{TERM_RELATIONSHIP_DIAGRAM}}
```

---

## Domain Model

### Aggregates

{{#AGGREGATES}}
#### {{AGGREGATE_NAME}} Aggregate

**Root Entity:** `{{ROOT_ENTITY}}`

**Purpose:** {{AGGREGATE_PURPOSE}}

**Invariants:**
{{#INVARIANTS}}
- {{INVARIANT}}
{{/INVARIANTS}}

```{{CODE_LANG}}
{{AGGREGATE_CODE}}
```

**Entities:**
| Entity | Purpose | Identity |
|--------|---------|----------|
{{#ENTITIES}}
| `{{ENTITY}}` | {{PURPOSE}} | {{IDENTITY}} |
{{/ENTITIES}}

**Value Objects:**
| Value Object | Purpose | Immutable |
|--------------|---------|-----------|
{{#VALUE_OBJECTS}}
| `{{VO}}` | {{PURPOSE}} | {{IMMUTABLE}} |
{{/VALUE_OBJECTS}}

**Lifecycle:**
```
{{LIFECYCLE_DIAGRAM}}
```

{{/AGGREGATES}}

### Entities

{{#STANDALONE_ENTITIES}}
#### {{ENTITY_NAME}}

**Identity:** {{IDENTITY_FIELD}}

```{{CODE_LANG}}
{{ENTITY_CODE}}
```

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
{{#ATTRIBUTES}}
| `{{NAME}}` | `{{TYPE}}` | {{REQUIRED}} | {{DESCRIPTION}} |
{{/ATTRIBUTES}}

**Business Rules:**
{{#RULES}}
- {{RULE}}
{{/RULES}}

{{/STANDALONE_ENTITIES}}

### Value Objects

{{#VALUE_OBJECTS_DETAIL}}
#### {{VO_NAME}}

**Purpose:** {{VO_PURPOSE}}

```{{CODE_LANG}}
{{VO_CODE}}
```

**Validation:**
{{#VALIDATION}}
- {{RULE}}
{{/VALIDATION}}

**Equality:** Based on {{EQUALITY_FIELDS}}

{{/VALUE_OBJECTS_DETAIL}}

---

## Domain Events

### Events Published

{{#EVENTS_PUBLISHED}}
#### {{EVENT_NAME}}

**Trigger:** {{TRIGGER}}

**Payload:**
```{{CODE_LANG}}
{{EVENT_PAYLOAD}}
```

**Consumers:**
{{#CONSUMERS}}
- {{CONSUMER}} - {{PURPOSE}}
{{/CONSUMERS}}

**Idempotency Key:** `{{IDEMPOTENCY_KEY}}`

{{/EVENTS_PUBLISHED}}

### Events Consumed

{{#EVENTS_CONSUMED}}
#### {{EVENT_NAME}}

**Source:** {{SOURCE_DOMAIN}}

**Handler:** `{{HANDLER}}`

**Side Effects:**
{{#SIDE_EFFECTS}}
- {{EFFECT}}
{{/SIDE_EFFECTS}}

**Failure Handling:** {{FAILURE_HANDLING}}

{{/EVENTS_CONSUMED}}

### Event Flow

```
{{EVENT_FLOW_DIAGRAM}}
```

---

## Domain Services

{{#DOMAIN_SERVICES}}
### {{SERVICE_NAME}}

**Purpose:** {{SERVICE_PURPOSE}}

**Operations:**

{{#OPERATIONS}}
#### `{{OPERATION_NAME}}`

```{{CODE_LANG}}
{{OPERATION_SIGNATURE}}
```

**Pre-conditions:**
{{#PRECONDITIONS}}
- {{CONDITION}}
{{/PRECONDITIONS}}

**Post-conditions:**
{{#POSTCONDITIONS}}
- {{CONDITION}}
{{/POSTCONDITIONS}}

**Domain Events Raised:**
{{#EVENTS_RAISED}}
- `{{EVENT}}`
{{/EVENTS_RAISED}}

{{/OPERATIONS}}

{{/DOMAIN_SERVICES}}

---

## Repositories

{{#REPOSITORIES}}
### {{REPOSITORY_NAME}}

**Aggregate:** `{{AGGREGATE}}`

**Interface:**
```{{CODE_LANG}}
{{REPOSITORY_INTERFACE}}
```

**Query Methods:**
| Method | Purpose | Returns |
|--------|---------|---------|
{{#QUERY_METHODS}}
| `{{METHOD}}` | {{PURPOSE}} | `{{RETURNS}}` |
{{/QUERY_METHODS}}

**Performance Considerations:**
{{#PERF_CONSIDERATIONS}}
- {{CONSIDERATION}}
{{/PERF_CONSIDERATIONS}}

{{/REPOSITORIES}}

---

## Application Services

{{#APPLICATION_SERVICES}}
### {{APP_SERVICE_NAME}}

**Purpose:** {{SERVICE_PURPOSE}}

**Use Cases:**

{{#USE_CASES}}
#### {{USE_CASE_NAME}}

**Input:** `{{INPUT_TYPE}}`

**Output:** `{{OUTPUT_TYPE}}`

**Steps:**
1. {{STEP_1}}
2. {{STEP_2}}
3. {{STEP_3}}

**Authorization:** {{AUTHORIZATION}}

**Transaction Scope:** {{TRANSACTION_SCOPE}}

{{/USE_CASES}}

{{/APPLICATION_SERVICES}}

---

## Business Rules Engine

### Rules Catalog

| Rule ID | Name | Category | Enforcement |
|---------|------|----------|-------------|
{{#BUSINESS_RULES_CATALOG}}
| {{RULE_ID}} | {{NAME}} | {{CATEGORY}} | {{ENFORCEMENT}} |
{{/BUSINESS_RULES_CATALOG}}

### Rule Details

{{#RULE_DETAILS}}
#### {{RULE_ID}}: {{RULE_NAME}}

**Category:** {{CATEGORY}}

**Description:** {{DESCRIPTION}}

**When:**
```
{{RULE_CONDITION}}
```

**Then:**
```
{{RULE_ACTION}}
```

**Exceptions:**
{{#EXCEPTIONS}}
- {{EXCEPTION}}
{{/EXCEPTIONS}}

**Examples:**
| Scenario | Input | Expected Outcome |
|----------|-------|------------------|
{{#EXAMPLES}}
| {{SCENARIO}} | {{INPUT}} | {{OUTCOME}} |
{{/EXAMPLES}}

{{/RULE_DETAILS}}

---

## Anti-Corruption Layer

### External System Mappings

{{#ACL_MAPPINGS}}
#### {{EXTERNAL_SYSTEM}}

**Translation:**
| External Concept | Domain Concept | Transformation |
|------------------|----------------|----------------|
{{#TRANSLATIONS}}
| {{EXTERNAL}} | {{INTERNAL}} | {{TRANSFORMATION}} |
{{/TRANSLATIONS}}

**Adapter:** `{{ADAPTER_CLASS}}`

```{{CODE_LANG}}
{{ADAPTER_CODE}}
```

{{/ACL_MAPPINGS}}

---

## Query Model (CQRS)

### Read Models

{{#READ_MODELS}}
#### {{READ_MODEL_NAME}}

**Purpose:** {{PURPOSE}}

**Projection:**
```{{CODE_LANG}}
{{PROJECTION_CODE}}
```

**Updated By Events:**
{{#UPDATING_EVENTS}}
- `{{EVENT}}`
{{/UPDATING_EVENTS}}

**Queries Supported:**
{{#SUPPORTED_QUERIES}}
- {{QUERY}}
{{/SUPPORTED_QUERIES}}

{{/READ_MODELS}}

---

## Testing Strategy

### Unit Tests

| Component | Test Focus | Coverage Target |
|-----------|------------|-----------------|
{{#UNIT_TESTS}}
| {{COMPONENT}} | {{FOCUS}} | {{COVERAGE}} |
{{/UNIT_TESTS}}

### Domain Scenarios

{{#DOMAIN_SCENARIOS}}
#### Scenario: {{SCENARIO_NAME}}

**Given:**
{{#GIVEN}}
- {{CONDITION}}
{{/GIVEN}}

**When:**
{{WHEN}}

**Then:**
{{#THEN}}
- {{OUTCOME}}
{{/THEN}}

{{/DOMAIN_SCENARIOS}}

### Property-Based Tests

{{#PROPERTY_TESTS}}
- **{{PROPERTY}}:** {{DESCRIPTION}}
{{/PROPERTY_TESTS}}

---

## Evolution & Migration

### Version History

| Version | Date | Changes |
|---------|------|---------|
{{#VERSION_HISTORY}}
| {{VERSION}} | {{DATE}} | {{CHANGES}} |
{{/VERSION_HISTORY}}

### Planned Changes

{{#PLANNED_CHANGES}}
- **{{CHANGE}}** ({{TIMELINE}}) - {{DESCRIPTION}}
{{/PLANNED_CHANGES}}

### Deprecations

| Component | Deprecated | Replacement | Removal Date |
|-----------|------------|-------------|--------------|
{{#DEPRECATIONS}}
| {{COMPONENT}} | {{DEPRECATED_DATE}} | {{REPLACEMENT}} | {{REMOVAL_DATE}} |
{{/DEPRECATIONS}}

---

## References

### Domain Expert Resources

{{#EXPERT_RESOURCES}}
- [{{TITLE}}]({{URL}})
{{/EXPERT_RESOURCES}}

### Technical References

{{#TECH_REFERENCES}}
- [{{TITLE}}]({{URL}})
{{/TECH_REFERENCES}}

### Related Domains

{{#RELATED_DOMAINS}}
- [{{DOMAIN_NAME}}]({{DOMAIN_SPEC_URL}})
{{/RELATED_DOMAINS}}
