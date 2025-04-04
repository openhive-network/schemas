from __future__ import annotations

from .json_rpc.asynchronous import create_endpoint as create_json_rpc_async_endpoint
from .json_rpc.synchronous import create_endpoint as create_json_rpc_endpoint

__all__ = [
    "create_json_rpc_async_endpoint",
    "create_json_rpc_endpoint",
]
