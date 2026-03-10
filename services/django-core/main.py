from fastAPI import FastAPI
from app.api.routes import routes

app = FastAPI(title= "Voice AI Orchestrator")

app.include_router(routes)