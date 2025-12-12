# Product Specification: {{PRODUCT_NAME}}

## Document Info

| Attribute | Value |
|-----------|-------|
| **Product** | {{PRODUCT_NAME}} |
| **Version** | {{SPEC_VERSION}} |
| **Status** | {{STATUS}} |
| **Author** | {{AUTHOR}} |
| **Last Updated** | {{LAST_UPDATED}} |
| **Reviewers** | {{REVIEWERS}} |

---

## Executive Summary

### Problem Statement

{{PROBLEM_STATEMENT}}

### Solution Overview

{{SOLUTION_OVERVIEW}}

### Success Metrics

| Metric | Current | Target | Timeline |
|--------|---------|--------|----------|
{{#SUCCESS_METRICS}}
| {{METRIC}} | {{CURRENT}} | {{TARGET}} | {{TIMELINE}} |
{{/SUCCESS_METRICS}}

---

## Background

### Context

{{CONTEXT}}

### Current State

{{CURRENT_STATE}}

### Why Now?

{{WHY_NOW}}

### Prior Art

| Solution | Pros | Cons | Why Not |
|----------|------|------|---------|
{{#PRIOR_ART}}
| {{SOLUTION}} | {{PROS}} | {{CONS}} | {{WHY_NOT}} |
{{/PRIOR_ART}}

---

## Goals & Non-Goals

### Goals

{{#GOALS}}
1. **{{GOAL_TITLE}}** - {{GOAL_DESCRIPTION}}
{{/GOALS}}

### Non-Goals

{{#NON_GOALS}}
- {{NON_GOAL}}
{{/NON_GOALS}}

### Future Considerations

{{#FUTURE_CONSIDERATIONS}}
- {{CONSIDERATION}}
{{/FUTURE_CONSIDERATIONS}}

---

## User Research

### Target Users

{{#USER_PERSONAS}}
#### {{PERSONA_NAME}}

| Attribute | Value |
|-----------|-------|
| **Role** | {{ROLE}} |
| **Goals** | {{GOALS}} |
| **Pain Points** | {{PAIN_POINTS}} |
| **Technical Level** | {{TECH_LEVEL}} |

**User Story:**
> As a {{PERSONA_NAME}}, I want to {{WANT}} so that {{BENEFIT}}.

{{/USER_PERSONAS}}

### User Research Findings

{{#RESEARCH_FINDINGS}}
#### {{FINDING_TITLE}}

**Source:** {{SOURCE}}

**Insight:** {{INSIGHT}}

**Implications:** {{IMPLICATIONS}}

{{/RESEARCH_FINDINGS}}

---

## Requirements

### Functional Requirements

{{#FUNCTIONAL_REQUIREMENTS}}
#### {{REQ_ID}}: {{REQ_TITLE}}

| Attribute | Value |
|-----------|-------|
| **Priority** | {{PRIORITY}} |
| **Complexity** | {{COMPLEXITY}} |
| **Dependencies** | {{DEPENDENCIES}} |

**Description:**
{{REQ_DESCRIPTION}}

**Acceptance Criteria:**
{{#ACCEPTANCE_CRITERIA}}
- [ ] {{CRITERION}}
{{/ACCEPTANCE_CRITERIA}}

{{/FUNCTIONAL_REQUIREMENTS}}

### Non-Functional Requirements

| Category | Requirement | Target | Measurement |
|----------|-------------|--------|-------------|
{{#NON_FUNCTIONAL}}
| {{CATEGORY}} | {{REQUIREMENT}} | {{TARGET}} | {{MEASUREMENT}} |
{{/NON_FUNCTIONAL}}

### Constraints

{{#CONSTRAINTS}}
- **{{CONSTRAINT_TYPE}}:** {{CONSTRAINT_DESCRIPTION}}
{{/CONSTRAINTS}}

---

## User Experience

### User Flows

{{#USER_FLOWS}}
#### {{FLOW_NAME}}

**Trigger:** {{TRIGGER}}

**Steps:**
```
{{FLOW_DIAGRAM}}
```

**Success State:** {{SUCCESS_STATE}}

**Error States:**
{{#ERROR_STATES}}
- {{ERROR_STATE}}
{{/ERROR_STATES}}

{{/USER_FLOWS}}

### Wireframes

{{#WIREFRAMES}}
#### {{SCREEN_NAME}}

![{{SCREEN_NAME}}]({{WIREFRAME_URL}})

**Key Elements:**
{{#ELEMENTS}}
- {{ELEMENT}}
{{/ELEMENTS}}

{{/WIREFRAMES}}

### Copy & Messaging

| Context | Message | Notes |
|---------|---------|-------|
{{#COPY}}
| {{CONTEXT}} | "{{MESSAGE}}" | {{NOTES}} |
{{/COPY}}

---

## Technical Approach

### High-Level Architecture

```
{{ARCHITECTURE_DIAGRAM}}
```

### Key Technical Decisions

{{#TECH_DECISIONS}}
#### {{DECISION_TITLE}}

**Context:** {{CONTEXT}}

**Options Considered:**
{{#OPTIONS}}
- **{{OPTION}}:** {{DESCRIPTION}}
{{/OPTIONS}}

**Decision:** {{DECISION}}

**Rationale:** {{RATIONALE}}

{{/TECH_DECISIONS}}

### Data Model

```
{{DATA_MODEL}}
```

### API Changes

| Endpoint | Method | Change | Breaking |
|----------|--------|--------|----------|
{{#API_CHANGES}}
| `{{ENDPOINT}}` | {{METHOD}} | {{CHANGE}} | {{BREAKING}} |
{{/API_CHANGES}}

---

## Launch Plan

### Phases

{{#PHASES}}
#### Phase {{PHASE_NUMBER}}: {{PHASE_NAME}}

**Timeline:** {{TIMELINE}}

**Scope:**
{{#SCOPE}}
- {{SCOPE_ITEM}}
{{/SCOPE}}

**Success Criteria:**
{{#CRITERIA}}
- {{CRITERION}}
{{/CRITERIA}}

**Rollout:** {{ROLLOUT_STRATEGY}}

{{/PHASES}}

### Feature Flags

| Flag | Phase | Default | Description |
|------|-------|---------|-------------|
{{#FEATURE_FLAGS}}
| `{{FLAG}}` | {{PHASE}} | {{DEFAULT}} | {{DESCRIPTION}} |
{{/FEATURE_FLAGS}}

### Rollback Plan

{{ROLLBACK_PLAN}}

---

## Risks & Mitigations

| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
{{#RISKS}}
| {{RISK}} | {{PROBABILITY}} | {{IMPACT}} | {{MITIGATION}} | @{{OWNER}} |
{{/RISKS}}

---

## Dependencies

### Internal Dependencies

| Dependency | Team | Status | Timeline | Blocker |
|------------|------|--------|----------|---------|
{{#INTERNAL_DEPS}}
| {{DEPENDENCY}} | {{TEAM}} | {{STATUS}} | {{TIMELINE}} | {{BLOCKER}} |
{{/INTERNAL_DEPS}}

### External Dependencies

| Dependency | Vendor | Status | Risk |
|------------|--------|--------|------|
{{#EXTERNAL_DEPS}}
| {{DEPENDENCY}} | {{VENDOR}} | {{STATUS}} | {{RISK}} |
{{/EXTERNAL_DEPS}}

---

## Resources

### Team

| Role | Person | Allocation |
|------|--------|------------|
{{#TEAM}}
| {{ROLE}} | @{{PERSON}} | {{ALLOCATION}} |
{{/TEAM}}

### Timeline

| Milestone | Target Date | Status |
|-----------|-------------|--------|
{{#MILESTONES}}
| {{MILESTONE}} | {{DATE}} | {{STATUS}} |
{{/MILESTONES}}

### Budget

| Category | Estimated | Approved |
|----------|-----------|----------|
{{#BUDGET}}
| {{CATEGORY}} | {{ESTIMATED}} | {{APPROVED}} |
{{/BUDGET}}

---

## Success Measurement

### KPIs

| KPI | Definition | Baseline | Target | Measurement |
|-----|------------|----------|--------|-------------|
{{#KPIS}}
| {{KPI}} | {{DEFINITION}} | {{BASELINE}} | {{TARGET}} | {{MEASUREMENT}} |
{{/KPIS}}

### Analytics Events

| Event | Trigger | Properties |
|-------|---------|------------|
{{#EVENTS}}
| `{{EVENT}}` | {{TRIGGER}} | {{PROPERTIES}} |
{{/EVENTS}}

### Dashboards

| Dashboard | Purpose | URL |
|-----------|---------|-----|
{{#DASHBOARDS}}
| {{NAME}} | {{PURPOSE}} | [Link]({{URL}}) |
{{/DASHBOARDS}}

---

## Support & Operations

### Documentation Needed

| Document | Owner | Status |
|----------|-------|--------|
{{#DOCS_NEEDED}}
| {{DOCUMENT}} | @{{OWNER}} | {{STATUS}} |
{{/DOCS_NEEDED}}

### Support Training

{{SUPPORT_TRAINING}}

### Runbook

[Operations Runbook]({{RUNBOOK_URL}})

---

## Open Questions

{{#OPEN_QUESTIONS}}
- [ ] **{{QUESTION}}** - Owner: @{{OWNER}}, Due: {{DUE}}
{{/OPEN_QUESTIONS}}

---

## Appendix

### Glossary

| Term | Definition |
|------|------------|
{{#GLOSSARY}}
| {{TERM}} | {{DEFINITION}} |
{{/GLOSSARY}}

### References

{{#REFERENCES}}
- [{{TITLE}}]({{URL}})
{{/REFERENCES}}

### Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
{{#REVISIONS}}
| {{VERSION}} | {{DATE}} | @{{AUTHOR}} | {{CHANGES}} |
{{/REVISIONS}}
