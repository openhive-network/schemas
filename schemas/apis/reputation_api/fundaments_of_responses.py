from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName, HiveInt
from schemas._preconfigured_base_model import PreconfiguredBaseModel


class GetAccountReputationsFundament(PreconfiguredBaseModel):
    account: AccountName
    reputation: HiveInt
