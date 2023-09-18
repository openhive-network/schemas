from __future__ import annotations

from typing import Generic

from pydantic import Field, conlist
from pydantic.generics import GenericModel

import schemas.apis.account_history_api.response_schemas as account_history_api
import schemas.apis.block_api.fundaments_of_responses as fundaments_block_api
import schemas.apis.database_api.fundaments_of_reponses as fundaments_database_api
import schemas.apis.database_api.response_schemas as database_api
import schemas.apis.network_broadcast_api.response_schemas as network_broadcast_api
from schemas._operation_objects import Hf26ApiAllOperationObject
from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.wallet_bridge_api.fundaments_of_responses import (
    Account,
    FindRecurrentTransfersFundament,
    GetCollateralizedConversionRequestsFundament,
    GetConversionRequestsFundament,
    ListRcDirectDelegationsFundament,
)
from schemas.fields.assets.hbd import AssetHbdHF26
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveT
from schemas.fields.assets.vests import AssetVestsHF26
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.custom import (
    HardforkVersion,
    Price,
    Proposal,
    RcAccountObject,
)
from schemas.fields.hex import TransactionId
from schemas.fields.hive_int import HiveInt
from schemas.fields.hive_list import HiveList


class BroadcastTransaction(network_broadcast_api.BroadcastTransaction):
    """This response is also empty json"""


class BroadcastTransactionSynchronous(PreconfiguredBaseModel):
    block_num: HiveInt
    expired: bool
    id_: TransactionId = Field(alias="id")
    rc_cost: HiveInt | None
    trx_num: HiveInt


class FindProposals(PreconfiguredBaseModel):
    proposals: HiveList[Proposal[AssetHbdHF26]]


FindRcAccounts = HiveList[RcAccountObject[AssetVestsHF26]]


FindRecurrentTransfers = HiveList[FindRecurrentTransfersFundament[AssetHiveHF26]]


GetAccount = Account[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26] | None


GetAccountHistory = HiveList[tuple[HiveInt, Hf26ApiAllOperationObject]]


GetAccounts = HiveList[Account[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]]


class GetActiveWitnesses(PreconfiguredBaseModel):
    witnesses: conlist(AccountName, min_items=1, max_items=21)  # type: ignore
    future_witnesses: conlist(AccountName, min_items=1, max_items=21) | None = None  # type: ignore


class GetBlock(PreconfiguredBaseModel):
    """This model can be empty"""

    block: fundaments_block_api.Hf26Block | None = None


class GetChainProperties(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT]):
    account_creation_fee: AssetHiveT
    maximum_block_size: HiveInt
    hbd_interest_rate: HiveInt
    account_subsidy_budget: HiveInt
    account_subsidy_decay: HiveInt


GetCollateralizedConversionRequests = list[GetCollateralizedConversionRequestsFundament[AssetHiveHF26, AssetHbdHF26]]


GetConversionRequests = list[GetConversionRequestsFundament[AssetHbdHF26]]


class GetCurrentMedianHistoryPrice(Price[AssetHiveHF26, AssetHbdHF26]):
    """Identical response as Price field, HF26 format of Assets"""


class GetDynamicGlobalProperties(database_api.GetDynamicGlobalProperties[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]):
    """Identical as in database_api"""


class GetFeedHistory(database_api.GetFeedHistory[AssetHiveHF26, AssetHbdHF26]):
    """Identical as in database_api"""


GetHardforkVersion = HardforkVersion


GetOpenOrders = HiveList[fundaments_database_api.LimitOrdersFundament[AssetHiveHF26, AssetHbdHF26]]


class GetOpsInBlock(account_history_api.GetOpsInBlock):
    """identical as in account_history_api"""


class GetOrderBook(database_api.GetOrderBook):
    """Identical as in database_api"""


class GetOwnerHistory(PreconfiguredBaseModel):
    owner_auths: HiveList[fundaments_database_api.OwnerHistoriesFundament]
    """Identical as in database_api"""


class GetRewardFund(fundaments_database_api.GetRewardFundsFundament[AssetHiveHF26]):
    """Identical as get_reward_funds funds field"""


class GetTransaction(account_history_api.GetTransaction):
    """Identical as in account_history_api"""


class GetVersion(database_api.GetVersion):
    """Identical as in database_api"""


GetWithdrawRoutes = list[fundaments_database_api.WithdrawVestingRoutesFundament]


GetWitness = fundaments_database_api.WitnessesFundament[AssetHiveHF26, AssetHbdHF26] | None


class GetWitnessSchedule(database_api.GetWitnessSchedule[AssetHiveHF26]):
    """Identical as in database_api"""


IsKnownTransaction = bool

ListAccounts = list[AccountName]

ListMyAccounts = HiveList[Account[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]]


class ListProposals(database_api.ListProposals):
    """Identical as in database_api"""


class ListProposalVotes(database_api.ListProposalVotes):
    """Identical as in database_api"""


ListRcAccounts = HiveList[RcAccountObject[AssetVestsHF26]]


ListRcDirectDelegations = HiveList[ListRcDirectDelegationsFundament]


class ListWitnesses(database_api.ListWitnesses):
    """Identical as in database_api"""
