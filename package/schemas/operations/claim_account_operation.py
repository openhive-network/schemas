from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, AssetHive, LegacyAssetHive


class ClaimAccountOperation(BaseModel, extra=Extra.forbid):
    creator: AccountName
    fee: AssetHive | LegacyAssetHive
