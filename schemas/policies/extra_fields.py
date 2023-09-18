from __future__ import annotations

from dataclasses import dataclass

from pydantic import Extra

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.policies.policy import Policy


@dataclass
class ExtraFields(Policy):
    policy: Extra

    def apply(self) -> None:
        PreconfiguredBaseModel.Config.extra = self.policy
