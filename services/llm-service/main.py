from fastapi import FastAPI
from pydantic import BaseModel
from llm_engine import process_text

app = FastAPI(title="LLM Service")

class TextRequest(BaseModel):
    text: str

@app.post("/intent")
def detect_intent(req: TextRequest):

    result = process_text(req.text)

    return result