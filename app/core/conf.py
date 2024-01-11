# -*- coding: utf-8 -*-
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # FastAPI
    API_V1_STR: str = '/api/v1'
    TITLE: str = 'Nebula'
    VERSION: str = '0.0.1'
    DESCRIPTION: str = 'PylerAI Evaluation and Labelling Platform'
    DOCS_URL: str = f'{API_V1_STR}/docs'

    # Uvicorn
    UVICORN_HOST: str = '127.0.0.1'
    UVICORN_PORT: int = 8000
    UVICORN_RELOAD: bool = True

    # Log
    LOG_STDOUT_FILENAME: str = 'nebula_access.log'
    LOG_STDERR_FILENAME: str = 'nebula_error.log'

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()
