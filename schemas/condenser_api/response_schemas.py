from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

import schemas.block_api.fundaments_of_responses as fundaments_block_api
import schemas.database_api.fundaments_of_reponses as fundaments_database_api
import schemas.database_api.response_schemas as database_api
import schemas.network_broadcast_api.response_schemas as broadcast_api
import schemas.wallet_bridge_api.fundaments_of_responses as fundaments_wallet_bridge_api
import schemas.wallet_bridge_api.response_schemas as wallet_bridge_api
from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbdLegacy,
    AssetHiveLegacy,
    AssetVestsLegacy,
    EmptyString,
    HiveDateTime,
    HiveInt,
)
from schemas.__private.hive_fields_custom_schemas import Price, Proposal
from schemas.condenser_api.fundaments_of_responses import (
    GetAccountHistoryFundament,
    GetAccountReputationsFundament,
    GetAccountsFundament,
    GetActiveVotesFundament,
    GetBlockFundament,
    GetBlogEntriesFundament,
    GetBlogFundament,
    GetCommentDiscussionsByPayoutFundament,
)


class BroadcastTransaction(broadcast_api.BroadcastTransaction):
    """This response as it is in network_broadcast api should return an empty dict"""


class BroadcastTransactionSynchronous(wallet_bridge_api.BroadcastTransactionSynchronous):
    """Identical response as response from wallet_bridge_api"""


class FindProposals(Proposal[AssetHbdLegacy]):
    """This response is identical as Proposal field, but here Legacy format is required and status excluded"""

    status: str | None = Field(None, exclude=True)  # type: ignore


FindRcAccounts = wallet_bridge_api.FindRcAccounts[AssetVestsLegacy]  # identical as in wallet_bridge_api, but legacy


class FindRecurrentTransfers(fundaments_database_api.FindRecurrentTransfersFundament[AssetHiveLegacy]):
    """Identical response like fundament for find_recurrent_transfers from database_api, but assets are legacy"""


GetAccountCount = HiveInt  # should return just integer


GetAccountHistory = list[HiveInt, GetAccountHistoryFundament]  # type: ignore


GetAccountReputations = list[GetAccountReputationsFundament]


GetAccounts = list[GetAccountsFundament]


GetActiveVotes = list[GetActiveVotesFundament]


class GetActiveWitnesses(database_api.GetActiveWitnesses):
    """Identical response as in database_api, future_witnesses pole exclude"""

    future_witnesses: list[AccountName | EmptyString] | None = Field(None, exclude=True)


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

    active: HiveDateTime
    url: str
    root_title: str
    pending_payout_value: AssetHiveLegacy
    total_pending_payout_value: AssetHiveLegacy
    active_votes: list[str]
    replies: list[str]
    author_reputation: HiveInt
    promoted: AssetHiveLegacy
    body_length: HiveInt
    reblogged_by: list[str]


class GetContentReplies(GetContent):
    """Identical response like GetContent above"""


"""Identical as in wallet_bridge_api, just Legacy Asset format"""
GetConversionRequests = list[fundaments_wallet_bridge_api.GetConversionRequestsFundament[AssetHbdLegacy]]


class GetCurrentMedianHistoryPrice(Price[AssetHiveLegacy, AssetHbdLegacy]):
    """Identical response as Price field, Legacy format of Assets"""
