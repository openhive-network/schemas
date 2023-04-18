from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, AssetHbd, HiveDateTime, Int64t, LegacyAssetHbd


class UpdateProposalOperation(PreconfiguredBaseModel):
    proposal_id: Int64t
    creator: AccountName
    daily_pay: LegacyAssetHbd | AssetHbd
    subject: str
    permlink: str
    extensions: HiveDateTime
