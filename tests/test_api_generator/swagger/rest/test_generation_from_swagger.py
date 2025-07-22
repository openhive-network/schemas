from __future__ import annotations

from typing import get_type_hints

import pytest

from tests.test_api_generator.generate_clients_and_collections import (
    OUTPUT_ASYNC_REST_API_CLIENT_DESTINATION,
    OUTPUT_SYNC_REST_API_CLIENT_DESTINATION,
)
from tests.test_api_generator.messages import ENDPOINT_IS_NOT_CALLABLE_MESSAGE, ENDPOINT_NOT_GENERATED_MESSAGE
from tests.test_api_generator.swagger.rest.valid_output import (
    get_valid_params_for_async_balances_endpoint,
    get_valid_params_for_sync_balances_endpoint,
    get_valid_params_for_test_2_async_endpoint,
    get_valid_params_for_test_2_sync_endpoint,
)


@pytest.mark.parametrize("api_type", ["sync", "async"])
def test_is_api_package_created(api_type: str) -> None:
    # ARRANGE
    api_destination = (
        OUTPUT_SYNC_REST_API_CLIENT_DESTINATION if api_type == "sync" else OUTPUT_ASYNC_REST_API_CLIENT_DESTINATION
    )

    # ASSERT
    assert api_destination.exists(), "API file was not created"


@pytest.mark.parametrize("api_type", ["sync", "async"])
def test_endpoint_methods_created(api_type: str) -> None:
    # ARRANGE
    if api_type == "async":
        from tests.test_api_generator.swagger.rest.generated_async.test_api_client import (  # type: ignore[import-untyped]
            TestApi,
        )
    else:
        from tests.test_api_generator.swagger.rest.generated_sync.test_api_client import (  # type: ignore[import-untyped]
            TestApi,
        )

    # ASSERT
    assert hasattr(TestApi, "test_balances"), ENDPOINT_NOT_GENERATED_MESSAGE
    assert hasattr(TestApi, "test_2"), ENDPOINT_NOT_GENERATED_MESSAGE

    assert callable(TestApi.test_balances), ENDPOINT_IS_NOT_CALLABLE_MESSAGE
    assert callable(TestApi.test_2), ENDPOINT_IS_NOT_CALLABLE_MESSAGE


@pytest.mark.parametrize("api_type", ["sync", "async"])
def test_api_methods_signature(api_type: str) -> None:
    # ARRANGE & ACT
    if api_type == "async":
        from tests.test_api_generator.swagger.rest.generated_async.test_api_client import (
            TestApi,
        )

        valid_params_for_balances_endpoint = get_valid_params_for_async_balances_endpoint()
        valid_params_for_test_2_endpoint = get_valid_params_for_test_2_async_endpoint()

    else:
        from tests.test_api_generator.swagger.rest.generated_sync.test_api_client import TestApi

        valid_params_for_balances_endpoint = get_valid_params_for_sync_balances_endpoint()
        valid_params_for_test_2_endpoint = get_valid_params_for_test_2_sync_endpoint()

    test_api_instance = TestApi()

    test_2_endpoint_type_hints = get_type_hints(test_api_instance.test_2)
    test_balances_endpoint_type_hints = get_type_hints(test_api_instance.test_balances)

    # ASSERT
    assert (
        test_balances_endpoint_type_hints == valid_params_for_balances_endpoint
    ), "Test balances endpoint generated from swagger signature is invalid"

    assert (
        test_2_endpoint_type_hints == valid_params_for_test_2_endpoint
    ), "Test 2 endpoint generated from swagger signature is invalid"
