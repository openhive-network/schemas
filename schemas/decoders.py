from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Annotated, Any

import msgspec
from msgspec.json import Decoder

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.condenser_api.response_schemas import GetSavingsWithdrawTo
from schemas.apis.market_history_api.fundaments_of_responses import BucketSizes
from schemas.apis.wallet_bridge_api.response_schemas import _GetActiveWitnesseslist
from schemas.fields._init_validators import InitValidator, ValidatorInt, ValidatorString
from schemas.fields.assets._base import AssetBase, AssetHbd, AssetHive, AssetNaiAmount, AssetVests
from schemas.fields.hex import Sha256
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt, HiveIntFactory
from schemas.fields.integers import Int64t, Uint64t
from schemas.fields.resolvables import AnyAssetImpl, JsonString, OptionallyEmpty, Resolvable
from schemas.fields.version import Version

DecoderFactory = Callable[[type[msgspec.Struct]], Decoder[msgspec.Struct]]


def dec_hook_base(type_: type, obj: Any) -> Any:
    type_handlers: dict[type, Callable[[Any], Any]] = {
        HiveInt: HiveInt,
        HiveDateTime: HiveDateTime,
        BucketSizes: BucketSizes,
        AssetNaiAmount: AssetNaiAmount,
        Sha256: Sha256,
        Version: Version,
        Int64t: Int64t,
        Uint64t: Uint64t,
        Path: Path,
        _GetActiveWitnesseslist: _GetActiveWitnesseslist,
        GetSavingsWithdrawTo: GetSavingsWithdrawTo,
        AnyAssetImpl: lambda obj: AnyAssetImpl.resolve(type_, obj),
    }

    handler = type_handlers.get(type_)
    if handler:
        return handler(obj)

    if Resolvable.is_resolvable(type_):
        return type_.resolve(type_, obj)  # type: ignore

    if issubclass(type_, InitValidator):
        return type_(obj)

    raise NotImplementedError(f"Objects of type {type_} are not supported")


def dec_hook_legacy(type_: type, obj: Any) -> Any:
    if type_ is AssetVests:
        return AssetVests.from_legacy(obj)
    if type_ is AssetHive:
        return AssetHive.from_legacy(obj)
    if type_ is AssetHbd:
        return AssetHbd.from_legacy(obj)
    return dec_hook_base(type_, obj)


def dec_hook_hf26(type_: type, obj: Any) -> Any:
    if type_ is AssetVests:
        return AssetVests.from_nai(obj)
    if type_ is AssetHive:
        return AssetHive.from_nai(obj)
    if type_ is AssetHbd:
        return AssetHbd.from_nai(obj)
    return dec_hook_base(type_, obj)


def get_legacy_decoder(type_: type[msgspec.Struct]) -> Decoder[msgspec.Struct]:
    return msgspec.json.Decoder(type_, dec_hook=dec_hook_legacy)


def get_hf26_decoder(type_: type[msgspec.Struct]) -> Decoder[msgspec.Struct]:
    return msgspec.json.Decoder(type_, dec_hook=dec_hook_hf26)


def validate_schema_field(data: Any, annotated_model: Annotated[Any, ...]) -> Annotated[Any, ...]:
    return annotated_model(data)


def is_matching_model(data: Any, annotated_model: Annotated[Any, ...]) -> bool:
    try:
        validate_schema_field(data, annotated_model)
    except msgspec.ValidationError:
        return False
    return True


def schema_hook(obj: Any) -> dict[str, str]:  # noqa: PLR0911
    if obj is Path:
        return {"type": "string", "format": "path"}
    if obj is HiveDateTime:
        return {"type": "string", "format": "date-time"}
    if obj is OptionallyEmpty:
        return {"type": "str"}
    if obj is JsonString:
        return {"type": "str"}
    if issubclass(obj, HiveIntFactory):
        return {"type": "integer"}
    if issubclass(obj, ValidatorInt):
        return {"type": "integer"}
    if issubclass(obj, AssetBase):
        return {"type": "asset"}
    if issubclass(obj, ValidatorString):
        return {"type": "str"}
    if issubclass(obj, PreconfiguredBaseModel):
        return {"type": "object"}

    raise NotImplementedError(f"Objects of type {obj} are not supported")
