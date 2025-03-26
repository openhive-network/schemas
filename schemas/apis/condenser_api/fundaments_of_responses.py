from __future__ import annotations

from typing import Any, Literal

from msgspec import field

import schemas.apis.database_api.fundaments_of_reponses as fundaments_database_api
from schemas._operation_objects import LegacyApiAllOperationObject
from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVests
from schemas.fields.basic import (
    AccountName,
    FloatAsString,
    OptionallyEmptyAccountName,
    Permlink,
    Url,
)
from schemas.fields.compound import Proposal
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt


class HiveMindResponses(PreconfiguredBaseModel):
    """Base class for all responses from HiveMind"""

    code: Literal[-32003]
    message: Literal["Assert Exception:false: Supported by hivemind"]
    data: dict[str, Any]


class FindProposalsFundament(Proposal):
    """Change format of Assets to Legacy, excluded status field"""

    status: str | None = field(default=None)  # type: ignore


class GetAccountReputationsFundament(PreconfiguredBaseModel):
    account: AccountName
    reputation: HiveInt


class GetAccountsFundament(fundaments_database_api.AccountItemFundament, kw_only=True):
    """Base for this response is list_accounts from database api. Some additional fields are here and two excluded"""

    last_post_edit: HiveDateTime | None = field(default=None)  # type: ignore
    is_smt: bool | None = field(default=None)  # type: ignore

    post_history: list[str]
    vote_history: list[str]
    witness_votes: list[str]
    vesting_balance: AssetHive
    transfer_history: list[str]
    voting_power: HiveInt
    market_history: list[str]
    tags_usage: list[str]
    reputation: HiveInt
    guest_bloggers: list[str]
    other_history: list[str]


class GetAccountHistoryFundament(LegacyApiAllOperationObject, kw_only=True):
    operation_id: HiveInt = field(default=None)  # type: ignore


class GetActiveVotesFundament(PreconfiguredBaseModel, kw_only=True):
    percent: HiveInt
    reputation: HiveInt
    rshares: HiveInt
    time: HiveDateTime
    voter: AccountName
    weight: HiveInt


class GetBlogEntriesFundament(PreconfiguredBaseModel, kw_only=True):
    author: AccountName
    permlink: str
    blog: AccountName
    reblogged_on: HiveDateTime
    entry_id: HiveInt


class ActiveVotes(PreconfiguredBaseModel, kw_only=True):
    """This is field which is used in GetCommentDiscussionsByPayout model"""

    percent: HiveInt
    reputation: HiveInt
    rshares: HiveInt
    voter: AccountName


class GetCommentDiscussionsByPayoutFundament(fundaments_database_api.FindCommentsFundament, kw_only=True):
    id_: HiveInt | None = field(default=None)  # type: ignore
    abs_rshares: HiveInt | None = field(default=None)  # type: ignore
    vote_rshares: HiveInt | None = field(default=None)  # type: ignore
    children_abs_rshares: HiveInt | None = field(default=None)  # type: ignore
    max_cashout_time: HiveDateTime | None = field(default=None)  # type: ignore
    total_vote_weight: HiveInt | None = field(default=None)  # type: ignore
    reward_weight: HiveInt | None = field(default=None)  # type: ignore
    author_rewards: HiveInt | None = field(default=None)  # type: ignore
    net_votes: HiveInt | None = field(default=None)  # type: ignore
    root_author: OptionallyEmptyAccountName | None = field(default=None)  # type: ignore
    root_permlink: Permlink | None = field(default=None)  # type: ignore
    allow_replies: bool | None = field(default=None)  # type: ignore
    allow_votes: bool | None = field(default=None)  # type: ignore
    allow_curation_rewards: bool | None = field(default=None)  # type: ignore

    pending_payout_value: AssetHbd
    promoted: AssetHbd
    replies: list[str]
    body_length: HiveInt
    author_reputation: HiveInt
    url: Url
    root_title: str
    post_id: HiveInt
    active_votes: list[ActiveVotes]


class GetBlogFundament(PreconfiguredBaseModel, kw_only=True):
    """Identical as find_comments in database_api, just four more fields"""

    blog: AccountName
    entry_id: HiveInt
    comment: GetCommentDiscussionsByPayoutFundament  # this field is the same as model GetCommentDiscussionByPayout
    reblogged_on: HiveDateTime


class GetDiscussionsByAuthorBeforeDateFundament(GetCommentDiscussionsByPayoutFundament, kw_only=True):
    """The same structure as response above ->  GetCommentDiscussionsByPayoutFundament"""


class GetEscrowFundament(fundaments_database_api.EscrowsFundament, kw_only=True):
    """Identical like response from database_api, just one additional field and Legacy format of Assets
    This response could also be null, the reason why split into Fundament and main response
    """


class GetExpiringVestingDelegationFundament(PreconfiguredBaseModel, kw_only=True):
    id_: HiveInt = field(name="id")
    delegator: AccountName
    vesting_shares: AssetVests
    expiration: HiveDateTime


class FollowFundament(PreconfiguredBaseModel, kw_only=True):
    """response without base in any other api
    fundament for get_followers and get_following
    """

    follower: AccountName
    following: AccountName
    what: list[str]


class GetOpsInBlockFundament(LegacyApiAllOperationObject, kw_only=True):
    """just operation_id from base excluded, rest the same"""

    operation_id: HiveInt | None = field(default=None)  # type: ignore


class GetTrendingTagsFundament(PreconfiguredBaseModel, kw_only=True):
    name: AccountName
    total_payouts: AssetHbd
    top_posts: HiveInt
    comments: HiveInt
    net_votes: HiveInt | None = None
    trending: str | None = None


class ListProposalsFundament(Proposal, kw_only=True):
    """Proposal field converted to Legacy format of Assets"""

    status: str | None = field(default=None)  # type: ignore


class ListRcDirectDelegationsFundament(PreconfiguredBaseModel, kw_only=True):
    from_: AccountName = field(name="from")
    to: AccountName
    delegated_rc: HiveInt


class LookupAccountNamesFundament(fundaments_database_api.AccountItemFundament, kw_only=True):
    last_post_edit: HiveDateTime | None = field(default=None)  # type: ignore
    is_smt: bool | None = field(default=None)  # type: ignore

    voting_power: HiveInt


class GetExpiringVestingDelegationsFundament(PreconfiguredBaseModel, kw_only=True):
    id_: HiveInt = field(name="id")
    delegator: AccountName
    vesting_shares: AssetVests
    expiration: HiveDateTime


class GetOpenOrdersFundament(fundaments_database_api.LimitOrdersFundament, kw_only=True):
    """Same as in database_api -> list_limit_orders, just Legacy format of Assets and two additional fields"""

    real_price: FloatAsString
    rewarded: bool


class GetVestingDelegationsFundament(PreconfiguredBaseModel, kw_only=True):
    id_: HiveInt = field(name="id")
    delegator: AccountName
    delegatee: AccountName
    vesting_shares: AssetVests
    min_delegation_time: HiveDateTime
