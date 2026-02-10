# Consistency Standards

> Establish and maintain naming conventions, taxonomy standards, style guides, and reuse patterns across documentation and code.

## Overview

Inconsistency is one of the most common and insidious problems in codebases and documentation. When the same concept has three different names, when file naming follows no pattern, when documentation switches between "you" and "we" mid-paragraph -- users get confused and developers waste time. This skill provides a systematic approach to establishing and enforcing consistency across every layer of a project.

The Consistency Standards skill covers naming conventions (camelCase, PascalCase, snake_case, kebab-case), file naming patterns, terminology glossaries, voice and tone guidelines, and content reuse strategies. It addresses the DRY principle not just in code but in documentation, providing patterns for single-source content components, variables, conditionals, and templates that eliminate duplication and ensure updates propagate everywhere.

Within the SkillStack collection, this skill is a foundational cross-cutting concern. It supports API Design (consistent endpoint and field naming), Code Review (style consistency checks), Content Modelling (uniform type and field naming), and CI/CD Pipelines (consistent workflow naming and structure).

## What's Included

This skill is a self-contained reference in `SKILL.md` without additional subdirectories. All patterns, conventions, and checklists are included directly in the skill definition.

## Key Features

- **Case style reference**: Complete guide to camelCase, PascalCase, snake_case, kebab-case, and SCREAMING_SNAKE with when to use each
- **File naming conventions**: Structured `[type]-[name]-[variant].[ext]` pattern for predictable file organization
- **Terminology glossaries**: Template for defining canonical terms and their prohibited alternatives
- **Voice and tone guidelines**: Context-specific voice rules for instructions, errors, and success messages
- **Content reuse patterns**: Snippets, variables, conditionals, and templates for DRY documentation
- **Style audit checklist**: Actionable checklist for capitalization, date formats, UI element names, and glossary compliance
- **Anti-pattern detection**: Identifies synonym sprawl, inconsistent capitalization, mixed voice, and orphaned content

## Usage Examples

**Establish naming conventions for a new project:**
```
Define naming conventions for our TypeScript monorepo covering
files, components, variables, constants, and database columns.
```
Expected output: A comprehensive naming guide mapping each element type to its case style, with file naming patterns, component naming rules, and database column conventions with examples for each.

**Create a terminology glossary:**
```
Create a terminology glossary for our developer documentation
that standardizes how we refer to UI actions, system components,
and user roles.
```
Expected output: A glossary table with canonical terms, definitions, and "Do Not Use" alternatives -- e.g., use "click" not "press" or "hit", use "select" not "pick".

**Audit documentation for consistency:**
```
Review our documentation for consistency issues -- check for
mixed terminology, inconsistent capitalization, and voice changes.
```
Expected output: A categorized list of consistency violations organized by type (terminology, capitalization, voice, formatting) with specific locations and recommended fixes.

**Set up content reuse patterns:**
```
Our authentication setup instructions are duplicated across 5
different docs. Help us set up a content reuse pattern.
```
Expected output: A single-source content architecture using include directives and variables, with a shared authentication snippet and instructions for replacing duplicated content.

**Define voice and tone guidelines:**
```
Create voice and tone guidelines for our product's error messages,
success notifications, and help text.
```
Expected output: A voice and tone matrix mapping each message context to its recommended voice, with before/after examples showing how to transform existing copy.

## Quick Start

1. **Audit current state** -- Identify existing inconsistencies in naming, terminology, and voice
2. **Define case styles** -- Map each element type (variables, files, classes, URLs) to a case convention
3. **Build a glossary** -- List canonical terms for your domain with prohibited alternatives
4. **Set voice guidelines** -- Define voice and tone for each content context
5. **Create reuse patterns** -- Extract duplicated content into single-source snippets and variables
6. **Apply the style checklist** -- Run through the checklist to verify compliance
7. **Integrate into reviews** -- Add consistency checks to your code review process

## Related Skills

- **[Code Review](../code-review/)** -- Enforce consistency standards during code reviews
- **[API Design](../api-design/)** -- Apply consistent naming to endpoints, fields, and schemas
- **[Content Modelling](../content-modelling/)** -- Use consistent type and field naming in content models
- **[CI/CD Pipelines](../cicd-pipelines/)** -- Maintain consistent workflow naming and structure

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 34 production-grade skills for Claude Code.
