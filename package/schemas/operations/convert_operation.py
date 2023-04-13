from pydantic import Field

from schemas.__private.hive_fields_schemas import AccountName, Uint32t, LegacyAssetHbd
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class ConvertOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    request_id: Uint32t = 0
    amount: LegacyAssetHbd
