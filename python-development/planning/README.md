# Planning Directory

## Purpose

This directory contains **historical architectural proposals and planning documents** that were created during the development of the python3-development skill but were **not implemented** in the final design.

## Contents

### reference-document-architecture.md

A comprehensive 2500+ line architectural proposal that outlined a different structure for the python3-development skill than what was ultimately implemented.

**Proposed Structure** (in this document):

- `docs/scenarios/` - Scenario-specific guides (CLI, TUI, modules, scripts)
- `docs/standards/` - Cross-cutting standards and patterns
- `docs/frameworks/` - Framework-specific deep dives

**Actual Implemented Structure** (current):

- `references/` - Reference documentation and module guides
- `commands/` - Command patterns and orchestration workflows

**Why It's Archived:**

- The document proposed an architecture that was never implemented
- The skill evolved in a different direction with simpler organization
- Preserving it provides historical context for design decisions
- Contains valuable thinking about progressive disclosure and token optimization

**Status:** Historical proposal, not implemented

**Note on Document Quality:** This archived document may contain markdown linting issues (e.g., code blocks without language specifiers). These have been preserved as-is to maintain the historical record. Do not use this document as a template for new documentation.

## Usage

These documents are **read-only archives**. They should not be used as current guidance for the python3-development skill. For current documentation, see:

- `../SKILL.md` - Current skill orchestration and usage
- `../references/` - Current reference documentation
- `../commands/` - Current command patterns

## When to Reference Planning Documents

Reference these documents when:

- Understanding the evolution of the skill's design
- Researching alternative architectural approaches
- Learning about decision-making processes
- Considering major architectural changes

**Do not** reference these documents for:

- Current usage patterns
- Active development guidance
- Implementation details
