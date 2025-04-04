from __future__ import annotations

from .asynchronous.single_api_generator import generate_api_client as generate_async_api_client
from .synchronous.single_api_generator import generate_api_client as generate_sync_api_client

__all__ = ["generate_async_api_client", "generate_sync_api_client"]
