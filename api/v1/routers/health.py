from typing import Union

import fastapi
import schemas
from core.config import settings
from fastapi import responses

router = fastapi.APIRouter()


class HealthResponse(responses.JSONResponse):
    media_type = "application/health+json"


@router.get(
    "/health",
    response_model=schemas.Health,
    response_class=HealthResponse,
    responses={500: {"model": schemas.Health}},
)
async def get_health(response: HealthResponse) -> Union[dict[str, str], HealthResponse]:
    response.headers["Cache-Control"] = "max-age=3600"

    content = {
        "status": schemas.Status.PASS,
        "version": settings.version,
        "releaseId": settings.releaseId,
    }

    return content
