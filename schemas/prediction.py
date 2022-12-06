import pydantic


class QuestionContextIn(pydantic.BaseModel):
    question: str = pydantic.Field(..., example="Where do i live")
    context: str = pydantic.Field(
        ..., example="My name is Wolfgang and I live in Berlin"
    )


class PredictionOut(pydantic.BaseModel):
    answer: str = pydantic.Field(..., example="Celeration")
    score: float = pydantic.Field(..., example=0.9999)

    @pydantic.validator("score")
    def round_probability(cls, v: float) -> float:
        return round(v, 10)
