#!/usr/bin/env python3
"""
Documentation Analyzer for skill-creator-from-docs

Analyzes extracted documentation to identify:
- Tool type (CLI, API, Library, Framework)
- Common workflows and usage patterns
- Code examples
- Patterns across examples
- Pitfalls and warnings
- Documentation gaps
"""

import re
import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Any, Optional, Set
from pathlib import Path

# Import from doc_extractor
try:
    from doc_extractor import DocumentationCorpus, Page
except ImportError:
    print("Error: doc_extractor module not found", file=sys.stderr)
    print("Make sure doc_extractor.py is in the same directory", file=sys.stderr)
    sys.exit(1)


class ToolType(Enum):
    """Classification of tool types."""
    CLI = "cli"
    API = "api"
    LIBRARY = "library"
    FRAMEWORK = "framework"
    UNKNOWN = "unknown"


@dataclass
class CodeExample:
    """Represents a code example extracted from documentation."""
    title: str
    language: str
    code: str
    source_url: str
    context: str = ""  # Surrounding text
    example_type: str = "basic"  # basic, advanced, edge_case

    def __repr__(self):
        return f"CodeExample(title='{self.title}', language='{self.language}', lines={len(self.code.split())})"


@dataclass
class Workflow:
    """Represents a common usage workflow."""
    name: str
    description: str
    steps: List[str]
    frequency: str = "common"  # common, occasional, advanced
    examples: List[CodeExample] = field(default_factory=list)
    source_urls: List[str] = field(default_factory=list)

    def __repr__(self):
        return f"Workflow(name='{self.name}', steps={len(self.steps)}, examples={len(self.examples)})"


@dataclass
class Pattern:
    """Represents a pattern identified across multiple examples."""
    name: str
    description: str
    occurrences: int
    example_ids: List[int]  # Indices into examples list
    common_structure: str
    variable_parts: List[str]

    def __repr__(self):
        return f"Pattern(name='{self.name}', occurrences={self.occurrences})"


@dataclass
class Pitfall:
    """Represents a documented pitfall or warning."""
    description: str
    source_url: str
    severity: str = "medium"  # low, medium, high
    context: str = ""

    def __repr__(self):
        return f"Pitfall(severity='{self.severity}', desc='{self.description[:50]}...')"


@dataclass
class Gap:
    """Represents a documentation gap or ambiguity."""
    description: str
    impact: str = "medium"  # low, medium, high
    status: str = "to_research"  # to_research, documented, resolved, accepted
    notes: str = ""

    def __repr__(self):
        return f"Gap(impact='{self.impact}', status='{self.status}')"


@dataclass
class AnalysisContext:
    """Complete analysis results."""
    tool_type: ToolType
    tool_type_confidence: float
    tool_type_reasoning: List[str]
    workflows: List[Workflow]
    examples: List[CodeExample]
    patterns: List[Pattern]
    pitfalls: List[Pitfall]
    gaps: List[Gap]
    metadata: Dict[str, Any] = field(default_factory=dict)

    def summary(self) -> str:
        """Generate summary string."""
        return f"""Analysis Summary:
- Tool Type: {self.tool_type.value} (confidence: {self.tool_type_confidence:.0%})
- Workflows: {len(self.workflows)}
- Examples: {len(self.examples)}
- Patterns: {len(self.patterns)}
- Pitfalls: {len(self.pitfalls)}
- Gaps: {len(self.gaps)}
"""


class DocAnalyzer:
    """Analyze documentation corpus."""

    # Tool type indicators
    CLI_INDICATORS = [
        'command', 'flag', 'option', '--', 'usage:', 'arguments:',
        'cli', 'command-line', 'terminal', 'shell', 'bash', '$'
    ]

    API_INDICATORS = [
        'endpoint', 'request', 'response', 'POST', 'GET', 'PUT', 'DELETE',
        'api', 'rest', 'http', 'json', 'authentication', 'header'
    ]

    LIBRARY_INDICATORS = [
        'import', 'class', 'function', 'method', 'module', 'package',
        'install', 'pip', 'npm', 'require', 'from', 'def '
    ]

    FRAMEWORK_INDICATORS = [
        'scaffold', 'generate', 'project', 'app', 'create-',
        'framework', 'boilerplate', 'template', 'structure'
    ]

    # Pitfall keywords
    PITFALL_KEYWORDS = [
        'warning:', 'note:', 'important:', '⚠️', 'caution:', 'attention:',
        'gotcha', 'common mistake', 'pitfall', 'error:', 'fails',
        'deprecated', 'breaking change'
    ]

    # Gap indicators
    GAP_INDICATORS = [
        'see documentation', 'refer to', 'advanced usage', 'for more details',
        'coming soon', 'TODO', 'WIP', 'not documented', 'tbd'
    ]

    def __init__(self, verbose: bool = True):
        self.verbose = verbose

    def log(self, message: str):
        """Log message if verbose."""
        if self.verbose:
            print(f"[DocAnalyzer] {message}", file=sys.stderr)

    def analyze(self, corpus: DocumentationCorpus) -> AnalysisContext:
        """
        Perform complete analysis on documentation corpus.

        Args:
            corpus: Extracted documentation corpus

        Returns:
            AnalysisContext with all analysis results
        """
        self.log(f"Analyzing corpus: {corpus.source}")
        self.log(f"Pages to analyze: {len(corpus.pages)}")

        # Combine all content for analysis
        full_content = "\n\n".join(page.content for page in corpus.pages)

        # Step 1: Classify tool type
        tool_type, confidence, reasoning = self.classify_tool_type(corpus)
        self.log(f"✅ Tool type: {tool_type.value} (confidence: {confidence:.0%})")

        # Step 2: Extract workflows
        workflows = self.extract_workflows(corpus)
        self.log(f"✅ Workflows identified: {len(workflows)}")

        # Step 3: Extract code examples
        examples = self.extract_examples(corpus)
        self.log(f"✅ Examples extracted: {len(examples)}")

        # Step 4: Identify patterns
        patterns = self.identify_patterns(examples)
        self.log(f"✅ Patterns found: {len(patterns)}")

        # Step 5: Extract pitfalls
        pitfalls = self.extract_pitfalls(corpus)
        self.log(f"✅ Pitfalls identified: {len(pitfalls)}")

        # Step 6: Analyze gaps
        gaps = self.analyze_gaps(corpus)
        self.log(f"✅ Gaps found: {len(gaps)}")

        # Create analysis context
        context = AnalysisContext(
            tool_type=tool_type,
            tool_type_confidence=confidence,
            tool_type_reasoning=reasoning,
            workflows=workflows,
            examples=examples,
            patterns=patterns,
            pitfalls=pitfalls,
            gaps=gaps,
            metadata={
                'source': corpus.source,
                'pages_analyzed': len(corpus.pages),
                'total_content_length': len(full_content)
            }
        )

        self.log("\n" + context.summary())
        return context

    def classify_tool_type(self, corpus: DocumentationCorpus) -> tuple[ToolType, float, List[str]]:
        """
        Classify the tool type based on documentation content.

        Returns:
            (ToolType, confidence_score, reasoning_list)
        """
        full_content = "\n".join(page.content.lower() for page in corpus.pages)

        scores = {
            ToolType.CLI: 0,
            ToolType.API: 0,
            ToolType.LIBRARY: 0,
            ToolType.FRAMEWORK: 0
        }

        reasoning = []

        # Count indicators
        for indicator in self.CLI_INDICATORS:
            count = full_content.count(indicator.lower())
            if count > 0:
                scores[ToolType.CLI] += count
                if count > 2:
                    reasoning.append(f"Found '{indicator}' {count} times")

        for indicator in self.API_INDICATORS:
            count = full_content.count(indicator.lower())
            if count > 0:
                scores[ToolType.API] += count
                if count > 2:
                    reasoning.append(f"Found '{indicator}' {count} times")

        for indicator in self.LIBRARY_INDICATORS:
            count = full_content.count(indicator.lower())
            if count > 0:
                scores[ToolType.LIBRARY] += count
                if count > 2:
                    reasoning.append(f"Found '{indicator}' {count} times")

        for indicator in self.FRAMEWORK_INDICATORS:
            count = full_content.count(indicator.lower())
            if count > 0:
                scores[ToolType.FRAMEWORK] += count
                if count > 2:
                    reasoning.append(f"Found '{indicator}' {count} times")

        # Determine winner
        if max(scores.values()) == 0:
            return ToolType.UNKNOWN, 0.0, ["No clear indicators found"]

        winner = max(scores, key=scores.get)
        total_score = sum(scores.values())
        confidence = scores[winner] / total_score if total_score > 0 else 0.0

        return winner, confidence, reasoning[:5]  # Top 5 reasons

    def extract_workflows(self, corpus: DocumentationCorpus) -> List[Workflow]:
        """Extract common workflows from documentation."""
        workflows = []

        for page in corpus.pages:
            # Look for numbered steps or procedure sections
            lines = page.content.split('\n')

            current_workflow = None
            current_steps = []

            for i, line in enumerate(lines):
                # Look for workflow headers
                if any(keyword in line.lower() for keyword in ['workflow', 'quick start', 'getting started', 'how to', 'tutorial']):
                    if current_workflow and current_steps:
                        workflows.append(current_workflow)

                    current_workflow = Workflow(
                        name=line.strip('#').strip(),
                        description="",
                        steps=[],
                        source_urls=[page.url]
                    )
                    current_steps = []

                # Look for numbered steps
                elif re.match(r'^\d+\.', line.strip()) or re.match(r'^-\s', line.strip()):
                    if current_workflow:
                        current_steps.append(line.strip())

            # Add last workflow
            if current_workflow and current_steps:
                current_workflow.steps = current_steps
                workflows.append(current_workflow)

        return workflows

    def extract_examples(self, corpus: DocumentationCorpus) -> List[CodeExample]:
        """Extract code examples from documentation."""
        examples = []

        for page in corpus.pages:
            # Find code blocks (markdown style)
            code_blocks = re.findall(
                r'```(\w+)?\n(.*?)\n```',
                page.content,
                re.DOTALL
            )

            for i, (language, code) in enumerate(code_blocks):
                if not language:
                    language = "unknown"

                # Try to find title/context before code block
                code_pos = page.content.find(f"```{language}\n{code}")
                context_start = max(0, code_pos - 200)
                context = page.content[context_start:code_pos].strip()

                # Extract title from nearby headings
                title = f"Example {len(examples) + 1}"
                for line in context.split('\n')[-3:]:
                    if line.startswith('#'):
                        title = line.strip('#').strip()
                        break

                example = CodeExample(
                    title=title,
                    language=language,
                    code=code.strip(),
                    source_url=page.url,
                    context=context[-100:] if len(context) > 100 else context
                )

                examples.append(example)

        return examples

    def identify_patterns(self, examples: List[CodeExample]) -> List[Pattern]:
        """Identify patterns across multiple code examples."""
        patterns = []

        # Group examples by language
        by_language = {}
        for i, example in enumerate(examples):
            if example.language not in by_language:
                by_language[example.language] = []
            by_language[example.language].append((i, example))

        # Look for common structures within each language
        for language, lang_examples in by_language.items():
            if len(lang_examples) < 2:
                continue

            # Simple pattern detection: look for common lines
            line_counts = {}
            for idx, example in lang_examples:
                for line in example.code.split('\n'):
                    line = line.strip()
                    if len(line) > 10:  # Skip very short lines
                        if line not in line_counts:
                            line_counts[line] = []
                        line_counts[line].append(idx)

            # Find lines that appear in multiple examples
            for line, indices in line_counts.items():
                if len(indices) >= 2:
                    pattern = Pattern(
                        name=f"{language.upper()} common pattern",
                        description=f"Line appears in {len(indices)} examples",
                        occurrences=len(indices),
                        example_ids=indices,
                        common_structure=line,
                        variable_parts=[]
                    )
                    patterns.append(pattern)

        # Limit to most frequent patterns
        patterns.sort(key=lambda p: p.occurrences, reverse=True)
        return patterns[:10]

    def extract_pitfalls(self, corpus: DocumentationCorpus) -> List[Pitfall]:
        """Extract pitfalls and warnings from documentation."""
        pitfalls = []

        for page in corpus.pages:
            lines = page.content.split('\n')

            for i, line in enumerate(lines):
                line_lower = line.lower()

                # Check for pitfall keywords
                for keyword in self.PITFALL_KEYWORDS:
                    if keyword in line_lower:
                        # Extract context (this line + next 2 lines)
                        context_lines = lines[i:min(i+3, len(lines))]
                        context = '\n'.join(context_lines).strip()

                        # Determine severity
                        severity = "medium"
                        if any(word in line_lower for word in ['critical', 'breaking', 'error']):
                            severity = "high"
                        elif any(word in line_lower for word in ['note', 'tip']):
                            severity = "low"

                        pitfall = Pitfall(
                            description=context[:200],
                            source_url=page.url,
                            severity=severity,
                            context=context
                        )
                        pitfalls.append(pitfall)
                        break  # One pitfall per line

        return pitfalls

    def analyze_gaps(self, corpus: DocumentationCorpus) -> List[Gap]:
        """Identify documentation gaps and ambiguities."""
        gaps = []

        for page in corpus.pages:
            content_lower = page.content.lower()

            for indicator in self.GAP_INDICATORS:
                if indicator in content_lower:
                    # Find the context around this indicator
                    pos = content_lower.find(indicator)
                    context_start = max(0, pos - 50)
                    context_end = min(len(page.content), pos + 150)
                    context = page.content[context_start:context_end]

                    # Determine impact
                    impact = "medium"
                    if any(word in context.lower() for word in ['important', 'required', 'must']):
                        impact = "high"
                    elif any(word in context.lower() for word in ['optional', 'advanced']):
                        impact = "low"

                    gap = Gap(
                        description=f"Reference to external documentation: {context[:100]}...",
                        impact=impact,
                        status="to_research",
                        notes=f"Found indicator: '{indicator}'"
                    )
                    gaps.append(gap)

        return gaps[:20]  # Limit gaps


def main():
    """CLI interface for doc_analyzer."""
    import argparse
    import json

    parser = argparse.ArgumentParser(
        description="Analyze extracted documentation"
    )
    parser.add_argument(
        'corpus_path',
        help='Path to corpus.json file (from doc_extractor)'
    )
    parser.add_argument(
        '--output',
        help='Output file for analysis results (JSON)'
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Suppress progress messages'
    )

    args = parser.parse_args()

    analyzer = DocAnalyzer(verbose=not args.quiet)

    try:
        # Load corpus
        corpus_path = Path(args.corpus_path)

        if corpus_path.is_dir():
            # Look for corpus.json in directory
            corpus_file = corpus_path / "corpus.json"
            if not corpus_file.exists():
                print(f"Error: No corpus.json found in {corpus_path}", file=sys.stderr)
                return 1
        else:
            corpus_file = corpus_path

        if not corpus_file.exists():
            print(f"Error: File not found: {corpus_file}", file=sys.stderr)
            return 1

        # Load corpus from JSON
        with open(corpus_file, 'r') as f:
            data = json.load(f)

        # Reconstruct corpus
        pages = [
            Page(
                url=p['url'],
                title=p['title'],
                content=p['content'],
                metadata=p.get('metadata', {})
            )
            for p in data['pages']
        ]

        corpus = DocumentationCorpus(
            source=data['source'],
            pages=pages,
            metadata=data.get('metadata', {})
        )

        # Analyze
        context = analyzer.analyze(corpus)

        # Output results
        if args.output:
            output_path = Path(args.output)

            # Convert to JSON-serializable format
            result = {
                'tool_type': context.tool_type.value,
                'tool_type_confidence': context.tool_type_confidence,
                'tool_type_reasoning': context.tool_type_reasoning,
                'workflows': [
                    {
                        'name': w.name,
                        'description': w.description,
                        'steps': w.steps,
                        'frequency': w.frequency
                    }
                    for w in context.workflows
                ],
                'examples': [
                    {
                        'title': e.title,
                        'language': e.language,
                        'code': e.code,
                        'source_url': e.source_url
                    }
                    for e in context.examples
                ],
                'patterns': [
                    {
                        'name': p.name,
                        'description': p.description,
                        'occurrences': p.occurrences
                    }
                    for p in context.patterns
                ],
                'pitfalls': [
                    {
                        'description': p.description,
                        'severity': p.severity,
                        'source_url': p.source_url
                    }
                    for p in context.pitfalls
                ],
                'gaps': [
                    {
                        'description': g.description,
                        'impact': g.impact,
                        'status': g.status
                    }
                    for g in context.gaps
                ],
                'metadata': context.metadata
            }

            output_path.write_text(json.dumps(result, indent=2), encoding='utf-8')
            print(f"\n✅ Analysis saved to: {output_path}")
        else:
            print("\n" + "="*60)
            print(context.summary())
            print("="*60)

        return 0

    except Exception as e:
        print(f"\n❌ Analysis failed: {e}", file=sys.stderr)
        if not args.quiet:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
