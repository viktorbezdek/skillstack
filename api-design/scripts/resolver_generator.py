#!/usr/bin/env python3
"""
GraphQL Resolver Generator

Generates TypeScript resolvers from GraphQL schema definitions.
Includes DataLoader integration, type definitions, and test stubs.

Part of senior-graphql skill for engineering-team.

Usage:
    python resolver_generator.py schema.graphql --output src/resolvers
    python resolver_generator.py schema.graphql --output src/resolvers --dataloader
    python resolver_generator.py schema.graphql --output src/resolvers --types User,Post
    python resolver_generator.py schema.graphql --output src/resolvers --tests
    python resolver_generator.py --help
    python resolver_generator.py --version
"""

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


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
    is_relation: bool = False


@dataclass
class GraphQLType:
    """Represents a GraphQL type"""
    name: str
    kind: str
    fields: List[GraphQLField]
    implements: List[str]


class ResolverGenerator:
    """Generates TypeScript resolvers from GraphQL schema"""

    # Built-in scalar types
    SCALAR_TYPES = {'String', 'Int', 'Float', 'Boolean', 'ID'}

    # Type mappings for TypeScript
    TS_TYPE_MAP = {
        'String': 'string',
        'Int': 'number',
        'Float': 'number',
        'Boolean': 'boolean',
        'ID': 'string',
        'DateTime': 'Date',
        'JSON': 'Record<string, unknown>',
    }

    def __init__(self, schema_path: str, output_dir: str, verbose: bool = False):
        """
        Initialize generator.

        Args:
            schema_path: Path to GraphQL schema file
            output_dir: Output directory for generated files
            verbose: Enable verbose output
        """
        self.schema_path = Path(schema_path)
        self.output_dir = Path(output_dir)
        self.verbose = verbose
        self.types: List[GraphQLType] = []
        self.queries: List[GraphQLField] = []
        self.mutations: List[GraphQLField] = []
        self.subscriptions: List[GraphQLField] = []
        self.custom_scalars: Set[str] = set()
        self.type_names: Set[str] = set()

    def generate(self, include_dataloader: bool = False,
                 include_tests: bool = False,
                 filter_types: Optional[List[str]] = None,
                 dry_run: bool = False) -> Dict[str, str]:
        """
        Generate resolver files.

        Args:
            include_dataloader: Include DataLoader factories
            include_tests: Generate test files
            filter_types: Only generate for specific types
            dry_run: Preview without writing files

        Returns:
            Dict mapping file paths to contents
        """
        if self.verbose:
            print(f"Reading schema: {self.schema_path}")

        # Load and parse schema
        self._parse_schema()

        # Filter types if specified
        if filter_types:
            self.types = [t for t in self.types if t.name in filter_types]
            if self.verbose:
                print(f"Filtered to {len(self.types)} types: {', '.join(t.name for t in self.types)}")

        # Generate files
        files: Dict[str, str] = {}

        # Generate type resolvers
        for gql_type in self.types:
            if gql_type.kind in ['type', 'interface']:
                filename = f"{self._to_kebab_case(gql_type.name)}.resolver.ts"
                content = self._generate_type_resolver(gql_type, include_dataloader)
                files[filename] = content

                if include_tests:
                    test_filename = f"{self._to_kebab_case(gql_type.name)}.resolver.test.ts"
                    test_content = self._generate_resolver_test(gql_type)
                    files[test_filename] = test_content

        # Generate query resolver
        if self.queries:
            files['query.resolver.ts'] = self._generate_query_resolver()
            if include_tests:
                files['query.resolver.test.ts'] = self._generate_query_test()

        # Generate mutation resolver
        if self.mutations:
            files['mutation.resolver.ts'] = self._generate_mutation_resolver()
            if include_tests:
                files['mutation.resolver.test.ts'] = self._generate_mutation_test()

        # Generate subscription resolver
        if self.subscriptions:
            files['subscription.resolver.ts'] = self._generate_subscription_resolver()

        # Generate index file
        files['index.ts'] = self._generate_index_file(files.keys())

        # Generate types file
        files['types.ts'] = self._generate_types_file()

        # Generate context file
        files['context.ts'] = self._generate_context_file(include_dataloader)

        # Generate DataLoader factories
        if include_dataloader:
            files['dataloaders.ts'] = self._generate_dataloaders()

        # Write files
        if not dry_run:
            self._write_files(files)
        else:
            print("\n[DRY RUN] Would generate the following files:")
            for filename in sorted(files.keys()):
                print(f"  {self.output_dir / filename}")

        return files

    def _parse_schema(self) -> None:
        """Parse GraphQL schema file"""
        if not self.schema_path.exists():
            raise FileNotFoundError(f"Schema file not found: {self.schema_path}")

        schema = self.schema_path.read_text()

        # Remove comments
        clean_schema = re.sub(r'#.*$', '', schema, flags=re.MULTILINE)
        clean_schema = re.sub(r'""".*?"""', '', clean_schema, flags=re.DOTALL)

        # Parse custom scalars
        scalar_pattern = re.compile(r'scalar\s+(\w+)')
        for match in scalar_pattern.finditer(clean_schema):
            scalar_name = match.group(1)
            if scalar_name not in self.SCALAR_TYPES:
                self.custom_scalars.add(scalar_name)

        # Parse type definitions
        type_pattern = re.compile(
            r'(type|interface|input)\s+(\w+)'
            r'(?:\s+implements\s+([^\{]+))?'
            r'\s*\{([^}]*)\}',
            re.DOTALL
        )

        for match in type_pattern.finditer(clean_schema):
            kind = match.group(1)
            name = match.group(2)
            implements_str = match.group(3)
            body = match.group(4)

            self.type_names.add(name)

            implements = []
            if implements_str:
                implements = [i.strip() for i in implements_str.split('&')]

            fields = self._parse_fields(body)

            if name == 'Query':
                self.queries = fields
            elif name == 'Mutation':
                self.mutations = fields
            elif name == 'Subscription':
                self.subscriptions = fields
            else:
                gql_type = GraphQLType(
                    name=name,
                    kind=kind,
                    fields=fields,
                    implements=implements
                )
                self.types.append(gql_type)

    def _parse_fields(self, body: str) -> List[GraphQLField]:
        """Parse fields from type body"""
        fields = []

        field_pattern = re.compile(
            r'(\w+)\s*'
            r'(?:\(([^)]*)\))?\s*'
            r':\s*'
            r'(\[)?(\w+)(!)?(\])?(!)?\s*'
        )

        for match in field_pattern.finditer(body):
            name = match.group(1)
            args_str = match.group(2)
            is_list = match.group(3) is not None
            type_name = match.group(4)
            inner_required = match.group(5) is not None
            outer_required = match.group(7) is not None

            arguments = []
            if args_str:
                arguments = self._parse_arguments(args_str)

            is_required = outer_required if is_list else inner_required

            # Determine if this is a relation field
            is_relation = type_name not in self.SCALAR_TYPES and type_name not in self.custom_scalars

            field = GraphQLField(
                name=name,
                type_name=type_name,
                is_required=is_required,
                is_list=is_list,
                arguments=arguments,
                is_relation=is_relation
            )
            fields.append(field)

        return fields

    def _parse_arguments(self, args_str: str) -> List[Dict[str, str]]:
        """Parse field arguments"""
        arguments = []
        arg_pattern = re.compile(r'(\w+)\s*:\s*(\[)?(\w+)(!)?(\])?(!)?\s*(?:=\s*([^,\)]+))?')

        for match in arg_pattern.finditer(args_str):
            arg = {
                'name': match.group(1),
                'type': match.group(3),
                'is_list': match.group(2) is not None,
                'is_required': match.group(4) is not None or match.group(6) is not None,
                'default': match.group(7).strip() if match.group(7) else None
            }
            arguments.append(arg)

        return arguments

    def _generate_type_resolver(self, gql_type: GraphQLType, include_dataloader: bool) -> str:
        """Generate resolver for a type"""
        lines = []

        # Imports
        lines.append("// Auto-generated by resolver_generator.py")
        lines.append(f"// Type: {gql_type.name}")
        lines.append("")
        lines.append("import { Context } from './context';")
        if include_dataloader:
            lines.append("import { Loaders } from './dataloaders';")
        lines.append("")

        # Parent type
        parent_type = self._get_ts_type(gql_type.name, False, False)
        lines.append(f"// Parent type for {gql_type.name} resolvers")
        lines.append(f"type Parent = {{")
        for field in gql_type.fields:
            if not field.is_relation:
                ts_type = self._get_ts_type(field.type_name, field.is_list, field.is_required)
                lines.append(f"  {field.name}: {ts_type};")
            else:
                # For relations, only include the foreign key
                lines.append(f"  {field.name}Id?: string;")
        lines.append("};")
        lines.append("")

        # Resolvers
        lines.append(f"export const {gql_type.name}Resolvers = {{")
        lines.append(f"  {gql_type.name}: {{")

        for field in gql_type.fields:
            if field.is_relation:
                # Relation field needs resolver
                args_type = self._get_args_type(field.arguments)
                return_type = self._get_ts_type(field.type_name, field.is_list, field.is_required)

                lines.append(f"    {field.name}: async (")
                lines.append(f"      parent: Parent,")
                if field.arguments:
                    lines.append(f"      args: {args_type},")
                else:
                    lines.append(f"      _args: Record<string, never>,")
                lines.append(f"      {{ loaders, prisma }}: Context")
                lines.append(f"    ): Promise<{return_type}> => {{")

                if include_dataloader:
                    if field.is_list:
                        lines.append(f"      // Use DataLoader for batch loading")
                        lines.append(f"      return loaders.{self._to_camel_case(field.type_name)}By{gql_type.name}Loader.load(parent.id);")
                    else:
                        lines.append(f"      // Use DataLoader for batch loading")
                        lines.append(f"      if (!parent.{field.name}Id) return null;")
                        lines.append(f"      return loaders.{self._to_camel_case(field.type_name)}Loader.load(parent.{field.name}Id);")
                else:
                    if field.is_list:
                        lines.append(f"      // TODO: Implement with DataLoader to prevent N+1")
                        lines.append(f"      return prisma.{self._to_camel_case(field.type_name)}.findMany({{")
                        lines.append(f"        where: {{ {self._to_camel_case(gql_type.name)}Id: parent.id }}")
                        lines.append(f"      }});")
                    else:
                        lines.append(f"      if (!parent.{field.name}Id) return null;")
                        lines.append(f"      return prisma.{self._to_camel_case(field.type_name)}.findUnique({{")
                        lines.append(f"        where: {{ id: parent.{field.name}Id }}")
                        lines.append(f"      }});")

                lines.append("    },")
                lines.append("")

        lines.append("  },")
        lines.append("};")

        return "\n".join(lines)

    def _generate_query_resolver(self) -> str:
        """Generate Query resolver"""
        lines = []
        lines.append("// Auto-generated by resolver_generator.py")
        lines.append("// Query Resolvers")
        lines.append("")
        lines.append("import { Context } from './context';")
        lines.append("")

        lines.append("export const QueryResolvers = {")
        lines.append("  Query: {")

        for query in self.queries:
            args_type = self._get_args_type(query.arguments)
            return_type = self._get_ts_type(query.type_name, query.is_list, query.is_required)

            lines.append(f"    {query.name}: async (")
            lines.append(f"      _parent: undefined,")
            if query.arguments:
                lines.append(f"      args: {args_type},")
            else:
                lines.append(f"      _args: Record<string, never>,")
            lines.append(f"      {{ prisma, user }}: Context")
            lines.append(f"    ): Promise<{return_type}> => {{")

            # Generate implementation based on common patterns
            if query.name == 'me':
                lines.append("      if (!user) throw new Error('Not authenticated');")
                lines.append("      return prisma.user.findUnique({ where: { id: user.id } });")
            elif query.is_list:
                model_name = self._to_camel_case(query.type_name.replace('Connection', ''))
                lines.append(f"      // TODO: Implement pagination if needed")
                if any(arg['name'] in ['first', 'last', 'after', 'before'] for arg in query.arguments):
                    lines.append(f"      const {{ first, after }} = args;")
                    lines.append(f"      return prisma.{model_name}.findMany({{")
                    lines.append(f"        take: first ?? 10,")
                    lines.append(f"        cursor: after ? {{ id: after }} : undefined,")
                    lines.append(f"        skip: after ? 1 : 0,")
                    lines.append(f"      }});")
                else:
                    lines.append(f"      return prisma.{model_name}.findMany();")
            else:
                model_name = self._to_camel_case(query.type_name)
                if any(arg['name'] == 'id' for arg in query.arguments):
                    lines.append(f"      return prisma.{model_name}.findUnique({{")
                    lines.append(f"        where: {{ id: args.id }}")
                    lines.append(f"      }});")
                else:
                    lines.append(f"      // TODO: Implement query logic")
                    lines.append(f"      throw new Error('Not implemented');")

            lines.append("    },")
            lines.append("")

        lines.append("  },")
        lines.append("};")

        return "\n".join(lines)

    def _generate_mutation_resolver(self) -> str:
        """Generate Mutation resolver"""
        lines = []
        lines.append("// Auto-generated by resolver_generator.py")
        lines.append("// Mutation Resolvers")
        lines.append("")
        lines.append("import { Context } from './context';")
        lines.append("import { pubsub, EVENTS } from '../pubsub';")
        lines.append("")

        lines.append("export const MutationResolvers = {")
        lines.append("  Mutation: {")

        for mutation in self.mutations:
            args_type = self._get_args_type(mutation.arguments)
            return_type = self._get_ts_type(mutation.type_name, mutation.is_list, mutation.is_required)

            lines.append(f"    {mutation.name}: async (")
            lines.append(f"      _parent: undefined,")
            if mutation.arguments:
                lines.append(f"      args: {args_type},")
            else:
                lines.append(f"      _args: Record<string, never>,")
            lines.append(f"      {{ prisma, user }}: Context")
            lines.append(f"    ): Promise<{return_type}> => {{")

            # Common mutation patterns
            if mutation.name.startswith('create'):
                entity = mutation.name[6:]  # Remove 'create' prefix
                model_name = self._to_camel_case(entity)
                lines.append("      if (!user) throw new Error('Not authenticated');")
                lines.append("")
                lines.append(f"      const {model_name} = await prisma.{model_name}.create({{")
                lines.append(f"        data: {{")
                lines.append(f"          ...args.input,")
                lines.append(f"          authorId: user.id, // Adjust based on your schema")
                lines.append(f"        }}")
                lines.append(f"      }});")
                lines.append("")
                lines.append(f"      // Publish event for subscriptions")
                lines.append(f"      await pubsub.publish(EVENTS.{entity.upper()}_CREATED, {{ {model_name}Created: {model_name} }});")
                lines.append("")
                lines.append(f"      return {{ {model_name} }};")
            elif mutation.name.startswith('update'):
                entity = mutation.name[6:]
                model_name = self._to_camel_case(entity)
                lines.append("      if (!user) throw new Error('Not authenticated');")
                lines.append("")
                lines.append(f"      const {model_name} = await prisma.{model_name}.update({{")
                lines.append(f"        where: {{ id: args.id }},")
                lines.append(f"        data: args.input")
                lines.append(f"      }});")
                lines.append("")
                lines.append(f"      return {{ {model_name} }};")
            elif mutation.name.startswith('delete'):
                entity = mutation.name[6:]
                model_name = self._to_camel_case(entity)
                lines.append("      if (!user) throw new Error('Not authenticated');")
                lines.append("")
                lines.append(f"      const {model_name} = await prisma.{model_name}.delete({{")
                lines.append(f"        where: {{ id: args.id }}")
                lines.append(f"      }});")
                lines.append("")
                lines.append(f"      return {{ {model_name}, success: true }};")
            else:
                lines.append("      // TODO: Implement mutation logic")
                lines.append("      throw new Error('Not implemented');")

            lines.append("    },")
            lines.append("")

        lines.append("  },")
        lines.append("};")

        return "\n".join(lines)

    def _generate_subscription_resolver(self) -> str:
        """Generate Subscription resolver"""
        lines = []
        lines.append("// Auto-generated by resolver_generator.py")
        lines.append("// Subscription Resolvers")
        lines.append("")
        lines.append("import { withFilter } from 'graphql-subscriptions';")
        lines.append("import { pubsub, EVENTS } from '../pubsub';")
        lines.append("import { Context } from './context';")
        lines.append("")

        lines.append("export const SubscriptionResolvers = {")
        lines.append("  Subscription: {")

        for sub in self.subscriptions:
            event_name = self._to_screaming_snake(sub.name)

            if sub.arguments:
                # Subscription with filter
                lines.append(f"    {sub.name}: {{")
                lines.append(f"      subscribe: withFilter(")
                lines.append(f"        () => pubsub.asyncIterator([EVENTS.{event_name}]),")
                lines.append(f"        (payload, variables) => {{")
                # Generate filter logic based on arguments
                for arg in sub.arguments:
                    lines.append(f"          // Filter by {arg['name']}")
                    lines.append(f"          if (variables.{arg['name']}) {{")
                    lines.append(f"            return payload.{sub.name}.{arg['name']} === variables.{arg['name']};")
                    lines.append(f"          }}")
                lines.append(f"          return true;")
                lines.append(f"        }}")
                lines.append(f"      ),")
                lines.append(f"    }},")
            else:
                # Simple subscription
                lines.append(f"    {sub.name}: {{")
                lines.append(f"      subscribe: () => pubsub.asyncIterator([EVENTS.{event_name}]),")
                lines.append(f"    }},")
            lines.append("")

        lines.append("  },")
        lines.append("};")

        return "\n".join(lines)

    def _generate_index_file(self, filenames) -> str:
        """Generate index.ts that exports all resolvers"""
        lines = []
        lines.append("// Auto-generated by resolver_generator.py")
        lines.append("// Re-exports all resolvers")
        lines.append("")

        resolver_files = [f for f in filenames if f.endswith('.resolver.ts') and not f.endswith('.test.ts')]

        imports = []
        exports = []

        for filename in sorted(resolver_files):
            module_name = filename.replace('.resolver.ts', '')
            resolver_name = f"{self._to_pascal_case(module_name)}Resolvers"
            imports.append(f"import {{ {resolver_name} }} from './{module_name}.resolver';")
            exports.append(resolver_name)

        lines.extend(imports)
        lines.append("")
        lines.append("export const resolvers = {")
        for export in exports:
            lines.append(f"  ...{export},")
        lines.append("};")
        lines.append("")
        lines.append("export * from './types';")
        lines.append("export * from './context';")

        return "\n".join(lines)

    def _generate_types_file(self) -> str:
        """Generate TypeScript type definitions"""
        lines = []
        lines.append("// Auto-generated by resolver_generator.py")
        lines.append("// TypeScript type definitions")
        lines.append("")

        # Generate type for each GraphQL type
        for gql_type in self.types:
            if gql_type.kind == 'input':
                lines.append(f"export interface {gql_type.name} {{")
            else:
                lines.append(f"export interface {gql_type.name} {{")

            for field in gql_type.fields:
                ts_type = self._get_ts_type(field.type_name, field.is_list, field.is_required)
                optional = '' if field.is_required else '?'
                lines.append(f"  {field.name}{optional}: {ts_type};")

            lines.append("}")
            lines.append("")

        # Generate Payload types for mutations
        for mutation in self.mutations:
            if mutation.type_name.endswith('Payload'):
                lines.append(f"export interface {mutation.type_name} {{")
                entity_name = mutation.type_name.replace('Payload', '').replace('Create', '').replace('Update', '').replace('Delete', '')
                lines.append(f"  {self._to_camel_case(entity_name)}?: {entity_name};")
                lines.append("  success?: boolean;")
                lines.append("  errors?: string[];")
                lines.append("}")
                lines.append("")

        return "\n".join(lines)

    def _generate_context_file(self, include_dataloader: bool) -> str:
        """Generate context type definition"""
        lines = []
        lines.append("// Auto-generated by resolver_generator.py")
        lines.append("// GraphQL Context type")
        lines.append("")
        lines.append("import { PrismaClient } from '@prisma/client';")
        if include_dataloader:
            lines.append("import { Loaders, createLoaders } from './dataloaders';")
        lines.append("")

        lines.append("export interface User {")
        lines.append("  id: string;")
        lines.append("  email: string;")
        lines.append("  name?: string;")
        lines.append("}")
        lines.append("")

        lines.append("export interface Context {")
        lines.append("  prisma: PrismaClient;")
        lines.append("  user: User | null;")
        if include_dataloader:
            lines.append("  loaders: Loaders;")
        lines.append("}")
        lines.append("")

        lines.append("// Context factory")
        lines.append("export const createContext = (prisma: PrismaClient, user: User | null): Context => ({")
        lines.append("  prisma,")
        lines.append("  user,")
        if include_dataloader:
            lines.append("  loaders: createLoaders(prisma),")
        lines.append("});")

        return "\n".join(lines)

    def _generate_dataloaders(self) -> str:
        """Generate DataLoader factories"""
        lines = []
        lines.append("// Auto-generated by resolver_generator.py")
        lines.append("// DataLoader factories for batch loading")
        lines.append("")
        lines.append("import DataLoader from 'dataloader';")
        lines.append("import { PrismaClient } from '@prisma/client';")
        lines.append("")

        # Import types
        type_names = [t.name for t in self.types if t.kind == 'type']
        if type_names:
            lines.append(f"import {{ {', '.join(type_names)} }} from './types';")
            lines.append("")

        lines.append("export const createLoaders = (prisma: PrismaClient) => ({")

        for gql_type in self.types:
            if gql_type.kind != 'type':
                continue

            model_name = self._to_camel_case(gql_type.name)

            # Single entity loader
            lines.append(f"  // Load {gql_type.name} by ID")
            lines.append(f"  {model_name}Loader: new DataLoader<string, {gql_type.name} | null>(")
            lines.append(f"    async (ids) => {{")
            lines.append(f"      const items = await prisma.{model_name}.findMany({{")
            lines.append(f"        where: {{ id: {{ in: [...ids] }} }}")
            lines.append(f"      }});")
            lines.append(f"      const itemMap = new Map(items.map(item => [item.id, item]));")
            lines.append(f"      return ids.map(id => itemMap.get(id) ?? null);")
            lines.append(f"    }}")
            lines.append(f"  ),")
            lines.append("")

            # Related entities loaders
            for field in gql_type.fields:
                if field.is_relation and field.is_list:
                    related_type = field.type_name
                    related_model = self._to_camel_case(related_type)
                    lines.append(f"  // Load {related_type}s by {gql_type.name} ID")
                    lines.append(f"  {related_model}By{gql_type.name}Loader: new DataLoader<string, {related_type}[]>(")
                    lines.append(f"    async (parentIds) => {{")
                    lines.append(f"      const items = await prisma.{related_model}.findMany({{")
                    lines.append(f"        where: {{ {model_name}Id: {{ in: [...parentIds] }} }}")
                    lines.append(f"      }});")
                    lines.append(f"      const grouped = new Map<string, {related_type}[]>();")
                    lines.append(f"      items.forEach(item => {{")
                    lines.append(f"        const key = item.{model_name}Id;")
                    lines.append(f"        const existing = grouped.get(key) ?? [];")
                    lines.append(f"        existing.push(item);")
                    lines.append(f"        grouped.set(key, existing);")
                    lines.append(f"      }});")
                    lines.append(f"      return parentIds.map(id => grouped.get(id) ?? []);")
                    lines.append(f"    }}")
                    lines.append(f"  ),")
                    lines.append("")

        lines.append("});")
        lines.append("")
        lines.append("export type Loaders = ReturnType<typeof createLoaders>;")

        return "\n".join(lines)

    def _generate_resolver_test(self, gql_type: GraphQLType) -> str:
        """Generate test file for type resolver"""
        lines = []
        lines.append("// Auto-generated by resolver_generator.py")
        lines.append(f"// Tests for {gql_type.name} resolvers")
        lines.append("")
        lines.append(f"import {{ {gql_type.name}Resolvers }} from './{self._to_kebab_case(gql_type.name)}.resolver';")
        lines.append("")

        lines.append(f"describe('{gql_type.name}Resolvers', () => {{")

        for field in gql_type.fields:
            if field.is_relation:
                lines.append(f"  describe('{field.name}', () => {{")
                lines.append(f"    it('should resolve {field.name}', async () => {{")
                lines.append(f"      // TODO: Implement test")
                lines.append(f"      const parent = {{ id: 'test-id', {field.name}Id: 'related-id' }};")
                lines.append(f"      const context = {{")
                lines.append(f"        prisma: {{}},")
                lines.append(f"        loaders: {{}},")
                lines.append(f"        user: null")
                lines.append(f"      }};")
                lines.append(f"      ")
                lines.append(f"      // const result = await {gql_type.name}Resolvers.{gql_type.name}.{field.name}(")
                lines.append(f"      //   parent,")
                lines.append(f"      //   {{}},")
                lines.append(f"      //   context")
                lines.append(f"      // );")
                lines.append(f"      ")
                lines.append(f"      // expect(result).toBeDefined();")
                lines.append(f"    }});")
                lines.append(f"  }});")
                lines.append("")

        lines.append("});")

        return "\n".join(lines)

    def _generate_query_test(self) -> str:
        """Generate test file for Query resolver"""
        lines = []
        lines.append("// Auto-generated by resolver_generator.py")
        lines.append("// Tests for Query resolvers")
        lines.append("")
        lines.append("import { QueryResolvers } from './query.resolver';")
        lines.append("")

        lines.append("describe('QueryResolvers', () => {")

        for query in self.queries:
            lines.append(f"  describe('{query.name}', () => {{")
            lines.append(f"    it('should return {query.type_name}', async () => {{")
            lines.append(f"      // TODO: Implement test")
            lines.append(f"    }});")
            lines.append(f"  }});")
            lines.append("")

        lines.append("});")

        return "\n".join(lines)

    def _generate_mutation_test(self) -> str:
        """Generate test file for Mutation resolver"""
        lines = []
        lines.append("// Auto-generated by resolver_generator.py")
        lines.append("// Tests for Mutation resolvers")
        lines.append("")
        lines.append("import { MutationResolvers } from './mutation.resolver';")
        lines.append("")

        lines.append("describe('MutationResolvers', () => {")

        for mutation in self.mutations:
            lines.append(f"  describe('{mutation.name}', () => {{")
            lines.append(f"    it('should execute {mutation.name}', async () => {{")
            lines.append(f"      // TODO: Implement test")
            lines.append(f"    }});")
            lines.append(f"  }});")
            lines.append("")

        lines.append("});")

        return "\n".join(lines)

    def _write_files(self, files: Dict[str, str]) -> None:
        """Write generated files to output directory"""
        self.output_dir.mkdir(parents=True, exist_ok=True)

        for filename, content in files.items():
            filepath = self.output_dir / filename
            filepath.write_text(content)
            if self.verbose:
                print(f"  Generated: {filepath}")

    # Utility methods

    def _get_ts_type(self, gql_type: str, is_list: bool, is_required: bool) -> str:
        """Convert GraphQL type to TypeScript type"""
        ts_type = self.TS_TYPE_MAP.get(gql_type, gql_type)

        if is_list:
            ts_type = f"{ts_type}[]"

        if not is_required:
            ts_type = f"{ts_type} | null"

        return ts_type

    def _get_args_type(self, arguments: List[Dict[str, str]]) -> str:
        """Generate TypeScript type for arguments"""
        if not arguments:
            return "Record<string, never>"

        parts = []
        for arg in arguments:
            ts_type = self._get_ts_type(arg['type'], arg.get('is_list', False), arg.get('is_required', False))
            optional = '' if arg.get('is_required') else '?'
            parts.append(f"{arg['name']}{optional}: {ts_type}")

        return "{ " + "; ".join(parts) + " }"

    def _to_kebab_case(self, name: str) -> str:
        """Convert PascalCase to kebab-case"""
        result = re.sub(r'([A-Z])', r'-\1', name).lower()
        return result.lstrip('-')

    def _to_camel_case(self, name: str) -> str:
        """Convert PascalCase to camelCase"""
        return name[0].lower() + name[1:] if name else name

    def _to_pascal_case(self, name: str) -> str:
        """Convert kebab-case to PascalCase"""
        return ''.join(word.capitalize() for word in name.split('-'))

    def _to_screaming_snake(self, name: str) -> str:
        """Convert camelCase to SCREAMING_SNAKE_CASE"""
        result = re.sub(r'([A-Z])', r'_\1', name).upper()
        return result.lstrip('_')


def main():
    """Main entry point with CLI interface"""
    parser = argparse.ArgumentParser(
        description="GraphQL Resolver Generator - Generate TypeScript resolvers from schema",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s schema.graphql --output src/resolvers
  %(prog)s schema.graphql --output src/resolvers --dataloader
  %(prog)s schema.graphql --output src/resolvers --types User,Post
  %(prog)s schema.graphql --output src/resolvers --tests
  %(prog)s schema.graphql --output src/resolvers --dry-run

Part of senior-graphql skill for engineering-team.
"""
    )

    parser.add_argument(
        'schema',
        nargs='?',
        help='Path to GraphQL schema file'
    )

    parser.add_argument(
        '-o', '--output',
        required=False,
        default='./resolvers',
        help='Output directory for generated files (default: ./resolvers)'
    )

    parser.add_argument(
        '--dataloader',
        action='store_true',
        help='Include DataLoader factories for N+1 prevention'
    )

    parser.add_argument(
        '--tests',
        action='store_true',
        help='Generate test file stubs'
    )

    parser.add_argument(
        '--types',
        help='Comma-separated list of types to generate (default: all)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview files without writing'
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

    if not args.schema:
        parser.print_help()
        sys.exit(1)

    try:
        generator = ResolverGenerator(
            args.schema,
            args.output,
            verbose=args.verbose
        )

        filter_types = args.types.split(',') if args.types else None

        files = generator.generate(
            include_dataloader=args.dataloader,
            include_tests=args.tests,
            filter_types=filter_types,
            dry_run=args.dry_run
        )

        if not args.dry_run:
            print(f"\nGenerated {len(files)} files in {args.output}/")
            if args.verbose:
                print("\nFiles generated:")
                for filename in sorted(files.keys()):
                    print(f"  - {filename}")

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error generating resolvers: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
