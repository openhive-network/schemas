from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, overload

from schemas.operation import Operation
from schemas.virtual_operation import VirtualOperation

if TYPE_CHECKING:
    from collections.abc import Callable


@dataclass
class Filter:
    low: int
    high: int


def split_filter(calculated_filter: int) -> Filter:
    high = calculated_filter >> 64
    low = calculated_filter & ~(high << 64)
    return Filter(high=high, low=low)


@overload
def _build_any_filter(get_filter: Callable[[type[Operation]], int], *ops: type[Operation]) -> int: ...


@overload
def _build_any_filter(get_filter: Callable[[type[VirtualOperation]], int], *ops: type[VirtualOperation]) -> int: ...


def _build_any_filter(
    get_filter: Callable[[type[Operation]], int] | Callable[[type[VirtualOperation]], int],
    *ops: type[Operation] | type[VirtualOperation],
) -> int:
    return sum([(2 ** get_filter(op)) for op in ops])  # type: ignore[arg-type]


def build_filter(*ops: type[Operation]) -> int:
    """
    Used to build a filter for a get_account_history

    Learn more: https://developers.hive.io/apidefinitions/#account_history_api.get_account_history
    """
    return _build_any_filter(lambda op: op.offset(), *ops)


def build_vop_filter(*vops: type[VirtualOperation]) -> int:
    """
    Used to build a filter for a enum_virtual_ops

    Learn more: https://developers.hive.io/apidefinitions/#account_history_api.enum_virtual_ops
    """

    def vop_offset(vop: type[VirtualOperation]) -> int:
        return vop.vop_offset()

    return _build_any_filter(vop_offset, *vops)
