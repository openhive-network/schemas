from __future__ import annotations

from schemas.hive_fields_basic_schemas import AccountName, HiveInt
from schemas.preconfigured_base_model import PreconfiguredBaseModel


class GetAccountReputationsFundament(PreconfiguredBaseModel):
    account: AccountName
    reputation: HiveInt
