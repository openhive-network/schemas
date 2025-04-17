from __future__ import annotations

from pathlib import Path

from schemas.apis.api_client_generator.asynchronous.api_collection_generator import (
    generate_api_collection as generate_async_api_collection,
)
from schemas.apis.api_client_generator.asynchronous.single_api_generator import (
    generate_api_client as generate_async_api_client,
)
from schemas.apis.api_client_generator.synchronous.api_collection_generator import generate_api_collection
from schemas.apis.api_client_generator.synchronous.single_api_generator import generate_api_client
from tests.test_api_generator.api_definition import GENERATOR_TEST_API_COLLECTION, GENERATOR_TEST_SINGLE_API
from tests.test_api_generator.base_api_classes import TestAsyncApi, TestSyncApi

SYNC_API_COLLECTION_NAME = "GeneratedSyncApiCollection"
ASYNC_API_COLLECTION_NAME = "GeneratedAsyncApiCollection"

SINGLE_ASYNC_API_DESTINATION = Path(__file__).parent / "generated_async_single_api.py"
SINGLE_SYNC_API_DESTINATION = Path(__file__).parent / "generated_sync_single_api.py"
COLLECTION_ASYNC_API_DESTINATION = Path(__file__).parent / "generated_async_api_collection.py"
COLLECTION_SYNC_API_DESTINATION = Path(__file__).parent / "generated_sync_api_collection.py"


def generate_needed_modules() -> None:
    generate_api_client(
        GENERATOR_TEST_SINGLE_API,  # type: ignore[arg-type]
        TestSyncApi,
        path=SINGLE_SYNC_API_DESTINATION,
    )

    generate_async_api_client(
        GENERATOR_TEST_SINGLE_API,  # type: ignore[arg-type]
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
    generate_needed_modules()
