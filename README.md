# Kubernetes Observability Project

## 📌 Overview

This project demonstrates a complete observability pipeline using:

- Python (Flask)
- Kubernetes
- Prometheus
- ServiceMonitor (Prometheus Operator)

## 🧱 Architecture

App → Service → ServiceMonitor → Prometheus


## 🚀 Running locally

```bash
minikube start

eval $(minikube docker-env)
docker build -t platform-app ./app

kubectl apply -f k8s/

📊 Metrics
app_requests_total
🧠 Key Learnings
Kubernetes service discovery
Prometheus scraping
Debugging metrics exposure issues
Observability fundamentals

---

# 🔍 PASSO 9 — TESTE FINAL (RÁPIDO)

Depois da refatoração:

```bash
docker build -t platform-app ./app
kubectl rollout restart deployment platform-app -n platform-dev