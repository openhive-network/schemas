from __future__ import annotations

from schemas._preconfigured_base_model import PreconfiguredBaseModel


class Operation(PreconfiguredBaseModel):
    """Base class for all operations to provide valid json serialization"""

    __operation_name__: str

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
