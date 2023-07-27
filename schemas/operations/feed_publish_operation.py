from __future__ import annotations

from schemas.hive_fields_basic_schemas import AccountName, AssetHbdHF26, AssetHiveHF26, HbdExchangeRate
from schemas.preconfigured_base_model import Operation


class FeedPublishOperation(Operation):
    publisher: AccountName
    exchange_rate: HbdExchangeRate[AssetHiveHF26, AssetHbdHF26]
