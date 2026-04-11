# Python Development

> **v1.1.24** | Development | 26 iterations

Comprehensive Python development skill covering modern tooling (uv, ruff, mypy, pytest), best practices, coding standards, library architecture, functional patterns, async programming, MicroPython, and production-grade development workflows.

## What Problem Does This Solve

Python's ecosystem has modernized significantly — pip, Black, flake8, and isort have been superseded by faster, simpler alternatives — but most developers are still working with outdated toolchains and patterns. Inconsistent dependency management, missing type annotations, and poor project structure cause builds that don't reproduce, type errors that slip to production, and codebases that resist refactoring. This skill encodes current best practices for Python 3.11+ with the modern toolchain (uv, ruff, mypy) from simple scripts to PyPI-published libraries.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Set up a new Python project with proper tooling" | Standard project setup using uv, ruff, mypy, and pytest with a complete pyproject.toml configuration |
| "Which Python package manager should I use?" | Tier selection guide (Minimal/Standard/Full) and uv commands replacing pip, virtualenv, and pip-tools |
| "My async code is blocking the event loop" | Async patterns with httpx.AsyncClient, asyncio.to_thread(), and the anti-patterns that cause blocking |
| "How do I structure a Python library for PyPI publishing" | Full project layout (src/ layout), pyproject.toml with Hatchling build system, and CI/CD publishing workflow |
| "Help me add type checking to my Python codebase" | mypy configuration for strict mode, modern type annotation syntax (list[str] not List[str]), and Protocol-based interfaces |
| "My Python code passes tests but has quality issues" | Quality gates checklist: ruff format, ruff check, mypy strict, pytest with >80% coverage, bandit for security |

## When NOT to Use This Skill

- TypeScript or JavaScript development -- use [typescript-development](../typescript-development/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install python-development@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the python-development skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `python`
- `uv`
- `ruff`
- `mypy`
- `pytest`
- `fastapi`

## What's Inside

- **Quick Start** -- Tier selection table (Minimal/Standard/Full) and a complete Standard project setup sequence from uv init to running quality checks.
- **Core Principles** -- Six non-negotiable practices: uv for everything, type hints everywhere, ruff for quality, pytest for testing, locked dependencies, and PEP 723 for scripts.
- **Modern Python Toolchain (2024-2025)** -- Command reference for uv (dependency management), ruff (linting and formatting), and mypy (type checking) replacing the legacy pip/Black/flake8 stack.
- **Project Structure** -- Canonical src/ layout with pyproject.toml configuration for ruff, mypy, and pytest settings.
- **Anti-Patterns to Avoid** -- Table of nine common Python mistakes (mutable defaults, blocking async, inheritance overuse, bare except) with their correct replacements.
- **Quality Gates** -- Five mandatory checks every Python task must pass before completion, plus stricter thresholds (>95% coverage, bandit security scan) for critical code.
- **Official Documentation** -- Direct links to Python, uv, ruff, mypy, pytest, and PEP index documentation.

## Version History

- `1.1.24` fix(languages+tools): optimize descriptions for git-workflow, mcp-server, python, typescript (b65bc7d)
- `1.1.23` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.1.22` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.1.21` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.1.20` refactor: remove old file locations after plugin restructure (a26a802)
- `1.1.19` docs: update README and install commands to marketplace format (af9e39c)
- `1.1.18` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.1.17` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.1.16` fix: make all shell scripts executable and fix Python syntax errors (61ac964)
- `1.1.15` docs: add detailed README documentation for all 34 skills (7ba1274)

## Related Skills

- **[Api Design](../api-design/)** -- Comprehensive API design skill for REST, GraphQL, gRPC, and Python library architectures. Design endpoints, schemas, aut...
- **[Debugging](../debugging/)** -- Comprehensive debugging skill combining systematic debugging methodology, browser DevTools automation, E2E testing with ...
- **[Frontend Design](../frontend-design/)** -- Comprehensive Frontend Design (UI/UX) skill combining UI design systems, component libraries, CSS/Tailwind styling, acce...
- **[Gws Cli](../gws-cli/)** -- Google Workspace CLI (gws) skill for managing Drive, Gmail, Sheets, Calendar, Docs, Chat, Tasks, and 11 more Workspace A...
- **[Mcp Server](../mcp-server/)** -- Comprehensive MCP (Model Context Protocol) server development skill. Build, configure, and manage MCP servers using Pyth...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
