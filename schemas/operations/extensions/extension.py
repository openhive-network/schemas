from __future__ import annotations
from abc import abstractmethod

from schemas._preconfigured_base_model import PreconfiguredBaseModel


class OperationExtension(PreconfiguredBaseModel):

    @classmethod
    @abstractmethod
    def get_name(cls) -> str:
        """
        Get the name of the operation.

        e.g. `transfer` for `TransferOperation`
        """
