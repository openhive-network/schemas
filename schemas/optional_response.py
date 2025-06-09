from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self


class OptionalResponse(ABC):
    @abstractmethod
    def is_set(self) -> bool:
        ...

    @property
    @abstractmethod
    def ensure(self) -> Self:
        ...
