# TaskFlow

> A modern task management API for building productivity applications

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.1.0-orange.svg)]()

## Overview

TaskFlow is a RESTful API service that provides robust task management capabilities for your applications. Built with performance and developer experience in mind, it offers real-time updates, flexible querying, and seamless integrations.

## Features

- **Task Management** - Create, update, and organize tasks with rich metadata
- **Project Organization** - Group tasks into projects with customizable workflows
- **Real-time Updates** - WebSocket support for instant synchronization
- **Flexible Querying** - Filter, sort, and search with powerful query syntax
- **Team Collaboration** - Share projects and assign tasks to team members
- **Webhooks** - Get notified when tasks change

## Quick Start

```bash
# Clone the repository
git clone https://github.com/example/taskflow.git
cd taskflow

# Install dependencies
npm install

# Set up environment
cp .env.example .env

# Run the development server
npm run dev
```

The API will be available at `http://localhost:3000`.

## Documentation

| Document | Description |
|----------|-------------|
| [Getting Started](docs/getting-started.md) | First-time setup guide |
| [API Reference](docs/api-reference.md) | Complete endpoint documentation |
| [Architecture](docs/architecture.md) | System design overview |
| [Contributing](CONTRIBUTING.md) | How to contribute |

## Prerequisites

- Node.js 18 or higher
- PostgreSQL 14 or higher
- Redis 7 or higher (for caching)

## Installation

### Using npm

```bash
npm install
npm run build
npm start
```

### Using Docker

```bash
docker-compose up -d
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | `3000` |
| `DATABASE_URL` | PostgreSQL connection string | Required |
| `REDIS_URL` | Redis connection string | `redis://localhost:6379` |
| `JWT_SECRET` | Secret for JWT signing | Required |
| `LOG_LEVEL` | Logging verbosity | `info` |

## Usage

### Create a Task

```bash
curl -X POST http://localhost:3000/api/tasks \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project proposal",
    "description": "Write and submit the Q4 project proposal",
    "dueDate": "2024-03-15",
    "priority": "high"
  }'
```

### List Tasks

```bash
curl http://localhost:3000/api/tasks \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Update a Task

```bash
curl -X PATCH http://localhost:3000/api/tasks/task_123 \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"status": "completed"}'
```

## Project Structure

```
taskflow/
├── src/
│   ├── controllers/    # Request handlers
│   ├── models/         # Database models
│   ├── services/       # Business logic
│   ├── middleware/     # Express middleware
│   └── utils/          # Helper functions
├── tests/              # Test suites
├── docs/               # Documentation
└── scripts/            # Utility scripts
```

## Testing

```bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run specific test file
npm test -- --grep "Task API"
```

## Contributing

We welcome contributions! Please read our [Contributing Guide](CONTRIBUTING.md) for details on:

- Code of conduct
- Development setup
- Pull request process
- Coding standards

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Express.js](https://expressjs.com/) - Web framework
- [Prisma](https://www.prisma.io/) - Database ORM
- [Socket.io](https://socket.io/) - Real-time engine

---

Made with ❤️ by the TaskFlow Team
