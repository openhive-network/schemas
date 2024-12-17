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

        from schemas.operations import AnyHf26Operation

        return len(get_args(AnyHf26Operation))

    @classmethod
    def offset(cls) -> int:
        return super().offset() + cls.__get_first_vop_offset()

    @classmethod
    def vop_offset(cls) -> int:
        return super().offset()
