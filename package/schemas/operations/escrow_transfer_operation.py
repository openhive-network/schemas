from pydantic import BaseModel, Extra, Json

from schemas.predefined import (AccountName,
                                Uint32t,
                                AssetHive,
                                AssetHbd,
                                LegacyAssetHive,
                                LegacyAssetHbd,
                                HiveDateTime)


class EscrowTransferOperation(BaseModel, extra=Extra.forbid):
    From: AccountName
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t = 30
    hbd_amount: AssetHbd | LegacyAssetHbd
    hive_amount: AssetHive | LegacyAssetHbd
    fee: AssetHive | AssetHbd | LegacyAssetHbd | LegacyAssetHive
    ratification_deadline: HiveDateTime
    escrow_expiration: HiveDateTime
    json_meta: Json
