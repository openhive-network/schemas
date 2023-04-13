from pydantic import Field

from schemas.package.schemas.predefined import AccountName, LegacyAssetHive, LegacyAssetHbd, Uint16t
from preconfigure_base_model import PreconfiguredBaseModel


class RecurrentTransferOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    amount: LegacyAssetHbd | LegacyAssetHive
    memo: str
    recurrence: Uint16t = 0
    executions: Uint16t = 0
