from __future__ import annotations

from abc import ABC, ABCMeta, abstractmethod
from typing import Any


class OverrideTypeNameMeta(ABCMeta):
    def __str__(cls) -> str:
        return cls.__name__


class Serializable(ABC, metaclass=OverrideTypeNameMeta):
    @abstractmethod
    def serialize(self) -> Any:
        ...

    def serialize_as_legacy(self) -> Any:
        return self.serialize()
