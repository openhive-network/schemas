from __future__ import annotations

from schemas.package.schemas.predefined import AccountName, Uint16t
from preconfigure_base_model import PreconfiguredBaseModel


class SetWithdrawVestingRouteOperation(PreconfiguredBaseModel):
    from_account: AccountName
    to_account: AccountName
    percent: Uint16t = 0
    auto_vest: bool = False
