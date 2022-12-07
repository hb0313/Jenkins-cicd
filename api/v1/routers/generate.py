from typing import List

import fastapi
from transformers import (
    BlenderbotSmallForConditionalGeneration,
    BlenderbotSmallTokenizer,
)

import schemas

bot_tokenizer = BlenderbotSmallTokenizer.from_pretrained(
    "facebook/blenderbot_small-90M"
)
bot_model = BlenderbotSmallForConditionalGeneration.from_pretrained(
    "facebook/blenderbot_small-90M"
)

router = fastapi.APIRouter()


@router.post(
    "/generate",
    response_model=List[schemas.GenerateOut],
    responses={
        400: {"model": schemas.InvalidStringError},
        500: {"model": schemas.MLModelNotFoundError},
    },
)
async def text_generation(
    user: str = fastapi.Body(default=None, embed=True)
) -> List[dict[str, str]]:
    """
    Use this API for multi conversation text generation.

    How to use:
    1. Enter a text such as a question.
    2. Click execute.
    3. JSON output will be generated with a bot response.
    """

    try:
        inputs = bot_tokenizer(user, return_tensors="pt")
        generation = bot_model.generate(**inputs, max_length=100)
        result = bot_tokenizer.decode(generation[0], skip_special_tokens=True)
    except ValueError:
        raise fastapi.HTTPException(
            status_code=404, detail="ERROR: Invalid string passed"
        )

    return [{"bot": str(result)}]
