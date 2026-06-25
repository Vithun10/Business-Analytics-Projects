from fastapi import FastAPI
import os 

from app.database import engine
from app.models.db_models import Base
from app.routers.transactions import router as transaction_router
from fastapi.middleware.cors import CORSMiddleware

from app.routers.audit import (
    router as audit_router
)

from app.routers.dashboard import (
    router as dashboard_router
)

from app.routers.scoring import (
    router as scoring_router
)

from app.routers.model_performance import (
    router as model_performance_router
)

from app.routers.trends import (
    router as trends_router
)

from app.routers.uploads import (
    router as uploads_router
)

from app.routers.explainability import (
    router as explainability_router
)

from app.routers.ai_analyst import (
    router as ai_analyst_router
)

from app.routers.reports import (
    router as reports_router
)

from app.routers.research import (
    router as research_router
)

from app.routers.simulator import (
    router as simulator_router
)

from app.routers.alerts import (
    router as alerts_router
)

from app.routers.shap import (
    router as shap_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="VERIS",
    version="1.0.0"
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

frontend_url = os.getenv("FRONTEND_URL")

if frontend_url:
    origins.append(frontend_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    transaction_router,
    prefix="/api/v1"
)

app.include_router(
    audit_router,
    prefix="/api/v1"
)

app.include_router(
    dashboard_router,
    prefix="/api/v1"
)

app.include_router(
    scoring_router,
    prefix="/api/v1"
)

app.include_router(
    model_performance_router,
    prefix="/api/v1"
)

app.include_router(
    trends_router,
    prefix="/api/v1"
)

app.include_router(
    uploads_router,
    prefix="/api/v1"
)

app.include_router(
    explainability_router,
    prefix="/api/v1"
)

app.include_router(
    ai_analyst_router,
    prefix="/api/v1"
)

app.include_router(
    reports_router,
    prefix="/api/v1"
)

app.include_router(
    research_router,
    prefix="/api/v1"
)

app.include_router(
    simulator_router,
    prefix="/api/v1"
)

app.include_router(
    alerts_router,
    prefix="/api/v1"
)

app.include_router(
    shap_router,
    prefix="/api/v1"
)

@app.get("/")
def root():
    return {
        "application": "VERIS",
        "status": "running"
    }

