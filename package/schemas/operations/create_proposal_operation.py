from __future__ import annotations

from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, HiveDateTime, AssetHbd, LegacyAssetHbd


class CreateProposalOperation(BaseModel, extra=Extra.forbid):
    creator: AccountName
    receiver: AccountName
    start_date: HiveDateTime
    end_date: HiveDateTime
    daily_pay: AssetHbd | LegacyAssetHbd
    subject: str
    permlink: str
    




