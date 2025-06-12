from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from schemas.policies.policy import Policy


@dataclass
class DisableSwapTypes(Policy):
    is_swap_types_disabled: ClassVar[bool] = False
    disabled: bool = False

    def apply(self) -> None:
        DisableSwapTypes.is_swap_types_disabled = self.disabled

    @classmethod
    def is_disabled(cls) -> bool:
        return DisableSwapTypes.is_swap_types_disabled
