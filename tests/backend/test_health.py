"""TRCS-7: regression test for the ``GET /health`` endpoint.

Verifies the contract that load balancers and uptime monitors rely on:
``status == "ok"``, a non-empty ``version`` string, and an ISO 8601
``timestamp``. Patterned after ``backend/tests/_template.py`` (httpx
``AsyncClient`` over the ASGI transport, no DynamoDB fixture since
``/health`` is open and stateless).
"""

from __future__ import annotations

from collections.abc import AsyncIterator
from datetime import datetime

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_health_returns_ok_payload(client: AsyncClient) -> None:
    response = await client.get("/health")

    assert response.status_code == 200

    payload = response.json()
    assert {"status", "version", "timestamp"} <= payload.keys()

    assert payload["status"] == "ok"

    version = payload["version"]
    assert isinstance(version, str) and version != ""

    timestamp = payload["timestamp"]
    assert isinstance(timestamp, str)
    # ``datetime.fromisoformat`` accepts the RFC 3339 / ISO 8601 subset that
    # FastAPI emits for ``datetime`` fields. A non-conforming string raises
    # ``ValueError`` and fails the test.
    datetime.fromisoformat(timestamp)
