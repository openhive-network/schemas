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
from schemas.fields.compound import ProposalFundament
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt


class HiveMindResponses(PreconfiguredBaseModel):
    """Base class for all responses from HiveMind"""

    code: Literal[-32003]
    message: Literal["Assert Exception:false: Supported by hivemind"]
    data: dict[str, Any]


class FindProposalsFundament(ProposalFundament):
    status: str | None = None


class GetAccountReputationsFundament(PreconfiguredBaseModel):
    account: AccountName
    reputation: HiveInt


class GetAccountsFundament(fundaments_database_api.AccountItemBase, kw_only=True):
    """Base for this response is list_accounts from database api. Some additional fields are here and two excluded"""

    last_post_edit: HiveDateTime | None = None
    is_smt: bool | None = None

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
    operation_id: HiveInt | None = None


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


class GetCommentDiscussionsByPayoutFundament(fundaments_database_api.FindCommentsBase, kw_only=True):
    id_: HiveInt | None = field(name="id", default=None)
    abs_rshares: HiveInt | None = None
    vote_rshares: HiveInt | None = None
    children_abs_rshares: HiveInt | None = None
    max_cashout_time: HiveDateTime | None = None
    total_vote_weight: HiveInt | None = None
    reward_weight: HiveInt | None = None
    author_rewards: HiveInt | None = None
    net_votes: HiveInt | None = None
    root_author: OptionallyEmptyAccountName | None = None
    root_permlink: Permlink | None = None
    allow_replies: bool | None = None
    allow_votes: bool | None = None
    allow_curation_rewards: bool | None = None

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
    """Identical like response from database_api, just one additional field.
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

    operation_id: HiveInt | None = None


class GetTrendingTagsFundament(PreconfiguredBaseModel, kw_only=True):
    name: AccountName
    total_payouts: AssetHbd
    top_posts: HiveInt
    comments: HiveInt
    net_votes: HiveInt | None = None
    trending: str | None = None


class ListProposalsFundament(ProposalFundament, kw_only=True):
    status: str | None = None


class ListRcDirectDelegationsFundament(PreconfiguredBaseModel, kw_only=True):
    from_: AccountName = field(name="from")
    to: AccountName
    delegated_rc: HiveInt


class LookupAccountNamesFundament(fundaments_database_api.AccountItemBase, kw_only=True):
    last_post_edit: HiveDateTime | None = None
    is_smt: bool | None = None

    voting_power: HiveInt


class GetExpiringVestingDelegationsFundament(PreconfiguredBaseModel, kw_only=True):
    id_: HiveInt = field(name="id")
    delegator: AccountName
    vesting_shares: AssetVests
    expiration: HiveDateTime


class GetOpenOrdersFundament(fundaments_database_api.LimitOrdersFundament, kw_only=True):
    """Same as in database_api -> list_limit_orders, just two additional fields"""

    real_price: FloatAsString
    rewarded: bool


class GetVestingDelegationsFundament(PreconfiguredBaseModel, kw_only=True):
    id_: HiveInt = field(name="id")
    delegator: AccountName
    delegatee: AccountName
    vesting_shares: AssetVests
    min_delegation_time: HiveDateTime
