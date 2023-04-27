from __future__ import annotations

from schemas.__private.hive_fields_schemas import (
    AccountName,
    AssetHbd,
    HiveDateTime,
    Int64t,
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class UpdateProposalOperation(PreconfiguredBaseModel):
    proposal_id: Int64t
    creator: AccountName
    daily_pay: AssetHbd
    subject: str
    permlink: str
    extensions: HiveDateTime
