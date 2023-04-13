from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, Uint32t


class LimitOrderCancelOperation(PreconfiguredBaseModel):
    owner: AccountName
    order_id: Uint32t = 0  # type: ignore
