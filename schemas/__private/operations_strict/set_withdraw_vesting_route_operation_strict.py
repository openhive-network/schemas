from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName, Uint16t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class SetWithdrawVestingRouteOperationStrict(PreconfiguredBaseModel):
    from_account: AccountName
    to_account: AccountName
    percent: Uint16t
    auto_vest: bool
