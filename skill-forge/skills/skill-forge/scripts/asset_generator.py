#!/usr/bin/env python3
"""
Asset Generator for skill-creator-from-docs

Generates support assets to help users succeed:
- Troubleshooting decision trees
- Quick reference cheatsheets
- Configuration file templates
- Example usage documentation
"""

import json
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional


@dataclass
class SupportAssets:
    """Complete set of support assets for a tool."""
    tool_name: str
    tool_type: str
    troubleshooting_tree: str = ""
    quick_reference: str = ""
    config_template: str = ""
    examples_doc: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


class AssetGenerator:
    """Generate support assets from analysis data."""

    # Troubleshooting tree template
    TROUBLESHOOTING_TEMPLATE = '''# Troubleshooting Guide: {tool_name}

**Generated:** {timestamp}

This guide helps diagnose and fix common issues with {tool_name}.

## Quick Diagnosis

Run the automated validation first:
```bash
./scripts/validate_prereqs.sh
```

If validation passes but you still have issues, use the decision trees below.

---

{decision_trees}

---

## General Troubleshooting Steps

1. **Check prerequisites**: Ensure all required tools/dependencies are installed
2. **Verify configuration**: Check environment variables and config files
3. **Review logs**: Look for error messages in output
4. **Consult documentation**: Review the official {tool_name} documentation
5. **Seek help**: If stuck, consult the community or support channels

## Getting Help

- Check the official documentation
- Search for similar issues in community forums
- Review the examples in `docs/examples.md`
- Run `./scripts/validate_prereqs.sh` for diagnostic information
'''

    DECISION_TREE_TEMPLATE = '''
## Problem: {problem}

**Symptoms:**
{symptoms}

**Diagnosis Steps:**

{diagnosis_steps}

**Common Solutions:**
{solutions}

**Prevention:**
{prevention}
'''

    # Quick reference template
    QUICK_REFERENCE_TEMPLATE = '''# Quick Reference: {tool_name}

**Generated:** {timestamp}

Quick reference for common {tool_name} operations.

## Common Workflows

{workflows}

## Key Commands

{commands}

## Configuration

{configuration}

## Tips & Tricks

{tips}

## See Also

- Full documentation: `README.md`
- Templates: `templates/`
- Troubleshooting: `docs/troubleshooting.md`
- Examples: `docs/examples.md`
'''

    # Config template
    CONFIG_FILE_TEMPLATE = '''# Configuration Template: {tool_name}
# Generated: {timestamp}
#
# Copy this file and customize for your needs.
# Remove the '#' to uncomment configuration options.

{config_sections}
'''

    # Examples documentation
    EXAMPLES_TEMPLATE = '''# Examples: {tool_name}

**Generated:** {timestamp}

Practical examples for using {tool_name}.

## Basic Usage

{basic_examples}

## Common Workflows

{workflow_examples}

## Advanced Usage

{advanced_examples}

## Tips

{tips}
'''

    def __init__(self, verbose: bool = True):
        self.verbose = verbose

    def log(self, message: str):
        """Log message if verbose mode enabled."""
        if self.verbose:
            print(f"[AssetGenerator] {message}", file=sys.stderr)

    def generate_assets(
        self,
        analysis: Dict[str, Any],
        templates: Optional[Dict[str, Any]] = None
    ) -> SupportAssets:
        """
        Generate complete support asset set.

        Args:
            analysis: Analysis data from doc_analyzer
            templates: Optional template metadata

        Returns:
            SupportAssets with all asset types
        """
        tool_type = analysis.get('tool_type', 'unknown')
        tool_name = analysis.get('metadata', {}).get('tool_name', 'Tool')

        self.log(f"Generating support assets for {tool_name} ({tool_type})")

        # Extract data
        pitfalls = analysis.get('pitfalls', [])
        workflows = analysis.get('workflows', [])
        examples = analysis.get('examples', [])

        assets = SupportAssets(
            tool_name=tool_name,
            tool_type=tool_type,
            metadata={
                'generated_at': datetime.now().isoformat(),
                'pitfalls_count': len(pitfalls),
                'workflows_count': len(workflows),
                'examples_count': len(examples)
            }
        )

        # Generate each asset type
        self.log("Generating troubleshooting decision tree")
        assets.troubleshooting_tree = self.generate_troubleshooting_tree(
            tool_name, pitfalls
        )

        self.log("Generating quick reference")
        assets.quick_reference = self.generate_quick_reference(
            tool_name, tool_type, workflows, examples
        )

        self.log("Generating configuration template")
        assets.config_template = self.generate_config_template(
            tool_name, tool_type, examples
        )

        self.log("Generating examples documentation")
        assets.examples_doc = self.generate_examples_doc(
            tool_name, workflows, examples
        )

        self.log("✅ Generated all support assets")
        return assets

    def generate_troubleshooting_tree(
        self,
        tool_name: str,
        pitfalls: List[Dict[str, Any]]
    ) -> str:
        """
        Generate troubleshooting decision tree from pitfalls.

        Args:
            tool_name: Name of the tool
            pitfalls: List of pitfalls from analysis

        Returns:
            Markdown troubleshooting guide
        """
        # Group pitfalls by type/category
        decision_trees = []

        for i, pitfall in enumerate(pitfalls[:10], 1):  # Top 10 pitfalls
            description = pitfall.get('description', '')
            severity = pitfall.get('severity', 'medium')
            context = pitfall.get('context', '')

            # Extract problem from description
            problem = description.split('.')[0] if '.' in description else description

            # Generate symptoms
            symptoms = self._generate_symptoms(description, context)

            # Generate diagnosis steps
            diagnosis_steps = self._generate_diagnosis_steps(description, severity)

            # Generate solutions
            solutions = self._generate_solutions(description, severity)

            # Generate prevention
            prevention = self._generate_prevention(description)

            tree = self.DECISION_TREE_TEMPLATE.format(
                problem=problem,
                symptoms=symptoms,
                diagnosis_steps=diagnosis_steps,
                solutions=solutions,
                prevention=prevention
            )

            decision_trees.append(tree)

        guide = self.TROUBLESHOOTING_TEMPLATE.format(
            tool_name=tool_name,
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            decision_trees='\n'.join(decision_trees)
        )

        self.log(f"Generated troubleshooting guide with {len(decision_trees)} decision trees")
        return guide

    def _generate_symptoms(self, description: str, context: str) -> str:
        """Generate symptom list from description."""
        symptoms = []

        # Common symptom patterns
        if 'error' in description.lower():
            symptoms.append("- Error message appears in output")
        if 'fail' in description.lower():
            symptoms.append("- Operation fails to complete")
        if 'not found' in description.lower():
            symptoms.append("- Command or resource not found")
        if 'permission' in description.lower():
            symptoms.append("- Permission denied errors")

        # Add context as symptom if available
        if context:
            symptoms.append(f"- {context}")

        return '\n'.join(symptoms) if symptoms else "- See error message for details"

    def _generate_diagnosis_steps(self, description: str, severity: str) -> str:
        """Generate diagnosis steps."""
        steps = []

        if 'not found' in description.lower():
            steps.append("1. **Check installation**: Verify the tool is installed")
            steps.append("   ```bash\n   which TOOL_NAME\n   ```")
            steps.append("2. **Check PATH**: Ensure installation directory is in PATH")
            steps.append("   ```bash\n   echo $PATH\n   ```")

        elif 'permission' in description.lower():
            steps.append("1. **Check file permissions**: Verify read/write access")
            steps.append("   ```bash\n   ls -la FILE_PATH\n   ```")
            steps.append("2. **Check ownership**: Ensure correct file ownership")
            steps.append("   ```bash\n   stat FILE_PATH\n   ```")

        elif 'api' in description.lower() or 'key' in description.lower():
            steps.append("1. **Check credentials**: Verify API key is set")
            steps.append("   ```bash\n   echo $API_KEY\n   ```")
            steps.append("2. **Test connectivity**: Verify network access")
            steps.append("   ```bash\n   curl -I https://api.example.com\n   ```")

        else:
            steps.append("1. **Review error message**: Check the full error output")
            steps.append("2. **Check prerequisites**: Run validation script")
            steps.append("   ```bash\n   ./scripts/validate_prereqs.sh\n   ```")

        return '\n'.join(steps) if steps else "1. Review the error message for specific details"

    def _generate_solutions(self, description: str, severity: str) -> str:
        """Generate solution list."""
        solutions = []

        if 'install' in description.lower():
            solutions.append("- **Install missing dependency**: Follow installation instructions")
            solutions.append("- **Update package manager**: Ensure package index is current")

        if 'config' in description.lower():
            solutions.append("- **Check configuration**: Review config file syntax")
            solutions.append("- **Use template**: Copy from `templates/config-template.yaml`")

        if 'permission' in description.lower():
            solutions.append("- **Fix permissions**: `chmod 644 FILE_PATH`")
            solutions.append("- **Fix ownership**: `chown USER:GROUP FILE_PATH`")

        if not solutions:
            solutions.append("- **Consult documentation**: Review official docs for guidance")
            solutions.append("- **Check examples**: See `docs/examples.md` for working examples")

        return '\n'.join(solutions)

    def _generate_prevention(self, description: str) -> str:
        """Generate prevention tips."""
        tips = []

        tips.append("- Run `./scripts/validate_prereqs.sh` before starting")
        tips.append("- Follow the pre-flight checklist: `checklists/pre-flight.md`")

        if 'config' in description.lower():
            tips.append("- Use provided configuration templates")

        if 'install' in description.lower():
            tips.append("- Use `./scripts/setup.sh` for automated setup")

        return '\n'.join(tips)

    def generate_quick_reference(
        self,
        tool_name: str,
        tool_type: str,
        workflows: List[Dict[str, Any]],
        examples: List[Dict[str, Any]]
    ) -> str:
        """
        Generate quick reference cheatsheet.

        Args:
            tool_name: Name of the tool
            tool_type: Type of tool
            workflows: List of workflows
            examples: Code examples

        Returns:
            Markdown quick reference
        """
        # Workflows section
        workflow_items = []
        for workflow in workflows[:5]:  # Top 5 workflows
            name = workflow.get('name', 'Workflow')
            description = workflow.get('description', '')
            steps = workflow.get('steps', [])

            workflow_items.append(f"### {name}")
            if description:
                workflow_items.append(f"\n{description}\n")

            if steps:
                workflow_items.append("**Steps:**")
                for step in steps[:3]:  # First 3 steps
                    workflow_items.append(f"1. {step}")
                workflow_items.append("")

        workflows_text = '\n'.join(workflow_items) if workflow_items else "See full documentation for workflows."

        # Commands section
        commands = self._extract_commands(examples, tool_type)
        commands_text = '\n'.join(commands) if commands else "See examples for command usage."

        # Configuration section
        config_text = self._generate_config_quick_ref(tool_type)

        # Tips section
        tips = [
            "- Use templates from `templates/` as starting points",
            "- Run validation before execution: `./scripts/validate_prereqs.sh`",
            "- Check troubleshooting guide if issues arise",
            "- Review examples for common patterns"
        ]
        tips_text = '\n'.join(tips)

        reference = self.QUICK_REFERENCE_TEMPLATE.format(
            tool_name=tool_name,
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            workflows=workflows_text,
            commands=commands_text,
            configuration=config_text,
            tips=tips_text
        )

        self.log("Generated quick reference cheatsheet")
        return reference

    def _extract_commands(
        self,
        examples: List[Dict[str, Any]],
        tool_type: str
    ) -> List[str]:
        """Extract command examples from code examples."""
        commands = []

        for example in examples[:5]:  # First 5 examples
            code = example.get('code', '')
            title = example.get('title', '')
            language = example.get('language', '')

            if language in ['bash', 'shell', 'sh']:
                # Extract bash commands
                lines = code.split('\n')
                for line in lines[:3]:  # First 3 lines
                    line = line.strip()
                    if line and not line.startswith('#'):
                        commands.append(f"```bash\n{line}\n```")
                        if title:
                            commands.append(f"*{title}*\n")
                        break

        return commands if commands else ["No command examples available"]

    def _generate_config_quick_ref(self, tool_type: str) -> str:
        """Generate configuration quick reference."""
        if tool_type in ['api', 'library']:
            return """
**Environment Variables:**
```bash
export API_KEY='your-key-here'
export API_URL='https://api.example.com'
```

**Config File:** `~/.config/tool/config.yaml`
"""
        elif tool_type == 'cli':
            return """
**Config File:** `~/.config/tool/config.yaml`

**Common Options:**
- `--verbose`: Enable detailed output
- `--config PATH`: Use custom config file
"""
        else:
            return "See configuration template in `templates/`"

    def generate_config_template(
        self,
        tool_name: str,
        tool_type: str,
        examples: List[Dict[str, Any]]
    ) -> str:
        """
        Generate configuration file template.

        Args:
            tool_name: Name of the tool
            tool_type: Type of tool
            examples: Code examples

        Returns:
            Configuration file template
        """
        sections = []

        # Common sections
        sections.append("""
# General Settings
# Uncomment and customize as needed

# name: my-project
# verbose: false
# log_level: info
""")

        # Type-specific sections
        if tool_type in ['api', 'library']:
            sections.append("""
# API Configuration
# api_key: YOUR_API_KEY_HERE
# api_url: https://api.example.com
# timeout: 30
# retry_attempts: 3
""")

        elif tool_type == 'cli':
            sections.append("""
# CLI Settings
# output_format: json
# color: auto
# pager: less
""")

        sections.append("""
# Advanced Settings
# cache_enabled: true
# cache_dir: ~/.cache/tool
# max_cache_size: 1GB
""")

        template = self.CONFIG_FILE_TEMPLATE.format(
            tool_name=tool_name,
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            config_sections='\n'.join(sections)
        )

        self.log("Generated configuration template")
        return template

    def generate_examples_doc(
        self,
        tool_name: str,
        workflows: List[Dict[str, Any]],
        examples: List[Dict[str, Any]]
    ) -> str:
        """
        Generate examples documentation.

        Args:
            tool_name: Name of the tool
            workflows: List of workflows
            examples: Code examples

        Returns:
            Markdown examples documentation
        """
        # Basic examples
        basic_examples = []
        for example in examples[:2]:  # First 2 examples
            if example.get('example_type') == 'basic':
                title = example.get('title', 'Example')
                code = example.get('code', '')
                language = example.get('language', '')
                context = example.get('context', '')

                basic_examples.append(f"### {title}\n")
                if context:
                    basic_examples.append(f"{context}\n")
                basic_examples.append(f"```{language}\n{code}\n```\n")

        basic_text = '\n'.join(basic_examples) if basic_examples else "See templates for basic examples."

        # Workflow examples
        workflow_examples = []
        for workflow in workflows[:3]:  # First 3 workflows
            name = workflow.get('name', 'Workflow')
            description = workflow.get('description', '')
            steps = workflow.get('steps', [])
            workflow_examples_list = workflow.get('examples', [])

            workflow_examples.append(f"### {name}\n")
            if description:
                workflow_examples.append(f"{description}\n")

            if steps:
                workflow_examples.append("**Steps:**")
                for i, step in enumerate(steps, 1):
                    workflow_examples.append(f"{i}. {step}")
                workflow_examples.append("")

            # Add code example if available
            if workflow_examples_list:
                first_example = workflow_examples_list[0]
                code = first_example.get('code', '')
                language = first_example.get('language', '')
                if code:
                    workflow_examples.append(f"```{language}\n{code}\n```\n")

        workflow_text = '\n'.join(workflow_examples) if workflow_examples else "See workflows in documentation."

        # Advanced examples
        advanced_examples = []
        for example in examples:
            if example.get('example_type') == 'advanced':
                title = example.get('title', 'Advanced Example')
                code = example.get('code', '')
                language = example.get('language', '')

                advanced_examples.append(f"### {title}\n")
                advanced_examples.append(f"```{language}\n{code}\n```\n")

        advanced_text = '\n'.join(advanced_examples) if advanced_examples else "See documentation for advanced usage."

        # Tips
        tips = [
            "- Start with basic examples and progress to advanced",
            "- Use templates as starting points for your own code",
            "- Review troubleshooting guide if examples don't work as expected",
            "- Customize examples for your specific use case"
        ]
        tips_text = '\n'.join(tips)

        doc = self.EXAMPLES_TEMPLATE.format(
            tool_name=tool_name,
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            basic_examples=basic_text,
            workflow_examples=workflow_text,
            advanced_examples=advanced_text,
            tips=tips_text
        )

        self.log("Generated examples documentation")
        return doc

    def save_assets(
        self,
        assets: SupportAssets,
        output_dir: str
    ):
        """
        Save support assets to directory.

        Args:
            assets: SupportAssets to save
            output_dir: Base output directory
        """
        base_path = Path(output_dir)
        base_path.mkdir(parents=True, exist_ok=True)

        self.log(f"Saving support assets to: {output_dir}")

        # Create docs directory
        docs_dir = base_path / 'docs'
        docs_dir.mkdir(exist_ok=True)

        # Create templates directory
        templates_dir = base_path / 'templates'
        templates_dir.mkdir(exist_ok=True)

        # Save troubleshooting guide
        troubleshooting_file = docs_dir / 'troubleshooting.md'
        troubleshooting_file.write_text(assets.troubleshooting_tree, encoding='utf-8')

        # Save quick reference
        reference_file = docs_dir / 'quick-reference.md'
        reference_file.write_text(assets.quick_reference, encoding='utf-8')

        # Save examples
        examples_file = docs_dir / 'examples.md'
        examples_file.write_text(assets.examples_doc, encoding='utf-8')

        # Save config template
        config_file = templates_dir / 'config-template.yaml'
        config_file.write_text(assets.config_template, encoding='utf-8')

        # Save metadata
        metadata = {
            'tool_name': assets.tool_name,
            'tool_type': assets.tool_type,
            'assets': {
                'troubleshooting': 'docs/troubleshooting.md',
                'quick_reference': 'docs/quick-reference.md',
                'examples': 'docs/examples.md',
                'config_template': 'templates/config-template.yaml'
            },
            'metadata': assets.metadata
        }

        metadata_file = base_path / 'assets_metadata.json'
        metadata_file.write_text(json.dumps(metadata, indent=2), encoding='utf-8')

        self.log("✅ Saved all support assets")


def main():
    """CLI interface for asset_generator."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate support assets from analyzed documentation"
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
        '--output-dir',
        default='assets',
        help='Directory to save assets (default: assets)'
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

        # Load templates if provided
        templates = None
        if args.templates:
            templates_path = Path(args.templates)
            if templates_path.exists():
                with open(templates_path, 'r', encoding='utf-8') as f:
                    templates = json.load(f)

        # Create generator
        generator = AssetGenerator(verbose=not args.quiet)

        # Generate assets
        assets = generator.generate_assets(analysis, templates)

        # Save assets
        generator.save_assets(assets, args.output_dir)

        # Print summary
        print(f"\n✅ Asset generation complete!")
        print(f"   Tool: {assets.tool_name} ({assets.tool_type})")
        print(f"   Output directory: {args.output_dir}")
        print(f"\n   Generated files:")
        print(f"   - docs/troubleshooting.md")
        print(f"   - docs/quick-reference.md")
        print(f"   - docs/examples.md")
        print(f"   - templates/config-template.yaml")
        print(f"   - assets_metadata.json")

        return 0

    except Exception as e:
        print(f"\n❌ Asset generation failed: {e}", file=sys.stderr)
        if not args.quiet:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
