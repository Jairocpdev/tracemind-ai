from fastapi import FastAPI
from pydantic import BaseModel
from app.ai_engine import analyze_log

app = FastAPI(title="TraceMind AI - Local Mode")

class LogInput(BaseModel):
    service: str
    message: str

@app.get("/")
def root():
    return {"status": "TraceMind rodando!", "docs": "/docs"}

@app.post("/ingest")
def ingest_log(log: LogInput):
    severity, result, embedding = analyze_log(log.message, [])
    return {
        "service": log.service,
        "severity": severity,
        "ai_analysis": result,
        "embedding_size": len(embedding)
    }