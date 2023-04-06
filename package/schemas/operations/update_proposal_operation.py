from __future__ import annotations

from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, Int64t, AssetHbd, LegacyAssetHbd, HiveDateTime


class UpdateProposalOperation(BaseModel, extra=Extra.forbid):
    proposal_id: Int64t
    creator: AccountName
    daily_pay: LegacyAssetHbd | AssetHbd
    subject: str
    permlink: str
    extensions: HiveDateTime
    