from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbdHF26,
    AssetHive,
    AssetHiveHF26,
    AssetVests,
    HiveInt,
)
from schemas.__private.hive_fields_custom_schemas import Price, RcAccountObject, TransactionId
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.wallet_bridge_api.fundaments_of_responses import (
    GetCollateralizedConversionRequestsFundament,
    GetConversionRequestsFundament,
)


class BroadcastTransactionSynchronous(PreconfiguredBaseModel):
    block_num: HiveInt
    expired: bool
    id_: TransactionId = Field(..., alias="id")
    rc_cost: HiveInt | None
    trx_num: HiveInt


FindRcAccounts = list[RcAccountObject[AssetVests]]


class GetChainProperties(PreconfiguredBaseModel, GenericModel, Generic[AssetHive]):
    account_creation_fee: AssetHive
    maximum_block_size: HiveInt
    hbd_interest_rate: HiveInt
    account_subsidy_budget: HiveInt
    account_subsidy_decay: HiveInt


GetCollateralizedConversionRequests = list[GetCollateralizedConversionRequestsFundament[AssetHiveHF26, AssetHbdHF26]]


GetConversionRequests = list[GetConversionRequestsFundament[AssetHbdHF26]]


class GetCurrentMedianHistoryPrice(Price[AssetHiveHF26, AssetHbdHF26]):
    """Identical response as Price field, HF26 format of Assets"""


ListAccounts = list[AccountName]
