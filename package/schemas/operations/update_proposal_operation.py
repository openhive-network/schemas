from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName, Int64t, AssetHbd, LegacyAssetHbd, HiveDateTime
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class UpdateProposalOperation(PreconfiguredBaseModel):
    proposal_id: Int64t
    creator: AccountName
    daily_pay: LegacyAssetHbd | AssetHbd
    subject: str
    permlink: str
    extensions: HiveDateTime
