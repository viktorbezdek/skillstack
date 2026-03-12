# UX Writing

> Write clear, helpful, human interface text including microcopy, error messages, button labels, empty states, and conversational UI.

## Overview

Every word in a user interface is a design decision. Poorly written error messages confuse users, vague button labels slow them down, and empty states without guidance lead to abandonment. This skill provides a systematic approach to writing interface text that is clear, concise, useful, and human, covering every UI pattern from buttons and form labels to error messages, confirmation dialogs, and empty states.

The skill defines tone-by-context rules so that success states feel celebratory, error states feel helpful rather than blaming, warnings are direct and unambiguous, and empty states are encouraging rather than barren. Every pattern follows a consistent formula that can be applied across any product.

Within the SkillStack collection, this skill works naturally alongside user-journey-design (providing the right copy at each touchpoint), persona-definition (tailoring voice to the audience), and navigation-design (labeling navigation elements effectively).

## What's Included

This is a focused skill with all guidance contained in a single SKILL.md file. It does not include separate reference, template, script, or example directories. The core principles, tone-by-context rules, and UI pattern formulas are all embedded directly in the skill definition.

## Key Features

- **Four core principles** for interface text: Clear (simple words, active voice), Concise (front-loaded key info), Useful (provides next steps), and Human (empathetic, conversational)
- **Tone-by-context framework** with specific tonal guidance for success, error, warning, and empty states
- **Button copy formula** using the [Verb] + [Object] pattern to replace generic labels like "Submit" or "Click here"
- **Error message pattern** that replaces cryptic codes with human-readable descriptions and actionable next steps
- **Confirmation dialog structure** with clear consequence statements and action-labeled buttons
- **Form label guidance** including placeholder text and helper text conventions
- **Empty state patterns** that encourage action rather than presenting a dead end

## Usage Examples

### Write error messages for a form validation flow

```
Write UX-friendly error messages for a registration form with fields: email, password (min 8 chars, 1 uppercase, 1 number), and username (3-20 chars, alphanumeric only).
```

Produces specific, helpful error messages for each validation rule, such as "Password needs at least one uppercase letter" instead of "Invalid password format", with inline placement guidance.

### Rewrite generic button labels across an app

```
Rewrite these button labels to be more specific: "Submit", "OK", "Click here", "Go", "Yes", "Proceed".
```

Transforms each label using the [Verb] + [Object] formula, producing context-appropriate alternatives like "Save changes", "Create account", "Download report" based on the action being performed.

### Design empty states for a project management tool

```
Write empty state copy for these screens in a project management app: projects list, task board, team members, and activity feed.
```

Creates encouraging empty state messages with clear calls to action, such as "No projects yet. Create your first project to get started." with a prominent action button label.

### Write a confirmation dialog for a destructive action

```
Write the confirmation dialog copy for permanently deleting a user account, including all associated data (projects, files, comments).
```

Produces a dialog with a clear title ("Delete your account?"), specific consequence statement ("This permanently removes all your projects, files, and comments. This cannot be undone."), and action-labeled buttons (["Delete my account", "Keep my account"]).

### Create onboarding tooltip copy

```
Write tooltip microcopy for a 4-step onboarding tour of a dashboard: navigation sidebar, search bar, notifications bell, and user settings.
```

Produces concise, action-oriented tooltips that explain what each element does and invite exploration, following the clear-concise-useful-human principles.

## Quick Start

1. **Identify the context** - Determine what state the user is in (success, error, warning, empty, neutral) to set the right tone.
2. **Apply the principles** - Write text that is clear (no jargon), concise (front-load the key info), useful (include a next step), and human (use "you" and conversational language).
3. **Use the formulas** - For buttons, use [Verb] + [Object]. For errors, use [What happened] + [How to fix it]. For empty states, use [What goes here] + [How to start].
4. **Read it aloud** - If the text sounds robotic or confusing when spoken, rewrite it.
5. **Cut by half** - After your first draft, try to cut the word count in half while preserving meaning.

## Related Skills

- [user-journey-design](../user-journey-design/) - Map the journey touchpoints where interface text appears
- [persona-definition](../persona-definition/) - Define the audience to calibrate voice and vocabulary
- [navigation-design](../navigation-design/) - Apply UX writing to navigation labels and wayfinding
- [content-modelling](../content-modelling/) - Structure content models that support consistent copy
- [frontend-design](../frontend-design/) - Frontend design patterns that incorporate UX writing best practices
- [example-design](../example-design/) - Design clear examples and tutorials with effective instructional text

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `claude plugin add github:viktorbezdek/skillstack/ux-writing` — 34 production-grade skills for Claude Code.
