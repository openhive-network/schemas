from __future__ import annotations

from schemas.__private.hive_fields_schemas import (
    AssetHbdNai,
    AssetHiveNai,
    AssetVestsNai,
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.database_api.fundaments_of_reponses import (
    AccountItemFundament,
    FindAccountRecoveryRequestsFundament,
    FindChangeRecoveryAccountRequestsFundament,
    FindCollateralizedConversionRequestsFundament,
    FindCommentsFundament,
    FindDeclineVotingRightsRequestsFundament,
    FindEscrowsFundament,
    FindHbdConversionRequestsFundament,
)


class FindAccountRecoveryRequests(PreconfiguredBaseModel):
    requests: list[FindAccountRecoveryRequestsFundament]


class FindAccounts(PreconfiguredBaseModel):
    accounts: list[AccountItemFundament[AssetHiveNai, AssetHbdNai, AssetVestsNai]]


class FindChangeRecoveryAccountRequests(PreconfiguredBaseModel):
    requests: list[FindChangeRecoveryAccountRequestsFundament]


class FindCollateralizedConversionRequests(PreconfiguredBaseModel):
    requests: list[FindCollateralizedConversionRequestsFundament[AssetHiveNai, AssetHbdNai]]


class FindComments(PreconfiguredBaseModel):
    comments: list[FindCommentsFundament[AssetHbdNai]]


class FindDeclineVotingRightsRequests(PreconfiguredBaseModel):
    requests: list[FindDeclineVotingRightsRequestsFundament]


class FindEscrows(PreconfiguredBaseModel):
    escrows: list[FindEscrowsFundament[AssetHiveNai, AssetHbdNai]]


class FindHbdConversionRequests(PreconfiguredBaseModel):
    requests: list[FindHbdConversionRequestsFundament[AssetHbdNai]]
