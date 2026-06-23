# Incident Report: Nginx Deployment Unavailable

## Severity

SEV-3 (Simulated Incident)

---

## Summary

A simulated incident was triggered by scaling the `nginx-deployment` to zero replicas in order to validate the Kubernetes observability stack, including Prometheus alerting, Grafana dashboards, and Alertmanager notifications.

---

## Environment

- Kubernetes: Minikube
- Namespace: development
- Monitoring Stack: Prometheus, Grafana, Alertmanager
- Application: nginx-deployment

---

## Impact

- Application became unavailable
- Deployment replicas dropped to 0
- No external users impacted (lab environment)

---

## Timeline

| Time | Event |
|------|------|
| T0 | Deployment scaled to 0 replicas |
| T+1m | Prometheus detected zero replicas |
| T+2m | Alert transitioned to FIRING state |
| T+3m | Incident investigated |
| T+4m | Deployment restored |

---

## Root Cause

The incident was intentionally triggered by manually scaling the deployment to zero replicas:

```bash
kubectl scale deployment nginx-deployment \
--replicas=0 \
-n development