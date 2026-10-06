"""
Response from API has three poles -> id, jsonrpc and result. The factory method from HiveResult class is using to
return result pole, cause is must be validated deeper and then all operations is being performed on result field.
Yoy must use it like this -> HiveResult.factory(type_of_response, **response_from_api_json/dict).
"""

from __future__ import annotations

import json as json_module
import os
import types
from collections.abc import Callable, Mapping, Sequence
from functools import cache
from threading import Event, Lock, Semaphore
from typing import Any, Final, Generic, Literal, TypeVar, Union, cast, get_args, get_origin

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

    When the expected type is built only of builtins and types providing `from_builtins` (generated public
    models), the response is NOT validated: the result is built from parsed JSON as is
    (see `_build_without_validation`). Otherwise (msgspec models, field types like `HiveInt` or `AccountName`)
    the result is decoded (and so validated) by msgspec.
    In case when result field is not present, the JSONRPCError is returned.

    Args:
        expected_model: Expected type of the result field.
        json: Raw JSON-RPC response.
        serialization: Serialization used by the response (`hf26` or `legacy`).

    Returns:
        The response model.
    """
    assert serialization in ("hf26", "legacy")
    if _is_buildable_without_validation(expected_model):  # type: ignore[arg-type]
        return _build_without_validation(expected_model, json)
    response_cls: type[JSONRPCResult[ExpectResultT] | JSONRPCError]
    response_cls = acquire_model(expected_model) if "result" in json else JSONRPCError
    return response_cls.parse_raw(json, (get_hf26_decoder if serialization == "hf26" else get_legacy_decoder))


def _build_without_validation(expected_model: Any, raw: str) -> JSONRPCResult[Any] | JSONRPCError:
    parsed = json_module.loads(raw)
    if not isinstance(parsed, dict) or "result" not in parsed:
        return msgspec.json.decode(raw, type=JSONRPCError)
    # result is assigned after construction, so PreconfiguredBaseModel type swapping (__post_init__) never touches it
    response: JSONRPCResult[Any] = JSONRPCResult(
        id_=parsed.get("id", 0), jsonrpc=parsed.get("jsonrpc", "2.0"), result=None
    )
    response.result = _result_builder(expected_model)(parsed["result"])
    return response


_BUILTIN_LEAVES: Final[frozenset[Any]] = frozenset({str, int, float, bool, bytes, type(None), Any})
_BUILTIN_CONTAINERS: Final[frozenset[Any]] = frozenset(
    {list, tuple, dict, Sequence, Mapping, Union, types.UnionType, Literal}
)


@cache
def _is_buildable_without_validation(type_: Any) -> bool:
    """Check if the type tree consists only of builtins and types providing `from_builtins`."""
    if type_ in _BUILTIN_LEAVES or type_ is None:
        return True
    if isinstance(type_, type) and callable(getattr(type_, "from_builtins", None)):
        return True
    origin = get_origin(type_)
    if origin is Literal:
        return True
    if origin not in _BUILTIN_CONTAINERS:
        return False
    return all(_is_buildable_without_validation(arg) for arg in get_args(type_) if arg is not Ellipsis)


@cache
def _result_builder(type_: Any) -> Callable[[Any], Any]:
    """
    Build nested results of types providing `from_builtins` (generated public models); leave everything else as is.

    No type checking is performed.
    """
    if isinstance(type_, type) and callable(from_builtins := getattr(type_, "from_builtins", None)):
        return lambda value: from_builtins(value) if isinstance(value, dict) else value

    origin = get_origin(type_)
    args = get_args(type_)
    if origin in (list, Sequence) and args:
        item = _result_builder(args[0])
        return lambda value: [item(element) for element in value] if isinstance(value, list) else value
    if origin in (Union, types.UnionType):
        candidates = [arg for arg in args if arg is not type(None)]
        if len(candidates) == 1:
            single = _result_builder(candidates[0])
            return lambda value: None if value is None else single(value)
    return lambda value: value
