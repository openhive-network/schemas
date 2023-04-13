from pydantic import Field

from schemas.__private.hive_fields_schemas import AccountName, PublicKey, LegacyAssetHive, LegacyAssetHbd
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class TransferOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    amount: LegacyAssetHive | LegacyAssetHbd
    memo: PublicKey
