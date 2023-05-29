from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

import schemas.block_api.fundaments_of_responses as fundaments_block_api
import schemas.database_api.fundaments_of_reponses as fundaments_database_api
from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbdLegacy,
    AssetHiveLegacy,
    AssetVestsLegacy,
    EmptyString,
    HiveDateTime,
    HiveInt,
)
from schemas.__private.hive_fields_custom_schemas import Permlink, Proposal
from schemas.__private.operation_objects import LegacyApiAllOperationObject
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class HiveMindResponses(PreconfiguredBaseModel):
    """Base class for all responses from HiveMind"""

    code: Literal[-32003]
    message: Literal["Assert Exception:false: Supported by hivemind"]
    data: dict[str, Any]


class FindProposalsFundament(Proposal[AssetHbdLegacy]):
    """Change format of Assets to Legacy, excluded status field"""

    status: str | None = Field(None, exclude=True)  # type: ignore


class GetAccountReputationsFundament(PreconfiguredBaseModel):
    account: AccountName
    reputation: HiveInt


class GetAccountsFundament(
    fundaments_database_api.AccountItemFundament[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]
):
    """Base for this response is list_accounts from database api. Some additional fields are here and two excluded"""

    last_post_edit: HiveDateTime | None = Field(None, exclude=True)  # type: ignore
    is_smt: bool | None = Field(None, exclude=True)  # type: ignore

    post_history: list[str]
    vote_history: list[str]
    witness_votes: list[str]
    vesting_balance: AssetHiveLegacy
    transfer_history: list[str]
    voting_power: HiveInt
    market_history: list[str]
    tags_usage: list[str]
    reputation: HiveInt
    guest_bloggers: list[str]
    other_history: list[str]


class GetAccountHistoryFundament(LegacyApiAllOperationObject):
    operation_id: HiveInt = Field(None, exclude=True)  # type: ignore


class GetActiveVotesFundament(PreconfiguredBaseModel):
    percent: HiveInt
    reputation: HiveInt
    rshares: HiveInt
    time: HiveDateTime
    voter: AccountName
    weight: HiveInt


class GetBlockFundament(fundaments_block_api.Block):
    """Identical as in block_api, just extensions changed"""

    extensions: list[tuple[str, Any]]


class GetBlogEntriesFundament(PreconfiguredBaseModel):
    author: AccountName
    permlink: str
    blog: AccountName
    reblogged_on: HiveDateTime
    entry_id: HiveInt


class ActiveVotes(PreconfiguredBaseModel):
    """This is field which is used in GetCommentDiscussionsByPayout model"""

    percent: HiveInt
    reputation: HiveInt
    rshares: HiveInt
    voter: AccountName


class GetCommentDiscussionsByPayoutFundament(fundaments_database_api.FindCommentsFundament[AssetHbdLegacy]):
    id_: HiveInt | None = Field(None, exclude=True)  # type: ignore
    abs_rshares: HiveInt | None = Field(None, exclude=True)  # type: ignore
    vote_rshares: HiveInt | None = Field(None, exclude=True)  # type: ignore
    children_abs_rshares: HiveInt | None = Field(None, exclude=True)  # type: ignore
    max_cashout_time: HiveDateTime | None = Field(None, exclude=True)  # type: ignore
    total_vote_weight: HiveInt | None = Field(None, exclude=True)  # type: ignore
    reward_weight: HiveInt | None = Field(None, exclude=True)  # type: ignore
    author_rewards: HiveInt | None = Field(None, exclude=True)  # type: ignore
    net_votes: HiveInt | None = Field(None, exclude=True)  # type: ignore
    root_author: AccountName | EmptyString | None = Field(None, exclude=True)  # type: ignore
    root_permlink: Permlink | EmptyString | None = Field(None, exclude=True)  # type: ignore
    allow_replies: bool | None = Field(None, exclude=True)  # type: ignore
    allow_votes: bool | None = Field(None, exclude=True)  # type: ignore
    allow_curation_rewards: bool | None = Field(None, exclude=True)  # type: ignore

    pending_payout_value: AssetHbdLegacy
    promoted: AssetHbdLegacy
    replies: list[str]
    body_length: HiveInt
    author_reputation: HiveInt
    url: str
    root_title: str
    post_id: HiveInt
    active_votes: list[ActiveVotes]


class GetBlogFundament(PreconfiguredBaseModel):
    """Identical as find_comments in database_api, just four more fields"""

    blog: AccountName
    entry_id: HiveInt
    comment: GetCommentDiscussionsByPayoutFundament  # this field is the same as model GetCommentDiscussionByPayout
    reblogged_on: HiveDateTime


class GetDiscussionsByAuthorBeforeDateFundament(GetCommentDiscussionsByPayoutFundament):
    """The same structure as response above ->  GetCommentDiscussionsByPayoutFundament"""


class GetEscrowFundament(fundaments_database_api.EscrowsFundament[AssetHiveLegacy, AssetHbdLegacy]):
    """Identical like response from database_api, just one additional field and Legacy format of Assets
    This response could also be null, the reason why split into Fundament and main response
    """


class GetExpiringVestingDelegationFundament(PreconfiguredBaseModel):
    id_: HiveInt = Field(..., alias="id")
    delegator: AccountName
    vesting_shares: AssetVestsLegacy
    expiration: HiveDateTime


class FollowFundament(PreconfiguredBaseModel):
    """response without base in any other api
    fundament for get_followers and get_following
    """

    follower: AccountName
    following: AccountName
    what: list[str]


class GetOpsInBlockFundament(LegacyApiAllOperationObject):
    """just operation_id from base excluded, rest the same"""

    operation_id: HiveInt | None = Field(None, exclude=True)  # type: ignore


class GetTrendingTagsFundament(PreconfiguredBaseModel):
    name: AccountName
    total_payouts: AssetHbdLegacy
    top_posts: HiveInt
    comments: HiveInt
    net_votes: HiveInt | None
    trending: str | None


class ListProposalsFundament(Proposal[AssetHbdLegacy]):
    """Proposal field converted to Legacy format of Assets"""

    status: str | None = Field(None, exclude=True)  # type: ignore


class ListRcDirectDelegationsFundament(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    delegated_rc: HiveInt


class LookupAccountNamesFundament(
    fundaments_database_api.AccountItemFundament[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]
):
    last_post_edit: HiveDateTime | None = Field(None, exclude=True)  # type: ignore
    is_smt: bool | None = Field(None, exclude=True)  # type: ignore

    voting_power: HiveInt