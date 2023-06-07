from typing import Any

import fastapi

from schemas.documentation import DocumentationOut

router = fastapi.APIRouter()


@router.get("/documentation", response_model=DocumentationOut)
def get_doc() -> dict[str, Any]:
    docs: dict[str, Any] = {
        "model_name": "image_classification_vissl",
        "short_desc": (
            "ViSSL is a computer vision library for state-of-the-art deep learning"
            " models. It provides pre-trained models, tools for training new models,"
            " and a framework for building custom models."
        ),
        "ideal": (
            "Ideal for computer vision tasks that require high accuracy and advanced"
            " features, such as object detection, semantic segmentation, and instance"
            " segmentation."
        ),
        "not_ideal": (
            "May not be ideal for low-resource or real-time applications due to the"
            " computational intensity of the models."
        ),
        "input_args": {"example1": "Image file in a format supported by the library."},
        "output_args": {"example1": "BMP"},
    }
    return docs
