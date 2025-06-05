from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from schemas.policies.policy import Policy


class Extra(str, Enum):
    allow = "allow"
    ignore = "ignore"
    forbid = "forbid"


@dataclass
class ExtraFields(Policy):
    policy: Extra

    def apply(self) -> None:
        pass
