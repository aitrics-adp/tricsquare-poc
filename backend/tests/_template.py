"""Test template — copy this file to ``tests/test_<feature>.py`` to start a new test module.

Required cases (per ``backend/CLAUDE.md``):
    1. happy        — authorized request, valid input, expected response.
    2. auth_fail    — missing/invalid token returns 401.
    3. invalid_input — malformed payload returns 422.

Conventions:
    - Use ``moto`` to stub DynamoDB; never hit real AWS in tests.
    - Use ``httpx.AsyncClient`` with FastAPI's ASGI transport for endpoint tests.
    - Each test creates its own table via the ``ddb_table`` fixture for isolation.
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator

import boto3
import pytest
from httpx import ASGITransport, AsyncClient
from moto import mock_aws

from app.auth import issue_token
from app.config import get_settings
from app.main import app


@pytest.fixture
def ddb_table() -> Iterator[None]:
    """Create a synthetic DDB table inside a moto context for the duration of a test."""
    with mock_aws():
        settings = get_settings()
        client = boto3.client("dynamodb", region_name=settings.aws_region)
        client.create_table(
            TableName=settings.ddb_table_name,
            KeySchema=[
                {"AttributeName": "PK", "KeyType": "HASH"},
                {"AttributeName": "SK", "KeyType": "RANGE"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "PK", "AttributeType": "S"},
                {"AttributeName": "SK", "AttributeType": "S"},
            ],
            BillingMode="PAY_PER_REQUEST",
        )
        yield


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def auth_headers() -> dict[str, str]:
    token = issue_token(user_id="test-user", role="patient")
    return {"Authorization": f"Bearer {token}"}


# --------------------------------------------------------------------------- #
# Replace the placeholders below with real assertions for the feature.
# --------------------------------------------------------------------------- #


async def test_happy_path(
    client: AsyncClient,
    auth_headers: dict[str, str],
    ddb_table: None,
) -> None:
    """Authorized request with valid input returns 2xx."""
    response = await client.get("/example", headers=auth_headers)
    assert response.status_code in (200, 404)  # adjust once endpoint is implemented


async def test_auth_fail(client: AsyncClient) -> None:
    """Missing token returns 401."""
    response = await client.get("/example")
    assert response.status_code == 401


async def test_invalid_input(
    client: AsyncClient,
    auth_headers: dict[str, str],
    ddb_table: None,
) -> None:
    """Malformed payload returns 422."""
    response = await client.post("/example", json={"bad": "payload"}, headers=auth_headers)
    assert response.status_code in (404, 405, 422)  # adjust once endpoint accepts POST
