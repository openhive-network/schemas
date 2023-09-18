from __future__ import annotations

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.reputation_api.fundaments_of_responses import GetAccountReputationsFundament
from schemas.fields.hive_list import HiveList


class GetAccountReputations(PreconfiguredBaseModel):
    reputations: HiveList[GetAccountReputationsFundament]
