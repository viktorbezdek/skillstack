# Python Development - Extended Patterns & Examples

Detailed code examples, testing patterns, and advanced topics extracted from the core skill.

## Writing Python Code - Detailed Examples

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

## Scripts

- `scripts/setup-project.sh` - Initialize new Python project
- `scripts/check-code-quality.sh` - Run all quality checks
- `scripts/mqtt_client.py` - MQTT client for IoT
- `scripts/touch_handler.py` - Touch input handling
- `scripts/rgb_backlight.py` - RGB LED control
- `scripts/ble_gatt_server.py` - BLE GATT server

---

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
