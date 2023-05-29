from __future__ import annotations

from typing import Generic, Literal

from pydantic import Field, conlist
from pydantic.generics import GenericModel

import schemas.account_history_api.response_schemas as account_history_api
import schemas.block_api.fundaments_of_responses as fundaments_block_api
import schemas.database_api.fundaments_of_reponses as fundaments_database_api
import schemas.database_api.response_schemas as database_api
import schemas.network_broadcast_api.response_schemas as network_broadcast_api
from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbdHF26,
    AssetHive,
    AssetHiveHF26,
    AssetVests,
    AssetVestsHF26,
    HiveInt,
)
from schemas.__private.hive_fields_custom_schemas import (
    HardforkVersion,
    Price,
    Proposal,
    RcAccountObject,
    TransactionId,
)
from schemas.__private.operation_objects import Hf26ApiOperationObject
from schemas.__private.operations import LegacyOperationRepresentationType
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.wallet_bridge_api.fundaments_of_responses import (
    Account,
    FindRecurrentTransfersFundament,
    GetCollateralizedConversionRequestsFundament,
    GetConversionRequestsFundament,
    ListRcDirectDelegationsFundament,
)


class BroadcastTransaction(network_broadcast_api.BroadcastTransaction):
    """This response is also empty json"""


class BroadcastTransactionSynchronous(PreconfiguredBaseModel):
    block_num: HiveInt
    expired: bool
    id_: TransactionId = Field(..., alias="id")
    rc_cost: HiveInt | None
    trx_num: HiveInt


class FindProposals(PreconfiguredBaseModel):
    proposals: list[Proposal[AssetHbdHF26]]


FindRcAccounts = list[RcAccountObject[AssetVests]]


FindRecurrentTransfers = list[FindRecurrentTransfersFundament[AssetHiveHF26]]


GetAccount = Account[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26] | Literal["Null"]


GetAccountHistory = list[tuple[HiveInt, Hf26ApiOperationObject]]


GetAccounts = list[Account[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]]


class GetActiveWitnesses(PreconfiguredBaseModel):
    witnesses: conlist(AccountName, min_items=1, max_items=21)  # type: ignore
    future_witnesses: conlist(AccountName, min_items=1, max_items=21) | None  # type: ignore


class GetBlock(PreconfiguredBaseModel):
    """This model can be empty"""

    block: fundaments_block_api.Block | None


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


class GetDynamicGlobalProperties(database_api.GetDynamicGlobalProperties[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]):
    """Identical as in database_api"""


class GetFeedHistory(database_api.GetFeedHistory[AssetHiveHF26, AssetHbdHF26]):
    """Identical as in database_api"""


GetHardforkVersion = HardforkVersion


GetOpenOrders = list[fundaments_database_api.LimitOrdersFundament[AssetHiveHF26, AssetHbdHF26]]


class GetOpsInBlock(PreconfiguredBaseModel):
    ops: Hf26ApiOperationObject


class GetOrderBook(database_api.GetOrderBook):
    """Identical as in database_api"""


class GetOwnerHistory(fundaments_database_api.OwnerHistoriesFundament):
    """Identical as in database_api"""


class GetTransaction(account_history_api.GetTransaction[LegacyOperationRepresentationType]):
    """Identical as in account_history_api"""


class GetVersion(database_api.GetVersion):
    """Identical as in database_api"""


GetWithdrawRoutes = list[fundaments_database_api.WithdrawVestingRoutesFundament]


GetWitness = Literal["Null"] | AccountName


class GetWitnessSchedule(database_api.GetWitnessSchedule[AssetHiveHF26]):
    """Identical as in database_api"""


IsKnownTransaction = bool


ListMyAccounts = list[Account[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]]


class ListProposals(database_api.ListProposals):
    """Identical as in database_api"""


ListRcAccounts = list[RcAccountObject[AssetVestsHF26]]


ListRcDirectDelegations = list[ListRcDirectDelegationsFundament]


class ListWitnesses(database_api.ListWitnesses):
    """Identical as in database_api"""
