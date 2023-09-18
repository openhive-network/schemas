from __future__ import annotations

from typing import Any, Generic

from pydantic import Field, Json
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbd,
    AssetHive,
    AssetVests,
    Authority,
    EmptyString,
    HiveDateTime,
    HiveInt,
    PublicKey,
)
from schemas.__private.hive_fields_custom_schemas import DelayedVotes, Manabar
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class Account(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd, AssetVests]):
    id_: HiveInt = Field(alias="id")
    name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: str
    posting_json_metadata: Json[Any] | EmptyString
    proxy: AccountName | EmptyString
    previous_owner_update: HiveDateTime
    last_owner_update: HiveDateTime
    last_account_update: HiveDateTime
    created: HiveDateTime
    mined: bool
    recovery_account: AccountName | EmptyString
    last_account_recovery: HiveDateTime
    reset_account: AccountName
    comment_count: HiveInt
    lifetime_vote_count: HiveInt
    post_count: HiveInt
    can_vote: bool
    voting_manabar: Manabar
    downvote_manabar: Manabar
    balance: AssetHive
    savings_balance: AssetHive
    hbd_balance: AssetHbd
    hbd_seconds: HiveInt
    hbd_seconds_last_update: HiveDateTime
    hbd_last_interest_payment: HiveDateTime
    savings_hbd_balance: AssetHbd
    savings_hbd_seconds: HiveInt
    savings_hbd_seconds_last_update: HiveDateTime
    savings_hbd_last_interest_payment: HiveDateTime
    savings_withdraw_requests: HiveInt
    reward_hbd_balance: AssetHbd
    reward_hive_balance: AssetHive
    reward_vesting_balance: AssetVests
    reward_vesting_hive: AssetHive
    vesting_shares: AssetVests
    delegated_vesting_shares: AssetVests
    received_vesting_shares: AssetVests
    vesting_withdraw_rate: AssetVests
    post_voting_power: AssetVests
    next_vesting_withdrawal: HiveDateTime
    withdrawn: HiveInt
    to_withdraw: HiveInt
    withdraw_routes: HiveInt
    pending_transfers: HiveInt
    curation_rewards: HiveInt
    posting_rewards: HiveInt
    proxied_vsf_votes: list[HiveInt]
    witnesses_voted_for: HiveInt
    last_post: HiveDateTime
    last_root_post: HiveDateTime
    last_post_edit: HiveDateTime
    last_vote_time: HiveDateTime
    post_bandwidth: HiveInt
    pending_claimed_accounts: HiveInt
    open_recurrent_transfers: HiveInt
    is_smt: bool
    governance_vote_expiration_ts: HiveDateTime
    delayed_votes: list[DelayedVotes] = Field(default_factory=list)


class GetCollateralizedConversionRequestsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    id_: HiveInt = Field(alias="id")
    owner: AccountName
    requestid: HiveInt
    collateral_amount: AssetHive
    converted_amount: AssetHbd
    conversion_date: HiveDateTime


class GetConversionRequestsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHbd]):
    id_: HiveInt = Field(alias="id")
    owner: AccountName
    requestid: HiveInt
    amount: AssetHbd
    conversion_date: HiveDateTime


class FindRecurrentTransfersFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive]):
    id_: HiveInt = Field(alias="id")
    trigger_date: HiveDateTime
    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetHive
    memo: str
    recurrence: HiveInt
    consecutive_failures: HiveInt
    remaining_executions: HiveInt
    pair_id: HiveInt


class ListRcDirectDelegationsFundament(PreconfiguredBaseModel):
    from_: AccountName = Field(alias="from")
    to: AccountName
    delegated_rc: HiveInt
