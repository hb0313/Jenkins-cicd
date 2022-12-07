import os.path

from pydantic import BaseSettings


class Settings(BaseSettings):
    version: str = "1.0"
    releaseId: str = "1.1"
    API_V1_STR: str = "/api/v1"
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


settings = Settings()
