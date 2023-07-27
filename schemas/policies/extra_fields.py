from __future__ import annotations

from dataclasses import dataclass

from pydantic import Extra

from schemas.policies.policy import Policy
from schemas.preconfigured_base_model import PreconfiguredBaseModel


@dataclass
class ExtraFields(Policy):
    policy: Extra

    def apply(self) -> None:
        PreconfiguredBaseModel.Config.extra = self.policy
