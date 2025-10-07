# Runbook: {{SERVICE_NAME}}

Operational runbook for {{SERVICE_NAME}}.

## Service Overview

| Attribute | Value |
|-----------|-------|
| **Service** | {{SERVICE_NAME}} |
| **Owner** | @{{OWNER}} |
| **On-Call** | {{ON_CALL_ROTATION}} |
| **Criticality** | {{CRITICALITY}} |
| **SLA** | {{SLA}} |

### Quick Links

| Resource | Link |
|----------|------|
| Dashboard | [{{DASHBOARD_NAME}}]({{DASHBOARD_URL}}) |
| Logs | [{{LOGS_NAME}}]({{LOGS_URL}}) |
| Alerts | [{{ALERTS_NAME}}]({{ALERTS_URL}}) |
| Source Code | [{{REPO_NAME}}]({{REPO_URL}}) |
| Documentation | [{{DOCS_NAME}}]({{DOCS_URL}}) |

---

## Service Architecture

```
{{ARCHITECTURE_DIAGRAM}}
```

### Dependencies

| Dependency | Type | Criticality | Health Check |
|------------|------|-------------|--------------|
{{#DEPENDENCIES}}
| {{NAME}} | {{TYPE}} | {{CRITICALITY}} | [Check]({{HEALTH_URL}}) |
{{/DEPENDENCIES}}

### Endpoints

| Endpoint | Purpose | Expected Latency |
|----------|---------|------------------|
{{#ENDPOINTS}}
| `{{ENDPOINT}}` | {{PURPOSE}} | {{LATENCY}} |
{{/ENDPOINTS}}

---

## Health Verification

### Health Check Commands

```bash
# Basic health check
{{HEALTH_CHECK_CMD}}

# Detailed health check
{{DETAILED_HEALTH_CMD}}

# Check all dependencies
{{DEPS_CHECK_CMD}}
```

### Expected Healthy State

```
{{HEALTHY_OUTPUT}}
```

### Health Check Interpretation

| Status | Meaning | Action |
|--------|---------|--------|
| `healthy` | All systems operational | None |
| `degraded` | Partial functionality | Monitor, investigate |
| `unhealthy` | Service impaired | Immediate action |

---

## Common Issues

{{#COMMON_ISSUES}}
### {{ISSUE_TITLE}}

**Severity:** {{SEVERITY}}

**Symptoms:**
{{#SYMPTOMS}}
- {{SYMPTOM}}
{{/SYMPTOMS}}

**Likely Causes:**
{{#CAUSES}}
1. {{CAUSE}}
{{/CAUSES}}

**Diagnosis:**

```bash
{{DIAGNOSIS_COMMANDS}}
```

**Resolution:**

{{#RESOLUTION_STEPS}}
{{STEP_NUM}}. {{STEP}}
   ```bash
   {{STEP_COMMAND}}
   ```
{{/RESOLUTION_STEPS}}

**Verification:**

```bash
{{VERIFICATION_CMD}}
```

**Prevention:**
{{PREVENTION}}

---

{{/COMMON_ISSUES}}

## Alert Responses

{{#ALERTS}}
### Alert: {{ALERT_NAME}}

**Severity:** {{SEVERITY}}

**Description:** {{DESCRIPTION}}

**Threshold:** {{THRESHOLD}}

**Immediate Actions:**
{{#IMMEDIATE_ACTIONS}}
1. {{ACTION}}
{{/IMMEDIATE_ACTIONS}}

**Investigation:**

```bash
{{INVESTIGATION_COMMANDS}}
```

**Resolution:**
{{RESOLUTION}}

**Escalation:** {{ESCALATION_PATH}}

---

{{/ALERTS}}

## Deployment

### Deployment Commands

```bash
# Deploy new version
{{DEPLOY_CMD}}

# Check deployment status
{{DEPLOY_STATUS_CMD}}

# View deployment logs
{{DEPLOY_LOGS_CMD}}
```

### Pre-Deployment Checklist

- [ ] All tests passing
- [ ] Database migrations ready
- [ ] Feature flags configured
- [ ] Rollback plan verified
- [ ] Stakeholders notified

### Post-Deployment Verification

```bash
{{POST_DEPLOY_VERIFICATION}}
```

### Rollback

```bash
# Initiate rollback
{{ROLLBACK_CMD}}

# Verify rollback
{{ROLLBACK_VERIFY_CMD}}
```

**Rollback Criteria:**
{{#ROLLBACK_CRITERIA}}
- {{CRITERION}}
{{/ROLLBACK_CRITERIA}}

---

## Scaling

### Current Configuration

| Metric | Min | Current | Max |
|--------|-----|---------|-----|
{{#SCALING_CONFIG}}
| {{METRIC}} | {{MIN}} | {{CURRENT}} | {{MAX}} |
{{/SCALING_CONFIG}}

### Manual Scaling

```bash
# Scale up
{{SCALE_UP_CMD}}

# Scale down
{{SCALE_DOWN_CMD}}

# Check current scale
{{SCALE_STATUS_CMD}}
```

### Auto-Scaling Triggers

| Trigger | Threshold | Action | Cooldown |
|---------|-----------|--------|----------|
{{#AUTOSCALE_TRIGGERS}}
| {{TRIGGER}} | {{THRESHOLD}} | {{ACTION}} | {{COOLDOWN}} |
{{/AUTOSCALE_TRIGGERS}}

---

## Database Operations

### Connection Information

```bash
# Connect to database
{{DB_CONNECT_CMD}}

# Check connection count
{{DB_CONNECTIONS_CMD}}
```

### Common Queries

```sql
-- Check table sizes
{{TABLE_SIZE_QUERY}}

-- Check slow queries
{{SLOW_QUERY_CHECK}}

-- Check replication lag
{{REPLICATION_LAG_QUERY}}
```

### Emergency Procedures

#### Kill Long-Running Query

```sql
{{KILL_QUERY_CMD}}
```

#### Force Failover

```bash
{{FAILOVER_CMD}}
```

---

## Log Analysis

### Log Locations

| Log Type | Location | Retention |
|----------|----------|-----------|
{{#LOG_LOCATIONS}}
| {{TYPE}} | {{LOCATION}} | {{RETENTION}} |
{{/LOG_LOCATIONS}}

### Useful Log Queries

```bash
# Recent errors
{{ERROR_LOG_QUERY}}

# Request latency
{{LATENCY_LOG_QUERY}}

# Specific user activity
{{USER_LOG_QUERY}}

# Failed authentications
{{AUTH_FAIL_QUERY}}
```

### Log Format

```
{{LOG_FORMAT_EXAMPLE}}
```

---

## Secrets & Configuration

### Secret Locations

| Secret | Location | Rotation |
|--------|----------|----------|
{{#SECRETS}}
| {{SECRET}} | {{LOCATION}} | {{ROTATION}} |
{{/SECRETS}}

### Rotate Secrets

```bash
# Rotate API key
{{ROTATE_API_KEY_CMD}}

# Rotate database password
{{ROTATE_DB_PASS_CMD}}
```

### Configuration Reload

```bash
# Reload configuration without restart
{{CONFIG_RELOAD_CMD}}
```

---

## Maintenance Procedures

### Scheduled Maintenance

{{#MAINTENANCE_PROCEDURES}}
#### {{PROCEDURE_NAME}}

**Frequency:** {{FREQUENCY}}

**Duration:** {{DURATION}}

**Impact:** {{IMPACT}}

**Steps:**
{{#STEPS}}
1. {{STEP}}
{{/STEPS}}

**Verification:**
{{VERIFICATION}}

---

{{/MAINTENANCE_PROCEDURES}}

### Data Cleanup

```bash
# Cleanup old data
{{CLEANUP_CMD}}

# Verify cleanup
{{CLEANUP_VERIFY_CMD}}
```

---

## Disaster Recovery

### Backup Information

| Data | Backup Frequency | Retention | Location |
|------|------------------|-----------|----------|
{{#BACKUPS}}
| {{DATA}} | {{FREQUENCY}} | {{RETENTION}} | {{LOCATION}} |
{{/BACKUPS}}

### Restore Procedure

```bash
# List available backups
{{LIST_BACKUPS_CMD}}

# Restore from backup
{{RESTORE_CMD}}

# Verify restore
{{RESTORE_VERIFY_CMD}}
```

### Recovery Time Objectives

| Scenario | RTO | RPO |
|----------|-----|-----|
{{#RTO_RPO}}
| {{SCENARIO}} | {{RTO}} | {{RPO}} |
{{/RTO_RPO}}

---

## Escalation

### Escalation Matrix

| Severity | Initial Contact | Escalate After | Final Escalation |
|----------|-----------------|----------------|------------------|
| P1 | {{P1_INITIAL}} | {{P1_AFTER}} | {{P1_FINAL}} |
| P2 | {{P2_INITIAL}} | {{P2_AFTER}} | {{P2_FINAL}} |
| P3 | {{P3_INITIAL}} | {{P3_AFTER}} | {{P3_FINAL}} |

### Contact Information

| Role | Name | Contact |
|------|------|---------|
{{#CONTACTS}}
| {{ROLE}} | {{NAME}} | {{CONTACT}} |
{{/CONTACTS}}

---

## Appendix

### Useful Commands Cheatsheet

```bash
{{CHEATSHEET}}
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
{{#ENV_VARS}}
| `{{VAR}}` | {{DESCRIPTION}} | {{DEFAULT}} |
{{/ENV_VARS}}

### Related Documentation

{{#RELATED_DOCS}}
- [{{TITLE}}]({{URL}})
{{/RELATED_DOCS}}
