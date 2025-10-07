# Integration: {{INTEGRATION_NAME}}

Technical specification for integration with {{EXTERNAL_SYSTEM}}.

## Overview

| Attribute | Value |
|-----------|-------|
| **Integration Name** | {{INTEGRATION_NAME}} |
| **External System** | {{EXTERNAL_SYSTEM}} |
| **Integration Type** | {{INTEGRATION_TYPE}} |
| **Owner** | @{{OWNER}} |
| **Status** | {{STATUS}} |
| **Version** | {{INTEGRATION_VERSION}} |

### Purpose

{{INTEGRATION_PURPOSE}}

### Business Value

{{#BUSINESS_VALUE}}
- {{VALUE}}
{{/BUSINESS_VALUE}}

---

## External System Information

### Vendor Details

| Attribute | Value |
|-----------|-------|
| **Vendor** | {{VENDOR_NAME}} |
| **Product** | {{PRODUCT_NAME}} |
| **Documentation** | [Link]({{VENDOR_DOCS_URL}}) |
| **Support Contact** | {{VENDOR_SUPPORT}} |
| **SLA** | {{VENDOR_SLA}} |

### API Information

| Attribute | Value |
|-----------|-------|
| **API Type** | {{API_TYPE}} |
| **Base URL (Prod)** | `{{PROD_API_URL}}` |
| **Base URL (Sandbox)** | `{{SANDBOX_API_URL}}` |
| **API Version** | {{API_VERSION}} |
| **Rate Limits** | {{RATE_LIMITS}} |

### Authentication

**Method:** {{AUTH_METHOD}}

```{{CODE_LANG}}
{{AUTH_EXAMPLE}}
```

**Credentials Location:** {{CREDENTIALS_LOCATION}}

**Token Refresh:** {{TOKEN_REFRESH_MECHANISM}}

---

## Integration Architecture

### Data Flow

```
{{DATA_FLOW_DIAGRAM}}
```

### Components Involved

| Component | Role | Location |
|-----------|------|----------|
{{#COMPONENTS}}
| {{COMPONENT}} | {{ROLE}} | `{{LOCATION}}` |
{{/COMPONENTS}}

### Sequence Diagram

```
{{SEQUENCE_DIAGRAM}}
```

---

## API Endpoints Used

### Outbound Calls (We Call Them)

{{#OUTBOUND_ENDPOINTS}}
#### `{{METHOD}} {{ENDPOINT}}`

**Purpose:** {{PURPOSE}}

**Request:**
```{{CODE_LANG}}
{{REQUEST_EXAMPLE}}
```

**Response:**
```{{CODE_LANG}}
{{RESPONSE_EXAMPLE}}
```

**Error Codes:**

| Code | Meaning | Our Handling |
|------|---------|--------------|
{{#ERRORS}}
| `{{CODE}}` | {{MEANING}} | {{HANDLING}} |
{{/ERRORS}}

**Rate Limit:** {{RATE_LIMIT}}

{{/OUTBOUND_ENDPOINTS}}

### Inbound Webhooks (They Call Us)

{{#INBOUND_WEBHOOKS}}
#### `{{WEBHOOK_EVENT}}`

**Our Endpoint:** `{{OUR_ENDPOINT}}`

**Payload:**
```{{CODE_LANG}}
{{PAYLOAD_EXAMPLE}}
```

**Verification:**
```{{CODE_LANG}}
{{VERIFICATION_CODE}}
```

**Processing:**
{{PROCESSING_DESCRIPTION}}

{{/INBOUND_WEBHOOKS}}

---

## Data Mapping

### Outbound Mapping (Our Data → Their Format)

| Our Field | Their Field | Transformation | Notes |
|-----------|-------------|----------------|-------|
{{#OUTBOUND_MAPPING}}
| `{{OUR_FIELD}}` | `{{THEIR_FIELD}}` | {{TRANSFORMATION}} | {{NOTES}} |
{{/OUTBOUND_MAPPING}}

### Inbound Mapping (Their Data → Our Format)

| Their Field | Our Field | Transformation | Notes |
|-------------|-----------|----------------|-------|
{{#INBOUND_MAPPING}}
| `{{THEIR_FIELD}}` | `{{OUR_FIELD}}` | {{TRANSFORMATION}} | {{NOTES}} |
{{/INBOUND_MAPPING}}

### Data Type Conversions

| Concept | Their Format | Our Format | Conversion |
|---------|--------------|------------|------------|
{{#TYPE_CONVERSIONS}}
| {{CONCEPT}} | {{THEIR_FORMAT}} | {{OUR_FORMAT}} | {{CONVERSION}} |
{{/TYPE_CONVERSIONS}}

---

## Sync Strategy

### Sync Type

{{SYNC_TYPE_DESCRIPTION}}

### Sync Schedule

| Sync | Direction | Frequency | Trigger |
|------|-----------|-----------|---------|
{{#SYNC_SCHEDULE}}
| {{SYNC_NAME}} | {{DIRECTION}} | {{FREQUENCY}} | {{TRIGGER}} |
{{/SYNC_SCHEDULE}}

### Conflict Resolution

| Scenario | Resolution | Rationale |
|----------|------------|-----------|
{{#CONFLICT_RESOLUTION}}
| {{SCENARIO}} | {{RESOLUTION}} | {{RATIONALE}} |
{{/CONFLICT_RESOLUTION}}

### Idempotency

{{IDEMPOTENCY_STRATEGY}}

---

## Error Handling

### Error Categories

| Category | Examples | Retry | Alert |
|----------|----------|-------|-------|
| Transient | Network timeout, 503 | Yes ({{TRANSIENT_RETRY}}) | After {{TRANSIENT_ALERT}} |
| Rate Limit | 429 | Yes (backoff) | After {{RATE_ALERT}} |
| Auth | 401, 403 | No | Immediate |
| Validation | 400, 422 | No | Logged |
| Server | 500 | Yes ({{SERVER_RETRY}}) | After {{SERVER_ALERT}} |

### Retry Strategy

```{{CODE_LANG}}
{{RETRY_CONFIG}}
```

### Circuit Breaker

| Setting | Value |
|---------|-------|
| Failure Threshold | {{CB_THRESHOLD}} |
| Timeout | {{CB_TIMEOUT}} |
| Half-Open After | {{CB_HALF_OPEN}} |

### Fallback Behavior

{{FALLBACK_DESCRIPTION}}

### Dead Letter Queue

| Queue | Purpose | Retention |
|-------|---------|-----------|
| {{DLQ_NAME}} | {{DLQ_PURPOSE}} | {{DLQ_RETENTION}} |

---

## Security

### Credentials Management

| Credential | Storage | Rotation |
|------------|---------|----------|
{{#CREDENTIALS}}
| {{CREDENTIAL}} | {{STORAGE}} | {{ROTATION}} |
{{/CREDENTIALS}}

### Data in Transit

| Direction | Encryption | Certificate |
|-----------|------------|-------------|
| Outbound | {{OUTBOUND_ENCRYPTION}} | {{OUTBOUND_CERT}} |
| Inbound | {{INBOUND_ENCRYPTION}} | {{INBOUND_CERT}} |

### IP Allowlisting

**Their IPs (for our allowlist):**
{{#THEIR_IPS}}
- `{{IP}}`
{{/THEIR_IPS}}

**Our IPs (for their allowlist):**
{{#OUR_IPS}}
- `{{IP}}`
{{/OUR_IPS}}

### Audit Logging

| Event | Logged Fields | Retention |
|-------|---------------|-----------|
{{#AUDIT_EVENTS}}
| {{EVENT}} | {{FIELDS}} | {{RETENTION}} |
{{/AUDIT_EVENTS}}

---

## Testing

### Sandbox Environment

| Attribute | Value |
|-----------|-------|
| **URL** | `{{SANDBOX_URL}}` |
| **Credentials** | {{SANDBOX_CREDS_LOCATION}} |
| **Limitations** | {{SANDBOX_LIMITATIONS}} |

### Test Scenarios

{{#TEST_SCENARIOS}}
#### {{SCENARIO_NAME}}

**Setup:**
{{SETUP}}

**Steps:**
{{#STEPS}}
1. {{STEP}}
{{/STEPS}}

**Expected Result:**
{{EXPECTED}}

{{/TEST_SCENARIOS}}

### Mock Server

```{{CODE_LANG}}
{{MOCK_SERVER_CONFIG}}
```

---

## Monitoring

### Health Checks

| Check | Endpoint | Frequency | Timeout |
|-------|----------|-----------|---------|
{{#HEALTH_CHECKS}}
| {{CHECK}} | `{{ENDPOINT}}` | {{FREQUENCY}} | {{TIMEOUT}} |
{{/HEALTH_CHECKS}}

### Metrics

| Metric | Type | Labels | Alert Threshold |
|--------|------|--------|-----------------|
{{#METRICS}}
| `{{METRIC}}` | {{TYPE}} | {{LABELS}} | {{THRESHOLD}} |
{{/METRICS}}

### Alerts

| Alert | Condition | Severity | Runbook |
|-------|-----------|----------|---------|
{{#ALERTS}}
| {{ALERT}} | {{CONDITION}} | {{SEVERITY}} | [Link]({{RUNBOOK}}) |
{{/ALERTS}}

### Dashboard

[Integration Dashboard]({{DASHBOARD_URL}})

---

## Operations

### Runbook

#### Integration Health Check

1. {{HEALTH_CHECK_STEP_1}}
2. {{HEALTH_CHECK_STEP_2}}
3. {{HEALTH_CHECK_STEP_3}}

#### Common Issues

{{#COMMON_ISSUES}}
##### {{ISSUE_NAME}}

**Symptoms:** {{SYMPTOMS}}

**Diagnosis:**
```bash
{{DIAGNOSIS_COMMANDS}}
```

**Resolution:**
{{RESOLUTION}}

{{/COMMON_ISSUES}}

### Maintenance Windows

| System | Window | Notification |
|--------|--------|--------------|
| {{EXTERNAL_SYSTEM}} | {{THEIR_WINDOW}} | {{THEIR_NOTIFICATION}} |
| Our System | {{OUR_WINDOW}} | {{OUR_NOTIFICATION}} |

---

## Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
{{#ENV_VARS}}
| `{{VAR}}` | {{DESCRIPTION}} | {{REQUIRED}} | {{DEFAULT}} |
{{/ENV_VARS}}

### Feature Flags

| Flag | Description | Default |
|------|-------------|---------|
{{#FLAGS}}
| `{{FLAG}}` | {{DESCRIPTION}} | {{DEFAULT}} |
{{/FLAGS}}

---

## Compliance

### Data Handling

| Data Type | Classification | Retention | Deletion |
|-----------|----------------|-----------|----------|
{{#DATA_HANDLING}}
| {{DATA_TYPE}} | {{CLASSIFICATION}} | {{RETENTION}} | {{DELETION}} |
{{/DATA_HANDLING}}

### Regulatory Requirements

{{#REGULATORY}}
- **{{REGULATION}}:** {{REQUIREMENT}}
{{/REGULATORY}}

---

## References

- [Vendor API Documentation]({{VENDOR_DOCS}})
- [Internal Design Doc]({{DESIGN_DOC}})
- [Runbook]({{RUNBOOK}})
- [Dashboard]({{DASHBOARD}})
- [Support Channel]({{SUPPORT_CHANNEL}})
