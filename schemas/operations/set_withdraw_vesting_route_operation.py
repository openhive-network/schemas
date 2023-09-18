from __future__ import annotations

from typing import Final

from schemas.fields.basic import AccountName, Uint16t
from schemas.operation import Operation

DEFAULT_PERCENT: Final[Uint16t] = Uint16t(0)
DEFAULT_AUTO_VEST: Final[bool] = False


class SetWithdrawVestingRouteOperation(Operation):
    __operation_name__ = "set_withdraw_vesting_route"

    from_account: AccountName
    to_account: AccountName
    percent: Uint16t = DEFAULT_PERCENT
    auto_vest: bool = DEFAULT_AUTO_VEST
