from typing import List, Union

from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    DATABASE_NAME: str
    DATABASE_URL: str
    SECRET_KEY: str
    SALT_SECRET_KEY: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
