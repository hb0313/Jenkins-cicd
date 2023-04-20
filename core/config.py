import os
from glob import glob
from typing import Any

import torch
from fastapi import HTTPException
from pydantic import BaseSettings


class SileroModel:
    def __init__(self) -> None:
        self._model: Any = None
        self._model_name: str = "silero_tts"
        self._decoder: Any
        self._utils: Any
        self._device: Any

    def initialize_model(self) -> None:
        self._device = torch.device("cpu")
        self._model, self._decoder, self._utils = torch.hub.load(
            repo_or_dir="snakers4/silero-models",
            model="silero_stt",
            language="en",
            device=self._device,
        )

    def _save_audio(self, audio_file: bytes) -> None:
        with open("saved_audio.wav", "wb") as f:
            f.write(audio_file)

    def _remove_audio_files(self) -> None:
        """
        Search for all .png files and delete them
        """
        for f in glob("*.wav"):
            if os.path.exists(f):
                os.remove(f)

    def get_model(self) -> Any:
        return self._model

    def predict(self, audio_file: bytes) -> str:
        try:
            self._remove_audio_files()
            self._save_audio(audio_file)
            (read_batch, split_into_batches, _, prepare_model_input) = self._utils
            test_files = glob("saved_audio.wav")
            batches = split_into_batches(test_files, batch_size=10)
            input_data = prepare_model_input(
                read_batch(batches[0]), device=self._device
            )
            output = self._model(input_data)
            store_text = []
            for example in output:
                store_text.append(self._decoder(example.cpu()))
            return "".join(store_text)
        except Exception:
            raise HTTPException(400, detail="failed to convert your audio to text")


class Settings(BaseSettings):
    version: str = "1.0"
    releaseId: str = "1.1"
    API_V1_STR: str = "/api/v1"
    APP_NAME: str = "Text to Speech Silero"


settings = Settings()
silero = SileroModel()
