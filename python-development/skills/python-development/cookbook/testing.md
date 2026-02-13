# Testing Cookbook

pytest patterns and fixtures for Python 3.14+.

---

## Setup pytest with Coverage

**Problem**: Need to configure pytest with coverage reporting and best practices for a Python project.

**Solution**:
```bash
uv add --dev pytest pytest-cov pytest-asyncio
```

```toml
# pyproject.toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
addopts = """
    --cov=src
    --cov-report=term-missing
    --cov-report=html
    --cov-fail-under=80
    -v
    --strict-markers
"""
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
]
asyncio_mode = "auto"
```

**Tip**: Use `asyncio_mode = "auto"` to avoid decorating every async test with `@pytest.mark.asyncio`.

---

## Write Basic Unit Tests

**Problem**: Need to test class methods, validation, and equality in a structured way.

**Solution**:
```python
# tests/test_entities.py
import pytest
from my_project.entities import User

class TestUser:
    def test_user_creation(self):
        user = User(name="Alice", email="alice@example.com")
        assert user.name == "Alice"
        assert user.email == "alice@example.com"

    def test_user_validation_raises(self):
        with pytest.raises(ValueError) as exc_info:
            User(name="", email="invalid")
        assert "name cannot be empty" in str(exc_info.value)

    def test_user_equality(self):
        user1 = User(name="Alice", email="a@b.com")
        user2 = User(name="Alice", email="a@b.com")
        assert user1 == user2
```

**Tip**: Group related tests in classes with the `Test` prefix for better organization and shared setup.

---

## Test Exceptions

**Problem**: Need to verify that code raises the correct exceptions with specific messages.

**Solution**:
```python
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_value_error_message():
    with pytest.raises(ValueError, match=r"must be positive"):
        create_user(age=-1)
```

**Tip**: Use the `match` parameter with a regex pattern to verify exception messages contain expected text.

---

## Compare Floating Point Numbers

**Problem**: Floating point arithmetic can produce slightly different results that fail equality checks.

**Solution**:
```python
def test_float_comparison():
    result = 0.1 + 0.2
    assert result == pytest.approx(0.3)

def test_with_tolerance():
    assert 2.0 == pytest.approx(2.1, abs=0.2)
    assert 2.0 == pytest.approx(2.02, rel=0.02)
```

**Tip**: Use `abs` for absolute tolerance (fixed margin) or `rel` for relative tolerance (percentage-based).

---

## Create Reusable Test Fixtures

**Problem**: Tests need shared setup objects like users or database connections with proper cleanup.

**Solution**:
```python
# tests/conftest.py
import pytest
from my_project.entities import User
from my_project.database import Database

@pytest.fixture
def user():
    """Create test user."""
    return User(name="Alice", email="alice@example.com")

@pytest.fixture
def database():
    """Create and cleanup test database."""
    db = Database(":memory:")
    db.create_tables()
    yield db
    db.close()

# tests/test_services.py
def test_save_user(database, user):
    database.save(user)
    assert database.get_user(user.id) == user
```

**Tip**: Use `yield` in fixtures to run cleanup code after the test completes, ensuring resources are properly released.

---

## Control Fixture Scope

**Problem**: Some fixtures are expensive to create and should be shared across multiple tests.

**Solution**:
```python
@pytest.fixture(scope="session")
def app():
    """Shared across all tests in session."""
    return create_app()

@pytest.fixture(scope="module")
def client(app):
    """Shared within a test module."""
    return app.test_client()

@pytest.fixture(scope="class")
def users():
    """Shared within a test class."""
    return [User(name=f"User{i}") for i in range(10)]

@pytest.fixture  # scope="function" is default
def temp_file():
    """Created fresh for each test."""
    with tempfile.NamedTemporaryFile() as f:
        yield f
```

**Tip**: Use `scope="session"` for expensive one-time setup like database connections, and `scope="function"` (default) for test isolation.

---

## Run Tests with Multiple Backend Implementations

**Problem**: Need to verify code works with different database backends or configurations.

**Solution**:
```python
@pytest.fixture(params=["postgres", "mysql", "sqlite"])
def database(request):
    """Run tests with multiple database backends."""
    db_type = request.param
    db = create_database(db_type)
    yield db
    db.close()
```

**Tip**: Parameterized fixtures automatically run all tests using the fixture multiple times, once per parameter value.

---

## Create Factory Fixtures

**Problem**: Need to create multiple instances of an object with different attributes in a single test.

**Solution**:
```python
@pytest.fixture
def make_user():
    """Factory fixture for creating users with custom attributes."""
    def _make_user(name: str = "Test", age: int = 25):
        return User(name=name, age=age)
    return _make_user

def test_multiple_users(make_user):
    alice = make_user(name="Alice", age=30)
    bob = make_user(name="Bob", age=25)
    assert alice.name != bob.name
```

**Tip**: Factory fixtures return a callable function, allowing flexible object creation with custom parameters in each test.

---

## Test with Multiple Input Values

**Problem**: Need to test the same function with many different input/output combinations.

**Solution**:
```python
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
    (0, 0),
    (-1, -2),
])
def test_double(input, expected):
    assert double(input) == expected
```

**Tip**: Parametrize creates a separate test for each tuple, making it easy to spot which specific inputs fail.

---

## Test All Combinations of Parameters

**Problem**: Need to test a function with every combination of two or more parameter sets.

**Solution**:
```python
@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [10, 20])
def test_multiply(x, y):
    # Runs 6 times: (1,10), (1,20), (2,10), (2,20), (3,10), (3,20)
    assert multiply(x, y) == x * y
```

**Tip**: Stacking multiple `@pytest.mark.parametrize` decorators creates the cartesian product of all parameters.

---

## Add Descriptive Test IDs

**Problem**: Parametrized test names like `test_age[0]` don't clearly indicate what's being tested.

**Solution**:
```python
@pytest.mark.parametrize("age,valid", [
    pytest.param(18, True, id="adult"),
    pytest.param(17, False, id="minor"),
    pytest.param(65, True, id="senior"),
    pytest.param(-1, False, id="negative"),
])
def test_age_validation(age, valid):
    if valid:
        user = User(name="Test", age=age)
        assert user.age == age
    else:
        with pytest.raises(ValueError):
            User(name="Test", age=age)
```

**Tip**: Custom IDs make test output readable: `test_age_validation[adult]` instead of `test_age_validation[18-True]`.

---

## Test Async Functions

**Problem**: Need to test asynchronous functions and coroutines.

**Solution**:
```python
# tests/test_async.py
import pytest
from my_project.services import AsyncUserService

@pytest.mark.asyncio
async def test_fetch_user():
    service = AsyncUserService()
    user = await service.get_user(1)
    assert user.name == "Alice"

@pytest.mark.asyncio
async def test_fetch_multiple_users():
    service = AsyncUserService()
    users = await service.get_users([1, 2, 3])
    assert len(users) == 3
```

**Tip**: With `asyncio_mode = "auto"` in config, you can omit the `@pytest.mark.asyncio` decorator.

---

## Create Async Fixtures

**Problem**: Tests need async setup like HTTP clients or database connections.

**Solution**:
```python
@pytest.fixture
async def async_client():
    import httpx
    async with httpx.AsyncClient() as client:
        yield client

@pytest.mark.asyncio
async def test_api_call(async_client):
    response = await async_client.get("https://api.example.com/users")
    assert response.status_code == 200
```

**Tip**: Async fixtures automatically handle async context managers and cleanup with async generators.

---

## Mock External Dependencies

**Problem**: Tests shouldn't call real databases or external APIs.

**Solution**:
```python
from unittest.mock import Mock, patch, AsyncMock

def test_with_mock():
    mock_db = Mock()
    mock_db.query.return_value = [{"id": 1, "name": "Alice"}]

    service = UserService(db=mock_db)
    result = service.get_users()

    assert len(result) == 1
    mock_db.query.assert_called_once()
```

**Tip**: Use `return_value` to set what the mock returns, and `assert_called_once()` to verify it was used correctly.

---

## Patch Module-Level Functions

**Problem**: Need to mock imported functions like `requests.get` without modifying the code under test.

**Solution**:
```python
@patch("my_project.services.requests.get")
def test_external_api(mock_get):
    mock_get.return_value.json.return_value = {"status": "ok"}

    result = call_external_api()

    assert result["status"] == "ok"
    mock_get.assert_called_once()

def test_with_context_manager():
    with patch("my_project.services.database") as mock_db:
        mock_db.query.return_value = []
        result = get_users()
        assert result == []
```

**Tip**: Use the full import path where the function is used, not where it's defined: `my_project.services.requests`, not `requests`.

---

## Mock Async Functions

**Problem**: Need to mock async functions and verify they were awaited.

**Solution**:
```python
@pytest.fixture
async def mock_api():
    api = AsyncMock()
    api.fetch.return_value = {"status": "ok"}
    return api

@pytest.mark.asyncio
async def test_async_service(mock_api):
    service = AsyncService(api=mock_api)
    result = await service.process()

    assert result["status"] == "ok"
    mock_api.fetch.assert_awaited_once()
```

**Tip**: Use `AsyncMock` instead of `Mock` for async functions, and `assert_awaited_once()` instead of `assert_called_once()`.

---

## Mock Context Managers

**Problem**: Need to mock objects that use `__enter__` and `__exit__` like file handles.

**Solution**:
```python
from unittest.mock import MagicMock

def test_context_manager():
    mock_file = MagicMock()
    mock_file.__enter__.return_value = mock_file
    mock_file.read.return_value = "content"

    with mock_file as f:
        assert f.read() == "content"
```

**Tip**: `MagicMock` automatically implements magic methods like `__enter__`, `__exit__`, `__len__`, and `__iter__`.

---

## Spy on Real Objects

**Problem**: Want to verify a method was called while still executing the real implementation.

**Solution**:
```python
from unittest.mock import patch

def test_spy_on_method():
    user = User(name="Alice")

    with patch.object(user, "validate", wraps=user.validate) as spy:
        user.save()
        spy.assert_called_once()
```

**Tip**: The `wraps` parameter creates a spy that tracks calls but still executes the original method.

---

## Generate Coverage Reports

**Problem**: Need to know which lines of code are tested and identify gaps.

**Solution**:
```bash
# Basic coverage
uv run pytest --cov=src

# With missing lines
uv run pytest --cov=src --cov-report=term-missing

# HTML report
uv run pytest --cov=src --cov-report=html
open htmlcov/index.html

# Fail if below threshold
uv run pytest --cov=src --cov-fail-under=80
```

**Tip**: Use `--cov-report=term-missing` during development to quickly see uncovered lines, and HTML reports for detailed analysis.

---

## Configure Coverage Exclusions

**Problem**: Some lines like debug code or type checking shouldn't count against coverage.

**Solution**:
```toml
# pyproject.toml
[tool.coverage.run]
source = ["src"]
branch = true
omit = ["tests/*", "*/__main__.py"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise NotImplementedError",
    "if TYPE_CHECKING:",
]
fail_under = 80
```

**Tip**: Enable `branch = true` to measure branch coverage, not just line coverage, for more thorough testing.

---

## Organize Tests by Type

**Problem**: Large projects need structure to separate unit, integration, and end-to-end tests.

**Solution**:
```
tests/
├── conftest.py           # Shared fixtures
├── unit/
│   ├── test_entities.py
│   └── test_services.py
├── integration/
│   └── test_api.py
└── e2e/
    └── test_workflow.py
```

**Tip**: Place shared fixtures in `conftest.py` at each level to make them available to all tests in that directory and subdirectories.

---

## Mark Tests by Category

**Problem**: Need to selectively run slow tests, integration tests, or exclude certain categories.

**Solution**:
```python
import pytest

@pytest.mark.slow
def test_slow_operation():
    ...

@pytest.mark.integration
def test_database_integration():
    ...

# Run only fast tests
# uv run pytest -m "not slow"

# Run only integration tests
# uv run pytest -m integration
```

**Tip**: Define markers in `pyproject.toml` with descriptions to document what each marker means and enable `--strict-markers`.

---

## Common pytest Commands

**Problem**: Need quick reference for running tests in different ways during development.

**Solution**:
```bash
# Run all tests
uv run pytest

# Verbose output
uv run pytest -v

# Stop on first failure
uv run pytest -x

# Run specific test
uv run pytest tests/test_user.py::TestUser::test_creation

# Run tests matching pattern
uv run pytest -k "user and not slow"

# Show print statements
uv run pytest -s

# Run last failed
uv run pytest --lf

# Parallel execution (requires pytest-xdist)
uv run pytest -n auto
```

**Tip**: Use `pytest -x --lf` during development to quickly iterate: stop on first failure, then rerun only failures on next run.

---
