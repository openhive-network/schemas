from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName, AssetHbdNai, AssetHiveNai, HbdExchangeRate
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class FeedPublishOperation(PreconfiguredBaseModel):
    publisher: AccountName
    exchange_rate: HbdExchangeRate[AssetHiveNai, AssetHbdNai]
