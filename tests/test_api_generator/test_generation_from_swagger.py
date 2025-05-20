from __future__ import annotations

from typing import get_type_hints

import pytest

from tests.test_api_generator.api_definition import (
    VALID_ENDPOINT_FROM_SWAGGER_PARAMS,
    VALID_ENDPOINT_FROM_SWAGGER_PARAMS_LIST_RETURN,
)
from tests.test_api_generator.generate_clients_and_collections import (
    ASYNC_API_FROM_SWAGGER_DESTINATION,
    DESCRIPTION_OUTPUT_FILE,
    SYNC_API_FROM_SWAGGER_DESTINATION,
)
from tests.test_api_generator.messages import ENDPOINT_IS_NOT_CALLABLE_MESSAGE, ENDPOINT_NOT_GENERATED_MESSAGE


def test_is_api_description_created() -> None:
    # ASSERT
    assert DESCRIPTION_OUTPUT_FILE.exists(), "API description from swagger was not created"


@pytest.mark.parametrize("api_type", ["sync", "async"])
def test_is_api_file_created(api_type: str) -> None:
    # ARRANGE
    api_destination = SYNC_API_FROM_SWAGGER_DESTINATION if api_type == "sync" else ASYNC_API_FROM_SWAGGER_DESTINATION

    # ASSERT
    assert api_destination.exists(), "API file was not created"


@pytest.mark.parametrize("api_type", ["sync", "async"])
def test_endpoint_methods_created(api_type: str) -> None:
    # ARRANGE
    if api_type == "async":
        from tests.test_api_generator.generated_async_api_from_swagger import TestApi  # type: ignore[import-untyped]
    else:
        from tests.test_api_generator.generated_sync_api_from_swagger import TestApi  # type: ignore[import-untyped]

    # ASSERT
    assert hasattr(TestApi, "first_endpoint"), ENDPOINT_NOT_GENERATED_MESSAGE
    assert hasattr(TestApi, "second_endpoint"), ENDPOINT_NOT_GENERATED_MESSAGE

    assert callable(TestApi.first_endpoint), ENDPOINT_IS_NOT_CALLABLE_MESSAGE
    assert callable(TestApi.second_endpoint), ENDPOINT_IS_NOT_CALLABLE_MESSAGE


@pytest.mark.parametrize("api_type", ["sync", "async"])
def test_api_methods_signature(api_type: str) -> None:
    # ARRANGE & ACT
    if api_type == "async":
        from tests.test_api_generator.generated_async_api_from_swagger import (
            SecondEndpointResponseItem,
            TestApi,
        )
    else:
        from tests.test_api_generator.generated_sync_api_from_swagger import (
            SecondEndpointResponseItem,
            TestApi,
        )

    test_api_instance = TestApi()

    # ASSERT
    assert (
        get_type_hints(test_api_instance.first_endpoint) == VALID_ENDPOINT_FROM_SWAGGER_PARAMS
    ), "First test endpoint generated from swagger signature is invalid"

    second_endpoint_type_hints = get_type_hints(test_api_instance.second_endpoint)
    second_endpoint_return = second_endpoint_type_hints.pop("return")

    assert (
        second_endpoint_return == list[SecondEndpointResponseItem]
    ), "Second test endpoint generated from swagger return type is not a list"
    assert (
        second_endpoint_type_hints == VALID_ENDPOINT_FROM_SWAGGER_PARAMS_LIST_RETURN
    ), "Second test endpoint generated from swagger signature is invalid"
