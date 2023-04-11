from schemas.package.schemas.predefined import AccountName, Uint32t
from preconfigure_base_model import PreconfiguredBaseModel


class LimitOrderCancelOperation(PreconfiguredBaseModel):
    owner: AccountName
    order_id: Uint32t = 0
