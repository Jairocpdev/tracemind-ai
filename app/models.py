from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base() 

class LogEvent(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True) 
    raw_log = Column(String) 
    severity = Column(String)
    root_cause = Column(String)
    solution = Column(String)
    similarity_score = Column(Float) 
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

