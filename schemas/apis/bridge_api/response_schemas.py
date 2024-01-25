from __future__ import annotations

from typing import Any

from pydantic import Field

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.bridge_api.fundaments_of_reponses import GetPostItem, GetProfileItem, PostNotification
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt

GetPost = list[GetPostItem]
GetAccountPosts = list[GetPostItem]
GetRankedPosts = list[GetPostItem]
GetProfile = GetProfileItem
GetTrendingTopics = list[tuple[AccountName, str]]


class GetRelationshipBetweenAccounts(PreconfiguredBaseModel):
    follows: bool
    ignores: bool
    blacklists: bool
    follows_blacklists: bool
    follows_muted: bool


GetFollowList = list[Any]
DoesUserFollowAnyLists = bool
PostNotifications = list[PostNotification]
AccountNotifications = list[PostNotification]


class UnreadNotifications(PreconfiguredBaseModel):
    lastread: HiveDateTime
    unread: HiveInt


GetPayoutStats = list[tuple[str, str, float, HiveInt, HiveInt | None]]


class GetCommunity(PreconfiguredBaseModel):
    id_: HiveInt = Field(alias="id")
    name: str
    title: str
    about: str
    lang: str
    type_id: HiveInt
    is_nsfw: bool
    subscribers: HiveInt
    created_at: HiveDateTime
    sum_pending: HiveInt
    num_pending: HiveInt
    num_authors: HiveInt
    avatar_url: str
    description: str
    flag_text: str
    settings: Any
    context: Any
    team: list[tuple[str, str, str]]


class GetCommunityContext(PreconfiguredBaseModel):
    role: str
    subscribed: bool
    title: str


class ListCommunities(PreconfiguredBaseModel):
    id_: HiveInt = Field(alias="id")
    name: str
    title: str
    about: str
    lang: str
    type_id: HiveInt
    is_nsfw: bool
    subscribers: HiveInt
    sum_pending: HiveInt
    num_pending: HiveInt
    num_authors: HiveInt
    created_at: HiveDateTime
    avatar_url: str
    context: Any
    admins: list[AccountName]


ListPopCommunities = list[tuple[AccountName, str]]
ListCommunityRoles = list[tuple[AccountName, str, str]]
ListSubscribers = list[tuple[AccountName, str, str | None, HiveDateTime]]
ListAllSubscriptions = list[tuple[str, str, str, str]]
