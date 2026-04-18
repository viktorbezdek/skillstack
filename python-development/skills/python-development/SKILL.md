---
name: python-development
description: Python development — use when the user works with .py files, pyproject.toml, uv, ruff, mypy, pytest, async/await, MicroPython, CLI tools, or PyPI publishing. Covers modern tooling, best practices, library architecture, functional patterns, and production workflows. NOT for TypeScript or JavaScript development (use typescript-development), NOT for React component patterns (use react-development).
---

# Python Development - Comprehensive Skill

Expert guidance for modern Python development (Python 3.11-3.14+), covering everything from simple scripts to production-grade systems, library architecture, and embedded development.

## When to Use This Skill

Activate this skill when:
- Working with `.py` files, `pyproject.toml`, or `uv.lock`
- Writing, testing, or reviewing Python code
- Managing Python dependencies or virtual environments
- Using commands like `uv`, `pytest`, `ruff`, or `mypy`
- Building CLI applications with Typer/Click
- Designing Python libraries or packages
- Working with async/await patterns
- Developing for embedded systems (MicroPython, RP2350)
- Setting up CI/CD for Python projects
- Publishing packages to PyPI

## When NOT to Use This Skill

- **TypeScript or JavaScript development** → use `typescript-development`
- **React component patterns or hooks** → use `react-development`
- **TDD methodology (Red-Green-Refactor cycle)** → use `test-driven-development` (this skill covers pytest patterns but not the full TDD workflow)
- **Django/Flask framework-specific patterns** → this skill covers Python fundamentals; dedicated framework plugins provide deeper coverage

## Decision Trees

### Tier Selection

```
What are you building?
  │
  ├─ Single-file script, one-off utility, quick data processing
  │   └─ MINIMAL tier: PEP 723 inline metadata, no project scaffolding
  │
  ├─ Multi-file project, team development, anything with tests
  │   └─ STANDARD tier (default): src/ layout + uv + ruff + mypy + pytest
  │
  └─ PyPI package, production system requiring CI/CD
      └─ FULL tier: Complete tooling + bandit + CI/CD + release workflow
```

**Default to Standard** — it covers most use cases.

### Async vs Sync Decision

```
Does the task involve I/O-bound operations (HTTP, DB, file, network)?
  │
  ├─ No → Use synchronous code (simpler, easier to debug)
  │
  └─ Yes → Are operations concurrent (many requests at once)?
      │
      ├─ No → Simple async/await with httpx.AsyncClient
      │
      └─ Yes → asyncio.Semaphore per resource + httpx.AsyncClient
               with connection pooling + retry logic
```

### Protocol vs ABC Decision

```
Do you need structural subtyping (duck typing with type safety)?
  │
  ├─ Yes → Protocol
  │   └─ Enables dependency injection, avoids inheritance coupling
  │
  └─ No → Do you need runtime type checking or enforced method implementation?
      │
      ├─ Yes → ABC with @abstractmethod
      │
      └─ No → Protocol (lighter weight, preferred default)
```

### Library vs Application Architecture Decision

```
Will this code be imported by other projects?
  │
  ├─ Yes → Library architecture:
  │   - Protocol-based API surface
  │   - py.typed marker
  │   - Minimal public exports (__all__)
  │   - Stable deprecation policy
  │   - pyproject.toml with [project.optional-dependencies]
  │
  └─ No → Application architecture:
      - Direct implementation (no Protocol overhead)
      - Simpler project structure
      - pyproject.toml with [project.scripts]
```

## Quick Start

### Standard Project Setup

```bash
# Install Python 3.12+ and uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create new project
uv init my-project
cd my-project

# Add dependencies
uv add requests pydantic httpx

# Add dev dependencies
uv add --dev pytest pytest-cov ruff mypy

# Run quality checks
uv run ruff check .          # Linting
uv run ruff format .         # Formatting
uv run mypy .                # Type checking
uv run pytest --cov          # Tests with coverage
```

## Core Principles

1. **Use uv for everything**: 10-100x faster than pip, all-in-one tool
2. **Type hints everywhere**: Use type annotations for all functions and classes
3. **Ruff for quality**: Single tool for linting and formatting (replaces Black, flake8, isort)
4. **Test with pytest**: Comprehensive tests with fixtures and parametrization
5. **Lock dependencies**: Always maintain `uv.lock` for reproducible builds
6. **PEP 723 for scripts**: Use inline script metadata for single-file scripts

## Modern Python Toolchain (2024-2025)

### Package Management: uv

```bash
uv init my-project && cd my-project   # Initialize
uv add requests pandas numpy           # Add deps
uv add --dev pytest ruff mypy          # Add dev deps
uv sync                                # Sync with lockfile
uv lock --upgrade                      # Update lockfile
uv run python script.py                # Run code
uv run pytest                          # Run tests
```

### Code Quality: ruff

```bash
ruff check .         # Check for issues
ruff check --fix .   # Auto-fix issues
ruff format .        # Format code
```

### Type Checking: mypy

```bash
mypy .          # Type check entire project
mypy --strict . # Strict mode
```

## Project Structure

```
myproject/
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_main.py
│   └── test_utils.py
├── docs/
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

### pyproject.toml Configuration

```toml
[project]
name = "myproject"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["requests>=2.31.0"]

[project.optional-dependencies]
dev = ["pytest>=8.0.0", "ruff>=0.8.0", "mypy>=1.13.0"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W", "B", "Q"]

[tool.mypy]
python_version = "3.11"
strict = true

[tool.pytest.ini_options]
testpaths = ["tests"]
```

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| **Mutable default args** `def f(lst=[])` | Default value is shared across all calls; mutations persist unexpectedly | `def f(lst: list \| None = None)` then `lst = lst or []` inside |
| **`requests.get` in async** | Blocks the event loop; all concurrent tasks stall | `httpx.AsyncClient` for async HTTP; `requests` only in sync code |
| **Classes for data bags** | Boilerplate `__init__`, mutable by default, no equality | `@dataclass(frozen=True)` for immutable value objects, or `NamedTuple` for lightweight records |
| **Deep inheritance hierarchies** | Tight coupling, fragile base class, hard to test | `Protocol` + composition; define behavior by what it does, not what it is |
| **Mutating function args** | Side effects make code unpredictable and hard to test | Return new values; use frozen dataclasses; prefer pure functions |
| **`try/except Exception`** | Swallows all errors including KeyboardInterrupt, SystemExit | Catch specific types: `except (ValueError, KeyError)` |
| **Blocking in async** | `time.sleep()`, `requests.get()`, `subprocess.run()` freeze the event loop | `await asyncio.to_thread(fn)` or `asyncio.sleep()` for non-blocking alternatives |
| **`from module import *`** | Pollutes namespace, makes dependencies invisible, breaks linters | Explicit imports: `from module import ClassA, func_b` |
| **Bare `except:`** | Catches everything including SystemExit/KeyboardInterrupt; hides bugs | `except (SpecificError, AnotherError):` |
| **Using `List[str]` etc.** | Legacy typing; deprecated since Python 3.9 | Use modern syntax: `list[str]`, `dict[str, int]`, `tuple[int, ...]` |
| **Ignoring mypy errors** | Type errors at compile time become runtime crashes | Fix the type; use `# type: ignore[specific-code]` with comment explaining why |
| **Testing with production URLs** | Tests hit real APIs, flaky, slow, depend on network | Mock HTTP calls with `pytest-httpx` or `respx`; test against fixtures |

## Quality Gates

Every Python task must pass:

1. **Format-first**: `uv run ruff format .`
2. **Linting**: `uv run ruff check .`
3. **Type checking**: `uv run mypy .`
4. **Tests**: `uv run pytest` (>80% coverage)
5. **Modern patterns**: No legacy typing (use `list[str]` not `List[str]`)

For critical code (payments, auth, security):
- Coverage >95%
- Security scan: `uv run bandit -r src/`

See [Extended Patterns](references/extended-patterns.md) for detailed code examples, testing patterns, async patterns, itertools/functools usage, library architecture, workflow routing, and complete reference file listings.

## Official Documentation

- Python: https://docs.python.org/
- uv: https://docs.astral.sh/uv/
- Ruff: https://docs.astral.sh/ruff/
- mypy: https://mypy-lang.org/
- pytest: https://docs.pytest.org/
- PEPs: https://peps.python.org/
