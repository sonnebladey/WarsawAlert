from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 

DATABASE_URL = "postgresql+psycopg://localhost:5432/warsaw_alert"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine) #bind craeted sessions with Engine

def get_db():
    with SessionLocal() as session: 
        yield session 