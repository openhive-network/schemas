"""
Response from API has three poles -> id, jsonrpc and result. The factory method from HiveResult class is using to
return result pole, cause is must be validated deeper and then all operations is being performed on result field.
Yoy must use it like this -> HiveResult.factory(type_of_response, **response_from_api_json/dict).
"""
from __future__ import annotations

import os
from collections.abc import Sequence
from threading import Event, Lock, Semaphore
from typing import Any, Generic, Type, TypeVar, get_origin, get_args

import msgspec
from pydantic import Field

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.condenser_api.response_schemas import GetDiscussionsByBlog
from schemas.apis.market_history_api.fundaments_of_responses import BucketSizes
from schemas.fields.assets._base import AssetHbd, AssetHive, AssetNaiAmount, AssetVest
from schemas.fields.basic import Permlink, PublicKey, OptionallyEmpty, AccountName
from schemas.fields.hex import Hex, Sha256, TransactionId
from schemas.fields.hive_int import HiveInt
from schemas.fields.version import Version

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


class JSONRPCBase(msgspec.Struct, kw_only=True):
    id: int = 0
    jsonrpc: str = "2.0"


class JSONRPCRequest(JSONRPCBase):
    method: str
    params: dict[str, Any] = Field(default_factory=dict)


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

                    # class JSONRPCResultImpl(JSONRPCResult[expected_model]):  # type: ignore[valid-type]
                    #     result: expected_model  # type: ignore[valid-type]
                    JSONRPCResultImpl = msgspec.defstruct("JSONRPCResultImpl", [("result", expected_model)], bases=(JSONRPCResult,))

                    CACHED_MODELS[expected_model] = JSONRPCResultImpl  # type: ignore[assignment]

                    return JSONRPCResultImpl
                finally:
                    READ_SEMAPHORE.release(n=MAX_THREADS - 1)
        finally:
            WRITE_LOCK_EVENT.set()
    finally:
        READ_SEMAPHORE.release()

def testnet_hf26_dec_hook(type: Type, obj: Any) -> Any:
    if type is HiveInt:
        return HiveInt(obj)
    if type is BucketSizes:
        return BucketSizes(obj)
    # if type is AssetVest:
    #     return AssetVest.from_nai(obj)
    # if type is AssetHive:
    #     return AssetHive.from_nai(obj)
    # if type is AssetHbd:
    #     return AssetHbd.from_nai(obj)
    if type is AssetNaiAmount:
        return AssetNaiAmount(obj)
    if type is Permlink:
        return Permlink(obj)
    if type is PublicKey:
        return PublicKey(obj)
    if type is Sha256:
        return Sha256(obj)
    if type is Version:
        return Version(obj)
    if type is TransactionId:
        return TransactionId(obj)
    if type is Hex:
        return Hex(obj)
    orig_type = get_origin(type)
    if orig_type is not None and orig_type is OptionallyEmpty:
        return OptionallyEmpty.resolve(type, obj)
    else:
        raise NotImplementedError(f"Objects of type {type} are not supported")

def get_response_model(
    expected_model: type[ExpectResultT], json: str
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
    response_cls: type[JSONRPCResult[ExpectResultT] | JSONRPCError]
    response_cls = acquire_model(expected_model) # if "result" in kwargs else JSONRPCError

    # response_cls.update_forward_refs(**locals())
    testnet_hf26_decoder = msgspec.json.Decoder(response_cls, dec_hook=testnet_hf26_dec_hook)
    msg = testnet_hf26_decoder.decode(json)

    try:
        return testnet_hf26_decoder.decode(json)
    except msgspec.ValidationError:
        return msgspec.json.decode(json, type=JSONRPCError)
