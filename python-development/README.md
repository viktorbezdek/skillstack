# Python Development

> **v1.1.24** | Development | 26 iterations

> Production-grade Python development guidance covering modern tooling (uv, ruff, mypy, pytest), best practices, library architecture, async patterns, MicroPython, and complete development workflows.

## The Problem

Python's ecosystem moves fast, and best practices from two years ago are already outdated. Teams still initialize projects with `pip install` and `requirements.txt` when uv is 10-100x faster. They write untyped code and catch type errors in production instead of at build time. They use Black, flake8, and isort as three separate tools when ruff replaces all of them in a single pass. They structure projects without `src/` layout and hit import collisions in CI. They write tests without fixtures or parametrization and end up with fragile, duplicated test code.

The knowledge is scattered across dozens of PEPs, tool documentation sites, and blog posts. A developer starting a new Python project has to make fifty small decisions -- project layout, dependency management, linting rules, type checking strictness, test structure, async patterns, packaging format -- and getting any one of them wrong creates technical debt that compounds over the project's lifetime. Senior developers carry this knowledge in their heads; junior developers learn it through painful mistakes over months or years.

For specialized domains like embedded development (MicroPython on RP2350) or library architecture for PyPI publishing, the gap is even wider. The patterns that work for application development actively harm library design, and MicroPython's async model has critical differences from CPython that cause subtle bugs if you treat them the same way.

## The Solution

This plugin encodes production-grade Python expertise into a skill that activates whenever you work with `.py` files, `pyproject.toml`, uv, ruff, mypy, or pytest. It provides opinionated but well-reasoned defaults for every decision point in Python development: uv for dependency management, ruff for linting and formatting, mypy in strict mode for type checking, pytest with fixtures and parametrization for testing, and `src/` layout for project structure.

The skill covers three tiers of complexity -- Minimal (single-file scripts with PEP 723 inline metadata), Standard (multi-file projects with full toolchain), and Full (PyPI packages with CI/CD pipelines) -- and defaults to Standard because it fits most use cases. It enforces quality gates before any code is considered complete: format with ruff, lint, type-check, and test with >80% coverage.

Beyond the core methodology, 29 reference files provide deep guidance on specific topics: async patterns, exception handling, dependency management, security best practices, performance optimization, packaging for PyPI, MicroPython async patterns for embedded hardware, and more. The skill loads these on demand -- you get the right depth for your specific question without being overwhelmed by irrelevant detail.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Project setup takes 30+ minutes of decisions about tools, layout, and configuration | `uv init` + opinionated `pyproject.toml` with ruff, mypy, and pytest configured in under 5 minutes |
| Three separate tools for linting, formatting, and import sorting (Black + flake8 + isort) | Single tool: ruff handles linting, formatting, and import sorting in one pass |
| Type errors discovered in production or during code review | mypy strict mode catches type errors at development time with full annotation coverage |
| Tests without fixtures or parametrization -- duplicated setup code and fragile assertions | pytest fixtures, parametrization, and conftest patterns that produce maintainable, DRY test suites |
| Dependency management with pip and manually maintained requirements.txt | uv manages dependencies 10-100x faster with lockfile-based reproducible builds |
| Mutable default arguments, bare except clauses, and blocking calls in async code | Anti-pattern detection catches common Python mistakes before they ship |
| Library architecture designed like application code -- coupling, leaky abstractions, missing `py.typed` | Dedicated library architecture guidance covering API surface, protocols, packaging, and PyPI publishing |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install python-development@skillstack
```

### Verify installation

After installing, test with:

```
Set up a new Python project with uv, ruff, mypy, and pytest
```

The skill should activate and walk you through project initialization with a properly configured `pyproject.toml`.

## Quick Start

1. **Install** the plugin using the commands above
2. **Start a new project** by saying: `Create a Python CLI tool that fetches weather data from an API`
3. The skill **scaffolds** the project with `uv init`, `src/` layout, and a configured `pyproject.toml` including ruff, mypy, and pytest settings
4. As you develop, **ask for help** naturally: `Add error handling to this HTTP client` or `Write tests for the weather parser`
5. Before shipping, the skill **enforces quality gates**: `uv run ruff format . && uv run ruff check . && uv run mypy . && uv run pytest --cov`

## What's Inside

This is a single-skill plugin with an extensive reference layer covering 29 specialized topics.

| Component | Purpose |
|---|---|
| `SKILL.md` | Core methodology -- tier selection, project setup, toolchain configuration, anti-patterns, quality gates |
| `templates/test-template.py` | Standardized pytest test file template with fixtures and parametrization |
| 29 reference files | Deep guidance on specialized topics (loaded on demand) |

**Eval coverage:** 13 trigger evaluation cases, 3 output evaluation cases.

**Key references:**

| Reference | Topic |
|---|---|
| `extended-patterns.md` | Detailed code examples, testing patterns, async patterns, itertools/functools |
| `testing-methodology.md` | Comprehensive pytest methodology -- fixtures, parametrization, coverage |
| `async-patterns.md` | Async/await patterns, event loops, concurrency with asyncio and httpx |
| `architectural-principles.md` | Library architecture, API surface design, protocols over inheritance |
| `type-hints.md` | Modern type annotations, generics, Protocol, TypeVar, overloads |
| `conventions-and-style.md` | PEP 8, naming conventions, import organization, code structure |
| `code-quality-tools.md` | Ruff configuration, mypy settings, bandit security scanning |
| `dependency-management.md` | uv workflows, lockfiles, optional dependencies, version constraints |
| `exception-handling.md` | Exception hierarchies, CLI error handling with Typer, retry patterns |
| `performance-optimization.md` | Profiling, caching, generators, C extensions, memory optimization |
| `security-best-practices.md` | Input validation, secrets management, SQL injection prevention |
| `packaging-distribution.md` | PyPI publishing, build backends, versioning, `py.typed` markers |
| `project-structure.md` | `src/` layout, monorepo patterns, configuration files |
| `pep-standards.md` | Quick reference for key PEPs (723, 695, 604, 585, etc.) |
| `PEP723.md` | Inline script metadata for single-file scripts |
| `micropython_async.md` | MicroPython async patterns for RP2350 embedded development |
| `presto_hardware.md` | Pimoroni Presto hardware reference for embedded projects |
| `display_rendering.md` | Display rendering on RP2350 hardware |
| `common-libraries.md` | Curated library recommendations by domain |
| `functional-reference.md` | Functional programming patterns, itertools, functools |
| `docstrings-documentation.md` | Docstring standards, Sphinx/MkDocs integration |
| `uv.md` | Comprehensive uv command reference |

### python-development

**What it does:** Activates whenever you work with Python files, pyproject.toml, uv, ruff, mypy, or pytest. Provides expert guidance on project setup, code patterns, testing, async development, library architecture, and the complete modern Python toolchain. Automatically selects the right tier of complexity (Minimal, Standard, or Full) based on your project.

**Try these prompts:**

```
Set up a new Python project with uv, ruff, and pytest -- I want strict type checking from the start
```

```
This function uses mutable default arguments and bare except clauses -- fix the anti-patterns
```

```
Write parametrized pytest tests for this data validation module
```

```
I need to make 500 concurrent HTTP requests -- show me the async pattern with httpx
```

```
My Python library needs to be published to PyPI with proper packaging -- walk me through the setup
```

```
Convert this synchronous Flask endpoint to async using FastAPI
```

## Real-World Walkthrough

You are building a CLI tool that aggregates metrics from multiple cloud providers (AWS CloudWatch, GCP Monitoring, Azure Monitor) and outputs a unified cost report. The tool needs to handle API rate limits, authenticate with each provider, and produce both JSON and CSV output. You have a rough script that works for AWS but it is a single 400-line file with no tests.

You open Claude Code in the project directory and say:

```
I have a rough Python script that pulls AWS CloudWatch metrics. I need to turn it into a proper CLI tool that also supports GCP and Azure. Help me structure this as a real project.
```

The skill activates and starts with project setup. It runs `uv init cloud-metrics && cd cloud-metrics` and creates the `src/` layout with a properly configured `pyproject.toml`. The configuration includes ruff with rules `["E", "F", "I", "N", "W", "B", "Q"]`, mypy in strict mode, and pytest targeting the `tests/` directory. It adds core dependencies (`httpx`, `typer`, `pydantic`, `rich`) and dev dependencies (`pytest`, `pytest-cov`, `pytest-asyncio`, `ruff`, `mypy`).

The skill suggests a module structure based on the architectural principles reference:

```
src/cloud_metrics/
    __init__.py
    cli.py           # Typer CLI entry point
    providers/
        __init__.py
        base.py       # Protocol defining provider interface
        aws.py
        gcp.py
        azure.py
    models.py         # Pydantic models for metrics data
    formatters.py     # JSON and CSV output formatters
    rate_limiter.py   # Token bucket rate limiter
```

You ask about the provider interface design:

```
Should I use an abstract base class or a Protocol for the provider interface?
```

The skill recommends `Protocol` over `ABC` -- it enables structural subtyping (duck typing with type safety), avoids inheritance coupling, and works better with dependency injection. It shows a `MetricsProvider` protocol with `authenticate()`, `fetch_metrics()`, and `get_cost_report()` methods, all properly typed with return type annotations.

Next, you tackle the async HTTP problem:

```
Each provider API has different rate limits. How do I make 50 concurrent requests to AWS while limiting GCP to 10?
```

The skill loads the async-patterns reference and shows you a pattern using `asyncio.Semaphore` per provider combined with `httpx.AsyncClient`. It structures the code as an async context manager that handles connection pooling, automatic retries with exponential backoff, and per-provider concurrency limits. It warns against a common anti-pattern: using `requests.get` in async code, which blocks the event loop.

You build the AWS provider and want to test it:

```
Write tests for the AWS provider -- I need to mock the HTTP calls
```

The skill produces a test file following the template structure. It creates a `conftest.py` with shared fixtures: a mock `httpx.AsyncClient`, sample CloudWatch response data as frozen dataclasses, and a configured `MetricsProvider` instance. The tests use `pytest.mark.asyncio`, parametrize across different metric types (CPU, memory, network), and mock the HTTP client at the module level where it is imported (not where it is defined). Each test follows the `test_<function>_<scenario>_<expected>` naming convention.

After implementing all three providers, you run the quality gates:

```bash
uv run ruff format .          # Formats 12 files
uv run ruff check .           # 0 issues
uv run mypy .                 # Success: no issues found
uv run pytest --cov           # 47 passed, 92% coverage
```

Everything passes. You then add the Typer CLI entry point with `--provider`, `--format`, and `--date-range` options. The skill shows the exception handling pattern from the reference: a top-level `app_callback` that catches provider-specific exceptions and translates them into user-friendly error messages with `rich` formatting, avoiding raw tracebacks in the terminal.

The final step is packaging:

```
I want to publish this to our internal PyPI registry
```

The skill references the packaging guide and walks you through adding `[project.scripts]` to `pyproject.toml` for the CLI entry point, creating a `py.typed` marker for downstream type checking, choosing hatchling as the build backend, and configuring the internal registry URL in `uv.toml`. It produces a CI/CD checklist: version bump, changelog update, `uv build`, `uv publish --index internal`.

## Usage Scenarios

### Scenario 1: Modernizing a legacy Python project

**Context:** You inherited a Python 3.8 project that uses `requirements.txt`, Black, flake8, isort, and unittest. You want to modernize the toolchain without rewriting the code.

**You say:** `Help me migrate this project from pip/requirements.txt to uv and replace Black+flake8+isort with ruff`

**The skill provides:**
- Step-by-step migration from `requirements.txt` to `pyproject.toml` with uv
- Ruff configuration that matches the existing Black, flake8, and isort settings
- Migration path from unittest to pytest (keeping existing tests working during transition)
- Updated CI/CD configuration for the new toolchain

**You end up with:** A modernized project with uv lockfile, single-tool linting/formatting via ruff, and faster CI builds -- without changing any production code.

### Scenario 2: Building an async data pipeline

**Context:** You need to fetch data from 5 REST APIs concurrently, transform it, and load it into a PostgreSQL database. The APIs have different rate limits and authentication methods.

**You say:** `I need to build an async data pipeline that fetches from 5 APIs concurrently with different rate limits`

**The skill provides:**
- Async architecture using `httpx.AsyncClient` with per-source `asyncio.Semaphore`
- Pydantic models for data validation between fetch and transform stages
- Connection pooling patterns for PostgreSQL with asyncpg
- Error handling with per-source retry logic and dead-letter queuing

**You end up with:** A typed, tested async pipeline with proper rate limiting, error isolation per source, and >80% test coverage using mocked HTTP responses.

### Scenario 3: Designing a Python library for PyPI

**Context:** You have utility functions used across three internal projects. You want to extract them into a proper library and publish to PyPI.

**You say:** `I want to turn these utility functions into a proper Python library and publish it to PyPI`

**The skill provides:**
- Library-specific project structure (different from application structure)
- Protocol-based API surface design instead of class inheritance
- `py.typed` marker and strict mypy configuration for downstream type checking
- Build, version, and publish workflow with hatchling and uv

**You end up with:** A well-structured, typed, documented library with proper packaging metadata, ready for `uv publish`.

### Scenario 4: MicroPython embedded development

**Context:** You are developing firmware for a Pimoroni Presto board (RP2350) that needs to read sensors, update a display, and communicate over WiFi -- all concurrently using MicroPython's async model.

**You say:** `I need async patterns for MicroPython on RP2350 -- sensor reading, display updates, and WiFi all running concurrently`

**The skill provides:**
- MicroPython-specific async patterns (different from CPython's asyncio)
- Hardware-aware task scheduling for sensor polling and display rendering
- WiFi connection management with reconnection logic
- Memory-efficient patterns for constrained embedded environments

**You end up with:** A working async firmware architecture that handles concurrent hardware tasks without blocking, optimized for RP2350's memory constraints.

## Ideal For

- **Python developers starting new projects** -- the opinionated defaults (uv + ruff + mypy + pytest) eliminate thirty minutes of toolchain decisions and produce a consistent, production-ready setup
- **Teams modernizing legacy Python codebases** -- migration guidance from pip/requirements.txt to uv, from unittest to pytest, from Black+flake8 to ruff
- **Engineers building async services and data pipelines** -- async patterns, concurrency control, and httpx usage tuned for real-world rate-limited API interactions
- **Library authors publishing to PyPI** -- architecture guidance specific to libraries (not applications) with proper typing, packaging, and API surface design
- **Embedded developers using MicroPython** -- RP2350-specific async patterns and hardware references that account for MicroPython's differences from CPython

## Not For

- **TypeScript or JavaScript development** -- use [typescript-development](../typescript-development/) for TS/JS projects with Node.js, Bun, or Deno
- **React component patterns and hooks** -- use [react-development](../react-development/) for React-specific architecture, state management, and component design
- **Test methodology and TDD workflow** -- use [test-driven-development](../test-driven-development/) for the Red-Green-Refactor cycle; this skill covers pytest patterns but not the full TDD methodology

## How It Works Under the Hood

The plugin is a single skill with progressive disclosure through 29 reference files organized by topic. The SKILL.md body contains the essential methodology: tier selection, project setup, toolchain configuration, anti-patterns, and quality gates. This covers the core 80% of Python development needs.

When you ask about a specific topic -- async patterns, library packaging, exception handling, MicroPython -- the skill loads the relevant reference file on demand. This keeps the initial context lean while providing deep expertise when needed. The reference layer covers:

- **Toolchain:** uv, ruff, mypy configuration and usage
- **Patterns:** async, functional, exception handling, performance optimization
- **Architecture:** project structure, library design, API surface, protocols
- **Quality:** testing methodology, security practices, code quality tools
- **Packaging:** PyPI publishing, build backends, versioning
- **Specialized:** MicroPython async, RP2350 hardware, display rendering

A test template (`templates/test-template.py`) provides a standardized starting point for new test files with fixtures, parametrization, and naming conventions.

## Related Plugins

- **[Test-Driven Development](../test-driven-development/)** -- The Red-Green-Refactor methodology for writing tests before implementation code
- **[Testing Framework](../testing-framework/)** -- Test infrastructure setup and framework selection across multiple languages
- **[TypeScript Development](../typescript-development/)** -- The TypeScript equivalent of this plugin for TS/JS projects
- **[Debugging](../debugging/)** -- Systematic debugging methodology for root cause analysis
- **[CI/CD Pipelines](../cicd-pipelines/)** -- Pipeline configuration for automated testing and deployment

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
