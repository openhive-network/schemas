from __future__ import annotations

import json
from abc import abstractmethod
from typing import TYPE_CHECKING, Any, Literal

import msgspec
from typing_extensions import Self

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.decoders import get_hf26_decoder
from schemas.encoders import enc_hook_base

if TYPE_CHECKING:
    from collections.abc import Iterable


class ApplicationOperation(PreconfiguredBaseModel):
    @classmethod
    @abstractmethod
    def get_name(cls) -> str:
        """
        Get the name of the operation.

        e.g. `transfer` for `TransferOperation`
        """

    @classmethod
    def validate(cls, value: Any) -> Self:
        if isinstance(value, cls):
            return value

        if isinstance(value, str):
            try:
                decoder = get_hf26_decoder(cls)
                return decoder.decode(value)
            except msgspec.DecodeError as error:
                raise ValueError(f"Value is not a valid application operation string! Received `{value}`") from error

        raise ValueError(f"Value is not a valid type! Received `{value}` with type `{type(value)}`")

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
            ),
            separators=(",", ":"),
        )
