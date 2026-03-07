from enum import enum

class Service(str, Enum):
    STT = "stt-service"
    TTS = "tts-service"
    LLM = "llm-request"
    ACTION = "action-service"