from typing import List, Union

import fastapi
from transformers import pipeline

import schemas

classifier = pipeline(
    "zero-shot-classification", model="typeform/distilbert-base-uncased-mnli"
)

router = fastapi.APIRouter()


@router.post(
    "/classify",
    response_model=List[schemas.AnswerOut],
    responses={
        400: {"model": schemas.InvalidStringError},
        500: {"model": schemas.MLModelNotFoundError},
    },
)
async def classification(
    sentence: str = fastapi.Body(default=None, embed=True),
    label: List[str] = fastapi.Body(default=None, embed=True),
) -> List[dict[str, Union[str, float]]]:
    """
    Use this API for zero shot text classification

    How to use:
    1. Click try it.
    2. Input the sentence
    3. Click execute
    4. Response will be a JSON with answer.
    """

    if classifier is None:
        raise fastapi.HTTPException(500, "ML model not found")

    try:
        labels = label[0].split(",")
        res = classifier(sentence, labels, multi_class=True)
        # print(res)
        predictions: list[dict[str, Union[str, float]]] = [
            {
                "label": res["labels"][i],
                "score": res["scores"][i],
            }
            for i in range(len(labels))
        ]
    except ValueError:
        raise fastapi.HTTPException(
            status_code=404, detail="ERROR: Unable to classify string"
        )

    return predictions
