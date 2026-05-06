"""Router template — copy this file to ``app/routers/<feature>.py`` to start a new router.

Steps after copy:
    1. Rename ``router`` prefix/tag and replace example endpoints with real ones.
    2. Add ``app.include_router(<feature>.router)`` to ``app/main.py``.
    3. Copy ``tests/_template.py`` to ``tests/test_<feature>.py`` and write
       happy / auth_fail / invalid_input cases.

Conventions:
    - Always declare ``response_model`` so OpenAPI/Pydantic validate the shape.
    - Use ``Depends(get_current_user)`` for any endpoint that requires auth.
    - Raise ``HTTPException`` explicitly for error paths — never return error dicts.
    - Access DynamoDB via helpers in ``app.db`` (no direct ``boto3`` calls).
"""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.auth import CurrentUser, get_current_user
from app.schemas import ErrorResponse

router = APIRouter(
    prefix="/example",
    tags=["example"],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": ErrorResponse},
    },
)

CurrentUserDep = Annotated[CurrentUser, Depends(get_current_user)]


@router.get("", response_model=dict[str, str])
def list_examples(user: CurrentUserDep) -> dict[str, str]:
    """Replace with real list logic. Returns the calling user's id as a sanity check."""
    return {"requested_by": user.user_id}


@router.get("/{example_id}", response_model=dict[str, str])
def get_example(example_id: str, user: CurrentUserDep) -> dict[str, str]:
    if not example_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="example_id is required",
        )
    return {"id": example_id, "requested_by": user.user_id}
