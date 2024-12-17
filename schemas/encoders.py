from __future__ import annotations

from typing import Any

import msgspec
from msgspec.json import Encoder

from schemas.fields.assets._base import AssetHbd, AssetHive, AssetNaiAmount, AssetVests
from schemas.fields.hive_int import HiveInt
from schemas.fields.resolvables import JsonString


def enc_hook_base(obj: Any) -> Any:
    if isinstance(obj, AssetNaiAmount):
        return str(obj.value)
    if isinstance(obj, HiveInt):
        return obj.value
    if isinstance(obj, JsonString):
        return obj.value
    return None


def enc_hook_legacy(obj: Any) -> Any:
    if isinstance(obj, (AssetHbd | AssetHive | AssetVests)):
        return obj.as_legacy()
    return enc_hook_base(obj)


def enc_hook_hf26(obj: Any) -> Any:
    if isinstance(obj, (AssetHbd | AssetHive | AssetVests)):
        return obj.as_nai()
    return enc_hook_base(obj)


def get_legacy_encoder() -> Encoder:
    return msgspec.json.Encoder(enc_hook=enc_hook_legacy)


def get_hf26_encoder() -> Encoder:
    return msgspec.json.Encoder(enc_hook=enc_hook_hf26)
