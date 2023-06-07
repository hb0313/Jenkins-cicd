import io
from typing import Mapping, Union

import fastapi
import PIL
import torch
from transformers import AutoFeatureExtractor, RegNetForImageClassification

import schemas

TValue = Union[str, bytes]
TResult = Mapping[str, TValue]

router = fastapi.APIRouter()

model_path = "regnet-y-040/"
feature_extractor = AutoFeatureExtractor.from_pretrained(model_path)
model = RegNetForImageClassification.from_pretrained(model_path)


@router.post(
    "/classify",
    response_model=schemas.PredictionOut,
    responses={
        400: {"model": schemas.InvalidStringError},
        500: {"model": schemas.MLModelNotFoundError},
    },
)
async def image_classification(
    file: fastapi.UploadFile = fastapi.File(...),
) -> TResult:
    """
    Use this API for image classification.
    How to use:
    1. Upload a jpeg or png image
    2. Click execute
    3. JSON output will be generated with the image labels
    """

    image_types = {"image/png", "image/jpeg"}
    if file.content_type not in image_types:
        raise fastapi.HTTPException(400, "Image must be jpeg or png format")

    # predict
    if model is None:
        raise fastapi.HTTPException(500, "ML model not found")

    content = await file.read()
    image = PIL.Image.open(io.BytesIO(content))

    inputs = feature_extractor(image, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits

    # model predicts one of the 1000 ImageNet classes
    predicted_label = logits.argmax(-1).item()

    classification: TResult = {
        "label": model.config.id2label[predicted_label],
        "model": "Vissl - RegnetY-40",
    }

    return classification
