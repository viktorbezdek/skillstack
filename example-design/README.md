# Example Design

> Design effective code examples, tutorials, and runnable samples with progressive complexity that teach concepts clearly.

## Overview

Code examples are the most-read part of any technical documentation, yet they are often an afterthought -- incomplete snippets with foo/bar variables that cannot be copy-pasted and do not actually run. This skill provides a systematic framework for creating examples that genuinely teach, progressing from minimal happy-path snippets to production-ready reference implementations.

The Example Design skill is aimed at developers writing documentation, API references, tutorials, and README files. It defines four example types (snippet, complete example, tutorial, reference app) with clear guidelines for length, structure, and quality. The progressive complexity framework ensures readers can start simple and build up to advanced usage without being overwhelmed.

As part of the SkillStack collection, this skill is a core dependency for the documentation-generator (API docs and tutorials), and it complements edge-case-coverage (adding error handling examples) and frontend-design (component usage examples). It provides the content quality standards that make other skills' output genuinely useful.

## What's Included

This skill is a focused methodology skill contained in a single `SKILL.md` file. It does not include separate references, scripts, templates, or examples directories -- all content is self-contained in the skill definition, providing concise, immediately actionable frameworks for designing examples.

## Key Features

- Four example types with clear purpose and length guidelines (Snippet: 5-15 lines, Complete: 20-50 lines, Tutorial: multi-file, Reference app: full project)
- Five-level progressive complexity framework (Minimal, Configuration, Error handling, Edge cases, Production-ready)
- Structured example anatomy (Context, Setup, Core concept, Result) ensuring every example is self-contained
- Quality checklist enforcing runnable, complete, minimal, commented, realistic, and tested examples
- Tutorial structure template with time estimates, prerequisites, step-by-step instructions, and next steps
- Anti-pattern identification (foo/bar variables, missing imports, outdated syntax, no expected output, untested code, unexplained walls of code)
- Copy-paste readiness as a first-class requirement for all example types

## Usage Examples

**Create API documentation examples:**
```
Write code examples for our REST API authentication endpoints.
```
Produces a progressive series: Level 1 shows basic token request, Level 2 adds configuration options, Level 3 adds error handling for expired/invalid tokens, Level 4 covers edge cases like rate limiting, Level 5 shows a production-ready auth wrapper with retry logic.

**Design a getting-started tutorial:**
```
Create a step-by-step tutorial for setting up our SDK.
```
Generates a structured tutorial with estimated time, prerequisites list, numbered steps with explanation-code-result blocks, and next steps linking to advanced topics.

**Improve existing code examples:**
```
Review our README examples and suggest improvements.
```
Applies the quality checklist to identify missing imports, foo/bar variables, lack of expected output, and examples that cannot be copy-pasted directly. Suggests specific improvements for each.

**Create component usage examples:**
```
Write usage examples for our Button component showing all variants.
```
Creates snippet-level examples for each variant (primary, secondary, destructive, outline), then a complete example showing composition, and finally a tutorial for building a custom variant.

**Write error handling examples:**
```
Show how to handle errors from our payment processing library.
```
Uses the progressive complexity framework to start with basic try/catch, then add specific error type handling, retry logic, timeout handling, and finally a production-ready error handling pattern with logging.

## Quick Start

1. **Determine your example type** based on what you are documenting:
   - Single concept? Use a **snippet** (5-15 lines)
   - Complete working code? Use a **complete example** (20-50 lines)
   - Teaching a workflow? Use a **tutorial** (multi-file, step-by-step)
   - Showing production patterns? Use a **reference app** (full project)

2. **Structure every example** with four parts:
   - Context: what this does (a comment or docstring)
   - Setup: prerequisites and imports
   - Core: the main concept, clearly highlighted
   - Result: expected output

3. **Apply progressive complexity** -- start with the simplest possible version that works, then layer on configuration, error handling, edge cases, and production concerns in separate examples.

4. **Run the quality checklist** before publishing:
   - Can it be copy-pasted and run immediately?
   - Are all imports included?
   - Is there any unrelated code that could be removed?
   - Are the key lines commented?
   - Does it use realistic variable names and data?
   - Has it been tested?

## Related Skills

- **documentation-generator** -- Uses example-design for API docs, tutorials, and getting-started guides
- **edge-case-coverage** -- Provides the error scenarios that Level 3-4 examples should demonstrate
- **frontend-design** -- Apply example design to component library documentation and storybook stories
- **debugging** -- Create minimal reproduction examples for bug reports

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `claude plugin add github:viktorbezdek/skillstack/example-design` -- 34 production-grade skills for Claude Code.
