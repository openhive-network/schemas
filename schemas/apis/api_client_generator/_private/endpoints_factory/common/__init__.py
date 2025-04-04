from __future__ import annotations

from .asynchronous import create_endpoint as create_async_endpoint
from .synchronous import create_endpoint

__all__ = ["create_endpoint", "create_async_endpoint"]
