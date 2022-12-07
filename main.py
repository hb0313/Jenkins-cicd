import fastapi
import uvicorn
from fastapi import responses

from api.v1.routers import health, summarization
from core.config import settings

app = fastapi.FastAPI(
    title="Text Summarization - Bert2Bert Small",
    version=settings.releaseId,
)

app.include_router(health.router, prefix=settings.API_V1_STR, tags=["health"])
app.include_router(summarization.router, prefix=settings.API_V1_STR, tags=["classify"])


@app.get("/", include_in_schema=False)
async def index() -> responses.RedirectResponse:
    return responses.RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(app, debug=True)
