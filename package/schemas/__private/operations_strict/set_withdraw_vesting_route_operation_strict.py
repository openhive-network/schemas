from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, Uint16t


class SetWithdrawVestingRouteOperationStrict(PreconfiguredBaseModel):
    from_account: AccountName
    to_account: AccountName
    percent: Uint16t
    auto_vest: bool
