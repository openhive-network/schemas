from __future__ import annotations

from schemas.apis.reputation_api.fundaments_of_responses import GetAccountReputationsFundament
from schemas.hive_fields_basic_schemas import HiveList
from schemas.preconfigured_base_model import PreconfiguredBaseModel


class GetAccountReputations(PreconfiguredBaseModel):
    reputations: HiveList[GetAccountReputationsFundament]
