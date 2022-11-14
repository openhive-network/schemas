from schemas.predefined import *

__RC_ACCOUNT_API_OBJECT = Map({
    'account': AccountName(),
    'rc_manabar': Manabar(),
    'max_rc_creation_adjustment': AssetVests(),
    'max_rc': Int(),
    'delegated_rc': Int(),
    'received_delegated_rc': Int(),
})

__RESOURCE_DYNAMIC_PARAMS = Map({
    'resource_unit': Int(),
    'budget_per_time_unit': Int(),
    'pool_eq': Int(),
    'max_pool_size': Int(),
    'decay_params': Map({
        'decay_per_time_unit': Int(),
        'decay_per_time_unit_denom_shift': Int(),
    }),
    'min_decay': Int(),
})

__PRICE_CURVE_PARAMS = Map({
    'coeff_a': Int(),
    'coeff_b': Int(),
    'shift': Int(),
})

find_rc_accounts = Map({
    'rc_accounts': Array(__RC_ACCOUNT_API_OBJECT)
})

get_resource_params = Map({
    'resource_names': Array(Str()),
    'resource_params': Map({
        'resource_history_bytes': Map({
            'resource_dynamics_params': __RESOURCE_DYNAMIC_PARAMS,
            'price_curve_params': __PRICE_CURVE_PARAMS,
        }),
        'resource_new_accounts': Map({
            'resource_dynamics_params': __RESOURCE_DYNAMIC_PARAMS,
            'price_curve_params': __PRICE_CURVE_PARAMS,
        }),
        'resource_market_bytes': Map({
            'resource_dynamics_params': __RESOURCE_DYNAMIC_PARAMS,
            'price_curve_params': __PRICE_CURVE_PARAMS,
        }),
        'resource_state_bytes': Map({
            'resource_dynamics_params': __RESOURCE_DYNAMIC_PARAMS,
            'price_curve_params': __PRICE_CURVE_PARAMS,
        }),
        'resource_execution_time': Map({
            'resource_dynamics_params': __RESOURCE_DYNAMIC_PARAMS,
            'price_curve_params': __PRICE_CURVE_PARAMS,
        })
    }),
    'size_info': Map({
        'resource_state_bytes': Map({
            resource_state_size: Int(minimum=0) for resource_state_size in [
                'TEMPORARY_STATE_BYTE',
                'LASTING_STATE_BYTE',
                'PERSISTENT_STATE_BYTE',
                'account_create_base_size',
                'authority_account_member_size',
                'authority_key_member_size',
                'owner_authority_history_object_size',
                'transfer_to_vesting_size',
                'request_account_recovery_size',
                'change_recovery_account_size',
                'comment_base_size',
                'comment_permlink_char_size',
                'comment_beneficiaries_member_size',
                'vote_size',
                'convert_size',
                'collateralized_convert_size',
                'decline_voting_rights_size',
                'escrow_transfer_size',
                'limit_order_create_size',
                'transfer_from_savings_size',
                'transaction_base_size',
                'vesting_delegation_object_size',
                'vesting_delegation_expiration_object_size',
                'delegate_vesting_shares_size',
                'set_withdraw_vesting_route_size',
                'witness_update_base_size',
                'witness_update_url_char_size',
                'account_witness_vote_size',
                'create_proposal_base_size',
                'create_proposal_subject_permlink_char_size',
                'update_proposal_votes_member_size',
                'recurrent_transfer_base_size',
                'delegate_rc_base_size',
            ]
        }),
        'resource_execution_time': Map({
            resource_execution_time: Int(minimum=0) for resource_execution_time in [
                'account_create_time',
                'account_create_with_delegation_time',
                'account_witness_vote_time',
                'comment_time',
                'comment_options_time',
                'convert_time',
                'collateralized_convert_time',
                'create_claimed_account_time',
                'decline_voting_rights_time',
                'delegate_vesting_shares_time',
                'escrow_transfer_time',
                'limit_order_create_time',
                'limit_order_create2_time',
                'request_account_recovery_time',
                'set_withdraw_vesting_route_time',
                'vote_time',
                'witness_update_time',
                'transfer_time',
                'transfer_to_vesting_time',
                'transfer_to_savings_time',
                'transfer_from_savings_time',
                'claim_reward_balance_time',
                'withdraw_vesting_time',
                'account_update_time',
                'account_update2_time',
                'account_witness_proxy_time',
                'cancel_transfer_from_savings_time',
                'change_recovery_account_time',
                'claim_account_time',
                'custom_time',
                'custom_json_time',
                'custom_binary_time',
                'delete_comment_time',
                'escrow_approve_time',
                'escrow_dispute_time',
                'escrow_release_time',
                'feed_publish_time',
                'limit_order_cancel_time',
                'witness_set_properties_time',
                'create_proposal_time',
                'update_proposal_time',
                'update_proposal_votes_time',
                'remove_proposal_time',
                'recurrent_transfer_base_time',
                'recurrent_transfer_processing_time',
                'delegate_rc_time',
                'verify_authority_time',
                'transaction_time',
                'recover_account_time',
                'pow_time',
                'pow2_time',
            ]
        })
    })
})

__RESOURCE_POOL_STATE = Map({
    'pool': Int(),
    'fill_level': Int(),
})

get_resource_pool = Map({
    'resource_pool': Map({
        resource_pool: __RESOURCE_POOL_STATE for resource_pool in [
            'resource_history_bytes',
            'resource_new_accounts',
            'resource_market_bytes',
            'resource_state_bytes',
            'resource_execution_time',
        ]
    })
})

list_rc_accounts = Map({
    'rc_accounts': Array(__RC_ACCOUNT_API_OBJECT)
})

list_rc_direct_delegations = Map({
    'rc_direct_delegations': Array(
        Map({
            'delegated_rc': Int(),
            'from': AccountName(),
            'to': AccountName()
        })
    )
})
