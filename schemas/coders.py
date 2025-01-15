

from typing import Any, Type, get_origin

import msgspec
from msgspec.json import Decoder
from schemas.apis.market_history_api.fundaments_of_responses import BucketSizes
from schemas.fields.assets._base import AssetHbd, AssetHive, AssetNaiAmount, AssetVest
from schemas.fields.basic import Permlink, PublicKey, Url
from schemas.fields.hex import Hex, Sha256, TransactionId
from schemas.fields.hive_int import HiveInt
from schemas.fields.resolvables import AnyAsset, Resolvable
from schemas.fields.version import Version


def dec_hook_base(type: Type, obj: Any) -> Any:
    if type is HiveInt:
        return HiveInt(obj)
    if type is BucketSizes:
        return BucketSizes(obj)
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
    if type is Url:
        return Url(obj)
    if type is AnyAsset:
        return AnyAsset.resolve(type, obj)
    # if isinstance(obj, JsonString):
    #     return obj.value

    orig_type = get_origin(type)
    if orig_type is not None and issubclass(orig_type, Resolvable):
        return type.resolve(type, obj)
    else:
        raise NotImplementedError(f"Objects of type {type} are not supported")

def dec_hook_legacy(type: Type, obj: Any) -> Any:
    if type is AssetVest:
        return AssetVest.from_legacy(obj)
    if type is AssetHive:
        return AssetHive.from_legacy(obj)
    if type is AssetHbd:
        return AssetHbd.from_legacy(obj)
    return dec_hook_base(type, obj)

def dec_hook_hf26(type: Type, obj: Any) -> Any:
    if type is AssetVest:
        return AssetVest.from_nai(obj)
    if type is AssetHive:
        return AssetHive.from_nai(obj)
    if type is AssetHbd:
        return AssetHbd.from_nai(obj)
    return dec_hook_base(type, obj)

def get_legacy_decoder(type_: type) -> Decoder:
    return msgspec.json.Decoder(type_, dec_hook=dec_hook_legacy)

def get_hf26_decoder(type_: type) -> Decoder:
    return msgspec.json.Decoder(type_, dec_hook=dec_hook_hf26)
