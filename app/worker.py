from celery import Celery
from.ai_engine import analyze_log
from.models import LogEvent
import sqlalchemy

celery_app = Celery('worker', broker='redis://redis:6379/0')
engine = sqlalchemy.create_engine("postgresql://user:pass@db:5432/tracemind")

@celery_app.task
def process_log_task(service, message):
    similar = ["Connection timeout no Redis em 2024"]

    severity, ai_json, embedding = analyze_log(message, similar)

    print(f"Log de {service} analisado: {severity}")
    return ai_json