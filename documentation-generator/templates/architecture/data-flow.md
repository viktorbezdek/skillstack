# Data Flow Documentation

Complete data flow specification for {{PROJECT_NAME}}.

## Overview

This document describes how data moves through {{PROJECT_NAME}}, including entry points, transformations, storage, and outputs.

---

## Data Flow Diagram

### High-Level Flow

```
{{HIGH_LEVEL_FLOW_DIAGRAM}}
```

### Detailed Flow

```
{{DETAILED_FLOW_DIAGRAM}}
```

---

## Data Entry Points

{{#ENTRY_POINTS}}
### {{ENTRY_POINT_NAME}}

| Attribute | Value |
|-----------|-------|
| **Type** | {{TYPE}} |
| **Protocol** | {{PROTOCOL}} |
| **Authentication** | {{AUTH}} |
| **Rate Limit** | {{RATE_LIMIT}} |

**Data Format:**
```{{FORMAT}}
{{DATA_SCHEMA}}
```

**Validation:**
{{#VALIDATIONS}}
- {{VALIDATION}}
{{/VALIDATIONS}}

**Processing Pipeline:**
```
{{ENTRY_POINT_NAME}} → {{PIPELINE_STEP_1}} → {{PIPELINE_STEP_2}} → {{DESTINATION}}
```

{{/ENTRY_POINTS}}

---

## Data Transformations

{{#TRANSFORMATIONS}}
### {{TRANSFORMATION_NAME}}

| Attribute | Value |
|-----------|-------|
| **Input** | {{INPUT_TYPE}} |
| **Output** | {{OUTPUT_TYPE}} |
| **Trigger** | {{TRIGGER}} |
| **Location** | `{{CODE_LOCATION}}` |

**Transformation Logic:**

```{{CODE_LANG}}
{{TRANSFORMATION_CODE}}
```

**Input Schema:**
```{{FORMAT}}
{{INPUT_SCHEMA}}
```

**Output Schema:**
```{{FORMAT}}
{{OUTPUT_SCHEMA}}
```

**Field Mappings:**

| Input Field | Output Field | Transformation |
|-------------|--------------|----------------|
{{#FIELD_MAPPINGS}}
| `{{INPUT}}` | `{{OUTPUT}}` | {{TRANSFORM}} |
{{/FIELD_MAPPINGS}}

**Error Handling:**
{{ERROR_HANDLING}}

{{/TRANSFORMATIONS}}

---

## Data Stores

{{#DATA_STORES}}
### {{STORE_NAME}}

| Attribute | Value |
|-----------|-------|
| **Type** | {{STORE_TYPE}} |
| **Technology** | {{TECHNOLOGY}} |
| **Purpose** | {{PURPOSE}} |
| **Retention** | {{RETENTION}} |
| **Encryption** | {{ENCRYPTION}} |

**Schema:**
```{{SCHEMA_FORMAT}}
{{SCHEMA}}
```

**Indexes:**
| Index | Fields | Purpose |
|-------|--------|---------|
{{#INDEXES}}
| {{INDEX_NAME}} | {{FIELDS}} | {{PURPOSE}} |
{{/INDEXES}}

**Access Patterns:**
| Pattern | Query | Frequency |
|---------|-------|-----------|
{{#ACCESS_PATTERNS}}
| {{PATTERN}} | {{QUERY}} | {{FREQUENCY}} |
{{/ACCESS_PATTERNS}}

**Data Lifecycle:**
```
Created → {{LIFECYCLE_STAGES}} → Archived/Deleted
```

{{/DATA_STORES}}

---

## Data Flows

{{#DATA_FLOWS}}
### Flow: {{FLOW_NAME}}

**Description:** {{FLOW_DESCRIPTION}}

**Trigger:** {{TRIGGER}}

**Sequence:**

```
{{SEQUENCE_DIAGRAM}}
```

**Steps:**

| Step | Component | Action | Data |
|------|-----------|--------|------|
{{#FLOW_STEPS}}
| {{STEP_NUM}} | {{COMPONENT}} | {{ACTION}} | {{DATA}} |
{{/FLOW_STEPS}}

**Data Mutations:**

| Step | Before | After |
|------|--------|-------|
{{#MUTATIONS}}
| {{STEP}} | {{BEFORE}} | {{AFTER}} |
{{/MUTATIONS}}

**Error Scenarios:**
| Error | Handling | Data State |
|-------|----------|------------|
{{#ERROR_SCENARIOS}}
| {{ERROR}} | {{HANDLING}} | {{STATE}} |
{{/ERROR_SCENARIOS}}

{{/DATA_FLOWS}}

---

## Event Streams

{{#EVENT_STREAMS}}
### {{STREAM_NAME}}

| Attribute | Value |
|-----------|-------|
| **Platform** | {{PLATFORM}} |
| **Topic/Queue** | {{TOPIC}} |
| **Partitioning** | {{PARTITIONING}} |
| **Retention** | {{RETENTION}} |

**Event Types:**

| Event | Schema | Producers | Consumers |
|-------|--------|-----------|-----------|
{{#EVENT_TYPES}}
| `{{EVENT}}` | [Schema](#{{SCHEMA_ANCHOR}}) | {{PRODUCERS}} | {{CONSUMERS}} |
{{/EVENT_TYPES}}

**Ordering Guarantees:** {{ORDERING}}

**Delivery Guarantees:** {{DELIVERY}}

{{/EVENT_STREAMS}}

---

## Data Synchronization

### Sync Patterns

{{#SYNC_PATTERNS}}
#### {{PATTERN_NAME}}

**Systems:** {{SYSTEM_A}} ↔ {{SYSTEM_B}}

**Direction:** {{DIRECTION}}

**Frequency:** {{FREQUENCY}}

**Mechanism:** {{MECHANISM}}

**Conflict Resolution:** {{CONFLICT_RESOLUTION}}

**Sync Flow:**
```
{{SYNC_FLOW_DIAGRAM}}
```

{{/SYNC_PATTERNS}}

### Data Consistency

| Data Type | Consistency Model | Recovery |
|-----------|-------------------|----------|
{{#CONSISTENCY}}
| {{DATA_TYPE}} | {{MODEL}} | {{RECOVERY}} |
{{/CONSISTENCY}}

---

## Caching

{{#CACHES}}
### {{CACHE_NAME}}

| Attribute | Value |
|-----------|-------|
| **Technology** | {{TECHNOLOGY}} |
| **Purpose** | {{PURPOSE}} |
| **TTL** | {{TTL}} |
| **Size Limit** | {{SIZE_LIMIT}} |

**Cached Data:**
| Key Pattern | Value Type | Invalidation |
|-------------|------------|--------------|
{{#CACHED_DATA}}
| `{{KEY_PATTERN}}` | {{VALUE_TYPE}} | {{INVALIDATION}} |
{{/CACHED_DATA}}

**Cache Strategy:** {{STRATEGY}}

**Cache Miss Flow:**
```
{{CACHE_MISS_FLOW}}
```

{{/CACHES}}

---

## Data Outputs

{{#OUTPUTS}}
### {{OUTPUT_NAME}}

| Attribute | Value |
|-----------|-------|
| **Type** | {{OUTPUT_TYPE}} |
| **Destination** | {{DESTINATION}} |
| **Format** | {{FORMAT}} |
| **Frequency** | {{FREQUENCY}} |

**Output Schema:**
```{{SCHEMA_FORMAT}}
{{OUTPUT_SCHEMA}}
```

**Consumers:**
{{#CONSUMERS}}
- {{CONSUMER}} - {{USAGE}}
{{/CONSUMERS}}

{{/OUTPUTS}}

---

## Data Lineage

### Lineage Map

```
{{LINEAGE_DIAGRAM}}
```

### Field-Level Lineage

| Output Field | Source(s) | Transformations |
|--------------|-----------|-----------------|
{{#FIELD_LINEAGE}}
| `{{OUTPUT_FIELD}}` | {{SOURCES}} | {{TRANSFORMATIONS}} |
{{/FIELD_LINEAGE}}

---

## Data Quality

### Quality Checks

| Check | Data | Rule | Frequency |
|-------|------|------|-----------|
{{#QUALITY_CHECKS}}
| {{CHECK}} | {{DATA}} | {{RULE}} | {{FREQUENCY}} |
{{/QUALITY_CHECKS}}

### Quality Metrics

| Metric | Target | Current | Alert Threshold |
|--------|--------|---------|-----------------|
{{#QUALITY_METRICS}}
| {{METRIC}} | {{TARGET}} | {{CURRENT}} | {{THRESHOLD}} |
{{/QUALITY_METRICS}}

---

## Security & Compliance

### Data Classification

| Data Type | Classification | Handling Requirements |
|-----------|----------------|----------------------|
{{#DATA_CLASSIFICATION}}
| {{DATA_TYPE}} | {{CLASSIFICATION}} | {{REQUIREMENTS}} |
{{/DATA_CLASSIFICATION}}

### Encryption

| Location | At Rest | In Transit |
|----------|---------|------------|
{{#ENCRYPTION}}
| {{LOCATION}} | {{AT_REST}} | {{IN_TRANSIT}} |
{{/ENCRYPTION}}

### Access Controls

| Data | Read Access | Write Access | Admin Access |
|------|-------------|--------------|--------------|
{{#ACCESS_CONTROLS}}
| {{DATA}} | {{READ}} | {{WRITE}} | {{ADMIN}} |
{{/ACCESS_CONTROLS}}

### Audit Trail

| Event | Logged Fields | Retention |
|-------|---------------|-----------|
{{#AUDIT_EVENTS}}
| {{EVENT}} | {{FIELDS}} | {{RETENTION}} |
{{/AUDIT_EVENTS}}

---

## Disaster Recovery

### Backup Strategy

| Data Store | Backup Type | Frequency | Retention |
|------------|-------------|-----------|-----------|
{{#BACKUP_STRATEGY}}
| {{STORE}} | {{TYPE}} | {{FREQUENCY}} | {{RETENTION}} |
{{/BACKUP_STRATEGY}}

### Recovery Procedures

| Scenario | RTO | RPO | Procedure |
|----------|-----|-----|-----------|
{{#RECOVERY}}
| {{SCENARIO}} | {{RTO}} | {{RPO}} | [Link]({{PROCEDURE_URL}}) |
{{/RECOVERY}}

---

## Monitoring

### Data Flow Metrics

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
{{#FLOW_METRICS}}
| `{{METRIC}}` | {{DESCRIPTION}} | {{THRESHOLD}} |
{{/FLOW_METRICS}}

### Dashboards

| Dashboard | Purpose | Link |
|-----------|---------|------|
{{#DASHBOARDS}}
| {{NAME}} | {{PURPOSE}} | [View]({{URL}}) |
{{/DASHBOARDS}}
