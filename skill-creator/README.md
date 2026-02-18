# Skill Creator

> Comprehensive skill creation framework combining philosophy-first design, evidence-based prompting, progressive disclosure, anti-pattern prevention, and enterprise-grade workflows.

## Overview

Creating effective Claude Code skills is itself a skill. The difference between a mediocre skill (a glorified checklist that rarely activates) and a great skill (an expert mental framework that reliably produces extraordinary results) comes down to deliberate design principles. This skill encodes the complete methodology for building production-grade skills, from initial intent analysis through validation and deployment.

This skill is for anyone creating, reviewing, or improving Claude Code skills -- whether you are building a skill from scratch, converting documentation into a skill, auditing existing skills for quality, or designing enterprise skill ecosystems. It covers the full lifecycle from philosophy-first design through adversarial testing.

Within the SkillStack collection, Skill Creator is the meta-skill -- the skill that builds other skills. It embodies the SkillStack philosophy that skills are mental frameworks (not checklists), encodes the progressive disclosure architecture (SKILL.md < 500 lines, details in references/), and provides the quality standards that all other skills in the collection aspire to meet.

## What's Included

### References: Core
- **skill-forge.md** -- Complete 8-phase methodology for production skill creation
- **skill_creation.md** -- 6-step workflow for creating skills from documentation
- **progressive_disclosure.md** -- Loading architecture: metadata -> instructions -> deep references
- **core_principles.md** -- Fundamental principles underlying effective skills

### References: Anti-Patterns and Best Practices
- **anti-patterns.md** -- Comprehensive anti-pattern catalog with detection and fixes
- **antipatterns.md** -- Additional anti-patterns and edge cases
- **best_practices_checklist.md** -- Quality checklist for skill assessment
- **shibboleths.md** -- Expert vs. novice knowledge encoding patterns

### References: Advanced Topics
- **evidence-based-prompting.md** -- Research-backed prompting techniques for skill instructions
- **prompting-principles.md** -- Prompting patterns and principles for skill content
- **composability.md** -- Skill composition patterns for building skill ecosystems
- **variation-patterns.md** -- Techniques for encouraging output diversity and avoiding convergence
- **degrees_of_freedom.md** -- Managing flexibility and constraint in skill design
- **philosophy-patterns.md** -- Patterns for establishing philosophy-first skill sections
- **token_efficiency.md** -- Token optimization techniques for skill content
- **optimization.md** -- Skill performance optimization strategies

### References: Enterprise and Workflows
- **skill-factory-workflow.md** -- Enterprise-scale skill creation workflows
- **SKILL-AUDIT-PROTOCOL.md** -- Formal audit methodology for skill quality assessment
- **REQUIRED-SECTIONS.md** -- Section requirements for different skill tiers
- **validation.md** -- Validation guidelines and criteria
- **validation-checklist.md** -- Detailed validation checklist
- **enterprise-checklist.md** -- Enterprise deployment checklist
- **enterprise-skill-factory-reference.md** -- Enterprise skill factory reference
- **enterprise-step-by-step-guide.md** -- Step-by-step enterprise guide
- **skill-lifecycle.md** -- Skill lifecycle management from creation to retirement

### References: Specialized Topics
- **agent-creator.md** -- Creating agent-powered skills with tool orchestration
- **agent-patterns.md** -- Agent design patterns for complex workflows
- **skill-creator-agent.md** -- Agent-based skill creation automation
- **auto_activation_patterns.md** -- Patterns for reliable skill activation
- **cookbook_patterns.md** -- Common skill patterns cookbook
- **core_standards.md** -- Core quality standards
- **comprehensive_checklist.md** -- Comprehensive skill quality checklist
- **detailed_process_steps.md** -- Detailed process documentation
- **editing_guidance.md** -- Guidelines for editing and improving skills
- **evaluation_driven_development.md** -- Using evaluation to drive skill development
- **file-structure-standards.md** -- File and directory structure standards
- **interactive-discovery.md** -- Interactive skill discovery patterns
- **mcp_vs_scripts.md** -- When to use MCP servers vs. scripts
- **micro-skill-creator.md** -- Creating focused micro-skills
- **multi_model_testing.md** -- Testing skills across multiple LLM models
- **output-patterns.md** -- Output format patterns
- **patterns.md** -- General skill design patterns
- **quick_reference.md** -- Quick reference card
- **quick-reference.md** -- Alternative quick reference
- **research_protocol.md** -- Research protocol for skill domain analysis
- **scoring-rubric.md** -- Scoring rubric for skill quality assessment
- **self-contained-tools.md** -- Self-contained tool patterns
- **skill-composition.md** -- Composing skills from smaller units
- **skill-creation-meta-principles.md** -- Meta-principles for skill creation
- **troubleshooting.md** -- Common issues and solutions
- **workflows.md** -- Workflow patterns for skill creation
- **EXPERTISE-ADDENDUM.md** -- Expertise encoding addendum
- **MIGRATION_GUIDE.md** -- Migration guide for skill format updates
- **RECURSIVE-IMPROVEMENT-ADDENDUM.md** -- Recursive improvement methodology

### Scripts: Core
- **init_skill.py** -- Initialize a new skill directory structure with scaffolded files
- **quick_validate.py** -- Fast validation checks for skill structure and content
- **validate_skill.py** -- Full validation suite for skill quality
- **analyze_skill.py** -- Quality scoring (0-100) with detailed breakdown
- **upgrade_skill.py** -- Generate improvement suggestions for existing skills
- **package_skill.py** -- Validate and package a skill to a distributable zip
- **create_skill.py** -- Alternative skill creation script
- **skill-generator.py** -- Skill generation automation

### Scripts: Documentation
- **extract_structure.py** -- Parse documentation to structured JSON
- **doc_analyzer.py** -- Analyze documentation for skill-relevant content
- **doc_extractor.py** -- Extract content from URLs for skill creation

### Scripts: Validation
- **test_activation.py** -- Test skill trigger activation against sample queries
- **check_self_contained.py** -- Verify all referenced files exist in the skill
- **validate_flowchart.sh** -- Validate Mermaid/ASCII flowchart syntax
- **validate_structure.sh** -- Validate skill directory structure
- **validate-skill.sh** -- Shell-based skill validation
- **validate_agent.py** -- Validate agent-powered skills

### Scripts: Generation
- **generate_agent.sh** -- Generate agent specification from skill
- **generate_boilerplate.py** -- Generate boilerplate files for a new skill
- **generate-structure.sh** -- Generate directory structure
- **asset_generator.py** -- Generate skill assets (templates, configs)
- **guardrail_generator.py** -- Generate guardrails and constraints
- **init_project.py** -- Initialize a skill project workspace
- **skill_md_generator.py** -- Generate SKILL.md from structured input
- **template_synthesizer.py** -- Synthesize templates from examples
- **analyze_conciseness.py** -- Analyze and improve skill conciseness
- **gap_researcher.py** -- Research gaps in skill coverage

### Scripts: Tests
- **tests/test_validate_skill.py** -- Unit tests for the validation script

### Templates: SKILL.md Templates
- **SKILL_TEMPLATE.md** -- Full-featured SKILL.md template
- **SKILL-template.md** -- Alternative SKILL.md template
- **minimal-skeleton/SKILL.md** -- Minimal starter SKILL.md
- **skill-skeleton/SKILL.md** -- Standard skeleton with references and scripts

### Templates: Script Templates
- **helper-script.py.template** -- Python helper script template
- **helper-script.sh.template** -- Bash helper script template
- **scripts-template.sh** -- Script boilerplate template

### Templates: Configuration
- **skill-schema.json** -- JSON schema for skill contracts and validation
- **skill-metrics.yaml** -- Metrics tracking template
- **config-template.json** -- JSON configuration template
- **config-template.yml.template** -- YAML configuration template
- **project-structure.yaml** -- Project structure specification
- **capabilities.json** -- Skill capabilities declaration
- **intake-template.yaml** -- Skill intake/requirements template

### Templates: Protocols
- **cov-protocol.md** -- Chain-of-Verification protocol for instruction verification
- **adversarial-testing-protocol.md** -- Red-team testing protocol

### Templates: Documentation
- **readme-template.md** -- README template for skills
- **README-scripts.md.template** -- Scripts README template
- **reference-template.md** -- Reference file template
- **instruction-template.md** -- Instruction writing template
- **examples-template.md** -- Examples file template
- **RESEARCH_LOG_TEMPLATE.md** -- Research log template
- **tool-skill-SKILL.md.template** -- Tool-based skill template
- **agent-spec.yaml** -- Agent specification template
- **gitignore-template.txt** -- .gitignore template for skills

### Examples: Complete Skills
- **algorithmic-art/** -- Creative coding skill example (SKILL.md + README)
- **artifacts-builder/** -- Artifact creation skill example
- **brand-guidelines/** -- Brand guidelines skill example
- **canvas-design/** -- Canvas design skill example
- **internal-comms/** -- Internal communications skill example
- **slack-gif-creator/** -- Slack GIF creator skill example
- **template-skill/** -- Bare template skill example
- **theme-factory/** -- Theme factory skill example
- **webapp-testing/** -- Web application testing skill example

### Examples: Document Skills
- **document-skills/pdf/** -- PDF generation skill with references
- **document-skills/docx/** -- DOCX generation skill with references
- **document-skills/pptx/** -- PPTX generation skill with references
- **document-skills/xlsx/** -- XLSX generation skill with references

### Examples: Good Skills
- **good-skills/clip-aware-embeddings/** -- Exemplary skill showing best practices (includes validation script)

### Examples: Transformation
- **before-after/basic-to-effective.md** -- Before/after showing a basic skill transformed into an effective one
- **before-after/procedural-to-philosophical.md** -- Before/after showing a checklist transformed into a mental framework
- **annotated/frontend-design-analysis.md** -- Line-by-line annotated analysis of a frontend skill

### Examples: Enterprise
- **enterprise-examples.md** -- Enterprise-scale skill examples and patterns

### Examples: Tests
- **tests/** -- 6 validation test cases covering basic templates, complex projects, and integration scenarios

### Assets
- **command_template.md** -- Command documentation template
- **frontmatter_templates.md** -- YAML frontmatter examples
- **llmstxt_templates.md** -- LLMs.txt format templates
- **readme_template.md** -- README asset template
- **skill_asset_template.md** -- Generic skill asset template
- **skill_md_template.md** -- SKILL.md content template
- **skill_reference_template.md** -- Reference file asset template
- **flowcharts/** -- 6 flowchart templates (approval workflows, decision trees, parallel execution, simple workflows, swimlane architecture, user onboarding)

## Key Features

- **Philosophy-first design**: Skills establish "how to think" before "what to do" -- mental frameworks, not checklists
- **Progressive disclosure architecture**: Metadata (~100 tokens) -> SKILL.md (<500 lines) -> references (as needed)
- **8-phase creation methodology**: Schema -> Cognitive Frame -> Intent Archaeology -> Use Cases -> Architecture -> Metadata -> Instructions -> Validation
- **Anti-pattern prevention**: Detects and prevents Reference Illusion, Description Soup, Template Theater, Everything Skill, and Orphaned Sections
- **Shibboleth encoding**: Captures deep expert knowledge that separates novice from expert understanding
- **Quality scoring**: Automated 0-100 scoring with analyze_skill.py targeting 70+ for production skills
- **Activation engineering**: Description field optimization with keywords AND NOT clauses for reliable triggering
- **Enterprise workflows**: Scalable processes for teams creating and maintaining large skill collections

## Usage Examples

Create a new skill from scratch:
```
Create a skill for Kubernetes deployment management. It should cover kubectl operations, Helm charts, and common debugging patterns. Target audience is developers who deploy but aren't DevOps specialists.
```

Convert documentation into a skill:
```
Here's the documentation for the Stripe API. Create a skill that encodes the key patterns, common pitfalls, and best practices for integrating Stripe payments.
```

Audit an existing skill:
```
Review this skill [paste SKILL.md] and score it. Check for proper description engineering, anti-pattern coverage, progressive disclosure, shibboleth encoding, and activation reliability.
```

Improve a low-scoring skill:
```
This skill scores 45/100 on analyze_skill.py. The main issues are: vague description, no anti-patterns section, and all content crammed into SKILL.md with no references. Help me upgrade it to 70+.
```

Design a skill ecosystem:
```
I need a set of composable skills for our data engineering team covering: dbt models, Airflow DAGs, data quality checks, and schema migrations. Design how these skills should relate to and reference each other.
```

## Quick Start

1. Decide whether you need the Quick Track (simple skills, phases 1-7) or Expert Track (production skills, phases 0-8).
2. Initialize your skill: `python scripts/init_skill.py <skill-name> --path <output-dir>`
3. Write your description with trigger keywords AND a NOT clause.
4. Establish philosophy first, then add procedures, decision trees, and anti-patterns.
5. Keep SKILL.md under 500 lines -- move deep content to `references/`.
6. Validate: `python scripts/quick_validate.py <skill-path>` for fast checks, `python scripts/analyze_skill.py <skill-path>` for scoring.
7. Test activation: does the skill trigger on the right queries and stay silent on the wrong ones?

## Related Skills

- **Prompt Engineering** -- Prompting principles that underpin effective skill instructions
- **Systems Thinking** -- Design skill ecosystems with feedback loops and composability
- **Creative Problem-Solving** -- Generate innovative skill designs and mental frameworks

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install skill-creator@skillstack` -- 34 production-grade skills for Claude Code.
