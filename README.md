# 🚀 Kubernetes Platform Project

Projeto completo de aplicação containerizada rodando em Kubernetes com PostgreSQL interno, FastAPI, HPA, Ingress e organização profissional utilizando Kustomize.

---

# 📌 Visão Geral

Este projeto demonstra a construção de uma aplicação moderna baseada em microsserviços utilizando:

* ✅ FastAPI (API REST)
* ✅ PostgreSQL rodando dentro do cluster
* ✅ Kubernetes (Deployments, Services, HPA, Ingress)
* ✅ ConfigMap e Secret
* ✅ Resource Limits
* ✅ Liveness e Readiness Probes
* ✅ Estrutura organizada com Kustomize (base + overlays)

O objetivo é simular um ambiente próximo ao utilizado em empresas.

---

# 🏗️ Arquitetura do Projeto

```
k8s-platform-project/
│
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── k8s/
│   ├── base/
│   │   ├── namespace.yaml
│   │   ├── configmap.yaml
│   │   ├── secret.yaml
│   │   ├── postgres-deployment.yaml
│   │   ├── postgres-service.yaml
│   │   ├── app-deployment.yaml
│   │   ├── app-service.yaml
│   │   ├── ingress.yaml
│   │   ├── hpa.yaml
│   │   └── kustomization.yaml
│   │
│   └── overlays/
│       └── dev/
│           └── kustomization.yaml
│
└── README.md
```

---

# 🧱 Componentes Kubernetes

## Namespace

Ambiente isolado chamado `platform-dev`.

## PostgreSQL

* Deployment com 1 réplica
* Service ClusterIP interno
* Credenciais configuradas via variáveis de ambiente

## Aplicação FastAPI

* Deployment com 2 réplicas
* Resource Requests e Limits
* Liveness Probe
* Readiness Probe
* Variáveis injetadas via ConfigMap e Secret

## Service

* Tipo ClusterIP
* Comunicação interna no cluster

## Ingress

* Roteamento HTTP via host `platform.local`

## HPA

* Escala automática baseada em uso de CPU
* Mínimo: 2 réplicas
* Máximo: 5 réplicas

---

# ⚙️ Pré-Requisitos

* Docker instalado
* Kubernetes (Minikube recomendado)
* kubectl configurado

Se estiver usando Minikube:

```bash
minikube start
minikube addons enable ingress
minikube addons enable metrics-server
```

---

# 🐳 Build da Imagem

Entre na pasta do projeto:

```bash
cd k8s-platform-project
```

Build da imagem:

```bash
docker build -t SEU_DOCKERHUB/platform-app:latest ./app
```

Push para o Docker Hub:

```bash
docker push SEU_DOCKERHUB/platform-app:latest
```

⚠️ Importante: Atualize o arquivo `k8s/base/app-deployment.yaml` com seu usuário do Docker Hub.

---

# 🚀 Deploy no Kubernetes

Aplicar via Kustomize:

```bash
kubectl apply -k k8s/overlays/dev
```

---

# 🔍 Verificação

Listar pods:

```bash
kubectl get pods -n platform-dev
```

Listar services:

```bash
kubectl get svc -n platform-dev
```

Listar ingress:

```bash
kubectl get ingress -n platform-dev
```

---

# 🌐 Acessando a Aplicação

## Opção 1 — Port Forward (Mais simples)

```bash
kubectl port-forward svc/platform-service 8080:80 -n platform-dev
```

Acesse:

```
http://localhost:8080
```

Endpoints disponíveis:

* `/` → Mensagem principal
* `/health` → Health check
* `/db-check` → Teste de conexão com PostgreSQL

---

## Opção 2 — Ingress (Minikube)

Obter IP:

```bash
minikube ip
```

Adicionar no arquivo hosts:

```
IP_DO_MINIKUBE platform.local
```

Acessar:

```
http://platform.local
```

---

# 🧪 Testando o HPA

Gerar carga manual ou utilizar ferramentas como hey ou ab.

Verificar escalonamento:

```bash
kubectl get hpa -n platform-dev
```

---

# 🛠️ Debug

Ver logs de um pod:

```bash
kubectl logs NOME_DO_POD -n platform-dev
```

Descrever pod:

```bash
kubectl describe pod NOME_DO_POD -n platform-dev
```

---

# 📈 Próximos Passos

* Migrar PostgreSQL para StatefulSet + PVC
* Converter projeto para Helm
* Implementar CI com GitHub Actions
* Evoluir para GitOps com ArgoCD
* Adicionar Observabilidade (Prometheus + Grafana)

---

# 👨‍💻 Autor

**Daniel Viana**
📧 Email: [daniel-viana2127@yahoo.com](mailto:daniel-viana2127@yahoo.com)
🔗 GitHub: [https://github.com/danielviana2127](https://github.com/danielviana2127)
