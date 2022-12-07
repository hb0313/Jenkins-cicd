from pydantic import BaseModel


class MLModelNotFoundError(BaseModel):
    detail: str = "ML model not found"


class InvalidStringError(BaseModel):
    detail: str = "String is too long"
