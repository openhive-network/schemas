from __future__ import annotations

from pathlib import Path

from schemas.apis.api_client_generator.json_rpc import (
    generate_api_client,
    generate_api_collection,
    generate_api_description,
)
from schemas.apis.api_client_generator.rest import generate_api_client_from_swagger
from tests.test_api_generator.base_api_classes import (
    MockAsyncJsonRpcApiBase,
    MockAsyncRestApiBase,
    MockSyncJsonRpcApiBase,
    MockSyncRestApiBase,
)
from tests.test_api_generator.manual_definition.input import (
    GENERATOR_TEST_API_COLLECTION,
    GENERATOR_TEST_SINGLE_API,
)

SYNC_API_COLLECTION_NAME = "GeneratedSyncApiCollection"
ASYNC_API_COLLECTION_NAME = "GeneratedAsyncApiCollection"

SINGLE_ASYNC_API_DESTINATION = Path(__file__).parent / "manual_definition" / "generated_async_single_api.py"
SINGLE_SYNC_API_DESTINATION = Path(__file__).parent / "manual_definition" / "generated_sync_single_api.py"
COLLECTION_ASYNC_API_DESTINATION = Path(__file__).parent / "manual_definition" / "generated_async_api_collection.py"
COLLECTION_SYNC_API_DESTINATION = Path(__file__).parent / "manual_definition" / "generated_sync_api_collection.py"

OPENAPI_JSON_RPC_DEFINITION_DESTINATION = Path(__file__).parent / "swagger" / "json_rpc" / "openapi.json"
SYNC_JSON_RPC_API_FROM_SWAGGER_DESTINATION = Path(__file__).parent / "swagger" / "json_rpc" / "generated_sync_api.py"
JSON_RPC_DESCRIPTION_OUTPUT_FILE = Path(__file__).parent / "swagger" / "json_rpc" / "api_description.py"
ASYNC_JSON_RPC_API_FROM_SWAGGER_DESTINATION = Path(__file__).parent / "swagger" / "json_rpc" / "generated_async_api.py"

OPENAPI_REST_DEFINITION_DESTINATION = Path(__file__).parent / "swagger" / "rest" / "openapi.json"
OUTPUT_SYNC_REST_API_CLIENT_DESTINATION = Path(__file__).parent / "swagger" / "rest" / "generated_sync"
OUTPUT_ASYNC_REST_API_CLIENT_DESTINATION = Path(__file__).parent / "swagger" / "rest" / "generated_async"


def generate_api_description_from_swagger() -> None:
    generate_api_description(
        "test_api_description", OPENAPI_JSON_RPC_DEFINITION_DESTINATION, JSON_RPC_DESCRIPTION_OUTPUT_FILE
    )


def generate_clients_and_collections() -> None:
    from .swagger.json_rpc.api_description import test_api_description  # type: ignore[import-untyped]

    generate_api_client_from_swagger(
        OPENAPI_REST_DEFINITION_DESTINATION,
        OUTPUT_SYNC_REST_API_CLIENT_DESTINATION,
        base_class=MockSyncRestApiBase,  # type: ignore[arg-type]
        asynchronous=False,
    )

    generate_api_client_from_swagger(
        OPENAPI_REST_DEFINITION_DESTINATION,
        OUTPUT_ASYNC_REST_API_CLIENT_DESTINATION,
        base_class=MockAsyncRestApiBase,  # type: ignore[arg-type]
    )

    generate_api_client(
        test_api_description,
        MockSyncJsonRpcApiBase,  # type: ignore[arg-type]
        path=SYNC_JSON_RPC_API_FROM_SWAGGER_DESTINATION,
        asynchronous=False,
    )

    generate_api_client(
        test_api_description,
        MockAsyncJsonRpcApiBase,  # type: ignore[arg-type]
        path=ASYNC_JSON_RPC_API_FROM_SWAGGER_DESTINATION,
    )

    generate_api_client(
        GENERATOR_TEST_SINGLE_API,  # type: ignore[arg-type]
        MockSyncJsonRpcApiBase,  # type: ignore[arg-type]
        path=SINGLE_SYNC_API_DESTINATION,
        asynchronous=False,
    )

    generate_api_client(
        GENERATOR_TEST_SINGLE_API,  # type: ignore[arg-type]
        MockAsyncJsonRpcApiBase,  # type: ignore[arg-type]
        path=SINGLE_ASYNC_API_DESTINATION,
    )

    generate_api_collection(
        GENERATOR_TEST_API_COLLECTION,
        MockSyncJsonRpcApiBase,  # type: ignore[arg-type]
        collection_name=SYNC_API_COLLECTION_NAME,
        path=COLLECTION_SYNC_API_DESTINATION,
        asynchronous=False,
    )

    generate_api_collection(
        GENERATOR_TEST_API_COLLECTION,
        MockAsyncJsonRpcApiBase,  # type: ignore[arg-type]
        collection_name=ASYNC_API_COLLECTION_NAME,
        path=COLLECTION_ASYNC_API_DESTINATION,
    )
