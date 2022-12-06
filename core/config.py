from typing import Any, Tuple, Union

import pydantic
from transformers import pipeline


class RobertaBaseModel:
    def __init__(self) -> None:
        self._model_path = "akdeniz27/roberta-base-cuad"

    def initialize_model(self) -> None:
        self._model = pipeline(
            task="question-answering",
            model=self._model_path,
            tokenizer=self._model_path,
        )

    def get_model(self) -> Union[Any, None]:
        return self._model

    def predict_qa(self, question: str, context: str) -> Tuple[str, str]:
        answer = self._model({"question": question, "context": context})
        return answer["score"], answer["answer"]


class Settings(pydantic.BaseSettings):
    version: str = "1.0"
    releaseId: str = "1.1"


settings = Settings()
roberta = RobertaBaseModel()
