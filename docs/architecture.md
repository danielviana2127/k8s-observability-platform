# Arquitetura

A aplicação segue o fluxo:

Usuário → Service → Pod → /metrics → Prometheus → Grafana

## Componentes

- Flask App: expõe métricas
- Kubernetes Service: expõe aplicação
- ServiceMonitor: integra com Prometheus
- Prometheus: coleta métricas
- Grafana: visualiza métricas