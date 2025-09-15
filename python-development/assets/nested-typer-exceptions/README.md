# Exception Chain Explosion Demonstration Scripts

This directory contains executable demonstration scripts showing the anti-pattern of exception chain explosion in Typer CLI applications and the correct patterns to prevent it.

## Quick Reference

| Script                                                                                                                     | Output     | Purpose                                                    |
| -------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------------------------------------------------------- |
| [nested-typer-exception-explosion.py](./nested-typer-exception-explosion.py)                                               | ~220 lines | Shows the anti-pattern with 7 layers of exception wrapping |
| [nested-typer-exception-explosion_naive_workaround.py](./nested-typer-exception-explosion_naive_workaround.py)             | ~80 lines  | Shows the isinstance band-aid workaround                   |
| [nested-typer-exception-explosion_corrected_typer_echo.py](./nested-typer-exception-explosion_corrected_typer_echo.py)     | 1 line     | Correct pattern using typer.echo                           |
| [nested-typer-exception-explosion_corrected_rich_console.py](./nested-typer-exception-explosion_corrected_rich_console.py) | 1 line     | Correct pattern using Rich Console                         |

## Running the Scripts

All scripts use PEP 723 inline script metadata and can be run directly:

```bash
# Run directly (uv handles dependencies automatically)
./nested-typer-exception-explosion.py broken.json

# Or explicitly with uv
uv run nested-typer-exception-explosion.py broken.json
```

The scripts will create `broken.json` with invalid content if it doesn't exist.

## The Problem

**Anti-pattern:** Every function catches and re-wraps exceptions → 220 lines of traceback for "file not found"

**Correct pattern:** Let exceptions bubble naturally, only catch at specific points → 1 line of clean output

## Documentation

For detailed explanations, code patterns, and best practices, see:

**[Exception Handling in Python CLI Applications with Typer](../../references/exception-handling.md)**

This comprehensive guide includes:

- Complete explanation of the exception chain explosion problem
- Correct patterns using `typer.Exit` subclasses
- When to catch exceptions and when to let them bubble
- Full code examples with detailed annotations
- DO/DON'T guidelines

## External References

- [Typer Terminating Documentation](https://github.com/fastapi/typer/blob/master/docs/tutorial/terminating.md)
- [Typer Exceptions Documentation](https://github.com/fastapi/typer/blob/master/docs/tutorial/exceptions.md)
- [Typer Printing Documentation](https://github.com/fastapi/typer/blob/master/docs/tutorial/printing.md)
