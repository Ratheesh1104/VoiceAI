from pydantic import BaseModel
from typing import Optional

class AudioRequest(BaseModel):
    session_id: str
    audio_base64: str


class STTResponse(BaseModel):
    session_id: str
    text: str


class LLMRequest(BaseModel):
    session_id: str
    text: str


class LLMResponse(BaseModel):
    session_id: str
    response: str


class TTSRequest(BaseModel):
    session_id: str
    text: str


class TTSResponse(BaseModel):
    session_id: str
    audio_base64: str


class ActionRequest(BaseModel):
    session_id: str
    action_name: str
    parameters: Optional[dict]