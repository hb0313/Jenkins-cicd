from fastapi import APIRouter, Depends, File, HTTPException

from core.config import silero
from schemas import error as e
from schemas import transcription as p

router = APIRouter()


def check_if_model_exists() -> None:
    if silero.get_model() is None:
        raise HTTPException(500, "ML model not found")


@router.post(
    "/convert",
    response_model=p.PredictionOut,
    responses={
        400: {"model": e.InvalidAudioError},
        500: {"model": e.MLModelNotFoundError},
    },
    dependencies=[Depends(check_if_model_exists)],
)
async def speech_to_text(audio_file: bytes = File(...)) -> dict[str, str]:

    """
    Use this API for Speech To Text translation .
    How to use:
    1. Input an audio file
    2. Click execute
    3. Json Output will be generated with the text
    """

    prediction: str = silero.predict(audio_file)
    return {"text": prediction}
