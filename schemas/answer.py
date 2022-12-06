import pydantic


class AnswerOut(pydantic.BaseModel):
    description: str
    probability: float
