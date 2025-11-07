---
name: python-development
description: Comprehensive Python development skill covering modern tooling (uv, ruff, mypy, pytest), best practices, coding standards, library architecture, functional patterns, async programming, MicroPython, and production-grade development workflows. Use when writing Python code, managing dependencies, testing, type checking, creating CLI tools, designing libraries, or working with embedded Python systems.
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

## Quick Start

### Tier Selection

Choose your complexity level:

| Tier | Use Case | Setup |
|------|----------|-------|
| **Minimal** | Single-file utilities, scripts | Just Python 3.12+ |
| **Standard** | Multi-file projects, team work | Python + uv + ruff + mypy + pytest |
| **Full** | PyPI packages, production systems | Complete tooling ecosystem + CI/CD |

**Default to Standard** - it covers most use cases.

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
# Project initialization
uv init my-project && cd my-project

# Dependency management
uv add requests pandas numpy
uv add --dev pytest ruff mypy
uv remove requests
uv sync              # Sync with lockfile
uv lock --upgrade    # Update lockfile

# Running code
uv run python script.py
uv run pytest

# Virtual environments
uv venv
uv venv .venv --python 3.12
```

### Code Quality: ruff

```bash
# Check for issues
ruff check .

# Auto-fix issues
ruff check --fix .

# Format code
ruff format .
```

### Type Checking: mypy

```bash
# Type check entire project
mypy .

# Strict mode
mypy --strict .
```

### Testing: pytest

```bash
# Run all tests
pytest

# With coverage
pytest --cov

# Specific test
pytest tests/test_auth.py::test_login
```

## Project Structure

### Standard Layout

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
description = "Description of my project"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "requests>=2.31.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "ruff>=0.8.0",
    "mypy>=1.13.0",
]

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
warn_return_any = true
warn_unused_configs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
python_functions = "test_*"
```

## Writing Python Code

### Type Hints (Python 3.10+)

```python
from pathlib import Path

def process_data(
    items: list[str],
    config: dict[str, int],
    output_path: Path | None = None,
) -> list[int]:
    """Process items according to configuration.

    Args:
        items: List of items to process
        config: Configuration dictionary
        output_path: Optional path to write results

    Returns:
        List of processed integers

    Raises:
        ValueError: If items is empty
    """
    if not items:
        raise ValueError("items cannot be empty")

    results: list[int] = []
    for item in items:
        value = config.get(item, 0)
        results.append(value)

    if output_path is not None:
        output_path.write_text(str(results))

    return results
```

### Pure Functions + Immutability

```python
from dataclasses import dataclass

@dataclass(frozen=True)  # Immutable
class Point:
    x: float
    y: float

    def translate(self, dx: float, dy: float) -> "Point":
        return Point(self.x + dx, self.y + dy)  # New instance
```

### Structural Typing with Protocol

```python
from typing import Protocol

class Persistable(Protocol):
    def save(self) -> None: ...
    def load(self) -> None: ...

def backup(store: Persistable) -> None:  # Duck typing!
    store.save()
```

### Composition with Pipe

```python
from functools import reduce
from typing import Callable, Any

def pipe(*fns: Callable[[Any], Any]) -> Callable[[Any], Any]:
    return reduce(lambda f, g: lambda x: g(f(x)), fns)

# Usage: read left-to-right
process = pipe(parse, validate, transform, save)
result = process(data)
```

## Single-File Scripts (PEP 723)

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests>=2.31.0",
#     "rich>=13.0.0",
# ]
# ///
"""Script to fetch and display API data."""

import requests
from rich.console import Console

console = Console()

def main() -> None:
    """Fetch and display data from API."""
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()
    data = response.json()
    console.print(data)

if __name__ == "__main__":
    main()
```

## Testing with pytest

### Test Structure

```python
# tests/test_calculator.py
import pytest
from myproject.calculator import Calculator

class TestCalculator:
    """Test suite for Calculator class."""

    @pytest.fixture
    def calc(self) -> Calculator:
        """Provide a Calculator instance."""
        return Calculator()

    def test_add(self, calc: Calculator) -> None:
        """Test addition operation."""
        result = calc.add(2, 3)
        assert result == 5

    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (10, -5, 5),
    ])
    def test_add_parametrized(
        self,
        calc: Calculator,
        a: int,
        b: int,
        expected: int,
    ) -> None:
        """Test addition with multiple inputs."""
        assert calc.add(a, b) == expected

    def test_divide_by_zero(self, calc: Calculator) -> None:
        """Test division by zero raises error."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)
```

## Async Patterns

```python
import asyncio
import httpx

# TaskGroup: Structured concurrency (3.11+)
async def fetch_all(urls: list[str]) -> list[str]:
    async with httpx.AsyncClient() as client:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(client.get(url)) for url in urls]
    return [t.result().text for t in tasks]

# Async generator
async def async_range(n: int):
    for i in range(n):
        await asyncio.sleep(0.01)
        yield i

# Gather with error handling
async def fetch_safe(urls: list[str]):
    results = await asyncio.gather(
        *[fetch(url) for url in urls],
        return_exceptions=True
    )
    successes = [r for r in results if not isinstance(r, Exception)]
    errors = [r for r in results if isinstance(r, Exception)]
    return successes, errors
```

## Itertools Patterns

```python
from itertools import chain, batched, pairwise, groupby, accumulate, takewhile

# chain: Flatten iterables
list(chain([1, 2], [3, 4]))  # [1, 2, 3, 4]

# batched: Chunk into groups (3.12+)
list(batched("ABCDEFG", 3))  # [('A','B','C'), ('D','E','F'), ('G',)]

# pairwise: Consecutive pairs
list(pairwise("ABCD"))  # [('A','B'), ('B','C'), ('C','D')]

# accumulate: Running totals
list(accumulate([1, 2, 3, 4]))  # [1, 3, 6, 10]
```

## Functools Patterns

```python
from functools import reduce, partial, lru_cache

# reduce: Fold to single value
reduce(lambda acc, x: acc + x, [1, 2, 3, 4], 0)  # 10

# partial: Fix arguments
from operator import mul
double = partial(mul, 2)
double(5)  # 10

# lru_cache: Memoization
@lru_cache(maxsize=128)
def fib(n: int) -> int:
    return n if n < 2 else fib(n-1) + fib(n-2)
```

## Library Architecture

When designing Python libraries, follow these principles:

### Project Structure
- Use src/ layout for proper packaging
- Define public API in `__init__.py`
- Mark internal APIs with `_leading_underscore`
- Define `__all__` explicitly

### API Design
- Design for `import lib` then `lib.Thing()` pattern
- Use short, clear names
- Support duck typing where possible
- Prefer keyword arguments

### Quality Requirements
- Type hints on all public APIs
- Comprehensive docstrings (Google or NumPy style)
- Custom exception hierarchy defined
- >90% test coverage for public APIs
- No breaking changes in minor versions

See `references/architectural-principles.md` for comprehensive guidance.

## Exception Handling

```python
def get_user(id):
    return db.query(User, id)  # Errors surface naturally

def get_user_with_handling(id):
    try:
        return db.query(User, id)
    except ConnectionError:
        logger.warning("DB unavailable, using cache")
        return cache.get(f"user:{id}")  # Specific recovery action
```

Catch exceptions only when you have a specific recovery action. Let all other errors propagate.

## Anti-Patterns to Avoid

| Avoid | Do Instead |
|-------|------------|
| Mutable default args `def f(lst=[])` | `def f(lst=None)` |
| `requests.get` in async | `httpx.AsyncClient` |
| Classes for data bags | `@dataclass(frozen=True)` |
| Inheritance hierarchies | Protocols + composition |
| Mutating function args | Return new values |
| `try/except Exception` | Specific exception types |
| Blocking in async | `await asyncio.to_thread(fn)` |
| `from module import *` | Explicit imports |
| Bare `except:` | `except (ValueError, KeyError)` |

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

## Workflow Routing

| Task | Workflow File |
|------|---------------|
| "create python project", "new project", "uv init" | `workflows/Project.md` |
| "python script", "single file", "PEP 723" | `workflows/Script.md` |
| "run tests", "pytest", "coverage" | `workflows/Test.md` |
| "lint", "format", "ruff" | `workflows/Lint.md` |
| "type check", "mypy", "type hints" | `workflows/Type.md` |
| "dependencies", "uv add", "requirements" | `workflows/Deps.md` |
| "build package", "publish", "pypi" | `workflows/Package.md` |
| "monorepo", "workspace" | `workflows/Workspace.md` |

## Reference Files

This skill includes comprehensive reference documentation:

### Core Development
- `references/conventions-and-style.md` - PEP-8, Ruff, Black, naming
- `references/project-structure.md` - src/ layout, imports, organization
- `references/dependency-management.md` - uv, Poetry, pip, venv
- `references/testing-methodology.md` - pytest, fixtures, coverage
- `references/type-hints.md` - Modern typing, mypy, protocols
- `references/code-quality-tools.md` - Ruff, mypy, Bandit setup

### Advanced Topics
- `references/async-patterns.md` - asyncio, TaskGroup, structured concurrency
- `references/security-best-practices.md` - OWASP, validation, scanning
- `references/performance-optimization.md` - Profiling, patterns, Cython
- `references/packaging-distribution.md` - pyproject.toml, PyPI, versioning
- `references/common-libraries.md` - Standard library + ecosystem essentials
- `references/docstrings-documentation.md` - PEP-257, Sphinx

### Library Architecture
- `references/architectural-principles.md` - SOLID, API design, extensibility
- `references/pep-standards.md` - PEP-8, PEP-484, PEP-517/518, etc.
- `references/exception-handling.md` - Exception patterns for CLI/Typer
- `references/PEP723.md` - Inline script metadata

### Mypy Documentation
- `references/mypy-docs/generics.rst` - Generic types
- `references/mypy-docs/protocols.rst` - Structural typing
- `references/mypy-docs/type_narrowing.rst` - Type narrowing
- `references/mypy-docs/typed_dict.rst` - TypedDict patterns
- `references/mypy-docs/additional_features.rst` - Advanced features

### Modern Modules Library
- `references/modern-modules.md` - 50+ library guides
- `references/modern-modules/*.md` - Individual module deep-dives

### UV Documentation
- `references/uv.md` - Complete UV reference

### MicroPython/Embedded
- `references/micropython_async.md` - Async patterns for embedded
- `references/display_rendering.md` - Memory-efficient rendering
- `references/presto_hardware.md` - RP2350/Pimoroni hardware reference

### Cookbooks
- `cookbook/patterns.md` - Functional patterns & composition
- `cookbook/async.md` - Async/await deep dive
- `cookbook/testing.md` - pytest patterns & fixtures
- `cookbook/design-patterns.md` - Builder, DI, Factory, Strategy
- `cookbook/modern.md` - Python 3.8-3.14 key features

## Assets and Templates

- `assets/pyproject.toml.template` - Production-ready pyproject.toml
- `assets/pyproject-toml-template.toml` - Alternative template
- `assets/README.md.template` - Comprehensive README template
- `assets/CONTRIBUTING.md.template` - Contribution guide template
- `assets/project-structure.txt` - Recommended package organization
- `assets/test-structure.txt` - Recommended test organization
- `assets/example-exceptions.py` - Custom exception hierarchy pattern
- `assets/example-config.py` - Configuration pattern example
- `assets/version.py` - Version management pattern
- `assets/hatch_build.py` - Build hook for binary handling

## Scripts

- `scripts/setup-project.sh` - Initialize new Python project
- `scripts/check-code-quality.sh` - Run all quality checks
- `scripts/mqtt_client.py` - MQTT client for IoT
- `scripts/touch_handler.py` - Touch input handling
- `scripts/rgb_backlight.py` - RGB LED control
- `scripts/ble_gatt_server.py` - BLE GATT server

## Official Documentation

- Python: https://docs.python.org/
- uv: https://docs.astral.sh/uv/
- Ruff: https://docs.astral.sh/ruff/
- mypy: https://mypy-lang.org/
- pytest: https://docs.pytest.org/
- PEPs: https://peps.python.org/

## Source Skills

This curated skill merges content from:
1. Python Development Best Practices
2. Python Coding Standards
3. UV: Ultra-Fast Python Package Manager
4. Opinionated Python Development Skill
5. Python Development Skill
6. Python Development (Functional-First)
7. Python Library Architect
8. RP2350/Pimoroni Presto MicroPython Development



