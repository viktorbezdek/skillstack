"""Shared library for the hindsight Claude Code integration hooks."""

from . import cli, transcript  # pyright: ignore[reportAttributeAccessIssue]  # noqa: F401

__all__ = ["cli", "transcript"]
