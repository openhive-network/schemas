from __future__ import annotations

from typing import Final

from schemas.fields.integers import Uint32t
from schemas.operation import Operation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class CustomBaseOperation(Operation):
    @classmethod
    def offset(cls) -> None:  # type: ignore
        raise ValueError("Offset parameter not available")
