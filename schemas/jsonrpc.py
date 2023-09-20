"""
Response from API has three poles -> id, jsonrpc and result. The factory method from HiveResult class is using to
return result pole, cause is must be validated deeper and then all operations is being performed on result field.
Yoy must use it like this -> HiveResult.factory(type_of_response, **response_from_api_json/dict).
"""
from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Generic, TypeVar

from pydantic import Field
from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel

__all__ = [
    "get_response_model",
    "ExpectResultT",
    "JSONRPCBase",
    "JSONRPCError",
    "JSONRPCRequest",
    "JSONRPCResult",
]

"""
Following union in TypeVar can be extended when new endpoints appear
"""
ExpectResultT = TypeVar(
    "ExpectResultT",
    bound=PreconfiguredBaseModel
    | Sequence[PreconfiguredBaseModel]
    | Sequence[PreconfiguredBaseModel | None]
    | str
    | int
    | None
    | Sequence[str]
    | Sequence[int]
    | Sequence[Sequence[str]]
    | Sequence[tuple[int, PreconfiguredBaseModel]],
)


class JSONRPCBase(PreconfiguredBaseModel):
    id_: int = Field(alias="id", default=0)
    jsonrpc: str = "2.0"


class JSONRPCRequest(JSONRPCBase):
    method: str
    params: dict[str, Any] = Field(default_factory=dict)


class JSONRPCError(JSONRPCBase):
    error: dict[str, Any]


class JSONRPCResult(JSONRPCBase, GenericModel, Generic[ExpectResultT]):
    result: ExpectResultT


def get_response_model(
    expected_model: type[ExpectResultT], **kwargs: Any
) -> JSONRPCResult[ExpectResultT] | JSONRPCError:
    """
    Use this method to create response model from the given parameters (as kwargs).

    This function is used to perform validation on the result field. You choose the expected type of the result field.
    In case when something is wrong and result field is not present, the JSONRPCError is returned.

    Args:
        expected_model: Expected type of the result field.
        **kwargs: Parameters to create response model.

    Returns:
        The response model.
    """
    response_cls = JSONRPCResult[expected_model] if "result" in kwargs else JSONRPCError  # type: ignore[valid-type]
    response_cls.update_forward_refs(**locals())
    return response_cls(**kwargs)  # type: ignore[return-value]
