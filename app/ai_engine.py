from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

load_dotenv()

model = SentenceTransformer('all-MiniLM-L6-v2')

KNOWLEDGE_BASE = {
    "postgres": {"cause": "Banco Postgres fora do ar", "solution": "Verifique docker-compose ps e reinicie o serviço db"},
    "redis": {"cause": "Falha de conexão no Redis", "solution": "Cheque se o container redis está rodando e a porta 6379"},
    "timeout": {"cause": "Timeout de conexão", "solution": "Aumente o timeout ou verifique latência de rede"},
    "500": {"cause": "Erro interno no servidor", "solution": "Verifique logs da API em /logs"},
}

def analyze_log(raw_log: str, similar_logs: list):
    embedding = model.encode(raw_log)
    
    severity = "CRITICAL" if any(x in raw_log.lower() for x in ["500", "exception", "error", "failed"]) else "WARNING"
    
    log_lower = raw_log.lower()
    root_cause = "Causa desconhecida - log novo"
    solution = "Adicionar este padrão à base de conhecimento"
    
    for keyword, info in KNOWLEDGE_BASE.items():
        if keyword in log_lower:
            root_cause = info["cause"]
            solution = info["solution"]
            break
    
    result = f'{{"root_cause": "{root_cause}", "solution": "{solution}"}}'
    
    return severity, result, embedding