from __future__ import annotations

from typing import Any, Generic

from pydantic import BaseModel, Field, Json

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.assets.hbd import AssetHbdT
from schemas.fields.assets.hive import AssetHiveT
from schemas.fields.assets.vests import AssetVestsT
from schemas.fields.basic import (
    AccountName,
    EmptyString,
    PublicKey,
)
from schemas.fields.compound import Authority, DelayedVotes, Manabar
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt


class Account(PreconfiguredBaseModel, BaseModel, Generic[AssetHiveT, AssetHbdT, AssetVestsT]):
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
    balance: AssetHiveT
    savings_balance: AssetHiveT
    hbd_balance: AssetHbdT
    hbd_seconds: HiveInt
    hbd_seconds_last_update: HiveDateTime
    hbd_last_interest_payment: HiveDateTime
    savings_hbd_balance: AssetHbdT
    savings_hbd_seconds: HiveInt
    savings_hbd_seconds_last_update: HiveDateTime
    savings_hbd_last_interest_payment: HiveDateTime
    savings_withdraw_requests: HiveInt
    reward_hbd_balance: AssetHbdT
    reward_hive_balance: AssetHiveT
    reward_vesting_balance: AssetVestsT
    reward_vesting_hive: AssetHiveT
    vesting_shares: AssetVestsT
    delegated_vesting_shares: AssetVestsT
    received_vesting_shares: AssetVestsT
    vesting_withdraw_rate: AssetVestsT
    post_voting_power: AssetVestsT
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


class GetCollateralizedConversionRequestsFundament(
    PreconfiguredBaseModel, BaseModel, Generic[AssetHiveT, AssetHbdT]
):
    id_: HiveInt = Field(alias="id")
    owner: AccountName
    requestid: HiveInt
    collateral_amount: AssetHiveT
    converted_amount: AssetHbdT
    conversion_date: HiveDateTime


class GetConversionRequestsFundament(PreconfiguredBaseModel, BaseModel, Generic[AssetHbdT]):
    id_: HiveInt = Field(alias="id")
    owner: AccountName
    requestid: HiveInt
    amount: AssetHbdT
    conversion_date: HiveDateTime


class FindRecurrentTransfersFundament(PreconfiguredBaseModel, BaseModel, Generic[AssetHiveT, AssetHbdT]):
    id_: HiveInt = Field(alias="id")
    trigger_date: HiveDateTime
    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetHiveT | AssetHbdT
    memo: str
    recurrence: HiveInt
    consecutive_failures: HiveInt
    remaining_executions: HiveInt
    pair_id: HiveInt


class ListRcDirectDelegationsFundament(PreconfiguredBaseModel):
    from_: AccountName = Field(alias="from")
    to: AccountName
    delegated_rc: HiveInt
