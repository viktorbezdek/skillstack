# Reference Guide

## Data Structure Selection

| Need | Data Structure |
|------|----------------|
| Ordered, mutable sequence | `list` |
| Immutable sequence | `tuple` |
| Fast lookup by key | `dict` |
| Membership testing | `set` / `frozenset` |
| FIFO queue | `collections.deque` |
| Priority queue | `heapq` |
| Counting | `collections.Counter` |
| Ordered dict | `dict` (insertion order since 3.7) |
| Default values | `collections.defaultdict` |

### When to Use What

- **list**: Default mutable sequence. O(1) append, O(n) insert/delete.
- **tuple**: Immutable, hashable. Use for fixed data, dict keys, return values.
- **dict**: Key-value lookup. O(1) average access.
- **set**: Membership testing O(1), deduplication, set operations.
- **deque**: Fast append/pop from both ends. Use for queues.
- **namedtuple/dataclass**: Structured data with named fields.

## Naming Conventions (PEP 8)

```python
# snake_case for functions and variables
def calculate_total_price(items: list) -> float: ...
user_count = 42

# SCREAMING_SNAKE_CASE for constants
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT = 30

# PascalCase for classes
class UserRepository: ...
class HTTPClient: ...  # Acronyms capitalized

# _leading underscore for private
def _internal_helper(): ...
_cache = {}

# __dunder__ for magic methods
def __init__(self): ...
def __repr__(self): ...
```

## Best Practices

### Do

- **Use type hints**: Document intent, enable static analysis
- **Prefer immutability**: `frozen=True` dataclasses, tuples over lists
- **Write pure functions**: Same input, same output, no side effects
- **Use context managers**: `with` for resource cleanup
- **Leverage comprehensions**: Readable, Pythonic transformations
- **Validate at boundaries**: Check external input, trust internal data
- **Use Protocol for interfaces**: Structural typing, duck typing

### Don't

- **Avoid mutable default args**: `def f(lst=None)` not `def f(lst=[])`
- **Don't catch bare Exception**: Be specific about error types
- **Avoid global state**: Pass dependencies explicitly
- **Don't mutate function args**: Return new values instead
- **Avoid deep inheritance**: Composition over inheritance
- **Don't ignore type errors**: Fix them, they catch bugs

## Code Organization

```
my-project/
├── src/my_project/
│   ├── __init__.py
│   ├── main.py          # Entry point
│   ├── config.py        # Configuration
│   ├── domain/          # Business entities
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── order.py
│   ├── services/        # Business logic
│   │   └── user_service.py
│   ├── adapters/        # External interfaces
│   │   ├── db.py
│   │   └── api.py
│   └── utils/           # Shared utilities
├── tests/
│   ├── unit/
│   └── integration/
├── pyproject.toml
└── uv.lock
```

## Error Handling

```python
# Custom exceptions with context
class UserNotFoundError(Exception):
    def __init__(self, user_id: int):
        self.user_id = user_id
        super().__init__(f"User {user_id} not found")

# Catch specific exceptions
try:
    user = find_user(user_id)
except UserNotFoundError as e:
    logger.warning(f"User {e.user_id} not found")
    return None
except DatabaseError:
    logger.exception("Database error")
    raise

# Result types instead of exceptions
from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar("T")

@dataclass(frozen=True)
class Ok(Generic[T]):
    value: T

@dataclass(frozen=True)
class Err:
    error: str

Result = Ok[T] | Err
```

## Performance Tips

### Prefer

- **Generator expressions**: `(x for x in items)` for large data
- **`dict.get()`**: Avoid KeyError, provide defaults
- **`set` for membership**: O(1) vs O(n) for lists
- **Local variables**: Faster than globals in tight loops
- **`itertools`**: Memory-efficient iteration
- **`__slots__`**: Reduce memory for many instances

### Avoid

- **Repeated attribute lookup**: Cache `obj.attr` in loops
- **String concatenation in loops**: Use `"".join(parts)`
- **Creating lists for iteration**: Use generators
- **`import` inside functions**: Move to module level

## Common Idioms

```python
# Unpacking
first, *rest = items
a, b = b, a  # Swap

# Dict comprehension with condition
{k: v for k, v in data.items() if v is not None}

# Defaultdict for grouping
from collections import defaultdict
groups = defaultdict(list)
for item in items:
    groups[item.category].append(item)

# Counter for frequencies
from collections import Counter
counts = Counter(["a", "b", "a", "c", "a"])
# Counter({'a': 3, 'b': 1, 'c': 1})

# Enumerate with start
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")

# Zip for parallel iteration
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# any/all for conditions
if any(item.is_valid for item in items): ...
if all(x > 0 for x in numbers): ...

# Walrus operator
if (match := pattern.search(text)):
    print(match.group(0))
```

## Type Hints Quick Reference

```python
# Basic types
x: int = 1
s: str = "hello"
flag: bool = True

# Collections
items: list[str] = []
counts: dict[str, int] = {}
ids: set[int] = set()

# Optional (None possible)
name: str | None = None

# Union
value: int | str = 42

# Callable
from typing import Callable
fn: Callable[[int, str], bool]

# TypeVar for generics
from typing import TypeVar
T = TypeVar("T")
def first(items: list[T]) -> T: ...

# Protocol for structural typing
from typing import Protocol

class Printable(Protocol):
    def __str__(self) -> str: ...
```
