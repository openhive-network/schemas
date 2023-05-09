from __future__ import annotations

from typing import Any, Generic

from pydantic import Field, Json, validator
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_schemas import (
    AccountName,
    AssetHbd,
    AssetHbdNai,
    AssetHive,
    AssetHiveNai,
    AssetVests,
    Authority,
    DelayedVotes,
    EmptyString,
    HardforkVersion,
    HbdExchangeRate,
    HiveDateTime,
    HiveInt,
    Manabar,
    Permlink,
    Price,
    PublicKey,
    Sha256,
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class FindAccountRecoveryRequestsFundament(PreconfiguredBaseModel):
    id_: HiveInt = Field(..., alias="id")
    account_to_recover: AccountName
    new_owner_authority: Authority
    expires: HiveDateTime


class AccountItemFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd, AssetVests]):
    """Base class for FindAccount and ListAccounts"""

    id_: HiveInt = Field(..., alias="id")
    name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: Json[Any] | EmptyString
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
    delayed_votes: list[DelayedVotes]
    governance_vote_expiration_ts: HiveDateTime


class FindChangeRecoveryAccountRequestsFundament(PreconfiguredBaseModel):
    id_: HiveInt = Field(..., alias="id")
    account_to_recover: AccountName
    recovery_account: AccountName | EmptyString
    effective_on: HiveDateTime


class FindCollateralizedConversionRequestsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    id_: HiveInt = Field(..., alias="id")
    owner: AccountName
    request_id: HiveInt
    collateral_amount: AssetHive
    converted_amount: AssetHbd
    conversion_date: HiveDateTime


class FindCommentsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHbd]):
    id_: HiveInt = Field(..., alias="id")
    author: EmptyString
    permlink: EmptyString
    category: EmptyString
    parent_author: EmptyString
    parent_permlink: EmptyString
    title: EmptyString
    body: EmptyString
    json_metadata: Json[Any] | EmptyString
    last_update: HiveDateTime
    created: HiveDateTime
    last_payout: HiveDateTime
    depth: HiveInt
    children: HiveInt
    net_rshares: HiveInt
    abs_rshares: HiveInt
    vote_rshares: HiveInt
    children_abs_rshares: HiveInt
    cashout_time: HiveDateTime
    max_cashout_time: HiveDateTime
    total_vote_weight: HiveDateTime
    reward_weight: HiveInt
    total_payout_value: AssetHbd
    curator_payout_value: AssetHbd
    author_rewards: HiveInt
    net_votes: HiveInt
    root_author: EmptyString
    root_permlink: EmptyString
    max_accepted_payout: AssetHbd
    percent_hbd: HiveInt
    allow_replies: bool
    allow_votes: bool
    allow_curation_rewards: bool
    was_voted_on: bool
    beneficiaries: list[Any]


class FindDeclineVotingRightsRequestsFundament(PreconfiguredBaseModel):
    id_: HiveInt = Field(..., alias="id")
    account: AccountName
    effective_date: HiveDateTime


class FindEscrowsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    id_: HiveInt = Field(..., alias="id")
    escrow_id: HiveInt
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    agent: AccountName
    ratification_deadline: HiveDateTime
    escrow_expiration: HiveDateTime
    hbd_balance: AssetHbd
    hive_balance: AssetHive
    pending_fee: AssetHbd | AssetHive
    to_approved: bool
    agent_approved: bool
    disputed: bool


class FindHbdConversionRequestsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHbd]):
    id_: HiveInt = Field(..., alias="id")
    owner: AccountName
    requestid: HiveInt
    amount: AssetHbd
    conversion_date: HiveDateTime


class FindLimitOrdersFundament(PreconfiguredBaseModel):
    id_: HiveInt = Field(..., alias="id")
    created: HiveDateTime
    expiration: HiveDateTime
    seller: AccountName
    orderid: HiveInt
    for_sale: HiveInt
    sell_price: Price[AssetHiveNai, AssetHbdNai]


class FindOwnerHistoriesFundament(PreconfiguredBaseModel):
    id_: HiveInt = Field(..., alias="id")
    account: AccountName
    previous_owner_authority: Authority
    last_valid_date: HiveDateTime


class FindRecurrentTransfersFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive]):
    id_: HiveInt = Field(..., alias="id")
    trigger_date: HiveDateTime
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    amount: AssetHive
    memo: str
    recurrence: HiveInt
    consecutive_failures: HiveInt
    remaining_executions: HiveInt


class FindSavingsWithdrawalsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    id_: HiveInt = Field(..., alias="id")
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    memo: str
    request_id: HiveInt
    amount: AssetHive | AssetHbd
    complete: HiveDateTime


class FindVestingDelegationExpirationsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetVests]):
    id_: HiveInt = Field(..., alias="id")
    delegator: AccountName
    vesting_shares: AssetVests
    expiration: HiveDateTime


class FindVestingDelegationsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetVests]):
    id_: HiveInt = Field(..., alias="id")
    delegator: AccountName
    delegatee: AccountName
    vesting_shares: AssetVests
    min_delegation_time: HiveDateTime


class FindWithdrawVestingRoutesFundament(PreconfiguredBaseModel):
    id_: HiveInt = Field(..., alias="id")
    from_account: AccountName
    to_account: AccountName
    percent: HiveInt
    auto_vest: bool


class FindWitnessFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive]):
    id_: HiveInt = Field(..., alias="id")
    owner: AccountName
    created: HiveDateTime
    url: str
    votes: HiveInt
    virtual_last_update: str
    virtual_position: str
    virtual_scheduled_time: str
    total_missed: HiveInt
    last_aslot: int
    last_confirmed_block_num: HiveInt
    pow_worker: HiveInt
    signing_key: PublicKey
    props: dict[str, AssetHive | HiveInt]
    hbd_exchange_rate: HbdExchangeRate[AssetHiveNai, AssetHbdNai]
    last_hbd_exchange_update: HiveDateTime
    last_work: Sha256
    running_version: HardforkVersion
    hardfork_version_vote: HardforkVersion
    hardfork_time_vote: HiveDateTime
    available_witness_account_subsidies: HiveInt

    @validator("props")
    @classmethod
    def check_props(cls, value: dict[str, AssetHiveNai | HiveInt]) -> dict[str, AssetHiveNai | HiveInt]:
        allowed_keys = [
            "account_creation_fee",
            "maximum_block_size",
            "hbd_interest_rate",
            "account_subsidy_budget",
            "account_subsidy_decay",
        ]
        for key in value:
            if key not in allowed_keys:
                raise ValueError("Unrecognized key in field props !")
        return value


class CashoutInfoField(PreconfiguredBaseModel, GenericModel, Generic[AssetHbd]):
    """
    This is cashout_info field from get_comment_pending_payouts response
    """

    total_vote_weight: HiveInt
    total_payout_value: AssetHbd
    curator_payout_value: AssetHbd
    max_accepted_payout: AssetHbd
    author_rewards: HiveInt
    children_abs_rshares: HiveInt
    net_rshares: HiveInt
    abs_rshares: HiveInt
    vote_rshares: HiveInt
    net_votes: HiveInt
    last_payout: HiveDateTime
    cashout_time: HiveDateTime
    max_cashout_time: HiveDateTime
    percent_hbd: HiveInt
    reward_weight: HiveInt
    allow_replies: bool
    allow_votes: bool
    allow_curation_rewards: bool
    was_voted_on: bool


class GetCommentPendingPayoutsFundament(PreconfiguredBaseModel):
    author: AccountName
    permlink: Permlink
    cashout_info: CashoutInfoField[AssetHbdNai]
