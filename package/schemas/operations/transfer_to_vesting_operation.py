from pydantic import Field

from schemas.package.schemas.predefined import AccountName, LegacyAssetHive
from preconfigure_base_model import PreconfiguredBaseModel


class TransferToVestingOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName | None
    amount: LegacyAssetHive
