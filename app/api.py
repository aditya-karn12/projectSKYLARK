from fastapi import FastAPI
from pydantic import BaseModel

from app import get_insight_engine, get_source_status

app = FastAPI(title="Skylark Drones BI Agent", version="1.0.0")
engine = get_insight_engine()


class QueryRequest(BaseModel):
    question: str


@app.get("/api/health")
def health():
    return {"status": "ok", "service": "Skylark Drones BI Agent"}


@app.get("/api/source-status")
def source_status():
    return get_source_status()


@app.get("/api/requirements")
def requirements():
    return {
        "compliance": get_source_status()["requirements_status"],
        "note": "This project is locally validated and deploy-ready; live Monday.com integration activates only when valid API credentials and board IDs are provided.",
    }


@app.get("/api/metrics")
def metrics():
    return engine.get_kpis()


@app.post("/api/query")
def query(req: QueryRequest):
    return engine.answer_query(req.question)


@app.get("/api/summary")
def summary():
    return engine.get_leadership_summary()
