from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class Policy:
    @abstractmethod
    def apply(self) -> None: ...


def set_policies(*policies: Policy) -> None:
    for policy in policies:
        policy.apply()
