from typing import Union

import fastapi

import schemas
from core.config import roberta

router = fastapi.APIRouter()


def check_if_model_exist() -> None:
    if roberta.get_model() is None:
        raise fastapi.HTTPException(500, "ML model not found")


@router.post(
    "/qa",
    response_model=list[schemas.PredictionOut],
    responses={
        400: {"model": schemas.InvalidStringError},
        500: {"model": schemas.MLModelNotFoundError},
    },
    dependencies=[fastapi.Depends(check_if_model_exist)],
)
async def question_answering(
    query: schemas.QuestionContextIn = fastapi.Body(default=None),
) -> list[dict[str, Union[str, float]]]:
    """
    Use this API for question-answering
    """
    score, answer = roberta.predict_qa(query.question, query.context)

    predictions: list[dict[str, Union[str, float]]] = [
        {"answer": answer, "score": score}
    ]
    return predictions
