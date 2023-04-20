from pydantic import BaseModel


class MLModelNotFoundError(BaseModel):
    detail: str = "ML model not found"


class InvalidAudioError(BaseModel):
    detail: str = "Audio is too long"
