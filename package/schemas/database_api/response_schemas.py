from schemas.predefined import *
from test_tools import Asset


find_account_recovery_requests = Map({
    'requests': Array(
        Map({
            'id': Int(),
            'account_to_recover': AccountName(),
            'new_owner_authority': Authority(),
            'expires': Date(),
        })
    )
})

find_accounts = Map({
    'accounts': Array(
        Map({
            'id': Int(),
            'name': AccountName(),
            'owner': Authority(),
            'active': Authority(),
            'posting': Authority(),
            'memo_key': PublicKey(),
            'json_metadata': AnyOf(Json(), Str(pattern='')),
            'posting_json_metadata': AnyOf(Json(), Str(pattern='')),
            'proxy': Str(),
            'previous_owner_update': Date(),
            'last_owner_update': Date(),
            'last_account_update': Date(),
            'created': Date(),
            'mined': Bool(),
            'recovery_account': AnyOf(AccountName(), Str(pattern='')),
            'last_account_recovery': Date(),
            'reset_account': AccountName(),
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
            'proxied_vsf_votes': Array(Int()),
            'witnesses_voted_for': Int(),
            'last_post': Date(),
            'last_root_post': Date(),
            'last_post_edit': Date(),
            'last_vote_time': Date(),
            'post_bandwidth': Int(),
            'pending_claimed_accounts': Int(),
            'open_recurrent_transfers': Int(),
            'is_smt': Bool(),
            'delayed_votes': Array(),
            'governance_vote_expiration_ts': Date()
        })
    )
})

find_change_recovery_account_requests = Map({
    'requests': Array(
        Map({
            'id': Int(),
            'account_to_recover': AccountName(),
            'recovery_account': AnyOf(AccountName(), Str(pattern='')),
            'effective_on': Date(),
        })
    )
})

find_collateralized_conversion_requests = Map({
    'requests': Array(
        Map({
            'id': Int(),
            'owner': AccountName(),
            'requestid': Int(),
            'collateral_amount': AssetHive(),
            'converted_amount': AssetHbd(),
            'conversion_date': Date(),
        })
    )
})

# In find_comments schema there is a plenty of string fields with empty pattern. The reason of this operation is hived
# which don't keep part of information about comments. Only most valuable information is keeped. For getting whole
# information about comments ask hivemind database.

find_comments = Map({
    'comments': Array(
        Map({
            'id': Int(),
            'author': Str(pattern=''),
            'permlink': Str(pattern=''),
            'category': Str(pattern=''),
            'parent_author': Str(pattern=''),
            'parent_permlink': Str(pattern=''),
            'title': Str(pattern=''),
            'body': Str(pattern=''),
            'json_metadata': AnyOf(Json(), Str(pattern='')),
            'last_update': Date(),
            'created': Date(),
            'last_payout': Date(),
            'depth': Int(),
            'children': Int(),
            'net_rshares': Int(),
            'abs_rshares': Int(),
            'vote_rshares': Int(),
            'children_abs_rshares': Int(),
            'cashout_time': Date(),
            'max_cashout_time': Date(),
            'total_vote_weight': Int(),
            'reward_weight': Int(),
            'total_payout_value': AssetHbd(),
            'curator_payout_value': AssetHbd(),
            'author_rewards': Int(),
            'net_votes': Int(),
            'root_author': Str(pattern=''),
            'root_permlink': Str(pattern=''),
            'max_accepted_payout': AssetHbd(),
            'percent_hbd': Int(),
            'allow_replies': Bool(),
            'allow_votes': Bool(),
            'allow_curation_rewards': Bool(),
            'was_voted_on': Bool(),
            'beneficiaries': Array()
        })
    )
})

find_decline_voting_rights_requests = Map({
    'requests': Array(
        Map({
            'id': Int(),
            'account': AccountName(),
            'effective_date': Date(),
        })
    )
})

find_escrows = Map({
    'escrows': Array(
        Map({
            'id': Int(),
            'escrow_id': Int(),
            'from': AccountName(),
            'to': AccountName(),
            'agent': AccountName(),
            'ratification_deadline': Date(),
            'escrow_expiration': Date(),
            'hbd_balance': AssetHbd(),
            'hive_balance': AssetHive(),
            'pending_fee': AssetHbd(),
            'to_approved': Bool(),
            'agent_approved': Bool(),
            'disputed': Bool(),
        })
    )
})

find_hbd_conversion_requests = Map({
    'requests': Array(
        Map({
            'id': Int(),
            'owner': AccountName(),
            'requestid': Int(),
            'amount': AssetHbd(),
            'conversion_date': Date(),
        })
    )
})

find_limit_orders = Map({
    'orders': Array(
        Map({
            'id': Int(),
            'created': Date(),
            'expiration': Date(),
            'seller': AccountName(),
            'orderid': Int(),
            'for_sale': Int(),
            'sell_price': Price(AssetHive(), AssetHbd())
        })
    )
})

find_owner_histories = Map({
    'owner_auths': Array(
        Map({
            'id': Int(),
            'account': AccountName(),
            'previous_owner_authority': Authority(),
            'last_valid_time': Date(),
        })
    )
})

find_proposals = Map({
    'proposals':  Array(
        Proposal()
    )
})

find_recurrent_transfers = Map({
    'recurrent_transfers': Array(
        Map({
            'id': Int(),
            'trigger_date': Date(),
            'from': AccountName(),
            'to': AccountName(),
            'amount': AssetHive(),
            'memo': Str(),
            'recurrence': Int(),
            'consecutive_failures': Int(),
            'remaining_executions': Int(),
        })
    )
})

find_savings_withdrawals = Map({
    'withdrawals': Array(
        Map({
            'id': Int(),
            'from': AccountName(),
            'to': AccountName(),
            'memo': Str(),
            'request_id': Int(),
            'amount': AssetHive(),
            'complete': Date()
        })
    )
})

find_vesting_delegation_expirations = Map({
    'delegations': Array(
        Map({
            'id': Int(),
            'delegator': AccountName(),
            'vesting_shares': AssetVests(),
            'expiration': Date(),
        })
    )
})

find_vesting_delegations = Map({
    'delegations': Array(
        Map({
            'id': Int(),
            'delegator': AccountName(),
            'delegatee': AccountName(),
            'vesting_shares': AssetVests(),
            'min_delegation_time': Date(),
        })
    )
})

find_withdraw_vesting_routes = Map({
    'routes': Array(
        Map({
            'id': Int(),
            'from_account': AccountName(),
            'to_account': AccountName(),
            'percent': Int(),
            'auto_vest': Bool(),
        })
    )
})

find_witnesses = Map({
    'witnesses': Array(
        Map({
            'id': Int(),
            'owner': AccountName(),
            'created': Date(),
            'url': Str(),
            'votes': Int(),
            'virtual_last_update': Str(),
            'virtual_position': Str(),
            'virtual_scheduled_time': Str(),
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

# when witnesses are not elected they are displayed as empty string. The situation does not exist in mainnet.
get_active_witnesses = Map({
    'witnesses': Array(
        AnyOf(
            AccountName(),
            Str(pattern='')
        )
    )
})

get_comment_pending_payouts = Map({
    'cashout_infos': Array(
        Map({
            'author': AccountName(),
            'permlink': Permlink(),
            'cashout_info': Map({
                'total_vote_weight': Int(),
                'total_payout_value': AssetHbd(),
                'curator_payout_value': AssetHbd(),
                'max_accepted_payout': AssetHbd(),
                'author_rewards': Int(),
                'children_abs_rshares': Int(),
                'net_rshares': Int(),
                'abs_rshares': Int(),
                'vote_rshares': Int(),
                'net_votes': Int(),
                'last_payout': Date(),
                'cashout_time': Date(),
                'max_cashout_time': Date(),
                'percent_hbd': Int(),
                'reward_weight': Int(),
                'allow_replies': Bool(),
                'allow_votes': Bool(),
                'allow_curation_rewards': Bool(),
                'was_voted_on': Bool(),
            })
        })
    )
})

get_config = Map({
    'HIVE_CHAIN_ID': Hex(),
    'HIVE_TREASURY_ACCOUNT': AccountName(),
    'IS_TEST_NET': Bool(),
    'HIVE_ENABLE_SMT': Bool(),
    'HIVE_DEFAULT_HF_9_COMPROMISED_ACCOUNTS_PUBLIC_KEY_STR': PublicKey(),
    'HIVE_INIT_PUBLIC_KEY_STR': PublicKey(),
    'HIVE_HF_9_COMPROMISED_ACCOUNTS_PUBLIC_KEY_STR': PublicKey(),
    'HIVE_INIT_PUBLIC_KEY': PublicKey(),
    'HIVE_BLOCKCHAIN_VERSION': HardforkVersion(),
    'OLD_CHAIN_ID': Hex(),
    'HIVE_ADDRESS_PREFIX': Str(),
    'HIVE_GENESIS_TIME': Date(),
    'HIVE_MINING_TIME': Date(),
    'HIVE_CASHOUT_WINDOW_SECONDS': Int(),
    'HIVE_CASHOUT_WINDOW_SECONDS_PRE_HF12': Int(),
    'HIVE_CASHOUT_WINDOW_SECONDS_PRE_HF17': Int(),
    'HIVE_SECOND_CASHOUT_WINDOW': Int(),
    'HIVE_MAX_CASHOUT_WINDOW_SECONDS': Int(),
    'HIVE_UPVOTE_LOCKOUT_HF7': Int(),
    'HIVE_UPVOTE_LOCKOUT_SECONDS': Int(),
    'HIVE_UPVOTE_LOCKOUT_HF17': Int(),
    'HIVE_MIN_ACCOUNT_CREATION_FEE': Int(),
    'HIVE_MAX_ACCOUNT_CREATION_FEE': Int(),
    'HIVE_OWNER_AUTH_RECOVERY_PERIOD': Int(),
    'HIVE_ACCOUNT_RECOVERY_REQUEST_EXPIRATION_PERIOD': Int(),
    'HIVE_OWNER_UPDATE_LIMIT': Int(),
    'HIVE_OWNER_AUTH_HISTORY_TRACKING_START_BLOCK_NUM': Int(),
    'HIVE_INIT_SUPPLY': Int(),
    'HIVE_HBD_INIT_SUPPLY': Int(),
    'TESTNET_BLOCK_LIMIT': Int(),
    'HIVE_PROPOSAL_MAINTENANCE_PERIOD': Int(),
    'HIVE_PROPOSAL_MAINTENANCE_CLEANUP': Int(),
    'HIVE_DAILY_PROPOSAL_MAINTENANCE_PERIOD': Int(),
    'HIVE_GOVERNANCE_VOTE_EXPIRATION_PERIOD': Int(),
    'HIVE_GLOBAL_REMOVE_THRESHOLD': Int(),
    'HIVE_START_MINER_VOTING_BLOCK': Int(),
    'HIVE_DELAYED_VOTING_TOTAL_INTERVAL_SECONDS': Int(),
    'HIVE_DELAYED_VOTING_INTERVAL_SECONDS': Int(),
    'HIVE_REVERSE_AUCTION_WINDOW_SECONDS_HF25': Int(),
    'HIVE_EARLY_VOTING_SECONDS_HF25': Int(),
    'HIVE_MID_VOTING_SECONDS_HF25': Int(),
    'VESTS_SYMBOL': Map({
        'nai': AssetVests.Nai(),
        'decimals': AssetVests.Precision(),
    }),
    'HIVE_SYMBOL': Map({
        'nai': AssetHive.Nai(),
        'decimals': AssetHive.Precision(),
    }),
    'HBD_SYMBOL': Map({
        'nai': AssetHbd.Nai(),
        'decimals': AssetHbd.Precision(),
    }),
    'HIVE_BLOCKCHAIN_HARDFORK_VERSION': HardforkVersion(),
    'HIVE_100_PERCENT': Int(),
    'HIVE_1_PERCENT': Int(),
    'HIVE_1_BASIS_POINT': Int(),
    'HIVE_BLOCK_INTERVAL': Int(),
    'HIVE_BLOCKS_PER_YEAR': Int(),
    'HIVE_BLOCKS_PER_DAY': Int(),
    'HIVE_START_VESTING_BLOCK': Int(),
    'HIVE_INIT_MINER_NAME': AccountName(),
    'HIVE_NUM_INIT_MINERS': Int(),
    'HIVE_INIT_TIME': Date(),
    'HIVE_MAX_WITNESSES': Int(),
    'HIVE_MAX_VOTED_WITNESSES_HF0': Int(),
    'HIVE_MAX_MINER_WITNESSES_HF0': Int(),
    'HIVE_MAX_RUNNER_WITNESSES_HF0': Int(),
    'HIVE_MAX_VOTED_WITNESSES_HF17': Int(),
    'HIVE_MAX_MINER_WITNESSES_HF17': Int(),
    'HIVE_MAX_RUNNER_WITNESSES_HF17': Int(),
    'HIVE_HARDFORK_REQUIRED_WITNESSES': Int(),
    'HIVE_MAX_TIME_UNTIL_EXPIRATION': Int(),
    'HIVE_MAX_MEMO_SIZE': Int(),
    'HIVE_MAX_PROXY_RECURSION_DEPTH': Int(),
    'HIVE_VESTING_WITHDRAW_INTERVALS_PRE_HF_16': Int(),
    'HIVE_VESTING_WITHDRAW_INTERVALS': Int(),
    'HIVE_VESTING_WITHDRAW_INTERVAL_SECONDS': Int(),
    'HIVE_MAX_WITHDRAW_ROUTES': Int(),
    'HIVE_MAX_PENDING_TRANSFERS': Int(),
    'HIVE_MAX_OPEN_RECURRENT_TRANSFERS': Int(),
    'HIVE_MAX_CONSECUTIVE_RECURRENT_TRANSFER_FAILURES': Int(),
    'HIVE_MAX_RECURRENT_TRANSFER_END_DATE': Int(),
    'HIVE_MAX_RECURRENT_TRANSFERS_PER_BLOCK': Int(),
    'HIVE_MIN_RECURRENT_TRANSFERS_RECURRENCE': Int(),
    'HIVE_SAVINGS_WITHDRAW_TIME': Int(),
    'HIVE_SAVINGS_WITHDRAW_REQUEST_LIMIT': Int(),
    'HIVE_VOTING_MANA_REGENERATION_SECONDS': Int(),
    'HIVE_MAX_VOTE_CHANGES': Int(),
    'HIVE_REVERSE_AUCTION_WINDOW_SECONDS_HF6': Int(),
    'HIVE_REVERSE_AUCTION_WINDOW_SECONDS_HF20': Int(),
    'HIVE_REVERSE_AUCTION_WINDOW_SECONDS_HF21': Int(),
    'HIVE_MIN_VOTE_INTERVAL_SEC': Int(),
    'HIVE_VOTE_DUST_THRESHOLD': Int(),
    'HIVE_DOWNVOTE_POOL_PERCENT_HF21': Int(),
    'HIVE_MIN_ROOT_COMMENT_INTERVAL': Int(),
    'HIVE_MIN_REPLY_INTERVAL': Int(),
    'HIVE_MIN_REPLY_INTERVAL_HF20': Int(),
    'HIVE_MIN_COMMENT_EDIT_INTERVAL': Int(),
    'HIVE_POST_AVERAGE_WINDOW': Int(),
    'HIVE_POST_WEIGHT_CONSTANT': Int(),
    'HIVE_MAX_ACCOUNT_WITNESS_VOTES': Int(),
    'HIVE_DEFAULT_HBD_INTEREST_RATE': Int(),
    'HIVE_INFLATION_RATE_START_PERCENT': Int(),
    'HIVE_INFLATION_RATE_STOP_PERCENT': Int(),
    'HIVE_INFLATION_NARROWING_PERIOD': Int(),
    'HIVE_CONTENT_REWARD_PERCENT_HF16': Int(),
    'HIVE_VESTING_FUND_PERCENT_HF16': Int(),
    'HIVE_PROPOSAL_FUND_PERCENT_HF0': Int(),
    'HIVE_CONTENT_REWARD_PERCENT_HF21': Int(),
    'HIVE_PROPOSAL_FUND_PERCENT_HF21': Int(),
    'HIVE_HF21_CONVERGENT_LINEAR_RECENT_CLAIMS': Int(),
    'HIVE_CONTENT_CONSTANT_HF21': Int(),
    'HIVE_MINER_PAY_PERCENT': Int(),
    'HIVE_MAX_RATION_DECAY_RATE': Int(),
    'HIVE_BANDWIDTH_AVERAGE_WINDOW_SECONDS': Int(),
    'HIVE_BANDWIDTH_PRECISION': Int(),
    'HIVE_MAX_COMMENT_DEPTH_PRE_HF17': Int(),
    'HIVE_MAX_COMMENT_DEPTH': Int(),
    'HIVE_SOFT_MAX_COMMENT_DEPTH': Int(),
    'HIVE_MAX_RESERVE_RATIO': Int(),
    'HIVE_CREATE_ACCOUNT_WITH_HIVE_MODIFIER': Int(),
    'HIVE_CREATE_ACCOUNT_DELEGATION_RATIO': Int(),
    'HIVE_CREATE_ACCOUNT_DELEGATION_TIME': Int(),
    'HIVE_MINING_REWARD': AssetHive(),
    'HIVE_EQUIHASH_N': Int(),
    'HIVE_EQUIHASH_K': Int(),
    'HIVE_LIQUIDITY_TIMEOUT_SEC': Int(),
    'HIVE_MIN_LIQUIDITY_REWARD_PERIOD_SEC': Int(),
    'HIVE_LIQUIDITY_REWARD_PERIOD_SEC': Int(),
    'HIVE_LIQUIDITY_REWARD_BLOCKS': Int(),
    'HIVE_MIN_LIQUIDITY_REWARD': AssetHive(),
    'HIVE_MIN_CONTENT_REWARD': AssetHive(),
    'HIVE_MIN_CURATE_REWARD': AssetHive(),
    'HIVE_MIN_PRODUCER_REWARD': AssetHive(),
    'HIVE_MIN_POW_REWARD': AssetHive(),
    'HIVE_ACTIVE_CHALLENGE_FEE': AssetHive(),
    'HIVE_OWNER_CHALLENGE_FEE': AssetHive(),
    'HIVE_ACTIVE_CHALLENGE_COOLDOWN': Int(),
    'HIVE_OWNER_CHALLENGE_COOLDOWN': Int(),
    'HIVE_POST_REWARD_FUND_NAME': Str(),
    'HIVE_COMMENT_REWARD_FUND_NAME': Str(),
    'HIVE_RECENT_RSHARES_DECAY_TIME_HF17': Int(),
    'HIVE_RECENT_RSHARES_DECAY_TIME_HF19': Int(),
    'HIVE_CONTENT_CONSTANT_HF0': Int(),
    'HIVE_APR_PERCENT_MULTIPLY_PER_BLOCK': Int(),
    'HIVE_APR_PERCENT_SHIFT_PER_BLOCK': Int(),
    'HIVE_APR_PERCENT_MULTIPLY_PER_ROUND': Int(),
    'HIVE_APR_PERCENT_SHIFT_PER_ROUND': Int(),
    'HIVE_APR_PERCENT_MULTIPLY_PER_HOUR': Int(),
    'HIVE_APR_PERCENT_SHIFT_PER_HOUR': Int(),
    'HIVE_CURATE_APR_PERCENT': Int(),
    'HIVE_CONTENT_APR_PERCENT': Int(),
    'HIVE_LIQUIDITY_APR_PERCENT': Int(),
    'HIVE_PRODUCER_APR_PERCENT': Int(),
    'HIVE_POW_APR_PERCENT': Int(),
    'HIVE_MIN_PAYOUT_HBD': AssetHbd(),
    'HIVE_HBD_START_PERCENT_HF14': Int(),
    'HIVE_HBD_STOP_PERCENT_HF14': Int(),
    'HIVE_HBD_START_PERCENT_HF20': Int(),
    'HIVE_HBD_STOP_PERCENT_HF20': Int(),
    'HIVE_HBD_START_PERCENT_HF26': Int(),
    'HIVE_HBD_STOP_PERCENT_HF26': Int(),
    'HIVE_HBD_HARD_LIMIT_PRE_HF26': Int(),
    'HIVE_HBD_HARD_LIMIT': Int(),
    'HIVE_MIN_ACCOUNT_NAME_LENGTH': Int(enum=[3]),
    'HIVE_MAX_ACCOUNT_NAME_LENGTH': Int(enum=[16]),
    'HIVE_MIN_PERMLINK_LENGTH': Int(),
    'HIVE_MAX_PERMLINK_LENGTH': Int(enum=[256]),
    'HIVE_MAX_WITNESS_URL_LENGTH': Int(),
    'HIVE_MAX_SHARE_SUPPLY': Int(),
    'HIVE_MAX_SATOSHIS': Int(),
    'HIVE_MAX_SIG_CHECK_DEPTH': Int(),
    'HIVE_MAX_SIG_CHECK_ACCOUNTS': Int(),
    'HIVE_MIN_TRANSACTION_SIZE_LIMIT': Int(),
    'HIVE_SECONDS_PER_YEAR': Int(),
    'HIVE_HBD_INTEREST_COMPOUND_INTERVAL_SEC': Int(),
    'HIVE_MAX_TRANSACTION_SIZE': Int(),
    'HIVE_MIN_BLOCK_SIZE_LIMIT': Int(),
    'HIVE_MAX_BLOCK_SIZE': Int(),
    'HIVE_MIN_BLOCK_SIZE': Int(),
    'HIVE_BLOCKS_PER_HOUR': Int(),
    'HIVE_FEED_INTERVAL_BLOCKS': Int(),
    'HIVE_FEED_HISTORY_WINDOW_PRE_HF_16': Int(),
    'HIVE_FEED_HISTORY_WINDOW': Int(),
    'HIVE_MAX_FEED_AGE_SECONDS': Int(),
    'HIVE_MIN_FEEDS': Int(),
    'HIVE_CONVERSION_DELAY_PRE_HF_16': Int(),
    'HIVE_CONVERSION_DELAY': Int(),
    'HIVE_COLLATERALIZED_CONVERSION_DELAY': Int(),
    'HIVE_CONVERSION_COLLATERAL_RATIO': Int(),
    'HIVE_COLLATERALIZED_CONVERSION_FEE': Int(),
    'HIVE_MIN_UNDO_HISTORY': Int(),
    'HIVE_MAX_UNDO_HISTORY': Int(),
    'HIVE_MIN_TRANSACTION_EXPIRATION_LIMIT': Int(),
    'HIVE_BLOCKCHAIN_PRECISION': Int(),
    'HIVE_BLOCKCHAIN_PRECISION_DIGITS': Int(),
    'HIVE_MAX_INSTANCE_ID': Int(),
    'HIVE_MAX_AUTHORITY_MEMBERSHIP': Int(),
    'HIVE_MAX_ASSET_WHITELIST_AUTHORITIES': Int(),
    'HIVE_MAX_URL_LENGTH': Int(),
    'HIVE_IRREVERSIBLE_THRESHOLD': Int(),
    'HIVE_VIRTUAL_SCHEDULE_LAP_LENGTH': Int(),
    'HIVE_VIRTUAL_SCHEDULE_LAP_LENGTH2': Int(),
    'HIVE_INITIAL_VOTE_POWER_RATE': Int(),
    'HIVE_REDUCED_VOTE_POWER_RATE': Int(),
    'HIVE_MAX_LIMIT_ORDER_EXPIRATION': Int(),
    'HIVE_DELEGATION_RETURN_PERIOD_HF0': Int(),
    'HIVE_DELEGATION_RETURN_PERIOD_HF20': Int(),
    'HIVE_RD_MIN_DECAY_BITS': Int(),
    'HIVE_RD_MAX_DECAY_BITS': Int(),
    'HIVE_RD_DECAY_DENOM_SHIFT': Int(),
    'HIVE_RD_MAX_POOL_BITS': Int(),
    'HIVE_RD_MAX_BUDGET_1': Int(),
    'HIVE_RD_MAX_BUDGET_2': Int(),
    'HIVE_RD_MAX_BUDGET_3': Int(),
    'HIVE_RD_MAX_BUDGET': Int(),
    'HIVE_RD_MIN_DECAY': Int(),
    'HIVE_RD_MIN_BUDGET': Int(),
    'HIVE_RD_MAX_DECAY': Int(),
    'HIVE_ACCOUNT_SUBSIDY_PRECISION': Int(),
    'HIVE_WITNESS_SUBSIDY_BUDGET_PERCENT': Int(),
    'HIVE_WITNESS_SUBSIDY_DECAY_PERCENT': Int(),
    'HIVE_DEFAULT_ACCOUNT_SUBSIDY_DECAY': Int(),
    'HIVE_DEFAULT_ACCOUNT_SUBSIDY_BUDGET': Int(),
    'HIVE_DECAY_BACKSTOP_PERCENT': Int(),
    'HIVE_BLOCK_GENERATION_POSTPONED_TX_LIMIT': Int(),
    'HIVE_PENDING_TRANSACTION_EXECUTION_LIMIT': Int(),
    'HIVE_CUSTOM_OP_ID_MAX_LENGTH': Int(),
    'HIVE_CUSTOM_OP_DATA_MAX_LENGTH': Int(),
    'HIVE_BENEFICIARY_LIMIT': Int(),
    'HIVE_COMMENT_TITLE_LIMIT': Int(),
    'HIVE_ONE_DAY_SECONDS': Int(),
    'HIVE_MINER_ACCOUNT': AccountName(),
    'HIVE_NULL_ACCOUNT': AccountName(),
    'HIVE_TEMP_ACCOUNT': AccountName(),
    'HIVE_PROXY_TO_SELF_ACCOUNT': Str(),
    'HIVE_ROOT_POST_PARENT': Str(),
    'OBSOLETE_TREASURY_ACCOUNT': AccountName(),
    'NEW_HIVE_TREASURY_ACCOUNT': AccountName(),
    'HIVE_TREASURY_FEE': Int(),
    'HIVE_PROPOSAL_SUBJECT_MAX_LENGTH': Int(),
    'HIVE_PROPOSAL_MAX_IDS_NUMBER': Int(),
    'HIVE_PROPOSAL_FEE_INCREASE_DAYS': Int(),
    'HIVE_PROPOSAL_FEE_INCREASE_DAYS_SEC': Int(),
    'HIVE_PROPOSAL_FEE_INCREASE_AMOUNT': Int(),
    'HIVE_PROPOSAL_CONVERSION_RATE': Int(),
})

get_current_price_feed = Price(AssetHbd(), AssetHive())

get_dynamic_global_properties = Map({
    'available_account_subsidies': Int(),
    'content_reward_percent': Int(),
    'current_aslot': Int(),
    'current_hbd_supply': AssetHbd(),
    'current_remove_threshold': Int(),
    'current_supply': AssetHive(),
    'current_witness': AccountName(),
    'delegation_return_period': Int(),
    'downvote_pool_percent': Int(),
    'early_voting_seconds':Int(),
    'hbd_interest_rate': Int(),
    'hbd_print_rate': Int(),
    'hbd_start_percent': Int(),
    'hbd_stop_percent': Int(),
    'head_block_id': TransactionId(),
    'head_block_number': Int(),
    'id': Int(),
    'init_hbd_supply': AssetHbd(),
    'last_budget_time': Date(),
    'last_irreversible_block_num': Int(),
    'max_consecutive_recurrent_transfer_failures': Int(),
    'max_open_recurrent_transfers': Int(),
    'max_recurrent_transfer_end_date': Int(),
    'maximum_block_size': Int(),
    'mid_voting_seconds': Int(),
    'min_recurrent_transfers_recurrence': Int(),
    'next_daily_maintenance_time': Date(),
    'next_maintenance_time': Date(),
    'num_pow_witnesses': Int(),
    'participation_count': Int(),
    'pending_rewarded_vesting_hive': AssetHive(),
    'pending_rewarded_vesting_shares': AssetVests(),
    'recent_slots_filled': Int(),
    'required_actions_partition_percent': Int(),
    'reverse_auction_seconds': Int(),
    'proposal_fund_percent': Int(),
    'dhf_interval_ledger': AssetHbd(),
    'time': Date(),
    'total_pow': Int(),
    'total_reward_fund_hive': AssetHive(),
    'total_reward_shares2': Int(),
    'total_vesting_fund_hive': AssetHive(),
    'total_vesting_shares': AssetVests(),
    'vesting_reward_percent': Int(),
    'virtual_supply': AssetHive(),
    'vote_power_reserve_rate': Int(),
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

get_hardfork_properties = Map({
    'id': Int(),
    'processed_hardforks': Array(Date()),
    'last_hardfork': Int(),
    'current_hardfork_version': HardforkVersion(),
    'next_hardfork': HardforkVersion(),
    'next_hardfork_time': Date(),
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
            'order_price': Price(AssetHbd(), AssetHive()),
            'real_price': Str(),
            'hive': Int(),
            'hbd': Int(),
            'created': Date(),
        })
    ),
})

get_potential_signatures = Map({
    'keys': Array(PublicKey())
})

get_required_signatures = Map({
    'keys': Array(PublicKey())
})

get_reward_funds = Map({
    'funds': Array(
        Map({
            'id': Int(),
            'name': AccountName(),
            'reward_balance': AssetHive(),
            'recent_claims': Int(),
            'last_update': Date(),
            'content_constant': Int(),
            'percent_curation_rewards': Int(),
            'percent_content_rewards': Int(),
            'author_reward_curve': Str(),
            'curation_reward_curve': Str(),
        })
    )
})

get_transaction_hex = Map({
    'hex': Hex()
})

get_version = Map({
    'blockchain_version': HardforkVersion(),
    'hive_revision': Hex(),
    'fc_revision': Hex(),
    'chain_id': Hex()
})

get_witness_schedule = Map({
    'id': Int(),
    'current_virtual_time': Int(),
    'next_shuffle_block_num': Int(),
    'current_shuffled_witnesses': Array(
        AnyOf(
            AccountName(),
            Str(pattern='')
        )
    ),
    'num_scheduled_witnesses': Int(),
    'elected_weight': Int(),
    'timeshare_weight': Int(),
    'miner_weight': Int(),
    'witness_pay_normalization_factor': Int(),
    'median_props': Map({
        'account_creation_fee': AssetHive(),
        'maximum_block_size': Int(),
        'hbd_interest_rate': Int(),
        'account_subsidy_budget': Int(),
        'account_subsidy_decay': Int()
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
            'decay_per_time_unit_denom_shift': Int()
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
            'decay_per_time_unit_denom_shift': Int()
        }),
        'min_decay': Int(),
    }),
    'min_witness_account_subsidy_decay': Int()
})

is_known_transaction = Map({
    'is_known': Bool()
})

list_account_recovery_requests = Map({
    'requests': Array(
        Map({
            'id': Int(),
            'account_to_recover': AccountName(),
            'new_owner_authority': Authority(),
            'expires': Date(),
        })
    )
})

list_accounts = Map({
    'accounts': Array(
        Map({
            'id': Int(),
            'name': AccountName(),
            'owner': Authority(),
            'active': Authority(),
            'posting': Authority(),
            'memo_key': PublicKey(),
            'json_metadata': AnyOf(Json(), Str(pattern='')),
            'posting_json_metadata': AnyOf(Json(), Str(pattern='')),
            'proxy': Str(),
            'previous_owner_update': Date(),
            'last_owner_update': Date(),
            'last_account_update': Date(),
            'created': Date(),
            'mined': Bool(),
            'recovery_account': AnyOf(AccountName(), Str(pattern='')),
            'last_account_recovery': Date(),
            'reset_account': AccountName(),
            'comment_count': Int(),
            'lifetime_vote_count': Int(),
            'post_count': Int(),
            'can_vote': Bool(),
            'voting_manabar': Manabar(),
            'downvote_manabar': Manabar(),
            'balance': AssetHive(),
            'savings_balance': AssetHive(),
            'hbd_balance': AssetHbd(),
            'hbd_seconds': Str(),
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
            'proxied_vsf_votes': Array(Int()),
            'witnesses_voted_for': Int(),
            'last_post': Date(),
            'last_root_post': Date(),
            'last_post_edit': Date(),
            'last_vote_time': Date(),
            'post_bandwidth': Int(),
            'pending_claimed_accounts': Int(),
            'open_recurrent_transfers': Int(),
            'is_smt': Bool(),
            'delayed_votes': Array(),
            'governance_vote_expiration_ts': Date(),
        })
    )
})

list_change_recovery_account_requests = Map({
    'requests': Array(
        Map({
            'id': Int(),
            'account_to_recover': AccountName(),
            'recovery_account': AnyOf(AccountName(), Str(pattern='')),
            'effective_on': Date()
        })
    )
})

list_collateralized_conversion_requests = Map({
    'requests': Array(
        Map({
            'id': Int(),
            'owner': AccountName(),
            'requestid': Int(),
            'collateral_amount': AssetHive(),
            'converted_amount': AssetHbd(),
            'conversion_date': Date(),
        })
    )
})

list_decline_voting_rights_requests = Map({
    'requests': Array(
        Map({
            'id': Int(),
            'account': AccountName(),
            'effective_date': Date(),
        })
    )
})

list_escrows = Map({
    'escrows': Array(
        Map({
            'id': Int(),
            'escrow_id': Int(),
            'from': AccountName(),
            'to': AccountName(),
            'agent': AccountName(),
            'ratification_deadline': Date(),
            'escrow_expiration': Date(),
            'hbd_balance': AssetHbd(),
            'hive_balance': AssetHive(),
            'pending_fee': AssetHbd(),
            'to_approved': Bool(),
            'agent_approved': Bool(),
            'disputed': Bool(),
        })
    )
})

list_hbd_conversion_requests = Map({
    'requests': Array(
        Map({
            'id': Int(),
            'owner': AccountName(),
            'requestid': Int(),
            'amount': AssetHbd(),
            'conversion_date': Date(),
        })
    )
})

list_limit_orders = Map({
    'orders': Array(
        Map({
            'id': Int(),
            'created': Date(),
            'expiration': Date(),
            'seller': AccountName(),
            'orderid': Int(),
            'for_sale': Int(),
            'sell_price': Price(AssetHive(), AssetHbd()),
        })
    )
})

list_owner_histories = Map({
    'owner_auths': Array(
        Map({
            'id': Int(),
            'account': AccountName(),
            'previous_owner_authority': Authority(),
            'last_valid_time': Date(),
        })
    )
})

list_proposal_votes = Map({
    'proposal_votes': Array(
        Map({
            'id': Int(),
            'voter': AccountName(),
            'proposal': Proposal(),
        })
    )
})

list_proposals = Map({
    'proposals': Array(Proposal())
})

list_savings_withdrawals = Map({
    'withdrawals': Array(
        Map({
            'id': Int(),
            'from': AccountName(),
            'to': AccountName(),
            'memo': Str(),
            'request_id': Int(),
            'amount': AssetHive(),
            'complete': Date(),
        })
    )
})

list_vesting_delegation_expirations = Map({
    'delegations': Array(
        Map({
            'id': Int(),
            'delegator': AccountName(),
            'vesting_shares': AssetVests(),
            'expiration': Date(),
        })
    )
})

list_vesting_delegations = Map({
    'delegations': Array(
        Map({
            'id': Int(),
            'delegator': AccountName(),
            'delegatee': AccountName(),
            'vesting_shares': AssetVests(),
            'min_delegation_time': Date(),
        })
    )
})

list_withdraw_vesting_routes = Map({
    'routes': Array(
        Map({
            'id': Int(),
            'from_account': AccountName(),
            'to_account': AccountName(),
            'percent': Int(),
            'auto_vest': Bool(),
        })
    )
})

list_witness_votes = Map({
    'votes': Array(
        Map({
            'id': Int(),
            'witness': AccountName(),
            'account': AccountName(),
        })
    )
})

list_witnesses = Map({
    'witnesses': Array(
        Map({
            'id': Int(),
            'owner': AccountName(),
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
            'last_work': Int(),
            'running_version': HardforkVersion(),
            'hardfork_version_vote': HardforkVersion(),
            'hardfork_time_vote': Date(),
            'available_witness_account_subsidies': Int(),
        })
    )
})

verify_authority = Map({
    'valid': Bool()
})

verify_signatures = Map({
    'valid': Bool()
})
