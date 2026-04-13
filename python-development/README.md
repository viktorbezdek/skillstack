# Python Development

> **v1.1.24** | Development | 26 iterations

Comprehensive Python development skill covering modern tooling (uv, ruff, mypy, pytest), best practices, coding standards, library architecture, functional patterns, async programming, MicroPython, and production-grade development workflows.

## What Problem Does This Solve

Python's ecosystem has modernized significantly -- pip, Black, flake8, and isort have been superseded by faster, simpler alternatives -- but most developers and LLMs are still generating code with outdated toolchains and legacy patterns. Inconsistent dependency management, missing type annotations, mutable default arguments, bare excepts, and poor project structure cause builds that do not reproduce, type errors that slip to production, and codebases that resist refactoring. This skill encodes the current best practices for Python 3.11+ with the modern toolchain (uv, ruff, mypy, pytest), from single-file scripts to PyPI-published libraries and MicroPython embedded systems.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Set up a new Python project with proper tooling" | Standard project setup using uv init, ruff, mypy, and pytest with a complete pyproject.toml and src/ layout |
| "My async code is blocking the event loop" | Async patterns with httpx.AsyncClient, asyncio.to_thread(), and the anti-patterns that cause blocking |
| "How do I structure a Python library for PyPI publishing?" | Full project layout (src/ layout), pyproject.toml with Hatchling build system, and CI/CD publishing workflow |
| "Help me add type checking to my Python codebase" | mypy configuration for strict mode, modern annotation syntax (list[str] not List[str]), and Protocol-based interfaces |
| "My Python code passes tests but has quality issues" | Five-gate quality checklist: ruff format, ruff check, mypy strict, pytest with >80% coverage, bandit for security-critical code |

## When NOT to Use This Skill

- TypeScript or JavaScript development -- use [typescript-development](../typescript-development/) instead
- React component patterns -- use [react-development](../react-development/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install python-development@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the python-development skill to set up a new CLI tool with Typer
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `python`
- `uv`
- `ruff`
- `mypy`
- `pytest`
- `fastapi`

## What's Inside

This plugin includes a skill, slash commands, reference documentation, cookbooks, workflow guides, scripts, and templates.

### Skill

| Component | Purpose |
|---|---|
| `SKILL.md` | Core principles, modern toolchain reference (uv, ruff, mypy), project structure, anti-pattern table, quality gates |
| `references/extended-patterns.md` | Detailed code examples for type hints, testing, async, itertools/functools, library architecture |
| `references/async-patterns.md` | asyncio patterns, event loop management, httpx async client usage |
| `references/conventions-and-style.md` | PEP 8 conventions, naming rules, import ordering |
| `references/dependency-management.md` | uv workflows, lockfile management, virtual environment handling |
| `references/exception-handling.md` | Exception hierarchies, custom exceptions, context-appropriate catching |
| `references/type-hints.md` | Modern type annotation patterns, generics, Protocols, TypeVar |
| `references/testing-methodology.md` | pytest patterns, fixtures, parametrization, coverage enforcement |
| `references/packaging-distribution.md` | PyPI publishing, build systems, versioning |
| `references/security-best-practices.md` | bandit scanning, secret management, input validation |
| `references/performance-optimization.md` | Profiling, caching, lazy evaluation, memory optimization |
| `references/project-structure.md` | src/ layout conventions, monorepo patterns |
| `references/functional-reference.md` | Functional programming patterns in Python |
| `references/uv.md` | Comprehensive uv command reference |
| `cookbook/` | Recipes for async, design patterns, modern Python, testing, and common patterns |

### Slash Commands

| Command | Purpose |
|---|---|
| `create-feature-task` | Set up a structured feature development task with phases, tracking, and documentation |
| `use-command-template` | Generate new slash commands following established patterns |
| `analyze-test-failures` | Investigate failing tests with a balanced approach -- distinguishes test bugs from real bugs |
| `comprehensive-test-review` | Full test review following a standardized checklist |
| `test-failure-mindset` | Set balanced investigative approach for test failure analysis |

### Scripts and Tools

| Component | Purpose |
|---|---|
| `scripts/setup-project.sh` | Project scaffolding automation |
| `scripts/check-code-quality.sh` | Quality gate runner (ruff + mypy + pytest) |
| `tools/python-check` | Quick Python code validation |
| `tools/python-lint` | Linting wrapper |
| `workflows/` | Guided workflows for dependencies, linting, packaging, project setup, scripting, testing, type checking, and workspace management |

## Usage Scenarios

**Scenario 1 -- Greenfield project setup.** You are starting a new Python CLI tool. The skill provides the uv init sequence, generates a pyproject.toml with ruff/mypy/pytest configuration, scaffolds the src/ layout, and sets up quality gates so every commit passes format, lint, type-check, and test checks.

**Scenario 2 -- Modernizing a legacy codebase.** Your project still uses pip, Black, flake8, and isort with `Optional[List[str]]` type annotations. The skill guides migration to uv for package management, ruff as a single replacement for Black+flake8+isort, and modern annotation syntax (`list[str] | None`), preserving all existing functionality.

**Scenario 3 -- Debugging async issues.** Your FastAPI endpoint is hanging under load because a synchronous library call is blocking the event loop. The skill identifies the anti-pattern (using `requests.get` in async context) and provides the fix (`httpx.AsyncClient` or `asyncio.to_thread()` for legacy sync calls).

**Scenario 4 -- Publishing a library to PyPI.** You have a utility library ready for distribution. The skill provides the Hatchling build system setup, version management, README configuration for PyPI, and the `uv build && uv publish` workflow with CI/CD integration.

**Scenario 5 -- Embedded MicroPython development.** You are writing firmware for an RP2350 board. The skill includes MicroPython-specific patterns, async references for constrained environments, and example scripts for BLE GATT servers, MQTT clients, and touch handlers.

## Related Skills

- **[Test Driven Development](../test-driven-development/)** -- Red-Green-Refactor methodology with pytest-specific TDD patterns.
- **[Testing Framework](../testing-framework/)** -- Framework selection and test infrastructure setup across multiple languages.
- **[Api Design](../api-design/)** -- Design REST and GraphQL APIs that your Python services expose.
- **[Docker Containerization](../docker-containerization/)** -- Containerize Python applications with multi-stage builds.
- **[CI/CD Pipelines](../cicd-pipelines/)** -- Automate quality gates and deployment for Python projects.

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 52 production-grade plugins for Claude Code.
