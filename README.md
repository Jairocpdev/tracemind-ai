# TraceMind AI 🧠

API que transforma log de erro em diagnóstico automático com IA local, sem pagar OpenAI.

## Demo
```json
POST /ingest
{
  "service": "api",
  "message": "ERROR 500 psycopg2.OperationalError could not connect"
}

Response 200:
{
  "severity": "CRITICAL",
  "ai_analysis": "Erro de conexão com banco",
  "solution": "Verifique DATABASE_URL",
  "embedding_size": 384,
  "mode": "HEAVY"
}