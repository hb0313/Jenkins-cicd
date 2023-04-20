from typing import Any

import fastapi

from schemas.documentation import DocumentationOut

router = fastapi.APIRouter()


@router.get("/documentation", response_model=DocumentationOut)
def get_doc() -> dict[str, Any]:
    docs: dict[str, Any] = {
        "model_name": "audio_speech_to_text_silero",
        "short_desc": "Silero Speech-To-Text models are designed to provide enterprise-grade STT that is robust to various audio factors and supports multiple commonly spoken languages, with a decoder utility provided for ease of use.",
        "ideal": "ideal for a wide range of use cases that require accurate transcription of spoken language, particularly in noisy or diverse audio environments.",
        "not_ideal": "may not be ideal for use cases where the audio is not normalized or resampled to 16kHz",
        "input_args": [
            {
                "example1": "audio file in a normalized format with a 16kHz sampling rate"
            },
            {"example2": ".wav"},
        ],
        "output_args": [
            {"example1": ".mp3"},
            {"example2": "text string of audio speech"},
        ],
    }
    return docs
