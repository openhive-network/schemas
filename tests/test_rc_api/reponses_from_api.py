from __future__ import annotations

FIND_RC_ACCOUNTS = {
    "id": 0,
    "jsonrpc": "2.0",
    "result": {
        "rc_accounts": [
            {
                "account": "alice",
                "rc_manabar": {"current_mana": "0", "last_update_time": 0},
                "max_rc_creation_adjustment": {"amount": "0", "precision": 6, "nai": "@@000000037"},
                "max_rc": "0",
                "delegated_rc": "85392710",
                "received_delegated_rc": "85392710",
            }
        ]
    },
}

GET_RESOURCE_PARAMS = {
    "id": 0,
    "jsonrpc": "2.0",
    "result": {
        "resource_names": [
            "resource_history_bytes",
            "resource_new_accounts",
            "resource_market_bytes",
            "resource_state_bytes",
            "resource_execution_time",
        ],
        "resource_params": {
            "resource_history_bytes": {
                "resource_dynamics_params": {
                    "resource_unit": 1,
                    "budget_per_time_unit": 43403,
                    "pool_eq": "27050539251",
                    "max_pool_size": "54101078501",
                    "decay_params": {"decay_per_time_unit": 3613026481, "decay_per_time_unit_denom_shift": 51},
                    "min_decay": 0,
                },
                "price_curve_params": {"coeff_a": "14034213032882683904", "coeff_b": 211332338, "shift": 52},
            },
            "resource_new_accounts": {
                "resource_dynamics_params": {
                    "resource_unit": 10000,
                    "budget_per_time_unit": 797,
                    "pool_eq": 157691079,
                    "max_pool_size": 157691079,
                    "decay_params": {"decay_per_time_unit": 347321, "decay_per_time_unit_denom_shift": 36},
                    "min_decay": 0,
                },
                "price_curve_params": {"coeff_a": "16484671763857882971", "coeff_b": 1231961, "shift": 51},
            },
            "resource_market_bytes": {
                "resource_dynamics_params": {
                    "resource_unit": 10,
                    "budget_per_time_unit": 72338,
                    "pool_eq": 2003755169,
                    "max_pool_size": 4007510337,
                    "decay_params": {"decay_per_time_unit": 2540365427, "decay_per_time_unit_denom_shift": 46},
                    "min_decay": 0,
                },
                "price_curve_params": {"coeff_a": "9979884823383242752", "coeff_b": 15654337, "shift": 56},
            },
            "resource_state_bytes": {
                "resource_dynamics_params": {
                    "resource_unit": 1,
                    "budget_per_time_unit": 34722222,
                    "pool_eq": "21640431400373",
                    "max_pool_size": "43280862800744",
                    "decay_params": {"decay_per_time_unit": 3613026481, "decay_per_time_unit_denom_shift": 51},
                    "min_decay": 0,
                },
                "price_curve_params": {"coeff_a": "14034213032882683904", "coeff_b": "169065870315", "shift": 52},
            },
            "resource_execution_time": {
                "resource_dynamics_params": {
                    "resource_unit": 1,
                    "budget_per_time_unit": 10273973,
                    "pool_eq": "6403196140384",
                    "max_pool_size": "12806392280766",
                    "decay_params": {"decay_per_time_unit": 3613026481, "decay_per_time_unit_denom_shift": 51},
                    "min_decay": 0,
                },
                "price_curve_params": {"coeff_a": "14034213032882683904", "coeff_b": "50024969847", "shift": 52},
            },
        },
        "size_info": {
            "resource_state_bytes": {
                "authority_base_size": 40000,
                "authority_account_member_size": 180000,
                "authority_key_member_size": 350000,
                "account_object_base_size": 4800000,
                "account_authority_object_base_size": 400000,
                "account_recovery_request_object_base_size": 320000,
                "comment_object_base_size": 2010000,
                "comment_object_permlink_char_size": 10000,
                "comment_object_parent_permlink_char_size": 20000,
                "comment_object_beneficiaries_member_size": 180000,
                "comment_vote_object_base_size": 24675,
                "convert_request_object_base_size": 480000,
                "decline_voting_rights_request_object_base_size": 280000,
                "escrow_object_base_size": 1190000,
                "limit_order_object_base_size": 147440,
                "savings_withdraw_object_byte_size": 14656,
                "transaction_object_base_size": 6090,
                "transaction_object_byte_size": 174,
                "vesting_delegation_object_base_size": 600000,
                "vesting_delegation_expiration_object_base_size": 440000,
                "withdraw_vesting_route_object_base_size": 430000,
                "witness_object_base_size": 2660000,
                "witness_object_url_char_size": 10000,
                "witness_vote_object_base_size": 400000,
                "proposal_object_base_size": 680000,
                "proposal_vote_object_base_size": 240000,
                "proposal_vote_object_member_size": 80000,
                "smt_token_object_size": 2400000,
                "smt_ico_object_size": 403520,
                "smt_token_emissions_object_size": 1040000,
                "smt_ico_tier_object_size": 186240,
                "smt_contribution_object_size": 108640,
                "votable_assets_item_size": 200000,
                "STATE_BYTES_SCALE": 10000,
            },
            "resource_execution_time": {
                "account_create_operation_exec_time": 57700,
                "account_create_with_delegation_operation_exec_time": 57700,
                "account_update_operation_exec_time": 14000,
                "account_update2_operation_exec_time": 14000,
                "account_witness_proxy_operation_exec_time": 117000,
                "account_witness_vote_operation_exec_time": 23000,
                "cancel_transfer_from_savings_operation_exec_time": 11500,
                "change_recovery_account_operation_exec_time": 12000,
                "claim_account_operation_exec_time": 10000,
                "claim_reward_balance_operation_exec_time": 50300,
                "comment_operation_exec_time": 114100,
                "comment_options_operation_exec_time": 13200,
                "convert_operation_exec_time": 15700,
                "create_claimed_account_operation_exec_time": 57700,
                "custom_operation_exec_time": 11400,
                "custom_json_operation_exec_time": 11400,
                "custom_binary_operation_exec_time": 11400,
                "decline_voting_rights_operation_exec_time": 5300,
                "delegate_vesting_shares_operation_exec_time": 19900,
                "delete_comment_operation_exec_time": 51100,
                "escrow_approve_operation_exec_time": 9900,
                "escrow_dispute_operation_exec_time": 11500,
                "escrow_release_operation_exec_time": 17200,
                "escrow_transfer_operation_exec_time": 19100,
                "feed_publish_operation_exec_time": 6200,
                "limit_order_cancel_operation_exec_time": 9600,
                "limit_order_create_operation_exec_time": 31700,
                "limit_order_create2_operation_exec_time": 31700,
                "request_account_recovery_operation_exec_time": 54400,
                "set_withdraw_vesting_route_operation_exec_time": 17900,
                "transfer_from_savings_operation_exec_time": 17500,
                "transfer_operation_exec_time": 9600,
                "transfer_to_savings_operation_exec_time": 6400,
                "transfer_to_vesting_operation_exec_time": 44400,
                "vote_operation_exec_time": 26500,
                "withdraw_vesting_operation_exec_time": 10400,
                "witness_set_properties_operation_exec_time": 9500,
                "witness_update_operation_exec_time": 9500,
                "claim_reward_balance2_operation_exec_time": 50300,
                "smt_setup_operation_exec_time": 41000,
                "smt_setup_emissions_operation_exec_time": 13000,
                "smt_set_setup_parameters_operation_exec_time": 40000,
                "smt_set_runtime_parameters_operation_exec_time": 39000,
                "smt_create_operation_exec_time": 50000,
                "smt_contribute_operation_exec_time": 32000,
                "smt_setup_ico_tier_operation_exec_time": 13000,
                "smt_contributor_payout_action_exec_time": 60000,
                "smt_founder_payout_action_exec_time": 69000,
                "smt_token_launch_action_exec_time": 31000,
                "smt_ico_evaluation_action_exec_time": 21000,
                "smt_ico_launch_action_exec_time": 18000,
                "smt_token_emission_action_exec_time": 2400,
                "create_proposal_operation_exec_time": 31700,
                "update_proposal_votes_operation_exec_time": 12000,
                "remove_proposal_operation_exec_time": 12000,
            },
        },
    },
}

GET_RESOURCE_POOL = {
    "id": 0,
    "jsonrpc": "2.0",
    "result": {
        "resource_pool": {
            "resource_history_bytes": {"pool": "22530662270"},
            "resource_new_accounts": {"pool": 17589594},
            "resource_market_bytes": {"pool": 1919726127},
            "resource_state_bytes": {"pool": "17720687726725"},
            "resource_execution_time": {"pool": "5835324988127"},
        }
    },
}

LIST_RC_ACCOUNTS = FIND_RC_ACCOUNTS

LIST_RC_DIRECT_DELEGATIONS = {
    "id": 0,
    "jsonrpc": "2.0",
    "result": {
        "rc_direct_delegations": [
            {"from_id": 1234, "to_id": "4321", "from": "abraham", "to": "lincoln", "delegated_rc": "98765432123456789"}
        ]
    },
}
