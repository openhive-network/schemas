from __future__ import annotations

from pathlib import Path

from schemas.apis.api_client_generator import (
    generate_api_client,
    generate_api_collection,
    generate_json_rpc_api_description,
)
from tests.test_api_generator.base_api_classes import MockAsyncApiBase, MockSyncApiBase
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

OPENAPI_DEFINITION_DESTINATION = Path(__file__).parent / "swagger" / "openapi.json"
DESCRIPTION_OUTPUT_FILE = Path(__file__).parent / "swagger" / "api_description.py"
SYNC_API_FROM_SWAGGER_DESTINATION = Path(__file__).parent / "swagger" / "generated_sync_api.py"
ASYNC_API_FROM_SWAGGER_DESTINATION = Path(__file__).parent / "swagger" / "generated_async_api.py"


def generate_api_description_from_swagger() -> None:
    generate_json_rpc_api_description("test_api_description", OPENAPI_DEFINITION_DESTINATION, DESCRIPTION_OUTPUT_FILE)


def generate_clients_and_collections() -> None:
    from .swagger.api_description import test_api_description  # type: ignore[import-untyped]

    generate_api_client(
        test_api_description,
        MockSyncApiBase,  # type: ignore[arg-type]
        path=SYNC_API_FROM_SWAGGER_DESTINATION,
        asynchronous=False,
    )

    generate_api_client(
        test_api_description,
        MockAsyncApiBase,  # type: ignore[arg-type]
        path=ASYNC_API_FROM_SWAGGER_DESTINATION,
    )

    generate_api_client(
        GENERATOR_TEST_SINGLE_API,  # type: ignore[arg-type]
        MockSyncApiBase,  # type: ignore[arg-type]
        path=SINGLE_SYNC_API_DESTINATION,
        asynchronous=False,
    )

    generate_api_client(
        GENERATOR_TEST_SINGLE_API,  # type: ignore[arg-type]
        MockAsyncApiBase,  # type: ignore[arg-type]
        path=SINGLE_ASYNC_API_DESTINATION,
    )

    generate_api_collection(
        GENERATOR_TEST_API_COLLECTION,
        MockSyncApiBase,  # type: ignore[arg-type]
        collection_name=SYNC_API_COLLECTION_NAME,
        path=COLLECTION_SYNC_API_DESTINATION,
        asynchronous=False,
    )

    generate_api_collection(
        GENERATOR_TEST_API_COLLECTION,
        MockAsyncApiBase,  # type: ignore[arg-type]
        collection_name=ASYNC_API_COLLECTION_NAME,
        path=COLLECTION_ASYNC_API_DESTINATION,
    )
