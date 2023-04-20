import fastapi
import uvicorn
from fastapi import responses

from api.v1.routers import health, transcription
from core.config import settings, silero

# initialize model on application startup
silero.initialize_model()

app = fastapi.FastAPI(
    title=settings.APP_NAME,
    version=settings.releaseId,
)

app.include_router(health.router, prefix=settings.API_V1_STR, tags=["health"])
app.include_router(
    transcription.router, prefix=settings.API_V1_STR, tags=["Speech To Text"]
)


@app.get("/", include_in_schema=False)
async def index() -> responses.RedirectResponse:
    return responses.RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(app, debug=True)
