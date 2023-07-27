from __future__ import annotations

from schemas.hive_fields_basic_schemas import HiveList
from schemas.preconfigured_base_model import PreconfiguredBaseModel
from schemas.reputation_api.fundaments_of_responses import GetAccountReputationsFundament


class GetAccountReputations(PreconfiguredBaseModel):
    reputations: HiveList[GetAccountReputationsFundament]
