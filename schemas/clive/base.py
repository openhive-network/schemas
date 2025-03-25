from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Callable, Final, Literal, Protocol

import msgspec
from msgspec.json import Decoder, T

from schemas._preconfigured_base_model import DictStrAny
from schemas.encoders import enc_hook_base
from schemas.fields.serializable import Serializable

if TYPE_CHECKING:
    from collections.abc import Iterable

TIME_FORMAT_WITH_SECONDS: Final[str] = "%Y-%m-%dT%H:%M:%S"


class CliveBaseModel(msgspec.Struct):
    class Config:
        allow_population_by_field_name = True
        json_encoders = {  # noqa: RUF012;
            datetime: lambda d: d.strftime(TIME_FORMAT_WITH_SECONDS),
            Serializable: lambda x: x.serialize(),
        }

    def json(
        self,
        *,
        str_keys: bool = False,
        builtin_types: Iterable[type] | None = None,
        order: Literal[None, "deterministic", "sorted"] = None,
    ) -> str:
        return json.dumps(
            msgspec.to_builtins(
                obj=self, enc_hook=enc_hook_base, str_keys=str_keys, builtin_types=builtin_types, order=order
            )
        )

    def dict(  # noqa: A003
        self,
        *,
        str_keys: bool = False,
        builtin_types: Iterable[type] | None = None,
        order: Literal[None, "deterministic", "sorted"] = None,
    ) -> DictStrAny:
        output = msgspec.to_builtins(
            obj=self, enc_hook=enc_hook_base, str_keys=str_keys, builtin_types=builtin_types, order=order
        )
        assert isinstance(output, dict), f"Invalid format: {type(output)}, required dict"
        return output

    @classmethod
    def parse_file(cls, path: Path, decoder_factory: Callable[[type[T]], msgspec.json.Decoder[T]]) -> type[CliveBaseModel]:
        with Path.open(path, encoding="utf-8") as file:
            raw = file.read()
            return cls.parse_raw(raw, decoder_factory)

    @classmethod
    def parse_raw(cls, raw: str, decoder_factory: Callable[[type[T]], msgspec.json.Decoder[T]]) -> type[CliveBaseModel]:
        decoder = decoder_factory(cls)
        return decoder.decode(raw)


class DecoderFactory(Protocol):
    def __call__(self, cls: type[CliveBaseModel]) -> Decoder[type[CliveBaseModel]]:
        ...
