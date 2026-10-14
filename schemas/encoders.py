"""
Encoding of Hive types to JSON by msgspec (`enc_hook`).

Hive types have a fixed JSON form (e.g. `AssetHive` - NAI form, `LegacyAssetHive` - legacy form) - they encode
themselves (`Serializable.serialize`).
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from msgspec.json import Encoder

from schemas.fields.serializable import Serializable


def enc_hook_hf26(obj: Any) -> Any:
    if isinstance(obj, Serializable):
        return obj.serialize()
    if isinstance(obj, Path):
        return str(obj)
    raise NotImplementedError(f"Objects of type {type(obj)} are not supported")


def get_hf26_encoder() -> Encoder:
    return Encoder(enc_hook=enc_hook_hf26)
