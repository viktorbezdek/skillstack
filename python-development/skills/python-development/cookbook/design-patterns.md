# Design Patterns Cookbook

Functional and OOP patterns in Python using Protocols.

---

## Builder Pattern (Fluent API)

**Problem**: You need to construct complex objects step-by-step with a clean, readable API that allows method chaining.

**Solution**:
```python
from typing import Optional

class QueryBuilder:
    def __init__(self, table: str):
        self.table = table
        self._where = []
        self._limit: Optional[int] = None

    def where(self, condition: str) -> 'QueryBuilder':
        self._where.append(condition)
        return self

    def limit(self, n: int) -> 'QueryBuilder':
        self._limit = n
        return self

    def build(self) -> str:
        query = f"SELECT * FROM {self.table}"
        if self._where:
            query += " WHERE " + " AND ".join(self._where)
        if self._limit:
            query += f" LIMIT {self._limit}"
        return query

# Usage
query = (
    QueryBuilder("users")
    .where("age > 18")
    .where("status = 'active'")
    .limit(10)
    .build()
)
assert query == "SELECT * FROM users WHERE age > 18 AND status = 'active' LIMIT 10"
```

**Tip**: Return `self` from each builder method to enable method chaining. This creates a fluent API that reads like natural language.

---

## Dependency Injection

**Problem**: You want to decouple your code from specific implementations and make it easy to swap dependencies for testing or runtime configuration.

**Solution**:
```python
from typing import Protocol

class Logger(Protocol):
    def log(self, message: str) -> None: ...

class ConsoleLogger:
    def log(self, message: str) -> None:
        print(message)

class FileLogger:
    def __init__(self, path: str):
        self.path = path

    def log(self, message: str) -> None:
        with open(self.path, "a") as f:
            f.write(f"{message}\n")

class Service:
    def __init__(self, logger: Logger):
        self.logger = logger

    def process(self):
        self.logger.log("Processing...")
        # ... work ...
        self.logger.log("Done!")

# Usage - swap implementations freely
service = Service(ConsoleLogger())
service.process()

service = Service(FileLogger("app.log"))
service.process()
```

**Tip**: Use Protocol types to define interfaces without requiring inheritance. This allows any class with matching methods to satisfy the dependency.

---

## Factory Pattern

**Problem**: You need to create different types of objects based on runtime conditions without exposing the creation logic to the client.

**Solution**:
```python
from typing import Protocol, Literal

class DataSource(Protocol):
    def connect(self) -> None: ...
    def query(self, sql: str) -> list: ...

class PostgreSQL:
    def connect(self) -> None:
        print("Connected to PostgreSQL")

    def query(self, sql: str) -> list:
        return []

class MySQL:
    def connect(self) -> None:
        print("Connected to MySQL")

    def query(self, sql: str) -> list:
        return []

class SQLite:
    def connect(self) -> None:
        print("Connected to SQLite")

    def query(self, sql: str) -> list:
        return []

def create_datasource(db_type: Literal["postgres", "mysql", "sqlite"]) -> DataSource:
    match db_type:
        case "postgres":
            return PostgreSQL()
        case "mysql":
            return MySQL()
        case "sqlite":
            return SQLite()
        case _:
            raise ValueError(f"Unknown database: {db_type}")

# Usage
db = create_datasource("postgres")
db.connect()
```

**Tip**: Combine factory functions with Literal types for type-safe object creation. Python's match statement makes factories clean and exhaustive.

---

## Strategy Pattern

**Problem**: You need to switch between different algorithms or behaviors at runtime without modifying the client code.

**Solution**:
```python
from typing import Protocol

class SortStrategy(Protocol):
    def sort(self, items: list) -> list: ...

class QuickSort:
    def sort(self, items: list) -> list:
        if len(items) <= 1:
            return items
        pivot = items[len(items) // 2]
        left = [x for x in items if x < pivot]
        middle = [x for x in items if x == pivot]
        right = [x for x in items if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class MergeSort:
    def sort(self, items: list) -> list:
        if len(items) <= 1:
            return items
        mid = len(items) // 2
        left = self.sort(items[:mid])
        right = self.sort(items[mid:])
        return self._merge(left, right)

    def _merge(self, left: list, right: list) -> list:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort(self, items: list) -> list:
        return self.strategy.sort(items)

# Usage - swap algorithms at runtime
sorter = Sorter(QuickSort())
assert sorter.sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

sorter = Sorter(MergeSort())
assert sorter.sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
```

**Tip**: Strategy pattern is ideal when you have multiple ways to perform an operation. The Protocol type ensures all strategies share the same interface.

---

## Repository Pattern

**Problem**: You want to abstract data access logic and provide a collection-like interface for domain objects, making it easy to switch storage backends.

**Solution**:
```python
from typing import Protocol, TypeVar, Generic
from dataclasses import dataclass

T = TypeVar("T")

@dataclass(frozen=True)
class User:
    id: int
    name: str
    email: str

class Repository(Protocol[T]):
    def get(self, id: int) -> T | None: ...
    def save(self, entity: T) -> None: ...
    def delete(self, id: int) -> None: ...
    def list_all(self) -> list[T]: ...

class InMemoryUserRepository:
    def __init__(self):
        self._store: dict[int, User] = {}

    def get(self, id: int) -> User | None:
        return self._store.get(id)

    def save(self, entity: User) -> None:
        self._store[entity.id] = entity

    def delete(self, id: int) -> None:
        self._store.pop(id, None)

    def list_all(self) -> list[User]:
        return list(self._store.values())

# Usage
repo: Repository[User] = InMemoryUserRepository()
repo.save(User(1, "Alice", "alice@example.com"))
user = repo.get(1)
```

**Tip**: Use Generic protocols to create reusable repository interfaces. This pattern isolates business logic from persistence details.

---

## Observer Pattern (Event-Based)

**Problem**: You need to notify multiple objects about state changes or events without creating tight coupling between components.

**Solution**:
```python
from typing import Callable
from dataclasses import dataclass, field

@dataclass
class EventEmitter:
    _listeners: dict[str, list[Callable]] = field(default_factory=dict)

    def on(self, event: str, callback: Callable) -> None:
        if event not in self._listeners:
            self._listeners[event] = []
        self._listeners[event].append(callback)

    def emit(self, event: str, *args, **kwargs) -> None:
        for callback in self._listeners.get(event, []):
            callback(*args, **kwargs)

    def off(self, event: str, callback: Callable) -> None:
        if event in self._listeners:
            self._listeners[event].remove(callback)

# Usage
emitter = EventEmitter()

def on_user_created(user: dict):
    print(f"User created: {user['name']}")

def send_welcome_email(user: dict):
    print(f"Sending email to {user['email']}")

emitter.on("user:created", on_user_created)
emitter.on("user:created", send_welcome_email)

emitter.emit("user:created", {"name": "Alice", "email": "alice@example.com"})
```

**Tip**: Event-based systems decouple components by communicating through named events. Use string event names with namespaces (e.g., "user:created") for clarity.

---
