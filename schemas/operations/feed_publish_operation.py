from __future__ import annotations

from schemas.fields.basic import AccountName, AssetHbdHF26, AssetHiveHF26, HbdExchangeRate
from schemas.operation import Operation


class FeedPublishOperation(Operation):
    __operation_name__ = "feed_publish"

    publisher: AccountName
    exchange_rate: HbdExchangeRate[AssetHiveHF26, AssetHbdHF26]
