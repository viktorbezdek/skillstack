# Code Review - Extended Patterns & Examples

Detailed examples, workflow patterns, and integration guides extracted from the core skill.

## Evidence-Based Review Framework

### Finding Template

Every review finding MUST use this structure:

```yaml
finding:
  issue: "[description of problem]"
  evidence:
    location: "[file:line]"
    code_snippet: |
      [5 lines before]
      > [problematic line(s)]
      [5 lines after]
    evidence_type: "DIRECT | STYLE_RULE | BEST_PRACTICE"
  reference:
    source: "[style_guide | security_advisory | benchmark | standard]"
    citation: "[specific section or rule ID]"
    url: "[optional reference link]"
  severity: "CRITICAL | MAJOR | MINOR | NIT"
  scope: "ARCHITECTURE | MODULE | FUNCTION | LINE"
  confidence: number (0.0-1.0)
  suggested_fix: |
    [specific code change or approach]
```

### Example Finding

```yaml
finding:
  issue: "SQL injection vulnerability in user query"
  evidence:
    location: "src/api/users.js:42"
    code_snippet: |
      40: app.get('/users', (req, res) => {
      41:   const userId = req.query.id;
      > 42:   const sql = `SELECT * FROM users WHERE id = ${userId}`;
      43:   db.query(sql, (err, results) => {
      44:     res.json(results);
    evidence_type: "DIRECT"
  reference:
    source: "OWASP Top 10 2021"
    citation: "A03:2021 - Injection"
    url: "https://owasp.org/Top10/A03_2021-Injection/"
  severity: "CRITICAL"
  scope: "FUNCTION"
  confidence: 1.0
  suggested_fix: |
    Use parameterized queries:
    const sql = 'SELECT * FROM users WHERE id = ?';
    db.query(sql, [userId], (err, results) => {
```

---

## PR Comment Analysis Workflow

### Step 1: Extract PR Comments

```bash
cd /path/to/your/repo
python scripts/pr-comment-grabber.py owner/repo PR_NUMBER
```

Creates `pr-code-review-comments/pr{NUM}-code-review-comments.json`

### Step 2: Analyze with Three-Phase Validation

**Phase A: Initial Consolidation**
- Group comments by file and identify consensus
- Categorize by type (critical/design/style)

**Phase B: Context Validation**
- Check `.project-context.md` for project-specific constraints
- Validate comment applicability
- Flag outdated comments based on wrong assumptions

**Phase C: Impact Analysis**
- Search codebase for similar patterns using Grep
- Identify dependencies and potential breaking changes
- Generate "ripple effect" warnings for risky changes

### Comment JSON Schema

**Review comment (inline):**
```json
{
  "comment_type": "review",
  "id": 123456789,
  "user": "reviewer-username",
  "body": "Consider using a constant here instead of magic number",
  "path": "src/utils/constants.py",
  "line": 42,
  "diff_hunk": "@@ -40,6 +40,8 @@ ...",
  "created_at": "2025-01-15T14:30:00Z",
  "html_url": "https://github.com/owner/repo/pull/42#discussion_r123456789"
}
```

---

## Multi-Agent Swarm Review

### Execution Flow

```bash
#!/bin/bash
PR_NUMBER="$1"
FOCUS_AREAS="${2:-security,performance,style,tests,documentation}"

# Phase 1: PR Information Gathering
gh pr view "$PR_NUMBER" --json title,body,files,additions,deletions > pr-info.json
gh pr checkout "$PR_NUMBER"

# Phase 2-8: Initialize swarm, run parallel reviews, aggregate,
# generate fixes, assess merge readiness, create review comment
```

### Review Output Format

```markdown
# Automated Code Review (Evidence-Based)

**Overall Score**: 85/100
**Merge Ready**: Yes/No

## Review Summary
| Category | Score | Status |
|----------|-------|--------|
| Security | 90/100 | PASS |
| Performance | 85/100 | PASS |
| Style | 80/100 | PASS |
| Tests | 75/100 | FAIL |
| Quality | 88/100 | PASS |

## CRITICAL - Architecture-Level Issues
[Critical findings with evidence]

## MAJOR - Module-Level Issues
[Major findings with evidence]

## MINOR - Function-Level Improvements
[Minor findings with evidence]

## NIT - Line-Level Suggestions
[Nits with references]
```

---

## AI-Powered Consultation

### Basic Usage

```bash
uvx --from {SCRIPTS_PATH} consultant-cli \
  --prompt "Analyze this code for security vulnerabilities" \
  --file src/**/*.py \
  --slug "security-audit"
```

### Session Management

Sessions stored in `~/.consultant/sessions/{session-id}/`:
- `metadata.json`: Status, timestamps, token counts
- `prompt.txt`: Original user prompt
- `output.txt`: Streaming response
- `file_*`: Copies of all attached files

---

## Development Workflow Integration

### Integration Example

```python
from moai_workflow_testing import (
    AIDebugger, AIRefactorer, PerformanceProfiler,
    TDDManager, AutomatedCodeReviewer
)

# 1. AI-Powered Debugging
debugger = AIDebugger(context7_client=context7)
analysis = await debugger.debug_with_context7_patterns(error, context, path)

# 2. Smart Refactoring
refactorer = AIRefactorer(context7_client=context7)
refactor_plan = await refactorer.refactor_with_intelligence('/project/src')

# 3. Performance Optimization
profiler = PerformanceProfiler(context7_client=context7)
profiler.start_profiling(['cpu', 'memory', 'line'])
profile_results = profiler.stop_profiling()
bottlenecks = await profiler.detect_bottlenecks(profile_results)

# 4. Automated Code Review
reviewer = AutomatedCodeReviewer(context7_client=context7)
review_report = await reviewer.review_codebase('/project/src')
print(f"Overall TRUST Score: {review_report.overall_trust_score:.2f}")
```

### CI/CD Integration

```yaml
# .github/workflows/code-review.yml
name: Code Review
on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Extract PR Comments
        run: python scripts/pr-comment-grabber.py ${{ github.repository }} ${{ github.event.pull_request.number }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      - name: Run Code Review
        run: |
          moai-workflow review --project . --trust-score-min 0.8
      - uses: actions/upload-artifact@v3
        with:
          name: review-results
          path: pr-code-review-comments/
```

---

## Quality Gates and TRUST 5 Validation

### Quality Gate Configuration

```python
workflow = EnterpriseWorkflow(
    project_path="/project",
    quality_gates={
        'min_trust_score': 0.85,
        'max_critical_issues': 0,
        'required_coverage': 0.80
    }
)

results = await workflow.execute_with_validation()
if results.quality_passed:
    print("Ready for deployment")
else:
    workflow.show_quality_issues()
```

---

## Integration Examples

### Security Audit

```bash
uvx --from {SCRIPTS_PATH} consultant-cli \
  --prompt "Identify SQL injection vulnerabilities. For each: location, attack vector, fix." \
  --file "apps/*/src/**/*.{service,controller}.ts" \
  --slug "security-audit" \
  --model "claude-opus-4-5"
```

### PR Review

```bash
# Extract comments
python scripts/pr-comment-grabber.py owner/repo 42

# Generate diff
git diff origin/main...HEAD > /tmp/pr-diff.txt

# Consult AI for deep review
uvx --from {SCRIPTS_PATH} consultant-cli \
  --prompt "Review this PR for production deployment. Flag blockers and suggest regression tests." \
  --file /tmp/pr-diff.txt \
  --slug "pr-review"
```

### Automated Workflow

```bash
# Run complete code review workflow
moai-workflow execute --project /project/src --mode full

# Or individual components
moai-workflow review --project /project/src --trust-score-min 0.8
moai-workflow test --spec auth.spec --mode tdd
moai-workflow profile --target function_name --types cpu,memory
```

---

## Changelog

### v2.0.0 (Merged Skill)
- Combined 4 complementary skills into unified code review skill
- Integrated: Evidence-Based Code Review, PR Comment Analysis, Development Workflow Specialist, Consultant
- 55+ resource files covering all aspects of code review

### Source Skills
- **Evidence-Based Code Review v1.1.0**: Evidence-based multi-agent review
- **PR Comment Analysis v1.0**: GitHub PR comment extraction and analysis
- **Development Workflow Specialist v1.0.0**: TDD, debugging, optimization workflows
- **Consultant v1.0**: LiteLLM-based AI consultation
