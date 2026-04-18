---
name: ux-writing
description: >-
  Write effective microcopy, error messages, button labels, and interface text using
  UX writing principles. Use when crafting microcopy, UX copy, interface text, error
  messages, button labels, empty states, or conversational UI text. NOT for generating
  documentation (use documentation-generator). NOT for writing marketing copy or brand
  voice guidelines (use storytelling for narrative, not UI microcopy). NOT for designing
  the UI itself (use frontend-design or navigation-design).
---

# UX Writing

Write clear, helpful, human interface text.

## When to use this skill

- Writing or rewriting button labels, error messages, form labels, empty states
- Crafting conversational UI text (chatbots, onboarding flows, tooltips)
- Improving the clarity of interface copy in an existing product
- Setting up a tone-of-voice guide for a product's UI text
- Reviewing UI copy for consistency across a product

## When NOT to use this skill

- **Long-form documentation** → use `documentation-generator`
- **Marketing copy or brand narratives** → use `storytelling`
- **Designing UI layouts or components** → use `frontend-design` or `navigation-design`
- **Content strategy or information architecture** → use `content-modelling`

---

## Decision tree

```
What are you writing?
  │
  ├─ A button label or CTA
  │   └─ Formula: [Verb] + [Object]. Start with the action, name the thing.
  │
  ├─ An error message
  │   └─ Formula: What happened + Why + What to do next. Never blame the user.
  │
  ├─ An empty state
  │   └─ Formula: Why it's empty + How to fill it. Encourage, don't shame.
  │
  ├─ A confirmation dialog
  │   └─ Formula: Consequence + Irreversibility (if any) + Clear action/negative buttons
  │
  ├─ A tooltip or help text
  │   └─ Formula: One sentence max. Explain the non-obvious, skip the obvious.
  │
  └─ Onboarding or conversational UI flow
      └─ Map the emotional arc: uncertain → guided → confident. Adjust tone per step.
```

---

## Core Principles

| Principle | Description | Bad Example | Good Example |
|-----------|-------------|-------------|--------------|
| **Clear** | Simple words, active voice | "Authentication failed" | "Your password is incorrect" |
| **Concise** | Front-load key info | "In order to proceed, you must first" | "To continue," |
| **Useful** | Provide next steps | "Error 404" | "Page not found. Try searching or go to homepage." |
| **Human** | Empathetic, conversational | "Invalid input" | "Please enter a valid email address" |

## Tone by Context

| Context | Tone | Example |
|---------|------|---------|
| Success | Celebratory | "You're all set!" |
| Error | Helpful, not blaming | "Let's fix this" |
| Warning | Direct, honest | "This can't be undone" |
| Empty | Encouraging | "Create your first project" |
| Loading | Transparent | "Finding your files..." |

## UI Patterns

### Buttons
```
X Click here    -> Download report
X Submit        -> Save changes
```
Formula: [Verb] + [Object]

### Error Messages
```
X Error 404

-> Page not found
   Try searching or go to homepage.
```

### Confirmation Dialogs
```
Delete "Report"?
This can't be undone.
[Delete] [Cancel]
```

### Form Labels
```
Email address
[name@example.com]
We'll send a confirmation link.
```

## Anti-Patterns

1. **Blaming the user** — "You entered an invalid email" implies the user did something wrong. Fix: "Please enter a valid email address" — the system needs valid input, the user isn't at fault.
2. **Jargon and system language** — "Error 500: Internal Server Error" exposes backend terminology. Fix: "Something went wrong on our end. Try again in a moment."
3. **Dead-end messages** — errors or empty states with no next step. Fix: every message should include what the user can do next (retry, search, contact support).
4. **Vague button labels** — "OK", "Submit", "Cancel" without context. Fix: label buttons with the specific action — "Delete project", "Send invitation", "Save changes".
5. **Overly formal tone** — "Your request has been processed successfully" in a consumer product. Fix: "Done!" unless the context demands formality (legal, financial).
6. **Inconsistent terminology** — "Delete" in one place, "Remove" in another for the same action. Fix: pick one term and use it everywhere; create a microcopy glossary.
7. **Confirmations without consequences** — "Are you sure?" without explaining what will happen. Fix: "Delete this project? All 23 tasks will be permanently removed."
