from __future__ import annotations

from typing import Any

import msgspec
from msgspec.json import Encoder

from schemas.fields.assets._base import AssetBase, AssetNaiAmount
from schemas.fields.basic import ValidatorString
from schemas.fields.hive_int import HiveInt
from schemas.fields.resolvables import Resolvable


def enc_hook_base(obj: Any) -> Any:
    if isinstance(obj, ValidatorString):
        return str(obj)
    if isinstance(obj, AssetNaiAmount):
        return str(obj.value)
    if isinstance(obj, HiveInt):
        return obj.safe_int_value
    raise NotImplementedError(f"Objects of type {type(obj)} are not supported")


def enc_hook_legacy(obj: Any) -> Any:
    if Resolvable.is_resolvable(obj):
        return obj.serialize_as_legacy()
    if isinstance(obj, AssetBase):
        return obj.as_legacy()
    return enc_hook_base(obj)


def enc_hook_hf26(obj: Any) -> Any:
    if Resolvable.is_resolvable(obj):
        return obj.serialize()
    if isinstance(obj, AssetBase):
        return obj.as_nai()
    return enc_hook_base(obj)


def get_legacy_encoder() -> Encoder:
    return msgspec.json.Encoder(enc_hook=enc_hook_legacy)


def get_hf26_encoder() -> Encoder:
    return msgspec.json.Encoder(enc_hook=enc_hook_hf26)
