from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Serializable(ABC):
    @abstractmethod
    def serialize(self) -> Any:
        ...

    def serialize_as_legacy(self) -> Any:
        return self.serialize()
