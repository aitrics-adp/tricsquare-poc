"""FastAPI application entry point. Wraps with Mangum for AWS Lambda."""

from __future__ import annotations

from fastapi import FastAPI
from mangum import Mangum

from app import __version__
from app.config import get_settings
from app.routers import health

settings = get_settings()

app = FastAPI(
    title="TricSquare PRO API",
    version=__version__,
    description="환자 PRO 수집 MVP API.",
)

# Register routers below. New routers are created by copying
# ``app/routers/_template.py`` and registered here.
app.include_router(health.router)


handler = Mangum(app, lifespan="off")
