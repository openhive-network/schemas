from __future__ import annotations

from schemas.__private.hive_fields_schemas_strict import AccountName, AssetHbd, AssetHbdLegacy, HiveDateTime, Int64t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class UpdateProposalOperation(PreconfiguredBaseModel):
    proposal_id: Int64t
    creator: AccountName
    daily_pay: AssetHbdLegacy | AssetHbd
    subject: str
    permlink: str
    extensions: HiveDateTime
