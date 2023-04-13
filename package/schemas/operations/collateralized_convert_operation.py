from schemas.__private.hive_fields_schemas import AccountName, Uint32t, LegacyAssetHive
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class CollateralizedConvertOperation(PreconfiguredBaseModel):
    owner: AccountName
    request_id: Uint32t = 0
    amount: LegacyAssetHive
