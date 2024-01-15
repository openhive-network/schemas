from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import AccountName
from schemas.fields.compound import HbdExchangeRate
from schemas.operation import Operation


class _FeedPublishOperation(Operation, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "feed_publish"
    __offset__ = 7

    publisher: AccountName
    exchange_rate: HbdExchangeRate[AssetHiveT, AssetHbdT]


class FeedPublishOperation(_FeedPublishOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class FeedPublishOperationLegacy(_FeedPublishOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
