from __future__ import annotations

from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, Uint16t


class SetWithdrawVestingRouteOperation(BaseModel, extra=Extra.forbid):
    from_account: AccountName
    to_account: AccountName
    percent: Uint16t = 0
    auto_vest: bool = False
    