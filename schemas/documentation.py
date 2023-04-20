from typing import Any, Union

from pydantic import BaseModel


class DocumentationOut(BaseModel):
    model_name: str
    short_desc: str
    ideal: Union[str, Any]
    not_ideal: str
    input_args: dict[Any, Any]
    output_args: dict[Any, Any]
