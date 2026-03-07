import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    REDIS_URL: os.getenv("REDIS_URL", "")
    POSTGRES_USER: os.getenv("POSTGRES_USER", "voice")
    POSTGRES_PASSWORD: os.getenv("POSTGRES_PASSWORD", "voice")
    POSTGRES_DB: os.getenv("POSTGRES_DB", "voice_ai")
    POSTGRES_HOST: os.getenv("POSTGRES_HOST", "localhost")


    OOLLAMA_URL: os.getenv("OOLLAMA_URL", "http://ollama:11434")

Settings = Settings()
