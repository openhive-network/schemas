from schemas.predefined import *


# TODO After development the custom schema checking the 'operations', complete the diagrams below.
# [op]get_account_history
# [op]get_block ->extensions
# [op]get_transaction 'operations'
# [op]get_ops_in_block 'pole 'op'

broadcast_transaction = Map({})

broadcast_transaction_synchronous = Map({
    'block_num': Int(),
    'expired': Bool(),
    'id': TransactionId(),
    'trx_num': Int(),
})

__account = Map({
    'id': Int(),
    'name': Str(),
    'owner': Authority(),
    'active': Authority(),
    'posting': Authority(),
    'memo_key': PublicKey(),
    'json_metadata': AnyOf(Json(), EmptyString()),
    'posting_json_metadata': AnyOf(Json(), EmptyString()),
    'proxy': Str(),
    'previous_owner_update': Date(),
    'last_owner_update': Date(),
    'last_account_update': Date(),
    'created': Date(),
    'mined': Bool(),
    'recovery_account': Str(),
    'last_account_recovery': Date(),
    'reset_account': Str(),
    'comment_count': Int(),
    'lifetime_vote_count': Int(),
    'post_count': Int(),
    'can_vote': Bool(),
    'voting_manabar': Manabar(),
    'downvote_manabar': Manabar(),
    'balance': AssetHive(),
    'savings_balance': AssetHive(),
    'hbd_balance': AssetHbd(),
    'hbd_seconds': Int(),
    'hbd_seconds_last_update': Date(),
    'hbd_last_interest_payment': Date(),
    'savings_hbd_balance': AssetHbd(),
    'savings_hbd_seconds': Int(),
    'savings_hbd_seconds_last_update': Date(),
    'savings_hbd_last_interest_payment': Date(),
    'savings_withdraw_requests': Int(),
    'reward_hbd_balance': AssetHbd(),
    'reward_hive_balance': AssetHive(),
    'reward_vesting_balance': AssetVests(),
    'reward_vesting_hive': AssetHive(),
    'vesting_shares': AssetVests(),
    'delegated_vesting_shares': AssetVests(),
    'received_vesting_shares': AssetVests(),
    'vesting_withdraw_rate': AssetVests(),
    'post_voting_power': AssetVests(),
    'next_vesting_withdrawal': Date(),
    'withdrawn': Int(),
    'to_withdraw': Int(),
    'withdraw_routes': Int(),
    'pending_transfers': Int(),
    'curation_rewards': Int(),
    'posting_rewards': Int(),
    'proxied_vsf_votes': Array(
        Int(),
    ),
    'witnesses_voted_for': Int(),
    'last_post': Date(),
    'last_root_post': Date(),
    'last_post_edit': Date(),
    'last_vote_time': Date(),
    'post_bandwidth': Int(),
    'pending_claimed_accounts': Int(),
    'open_recurrent_transfers': Int(),
    'is_smt': Bool(),
    'delayed_votes': Array(
        Map({
            'time': Date(),
            'val': Int(),
        })
    ),
    'governance_vote_expiration_ts': Date(),
})

get_account = AnyOf(
    Null(),
    __account,
)

get_account_history = Array(
    ArrayStrict(
        Int(),
        Map({
            'trx_id': TransactionId(),
            'block': Int(),
            'trx_in_block': Int(),
            'op_in_trx': Int(),
            'virtual_op': Bool(),
            'timestamp': Date(),
            'op': Map({
                'type': Str(),
                'value': Map({}, allow_additional_properties=True),
            }),
            'operation_id': Int(),
        }),
    )
)

get_accounts = Array(__account)

list_accounts = Array(Str())

list_my_accounts = Array(__account)

find_recurrent_transfers = Array(
    Map({
        'id': Int(),
        'trigger_date': Date(),
        'from': Str(),
        'to': Str(),
        'amount': AssetHive(),
        'memo': Str(),
        'recurrence': Int(),
        'consecutive_failures': Int(),
        'remaining_executions': Int(),
    })
)

get_block = AnyOf(
    Map({}),
    Map({
        'block': Map({
            'previous': TransactionId(),
            'timestamp': Date(),
            'witness': Str(),
            'transaction_merkle_root': TransactionId(),
            'extensions': Array(
                Map({
                    'type': Str(),
                    'value': AnyOf(
                        Str(),
                        Map({}, allow_additional_properties=True),
                    ),
                })
            ),
            'witness_signature': Str(),
            'transactions': Array(Map({}, allow_additional_properties=True)),
            'block_id': TransactionId(),
            'signing_key': PublicKey(),
            'transaction_ids': Array(TransactionId()),
        })
    })
)

get_chain_properties = Map({
    'account_creation_fee': AssetHive(),
    'maximum_block_size': Int(),
    'hbd_interest_rate': Int(),
    'account_subsidy_budget': Int(),
    'account_subsidy_decay': Int(),
})

get_collateralized_conversion_requests = Array(
    Map({
        'id': Int(),
        'owner': Str(),
        'requestid': Int(),
        'collateral_amount': AssetHive(),
        'converted_amount': AssetHbd(),
        'conversion_date': Date(),
    })
)

get_conversion_requests = Array(
    Map({
        'id': Int(),
        'owner': Str(),
        'requestid': Int(),
        'amount': AssetHbd(),
        'conversion_date': Date(),
    })
)

get_current_median_history_price = Price(AssetHbd(), AssetHive())

get_dynamic_global_properties = Map({
    'id': Int(),
    'head_block_number': Int(),
    'head_block_id': TransactionId(),
    'time': Date(),
    'current_witness': Str(),
    'total_pow': Int(),
    'num_pow_witnesses': Int(),
    'virtual_supply': AssetHive(),
    'current_supply': AssetHive(),
    'init_hbd_supply': AssetHbd(),
    'current_hbd_supply': AssetHbd(),
    'total_vesting_fund_hive': AssetHive(),
    'total_vesting_shares': AssetVests(),
    'total_reward_fund_hive': AssetHive(),
    'total_reward_shares2': Int(),
    'pending_rewarded_vesting_shares': AssetVests(),
    'pending_rewarded_vesting_hive': AssetHive(),
    'hbd_interest_rate': Int(),
    'hbd_print_rate': Int(),
    'maximum_block_size': Int(),
    'required_actions_partition_percent': Int(),
    'current_aslot': Int(),
    'recent_slots_filled': Int(),
    'participation_count': Int(),
    'last_irreversible_block_num': Int(),
    'vote_power_reserve_rate': Int(),
    'delegation_return_period': Int(),
    'reverse_auction_seconds': Int(),
    'available_account_subsidies': Int(),
    'hbd_stop_percent': Int(),
    'hbd_start_percent': Int(),
    'next_maintenance_time': Date(),
    'last_budget_time': Date(),
    'next_daily_maintenance_time': Date(),
    'content_reward_percent': Int(),
    'vesting_reward_percent': Int(),
    'proposal_fund_percent': Int(),
    'dhf_interval_ledger': AssetHbd(),
    'downvote_pool_percent': Int(),
    'current_remove_threshold': Int(),
    'early_voting_seconds': Int(),
    'mid_voting_seconds': Int(),
    'max_consecutive_recurrent_transfer_failures': Int(),
    'max_recurrent_transfer_end_date': Int(),
    'min_recurrent_transfers_recurrence': Int(),
    'max_open_recurrent_transfers': Int(),
})

get_feed_history = Map({
    'id': Int(),
    'current_median_history': Price(AssetHbd(), AssetHive()),
    'market_median_history': Price(AssetHbd(), AssetHive()),
    'current_min_history': Price(AssetHbd(), AssetHive()),
    'current_max_history': Price(AssetHbd(), AssetHive()),
    'price_history': Array(
        Price(AssetHbd(), AssetHive())
    ),
})

get_hardfork_version = HardforkVersion()

get_open_orders = Array(
    Map({
        'id': Int(),
        'created': Date(),
        'expiration': Date(),
        'seller': Str(),
        'orderid': Int(),
        'for_sale': Int(),
        'sell_price': Price(AssetHive(), AssetHbd()),
    })
)

get_ops_in_block = Map({
    'ops': Array(
        Map({
            'trx_id': Int(),
            'block': Int(),
            'trx_in_block': Int(),
            'op_in_trx': Int(),
            'virtual_op': Bool(),
            'timestamp': Date(),
            'op': Map({
                'type': Str(),
                'value': Map({}, allow_additional_properties=True),
            }),
            'operation_id': Int(),
        })
    )
})

get_order_book = Map({
    'asks': Array(
        Map({
            'order_price': Price(AssetHive(), AssetHbd()),
            'real_price': Str(),
            'hive': Int(),
            'hbd': Int(),
            'created': Date(),
        })
    ),
    'bids': Array(
        Map({
            'order_price': Price(AssetHive(), AssetHbd()),
            'real_price': Str(),
            'hive': Int(),
            'hbd': Int(),
            'created': Date(),
        })
    )
})

get_owner_history = Map({
    'owner_auths': Array(
        Map({
            'id': Int(),
            'account': Str(),
            'previous_owner_authority': Authority(),
            'last_valid_time': Date(),
        })
    )
})

get_reward_fund = Map({
    'id': Int(),
    'name': Str(),
    'reward_balance': AssetHive(),
    'recent_claims': Int(),
    'last_update': Date(),
    'content_constant': Int(),
    'percent_curation_rewards': Int(),
    'percent_content_rewards': Int(),
    'author_reward_curve': Str(),
    'curation_reward_curve': Str(),
})

get_transaction = Map({
    'ref_block_num': Int(),
    'ref_block_prefix': Int(),
    'expiration': Date(),
    'operations': Array(
        Map({
            'type': Str(),
            'value': Map({}, allow_additional_properties=True),
        }),
    ),
    'extensions': Array(Any()),
    'signatures': Array(Str()),
    'transaction_id': TransactionId(),
    'block_num': Int(),
    'transaction_num': Int(),
})

get_version = Map({
    'blockchain_version': HardforkVersion(),
    'hive_revision': Str(),
    'fc_revision': Str(),
    'chain_id': Str(),
})

get_withdraw_routes = Array(
    Map({
        'id': Int(),
        'from_account': Str(),
        'to_account': Str(),
        'percent': Int(),
        'auto_vest': Bool(),
    })
)

is_known_transaction = Bool()

find_proposals = Map({
    'proposals': Array(
        Proposal(),
    )
})

list_proposal_votes = Map({
    'proposal_votes': Array(
        Map({
            'id': Int(),
            'voter': Str(),
            'proposal': Proposal(),
        })
    )
})

list_proposals = Map({
        'proposals': Array(
            Proposal(),
        )
    })

find_rc_accounts = Array(
    Map({
        'account': Str(),
        'rc_manabar': Manabar(),
        'max_rc_creation_adjustment': AssetVests(),
        'max_rc': Int(),
        'delegated_rc': Int(),
        'received_delegated_rc': Int(),
    })
)

list_rc_accounts = Array(
    Map({
        'account': Str(),
        'rc_manabar': Manabar(),
        'max_rc_creation_adjustment': AssetVests(),
        'max_rc': Int(),
        'delegated_rc': Int(),
        'received_delegated_rc': Int(),
    })
)

list_rc_direct_delegations = Array(
    Map({
        'from': Str(),
        'to': Str(),
        'delegated_rc': Int(),
    })
)

get_active_witnesses = Map({
    'witnesses': Array(Str(), minItems=1, maxItems=21),
})

get_witness = AnyOf(
    Null(),
    Map({
        'id': Int(),
        'owner': Str(),
        'created': Date(),
        'url': Str(),
        'votes': Int(),
        'virtual_last_update': Int(),
        'virtual_position': Int(),
        'virtual_scheduled_time': Int(),
        'total_missed': Int(),
        'last_aslot': Int(),
        'last_confirmed_block_num': Int(),
        'pow_worker': Int(),
        'signing_key': PublicKey(),
        'props': Map({
            'account_creation_fee': AssetHive(),
            'maximum_block_size': Int(),
            'hbd_interest_rate': Int(),
            'account_subsidy_budget': Int(),
            'account_subsidy_decay': Int(),
        }),
        'hbd_exchange_rate': Price(AssetHive(), AssetHive()),
        'last_hbd_exchange_update': Date(),
        'last_work': Str(),
        'running_version': HardforkVersion(),
        'hardfork_version_vote': HardforkVersion(),
        'hardfork_time_vote': Date(),
        'available_witness_account_subsidies': Int(),
    })
)

get_witness_schedule = Map({
    'id': Int(),
    'current_virtual_time': Int(),
    'next_shuffle_block_num': Int(),
    'current_shuffled_witnesses': Array(Str(), minItems=1, maxItems=21),
    'num_scheduled_witnesses': Int(minimum=1, maximum=21),
    'elected_weight': Int(),
    'timeshare_weight': Int(),
    'miner_weight': Int(),
    'witness_pay_normalization_factor': Int(),
    'median_props': Map({
        'account_creation_fee': AssetHive(),
        'maximum_block_size': Int(),
        'hbd_interest_rate': Int(),
        'account_subsidy_budget': Int(),
        'account_subsidy_decay': Int(),
    }),
    'majority_version': HardforkVersion(),
    'max_voted_witnesses': Int(),
    'max_miner_witnesses': Int(),
    'max_runner_witnesses': Int(),
    'hardfork_required_witnesses': Int(),
    'account_subsidy_rd': Map({
        'resource_unit': Int(),
        'budget_per_time_unit': Int(),
        'pool_eq': Int(),
        'max_pool_size': Int(),
        'decay_params': Map({
            'decay_per_time_unit': Int(),
            'decay_per_time_unit_denom_shift': Int(),
        }),
        'min_decay': Int(),
    }),
    'account_subsidy_witness_rd': Map({
        'resource_unit': Int(),
        'budget_per_time_unit': Int(),
        'pool_eq': Int(),
        'max_pool_size': Int(),
        'decay_params': Map({
            'decay_per_time_unit': Int(),
            'decay_per_time_unit_denom_shift': Int(),
        }),
        'min_decay': Int(),
    }),
    'min_witness_account_subsidy_decay': Int(),
})

list_witnesses = Map({
    'witnesses': Array(
        Map({
            'id': Int(),
            'owner': Str(),
            'created': Date(),
            'url': Str(),
            'votes': Int(),
            'virtual_last_update': Int(),
            'virtual_position': Int(),
            'virtual_scheduled_time': Int(),
            'total_missed': Int(),
            'last_aslot': Int(),
            'last_confirmed_block_num': Int(),
            'pow_worker': Int(),
            'signing_key': PublicKey(),
            'props': Map({
                'account_creation_fee': AssetHive(),
                'maximum_block_size': Int(),
                'hbd_interest_rate': Int(),
                'account_subsidy_budget': Int(),
                'account_subsidy_decay': Int(),
            }),
            'hbd_exchange_rate': Price(AssetHive(), AssetHive()),
            'last_hbd_exchange_update': Date(),
            'last_work': Str(),
            'running_version': HardforkVersion(),
            'hardfork_version_vote': HardforkVersion(),
            'hardfork_time_vote': Date(),
            'available_witness_account_subsidies': Int(),
        })
    )
})
