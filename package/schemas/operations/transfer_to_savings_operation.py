from pydantic import Field

from schemas.__private.hive_fields_schemas import AccountName, LegacyAssetHbd, LegacyAssetHive
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class TransferToSavingsOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    amount: LegacyAssetHbd | LegacyAssetHive
    memo: str
