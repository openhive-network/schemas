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
    HbdExchangeRate,
    HiveDateTime,
    HiveInt,
    PublicKey,
)
from schemas.__private.hive_fields_custom_schemas import (
    DelayedVotes,
    FloatAsString,
    HardforkVersion,
    Manabar,
    Permlink,
    Price,
    Proposal,
    Props,
    RdDynamicParams,
    Sha256,
    Version,
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


class FindChangeRecoveryAccountRequestsFundament(PreconfiguredBaseModel):
    id_: HiveInt = Field(..., alias="id")
    account_to_recover: AccountName | EmptyString
    recovery_account: AccountName | EmptyString
    effective_on: HiveDateTime


class FindCollateralizedConversionRequestsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    id_: HiveInt = Field(..., alias="id")
    owner: AccountName
    requestid: HiveInt
    collateral_amount: AssetHive
    converted_amount: AssetHbd
    conversion_date: HiveDateTime


class FindCommentsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHbd]):
    id_: HiveInt = Field(..., alias="id")
    author: EmptyString | AccountName
    permlink: EmptyString | Permlink
    category: EmptyString | str
    parent_author: EmptyString | AccountName
    parent_permlink: EmptyString | Permlink
    title: EmptyString | str
    body: EmptyString | str
    json_metadata: str
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
    total_vote_weight: HiveInt
    reward_weight: HiveInt
    total_payout_value: AssetHbd
    curator_payout_value: AssetHbd
    author_rewards: HiveInt
    net_votes: HiveInt
    root_author: AccountName | EmptyString
    root_permlink: Permlink | EmptyString
    max_accepted_payout: AssetHbd
    percent_hbd: HiveInt
    allow_replies: bool
    allow_votes: bool
    allow_curation_rewards: bool
    beneficiaries: list[Any]
    was_voted_on: bool


class FindDeclineVotingRightsRequestsFundament(PreconfiguredBaseModel):
    id_: HiveInt = Field(..., alias="id")
    account: AccountName
    effective_date: HiveDateTime


class EscrowsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    """Fundament class for list_escrows and find_escrows API responses"""

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


class HbdConversionRequestsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHbd]):
    """Fundament class for find_hbd_convertion_requests and list_hbd_conversion_requests"""

    id_: HiveInt = Field(..., alias="id")
    owner: AccountName
    requestid: HiveInt
    amount: AssetHbd
    conversion_date: HiveDateTime


class LimitOrdersFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    """Fundament class for find_limit_orders and list_limit_orders API responses"""

    id_: HiveInt = Field(..., alias="id")
    created: HiveDateTime
    expiration: HiveDateTime
    seller: AccountName | EmptyString
    orderid: HiveInt
    for_sale: HiveInt
    sell_price: Price[AssetHive, AssetHbd]


class OwnerHistoriesFundament(PreconfiguredBaseModel):
    """Fundament class for find_owner_histories and list_owner_histories API response"""

    id_: HiveInt = Field(..., alias="id")
    account: AccountName
    previous_owner_authority: Authority
    last_valid_time: HiveDateTime


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
    pair_id: HiveInt


class SavingsWithdrawalsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    """Fundament class for find_savings_withdrawals and list_savings_withdrawals"""

    id_: HiveInt = Field(..., alias="id")
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    memo: str
    request_id: HiveInt
    amount: AssetHive | AssetHbd
    complete: HiveDateTime


class VestingDelegationExpirationsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetVests]):
    """Fundament class for find_vesting_delegation_expirations and list_vesting_delegation_expirations"""

    id_: HiveInt = Field(..., alias="id")
    delegator: AccountName
    vesting_shares: AssetVests
    expiration: HiveDateTime


class VestingDelegationsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetVests]):
    """Fundament class for find_vesting_delegation and list_vesting_delegation"""

    id_: HiveInt = Field(..., alias="id")
    delegator: AccountName
    delegatee: AccountName
    vesting_shares: AssetVests
    min_delegation_time: HiveDateTime


class WithdrawVestingRoutesFundament(PreconfiguredBaseModel):
    """Fundament class for find_withdraw_vesting_routes and list_withdraw_vesting_routes"""

    id_: HiveInt = Field(..., alias="id")
    from_account: AccountName
    to_account: AccountName
    percent: HiveInt
    auto_vest: bool


class WitnessesFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    """Fundament class for find_witnesses and list_witnesses API responses"""

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
    props: Props[AssetHive]
    hbd_exchange_rate: HbdExchangeRate[AssetHive, AssetHbd]
    last_hbd_exchange_update: HiveDateTime
    last_work: Sha256
    running_version: HardforkVersion
    hardfork_version_vote: HardforkVersion
    hardfork_time_vote: HiveDateTime
    available_witness_account_subsidies: HiveInt


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


class GetCommentPendingPayoutsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHbd]):
    author: AccountName
    permlink: Permlink
    cashout_info: CashoutInfoField[AssetHbd] | None


class GetOrderBookFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    """
    Fundament class for both fields in GetOrderBook
    """

    order_price: Price[AssetHive, AssetHbd]
    real_price: FloatAsString
    hive: HiveInt
    hbd: HiveInt
    created: HiveDateTime


class GetRewardFundsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive]):
    id_: HiveInt = Field(..., alias="id")
    name: AccountName
    reward_balance: AssetHive
    recent_claims: HiveInt
    last_update: HiveDateTime
    content_constant: HiveInt
    percent_curation_rewards: HiveInt
    percent_content_rewards: HiveInt
    author_reward_curve: str
    curation_reward_curve: str


class GetWitnessScheduleFutureChangesFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive]):
    """Fundament class for future_changes field in get_witness_schedule response from API"""

    median_props: Props[AssetHive] | None = None
    num_scheduled_witnesses: HiveInt | None = None
    elected_weight: HiveInt | None = None
    timeshare_weight: HiveInt | None = None
    miner_weight: HiveInt | None = None
    witness_pay_normalization_factor: HiveInt | None = None
    majority_version: Version | None = None
    max_voted_witnesses: HiveInt | None = None
    max_miner_witnesses: HiveInt | None = None
    max_runner_witnesses: HiveInt | None = None
    hardfork_required_witnesses: HiveInt | None = None
    account_subsidy_rd: RdDynamicParams | None = None
    account_subsidy_witness_rd: RdDynamicParams | None = None
    min_witness_account_subsidy_decay: HiveInt | None = None


class ListAccountRecoveryRequestsFundament(PreconfiguredBaseModel):
    id_: HiveInt = Field(..., alias="id")
    account_to_recover: AccountName
    new_owner_authority: Authority
    expires: HiveDateTime


class ListChangeRecoveryAccountRequestsFundament(PreconfiguredBaseModel):
    id_: HiveInt = Field(..., alias="id")
    account_to_recover: AccountName
    recovery_account: AccountName | EmptyString
    effective_on: HiveDateTime


class ListCollateralizedConversionRequestsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    id_: HiveInt = Field(..., alias="id")
    owner: AccountName
    requestid: HiveInt
    collateral_amount: AssetHive
    converted_amount: AssetHbd
    conversion_date: HiveDateTime


class ListCommentsFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHbd]):
    author_rewards: HiveInt
    id_: HiveInt = Field(..., alias="id")
    author: AccountName
    permlink: Permlink
    category: str
    title: str
    body: str
    json_metadata: str
    created: HiveDateTime
    last_update: HiveDateTime
    depth: HiveInt
    children: HiveInt
    last_payout: HiveDateTime
    cashout_time: HiveDateTime
    max_cashout_time: HiveDateTime
    curator_payout_value: AssetHbd
    total_payout_value: AssetHbd
    reward_weight: HiveInt
    root_author: AccountName
    root_permlink: Permlink
    allow_replies: bool
    allow_votes: bool
    allow_curation_rewards: bool
    parent_author: AccountName | EmptyString
    parent_permlink: Permlink
    beneficiaries: list[str]
    max_accepted_payout: AssetHbd
    percent_hbd: HiveInt
    net_votes: HiveInt
    total_vote_weight: HiveInt
    vote_rshares: HiveInt
    net_rshares: HiveInt
    abs_rshares: HiveInt
    children_abs_rshares: HiveInt


class ListDeclineVotingRightsRequestsFundament(PreconfiguredBaseModel):
    id_: HiveInt = Field(..., alias="id")
    account: AccountName
    effective_date: HiveDateTime


class ListProposalVotesFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHbd]):
    id_: HiveInt = Field(..., alias="id")
    voter: AccountName
    proposal: Proposal[AssetHbd]


class ListWitnessVotesFundament(PreconfiguredBaseModel):
    id_: HiveInt = Field(..., alias="id")
    witness: AccountName
    account: AccountName
