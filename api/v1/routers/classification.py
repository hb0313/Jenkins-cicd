import os
from typing import List, Union

import fastapi
from torchvision import io
from transformers import AutoFeatureExtractor, SwinForImageClassification

import schemas

feature_extractor = AutoFeatureExtractor.from_pretrained(
    "microsoft/swin-base-patch4-window7-224-in22k"
)
model = SwinForImageClassification.from_pretrained(
    "microsoft/swin-base-patch4-window7-224-in22k"
)


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
    file: fastapi.UploadFile = fastapi.File(...),
) -> List[dict[str, Union[str, float]]]:
    """
    Use this API for image classification.

    API will classify in classes - dog, cat, horse, airplane, bird, ship, etc.

    How to use:
    1. Click try it.
    2. Input an image
    3. Click execute
    4. Response will be a JSON with answer.
    """

    image_types = {"image/png", "image/jpeg"}
    if file.content_type not in image_types:
        raise fastapi.HTTPException(400, "Image must be jpeg or png format")

    if model is None:
        raise fastapi.HTTPException(500, "ML model not found")

    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    image = io.read_image(f"uploads/{file.filename}")
    try:
        inputs = feature_extractor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits
        # model predicts one of the 1000 ImageNet classes
        predicted_class_idx = logits.argmax(-1).item()
    except ValueError:
        raise fastapi.HTTPException(
            status_code=404, detail="ERROR: Unable to detect objects from image"
        )
    finally:
        os.remove(f"uploads/{file.filename}")

    return [
        {
            "answer": model.config.id2label[predicted_class_idx],
        }
    ]
