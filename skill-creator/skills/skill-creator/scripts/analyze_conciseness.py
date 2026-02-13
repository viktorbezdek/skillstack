#!/usr/bin/env python3
"""
Analyze skill conciseness and suggest improvements.
Helps identify verbose sections for trimming.

Usage:
    python analyze_conciseness.py <skill-dir>

Analyzes:
    - Token count by section (using tiktoken)
    - Verbosity patterns (definitions, hedge words, etc.)
    - Provides actionable suggestions for improvement
"""

import argparse
import sys
import re
from pathlib import Path


def count_tokens_simple(text):
    """
    Simple token estimation (words * 1.3 approximation).
    For accurate counting, install tiktoken: pip install tiktoken
    """
    try:
        import tiktoken
        encoding = tiktoken.get_encoding("cl100k_base")
        return len(encoding.encode(text))
    except ImportError:
        # Fallback: Simple approximation
        words = len(text.split())
        return int(words * 1.3)  # Rough approximation


def analyze_section(section_name, section_text):
    """Analyze a single section for verbosity."""
    tokens = count_tokens_simple(section_text)
    lines = len(section_text.split('\n'))
    words = len(section_text.split())

    # Identify potential verbosity patterns
    issues = []

    # Check for common definitions (over-explanation)
    definition_patterns = [
        (r'PDF \(Portable Document Format\)', 'Defines PDF'),
        (r'JSON \(JavaScript Object Notation\)', 'Defines JSON'),
        (r'API \(Application Programming Interface\)', 'Defines API'),
        (r'CSV \(Comma[- ]Separated Values?\)', 'Defines CSV'),
        (r'XML \(eXtensible Markup Language\)', 'Defines XML'),
        (r'URL \(Uniform Resource Locator\)', 'Defines URL'),
    ]

    for pattern, desc in definition_patterns:
        if re.search(pattern, section_text, re.IGNORECASE):
            issues.append(desc)

    # Check for long parenthetical definitions
    long_parens = re.findall(r'\([^)]{50,}\)', section_text)
    if long_parens:
        issues.append(f"Long parentheticals ({len(long_parens)})")

    # Check for excessive examples
    example_count = section_text.lower().count('example')
    if example_count > 5:
        issues.append(f"Many examples ({example_count})")

    # Check for hedge words
    hedge_words = ['basically', 'essentially', 'generally', 'typically', 'usually']
    hedges_found = [w for w in hedge_words if w in section_text.lower()]
    if hedges_found:
        issues.append(f"Hedge words: {', '.join(hedges_found)}")

    # Check for verbose phrases
    verbose_phrases = [
        'it is important to note that',
        'it should be noted that',
        'there are many ways to',
        'you can also',
        'as you can see',
        'keep in mind that'
    ]
    phrases_found = [p for p in verbose_phrases if p in section_text.lower()]
    if phrases_found:
        issues.append(f"Verbose phrases: {len(phrases_found)}")

    # Token density (tokens per line)
    density = tokens / lines if lines > 0 else 0

    return {
        'name': section_name,
        'tokens': tokens,
        'lines': lines,
        'words': words,
        'density': density,
        'issues': issues
    }


def main(skill_path):
    """Analyze skill and report on conciseness."""
    skill_file = Path(skill_path) / 'SKILL.md'

    if not skill_file.exists():
        print(f"❌ SKILL.md not found at {skill_path}")
        return 1

    content = skill_file.read_text()

    # Split into sections (## headings)
    sections = re.split(r'^##\s+(.+)$', content, flags=re.MULTILINE)

    # Handle frontmatter separately
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if frontmatter_match:
        body = frontmatter_match.group(2)
        sections = re.split(r'^##\s+(.+)$', body, flags=re.MULTILINE)

    # Analyze each section
    results = []
    if len(sections) > 1:
        for i in range(1, len(sections), 2):
            if i + 1 < len(sections):
                section_name = sections[i]
                section_text = sections[i + 1]
                results.append(analyze_section(section_name, section_text))
    else:
        # No sections, analyze whole file
        results.append(analyze_section("Entire file", content))

    # Report
    total_tokens = sum(r['tokens'] for r in results)
    total_lines = sum(r['lines'] for r in results)

    print(f"\n📊 Conciseness Analysis: {skill_path}")
    print(f"{'='*70}")
    print(f"Total tokens: {total_tokens:,}")
    print(f"Total lines: {total_lines:,}")
    print(f"Recommended: < 5,000 tokens for SKILL.md")
    print()

    # Overall assessment
    if total_tokens > 8000:
        status = "❌ EXCESSIVE"
        advice = "Critical: Urgently needs progressive disclosure and content trimming"
    elif total_tokens > 5000:
        status = "⚠️  VERBOSE"
        advice = "Consider: Use progressive disclosure, move details to references/"
    elif total_tokens > 3000:
        status = "🟡 ACCEPTABLE"
        advice = "Good: Could trim slightly but generally reasonable"
    else:
        status = "✅ CONCISE"
        advice = "Excellent: Token count is well-optimized"

    print(f"Status: {status}")
    print(f"Advice: {advice}")
    print()

    # Sort by token count
    results.sort(key=lambda x: x['tokens'], reverse=True)

    print("📝 Sections by token count:")
    print(f"{'='*70}")
    for r in results:
        if r['tokens'] < 500:
            status = "✅"
        elif r['tokens'] < 1000:
            status = "🟡"
        else:
            status = "⚠️"

        # Truncate long section names
        name = r['name'][:50] + "..." if len(r['name']) > 50 else r['name']

        print(f"{status} {name}")
        print(f"   Tokens: {r['tokens']:,} | Lines: {r['lines']} | Words: {r['words']:,} | Density: {r['density']:.1f} tok/line")

        if r['issues']:
            for issue in r['issues'][:2]:  # Show first 2 issues per section
                print(f"   💡 {issue}")
        print()

    # Recommendations
    print(f"{'='*70}")
    print("💡 RECOMMENDATIONS")
    print(f"{'='*70}")

    recommendations = []

    if total_tokens > 5000:
        recommendations.append("🔹 Use progressive disclosure - move details to references/")

    # Find sections with most issues
    sections_with_issues = [r for r in results if r['issues']]
    if sections_with_issues:
        top_section = sections_with_issues[0]
        recommendations.append(f"🔹 Start with '{top_section['name'][:40]}' - has {len(top_section['issues'])} issues")

    # Check for definition patterns
    if any('Defines' in str(r['issues']) for r in results):
        recommendations.append("🔹 Remove common concept definitions (PDF, JSON, API, etc.)")

    # Check for hedge words
    if any('Hedge words' in str(r['issues']) for r in results):
        recommendations.append("🔹 Remove hedge words (basically, essentially, typically)")

    # Check for verbose phrases
    if any('Verbose phrases' in str(r['issues']) for r in results):
        recommendations.append("🔹 Cut unnecessary preambles and filler phrases")

    # Check for excessive examples
    if any('Many examples' in str(r['issues']) for r in results):
        recommendations.append("🔹 Consolidate or remove excessive examples")

    if recommendations:
        for rec in recommendations:
            print(rec)
    else:
        print("✅ No major issues detected - skill is well-optimized!")

    print()
    print("Run validation for more checks:")
    print(f"  python scripts/validate_skill.py --full-check {skill_path}")
    print()

    return 0


def main_cli():
    parser = argparse.ArgumentParser(
        description='Analyze skill conciseness and suggest improvements',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze a skill directory
  python analyze_conciseness.py ./my-skill/

  # Show this help message
  python analyze_conciseness.py --help

Analysis includes:
  - Token count by section (using tiktoken if available)
  - Verbosity patterns (definitions, hedge words, etc.)
  - Actionable suggestions for improvement
  - Section-by-section breakdown
        """
    )

    parser.add_argument(
        'skill_dir',
        help='Path to skill directory to analyze'
    )

    args = parser.parse_args()
    return main(args.skill_dir)


if __name__ == '__main__':
    sys.exit(main_cli())
