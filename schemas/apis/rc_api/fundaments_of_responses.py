from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetVests,
    HiveInt,
)
from schemas.__private.hive_fields_custom_schemas import Manabar
from schemas._preconfigured_base_model import PreconfiguredBaseModel


class RcAccount(PreconfiguredBaseModel, GenericModel, Generic[AssetVests]):
    account: AccountName
    rc_manabar: Manabar
    max_rc_creation_adjustment: AssetVests
    max_rc: HiveInt
    delegated_rc: HiveInt
    received_delegated_rc: HiveInt


class DecayParams(PreconfiguredBaseModel):
    decay_per_time_unit: HiveInt
    decay_per_time_unit_denom_shift: HiveInt


class ResourceDynamicParams(PreconfiguredBaseModel):
    resource_unit: HiveInt
    budget_per_time_unit: HiveInt
    pool_eq: HiveInt
    max_pool_size: HiveInt
    decay_params: DecayParams
    min_decay: HiveInt


class PriceCurveParams(PreconfiguredBaseModel):
    coeff_a: HiveInt
    coeff_b: HiveInt
    shift: HiveInt


class ResourceParam(PreconfiguredBaseModel):
    resource_dynamics_params: ResourceDynamicParams
    price_curve_params: PriceCurveParams


class ResourceParams(PreconfiguredBaseModel):
    resource_history_bytes: ResourceParam
    resource_new_accounts: ResourceParam
    resource_market_bytes: ResourceParam
    resource_state_bytes: ResourceParam
    resource_execution_time: ResourceParam


class ResourceStateBytes(PreconfiguredBaseModel):
    TEMPORARY_STATE_BYTE: HiveInt
    LASTING_STATE_BYTE: HiveInt
    PERSISTENT_STATE_BYTE: HiveInt
    account_create_base_size: HiveInt
    authority_account_member_size: HiveInt
    authority_key_member_size: HiveInt
    owner_authority_history_object_size: HiveInt
    transfer_to_vesting_size: HiveInt
    request_account_recovery_size: HiveInt
    change_recovery_account_size: HiveInt
    comment_base_size: HiveInt
    comment_permlink_char_size: HiveInt
    comment_beneficiaries_member_size: HiveInt
    vote_size: HiveInt
    convert_size: HiveInt
    collateralized_convert_size: HiveInt
    decline_voting_rights_size: HiveInt
    escrow_transfer_size: HiveInt
    limit_order_create_size: HiveInt
    transfer_from_savings_size: HiveInt
    transaction_base_size: HiveInt
    vesting_delegation_object_size: HiveInt
    vesting_delegation_expiration_object_size: HiveInt
    delegate_vesting_shares_size: HiveInt
    set_withdraw_vesting_route_size: HiveInt
    witness_update_base_size: HiveInt
    witness_update_url_char_size: HiveInt
    account_witness_vote_size: HiveInt
    create_proposal_base_size: HiveInt
    create_proposal_subject_permlink_char_size: HiveInt
    update_proposal_votes_member_size: HiveInt
    recurrent_transfer_base_size: HiveInt
    recurrent_transfer_memo_char_size: HiveInt
    delegate_rc_base_size: HiveInt


class ResourceExecutionTime(PreconfiguredBaseModel):
    account_create_time: HiveInt
    account_create_with_delegation_time: HiveInt
    account_witness_vote_time: HiveInt
    comment_time: HiveInt
    comment_options_time: HiveInt
    convert_time: HiveInt
    collateralized_convert_time: HiveInt
    create_claimed_account_time: HiveInt
    decline_voting_rights_time: HiveInt
    delegate_vesting_shares_time: HiveInt
    escrow_transfer_time: HiveInt
    limit_order_create_time: HiveInt
    limit_order_create2_time: HiveInt
    request_account_recovery_time: HiveInt
    set_withdraw_vesting_route_time: HiveInt
    vote_time: HiveInt
    witness_update_time: HiveInt
    transfer_time: HiveInt
    transfer_to_vesting_time: HiveInt
    transfer_to_savings_time: HiveInt
    transfer_from_savings_time: HiveInt
    claim_reward_balance_time: HiveInt
    withdraw_vesting_time: HiveInt
    account_update_time: HiveInt
    account_update2_time: HiveInt
    account_witness_proxy_time: HiveInt
    cancel_transfer_from_savings_time: HiveInt
    change_recovery_account_time: HiveInt
    claim_account_time: HiveInt
    custom_time: HiveInt
    custom_json_time: HiveInt
    custom_binary_time: HiveInt
    delete_comment_time: HiveInt
    escrow_approve_time: HiveInt
    escrow_dispute_time: HiveInt
    escrow_release_time: HiveInt
    feed_publish_time: HiveInt
    limit_order_cancel_time: HiveInt
    witness_set_properties_time: HiveInt
    create_proposal_time: HiveInt
    update_proposal_time: HiveInt
    update_proposal_votes_time: HiveInt
    remove_proposal_time: HiveInt
    recurrent_transfer_base_time: HiveInt
    recurrent_transfer_processing_time: HiveInt
    delegate_rc_time: HiveInt
    verify_authority_time: HiveInt
    transaction_time: HiveInt
    recover_account_time: HiveInt
    pow_time: HiveInt
    pow2_time: HiveInt


class SizeInfo(PreconfiguredBaseModel):
    resource_state_bytes: ResourceStateBytes
    resource_execution_time: ResourceExecutionTime


class Pool(PreconfiguredBaseModel):
    pool: HiveInt
    fill_level: HiveInt


class ResourcePool(PreconfiguredBaseModel):
    resource_history_bytes: Pool
    resource_new_accounts: Pool
    resource_market_bytes: Pool
    resource_state_bytes: Pool
    resource_execution_time: Pool


class RcDirectDelegations(PreconfiguredBaseModel):
    from_: AccountName = Field(alias="from")
    to: AccountName
    delegated_rc: HiveInt
