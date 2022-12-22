from typing import List, Union

import fastapi
import nemo.collections.nlp as nemo_nlp

import schemas

model = nemo_nlp.models.machine_translation.MTEncDecModel.from_pretrained(
    model_name="nmt_ru_en_transformer24x6"
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
) -> List[dict[str, Union[str, float]]]:
    """
    Use this API for text translation from German to English

    How to use:
    1. Click try it.
    2. Input the sentence
    3. Click execute
    4. Response will be a JSON with answer.
    """

    if model is None:
        raise fastapi.HTTPException(500, "ML model not found")

    try:
        result = model.translate(text=sentence, source_lang="de", target_lang="en")
    except ValueError:
        raise fastapi.HTTPException(
            status_code=404, detail="ERROR: Unable to classify string"
        )

    return [
        {
            "answer": result,
        }
    ]
