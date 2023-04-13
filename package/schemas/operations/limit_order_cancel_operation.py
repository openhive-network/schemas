from schemas.__private.hive_fields_schemas import AccountName, Uint32t
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class LimitOrderCancelOperation(PreconfiguredBaseModel):
    owner: AccountName
    order_id: Uint32t = 0
