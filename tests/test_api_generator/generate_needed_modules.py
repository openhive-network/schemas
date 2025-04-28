from __future__ import annotations

from pathlib import Path

from schemas.apis.api_client_generator._private.common.models_aliased import ApiDefinition
from schemas.apis.api_client_generator.api_description_generator.json_rpc import generate_api_description
from schemas.apis.api_client_generator.asynchronous.api_collection_generator import (
    generate_api_collection as generate_async_api_collection,
)
from schemas.apis.api_client_generator.asynchronous.single_api_generator import (
    generate_api_client as generate_async_api_client,
)
from schemas.apis.api_client_generator.synchronous.api_collection_generator import generate_api_collection
from schemas.apis.api_client_generator.synchronous.single_api_generator import generate_api_client
from tests.test_api_generator.api_collection_definition import GENERATOR_TEST_API_COLLECTION
from tests.test_api_generator.base_api_classes import TestAsyncApi, TestSyncApi

SYNC_API_COLLECTION_NAME = "GeneratedSyncApiCollection"
ASYNC_API_COLLECTION_NAME = "GeneratedAsyncApiCollection"

SINGLE_ASYNC_API_DESTINATION = Path(__file__).parent / "generated_async_single_api.py"
SINGLE_SYNC_API_DESTINATION = Path(__file__).parent / "generated_sync_single_api.py"
COLLECTION_ASYNC_API_DESTINATION = Path(__file__).parent / "generated_async_api_collection.py"
COLLECTION_SYNC_API_DESTINATION = Path(__file__).parent / "generated_sync_api_collection.py"
DESCRIPTION_DESTINATION = Path(__file__).parent / "api_description.py"


def generate_single_api_description() -> None:
    generate_api_description(Path(__file__).parent / "openapi.json", Path(__file__).parent / "api_description.py")


def generate_needed_modules(single_api_description: ApiDefinition) -> None:
    generate_api_client(
        single_api_description,
        TestSyncApi,
        path=SINGLE_SYNC_API_DESTINATION,
    )

    generate_async_api_client(
        single_api_description,
        TestAsyncApi,
        path=SINGLE_ASYNC_API_DESTINATION,
    )

    generate_api_collection(
        GENERATOR_TEST_API_COLLECTION,
        TestSyncApi,
        collection_name=SYNC_API_COLLECTION_NAME,
        path=COLLECTION_SYNC_API_DESTINATION,
    )

    generate_async_api_collection(
        GENERATOR_TEST_API_COLLECTION,
        TestAsyncApi,
        collection_name=ASYNC_API_COLLECTION_NAME,
        path=COLLECTION_ASYNC_API_DESTINATION,
    )


if __name__ == "__main__":
    generate_single_api_description()
    assert DESCRIPTION_DESTINATION.exists(), "API description file was not created."

    from tests.test_api_generator.api_description import test_api_description  # type: ignore[import-untyped]

    generate_needed_modules(test_api_description)
