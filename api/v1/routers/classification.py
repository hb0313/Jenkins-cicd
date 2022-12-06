import os
from typing import List, Union

import fastapi
from PIL import Image
from transformers import pipeline

import schemas

pipe = pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")

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
    labels: str = fastapi.Body(default=None, embed=True),
    file: fastapi.UploadFile = fastapi.File(...),
) -> List[dict[str, Union[str, float]]]:
    """
    Use this API for image classification.

    API will classify in classes - dog, cat, horse, airplane, bird, ship, etc.

    How to use:
    1. Click try it.
    2. Input an image and comma seprated labels
    3. Click execute
    4. Response will be a JSON with answer.
    """

    image_types = {"image/png", "image/jpeg"}
    if file.content_type not in image_types:
        raise fastapi.HTTPException(400, "Image must be jpeg or png format")

    if pipe is None:
        raise fastapi.HTTPException(500, "ML model not found")
    label = labels.split(",")
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    image = Image.open(f"uploads/{file.filename}")

    try:
        res = pipe(
            images=image,
            candidate_labels=label,
            hypothesis_template="This is a photo of a {}",
        )
        predictions: list[dict[str, Union[str, float]]] = [
            {
                "description": dic["label"],
                "probability": dic["score"],
            }
            for dic in res
        ]

    except ValueError as err:
        raise fastapi.HTTPException(status_code=404, detail=err)
    finally:
        os.remove(f"uploads/{file.filename}")

    return predictions
