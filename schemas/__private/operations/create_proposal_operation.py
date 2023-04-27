from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName, AssetHbd, HiveDateTime
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class CreateProposalOperation(PreconfiguredBaseModel):
    creator: AccountName
    receiver: AccountName
    start_date: HiveDateTime
    end_date: HiveDateTime
    daily_pay: AssetHbd
    subject: str
    permlink: str
