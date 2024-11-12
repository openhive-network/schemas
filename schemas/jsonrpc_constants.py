"""
Response from API has three poles -> id, jsonrpc and result. The factory method from HiveResult class is using to
return result pole, cause is must be validated deeper and then all operations is being performed on result field.
Yoy must use it like this -> HiveResult.factory(type_of_response, **response_from_api_json/dict).
"""
from __future__ import annotations

from typing import Any

from pydantic import Field

from schemas._preconfigured_base_model import PreconfiguredBaseModel

__all__ = [
    "JSONRPCBase",
    "JSONRPCError",
    "JSONRPCRequest",
]

"""
Following union in TypeVar can be extended when new endpoints appear
"""


class JSONRPCBase(PreconfiguredBaseModel):
    id_: int = Field(alias="id", default=0)
    jsonrpc: str = "2.0"


class JSONRPCRequest(JSONRPCBase):
    method: str
    params: dict[str, Any] = Field(default_factory=dict)


class JSONRPCError(JSONRPCBase):
    error: dict[str, Any]
