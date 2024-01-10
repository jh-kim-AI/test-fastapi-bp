# -*- coding: utf-8 -*-
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # Log
    LOG_STDOUT_FILENAME: str = 'nebula_access.log'
    LOG_STDERR_FILENAME: str = 'nebula_error.log'

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()
