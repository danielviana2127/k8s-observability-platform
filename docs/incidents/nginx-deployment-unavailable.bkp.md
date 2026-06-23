# Incident Report: Nginx Deployment Unavailable

## Incident Summary

This incident was intentionally simulated to validate the monitoring and alerting capabilities of the Kubernetes observability platform.

## Environment

- Kubernetes: Minikube
- Monitoring: Prometheus
- Visualization: Grafana
- Namespace: development
- Application: nginx-deployment

---

## Objective

Validate the following workflow:

Application Failure
→ Metrics Collection
→ Alert Generation
→ Incident Investigation
→ Service Recovery

---

## Incident Simulation

The deployment replicas were scaled to zero:

```bash
kubectl scale deployment nginx-deployment \
--replicas=0 \
-n development
```

### Expected Result

- Application unavailable
- Available replicas = 0
- Alert condition triggered

---

## Metrics Impacted

### Deployment Availability

```promql
kube_deployment_status_replicas_available
```

### Desired Replicas

```promql
kube_deployment_spec_replicas
```

---

## Alert Rule

Alert Name:

Deployment Unavailable

Condition:

Available Replicas < 1

Evaluation Interval:

1 minute

---

## Detection Flow

1. Deployment scaled to zero replicas.
2. Kubernetes updated cluster state.
3. Prometheus collected updated metrics.
4. Grafana evaluated alert rule.
5. Alert entered FIRING state.
6. DevOps engineer investigated incident.

---

## Resolution

Deployment restored:

```bash
kubectl scale deployment nginx-deployment \
--replicas=2 \
-n development
```

### Result

- Pods recreated successfully.
- Metrics returned to normal values.
- Alert returned to Normal state.

---

## Lessons Learned

- Monitoring pipeline validated successfully.
- Alerting workflow validated successfully.
- Dashboard metrics reflected real cluster state.
- Incident response process documented.

---

## Architecture Diagrams

### Platform Architecture

docs/architecture/platform-architecture.png

### Incident Flow

docs/architecture/incident-alert-flow.png