"""
    All the responses from this file have already specified Assets types to Legacy.
    There is no need to specify it by Generic, when want ot use.
"""

from __future__ import annotations

from typing import Any, Literal

from pydantic import Field, conlist, root_validator

import schemas.apis.account_history_api.response_schemas as account_history_api
import schemas.apis.block_api.fundaments_of_responses as fundaments_block_api
import schemas.apis.database_api.fundaments_of_reponses as fundaments_database_api
import schemas.apis.database_api.response_schemas as database_api
import schemas.apis.market_history_api.fundaments_of_responses as fundaments_market_history_api
import schemas.apis.market_history_api.response_schemas as market_history_api
import schemas.apis.network_broadcast_api.response_schemas as broadcast_api
import schemas.apis.wallet_bridge_api.fundaments_of_responses as fundaments_wallet_bridge_api
import schemas.apis.wallet_bridge_api.response_schemas as wallet_bridge_api
from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbdLegacy,
    AssetHiveLegacy,
    AssetVestsLegacy,
    EmptyString,
    HiveDateTime,
    HiveInt,
    HiveList,
    PublicKey,
)
from schemas.__private.hive_fields_custom_schemas import (
    HardforkVersion,
    Hex,
    HiveVersion,
    Price,
    RcAccountObject,
)
from schemas.__private.operations.representation_types import (
    LegacyOperationRepresentationType,
)
from schemas.__private.operations.representations import get_legacy_representation
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
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


class BroadcastTransaction(broadcast_api.BroadcastTransaction):
    """This response as it is in network_broadcast api should return an empty dict"""


class BroadcastTransactionSynchronous(wallet_bridge_api.BroadcastTransactionSynchronous):
    """Identical response as response from wallet_bridge_api"""


"""List of Proposals in Legacy format and without status field"""
FindProposals = HiveList[FindProposalsFundament]


FindRcAccounts = HiveList[RcAccountObject[AssetVestsLegacy]]  # identical as in wallet_bridge_api, but legacy


"""List of FindRecurrentTransfersFundaments from database_api in Legacy Assets format"""
FindRecurrentTransfers = HiveList[fundaments_database_api.FindRecurrentTransfersFundament[AssetHiveLegacy]]


class GetAccountCount(HiveInt):
    """Should return just integer"""


GetAccountHistory = list[tuple[HiveInt, GetAccountHistoryFundament]]


GetAccountReputations = HiveList[GetAccountReputationsFundament]


GetAccounts = HiveList[GetAccountsFundament]


GetActiveVotes = HiveList[GetActiveVotesFundament]


GetActiveWitnesses = list[AccountName | EmptyString]


class GetBlock(fundaments_block_api.LegacyBlock):
    """Identical as in block_api, just extensions changed"""

    extensions: list[tuple[str, Any]]


class GetBlockHeader(fundaments_block_api.GetBlockHeaderFundament):
    """Identical as in block_api, just extensions changed"""

    extensions: list[tuple[str, Any]]


GetBlog = HiveList[GetBlogFundament]


GetBlogEntries = HiveList[GetBlogEntriesFundament]


GetChainProperties = wallet_bridge_api.GetChainProperties[AssetHiveLegacy]  # like in wallet_bridge_api, just legacy


GetCollateralizedConversionRequests = HiveList[
    fundaments_wallet_bridge_api.GetCollateralizedConversionRequestsFundament[AssetHiveLegacy, AssetHbdLegacy]
]


GetCommentDiscussionsByPayout = HiveList[GetCommentDiscussionsByPayoutFundament]


class GetConfig(database_api.GetConfig[AssetHiveLegacy, AssetHbdLegacy]):
    """Field like in database_api, with few modifications"""

    HBD_SYMBOL: Literal["HBD", "TBD"]  # type: ignore
    HIVE_SYMBOL: Literal["HIVE", "TESTS"]  # type: ignore
    VESTS_SYMBOL: Literal["VESTS"]  # type: ignore
    NEW_HIVE_TREASURY_ACCOUNT: AccountName


class GetContent(fundaments_database_api.FindCommentsFundament[AssetHbdLegacy]):
    """Base from database_api, some additional fields"""

    url: str
    root_title: str
    pending_payout_value: AssetHiveLegacy | AssetHbdLegacy
    total_pending_payout_value: AssetHiveLegacy | AssetHbdLegacy
    active_votes: HiveList[GetActiveVotesFundament]
    replies: list[str]
    author_reputation: HiveInt
    promoted: AssetHiveLegacy | AssetHbdLegacy
    body_length: HiveInt
    reblogged_by: list[str]


"""List of GetContent fields"""
GetContentReplies = HiveList[GetContent]


"""Identical as in wallet_bridge_api, just Legacy Asset format"""
GetConversionRequests = HiveList[fundaments_wallet_bridge_api.GetConversionRequestsFundament[AssetHbdLegacy]]


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
GetEscrow = GetEscrowFundament | None


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

    asks: list[fundaments_database_api.GetOrderBookFundament[AssetHiveLegacy, AssetHbdLegacy]]
    bids: list[fundaments_database_api.GetOrderBookFundament[AssetHiveLegacy, AssetHbdLegacy]]


GetOwnerHistory = list[fundaments_database_api.OwnerHistoriesFundament]


class GetPostDiscussionsByPayout(GetDiscussionsByAuthorBeforeDate):
    """The same response as GetDiscussionsByAuthorBeforeDate"""


"""List of public keys or empty list"""
GetPotentialSignatures = list[PublicKey]


"""List of AccountNames is response"""
GetRebloggedBy = list[AccountName]


"""List of fundament from database_api"""
GetRecentTrades = HiveList[fundaments_market_history_api.GetRecentTradesFundament[AssetHiveLegacy, AssetHbdLegacy]]


"""Null or fundament from database_api"""
GetRecoveryRequest = fundaments_database_api.FindAccountRecoveryRequestsFundament | None


class GetRepliesByLastUpdate(GetDiscussionsByAuthorBeforeDate):
    """The same response as GetDiscussionsByAuthorBeforeDate"""


"""List of PublicKeys or empty list"""
GetRequiredSignatures = list[PublicKey]


class GetRewardFund(fundaments_database_api.GetRewardFundsFundament[AssetHiveLegacy]):
    """Identical as get_reward_funds funds field, just different Assets format"""


GetSavingsWithdrawFrom = list[fundaments_database_api.SavingsWithdrawalsFundament[AssetHiveLegacy, AssetHbdLegacy]]


class GetSavingsWithdrawTo(GetSavingsWithdrawFrom):
    """The sam as GetSavingsWithdrawFrom"""


class GetTagsUsedByAuthor(HiveMindResponses):
    """Supported by HiveMind"""


class GetTicker(market_history_api.GetTicker[AssetHiveLegacy, AssetHbdLegacy]):
    """The same response as in market_history_api"""


"""List of fundament from database_api"""
GetTradeHistory = HiveList[fundaments_market_history_api.GetTradeHistoryFundament[AssetHiveLegacy, AssetHbdLegacy]]


class GetTransaction(account_history_api.GetTransactionModel[LegacyOperationRepresentationType]):
    @root_validator(pre=True)
    @classmethod
    def check_operation(cls, values: dict[str, Any]) -> dict[str, Any]:
        values["operations"] = [
            get_legacy_representation(op_name)(type=op_name, value=op_value)
            for op_name, op_value in values["operations"]
        ]
        return values


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


class GetWitnessSchedule(database_api.GetWitnessSchedule[AssetHiveLegacy]):
    """Identical as in database_api, just Legacy format of Assets"""


"""List of fundaments from database_api in Legacy Asset format"""
GetWitnesses = list[fundaments_database_api.WitnessesFundament[AssetHiveLegacy, AssetHbdLegacy] | None]


class GetWitnessesByVote(GetWitnesses):
    """Identical response as GetWitnesses from condenser_api"""


"""Should return just bool value"""
IsKnownTransaction = bool


"""List of fundaments from database_api in Legacy format"""
ListProposalVotes = HiveList[fundaments_database_api.ListProposalVotesFundament[AssetHbdLegacy]]


"""Fundament is from fields -> Proposal, status pole excluded  and Asset converted to Legacy"""
ListProposals = HiveList[ListProposalsFundament]


"""List of field from custom_fields in Legacy Asset format """
ListRcAccounts = HiveList[RcAccountObject[AssetVestsLegacy]]


ListRcDirectDelegations = HiveList[ListRcDirectDelegationsFundament]


LookupAccountNames = HiveList[LookupAccountNamesFundament]


class LookupAccounts(wallet_bridge_api.ListAccounts):
    """Identical as in wallet_bridge_api"""


LookupWitnessAccounts = list[AccountName]


"""Should return just bool"""
VerifyAccountAuthority = bool

"""Should return just bool"""
VerifyAuthority = bool

GetVestingDelegations = list[GetVestingDelegationsFundament]
