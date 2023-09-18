from __future__ import annotations

from schemas.operation import Operation

__all__ = [
    "VirtualOperation",
]


class VirtualOperation(Operation):
    """Base class for all virtual operations"""
