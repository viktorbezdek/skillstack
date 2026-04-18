---
name: security-hardening-audit
description: Systematic security audit workflow for hardening a codebase through structured multi-pass analysis. Composes four skills across five phases — threat surface mapping with attack vector identification (risk-management), security-focused code review targeting OWASP and language-specific vulnerabilities (code-review), boundary condition and validation gap analysis (edge-case-coverage), and security test suite construction with fuzzing and property-based tests (testing-framework). Use when hardening an existing codebase before launch, after a security incident, during compliance preparation, or for periodic security reviews. Use when you want a structured audit rather than ad-hoc scanning. NOT for real-time intrusion detection or incident response — use your SIEM. NOT for infrastructure/network security — this covers application code only.
---

# Security Hardening Audit

> Security bugs are found by structure, not by luck. An ad-hoc "look for vulnerabilities" pass catches the easy ones and misses the systemic ones. A structured multi-pass audit — threat modeling, code review, edge case analysis, test hardening — finds the bugs that matter because each pass is optimized for a different class of vulnerability.

Most codebases have security gaps not because the team is careless, but because security review happens as a single pass with no framework. This workflow runs four distinct passes, each targeting a different vulnerability class, and produces a hardened codebase with evidence — not just a checklist.

---

## When to use this workflow

- Hardening a codebase before a public launch or major release
- Responding to a security incident by auditing the affected areas and beyond
- Preparing for a compliance audit (SOC2, HIPAA, PCI-DSS)
- Running a periodic (quarterly/annual) security review
- Onboarding a new codebase that hasn't had a security audit

## When NOT to use this workflow

- **Real-time incident response** — this is a proactive audit, not a reactive playbook; use your incident response runbook
- **Infrastructure/network security** — this covers application code; use infrastructure-specific tools for network, firewall, and cloud IAM
- **Dependency-only vulnerability scanning** — use `npm audit`, `pip-audit`, or Snyk directly; this workflow covers code, not just dependencies
- **Quick one-file fix for a known vulnerability** — just fix it; this workflow is for systematic audits, not patch management

---

## Prerequisites

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install risk-management@skillstack
/plugin install code-review@skillstack
/plugin install edge-case-coverage@skillstack
/plugin install testing-framework@skillstack
```

---

## Core principle

**Every security finding must produce both a fix and a test that proves the fix works.** A finding without a fix is a report that collects dust. A fix without a test is a fix that can regress silently. The audit is not complete when findings are listed — it's complete when every finding has a corresponding test that would catch the vulnerability if it were reintroduced.

Secondary principle: **layer the passes by vulnerability class.** Each phase targets a different attack surface. Threat modeling finds design-level vulnerabilities (missing auth boundaries, data flow issues). Code review finds implementation-level vulnerabilities (injection, leakage). Edge case analysis finds validation-level vulnerabilities (boundary bypasses, malformed input). Test hardening ensures the fixes stick.

---

## The phases

### Phase 1 — threat surface mapping (risk-management)

Load the `risk-management` skill. Before looking at any code, map the attack surface:

- **Entry points** — every way data enters the system: API endpoints, form inputs, file uploads, webhooks, message queues, CLI arguments, environment variables
- **Trust boundaries** — where does trusted data become untrusted? Where does internal data cross to external? Map every boundary.
- **Data sensitivity** — classify data by sensitivity: PII, credentials, financial data, health data, public data. Each class has different protection requirements.
- **Attack vectors per entry point** — for each entry point, list the attacks that apply: injection (SQL, XSS, command), authentication bypass, authorization escalation, information disclosure, denial of service, CSRF
- **Risk scoring** — likelihood x impact for each vector. High-likelihood, high-impact vectors get audited first.

This phase produces the audit scope — a prioritized list of what to examine and in what order. Without it, the code review in Phase 2 has no focus and will spend time on low-risk areas while missing high-risk ones.

Output: a threat model document with entry points, trust boundaries, attack vectors, and prioritized risk scores.

### Phase 2 — security-focused code review (code-review)

Load the `code-review` skill. Run a review focused exclusively on security, using the threat model from Phase 1 to prioritize:

**For each high-risk entry point, check:**

- **Injection** — is all user input parameterized before reaching SQL, shell, or template engines? Are there any string concatenation patterns near these boundaries?
- **Authentication** — can any endpoint be reached without proper auth? Are tokens validated on every request, not just at login?
- **Authorization** — can user A access user B's data by manipulating IDs or paths? Are authorization checks at the data layer, not just the route layer?
- **Information leakage** — do error messages expose stack traces, database schemas, or internal paths? Do API responses include fields the client shouldn't see?
- **Cryptography** — are secrets stored hashed (not encrypted, not plaintext)? Are deprecated algorithms in use (MD5, SHA1 for security purposes)?
- **Session management** — are sessions invalidated on logout? Do tokens expire? Is there session fixation protection?
- **OWASP Top 10** — systematic check against the current OWASP Top 10 for the relevant platform (web, API, mobile)

Document every finding with: location (file + line), vulnerability class, severity (critical/high/medium/low), and a specific remediation.

Output: a findings list with severity, location, and remediation for each vulnerability.

### Phase 3 — edge case and validation analysis (edge-case-coverage)

Load the `edge-case-coverage` skill. This phase catches what the code review misses — vulnerabilities that exist in boundary conditions and validation gaps:

- **Input boundaries** — maximum length strings, empty strings, null bytes, Unicode edge cases (zero-width characters, right-to-left override), extremely large numbers, negative values where only positive expected
- **Type coercion** — what happens when a string is passed where a number is expected? When an array is passed where an object is expected? Loose typing languages are especially vulnerable.
- **Race conditions** — are there time-of-check-to-time-of-use (TOCTOU) vulnerabilities? Can concurrent requests bypass rate limits or create duplicate resources?
- **State transitions** — can the system be put into an invalid state by calling operations in an unexpected order? (e.g., paying before checkout, accessing before auth)
- **Resource exhaustion** — can an attacker trigger unbounded memory allocation, file creation, or database writes? Are there missing limits on batch operations?
- **Encoding mismatches** — do different parts of the system interpret encoding differently? (URL encoding, HTML encoding, JSON encoding — mismatches are injection vectors)

For each gap found, trace whether it's exploitable in context. Not every edge case is a vulnerability — but every unhandled edge case near a trust boundary is a candidate.

Output: an edge case catalog with exploitability assessment for each finding.

### Phase 4 — security test hardening (testing-framework)

Load the `testing-framework` skill. For every finding from Phases 2 and 3, build tests:

**Per-finding tests:**
- Write a test that reproduces the vulnerability (the "red" state — confirming the bug exists or would exist without the fix)
- Implement the fix
- Verify the test passes with the fix in place
- The test now serves as a regression guard

**Systematic security tests:**
- **Fuzzing** — for parsers, deserializers, and input handlers, add fuzz tests that throw random/malformed data at them. Property: the system never crashes, never leaks internal state.
- **Property-based tests** — for authorization logic: "for any user and any resource, if the user doesn't own the resource and isn't admin, access is denied." For input validation: "for any string input, the output is always properly escaped."
- **Negative test suite** — a dedicated suite of tests that verify the system rejects what it should: invalid tokens, expired sessions, malformed payloads, unauthorized access attempts

Output: a security test suite with per-finding regression tests, fuzz tests, and property-based invariants.

### Phase 5 — remediation and re-audit

With findings from Phases 2-3 and tests from Phase 4:

1. **Fix all critical and high findings first** — these are blocking for any release
2. **Fix medium findings** — schedule low findings if not immediately fixable
3. **Re-run the Phase 2 code review** on the changed code — fixes sometimes introduce new vulnerabilities
4. **Re-run the full test suite** — confirm all security tests pass, no regressions in functional tests
5. **Update the threat model** — if fixes changed the architecture (new auth middleware, new validation layer), update the Phase 1 document

The audit is complete when: all critical/high findings are fixed, all fixes have regression tests, the test suite passes, and the threat model reflects the current state.

Output: a remediation report with fix evidence, test results, and updated threat model.

---

## Decision Tree

```
What's the security situation?
│
├─ Hardening before launch
│   └─ Run all 5 phases — full audit is the point
│
├─ After a security incident
│   └─ Phase 1 (threat model, scoped to affected area) → Phase 2 → Phase 4 → Phase 5
│      skip Phase 3 (edge cases) if the incident was a known vuln class
│
├─ Compliance preparation (SOC2, HIPAA, PCI-DSS)
│   └─ Phase 1 (threat model with compliance controls) → Phase 2 → Phase 4
│      Phase 3 optional — compliance usually needs evidence, not edge cases
│
├─ Periodic security review
│   └─ Phase 1 → Phase 2 only — focused review, not full hardening
│
├─ New codebase, never audited
│   └─ Run all 5 phases — you have no baseline
│
└─ Quick one-file fix for known vulnerability
    └─ Skip this workflow — just fix it directly
```

## Anti-Patterns

| # | Anti-Pattern | Symptom | Fix |
|---|---|---|---|
| 1 | **Checklist-only audit** | Team runs OWASP Top 10 as a generic checklist without mapping to their entry points | Phase 1's threat model ensures the review targets actual risk in your specific codebase, not abstract categories. |
| 2 | **Findings without fixes** | Beautiful report with 47 findings, but nobody fixes them; vulnerabilities ship | Phase 5 requires fixes and tests, not just findings. A finding without a fix is a report that collects dust. |
| 3 | **Fix-and-forget** | Vulnerability is fixed but no regression test added; a refactor reintroduces it 6 months later | Phase 4 requires a test for every finding. The test is the permanent guard. |
| 4 | **Scope creep into infrastructure** | Audit starts reviewing Kubernetes configs, firewall rules, cloud IAM | The scope is application code only. Infrastructure security requires different expertise and tools. |
| 5 | **Testing the happy path only** | All security tests pass, but none test malformed input or unauthorized access | Phase 4 requires negative tests, fuzz tests, and property-based invariants, not just functional tests. |
| 6 | **Auditing dependencies instead of code** | Team runs `npm audit` and calls it done | Dependency scanning is necessary but not sufficient. Phase 2 reviews YOUR code for injection, auth bypass, and leakage that no scanner catches. |

## Gates and failure modes

**Gate 1: the threat model gate.** Phase 2 cannot start until Phase 1's threat model exists. Reviewing code without knowing where the risks are produces unfocused reviews.

**Gate 2: the findings gate.** Phase 4 cannot start until Phases 2 and 3 have produced findings. Writing security tests without findings means testing what you imagine, not what's actually vulnerable.

**Gate 3: the regression gate.** Phase 5 cannot conclude until every fix has a corresponding test. Fixes without tests will regress.

**Failure mode: checklist-only audit.** The team runs through OWASP Top 10 as a checklist without mapping it to their specific entry points and data flows. Generic checklists miss application-specific vulnerabilities. Mitigation: Phase 1's threat model ensures the review targets actual risk.

**Failure mode: findings without fixes.** The audit produces a beautiful report with 47 findings, but nobody fixes them. The report sits in a wiki and the vulnerabilities ship. Mitigation: Phase 5 requires fixes and tests, not just findings.

**Failure mode: fix-and-forget.** Vulnerabilities are fixed but no regression tests are added. Six months later, a refactor reintroduces the same vulnerability. Mitigation: Phase 4 requires a test for every finding.

**Failure mode: scope creep into infrastructure.** The audit starts reviewing Kubernetes configs, firewall rules, and cloud IAM policies. Those are important but require different expertise and tools. Mitigation: the scope is application code only, stated in "When NOT to use."

---

## Output artifacts

1. **Threat model** — entry points, trust boundaries, attack vectors, risk scores
2. **Findings list** — from code review and edge case analysis, with severity and remediation
3. **Security test suite** — per-finding regression tests, fuzz tests, property-based invariants
4. **Remediation report** — fixes applied, test evidence, remaining items with schedule
5. **Updated threat model** — reflecting post-fix architecture

---

## Related workflows and skills

- For building a new API with security built in from the start, use the `api-to-production` workflow
- For debugging a specific security incident, use the `debug-complex-issue` workflow
- For ongoing risk management beyond code, use `risk-management` directly
- For compliance-specific testing frameworks, use `testing-framework` with compliance-oriented test patterns

---

> *SkillStack Workflows by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
