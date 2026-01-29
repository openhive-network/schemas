from __future__ import annotations

from abc import abstractmethod
from typing import Any, Self

import msgspec

from schemas._preconfigured_base_model import PreconfiguredBaseModel


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
                return cls.parse_raw(value)
            except msgspec.DecodeError as error:
                raise ValueError(f"Value is not a valid application operation string! Received `{value}`") from error

        raise ValueError(f"Value is not a valid type! Received `{value}` with type `{type(value)}`")
