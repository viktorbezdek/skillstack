# Component Specification: {{COMPONENT_NAME}}

Technical specification for the {{COMPONENT_NAME}} component.

## Overview

| Attribute | Value |
|-----------|-------|
| **Name** | {{COMPONENT_NAME}} |
| **Type** | {{COMPONENT_TYPE}} |
| **Owner** | @{{OWNER}} |
| **Status** | {{STATUS}} |
| **Version** | {{VERSION}} |
| **Location** | `{{COMPONENT_PATH}}` |

### Purpose

{{COMPONENT_PURPOSE}}

### Non-Goals

{{#NON_GOALS}}
- {{NON_GOAL}}
{{/NON_GOALS}}

---

## Architecture

### Position in System

```
{{ARCHITECTURE_DIAGRAM}}
```

### Dependencies

#### Upstream (This component depends on)

| Component | Type | Criticality | Failure Impact |
|-----------|------|-------------|----------------|
{{#UPSTREAM_DEPS}}
| {{COMPONENT}} | {{TYPE}} | {{CRITICALITY}} | {{FAILURE_IMPACT}} |
{{/UPSTREAM_DEPS}}

#### Downstream (Components that depend on this)

| Component | Type | Coupling | Breaking Change Impact |
|-----------|------|----------|------------------------|
{{#DOWNSTREAM_DEPS}}
| {{COMPONENT}} | {{TYPE}} | {{COUPLING}} | {{BREAKING_IMPACT}} |
{{/DOWNSTREAM_DEPS}}

#### External Dependencies

| Dependency | Version | Purpose | Alternatives |
|------------|---------|---------|--------------|
{{#EXTERNAL_DEPS}}
| {{PACKAGE}} | {{VERSION}} | {{PURPOSE}} | {{ALTERNATIVES}} |
{{/EXTERNAL_DEPS}}

---

## Interface

### Public API

{{#PUBLIC_API}}
#### `{{API_NAME}}`

```{{CODE_LANG}}
{{API_SIGNATURE}}
```

**Purpose:** {{API_PURPOSE}}

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
{{#PARAMS}}
| `{{NAME}}` | `{{TYPE}}` | {{REQUIRED}} | {{DEFAULT}} | {{DESCRIPTION}} |
{{/PARAMS}}

**Returns:** `{{RETURN_TYPE}}`

{{RETURN_DESCRIPTION}}

**Throws:**

| Error | Condition | Recovery |
|-------|-----------|----------|
{{#THROWS}}
| `{{ERROR}}` | {{CONDITION}} | {{RECOVERY}} |
{{/THROWS}}

**Example:**

```{{CODE_LANG}}
{{API_EXAMPLE}}
```

{{/PUBLIC_API}}

### Events Emitted

| Event | Payload | When Emitted |
|-------|---------|--------------|
{{#EVENTS_EMITTED}}
| `{{EVENT_NAME}}` | `{{PAYLOAD_TYPE}}` | {{WHEN_EMITTED}} |
{{/EVENTS_EMITTED}}

### Events Consumed

| Event | Source | Handler |
|-------|--------|---------|
{{#EVENTS_CONSUMED}}
| `{{EVENT_NAME}}` | {{SOURCE}} | `{{HANDLER}}` |
{{/EVENTS_CONSUMED}}

---

## Data Model

### Internal State

```{{CODE_LANG}}
{{STATE_DEFINITION}}
```

### Data Flow

```
{{DATA_FLOW_DIAGRAM}}
```

### Persistence

| Data | Storage | TTL | Encryption |
|------|---------|-----|------------|
{{#PERSISTENCE}}
| {{DATA}} | {{STORAGE}} | {{TTL}} | {{ENCRYPTION}} |
{{/PERSISTENCE}}

---

## Behavior

### State Machine

```
{{STATE_MACHINE_DIAGRAM}}
```

| State | Entry Actions | Exit Actions | Valid Transitions |
|-------|---------------|--------------|-------------------|
{{#STATES}}
| {{STATE}} | {{ENTRY}} | {{EXIT}} | {{TRANSITIONS}} |
{{/STATES}}

### Lifecycle

1. **Initialization**
   {{INIT_DESCRIPTION}}

2. **Normal Operation**
   {{NORMAL_DESCRIPTION}}

3. **Shutdown**
   {{SHUTDOWN_DESCRIPTION}}

### Invariants

{{#INVARIANTS}}
- **{{INVARIANT_NAME}}:** {{INVARIANT_DESCRIPTION}}
{{/INVARIANTS}}

---

## Configuration

### Options

| Option | Type | Default | Description | Env Var |
|--------|------|---------|-------------|---------|
{{#CONFIG_OPTIONS}}
| `{{OPTION}}` | `{{TYPE}}` | `{{DEFAULT}}` | {{DESCRIPTION}} | `{{ENV_VAR}}` |
{{/CONFIG_OPTIONS}}

### Example Configuration

```{{CONFIG_FORMAT}}
{{CONFIG_EXAMPLE}}
```

### Feature Flags

| Flag | Default | Description |
|------|---------|-------------|
{{#FEATURE_FLAGS}}
| `{{FLAG}}` | {{DEFAULT}} | {{DESCRIPTION}} |
{{/FEATURE_FLAGS}}

---

## Error Handling

### Error Types

| Error Code | Name | Severity | Retryable | Description |
|------------|------|----------|-----------|-------------|
{{#ERROR_TYPES}}
| `{{CODE}}` | {{NAME}} | {{SEVERITY}} | {{RETRYABLE}} | {{DESCRIPTION}} |
{{/ERROR_TYPES}}

### Recovery Strategies

{{#RECOVERY_STRATEGIES}}
#### {{STRATEGY_NAME}}

**Trigger:** {{TRIGGER}}

**Action:** {{ACTION}}

**Fallback:** {{FALLBACK}}

{{/RECOVERY_STRATEGIES}}

### Circuit Breaker

| Dependency | Threshold | Timeout | Half-Open After |
|------------|-----------|---------|-----------------|
{{#CIRCUIT_BREAKERS}}
| {{DEPENDENCY}} | {{THRESHOLD}} | {{TIMEOUT}} | {{HALF_OPEN}} |
{{/CIRCUIT_BREAKERS}}

---

## Performance

### Characteristics

| Metric | Target | Current | Notes |
|--------|--------|---------|-------|
| Latency (p50) | {{P50_TARGET}} | {{P50_CURRENT}} | {{P50_NOTES}} |
| Latency (p99) | {{P99_TARGET}} | {{P99_CURRENT}} | {{P99_NOTES}} |
| Throughput | {{THROUGHPUT_TARGET}} | {{THROUGHPUT_CURRENT}} | {{THROUGHPUT_NOTES}} |
| Memory | {{MEMORY_TARGET}} | {{MEMORY_CURRENT}} | {{MEMORY_NOTES}} |
| CPU | {{CPU_TARGET}} | {{CPU_CURRENT}} | {{CPU_NOTES}} |

### Scaling

| Dimension | Strategy | Trigger | Limit |
|-----------|----------|---------|-------|
{{#SCALING}}
| {{DIMENSION}} | {{STRATEGY}} | {{TRIGGER}} | {{LIMIT}} |
{{/SCALING}}

### Caching

| Cache | TTL | Invalidation | Size Limit |
|-------|-----|--------------|------------|
{{#CACHES}}
| {{CACHE}} | {{TTL}} | {{INVALIDATION}} | {{SIZE_LIMIT}} |
{{/CACHES}}

---

## Observability

### Metrics

| Metric | Type | Labels | Description |
|--------|------|--------|-------------|
{{#METRICS}}
| `{{METRIC_NAME}}` | {{TYPE}} | {{LABELS}} | {{DESCRIPTION}} |
{{/METRICS}}

### Logs

| Log Level | When | Fields |
|-----------|------|--------|
{{#LOGS}}
| {{LEVEL}} | {{WHEN}} | {{FIELDS}} |
{{/LOGS}}

### Traces

| Span | Parent | Attributes |
|------|--------|------------|
{{#TRACES}}
| {{SPAN}} | {{PARENT}} | {{ATTRIBUTES}} |
{{/TRACES}}

### Alerts

| Alert | Condition | Severity | Runbook |
|-------|-----------|----------|---------|
{{#ALERTS}}
| {{ALERT}} | {{CONDITION}} | {{SEVERITY}} | [Link]({{RUNBOOK}}) |
{{/ALERTS}}

---

## Security

### Authentication

{{AUTH_DESCRIPTION}}

### Authorization

| Action | Required Permission | Check Location |
|--------|---------------------|----------------|
{{#AUTHZ}}
| {{ACTION}} | {{PERMISSION}} | {{CHECK_LOCATION}} |
{{/AUTHZ}}

### Data Sensitivity

| Data | Classification | Handling |
|------|----------------|----------|
{{#DATA_SENSITIVITY}}
| {{DATA}} | {{CLASSIFICATION}} | {{HANDLING}} |
{{/DATA_SENSITIVITY}}

### Security Considerations

{{#SECURITY_CONSIDERATIONS}}
- {{CONSIDERATION}}
{{/SECURITY_CONSIDERATIONS}}

---

## Testing

### Test Coverage

| Type | Coverage | Location |
|------|----------|----------|
| Unit | {{UNIT_COVERAGE}} | `{{UNIT_LOCATION}}` |
| Integration | {{INT_COVERAGE}} | `{{INT_LOCATION}}` |
| E2E | {{E2E_COVERAGE}} | `{{E2E_LOCATION}}` |

### Test Scenarios

{{#TEST_SCENARIOS}}
#### {{SCENARIO_NAME}}

**Given:** {{GIVEN}}

**When:** {{WHEN}}

**Then:** {{THEN}}

{{/TEST_SCENARIOS}}

### Mocking

| Dependency | Mock Strategy | Mock Location |
|------------|---------------|---------------|
{{#MOCKS}}
| {{DEPENDENCY}} | {{STRATEGY}} | `{{LOCATION}}` |
{{/MOCKS}}

---

## Deployment

### Rollout Strategy

{{ROLLOUT_STRATEGY}}

### Feature Toggles

| Toggle | Stage | Percentage |
|--------|-------|------------|
{{#TOGGLES}}
| {{TOGGLE}} | {{STAGE}} | {{PERCENTAGE}} |
{{/TOGGLES}}

### Rollback Procedure

{{ROLLBACK_PROCEDURE}}

---

## Maintenance

### Common Tasks

{{#MAINTENANCE_TASKS}}
#### {{TASK_NAME}}

**When:** {{WHEN}}

**Steps:**
{{#STEPS}}
1. {{STEP}}
{{/STEPS}}

{{/MAINTENANCE_TASKS}}

### Known Issues

| Issue | Workaround | Fix ETA |
|-------|------------|---------|
{{#KNOWN_ISSUES}}
| {{ISSUE}} | {{WORKAROUND}} | {{FIX_ETA}} |
{{/KNOWN_ISSUES}}

---

## Changelog

### {{LATEST_VERSION}} ({{LATEST_DATE}})

{{#LATEST_CHANGES}}
- {{CHANGE}}
{{/LATEST_CHANGES}}

### Previous Versions

{{#PREVIOUS_VERSIONS}}
#### {{VERSION}} ({{DATE}})
{{#CHANGES}}
- {{CHANGE}}
{{/CHANGES}}
{{/PREVIOUS_VERSIONS}}

---

## References

- [Design Doc]({{DESIGN_DOC_URL}})
- [API Documentation]({{API_DOCS_URL}})
- [Runbook]({{RUNBOOK_URL}})
- [Dashboard]({{DASHBOARD_URL}})
