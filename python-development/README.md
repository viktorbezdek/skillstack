# Python Development

> Comprehensive Python development skill covering modern tooling (uv, ruff, mypy, pytest), best practices, coding standards, library architecture, functional patterns, async programming, MicroPython, and production-grade development workflows.

## Overview

Python development in 2024-2025 looks radically different from even two years ago. The toolchain has been revolutionized by uv (10-100x faster than pip), ruff (replaces Black, flake8, and isort in one tool), and modern Python 3.11-3.14+ features. This skill encodes all of that knowledge so you get current best practices by default, not outdated patterns that LLMs often suggest from their training data.

This skill covers the full spectrum from simple single-file scripts to production-grade systems, library architecture, and even embedded development with MicroPython. It is designed for Python developers at any level who want to write modern, type-safe, well-tested code using the latest tooling ecosystem.

Within the SkillStack collection, Python Development is one of the core language skills. It provides the foundation for any Python-based project and pairs well with the TDD skill (for test-driven workflows), the Code Review skill (for quality auditing), and the Risk Management skill (for production deployment safety).

## What's Included

### References
- **accessing_online_resources.md** -- Guidelines for fetching and working with online resources
- **api_reference.md** -- Python API design patterns and conventions
- **architectural-principles.md** -- Software architecture principles for Python projects
- **async-patterns.md** -- Async/await patterns, event loops, and concurrency
- **code-quality-tools.md** -- Configuration and usage of ruff, mypy, bandit, and other quality tools
- **common-libraries.md** -- Curated guide to recommended Python libraries by domain
- **conventions-and-style.md** -- Coding style conventions and naming standards
- **dependency-management.md** -- Managing dependencies with uv, lockfiles, and version constraints
- **display_rendering.md** -- Terminal display and Rich console rendering patterns
- **docstrings-documentation.md** -- Documentation standards and docstring formats
- **exception-handling.md** -- Exception hierarchy design and error handling patterns
- **extended-patterns.md** -- Advanced code patterns, testing, async, itertools/functools, and library architecture
- **functional-reference.md** -- Functional programming patterns in Python
- **index.md** -- Reference index and navigation guide
- **micropython_async.md** -- Async patterns specific to MicroPython
- **modern-modules.md** -- Guide to modern Python modules and when to use them
- **packaging-distribution.md** -- Building and publishing Python packages to PyPI
- **pep-standards.md** -- Key PEP standards and their practical application
- **PEP723.md** -- PEP 723 inline script metadata for single-file scripts
- **performance-optimization.md** -- Performance profiling and optimization techniques
- **presto_hardware.md** -- Hardware integration with Presto/RP2350
- **project-structure.md** -- Recommended project layouts and organization
- **python-development-orchestration.md** -- Orchestration patterns for complex Python workflows
- **security-best-practices.md** -- Security scanning, dependency auditing, and secure coding
- **skill-evaluation-scenarios.md** -- Scenarios for evaluating Python development quality
- **testing-methodology.md** -- Testing strategies, fixtures, parametrization, and coverage
- **tool-library-registry.md** -- Registry of tools and libraries with version recommendations
- **type-hints.md** -- Modern type hint patterns (Python 3.11+ style)
- **user-project-conventions.md** -- Conventions for user-facing project configuration
- **uv.md** -- Complete uv package manager reference

### References: Installation Guides
- **installation/linux.md** -- Python and uv setup on Linux
- **installation/macos.md** -- Python and uv setup on macOS
- **installation/overview.md** -- Cross-platform installation overview
- **installation/windows.md** -- Python and uv setup on Windows

### References: Modern Modules
- Detailed guides for 18 modern Python libraries including **httpx**, **attrs**, **arrow**, **prefect**, **fabric**, **GitPython**, **paho-mqtt**, **robotframework**, **uvloop**, and more

### References: mypy Documentation
- **mypy-docs/additional_features.rst** -- Advanced mypy features
- **mypy-docs/generics.rst** -- Generic types in mypy
- **mypy-docs/protocols.rst** -- Structural subtyping with Protocols
- **mypy-docs/type_narrowing.rst** -- Type narrowing techniques
- **mypy-docs/typed_dict.rst** -- TypedDict patterns

### Scripts
- **setup-project.sh** -- Initialize a new Python project with full tooling
- **check-code-quality.sh** -- Run all quality checks (ruff, mypy, pytest) in sequence
- **ble_gatt_server.py** -- BLE GATT server example for MicroPython/embedded
- **mqtt_client.py** -- MQTT client implementation example
- **rgb_backlight.py** -- RGB backlight controller for embedded hardware
- **touch_handler.py** -- Touch input handler for embedded displays

### Templates
- **test-template.py** -- Pytest test file template with fixtures and parametrization

### Assets
- **pyproject.toml.template** -- Production-ready pyproject.toml configuration template
- **pyproject-toml-template.toml** -- Alternative pyproject.toml template
- **README.md.template** -- Project README template
- **CONTRIBUTING.md.template** -- Contributing guidelines template
- **example-config.py** -- Example configuration module
- **example-exceptions.py** -- Example custom exception hierarchy
- **example.pre-commit-config.yaml** -- Pre-commit hooks configuration
- **hatch_build.py** -- Custom Hatch build hook example
- **project-structure.txt** -- Reference project directory layout
- **test-structure.txt** -- Reference test directory layout
- **version.py** -- Version management module example
- **nested-typer-exceptions/** -- Typer nested exception handling examples (4 files)
- **typer_examples/** -- Rich console and Typer integration examples

### Cookbook
- **async.md** -- Async programming recipes and patterns
- **design-patterns.md** -- Python design pattern implementations
- **modern.md** -- Modern Python idioms and features (3.11+)
- **patterns.md** -- Common coding patterns and solutions
- **testing.md** -- Testing recipes and advanced pytest techniques

### Workflows
- **Project.md** -- New project setup workflow
- **Deps.md** -- Dependency management workflow
- **Lint.md** -- Linting and formatting workflow
- **Test.md** -- Testing workflow
- **Type.md** -- Type checking workflow
- **Package.md** -- Packaging and distribution workflow
- **Script.md** -- Single-file script workflow (PEP 723)
- **Workspace.md** -- Multi-project workspace workflow

### Tools
- **python-check** -- Combined quality check tool
- **python-lint** -- Linting automation tool

### Commands
- **development/** -- Development command templates and patterns
- **testing/** -- Test analysis and failure investigation commands

### Resources
- **advanced-patterns.md** -- Advanced Python patterns reference
- **configs/pyproject.toml** -- Reference pyproject.toml configuration

## Key Features

- **Modern toolchain**: uv for package management, ruff for linting/formatting, mypy for type checking, pytest for testing
- **Three-tier project approach**: Minimal (scripts), Standard (team projects), and Full (PyPI packages) with appropriate tooling for each
- **Type-first development**: Modern type hints everywhere using Python 3.11+ syntax (list[str] not List[str])
- **Quality gates**: Automated format -> lint -> type-check -> test pipeline with configurable coverage thresholds
- **Async programming**: Complete async/await patterns including httpx, asyncio, and MicroPython async
- **Library architecture**: Patterns for building, packaging, and publishing Python libraries to PyPI
- **Embedded/MicroPython**: Support for MicroPython development targeting RP2350 and similar hardware
- **Anti-pattern prevention**: Active detection of common mistakes (mutable defaults, bare excepts, blocking in async, etc.)

## Usage Examples

Set up a new Python project with modern tooling:
```
Create a new Python project called "data-pipeline" with uv, ruff, mypy, and pytest configured. It should process CSV files and output JSON.
```

Write a well-tested async service:
```
Build an async HTTP client service using httpx that fetches data from multiple APIs concurrently, with proper error handling, retries, and type hints. Include pytest tests with fixtures.
```

Refactor legacy code to modern patterns:
```
Refactor this Python file to use modern patterns: replace List/Dict imports with built-in generics, add type hints, use dataclasses instead of plain dicts, and fix the mutable default argument.
```

Create a CLI application:
```
Build a Typer CLI tool that manages database migrations. It should have commands for create, up, down, and status. Use Rich for terminal output.
```

Set up a PEP 723 single-file script:
```
Write a standalone Python script with PEP 723 inline metadata that fetches weather data from an API and formats it as a table. It should be runnable with just `uv run script.py`.
```

## Quick Start

1. Start with a Python task -- writing new code, reviewing existing code, or setting up a project.
2. The skill auto-selects the appropriate tier: Minimal for scripts, Standard for projects, Full for packages.
3. All code output follows modern conventions: type hints, ruff-compliant formatting, proper error handling.
4. Quality gates run automatically: `uv run ruff format .` -> `uv run ruff check .` -> `uv run mypy .` -> `uv run pytest`.
5. For embedded work, mention MicroPython or RP2350 to activate hardware-specific patterns.

## Related Skills

- **TDD (Test-Driven Development)** -- Complement Python development with test-first methodology
- **Code Review** -- Audit Python codebases for quality and best practices
- **Risk Management** -- Assess deployment risks for production Python systems
- **Prompt Engineering** -- Build LLM-powered Python applications with optimized prompts

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 34 production-grade skills for Claude Code.
