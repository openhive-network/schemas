from schemas.package.schemas.predefined import AccountName, Uint32t, LegacyAssetHbd
from preconfigure_base_model import PreconfiguredBaseModel


class ConvertOperation(PreconfiguredBaseModel):
    From: AccountName
    request_id: Uint32t = 0
    amount: LegacyAssetHbd
