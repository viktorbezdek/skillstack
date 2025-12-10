# Platform-Specific Optimization Guide

Detailed guidance for optimizing prompts for different LLM platforms.

## Table of Contents
1. ChatGPT / GPT-4
2. Claude (Anthropic)
3. Gemini (Google)
4. Platform Comparison
5. Cross-Platform Best Practices

---

## 1. ChatGPT / GPT-4

### Platform Capabilities

**Context Window:**
- GPT-4: 8K, 32K, 128K tokens depending on model
- GPT-3.5-Turbo: 16K tokens
- Planning: Consider context limits when designing prompts

**Special Features:**
- Custom instructions (system-level guidance)
- Function calling / Tools
- Code Interpreter
- DALL-E integration
- Web browsing (in some versions)
- Vision capabilities (GPT-4 Vision)

### Optimization Strategies

#### 1. Structured Sections with Headers

ChatGPT responds well to clearly delineated sections:

```
# [MAIN_TASK]

## Context
[Background information]

## Requirements
1. [Requirement 1]
2. [Requirement 2]

## Output Format
[Specify structure]

## Examples
[If helpful]

## Constraints
- [Constraint 1]
- [Constraint 2]
```

#### 2. Custom Instructions

Leverage the custom instructions field:

**"How would you like ChatGPT to respond?"**
```
- Tone: Professional and concise
- Format: Use markdown with headers and bullets
- Depth: Provide detailed technical explanations
- Code: Include comments and type hints
- Citations: Link to sources when making claims
- Length: Be thorough but avoid unnecessary verbosity
```

#### 3. Conversation Starters

For iterative tasks, add conversation starters:

```
Your task: [Main objective]

[Detailed instructions]

**Follow-up questions you might ask:**
- "Can you explain [X] in more detail?"
- "What are the trade-offs between approaches?"
- "Can you provide an example of [Y]?"
```

#### 4. Function Calling

Structure prompts to leverage function calling:

```python
functions = [
    {
        "name": "search_knowledge_base",
        "description": "Search company knowledge base",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "limit": {"type": "integer"}
            }
        }
    }
]

prompt = """
Find information about [TOPIC] using the search_knowledge_base function.
Then synthesize findings into a summary.
"""
```

#### 5. Code Interpreter Optimization

For data analysis tasks:

```
Analyze this dataset using Code Interpreter:

Data: [DESCRIPTION or file]

Steps:
1. Load and explore the data
2. Check for missing values and outliers
3. Perform [SPECIFIC_ANALYSIS]
4. Create visualizations for key findings
5. Summarize insights

Show your code and explain each step.
```

### Best Practices for ChatGPT

✅ **Do:**
- Use clear section headers with markdown
- Specify exact output format
- Include examples for complex patterns
- Leverage custom instructions for consistent behavior
- Use numbered lists for sequential steps
- Add conversation starters for multi-turn interactions

❌ **Don't:**
- Exceed context window (monitor token count)
- Assume function calling without verification
- Mix instructions with unrelated context
- Use overly complex nested structures
- Forget to specify constraints explicitly

### ChatGPT-Specific Examples

**Research Task:**
```
# Research Request: [TOPIC]

## Objective
Provide comprehensive overview of [TOPIC] with focus on [ASPECT]

## Requirements
1. Cover key concepts
2. Include recent developments (2023-2024)
3. Cite authoritative sources
4. Identify controversies or debates

## Output Structure
### Overview (200 words)
### Key Concepts (400 words)
### Recent Developments (300 words)
### Debates & Controversies (200 words)
### Further Reading (5-7 sources)

## Style
- Academic but accessible
- Define technical terms
- Use examples to illustrate concepts
```

---

## 2. Claude (Anthropic)

### Platform Capabilities

**Context Window:**
- Claude 3.5 Sonnet: 200K tokens
- Claude 3 Opus: 200K tokens
- Claude 3 Haiku: 200K tokens
- Industry-leading context capacity

**Special Features:**
- Extended thinking (thinking tags)
- Computer use (beta)
- Document analysis
- Long-form content understanding
- Constitutional AI principles
- Vision capabilities (Claude 3+)

### Optimization Strategies

#### 1. Progressive Disclosure

Take advantage of large context window with layered information:

```
# [TASK_OVERVIEW]

## Quick Reference
[Core instructions - always loaded]

## Detailed Guidelines
[Comprehensive details - if needed]

## Advanced Scenarios
[Edge cases and special situations]

## Reference Materials
[Background information, schemas, examples]

Claude will selectively use sections as needed.
```

#### 2. Thinking Tags

Request explicit reasoning for complex tasks:

```
<thinking>
Work through this problem step by step:
1. Analyze the requirements
2. Consider different approaches
3. Evaluate trade-offs
4. Select optimal solution
5. Validate reasoning
</thinking>

Now provide your answer: [TASK]
```

#### 3. XML Structure for Complex Data

Use XML tags for structured information:

```
<task>
  <objective>Primary goal</objective>
  <constraints>
    <constraint type="time">24 hours</constraint>
    <constraint type="budget">$10,000</constraint>
  </constraints>
  <requirements>
    <requirement priority="high">Must have X</requirement>
    <requirement priority="medium">Should have Y</requirement>
  </requirements>
</task>

Analyze this task and provide structured recommendations.
```

#### 4. Long Document Analysis

Optimize for Claude's document capabilities:

```
I've provided a [NUMBER]-page document about [TOPIC].

Analysis Framework:
1. Document Structure
   - Identify key sections
   - Note organizational pattern

2. Core Arguments
   - Extract main thesis
   - Identify supporting arguments
   - Note evidence used

3. Critical Analysis
   - Strengths of arguments
   - Weaknesses or gaps
   - Assumptions made

4. Synthesis
   - Key takeaways
   - Implications
   - Related considerations

Please provide detailed analysis using this framework.
```

#### 5. Constitutional AI Alignment

Frame requests with values/principles:

```
Operating Principles:
- Prioritize accuracy over speed
- Acknowledge uncertainty when present
- Provide balanced perspectives
- Consider ethical implications
- Highlight potential biases

Task: [YOUR_REQUEST]

Apply these principles throughout your response.
```

### Best Practices for Claude

✅ **Do:**
- Use thinking tags for complex reasoning
- Leverage 200K context for comprehensive information
- Structure with XML for complex data
- Include reasoning frameworks
- Ask for self-verification on critical tasks
- Use progressive disclosure for lengthy prompts

❌ **Don't:**
- Provide redundant context (Claude has strong recall)
- Mix multiple complex tasks without clear structure
- Assume capabilities without verification
- Skip constraint specification
- Overload with unnecessary details upfront

### Claude-Specific Examples

**Multi-Document Analysis:**
```
I've provided three research papers on [TOPIC].

<analysis_framework>
  <step>Compare methodologies across papers</step>
  <step>Identify consensus findings</step>
  <step>Note contradictions or debates</step>
  <step>Evaluate evidence quality</step>
  <step>Synthesize implications</step>
</analysis_framework>

For each paper:
<paper id="1">
  <methodology>[DESCRIBE]</methodology>
  <key_findings>[LIST]</key_findings>
  <limitations>[NOTE]</limitations>
</paper>

Then provide comparative analysis following the framework.
```

**Complex Reasoning Task:**
```
<thinking>
Before answering, work through:
1. What are the key assumptions?
2. What information is critical vs. nice-to-have?
3. What approaches could work?
4. What are the trade-offs?
5. What's the most robust solution?
</thinking>

Problem: [DETAILED_PROBLEM_DESCRIPTION]

Requirements:
- Must satisfy [CONSTRAINTS]
- Should optimize for [CRITERIA]
- Consider [EDGE_CASES]

Provide your solution with explicit reasoning.
```

---

## 3. Gemini (Google)

### Platform Capabilities

**Context Window:**
- Gemini 1.5 Pro: Up to 2M tokens
- Gemini 1.5 Flash: Up to 1M tokens
- Largest context window available

**Special Features:**
- Multimodal (text, image, video, audio)
- Code execution
- Google Search integration
- Long-context understanding
- Grounding with Google Search

### Optimization Strategies

#### 1. Multimodal Prompting

Combine text, images, and other modalities:

```
Analyze this [TOPIC] using multiple inputs:

Text Context:
[BACKGROUND_INFORMATION]

Image 1: [DESCRIBE]
Image 2: [DESCRIBE]

Tasks:
1. Identify patterns across modalities
2. Synthesize insights
3. Highlight discrepancies
4. Provide integrated analysis

Consider how visual and textual information complement each other.
```

#### 2. Code Execution

Leverage built-in code execution:

```
Task: [ANALYSIS_TASK]

Use Python to:
1. [STEP_1 with code]
2. [STEP_2 with code]
3. [STEP_3 with code]

Execute code and show:
- Code used
- Output generated
- Interpretation of results

Dataset: [DESCRIPTION or data]
```

#### 3. Long Context Optimization

Utilize massive context window:

```
I'm providing [LARGE_AMOUNT] of information:

[EXTENSIVE_CONTEXT - could be hundreds of pages]

Cross-reference Analysis:
- Find connections between [CONCEPT_A] across all documents
- Track evolution of [THEME] chronologically
- Identify contradictions or inconsistencies
- Build comprehensive knowledge map

This task requires analyzing the full corpus - don't summarize, deeply analyze.
```

#### 4. Grounding with Search

Request search-grounded responses:

```
Research [CURRENT_TOPIC] using Google Search for up-to-date information.

Requirements:
- Find latest developments (2024)
- Verify facts across multiple sources
- Identify expert opinions
- Note any controversies

Ground your response in search results and cite sources.
```

#### 5. Comparative Analysis

Optimize for Gemini's analytical strength:

```
Compare [ITEM_A] vs [ITEM_B] across multiple dimensions:

Dimensions:
- [DIMENSION_1]: [CRITERIA]
- [DIMENSION_2]: [CRITERIA]
- [DIMENSION_3]: [CRITERIA]

For each dimension:
1. Detailed comparison
2. Quantitative metrics (if available)
3. Trade-offs
4. Use cases where each excels

Synthesize into recommendation matrix:
| Use Case | Better Choice | Why |
|----------|---------------|-----|

Include visual comparison if helpful.
```

### Best Practices for Gemini

✅ **Do:**
- Leverage multimodal capabilities
- Use code execution for data tasks
- Take advantage of massive context
- Request search grounding for current info
- Structure comparative analyses
- Include visual elements when relevant

❌ **Don't:**
- Ignore multimodal opportunities
- Forget to specify modality relationships
- Assume code execution without requesting
- Skip search grounding for current topics
- Provide redundant context (excellent long-context handling)

### Gemini-Specific Examples

**Multimodal Analysis:**
```
Analyze this marketing campaign using:

1. Campaign Text:
[COPY]

2. Visual Assets:
[Provide images]

3. Video Content:
[Provide video]

Analysis Framework:
- Message consistency across modalities
- Visual-textual alignment
- Emotional impact by medium
- Target audience resonance
- Suggested improvements

Provide integrated analysis considering all inputs.
```

---

## 4. Platform Comparison

### Feature Matrix

| Feature | ChatGPT | Claude | Gemini |
|---------|---------|---------|--------|
| Context Window | 128K max | 200K | 2M max |
| Multimodal | ✓ (GPT-4V) | ✓ (Claude 3+) | ✓✓ (Native) |
| Code Execution | ✓ (Interpreter) | ✓ (Computer Use) | ✓ (Built-in) |
| Function Calling | ✓✓ | ✓ | ✓ |
| Custom Instructions | ✓ | ~ (via prompts) | ~ (via prompts) |
| Search Integration | ✓ (some versions) | ✗ | ✓✓ |
| Thinking Process | ~ (implicit) | ✓✓ (explicit tags) | ~ (implicit) |

### Strength-Based Selection

**Choose ChatGPT for:**
- Function calling workflows
- Custom instructions standardization
- Code interpreter data analysis
- Multi-turn conversations
- Plugin ecosystem integration

**Choose Claude for:**
- Long document analysis (50-200 pages)
- Complex reasoning tasks
- Ethical considerations important
- Extended thinking required
- Detailed, nuanced analysis

**Choose Gemini for:**
- Massive context (>200K tokens)
- Multimodal analysis
- Current information (search grounding)
- Comparative analysis
- Code execution + large context

---

## 5. Cross-Platform Best Practices

### Universal Principles

**1. Clarity Over Cleverness**
```
❌ Bad (clever but unclear):
"Embark upon an intellectual journey through the labyrinth of..."

✅ Good (clear):
"Analyze [TOPIC] focusing on [ASPECTS]"
```

**2. Explicit Over Implicit**
```
❌ Bad (implicit):
"Tell me about Python"

✅ Good (explicit):
"Explain Python's main use cases for beginners, focusing on:
- Web development
- Data science
- Automation
Include one code example for each."
```

**3. Structured Over Unstructured**
```
❌ Bad (unstructured):
"I need help with marketing and also can you look at my code and maybe some research too"

✅ Good (structured):
"Three tasks:

Task 1 - Marketing:
[Specific request]

Task 2 - Code Review:
[Specific request]

Task 3 - Research:
[Specific request]"
```

### Platform-Agnostic Template

Works well across all platforms:

```
# [TASK_TITLE]

## Role
You are a [SPECIFIC_EXPERT] with [CREDENTIALS].

## Context
[ESSENTIAL_BACKGROUND]

## Task
[CLEAR_OBJECTIVE]

## Requirements
1. [REQUIREMENT_1]
2. [REQUIREMENT_2]
3. [REQUIREMENT_3]

## Output Format
[STRUCTURE_SPECIFICATION]

## Constraints
- [CONSTRAINT_1]
- [CONSTRAINT_2]

## Success Criteria
- [CRITERION_1]
- [CRITERION_2]
```

### Migration Checklist

When moving prompts between platforms:

**From ChatGPT to Claude:**
- [ ] Remove function calling syntax
- [ ] Expand context if needed (200K available)
- [ ] Add thinking tags for reasoning
- [ ] Convert custom instructions to explicit prompt sections
- [ ] Adjust for Claude's verbose style

**From Claude to ChatGPT:**
- [ ] Condense context (128K limit)
- [ ] Remove thinking tags (use implicit reasoning)
- [ ] Convert to function calling if applicable
- [ ] Add custom instructions if appropriate
- [ ] Adjust for ChatGPT's concise style

**From Gemini to Others:**
- [ ] Split multimodal into separate requests or describe visuals
- [ ] Remove search grounding requests
- [ ] Adapt code execution format
- [ ] Reduce context if needed (smaller windows)
- [ ] Simplify long-context dependencies

**Universal Adaptation:**
- [ ] Test with platform-specific examples
- [ ] Verify output quality
- [ ] Adjust length/detail level
- [ ] Re-tune constraints
- [ ] Update platform-specific features

### Testing Across Platforms

```python
# Template for multi-platform testing
platforms = {
    'chatgpt': {
        'model': 'gpt-4-turbo',
        'context_limit': 128000,
        'adaptations': ['custom_instructions', 'function_calling']
    },
    'claude': {
        'model': 'claude-3-5-sonnet-20250514',
        'context_limit': 200000,
        'adaptations': ['thinking_tags', 'xml_structure']
    },
    'gemini': {
        'model': 'gemini-1.5-pro',
        'context_limit': 2000000,
        'adaptations': ['multimodal', 'code_execution']
    }
}

def adapt_prompt(base_prompt, platform):
    """Adapt prompt for specific platform"""
    adaptations = platforms[platform]['adaptations']
    
    adapted = base_prompt
    
    for adaptation in adaptations:
        adapted = apply_adaptation(adapted, adaptation)
    
    return adapted

def test_cross_platform(base_prompt, test_cases):
    """Test prompt across platforms"""
    results = {}
    
    for platform in platforms:
        adapted_prompt = adapt_prompt(base_prompt, platform)
        platform_results = []
        
        for test_case in test_cases:
            response = run_llm(adapted_prompt, test_case, platform)
            score = evaluate(response, test_case['expected'])
            platform_results.append(score)
        
        results[platform] = {
            'avg_score': mean(platform_results),
            'adapted_prompt': adapted_prompt
        }
    
    return results
```

## Troubleshooting

### Common Platform Issues

**ChatGPT:**
- **Issue:** Responses too verbose
  - **Solution:** Add "Be concise" + word limit
- **Issue:** Missing function calls
  - **Solution:** Explicitly state "Use [function] to..."
- **Issue:** Context overflow
  - **Solution:** Chunk into multiple requests

**Claude:**
- **Issue:** Over-cautious responses
  - **Solution:** Add context about use case legitimacy
- **Issue:** Not using thinking tags
  - **Solution:** Explicitly request `<thinking>...</thinking>`
- **Issue:** Too much detail
  - **Solution:** Add specific length constraints

**Gemini:**
- **Issue:** Not grounding in search
  - **Solution:** Explicitly request "Use Google Search to..."
- **Issue:** Multimodal confusion
  - **Solution:** Clearly label and reference each input type
- **Issue:** Code not executing
  - **Solution:** Explicitly say "Execute this code:"
