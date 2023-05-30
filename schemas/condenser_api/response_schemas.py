"""
    All the responses from this file have already specified Assets types to Legacy.
    There is no need to specify it by Generic, when want ot use.
"""

from __future__ import annotations

from typing import Any, Literal

from pydantic import Field, conlist

import schemas.account_history_api.response_schemas as account_history_api
import schemas.block_api.fundaments_of_responses as fundaments_block_api
import schemas.database_api.fundaments_of_reponses as fundaments_database_api
import schemas.database_api.response_schemas as database_api
import schemas.market_history_api.fundaments_of_responses as fundaments_market_history_api
import schemas.market_history_api.response_schemas as market_history_api
import schemas.network_broadcast_api.response_schemas as broadcast_api
import schemas.wallet_bridge_api.fundaments_of_responses as fundaments_wallet_bridge_api
import schemas.wallet_bridge_api.response_schemas as wallet_bridge_api
from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbdLegacy,
    AssetHiveLegacy,
    AssetVestsLegacy,
    HiveDateTime,
    HiveInt,
    PublicKey,
)
from schemas.__private.hive_fields_custom_schemas import (
    FloatAsString,
    HardforkVersion,
    Hex,
    HiveVersion,
    Price,
    RcAccountObject,
)
from schemas.__private.operations import LegacyOperationRepresentationType
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.condenser_api.fundaments_of_responses import (
    FindProposalsFundament,
    FollowFundament,
    GetAccountHistoryFundament,
    GetAccountReputationsFundament,
    GetAccountsFundament,
    GetActiveVotesFundament,
    GetBlockFundament,
    GetBlogEntriesFundament,
    GetBlogFundament,
    GetCommentDiscussionsByPayoutFundament,
    GetDiscussionsByAuthorBeforeDateFundament,
    GetEscrowFundament,
    GetExpiringVestingDelegationFundament,
    GetOpsInBlockFundament,
    GetTrendingTagsFundament,
    HiveMindResponses,
    ListProposalsFundament,
    ListRcDirectDelegationsFundament,
    LookupAccountNamesFundament,
)


class BroadcastTransaction(broadcast_api.BroadcastTransaction):
    """This response as it is in network_broadcast api should return an empty dict"""


class BroadcastTransactionSynchronous(wallet_bridge_api.BroadcastTransactionSynchronous):
    """Identical response as response from wallet_bridge_api"""


"""List of Proposals in Legacy format and without status field"""
FindProposals = list[FindProposalsFundament]


FindRcAccounts = list[RcAccountObject[AssetVestsLegacy]]  # identical as in wallet_bridge_api, but legacy


"""List of FindRecurrentTransfersFundaments from database_api in Legacy Assets format"""
FindRecurrentTransfers = list[fundaments_database_api.FindRecurrentTransfersFundament[AssetHiveLegacy]] | list[str]


class GetAccountCount(HiveInt):
    """Should return just integer"""


GetAccountHistory = list[tuple[HiveInt, GetAccountHistoryFundament]]


GetAccountReputations = list[GetAccountReputationsFundament]


GetAccounts = list[GetAccountsFundament]


GetActiveVotes = list[GetActiveVotesFundament]


GetActiveWitnesses = list[AccountName]


GetBlock = GetBlockFundament | fundaments_block_api.EmptyModel


class GetBlockHeader(fundaments_block_api.GetBlockHeaderFundament):
    """Identical as in block_api, just extensions changed"""

    extensions: list[tuple[str, Any]]


GetBlog = list[GetBlogFundament]


GetBlogEntries = list[GetBlogEntriesFundament]


GetChainProperties = wallet_bridge_api.GetChainProperties[AssetHiveLegacy]  # like in wallet_bridge_api, just legacy


GetCollateralizedConversionRequests = list[
    fundaments_wallet_bridge_api.GetCollateralizedConversionRequestsFundament[AssetHiveLegacy, AssetHbdLegacy]
]


GetCommentDiscussionsByPayout = list[GetCommentDiscussionsByPayoutFundament]


class GetConfig(database_api.GetConfig[AssetHiveLegacy, AssetHbdLegacy]):
    """Field like in database_api, with few modifications"""

    HBD_SYMBOL: Literal["HBD"]  # type: ignore
    HIVE_SYMBOL: Literal["HIVE"]  # type: ignore
    VESTS_SYMBOL: Literal["VESTS"]  # type: ignore
    NEW_HIVE_TREASURY_ACCOUNT: AccountName


class GetContent(fundaments_database_api.FindCommentsFundament[AssetHbdLegacy]):
    """Base from database_api, some additional fields"""

    url: str
    root_title: str
    pending_payout_value: AssetHiveLegacy | AssetHbdLegacy
    total_pending_payout_value: AssetHiveLegacy | AssetHbdLegacy
    active_votes: list[GetActiveVotesFundament]
    replies: list[str]
    author_reputation: HiveInt
    promoted: AssetHiveLegacy | AssetHbdLegacy
    body_length: HiveInt
    reblogged_by: list[str]


"""List of GetContent fields"""
GetContentReplies = list[GetContent]


"""Identical as in wallet_bridge_api, just Legacy Asset format"""
GetConversionRequests = list[fundaments_wallet_bridge_api.GetConversionRequestsFundament[AssetHbdLegacy]]


class GetCurrentMedianHistoryPrice(Price[AssetHiveLegacy, AssetHbdLegacy]):
    """Identical response as Price field, Legacy format of Assets"""


class GetDiscussionsByActive(HiveMindResponses):
    """Supported by hivemind"""


GetDiscussionsByAuthorBeforeDate = list[GetDiscussionsByAuthorBeforeDateFundament]


class GetDiscussionsByBlog(GetDiscussionsByAuthorBeforeDate):
    """The same response as GetDiscussionsByAuthorBeforeDate"""


class GetDiscussionsByCashout(HiveMindResponses):
    """Supported by hivemind"""


class GetDiscussionsByChildren(HiveMindResponses):
    """Supported by hivemind"""


class GetDiscussionsByComments(GetDiscussionsByAuthorBeforeDate):
    """The same response as GetDiscussionsByAuthorBeforeDate"""


class GetDiscussionsByCreated(GetDiscussionsByAuthorBeforeDate):
    """The same response as GetDiscussionsByAuthorBeforeDate"""


class GetDiscussionsByFeed(GetDiscussionsByAuthorBeforeDate):
    """The same response as GetDiscussionsByAuthorBeforeDate"""


class GetDiscussionsByHot(GetDiscussionsByAuthorBeforeDate):
    """The same response as GetDiscussionsByAuthorBeforeDate"""


"could be an empty list"
GetDiscussionsByPromoted = list[GetDiscussionsByAuthorBeforeDate] | conlist(str, max_items=0)


class GetDiscussionsByTrending(GetDiscussionsByAuthorBeforeDate):
    """The same response as GetDiscussionsByAuthorBeforeDate"""


class GetDiscussionsByVotes(HiveMindResponses):
    """Supported by hivemind"""


class GetDynamicGlobalProperties(
    database_api.GetDynamicGlobalProperties[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]
):
    """Identical like response from database_api, just Legacy format of Assets and id exlcuded"""

    id_: HiveInt | None = Field(None, alias="id", exclude=True)  # type: ignore


"""GetEscrowFundament -> the same as in database_api, GetEscrow could also be null"""
GetEscrow = GetEscrowFundament | Literal["null"]


"""Could be list of defined in fundaments or empty list"""
GetExpiringVestingDelegation = list[GetExpiringVestingDelegationFundament] | conlist(str, max_items=0)


class GetFeed(HiveMindResponses):
    """Supported by HiveMind"""


class GetFeedEntries(HiveMindResponses):
    """Supported by HiveMind"""


class GetFeedHistory(database_api.GetFeedHistory[AssetHiveLegacy, AssetHbdLegacy]):
    """identical as in database_api just Legacy format of Assets"""


class GetFollowCount(PreconfiguredBaseModel):
    """Response without any base in other api"""

    account: AccountName
    follower_count: HiveInt
    following_count: HiveInt


"""List of fundaments from fundaments_of_responses"""
GetFollowers = list[FollowFundament]


"""List of fundaments from fundaments_of_responses or empty list"""
GetFollowing = list[FollowFundament] | conlist(str, max_items=0)


"""This response return just string, which is defined in custom fields ="""
GetHardforkVersion = HardforkVersion


"""This response is list which includes list of AccountNames"""
GetKeyReferences = list[tuple[AccountName]]


class GetMarketHistory(fundaments_market_history_api.GetMarketHistoryFundament):
    """Identical response as fundament of get_market_history from market_history_api"""


"""This response should includes list with sizes of buckets"""
GetMarketHistoryBuckets = list[fundaments_market_history_api.BucketSizes]


class GetNextScheduledHardfork(PreconfiguredBaseModel):
    """Response without any base in other api"""

    hf_version: HardforkVersion
    live_time: HiveDateTime


class GetOpenOrders(fundaments_database_api.LimitOrdersFundament[AssetHiveLegacy, AssetHbdLegacy]):
    """Same as in database_api -> list_limit_orders, just Legacy format of Assets and two additional fields"""

    real_price: FloatAsString
    rewarded: bool


"""List of fundaments from fundaments_of_responses"""
GetOpsInBlock = list[GetOpsInBlockFundament]  # something is wrong with operation


class GetOrderBook(PreconfiguredBaseModel):
    """Types of poles are from database_api_fundaments"""

    asks: list[fundaments_database_api.GetOrderBookFundament[AssetHiveLegacy, AssetHbdLegacy]]
    bids: list[fundaments_database_api.GetOrderBookFundament[AssetHiveLegacy, AssetHbdLegacy]]


class GetOwnerHistory(fundaments_database_api.OwnerHistoriesFundament):
    """Identical response like in owner_auths field from list_owner_histories model in database api"""


class GetPostDiscussionsByPayout(GetDiscussionsByAuthorBeforeDate):
    """The same response as GetDiscussionsByAuthorBeforeDate"""


"""List of public keys or empty list"""
GetPotentialSignatures = list[PublicKey] | list[str]


"""List of AccountNames is response"""
GetRebloggedBy = list[AccountName]


"""List of fundament from database_api"""
GetRecentTrades = list[fundaments_market_history_api.GetRecentTradesFundament[AssetHiveLegacy, AssetHbdLegacy]]


"""Null or fundament from database_api"""
GetRecoveryRequest = fundaments_database_api.FindAccountRecoveryRequestsFundament | Literal["null"]


class GetRepliesByLastUpdate(GetDiscussionsByAuthorBeforeDate):
    """The same response as GetDiscussionsByAuthorBeforeDate"""


"""List of PublicKeys or empty list"""
GetRequiredSignatures = list[PublicKey] | list[str]


class GetRewardFund(fundaments_database_api.GetRewardFundsFundament[AssetHiveLegacy]):
    """Identical as get_reward_funds funds field, just different Assets format"""


class GetSavingsWithdrawFrom(fundaments_database_api.SavingsWithdrawalsFundament[AssetHiveLegacy, AssetHbdLegacy]):
    """Just different Assets format, rest the same as in database_api"""


class GetSavingsWithdrawTo(GetSavingsWithdrawFrom):
    """The sam as GetSavingsWithdrawFrom"""


class GetTagsUsedByAuthor(HiveMindResponses):
    """Supported by HiveMind"""


class GetTicker(market_history_api.GetTicker[AssetHiveLegacy, AssetHbdLegacy]):
    """The same response as in market_history_api"""


"""List of fundament from database_api"""
GetTradeHistory = list[fundaments_market_history_api.GetTradeHistoryFundament[AssetHiveLegacy, AssetHbdLegacy]]


class GetTransaction(account_history_api.GetTransaction[LegacyOperationRepresentationType]):
    """The same as in account_history_api"""


"""This response return just Hex"""
GetTransactionHex = Hex


""""list of fundament from fundaments_file"""
GetTrendingTags = list[GetTrendingTagsFundament]


class GetVersion(HiveVersion):
    """Identical as field HiveVersion"""


class ListVestingDelegations(fundaments_database_api.VestingDelegationsFundament[AssetVestsLegacy]):
    """Identical as in database_api, just legacy format of Assets"""


class GetVolume(market_history_api.GetVolume[AssetHiveLegacy, AssetHbdLegacy]):
    """Everything the same as in market_history_api"""


"""List of fundaments for list_withdraw_vesting_routes from database_api"""
GetWithdrawRoutes = list[fundaments_database_api.WithdrawVestingRoutesFundament]


class GetWitnessByAccount(fundaments_database_api.WitnessesFundament[AssetHiveLegacy, AssetHbdLegacy]):
    """Identical as in database_api, just Legacy format of Assets"""


class GetWitnessCount(HiveInt):
    """Should return just integer"""


class GetWitnessesSchedule(database_api.GetWitnessSchedule[AssetHiveLegacy]):
    """Identical as in database_api, just Legacy format of Assets"""


"""List of fundaments from database_api in Legacy Asset format"""
GetWitnesses = list[fundaments_database_api.WitnessesFundament[AssetHiveLegacy, AssetHbdLegacy]]


class GetWitnessesByVote(GetWitnesses):
    """Identical response as GetWitnesses from condenser_api"""


"""Should return just bool value"""
IsKnownTransaction = bool


"""List of fundaments from database_api in Legacy format"""
ListProposalVotes = list[fundaments_database_api.ListProposalVotesFundament[AssetHbdLegacy]]


"""Fundament is from fields -> Proposal, status pole excluded  and Asset converted to Legacy"""
ListProposals = list[ListProposalsFundament]


"""List of field from custom_fields in Legacy Asset format """
ListRcAccounts = list[RcAccountObject[AssetVestsLegacy]]


ListRcDirectDelegations = list[ListRcDirectDelegationsFundament]


LookupAccountNames = list[LookupAccountNamesFundament]


class LookupAccounts(wallet_bridge_api.ListAccounts):
    """Identical as in wallet_bridge_api"""


LookupWitnessAccounts = list[AccountName]


"""Should return just bool"""
VerifyAccountAuthority = bool

"""Should return just bool"""
verify_authority = bool
