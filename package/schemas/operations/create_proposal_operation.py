from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, AssetHbd, HiveDateTime, LegacyAssetHbd


class CreateProposalOperation(PreconfiguredBaseModel):
    creator: AccountName
    receiver: AccountName
    start_date: HiveDateTime
    end_date: HiveDateTime
    daily_pay: AssetHbd | LegacyAssetHbd
    subject: str
    permlink: str
