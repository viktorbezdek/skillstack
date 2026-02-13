# Docker Configuration Overview

## Introduction

This document explains how Docker is configured and used within our system. Docker configurations are defined in the `meta.json` file and enable containerization for both development and production deployments.

## Core Concept: Flexible Docker Setup

Docker configurations in our system are:
- **Location-flexible**: Dockerfile can be placed in any folder
- **Registry-aware**: Image names include full container registry addresses
- **Environment-specific**: Different Dockerfiles for development vs production
- **Build-context aware**: Separation between Dockerfile location and build context

## Docker Configuration in meta.json

**⚠️ ALWAYS fetch the schema first:**
```
https://raw.githubusercontent.com/ghostmind-dev/run/refs/heads/main/meta/schema.json
```

The Docker configuration is defined under the `docker` property in `meta.json`:

```json
{
  "docker": {
    "default": {
      "root": "docker",
      "image": "gcr.io/ghostmind-core/docs-mcp",
      "env_based": false,
      "context_dir": "app"
    }
  }
}
```

### Configuration Properties

#### `root` (required)
- **Purpose**: Specifies the directory where Dockerfile(s) are located
- **Example**: `"root": "docker"`
- **Result**: Dockerfiles are in `/path/to/project/docker/`

#### `image` (required)
- **Purpose**: Full image name including registry address
- **Supported Registries**:
  - GitHub Container Registry: `ghcr.io/organization/image-name`
  - Google Cloud Registry: `gcr.io/project-id/image-name`
- **Example**: `"image": "gcr.io/ghostmind-core/docs-mcp"`

#### `env_based` (optional)
- **Purpose**: Whether to use environment-specific Dockerfiles
- **Values**: `true` or `false`
- **When `false`**: Uses `Dockerfile` (default)
- **When `true`**: Uses `Dockerfile.dev`, `Dockerfile.prod`, etc.

#### `context_dir` (optional)
- **Purpose**: Build context directory (relative to project root)
- **Default**: Project root if not specified
- **Example**: `"context_dir": "app"`
- **Result**: Docker build runs from `/path/to/project/app/`

#### `tag_modifiers` (optional)
- **Purpose**: Additional tags to apply to the image
- **Type**: Array of strings
- **Example**: `"tag_modifiers": ["latest", "v1.0.0"]`

**For complete `docker` property structure:** Fetch the schema

## Multiple Docker Configurations

You can define multiple Docker configurations for different purposes:

```json
{
  "docker": {
    "app": {
      "root": "docker",
      "image": "gcr.io/project/app",
      "context_dir": "app"
    },
    "worker": {
      "root": "docker/worker",
      "image": "gcr.io/project/worker",
      "context_dir": "worker"
    },
    "nginx": {
      "root": "docker/nginx",
      "image": "gcr.io/project/nginx"
    }
  }
}
```

## File Structure Examples

### Basic Setup
```
project/
├── meta.json
├── docker/
│   └── Dockerfile
└── app/
    └── (application code)
```

### Environment-Specific Setup
```
project/
├── meta.json
├── docker/
│   ├── Dockerfile.dev
│   └── Dockerfile.prod
└── app/
    └── (application code)
```

### Multi-Service Setup
```
project/
├── meta.json
├── docker/
│   ├── app/
│   │   └── Dockerfile
│   ├── worker/
│   │   └── Dockerfile
│   └── nginx/
│       └── Dockerfile
├── app/
└── worker/
```

## Container Registry Integration

### GitHub Container Registry
- **Format**: `ghcr.io/username/repository-name`
- **Authentication**: Uses `GITHUB_TOKEN`
- **Example**: `"image": "ghcr.io/ghostmind-dev/docs-mcp"`

### Google Cloud Registry
- **Format**: `gcr.io/project-id/image-name`
- **Authentication**: Uses Google Cloud credentials
- **Example**: `"image": "gcr.io/ghostmind-core/docs-mcp"`

## Build Process Integration

The `run` tool uses the Docker configuration to:

1. **Locate Dockerfile**: Uses `root` property to find Dockerfile
2. **Set build context**: Uses `context_dir` for Docker build context
3. **Tag images**: Applies full registry path from `image` property
4. **Handle environments**: Selects appropriate Dockerfile based on `env_based`

## Integration with Other Components

### Docker + Compose
Local development uses Docker images defined here:
```json
{
  "docker": {
    "default": { "image": "gcr.io/project/app" }
  },
  "compose": {
    "default": { "root": "local" }
  }
}
```

### Docker + Terraform
Production deployment references Docker images:
```json
{
  "docker": {
    "default": { "image": "gcr.io/project/app" }
  },
  "terraform": {
    "run": {
      "containers": ["default"]
    }
  }
}
```

## Best Practices

1. **Use full registry paths** in image names for clarity
2. **Separate Dockerfile location from build context** when needed
3. **Use multiple configurations** for multi-service applications
4. **Keep Dockerfiles in dedicated folders** for organization
5. **Use environment-based Dockerfiles** for different deployment targets

## Common Patterns

### Single Application
```json
{
  "docker": {
    "default": {
      "root": "docker",
      "image": "gcr.io/project/app",
      "context_dir": "app"
    }
  }
}
```

### Microservices
```json
{
  "docker": {
    "api": {
      "root": "docker/api",
      "image": "gcr.io/project/api",
      "context_dir": "services/api"
    },
    "worker": {
      "root": "docker/worker",
      "image": "gcr.io/project/worker",
      "context_dir": "services/worker"
    }
  }
}
```

### Development vs Production
```json
{
  "docker": {
    "app": {
      "root": "docker",
      "image": "gcr.io/project/app",
      "env_based": true,
      "context_dir": "app"
    }
  }
}
```

This configuration enables flexible, registry-aware Docker setups that integrate seamlessly with the broader system architecture.