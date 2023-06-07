import fastapi
import uvicorn
from fastapi import responses

from api.v1.routers import health, segment
from core.config import settings

app = fastapi.FastAPI(
    title="Pre-trained TSN Models on UCF101",
    version=settings.releaseId,
)

app.include_router(health.router, prefix=settings.API_V1_STR, tags=["health"])
app.include_router(
    segment.router, prefix=settings.API_V1_STR, tags=["image_segmentation"]
)


@app.get("/", include_in_schema=False)
async def index() -> responses.RedirectResponse:
    return responses.RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8083, host="0.0.0.0")
