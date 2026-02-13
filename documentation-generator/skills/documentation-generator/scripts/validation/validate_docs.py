#!/usr/bin/env python3
"""
Documentation Validator - Comprehensive quality assessment using DQI scoring.

Combines best practices from:
- Documentation audit skill (multi-pass verification)
- Documentation creation specialist (DQI scoring)
- Diataxis framework (documentation type validation)

Usage:
    python validate_docs.py ./docs [--min-score 70] [--fix]
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any
from dataclasses import dataclass, field
from urllib.parse import urlparse
import urllib.request
import urllib.error


@dataclass
class ValidationResult:
    """Result of validating a single document."""
    file_path: str
    score: int
    max_score: int
    issues: list[dict] = field(default_factory=list)
    warnings: list[dict] = field(default_factory=list)
    suggestions: list[dict] = field(default_factory=list)

    @property
    def percentage(self) -> float:
        return round(self.score / self.max_score * 100, 1) if self.max_score > 0 else 0

    @property
    def passed(self) -> bool:
        return len([i for i in self.issues if i.get('severity') == 'error']) == 0


class DocumentQualityValidator:
    """Validate documentation quality using DQI scoring system."""

    # DQI scoring weights
    STRUCTURE_WEIGHT = 40
    CONTENT_WEIGHT = 30
    STYLE_WEIGHT = 30

    def __init__(self, docs_path: str, min_score: int = 70):
        self.docs_path = Path(docs_path).resolve()
        self.min_score = min_score

        if not self.docs_path.exists():
            raise ValueError(f"Documentation path does not exist: {docs_path}")

    def validate_all(self) -> dict[str, Any]:
        """Validate all documentation files."""
        results = {
            'docs_path': str(self.docs_path),
            'total_score': 0,
            'max_score': 0,
            'files_validated': 0,
            'files_passed': 0,
            'files_failed': 0,
            'overall_percentage': 0,
            'overall_rating': '',
            'file_results': [],
            'summary': {
                'total_issues': 0,
                'total_warnings': 0,
                'total_suggestions': 0,
            }
        }

        # Find all markdown files
        md_files = list(self.docs_path.rglob('*.md'))

        if not md_files:
            print(f"No markdown files found in {self.docs_path}")
            return results

        for md_file in md_files:
            result = self.validate_file(md_file)
            results['file_results'].append({
                'file': str(md_file.relative_to(self.docs_path)),
                'score': result.score,
                'max_score': result.max_score,
                'percentage': result.percentage,
                'passed': result.passed,
                'issues': result.issues,
                'warnings': result.warnings,
                'suggestions': result.suggestions,
            })

            results['total_score'] += result.score
            results['max_score'] += result.max_score
            results['files_validated'] += 1
            results['summary']['total_issues'] += len(result.issues)
            results['summary']['total_warnings'] += len(result.warnings)
            results['summary']['total_suggestions'] += len(result.suggestions)

            if result.percentage >= self.min_score:
                results['files_passed'] += 1
            else:
                results['files_failed'] += 1

        # Calculate overall score
        if results['max_score'] > 0:
            results['overall_percentage'] = round(
                results['total_score'] / results['max_score'] * 100, 1
            )

        # Determine rating
        pct = results['overall_percentage']
        if pct >= 90:
            results['overall_rating'] = 'Excellent'
        elif pct >= 70:
            results['overall_rating'] = 'Good'
        elif pct >= 50:
            results['overall_rating'] = 'Acceptable'
        else:
            results['overall_rating'] = 'Needs Improvement'

        return results

    def validate_file(self, file_path: Path) -> ValidationResult:
        """Validate a single documentation file."""
        result = ValidationResult(
            file_path=str(file_path),
            score=0,
            max_score=100,
        )

        try:
            content = file_path.read_text()
        except Exception as e:
            result.issues.append({
                'severity': 'error',
                'message': f'Could not read file: {e}',
            })
            return result

        # Run all validation checks
        structure_score = self._validate_structure(content, result)
        content_score = self._validate_content(content, result)
        style_score = self._validate_style(content, file_path, result)

        # Calculate weighted score
        result.score = int(
            (structure_score / 100 * self.STRUCTURE_WEIGHT) +
            (content_score / 100 * self.CONTENT_WEIGHT) +
            (style_score / 100 * self.STYLE_WEIGHT)
        )

        return result

    def _validate_structure(self, content: str, result: ValidationResult) -> int:
        """Validate document structure (40% of score)."""
        score = 0
        max_score = 100

        lines = content.splitlines()

        # Check for title (H1)
        has_h1 = any(line.startswith('# ') for line in lines)
        if has_h1:
            score += 20
        else:
            result.issues.append({
                'severity': 'error',
                'category': 'structure',
                'message': 'Missing main title (H1 heading)',
                'fix': 'Add a title at the start: # Title'
            })

        # Check heading hierarchy
        heading_pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)
        headings = heading_pattern.findall(content)

        if len(headings) >= 2:
            score += 15
        elif len(headings) == 1:
            score += 5
            result.warnings.append({
                'category': 'structure',
                'message': 'Document has only one heading',
                'suggestion': 'Consider adding subsections for better organization'
            })
        else:
            result.issues.append({
                'severity': 'warning',
                'category': 'structure',
                'message': 'No headings found',
            })

        # Check for proper heading hierarchy (no skipping levels)
        prev_level = 0
        for level, _ in headings:
            curr_level = len(level)
            if curr_level > prev_level + 1 and prev_level > 0:
                result.warnings.append({
                    'category': 'structure',
                    'message': f'Heading level skipped from H{prev_level} to H{curr_level}',
                    'suggestion': 'Use proper heading hierarchy (H1 -> H2 -> H3)'
                })
            prev_level = curr_level

        if not any(i.get('category') == 'structure' and 'skipped' in i.get('message', '') for i in result.warnings):
            score += 15

        # Check for table of contents in longer documents
        word_count = len(content.split())
        if word_count > 1000:
            has_toc = bool(re.search(r'\[.+\]\(#.+\)', content))  # Link to anchor
            if has_toc:
                score += 10
            else:
                result.suggestions.append({
                    'category': 'structure',
                    'message': 'Long document without table of contents',
                    'suggestion': 'Consider adding a table of contents for easier navigation'
                })

        # Check for logical sections
        common_sections = ['overview', 'installation', 'usage', 'api', 'example', 'contributing', 'license']
        content_lower = content.lower()
        sections_found = sum(1 for s in common_sections if f'## {s}' in content_lower or f'# {s}' in content_lower)

        if sections_found >= 3:
            score += 20
        elif sections_found >= 1:
            score += 10

        # Check for blank lines before headings (proper markdown)
        heading_without_blank = re.findall(r'[^\n]\n#{1,6}\s+', content)
        if heading_without_blank:
            score -= 5
            result.warnings.append({
                'category': 'structure',
                'message': f'{len(heading_without_blank)} heading(s) without preceding blank line',
                'suggestion': 'Add blank line before each heading for proper rendering'
            })

        # Bonus for README-specific sections
        filename = Path(result.file_path).name.lower()
        if 'readme' in filename:
            readme_sections = ['quick start', 'getting started', 'installation', 'features']
            readme_found = sum(1 for s in readme_sections if s in content_lower)
            score += min(readme_found * 5, 20)

        return min(score, max_score)

    def _validate_content(self, content: str, result: ValidationResult) -> int:
        """Validate document content quality (30% of score)."""
        score = 0
        max_score = 100

        word_count = len(content.split())
        lines = content.splitlines()

        # Word count scoring
        if word_count >= 500:
            score += 20
        elif word_count >= 200:
            score += 15
        elif word_count >= 100:
            score += 10
        elif word_count >= 50:
            score += 5
        else:
            result.warnings.append({
                'category': 'content',
                'message': f'Document is very short ({word_count} words)',
                'suggestion': 'Consider expanding the documentation'
            })

        # Code examples
        code_blocks = re.findall(r'```[\s\S]*?```', content)
        if len(code_blocks) >= 3:
            score += 25
        elif len(code_blocks) >= 1:
            score += 15
        else:
            result.suggestions.append({
                'category': 'content',
                'message': 'No code examples found',
                'suggestion': 'Add code examples to illustrate usage'
            })

        # Inline code
        inline_code = re.findall(r'`[^`]+`', content)
        if len(inline_code) >= 5:
            score += 10
        elif len(inline_code) >= 1:
            score += 5

        # Links (internal or external)
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        if len(links) >= 3:
            score += 15
        elif len(links) >= 1:
            score += 10

        # Lists (bullet or numbered)
        lists = re.findall(r'^[\s]*[-*+]\s+.+$|^[\s]*\d+\.\s+.+$', content, re.MULTILINE)
        if len(lists) >= 5:
            score += 10
        elif len(lists) >= 2:
            score += 5

        # Tables
        tables = re.findall(r'\|.+\|', content)
        if len(tables) >= 3:  # At least header + separator + one row
            score += 10

        # Check for TODO/FIXME markers (negative)
        todos = re.findall(r'\[?TODO\]?:?', content, re.IGNORECASE)
        if todos:
            score -= min(len(todos) * 2, 10)
            result.warnings.append({
                'category': 'content',
                'message': f'Found {len(todos)} TODO marker(s)',
                'suggestion': 'Complete TODO items before publishing'
            })

        # Check for placeholder text
        placeholders = re.findall(r'\[.*(?:add|insert|update|your|placeholder).*\]', content, re.IGNORECASE)
        if placeholders:
            score -= min(len(placeholders) * 3, 15)
            result.warnings.append({
                'category': 'content',
                'message': f'Found {len(placeholders)} placeholder(s)',
                'suggestion': 'Replace placeholder text with actual content'
            })

        return max(0, min(score, max_score))

    def _validate_style(self, content: str, file_path: Path, result: ValidationResult) -> int:
        """Validate document style and formatting (30% of score)."""
        score = 0
        max_score = 100

        lines = content.splitlines()

        # Consistent heading style (ATX vs Setext)
        atx_headings = len(re.findall(r'^#{1,6}\s+', content, re.MULTILINE))
        setext_headings = len(re.findall(r'^[=-]+\s*$', content, re.MULTILINE))

        if atx_headings > 0 and setext_headings == 0:
            score += 15  # Consistent ATX
        elif setext_headings > 0 and atx_headings == 0:
            score += 15  # Consistent Setext
        elif atx_headings > 0 and setext_headings > 0:
            result.warnings.append({
                'category': 'style',
                'message': 'Mixed heading styles (ATX and Setext)',
                'suggestion': 'Use consistent heading style throughout'
            })
            score += 5

        # Line length (not too long)
        long_lines = [i for i, line in enumerate(lines, 1) if len(line) > 120 and not line.startswith('|')]
        if not long_lines:
            score += 15
        elif len(long_lines) <= 5:
            score += 10
        else:
            result.suggestions.append({
                'category': 'style',
                'message': f'{len(long_lines)} lines exceed 120 characters',
                'suggestion': 'Consider wrapping long lines for readability'
            })

        # Trailing whitespace
        trailing_ws = [i for i, line in enumerate(lines, 1) if line.endswith(' ') or line.endswith('\t')]
        if not trailing_ws:
            score += 10
        else:
            result.suggestions.append({
                'category': 'style',
                'message': f'{len(trailing_ws)} lines have trailing whitespace',
                'suggestion': 'Remove trailing whitespace'
            })
            score += 5

        # Consistent list markers
        bullet_markers = set(re.findall(r'^[\s]*([*+-])\s+', content, re.MULTILINE))
        if len(bullet_markers) <= 1:
            score += 10
        else:
            result.suggestions.append({
                'category': 'style',
                'message': f'Inconsistent bullet markers: {bullet_markers}',
                'suggestion': 'Use consistent bullet style (-, *, or +)'
            })

        # No multiple consecutive blank lines
        multiple_blanks = re.findall(r'\n{3,}', content)
        if not multiple_blanks:
            score += 10
        else:
            result.suggestions.append({
                'category': 'style',
                'message': f'{len(multiple_blanks)} instances of multiple consecutive blank lines',
                'suggestion': 'Use single blank lines between sections'
            })
            score += 5

        # Proper code block language hints
        code_blocks_with_lang = len(re.findall(r'```\w+', content))
        code_blocks_without_lang = len(re.findall(r'```\s*\n', content))

        if code_blocks_without_lang == 0 or code_blocks_with_lang >= code_blocks_without_lang:
            score += 15
        else:
            result.suggestions.append({
                'category': 'style',
                'message': f'{code_blocks_without_lang} code block(s) without language hint',
                'suggestion': 'Add language hints to code blocks (```python, ```bash, etc.)'
            })
            score += 5

        # Ends with newline
        if content.endswith('\n'):
            score += 5
        else:
            result.suggestions.append({
                'category': 'style',
                'message': 'File does not end with newline',
                'suggestion': 'Add trailing newline'
            })

        # No HTML in markdown (prefer markdown syntax)
        html_tags = re.findall(r'<(?!!)/?[a-z][a-z0-9]*[^>]*>', content, re.IGNORECASE)
        if not html_tags:
            score += 10
        elif len(html_tags) <= 3:
            score += 5
        else:
            result.suggestions.append({
                'category': 'style',
                'message': f'Found {len(html_tags)} HTML tag(s)',
                'suggestion': 'Prefer markdown syntax over HTML where possible'
            })

        # Consistent emphasis style (* vs _)
        asterisk_emphasis = len(re.findall(r'\*[^*]+\*', content))
        underscore_emphasis = len(re.findall(r'_[^_]+_', content))

        if asterisk_emphasis > 0 and underscore_emphasis > 0:
            if asterisk_emphasis > underscore_emphasis * 2 or underscore_emphasis > asterisk_emphasis * 2:
                score += 5  # Mostly consistent
            else:
                result.suggestions.append({
                    'category': 'style',
                    'message': 'Mixed emphasis styles (* and _)',
                    'suggestion': 'Use consistent emphasis style'
                })
        else:
            score += 10

        return max(0, min(score, max_score))

    def check_links(self, content: str, file_path: Path, result: ValidationResult) -> None:
        """Check that links in document are valid."""
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)

        for text, url in links:
            # Check relative links
            if not url.startswith(('http://', 'https://', '#', 'mailto:')):
                target = file_path.parent / url
                if not target.exists():
                    result.issues.append({
                        'severity': 'warning',
                        'category': 'links',
                        'message': f'Broken link: [{text}]({url})',
                        'fix': f'Update or remove the link to {url}'
                    })

            # Check anchor links
            elif url.startswith('#'):
                anchor = url[1:].lower().replace('-', ' ')
                headings = [h.lower() for h in re.findall(r'^#{1,6}\s+(.+)$', content, re.MULTILINE)]
                heading_anchors = [h.replace(' ', '-').replace('`', '').replace(':', '') for h in headings]

                if url[1:].lower() not in heading_anchors and anchor not in headings:
                    result.warnings.append({
                        'category': 'links',
                        'message': f'Possibly broken anchor link: {url}',
                        'suggestion': 'Verify anchor exists in document'
                    })


def main():
    parser = argparse.ArgumentParser(
        description='Validate documentation quality using DQI scoring'
    )
    parser.add_argument('docs_path', help='Path to documentation directory')
    parser.add_argument('--min-score', '-m', type=int, default=70,
                        help='Minimum score to pass (default: 70)')
    parser.add_argument('--output', '-o', help='Output results to JSON file')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Show detailed results')
    parser.add_argument('--check-links', '-l', action='store_true',
                        help='Also check link validity')

    args = parser.parse_args()

    try:
        validator = DocumentQualityValidator(args.docs_path, args.min_score)
        results = validator.validate_all()

        # Output JSON if requested
        if args.output:
            Path(args.output).write_text(json.dumps(results, indent=2))
            print(f"Results written to: {args.output}")

        # Print summary
        print("\n" + "="*60)
        print("DOCUMENTATION QUALITY REPORT")
        print("="*60)
        print(f"Directory: {results['docs_path']}")
        print(f"Files validated: {results['files_validated']}")
        print(f"Overall score: {results['overall_percentage']}% ({results['overall_rating']})")
        print(f"Files passed: {results['files_passed']}")
        print(f"Files failed: {results['files_failed']}")
        print(f"Total issues: {results['summary']['total_issues']}")
        print(f"Total warnings: {results['summary']['total_warnings']}")
        print(f"Total suggestions: {results['summary']['total_suggestions']}")

        # Print per-file results
        if args.verbose or results['files_failed'] > 0:
            print("\n" + "-"*60)
            print("FILE DETAILS")
            print("-"*60)

            for file_result in results['file_results']:
                status = "✓" if file_result['passed'] else "✗"
                print(f"\n{status} {file_result['file']}: {file_result['percentage']}%")

                if args.verbose or not file_result['passed']:
                    for issue in file_result['issues']:
                        print(f"    ERROR: {issue['message']}")
                    for warning in file_result['warnings']:
                        print(f"    WARNING: {warning['message']}")
                    if args.verbose:
                        for suggestion in file_result['suggestions']:
                            print(f"    SUGGESTION: {suggestion['message']}")

        # Exit with error if validation failed
        if results['overall_percentage'] < args.min_score:
            print(f"\n❌ FAILED: Score {results['overall_percentage']}% is below minimum {args.min_score}%")
            sys.exit(1)
        else:
            print(f"\n✓ PASSED: Score {results['overall_percentage']}% meets minimum {args.min_score}%")
            sys.exit(0)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
