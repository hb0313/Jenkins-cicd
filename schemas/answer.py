import pydantic


class AnswerOut(pydantic.BaseModel):
    label: str
    score: float = pydantic.Field(..., example=0.9999)

    @pydantic.validator("score")
    def round_probability(cls, v: float) -> float:
        return round(v, 4)
