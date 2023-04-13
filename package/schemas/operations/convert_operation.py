from pydantic import Field

from schemas.package.schemas.predefined import AccountName, Uint32t, LegacyAssetHbd
from preconfigure_base_model import PreconfiguredBaseModel


class ConvertOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    request_id: Uint32t = 0
    amount: LegacyAssetHbd
