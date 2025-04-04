from __future__ import annotations

from collections.abc import Callable
from typing import Annotated, Any, get_origin

import msgspec
from msgspec.json import Decoder

from schemas.apis.market_history_api.fundaments_of_responses import BucketSizes
from schemas.apis.wallet_bridge_api.response_schemas import _GetActiveWitnesseslist
from schemas.fields.assets._base import AssetHbd, AssetHive, AssetNaiAmount, AssetVests
from schemas.fields.basic import Permlink, PublicKey
from schemas.fields.hex import Sha256
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.fields.integers import Int64t, Uint64t
from schemas.fields.resolvables import AnyAssetImpl, Resolvable
from schemas.fields.version import Version

DecoderFactory = Callable[[type[msgspec.Struct]], Decoder[msgspec.Struct]]


def dec_hook_base(type_: type, obj: Any) -> Any:
    type_handlers: dict[type, Callable[[Any], Any]] = {
        HiveInt: HiveInt,
        HiveDateTime: HiveDateTime,
        BucketSizes: BucketSizes,
        AssetNaiAmount: AssetNaiAmount,
        Permlink: Permlink,
        PublicKey: PublicKey,
        Sha256: Sha256,
        Version: Version,
        Int64t: Int64t,
        Uint64t: Uint64t,
        # TransactionId: TransactionId,
        # Hex: Hex,
        # Url: Url,
        # CustomIdType: CustomIdType,
        _GetActiveWitnesseslist: _GetActiveWitnesseslist,
        AnyAssetImpl: lambda obj: AnyAssetImpl.resolve(type_, obj),
    }

    handler = type_handlers.get(type_)
    if handler:
        return handler(obj)

    orig_type = get_origin(type_)
    if orig_type is not None and issubclass(orig_type, Resolvable):
        return type_.resolve(type_, obj)  # type: ignore

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


def is_matching_model(data: Any, annotated_model: Annotated[Any, ...]) -> bool:
    try:
        msgspec.convert(data, type=annotated_model)
    except msgspec.ValidationError:
        return False
    return True
