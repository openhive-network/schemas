from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, LegacyAssetVests


class WithdrawVestingOperation(BaseModel, extra=Extra.forbid):
    account: AccountName
    vesting_shares: LegacyAssetVests
