from __future__ import annotations

from typing import Generic, Literal

from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.rc_api.fundaments_of_responses import (
    RcAccount,
    RcDirectDelegations,
    ResourceParams,
    ResourcePool,
    SizeInfo,
)
from schemas.fields.assets.vests import AssetVestsT


class FindRcAccounts(PreconfiguredBaseModel, GenericModel, Generic[AssetVestsT]):
    rc_accounts: list[RcAccount[AssetVestsT]]


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


class ListRcAccounts(FindRcAccounts[AssetVestsT]):
    pass


class ListRcDirectDelegations(PreconfiguredBaseModel):
    rc_direct_delegations: list[RcDirectDelegations]
