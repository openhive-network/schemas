from __future__ import annotations

from typing import get_type_hints

import pytest

from tests.test_api_generator.generate_clients_and_collections import (
    ASYNC_JSON_RPC_API_FROM_SWAGGER_DESTINATION,
    JSON_RPC_DESCRIPTION_OUTPUT_FILE,
    SYNC_JSON_RPC_API_FROM_SWAGGER_DESTINATION,
)
from tests.test_api_generator.messages import ENDPOINT_IS_NOT_CALLABLE_MESSAGE, ENDPOINT_NOT_GENERATED_MESSAGE
from tests.test_api_generator.swagger.json_rpc.valid_output import (
    VALID_PARAMS_FOR_FIRST_ENDPOINT,
    get_valid_params_for_second_endpoint,
)


def test_is_api_description_created() -> None:
    # ASSERT
    assert JSON_RPC_DESCRIPTION_OUTPUT_FILE.exists(), "json rpc API description from swagger was not created"


@pytest.mark.parametrize("api_type", ["sync", "async"])
def test_is_api_file_created(api_type: str) -> None:
    # ARRANGE
    api_destination = (
        SYNC_JSON_RPC_API_FROM_SWAGGER_DESTINATION
        if api_type == "sync"
        else ASYNC_JSON_RPC_API_FROM_SWAGGER_DESTINATION
    )

    # ASSERT
    assert api_destination.exists(), "API file was not created"


@pytest.mark.parametrize("api_type", ["sync", "async"])
def test_endpoint_methods_created(api_type: str) -> None:
    # ARRANGE
    if api_type == "async":
        from tests.test_api_generator.swagger.json_rpc.generated_async_api import (  # type: ignore[import-untyped]
            TestApi,
        )
    else:
        from tests.test_api_generator.swagger.json_rpc.generated_sync_api import TestApi  # type: ignore[import-untyped]

    # ASSERT
    assert hasattr(TestApi, "first_endpoint"), ENDPOINT_NOT_GENERATED_MESSAGE
    assert hasattr(TestApi, "second_endpoint"), ENDPOINT_NOT_GENERATED_MESSAGE

    assert callable(TestApi.first_endpoint), ENDPOINT_IS_NOT_CALLABLE_MESSAGE
    assert callable(TestApi.second_endpoint), ENDPOINT_IS_NOT_CALLABLE_MESSAGE


@pytest.mark.parametrize("api_type", ["sync", "async"])
def test_api_methods_signature(api_type: str) -> None:
    # ARRANGE & ACT
    if api_type == "async":
        from tests.test_api_generator.swagger.json_rpc.generated_async_api import (
            TestApi,
        )
    else:
        from tests.test_api_generator.swagger.json_rpc.generated_sync_api import TestApi

    test_api_instance = TestApi()

    # ASSERT
    assert (
        get_type_hints(test_api_instance.first_endpoint) == VALID_PARAMS_FOR_FIRST_ENDPOINT
    ), "First test endpoint generated from swagger signature is invalid"

    second_endpoint_type_hints = get_type_hints(test_api_instance.second_endpoint)

    assert (
        second_endpoint_type_hints == get_valid_params_for_second_endpoint()
    ), "Second test endpoint generated from swagger signature is invalid"
