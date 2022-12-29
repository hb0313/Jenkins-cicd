import fastapi
import uvicorn
from api.v1.routers import health, translation
from core.config import settings
from fastapi import responses

app = fastapi.FastAPI(
    title="NVIDIA Speech to Text - Quartznet 15x5 (French)",
    version=settings.releaseId,
)

app.include_router(health.router, prefix=settings.API_V1_STR, tags=["health"])
app.include_router(translation.router, prefix=settings.API_V1_STR, tags=["classify"])


@app.get("/", include_in_schema=False)
async def index() -> responses.RedirectResponse:
    return responses.RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(app)
