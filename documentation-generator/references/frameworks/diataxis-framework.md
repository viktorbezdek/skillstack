# Diataxis Documentation Framework

## Overview

Diataxis is a systematic framework for technical documentation authoring based on identifying four distinct documentation types, each serving a different user need.

## The Four Types

```
                    LEARNING                      DOING
              ┌───────────────────┬───────────────────┐
              │                   │                   │
              │    TUTORIALS      │    HOW-TO GUIDES  │
   PRACTICAL  │                   │                   │
              │  Learning-        │  Problem-         │
              │  oriented         │  oriented         │
              │                   │                   │
              ├───────────────────┼───────────────────┤
              │                   │                   │
              │   EXPLANATION     │    REFERENCE      │
 THEORETICAL  │                   │                   │
              │  Understanding-   │  Information-     │
              │  oriented         │  oriented         │
              │                   │                   │
              └───────────────────┴───────────────────┘
```

## Documentation Type Details

### 1. Tutorials (Learning + Practical)

**Purpose:** Take the reader by the hand through a series of steps to complete a project

**Characteristics:**
- Lesson-oriented
- Learning through doing
- Inspires confidence
- Repeatable
- Immediate results

**Key Principles:**
- Let the user learn by doing
- Get the user started
- Make sure the tutorial works
- Ensure the user sees results immediately
- Focus on concrete steps, not abstract concepts
- Provide minimum necessary explanation
- Focus only on the steps the user needs to take

**Writing Tips:**
- Use imperative language: "Create a file...", "Add the following..."
- Avoid explaining why - that's for Explanation docs
- Test every step
- Assume no prior knowledge
- Keep the tutorial path linear

**Example Structure:**
```markdown
# Building Your First App

## What You'll Build
[Brief description of end result]

## Prerequisites
- [Requirement 1]
- [Requirement 2]

## Step 1: Set Up Your Environment
[Instructions]

## Step 2: Create the Project
[Instructions]

## Step 3: Add Functionality
[Instructions]

## Next Steps
[Links to related tutorials or how-to guides]
```

### 2. How-To Guides (Doing + Practical)

**Purpose:** Guide the reader through the steps to solve a real-world problem

**Characteristics:**
- Goal-oriented
- Addresses specific tasks
- Provides working solutions
- Assumes some knowledge

**Key Principles:**
- Solve a specific problem
- Don't explain concepts
- Be flexible (allow for different approaches)
- Provide a series of steps
- Focus on results

**Writing Tips:**
- Title should describe the goal: "How to deploy to production"
- Don't teach - direct
- Assume competence
- Be practical over comprehensive

**Example Structure:**
```markdown
# How to Deploy to Production

## Overview
This guide shows you how to deploy your application to production.

## Prerequisites
- Working application
- Server access

## Steps

### 1. Prepare Your Application
```bash
npm run build
```

### 2. Configure Environment
[Configuration steps]

### 3. Deploy
[Deployment steps]

## Troubleshooting
[Common issues and solutions]
```

### 3. Reference (Doing + Theoretical)

**Purpose:** Describe the machinery - technical specifications

**Characteristics:**
- Information-oriented
- Dry and to-the-point
- Accurate and complete
- Structured for lookup

**Key Principles:**
- Be accurate
- Structure matters
- Be consistent
- Do only one thing - describe
- Provide examples

**Writing Tips:**
- Organize for easy scanning
- Use tables for structured data
- Keep descriptions factual
- Don't mix with tutorials or explanations
- Match the structure of the code/API

**Example Structure:**
```markdown
# API Reference

## `functionName(param1, param2)`

Creates a new instance.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `param1` | string | Yes | Description |
| `param2` | number | No | Description |

### Returns

`Object` - Description of return value

### Example

```javascript
const result = functionName('value', 42);
```

### Throws

- `TypeError` - If param1 is not a string
```

### 4. Explanation (Learning + Theoretical)

**Purpose:** Clarify and illuminate a particular topic

**Characteristics:**
- Understanding-oriented
- Provides context
- Discusses alternatives
- Explains why

**Key Principles:**
- Give context
- Explain design decisions
- Consider alternatives
- Don't instruct
- Make connections

**Writing Tips:**
- Discuss the "why" not the "how"
- Draw on multiple perspectives
- Reference other parts of the documentation
- Avoid being prescriptive

**Example Structure:**
```markdown
# Understanding Authentication

## Background

Authentication is the process of verifying identity...

## Why Token-Based Authentication?

Traditional session-based authentication has limitations...

### Advantages
- Stateless
- Scalable
- Cross-domain

### Trade-offs
- Token storage security
- Token size

## How It Fits Together

The authentication system interacts with...

## Further Reading
- [JWT RFC](https://...)
- [OAuth 2.0 Specification](https://...)
```

## Decision Tree

Use this to determine which type of documentation to write:

```
Is the reader trying to accomplish something?
├── Yes → Is there a specific end goal?
│         ├── Yes → HOW-TO GUIDE
│         └── No → TUTORIAL
│
└── No → Is the reader trying to understand something?
          ├── Yes → Does it need context/reasoning?
          │         ├── Yes → EXPLANATION
          │         └── No → REFERENCE
          └── No → Probably REFERENCE
```

## Common Mistakes

### Mistake 1: Mixing Types

**Wrong:**
```markdown
# Getting Started (Tutorial mixing with Reference)

First, create a file. The `createFile()` function takes three
parameters: name (string), content (Buffer), and options (object).
Options can include encoding, mode, and flag. Here's an example:

createFile('test.txt', 'Hello', { encoding: 'utf8' })
```

**Right:** Keep the reference material in a separate document.

### Mistake 2: Explaining in Reference

**Wrong:**
```markdown
# API Reference

## `authenticate()`

This function handles authentication. Authentication is important
because it ensures only authorized users can access the system.
In modern web applications, we typically use JWT tokens because
they're stateless and scalable...
```

**Right:** Just describe what it does, link to explanation.

### Mistake 3: Reference Disguised as How-To

**Wrong:**
```markdown
# How to Use the Configuration System

The configuration system supports the following options:
- `debug`: boolean
- `timeout`: number
- `retries`: number
...
```

**Right:** Either make it a true how-to (goal-oriented) or a reference (lookup-oriented).

## Implementation Checklist

When creating documentation, verify:

**For Tutorials:**
- [ ] Has clear learning goal
- [ ] Uses step-by-step format
- [ ] Shows immediate results
- [ ] Avoids detailed explanations
- [ ] Has been tested end-to-end

**For How-To Guides:**
- [ ] Addresses specific problem
- [ ] Assumes some knowledge
- [ ] Focuses on practical steps
- [ ] Includes troubleshooting
- [ ] Title describes the goal

**For Reference:**
- [ ] Organized for lookup
- [ ] Accurate and complete
- [ ] Uses consistent structure
- [ ] Includes all parameters/options
- [ ] Has examples

**For Explanation:**
- [ ] Provides context
- [ ] Explains reasoning
- [ ] Discusses alternatives
- [ ] Makes connections
- [ ] Doesn't instruct

## Further Reading

- [Diataxis Official Site](https://diataxis.fr/)
- [The Grand Unified Theory of Documentation](https://documentation.divio.com/)
