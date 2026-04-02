# marketing_helper_agents

Servizio multi-agente per il progetto marketing_helper.

## Obiettivo MVP

Il servizio espone un endpoint FastAPI `/agent/invoke` con orchestrazione LangGraph di base.
Per il modello LLM usa Ollama con `qwen3.5:2b`.

## Endpoint principali

- `GET /agent/health`
- `POST /agent/invoke`

Swagger disponibile su `http://localhost:8001/swagger` quando avviato con Docker Compose.

## Struttura

```text
app/
  main.py
  graph.py
  state.py
  agents/
  tools/
  core/
```

## Variabili ambiente

Vedi `.env.example`.

- `APP_NAME`
- `APP_ENV`
- `OLLAMA_URL`
- `OLLAMA_MODEL`
- `POSTGRES_URL`
- `REQUEST_TIMEOUT_SECONDS`

## Avvio locale (service only)

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
