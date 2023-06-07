import pydantic


class PredictionOut(pydantic.BaseModel):
    label: str
    model: str
