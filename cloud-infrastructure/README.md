# cloud-infrastructure

Infrastructure-as-code with Terraform and AWS CDK, cloud architecture patterns, cost optimisation, and multi-region deployment design.

## Overview

This plugin provides the `cloud-infrastructure` skill for Claude Code.

## Installation

Install via the SkillStack marketplace or copy this plugin directory into your Claude Code plugins folder.

## Usage

Invoke by describing your task naturally. The skill activates on relevant queries.

**Activates for:**
- Write Terraform to provision an RDS PostgreSQL instance with a read replica
- Design a multi-AZ VPC with public and private subnets for a 3-tier app
- Convert our Terraform S3 + CloudFront setup to AWS CDK TypeScript
- Our AWS bill doubled last month — what should we look at?

**Does NOT activate for:**
- Write a Kubernetes Deployment and Service for our FastAPI app (K8s application manifests — not infrastructure provisioning)
- Set up a GitHub Actions workflow for blue-green deploys (CI/CD pipeline — separate concern)
- Debug why our Docker container crashes on startup (App-layer debugging — not infra)

## Domain

**Engineering**

## Changelog

See [CHANGELOG.md](./CHANGELOG.md).
