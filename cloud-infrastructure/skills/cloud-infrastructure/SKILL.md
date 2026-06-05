---
name: cloud-infrastructure
description: >-
  Cloud infrastructure design and infrastructure-as-code (IaC) authoring. Use for Terraform module authoring, AWS CDK constructs, cloud architecture design (VPCs, load balancers, managed services, serverless), multi-region and disaster-recovery patterns, cost-optimisation analysis, and IaC code review. Trigger phrases: "write Terraform for", "design the AWS architecture", "set up a VPC", "convert this to CDK", "optimise our cloud costs". NOT for application-layer code — this skill models infrastructure, not the code running on it. NOT for Kubernetes application manifests (Deployments, Services, Ingress) — those belong in a k8s-specific skill. NOT for CI/CD pipeline configuration — that is a deployment concern separate from infrastructure provisioning.
allowed-tools: Read,Write,Edit,Bash
---

# cloud-infrastructure

Infrastructure-as-code with Terraform and AWS CDK, cloud architecture patterns, cost optimisation, and multi-region deployment design.

## When to use

- Write Terraform to provision an RDS PostgreSQL instance with a read replica
- Design a multi-AZ VPC with public and private subnets for a 3-tier app
- Convert our Terraform S3 + CloudFront setup to AWS CDK TypeScript
- Our AWS bill doubled last month — what should we look at?
- Design a disaster-recovery architecture with RPO < 1 hour across two regions
- Write a Terraform module for an EKS cluster with managed node groups
- Set up an IAM role with least-privilege access for a Lambda reading from S3
- Architect a serverless API: API Gateway + Lambda + DynamoDB

## When NOT to use

- Write a Kubernetes Deployment and Service for our FastAPI app — K8s application manifests — not infrastructure provisioning
- Set up a GitHub Actions workflow for blue-green deploys — CI/CD pipeline — separate concern
- Debug why our Docker container crashes on startup — App-layer debugging — not infra
- Write the FastAPI code for our API endpoint — Application code — not infrastructure

## Anti-patterns

### Symptom
Invoking this skill for tasks outside its scope — e.g., infrastructure concerns when the request is about application code, or vice versa.

### Problem
Scope mismatch wastes context and produces advice tuned for the wrong domain. A database schema skill answering a connection-pooling question gives schema advice when the real problem is operational configuration.

### Solution
Read the NOT for clauses carefully. If the request matches an exclusion, identify the correct skill (check SkillStack for the right domain) rather than stretching this skill to cover adjacent ground.
