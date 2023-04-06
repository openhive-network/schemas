from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, Uint32t, AssetHbd, LegacyAssetHbd, AssetHive, LegacyAssetHive


class EscrowReleaseOperation(BaseModel, extra=Extra.forbid):
    From: AccountName
    to: AccountName
    agent: AccountName
    who: AccountName
    receiver: AccountName
    escrow_id: Uint32t = 30
    hbd_amount: AssetHbd | LegacyAssetHbd  # here add default value
    hive_amount: AssetHive | LegacyAssetHive  # here add default value
