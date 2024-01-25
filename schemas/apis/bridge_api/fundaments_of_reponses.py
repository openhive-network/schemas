from __future__ import annotations

from typing import Any

from pydantic import Field

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.assets.hbd import AssetHbdLegacy
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt


class GetPostItemStats(PreconfiguredBaseModel):
    hide: bool
    gray: bool
    total_votes: HiveInt
    flag_weight: float


class GetPostItemVote(PreconfiguredBaseModel):
    rshares: HiveInt
    voter: AccountName


class GetPostItem(PreconfiguredBaseModel):
    post_id: HiveInt
    author: AccountName
    permlink: str
    category: str
    title: str
    body: str
    json_metadata: dict[str, Any]
    created: HiveDateTime
    updated: HiveDateTime
    depth: HiveInt
    children: HiveInt
    net_rshares: HiveInt
    is_paidout: bool
    payout_at: HiveDateTime
    payout: float
    pending_payout_value: AssetHbdLegacy
    author_payout_value: AssetHbdLegacy
    curator_payout_value: AssetHbdLegacy
    promoted: AssetHbdLegacy
    replies: list[Any]
    reblogs: HiveInt
    author_reputation: float
    stats: GetPostItemStats
    url: str
    beneficiaries: list[Any]
    max_accepted_payout: AssetHbdLegacy
    percent_hbd: HiveInt
    parent_author: AccountName
    parent_permlink: str
    active_votes: list[GetPostItemVote]
    blacklists: list[Any]
    community: str
    community_title: str
    author_role: str
    author_title: str


class GetProfileStats(PreconfiguredBaseModel):
    rank: HiveInt
    following: HiveInt
    followers: HiveInt


class GetProfileItem(PreconfiguredBaseModel):
    id_: HiveInt = Field(alias="id")
    name: AccountName
    created: HiveDateTime
    active: HiveDateTime
    post_count: HiveInt
    reputation: float
    blacklists: list[Any]
    stats: GetProfileStats
    metadata: dict[str, Any]


class PostNotification(PreconfiguredBaseModel):
    id_: HiveInt = Field(alias="id")
    type_: str = Field(alias="type")
    score: HiveInt
    date: HiveDateTime
    msg: str
    url: str
