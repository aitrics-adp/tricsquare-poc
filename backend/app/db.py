"""DynamoDB access helpers.

All DynamoDB I/O in the codebase MUST go through this module. Direct ``boto3``
calls in routers/services are prohibited (see ``backend/CLAUDE.md``).
"""

from __future__ import annotations

from functools import lru_cache
from typing import TYPE_CHECKING, Any

import boto3

from app.config import get_settings

if TYPE_CHECKING:
    from mypy_boto3_dynamodb.service_resource import Table


@lru_cache(maxsize=1)
def _resource() -> Any:
    settings = get_settings()
    kwargs: dict[str, Any] = {"region_name": settings.aws_region}
    if settings.ddb_endpoint_url:
        kwargs["endpoint_url"] = settings.ddb_endpoint_url
    return boto3.resource("dynamodb", **kwargs)


def get_table(name: str | None = None) -> Table:
    """Return the DynamoDB table resource. Defaults to the configured POC table."""
    table_name = name or get_settings().ddb_table_name
    return _resource().Table(table_name)


def get_item(pk: str, sk: str, *, table_name: str | None = None) -> dict[str, Any] | None:
    """Fetch a single item by composite key. Returns ``None`` if not found."""
    response = get_table(table_name).get_item(Key={"PK": pk, "SK": sk})
    item = response.get("Item")
    return dict(item) if item is not None else None


def put_item(item: dict[str, Any], *, table_name: str | None = None) -> None:
    """Write a single item. Caller is responsible for ``PK``/``SK`` shape."""
    get_table(table_name).put_item(Item=item)


def query_by_pk(
    pk: str,
    *,
    sk_prefix: str | None = None,
    table_name: str | None = None,
) -> list[dict[str, Any]]:
    """Query all items under a partition, optionally filtered by SK prefix."""
    from boto3.dynamodb.conditions import ConditionBase, Key

    condition: ConditionBase = Key("PK").eq(pk)
    if sk_prefix:
        condition = condition & Key("SK").begins_with(sk_prefix)
    response = get_table(table_name).query(KeyConditionExpression=condition)
    return [dict(item) for item in response.get("Items", [])]
