import fastapi
import uvicorn
from fastapi import responses
from starlette_prometheus import PrometheusMiddleware, metrics

import core.config as config
from api.v1.routers import health, prediction

# initialize roberta 2 model
config.roberta.initialize_model()

app = fastapi.FastAPI(
    title="Question Answer - RoBerta Base CUAD",
    version=config.settings.releaseId,
)
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", metrics)

app.include_router(health.router, tags=["health"])
app.include_router(prediction.router, prefix="/predict", tags=["prediction"])


@app.get("/", include_in_schema=False)
async def index() -> responses.RedirectResponse:
    return responses.RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(app, debug=True)
