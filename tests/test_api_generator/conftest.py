from __future__ import annotations

import pytest

from .generate_clients_and_collections import generate_clients_and_collections


@pytest.fixture(scope="session", autouse=True)
def generate_needed_modules() -> None:
    generate_clients_and_collections()
