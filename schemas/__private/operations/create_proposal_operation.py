from __future__ import annotations

from schemas.__private.hive_fields_schemas_strict import AccountName, AssetHbd, AssetHbdLegacy, HiveDateTimeStrict
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class CreateProposalOperation(PreconfiguredBaseModel):
    creator: AccountName
    receiver: AccountName
    start_date: HiveDateTimeStrict
    end_date: HiveDateTimeStrict
    daily_pay: AssetHbd | AssetHbdLegacy
    subject: str
    permlink: str
