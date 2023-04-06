from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, AssetVests, LegacyAssetVests


class DelegateVestingSharesOperation(BaseModel, extra=Extra.forbid):
    delegator: AccountName
    delegatee: AccountName
    vesting_shares: AssetVests | LegacyAssetVests
