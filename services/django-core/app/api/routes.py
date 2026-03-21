from fastapi import APIRouter, UploadFile, File
from app.pipeline.voice_pipeline import process_voice 

router = APIRouter()

@router.post("/voice")
async def voice_command(file: UploadFile = File(...)):
    result = await process_voice(file)
    return result