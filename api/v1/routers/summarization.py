from typing import Any, List

import fastapi
import torch
from transformers import BertTokenizerFast, EncoderDecoderModel

import schemas

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = BertTokenizerFast.from_pretrained(
    "mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization"
)
model = EncoderDecoderModel.from_pretrained(
    "mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization"
).to(device)

router = fastapi.APIRouter()


@router.post(
    "/classify",
    response_model=List[schemas.AnswerOut],
    responses={
        400: {"model": schemas.InvalidStringError},
        500: {"model": schemas.MLModelNotFoundError},
    },
)
async def text_summarization(
    text: str = fastapi.Body(embed=True),
) -> List[dict[str, Any]]:
    """
    Use this API for text summarization.
    How to use:
    1. sentence in string
    2. Click execute
    3. JSON output will be summarized sentence
    """
    try:
        inputs = tokenizer(
            [text],
            padding="max_length",
            truncation=True,
            max_length=512,
            return_tensors="pt",
        )
        input_ids = inputs.input_ids.to(device)
        attention_mask = inputs.attention_mask.to(device)

        output = model.generate(input_ids, attention_mask=attention_mask)

        res = tokenizer.decode(output[0], skip_special_tokens=True)
    except ValueError:
        raise fastapi.HTTPException(status_code=404, detail="ERROR: Invalid text")

    return [
        {
            "answer": res,
        }
    ]
