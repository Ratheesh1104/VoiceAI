from fastapi import FastAPI, UploadFile, File
import tempfile
from whisper_engine import transcribe

app = FastAPI(title="STT Service")

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        content = await file.read()
        tmp.write(content)

        text = transcribe(tmp.name)

    return {"text": text}