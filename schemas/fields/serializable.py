from __future__ import annotations

from abc import ABC, ABCMeta, abstractmethod
from typing import Any


class OverrideTypeNameMeta(ABCMeta):
    def __str__(cls) -> str:
        return cls.__name__


class Serializable(ABC, metaclass=OverrideTypeNameMeta):
    @abstractmethod
    def serialize(self) -> Any:
        """
        Serialize the object to a format suitable for storage or transmission.
        This method should be implemented by subclasses to define how the object
        is converted to a serializable format.
        """

    def serialize_as_legacy(self) -> Any:
        return self.serialize()

    def serialize_as_legacy_testnet(self) -> Any:
        return self.serialize_as_legacy()
