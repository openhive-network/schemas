from schemas.predefined import *

broadcast_transaction = Map({})

broadcast_transaction_synchronous = Map({
    'block_num': Int(),
    'expired': Bool(),
    'id': TransactionId(),
    'trx_num': Int(),
})

find_proposals = Array(
    Map({
        'creator': AccountName(),
        'daily_pay': LegacyAssetHbd(),
        'end_date': Date(),
        'id': Int(),
        'permlink': Str(),
        'proposal_id': Int(),
        'receiver': AccountName(),
        'start_date': Date(),
        'subject': Str(),
        'total_votes': Int(),
    })
)

find_rc_accounts = Array(RcAccountObject())

find_recurrent_transfers = Array(
    Map({
        'amount': LegacyAssetHive(),
        'consecutive_failures': Int(),
        'from': AccountName(),
        'id': Int(),
        'memo': Str(),
        'recurrence': Int(),
        'remaining_executions': Int(),
        'to': AccountName(),
        'trigger_date': Date(),
    })
)

get_account_count = Int()

get_account_history = Array(
    ArrayStrict(
        Int(),
        Map({
            'block': Int(),
            'op': ArrayStrict(
                Str(),
                Any(),
            ),
            'op_in_trx': Int(),
            'timestamp': Date(),
            'trx_id': TransactionId(),
            'trx_in_block': Int(),
            'virtual_op': Bool(),
        })
    )
)

get_account_reputations = Array(
    Map({
        'account': AccountName(),
        'reputation': Int(),
    })
)

get_accounts = Array(
    Map({
        'id': Int(),
        'name': AccountName(),
        'owner': Authority(),
        'active': Authority(),
        'posting': Authority(),
        'memo_key': PublicKey(),
        'json_metadata': AnyOf(Json(), EmptyString()),
        'posting_json_metadata': AnyOf(Json(), EmptyString()),
        'proxy': AnyOf(AccountName(), EmptyString()),
        'previous_owner_update': Date(),
        'last_owner_update': Date(),
        'last_account_update': Date(),
        'created': Date(),
        'mined': Bool(),
        'recovery_account': AnyOf(AccountName(), EmptyString()),
        'last_account_recovery': Date(),
        'reset_account': AccountName(),
        'comment_count': Int(),
        'lifetime_vote_count': Int(),
        'post_count': Int(),
        'can_vote': Bool(),
        'voting_manabar': Manabar(),
        'downvote_manabar': Manabar(),
        'balance': LegacyAssetHive(),
        'savings_balance': LegacyAssetHive(),
        'hbd_balance': LegacyAssetHbd(),
        'hbd_seconds': Int(),
        'hbd_seconds_last_update': Date(),
        'hbd_last_interest_payment': Date(),
        'savings_hbd_balance': LegacyAssetHbd(),
        'savings_hbd_seconds': Int(),
        'savings_hbd_seconds_last_update': Date(),
        'savings_hbd_last_interest_payment': Date(),
        'savings_withdraw_requests': Int(),
        'reward_hbd_balance': LegacyAssetHbd(),
        'reward_hive_balance': LegacyAssetHive(),
        'reward_vesting_balance': LegacyAssetVests(),
        'reward_vesting_hive': LegacyAssetHive(),
        'vesting_shares': LegacyAssetVests(),
        'delegated_vesting_shares': LegacyAssetVests(),
        'received_vesting_shares': LegacyAssetVests(),
        'vesting_withdraw_rate': LegacyAssetVests(),
        'post_voting_power': LegacyAssetVests(),
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
        'last_vote_time': Date(),
        'post_bandwidth': Int(),
        'pending_claimed_accounts': Int(),
        'open_recurrent_transfers': Int(),
        'delayed_votes': Array(
            Map({
                'time': Date(),
                'val': Int(),
            })
        ),
        'governance_vote_expiration_ts': Date(),
        'post_history': EmptyArray(),
        'vote_history': EmptyArray(),
        'witness_votes': Array(AccountName()),
        'vesting_balance': LegacyAssetHive(),
        'transfer_history': EmptyArray(),
        'voting_power': Int(),
        'market_history': EmptyArray(),
        'tags_usage': EmptyArray(),
        'reputation': Int(),
        'guest_bloggers': EmptyArray(),
        'other_history': EmptyArray(),
    })
)

get_active_votes = Array(
    Map({
        'percent': Int(),
        'reputation': Int(),
        'rshares': Int(),
        'time': Date(),
        'voter': AccountName(),
        'weight': Int(),
    })
)

get_active_witnesses = Array(
    AnyOf(
        AccountName(),
        EmptyString()
    ),
    minItems=1, maxItems=43
)

get_block = Map({
    'block_id': TransactionId(),
    'extensions': Array(ArrayStrict(Str(), Any())),
    'previous': TransactionId(),
    'signing_key': PublicKey(),
    'timestamp': Date(),
    'transaction_ids': Array(TransactionId(), unique_items=True),
    'transaction_merkle_root': TransactionId(),
    'transactions': Array(
        Map({
            'block_num': Int(),
            'expiration': Date(),
            'extensions': Array(Any()),
            'operations': Array(
                ArrayStrict(Str(), Any())
            ),
            'ref_block_num': Int(),
            'ref_block_prefix': Int(),
            'signatures': Array(Signature()),
            'transaction_id': TransactionId(),
            'transaction_num': Int(),
        })
    ),
    'witness': AccountName(),
    'witness_signature': Signature(),
})

get_block_header = Map({
    'previous': TransactionId(),
    'extensions': Array(
        ArrayStrict(Str(), Any()),
    ),
    'timestamp': Date(),
    'transaction_merkle_root': TransactionId(),
    'witness': AccountName(),
})

get_chain_properties = Map({
    'account_creation_fee': LegacyAssetHive(),
    'account_subsidy_budget': Int(),
    'account_subsidy_decay': Int(),
    'hbd_interest_rate': Int(),
    'maximum_block_size': Int(),
})

get_collateralized_conversion_requests = Array(
    Map({
        'collateral_amount': LegacyAssetHive(),
        'conversion_date': Date(),
        'converted_amount': LegacyAssetHbd(),
        'id': Int(),
        'owner': AccountName(),
        'requestid': Int(),
    })
)

get_config = Map({
    'HBD_SYMBOL': LegacyAssetHbd.Symbol(),
    'HIVE_100_PERCENT': Int(),
    'HIVE_1_BASIS_POINT': Int(),
    'HIVE_1_PERCENT': Int(),
    'HIVE_ACCOUNT_RECOVERY_REQUEST_EXPIRATION_PERIOD': Int(),
    'HIVE_ACCOUNT_SUBSIDY_PRECISION': Int(),
    'HIVE_ACTIVE_CHALLENGE_COOLDOWN': Int(),
    'HIVE_ACTIVE_CHALLENGE_FEE': LegacyAssetHive(),
    'HIVE_ADDRESS_PREFIX': Str(pattern=r'^(?:STM|TST)$'),
    'HIVE_APR_PERCENT_MULTIPLY_PER_BLOCK': Int(),
    'HIVE_APR_PERCENT_MULTIPLY_PER_HOUR': Int(),
    'HIVE_APR_PERCENT_MULTIPLY_PER_ROUND': Int(),
    'HIVE_APR_PERCENT_SHIFT_PER_BLOCK': Int(),
    'HIVE_APR_PERCENT_SHIFT_PER_HOUR': Int(),
    'HIVE_APR_PERCENT_SHIFT_PER_ROUND': Int(),
    'HIVE_BANDWIDTH_AVERAGE_WINDOW_SECONDS': Int(),
    'HIVE_BANDWIDTH_PRECISION': Int(),
    'HIVE_BENEFICIARY_LIMIT': Int(),
    'HIVE_BLOCKCHAIN_HARDFORK_VERSION': HardforkVersion(),
    'HIVE_BLOCKCHAIN_PRECISION': Int(),
    'HIVE_BLOCKCHAIN_PRECISION_DIGITS': Int(),
    'HIVE_BLOCKCHAIN_VERSION': HardforkVersion(),
    'HIVE_BLOCKS_PER_DAY': Int(),
    'HIVE_BLOCKS_PER_HOUR': Int(),
    'HIVE_BLOCKS_PER_YEAR': Int(),
    'HIVE_BLOCK_GENERATION_POSTPONED_TX_LIMIT': Int(),
    'HIVE_BLOCK_INTERVAL': Int(),
    'HIVE_CASHOUT_WINDOW_SECONDS': Int(),
    'HIVE_CASHOUT_WINDOW_SECONDS_PRE_HF12': Int(),
    'HIVE_CASHOUT_WINDOW_SECONDS_PRE_HF17': Int(),
    'HIVE_CHAIN_ID': Hex(),
    'HIVE_COLLATERALIZED_CONVERSION_DELAY': Int(),
    'HIVE_COLLATERALIZED_CONVERSION_FEE': Int(),
    'HIVE_COMMENT_REWARD_FUND_NAME': Str(),
    'HIVE_COMMENT_TITLE_LIMIT': Int(),
    'HIVE_CONTENT_APR_PERCENT': Int(),
    'HIVE_CONTENT_CONSTANT_HF0': Int(),
    'HIVE_CONTENT_CONSTANT_HF21': Int(),
    'HIVE_CONTENT_REWARD_PERCENT_HF16': Int(),
    'HIVE_CONTENT_REWARD_PERCENT_HF21': Int(),
    'HIVE_CONVERSION_COLLATERAL_RATIO': Int(),
    'HIVE_CONVERSION_DELAY': Int(),
    'HIVE_CONVERSION_DELAY_PRE_HF_16': Int(),
    'HIVE_CREATE_ACCOUNT_DELEGATION_RATIO': Int(),
    'HIVE_CREATE_ACCOUNT_DELEGATION_TIME': Int(),
    'HIVE_CREATE_ACCOUNT_WITH_HIVE_MODIFIER': Int(),
    'HIVE_CURATE_APR_PERCENT': Int(),
    'HIVE_CUSTOM_OP_DATA_MAX_LENGTH': Int(),
    'HIVE_CUSTOM_OP_ID_MAX_LENGTH': Int(),
    'HIVE_DAILY_PROPOSAL_MAINTENANCE_PERIOD': Int(),
    'HIVE_DECAY_BACKSTOP_PERCENT': Int(),
    'HIVE_DEFAULT_ACCOUNT_SUBSIDY_BUDGET': Int(),
    'HIVE_DEFAULT_ACCOUNT_SUBSIDY_DECAY': Int(),
    'HIVE_DEFAULT_HBD_INTEREST_RATE': Int(),
    'HIVE_DEFAULT_HF_9_COMPROMISED_ACCOUNTS_PUBLIC_KEY_STR': PublicKey(),
    'HIVE_DELAYED_VOTING_INTERVAL_SECONDS': Int(),
    'HIVE_DELAYED_VOTING_TOTAL_INTERVAL_SECONDS': Int(),
    'HIVE_DELEGATION_RETURN_PERIOD_HF0': Int(),
    'HIVE_DELEGATION_RETURN_PERIOD_HF20': Int(),
    'HIVE_DOWNVOTE_POOL_PERCENT_HF21': Int(),
    'HIVE_EARLY_VOTING_SECONDS_HF25': Int(),
    'HIVE_ENABLE_SMT': Bool(),
    'HIVE_EQUIHASH_K': Int(),
    'HIVE_EQUIHASH_N': Int(),
    'HIVE_FEED_HISTORY_WINDOW': Int(),
    'HIVE_FEED_HISTORY_WINDOW_PRE_HF_16': Int(),
    'HIVE_FEED_INTERVAL_BLOCKS': Int(),
    'HIVE_GENESIS_TIME': Date(),
    'HIVE_GLOBAL_REMOVE_THRESHOLD': Int(),
    'HIVE_GOVERNANCE_VOTE_EXPIRATION_PERIOD': Int(),
    'HIVE_HARDFORK_REQUIRED_WITNESSES': Int(),
    'HIVE_HBD_HARD_LIMIT': Int(),
    'HIVE_HBD_HARD_LIMIT_PRE_HF26': Int(),
    'HIVE_HBD_INIT_SUPPLY': Int(),
    'HIVE_HBD_INTEREST_COMPOUND_INTERVAL_SEC': Int(),
    'HIVE_HBD_START_PERCENT_HF14': Int(),
    'HIVE_HBD_START_PERCENT_HF20': Int(),
    'HIVE_HBD_START_PERCENT_HF26': Int(),
    'HIVE_HBD_STOP_PERCENT_HF14': Int(),
    'HIVE_HBD_STOP_PERCENT_HF20': Int(),
    'HIVE_HBD_STOP_PERCENT_HF26': Int(),
    'HIVE_HF21_CONVERGENT_LINEAR_RECENT_CLAIMS': Int(),
    'HIVE_HF_9_COMPROMISED_ACCOUNTS_PUBLIC_KEY_STR': PublicKey(),
    'HIVE_INFLATION_NARROWING_PERIOD': Int(),
    'HIVE_INFLATION_RATE_START_PERCENT': Int(),
    'HIVE_INFLATION_RATE_STOP_PERCENT': Int(),
    'HIVE_INITIAL_VOTE_POWER_RATE': Int(),
    'HIVE_INIT_MINER_NAME': AccountName(),
    'HIVE_INIT_PUBLIC_KEY': PublicKey(),
    'HIVE_INIT_PUBLIC_KEY_STR': PublicKey(),
    'HIVE_INIT_SUPPLY': Int(),
    'HIVE_INIT_TIME': Date(),
    'HIVE_IRREVERSIBLE_THRESHOLD': Int(),
    'HIVE_LIQUIDITY_APR_PERCENT': Int(),
    'HIVE_LIQUIDITY_REWARD_BLOCKS': Int(),
    'HIVE_LIQUIDITY_REWARD_PERIOD_SEC': Int(),
    'HIVE_LIQUIDITY_TIMEOUT_SEC': Int(),
    'HIVE_MAX_ACCOUNT_CREATION_FEE': Int(),
    'HIVE_MAX_ACCOUNT_NAME_LENGTH': Int(),
    'HIVE_MAX_ACCOUNT_WITNESS_VOTES': Int(),
    'HIVE_MAX_ASSET_WHITELIST_AUTHORITIES': Int(),
    'HIVE_MAX_AUTHORITY_MEMBERSHIP': Int(),
    'HIVE_MAX_BLOCK_SIZE': Int(),
    'HIVE_MAX_CASHOUT_WINDOW_SECONDS': Int(),
    'HIVE_MAX_COMMENT_DEPTH': Int(),
    'HIVE_MAX_COMMENT_DEPTH_PRE_HF17': Int(),
    'HIVE_MAX_CONSECUTIVE_RECURRENT_TRANSFER_FAILURES': Int(),
    'HIVE_MAX_FEED_AGE_SECONDS': Int(),
    'HIVE_MAX_INSTANCE_ID': Int(),
    'HIVE_MAX_LIMIT_ORDER_EXPIRATION': Int(),
    'HIVE_MAX_MEMO_SIZE': Int(),
    'HIVE_MAX_MINER_WITNESSES_HF0': Int(),
    'HIVE_MAX_MINER_WITNESSES_HF17': Int(),
    'HIVE_MAX_OPEN_RECURRENT_TRANSFERS': Int(),
    'HIVE_MAX_PENDING_TRANSFERS': Int(),
    'HIVE_MAX_PERMLINK_LENGTH': Int(),
    'HIVE_MAX_PROXY_RECURSION_DEPTH': Int(),
    'HIVE_MAX_RATION_DECAY_RATE': Int(),
    'HIVE_MAX_RECURRENT_TRANSFERS_PER_BLOCK': Int(),
    'HIVE_MAX_RECURRENT_TRANSFER_END_DATE': Int(),
    'HIVE_MAX_RESERVE_RATIO': Int(),
    'HIVE_MAX_RUNNER_WITNESSES_HF0': Int(),
    'HIVE_MAX_RUNNER_WITNESSES_HF17': Int(),
    'HIVE_MAX_SATOSHIS': Int(),
    'HIVE_MAX_SHARE_SUPPLY': Int(),
    'HIVE_MAX_SIG_CHECK_ACCOUNTS': Int(),
    'HIVE_MAX_SIG_CHECK_DEPTH': Int(),
    'HIVE_MAX_TIME_UNTIL_EXPIRATION': Int(),
    'HIVE_MAX_TRANSACTION_SIZE': Int(),
    'HIVE_MAX_UNDO_HISTORY': Int(),
    'HIVE_MAX_URL_LENGTH': Int(),
    'HIVE_MAX_VOTED_WITNESSES_HF0': Int(),
    'HIVE_MAX_VOTED_WITNESSES_HF17': Int(),
    'HIVE_MAX_VOTE_CHANGES': Int(),
    'HIVE_MAX_WITHDRAW_ROUTES': Int(),
    'HIVE_MAX_WITNESSES': Int(),
    'HIVE_MAX_WITNESS_URL_LENGTH': Int(),
    'HIVE_MID_VOTING_SECONDS_HF25': Int(),
    'HIVE_MINER_ACCOUNT': Str(),
    'HIVE_MINER_PAY_PERCENT': Int(),
    'HIVE_MINING_REWARD': LegacyAssetHive(),
    'HIVE_MINING_TIME': Date(),
    'HIVE_MIN_ACCOUNT_CREATION_FEE': Int(),
    'HIVE_MIN_ACCOUNT_NAME_LENGTH': Int(),
    'HIVE_MIN_BLOCK_SIZE': Int(),
    'HIVE_MIN_BLOCK_SIZE_LIMIT': Int(),
    'HIVE_MIN_COMMENT_EDIT_INTERVAL': Int(),
    'HIVE_MIN_CONTENT_REWARD': LegacyAssetHive(),
    'HIVE_MIN_CURATE_REWARD': LegacyAssetHive(),
    'HIVE_MIN_FEEDS': Int(),
    'HIVE_MIN_LIQUIDITY_REWARD': LegacyAssetHive(),
    'HIVE_MIN_LIQUIDITY_REWARD_PERIOD_SEC': Int(),
    'HIVE_MIN_PAYOUT_HBD': LegacyAssetHbd(),
    'HIVE_MIN_PERMLINK_LENGTH': Int(),
    'HIVE_MIN_POW_REWARD': LegacyAssetHive(),
    'HIVE_MIN_PRODUCER_REWARD': LegacyAssetHive(),
    'HIVE_MIN_RECURRENT_TRANSFERS_RECURRENCE': Int(),
    'HIVE_MIN_REPLY_INTERVAL': Int(),
    'HIVE_MIN_REPLY_INTERVAL_HF20': Int(),
    'HIVE_MIN_ROOT_COMMENT_INTERVAL': Int(),
    'HIVE_MIN_TRANSACTION_EXPIRATION_LIMIT': Int(),
    'HIVE_MIN_TRANSACTION_SIZE_LIMIT': Int(),
    'HIVE_MIN_UNDO_HISTORY': Int(),
    'HIVE_MIN_VOTE_INTERVAL_SEC': Int(),
    'HIVE_NULL_ACCOUNT': AccountName(),
    'HIVE_NUM_INIT_MINERS': Int(),
    'HIVE_ONE_DAY_SECONDS': Int(),
    'HIVE_OWNER_AUTH_HISTORY_TRACKING_START_BLOCK_NUM': Int(),
    'HIVE_OWNER_AUTH_RECOVERY_PERIOD': Int(),
    'HIVE_OWNER_CHALLENGE_COOLDOWN': Int(),
    'HIVE_OWNER_CHALLENGE_FEE': LegacyAssetHive(),
    'HIVE_OWNER_UPDATE_LIMIT': Int(),
    'HIVE_PENDING_TRANSACTION_EXECUTION_LIMIT': Int(),
    'HIVE_POST_AVERAGE_WINDOW': Int(),
    'HIVE_POST_REWARD_FUND_NAME': Str(),
    'HIVE_POST_WEIGHT_CONSTANT': Int(),
    'HIVE_POW_APR_PERCENT': Int(),
    'HIVE_PRODUCER_APR_PERCENT': Int(),
    'HIVE_PROPOSAL_CONVERSION_RATE': Int(),
    'HIVE_PROPOSAL_FEE_INCREASE_AMOUNT': Int(),
    'HIVE_PROPOSAL_FEE_INCREASE_DAYS': Int(),
    'HIVE_PROPOSAL_FEE_INCREASE_DAYS_SEC': Int(),
    'HIVE_PROPOSAL_FUND_PERCENT_HF0': Int(),
    'HIVE_PROPOSAL_FUND_PERCENT_HF21': Int(),
    'HIVE_PROPOSAL_MAINTENANCE_CLEANUP': Int(),
    'HIVE_PROPOSAL_MAINTENANCE_PERIOD': Int(),
    'HIVE_PROPOSAL_MAX_IDS_NUMBER': Int(),
    'HIVE_PROPOSAL_SUBJECT_MAX_LENGTH': Int(),
    'HIVE_PROXY_TO_SELF_ACCOUNT': Str(),
    'HIVE_RD_DECAY_DENOM_SHIFT': Int(),
    'HIVE_RD_MAX_BUDGET': Int(),
    'HIVE_RD_MAX_BUDGET_1': Int(),
    'HIVE_RD_MAX_BUDGET_2': Int(),
    'HIVE_RD_MAX_BUDGET_3': Int(),
    'HIVE_RD_MAX_DECAY': Int(),
    'HIVE_RD_MAX_DECAY_BITS': Int(),
    'HIVE_RD_MAX_POOL_BITS': Int(),
    'HIVE_RD_MIN_BUDGET': Int(),
    'HIVE_RD_MIN_DECAY': Int(),
    'HIVE_RD_MIN_DECAY_BITS': Int(),
    'HIVE_RECENT_RSHARES_DECAY_TIME_HF17': Int(),
    'HIVE_RECENT_RSHARES_DECAY_TIME_HF19': Int(),
    'HIVE_REDUCED_VOTE_POWER_RATE': Int(),
    'HIVE_REVERSE_AUCTION_WINDOW_SECONDS_HF20': Int(),
    'HIVE_REVERSE_AUCTION_WINDOW_SECONDS_HF21': Int(),
    'HIVE_REVERSE_AUCTION_WINDOW_SECONDS_HF25': Int(),
    'HIVE_REVERSE_AUCTION_WINDOW_SECONDS_HF6': Int(),
    'HIVE_ROOT_POST_PARENT': Str(),
    'HIVE_SAVINGS_WITHDRAW_REQUEST_LIMIT': Int(),
    'HIVE_SAVINGS_WITHDRAW_TIME': Int(),
    'HIVE_SECONDS_PER_YEAR': Int(),
    'HIVE_SECOND_CASHOUT_WINDOW': Int(),
    'HIVE_SOFT_MAX_COMMENT_DEPTH': Int(),
    'HIVE_START_MINER_VOTING_BLOCK': Int(),
    'HIVE_START_VESTING_BLOCK': Int(),
    'HIVE_SYMBOL': LegacyAssetHive.Symbol(),
    'HIVE_TEMP_ACCOUNT': Str(),
    'HIVE_TREASURY_ACCOUNT': AccountName(),
    'HIVE_TREASURY_FEE': Int(),
    'HIVE_UP_TO_DATE_MARGIN__BLOCK_STATS': Int(),
    'HIVE_UP_TO_DATE_MARGIN__FAST_CONFIRM': Int(),
    'HIVE_UP_TO_DATE_MARGIN__PENDING_TXS': Int(),
    'HIVE_UPVOTE_LOCKOUT_HF17': Int(),
    'HIVE_UPVOTE_LOCKOUT_HF7': Int(),
    'HIVE_UPVOTE_LOCKOUT_SECONDS': Int(),
    'HIVE_VESTING_FUND_PERCENT_HF16': Int(),
    'HIVE_VESTING_WITHDRAW_INTERVALS': Int(),
    'HIVE_VESTING_WITHDRAW_INTERVALS_PRE_HF_16': Int(),
    'HIVE_VESTING_WITHDRAW_INTERVAL_SECONDS': Int(),
    'HIVE_VIRTUAL_SCHEDULE_LAP_LENGTH': Int(),
    'HIVE_VIRTUAL_SCHEDULE_LAP_LENGTH2': Int(),
    'HIVE_VOTE_DUST_THRESHOLD': Int(),
    'HIVE_VOTING_MANA_REGENERATION_SECONDS': Int(),
    'HIVE_WITNESS_SUBSIDY_BUDGET_PERCENT': Int(),
    'HIVE_WITNESS_SUBSIDY_DECAY_PERCENT': Int(),
    'IS_TEST_NET': Bool(),
    'NEW_HIVE_TREASURY_ACCOUNT': AccountName(),
    'OBSOLETE_TREASURY_ACCOUNT': AccountName(),
    'OLD_CHAIN_ID': Hex(),
    'VESTS_SYMBOL': LegacyAssetVests.Symbol(),
})

get_conversion_requests = Array(
    Map({
        'amount': LegacyAssetHbd(),
        'conversion_date': Date(),
        'id': Int(),
        'owner': AccountName(),
        'requestid': Int(),
    })
)

get_current_median_history_price = Price(legacy_format=True)

get_dynamic_global_properties = Map({
    'available_account_subsidies': Int(),
    'content_reward_percent': Int(),
    'current_aslot': Int(),
    'current_hbd_supply': LegacyAssetHbd(),
    'current_remove_threshold': Int(),
    'current_supply': LegacyAssetHive(),
    'current_witness': AccountName(),
    'delegation_return_period': Int(),
    'dhf_interval_ledger': LegacyAssetHbd(),
    'downvote_pool_percent': Int(),
    'early_voting_seconds': Int(),
    'hbd_interest_rate': Int(),
    'hbd_print_rate': Int(),
    'hbd_start_percent': Int(),
    'hbd_stop_percent': Int(),
    'head_block_id': TransactionId(),
    'head_block_number': Int(),
    'init_hbd_supply': LegacyAssetHbd(),
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
    'pending_rewarded_vesting_hive': LegacyAssetHive(),
    'pending_rewarded_vesting_shares': LegacyAssetVests(),
    'proposal_fund_percent': Int(),
    'recent_slots_filled': Int(),
    'required_actions_partition_percent': Int(),
    'reverse_auction_seconds': Int(),
    'time': Date(),
    'total_pow': Int(),
    'total_reward_fund_hive': LegacyAssetHive(),
    'total_reward_shares2': Int(),
    'total_vesting_fund_hive': LegacyAssetHive(),
    'total_vesting_shares': LegacyAssetVests(),
    'vesting_reward_percent': Int(),
    'virtual_supply': LegacyAssetHive(),
    'vote_power_reserve_rate': Int(),
})

get_escrow = OneOf(
    Null(),
    Map({
        'agent': AccountName(),
        'agent_approved': Bool(),
        'disputed': Bool(),
        'escrow_expiration': Date(),
        'escrow_id': Int(),
        'from': AccountName(),
        'hbd_balance': LegacyAssetHbd(),
        'hive_balance': LegacyAssetHive(),
        'id': Int(),
        'pending_fee': OneOf(
            LegacyAssetHive(),
            LegacyAssetHbd(),
        ),
        'ratification_deadline': Date(),
        'to': AccountName(),
        'to_approved': Bool(),
    }),
)

get_expiring_vesting_delegations = Array(
    Map({
        'delegator': AccountName(),
        'expiration': Date(),
        'id': Int(),
        'vesting_shares': LegacyAssetVests(),
    })
)

get_feed_history = Map({
    'current_max_history': Price(legacy_format=True),
    'current_median_history': Price(legacy_format=True),
    'current_min_history': Price(legacy_format=True),
    'id': Int(),
    'market_median_history': Price(legacy_format=True),
    'price_history': Array(Price(legacy_format=True)),
})

get_hardfork_version = HardforkVersion()

get_key_references = Array(Array(AccountName()))

get_market_history = Array(
    Map({
        'id': Int(),
        'open': Date(),
        'seconds': Int(),
        'hive': Map({
            'high': Int(),
            'low': Int(),
            'open': Int(),
            'close': Int(),
            'volume': Int(),
        }),
        'non_hive': Map({
            'high': Int(),
            'low': Int(),
            'open': Int(),
            'close': Int(),
            'volume': Int(),
        }),
    })
)

get_market_history_buckets = Array(Int(), enum=[[15, 60, 300, 3600, 86400]])

get_next_scheduled_hardfork = Map({
    'hf_version': HardforkVersion(),
    'live_time': Date(),
})

get_open_orders = Array(
    Map({
        'created': Date(),
        'expiration': Date(),
        'for_sale': Int(),
        'id': Int(),
        'orderid': Int(),
        'real_price': FloatAsString(),
        'rewarded': Bool(),
        'sell_price': Price(legacy_format=True),
        'seller': AccountName(),
    })
)

get_ops_in_block = Array(
    Map({
        'block': Int(),
        'op': ArrayStrict(Str(), Any()),
        'op_in_trx': Int(),
        'timestamp': Date(),
        'trx_id': TransactionId(),
        'trx_in_block': Int(),
        'virtual_op': Bool(),
    })
)

get_order_book = Map({
    'asks': Array(Map({
        'created': Date(),
        'hbd': Int(),
        'hive': Int(),
        'order_price': Price(legacy_format=True),
        'real_price': FloatAsString(),
        })
    ),
    'bids': Array(Map({
        'created': Date(),
        'hbd': Int(),
        'hive': Int(),
        'order_price': Price(legacy_format=True),
        'real_price': FloatAsString(),
        })
    ),
})

get_owner_history = Array(
    Map({
        'account': AccountName(),
        'id': Int(),
        'last_valid_time': Date(),
        'previous_owner_authority': Authority(),
    })
)

get_potential_signatures = Array(PublicKey())

get_recent_trades = Array(
    Map({
        'date': Date(),
        'current_pays': AnyOf(LegacyAssetHive(), LegacyAssetHbd()),
        'open_pays': AnyOf(LegacyAssetHive(), LegacyAssetHbd()),
    })
)

get_recovery_request = Map({
    'id': Int(),
    'account_to_recover': AccountName(),
    'new_owner_authority': Authority(),
    'expires': Date(),
})

get_required_signatures = Array(PublicKey())

get_reward_fund = Map({
    'id': Int(),
    'name': AccountName(),
    'reward_balance': LegacyAssetHive(),
    'recent_claims': Int(),
    'last_update': Date(),
    'content_constant': Int(),
    'percent_curation_rewards': Int(),
    'percent_content_rewards': Int(),
    'author_reward_curve': Str(),
    'curation_reward_curve': Str(),
})

get_savings_withdraw_from = Array(
    Map({
        'id': Int(),
        'from': AccountName(),
        'to': AccountName(),
        'memo': Str(),
        'request_id': Int(),
        'amount': LegacyAssetHive(),
        'complete': Date(),
    })
)

get_savings_withdraw_to = Array(
    Map({
        'id': Int(),
        'from': AccountName(),
        'to': AccountName(),
        'memo': Str(),
        'request_id': Int(),
        'amount': LegacyAssetHive(),
        'complete': Date(),
    })
)

get_ticker = Map({
    'latest': Str(),
    'lowest_ask': Str(),
    'highest_bid': Str(),
    'percent_change': Str(),
    'hive_volume': LegacyAssetHive(),
    'hbd_volume': LegacyAssetHbd(),
})

get_trade_history = Array(
    Map({
        'date': Date(),
        'current_pays': AnyOf(LegacyAssetHive(), LegacyAssetHbd()),
        'open_pays': AnyOf(LegacyAssetHive(), LegacyAssetHbd()),
    })
)

get_transaction = Map({
    'ref_block_num': Int(),
    'ref_block_prefix': Int(),
    'expiration': Date(),
    'operations': Array(
        ArrayStrict(Str(), Any())
    ),
    'extensions': Array(Any()),
    'signatures': Array(Signature()),
    'transaction_id': TransactionId(),
    'block_num': Int(),
    'transaction_num': Int(),
})

get_transaction_hex = Hex()

get_version = HiveVersion()

get_vesting_delegations = Array(
    Map({
        'id': Int(),
        'delegator': AccountName(),
        'delegatee': AccountName(),
        'vesting_shares': LegacyAssetVests(),
        'min_delegation_time': Date(),
    })
)

get_volume = Map({
    'hive_volume': LegacyAssetHive(),
    'hbd_volume': LegacyAssetHbd(),
})

get_withdraw_routes = Array(
    Map({
        'id': Int(),
        'from_account': AccountName(),
        'to_account': AccountName(),
        'percent': Int(),
        'auto_vest': Bool(),
    })
)

get_witness_by_account = Map({
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
        'account_creation_fee': LegacyAssetHive(),
        'maximum_block_size': Int(),
        'hbd_interest_rate': Int(),
        'account_subsidy_budget': Int(),
        'account_subsidy_decay': Int(),
    }),
    'hbd_exchange_rate': HbdExchangeRate(legacy_format=True),
    'last_hbd_exchange_update': Date(),
    'last_work': Sha256(),
    'running_version': HardforkVersion(),
    'hardfork_version_vote': HardforkVersion(),
    'hardfork_time_vote': Date(),
    'available_witness_account_subsidies': Int(),
})

get_witness_count = Int()

get_witness_schedule = Map({
    'id': Int(),
    'current_virtual_time': Int(),
    'next_shuffle_block_num': Int(),
    'current_shuffled_witnesses': Array(
        AnyOf(
            AccountName(),
            EmptyString()
        )
    ),
    'future_shuffled_witnesses': Array(
        AnyOf(
            AccountName(),
            EmptyString()
        )
    ),
    'num_scheduled_witnesses': Int(),
    'elected_weight': Int(),
    'timeshare_weight': Int(),
    'miner_weight': Int(),
    'witness_pay_normalization_factor': Int(),
    'median_props': Map({
        'account_creation_fee': LegacyAssetHive(),
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
    'min_witness_account_subsidy_decay': Int(),
    'future_changes': Map({
        'num_scheduled_witnesses': Int(),
        'elected_weight': Int(),
        'timeshare_weight': Int(),
        'miner_weight': Int(),
        'witness_pay_normalization_factor': Int(),
        'median_props': Map({
            'account_creation_fee': LegacyAssetHive(),
            'maximum_block_size': Int(),
            'hbd_interest_rate': Int(),
            'account_subsidy_budget': Int(),
            'account_subsidy_decay': Int()
        },
        required_keys=[
        ]),
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
            'min_decay': Int()
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
            'min_decay': Int()
        }),
        'min_witness_account_subsidy_decay': Int()
    },
    required_keys=[
    ])
},
required_keys=[
    'id', 'current_virtual_time', 'next_shuffle_block_num', 'current_shuffled_witnesses',
    'num_scheduled_witnesses', 'elected_weight', 'timeshare_weight', 'miner_weight',
    'witness_pay_normalization_factor', 'median_props', 'majority_version', 'max_voted_witnesses',
    'max_miner_witnesses', 'max_runner_witnesses', 'hardfork_required_witnesses',
    'account_subsidy_rd', 'account_subsidy_witness_rd', 'min_witness_account_subsidy_decay'
])

get_witnesses = Array(
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
            'account_creation_fee': LegacyAssetHive(),
            'maximum_block_size': Int(),
            'hbd_interest_rate': Int(),
            'account_subsidy_budget': Int(),
            'account_subsidy_decay': Int(),
        }),
        'hbd_exchange_rate': HbdExchangeRate(legacy_format=True),
        'last_hbd_exchange_update': Date(),
        'last_work': Sha256(),
        'running_version': HardforkVersion(),
        'hardfork_version_vote': HardforkVersion(),
        'hardfork_time_vote': Date(),
        'available_witness_account_subsidies': Int(),
    })
)

get_witnesses_by_vote = Array(
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
                'account_creation_fee': LegacyAssetHive(),
                'maximum_block_size': Int(),
                'hbd_interest_rate': Int(),
                'account_subsidy_budget': Int(),
                'account_subsidy_decay': Int(),
            }),
        'hbd_exchange_rate': HbdExchangeRate(legacy_format=True),
        'last_hbd_exchange_update': Date(),
        'last_work': Sha256(),
        'running_version': HardforkVersion(),
        'hardfork_version_vote': HardforkVersion(),
        'hardfork_time_vote': Date(),
        'available_witness_account_subsidies': Int(),
    })
)

is_known_transaction = Bool()

list_proposal_votes = Array(
    Map({
        'id': Int(),
        'voter': AccountName(),
        'proposal': Map({
            'id': Int(),
            'proposal_id': Int(),
            'creator': Str(),
            'receiver': Str(),
            'start_date': Date(),
            'end_date': Date(),
            'daily_pay': LegacyAssetHbd(),
            'subject': Str(),
            'permlink': Str(),
            'total_votes': Int(),
            'status': Str(),
        }),
    })
)

list_proposals = Array(
    Map({
        'id': Int(),
        'proposal_id': Int(),
        'creator': AccountName(),
        'receiver': AccountName(),
        'start_date': Date(),
        'end_date': Date(),
        'daily_pay': LegacyAssetHbd(),
        'subject': Str(),
        'permlink': Str(),
        'total_votes': Int(),
    })
)

list_rc_accounts = Array(RcAccountObject())

list_rc_direct_delegations = Array(
    Map({
        'from': AccountName(),
        'to': AccountName(),
        'delegated_rc': Int(),
    })
)

lookup_account_names = Array(
    Map({
        'id': Int(),
        'name': AccountName(),
        'owner': Authority(),
        'active': Authority(),
        'posting': Authority(),
        'memo_key': PublicKey(),
        'json_metadata': AnyOf(Json(), EmptyString()),
        'posting_json_metadata': AnyOf(Json(), EmptyString()),
        'proxy': AnyOf(AccountName(), EmptyString()),
        'previous_owner_update': Date(),
        'last_owner_update': Date(),
        'last_account_update': Date(),
        'created': Date(),
        'mined': Bool(),
        'recovery_account': AnyOf(AccountName(), EmptyString()),
        'last_account_recovery': Date(),
        'reset_account': AccountName(),
        'comment_count': Int(),
        'lifetime_vote_count': Int(),
        'post_count': Int(),
        'can_vote': Bool(),
        'voting_manabar': Manabar(),
        'downvote_manabar': Manabar(),
        'voting_power': Int(),
        'balance': LegacyAssetHive(),
        'savings_balance': LegacyAssetHive(),
        'hbd_balance': LegacyAssetHbd(),
        'hbd_seconds': Int(),
        'hbd_seconds_last_update': Date(),
        'hbd_last_interest_payment': Date(),
        'savings_hbd_balance': LegacyAssetHbd(),
        'savings_hbd_seconds': Int(),
        'savings_hbd_seconds_last_update': Date(),
        'savings_hbd_last_interest_payment': Date(),
        'savings_withdraw_requests': Int(),
        'reward_hbd_balance': LegacyAssetHbd(),
        'reward_hive_balance': LegacyAssetHive(),
        'reward_vesting_balance': LegacyAssetVests(),
        'reward_vesting_hive': LegacyAssetHive(),
        'vesting_shares': LegacyAssetVests(),
        'delegated_vesting_shares': LegacyAssetVests(),
        'received_vesting_shares': LegacyAssetVests(),
        'vesting_withdraw_rate': LegacyAssetVests(),
        'post_voting_power': LegacyAssetVests(),
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
        'last_vote_time': Date(),
        'post_bandwidth': Int(),
        'pending_claimed_accounts': Int(),
        'open_recurrent_transfers': Int(),
        'delayed_votes': Array(
            Map({
                'time': Date(),
                'val': Int(),
            })),
        'governance_vote_expiration_ts': Date()
    })
)

lookup_accounts = Array(AccountName())

lookup_witness_accounts = Array(AccountName())

verify_authority = Bool()
