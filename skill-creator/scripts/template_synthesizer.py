#!/usr/bin/env python3
"""
Template Synthesizer for skill-creator-from-docs

Converts documentation examples into generalized, well-commented templates
with inline parameter explanations and sensible defaults.
"""

import json
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from enum import Enum


class TemplateType(Enum):
    """Types of templates that can be generated."""
    BASIC = "basic"
    ADVANCED = "advanced"
    CONFIGURATION = "configuration"
    WORKFLOW = "workflow"


@dataclass
class Template:
    """Represents a synthesized template."""
    name: str
    type: TemplateType
    language: str
    content: str
    placeholders: List[str] = field(default_factory=list)
    defaults: Dict[str, str] = field(default_factory=dict)
    usage_example: str = ""
    source_examples: List[int] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __repr__(self):
        return f"Template(name='{self.name}', type={self.type.value}, language='{self.language}')"


@dataclass
class ValidationResult:
    """Result of template validation."""
    is_valid: bool
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)


class TemplateSynthesizer:
    """Synthesize usable templates from documentation examples."""

    # Common placeholder patterns
    PLACEHOLDER_PATTERNS = {
        'url': r'https?://[^\s<>"\']+',
        'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'file_path': r'(?:/[\w.-]+)+|(?:[\w.-]+/)+[\w.-]+',
        'api_key': r'[A-Za-z0-9]{32,}',
        'number': r'\b\d+\b',
        'string': r"'[^']*'|\"[^\"]*\"",
        'variable': r'\$\{?\w+\}?',
    }

    def __init__(self, verbose: bool = True):
        self.verbose = verbose

    def log(self, message: str):
        """Log message if verbose mode enabled."""
        if self.verbose:
            print(f"[TemplateSynthesizer] {message}", file=sys.stderr)

    def synthesize_templates(
        self,
        examples: List[Dict[str, Any]],
        patterns: List[Dict[str, Any]],
        tool_type: str
    ) -> List[Template]:
        """
        Synthesize templates from examples and identified patterns.

        Args:
            examples: List of code examples from doc_analyzer
            patterns: List of patterns from doc_analyzer
            tool_type: Type of tool (cli, api, library, framework)

        Returns:
            List of Template objects
        """
        self.log(f"Synthesizing templates for {tool_type} tool")
        self.log(f"Input: {len(examples)} examples, {len(patterns)} patterns")

        templates = []

        # Group examples by language
        by_language = self._group_by_language(examples)

        for language, lang_examples in by_language.items():
            self.log(f"Processing {len(lang_examples)} {language} examples")

            # Create basic template from most common example
            basic = self._create_basic_template(lang_examples, language, tool_type)
            if basic:
                templates.append(basic)

            # Create advanced templates from patterns
            if patterns:
                advanced = self._create_advanced_templates(
                    lang_examples,
                    patterns,
                    language,
                    tool_type
                )
                templates.extend(advanced)

        self.log(f"✅ Generated {len(templates)} templates")
        return templates

    def _group_by_language(
        self,
        examples: List[Dict[str, Any]]
    ) -> Dict[str, List[Dict[str, Any]]]:
        """Group examples by programming language."""
        grouped = {}
        for example in examples:
            lang = example.get('language', 'unknown')
            if lang not in grouped:
                grouped[lang] = []
            grouped[lang].append(example)
        return grouped

    def _create_basic_template(
        self,
        examples: List[Dict[str, Any]],
        language: str,
        tool_type: str
    ) -> Optional[Template]:
        """Create basic template from most common/simplest example."""
        if not examples:
            return None

        # Find the simplest example (shortest, most basic)
        simplest = min(
            examples,
            key=lambda e: (
                e.get('example_type') != 'basic',  # Prefer basic examples
                len(e.get('code', ''))  # Then shortest
            )
        )

        code = simplest.get('code', '')
        if not code:
            return None

        self.log(f"Creating basic template from: {simplest.get('title', 'untitled')}")

        # Create template
        template_content = self._generalize_code(code, language)
        template_content = self.add_inline_comments(template_content, simplest, language)

        template = Template(
            name=f"{tool_type}_basic",
            type=TemplateType.BASIC,
            language=language,
            content=template_content,
            source_examples=[examples.index(simplest)],
            metadata={
                'source_title': simplest.get('title', ''),
                'created_at': datetime.now().isoformat()
            }
        )

        # Generate usage example
        template.usage_example = self.generate_usage_example(template, [simplest])

        return template

    def _create_advanced_templates(
        self,
        examples: List[Dict[str, Any]],
        patterns: List[Dict[str, Any]],
        language: str,
        tool_type: str
    ) -> List[Template]:
        """Create advanced templates from identified patterns."""
        templates = []

        for pattern in patterns:
            # Find examples that match this pattern
            pattern_examples = [
                examples[idx]
                for idx in pattern.get('example_ids', [])
                if idx < len(examples)
            ]

            if not pattern_examples:
                continue

            # Create template from pattern
            template = self._synthesize_from_pattern(
                pattern,
                pattern_examples,
                language,
                tool_type
            )

            if template:
                templates.append(template)

        return templates

    def _synthesize_from_pattern(
        self,
        pattern: Dict[str, Any],
        examples: List[Dict[str, Any]],
        language: str,
        tool_type: str
    ) -> Optional[Template]:
        """Synthesize template from a pattern and its examples."""
        common_structure = pattern.get('common_structure', '')
        variable_parts = pattern.get('variable_parts', [])

        if not common_structure:
            return None

        # Create template from common structure
        template_content = common_structure

        # Add placeholders for variable parts
        template_content = self._add_placeholders(
            template_content,
            variable_parts,
            language
        )

        # Add inline comments
        template_content = self.add_inline_comments(
            template_content,
            {'context': pattern.get('description', '')},
            language
        )

        template = Template(
            name=f"{tool_type}_{pattern.get('name', 'advanced')}",
            type=TemplateType.ADVANCED,
            language=language,
            content=template_content,
            source_examples=[examples.index(e) for e in examples if e in examples],
            metadata={
                'pattern_name': pattern.get('name', ''),
                'pattern_description': pattern.get('description', ''),
                'created_at': datetime.now().isoformat()
            }
        )

        return template

    def _generalize_code(self, code: str, language: str) -> str:
        """
        Generalize code by identifying and replacing specific values
        with placeholders.

        Args:
            code: Source code to generalize
            language: Programming language

        Returns:
            Generalized code with placeholders
        """
        generalized = code

        # Replace specific URLs
        generalized = re.sub(
            self.PLACEHOLDER_PATTERNS['url'],
            '${URL}',
            generalized
        )

        # Replace email addresses
        generalized = re.sub(
            self.PLACEHOLDER_PATTERNS['email'],
            '${EMAIL}',
            generalized
        )

        # Replace API keys (long alphanumeric strings)
        generalized = re.sub(
            r'\b[A-Za-z0-9]{32,}\b',
            '${API_KEY}',
            generalized
        )

        # Language-specific generalizations
        if language in ['bash', 'shell', 'sh']:
            # Replace file paths
            generalized = re.sub(
                r'(/[\w.-]+){2,}',
                '${FILE_PATH}',
                generalized
            )

        elif language in ['python', 'py']:
            # Replace string literals in function calls
            generalized = re.sub(
                r"([\w.]+\(['\"])([^'\"]+)(['\"])",
                r'\1${ARG}\3',
                generalized
            )

        elif language in ['javascript', 'js', 'typescript', 'ts']:
            # Replace string literals
            generalized = re.sub(
                r"(const|let|var)\s+\w+\s*=\s*['\"]([^'\"]+)['\"]",
                r"\1 VARIABLE = '${VALUE}'",
                generalized
            )

        return generalized

    def _add_placeholders(
        self,
        content: str,
        variable_parts: List[str],
        language: str
    ) -> str:
        """Add placeholder markers for variable parts."""
        result = content

        for var_part in variable_parts:
            # Create placeholder name from variable part
            placeholder_name = re.sub(r'\W+', '_', var_part).upper()
            placeholder = f"${{{placeholder_name}}}"

            # Replace the variable part with placeholder
            result = result.replace(var_part, placeholder)

        return result

    def add_inline_comments(
        self,
        template_content: str,
        context: Dict[str, Any],
        language: str
    ) -> str:
        """
        Add inline comments explaining parameters and sections.

        Args:
            template_content: Template code
            context: Context information (example or pattern data)
            language: Programming language

        Returns:
            Template with inline comments
        """
        # Determine comment syntax
        comment_syntax = self._get_comment_syntax(language)
        if not comment_syntax:
            return template_content

        lines = template_content.split('\n')
        commented_lines = []

        # Add header comment
        header = self._create_header_comment(context, comment_syntax)
        commented_lines.extend(header)

        # Process each line
        for line in lines:
            # Add comments for placeholders
            if '${' in line:
                placeholders = re.findall(r'\$\{(\w+)\}', line)
                if placeholders:
                    comment = f"{comment_syntax} {', '.join(placeholders)}: Replace with your value"
                    commented_lines.append(comment)

            commented_lines.append(line)

        return '\n'.join(commented_lines)

    def _get_comment_syntax(self, language: str) -> str:
        """Get comment syntax for language."""
        comment_map = {
            'python': '#',
            'py': '#',
            'bash': '#',
            'shell': '#',
            'sh': '#',
            'ruby': '#',
            'yaml': '#',
            'javascript': '//',
            'js': '//',
            'typescript': '//',
            'ts': '//',
            'java': '//',
            'go': '//',
            'rust': '//',
            'c': '//',
            'cpp': '//',
        }
        return comment_map.get(language.lower(), '#')

    def _create_header_comment(
        self,
        context: Dict[str, Any],
        comment_syntax: str
    ) -> List[str]:
        """Create header comment block for template."""
        lines = [
            f"{comment_syntax} Template: {context.get('title', 'Generated Template')}",
        ]

        if 'context' in context:
            lines.append(f"{comment_syntax} {context['context']}")

        if 'description' in context:
            lines.append(f"{comment_syntax} {context['description']}")

        lines.append(comment_syntax)
        return lines

    def create_variable_placeholders(self, template: Template) -> Template:
        """
        Create variable placeholders from template content.

        Updates template.placeholders list.
        """
        placeholders = re.findall(r'\$\{(\w+)\}', template.content)
        template.placeholders = list(set(placeholders))
        self.log(f"Found {len(template.placeholders)} placeholders: {', '.join(template.placeholders)}")
        return template

    def add_default_values(
        self,
        template: Template,
        examples: List[Dict[str, Any]]
    ) -> Template:
        """
        Add sensible default values to template based on examples.

        Updates template.defaults dict.
        """
        defaults = {}

        # Extract common values from examples
        for example in examples:
            code = example.get('code', '')

            # Find values for each placeholder
            for placeholder in template.placeholders:
                # Simple heuristic: find what was replaced
                pattern = f"\\$\\{{{placeholder}\\}}"

                # Look for common patterns
                if 'URL' in placeholder:
                    urls = re.findall(self.PLACEHOLDER_PATTERNS['url'], code)
                    if urls and placeholder not in defaults:
                        defaults[placeholder] = urls[0]

                elif 'FILE' in placeholder or 'PATH' in placeholder:
                    paths = re.findall(self.PLACEHOLDER_PATTERNS['file_path'], code)
                    if paths and placeholder not in defaults:
                        defaults[placeholder] = paths[0]

        template.defaults = defaults
        self.log(f"Generated {len(defaults)} default values")
        return template

    def validate_template_syntax(self, template: Template) -> ValidationResult:
        """
        Validate template syntax (non-blocking).

        Performs basic checks without execution.

        Args:
            template: Template to validate

        Returns:
            ValidationResult with any issues found
        """
        errors = []
        warnings = []
        suggestions = []

        content = template.content

        # Check for unclosed placeholders
        open_placeholders = content.count('${')
        close_placeholders = content.count('}')
        if open_placeholders != close_placeholders:
            errors.append(f"Mismatched placeholders: {open_placeholders} open, {close_placeholders} close")

        # Check for common syntax issues by language
        if template.language in ['python', 'py']:
            # Check for unmatched quotes
            single_quotes = content.count("'")
            double_quotes = content.count('"')
            if single_quotes % 2 != 0:
                warnings.append("Unmatched single quotes detected")
            if double_quotes % 2 != 0:
                warnings.append("Unmatched double quotes detected")

            # Check for indentation consistency
            lines = content.split('\n')
            tab_lines = sum(1 for line in lines if line.startswith('\t'))
            space_lines = sum(1 for line in lines if line.startswith('    '))
            if tab_lines > 0 and space_lines > 0:
                warnings.append("Mixed tabs and spaces in indentation")

        elif template.language in ['bash', 'shell', 'sh']:
            # Check for unmatched quotes
            if content.count('"') % 2 != 0:
                warnings.append("Unmatched double quotes in bash script")

        # Check for missing placeholders
        if not template.placeholders:
            suggestions.append("No placeholders found - consider if template needs variable parts")

        # Check for documentation
        comment_syntax = self._get_comment_syntax(template.language)
        if comment_syntax not in content:
            suggestions.append("Consider adding inline comments to explain usage")

        is_valid = len(errors) == 0

        result = ValidationResult(
            is_valid=is_valid,
            errors=errors,
            warnings=warnings,
            suggestions=suggestions
        )

        if is_valid:
            self.log(f"✅ Template '{template.name}' validation passed")
        else:
            self.log(f"❌ Template '{template.name}' validation failed: {len(errors)} errors")

        return result

    def generate_usage_example(
        self,
        template: Template,
        source_examples: List[Dict[str, Any]]
    ) -> str:
        """
        Generate usage example documentation for template.

        Args:
            template: Template to document
            source_examples: Original examples used to create template

        Returns:
            Markdown-formatted usage example
        """
        lines = [
            f"## Usage: {template.name}",
            "",
            f"**Type:** {template.type.value}",
            f"**Language:** {template.language}",
            "",
        ]

        # Add description from first source example
        if source_examples:
            first = source_examples[0]
            if 'context' in first:
                lines.append(f"**Description:** {first['context']}")
                lines.append("")

        # List placeholders
        if template.placeholders:
            lines.append("**Placeholders:**")
            for placeholder in sorted(template.placeholders):
                default = template.defaults.get(placeholder, 'No default')
                lines.append(f"- `${{{placeholder}}}`: {default}")
            lines.append("")

        # Show template
        lines.append("**Template:**")
        lines.append("```" + template.language)
        lines.append(template.content)
        lines.append("```")
        lines.append("")

        # Add example from source
        if source_examples and source_examples[0].get('code'):
            lines.append("**Example from documentation:**")
            lines.append("```" + template.language)
            lines.append(source_examples[0]['code'])
            lines.append("```")

        return '\n'.join(lines)

    def save_templates(
        self,
        templates: List[Template],
        output_dir: str
    ):
        """
        Save templates to directory.

        Args:
            templates: Templates to save
            output_dir: Directory to save to
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        self.log(f"Saving {len(templates)} templates to: {output_dir}")

        for template in templates:
            # Determine file extension
            ext_map = {
                'python': '.py',
                'py': '.py',
                'bash': '.sh',
                'shell': '.sh',
                'sh': '.sh',
                'javascript': '.js',
                'js': '.js',
                'typescript': '.ts',
                'ts': '.ts',
                'yaml': '.yaml',
                'json': '.json',
            }
            ext = ext_map.get(template.language.lower(), '.txt')

            # Save template file
            template_file = output_path / f"{template.name}{ext}"
            template_file.write_text(template.content, encoding='utf-8')

            # Save usage documentation
            usage_file = output_path / f"{template.name}_USAGE.md"
            usage_file.write_text(template.usage_example, encoding='utf-8')

        # Save metadata
        metadata = {
            'templates': [
                {
                    'name': t.name,
                    'type': t.type.value,
                    'language': t.language,
                    'placeholders': t.placeholders,
                    'defaults': t.defaults,
                    'source_examples': t.source_examples,
                    'metadata': t.metadata
                }
                for t in templates
            ],
            'created_at': datetime.now().isoformat(),
            'total_templates': len(templates)
        }

        metadata_file = output_path / '_templates_metadata.json'
        metadata_file.write_text(json.dumps(metadata, indent=2), encoding='utf-8')

        self.log(f"✅ Saved {len(templates)} templates + metadata")


def main():
    """CLI interface for template_synthesizer."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Synthesize templates from analyzed documentation"
    )
    parser.add_argument(
        'analysis_file',
        help='Path to analysis JSON file from doc_analyzer'
    )
    parser.add_argument(
        '--output-dir',
        default='templates',
        help='Directory to save templates (default: templates)'
    )
    parser.add_argument(
        '--validate',
        action='store_true',
        help='Validate templates after generation'
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

        # Extract data
        examples = analysis.get('examples', [])
        patterns = analysis.get('patterns', [])
        tool_type = analysis.get('tool_type', 'unknown')

        if not examples:
            print("⚠️  No examples found in analysis file", file=sys.stderr)
            return 0

        # Create synthesizer
        synthesizer = TemplateSynthesizer(verbose=not args.quiet)

        # Synthesize templates
        templates = synthesizer.synthesize_templates(examples, patterns, tool_type)

        if not templates:
            print("⚠️  No templates generated", file=sys.stderr)
            return 0

        # Add placeholders and defaults
        for template in templates:
            synthesizer.create_variable_placeholders(template)
            synthesizer.add_default_values(template, examples)

        # Validate if requested
        if args.validate:
            print("\nValidating templates...", file=sys.stderr)
            for template in templates:
                result = synthesizer.validate_template_syntax(template)
                if result.errors:
                    print(f"  ❌ {template.name}: {', '.join(result.errors)}", file=sys.stderr)
                elif result.warnings:
                    print(f"  ⚠️  {template.name}: {', '.join(result.warnings)}", file=sys.stderr)
                else:
                    print(f"  ✅ {template.name}: valid", file=sys.stderr)

        # Save templates
        synthesizer.save_templates(templates, args.output_dir)

        # Print summary
        print(f"\n✅ Template synthesis complete!")
        print(f"   Templates generated: {len(templates)}")
        print(f"   Output directory: {args.output_dir}")

        return 0

    except Exception as e:
        print(f"\n❌ Template synthesis failed: {e}", file=sys.stderr)
        if not args.quiet:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
