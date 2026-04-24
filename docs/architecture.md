# Architecture

This project follows a simple observability pipeline:

User → Service → Pod → Metrics → Prometheus

## Components

- Flask App (instrumented with Prometheus)
- Kubernetes Deployment
- Kubernetes Service
- ServiceMonitor (Prometheus Operator)
- Prometheus

## Flow

1. User hits the application
2. Request counter is incremented
3. Metrics exposed at /metrics
4. Prometheus scrapes metrics via ServiceMonitor