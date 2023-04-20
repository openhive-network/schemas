from __future__ import annotations

from schemas.__private.hive_fields_schemas_strict import AccountName, HbdExchangeRate
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class FeedPublishOperation(PreconfiguredBaseModel):
    publisher: AccountName
    exchange_rate: HbdExchangeRate
