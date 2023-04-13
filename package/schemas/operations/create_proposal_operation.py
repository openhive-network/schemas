from __future__ import annotations

from schemas.package.schemas.predefined import AccountName, HiveDateTime, AssetHbd, LegacyAssetHbd
from preconfigure_base_model import PreconfiguredBaseModel


class CreateProposalOperation(PreconfiguredBaseModel):
    creator: AccountName
    receiver: AccountName
    start_date: HiveDateTime
    end_date: HiveDateTime
    daily_pay: AssetHbd | LegacyAssetHbd
    subject: str
    permlink: str
