from schemas.package.schemas.predefined import AccountName, Uint32t, LegacyAssetHive
from preconfigure_base_model import PreconfiguredBaseModel


class CollateralizedConvertOperation(PreconfiguredBaseModel):
    owner: AccountName
    request_id: Uint32t = 0
    amount: LegacyAssetHive
