from app.ai_engine import analyze_log

severity, result, _ = analyze_log(
    "ERROR 500: psycopg2.OperationalError: could not connect to server",
    []
)
print(f"Severidade: {severity}")
print(f"Resultado IA: {result}")