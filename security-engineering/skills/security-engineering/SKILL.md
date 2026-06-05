---
name: security-engineering
description: >-
  Application security design and threat-informed engineering. Use for authentication and authorisation architecture (OAuth2, JWT, RBAC, ABAC), OWASP Top 10 vulnerability analysis, secrets management (Vault, AWS Secrets Manager, environment isolation), input validation patterns, secure API design, SQL injection and XSS prevention, and security-aware code review. Trigger phrases: "secure this endpoint", "design an auth system", "review this for security vulnerabilities", "how do I store secrets", "implement RBAC". NOT for network/infrastructure security (firewalls, VPNs, WAF config) — those belong in cloud-infrastructure. NOT for compliance auditing (SOC2, GDPR gap assessments) — that requires a compliance specialist. NOT for penetration testing or red-teaming — this skill is for defensive engineering, not offensive exercises.
allowed-tools: Read,Write,Edit,Bash
---

# security-engineering

Application security design, OWASP patterns, authentication architecture, secrets management, and threat-model-informed code review.

## When to use

- Design a JWT-based authentication system with refresh token rotation
- Review this login endpoint for security vulnerabilities
- How should I store API keys for third-party integrations?
- Implement role-based access control for our multi-tenant app
- This SQL query uses string concatenation — is it vulnerable to injection?
- Threat model our new payment endpoint
- How do I prevent CSRF attacks in a SPA with cookie-based auth?
- Design an OAuth2 authorization code flow with PKCE

## When NOT to use

- Configure our AWS VPC security groups — Network/infra security — cloud-infrastructure skill
- Help us pass our SOC2 Type II audit — Compliance audit — out of scope
- Run a penetration test on our staging environment — Offensive/pentest — out of scope
- Set up a WAF in front of our load balancer — Infrastructure security — not application-layer

## Anti-patterns

### Symptom
Invoking this skill for tasks outside its scope — e.g., infrastructure concerns when the request is about application code, or vice versa.

### Problem
Scope mismatch wastes context and produces advice tuned for the wrong domain. A database schema skill answering a connection-pooling question gives schema advice when the real problem is operational configuration.

### Solution
Read the NOT for clauses carefully. If the request matches an exclusion, identify the correct skill (check SkillStack for the right domain) rather than stretching this skill to cover adjacent ground.
