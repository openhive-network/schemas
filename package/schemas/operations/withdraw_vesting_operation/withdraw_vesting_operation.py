from pydantic import BaseModel, Extra

from schemas.__private.fields_schemas import AccountName, LegacyAssetVests


class WithdrawVestingOperation(BaseModel, extra=Extra.forbid):
    account: AccountName
    vesting_shares: LegacyAssetVests
