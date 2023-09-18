from __future__ import annotations

from schemas.fields.assets.hbd import AssetHbdHF26
from schemas.fields.assets.hive import AssetHiveHF26
from schemas.fields.basic import AccountName, HbdExchangeRate
from schemas.operation import Operation


class FeedPublishOperation(Operation):
    __operation_name__ = "feed_publish"

    publisher: AccountName
    exchange_rate: HbdExchangeRate[AssetHiveHF26, AssetHbdHF26]
