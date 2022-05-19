from schemas.predefined import *

# FIXME, Workaround: Method necessary to prepare the test environment for 'wallet bridge API' tests, used by TestTools.
#  Add a schema when developing the tests database API.
get_dynamic_global_properties = Any()


find_account_recovery_requests = Map({
    'requests': Array(
        Map({
            'id': Int(),
            'account_to_recover': Str(),
            'new_owner_authority': Authority(),
            'expires': Date(),
        })
    )
})

find_accounts = Map({

})

find_change_recovery_account_requests = Map({
    'requests': Array(
        Map({
            'id': Int(),
            'account_to_recover': Str(),
            'recovery_account': Str(),
            'effective_on': Date(),
        })
    )
})

find_collateralized_conversion_requests = Map({
    'requests': Array(
        Map({
            'id': Int(),
            'owner': Str(),
            'requestid': Int(),
            'collateral_amount': AssetHive(),
            'converted_amount': AssetHbd(),
            'conversion_date': Date(),
        })
    )
})

find_comments = Map({
    'comments': Array(
        Map({
            'id': Int(),
            'author': Str(),
            'permlink': Str(),
            'category': Str(),
            'parent_author': Str(),
            'parent_permlink': Str(),
            'title': Str(),
            'body': Str(),
            'json_metadata': Str(),
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
            'root_author': Str(),
            'root_permlink': Str(),
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
            'account': Str(),
            'effective_date': Date(),
        })
    )
})

find_escrows = Map({
    'escrows': Array(
        Map({
            'id': Int(),
            'escrow_id': Int(),
            'from': Str(),
            'to': Str(),
            'agent': Str(),
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

find_limit_orders = Map({
    'orders': Array(
        Map({
            'id': Int(),
            'created': Date(),
            'expiration': Date(),
            'seller': Str(),
            'orderid': Int(),
            'for_sale': Int(),
            'sell_price': Price(AssetHive(), AssetHbd())
        })
    )
})
find_hbd_conversion_requests = Map ({
    'requests': Array(
        Map({
            'id': Int(),
            'owner': Str(),
            'requestid': Int(),
            'amount': AssetHbd(),
            'conversion_date': Date(),
        })
    )
})

find_owner_histories = Map({
    'owner_auths': Array(
        Map({
            'id': Int(),
            'account': Str(),
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
            'from': Str(),
            'to': Str(),
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
            'from': Str(),
            'to': Str(),
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
            'delegator': Str(),
            'vesting_shares': AssetVests(),
            'expiration': Date(),
        })
    )
})

find_vesting_delegations = Map({
    'delegations': Array(
        Map({
            'id': Int(),
            'delegator': Str(),
            'delegatee': Str(),
            'vesting_shares': AssetVests(),
            'min_delegation_time': Date(),
        })
    )
})

find_withdraw_vesting_routes = Map({
    'routes': Array(
        Map({
            'id': Int(),
            'from_account': Str(),
            'to_account': Str(),
            'percent': Int(),
            'auto_vest': Bool(),
        })
    )
})

find_witnesses = Map({
    'witnesses': Array(
        Map({
            'id': Int(),
            'owner': Str(),
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

get_comment_pending_payouts = Map({
    'cashout_infos': Array(
        Map({
            'author': Str(),
            'permlink': Str(),
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

get_transaction_hex = Map({
    'hex': Str()
})

is_known_transaction = Map({
    'is_known': Bool()
})

list_account_recovery_requests = Map({
    'requests': Array(
        Map({
            'id': Int(),
            'account_to_recover': Str(),
            'new_owner_authority': Authority(),
            'expires': Date(),
        })
    )
})

list_accounts = Map({
    'accounts': Array(
        Map({
            'id': Int(), 'name': Str(),
            'owner': Authority(),
            'active': Authority(),
            'posting': Authority(),
            'memo_key': PublicKey(),
            'json_metadata': Str(),
            'posting_json_metadata': Str(),
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
            'account_to_recover': Str(),
            'recovery_account': Str(),
            'effective_on': Date()
        })
    )
})

list_collateralized_conversion_requests = Map({
    'requests': Array(
        Map({
            'id': Int(),
            'owner': Str(),
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
            'account': Str(),
            'effective_date': Date(),
        })
    )
})

list_escrows = Map({
    'escrows': Array(
        Map({
            'id': Int(),
            'escrow_id': Int(),
            'from': Str(),
            'to': Str(),
            'agent': Str(),
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
            'owner': Str(),
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
            'seller': Str(),
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
            'account': Str(),
            'previous_owner_authority': Authority(),
            'last_valid_time': Date(),
        })
    )
})

list_savings_withdrawals = Map({
    'withdrawals': Array(
        Map({
            'id': Int(),
            'from': Str(),
            'to': Str(),
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
            'delegator': Str(),
            'vesting_shares': AssetVests(),
            'expiration': Date(),
        })
    )
})

list_vesting_delegations = Map({
    'delegations': Array(
        Map({
            'id': Int(),
            'delegator': Str(),
            'delegatee': Str(),
            'vesting_shares': AssetVests(),
            'min_delegation_time': Date(),
        })
    )
})

list_withdraw_vesting_routes = Map({
    'routes': Array(
        Map({
            'id': Int(),
            'from_account': Str(),
            'to_account': Str(),
            'percent': Int(),
            'auto_vest': Bool(),
        })
    )
})

list_witness_votes = Map({
    'votes': Array(
        Map({
            'id': Int(),
            'witness': Str(),
            'account': Str(),
        })
    )
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

list_proposal_votes = Map({
    'proposal_votes': Array(
        Map({
            'id': Int(),
            'voter': Str(),
            'proposal': Proposal(),
        })
    )
})

verify_signatures = Map({
    'valid': Bool()
})

list_proposals = Map({
    'proposals': Array(Proposal())
})




