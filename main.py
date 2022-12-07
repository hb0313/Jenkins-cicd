import fastapi
import uvicorn
from fastapi import responses

from api.v1.routers import generate, health
from core.config import settings

app = fastapi.FastAPI(
    title="Text Generation - Facebook Blenderbot",
    version=settings.releaseId,
)

app.include_router(health.router, prefix=settings.API_V1_STR, tags=["health"])
app.include_router(generate.router, prefix=settings.API_V1_STR, tags=["generation"])


@app.get("/", include_in_schema=False)
async def index() -> responses.RedirectResponse:
    return responses.RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run("main:app", debug=True, reload=True)
