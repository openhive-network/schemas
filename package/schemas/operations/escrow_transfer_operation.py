from pydantic import Json, Field

from schemas.__private.hive_fields_schemas import (
    AccountName,
    Uint32t,
    AssetHive,
    AssetHbd,
    LegacyAssetHive,
    LegacyAssetHbd,
    HiveDateTime,
)
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class EscrowTransferOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t = 30
    hbd_amount: AssetHbd | LegacyAssetHbd  # to check
    hive_amount: AssetHive | LegacyAssetHbd  # to check
    fee: AssetHive | AssetHbd | LegacyAssetHbd | LegacyAssetHive
    ratification_deadline: HiveDateTime
    escrow_expiration: HiveDateTime
    json_meta: Json
