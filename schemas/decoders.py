from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Annotated, Any

import msgspec
from msgspec.json import Decoder

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.market_history_api.fundaments_of_responses import BucketSizes
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
    base_type_handlers: dict[type, Callable[[Any], Any]] = {
        HiveInt: HiveInt,
        HiveDateTime: HiveDateTime,
        BucketSizes: BucketSizes,
        AssetNaiAmount: AssetNaiAmount,
        Sha256: Sha256,
        Version: Version,
        Int64t: Int64t,
        Uint64t: Uint64t,
        Path: Path,
        AnyAssetImpl: lambda obj: AnyAssetImpl.resolve(type_, obj),
    }

    handler = base_type_handlers.get(type_)
    if handler:
        return handler(obj)

    if Resolvable.is_resolvable(type_):
        return type_.resolve(type_, obj)  # type: ignore

    if issubclass(type_, InitValidator):
        return type_(obj)

    raise NotImplementedError(f"Objects of type {type_} are not supported")


def dec_hook_legacy(type_: type, obj: Any) -> Any:
    legacy_map: dict[type[Any], Callable[[Any], Any]] = {
        AssetVests: AssetVests.from_legacy,
        AssetHive: AssetHive.from_legacy,
        AssetHbd: AssetHbd.from_legacy,
    }
    handler = legacy_map.get(type_)
    if handler:
        return handler(obj)
    return dec_hook_base(type_, obj)


def dec_hook_hf26(type_: type, obj: Any) -> Any:
    hf26_map: dict[type[Any], Callable[[Any], Any]] = {
        AssetVests: AssetVests.from_nai,
        AssetHive: AssetHive.from_nai,
        AssetHbd: AssetHbd.from_nai,
    }
    handler = hf26_map.get(type_)
    if handler:
        return handler(obj)
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


def schema_hook(obj: Any) -> dict[str, str]:
    direct_map: dict[Any, dict[str, str]] = {
        Path: {"type": "string", "format": "path"},
        HiveDateTime: {"type": "string", "format": "date-time"},
        OptionallyEmpty: {"type": "str"},
        JsonString: {"type": "str"},
    }
    if obj in direct_map:
        return direct_map[obj]

    subclass_map: list[tuple[Any, dict[str, str]]] = [
        (HiveIntFactory, {"type": "integer"}),
        (ValidatorInt, {"type": "integer"}),
        (AssetBase, {"type": "asset"}),
        (ValidatorString, {"type": "str"}),
        (PreconfiguredBaseModel, {"type": "object"}),
    ]
    for base, result in subclass_map:
        if isinstance(obj, type) and issubclass(obj, base):
            return result

    raise NotImplementedError(f"Objects of type {obj} are not supported")
