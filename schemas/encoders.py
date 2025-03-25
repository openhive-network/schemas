from __future__ import annotations

from typing import Any

import msgspec
from msgspec.json import Encoder

from schemas.fields.assets._base import AssetBase, AssetNaiAmount
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.fields.resolvables import JsonString, OptionallyEmpty


def enc_hook_base(obj: Any) -> Any:
    if isinstance(obj, AssetNaiAmount):
        return str(obj.value)
    if isinstance(obj, HiveInt):
        return obj.safe_int_value
    if isinstance(obj, HiveDateTime):
        return obj.__str__()
    if isinstance(obj, OptionallyEmpty):
        return str(obj)
    return None


def enc_hook_legacy(obj: Any) -> Any:
    if isinstance(obj, JsonString):
        return obj.encode()
    if isinstance(obj, AssetBase):
        return obj.as_legacy()
    return enc_hook_base(obj)


def enc_hook_hf26(obj: Any) -> Any:
    if isinstance(obj, JsonString):
        return obj.encode()
    if isinstance(obj, AssetBase):
        return obj.as_nai()
    return enc_hook_base(obj)


def enc_hook_hf26_json(obj: Any) -> Any:
    if isinstance(obj, JsonString):
        return obj.encode_json()
    if isinstance(obj, AssetBase):
        return obj.as_nai()
    return enc_hook_base(obj)


def get_legacy_encoder() -> Encoder:
    return msgspec.json.Encoder(enc_hook=enc_hook_legacy)


def get_hf26_encoder() -> Encoder:
    return msgspec.json.Encoder(enc_hook=enc_hook_hf26)


def get_hf26_json_encoder() -> Encoder:
    return msgspec.json.Encoder(enc_hook=enc_hook_hf26_json)
