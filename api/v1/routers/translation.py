from typing import List, Union

import fastapi
import nemo.collections.asr as nemo_asr
import schemas

model = nemo_asr.models.EncDecCTCModel.from_pretrained(
    model_name="stt_fr_quartznet15x5"
)

FILE = "audio.wav"

router = fastapi.APIRouter()


@router.post(
    "/classify",
    response_model=List[schemas.AnswerOut],
    responses={
        400: {"model": schemas.InvalidStringError},
        500: {"model": schemas.MLModelNotFoundError},
    },
)
async def transcription(
    file: bytes = fastapi.File(...),
) -> List[dict[str, Union[str, float]]]:
    """
    Use this API for text to speech

    How to use:
    1. Click try it.
    2. Input the sentence
    3. Click execute
    4. Response will be a JSON with answer.
    """

    if model is None:
        raise fastapi.HTTPException(500, "ML model not found")

    with open(FILE, "wb") as f:
        f.write(file)

    try:
        text = model.transcribe(["audio.wav"])
    except ValueError:
        raise fastapi.HTTPException(
            status_code=404, detail="ERROR: Unable to detect transcript in audio"
        )

    return [
        {
            "answer": text[0],
        }
    ]
