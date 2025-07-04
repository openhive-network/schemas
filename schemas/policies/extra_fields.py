from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from schemas.policies.policy import Policy


@dataclass
class ExtraFieldsPolicy(Policy):
    is_extra_fields_enabled: ClassVar[bool] = False
    allow: bool = False

    def apply(self) -> None:
        ExtraFieldsPolicy.is_extra_fields_enabled = self.allow

    @classmethod
    def is_allowed(cls) -> bool:
        return ExtraFieldsPolicy.is_extra_fields_enabled
