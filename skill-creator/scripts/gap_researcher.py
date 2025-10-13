#!/usr/bin/env python3
"""
Gap Researcher for skill-creator-from-docs

Researches documentation gaps using Perplexity MCP to clarify ambiguities
and fill in missing information from external sources.
"""

import json
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional


@dataclass
class ResearchQuery:
    """Represents a research query to be executed."""
    gap_id: int
    question: str
    context: str
    priority: str = "medium"  # low, medium, high
    status: str = "pending"  # pending, completed, failed


@dataclass
class ResearchFinding:
    """Represents findings from a research query."""
    query_id: int
    question: str
    answer: str
    sources: List[str]
    confidence: str = "medium"  # low, medium, high
    relevance: str = "general"  # general, task_specific
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class ResearchLog:
    """Complete research log documenting all queries and findings."""
    source: str
    queries: List[ResearchQuery]
    findings: List[ResearchFinding]
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if 'created_at' not in self.metadata:
            self.metadata['created_at'] = datetime.now().isoformat()

    def get_finding_for_query(self, query_id: int) -> Optional[ResearchFinding]:
        """Find research finding for a specific query."""
        for finding in self.findings:
            if finding.query_id == query_id:
                return finding
        return None

    def get_general_findings(self) -> List[ResearchFinding]:
        """Get findings marked as generally useful."""
        return [f for f in self.findings if f.relevance == "general"]

    def get_task_specific_findings(self) -> List[ResearchFinding]:
        """Get findings marked as task-specific."""
        return [f for f in self.findings if f.relevance == "task_specific"]


class GapResearcher:
    """Research documentation gaps using Perplexity MCP."""

    def __init__(self, use_perplexity_mcp: bool = True, verbose: bool = True):
        self.use_perplexity_mcp = use_perplexity_mcp
        self.verbose = verbose

    def log(self, message: str):
        """Log message if verbose mode enabled."""
        if self.verbose:
            print(f"[GapResearcher] {message}", file=sys.stderr)

    def generate_queries_from_gaps(
        self,
        gaps: List[Dict[str, Any]],
        context: str = ""
    ) -> List[ResearchQuery]:
        """
        Generate research queries from identified gaps.

        Args:
            gaps: List of gap dictionaries from doc_analyzer
            context: Additional context about the tool/documentation

        Returns:
            List of ResearchQuery objects prioritized by impact
        """
        queries = []

        for i, gap in enumerate(gaps):
            description = gap.get('description', '')
            impact = gap.get('impact', 'medium')

            # Convert impact to priority
            priority_map = {
                'low': 'low',
                'medium': 'medium',
                'high': 'high'
            }
            priority = priority_map.get(impact, 'medium')

            # Generate specific question from gap description
            question = self._formulate_question(description, context)

            query = ResearchQuery(
                gap_id=i,
                question=question,
                context=context,
                priority=priority
            )
            queries.append(query)

        self.log(f"Generated {len(queries)} research queries from gaps")
        return queries

    def _formulate_question(self, gap_description: str, context: str) -> str:
        """
        Formulate a specific research question from a gap description.

        Args:
            gap_description: Description of the documentation gap
            context: Tool/library context

        Returns:
            Specific research question
        """
        # Basic heuristics for question formulation
        if "mentioned but not explained" in gap_description.lower():
            # Extract the feature name
            feature = gap_description.split("'")[1] if "'" in gap_description else gap_description
            return f"How does {feature} work? Provide detailed explanation with examples."

        if "see documentation" in gap_description.lower():
            # External reference
            topic = gap_description.split("for")[1].strip() if "for" in gap_description else gap_description
            return f"What are the details of {topic}? Include usage examples and best practices."

        # Generic formulation
        return f"{gap_description} - Provide detailed explanation with examples and common use cases."

    def research_query(
        self,
        query: ResearchQuery,
        recency: str = "month"
    ) -> Optional[ResearchFinding]:
        """
        Research a single query using Perplexity MCP.

        Args:
            query: ResearchQuery to execute
            recency: Recency filter for Perplexity (day, week, month, year)

        Returns:
            ResearchFinding if successful, None if failed
        """
        self.log(f"Researching: {query.question[:80]}...")

        if self.use_perplexity_mcp:
            return self._research_with_perplexity(query, recency)
        else:
            return self._research_fallback(query)

    def _research_with_perplexity(
        self,
        query: ResearchQuery,
        recency: str
    ) -> Optional[ResearchFinding]:
        """
        Research using Perplexity MCP.

        This method integrates with the Perplexity MCP server.
        """
        self.log("Using Perplexity MCP for research")

        try:
            # TODO: Integrate with Perplexity MCP
            # For now, return placeholder
            self.log("⚠️  Perplexity MCP integration not yet implemented")
            return self._research_fallback(query)

        except Exception as e:
            self.log(f"⚠️  Perplexity research failed: {e}")
            return None

    def _research_fallback(self, query: ResearchQuery) -> Optional[ResearchFinding]:
        """
        Fallback research method when Perplexity MCP unavailable.

        Returns a placeholder finding indicating manual research needed.
        """
        self.log("Using fallback (manual research required)")

        finding = ResearchFinding(
            query_id=query.gap_id,
            question=query.question,
            answer="[Manual research required - Perplexity MCP not available]",
            sources=["[Requires human review]"],
            confidence="low",
            relevance="task_specific"
        )

        return finding

    def research_all(
        self,
        queries: List[ResearchQuery],
        max_queries: Optional[int] = None,
        recency: str = "month"
    ) -> ResearchLog:
        """
        Research all queries and compile findings.

        Args:
            queries: List of ResearchQuery objects
            max_queries: Optional limit on number of queries to execute
            recency: Recency filter for Perplexity

        Returns:
            ResearchLog with all findings
        """
        # Sort by priority (high -> medium -> low)
        priority_order = {'high': 0, 'medium': 1, 'low': 2}
        sorted_queries = sorted(
            queries,
            key=lambda q: priority_order.get(q.priority, 1)
        )

        # Limit queries if specified
        if max_queries:
            sorted_queries = sorted_queries[:max_queries]
            self.log(f"Limiting to {max_queries} highest priority queries")

        findings = []

        for query in sorted_queries:
            finding = self.research_query(query, recency)

            if finding:
                findings.append(finding)
                query.status = "completed"
                self.log(f"✅ Query {query.gap_id}: completed")
            else:
                query.status = "failed"
                self.log(f"❌ Query {query.gap_id}: failed")

        log = ResearchLog(
            source="gap_research",
            queries=sorted_queries,
            findings=findings,
            metadata={
                'total_queries': len(sorted_queries),
                'completed': len([q for q in sorted_queries if q.status == "completed"]),
                'failed': len([q for q in sorted_queries if q.status == "failed"]),
                'recency': recency
            }
        )

        self.log(f"Research complete: {len(findings)} findings from {len(sorted_queries)} queries")
        return log

    def classify_findings(self, log: ResearchLog) -> ResearchLog:
        """
        Classify findings as generally useful vs task-specific.

        Updates finding.relevance based on content analysis.

        Args:
            log: ResearchLog with findings to classify

        Returns:
            Updated ResearchLog
        """
        self.log("Classifying findings...")

        for finding in log.findings:
            # Simple heuristics for classification
            # Could be enhanced with more sophisticated analysis

            answer_lower = finding.answer.lower()

            # Indicators of general usefulness
            general_indicators = [
                'best practice',
                'common pattern',
                'typical usage',
                'recommended approach',
                'standard method',
                'widely used',
                'production use'
            ]

            # Indicators of task-specificity
            specific_indicators = [
                'edge case',
                'specific scenario',
                'rare situation',
                'advanced feature',
                'not commonly',
                'manual research required'
            ]

            general_score = sum(1 for ind in general_indicators if ind in answer_lower)
            specific_score = sum(1 for ind in specific_indicators if ind in answer_lower)

            if general_score > specific_score:
                finding.relevance = "general"
            else:
                finding.relevance = "task_specific"

        general = len(log.get_general_findings())
        specific = len(log.get_task_specific_findings())

        self.log(f"Classification: {general} general, {specific} task-specific")
        return log

    def save_research_log(
        self,
        log: ResearchLog,
        output_path: str,
        format: str = "json"
    ):
        """
        Save research log to file.

        Args:
            log: ResearchLog to save
            output_path: Path to save to
            format: 'json' or 'markdown'
        """
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        if format == "json":
            data = {
                'source': log.source,
                'metadata': log.metadata,
                'queries': [asdict(q) for q in log.queries],
                'findings': [asdict(f) for f in log.findings]
            }

            output.write_text(json.dumps(data, indent=2), encoding='utf-8')
            self.log(f"✅ Saved research log (JSON) to: {output_path}")

        elif format == "markdown":
            md = self._format_as_markdown(log)
            output.write_text(md, encoding='utf-8')
            self.log(f"✅ Saved research log (Markdown) to: {output_path}")

        else:
            raise ValueError(f"Unknown format: {format}")

    def _format_as_markdown(self, log: ResearchLog) -> str:
        """Format research log as markdown."""
        lines = [
            "# Research Log",
            "",
            f"**Source:** {log.source}",
            f"**Created:** {log.metadata.get('created_at')}",
            "",
            "## Summary",
            "",
            f"- Total Queries: {log.metadata.get('total_queries', 0)}",
            f"- Completed: {log.metadata.get('completed', 0)}",
            f"- Failed: {log.metadata.get('failed', 0)}",
            f"- General Findings: {len(log.get_general_findings())}",
            f"- Task-Specific Findings: {len(log.get_task_specific_findings())}",
            "",
            "---",
            "",
        ]

        # General findings first
        general = log.get_general_findings()
        if general:
            lines.extend([
                "## General Findings",
                "",
                "*These findings are generally useful and should be incorporated into the final skill.*",
                ""
            ])

            for finding in general:
                lines.extend([
                    f"### Query {finding.query_id}: {finding.question}",
                    "",
                    f"**Confidence:** {finding.confidence}",
                    "",
                    f"**Answer:**",
                    "",
                    finding.answer,
                    "",
                    f"**Sources:**",
                    ""
                ])
                for source in finding.sources:
                    lines.append(f"- {source}")
                lines.extend(["", "---", ""])

        # Task-specific findings
        specific = log.get_task_specific_findings()
        if specific:
            lines.extend([
                "## Task-Specific Findings",
                "",
                "*These findings are kept in the research log but not incorporated into the final skill.*",
                ""
            ])

            for finding in specific:
                lines.extend([
                    f"### Query {finding.query_id}: {finding.question}",
                    "",
                    f"**Confidence:** {finding.confidence}",
                    "",
                    f"**Answer:**",
                    "",
                    finding.answer,
                    "",
                    f"**Sources:**",
                    ""
                ])
                for source in finding.sources:
                    lines.append(f"- {source}")
                lines.extend(["", "---", ""])

        # Failed queries
        failed = [q for q in log.queries if q.status == "failed"]
        if failed:
            lines.extend([
                "## Failed Queries",
                "",
                "*These queries require human review.*",
                ""
            ])

            for query in failed:
                lines.extend([
                    f"### Query {query.gap_id}: {query.question}",
                    "",
                    f"**Priority:** {query.priority}",
                    f"**Context:** {query.context}",
                    "",
                    "---",
                    ""
                ])

        return "\n".join(lines)


def main():
    """CLI interface for gap_researcher."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Research documentation gaps using Perplexity MCP"
    )
    parser.add_argument(
        'analysis_file',
        help='Path to analysis JSON file from doc_analyzer'
    )
    parser.add_argument(
        '--output',
        default='research_log.json',
        help='Output path for research log (default: research_log.json)'
    )
    parser.add_argument(
        '--format',
        choices=['json', 'markdown'],
        default='json',
        help='Output format (default: json)'
    )
    parser.add_argument(
        '--max-queries',
        type=int,
        help='Maximum number of queries to research (prioritized by impact)'
    )
    parser.add_argument(
        '--recency',
        choices=['day', 'week', 'month', 'year'],
        default='month',
        help='Perplexity recency filter (default: month)'
    )
    parser.add_argument(
        '--no-perplexity',
        action='store_true',
        help='Do not use Perplexity MCP (fallback mode)'
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

        # Extract gaps
        gaps = analysis.get('gaps', [])
        if not gaps:
            print("⚠️  No gaps found in analysis file", file=sys.stderr)
            return 0

        # Create researcher
        researcher = GapResearcher(
            use_perplexity_mcp=not args.no_perplexity,
            verbose=not args.quiet
        )

        # Generate queries
        tool_type = analysis.get('tool_type', 'unknown')
        context = f"Tool type: {tool_type}"

        queries = researcher.generate_queries_from_gaps(gaps, context)

        # Research
        log = researcher.research_all(
            queries,
            max_queries=args.max_queries,
            recency=args.recency
        )

        # Classify findings
        log = researcher.classify_findings(log)

        # Save
        researcher.save_research_log(log, args.output, format=args.format)

        # Print summary
        print(f"\n✅ Research complete!")
        print(f"   Queries: {log.metadata.get('total_queries', 0)}")
        print(f"   Completed: {log.metadata.get('completed', 0)}")
        print(f"   Failed: {log.metadata.get('failed', 0)}")
        print(f"   General findings: {len(log.get_general_findings())}")
        print(f"   Task-specific findings: {len(log.get_task_specific_findings())}")
        print(f"   Output: {args.output}")

        return 0

    except Exception as e:
        print(f"\n❌ Research failed: {e}", file=sys.stderr)
        if not args.quiet:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
