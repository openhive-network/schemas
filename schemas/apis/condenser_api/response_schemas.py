"""
All the responses from this file have already specified Assets types to Legacy.
There is no need to specify it by Generic, when want ot use.
"""

from __future__ import annotations

from typing import Any, Literal

import msgspec

import schemas.apis.account_history_api.response_schemas as account_history_api
import schemas.apis.block_api.fundaments_of_responses as fundaments_block_api
import schemas.apis.database_api.fundaments_of_reponses as fundaments_database_api
import schemas.apis.database_api.response_schemas as database_api
import schemas.apis.market_history_api.fundaments_of_responses as fundaments_market_history_api
import schemas.apis.market_history_api.response_schemas as market_history_api
import schemas.apis.network_broadcast_api.response_schemas as broadcast_api
import schemas.apis.wallet_bridge_api.fundaments_of_responses as fundaments_wallet_bridge_api
import schemas.apis.wallet_bridge_api.response_schemas as wallet_bridge_api
from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.condenser_api.fundaments_of_responses import (
    FindProposalsFundament,
    FollowFundament,
    GetAccountHistoryFundament,
    GetAccountReputationsFundament,
    GetAccountsFundament,
    GetActiveVotesFundament,
    GetBlogEntriesFundament,
    GetBlogFundament,
    GetCommentDiscussionsByPayoutFundament,
    GetDiscussionsByAuthorBeforeDateFundament,
    GetEscrowFundament,
    GetExpiringVestingDelegationFundament,
    GetExpiringVestingDelegationsFundament,
    GetOpenOrdersFundament,
    GetOpsInBlockFundament,
    GetTrendingTagsFundament,
    GetVestingDelegationsFundament,
    HiveMindResponses,
    ListProposalsFundament,
    ListRcDirectDelegationsFundament,
    LookupAccountNamesFundament,
)
from schemas.fields.basic import (
    AccountName,
    EmptyList,
    OptionallyEmptyAccountName,
    PublicKey,
    Url,
)
from schemas.fields.compound import (
    Price,
    RcAccountObject,
)
from schemas.fields.hex import Hex
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.fields.hive_list import HiveList
from schemas.fields.resolvables import AssetUnionAssetHiveAssetHbd
from schemas.fields.version import HardforkVersion, HiveVersion
from schemas.operations import LegacyOperationRepresentation


class BroadcastTransaction(broadcast_api.BroadcastTransaction):
    """This response as it is in network_broadcast api should return an empty dict"""


class BroadcastTransactionSynchronous(wallet_bridge_api.BroadcastTransactionSynchronous):
    """Identical response as response from wallet_bridge_api"""


"""List of Proposals without status field"""
FindProposals = HiveList[FindProposalsFundament]


FindRcAccounts = HiveList[RcAccountObject]  # identical as in wallet_bridge_api, but legacy


"""List of FindRecurrentTransfersFundaments from database_api"""
FindRecurrentTransfers = HiveList[fundaments_database_api.FindRecurrentTransfersFundament]


GetAccountCount = HiveInt


GetAccountHistory = list[tuple[HiveInt, GetAccountHistoryFundament]]


GetAccountReputations = HiveList[GetAccountReputationsFundament]


GetAccounts = HiveList[GetAccountsFundament]


GetActiveVotes = HiveList[GetActiveVotesFundament]


GetActiveWitnesses = list[OptionallyEmptyAccountName]


class GetBlock(fundaments_block_api.LegacyBlock):
    """Identical as in block_api, just extensions changed"""

    extensions: list[tuple[HiveInt, Any]]


class GetBlockHeader(fundaments_block_api.GetBlockHeaderFundament):
    """Identical as in block_api, just extensions changed"""

    extensions: list[tuple[HiveInt, Any]]


GetBlog = HiveList[GetBlogFundament]


GetBlogEntries = HiveList[GetBlogEntriesFundament]


GetChainProperties = wallet_bridge_api.GetChainProperties  # like in wallet_bridge_api, just legacy


GetCollateralizedConversionRequests = HiveList[
    fundaments_wallet_bridge_api.GetCollateralizedConversionRequestsFundament
]


GetCommentDiscussionsByPayout = HiveList[GetCommentDiscussionsByPayoutFundament]


class GetConfig(database_api.GetConfigOrig):
    """Field like in database_api, with few modifications"""

    HBD_SYMBOL: Literal["HBD", "TBD"]  # type: ignore
    HIVE_SYMBOL: Literal["HIVE", "TESTS"]  # type: ignore
    VESTS_SYMBOL: Literal["VESTS"]  # type: ignore
    NEW_HIVE_TREASURY_ACCOUNT: AccountName


class GetContent(fundaments_database_api.FindCommentsFundament):
    """Base from database_api, some additional fields"""

    url: Url
    root_title: str
    pending_payout_value: AssetUnionAssetHiveAssetHbd
    total_pending_payout_value: AssetUnionAssetHiveAssetHbd
    active_votes: HiveList[GetActiveVotesFundament]
    replies: list[str]
    author_reputation: HiveInt
    promoted: AssetUnionAssetHiveAssetHbd
    body_length: HiveInt
    reblogged_by: list[str]


"""List of GetContent fields"""
GetContentReplies = HiveList[GetContent]


"""Identical as in wallet_bridge_api"""
GetConversionRequests = HiveList[fundaments_wallet_bridge_api.GetConversionRequestsFundament]


class GetCurrentMedianHistoryPrice(Price):
    """Identical response as Price field"""


class GetDiscussionsByActive(HiveMindResponses):
    """Supported by hivemind"""


GetDiscussionsByAuthorBeforeDate = list[GetDiscussionsByAuthorBeforeDateFundament]


GetDiscussionsByBlog = GetDiscussionsByAuthorBeforeDate


class GetDiscussionsByCashout(HiveMindResponses):
    """Supported by hivemind"""


class GetDiscussionsByChildren(HiveMindResponses):
    """Supported by hivemind"""


GetDiscussionsByComments = GetDiscussionsByAuthorBeforeDate


GetDiscussionsByCreated = GetDiscussionsByAuthorBeforeDate


GetDiscussionsByFeed = GetDiscussionsByAuthorBeforeDate


GetDiscussionsByHot = GetDiscussionsByAuthorBeforeDate


"could be an empty list"
GetDiscussionsByPromoted = list[GetDiscussionsByAuthorBeforeDate] | EmptyList


GetDiscussionsByTrending = GetDiscussionsByAuthorBeforeDate


class GetDiscussionsByVotes(HiveMindResponses):
    """Supported by hivemind"""


class GetDynamicGlobalProperties(database_api.GetDynamicGlobalProperties):
    """Identical like response from database_api, just id exlcuded"""

    id_: HiveInt | None = msgspec.field(default=None, name="id")  # type: ignore


"""GetEscrowFundament -> the same as in database_api, GetEscrow could also be null"""
GetEscrow = GetEscrowFundament | None


"""Could be list of defined in fundaments or empty list"""
GetExpiringVestingDelegation = list[GetExpiringVestingDelegationFundament] | EmptyList


class GetFeed(HiveMindResponses):
    """Supported by HiveMind"""


class GetFeedEntries(HiveMindResponses):
    """Supported by HiveMind"""


class GetFeedHistory(database_api.GetFeedHistoryOrig):
    """identical as in database_api"""


class GetFollowCount(PreconfiguredBaseModel):
    """Response without any base in other api"""

    account: AccountName
    follower_count: HiveInt
    following_count: HiveInt


"""List of fundaments from fundaments_of_responses"""
GetFollowers = list[FollowFundament]


"""List of fundaments from fundaments_of_responses or empty list"""
GetFollowing = list[FollowFundament] | EmptyList


"""This response return just string, which is defined in custom fields ="""
GetHardforkVersion = HardforkVersion


"""This response is list which includes list of AccountNames"""
GetKeyReferences = list[list[AccountName]]


GetMarketHistory = list[fundaments_market_history_api.GetMarketHistoryFundament]


"""This response should includes list with sizes of buckets"""
GetMarketHistoryBuckets = list[fundaments_market_history_api.BucketSizes]

GetExpiringVestingDelegations = list[GetExpiringVestingDelegationsFundament]


class GetNextScheduledHardfork(PreconfiguredBaseModel):
    """Response without any base in other api"""

    hf_version: HardforkVersion
    live_time: HiveDateTime


GetOpenOrders = list[GetOpenOrdersFundament]

"""List of fundaments from fundaments_of_responses"""
GetOpsInBlock = list[GetOpsInBlockFundament]  # something is wrong with operation


class GetOrderBook(PreconfiguredBaseModel):
    """Types of poles are from database_api_fundaments"""

    asks: list[fundaments_database_api.GetOrderBookFundament]
    bids: list[fundaments_database_api.GetOrderBookFundament]


GetOwnerHistory = list[fundaments_database_api.OwnerHistoriesFundament]


GetPostDiscussionsByPayout = GetDiscussionsByAuthorBeforeDate


"""List of public keys or empty list"""
GetPotentialSignatures = list[PublicKey]


"""List of AccountNames is response"""
GetRebloggedBy = list[AccountName]


"""List of fundament from database_api"""
GetRecentTrades = HiveList[fundaments_market_history_api.GetRecentTradesFundament]


"""Null or fundament from database_api"""
GetRecoveryRequest = fundaments_database_api.FindAccountRecoveryRequestsFundament | None


GetRepliesByLastUpdate = GetDiscussionsByAuthorBeforeDate


"""List of PublicKeys or empty list"""
GetRequiredSignatures = list[PublicKey]


class GetRewardFund(fundaments_database_api.GetRewardFundsFundament):
    """Identical as get_reward_funds funds field"""


GetSavingsWithdrawFrom = list[fundaments_database_api.SavingsWithdrawalsFundament]


GetSavingsWithdrawTo = GetSavingsWithdrawFrom


class GetTagsUsedByAuthor(HiveMindResponses):
    """Supported by HiveMind"""


class GetTicker(market_history_api.GetTicker):
    """The same response as in market_history_api"""


"""List of fundament from database_api"""
GetTradeHistory = HiveList[fundaments_market_history_api.GetTradeHistoryFundament]


class GetTransaction(account_history_api.GetTransactionBase):
    operations: list[LegacyOperationRepresentation]


"""This response return just Hex"""
GetTransactionHex = Hex


""""list of fundament from fundaments_file"""
GetTrendingTags = list[GetTrendingTagsFundament]


class GetVersion(HiveVersion):
    """Identical as field HiveVersion"""


class ListVestingDelegations(fundaments_database_api.VestingDelegationsFundament):
    """Identical as in database_api"""


class GetVolume(market_history_api.GetVolume):
    """Everything the same as in market_history_api"""


"""List of fundaments for list_withdraw_vesting_routes from database_api"""
GetWithdrawRoutes = list[fundaments_database_api.WithdrawVestingRoutesFundament]


class GetWitnessByAccount(fundaments_database_api.WitnessesFundament):
    """Identical as in database_api"""


GetWitnessCount = HiveInt


class GetWitnessSchedule(database_api.GetWitnessScheduleOrig):
    """Identical as in database_api"""


"""List of fundaments from database_api"""
GetWitnesses = list[fundaments_database_api.WitnessesFundament | None]


GetWitnessesByVote = GetWitnesses


"""Should return just bool value"""
IsKnownTransaction = bool


"""List of fundaments from database_api"""
ListProposalVotes = HiveList[fundaments_database_api.ListProposalVotesFundament]


"""Fundament is from fields -> Proposal, status pole excluded  and Asset converted to Legacy"""
ListProposals = HiveList[ListProposalsFundament]


"""List of field from custom_fields"""
ListRcAccounts = HiveList[RcAccountObject]


ListRcDirectDelegations = HiveList[ListRcDirectDelegationsFundament]


LookupAccountNames = HiveList[LookupAccountNamesFundament]


LookupAccounts = wallet_bridge_api.ListAccounts


LookupWitnessAccounts = list[AccountName]


"""Should return just bool"""
VerifyAccountAuthority = bool

"""Should return just bool"""
VerifyAuthority = bool

GetVestingDelegations = list[GetVestingDelegationsFundament]
