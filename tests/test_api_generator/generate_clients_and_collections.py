from __future__ import annotations

from pathlib import Path

from schemas.apis.api_client_generator import generate_api_client, generate_api_collection
from tests.test_api_generator.api_definition import GENERATOR_TEST_API_COLLECTION, GENERATOR_TEST_SINGLE_API
from tests.test_api_generator.base_api_classes import MockAsyncApiBase, MockSyncApiBase

SYNC_API_COLLECTION_NAME = "GeneratedSyncApiCollection"
ASYNC_API_COLLECTION_NAME = "GeneratedAsyncApiCollection"

SINGLE_ASYNC_API_DESTINATION = Path(__file__).parent / "generated_async_single_api.py"
SINGLE_SYNC_API_DESTINATION = Path(__file__).parent / "generated_sync_single_api.py"
COLLECTION_ASYNC_API_DESTINATION = Path(__file__).parent / "generated_async_api_collection.py"
COLLECTION_SYNC_API_DESTINATION = Path(__file__).parent / "generated_sync_api_collection.py"


def generate_clients_and_collections() -> None:
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
