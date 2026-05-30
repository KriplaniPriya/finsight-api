from app.core.database import create_db_and_tables
from fastapi import FastAPI
from app.models.model import User 

app = FastAPI(
    title= "Finsight API",
    description= "An API for financial insights and data analysis",
    version= "1.0.0"
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/health")
def health():
    return {"status":"ok"}