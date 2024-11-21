from __future__ import annotations

from typing import Generic, Literal

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.rc_api.fundaments_of_responses import (
    RcAccount,
    RcDirectDelegations,
    ResourceParams,
    ResourcePool,
    SizeInfo,
)
from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsT
from pydantic import BaseModel


class FindRcAccountsFundament(PreconfiguredBaseModel, BaseModel, Generic[AssetVestsT]):
    rc_accounts: list[RcAccount[AssetVestsT]]


FindRcAccounts = FindRcAccountsFundament[AssetVestsHF26]


class GetResourceParams(PreconfiguredBaseModel):
    resource_names: list[
        Literal[
            "resource_history_bytes",
            "resource_new_accounts",
            "resource_market_bytes",
            "resource_state_bytes",
            "resource_execution_time",
        ]
    ]
    resource_params: ResourceParams
    size_info: SizeInfo


class GetResourcePool(PreconfiguredBaseModel):
    resource_pool: ResourcePool


class ListRcAccountsFundament(PreconfiguredBaseModel, BaseModel, Generic[AssetVestsT]):
    rc_accounts: list[RcAccount[AssetVestsT]]


ListRcAccounts = ListRcAccountsFundament[AssetVestsHF26]


class ListRcDirectDelegations(PreconfiguredBaseModel):
    rc_direct_delegations: list[RcDirectDelegations]
