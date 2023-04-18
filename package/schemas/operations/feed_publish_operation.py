from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, HbdExchangeRate


class FeedPublishOperation(PreconfiguredBaseModel):
    publisher: AccountName
    exchange_rate: HbdExchangeRate
