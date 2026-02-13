#!/usr/bin/env python3
"""
Apollo Federation Scaffolder

Scaffolds Apollo Federation subgraphs with proper entity definitions,
reference resolvers, and gateway configuration.

Part of senior-graphql skill for engineering-team.

Usage:
    python federation_scaffolder.py users-service --entities User,Profile
    python federation_scaffolder.py posts-service --entities Post --references User
    python federation_scaffolder.py gateway --subgraphs users:4001,posts:4002
    python federation_scaffolder.py --help
    python federation_scaffolder.py --version
"""

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set


# Version
__version__ = "1.0.0"


@dataclass
class Entity:
    """Represents a Federation entity"""
    name: str
    key_field: str = "id"
    fields: List[Dict[str, str]] = field(default_factory=list)
    references: List[str] = field(default_factory=list)


@dataclass
class SubgraphConfig:
    """Configuration for a subgraph"""
    name: str
    port: int
    entities: List[Entity]
    references: List[str]  # External entities this subgraph references
    include_docker: bool = True
    include_tests: bool = True


class FederationScaffolder:
    """Scaffolds Apollo Federation subgraphs and gateway"""

    def __init__(self, output_dir: str, verbose: bool = False):
        """
        Initialize scaffolder.

        Args:
            output_dir: Base output directory
            verbose: Enable verbose output
        """
        self.output_dir = Path(output_dir)
        self.verbose = verbose

    def scaffold_subgraph(self, config: SubgraphConfig, dry_run: bool = False) -> Dict[str, str]:
        """
        Scaffold a Federation subgraph.

        Args:
            config: Subgraph configuration
            dry_run: Preview without writing

        Returns:
            Dict mapping file paths to contents
        """
        if self.verbose:
            print(f"Scaffolding subgraph: {config.name}")
            print(f"  Entities: {', '.join(e.name for e in config.entities)}")
            if config.references:
                print(f"  References: {', '.join(config.references)}")

        files: Dict[str, str] = {}

        # Package.json
        files['package.json'] = self._generate_package_json(config)

        # TypeScript config
        files['tsconfig.json'] = self._generate_tsconfig()

        # Environment
        files['.env.example'] = self._generate_env_example(config)
        files['.gitignore'] = self._generate_gitignore()

        # Source files
        files['src/index.ts'] = self._generate_server(config)
        files['src/schema.graphql'] = self._generate_schema(config)
        files['src/resolvers/index.ts'] = self._generate_resolvers(config)
        files['src/resolvers/reference.ts'] = self._generate_reference_resolvers(config)
        files['src/datasources/index.ts'] = self._generate_datasources(config)
        files['src/context.ts'] = self._generate_context(config)

        # DataLoader
        files['src/dataloaders/index.ts'] = self._generate_dataloaders(config)

        # Docker
        if config.include_docker:
            files['Dockerfile'] = self._generate_dockerfile()
            files['docker-compose.yml'] = self._generate_docker_compose(config)

        # Tests
        if config.include_tests:
            files['tests/setup.ts'] = self._generate_test_setup()
            files['tests/integration.test.ts'] = self._generate_integration_tests(config)
            files['jest.config.js'] = self._generate_jest_config()

        # README
        files['README.md'] = self._generate_readme(config)

        # Write files
        subgraph_dir = self.output_dir / config.name

        if not dry_run:
            self._write_files(subgraph_dir, files)
        else:
            print(f"\n[DRY RUN] Would generate in {subgraph_dir}/:")
            for filepath in sorted(files.keys()):
                print(f"  {filepath}")

        return files

    def scaffold_gateway(self, subgraphs: Dict[str, int], dry_run: bool = False) -> Dict[str, str]:
        """
        Scaffold Apollo Gateway.

        Args:
            subgraphs: Dict mapping subgraph names to ports
            dry_run: Preview without writing

        Returns:
            Dict mapping file paths to contents
        """
        if self.verbose:
            print("Scaffolding Apollo Gateway")
            for name, port in subgraphs.items():
                print(f"  {name}: port {port}")

        files: Dict[str, str] = {}

        files['package.json'] = self._generate_gateway_package_json()
        files['tsconfig.json'] = self._generate_tsconfig()
        files['.env.example'] = self._generate_gateway_env(subgraphs)
        files['.gitignore'] = self._generate_gitignore()

        files['src/index.ts'] = self._generate_gateway_server(subgraphs)
        files['src/supergraph.ts'] = self._generate_supergraph_config(subgraphs)

        files['Dockerfile'] = self._generate_gateway_dockerfile()
        files['docker-compose.yml'] = self._generate_gateway_docker_compose(subgraphs)

        files['README.md'] = self._generate_gateway_readme(subgraphs)

        # Write files
        gateway_dir = self.output_dir / 'gateway'

        if not dry_run:
            self._write_files(gateway_dir, files)
        else:
            print(f"\n[DRY RUN] Would generate in {gateway_dir}/:")
            for filepath in sorted(files.keys()):
                print(f"  {filepath}")

        return files

    # Subgraph file generators

    def _generate_package_json(self, config: SubgraphConfig) -> str:
        """Generate package.json for subgraph"""
        package = {
            "name": config.name,
            "version": "1.0.0",
            "description": f"Apollo Federation subgraph for {config.name}",
            "main": "dist/index.js",
            "scripts": {
                "dev": "ts-node-dev --respawn src/index.ts",
                "build": "tsc",
                "start": "node dist/index.js",
                "test": "jest",
                "test:watch": "jest --watch",
                "generate": "graphql-codegen",
                "lint": "eslint src --ext .ts",
                "compose": "rover supergraph compose --config ./supergraph.yaml"
            },
            "dependencies": {
                "@apollo/server": "^4.9.0",
                "@apollo/subgraph": "^2.5.0",
                "graphql": "^16.8.0",
                "graphql-tag": "^2.12.6",
                "dataloader": "^2.2.2",
                "@prisma/client": "^5.6.0",
                "dotenv": "^16.3.1"
            },
            "devDependencies": {
                "@types/node": "^20.10.0",
                "typescript": "^5.3.0",
                "ts-node-dev": "^2.0.0",
                "@graphql-codegen/cli": "^5.0.0",
                "@graphql-codegen/typescript": "^4.0.0",
                "@graphql-codegen/typescript-resolvers": "^4.0.0",
                "jest": "^29.7.0",
                "@types/jest": "^29.5.0",
                "ts-jest": "^29.1.0",
                "prisma": "^5.6.0",
                "eslint": "^8.55.0",
                "@typescript-eslint/eslint-plugin": "^6.0.0",
                "@typescript-eslint/parser": "^6.0.0"
            }
        }
        return json.dumps(package, indent=2)

    def _generate_tsconfig(self) -> str:
        """Generate TypeScript configuration"""
        config = {
            "compilerOptions": {
                "target": "ES2022",
                "module": "commonjs",
                "lib": ["ES2022"],
                "outDir": "./dist",
                "rootDir": "./src",
                "strict": True,
                "esModuleInterop": True,
                "skipLibCheck": True,
                "forceConsistentCasingInFileNames": True,
                "resolveJsonModule": True,
                "declaration": True,
                "declarationMap": True,
                "sourceMap": True
            },
            "include": ["src/**/*"],
            "exclude": ["node_modules", "dist", "tests"]
        }
        return json.dumps(config, indent=2)

    def _generate_env_example(self, config: SubgraphConfig) -> str:
        """Generate .env.example"""
        lines = [
            "# Server Configuration",
            f"PORT={config.port}",
            "NODE_ENV=development",
            "",
            "# Database",
            f"DATABASE_URL=postgresql://postgres:postgres@localhost:5432/{config.name.replace('-', '_')}",
            "",
            "# Redis (for caching/pubsub)",
            "REDIS_URL=redis://localhost:6379",
            "",
            "# JWT (for authentication)",
            "JWT_SECRET=your-secret-key-here",
            "",
            "# Apollo Studio (optional)",
            "APOLLO_KEY=",
            "APOLLO_GRAPH_REF=",
        ]
        return "\n".join(lines)

    def _generate_gitignore(self) -> str:
        """Generate .gitignore"""
        return """# Dependencies
node_modules/

# Build
dist/

# Environment
.env
.env.local

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Test
coverage/

# Prisma
prisma/migrations/*_*

# Logs
*.log
npm-debug.log*
"""

    def _generate_server(self, config: SubgraphConfig) -> str:
        """Generate main server file"""
        lines = []
        lines.append("// Apollo Federation Subgraph Server")
        lines.append(f"// Service: {config.name}")
        lines.append("")
        lines.append("import 'dotenv/config';")
        lines.append("import { ApolloServer } from '@apollo/server';")
        lines.append("import { startStandaloneServer } from '@apollo/server/standalone';")
        lines.append("import { buildSubgraphSchema } from '@apollo/subgraph';")
        lines.append("import { readFileSync } from 'fs';")
        lines.append("import { resolve } from 'path';")
        lines.append("import gql from 'graphql-tag';")
        lines.append("")
        lines.append("import { resolvers } from './resolvers';")
        lines.append("import { createContext, Context } from './context';")
        lines.append("")
        lines.append("// Load schema")
        lines.append("const typeDefs = gql(")
        lines.append("  readFileSync(resolve(__dirname, 'schema.graphql'), 'utf-8')")
        lines.append(");")
        lines.append("")
        lines.append("// Build federated schema")
        lines.append("const schema = buildSubgraphSchema([{ typeDefs, resolvers }]);")
        lines.append("")
        lines.append("// Create Apollo Server")
        lines.append("const server = new ApolloServer<Context>({")
        lines.append("  schema,")
        lines.append("  introspection: process.env.NODE_ENV !== 'production',")
        lines.append("});")
        lines.append("")
        lines.append("// Start server")
        lines.append("const start = async () => {")
        lines.append(f"  const port = parseInt(process.env.PORT || '{config.port}', 10);")
        lines.append("")
        lines.append("  const { url } = await startStandaloneServer(server, {")
        lines.append("    listen: { port },")
        lines.append("    context: async ({ req }) => createContext(req),")
        lines.append("  });")
        lines.append("")
        lines.append(f"  console.log(`🚀 {config.name} subgraph ready at ${{url}}`);")
        lines.append("};")
        lines.append("")
        lines.append("start().catch(console.error);")

        return "\n".join(lines)

    def _generate_schema(self, config: SubgraphConfig) -> str:
        """Generate GraphQL schema with Federation directives"""
        lines = []
        lines.append("# Apollo Federation Schema")
        lines.append(f"# Service: {config.name}")
        lines.append("")
        lines.append("extend schema")
        lines.append('  @link(url: "https://specs.apollo.dev/federation/v2.0",')
        lines.append('        import: ["@key", "@external", "@requires", "@provides", "@shareable"])')
        lines.append("")

        # Define owned entities
        for entity in config.entities:
            lines.append(f"# {entity.name} - Owned by this subgraph")
            lines.append(f'type {entity.name} @key(fields: "{entity.key_field}") {{')
            lines.append(f"  {entity.key_field}: ID!")

            # Add default fields based on entity name
            if entity.name == 'User':
                lines.extend([
                    "  email: String!",
                    "  name: String",
                    "  createdAt: DateTime!",
                    "  updatedAt: DateTime!",
                ])
            elif entity.name == 'Profile':
                lines.extend([
                    "  bio: String",
                    "  avatar: String",
                    "  website: String",
                    "  user: User!",
                ])
            elif entity.name == 'Post':
                lines.extend([
                    "  title: String!",
                    "  content: String!",
                    "  published: Boolean!",
                    "  author: User!",
                    "  createdAt: DateTime!",
                ])
            elif entity.name == 'Comment':
                lines.extend([
                    "  content: String!",
                    "  author: User!",
                    "  post: Post!",
                    "  createdAt: DateTime!",
                ])
            else:
                # Generic fields
                lines.extend([
                    "  name: String",
                    "  createdAt: DateTime!",
                ])

            lines.append("}")
            lines.append("")

        # Extend referenced entities
        for ref in config.references:
            lines.append(f"# {ref} - Extended from another subgraph")
            lines.append(f'extend type {ref} @key(fields: "id") {{')
            lines.append("  id: ID! @external")

            # Add extension fields based on entity relationship
            entity_names = [e.name for e in config.entities]
            for entity in config.entities:
                if ref == 'User' and entity.name in ['Post', 'Comment']:
                    lines.append(f"  {entity.name.lower()}s: [{entity.name}!]!")
                elif ref == 'Post' and entity.name == 'Comment':
                    lines.append(f"  comments: [Comment!]!")

            lines.append("}")
            lines.append("")

        # Query type
        lines.append("type Query {")
        for entity in config.entities:
            entity_lower = entity.name[0].lower() + entity.name[1:]
            lines.append(f"  {entity_lower}(id: ID!): {entity.name}")
            lines.append(f"  {entity_lower}s(first: Int, after: String): [{entity.name}!]!")
        lines.append("}")
        lines.append("")

        # Mutation type
        lines.append("type Mutation {")
        for entity in config.entities:
            entity_lower = entity.name[0].lower() + entity.name[1:]
            lines.append(f"  create{entity.name}(input: Create{entity.name}Input!): {entity.name}!")
            lines.append(f"  update{entity.name}(id: ID!, input: Update{entity.name}Input!): {entity.name}!")
            lines.append(f"  delete{entity.name}(id: ID!): Boolean!")
        lines.append("}")
        lines.append("")

        # Input types
        for entity in config.entities:
            lines.append(f"input Create{entity.name}Input {{")
            if entity.name == 'User':
                lines.extend(["  email: String!", "  name: String", "  password: String!"])
            elif entity.name == 'Post':
                lines.extend(["  title: String!", "  content: String!"])
            elif entity.name == 'Comment':
                lines.extend(["  content: String!", "  postId: ID!"])
            else:
                lines.append("  name: String")
            lines.append("}")
            lines.append("")

            lines.append(f"input Update{entity.name}Input {{")
            if entity.name == 'User':
                lines.extend(["  email: String", "  name: String"])
            elif entity.name == 'Post':
                lines.extend(["  title: String", "  content: String", "  published: Boolean"])
            elif entity.name == 'Comment':
                lines.append("  content: String")
            else:
                lines.append("  name: String")
            lines.append("}")
            lines.append("")

        # Custom scalars
        lines.append("scalar DateTime")

        return "\n".join(lines)

    def _generate_resolvers(self, config: SubgraphConfig) -> str:
        """Generate resolvers index file"""
        lines = []
        lines.append("// Resolver exports")
        lines.append("")
        lines.append("import { referenceResolvers } from './reference';")
        lines.append("import { Context } from '../context';")
        lines.append("")

        # Query resolvers
        lines.append("const Query = {")
        for entity in config.entities:
            entity_lower = entity.name[0].lower() + entity.name[1:]
            lines.append(f"  {entity_lower}: async (_: unknown, {{ id }}: {{ id: string }}, {{ dataSources }}: Context) => {{")
            lines.append(f"    return dataSources.{entity_lower}API.get{entity.name}(id);")
            lines.append("  },")
            lines.append("")
            lines.append(f"  {entity_lower}s: async (_: unknown, args: {{ first?: number; after?: string }}, {{ dataSources }}: Context) => {{")
            lines.append(f"    return dataSources.{entity_lower}API.get{entity.name}s(args.first, args.after);")
            lines.append("  },")
        lines.append("};")
        lines.append("")

        # Mutation resolvers
        lines.append("const Mutation = {")
        for entity in config.entities:
            entity_lower = entity.name[0].lower() + entity.name[1:]
            lines.append(f"  create{entity.name}: async (_: unknown, {{ input }}: {{ input: Record<string, unknown> }}, {{ dataSources, user }}: Context) => {{")
            lines.append("    if (!user) throw new Error('Not authenticated');")
            lines.append(f"    return dataSources.{entity_lower}API.create{entity.name}(input, user.id);")
            lines.append("  },")
            lines.append("")
            lines.append(f"  update{entity.name}: async (_: unknown, {{ id, input }}: {{ id: string; input: Record<string, unknown> }}, {{ dataSources, user }}: Context) => {{")
            lines.append("    if (!user) throw new Error('Not authenticated');")
            lines.append(f"    return dataSources.{entity_lower}API.update{entity.name}(id, input);")
            lines.append("  },")
            lines.append("")
            lines.append(f"  delete{entity.name}: async (_: unknown, {{ id }}: {{ id: string }}, {{ dataSources, user }}: Context) => {{")
            lines.append("    if (!user) throw new Error('Not authenticated');")
            lines.append(f"    return dataSources.{entity_lower}API.delete{entity.name}(id);")
            lines.append("  },")
        lines.append("};")
        lines.append("")

        lines.append("export const resolvers = {")
        lines.append("  Query,")
        lines.append("  Mutation,")
        lines.append("  ...referenceResolvers,")
        lines.append("};")

        return "\n".join(lines)

    def _generate_reference_resolvers(self, config: SubgraphConfig) -> str:
        """Generate Federation reference resolvers"""
        lines = []
        lines.append("// Federation reference resolvers")
        lines.append("// These resolve entity references from other subgraphs")
        lines.append("")
        lines.append("import { Context } from '../context';")
        lines.append("")

        lines.append("export const referenceResolvers = {")

        # Owned entities need __resolveReference
        for entity in config.entities:
            lines.append(f"  {entity.name}: {{")
            lines.append(f"    __resolveReference: async (")
            lines.append(f"      ref: {{ id: string }},")
            lines.append(f"      {{ dataSources }}: Context")
            lines.append(f"    ) => {{")
            entity_lower = entity.name[0].lower() + entity.name[1:]
            lines.append(f"      return dataSources.{entity_lower}API.get{entity.name}(ref.id);")
            lines.append("    },")

            # Add field resolvers for relations
            for ref in config.references:
                if ref == 'User':
                    lines.append("")
                    lines.append(f"    author: (parent: {{ authorId?: string }}) => {{")
                    lines.append(f"      if (!parent.authorId) return null;")
                    lines.append(f"      return {{ __typename: 'User', id: parent.authorId }};")
                    lines.append("    },")
                elif ref == 'Post' and entity.name == 'Comment':
                    lines.append("")
                    lines.append(f"    post: (parent: {{ postId?: string }}) => {{")
                    lines.append(f"      if (!parent.postId) return null;")
                    lines.append(f"      return {{ __typename: 'Post', id: parent.postId }};")
                    lines.append("    },")

            lines.append("  },")
            lines.append("")

        # Extended entities (references from other subgraphs)
        for ref in config.references:
            entity_names = [e.name for e in config.entities]

            if ref == 'User' and any(e in ['Post', 'Comment'] for e in entity_names):
                lines.append(f"  {ref}: {{")
                for entity in config.entities:
                    if entity.name in ['Post', 'Comment']:
                        entity_lower = entity.name[0].lower() + entity.name[1:]
                        lines.append(f"    {entity_lower}s: async (")
                        lines.append(f"      user: {{ id: string }},")
                        lines.append(f"      _args: unknown,")
                        lines.append(f"      {{ dataSources }}: Context")
                        lines.append(f"    ) => {{")
                        lines.append(f"      return dataSources.{entity_lower}API.get{entity.name}sByAuthor(user.id);")
                        lines.append("    },")
                lines.append("  },")
                lines.append("")

            elif ref == 'Post' and 'Comment' in entity_names:
                lines.append(f"  {ref}: {{")
                lines.append(f"    comments: async (")
                lines.append(f"      post: {{ id: string }},")
                lines.append(f"      _args: unknown,")
                lines.append(f"      {{ dataSources }}: Context")
                lines.append(f"    ) => {{")
                lines.append(f"      return dataSources.commentAPI.getCommentsByPost(post.id);")
                lines.append("    },")
                lines.append("  },")
                lines.append("")

        lines.append("};")

        return "\n".join(lines)

    def _generate_datasources(self, config: SubgraphConfig) -> str:
        """Generate data sources"""
        lines = []
        lines.append("// Data sources for database access")
        lines.append("")
        lines.append("import { PrismaClient } from '@prisma/client';")
        lines.append("")

        lines.append("const prisma = new PrismaClient();")
        lines.append("")

        for entity in config.entities:
            entity_lower = entity.name[0].lower() + entity.name[1:]
            lines.append(f"export class {entity.name}API {{")
            lines.append(f"  async get{entity.name}(id: string) {{")
            lines.append(f"    return prisma.{entity_lower}.findUnique({{ where: {{ id }} }});")
            lines.append("  }")
            lines.append("")
            lines.append(f"  async get{entity.name}s(first = 10, after?: string) {{")
            lines.append(f"    return prisma.{entity_lower}.findMany({{")
            lines.append(f"      take: first,")
            lines.append(f"      cursor: after ? {{ id: after }} : undefined,")
            lines.append(f"      skip: after ? 1 : 0,")
            lines.append(f"    }});")
            lines.append("  }")
            lines.append("")
            lines.append(f"  async get{entity.name}sByAuthor(authorId: string) {{")
            lines.append(f"    return prisma.{entity_lower}.findMany({{")
            lines.append(f"      where: {{ authorId }},")
            lines.append(f"    }});")
            lines.append("  }")
            lines.append("")
            if entity.name == 'Comment':
                lines.append(f"  async getCommentsByPost(postId: string) {{")
                lines.append(f"    return prisma.comment.findMany({{")
                lines.append(f"      where: {{ postId }},")
                lines.append(f"    }});")
                lines.append("  }")
                lines.append("")
            lines.append(f"  async create{entity.name}(input: Record<string, unknown>, userId: string) {{")
            lines.append(f"    return prisma.{entity_lower}.create({{")
            lines.append(f"      data: {{")
            lines.append(f"        ...input,")
            lines.append(f"        authorId: userId,")
            lines.append(f"      }} as any,")
            lines.append(f"    }});")
            lines.append("  }")
            lines.append("")
            lines.append(f"  async update{entity.name}(id: string, input: Record<string, unknown>) {{")
            lines.append(f"    return prisma.{entity_lower}.update({{")
            lines.append(f"      where: {{ id }},")
            lines.append(f"      data: input as any,")
            lines.append(f"    }});")
            lines.append("  }")
            lines.append("")
            lines.append(f"  async delete{entity.name}(id: string) {{")
            lines.append(f"    await prisma.{entity_lower}.delete({{ where: {{ id }} }});")
            lines.append(f"    return true;")
            lines.append("  }")
            lines.append("}")
            lines.append("")

        # Export factory
        lines.append("export const createDataSources = () => ({")
        for entity in config.entities:
            entity_lower = entity.name[0].lower() + entity.name[1:]
            lines.append(f"  {entity_lower}API: new {entity.name}API(),")
        lines.append("});")
        lines.append("")
        lines.append("export type DataSources = ReturnType<typeof createDataSources>;")

        return "\n".join(lines)

    def _generate_context(self, config: SubgraphConfig) -> str:
        """Generate context file"""
        lines = []
        lines.append("// GraphQL Context")
        lines.append("")
        lines.append("import { IncomingMessage } from 'http';")
        lines.append("import { createDataSources, DataSources } from './datasources';")
        lines.append("import { createLoaders, Loaders } from './dataloaders';")
        lines.append("")

        lines.append("export interface User {")
        lines.append("  id: string;")
        lines.append("  email: string;")
        lines.append("}")
        lines.append("")

        lines.append("export interface Context {")
        lines.append("  dataSources: DataSources;")
        lines.append("  loaders: Loaders;")
        lines.append("  user: User | null;")
        lines.append("}")
        lines.append("")

        lines.append("export const createContext = async (req: IncomingMessage): Promise<Context> => {")
        lines.append("  // Extract user from JWT token")
        lines.append("  const user = await authenticateRequest(req);")
        lines.append("")
        lines.append("  return {")
        lines.append("    dataSources: createDataSources(),")
        lines.append("    loaders: createLoaders(),")
        lines.append("    user,")
        lines.append("  };")
        lines.append("};")
        lines.append("")

        lines.append("const authenticateRequest = async (req: IncomingMessage): Promise<User | null> => {")
        lines.append("  const authHeader = req.headers.authorization;")
        lines.append("  if (!authHeader?.startsWith('Bearer ')) return null;")
        lines.append("")
        lines.append("  const token = authHeader.slice(7);")
        lines.append("  ")
        lines.append("  // TODO: Verify JWT and return user")
        lines.append("  // For now, return null (unauthenticated)")
        lines.append("  return null;")
        lines.append("};")

        return "\n".join(lines)

    def _generate_dataloaders(self, config: SubgraphConfig) -> str:
        """Generate DataLoader factories"""
        lines = []
        lines.append("// DataLoader factories for batch loading")
        lines.append("")
        lines.append("import DataLoader from 'dataloader';")
        lines.append("import { PrismaClient } from '@prisma/client';")
        lines.append("")

        lines.append("const prisma = new PrismaClient();")
        lines.append("")

        lines.append("export const createLoaders = () => ({")

        for entity in config.entities:
            entity_lower = entity.name[0].lower() + entity.name[1:]
            lines.append(f"  {entity_lower}Loader: new DataLoader(async (ids: readonly string[]) => {{")
            lines.append(f"    const items = await prisma.{entity_lower}.findMany({{")
            lines.append(f"      where: {{ id: {{ in: [...ids] }} }},")
            lines.append(f"    }});")
            lines.append(f"    const itemMap = new Map(items.map(item => [item.id, item]));")
            lines.append(f"    return ids.map(id => itemMap.get(id) ?? null);")
            lines.append(f"  }}),")
            lines.append("")

        lines.append("});")
        lines.append("")
        lines.append("export type Loaders = ReturnType<typeof createLoaders>;")

        return "\n".join(lines)

    def _generate_dockerfile(self) -> str:
        """Generate Dockerfile for subgraph"""
        return """# Build stage
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# Production stage
FROM node:20-alpine

WORKDIR /app

COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package*.json ./

ENV NODE_ENV=production

EXPOSE 4000

CMD ["node", "dist/index.js"]
"""

    def _generate_docker_compose(self, config: SubgraphConfig) -> str:
        """Generate docker-compose.yml for subgraph"""
        db_name = config.name.replace('-', '_')

        return f"""version: '3.8'

services:
  {config.name}:
    build: .
    ports:
      - "{config.port}:4000"
    environment:
      - NODE_ENV=development
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/{db_name}
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB={db_name}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
"""

    def _generate_test_setup(self) -> str:
        """Generate test setup file"""
        return """// Test setup
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

beforeAll(async () => {
  // Setup test database
});

afterAll(async () => {
  await prisma.$disconnect();
});

export { prisma };
"""

    def _generate_integration_tests(self, config: SubgraphConfig) -> str:
        """Generate integration tests"""
        lines = []
        lines.append("// Integration tests")
        lines.append("")
        lines.append("import { prisma } from './setup';")
        lines.append("")

        for entity in config.entities:
            entity_lower = entity.name[0].lower() + entity.name[1:]
            lines.append(f"describe('{entity.name} API', () => {{")
            lines.append(f"  describe('get{entity.name}', () => {{")
            lines.append(f"    it('should return {entity_lower} by id', async () => {{")
            lines.append(f"      // TODO: Implement test")
            lines.append(f"    }});")
            lines.append(f"  }});")
            lines.append("")
            lines.append(f"  describe('create{entity.name}', () => {{")
            lines.append(f"    it('should create new {entity_lower}', async () => {{")
            lines.append(f"      // TODO: Implement test")
            lines.append(f"    }});")
            lines.append(f"  }});")
            lines.append(f"}});")
            lines.append("")

        return "\n".join(lines)

    def _generate_jest_config(self) -> str:
        """Generate Jest configuration"""
        config = {
            "preset": "ts-jest",
            "testEnvironment": "node",
            "roots": ["<rootDir>/tests"],
            "setupFilesAfterEnv": ["<rootDir>/tests/setup.ts"],
            "moduleFileExtensions": ["ts", "js", "json"],
            "testMatch": ["**/*.test.ts"],
            "collectCoverageFrom": ["src/**/*.ts"],
            "coverageDirectory": "coverage"
        }
        return f"module.exports = {json.dumps(config, indent=2)};"

    def _generate_readme(self, config: SubgraphConfig) -> str:
        """Generate README for subgraph"""
        entities = ', '.join(e.name for e in config.entities)

        return f"""# {config.name}

Apollo Federation subgraph for {entities}.

## Quick Start

```bash
# Install dependencies
npm install

# Set up environment
cp .env.example .env

# Generate Prisma client
npx prisma generate

# Start development server
npm run dev
```

Server runs at http://localhost:{config.port}/graphql

## Entities

This subgraph owns the following entities:

{chr(10).join(f'- **{e.name}** (key: `{e.key_field}`)' for e in config.entities)}

{f"## References{chr(10)}{chr(10)}This subgraph extends:{chr(10)}{chr(10)}" + chr(10).join(f'- {ref}' for ref in config.references) if config.references else ''}

## Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run test` - Run tests
- `npm run lint` - Lint code

## Docker

```bash
docker-compose up -d
```

---

Generated by federation_scaffolder.py
"""

    # Gateway generators

    def _generate_gateway_package_json(self) -> str:
        """Generate package.json for gateway"""
        package = {
            "name": "apollo-gateway",
            "version": "1.0.0",
            "description": "Apollo Federation Gateway",
            "main": "dist/index.js",
            "scripts": {
                "dev": "ts-node-dev --respawn src/index.ts",
                "build": "tsc",
                "start": "node dist/index.js",
                "compose": "rover supergraph compose --config ./supergraph.yaml > supergraph.graphql"
            },
            "dependencies": {
                "@apollo/gateway": "^2.5.0",
                "@apollo/server": "^4.9.0",
                "graphql": "^16.8.0",
                "dotenv": "^16.3.1"
            },
            "devDependencies": {
                "@types/node": "^20.10.0",
                "typescript": "^5.3.0",
                "ts-node-dev": "^2.0.0"
            }
        }
        return json.dumps(package, indent=2)

    def _generate_gateway_env(self, subgraphs: Dict[str, int]) -> str:
        """Generate .env.example for gateway"""
        lines = [
            "# Gateway Configuration",
            "PORT=4000",
            "NODE_ENV=development",
            "",
            "# Subgraph URLs"
        ]
        for name, port in subgraphs.items():
            env_name = name.upper().replace('-', '_')
            lines.append(f"{env_name}_URL=http://localhost:{port}/graphql")

        lines.extend([
            "",
            "# Apollo Studio (optional)",
            "APOLLO_KEY=",
            "APOLLO_GRAPH_REF=",
        ])

        return "\n".join(lines)

    def _generate_gateway_server(self, subgraphs: Dict[str, int]) -> str:
        """Generate gateway server file"""
        lines = []
        lines.append("// Apollo Federation Gateway")
        lines.append("")
        lines.append("import 'dotenv/config';")
        lines.append("import { ApolloServer } from '@apollo/server';")
        lines.append("import { startStandaloneServer } from '@apollo/server/standalone';")
        lines.append("import { ApolloGateway, IntrospectAndCompose } from '@apollo/gateway';")
        lines.append("")

        lines.append("// Configure gateway with subgraphs")
        lines.append("const gateway = new ApolloGateway({")
        lines.append("  supergraphSdl: new IntrospectAndCompose({")
        lines.append("    subgraphs: [")

        for name, port in subgraphs.items():
            env_name = name.upper().replace('-', '_')
            lines.append(f"      {{ name: '{name}', url: process.env.{env_name}_URL || 'http://localhost:{port}/graphql' }},")

        lines.append("    ],")
        lines.append("  }),")
        lines.append("});")
        lines.append("")

        lines.append("// Create Apollo Server")
        lines.append("const server = new ApolloServer({")
        lines.append("  gateway,")
        lines.append("  introspection: process.env.NODE_ENV !== 'production',")
        lines.append("});")
        lines.append("")

        lines.append("// Start server")
        lines.append("const start = async () => {")
        lines.append("  const port = parseInt(process.env.PORT || '4000', 10);")
        lines.append("")
        lines.append("  const { url } = await startStandaloneServer(server, {")
        lines.append("    listen: { port },")
        lines.append("  });")
        lines.append("")
        lines.append("  console.log(`🚀 Gateway ready at ${url}`);")
        lines.append("};")
        lines.append("")
        lines.append("start().catch(console.error);")

        return "\n".join(lines)

    def _generate_supergraph_config(self, subgraphs: Dict[str, int]) -> str:
        """Generate supergraph configuration"""
        lines = []
        lines.append("// Supergraph configuration")
        lines.append("// Use with: rover supergraph compose --config supergraph.yaml")
        lines.append("")

        lines.append("export const subgraphs = {")
        for name, port in subgraphs.items():
            lines.append(f"  '{name}': 'http://localhost:{port}/graphql',")
        lines.append("};")

        return "\n".join(lines)

    def _generate_gateway_dockerfile(self) -> str:
        """Generate Dockerfile for gateway"""
        return """# Build stage
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# Production stage
FROM node:20-alpine

WORKDIR /app

COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package*.json ./

ENV NODE_ENV=production

EXPOSE 4000

CMD ["node", "dist/index.js"]
"""

    def _generate_gateway_docker_compose(self, subgraphs: Dict[str, int]) -> str:
        """Generate docker-compose.yml for gateway"""
        lines = ["version: '3.8'", "", "services:"]

        lines.append("  gateway:")
        lines.append("    build: .")
        lines.append("    ports:")
        lines.append('      - "4000:4000"')
        lines.append("    environment:")
        lines.append("      - NODE_ENV=development")

        for name, port in subgraphs.items():
            env_name = name.upper().replace('-', '_')
            lines.append(f"      - {env_name}_URL=http://{name}:{port}/graphql")

        lines.append("    depends_on:")
        for name in subgraphs.keys():
            lines.append(f"      - {name}")

        lines.append("")

        # Add placeholder services for subgraphs
        for name, port in subgraphs.items():
            lines.append(f"  {name}:")
            lines.append(f"    # TODO: Configure {name} subgraph service")
            lines.append(f"    image: node:20-alpine")
            lines.append(f"    ports:")
            lines.append(f'      - "{port}:4000"')
            lines.append("")

        return "\n".join(lines)

    def _generate_gateway_readme(self, subgraphs: Dict[str, int]) -> str:
        """Generate README for gateway"""
        subgraph_list = '\n'.join(f'- **{name}**: http://localhost:{port}/graphql' for name, port in subgraphs.items())

        return f"""# Apollo Federation Gateway

Composes multiple subgraphs into a unified GraphQL API.

## Subgraphs

{subgraph_list}

## Quick Start

```bash
# Install dependencies
npm install

# Set up environment
cp .env.example .env

# Start gateway (subgraphs must be running first)
npm run dev
```

Gateway runs at http://localhost:4000/graphql

## Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run compose` - Compose supergraph schema

## Docker

```bash
docker-compose up -d
```

---

Generated by federation_scaffolder.py
"""

    def _write_files(self, base_dir: Path, files: Dict[str, str]) -> None:
        """Write files to directory"""
        for filepath, content in files.items():
            full_path = base_dir / filepath
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content)
            if self.verbose:
                print(f"  Generated: {full_path}")


def main():
    """Main entry point with CLI interface"""
    parser = argparse.ArgumentParser(
        description="Apollo Federation Scaffolder - Generate subgraphs and gateway",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s users-service --entities User,Profile
  %(prog)s posts-service --entities Post --references User --port 4002
  %(prog)s gateway --subgraphs users:4001,posts:4002,comments:4003
  %(prog)s users-service --entities User --docker --tests

Part of senior-graphql skill for engineering-team.
"""
    )

    parser.add_argument(
        'name',
        nargs='?',
        help='Subgraph or gateway name'
    )

    parser.add_argument(
        '--entities',
        help='Comma-separated list of entities this subgraph owns'
    )

    parser.add_argument(
        '--references',
        help='Comma-separated list of entities from other subgraphs'
    )

    parser.add_argument(
        '--subgraphs',
        help='For gateway: comma-separated list of subgraph:port pairs'
    )

    parser.add_argument(
        '--port',
        type=int,
        default=4001,
        help='Port for the subgraph (default: 4001)'
    )

    parser.add_argument(
        '-o', '--output',
        default='.',
        help='Output directory (default: current directory)'
    )

    parser.add_argument(
        '--docker',
        action='store_true',
        default=True,
        help='Include Docker configuration (default: True)'
    )

    parser.add_argument(
        '--no-docker',
        action='store_true',
        help='Exclude Docker configuration'
    )

    parser.add_argument(
        '--tests',
        action='store_true',
        default=True,
        help='Include test files (default: True)'
    )

    parser.add_argument(
        '--no-tests',
        action='store_true',
        help='Exclude test files'
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

    if not args.name:
        parser.print_help()
        sys.exit(1)

    try:
        scaffolder = FederationScaffolder(args.output, verbose=args.verbose)

        # Determine if this is a gateway or subgraph
        if args.name == 'gateway' or args.subgraphs:
            # Scaffold gateway
            if not args.subgraphs:
                print("Error: --subgraphs required for gateway", file=sys.stderr)
                sys.exit(1)

            subgraphs = {}
            for pair in args.subgraphs.split(','):
                name, port = pair.split(':')
                subgraphs[name.strip()] = int(port.strip())

            files = scaffolder.scaffold_gateway(subgraphs, dry_run=args.dry_run)

        else:
            # Scaffold subgraph
            if not args.entities:
                print("Error: --entities required for subgraph", file=sys.stderr)
                sys.exit(1)

            entities = [Entity(name=e.strip()) for e in args.entities.split(',')]
            references = args.references.split(',') if args.references else []

            config = SubgraphConfig(
                name=args.name,
                port=args.port,
                entities=entities,
                references=[r.strip() for r in references],
                include_docker=args.docker and not args.no_docker,
                include_tests=args.tests and not args.no_tests
            )

            files = scaffolder.scaffold_subgraph(config, dry_run=args.dry_run)

        if not args.dry_run:
            print(f"\nGenerated {len(files)} files in {args.output}/{args.name}/")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
