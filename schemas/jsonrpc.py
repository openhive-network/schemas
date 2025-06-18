"""
Response from API has three poles -> id, jsonrpc and result. The factory method from HiveResult class is using to
return result pole, cause is must be validated deeper and then all operations is being performed on result field.
Yoy must use it like this -> HiveResult.factory(type_of_response, **response_from_api_json/dict).
"""

from __future__ import annotations

import os
from collections.abc import Sequence
from threading import Event, Lock, Semaphore
from typing import Any, Generic, Literal, TypeVar, cast

import msgspec

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.decoders import get_hf26_decoder, get_legacy_decoder

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
ExpectResult = (
    PreconfiguredBaseModel
    | Sequence[PreconfiguredBaseModel]
    | Sequence[PreconfiguredBaseModel | None]
    | str
    | int
    | None
    | Sequence[str]
    | Sequence[int]
    | Sequence[Sequence[str]]
    | Sequence[tuple[int, PreconfiguredBaseModel]]
)

ExpectResultT = TypeVar(
    "ExpectResultT",
    bound=ExpectResult,
)

CACHED_MODELS: dict[type[Any], JSONRPCResult[Any]] = {}
WRITE_LOCK = Lock()
WRITE_LOCK_EVENT = Event()
MAX_THREADS = os.cpu_count() or 10000
READ_SEMAPHORE = Semaphore(value=MAX_THREADS)


class JSONRPCBase(PreconfiguredBaseModel, kw_only=True, omit_defaults=False):
    id_: int = msgspec.field(name="id", default=0)
    jsonrpc: str = "2.0"


class JSONRPCRequest(JSONRPCBase):
    method: str
    params: dict[str, Any] = msgspec.field(default_factory=dict)


class JSONRPCError(JSONRPCBase):
    error: dict[str, Any]


class JSONRPCResult(JSONRPCBase, Generic[ExpectResultT]):
    result: ExpectResultT


def acquire(n: int) -> None:
    acquired = 0
    while acquired != n:
        acquired += int(READ_SEMAPHORE.acquire())


def acquire_model(expected_model: type[ExpectResultT]) -> type[JSONRPCResult[ExpectResultT]]:
    if WRITE_LOCK.locked():
        WRITE_LOCK_EVENT.wait()

    READ_SEMAPHORE.acquire()
    try:
        if expected_model in CACHED_MODELS:
            return CACHED_MODELS[expected_model]  # type: ignore[return-value]

        WRITE_LOCK_EVENT.clear()
        try:
            with WRITE_LOCK:
                acquire(MAX_THREADS - 1)
                try:
                    JSONRPCResultImpl = msgspec.defstruct(  # noqa: N806
                        "JSONRPCResultImpl", [("result", expected_model)], bases=(JSONRPCResult,)
                    )

                    CACHED_MODELS[expected_model] = JSONRPCResultImpl  # type: ignore[assignment]

                    return cast(type[JSONRPCResult[Any]], JSONRPCResultImpl)
                finally:
                    READ_SEMAPHORE.release(n=MAX_THREADS - 1)
        finally:
            WRITE_LOCK_EVENT.set()
    finally:
        READ_SEMAPHORE.release()


def get_response_model(
    expected_model: type[ExpectResultT], json: str, serialization: Literal["hf26", "legacy"]
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
    assert serialization in ("hf26", "legacy")
    response_cls: type[JSONRPCResult[ExpectResultT] | JSONRPCError]
    response_cls = acquire_model(expected_model) if "result" in json else JSONRPCError
    return response_cls.parse_raw(json, (get_hf26_decoder if serialization == "hf26" else get_legacy_decoder))
