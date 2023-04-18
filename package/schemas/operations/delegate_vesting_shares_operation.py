from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, AssetVestsLegacy
    from schemas.types import AssetVests


class DelegateVestingSharesOperation(PreconfiguredBaseModel):
    delegator: AccountName
    delegatee: AccountName
    vesting_shares: AssetVests | AssetVestsLegacy
