from __future__ import annotations

from schemas.package.schemas.predefined import AccountName, Int64t, AssetHbd, LegacyAssetHbd, HiveDateTime
from preconfigure_base_model import PreconfiguredBaseModel


class UpdateProposalOperation(PreconfiguredBaseModel):
    proposal_id: Int64t
    creator: AccountName
    daily_pay: LegacyAssetHbd | AssetHbd
    subject: str
    permlink: str
    extensions: HiveDateTime
