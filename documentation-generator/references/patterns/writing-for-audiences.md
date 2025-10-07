# Writing for Different Audiences

## Overview

Effective documentation serves different audiences with different needs. This guide helps you write appropriate content for both technical and non-technical readers.

## Audience Types

### Non-Technical Readers

**Who they are:**
- Business stakeholders
- Project managers
- End users (non-developers)
- Decision makers
- Support staff

**What they need:**
- What the product does (not how)
- Business value and benefits
- Simple step-by-step instructions
- Visual guides and screenshots
- Plain language explanations
- FAQ sections

**What they don't need:**
- Implementation details
- Code snippets (mostly)
- Technical architecture
- Developer terminology

### Technical Readers

**Who they are:**
- Developers
- DevOps engineers
- System administrators
- Technical architects
- QA engineers

**What they need:**
- API specifications
- Code examples
- Architecture details
- Configuration options
- Integration guides
- Troubleshooting details

**What they value:**
- Accuracy over simplicity
- Completeness
- Copy-paste ready code
- Edge case documentation

## Writing Guidelines

### For Non-Technical Readers

#### Language

**Do:**
- Use everyday words
- Define technical terms when unavoidable
- Use analogies and comparisons
- Write in active voice
- Keep sentences short (15-20 words)

**Don't:**
- Use jargon without explanation
- Assume prior knowledge
- Skip steps that seem "obvious"
- Use acronyms without defining them

**Example Transformation:**

| Technical | Non-Technical |
|-----------|---------------|
| "Execute the API endpoint" | "Click the button to send your data" |
| "Deploy to production" | "Make your changes live" |
| "Authenticate using OAuth" | "Sign in with your Google account" |
| "Parse the JSON response" | "The system will read the data and show you the results" |

#### Structure

```markdown
# Feature Name

## What It Does
[2-3 sentence explanation in plain language]

## Why You'd Use It
[Business value, problem it solves]

## How to Use It

### Step 1: [Action]
[Simple instruction]

[Screenshot or diagram]

### Step 2: [Action]
[Simple instruction]

## Common Questions

**Q: [Frequent question]?**
A: [Simple answer]

## Getting Help
[Support contact, resources]
```

#### Visual Elements

- **Screenshots:** Use liberally, annotate key areas
- **Diagrams:** Simple flowcharts, no technical notation
- **Videos:** Short (< 2 min) how-to clips
- **Icons:** Consistent meaning, not decorative

### For Technical Readers

#### Language

**Do:**
- Use precise technical terminology
- Be concise - developers scan
- Include type information
- Note version requirements
- Document edge cases

**Don't:**
- Over-explain basic concepts
- Pad with unnecessary words
- Hide important details in prose
- Skip error handling

**Example:**

```markdown
## `createUser(data: UserInput): Promise<User>`

Creates a new user account.

### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `data` | `UserInput` | Yes | User creation payload |

### UserInput

```typescript
interface UserInput {
  email: string;      // Must be valid email format
  name: string;       // 1-100 characters
  role?: UserRole;    // Default: 'user'
}
```

### Returns

`Promise<User>` - Created user object with `id` populated.

### Throws

- `ValidationError` - Invalid input data
- `ConflictError` - Email already exists

### Example

```typescript
const user = await createUser({
  email: 'user@example.com',
  name: 'John Doe',
  role: 'admin'
});
console.log(user.id); // 'usr_abc123'
```
```

#### Structure

```markdown
# Component/API Name

Brief description (1-2 sentences).

## Installation
[Copy-paste ready]

## Quick Start
[Minimal working example]

## API Reference
[Complete specification]

## Configuration
[All options with types and defaults]

## Advanced Usage
[Complex scenarios]

## Troubleshooting
[Common errors with solutions]
```

## Document Type by Audience

| Document | Primary Audience | Secondary |
|----------|------------------|-----------|
| README | Both | Start with non-technical, link to technical |
| Getting Started | Non-technical | Simplified technical sections |
| User Guide | Non-technical | - |
| API Reference | Technical | - |
| Architecture | Technical | Executive summaries for non-technical |
| Troubleshooting | Both | Separate sections by audience |
| FAQ | Both | Mark technical answers clearly |

## Hybrid Documents

Some documents serve both audiences. Use these techniques:

### Progressive Disclosure

Start simple, go deeper:

```markdown
## Saving Your Work

Click the Save button to save your changes.

<details>
<summary>Technical Details</summary>

The save operation performs a PUT request to `/api/documents/{id}`
with the following payload:

```json
{
  "content": "...",
  "metadata": {...}
}
```
</details>
```

### Audience Markers

Clearly label technical sections:

```markdown
## Configuration

### Basic Configuration

Edit your settings in the Settings panel:
1. Click your profile icon
2. Select "Settings"
3. Adjust options as needed

### Advanced Configuration (Developers)

Configuration can also be set via environment variables:

```bash
export APP_DEBUG=true
export APP_LOG_LEVEL=verbose
```
```

### Parallel Versions

For critical documents, maintain two versions:

```
docs/
├── user-guide/           # Non-technical
│   ├── getting-started.md
│   └── features.md
└── developer-guide/      # Technical
    ├── getting-started.md
    └── api.md
```

## Tone and Voice

### Non-Technical

- Friendly and approachable
- Encouraging ("Great job!")
- Patient (explain thoroughly)
- Supportive ("Don't worry if...")

**Example:**
> Welcome to MyApp! In the next few minutes, you'll set up your account and
> be ready to start organizing your projects. Don't worry if you get stuck—
> we're here to help.

### Technical

- Direct and efficient
- Neutral (facts, not feelings)
- Confident (definitive statements)
- Respectful of reader's time

**Example:**
> This guide covers installation and basic configuration. Prerequisites:
> Node.js 18+, npm 9+. Estimated time: 5 minutes.

## Testing Your Documentation

### For Non-Technical Content

- Have a non-developer follow the instructions
- Watch for confusion points
- Note questions asked
- Remove or explain any remaining jargon

### For Technical Content

- Copy-paste all code examples and run them
- Verify edge cases mentioned
- Check that prerequisites are complete
- Have a developer new to the project try it

## Checklist

### Non-Technical Document

- [ ] Uses plain language throughout
- [ ] Defines any technical terms used
- [ ] Includes visual guides
- [ ] Has clear, numbered steps
- [ ] Tested by a non-technical person
- [ ] Includes FAQ/support section
- [ ] Links to more detailed resources

### Technical Document

- [ ] All code examples are tested
- [ ] Types and signatures are accurate
- [ ] Error cases are documented
- [ ] Prerequisites are listed
- [ ] Versions are specified
- [ ] Edge cases are noted
- [ ] Can be used as reference (scannable)
