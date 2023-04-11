from __future__ import annotations

from schemas.package.schemas.predefined import AccountName
from preconfigure_base_model import PreconfiguredBaseModel


class DeclineVotingRightsOperation(PreconfiguredBaseModel):
    account: AccountName
    decline: bool = True
