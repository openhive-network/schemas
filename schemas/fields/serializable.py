from __future__ import annotations

from abc import ABC, ABCMeta, abstractmethod
from typing import Any, Self


class OverrideTypeNameMeta(ABCMeta):
    def __str__(cls) -> str:
        return cls.__name__


class Serializable(ABC, metaclass=OverrideTypeNameMeta):
    """
    Field type with its own JSON form - decoded by `deserialize` (`schemas.decoders`) and encoded by `serialize`
    (`schemas.encoders`).
    """

    def __new__(cls, *args: Any, **kwargs: Any) -> Serializable:
        if super().__new__ == object.__new__:
            return super().__new__(cls)
        return super().__new__(cls, *args, **kwargs)

    @classmethod
    def deserialize(cls, value: object) -> Self:
        """Create the object from its JSON form. By default by the constructor."""
        return cls(value)

    @abstractmethod
    def serialize(self) -> Any:
        """Return the JSON form of the object."""
