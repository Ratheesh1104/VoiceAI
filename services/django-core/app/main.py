from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Voice AI Orchestrator")

app.include_router(router)