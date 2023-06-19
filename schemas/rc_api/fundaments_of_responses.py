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
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


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
    authority_base_size: HiveInt
    authority_account_member_size: HiveInt
    authority_key_member_size: HiveInt
    account_object_base_size: HiveInt
    account_authority_object_base_size: HiveInt
    account_recovery_request_object_base_size: HiveInt
    comment_object_base_size: HiveInt
    comment_object_permlink_char_size: HiveInt
    comment_object_parent_permlink_char_size: HiveInt
    comment_object_beneficiaries_member_size: HiveInt
    comment_vote_object_base_size: HiveInt
    convert_request_object_base_size: HiveInt
    decline_voting_rights_request_object_base_size: HiveInt
    escrow_object_base_size: HiveInt
    limit_order_object_base_size: HiveInt
    savings_withdraw_object_byte_size: HiveInt
    transaction_object_base_size: HiveInt
    transaction_object_byte_size: HiveInt
    vesting_delegation_object_base_size: HiveInt
    vesting_delegation_expiration_object_base_size: HiveInt
    withdraw_vesting_route_object_base_size: HiveInt
    witness_object_base_size: HiveInt
    witness_object_url_char_size: HiveInt
    witness_vote_object_base_size: HiveInt
    proposal_object_base_size: HiveInt
    proposal_vote_object_base_size: HiveInt
    proposal_vote_object_member_size: HiveInt
    smt_token_object_size: HiveInt
    smt_ico_object_size: HiveInt
    smt_token_emissions_object_size: HiveInt
    smt_ico_tier_object_size: HiveInt
    smt_contribution_object_size: HiveInt
    votable_assets_item_size: HiveInt
    STATE_BYTES_SCALE: HiveInt


class ResourceExecutionTime(PreconfiguredBaseModel):
    account_create_operation_exec_time: HiveInt
    account_create_with_delegation_operation_exec_time: HiveInt
    account_update_operation_exec_time: HiveInt
    account_update2_operation_exec_time: HiveInt
    account_witness_proxy_operation_exec_time: HiveInt
    account_witness_vote_operation_exec_time: HiveInt
    cancel_transfer_from_savings_operation_exec_time: HiveInt
    change_recovery_account_operation_exec_time: HiveInt
    claim_account_operation_exec_time: HiveInt
    claim_reward_balance_operation_exec_time: HiveInt
    comment_operation_exec_time: HiveInt
    comment_options_operation_exec_time: HiveInt
    convert_operation_exec_time: HiveInt
    create_claimed_account_operation_exec_time: HiveInt
    custom_operation_exec_time: HiveInt
    custom_json_operation_exec_time: HiveInt
    custom_binary_operation_exec_time: HiveInt
    decline_voting_rights_operation_exec_time: HiveInt
    delegate_vesting_shares_operation_exec_time: HiveInt
    delete_comment_operation_exec_time: HiveInt
    escrow_approve_operation_exec_time: HiveInt
    escrow_dispute_operation_exec_time: HiveInt
    escrow_release_operation_exec_time: HiveInt
    escrow_transfer_operation_exec_time: HiveInt
    feed_publish_operation_exec_time: HiveInt
    limit_order_cancel_operation_exec_time: HiveInt
    limit_order_create_operation_exec_time: HiveInt
    limit_order_create2_operation_exec_time: HiveInt
    request_account_recovery_operation_exec_time: HiveInt
    set_withdraw_vesting_route_operation_exec_time: HiveInt
    transfer_from_savings_operation_exec_time: HiveInt
    transfer_operation_exec_time: HiveInt
    transfer_to_savings_operation_exec_time: HiveInt
    transfer_to_vesting_operation_exec_time: HiveInt
    vote_operation_exec_time: HiveInt
    withdraw_vesting_operation_exec_time: HiveInt
    witness_set_properties_operation_exec_time: HiveInt
    witness_update_operation_exec_time: HiveInt
    claim_reward_balance2_operation_exec_time: HiveInt
    smt_setup_operation_exec_time: HiveInt
    smt_setup_emissions_operation_exec_time: HiveInt
    smt_set_setup_parameters_operation_exec_time: HiveInt
    smt_set_runtime_parameters_operation_exec_time: HiveInt
    smt_create_operation_exec_time: HiveInt
    smt_contribute_operation_exec_time: HiveInt
    smt_setup_ico_tier_operation_exec_time: HiveInt
    smt_contributor_payout_action_exec_time: HiveInt
    smt_founder_payout_action_exec_time: HiveInt
    smt_token_launch_action_exec_time: HiveInt
    smt_ico_evaluation_action_exec_time: HiveInt
    smt_ico_launch_action_exec_time: HiveInt
    smt_token_emission_action_exec_time: HiveInt
    create_proposal_operation_exec_time: HiveInt
    update_proposal_votes_operation_exec_time: HiveInt
    remove_proposal_operation_exec_time: HiveInt


class SizeInfo(PreconfiguredBaseModel):
    resource_state_bytes: ResourceStateBytes
    resource_execution_time: ResourceExecutionTime


class Pool(PreconfiguredBaseModel):
    pool: HiveInt


class ResourcePool(PreconfiguredBaseModel):
    resource_history_bytes: Pool
    resource_new_accounts: Pool
    resource_market_bytes: Pool
    resource_state_bytes: Pool
    resource_execution_time: Pool


class RcDirectDelegations(PreconfiguredBaseModel):
    from_id: HiveInt
    to_id: HiveInt
    from_: AccountName = Field(alias="from")
    to: AccountName
    delegated_rc: HiveInt
