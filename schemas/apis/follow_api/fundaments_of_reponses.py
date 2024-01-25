from __future__ import annotations

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.hive_int import HiveInt


class GetAccountReputationsDetail(PreconfiguredBaseModel):
    name: AccountName
    reputation: HiveInt
