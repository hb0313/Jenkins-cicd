import pydantic


class InvalidMediaError(pydantic.BaseModel):
    detail: str = "Media not supported"


class MLModelNotFoundError(pydantic.BaseModel):
    detail: str = "ML model not found"
