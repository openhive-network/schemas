from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private import HbdExchangeRate
from schemas.__private.hive_fields_schemas import AccountName, AssetHbd, AssetHive
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class FeedPublishOperation(PreconfiguredBaseModel, GenericModel, Generic[AssetHbd, AssetHive]):
    publisher: AccountName
    exchange_rate: HbdExchangeRate
