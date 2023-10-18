from __future__ import annotations

from schemas.operation import Operation

__all__ = [
    "VirtualOperation",
]


class VirtualOperation(Operation):
    """Base class for all virtual operations"""

    @classmethod
    def __get_first_vop_offset(cls) -> int:
        from typing import get_args

        from schemas.operations import AnyOperation

        return len(get_args(AnyOperation))

    @classmethod
    def offset(cls) -> int:
        return super().offset() + cls.__get_first_vop_offset()

    @classmethod
    def vop_offset(cls) -> int:
        return super().offset()


def build_vop_filter(*vops: type[VirtualOperation]) -> int:
    return sum([(2**vop.vop_offset()) for vop in vops])
