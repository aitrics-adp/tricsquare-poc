"""Settings loader. Reads environment first; production should hydrate via SSM Parameter Store."""

from __future__ import annotations

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings.

    POC defaults assume local dev. Lambda receives values via SAM ``Environment``
    or SSM-backed Parameter Store references — never hardcode secrets.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    aws_region: str = Field(default="ap-northeast-2")
    ddb_table_name: str = Field(default="tricsquare-poc")
    ddb_endpoint_url: str | None = Field(default=None)

    jwt_secret: str = Field(default="dev-only-do-not-use-in-prod")
    jwt_algorithm: str = Field(default="HS256")
    jwt_expire_minutes: int = Field(default=60)

    log_level: str = Field(default="INFO")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Cached accessor — instantiated once per Lambda container."""
    return Settings()
