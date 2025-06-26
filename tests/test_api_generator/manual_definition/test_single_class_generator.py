from __future__ import annotations

from typing import get_type_hints

import pytest

from tests.test_api_generator.base_api_classes import VALID_RETURN_VALUE
from tests.test_api_generator.generate_clients_and_collections import (
    SINGLE_ASYNC_API_DESTINATION,
    SINGLE_SYNC_API_DESTINATION,
)
from tests.test_api_generator.manual_definition.output import (
    VALID_PARAMS_FOR_FIRST_AND_SECOND_ENDPOINT,
    VALID_PARAMS_FOR_THIRD_ENDPOINT,
)
from tests.test_api_generator.messages import ENDPOINT_IS_NOT_CALLABLE_MESSAGE, ENDPOINT_NOT_GENERATED_MESSAGE


@pytest.mark.parametrize("api_type", ["sync", "async"])
def test_is_api_file_created(api_type: str) -> None:
    # ARRANGE
    api_destination = SINGLE_SYNC_API_DESTINATION if api_type == "sync" else SINGLE_ASYNC_API_DESTINATION

    # ASSERT
    assert api_destination.exists(), "API file was not created"


@pytest.mark.parametrize("api_type", ["sync", "async"])
def test_endpoint_methods_created(api_type: str) -> None:
    # ARRANGE
    if api_type == "async":
        from tests.test_api_generator.manual_definition.generated_async_single_api import (  # type: ignore[import-untyped]
            TestApi,
        )

    else:
        from tests.test_api_generator.manual_definition.generated_sync_single_api import (  # type: ignore[import-untyped]
            TestApi,
        )

    # ASSERT
    assert hasattr(TestApi, "first_endpoint"), ENDPOINT_NOT_GENERATED_MESSAGE
    assert hasattr(TestApi, "second_endpoint"), ENDPOINT_NOT_GENERATED_MESSAGE
    assert hasattr(TestApi, "third_endpoint"), ENDPOINT_NOT_GENERATED_MESSAGE

    assert callable(TestApi.first_endpoint), ENDPOINT_IS_NOT_CALLABLE_MESSAGE
    assert callable(TestApi.second_endpoint), ENDPOINT_IS_NOT_CALLABLE_MESSAGE
    assert callable(TestApi.third_endpoint), ENDPOINT_IS_NOT_CALLABLE_MESSAGE


@pytest.mark.parametrize("api_type", ["sync", "async"])
def test_api_methods_signature(api_type: str) -> None:
    # ARRANGE & ACT
    if api_type == "async":
        from tests.test_api_generator.manual_definition.generated_async_single_api import TestApi
    else:
        from tests.test_api_generator.manual_definition.generated_sync_single_api import TestApi

    test_api_instance = TestApi()

    # ASSERT
    assert (
        get_type_hints(test_api_instance.first_endpoint) == VALID_PARAMS_FOR_FIRST_AND_SECOND_ENDPOINT
    ), "First test endpoint signature is invalid"
    assert (
        get_type_hints(test_api_instance.second_endpoint) == VALID_PARAMS_FOR_FIRST_AND_SECOND_ENDPOINT
    ), "Second test endpoint signature is invalid"
    assert (
        get_type_hints(test_api_instance.third_endpoint) == VALID_PARAMS_FOR_THIRD_ENDPOINT
    ), "Third test endpoint signature is invalid"


def test_sync_api_return_values() -> None:
    # ARRANGE & ACT
    from tests.test_api_generator.manual_definition.generated_sync_single_api import TestApi

    test_api_instance = TestApi()

    # ASSERT
    assert test_api_instance.first_endpoint() == VALID_RETURN_VALUE, "First test endpoint returned invalid value"
    assert test_api_instance.second_endpoint() == VALID_RETURN_VALUE, "Second test endpoint returned invalid value"
    assert test_api_instance.third_endpoint() == VALID_RETURN_VALUE, "Third test endpoint returned invalid value"


async def test_async_api_return_values() -> None:
    # ARRANGE & ACT
    from tests.test_api_generator.manual_definition.generated_async_single_api import TestApi

    test_api_instance = TestApi()

    # ASSERT
    assert await test_api_instance.first_endpoint() == VALID_RETURN_VALUE, "First test endpoint returned invalid value"
    assert (
        await test_api_instance.second_endpoint() == VALID_RETURN_VALUE
    ), "Second test endpoint returned invalid value"
    assert await test_api_instance.third_endpoint() == VALID_RETURN_VALUE, "Third test endpoint returned invalid value"
