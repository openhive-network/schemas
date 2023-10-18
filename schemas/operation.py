from __future__ import annotations

from dataclasses import dataclass

from schemas._preconfigured_base_model import PreconfiguredBaseModel

__all__ = [
    "Operation",
]


class Operation(PreconfiguredBaseModel):
    """Base class for all operations to provide valid json serialization"""

    __operation_name__: str
    __offset__: int

    @classmethod
    def get_name(cls) -> str:
        """
        Get the name of the operation.

        e.g. `transfer` for `TransferOperation`
        """
        return cls.__operation_name__

    @classmethod
    def get_name_with_suffix(cls) -> str:
        """
        Get the name of the operation with the `_operation` suffix.

        e.g. `transfer_operation` for `TransferOperation`
        """
        return f"{cls.get_name()}_operation"

    @classmethod
    def offset(cls) -> int:
        return cls.__offset__


def build_filter(*ops: type[Operation]) -> int:
    return sum([(2 ** op.offset()) for op in ops])


@dataclass
class Filter:
    low: int
    high: int


def split_filter(calculated_filter: int) -> Filter:
    high = calculated_filter >> 64
    low = calculated_filter & ~(high << 64)
    return Filter(high=high, low=low)
