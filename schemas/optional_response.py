from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self


class OptionalResponse:
    def is_set(self) -> bool:
        raise NotImplementedError("This method should be implemented in subclasses")

    @property
    def ensure(self) -> Self:
        raise NotImplementedError("This method should be implemented in subclasses")
