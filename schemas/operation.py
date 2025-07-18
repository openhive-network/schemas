from __future__ import annotations

from abc import abstractmethod

from schemas._preconfigured_base_model import PreconfiguredBaseModel

__all__ = ["Operation", "OperationExtension"]


class OperationAndOperationExtensionBase(PreconfiguredBaseModel):
    """Base class for Operation and OperationExtension"""

    @classmethod
    @abstractmethod
    def get_name(cls) -> str:
        """
        Get the name of the operation.

        e.g. `transfer` for `TransferOperation`
        """

    @classmethod
    def get_name_with_suffix(cls) -> str:
        """
        Get the name of the operation with the `_operation` suffix.

        e.g. `transfer_operation` for `TransferOperation`
        """
        return f"{cls.get_name()}_operation"


class OperationExtension(OperationAndOperationExtensionBase):
    """Base class for all operation extensions to provide valid json serialization"""


class Operation(OperationAndOperationExtensionBase):
    """Base class for all operations to provide valid json serialization"""

    @classmethod
    @abstractmethod
    def offset(cls) -> int:
        """Get the offset of the operation."""
