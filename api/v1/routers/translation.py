import base64
import os
from typing import List, Union

import fastapi
import schemas
import soundfile as sf
import torch
from nemo.collections.tts.models import HifiGanModel, Tacotron2Model

spec_generator = Tacotron2Model.from_pretrained("tts_en_tacotron2")
vocoder = HifiGanModel.from_pretrained(model_name="tts_hifigan")

FILE = "audio.wav"

router = fastapi.APIRouter()


@router.post(
    "/transalte",
    response_model=List[schemas.AnswerOut],
    responses={
        400: {"model": schemas.InvalidStringError},
        500: {"model": schemas.MLModelNotFoundError},
    },
)
async def transcription(
    text: str = fastapi.Body(...),
) -> List[dict[str, Union[str, float]]]:
    """
    Use this API for text to speech

    How to use:
    1. Click try it.
    2. Input the sentence
    3. Click execute
    4. Response will be a JSON.

    JSON Formate:

    {
        "content": base64 audio encoded string,
        "sampleRate": 22050 ,
        "encoding": "WAV",
        "languageCode": "English",
    }


    """

    if spec_generator is None:
        raise fastapi.HTTPException(500, "ML model not found")

    try:
        with torch.no_grad():
            parsed = spec_generator.parse(text)
            spectrogram = spec_generator.generate_spectrogram(tokens=parsed)
            audio = vocoder.convert_spectrogram_to_audio(spec=spectrogram)

            if isinstance(audio, torch.Tensor):
                audio = audio.to("cpu").numpy()
            sf.write("audio.wav", audio.T, 22050, format="WAV")

            with open(FILE, "rb") as f:
                audio_encoded = base64.b64encode(f.read())

    except ValueError:
        raise fastapi.HTTPException(
            status_code=404, detail="ERROR: Unable to detect transcript in audio"
        )
    finally:
        os.remove(f"{FILE}")

    return [
        {
            "content": str(audio_encoded),
            "sampleRate": 22050,
            "encoding": "WAV",
            "languageCode": "English",
        }
    ]
