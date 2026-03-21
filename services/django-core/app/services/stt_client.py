import requests

STT_URL = "http://stt-service:8001/transcribe"

async def transcribe(file):

    files = {"file": (file.filename, await file.read())}

    r = requests.post(STT_URL, files=files)

    return r.json()["text"]