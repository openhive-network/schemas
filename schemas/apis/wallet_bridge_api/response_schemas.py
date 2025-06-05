from __future__ import annotations

from typing import Annotated

import msgspec
from msgspec import field

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
from schemas.fields.assets._base import AssetHive
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.compound import (
    Price,
    Proposal,
    RcAccountObject,
)
from schemas.fields.hex import TransactionId
from schemas.fields.hive_int import HiveInt
from schemas.fields.hive_list import HiveList
from schemas.fields.version import HardforkVersion


class BroadcastTransaction(network_broadcast_api.BroadcastTransaction):
    """This response is also empty json"""


class BroadcastTransactionSynchronous(PreconfiguredBaseModel, kw_only=True):
    block_num: HiveInt
    expired: bool
    id_: TransactionId = field(name="id")
    rc_cost: HiveInt | None = None
    trx_num: HiveInt


class FindProposals(PreconfiguredBaseModel):
    proposals: HiveList[Proposal]


FindRcAccounts = HiveList[RcAccountObject]


FindRecurrentTransfers = HiveList[FindRecurrentTransfersFundament]


GetAccount = Account | None


GetAccountHistory = HiveList[tuple[HiveInt, Hf26ApiAllOperationObject]]


GetAccounts = HiveList[Account]


class GetActiveWitnesses(PreconfiguredBaseModel):
    witnesses: Annotated[list[AccountName], msgspec.Meta(min_length=1, max_length=21)]
    future_witnesses: Annotated[list[AccountName], msgspec.Meta(min_length=1, max_length=21)] | None = None


class GetBlock(PreconfiguredBaseModel):
    """This model can be empty"""

    block: fundaments_block_api.Hf26Block | None = None


class GetChainProperties(PreconfiguredBaseModel):
    account_creation_fee: AssetHive
    maximum_block_size: HiveInt
    hbd_interest_rate: HiveInt
    account_subsidy_budget: HiveInt
    account_subsidy_decay: HiveInt


GetCollateralizedConversionRequests = list[GetCollateralizedConversionRequestsFundament]


GetConversionRequests = list[GetConversionRequestsFundament]


class GetCurrentMedianHistoryPrice(Price):
    """Identical response as Price field, HF26 format of Assets"""


class GetDynamicGlobalProperties(database_api.GetDynamicGlobalPropertiesOrig):
    """Identical as in database_api"""


class GetFeedHistory(database_api.GetFeedHistoryOrig):
    """Identical as in database_api"""


GetHardforkVersion = HardforkVersion


GetOpenOrders = HiveList[fundaments_database_api.LimitOrdersFundament]


class GetOpsInBlock(account_history_api.GetOpsInBlock, kw_only=True):
    """identical as in account_history_api"""


class GetOrderBook(database_api.GetOrderBook):
    """Identical as in database_api"""


class GetOwnerHistory(PreconfiguredBaseModel):
    owner_auths: HiveList[fundaments_database_api.OwnerHistoriesFundament]
    """Identical as in database_api"""


class GetRewardFund(fundaments_database_api.GetRewardFundsFundament):
    """Identical as get_reward_funds funds field"""


class GetTransaction(account_history_api.GetTransaction):
    """Identical as in account_history_api"""


class GetVersion(database_api.GetVersion):
    """Identical as in database_api"""


GetWithdrawRoutes = list[fundaments_database_api.WithdrawVestingRoutesFundament]


GetWitness = fundaments_database_api.WitnessesFundament | None


class GetWitnessSchedule(database_api.GetWitnessScheduleOrig):
    """Identical as in database_api"""


IsKnownTransaction = bool

ListAccounts = list[AccountName]

ListMyAccounts = HiveList[Account]


class ListProposals(database_api.ListProposals):
    """Identical as in database_api"""


class ListProposalVotes(database_api.ListProposalVotes):
    """Identical as in database_api"""


ListRcAccounts = HiveList[RcAccountObject]


ListRcDirectDelegations = HiveList[ListRcDirectDelegationsFundament]


class ListWitnesses(database_api.ListWitnesses):
    """Identical as in database_api"""
