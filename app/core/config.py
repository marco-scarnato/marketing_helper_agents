from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "marketing-helper-agent"
    APP_ENV: str = "development"
    OLLAMA_URL: str = "http://ollama:11434"
    OLLAMA_MODEL: str = "qwen3.5:2b"
    POSTGRES_URL: str = "postgresql://creativehub:creativehub@postgres:5432/creativehub"
    REQUEST_TIMEOUT_SECONDS: float = 30.0

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
