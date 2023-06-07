import fastapi
import uvicorn
from fastapi import responses

from api.v1.routers import classification, documentation, health
from core.config import settings

app = fastapi.FastAPI(
    title="Image Classification - Vissl (RegnetY-60)",
    version=settings.releaseId,
)

app.include_router(health.router, prefix=settings.API_V1_STR, tags=["health"])
app.include_router(
    classification.router, prefix=settings.API_V1_STR, tags=["classification"]
)
app.include_router(
    documentation.router, prefix=settings.API_V1_STR, tags=["documentation"]
)


@app.get("/", include_in_schema=False)
async def index() -> responses.RedirectResponse:
    return responses.RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(app, debug=True)
