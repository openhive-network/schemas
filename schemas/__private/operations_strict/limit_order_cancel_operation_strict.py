from __future__ import annotations

from schemas.__private.hive_fields_schemas_strict import AccountName, Uint32t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class LimitOrderCancelOperationStrict(PreconfiguredBaseModel):
    owner: AccountName
    order_id: Uint32t
