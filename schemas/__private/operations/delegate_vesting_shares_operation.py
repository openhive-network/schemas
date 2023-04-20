from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName
from schemas.__private.hive_fields_schemas_strict import AssetVestsStrict
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class DelegateVestingSharesOperation(PreconfiguredBaseModel):
    delegator: AccountName
    delegatee: AccountName
    vesting_shares: AssetVestsStrict
