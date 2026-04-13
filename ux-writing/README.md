# UX Writing

> **v1.0.10** | Design & UX | 11 iterations

> Turn "Submit", "Error 404", and "Click here" into interface text that actually helps users succeed.

## The Problem

Interface text is the last thing that gets written and the first thing users read. Engineers fill in placeholder copy -- "Submit", "Error: Invalid input", "Click here to learn more" -- and that placeholder ships to production because nobody goes back to improve it. The result: users stare at a "Submit" button and do not know what they are submitting. They see "Error 404" and have no idea what to do about it. They encounter an empty screen with "No items found" and do not know how to create their first item.

Every label, error message, button, tooltip, and empty state is a micro-decision point for the user. Bad copy creates a moment of confusion. A moment of confusion creates hesitation. Hesitation creates form abandonment, support tickets, and the slow erosion of trust that shows up as churn but never gets attributed to the actual cause: the interface said "Submit" instead of "Save changes" and the user was not sure what would happen.

The problem is not that teams do not care about copy. It is that there is no framework for writing it. Engineers default to technical accuracy ("Error: Connection refused at port 443") when users need helpful guidance ("Can't connect to the server. Check your internet connection and try again."). Designers focus on layout and leave the words for later. Product managers write feature specs, not button labels. Nobody owns the words, so the words stay bad.

## The Solution

This plugin treats interface copy as a UX discipline with its own principles, patterns, and quality bar. The Clear-Concise-Useful-Human framework gives every piece of interface text four concrete criteria to meet: use simple words and active voice (Clear), front-load the key information and cut filler (Concise), always provide a next step the user can take (Useful), and sound empathetic and conversational rather than robotic (Human).

The skill provides tone calibration by context -- success messages are celebratory ("You're all set!"), error messages are helpful without blaming ("Let's fix this"), warnings are direct ("This can't be undone"), and empty states are encouraging ("Create your first project"). It includes concrete before/after rewrites for the four most common UI text patterns: buttons (Verb + Object formula), error messages (what happened + what to do), confirmation dialogs (action-specific title + irreversibility warning + labeled buttons), and form labels (plain language label + example placeholder + helper text).

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Button says "Submit" -- user does not know what will happen | Button says "Save changes" -- Verb + Object formula makes every action clear |
| Error says "Error 404" -- user has no recovery path | Error says "Page not found -- try searching or go to homepage" -- every error includes a next step |
| Empty state is blank or says "No items found" | Empty state says "Create your first project to start organizing your work" with a visible action button |
| Confirmation dialog says "Are you sure?" with OK/Cancel | Confirmation says "Delete 'Report'? This can't be undone." with [Delete]/[Cancel] buttons |
| Error messages use technical jargon: "Connection refused at port 443" | Error messages use human language: "Can't connect to the server. Check your internet connection and try again." |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install ux-writing@skillstack
```

### Prerequisites

No additional dependencies. Works with any Claude Code session.

### Verify installation

After installing, test with:

```
Rewrite these error messages to be more helpful -- "Error 404", "Invalid input", "Server error"
```

## Quick Start

1. Install the plugin with the commands above
2. Type: `My form buttons all say "Submit" -- rewrite them for each form type: signup, payment, and settings`
3. The skill applies the Verb + Object formula and produces context-specific labels: "Create account", "Complete payment", "Save settings"
4. Review the before/after comparison to see how each new label tells the user exactly what happens next
5. Next, try: `Write empty state copy for a dashboard that has no projects yet`

## What's Inside

This is a **single-skill plugin** with focused methodology and eval coverage.

| Component | Purpose |
|---|---|
| `skills/ux-writing/SKILL.md` | Core principles (Clear, Concise, Useful, Human), tone-by-context guidance, and four UI pattern rewrites (buttons, errors, confirmation dialogs, form labels) |
| `evals/trigger-evals.json` | 13 trigger scenarios for activation boundary testing |
| `evals/evals.json` | 3 output quality scenarios for copy improvement |

### ux-writing

**What it does:** Activates when you need to write or improve microcopy, error messages, button labels, empty states, confirmation dialogs, form labels, or any interface text. Applies the Clear-Concise-Useful-Human framework, calibrates tone by context (success, error, warning, empty state), and provides before/after rewrites using proven UI text patterns.

**Try these prompts:**

```
Rewrite our form error messages -- right now they just say "Invalid input" for everything
```

```
My checkout has five buttons that all say "Submit" or "Continue" -- write specific labels for each step
```

```
Write copy for the empty state when a user has no saved reports yet -- it needs to explain the feature and encourage the first action
```

```
Review this confirmation dialog: title says "Warning", body says "Are you sure?", buttons say "OK" and "Cancel". Rewrite it for a file deletion action.
```

```
Our app uses inconsistent tone -- errors sound angry, success messages sound robotic. Help me create a tone guide for all four contexts.
```

```
Write the microcopy for a password reset flow: the email prompt, the "check your email" confirmation, and the "password changed" success message
```

## Real-World Walkthrough

You are a frontend engineer working on a project management app. The app shipped three months ago with placeholder copy that was never replaced. Your support team reports that 30% of tickets are "I don't understand what this button does" or "I got an error and don't know what to do." Your PM asks you to do a "copy pass" across the app, but you have no framework for what good copy looks like.

You start with the worst offender -- the error messages:

```
Our app shows these errors and users always contact support. Rewrite them: "Error: Invalid input", "Operation failed", "Error 500", "Timeout", "Not authorized"
```

The skill applies the error message pattern: describe what went wrong in human language, then provide a specific next step. Your five errors become:

- "Error: Invalid input" becomes "This email address needs an @ symbol" (or whatever the specific validation failure is -- the skill teaches you to make errors field-specific, not form-level)
- "Operation failed" becomes "Could not save your changes. Check your connection and try again."
- "Error 500" becomes "Something went wrong on our end. We're looking into it -- try again in a few minutes."
- "Timeout" becomes "This is taking longer than usual. Check your connection or try again."
- "Not authorized" becomes "You don't have access to this page. Contact your team admin to request access."

Each rewrite follows the same structure: human-readable description + actionable next step. The skill points out that "Not authorized" is particularly bad because it does not tell the user who can fix it -- the rewrite adds "Contact your team admin" so the user has a concrete path forward.

Next, you tackle the buttons:

```
Here are all the buttons in our app that say "Submit": signup form, settings page, project creation, task assignment, and invoice generation. Rewrite each one.
```

The skill applies the Verb + Object formula. "Submit" on the signup form becomes "Create account." "Submit" on settings becomes "Save settings." "Submit" on project creation becomes "Create project." "Submit" on task assignment becomes "Assign task." "Submit" on invoice generation becomes "Generate invoice." Each button now tells the user exactly what clicking it will do.

Then the confirmation dialogs. Your app has a single reusable dialog component with the title "Warning", body "Are you sure you want to proceed?", and buttons "OK" and "Cancel." Every destructive action uses it -- deleting a project, removing a team member, canceling a subscription.

```
Rewrite our confirmation dialog for three different destructive actions: deleting a project, removing a team member, and canceling a subscription
```

The skill produces three context-specific dialogs:

**Delete project:** Title: "Delete 'Q4 Report'?" Body: "This will permanently delete the project and all its tasks. This can't be undone." Buttons: [Delete project] [Keep project]

**Remove team member:** Title: "Remove Sarah from this project?" Body: "Sarah will lose access to all project files and conversations." Buttons: [Remove member] [Cancel]

**Cancel subscription:** Title: "Cancel your Pro plan?" Body: "You'll keep access until March 15, then your account will switch to the free plan." Buttons: [Cancel subscription] [Keep Pro plan]

Each dialog uses the specific action as the title (not "Warning"), includes the consequence (not "Are you sure?"), and labels the buttons with the actual action (not "OK/Cancel"). The user knows exactly what will happen before they click.

Finally, you address empty states. Your app shows "No items" on every empty screen -- no explanation of the feature, no guidance on what to do first.

```
Write empty state copy for these screens: projects list (new user), team members (solo user), and reports (no data yet)
```

The skill applies the empty state pattern: describe what the feature does + encourage the first action. "No items" on the projects list becomes "Organize your work into projects. Create your first project to get started." with a [Create project] button. "No items" on team members becomes "Collaborate with your team. Invite colleagues to work together on projects." with an [Invite team member] button.

The result: your support tickets about confusing interface copy drop by half within the first month. The copy pass took a single day using the framework, compared to the weeks of ad-hoc rewrites you had been doing before. The Clear-Concise-Useful-Human framework becomes your team's standard for all new copy.

## Usage Scenarios

### Scenario 1: Rewriting form error messages

**Context:** You are a developer and your registration form shows "Invalid input" for every validation error. Users cannot figure out what is wrong with their submission.

**You say:** `Rewrite the error messages for our registration form -- right now every field just shows "Invalid input" when validation fails`

**The skill provides:**
- Field-specific error messages: "Email address needs an @ symbol", "Password must be at least 8 characters", "This username is already taken -- try another"
- Placement guidance: show errors inline below the field, not in a banner at the top
- Tone calibration: helpful without blaming ("needs an @ symbol" not "you entered an invalid email")

**You end up with:** Error messages that tell users exactly what is wrong and how to fix it, reducing form abandonment and support tickets.

### Scenario 2: Creating a tone guide for a new product

**Context:** You are a product designer launching a new app and want consistent voice across all interface text from day one.

**You say:** `Help me create a tone guide for our fitness app -- we want to sound motivating but not annoying`

**The skill provides:**
- Tone calibration across four contexts: success (celebratory but not over-the-top), error (supportive, not blaming), warning (honest, not scary), empty state (motivating, not pushy)
- Example copy for each context tailored to a fitness domain
- Anti-patterns to avoid: overly casual ("Oopsie!"), corporate ("An error has occurred"), or patronizing ("Great job clicking that button!")

**You end up with:** A documented tone guide with examples that your entire team can follow for consistent interface copy.

### Scenario 3: Writing onboarding microcopy

**Context:** Your SaaS app has a five-step onboarding wizard but users drop off at step 3. The copy in each step is generic ("Step 3 of 5") and does not explain why each step matters.

**You say:** `Write microcopy for each step of our onboarding wizard -- users drop off at step 3 (connecting their data source) and we think the copy isn't motivating enough`

**The skill provides:**
- Progress indicators that show value, not just position ("Almost there -- connect your data to see your first dashboard")
- Step descriptions that explain why each step matters ("Connect your data source so we can show you real insights, not sample data")
- Encouragement copy at friction points ("This usually takes about 2 minutes. We'll walk you through it.")

**You end up with:** Onboarding copy that motivates users through the hard steps and reduces drop-off by connecting each step to the value they will get.

### Scenario 4: Improving an existing confirmation dialog

**Context:** Your e-commerce app uses a generic "Are you sure?" dialog for removing items from the cart, and users accidentally confirm removals because the buttons say "OK" and "Cancel."

**You say:** `Users keep accidentally removing items from their cart because the confirmation dialog is too generic -- rewrite it`

**The skill provides:**
- Action-specific title: "Remove 'Blue Running Shoes' from your cart?"
- Consequence description: "You can always add it back later."
- Labeled buttons: [Remove item] [Keep in cart] instead of [OK] [Cancel]
- Optional: undo toast as an alternative to the confirmation dialog for low-stakes actions

**You end up with:** A confirmation dialog where users understand exactly what will happen and accidental removals drop significantly.

## Ideal For

- **Frontend engineers writing interface text** -- the framework replaces guesswork with concrete patterns for buttons, errors, empty states, and dialogs
- **Product teams doing a "copy pass" before launch** -- the four principles and tone guide provide a systematic approach instead of ad-hoc rewrites
- **Designers creating prototypes with realistic copy** -- placeholder text creates false usability signals; realistic copy reveals real friction
- **Teams with no dedicated UX writer** -- the patterns are simple enough for any team member to apply consistently

## Not For

- **Generating long-form documentation or help articles** -- use [documentation-generator](../documentation-generator/) for technical docs, tutorials, and API references
- **Designing visual layout or navigation patterns** -- use [frontend-design](../frontend-design/) for component design or [navigation-design](../navigation-design/) for information architecture
- **Creating content models for a CMS** -- use [content-modelling](../content-modelling/) for structured content types and editorial workflows

## How It Works Under the Hood

The plugin is a single compact skill with all methodology in the core `SKILL.md`. It defines four principles (Clear, Concise, Useful, Human), four tone contexts (success, error, warning, empty state), and four UI pattern templates (buttons, error messages, confirmation dialogs, form labels) with before/after examples.

The skill activates from natural language mentions of microcopy, UX copy, interface text, error messages, button labels, empty states, or conversational UI text. When activated, it identifies which UI pattern applies to your request, applies the appropriate principle and tone, and produces specific rewrites with explanations of why each change improves the user experience.

## Related Plugins

- **[User Journey Design](../user-journey-design/)** -- Map the journeys where your microcopy appears at each touchpoint
- **[Persona Definition](../persona-definition/)** -- Understand who reads your copy so tone and vocabulary match their expectations
- **[Navigation Design](../navigation-design/)** -- Design the navigation labels and wayfinding text
- **[Content Modelling](../content-modelling/)** -- Structure the content types that contain your copy
- **[Frontend Design](../frontend-design/)** -- Design the visual components where your copy lives

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — production-grade plugins for Claude Code.
