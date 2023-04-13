from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName, Uint16t
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class SetWithdrawVestingRouteOperation(PreconfiguredBaseModel):
    from_account: AccountName
    to_account: AccountName
    percent: Uint16t = 0
    auto_vest: bool = False
