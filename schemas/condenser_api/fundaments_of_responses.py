from __future__ import annotations

from typing import Any

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
from schemas.__private.hive_fields_custom_schemas import Permlink
from schemas.__private.operation_objects import LegacyApiAllOperationObject
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


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


class GetBlogFundament(fundaments_database_api.FindCommentsFundament[AssetHbdLegacy]):
    """Identical as find_comments in database_api, just four more fields"""

    active: HiveDateTime
    blog: AccountName
    reblog_on: HiveDateTime
    entry_id: HiveInt


class GetBlogEntriesFundament(PreconfiguredBaseModel):
    author: AccountName
    permlink: str
    blog: AccountName
    reblog_on: HiveDateTime
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
