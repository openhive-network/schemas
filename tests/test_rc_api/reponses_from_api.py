from __future__ import annotations

FIND_RC_ACCOUNTS = {
    "id": 0,
    "jsonrpc": "2.0",
    "result": {
        "rc_accounts": [
            {
                "account": "alice",
                "rc_manabar": {"current_mana": "0", "last_update_time": 0},
                "max_rc_creation_adjustment": {
                    "amount": "0",
                    "precision": 6,
                    "nai": "@@000000037",
                },
                "max_rc": "0",
                "delegated_rc": "85392710",
                "received_delegated_rc": "85392710",
            }
        ]
    },
}

GET_RESOURCE_PARAMS = {
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
                    "decay_params": {
                        "decay_per_time_unit": 3613026481,
                        "decay_per_time_unit_denom_shift": 51,
                    },
                    "min_decay": 0,
                },
                "price_curve_params": {
                    "coeff_a": "10525659774662010880",
                    "coeff_b": 211332338,
                    "shift": 50,
                },
            },
            "resource_new_accounts": {
                "resource_dynamics_params": {
                    "resource_unit": 10000,
                    "budget_per_time_unit": 797,
                    "pool_eq": 157691079,
                    "max_pool_size": 157691079,
                    "decay_params": {
                        "decay_per_time_unit": 347321,
                        "decay_per_time_unit_denom_shift": 36,
                    },
                    "min_decay": 0,
                },
                "price_curve_params": {
                    "coeff_a": "16484671763857882971",
                    "coeff_b": 1231961,
                    "shift": 51,
                },
            },
            "resource_market_bytes": {
                "resource_dynamics_params": {
                    "resource_unit": 10,
                    "budget_per_time_unit": 72338,
                    "pool_eq": 2003755169,
                    "max_pool_size": 4007510337,
                    "decay_params": {
                        "decay_per_time_unit": 2540365427,
                        "decay_per_time_unit_denom_shift": 46,
                    },
                    "min_decay": 0,
                },
                "price_curve_params": {
                    "coeff_a": "14969827235074865152",
                    "coeff_b": 15654337,
                    "shift": 55,
                },
            },
            "resource_state_bytes": {
                "resource_dynamics_params": {
                    "resource_unit": 1,
                    "budget_per_time_unit": 43546196,
                    "pool_eq": "27139923979692",
                    "max_pool_size": "54279847959383",
                    "decay_params": {
                        "decay_per_time_unit": 3613026481,
                        "decay_per_time_unit_denom_shift": 51,
                    },
                    "min_decay": 0,
                },
                "price_curve_params": {
                    "coeff_a": "10525659774662010880",
                    "coeff_b": "212030656091",
                    "shift": 50,
                },
            },
            "resource_execution_time": {
                "resource_dynamics_params": {
                    "resource_unit": 1,
                    "budget_per_time_unit": 40000000,
                    "pool_eq": "69256028844",
                    "max_pool_size": "138512057687",
                    "decay_params": {
                        "decay_per_time_unit": 2539677724,
                        "decay_per_time_unit_denom_shift": 42,
                    },
                    "min_decay": 0,
                },
                "price_curve_params": {
                    "coeff_a": "14969827235074865152",
                    "coeff_b": 541062725,
                    "shift": 59,
                },
            },
        },
        "size_info": {
            "resource_state_bytes": {
                "TEMPORARY_STATE_BYTE": 1,
                "LASTING_STATE_BYTE": 21900,
                "PERSISTENT_STATE_BYTE": 43800,
                "account_create_base_size": 46953600,
                "authority_account_member_size": 1051200,
                "authority_key_member_size": 1576800,
                "owner_authority_history_object_size": 120960,
                "transfer_to_vesting_size": 11520,
                "request_account_recovery_size": 4608,
                "change_recovery_account_size": 97920,
                "comment_base_size": 4237056,
                "comment_permlink_char_size": 168,
                "comment_beneficiaries_member_size": 1344,
                "vote_size": 24192,
                "convert_size": 10080,
                "collateralized_convert_size": 10752,
                "decline_voting_rights_size": 92160,
                "escrow_transfer_size": 4730400,
                "limit_order_create_size": 139776,
                "transfer_from_savings_size": 16704,
                "transaction_base_size": 128,
                "vesting_delegation_object_size": 1927200,
                "vesting_delegation_expiration_object_size": 14400,
                "delegate_vesting_shares_size": 1927200,
                "set_withdraw_vesting_route_size": 3153600,
                "witness_update_base_size": 23827200,
                "witness_update_url_char_size": 43800,
                "account_witness_vote_size": 1191360,
                "create_proposal_base_size": 336,
                "create_proposal_subject_permlink_char_size": 1,
                "update_proposal_votes_member_size": 1121280,
                "recurrent_transfer_base_size": 200,
                "recurrent_transfer_memo_char_size": 1,
                "delegate_rc_base_size": 1927200,
            },
            "resource_execution_time": {
                "account_create_time": 38710,
                "account_create_with_delegation_time": 40591,
                "account_witness_vote_time": 14741,
                "comment_time": 66178,
                "comment_options_time": 6202,
                "convert_time": 20563,
                "collateralized_convert_time": 23663,
                "create_claimed_account_time": 58415,
                "decline_voting_rights_time": 29091,
                "delegate_vesting_shares_time": 16727,
                "escrow_transfer_time": 19586,
                "limit_order_create_time": 14703,
                "limit_order_create2_time": 24391,
                "request_account_recovery_time": 7947,
                "set_withdraw_vesting_route_time": 10257,
                "vote_time": 18312,
                "witness_update_time": 4237,
                "transfer_time": 5999,
                "transfer_to_vesting_time": 42245,
                "transfer_to_savings_time": 6523,
                "transfer_from_savings_time": 17550,
                "claim_reward_balance_time": 27561,
                "withdraw_vesting_time": 221526,
                "account_update_time": 13322,
                "account_update2_time": 13648,
                "account_witness_proxy_time": 58126,
                "cancel_transfer_from_savings_time": 3154,
                "change_recovery_account_time": 10470,
                "claim_account_time": 8781,
                "custom_time": 674,
                "custom_json_time": 1509,
                "custom_binary_time": 100000,
                "delete_comment_time": 18050,
                "escrow_approve_time": 9663,
                "escrow_dispute_time": 6574,
                "escrow_release_time": 15340,
                "feed_publish_time": 3059,
                "limit_order_cancel_time": 6739,
                "witness_set_properties_time": 9450,
                "create_proposal_time": 32988,
                "update_proposal_time": 16781,
                "update_proposal_votes_time": 17304,
                "remove_proposal_time": 135428,
                "recurrent_transfer_base_time": 13908,
                "recurrent_transfer_processing_time": 14347,
                "delegate_rc_time": 75000,
                "verify_authority_time": 94165,
                "transaction_time": 6622,
                "recover_account_time": 18955,
                "pow_time": 201001,
                "pow2_time": 103827,
            },
        },
    },
    "id": 1,
}


GET_RESOURCE_POOL = {
    "id": 0,
    "jsonrpc": "2.0",
    "result": {
        "resource_pool": {
            "resource_history_bytes": {"pool": "22530662270", "fill_level": 0},
            "resource_new_accounts": {"pool": 17589594, "fill_level": 0},
            "resource_market_bytes": {"pool": 1919726127, "fill_level": 0},
            "resource_state_bytes": {"pool": "17720687726725", "fill_level": 0},
            "resource_execution_time": {"pool": "5835324988127", "fill_level": 0},
        }
    },
}

LIST_RC_ACCOUNTS = FIND_RC_ACCOUNTS

LIST_RC_DIRECT_DELEGATIONS = {
    "id": 0,
    "jsonrpc": "2.0",
    "result": {"rc_direct_delegations": [{"from": "abraham", "to": "lincoln", "delegated_rc": "98765432123456789"}]},
}
