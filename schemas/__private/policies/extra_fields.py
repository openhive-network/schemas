from __future__ import annotations

from dataclasses import dataclass

from pydantic import Extra

from schemas.__private.policies.policy import Policy
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


@dataclass
class ExtraFields(Policy):
    policy: Extra

    def apply(self) -> None:
        PreconfiguredBaseModel.Config.extra = self.policy
