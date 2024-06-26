from __future__ import annotations

from abc import ABC, abstractmethod


class Serializable(ABC):
    @abstractmethod
    def serialize(self) -> str:
        """Returns a json representation of the object"""
