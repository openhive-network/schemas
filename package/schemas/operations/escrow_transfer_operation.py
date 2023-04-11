from pydantic import Json

from schemas.package.schemas.predefined import (AccountName,
                                                Uint32t,
                                                AssetHive,
                                                AssetHbd,
                                                LegacyAssetHive,
                                                LegacyAssetHbd,
                                                HiveDateTime)
from preconfigure_base_model import PreconfiguredBaseModel


class EscrowTransferOperation(PreconfiguredBaseModel):
    From: AccountName
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t = 30
    hbd_amount: AssetHbd | LegacyAssetHbd  # to check
    hive_amount: AssetHive | LegacyAssetHbd  # to check
    fee: AssetHive | AssetHbd | LegacyAssetHbd | LegacyAssetHive
    ratification_deadline: HiveDateTime
    escrow_expiration: HiveDateTime
    json_meta: Json
