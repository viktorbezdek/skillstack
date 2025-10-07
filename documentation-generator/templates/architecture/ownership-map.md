# Ownership Map

Defines ownership, responsibilities, and escalation paths for all components of {{PROJECT_NAME}}.

## Overview

This document establishes clear ownership for every part of the codebase to ensure:
- Fast incident response
- Clear decision-making authority
- Accountability for code quality
- Efficient code review routing

---

## Team Structure

### Teams

{{#TEAMS}}
#### {{TEAM_NAME}}

| Role | Person | Contact |
|------|--------|---------|
{{#TEAM_MEMBERS}}
| {{ROLE}} | {{NAME}} | {{CONTACT}} |
{{/TEAM_MEMBERS}}

**Responsibilities:**
{{#TEAM_RESPONSIBILITIES}}
- {{RESPONSIBILITY}}
{{/TEAM_RESPONSIBILITIES}}

**On-call rotation:** {{ON_CALL_SCHEDULE}}

{{/TEAMS}}

---

## Code Ownership

### CODEOWNERS File

```
# {{PROJECT_NAME}} Code Owners
# This file defines who reviews PRs for each area

{{CODEOWNERS_CONTENT}}
```

### Ownership by Directory

| Path | Primary Owner | Secondary Owner | Team |
|------|---------------|-----------------|------|
{{#DIRECTORY_OWNERS}}
| `{{PATH}}` | @{{PRIMARY}} | @{{SECONDARY}} | {{TEAM}} |
{{/DIRECTORY_OWNERS}}

### Ownership by Component

{{#COMPONENTS}}
#### {{COMPONENT_NAME}}

| Attribute | Value |
|-----------|-------|
| **Path** | `{{COMPONENT_PATH}}` |
| **Primary Owner** | @{{PRIMARY_OWNER}} |
| **Secondary Owner** | @{{SECONDARY_OWNER}} |
| **Team** | {{TEAM}} |
| **Review Required** | {{REVIEW_REQUIRED}} |
| **SLA** | {{REVIEW_SLA}} |

**Responsibilities:**
- {{OWNER_RESPONSIBILITY_1}}
- {{OWNER_RESPONSIBILITY_2}}

**Decision Authority:**
- {{DECISION_AUTHORITY}}

{{/COMPONENTS}}

---

## Service Ownership

### Internal Services

| Service | Owner | Team | Runbook |
|---------|-------|------|---------|
{{#INTERNAL_SERVICES}}
| {{SERVICE_NAME}} | @{{OWNER}} | {{TEAM}} | [Runbook]({{RUNBOOK_URL}}) |
{{/INTERNAL_SERVICES}}

### External Dependencies

| Dependency | Internal Owner | Vendor Contact | Escalation |
|------------|----------------|----------------|------------|
{{#EXTERNAL_DEPS}}
| {{DEP_NAME}} | @{{INTERNAL_OWNER}} | {{VENDOR_CONTACT}} | {{ESCALATION_PATH}} |
{{/EXTERNAL_DEPS}}

---

## Database Ownership

| Database/Schema | Owner | Team | Access Level |
|-----------------|-------|------|--------------|
{{#DATABASES}}
| {{DB_NAME}} | @{{OWNER}} | {{TEAM}} | {{ACCESS_NOTES}} |
{{/DATABASES}}

### Migration Ownership

| Migration Path | Reviewer Required | Approval Required |
|----------------|-------------------|-------------------|
{{#MIGRATION_PATHS}}
| `{{PATH}}` | @{{REVIEWER}} | {{APPROVAL}} |
{{/MIGRATION_PATHS}}

---

## Infrastructure Ownership

### Cloud Resources

| Resource | Owner | Team | Environment |
|----------|-------|------|-------------|
{{#CLOUD_RESOURCES}}
| {{RESOURCE}} | @{{OWNER}} | {{TEAM}} | {{ENV}} |
{{/CLOUD_RESOURCES}}

### CI/CD Pipelines

| Pipeline | Owner | Approval Required |
|----------|-------|-------------------|
{{#PIPELINES}}
| {{PIPELINE}} | @{{OWNER}} | {{APPROVAL}} |
{{/PIPELINES}}

---

## Domain Ownership

### Business Domains

{{#DOMAINS}}
#### {{DOMAIN_NAME}}

| Attribute | Value |
|-----------|-------|
| **Domain Expert** | @{{DOMAIN_EXPERT}} |
| **Technical Owner** | @{{TECH_OWNER}} |
| **Product Owner** | @{{PRODUCT_OWNER}} |

**Scope:**
{{#DOMAIN_SCOPE}}
- {{SCOPE_ITEM}}
{{/DOMAIN_SCOPE}}

**Related Components:**
{{#DOMAIN_COMPONENTS}}
- `{{COMPONENT_PATH}}` - {{COMPONENT_DESC}}
{{/DOMAIN_COMPONENTS}}

{{/DOMAINS}}

---

## Review Requirements

### PR Review Matrix

| Change Type | Required Reviewers | Approval Count |
|-------------|-------------------|----------------|
{{#REVIEW_MATRIX}}
| {{CHANGE_TYPE}} | {{REVIEWERS}} | {{APPROVALS}} |
{{/REVIEW_MATRIX}}

### Special Review Requirements

| Condition | Additional Reviewer | Reason |
|-----------|---------------------|--------|
{{#SPECIAL_REVIEWS}}
| {{CONDITION}} | @{{REVIEWER}} | {{REASON}} |
{{/SPECIAL_REVIEWS}}

---

## Escalation Paths

### Technical Escalation

```
Level 1: Component Owner
    ↓ (no response in {{L1_SLA}})
Level 2: Team Lead
    ↓ (no response in {{L2_SLA}})
Level 3: {{L3_ROLE}}
    ↓ (critical issue)
Level 4: {{L4_ROLE}}
```

### Incident Escalation

| Severity | Initial Contact | Escalation After | Final Escalation |
|----------|-----------------|------------------|------------------|
| P1 (Critical) | {{P1_INITIAL}} | {{P1_ESCALATION}} | {{P1_FINAL}} |
| P2 (High) | {{P2_INITIAL}} | {{P2_ESCALATION}} | {{P2_FINAL}} |
| P3 (Medium) | {{P3_INITIAL}} | {{P3_ESCALATION}} | {{P3_FINAL}} |
| P4 (Low) | {{P4_INITIAL}} | {{P4_ESCALATION}} | {{P4_FINAL}} |

---

## On-Call Responsibilities

### Rotation Schedule

| Team | Schedule | Primary | Secondary |
|------|----------|---------|-----------|
{{#ON_CALL}}
| {{TEAM}} | {{SCHEDULE}} | @{{PRIMARY}} | @{{SECONDARY}} |
{{/ON_CALL}}

### On-Call Expectations

1. **Response Time:** {{RESPONSE_TIME_SLA}}
2. **Acknowledgment:** {{ACK_SLA}}
3. **Resolution or Escalation:** {{RESOLUTION_SLA}}

---

## Decision Rights

### Architecture Decisions

| Decision Type | Decision Maker | Consulted | Informed |
|---------------|----------------|-----------|----------|
{{#ARCH_DECISIONS}}
| {{DECISION_TYPE}} | @{{DECIDER}} | {{CONSULTED}} | {{INFORMED}} |
{{/ARCH_DECISIONS}}

### Breaking Changes

| Impact | Required Approval | Notice Period |
|--------|-------------------|---------------|
{{#BREAKING_CHANGES}}
| {{IMPACT}} | {{APPROVAL}} | {{NOTICE}} |
{{/BREAKING_CHANGES}}

---

## Contact Directory

### Quick Contacts

| Need Help With | Contact | Method |
|----------------|---------|--------|
{{#QUICK_CONTACTS}}
| {{HELP_WITH}} | @{{CONTACT}} | {{METHOD}} |
{{/QUICK_CONTACTS}}

### Communication Channels

| Channel | Purpose | Members |
|---------|---------|---------|
{{#CHANNELS}}
| {{CHANNEL}} | {{PURPOSE}} | {{MEMBERS}} |
{{/CHANNELS}}

---

## Ownership Transfer

### Process for Transferring Ownership

1. **Announce:** Notify stakeholders {{ANNOUNCE_LEAD_TIME}} in advance
2. **Document:** Update this ownership map
3. **Knowledge Transfer:** Complete {{KT_REQUIREMENTS}}
4. **Handoff Meeting:** Conduct formal handoff
5. **Shadow Period:** {{SHADOW_PERIOD}} of shadowing
6. **Update CODEOWNERS:** PR to update file

### Checklist for New Owners

- [ ] Access to all relevant systems
- [ ] Added to on-call rotation
- [ ] Completed knowledge transfer sessions
- [ ] Reviewed existing documentation
- [ ] Met with key stakeholders
- [ ] Understands escalation paths
- [ ] Has runbooks for common issues
