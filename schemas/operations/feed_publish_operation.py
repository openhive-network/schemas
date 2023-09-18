from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbdHF26, AssetHiveHF26, HbdExchangeRate
from schemas.__private.operation import Operation


class FeedPublishOperation(Operation):
    __operation_name__ = "feed_publish"

    publisher: AccountName
    exchange_rate: HbdExchangeRate[AssetHiveHF26, AssetHbdHF26]
