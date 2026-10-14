"""
Decoding of Hive types from JSON by msgspec (`dec_hook`).

Hive types have a fixed JSON form (e.g. `AssetHive` - NAI form, `LegacyAssetHive` - legacy form) - they decode
themselves (`Serializable.deserialize`).
"""

from __future__ import annotations

import threading
from collections.abc import Callable
from pathlib import Path
from typing import Any, get_origin

import msgspec
from msgspec.json import Decoder

from schemas.fields.serializable import Serializable

DecoderFactory = Callable[[type[msgspec.Struct]], Decoder[msgspec.Struct]]

# Lock to protect against race conditions during concurrent decoder creation.
# msgspec's type annotation resolution is not thread-safe in Python 3.14.
_decoder_lock = threading.Lock()


def dec_hook_hf26(type_: type, obj: Any) -> Any:
    cls: type = get_origin(type_) or type_  # generic types (e.g. `JsonString[object]`) are given with their parameters
    if cls is object:  # any value (e.g. an item of a free-form JSON array) is kept as it is
        return obj
    if issubclass(cls, Serializable):
        return cls.deserialize(obj)
    if cls is Path:
        return Path(obj)
    raise NotImplementedError(f"Objects of type {type_} are not supported")


def get_hf26_decoder(type_: type[msgspec.Struct]) -> Decoder[msgspec.Struct]:
    with _decoder_lock:
        return msgspec.json.Decoder(type_, dec_hook=dec_hook_hf26)
