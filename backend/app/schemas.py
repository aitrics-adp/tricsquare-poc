"""Common Pydantic schemas. Feature-specific schemas live alongside their routers/services."""

from __future__ import annotations

from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field


def _utcnow() -> datetime:
    return datetime.now(UTC)


class TricsquareModel(BaseModel):
    """Base model with strict-by-default config.

    - ``extra='forbid'`` catches typos in client payloads.
    - ``frozen=False`` so router code can mutate locally if needed.
    """

    model_config = ConfigDict(extra="forbid", populate_by_name=True)


class TimestampedModel(TricsquareModel):
    """Mixin for entities persisted to DynamoDB."""

    created_at: datetime = Field(default_factory=_utcnow)
    updated_at: datetime = Field(default_factory=_utcnow)


class ErrorResponse(TricsquareModel):
    """Uniform error envelope returned with non-2xx HTTPException responses."""

    detail: str
