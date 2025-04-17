from __future__ import annotations

import pytest

from tests.test_api_generator.base_api_classes import VALID_RETURN_VALUE
from tests.test_api_generator.generate_needed_modules import (
    COLLECTION_ASYNC_API_DESTINATION,
    COLLECTION_SYNC_API_DESTINATION,
)


def test_generate_sync_api_collection() -> None:
    # ARRANGE
    api_destination = COLLECTION_SYNC_API_DESTINATION

    # ASSERT
    assert api_destination.exists(), "API collection file was not created"

    from .generated_sync_api_collection import GeneratedSyncApiCollection  # type: ignore[import-untyped]

    assert GeneratedSyncApiCollection().first_test_api.first_endpoint() == VALID_RETURN_VALUE


@pytest.mark.asyncio
async def test_generate_async_api_collection() -> None:
    # ARRANGE
    api_destination = COLLECTION_ASYNC_API_DESTINATION

    # ASSERT
    assert api_destination.exists(), "API collection file was not created"

    from .generated_async_api_collection import GeneratedAsyncApiCollection  # type: ignore[import-untyped]

    assert await GeneratedAsyncApiCollection().first_test_api.first_endpoint() == VALID_RETURN_VALUE
