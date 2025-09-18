#!/usr/bin/env python3
"""
GraphQL Schema Analyzer

Analyzes GraphQL schemas for quality, complexity, and best practices compliance.
Provides detailed reports on types, fields, complexity scores, and recommendations.

Part of senior-graphql skill for engineering-team.

Usage:
    python schema_analyzer.py schema.graphql
    python schema_analyzer.py schema.graphql --output json
    python schema_analyzer.py schema.graphql --validate
    python schema_analyzer.py schema.graphql --complexity
    python schema_analyzer.py --help
    python schema_analyzer.py --version
"""

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Any


# Version
__version__ = "1.0.0"


@dataclass
class GraphQLField:
    """Represents a GraphQL field"""
    name: str
    type_name: str
    is_required: bool
    is_list: bool
    arguments: List[Dict[str, str]]
    description: Optional[str]
    is_deprecated: bool
    deprecation_reason: Optional[str]


@dataclass
class GraphQLType:
    """Represents a GraphQL type definition"""
    name: str
    kind: str  # type, interface, input, enum, union, scalar
    fields: List[GraphQLField]
    description: Optional[str]
    implements: List[str]
    directives: List[str]
    enum_values: List[str]  # For enum types
    union_types: List[str]  # For union types


@dataclass
class SchemaAnalysis:
    """Complete schema analysis results"""
    file_path: str
    types: List[GraphQLType]
    queries: List[GraphQLField]
    mutations: List[GraphQLField]
    subscriptions: List[GraphQLField]
    custom_scalars: List[str]
    directives: List[str]
    complexity_score: float
    issues: List[Dict[str, str]]
    recommendations: List[str]
    stats: Dict[str, int]


class GraphQLSchemaAnalyzer:
    """Analyzes GraphQL schema files for quality and best practices"""

    # Naming conventions
    TYPE_NAME_PATTERN = re.compile(r'^[A-Z][a-zA-Z0-9]*$')
    FIELD_NAME_PATTERN = re.compile(r'^[a-z][a-zA-Z0-9]*$')
    ENUM_VALUE_PATTERN = re.compile(r'^[A-Z][A-Z0-9_]*$')

    # Built-in types to ignore
    BUILTIN_TYPES = {'String', 'Int', 'Float', 'Boolean', 'ID'}
    BUILTIN_DIRECTIVES = {'deprecated', 'skip', 'include', 'specifiedBy'}

    # Complexity weights
    COMPLEXITY_WEIGHTS = {
        'type': 1,
        'interface': 2,
        'input': 1,
        'enum': 0.5,
        'union': 1.5,
        'scalar': 0.5,
        'field': 0.2,
        'argument': 0.1,
        'directive': 0.5,
    }

    def __init__(self, schema_path: str, verbose: bool = False):
        """
        Initialize analyzer with schema file path.

        Args:
            schema_path: Path to GraphQL schema file
            verbose: Enable verbose output
        """
        self.schema_path = Path(schema_path)
        self.verbose = verbose
        self.raw_schema = ""
        self.types: List[GraphQLType] = []
        self.queries: List[GraphQLField] = []
        self.mutations: List[GraphQLField] = []
        self.subscriptions: List[GraphQLField] = []
        self.custom_scalars: List[str] = []
        self.directives: List[str] = []
        self.issues: List[Dict[str, str]] = []
        self.recommendations: List[str] = []

    def analyze(self) -> SchemaAnalysis:
        """
        Analyze the GraphQL schema.

        Returns:
            SchemaAnalysis with complete results
        """
        if self.verbose:
            print(f"Analyzing schema: {self.schema_path}")

        # Load schema
        self._load_schema()

        # Parse types
        self._parse_types()

        # Parse operations
        self._parse_operations()

        # Parse scalars and directives
        self._parse_scalars()
        self._parse_directives()

        # Validate naming conventions
        self._validate_naming()

        # Check best practices
        self._check_best_practices()

        # Calculate complexity
        complexity = self._calculate_complexity()

        # Generate recommendations
        self._generate_recommendations()

        # Build stats
        stats = self._build_stats()

        return SchemaAnalysis(
            file_path=str(self.schema_path),
            types=self.types,
            queries=self.queries,
            mutations=self.mutations,
            subscriptions=self.subscriptions,
            custom_scalars=self.custom_scalars,
            directives=self.directives,
            complexity_score=complexity,
            issues=self.issues,
            recommendations=self.recommendations,
            stats=stats
        )

    def _load_schema(self) -> None:
        """Load and preprocess schema file"""
        if not self.schema_path.exists():
            raise FileNotFoundError(f"Schema file not found: {self.schema_path}")

        self.raw_schema = self.schema_path.read_text()

        # Remove comments for easier parsing
        self.clean_schema = re.sub(r'#.*$', '', self.raw_schema, flags=re.MULTILINE)
        # Remove string literals to avoid false positives
        self.clean_schema = re.sub(r'""".*?"""', '', self.clean_schema, flags=re.DOTALL)
        self.clean_schema = re.sub(r'"[^"]*"', '""', self.clean_schema)

    def _parse_types(self) -> None:
        """Parse type definitions from schema"""
        # Pattern for type definitions
        type_pattern = re.compile(
            r'(type|interface|input|enum|union)\s+(\w+)'
            r'(?:\s+implements\s+([^\{]+))?'
            r'(?:\s*@(\w+)(?:\([^)]*\))?)*'
            r'\s*\{([^}]*)\}',
            re.DOTALL
        )

        for match in type_pattern.finditer(self.clean_schema):
            kind = match.group(1)
            name = match.group(2)
            implements_str = match.group(3)
            body = match.group(5)

            # Skip Query, Mutation, Subscription as they're handled separately
            if name in {'Query', 'Mutation', 'Subscription'}:
                continue

            implements = []
            if implements_str:
                implements = [i.strip() for i in implements_str.split('&')]

            # Parse fields or enum values
            fields = []
            enum_values = []
            union_types = []

            if kind == 'enum':
                enum_values = self._parse_enum_values(body)
            elif kind == 'union':
                union_types = self._parse_union_types(body)
            else:
                fields = self._parse_fields(body)

            # Extract description from original schema
            description = self._extract_description(name)

            # Extract directives
            directives = re.findall(r'@(\w+)', match.group(0))

            gql_type = GraphQLType(
                name=name,
                kind=kind,
                fields=fields,
                description=description,
                implements=implements,
                directives=directives,
                enum_values=enum_values,
                union_types=union_types
            )
            self.types.append(gql_type)

    def _parse_fields(self, body: str) -> List[GraphQLField]:
        """Parse fields from type body"""
        fields = []

        # Field pattern: fieldName(args): Type! @directive
        field_pattern = re.compile(
            r'(\w+)\s*'
            r'(?:\(([^)]*)\))?\s*'
            r':\s*'
            r'(\[)?(\w+)(!)?(\])?(!)?\s*'
            r'(@deprecated(?:\([^)]*\))?)?'
        )

        for match in field_pattern.finditer(body):
            name = match.group(1)
            args_str = match.group(2)
            is_list = match.group(3) is not None
            type_name = match.group(4)
            inner_required = match.group(5) is not None
            list_end = match.group(6) is not None
            outer_required = match.group(7) is not None
            deprecated = match.group(8)

            # Parse arguments
            arguments = []
            if args_str:
                arguments = self._parse_arguments(args_str)

            # Determine if required
            is_required = outer_required if is_list else inner_required

            # Check deprecation
            is_deprecated = deprecated is not None
            deprecation_reason = None
            if deprecated:
                reason_match = re.search(r'reason:\s*"([^"]*)"', deprecated)
                if reason_match:
                    deprecation_reason = reason_match.group(1)

            field = GraphQLField(
                name=name,
                type_name=type_name,
                is_required=is_required,
                is_list=is_list,
                arguments=arguments,
                description=None,  # Would need full parsing for this
                is_deprecated=is_deprecated,
                deprecation_reason=deprecation_reason
            )
            fields.append(field)

        return fields

    def _parse_arguments(self, args_str: str) -> List[Dict[str, str]]:
        """Parse field arguments"""
        arguments = []
        # Simple argument pattern: argName: Type
        arg_pattern = re.compile(r'(\w+)\s*:\s*(\[)?(\w+)(!)?(\])?(!)?')

        for match in arg_pattern.finditer(args_str):
            arg = {
                'name': match.group(1),
                'type': match.group(3),
                'is_list': match.group(2) is not None,
                'is_required': match.group(4) is not None or match.group(6) is not None
            }
            arguments.append(arg)

        return arguments

    def _parse_enum_values(self, body: str) -> List[str]:
        """Parse enum values"""
        # Enum values are uppercase identifiers
        return re.findall(r'\b([A-Z][A-Z0-9_]*)\b', body)

    def _parse_union_types(self, body: str) -> List[str]:
        """Parse union member types"""
        # Union types after = sign
        union_match = re.search(r'=\s*([^}]+)', body)
        if union_match:
            types_str = union_match.group(1)
            return [t.strip() for t in types_str.split('|')]
        return []

    def _parse_operations(self) -> None:
        """Parse Query, Mutation, and Subscription types"""
        for op_type, target_list in [
            ('Query', self.queries),
            ('Mutation', self.mutations),
            ('Subscription', self.subscriptions)
        ]:
            pattern = re.compile(
                rf'type\s+{op_type}\s*\{{([^}}]*)\}}',
                re.DOTALL
            )
            match = pattern.search(self.clean_schema)
            if match:
                fields = self._parse_fields(match.group(1))
                target_list.extend(fields)

    def _parse_scalars(self) -> None:
        """Parse custom scalar definitions"""
        scalar_pattern = re.compile(r'scalar\s+(\w+)')
        scalars = scalar_pattern.findall(self.clean_schema)
        self.custom_scalars = [s for s in scalars if s not in self.BUILTIN_TYPES]

    def _parse_directives(self) -> None:
        """Parse custom directive definitions"""
        directive_pattern = re.compile(r'directive\s+@(\w+)')
        directives = directive_pattern.findall(self.clean_schema)
        self.directives = [d for d in directives if d not in self.BUILTIN_DIRECTIVES]

    def _extract_description(self, type_name: str) -> Optional[str]:
        """Extract description comment for a type"""
        # Look for """ description """ or # comment before type
        pattern = re.compile(
            rf'(?:"""([^"]*)"""\s*)?(?:#\s*([^\n]*)\n\s*)?'
            rf'(?:type|interface|input|enum|union)\s+{type_name}',
            re.DOTALL
        )
        match = pattern.search(self.raw_schema)
        if match:
            return (match.group(1) or match.group(2) or '').strip() or None
        return None

    def _validate_naming(self) -> None:
        """Validate naming conventions"""
        for gql_type in self.types:
            # Type names should be PascalCase
            if not self.TYPE_NAME_PATTERN.match(gql_type.name):
                self.issues.append({
                    'severity': 'warning',
                    'type': 'naming',
                    'message': f"Type '{gql_type.name}' should use PascalCase",
                    'location': gql_type.name
                })

            # Field names should be camelCase
            for field in gql_type.fields:
                if not self.FIELD_NAME_PATTERN.match(field.name):
                    self.issues.append({
                        'severity': 'warning',
                        'type': 'naming',
                        'message': f"Field '{field.name}' in type '{gql_type.name}' should use camelCase",
                        'location': f"{gql_type.name}.{field.name}"
                    })

            # Enum values should be SCREAMING_SNAKE_CASE
            for value in gql_type.enum_values:
                if not self.ENUM_VALUE_PATTERN.match(value):
                    self.issues.append({
                        'severity': 'warning',
                        'type': 'naming',
                        'message': f"Enum value '{value}' in '{gql_type.name}' should use SCREAMING_SNAKE_CASE",
                        'location': f"{gql_type.name}.{value}"
                    })

    def _check_best_practices(self) -> None:
        """Check for GraphQL best practices violations"""
        # Check for missing descriptions
        types_without_desc = [t.name for t in self.types if not t.description]
        if types_without_desc:
            self.issues.append({
                'severity': 'info',
                'type': 'documentation',
                'message': f"{len(types_without_desc)} types missing descriptions",
                'location': ', '.join(types_without_desc[:5]) + ('...' if len(types_without_desc) > 5 else '')
            })

        # Check for mutations not returning payload types
        for mutation in self.mutations:
            if not mutation.type_name.endswith('Payload') and mutation.type_name not in self.BUILTIN_TYPES:
                self.issues.append({
                    'severity': 'warning',
                    'type': 'best_practice',
                    'message': f"Mutation '{mutation.name}' should return a Payload type, not '{mutation.type_name}'",
                    'location': f"Mutation.{mutation.name}"
                })

        # Check for lists without pagination
        for gql_type in self.types:
            for field in gql_type.fields:
                if field.is_list and not any(arg['name'] in ['first', 'last', 'limit', 'offset', 'after', 'before']
                                              for arg in field.arguments):
                    # Only warn for non-connection types
                    if not field.type_name.endswith('Connection') and not field.type_name.endswith('Edge'):
                        self.issues.append({
                            'severity': 'info',
                            'type': 'best_practice',
                            'message': f"List field '{field.name}' in '{gql_type.name}' may need pagination arguments",
                            'location': f"{gql_type.name}.{field.name}"
                        })

        # Check for deprecated fields without reason
        for gql_type in self.types:
            for field in gql_type.fields:
                if field.is_deprecated and not field.deprecation_reason:
                    self.issues.append({
                        'severity': 'warning',
                        'type': 'documentation',
                        'message': f"Deprecated field '{field.name}' in '{gql_type.name}' should have a deprecation reason",
                        'location': f"{gql_type.name}.{field.name}"
                    })

        # Check for Input types not following naming convention
        for gql_type in self.types:
            if gql_type.kind == 'input' and not gql_type.name.endswith('Input'):
                self.issues.append({
                    'severity': 'info',
                    'type': 'naming',
                    'message': f"Input type '{gql_type.name}' should end with 'Input' suffix",
                    'location': gql_type.name
                })

    def _calculate_complexity(self) -> float:
        """Calculate overall schema complexity score"""
        complexity = 0.0

        # Types
        for gql_type in self.types:
            complexity += self.COMPLEXITY_WEIGHTS.get(gql_type.kind, 1)
            complexity += len(gql_type.fields) * self.COMPLEXITY_WEIGHTS['field']
            for field in gql_type.fields:
                complexity += len(field.arguments) * self.COMPLEXITY_WEIGHTS['argument']

        # Operations
        complexity += len(self.queries) * self.COMPLEXITY_WEIGHTS['field']
        complexity += len(self.mutations) * self.COMPLEXITY_WEIGHTS['field'] * 1.5
        complexity += len(self.subscriptions) * self.COMPLEXITY_WEIGHTS['field'] * 2

        # Scalars and directives
        complexity += len(self.custom_scalars) * self.COMPLEXITY_WEIGHTS['scalar']
        complexity += len(self.directives) * self.COMPLEXITY_WEIGHTS['directive']

        return round(complexity, 2)

    def _generate_recommendations(self) -> None:
        """Generate actionable recommendations"""
        # Group issues by type
        issue_counts = {}
        for issue in self.issues:
            issue_type = issue['type']
            issue_counts[issue_type] = issue_counts.get(issue_type, 0) + 1

        if issue_counts.get('naming', 0) > 3:
            self.recommendations.append(
                "Review naming conventions: Use PascalCase for types, camelCase for fields, "
                "SCREAMING_SNAKE_CASE for enum values"
            )

        if issue_counts.get('documentation', 0) > 0:
            self.recommendations.append(
                "Add descriptions to types and fields for better API documentation"
            )

        if issue_counts.get('best_practice', 0) > 0:
            self.recommendations.append(
                "Follow GraphQL best practices: Payload types for mutations, "
                "pagination for list fields, Input suffix for input types"
            )

        # Check for missing common patterns
        type_names = {t.name for t in self.types}
        if not any('Connection' in name for name in type_names):
            self.recommendations.append(
                "Consider implementing Relay-style pagination with Connection/Edge types for scalability"
            )

        if len(self.subscriptions) == 0:
            self.recommendations.append(
                "Consider adding subscriptions for real-time features if your app needs live updates"
            )

        if len(self.custom_scalars) == 0:
            self.recommendations.append(
                "Consider custom scalars like DateTime, URL, Email for better type safety"
            )

    def _build_stats(self) -> Dict[str, int]:
        """Build statistics summary"""
        return {
            'total_types': len(self.types),
            'object_types': len([t for t in self.types if t.kind == 'type']),
            'interfaces': len([t for t in self.types if t.kind == 'interface']),
            'input_types': len([t for t in self.types if t.kind == 'input']),
            'enums': len([t for t in self.types if t.kind == 'enum']),
            'unions': len([t for t in self.types if t.kind == 'union']),
            'queries': len(self.queries),
            'mutations': len(self.mutations),
            'subscriptions': len(self.subscriptions),
            'custom_scalars': len(self.custom_scalars),
            'custom_directives': len(self.directives),
            'total_fields': sum(len(t.fields) for t in self.types),
            'deprecated_fields': sum(
                len([f for f in t.fields if f.is_deprecated])
                for t in self.types
            ),
            'issues_count': len(self.issues),
            'critical_issues': len([i for i in self.issues if i['severity'] == 'error']),
            'warnings': len([i for i in self.issues if i['severity'] == 'warning']),
        }


def format_text_output(analysis: SchemaAnalysis) -> str:
    """Format analysis as human-readable text"""
    lines = []
    lines.append("=" * 60)
    lines.append("GRAPHQL SCHEMA ANALYSIS")
    lines.append("=" * 60)
    lines.append(f"File: {analysis.file_path}")
    lines.append(f"Analyzed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    # Stats
    lines.append("STATISTICS")
    lines.append("-" * 40)
    stats = analysis.stats
    lines.append(f"  Total Types:      {stats['total_types']}")
    lines.append(f"    - Object Types: {stats['object_types']}")
    lines.append(f"    - Interfaces:   {stats['interfaces']}")
    lines.append(f"    - Input Types:  {stats['input_types']}")
    lines.append(f"    - Enums:        {stats['enums']}")
    lines.append(f"    - Unions:       {stats['unions']}")
    lines.append(f"  Queries:          {stats['queries']}")
    lines.append(f"  Mutations:        {stats['mutations']}")
    lines.append(f"  Subscriptions:    {stats['subscriptions']}")
    lines.append(f"  Custom Scalars:   {stats['custom_scalars']}")
    lines.append(f"  Custom Directives:{stats['custom_directives']}")
    lines.append(f"  Total Fields:     {stats['total_fields']}")
    lines.append(f"  Deprecated Fields:{stats['deprecated_fields']}")
    lines.append("")

    # Complexity
    lines.append("COMPLEXITY SCORE")
    lines.append("-" * 40)
    complexity = analysis.complexity_score
    if complexity < 20:
        level = "LOW"
    elif complexity < 50:
        level = "MODERATE"
    elif complexity < 100:
        level = "HIGH"
    else:
        level = "VERY HIGH"
    lines.append(f"  Score: {complexity} ({level})")
    lines.append("")

    # Operations summary
    lines.append("OPERATIONS")
    lines.append("-" * 40)
    if analysis.queries:
        lines.append(f"  Queries ({len(analysis.queries)}):")
        for q in analysis.queries[:10]:
            lines.append(f"    - {q.name}: {q.type_name}{'!' if q.is_required else ''}")
        if len(analysis.queries) > 10:
            lines.append(f"    ... and {len(analysis.queries) - 10} more")
    if analysis.mutations:
        lines.append(f"  Mutations ({len(analysis.mutations)}):")
        for m in analysis.mutations[:10]:
            lines.append(f"    - {m.name}: {m.type_name}")
        if len(analysis.mutations) > 10:
            lines.append(f"    ... and {len(analysis.mutations) - 10} more")
    if analysis.subscriptions:
        lines.append(f"  Subscriptions ({len(analysis.subscriptions)}):")
        for s in analysis.subscriptions:
            lines.append(f"    - {s.name}: {s.type_name}")
    lines.append("")

    # Issues
    if analysis.issues:
        lines.append("ISSUES")
        lines.append("-" * 40)
        for issue in analysis.issues[:20]:
            icon = "!" if issue['severity'] == 'error' else "?" if issue['severity'] == 'warning' else "i"
            lines.append(f"  [{icon}] {issue['message']}")
            lines.append(f"      Location: {issue['location']}")
        if len(analysis.issues) > 20:
            lines.append(f"  ... and {len(analysis.issues) - 20} more issues")
        lines.append("")

    # Recommendations
    if analysis.recommendations:
        lines.append("RECOMMENDATIONS")
        lines.append("-" * 40)
        for i, rec in enumerate(analysis.recommendations, 1):
            lines.append(f"  {i}. {rec}")
        lines.append("")

    lines.append("=" * 60)

    return "\n".join(lines)


def format_json_output(analysis: SchemaAnalysis) -> str:
    """Format analysis as JSON"""
    def serialize_field(f: GraphQLField) -> dict:
        return {
            'name': f.name,
            'type': f.type_name,
            'isRequired': f.is_required,
            'isList': f.is_list,
            'arguments': f.arguments,
            'isDeprecated': f.is_deprecated,
            'deprecationReason': f.deprecation_reason
        }

    def serialize_type(t: GraphQLType) -> dict:
        return {
            'name': t.name,
            'kind': t.kind,
            'description': t.description,
            'implements': t.implements,
            'directives': t.directives,
            'fields': [serialize_field(f) for f in t.fields],
            'enumValues': t.enum_values,
            'unionTypes': t.union_types
        }

    output = {
        'file': analysis.file_path,
        'analyzedAt': datetime.now().isoformat(),
        'stats': analysis.stats,
        'complexityScore': analysis.complexity_score,
        'types': [serialize_type(t) for t in analysis.types],
        'queries': [serialize_field(q) for q in analysis.queries],
        'mutations': [serialize_field(m) for m in analysis.mutations],
        'subscriptions': [serialize_field(s) for s in analysis.subscriptions],
        'customScalars': analysis.custom_scalars,
        'customDirectives': analysis.directives,
        'issues': analysis.issues,
        'recommendations': analysis.recommendations
    }

    return json.dumps(output, indent=2)


def main():
    """Main entry point with CLI interface"""
    parser = argparse.ArgumentParser(
        description="GraphQL Schema Analyzer - Analyze schemas for quality and best practices",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s schema.graphql
  %(prog)s schema.graphql --output json
  %(prog)s schema.graphql --validate
  %(prog)s schema.graphql --complexity

Part of senior-graphql skill for engineering-team.
"""
    )

    parser.add_argument(
        'schema',
        nargs='?',
        help='Path to GraphQL schema file (.graphql or .gql)'
    )

    parser.add_argument(
        '-o', '--output',
        choices=['text', 'json'],
        default='text',
        help='Output format (default: text)'
    )

    parser.add_argument(
        '--validate',
        action='store_true',
        help='Validate schema and return exit code based on issues'
    )

    parser.add_argument(
        '--complexity',
        action='store_true',
        help='Show only complexity analysis'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )

    parser.add_argument(
        '--version',
        action='version',
        version=f'%(prog)s {__version__}'
    )

    args = parser.parse_args()

    # Require schema file unless showing version
    if not args.schema:
        parser.print_help()
        sys.exit(1)

    # Run analysis
    try:
        analyzer = GraphQLSchemaAnalyzer(args.schema, verbose=args.verbose)
        analysis = analyzer.analyze()

        # Format and output
        if args.complexity:
            # Show only complexity
            print(f"Schema Complexity Score: {analysis.complexity_score}")
            if analysis.complexity_score < 20:
                print("Level: LOW - Simple schema, easy to maintain")
            elif analysis.complexity_score < 50:
                print("Level: MODERATE - Average complexity")
            elif analysis.complexity_score < 100:
                print("Level: HIGH - Complex schema, consider splitting")
            else:
                print("Level: VERY HIGH - Consider federation or schema restructuring")
        elif args.output == 'json':
            print(format_json_output(analysis))
        else:
            print(format_text_output(analysis))

        # Exit code for validation
        if args.validate:
            critical_count = len([i for i in analysis.issues if i['severity'] == 'error'])
            if critical_count > 0:
                sys.exit(1)

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error analyzing schema: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
