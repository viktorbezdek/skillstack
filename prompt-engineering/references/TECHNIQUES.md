# Prompting Techniques Catalog

Complete reference for prompt engineering techniques with detailed examples and use cases.

## Foundation Techniques

### 1. Role Assignment

**What:** Define specific expertise, credentials, and perspective for the AI

**When:** Always for professional tasks, domain-specific work, or when expertise level matters

**Example:**
```
You are a senior data scientist with 10 years of experience in machine learning and statistical analysis.

Credentials:
- PhD in Computer Science (Machine Learning)
- Published researcher in NeurIPS and ICML
- Led ML teams at Fortune 500 companies

Methodology:
- Evidence-based analysis
- Statistical rigor
- Practical business focus

Task: [Your request]
```

**Variations:**
- **Minimal:** "You are an expert in [domain]"
- **Moderate:** "You are a [role] with [years] experience in [domain]"
- **Comprehensive:** Full credentials, methodology, perspective (as above)

### 2. Context Layering

**What:** Provide essential background without overwhelming context window

**When:** Task requires specific domain knowledge, constraints, or situational awareness

**Example:**
```
Background:
- Company: B2B SaaS, 200 employees, Series B
- Product: Project management tool
- Market: Mid-market (100-1000 employee companies)
- Current stage: Product-market fit achieved, scaling GTM

Constraints:
- Budget: $500K for initiative
- Timeline: Q4 2024 launch
- Team: 5 engineers, 2 designers

Requirements:
- Must integrate with Slack, Teams
- GDPR compliant
- Mobile-first design

Task: [Your request with this context]
```

**Pro tips:**
- Provide only essential context
- Structure hierarchically (overview → specifics)
- Use bullet points for scannability
- Avoid redundancy with general knowledge

### 3. Output Specification

**What:** Define exact format, structure, length, and style

**When:** Whenever output format matters for usability or integration

**Examples:**

**Structured output:**
```
Provide response in JSON format:
{
  "summary": "Brief overview (max 100 words)",
  "findings": [
    {
      "category": "string",
      "insight": "string",
      "evidence": "string",
      "confidence": "high|medium|low"
    }
  ],
  "recommendations": ["action 1", "action 2", "action 3"]
}
```

**Report format:**
```
Structure response as:

# [Title]

## Executive Summary
[3-4 sentences]

## Analysis
### Finding 1
[Details with evidence]

### Finding 2
[Details with evidence]

## Recommendations
1. [Specific action with rationale]
2. [Specific action with rationale]

Length: 500-750 words
Style: Professional, data-driven
```

**Length constraints:**
```
- "Respond in exactly 3 paragraphs"
- "Keep under 200 words"
- "Provide detailed analysis (800-1200 words)"
- "Be extremely concise (max 5 bullet points)"
```

### 4. Constraint Definition

**What:** Set clear boundaries, requirements, and limitations

**When:** Need specific compliance, style requirements, or scope boundaries

**Example:**
```
Constraints:
- MUST include citations for all claims
- MUST NOT use jargon (explain technical terms)
- MUST stay within scope of Q3 2024 only
- MUST follow APA citation style
- MUST consider accessibility (WCAG 2.1 AA)
- SHOULD prioritize recent sources (2023-2024)
- SHOULD NOT exceed 1000 words
```

**Constraint types:**
- **Hard constraints:** MUST/MUST NOT
- **Soft constraints:** SHOULD/SHOULD NOT  
- **Preferences:** PREFER/AVOID

### 5. Success Criteria

**What:** Define measurable outcomes and validation methods

**When:** Important to evaluate success or guide decision-making

**Example:**
```
Success criteria:
1. Technical accuracy
   - All code compiles without errors
   - Follows PEP 8 style guide
   - Includes comprehensive docstrings

2. Completeness
   - Addresses all 5 requirements
   - Includes error handling
   - Provides usage examples

3. Quality
   - Code coverage >80%
   - Passes all test cases
   - Performance: <100ms response time

Validation:
- Run pytest suite (must pass 100%)
- pylint score >8.5/10
- Manual review for edge cases
```

## Advanced Techniques

### 6. Chain-of-Thought (CoT)

**What:** Explicitly request step-by-step reasoning

**When:** Complex reasoning, math problems, multi-step analysis, debugging

**Basic pattern:**
```
Think through this step-by-step:
1. Identify the key components
2. Analyze relationships
3. Reason through each step
4. Draw conclusions
5. Verify the answer

Problem: [Your problem]
```

**Advanced pattern:**
```
Use this reasoning framework:

## Problem Decomposition
- Break into sub-problems
- Identify dependencies
- List assumptions

## Solution Strategy
- Consider multiple approaches
- Evaluate trade-offs
- Select optimal path

## Execution
- Work through each step
- Show intermediate results
- Check consistency

## Validation
- Verify against constraints
- Test edge cases
- Confirm answer reasonableness

Now apply to: [Your problem]
```

**Few-Shot CoT:**
```
Here's an example of step-by-step reasoning:

Q: If 3 painters can paint 3 rooms in 3 hours, how many painters needed for 6 rooms in 6 hours?

A: Let me work through this:
1. First, find rate per painter: 3 painters paint 3 rooms in 3 hours
   - This means each painter paints 1 room in 3 hours
   - Rate: 1/3 room per hour per painter
2. For 6 rooms in 6 hours:
   - Need 6 rooms painted total
   - Have 6 hours available
   - Each painter can paint: 6 hours × 1/3 room/hr = 2 rooms
3. Therefore: 6 rooms ÷ 2 rooms/painter = 3 painters needed

Now solve this: [Your problem]
```

### 7. Few-Shot Learning

**What:** Provide 2-5 examples of desired input/output pattern

**When:** Specific format needed, style matching, pattern recognition

**Structure:**
```
[Optional: Brief instruction]

Example 1:
Input: [Sample input 1]
Output: [Ideal output 1]

Example 2:
Input: [Sample input 2]
Output: [Ideal output 2]

Example 3:
Input: [Sample input 3]
Output: [Ideal output 3]

Now apply this pattern to:
Input: [Your actual input]
```

**Real example (commit messages):**
```
Generate commit messages following these examples:

Example 1:
Diff: Added user authentication with JWT
Output:
feat(auth): implement JWT-based authentication

- Add login/logout endpoints
- Create token validation middleware
- Update user model with password hashing

Example 2:
Diff: Fixed timezone bug in reports
Output:
fix(reports): correct timezone handling

- Use UTC for all date storage
- Convert to local timezone only for display
- Add timezone tests

Example 3:
Diff: Updated README with setup instructions
Output:
docs(readme): add setup instructions

- Include prerequisites section
- Add step-by-step installation
- Document common troubleshooting

Now generate for:
Diff: [Your actual diff]
```

**Example selection tips:**
- Include range of complexity (simple → advanced)
- Show edge cases if relevant
- Maintain consistent format
- Use realistic, representative examples

### 8. Multi-Perspective Analysis

**What:** Request analysis from multiple viewpoints

**When:** Complex decisions, stakeholder alignment, comprehensive evaluation

**Example:**
```
Analyze this proposal from multiple perspectives:

## Technical Perspective (Engineering Lead)
- Feasibility assessment
- Technical risks
- Architecture implications
- Resource requirements

## Business Perspective (Product Manager)
- Market opportunity
- Competitive advantage
- ROI potential
- Time-to-market

## User Perspective (UX Designer)
- User needs addressed
- Experience quality
- Accessibility considerations
- Adoption barriers

## Risk Perspective (Security Officer)
- Security implications
- Compliance requirements
- Data protection
- Threat landscape

For each perspective:
1. Key considerations
2. Potential concerns
3. Recommendations
4. Priority level

Proposal: [Your proposal]
```

### 9. Decomposition & Delegation

**What:** Break complex task into manageable subtasks

**When:** Multi-faceted projects, complex workflows, parallel processing

**Pattern:**
```
Break down this task hierarchically:

## Primary Task
[Main objective]

## Core Components
1. Component A
   - Subtask A1
   - Subtask A2
   - Subtask A3
   
2. Component B
   - Subtask B1
   - Subtask B2

3. Component C
   - Subtask C1
   - Subtask C2

## Dependency Map
- B requires A1 complete
- C requires A2, B1 complete
- Final integration requires all

## Execution Plan
Phase 1: [A1, A2] (parallel)
Phase 2: [A3, B1] (B1 depends on A1)
Phase 3: [B2, C1] (parallel)
Phase 4: [C2, integration]

Now execute on: [Your task]
```

### 10. Meta-Prompting

**What:** Use abstract frameworks instead of specific examples

**When:** Token efficiency important, generalizable patterns, avoiding bias

**Example:**
```
Framework: [ABSTRACT PATTERN]
- Structure: [GENERAL APPROACH]
- Principles: [CORE RULES]
- Adaptation: [HOW TO CUSTOMIZE]

Apply this framework to: [SPECIFIC DOMAIN]
Constraints: [SPECIFIC REQUIREMENTS]

Instead of:
"Here are 5 examples of good product descriptions..."

Use:
"Product descriptions should follow this framework:
- Hook (grab attention)
- Features (what it has)
- Benefits (what it solves)
- Social proof (validation)
- Call-to-action (next step)

Adapt this framework for: [Your product]"
```

## Specialized Techniques

### 11. Socratic Method (Teaching)

**What:** Guide learning through questions rather than direct answers

**When:** Educational content, concept understanding, critical thinking

**Example:**
```
Help the user understand [concept] using Socratic method:

1. Start with what they know
   - "What do you already know about [concept]?"
   
2. Build on their understanding
   - "How might that relate to [related concept]?"
   
3. Challenge assumptions gently
   - "What if [edge case]?"
   
4. Guide to discovery
   - "What pattern do you notice?"
   
5. Solidify understanding
   - "Can you explain it in your own words?"

Don't give direct answers - ask guiding questions.
```

### 12. Constraint-Based Generation

**What:** Use strict constraints to guide creative generation

**When:** Creative tasks needing structure, specific requirements

**Example:**
```
Generate [creative content] with these constraints:

Mandatory constraints:
- Exactly 3 stanzas of 4 lines each
- ABAB rhyme scheme
- Include words: [list]
- Theme: [specific theme]
- Tone: [specific tone]

Optional constraints:
- Prefer metaphors over similes
- Alliteration in at least 2 lines
- Vivid imagery

Follow these constraints strictly while maximizing creativity.
```

### 13. Iterative Refinement

**What:** Explicitly request multiple iterations with improvements

**When:** High-quality output needed, refinement important

**Example:**
```
Create [output] using iterative refinement:

Iteration 1: Quick draft
- Focus on structure and key points
- Don't worry about polish

Iteration 2: Enhance content
- Expand key sections
- Add supporting details
- Include examples

Iteration 3: Polish
- Refine language
- Improve flow
- Check consistency

Iteration 4: Optimize
- Remove redundancy
- Tighten prose
- Verify all requirements met

Show all iterations so I can see progression.
```

### 14. Prompt Chaining

**What:** Break task into sequential prompts, each feeding into next

**When:** Complex multi-stage workflows, intermediate validation needed

**Example:**
```
Stage 1 Prompt:
"Extract all key features from this product description: [text]"

[Use output in Stage 2]

Stage 2 Prompt:
"For these features: [Stage 1 output]
Categorize them into: Must-have, Nice-to-have, Differentiators"

[Use output in Stage 3]

Stage 3 Prompt:
"Using this categorization: [Stage 2 output]
Create competitive positioning for each category"

[Use output in Stage 4]

Stage 4 Prompt:
"Synthesize this analysis: [Stage 3 output]
Into executive summary with strategic recommendations"
```

### 15. ReAct (Reasoning + Acting)

**What:** Combine reasoning with tool use/actions

**When:** Tasks needing information retrieval, external tools, multi-step research

**Pattern:**
```
Use this Thought-Action-Observation cycle:

Thought: [Reasoning about what to do next]
Action: [Specific action to take]
Observation: [Results from action]

Repeat until task complete.

Example:
Thought: I need current information about X
Action: Search[latest news about X]
Observation: [search results]
Thought: Based on results, I need to verify Y
Action: WebFetch[authoritative source URL]
Observation: [fetched content]
Thought: Now I can synthesize findings
Action: Answer[final response]

Apply this to: [Your task]
```

## Platform-Specific Techniques

### Claude-Specific

**Extended thinking:**
```
<thinking>
Work through the problem internally before responding:
- Consider multiple approaches
- Evaluate trade-offs
- Check reasoning
- Validate conclusions
</thinking>

Then provide: [structured response]
```

**XML structure:**
```
Use XML tags for complex data:

<analysis>
  <finding type="primary">
    <claim>Main finding</claim>
    <evidence>Supporting data</evidence>
    <confidence>high</confidence>
  </finding>
</analysis>
```

### ChatGPT-Specific

**Custom instructions:**
```
How would you like ChatGPT to respond?
- Tone: [Professional/Casual/Technical]
- Length: [Concise/Detailed/Comprehensive]
- Format: [Structured/Narrative/Mixed]
- Depth: [Overview/Intermediate/Expert]
```

**Conversation starters:**
```
Add these for multi-turn:
- "What would you like to know more about?"
- "Should I dive deeper into any section?"
- "Would you like me to rephrase anything?"
```

### Gemini-Specific

**Multimodal prompts:**
```
Analyze this image and text together:
Image: [provide image]
Text: [provide text]

Tasks:
- How do they complement each other?
- What's the combined message?
- Suggest improvements to alignment
```

**Code execution:**
```
Use Python to:
1. Load the data
2. Perform analysis
3. Generate visualizations
4. Return insights

Execute code and show both code and results.
```

## Technique Selection Guide

| Task Type | Primary Technique | Secondary Techniques |
|-----------|------------------|---------------------|
| Complex reasoning | Chain-of-thought | Decomposition, Validation |
| Pattern matching | Few-shot learning | Examples, Templates |
| Creative generation | Constraints + Role | Examples, Iteration |
| Multi-stakeholder | Multi-perspective | Frameworks, Trade-off analysis |
| Teaching/Learning | Socratic method | Examples, Analogies |
| Research synthesis | ReAct | Multi-perspective, Chain-of-thought |
| Technical tasks | Constraints + Tests | Few-shot, Error handling |
| Decision support | Multi-perspective | Trade-off analysis, Criteria weighting |

## Combining Techniques

Most effective prompts combine multiple techniques:

**Example: Complex Research Task**
```
[Role Assignment]
You are a market research analyst specializing in SaaS.

[Context Layering]
Company: B2B project management tool
Market: Mid-market (100-1000 employees)
Stage: Series B, scaling GTM

[Multi-Perspective]
Analyze from:
- Customer perspective
- Competitive perspective
- Market trends perspective

[Chain-of-Thought]
For each perspective:
1. Identify key factors
2. Analyze implications
3. Draw insights

[Output Specification]
Format as structured report:
## Perspective 1: Customers
[Analysis following CoT]

## Perspective 2: Competition
[Analysis following CoT]

## Perspective 3: Market
[Analysis following CoT]

## Synthesis
[Combined insights and recommendations]

[Constraints]
- Use data from 2023-2024 only
- Cite all sources
- 1000-1500 words
- Include actionable recommendations
```

## Anti-Patterns to Avoid

❌ **Over-specification:**
Don't micro-manage every detail - trust the model

❌ **Redundant instructions:**
"Be clear and concise and brief and to the point"

❌ **Conflicting constraints:**
"Be extremely detailed but keep it under 100 words"

❌ **Vague success criteria:**
"Make it good" vs. "Ensure accuracy >95%, completeness >90%"

❌ **Too many examples:**
5-7 examples rarely better than 2-3 well-chosen ones

❌ **Generic roles:**
"You are an expert" vs. "You are a senior ML engineer with NLP specialization"

❌ **Assuming context:**
Don't assume model knows your company-specific terms without definition
