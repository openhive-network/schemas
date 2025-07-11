from __future__ import annotations

from typing import Any

from msgspec import field

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVests
from schemas.fields.basic import AccountName, OptionallyEmptyAccountName, PublicKey
from schemas.fields.compound import Authority, DelayedVotes, Manabar
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.fields.resolvables import AssetUnionAssetHiveAssetHbd, JsonString


class Account(PreconfiguredBaseModel, kw_only=True):
    id_: HiveInt = field(name="id")
    name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: str
    posting_json_metadata: JsonString[Any]
    proxy: OptionallyEmptyAccountName
    previous_owner_update: HiveDateTime
    last_owner_update: HiveDateTime
    last_account_update: HiveDateTime
    created: HiveDateTime
    mined: bool
    recovery_account: OptionallyEmptyAccountName
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
    delayed_votes: list[DelayedVotes] | None = None


class GetCollateralizedConversionRequestsFundament(PreconfiguredBaseModel, kw_only=True):
    id_: HiveInt = field(name="id")
    owner: AccountName
    requestid: HiveInt
    collateral_amount: AssetHive
    converted_amount: AssetHbd
    conversion_date: HiveDateTime


class GetConversionRequestsFundament(PreconfiguredBaseModel, kw_only=True):
    id_: HiveInt = field(name="id")
    owner: AccountName
    requestid: HiveInt
    amount: AssetHbd
    conversion_date: HiveDateTime


class FindRecurrentTransfersFundament(PreconfiguredBaseModel, kw_only=True):
    id_: HiveInt = field(name="id")
    trigger_date: HiveDateTime
    from_: AccountName = field(name="from")
    to: AccountName
    amount: AssetUnionAssetHiveAssetHbd
    memo: str
    recurrence: HiveInt
    consecutive_failures: HiveInt
    remaining_executions: HiveInt
    pair_id: HiveInt


class ListRcDirectDelegationsFundament(PreconfiguredBaseModel, kw_only=True):
    from_: AccountName = field(name="from")
    to: AccountName
    delegated_rc: HiveInt
