from __future__ import annotations

import pytest


@pytest.fixture(scope="session", autouse=True)
def generate_needed_modules() -> None:
    from .generate_clients_and_collections import generate_api_description_from_swagger

    generate_api_description_from_swagger()

    from .generate_clients_and_collections import generate_clients_and_collections

    generate_clients_and_collections()
