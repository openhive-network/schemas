from pydantic import Field

from schemas.package.schemas.predefined import AccountName, LegacyAssetHbd, LegacyAssetHive
from preconfigure_base_model import PreconfiguredBaseModel


class TransferToSavingsOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias='from')
    to: AccountName
    amount: LegacyAssetHbd | LegacyAssetHive
    memo: str
