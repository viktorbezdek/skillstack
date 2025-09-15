# Modern Python Cookbook

Key features from Python 3.8 through 3.14, organized as practical recipes.

---

## Walrus Operator (3.8+)

**Problem**: You need to assign a value and use it in an expression without splitting into multiple lines.

**Solution**:
```python
# Read until empty line
while (line := input()) != "":
    print(f"Got: {line}")

# Filter and capture
if (match := pattern.search(text)) is not None:
    print(match.group(0))

# List comprehension with reuse
results = [y for x in data if (y := expensive(x)) > threshold]
```

**Tip**: The walrus operator `:=` reduces boilerplate when you need both assignment and the value in conditions or comprehensions.

---

## Positional-Only Parameters (3.8+)

**Problem**: You want to prevent callers from using keyword arguments for certain parameters, ensuring API stability.

**Solution**:
```python
def greet(name, /, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")              # OK
greet("Alice", "Hi")        # OK
greet(name="Alice")         # TypeError - name is positional-only
```

**Tip**: Use `/` to mark parameters as positional-only, allowing you to rename internal parameters without breaking compatibility.

---

## Self-Documenting F-Strings (3.8+)

**Problem**: You're debugging or logging and want to print variable names along with their values.

**Solution**:
```python
x = 10
y = 25
print(f"{x=}, {y=}, {x+y=}")
# Output: x=10, y=25, x+y=35

user = {"name": "Alice", "age": 30}
print(f"{user['name']=}")
# Output: user['name']='Alice'
```

**Tip**: The `=` specifier in f-strings shows both the expression and its value, perfect for quick debugging.

---

## Dict Merge Operators (3.9+)

**Problem**: You need to merge dictionaries or update one dict with another's values.

**Solution**:
```python
defaults = {"host": "localhost", "port": 8080}
overrides = {"port": 3000, "debug": True}

# Merge (new dict)
config = defaults | overrides
# {'host': 'localhost', 'port': 3000, 'debug': True}

# Update in place
defaults |= overrides
```

**Tip**: Use `|` for merging (creates new dict) and `|=` for in-place updates, replacing the older `{**d1, **d2}` pattern.

---

## Built-in Generic Types (3.9+)

**Problem**: You want type hints without importing from the `typing` module.

**Solution**:
```python
# No more typing.List, typing.Dict imports
def process(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}

# Works with all builtins
ids: set[int] = {1, 2, 3}
pairs: tuple[str, int] = ("age", 25)
```

**Tip**: All built-in collection types now support generic syntax directly, making type hints cleaner and more readable.

---

## String Prefix/Suffix Removal (3.9+)

**Problem**: You need to cleanly remove known prefixes or suffixes from strings.

**Solution**:
```python
filename = "test_user_service.py"

filename.removeprefix("test_")     # "user_service.py"
filename.removesuffix(".py")       # "test_user_service"

# Replaces awkward patterns like:
# s[len(prefix):] if s.startswith(prefix) else s
```

**Tip**: These methods only remove the prefix/suffix if present, otherwise return the original string unchanged.

---

## Pattern Matching (3.10+)

**Problem**: You need to match complex data structures and extract values in a clean, readable way.

**Solution**:
```python
def handle(command):
    match command.split():
        case ["quit"]:
            return "Goodbye"
        case ["load", filename]:
            return f"Loading {filename}"
        case ["save", filename, "--force"]:
            return f"Force saving {filename}"
        case _:
            return "Unknown command"

# With guards
match point:
    case (x, y) if x == y:
        print("On diagonal")
    case (x, y):
        print(f"At ({x}, {y})")

# Class patterns
match event:
    case Click(x=0, y=0):
        print("Origin click")
    case Click(x=x, y=y):
        print(f"Click at {x}, {y}")
```

**Tip**: Pattern matching is more powerful than `if/elif` chains, supporting destructuring, guards, and type matching in a single construct.

---

## Union Type Syntax (3.10+)

**Problem**: You want cleaner type hints for values that can be multiple types.

**Solution**:
```python
# Instead of Union[int, str]
def process(value: int | str | None) -> str:
    if value is None:
        return "empty"
    return str(value)

# Works in isinstance too
isinstance(x, int | str)  # Same as isinstance(x, (int, str))
```

**Tip**: The `|` syntax works in both type hints and runtime type checking with `isinstance()`.

---

## Parenthesized Context Managers (3.10+)

**Problem**: You need to use multiple context managers without deeply nested indentation.

**Solution**:
```python
with (
    open("input.txt") as src,
    open("output.txt", "w") as dst,
    some_lock as lock,
):
    dst.write(src.read())
```

**Tip**: Parentheses allow you to format multiple context managers cleanly across multiple lines without backslash continuation.

---

## Exception Groups (3.11+)

**Problem**: You need to raise or handle multiple exceptions at once, common in concurrent code.

**Solution**:
```python
# Raise multiple exceptions
raise ExceptionGroup("errors", [
    ValueError("invalid value"),
    TypeError("wrong type"),
])

# Catch by type
try:
    async_operation()
except* ValueError as eg:
    print(f"Value errors: {eg.exceptions}")
except* TypeError as eg:
    print(f"Type errors: {eg.exceptions}")
```

**Tip**: Use `except*` (not `except`) to handle exception groups. Each handler processes all exceptions of that type.

---

## TaskGroup for Structured Concurrency (3.11+)

**Problem**: You want to run multiple async tasks and ensure all complete or all cancel together on error.

**Solution**:
```python
import asyncio

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch("url1"))
        task2 = tg.create_task(fetch("url2"))
    # All tasks complete or all cancelled on error
    return task1.result(), task2.result()
```

**Tip**: TaskGroup provides automatic cancellation of sibling tasks if any task fails, preventing orphaned tasks.

---

## TOML Parser (3.11+)

**Problem**: You need to parse TOML configuration files without external dependencies.

**Solution**:
```python
import tomllib

with open("pyproject.toml", "rb") as f:
    config = tomllib.load(f)

# Or from string
data = tomllib.loads('[section]\nkey = "value"')
```

**Tip**: Note that files must be opened in binary mode (`"rb"`). `tomllib` is read-only; use `tomli_w` for writing.

---

## Self Type (3.11+)

**Problem**: You want method return types to correctly refer to the current class, not the parent.

**Solution**:
```python
from typing import Self

class Builder:
    def with_name(self, name: str) -> Self:
        self.name = name
        return self

    def clone(self) -> Self:
        return type(self)()
```

**Tip**: `Self` is especially useful for builder patterns and methods that return the instance for chaining.

---

## Type Parameter Syntax (3.12+)

**Problem**: You want to write generic functions and classes without the boilerplate of `TypeVar`.

**Solution**:
```python
# Old way
from typing import TypeVar
T = TypeVar("T")
def first(items: list[T]) -> T: ...

# New way - cleaner!
def first[T](items: list[T]) -> T:
    return items[0]

# Generic classes
class Stack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

# Constrained types
def add[T: (int, float)](a: T, b: T) -> T:
    return a + b
```

**Tip**: The new bracket syntax is more concise and puts type parameters directly in function/class signatures.

---

## Type Alias Statement (3.12+)

**Problem**: You want to create type aliases that are properly recognized as types, not runtime values.

**Solution**:
```python
# Old way
from typing import TypeAlias
Vector: TypeAlias = list[float]

# New way
type Vector = list[float]
type Point = tuple[float, float]
type Callback[T] = Callable[[T], None]
```

**Tip**: The `type` statement creates proper type aliases that support generic parameters cleanly.

---

## F-String Improvements (3.12+)

**Problem**: You need to use quotes inside f-strings or format complex multiline expressions.

**Solution**:
```python
# Nested quotes (any quote style)
print(f"User: {user["name"]}")  # Now works!
print(f'Status: {data['status']}')

# Multiline expressions
result = f"{
    some_long_function_call(
        arg1,
        arg2
    )
}"

# Comments inside f-strings
f"{x:=10}"  # This is a format spec, not walrus!
```

**Tip**: You can now use any quote style inside f-strings without escaping, making JSON and dict access much cleaner.

---

## Override Decorator (3.12+)

**Problem**: You want to catch typos or signature mismatches when overriding parent class methods.

**Solution**:
```python
from typing import override

class Parent:
    def greet(self) -> str:
        return "Hello"

class Child(Parent):
    @override
    def greet(self) -> str:  # Type checker verifies this exists in parent
        return "Hi"

    @override
    def great(self) -> str:  # Error: typo, no such method in parent
        return "Oops"
```

**Tip**: Use `@override` to make type checkers verify that you're actually overriding a parent method, catching typos early.

---

## Batched Iteration (3.12+)

**Problem**: You need to process data in fixed-size chunks.

**Solution**:
```python
from itertools import batched

list(batched("ABCDEFG", 3))
# [('A', 'B', 'C'), ('D', 'E', 'F'), ('G',)]

# Process in chunks
for batch in batched(large_dataset, 100):
    process_batch(batch)
```

**Tip**: `batched()` is more efficient than manual chunking and handles the final partial batch automatically.

---

## Free-Threaded Python (3.13+)

**Problem**: You need true parallel execution for CPU-bound tasks without multiprocessing overhead.

**Solution**:
```python
# Build/install with: --disable-gil
# True parallelism for CPU-bound threads

import threading

# These now run in parallel on multiple cores
threads = [
    threading.Thread(target=cpu_intensive, args=(data,))
    for data in chunks
]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

**Tip**: Free-threaded mode must be enabled at build time. It's experimental in 3.13 but enables true CPU parallelism with threads.

---

## Copy and Replace (3.13+)

**Problem**: You want to create a copy of an object with some fields changed, especially for dataclasses.

**Solution**:
```python
from copy import replace
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

alice = User("Alice", 30)
bob = replace(alice, name="Bob")
# User(name='Bob', age=30)
```

**Tip**: `replace()` works with any object that has `__replace__()`, including dataclasses, namedtuples, and custom classes.

---

## Deprecated Decorator (3.13+)

**Problem**: You need to mark functions as deprecated with proper warnings.

**Solution**:
```python
from warnings import deprecated

@deprecated("Use new_function() instead")
def old_function():
    ...

old_function()  # Emits DeprecationWarning
```

**Tip**: The decorator provides a standard way to deprecate APIs, making migration paths clear to users.

---

## Template Strings (3.14+)

**Problem**: You want safe, inspectable string templates that aren't immediately evaluated like f-strings.

**Solution**:
```python
name = "Alice"
age = 30

# Template object (not evaluated string)
template = t"Hello {name}, age {age}"

# Safer than f-strings for user templates
# Can inspect/transform before rendering
print(template.strings)       # ("Hello ", ", age ", "")
print(template.interpolations) # (Interpolation(name, ...), ...)
```

**Tip**: t-strings return template objects you can inspect and control, preventing injection attacks in user-provided templates.

---

## Deferred Annotation Evaluation (3.14+)

**Problem**: You need forward references in type hints without quote strings.

**Solution**:
```python
# Forward references work without quotes!
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Node | None = None  # No "Node" quotes needed

    def append(self, node: Node) -> Node:
        self.next = node
        return node
```

**Tip**: Annotations are evaluated lazily, so you can reference classes before they're fully defined without string quotes.

---

## Time-Sortable UUIDs (3.14+)

**Problem**: You need UUIDs that maintain chronological order for database efficiency.

**Solution**:
```python
from uuid import uuid7

id1 = uuid7()
id2 = uuid7()

assert id1 < id2  # Chronologically sortable!
# Great for database primary keys
```

**Tip**: UUID v7 includes a timestamp, making them naturally sortable and more database-friendly than UUID v4.

---

## Pathlib Copy and Move (3.14+)

**Problem**: You want to copy or move files using pathlib instead of shutil.

**Solution**:
```python
from pathlib import Path

src = Path("file.txt")
src.copy(Path("backup/file.txt"))
src.move(Path("archive/file.txt"))

# Directory copy
Path("src/").copy(Path("backup/"), recursive=True)
```

**Tip**: These methods integrate file operations directly into Path objects, eliminating the need for separate shutil imports.

---

## Simplified Exception Syntax (3.14+)

**Problem**: You want to catch multiple exception types without tuple syntax.

**Solution**:
```python
# Multiple exception types without parentheses
try:
    risky_operation()
except ValueError, TypeError, KeyError:  # No tuple needed!
    handle_error()
```

**Tip**: The comma-separated syntax matches the consistency of other Python syntax and reduces visual clutter.

---

## Quick Reference

| Version | Key Feature | Example |
|---------|-------------|---------|
| 3.8 | Walrus `:=` | `if (n := len(x)) > 10:` |
| 3.8 | Positional-only `/` | `def f(x, /):` |
| 3.9 | Dict merge `\|` | `d1 \| d2` |
| 3.9 | Built-in generics | `list[int]` |
| 3.10 | Pattern matching | `match x: case ...:` |
| 3.10 | Union `\|` | `int \| str` |
| 3.11 | Exception groups | `except* ValueError:` |
| 3.11 | TaskGroup | `async with TaskGroup():` |
| 3.12 | Type params | `def f[T](x: T):` |
| 3.12 | `type` statement | `type Alias = ...` |
| 3.13 | Free-threaded | No GIL option |
| 3.13 | `@deprecated` | Deprecation decorator |
| 3.14 | t-strings | `t"Hello {name}"` |
| 3.14 | `uuid7()` | Time-sortable UUIDs |
