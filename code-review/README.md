# Code Review

> **v1.1.24** | Quality & Testing | 26 iterations

Perform thorough code reviews with multi-agent swarm analysis covering security, performance, style, tests, and documentation. Analyze PRs, extract and prioritize comments, and generate actionable fix plans.

## What Problem Does This Solve

Code reviews performed without systematic structure miss security vulnerabilities, let performance bottlenecks pass, and produce inconsistent feedback that's hard for authors to act on. Pull requests with many reviewers generate overlapping comments without clear priority — leaving authors unsure what must be fixed versus what's a suggestion. This skill applies multi-agent parallel analysis across five quality dimensions (security, performance, style, tests, documentation) with every finding grounded to a specific file and line number, severity level, and actionable fix.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Review this PR before I merge it" | Multi-agent swarm review with five parallel specialists (security, performance, style, tests, docs) producing prioritized findings with file:line references |
| "There are 30 comments on my PR from 4 reviewers — what should I fix first?" | PR comment extraction and consolidation workflow identifying high-consensus issues where multiple reviewers flagged the same concern |
| "I need to audit this codebase for security vulnerabilities" | Security reviewer agent scanning for unsafe patterns, secret exposure, injection risks, and auth issues with CRITICAL/MAJOR severity classification |
| "Does this code have performance problems I'm missing?" | Performance analyst agent identifying bottlenecks, unnecessary database calls, and optimization opportunities with evidence-backed findings |
| "How do I know if my review findings are real issues or false positives?" | TRUST 5 validation framework requiring 2+ confirming signals before flagging violations, with <5% false positive rate target |
| "I need a structured action plan from this code review" | Prioritized fix plan organized by severity (CRITICAL → MAJOR → MINOR → NIT) with specific code change suggestions for each finding |

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install code-review@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the code-review skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `code-review`
- `security`
- `performance`
- `style`

## What's Inside

- **When to Use** -- Conditions for applying this skill with explicit exclusions (simple formatting, trivial changes, generated code)
- **Core Capabilities** -- Evidence-based review requirements (file:line, evidence type, severity, confidence), PR comment extraction and grouping, five-agent parallel swarm, AI-powered consultation, and TRUST 5 validation framework
- **Severity Levels** -- Four-level classification (CRITICAL → MAJOR → MINOR → NIT) with scope definitions from architecture to line level
- **Validation Rules** -- Constraints ensuring findings are evidence-backed, include line numbers, distinguish symptoms from root causes, and maintain <5% false positive rate
- **Success Criteria** -- Measurable targets: zero false negatives, <5% false positive rate, 100% actionable findings with file paths and fix guidance
- **Resources Reference** -- Scripts (PR comment grabber, multi-agent orchestrator, security scanner), reference docs (analysis prompts, impact methodology, validation workflow), and review templates

## Key Capabilities

- **Security Reviewer**
- **Performance Analyst**
- **Style Reviewer**
- **Test Specialist**
- **Documentation Reviewer**
- **Truthfulness**

## Version History

- `1.1.24` fix(testing+debugging): optimize descriptions with NOT clauses for disambiguation (b00fc60)
- `1.1.23` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.1.22` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.1.21` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.1.20` refactor: remove old file locations after plugin restructure (a26a802)
- `1.1.19` docs: update README and install commands to marketplace format (af9e39c)
- `1.1.18` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.1.17` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.1.16` fix: resolve broken links, flatten faber scripts, add validate-patterns.py (4647f46)
- `1.1.15` fix: make all shell scripts executable and fix Python syntax errors (61ac964)

## Related Skills

- **[Consistency Standards](../consistency-standards/)** -- Establish and maintain naming conventions, taxonomy standards, style guides, and reuse patterns across documentation and...
- **[Edge Case Coverage](../edge-case-coverage/)** -- Identify and document boundary conditions, error scenarios, corner cases, and validation requirements.
- **[Test Driven Development](../test-driven-development/)** -- Comprehensive Test-Driven Development skill implementing Red-Green-Refactor cycle across Python, TypeScript, JavaScript,...
- **[Testing Framework](../testing-framework/)** -- Comprehensive testing framework for multiple languages and platforms. Covers unit testing (Rust, TypeScript, PHP, Shell)...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
