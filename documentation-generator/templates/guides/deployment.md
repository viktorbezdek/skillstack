# Deployment Guide

How to deploy {{PROJECT_NAME}} to various environments.

## Deployment Checklist

Before deploying:

- [ ] All tests passing
- [ ] Environment variables configured
- [ ] Secrets securely stored
- [ ] Database migrations ready
- [ ] Monitoring configured
- [ ] Backup strategy in place
- [ ] Rollback plan documented

## Deployment Options

| Method | Best For | Complexity |
|--------|----------|------------|
| [Docker](#docker-deployment) | Most deployments | Low |
| [Kubernetes](#kubernetes) | Large-scale, high-availability | Medium |
| [Bare Metal](#bare-metal) | Full control, specific requirements | High |
| [Serverless](#serverless) | Event-driven, auto-scaling | Low |
| [PaaS](#platform-as-a-service) | Quick deployment, managed infra | Low |

## Docker Deployment

### Single Container

```bash
# Build the image
docker build -t {{PROJECT_NAME}}:{{VERSION}} .

# Run the container
docker run -d \
  --name {{PROJECT_NAME}} \
  --restart unless-stopped \
  -p {{PORT}}:{{CONTAINER_PORT}} \
  -v {{DATA_VOLUME}}:/data \
  -e {{ENV_PREFIX}}_DATABASE_URL="${DATABASE_URL}" \
  -e {{ENV_PREFIX}}_SECRET_KEY="${SECRET_KEY}" \
  {{PROJECT_NAME}}:{{VERSION}}
```

### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  {{PROJECT_NAME}}:
    image: {{DOCKER_IMAGE}}:{{VERSION}}
    restart: unless-stopped
    ports:
      - "{{PORT}}:{{CONTAINER_PORT}}"
    environment:
      - {{ENV_PREFIX}}_ENV=production
      - {{ENV_PREFIX}}_DATABASE_URL=${DATABASE_URL}
      - {{ENV_PREFIX}}_SECRET_KEY=${SECRET_KEY}
    volumes:
      - app-data:/data
      - ./config:/etc/{{PROJECT_NAME}}:ro
    depends_on:
      - db
      - redis
    healthcheck:
      test: ["CMD", "{{HEALTH_CHECK_CMD}}"]
      interval: 30s
      timeout: 10s
      retries: 3

  db:
    image: {{DATABASE_IMAGE}}
    restart: unless-stopped
    volumes:
      - db-data:/var/lib/{{DATABASE}}
    environment:
      - {{DB_ENV_VARS}}

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    volumes:
      - redis-data:/data

volumes:
  app-data:
  db-data:
  redis-data:
```

```bash
# Deploy
docker-compose up -d

# View logs
docker-compose logs -f {{PROJECT_NAME}}

# Update
docker-compose pull && docker-compose up -d
```

## Kubernetes

### Deployment Manifest

```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{PROJECT_NAME}}
  labels:
    app: {{PROJECT_NAME}}
spec:
  replicas: 3
  selector:
    matchLabels:
      app: {{PROJECT_NAME}}
  template:
    metadata:
      labels:
        app: {{PROJECT_NAME}}
    spec:
      containers:
        - name: {{PROJECT_NAME}}
          image: {{DOCKER_IMAGE}}:{{VERSION}}
          ports:
            - containerPort: {{CONTAINER_PORT}}
          env:
            - name: {{ENV_PREFIX}}_ENV
              value: production
            - name: {{ENV_PREFIX}}_DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: {{PROJECT_NAME}}-secrets
                  key: database-url
          resources:
            requests:
              memory: "{{MIN_MEMORY}}"
              cpu: "{{MIN_CPU}}"
            limits:
              memory: "{{MAX_MEMORY}}"
              cpu: "{{MAX_CPU}}"
          livenessProbe:
            httpGet:
              path: /health
              port: {{CONTAINER_PORT}}
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /ready
              port: {{CONTAINER_PORT}}
            initialDelaySeconds: 5
            periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: {{PROJECT_NAME}}
spec:
  selector:
    app: {{PROJECT_NAME}}
  ports:
    - port: 80
      targetPort: {{CONTAINER_PORT}}
  type: ClusterIP
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: {{PROJECT_NAME}}
  annotations:
    kubernetes.io/ingress.class: nginx
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  tls:
    - hosts:
        - {{DOMAIN}}
      secretName: {{PROJECT_NAME}}-tls
  rules:
    - host: {{DOMAIN}}
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: {{PROJECT_NAME}}
                port:
                  number: 80
```

### Helm Chart

```bash
# Install
helm install {{PROJECT_NAME}} ./charts/{{PROJECT_NAME}} \
  --namespace {{NAMESPACE}} \
  --set image.tag={{VERSION}} \
  --set replicas=3 \
  --values values.production.yaml

# Upgrade
helm upgrade {{PROJECT_NAME}} ./charts/{{PROJECT_NAME}} \
  --namespace {{NAMESPACE}} \
  --set image.tag={{NEW_VERSION}}

# Rollback
helm rollback {{PROJECT_NAME}} --namespace {{NAMESPACE}}
```

## Bare Metal

### System Service (systemd)

```ini
# /etc/systemd/system/{{PROJECT_NAME}}.service
[Unit]
Description={{PROJECT_NAME}}
After=network.target

[Service]
Type=simple
User={{SERVICE_USER}}
Group={{SERVICE_GROUP}}
WorkingDirectory={{INSTALL_DIR}}
ExecStart={{BINARY_PATH}} start
ExecReload=/bin/kill -HUP $MAINPID
Restart=always
RestartSec=5
Environment={{ENV_PREFIX}}_ENV=production
EnvironmentFile=/etc/{{PROJECT_NAME}}/environment

[Install]
WantedBy=multi-user.target
```

```bash
# Install and start
sudo systemctl daemon-reload
sudo systemctl enable {{PROJECT_NAME}}
sudo systemctl start {{PROJECT_NAME}}

# Check status
sudo systemctl status {{PROJECT_NAME}}

# View logs
sudo journalctl -u {{PROJECT_NAME}} -f
```

### Nginx Reverse Proxy

```nginx
# /etc/nginx/sites-available/{{PROJECT_NAME}}
upstream {{PROJECT_NAME}}_backend {
    server 127.0.0.1:{{PORT}};
    keepalive 64;
}

server {
    listen 80;
    server_name {{DOMAIN}};
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name {{DOMAIN}};

    ssl_certificate /etc/letsencrypt/live/{{DOMAIN}}/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/{{DOMAIN}}/privkey.pem;

    location / {
        proxy_pass http://{{PROJECT_NAME}}_backend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }
}
```

## Serverless

### AWS Lambda

```yaml
# serverless.yml
service: {{PROJECT_NAME}}

provider:
  name: aws
  runtime: {{RUNTIME}}
  region: ${opt:region, 'us-east-1'}
  environment:
    {{ENV_PREFIX}}_ENV: production
    {{ENV_PREFIX}}_DATABASE_URL: ${ssm:/{{PROJECT_NAME}}/database-url}

functions:
  api:
    handler: {{HANDLER}}
    events:
      - http:
          path: /{proxy+}
          method: ANY
    timeout: 30
    memorySize: 512
```

### Vercel

```json
// vercel.json
{
  "version": 2,
  "builds": [
    {
      "src": "{{ENTRY_POINT}}",
      "use": "{{VERCEL_BUILDER}}"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "{{ENTRY_POINT}}"
    }
  ],
  "env": {
    "{{ENV_PREFIX}}_ENV": "production"
  }
}
```

## Platform as a Service

### Heroku

```bash
# Create app
heroku create {{PROJECT_NAME}}

# Set config
heroku config:set {{ENV_PREFIX}}_ENV=production
heroku config:set {{ENV_PREFIX}}_DATABASE_URL="${DATABASE_URL}"

# Deploy
git push heroku main

# Scale
heroku ps:scale web=2
```

### Railway

```bash
# Install CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

### Render

```yaml
# render.yaml
services:
  - type: web
    name: {{PROJECT_NAME}}
    env: {{RUNTIME}}
    buildCommand: {{BUILD_COMMAND}}
    startCommand: {{START_COMMAND}}
    healthCheckPath: /health
    envVars:
      - key: {{ENV_PREFIX}}_ENV
        value: production
      - key: {{ENV_PREFIX}}_DATABASE_URL
        fromDatabase:
          name: {{PROJECT_NAME}}-db
          property: connectionString

databases:
  - name: {{PROJECT_NAME}}-db
    plan: starter
```

## Environment Configuration

### Production Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
{{#PROD_ENV_VARS}}
| `{{NAME}}` | {{REQUIRED}} | {{DESCRIPTION}} |
{{/PROD_ENV_VARS}}

### Secrets Management

**Recommended approaches:**

1. **Cloud provider secrets** - AWS Secrets Manager, GCP Secret Manager, Azure Key Vault
2. **HashiCorp Vault** - Self-hosted secret management
3. **Kubernetes Secrets** - Native K8s secret storage
4. **Environment files** - Only for development

**Never:**
- Commit secrets to version control
- Log sensitive data
- Use default/example credentials in production

## Database Migrations

```bash
# Run migrations before deployment
{{MIGRATE_COMMAND}}

# Verify migration status
{{MIGRATE_STATUS_COMMAND}}

# Rollback if needed
{{MIGRATE_ROLLBACK_COMMAND}}
```

## Health Checks

### Endpoints

| Endpoint | Purpose | Expected Response |
|----------|---------|-------------------|
| `/health` | Basic health check | `200 OK` |
| `/ready` | Readiness check | `200 OK` when ready |
| `/metrics` | Prometheus metrics | Metrics data |

### Health Check Configuration

```yaml
healthcheck:
  enabled: true
  path: /health
  interval: 30s
  timeout: 10s
  unhealthyThreshold: 3
```

## Monitoring & Logging

### Application Metrics

```yaml
# Prometheus scrape config
- job_name: '{{PROJECT_NAME}}'
  static_configs:
    - targets: ['{{HOST}}:{{METRICS_PORT}}']
```

### Log Aggregation

```yaml
# Fluentd/Fluent Bit config
[INPUT]
    Name forward
    Listen 0.0.0.0
    Port 24224

[OUTPUT]
    Name elasticsearch
    Match *
    Host {{ELASTICSEARCH_HOST}}
    Index {{PROJECT_NAME}}-logs
```

### Alerting

```yaml
# Prometheus alerting rules
groups:
  - name: {{PROJECT_NAME}}
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.1
        for: 5m
        labels:
          severity: critical
```

## Rollback Procedures

### Docker

```bash
# Roll back to previous image
docker-compose down
docker-compose pull {{PROJECT_NAME}}:{{PREVIOUS_VERSION}}
docker-compose up -d
```

### Kubernetes

```bash
# Roll back deployment
kubectl rollout undo deployment/{{PROJECT_NAME}}

# Roll back to specific revision
kubectl rollout undo deployment/{{PROJECT_NAME}} --to-revision=2
```

### Database

```bash
# Roll back database migration
{{MIGRATE_ROLLBACK_COMMAND}}
```

## Security Checklist

- [ ] TLS/HTTPS enabled
- [ ] Secrets not in environment variables (use secret manager)
- [ ] Firewall rules configured
- [ ] Rate limiting enabled
- [ ] CORS properly configured
- [ ] Security headers set
- [ ] Dependency vulnerabilities scanned
- [ ] Container running as non-root

## Troubleshooting

### Container Won't Start

1. Check logs: `docker logs {{PROJECT_NAME}}`
2. Verify environment variables
3. Check port availability
4. Verify dependencies are running

### Health Checks Failing

1. Check application logs
2. Verify database connectivity
3. Check resource limits (memory/CPU)
4. Verify network connectivity

### High Memory Usage

1. Check for memory leaks
2. Review resource limits
3. Scale horizontally instead of vertically
4. Enable garbage collection logging
