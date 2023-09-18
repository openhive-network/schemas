from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import HiveList
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.reputation_api.fundaments_of_responses import GetAccountReputationsFundament


class GetAccountReputations(PreconfiguredBaseModel):
    reputations: HiveList[GetAccountReputationsFundament]
