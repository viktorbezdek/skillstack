---
title: "Python Development Orchestration Guide"
description: "Guide for orchestrating Python development tasks using specialized agents and commands"
version: "1.0.0"
last_updated: "2025-11-02"
document_type: "guide"
python_compatibility: "3.11+"
related_docs:
  - "../SKILL.md"
  - "./modern-modules.md"
  - "./tool-library-registry.md"
---

# Python Development Orchestration Guide

Comprehensive guide for orchestrating Python development tasks using specialized agents and commands. This guide provides detailed workflows and patterns for coordinating multiple agents to accomplish complex Python development goals.

**Quick Reference**: For a concise overview and quick-start examples, see [SKILL.md](../SKILL.md).

## Available Agents and Commands

### Agents (in ~/.claude/agents/)

- **python-cli-architect**: Build modern CLI applications with Typer and Rich
- **python-portable-script**: Create stdlib-only portable scripts
- **python-pytest-architect**: Design comprehensive test suites
- **python-code-reviewer**: Review Python code for quality and standards
- **spec-architect**: Design system architecture
- **spec-planner**: Break down tasks into implementation plans

### Commands (in this skill: references/commands/)

- **/modernpython**: Apply Python 3.11+ best practices and modern patterns
- **/shebangpython**: Validate PEP 723 shebang compliance

### External Skills

- **uv**: Package management with uv (always use for Python dependency management)

## Core Workflow Patterns

### 1. TDD Workflow (Test-Driven Development)

**When to use**: Building new features, fixing bugs with test coverage

**Pattern**:

```text
1. Design → @agent-spec-architect
   Input: Feature requirements
   Output: Architecture design, component interfaces

2. Write Tests → @agent-python-pytest-architect
   Input: Architecture design, expected behavior
   Output: Complete test suite (fails initially)

3. Implement → @agent-python-cli-architect OR @agent-python-portable-script
   Input: Tests, architecture design
   Output: Implementation that makes tests pass

4. Review → @agent-python-code-reviewer
   Input: Implementation + tests
   Output: Review feedback, improvement suggestions

5. Validate
   - Code quality checks (linting, formatting) performed and issues addressed per the holistic-linting skill
   - Apply: /modernpython to check modern patterns
   - Run: uv run pytest
   - Verify: CI compatibility by checking .gitlab-ci.yml or .github/workflows/
```

**Example**:

```text
User: "Build a CLI tool to process CSV files with progress bars"

Step 1: @agent-spec-architect
  "Design architecture for CSV processing CLI with progress tracking"
  → Architecture design with components

Step 2: @agent-python-pytest-architect
  "Create test suite for CSV processor based on this architecture"
  → Test files in tests/

Step 3: @agent-python-cli-architect
  "Implement CSV processor CLI with Typer+Rich based on these tests"
  → Implementation in packages/

Step 4: @agent-python-code-reviewer
  "Review this implementation against the architecture and test requirements"
  → Review findings, suggested improvements

Step 5: Validate
  → All tests pass, coverage >80%, linting clean
```

### 2. Feature Addition Workflow

**When to use**: Adding new functionality to existing codebase

**Pattern**:

```text
1. Requirements → User or @agent-spec-analyst
   Output: Clear requirements, acceptance criteria

2. Architecture → @agent-spec-architect
   Input: Requirements, existing codebase structure
   Output: Design that integrates with existing code

3. Implementation Plan → @agent-spec-planner
   Input: Architecture design
   Output: Step-by-step implementation tasks

4. Implement → @agent-python-cli-architect OR @agent-python-portable-script
   Input: Implementation plan, existing code patterns
   Output: New feature implementation

5. Testing → @agent-python-pytest-architect
   Input: Implementation, edge cases
   Output: Tests for new feature + integration tests

6. Review → @agent-python-code-reviewer
   Input: All changes (implementation + tests)
   Output: Quality assessment, improvements

7. Validate
   - Check: No regressions in existing tests
   - Verify: New feature has >80% coverage
   - Code quality checks (linting, formatting) performed and issues addressed per the holistic-linting skill
   - Apply: /modernpython for consistency
```

### 3. Code Review Workflow

**When to use**: Before merging changes, during PR review

**Pattern**:

```text
1. Self-Review → Apply /modernpython
   Check: Modern Python patterns used
   Check: No legacy typing imports

2. Standards Validation → Apply /shebangpython (if scripts)
   Check: PEP 723 compliance
   Check: Correct shebang format

3. Agent Review → @agent-python-code-reviewer
   Input: All changed files
   Output: Comprehensive review findings

4. Fix Issues → Appropriate agent
   Input: Review findings
   Output: Corrections

5. Re-validate
   - Code quality checks (linting, formatting) performed and issues addressed per the holistic-linting skill
   - Run: uv run pytest
   - Verify: All review issues addressed
```

### 4. Refactoring Workflow

**When to use**: Improving code structure without changing behavior

**Pattern**:

```text
1. Tests First → Verify existing test coverage
   Check: Tests exist for code being refactored
   Check: Tests pass before refactoring
   If missing: @agent-python-pytest-architect creates tests

2. Refactor → @agent-python-cli-architect or @agent-python-portable-script
   Input: Code to refactor + test suite
   Constraint: Must not break existing tests
   Output: Refactored code

3. Validate → Tests still pass
   Run: uv run pytest
   Verify: Coverage maintained or improved

4. Review → @agent-python-code-reviewer
   Input: Before/after comparison
   Output: Verification refactoring improved quality

5. Apply Standards
   - Apply: /modernpython for modern patterns
   - Code quality checks (linting, formatting) performed and issues addressed per the holistic-linting skill
```

### 5. Debugging Workflow

**When to use**: Investigating and fixing bugs

**Pattern**:

```text
1. Reproduce → Write failing test
   @agent-python-pytest-architect
   Input: Bug description, steps to reproduce
   Output: Test that demonstrates bug

2. Trace → Investigate root cause
   Use: Debugging tools, logging
   Identify: Specific code causing issue

3. Fix → Appropriate agent
   @agent-python-cli-architect or @agent-python-portable-script
   Input: Failing test + root cause
   Output: Fix that makes test pass

4. Test → Verify fix + no regressions
   Run: Full test suite
   Verify: Bug test now passes
   Verify: No other tests broke

5. Review → @agent-python-code-reviewer
   Input: Fix + test
   Output: Verification fix is proper solution

6. Validate
   - Apply: /modernpython
   - Code quality checks (linting, formatting) performed and issues addressed per the holistic-linting skill
```

## Agent Selection Guide

### When to Use python-cli-architect

**Use when**:

- **DEFAULT choice for scripts and CLI tools**
- Building command-line applications with rich user interaction
- Need progress bars, tables, colored output
- User-facing CLI tools and automation scripts
- Any script where UX matters (formatted output, progress feedback)
- PEP 723 + uv available (internet access present)

**Characteristics**:

- Uses Typer for CLI framework
- Uses Rich for terminal output
- Focuses on UX and polish
- PEP 723 makes dependencies transparent (single file)
- Better UX than stdlib alternatives
- Works anywhere with Python 3.11+ and internet access

**Complexity Advantage** (IMPORTANT):

- ✅ **LESS development complexity** - Libraries handle the hard work (argument parsing, output formatting, validation)
- ✅ **LESS code to write** - Typer CLI boilerplate and Rich formatting come built-in
- ✅ **Better UX** - Professional output with minimal effort
- ✅ **Just as portable** - PEP 723 + uv makes single-file scripts with dependencies work seamlessly

**This agent is EASIER to use than stdlib-only approaches. Choose this as the default unless portability restrictions exist.**

**Rich Width Handling**: For Rich Panel/Table width issues in CI/non-TTY environments, see [Typer and Rich CLI Examples](../assets/typer_examples/index.md) for complete solutions including the `get_rendered_width()` helper pattern.

**Example tasks**:

- "Build a CLI tool to manage database backups with progress bars"
- "Create an interactive file browser with color-coded output"
- "Create a script to scan git repositories and show status tree"
- "Build a deployment verification tool with progress bars"

### When to Use python-portable-script

**Use when** (RARE - ask user first if unclear):

- **Restricted environment**: No internet access (airgapped, embedded systems)
- **No uv available**: Locked-down systems where uv cannot be installed
- **Hard stdlib-only requirement**: Explicitly requested by user
- **1% case**: Only when deployment environment truly restricts dependencies

**Characteristics**:

- Stdlib only (argparse, pathlib, subprocess)
- Defensive error handling
- Cross-platform compatibility
- Stdlib only (no PEP 723 needed - nothing to declare)
- Use PEP 723 ONLY if adding external dependencies later
- Ask deployment environment questions before choosing this agent
- This is the EXCEPTION, not the rule
- Consider python-cli-architect first unless restrictions confirmed

**Complexity Trade-off** (IMPORTANT):

- ❌ **MORE development complexity** - Manual implementation of everything (argument parsing, output formatting, validation, error handling)
- ❌ **MORE code to write** - Build from scratch what libraries provide tested
- ❌ **Basic UX** - Limited formatting capabilities
- ✅ **Maximum portability** - The ONLY reason to choose this: runs anywhere Python exists without network access

**This agent is NOT simpler to use - it requires MORE work to build the same functionality. Choose it ONLY for portability, not for simplicity.**

**Note**: Only use this agent if deployment environment restrictions are confirmed. With PEP 723 + uv, python-cli-architect is preferred for better UX. ASK: "Will this run without internet access or where uv cannot be installed?" See [PEP 723 Reference](./PEP723.md) for details on when to use inline script metadata.

**Example tasks**:

- "Create a deployment script using only stdlib"
- "Build a config file validator that runs without dependencies"

## Agent Selection Decision Process

### For Scripts and CLI Tools

**Step 1: Default to python-cli-architect**

- Provides better UX (Rich components, progress bars, tables)
- PEP 723 + uv handles dependencies (still single file)
- Works in 99% of scenarios

**Step 2: Only use python-portable-script if:**

- User explicitly states "stdlib only" requirement
- OR deployment environment is confirmed restricted:
  - No internet access (airgapped network, embedded system)
  - uv cannot be installed (locked-down corporate environment)
  - Security policy forbids external dependencies

**Step 3: When uncertain, ASK:**

1. "Where will this script be deployed?"
2. "Does the environment have internet access?"
3. "Can uv be installed in the target environment?"
4. "Is stdlib-only a hard requirement, or would you prefer better UX?"

**Decision Tree**:

```text
Does the deployment environment have internet access?
├─ YES → Use python-cli-architect (default)
│         Single file + PEP 723 + uv = transparent dependencies
│
└─ NO → Is uv installable in the environment?
        ├─ YES → Use python-cli-architect (default)
        │         uv can cache dependencies for offline use
        │
        └─ NO → Use python-portable-script (exception)
                 Truly restricted environment requires stdlib-only
```

If answers indicate normal environment → python-cli-architect

If answers indicate restrictions → python-portable-script

**When in doubt**: Use python-cli-architect. PEP 723 + uv makes single-file scripts with dependencies just as portable as stdlib-only scripts for 99% of deployment scenarios.

### When to Use python-pytest-architect

**Use when**:

- Designing test suites from scratch
- Need comprehensive test coverage strategy
- Implementing advanced testing (property-based, mutation)
- Test architecture decisions

**Characteristics**:

- Modern pytest patterns
- pytest-mock exclusively (never unittest.mock)
- AAA pattern (Arrange-Act-Assert)
- Coverage and mutation testing

**Example tasks**:

- "Design test suite for payment processing module"
- "Create property-based tests for data validation"

### When to Use python-code-reviewer

**Use when**:

- Reviewing code for quality, patterns, standards
- Post-implementation validation
- Pre-merge code review
- Identifying improvement opportunities

**Characteristics**:

- Checks against modern Python standards
- Identifies anti-patterns
- Suggests improvements
- Validates against project patterns

**Example tasks**:

- "Review this PR for code quality"
- "Check if implementation follows best practices"

## Command Usage Patterns

### /modernpython

**Apply to**: Load as reference guide (optional file path argument for context)

**Use when**:

- As reference guide when writing new code
- Learning modern Python 3.11-3.14 features and patterns
- Understanding official PEPs (585, 604, 695, etc.)
- Identifying legacy patterns to avoid
- Finding modern alternatives for old code

**Note**: This is a reference document to READ, not an automated validation tool.

**Usage**:

```text
/modernpython
→ Loads comprehensive reference guide
→ Provides Python 3.11+ pattern examples
→ Includes PEP citations with WebFetch commands
→ Shows legacy patterns to avoid
→ Shows modern alternatives to use
→ Framework-specific guides (Typer, Rich, pytest)
```

**With file path**:

```text
/modernpython packages/mymodule.py
→ Loads guide for reference while working on specified file
→ Use guide to manually identify and refactor legacy patterns
```

### /shebangpython

**Apply to**: Individual Python scripts

**Use when**:

- Creating new standalone scripts
- Ensuring PEP 723 compliance
- Correcting script configuration

**Pattern**:

```text
/shebangpython scripts/deploy.py
→ Analyzes imports to determine dependency type
→ **Corrects shebang** to match script type (edits file if wrong)
→ **Adds PEP 723 metadata** if external dependencies detected (edits file)
→ **Removes PEP 723 metadata** if stdlib-only (edits file)
→ Sets execute bit if needed
→ Provides detailed verification report
```

## Integration with uv Skill

**Always use uv skill for**:

- Package management: `uv add <package>`
- Running scripts: `uv run script.py`
- Running tools: `uv run pytest`, `uv run ruff`
- Creating projects: `uv init`

**Never use**:

- `pip install` (use `uv add`)
- `python -m pip` (use `uv`)
- `pipenv`, `poetry` (use `uv`)

## Quality Gates

**CRITICAL**: The orchestrator MUST instruct agents to use the holistic-linting skill for all code quality checks.

**Every Python development task must pass**:

1. **Code quality**: Activate holistic-linting skill for linting, formatting, and type checking workflows
2. **Tests**: `uv run pytest` (>80% coverage)
3. **Standards**: `/modernpython` for modern patterns
4. **Script compliance**: `/shebangpython` for standalone scripts

**For critical code** (payments, auth, security):

- Coverage: >95%
- Mutation testing: `uv run mutmut run`
- Security scan: `uv run bandit -r packages/`

**CI Compatibility**: After local checks pass, verify CI requirements are met by checking CI config files for additional validators.

## Reference Example

**Complete working example**: `~/.claude/agents/python-cli-demo.py`

This file demonstrates all modern Python CLI patterns:

- PEP 723 inline script metadata with correct shebang
- Typer + Rich integration (Typer includes Rich, don't add separately)
- Modern Python 3.11+ patterns (StrEnum, Protocol, TypeVar, etc.)
- Proper type annotations with Annotated syntax
- Rich components (Console, Progress, Table, Panel)
- Async processing patterns
- Comprehensive docstrings

Use this as the reference implementation when creating CLI tools.

## Examples of Complete Workflows

### Example: Building a CLI Tool

```text
User: "Build a CLI tool to validate YAML configurations"

Orchestrator:
1. @agent-spec-architect
   "Design architecture for YAML validation CLI"
   → Component design, validation rules

2. @agent-python-pytest-architect
   "Create test suite for YAML validator"
   → tests/test_validator.py with fixtures

3. @agent-python-cli-architect
   "Implement YAML validator CLI with Typer based on tests"
   Reference: ~/.claude/agents/python-cli-demo.py for patterns
   → packages/validator.py with Typer+Rich UI

4. Validation:
   /shebangpython packages/validator.py
   Activate holistic-linting skill for code quality checks on packages/validator.py tests/
   uv run pytest

5. @agent-python-code-reviewer
   "Review validator implementation"
   → Quality check, improvements

6. Fix any issues and re-validate
```

### Example: Fixing a Bug

```text
User: "Fix bug where CSV parser fails on empty rows"

Orchestrator:
1. @agent-python-pytest-architect
   "Write test that reproduces CSV parser bug with empty rows"
   → tests/test_csv_parser.py::test_empty_rows (failing)

2. @agent-python-cli-architect
   "Fix CSV parser to handle empty rows, making test pass"
   → packages/csv_parser.py updated

3. Validation:
   uv run pytest  # Verify bug test passes
   uv run pytest  # Verify no regression

4. @agent-python-code-reviewer
   "Review bug fix and test"
   → Verify proper solution

5. Apply standards:
   /modernpython packages/csv_parser.py
   Activate holistic-linting skill for code quality checks on packages/csv_parser.py tests/
```

## Anti-Patterns to Avoid

### Don't: Write Python code as orchestrator

```text
❌ Orchestrator writes implementation directly
```

### Do: Delegate to appropriate agent

```text
✅ @agent-python-cli-architect writes implementation
✅ @agent-python-code-reviewer validates it
```

### Don't: Skip validation steps

```text
❌ Implement → Done (no tests, no review, no linting)
```

### Do: Follow complete workflow

```text
✅ Implement → Test → Review → Validate → Done
```

### Don't: Mix agent contexts

```cpp
❌ Ask python-portable-script to build Typer CLI
❌ Ask python-cli-architect to avoid all dependencies
```

### Do: Choose correct agent for context

```text
✅ python-cli-architect for user-facing CLI tools
✅ python-portable-script for stdlib-only scripts
```

## Summary

**Orchestration = Coordination, Not Implementation**

1. Choose the right agent for the task
2. Provide clear inputs and context
3. Chain agents for complex workflows (architect → test → implement → review)
4. Always validate with quality gates
5. Use commands for standards checking
6. Integrate with uv skill for package management

**Success = Right agent + Clear inputs + Proper validation**
