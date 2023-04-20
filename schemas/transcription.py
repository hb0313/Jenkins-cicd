from pydantic import BaseModel


class PredictionOut(BaseModel):
    text: str
