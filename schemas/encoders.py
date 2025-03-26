from __future__ import annotations

from pathlib import Path
from typing import Any

import msgspec
from msgspec.json import Encoder

from schemas.fields.serializable import Serializable


def enc_hook_base(obj: Any) -> Any:
    if isinstance(obj, Path):
        return str(obj)
    raise NotImplementedError(f"Objects of type {type(obj)} are not supported")


def enc_hook_legacy(obj: Any) -> Any:
    if isinstance(obj, Serializable):
        return obj.serialize_as_legacy()
    return enc_hook_base(obj)


def enc_hook_hf26(obj: Any) -> Any:
    if isinstance(obj, Serializable):
        return obj.serialize()
    return enc_hook_base(obj)


def get_legacy_encoder() -> Encoder:
    return msgspec.json.Encoder(enc_hook=enc_hook_legacy)


def get_hf26_encoder() -> Encoder:
    return msgspec.json.Encoder(enc_hook=enc_hook_hf26)
