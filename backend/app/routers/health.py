"""Health check endpoint. Open (no auth) — called by load balancers / monitors."""

from __future__ import annotations

from datetime import UTC, datetime

from fastapi import APIRouter

from app import __version__
from app.schemas import TricsquareModel

router = APIRouter(tags=["health"])


class HealthResponse(TricsquareModel):
    status: str
    version: str
    timestamp: datetime


@router.get("/health", response_model=HealthResponse)
def get_health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        version=__version__,
        timestamp=datetime.now(UTC),
    )
