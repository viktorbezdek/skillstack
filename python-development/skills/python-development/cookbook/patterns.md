# Functional Patterns Cookbook

Deep dive into functional programming patterns in Python 3.14+.

---

## Higher-Order Functions

**Problem**: You need to pass functions as arguments to other functions or return them as values.

**Solution**:
```python
from typing import Callable

def apply_twice(f: Callable[[int], int], x: int) -> int:
    return f(f(x))

def increment(x: int) -> int:
    return x + 1

result = apply_twice(increment, 5)
assert result == 7  # 5 → 6 → 7
```

**Tip**: Higher-order functions enable powerful abstractions. Use type hints to make the function signatures clear and catch errors early.

---

## Pure Functions

**Problem**: You want functions that are predictable, testable, and free from side effects.

**Solution**:
```python
# ✅ Pure: Same input → Same output, no side effects
def calculate_discount(price: float, rate: float) -> float:
    return price * (1 - rate)

# ❌ Impure: Side effects (modifies external state)
total = 0
def add_to_total(amount: float) -> None:
    global total
    total += amount
```

**Tip**: Pure functions are easier to test, reason about, and parallelize. Avoid global state and mutations when possible.

---

## Map, Filter, Reduce

**Problem**: You need to transform, filter, or aggregate collections of data.

**Solution**:
```python
from functools import reduce
from operator import add, mul

numbers = [1, 2, 3, 4, 5]

# Map: Transform each element
doubled = list(map(lambda x: x * 2, numbers))
assert doubled == [2, 4, 6, 8, 10]

# Filter: Keep elements matching predicate
evens = list(filter(lambda x: x % 2 == 0, numbers))
assert evens == [2, 4]

# Reduce: Accumulate to single value
product = reduce(mul, numbers, 1)
assert product == 120

# ✅ Prefer comprehensions when readable
doubled_comp = [x * 2 for x in numbers]
evens_comp = [x for x in numbers if x % 2 == 0]
```

**Tip**: Comprehensions are often more Pythonic than map/filter. Use reduce for accumulation, but consider built-ins like sum() when available.

---

## List Comprehensions

**Problem**: You need to transform or filter lists concisely.

**Solution**:
```python
# Basic
squares = [x ** 2 for x in range(10)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Nested comprehension (flatten)
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [item for row in matrix for item in row]
assert flattened == [1, 2, 3, 4, 5, 6]

# Dictionary comprehension
user_ages = {user["name"]: user["age"] for user in users}

# Set comprehension
unique_lengths = {len(word) for word in ["apple", "pie", "cat"]}
```

**Tip**: Keep comprehensions simple. If logic gets complex, extract it to a named function for readability.

---

## Generator Expressions

**Problem**: You need to process large datasets without loading everything into memory.

**Solution**:
```python
# Generator: Lazy, memory-efficient
squares_gen = (x ** 2 for x in range(10))

# Consume one at a time
assert next(squares_gen) == 0
assert next(squares_gen) == 1

# Memory-efficient for large datasets
large_data = (x ** 2 for x in range(1_000_000))  # No intermediate list
result = sum(large_data)  # Process lazily
```

**Tip**: Use generator expressions (parentheses) instead of list comprehensions (brackets) when you only need to iterate once or when working with large datasets.

---

## Readable Comprehensions

**Problem**: Your comprehensions are becoming too complex and hard to understand.

**Solution**:
```python
# ✅ Keep simple and readable
good = [x * 2 for x in numbers if x > 5]

# ❌ Avoid overly complex
bad = [x * 2 if x > 5 else x for x in numbers]

# Extract to function if complex
def is_valid(item: dict) -> bool:
    return item["age"] >= 18 and item["status"] == "active"

valid_items = [item for item in data if is_valid(item)]
```

**Tip**: If a comprehension has multiple conditions or complex logic, extract the logic into a well-named function.

---

## Infinite Iterators

**Problem**: You need to generate infinite sequences or cycle through values repeatedly.

**Solution**:
```python
from itertools import count, cycle, repeat

# count: Infinite counter
counter = count(start=10, step=2)
assert next(counter) == 10
assert next(counter) == 12

# cycle: Endlessly repeat iterable
colors = cycle(['red', 'green', 'blue'])
assert next(colors) == 'red'

# repeat: Repeat value n times
repeated = list(repeat('x', 3))
assert repeated == ['x', 'x', 'x']
```

**Tip**: Infinite iterators are memory-efficient but need explicit stopping conditions. Use with islice() or takewhile() to limit output.

---

## Chaining and Accumulating

**Problem**: You need to concatenate iterables or compute running aggregations.

**Solution**:
```python
from itertools import chain, accumulate
from operator import add, mul

# chain: Concatenate iterables
combined = list(chain([1, 2], [3, 4], [5, 6]))
assert combined == [1, 2, 3, 4, 5, 6]

# accumulate: Running total/aggregation
cumsum = list(accumulate([1, 2, 3, 4], add))
assert cumsum == [1, 3, 6, 10]

cumprod = list(accumulate([1, 2, 3, 4], mul))
assert cumprod == [1, 2, 6, 24]
```

**Tip**: Use chain.from_iterable() to flatten nested iterables efficiently. accumulate() is great for running totals and cumulative operations.

---

## Batching and Pairing

**Problem**: You need to group elements into chunks or create consecutive pairs.

**Solution**:
```python
from itertools import batched, pairwise

# batched: Group into fixed-size chunks (3.12+)
data = list(batched('ABCDEFG', 2))
assert data == [('A', 'B'), ('C', 'D'), ('E', 'F'), ('G',)]

# pairwise: Consecutive overlapping pairs
pairs = list(pairwise('ABCD'))
assert pairs == [('A', 'B'), ('B', 'C'), ('C', 'D')]
```

**Tip**: batched() is perfect for processing data in chunks. pairwise() is useful for comparing consecutive elements or computing differences.

---

## Filtering Iterators

**Problem**: You need to filter or slice iterators based on conditions.

**Solution**:
```python
from itertools import filterfalse, takewhile, dropwhile, islice

numbers = [1, 4, 6, 3, 8, 2, 5]

# filterfalse: Opposite of filter
odds = list(filterfalse(lambda x: x % 2 == 0, numbers))
assert odds == [1, 3, 5]

# takewhile: Keep while condition is true
taken = list(takewhile(lambda x: x < 5, [1, 4, 6, 3, 8]))
assert taken == [1, 4]  # Stops at 6

# dropwhile: Skip while condition is true
dropped = list(dropwhile(lambda x: x < 5, [1, 4, 6, 3, 8]))
assert dropped == [6, 3, 8]

# islice: Slice without creating list
sliced = list(islice(range(10), 2, 7, 2))
assert sliced == [2, 4, 6]
```

**Tip**: takewhile() and dropwhile() stop at the first failure, unlike filter(). Use islice() for memory-efficient slicing of large iterators.

---

## Combinatorics

**Problem**: You need to generate combinations, permutations, or cartesian products.

**Solution**:
```python
from itertools import combinations, permutations, product

# combinations: All r-length subsets
combos = list(combinations('ABC', 2))
assert combos == [('A', 'B'), ('A', 'C'), ('B', 'C')]

# permutations: All orderings
perms = list(permutations('ABC', 2))
assert len(perms) == 6  # 3 * 2

# product: Cartesian product (like nested loops)
pairs = list(product('AB', [1, 2]))
assert pairs == [('A', 1), ('A', 2), ('B', 1), ('B', 2)]

# product with repeat
all_binary = list(product([0, 1], repeat=3))
assert len(all_binary) == 8  # 2^3
```

**Tip**: These functions grow exponentially. Be careful with large inputs. Use them for small sets or with islice() to limit output.

---

## Grouping Elements

**Problem**: You need to group consecutive equal elements or group by a key.

**Solution**:
```python
from itertools import groupby

# groupby: Group consecutive equal elements
data = 'AAAABBBCCDAA'
grouped = [(key, len(list(group))) for key, group in groupby(data)]
assert grouped == [('A', 4), ('B', 3), ('C', 2), ('D', 1), ('A', 2)]

# groupby requires sorted data for meaningful grouping
people = [
    {"name": "Alice", "dept": "eng"},
    {"name": "Bob", "dept": "eng"},
    {"name": "Carol", "dept": "hr"},
]
sorted_people = sorted(people, key=lambda x: x["dept"])

for dept, group in groupby(sorted_people, key=lambda x: x["dept"]):
    members = [p["name"] for p in group]
    print(f"{dept}: {members}")
```

**Tip**: Always sort your data by the grouping key before using groupby(). The groups are consecutive, not global.

---

## Itertools Recipes

**Problem**: You need common iterator patterns like flattening, taking n items, or finding unique elements.

**Solution**:
```python
from itertools import islice, chain

# flatten one level
def flatten(list_of_lists):
    return chain.from_iterable(list_of_lists)

nested = [[1, 2], [3, 4], [5, 6]]
assert list(flatten(nested)) == [1, 2, 3, 4, 5, 6]

# take first n items
def take(n: int, iterable):
    return list(islice(iterable, n))

assert take(3, range(10)) == [0, 1, 2]

# unique elements (preserving order)
def unique(iterable, key=None):
    seen = set()
    for item in iterable:
        k = key(item) if key else item
        if k not in seen:
            seen.add(k)
            yield item
```

**Tip**: Build a library of common iterator recipes. These patterns appear frequently and are more efficient than list-based approaches.

---

## Reduce for Accumulation

**Problem**: You need to combine all elements of a sequence into a single value using a custom operation.

**Solution**:
```python
from functools import reduce
from operator import add, mul

numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers)
assert total == 15

product = reduce(mul, numbers)
assert product == 120

# Custom reducer
def concat_strings(acc: str, s: str) -> str:
    return f"{acc},{s}" if acc else s

words = ["apple", "banana", "cherry"]
result = reduce(concat_strings, words, "")
assert result == "apple,banana,cherry"
```

**Tip**: Always provide an initial value to reduce() when possible. Use operator module functions (add, mul) instead of lambdas for better performance.

---

## Partial Application

**Problem**: You need to create specialized versions of functions by fixing some arguments.

**Solution**:
```python
from functools import partial

def power(base: int, exponent: int) -> int:
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

assert square(5) == 25
assert cube(5) == 125

# With positional args
def greet(greeting: str, name: str) -> str:
    return f"{greeting}, {name}!"

say_hello = partial(greet, "Hello")
assert say_hello("Alice") == "Hello, Alice!"
```

**Tip**: Use partial() to create specialized functions without writing wrapper functions. Great for callbacks and configuration.

---

## Memoization

**Problem**: You have expensive function calls that repeat with the same arguments.

**Solution**:
```python
from functools import lru_cache, cached_property

@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Without cache: O(2^n), With cache: O(n)
assert fibonacci(100) == 354224848179261915075

print(fibonacci.cache_info())
fibonacci.cache_clear()  # Clear cache

# cached_property for classes
class User:
    def __init__(self, user_id: int):
        self.user_id = user_id

    @cached_property
    def full_name(self) -> str:
        return f"User-{self.user_id}"  # Computed once
```

**Tip**: lru_cache is perfect for recursive functions and expensive computations. Use cached_property for expensive instance computations that only need to run once.

---

## Function Overloading

**Problem**: You want different behavior based on the argument type without manual type checking.

**Solution**:
```python
from functools import singledispatch

@singledispatch
def process(arg: object) -> str:
    return f"Default: {arg}"

@process.register(int)
def _(arg: int) -> str:
    return f"Integer: {arg * 2}"

@process.register(list)
def _(arg: list) -> str:
    return f"List with {len(arg)} items"

assert process(5) == "Integer: 10"
assert process([1, 2, 3]) == "List with 3 items"
assert process("hello") == "Default: hello"
```

**Tip**: singledispatch dispatches on the type of the first argument. Great for creating extensible APIs without complex if/isinstance chains.

---

## Function Composition

**Problem**: You want to combine multiple functions into a single function that applies them in sequence.

**Solution**:
```python
from typing import Callable, TypeVar

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')

def compose(f: Callable[[T], U], g: Callable[[U], V]) -> Callable[[T], V]:
    def composed(x: T) -> V:
        return g(f(x))
    return composed

def add_one(x: int) -> int:
    return x + 1

def double(x: int) -> int:
    return x * 2

add_then_double = compose(add_one, double)
assert add_then_double(5) == 12  # (5 + 1) * 2
```

**Tip**: Composition reads right-to-left (mathematical style). For left-to-right, use pipe functions or method chaining.

---

## Pipeline Pattern

**Problem**: You want to chain multiple transformations in a readable left-to-right order.

**Solution**:
```python
from functools import reduce
from typing import Callable, Any

def pipe(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]:
    return reduce(lambda f, g: lambda x: g(f(x)), functions, lambda x: x)

def add_one(x: int) -> int:
    return x + 1

def triple(x: int) -> int:
    return x * 3

pipeline = pipe(add_one, triple, lambda x: x - 2)
assert pipeline(5) == 16  # 5 → 6 → 18 → 16
```

**Tip**: Pipelines make data transformations more readable. Each function receives the output of the previous one.

---

## Fluent Pipeline Class

**Problem**: You want method chaining for readable, type-safe data transformations.

**Solution**:
```python
from typing import Generic, TypeVar, Callable

T = TypeVar('T')
U = TypeVar('U')

class Pipeline(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def then(self, func: Callable[[T], U]) -> 'Pipeline[U]':
        return Pipeline(func(self.value))

    def get(self) -> T:
        return self.value

def add_one(x: int) -> int:
    return x + 1

def triple(x: int) -> int:
    return x * 3

result = (
    Pipeline(5)
    .then(add_one)
    .then(triple)
    .then(lambda x: x - 2)
    .get()
)
assert result == 16
```

**Tip**: Fluent interfaces improve readability. This pattern is especially useful for data processing workflows.

---

## Frozen Dataclasses

**Problem**: You want immutable data structures that prevent accidental modification.

**Solution**:
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinates:
    x: float
    y: float

    def move(self, dx: float, dy: float) -> 'Coordinates':
        return Coordinates(self.x + dx, self.y + dy)

c1 = Coordinates(0, 0)
c2 = c1.move(1, 1)

assert c1.x == 0  # Original unchanged
assert c2.x == 1  # New instance
```

**Tip**: Frozen dataclasses are hashable and can be used as dictionary keys. Return new instances instead of mutating for immutability.

---

## NamedTuple for Immutability

**Problem**: You need lightweight, immutable records with named fields.

**Solution**:
```python
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float

p1 = Point(0, 0)
x, y = p1  # Unpack
# p1.x = 5  # TypeError - immutable
```

**Tip**: NamedTuples are memory-efficient and faster than dataclasses. Use them for simple immutable records.

---

## Immutable Collections

**Problem**: You need to prevent modifications to dictionaries or expose read-only views.

**Solution**:
```python
from types import MappingProxyType

config = {"api_key": "secret", "timeout": 30}
readonly_config = MappingProxyType(config)
# readonly_config["api_key"] = "new"  # TypeError

# Functional list operations with tuples
def append_immutable(lst: tuple, item) -> tuple:
    return lst + (item,)

numbers = (1, 2, 3)
new_numbers = append_immutable(numbers, 4)
assert numbers == (1, 2, 3)  # Unchanged
assert new_numbers == (1, 2, 3, 4)
```

**Tip**: MappingProxyType creates a read-only view of a dictionary. Use tuples instead of lists for immutable sequences.

---

## Copy-on-Write Pattern

**Problem**: You need to update data structures without mutating the original.

**Solution**:
```python
from copy import copy
from dataclasses import dataclass

@dataclass
class UserProfile:
    name: str
    settings: dict

    def with_setting(self, key: str, value: object) -> 'UserProfile':
        new_settings = copy(self.settings)
        new_settings[key] = value
        return UserProfile(name=self.name, settings=new_settings)

profile1 = UserProfile("Alice", {"theme": "light"})
profile2 = profile1.with_setting("theme", "dark")

assert profile1.settings["theme"] == "light"  # Unchanged
assert profile2.settings["theme"] == "dark"
```

**Tip**: Copy-on-write provides a balance between immutability and performance. Use copy() for shallow copies or deepcopy() for nested structures.

---
