from __future__ import annotations

from typing import get_type_hints

import pytest

from tests.test_api_generator.api_definition_params_result import VALID_ENDPOINT_PARAMS
from tests.test_api_generator.base_api_classes import VALID_RETURN_VALUE
from tests.test_api_generator.generate_clients_and_collections import (
    COLLECTION_ASYNC_API_DESTINATION,
    COLLECTION_SYNC_API_DESTINATION,
)
from tests.test_api_generator.messages import (
    API_NOT_GENERATED_MESSAGE,
    ENDPOINT_IS_NOT_CALLABLE_MESSAGE,
    ENDPOINT_NOT_GENERATED_MESSAGE,
)


@pytest.mark.parametrize("api_type", ["sync", "async"])
def test_is_collection_generated(api_type: str) -> None:
    # ARRANGE
    api_destination = COLLECTION_SYNC_API_DESTINATION if api_type == "sync" else COLLECTION_ASYNC_API_DESTINATION

    # ASSERT
    assert api_destination.exists(), "API collection file was not created"


@pytest.mark.parametrize("api_type", ["sync", "async"])
def test_endpoint_methods_created_and_are_callable(api_type: str) -> None:
    # ARRANGE & ACT
    if api_type == "async":
        from tests.test_api_generator.generated_async_api_collection import (  # type: ignore[import-untyped]
            GeneratedAsyncApiCollection as GeneratedCollection,
        )
    else:
        from tests.test_api_generator.generated_sync_api_collection import (  # type: ignore[import-untyped]
            GeneratedSyncApiCollection as GeneratedCollection,
        )

    api_collection = GeneratedCollection()

    # ASSERT
    assert hasattr(api_collection, "first_test_api"), API_NOT_GENERATED_MESSAGE
    assert hasattr(api_collection, "second_test_api"), API_NOT_GENERATED_MESSAGE

    assert hasattr(api_collection.first_test_api, "first_endpoint"), ENDPOINT_NOT_GENERATED_MESSAGE
    assert hasattr(api_collection.first_test_api, "second_endpoint"), ENDPOINT_NOT_GENERATED_MESSAGE
    assert hasattr(api_collection.second_test_api, "first_endpoint"), ENDPOINT_NOT_GENERATED_MESSAGE

    assert callable(api_collection.first_test_api.first_endpoint), ENDPOINT_IS_NOT_CALLABLE_MESSAGE
    assert callable(api_collection.first_test_api.second_endpoint), ENDPOINT_IS_NOT_CALLABLE_MESSAGE

    assert callable(api_collection.second_test_api.first_endpoint), ENDPOINT_IS_NOT_CALLABLE_MESSAGE


@pytest.mark.parametrize("api_type", ["sync", "async"])
def test_api_methods_signature(api_type: str) -> None:
    # ARRANGE & ACT
    if api_type == "async":
        from tests.test_api_generator.generated_async_api_collection import (
            GeneratedAsyncApiCollection as GeneratedCollection,
        )
    else:
        from tests.test_api_generator.generated_sync_api_collection import (
            GeneratedSyncApiCollection as GeneratedCollection,
        )

    api_collection = GeneratedCollection()

    # ASSERT
    assert (
        get_type_hints(api_collection.first_test_api.first_endpoint) == VALID_ENDPOINT_PARAMS
    ), "First test endpoint signature is invalid"
    assert (
        get_type_hints(api_collection.first_test_api.second_endpoint) == VALID_ENDPOINT_PARAMS
    ), "Second test endpoint signature is invalid"

    assert (
        get_type_hints(api_collection.second_test_api.first_endpoint) == VALID_ENDPOINT_PARAMS
    ), "First test endpoint signature is invalid"


def test_sync_api_return_values() -> None:
    # ARRANGE & ACT
    from tests.test_api_generator.generated_sync_api_collection import (
        GeneratedSyncApiCollection,
    )

    api_collection = GeneratedSyncApiCollection()

    # ASSERT
    assert (
        api_collection.first_test_api.first_endpoint() == VALID_RETURN_VALUE
    ), "First test endpoint returned invalid value"
    assert (
        api_collection.first_test_api.second_endpoint() == VALID_RETURN_VALUE
    ), "Second test endpoint returned invalid value"

    assert (
        api_collection.second_test_api.first_endpoint() == VALID_RETURN_VALUE
    ), "First test endpoint returned invalid value"


async def test_async_api_return_values() -> None:
    # ARRANGE & ACT
    from tests.test_api_generator.generated_async_api_collection import GeneratedAsyncApiCollection

    api_collection = GeneratedAsyncApiCollection()

    # ASSERT
    assert (
        await api_collection.first_test_api.first_endpoint() == VALID_RETURN_VALUE
    ), "First test endpoint returned invalid value"
    assert (
        await api_collection.first_test_api.second_endpoint() == VALID_RETURN_VALUE
    ), "Second test endpoint returned invalid value"

    assert (
        await api_collection.second_test_api.first_endpoint() == VALID_RETURN_VALUE
    ), "First test endpoint returned invalid value"
