#!/usr/bin/env python3
"""
SKILL.md Generator for skill-creator-from-docs

Generates complete SKILL.md file from all analysis and generated components.
Applies progressive disclosure to keep main skill file < 500 lines.
"""

import json
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional


@dataclass
class SkillMD:
    """Complete SKILL.md content."""
    frontmatter: str
    overview: str
    quick_start: str
    workflows: str
    templates_ref: str
    guardrails_ref: str
    troubleshooting_ref: str
    see_also: str
    metadata: Dict[str, Any] = field(default_factory=dict)

    def compile(self) -> str:
        """Compile all sections into final SKILL.md."""
        sections = [
            self.frontmatter,
            "",
            self.overview,
            "",
            self.quick_start,
            "",
            self.workflows,
            "",
            self.templates_ref,
            "",
            self.guardrails_ref,
            "",
            self.troubleshooting_ref,
            "",
            self.see_also
        ]
        return '\n'.join(sections)


class SkillMDGenerator:
    """Generate SKILL.md from analysis and generated components."""

    FRONTMATTER_TEMPLATE = '''---
name: {skill_name}
description: {description}
---'''

    OVERVIEW_TEMPLATE = '''# {tool_name}

{description}

## When to Use This Skill

{use_when}

## What This Skill Provides

{provides}'''

    QUICK_START_TEMPLATE = '''## Quick Start

{quick_start_content}

**Next Steps:**
- Review common workflows below
- Check available templates in `templates/`
- Run pre-flight checks: `./scripts/validate_prereqs.sh`'''

    WORKFLOWS_TEMPLATE = '''## Common Workflows

{workflow_list}'''

    TEMPLATES_REF_TEMPLATE = '''## Available Templates

{template_list}

**Usage:**
1. Copy template from `templates/`
2. Customize placeholders (marked with `${{}}`)
3. Follow inline comments for guidance

See `templates/*/USAGE.md` for detailed documentation.'''

    GUARDRAILS_TEMPLATE = '''## Guardrails & Validation

This skill includes multi-layered guardrails to prevent common pitfalls:

**Layer 1: Inline Warnings**
Templates include `⚠️ PITFALL` comments at critical points.

**Layer 2: Pre-flight Validation**
Run before executing: `./scripts/validate_prereqs.sh`

**Layer 3: Checklists**
Manual validation: `checklists/pre-flight.md`

**Layer 4: Setup Automation**
Guided setup: `./scripts/setup.sh`

**Common Pitfalls:** {pitfall_count} identified and documented'''

    TROUBLESHOOTING_TEMPLATE = '''## Troubleshooting

If you encounter issues:

1. **Run automated validation**: `./scripts/validate_prereqs.sh`
2. **Check pre-flight checklist**: `checklists/pre-flight.md`
3. **Consult troubleshooting guide**: `docs/troubleshooting.md`
4. **Review examples**: `docs/examples.md`

**Decision Trees:** {tree_count} troubleshooting decision trees available in `docs/troubleshooting.md`'''

    SEE_ALSO_TEMPLATE = '''## See Also

- **Quick Reference**: `docs/quick-reference.md` - Cheatsheet for common operations
- **Examples**: `docs/examples.md` - Practical usage examples
- **Configuration**: `templates/config-template.yaml` - Configuration template
- **Research Log**: `RESEARCH_LOG.md` - Documentation analysis and decisions'''

    def __init__(self, verbose: bool = True):
        self.verbose = verbose

    def log(self, message: str):
        """Log message if verbose mode enabled."""
        if self.verbose:
            print(f"[SkillMDGenerator] {message}", file=sys.stderr)

    def generate_skill_md(
        self,
        analysis: Dict[str, Any],
        templates: Optional[Dict[str, Any]] = None,
        guardrails: Optional[Dict[str, Any]] = None,
        assets: Optional[Dict[str, Any]] = None
    ) -> SkillMD:
        """
        Generate complete SKILL.md from all components.

        Args:
            analysis: Analysis data from doc_analyzer
            templates: Template metadata (optional)
            guardrails: Guardrail metadata (optional)
            assets: Asset metadata (optional)

        Returns:
            SkillMD object with all sections
        """
        tool_type = analysis.get('tool_type', 'unknown')
        tool_name = analysis.get('metadata', {}).get('tool_name', 'Tool')

        self.log(f"Generating SKILL.md for {tool_name} ({tool_type})")

        # Extract data
        workflows = analysis.get('workflows', [])
        examples = analysis.get('examples', [])
        pitfalls = analysis.get('pitfalls', [])

        skill = SkillMD(
            frontmatter="",
            overview="",
            quick_start="",
            workflows="",
            templates_ref="",
            guardrails_ref="",
            troubleshooting_ref="",
            see_also="",
            metadata={
                'tool_name': tool_name,
                'tool_type': tool_type,
                'generated_at': datetime.now().isoformat()
            }
        )

        # Generate each section
        self.log("Generating frontmatter")
        skill.frontmatter = self.generate_frontmatter(
            tool_name, tool_type, workflows, pitfalls
        )

        self.log("Generating overview")
        skill.overview = self.generate_overview(
            tool_name, tool_type, workflows
        )

        self.log("Generating quick start")
        skill.quick_start = self.generate_quick_start(
            tool_name, examples, templates
        )

        self.log("Generating workflows section")
        skill.workflows = self.generate_workflows_section(workflows)

        self.log("Generating templates reference")
        skill.templates_ref = self.generate_templates_reference(templates)

        self.log("Generating guardrails reference")
        skill.guardrails_ref = self.generate_guardrails_reference(
            pitfalls, guardrails
        )

        self.log("Generating troubleshooting reference")
        skill.troubleshooting_ref = self.generate_troubleshooting_reference(
            pitfalls
        )

        self.log("Generating see also section")
        skill.see_also = self.SEE_ALSO_TEMPLATE

        self.log("✅ Generated complete SKILL.md")
        return skill

    def generate_frontmatter(
        self,
        tool_name: str,
        tool_type: str,
        workflows: List[Dict[str, Any]],
        pitfalls: List[Dict[str, Any]]
    ) -> str:
        """
        Generate YAML frontmatter.

        Args:
            tool_name: Name of the tool
            tool_type: Type (cli, api, library, framework)
            workflows: List of workflows
            pitfalls: List of pitfalls

        Returns:
            YAML frontmatter string
        """
        # Generate skill name (lowercase, hyphenated)
        skill_name = tool_name.lower().replace(' ', '-').replace('_', '-')

        # Generate description
        description = self._generate_description(tool_name, tool_type, workflows, pitfalls)

        frontmatter = self.FRONTMATTER_TEMPLATE.format(
            skill_name=skill_name,
            description=description
        )

        return frontmatter

    def _generate_description(
        self,
        tool_name: str,
        tool_type: str,
        workflows: List[Dict[str, Any]],
        pitfalls: List[Dict[str, Any]]
    ) -> str:
        """Generate skill description."""
        # Type-specific intro
        type_intros = {
            'cli': f"Use {tool_name} CLI effectively with templates, validation, and best practices.",
            'api': f"Integrate with {tool_name} API using tested patterns and error handling.",
            'library': f"Use {tool_name} library with type-safe patterns and examples.",
            'framework': f"Build applications with {tool_name} following proven workflows."
        }

        intro = type_intros.get(tool_type, f"Use {tool_name} with comprehensive guidance and templates.")

        # Add workflow count
        if workflows:
            intro += f" Includes {len(workflows)} documented workflows"

        # Add pitfall prevention
        if pitfalls:
            intro += f" and {len(pitfalls)} pitfall preventions"

        intro += "."

        return intro

    def generate_overview(
        self,
        tool_name: str,
        tool_type: str,
        workflows: List[Dict[str, Any]]
    ) -> str:
        """Generate overview section."""
        # Description
        description = f"Comprehensive skill for using {tool_name} effectively."

        # Use when
        use_when_items = [
            f"- Working with {tool_name}",
            f"- Need templates for common {tool_type} operations",
            "- Want validation before execution",
            "- Need troubleshooting guidance"
        ]

        if workflows:
            use_when_items.insert(1, f"- Following {tool_name} workflows")

        use_when = '\n'.join(use_when_items)

        # Provides
        provides_items = [
            "- **Tested Templates**: Ready-to-use code templates with inline comments",
            "- **Common Workflows**: Step-by-step guides for frequent tasks",
            "- **Pre-flight Validation**: Automated checks before execution",
            "- **Troubleshooting Trees**: Decision trees for common issues",
            "- **Quick Reference**: Cheatsheet for common operations",
            "- **Configuration Templates**: Example configuration files"
        ]

        provides = '\n'.join(provides_items)

        overview = self.OVERVIEW_TEMPLATE.format(
            tool_name=tool_name,
            description=description,
            use_when=use_when,
            provides=provides
        )

        return overview

    def generate_quick_start(
        self,
        tool_name: str,
        examples: List[Dict[str, Any]],
        templates: Optional[Dict[str, Any]]
    ) -> str:
        """Generate quick start section."""
        # Find simplest example or use first template
        content_parts = []

        content_parts.append(f"### Basic Usage\n")

        if examples and examples[0].get('code'):
            example = examples[0]
            code = example.get('code', '')
            language = example.get('language', '')
            title = example.get('title', 'Example')

            content_parts.append(f"**{title}:**\n")
            content_parts.append(f"```{language}\n{code}\n```")

        else:
            content_parts.append(f"Check `templates/` for ready-to-use templates.\n")

        content_parts.append("\n**Pre-flight Check:**")
        content_parts.append("```bash")
        content_parts.append("./scripts/validate_prereqs.sh")
        content_parts.append("```")

        quick_start = self.QUICK_START_TEMPLATE.format(
            quick_start_content='\n'.join(content_parts)
        )

        return quick_start

    def generate_workflows_section(
        self,
        workflows: List[Dict[str, Any]]
    ) -> str:
        """Generate workflows section."""
        workflow_items = []

        for i, workflow in enumerate(workflows[:5], 1):  # Top 5 workflows
            name = workflow.get('name', f'Workflow {i}')
            description = workflow.get('description', '')
            steps = workflow.get('steps', [])

            workflow_items.append(f"### {i}. {name}\n")

            if description:
                workflow_items.append(f"{description}\n")

            if steps:
                workflow_items.append("**Steps:**")
                for step_num, step in enumerate(steps[:5], 1):  # First 5 steps
                    workflow_items.append(f"{step_num}. {step}")
                workflow_items.append("")

        workflow_list = '\n'.join(workflow_items) if workflow_items else "See templates for common usage patterns."

        return self.WORKFLOWS_TEMPLATE.format(workflow_list=workflow_list)

    def generate_templates_reference(
        self,
        templates: Optional[Dict[str, Any]]
    ) -> str:
        """Generate templates reference section."""
        if not templates or 'templates' not in templates:
            template_list = "Templates available in `templates/` directory."
        else:
            template_items = []
            for template in templates.get('templates', [])[:10]:  # Max 10
                name = template.get('name', 'template')
                template_type = template.get('type', 'basic')
                language = template.get('language', '')

                template_items.append(f"- **{name}** ({template_type}): {language} template")

            template_list = '\n'.join(template_items) if template_items else "Check `templates/` directory."

        return self.TEMPLATES_REF_TEMPLATE.format(template_list=template_list)

    def generate_guardrails_reference(
        self,
        pitfalls: List[Dict[str, Any]],
        guardrails: Optional[Dict[str, Any]]
    ) -> str:
        """Generate guardrails reference section."""
        pitfall_count = len(pitfalls)

        return self.GUARDRAILS_TEMPLATE.format(pitfall_count=pitfall_count)

    def generate_troubleshooting_reference(
        self,
        pitfalls: List[Dict[str, Any]]
    ) -> str:
        """Generate troubleshooting reference section."""
        tree_count = min(len(pitfalls), 10)  # Max 10 decision trees

        return self.TROUBLESHOOTING_TEMPLATE.format(tree_count=tree_count)

    def save_skill_md(
        self,
        skill: SkillMD,
        output_path: str
    ):
        """
        Save SKILL.md to file.

        Args:
            skill: SkillMD object
            output_path: Path to save SKILL.md
        """
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        # Compile and save
        content = skill.compile()
        output.write_text(content, encoding='utf-8')

        # Count lines for progressive disclosure check
        line_count = len(content.split('\n'))

        self.log(f"✅ Saved SKILL.md ({line_count} lines)")

        if line_count > 500:
            self.log(f"⚠️  SKILL.md exceeds 500 lines - consider moving content to references/")

        return line_count


def main():
    """CLI interface for skill_md_generator."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate SKILL.md from analysis and components"
    )
    parser.add_argument(
        'analysis_file',
        help='Path to analysis JSON file from doc_analyzer'
    )
    parser.add_argument(
        '--templates',
        help='Path to templates metadata JSON (optional)'
    )
    parser.add_argument(
        '--guardrails',
        help='Path to guardrails metadata JSON (optional)'
    )
    parser.add_argument(
        '--assets',
        help='Path to assets metadata JSON (optional)'
    )
    parser.add_argument(
        '--output',
        default='SKILL.md',
        help='Output path for SKILL.md (default: SKILL.md)'
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Suppress progress messages'
    )

    args = parser.parse_args()

    try:
        # Load analysis file
        analysis_path = Path(args.analysis_file)
        if not analysis_path.exists():
            print(f"❌ Analysis file not found: {args.analysis_file}", file=sys.stderr)
            return 1

        with open(analysis_path, 'r', encoding='utf-8') as f:
            analysis = json.load(f)

        # Load optional metadata files
        templates = None
        if args.templates:
            templates_path = Path(args.templates)
            if templates_path.exists():
                with open(templates_path, 'r', encoding='utf-8') as f:
                    templates = json.load(f)

        guardrails = None
        if args.guardrails:
            guardrails_path = Path(args.guardrails)
            if guardrails_path.exists():
                with open(guardrails_path, 'r', encoding='utf-8') as f:
                    guardrails = json.load(f)

        assets = None
        if args.assets:
            assets_path = Path(args.assets)
            if assets_path.exists():
                with open(assets_path, 'r', encoding='utf-8') as f:
                    assets = json.load(f)

        # Create generator
        generator = SkillMDGenerator(verbose=not args.quiet)

        # Generate SKILL.md
        skill = generator.generate_skill_md(
            analysis,
            templates,
            guardrails,
            assets
        )

        # Save SKILL.md
        line_count = generator.save_skill_md(skill, args.output)

        # Print summary
        print(f"\n✅ SKILL.md generation complete!")
        print(f"   Tool: {skill.metadata['tool_name']} ({skill.metadata['tool_type']})")
        print(f"   Output: {args.output}")
        print(f"   Lines: {line_count}")

        if line_count > 500:
            print(f"   ⚠️  Exceeds 500-line recommendation for progressive disclosure")

        return 0

    except Exception as e:
        print(f"\n❌ SKILL.md generation failed: {e}", file=sys.stderr)
        if not args.quiet:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
