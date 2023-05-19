from __future__ import annotations

from pydantic import Field

import schemas.block_api.fundaments_of_responses as fundaments_block_api
import schemas.database_api.fundaments_of_reponses as fundaments_database_api
from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbdLegacy,
    AssetHiveLegacy,
    AssetVestsLegacy,
    HiveDateTime,
    HiveInt,
)
from schemas.__private.operation_objects import LegacyApiAllOperationObject
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class GetAccountsFundament(
    fundaments_database_api.AccountItemFundament[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]
):
    """Base for this response is list_accounts from database api. Some additional fields are here and two excluded"""

    last_post_edit = Field(None, exclude=True)  # type: ignore
    is_smt = Field(None, exclude=True)  # type: ignore

    post_history: list[str]
    vote_history: list[str]
    witness_votes: list[str]
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


class GetBlockHeaderFundament(fundaments_block_api.GetBlockHeaderFundament):
    """Identical as in block_api, just extensions changed"""


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
