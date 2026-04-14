Smart Monitoring API

API para monitoramento de serviços HTTP com arquitetura distribuída.

* Arquitetura
    Flask (API REST)
    PostgreSQL (persistência)
    Redis (fila/mensageria)
    Celery (processamento assíncrono)
    Docker (containerização)
* Funcionalidades
    Cadastro de serviços
    Health check automático
    Monitoramento de disponibilidade
    Medição de tempo de resposta
    Histórico de execução
* Arquitetura
    Client → Flask API → PostgreSQL
               ↓
             Redis → Celery Worker

* Como rodar
    docker compose up --build

* Endpoints
    Criar serviço
        POST /services

    Listar serviços
        GET /services

    Métricas
        GET /metrics

