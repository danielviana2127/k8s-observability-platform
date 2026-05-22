# 🚀 Kubernetes Observability Platform

Projeto completo de observabilidade utilizando Kubernetes, Prometheus, Grafana e Alertmanager, com deploy estruturado via Kustomize.

---
## 🧪 Projeto 100% Funcional

Este projeto foi testado localmente com Minikube e demonstra:

- Coleta de métricas com Prometheus
- Visualização de métricas com Grafana
- Sistema de alertas utilizando Alertmanager
- Deploy declarativo utilizando Kustomize
- Pipeline CI/CD utilizando GitHub Actions
- Troubleshooting e debugging em Kubernetes

---
## 📌 Visão Geral

Este projeto demonstra a construção de uma plataforma completa de observabilidade para aplicações Kubernetes, seguindo práticas modernas utilizadas em ambientes cloud-native e DevOps.

A aplicação Flask expõe métricas customizadas via Prometheus Client, permitindo monitoramento, criação de dashboards e geração de alertas automatizados.

---

## 🧱 Arquitetura

```
User → Flask Application
           ↓
Prometheus → Métricas
           ↓
Grafana → Dashboards
           ↓
Alertmanager → Alertas por Email
```

---

## ⚙️ Tecnologias Utilizadas

* Python (Flask)
* Prometheus Client
* Kubernetes
* Kustomize
* Prometheus Operator (kube-prometheus-stack)
* Grafana
* Alertmanager
* Docker
* GitHub Actions
* Minikube

---

## 📦 Estrutura do Projeto

```
k8s-observability-platform/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── k8s/
│   ├── alertmanager-config.yaml
│   ├── base/
│   │   ├── app-deployment.yaml
│   │   ├── app-service.yaml
│   │   ├── namespace.yaml
│   │   ├── service-monitor.yaml
│   │   ├── prometheus-rule.yaml
│   │   └── kustomization.yaml
│   │
│   └── overlays/
│       └── dev/
│           └── kustomization.yaml
│
├── docs/
│   └── architecture.md
│
└── README.md
```

---

## 📊 Métricas Coletadas

As seguintes métricas são coletadas pela aplicação:

* `app_requests_total`
* `process_cpu_seconds_total`
* `process_resident_memory_bytes`

---

## 📈 Dashboard (Grafana)

### Taxa de Requisições

```promql
sum(rate(app_requests_total[1m]))
```

### Total de Requisições

```promql
sum(app_requests_total)
```

### Requisições por Endpoint

```promql
sum by (endpoint) (rate(app_requests_total[1m]))
```

---

## 🚨 Alertas Configurados

### 🔸 NoRequests

Dispara quando a aplicação não recebe requisições:

```promql
sum(rate(app_requests_total[2m])) == 0
```

---

### 🔸 HighRequestRate

Dispara quando há alta taxa de requisições:

```promql
sum(rate(app_requests_total[1m])) > 5
```

---

## 🔔 Sistema de Notificações

Alertas enviados utilizando:

* Alertmanager
* SMTP Gmail

---

## 🔄 CI/CD Pipeline

O Projeto possui pipeline automatizada utilizando GitHub Actions.

Validações executadas

* Checkout do código
* Build da imagem Docker
* Validação de manifests Kubernetes
* Validação Kustomize

---

## 🛠️ Deploy com Kustomize

### Aplicar toda infraestrutura

```bash
kubectl apply -k k8s/overlays/dev
```

---

## ▶️ Acessos Locais

### Aplicação

```bash
kubectl port-forward svc/platform-service -n platform-dev 8080:80
```

---

### Prometheus

```bash
kubectl port-forward svc/monitoring-kube-prometheus-prometheus -n monitoring 9090:9090
```

---

### Grafana

```bash
kubectl port-forward svc/monitoring-grafana -n monitoring 3000:80
```

---

### Alertmanager

```bash
kubectl port-forward svc/monitoring-kube-prometheus-alertmanager -n monitoring 9093:9093
```

---

## 🧪 Testes

### Gerar carga na aplicação

```bash
for i in {1..200}; do curl http://localhost:8080/; done
```

---

## 🛠️ Troubleshooting Realizado

Durante o desenvolvimento deste projeto foram realizados diversos diagnósticos e troubleshooting em Kubernetes:

* CrashLoopBackOff em containers
* Ajuste de readiness/liveness probes
* Diagnóstico utilizando kubectl logs
* Diagnóstico utilizando kubectl describe
* Troubleshooting de recursos no Minikube
* Debugging de deployments Kubernetes

---

# 📚 Lessons Learned

Principais conhecimentos adquiridos durante o projeto:

* Observabilidade em Kubernetes
* Monitoramento com Prometheus
* Dashboards com Grafana
* Gerenciamento de alertas
* Deploy declarativo com Kustomize
* Automação CI/CD
* Troubleshooting Kubernetes
* Kubernetes probes
* Containers e Docker
* Debugging de infraestrutura

---

## 🎯 Objetivo

Demonstrar conhecimento prático em:

* Observabilidade
* Monitoramento
* Alertas
* Kubernetes
* Kustomize
* DevOps
* SRE
* CI/CD
* Troubleshooting

---

## 📸 Evidências

### Prometheus Targets
![Prometheus Targets](docs/images/prometheus-targets.png)

### Prometheus Query
![Prometheus Query](docs/images/prometheus-query.png)

### Prometheus Alerts
![Prometheus Alerts](docs/images/prometheus-alerts.png)

### Grafana Dashboard
![Grafana](docs/images/grafana-dashboard.png)

### Kubernetes Pods
![Pods](docs/images/kubectl-pods.png)

### Services & Endpoints
![Services](docs/images/k8s-services.png)

---

## 👨‍💻 Autor

Daniel Viana

