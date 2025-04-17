from __future__ import annotations

import pytest

from tests.test_api_generator.base_api_classes import VALID_RETURN_VALUE
from tests.test_api_generator.generate_needed_modules import SINGLE_ASYNC_API_DESTINATION, SINGLE_SYNC_API_DESTINATION


def test_generate_sync_api() -> None:
    # ARRANGE
    api_destination = SINGLE_SYNC_API_DESTINATION

    # ASSERT
    assert api_destination.exists(), "API file was not created"

    from tests.test_api_generator.generated_sync_single_api import TestApi  # type: ignore[import-untyped]

    assert TestApi().first_endpoint() == VALID_RETURN_VALUE


@pytest.mark.asyncio
async def test_generate_async_api() -> None:
    # ARRANGE
    api_destination = SINGLE_ASYNC_API_DESTINATION

    # ASSERT
    assert api_destination.exists(), "API file was not created"

    from tests.test_api_generator.generated_async_single_api import TestApi  # type: ignore[import-untyped]

    assert await TestApi().first_endpoint() == VALID_RETURN_VALUE
