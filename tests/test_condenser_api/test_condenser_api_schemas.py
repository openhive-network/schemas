from __future__ import annotations

import json
from typing import Any

import pytest

from schemas.apis import condenser_api
from schemas.jsonrpc import get_response_model

from . import responses_from_api


@pytest.mark.parametrize(
    "schema, parameters",
    [
        (condenser_api.GetDiscussionsByAuthorBeforeDate, responses_from_api.GET_DISCUSSIONS_BY_AUTHOR_BEFORE_DATE),
        # (condenser_api.GetDiscussionsByBlog, responses_from_api.GET_DISCUSSIONS_BY_BLOG),
        # (condenser_api.GetDiscussionsByComments, responses_from_api.GET_DISCUSSIONS_BY_COMMENTS),
        # (condenser_api.GetDiscussionsByCreated, responses_from_api.GET_DISCUSSIONS_BY_CREATED), 
        # (condenser_api.GetDiscussionsByFeed, responses_from_api.GET_DISCUSSIONS_BY_FEED),
        # (condenser_api.GetDiscussionsByHot, responses_from_api.GET_DISCUSSIONS_BY_HOT),
        # (condenser_api.GetDiscussionsByTrending, responses_from_api.GET_DISCUSSIONS_BY_TRENDING),
        # (condenser_api.GetDynamicGlobalProperties, responses_from_api.GET_DYNAMIC_GLOBAL_PROPERTIES),
        # (condenser_api.GetFeedHistory, responses_from_api.GET_FEED_HISTORY),
        # (condenser_api.GetPostDiscussionsByPayout, responses_from_api.GET_POST_DISCUSSION_BY_PAYOUT),
        # (condenser_api.GetRepliesByLastUpdate, responses_from_api.GET_REPLIES_BY_LAST_UPDATE),
        # (condenser_api.FindProposals, responses_from_api.FIND_PROPOSALS),
        # (condenser_api.FindRecurrentTransfers, responses_from_api.FIND_RECURRENT_TRANSFERS),
        # (condenser_api.GetAccountCount, responses_from_api.GET_ACCOUNT_COUNT),
        # (condenser_api.GetAccountReputations, responses_from_api.GET_ACCOUNT_REPUTATIONS),
        # (condenser_api.GetAccounts, responses_from_api.GET_ACCOUNTS),
        # (condenser_api.GetActiveVotes, responses_from_api.GET_ACTIVE_VOTES),
        # (condenser_api.GetActiveWitnesses, responses_from_api.GET_ACTIVE_WITNESSES),
        # (condenser_api.GetBlock, responses_from_api.GET_BLOCK),
        # (condenser_api.GetBlockHeader, responses_from_api.GET_BLOCK_HEADER),
        # (condenser_api.GetBlog, responses_from_api.GET_BLOG),
        # (condenser_api.GetBlogEntries, responses_from_api.GET_BLOG_ENTRIES),
        # (condenser_api.GetChainProperties, responses_from_api.GET_CHAIN_PROPERTIES),
        # (condenser_api.GetCommentDiscussionsByPayout, responses_from_api.GET_COMMENT_DISCUSSION_BY_PAYOUT),
        # (condenser_api.GetConfig, responses_from_api.GET_CONFIG),
        # (condenser_api.GetContent, responses_from_api.GET_CONTENT),
        # (condenser_api.GetContentReplies, responses_from_api.GET_CONTENT_REPLIES),
        # (condenser_api.GetCurrentMedianHistoryPrice, responses_from_api.GET_CURRENT_MEDIAN_HISTORY_PRICE),
        # (condenser_api.GetEscrow, responses_from_api.GET_ESCROW),
        # (condenser_api.GetFollowCount, responses_from_api.GET_FOLLOW_COUNT),
        # (condenser_api.GetFollowers, responses_from_api.GET_FOLLOWERS),
        # (condenser_api.GetHardforkVersion, responses_from_api.GET_HARDFORK_VERSION),
        # (condenser_api.GetMarketHistoryBuckets, responses_from_api.GET_MARKET_HISTORY_BUCKETS),
        # (condenser_api.GetNextScheduledHardfork, responses_from_api.GET_NEXT_SCHEDULED_HARDFORK),
        # (condenser_api.GetOrderBook, responses_from_api.GET_ORDER_BOOK),
        # (condenser_api.GetRebloggedBy, responses_from_api.GET_REBLOGGED_BY),
        # (condenser_api.GetRecentTrades, responses_from_api.GET_RECENT_TRADES),
        # (condenser_api.GetRewardFund, responses_from_api.GET_REWARD_FUND),
        # (condenser_api.GetTicker, responses_from_api.GET_TICKER),
        # (condenser_api.GetTradeHistory, responses_from_api.GET_TRADE_HISTORY),
        # (condenser_api.GetTransactionHex, responses_from_api.GET_TRANSACTION_HEX),
        # (condenser_api.GetTrendingTags, responses_from_api.GET_TRENDING_TAGS),
        # (condenser_api.GetVersion, responses_from_api.GET_VERSION),
        # (condenser_api.GetVolume, responses_from_api.GET_VOLUME),
        # (condenser_api.GetWithdrawRoutes, responses_from_api.GET_WITHDRAW_ROUTES),
        # (condenser_api.GetWitnessByAccount, responses_from_api.GET_WITNESS_BY_ACCOUNT),
        # (condenser_api.GetWitnessCount, responses_from_api.GET_WITNESS_COUNT),
        # (condenser_api.GetWitnessSchedule, responses_from_api.GET_WITNESS_SCHEDULE),
        # (condenser_api.GetWitnesses, responses_from_api.GET_WITNESSES),
        # (condenser_api.GetWitnessesByVote, responses_from_api.GET_WITNESSES_BY_VOTE),
        # (condenser_api.IsKnownTransaction, responses_from_api.IS_KNOWN_TRANSACTION),
        # (condenser_api.ListProposalVotes, responses_from_api.LIST_PROPOSAL_VOTES),
        # (condenser_api.ListProposals, responses_from_api.LIST_PROPOSALS),
        # (condenser_api.LookupAccountNames, responses_from_api.LOOKUP_ACCOUNT_NAMES),
        # (condenser_api.LookupAccounts, responses_from_api.LOOKUP_ACCOUNTS),
        # (condenser_api.GetAccountHistory, responses_from_api.GET_ACCOUNT_HISTORY),
        # (condenser_api.GetOpsInBlock, responses_from_api.GET_OPS_IN_BLOCK),
        # (condenser_api.GetTransaction, responses_from_api.GET_TRANSACTION),
        # (condenser_api.GetFeed, responses_from_api.GET_FEED),
    ],
)
def test_responses_from_api_correct_values(schema: Any, parameters: Any) -> None:
    # ACT & ASSERT
    get_response_model(schema, json.dumps(parameters))
