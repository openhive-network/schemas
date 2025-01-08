from __future__ import annotations

from typing import Final

from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint16t
from schemas.operation import Operation

DEFAULT_PERCENT: Final[Uint16t] = Uint16t(0)
DEFAULT_AUTO_VEST: Final[bool] = False


class SetWithdrawVestingRouteOperation(Operation):
    from_account: AccountName
    to_account: AccountName
    percent: Uint16t = DEFAULT_PERCENT
    auto_vest: bool = DEFAULT_AUTO_VEST

    @classmethod
    def get_name(cls) -> str:
        return "set_withdraw_vesting_route"

    @classmethod
    def offset(cls) -> int:
        return 20
