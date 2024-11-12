from __future__ import annotations

from typing import Any

from schemas.jsonrpc_constants import JSONRPCBase, JSONRPCError
from schemas.jsonrpc_models.jsonrpc_models import get_jsonrpc_response_types_name


def get_response_model(expected_model: type, endpoint: str, /, **kwargs: Any) -> JSONRPCBase | JSONRPCError:
    model = get_jsonrpc_response_types_name(expected_model, endpoint) if "result" in kwargs else JSONRPCError
    filled_model = model(**kwargs)
    assert isinstance(filled_model, JSONRPCBase | JSONRPCError), "Model is in incorrect type"
    return filled_model
