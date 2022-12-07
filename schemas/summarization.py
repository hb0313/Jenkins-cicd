import pydantic


class AnswerOut(pydantic.BaseModel):
    answer: str
