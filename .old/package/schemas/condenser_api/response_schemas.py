from copy import deepcopy

from schemas.predefined import *

from ..wallet_bridge_api import response_schemas as wallet_bridge_schemas
from ..database_api import response_schemas as database_schemas
from ..account_history_api import response_schemas as account_history_schemas
from ..market_history_api import response_schemas as market_history_schemas
from ..rc_api import response_schemas as rc_schemas

from schemas.__private.modify.schema_asset_converter import convert_assets_to_legacy_format
from schemas.__private.modify.schema_expander import add_schema_to_map
from schemas.__private.modify.schema_reducer import remove_schema_from_map

broadcast_transaction = wallet_bridge_schemas.broadcast_transaction


broadcast_transaction_synchronous = wallet_bridge_schemas.broadcast_transaction_synchronous


find_proposals = deepcopy(database_schemas.find_proposals['proposals'])
remove_schema_from_map(find_proposals, path='0.status')
find_proposals = convert_assets_to_legacy_format(find_proposals)


find_recurrent_transfers = convert_assets_to_legacy_format(database_schemas.find_recurrent_transfers['recurrent_transfers'])


find_rc_accounts = convert_assets_to_legacy_format(rc_schemas.find_rc_accounts["rc_accounts"])


get_account_count = Int()


get_account_history = deepcopy(account_history_schemas.get_account_history['history'])
remove_schema_from_map(get_account_history, path='0.1.operation_id')


get_account_reputations = Array(
    Map({
        'account': AccountName(),
        'reputation': Int(),
    })
)


get_accounts = deepcopy(database_schemas.find_accounts['accounts'])
remove_schema_from_map(get_accounts, path='0.last_post_edit')
remove_schema_from_map(get_accounts, path='0.is_smt')
add_schema_to_map(get_accounts, path='0', key='post_history', schema=EmptyArray())
add_schema_to_map(get_accounts, path='0', key='vote_history', schema=EmptyArray())
add_schema_to_map(get_accounts, path='0', key='witness_votes', schema=Array(AccountName()))
add_schema_to_map(get_accounts, path='0', key='vesting_balance', schema=LegacyAssetHive())
add_schema_to_map(get_accounts, path='0', key='transfer_history', schema=EmptyArray())
add_schema_to_map(get_accounts, path='0', key='voting_power', schema=Int())
add_schema_to_map(get_accounts, path='0', key='market_history', schema=EmptyArray())
add_schema_to_map(get_accounts, path='0', key='tags_usage', schema=EmptyArray())
add_schema_to_map(get_accounts, path='0', key='reputation', schema=Int())
add_schema_to_map(get_accounts, path='0', key='guest_bloggers', schema=EmptyArray())
add_schema_to_map(get_accounts, path='0', key='other_history', schema=EmptyArray())
get_accounts = convert_assets_to_legacy_format(get_accounts)


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

get_active_witnesses = database_schemas.get_active_witnesses['witnesses']

get_block = deepcopy(wallet_bridge_schemas.get_block[1]['block'])
remove_schema_from_map(get_block, path='extensions')
add_schema_to_map(get_block, key='extensions', schema=Array(ArrayStrict(Str(), Any())))


get_block_header = Map({
    'previous': TransactionId(),
    'extensions': Array(
        ArrayStrict(Str(), Any()),
    ),
    'timestamp': Date(),
    'transaction_merkle_root': TransactionId(),
    'witness': AccountName(),
})

get_chain_properties = convert_assets_to_legacy_format(wallet_bridge_schemas.get_chain_properties)

get_collateralized_conversion_requests = convert_assets_to_legacy_format(wallet_bridge_schemas.get_collateralized_conversion_requests)

get_config = deepcopy(database_schemas.get_config)
remove_schema_from_map(get_config, path='HBD_SYMBOL')
remove_schema_from_map(get_config, path='HIVE_SYMBOL')
remove_schema_from_map(get_config, path='VESTS_SYMBOL')
add_schema_to_map(get_config, key='HBD_SYMBOL', schema=LegacyAssetHbd.Symbol())
add_schema_to_map(get_config, key='HIVE_SYMBOL', schema=LegacyAssetHive.Symbol())
add_schema_to_map(get_config, key='NEW_HIVE_TREASURY_ACCOUNT', schema=AccountName())
add_schema_to_map(get_config, key='VESTS_SYMBOL', schema=LegacyAssetVests.Symbol())
get_config = convert_assets_to_legacy_format(get_config)

get_conversion_requests = convert_assets_to_legacy_format(wallet_bridge_schemas.get_conversion_requests)


get_current_median_history_price = convert_assets_to_legacy_format(wallet_bridge_schemas.get_current_median_history_price)


get_dynamic_global_properties = deepcopy(database_schemas.get_dynamic_global_properties)
remove_schema_from_map(get_dynamic_global_properties, path='id')
get_dynamic_global_properties = convert_assets_to_legacy_format(get_dynamic_global_properties)


get_escrow = deepcopy(database_schemas.find_escrows['escrows'][0])
add_schema_to_map(get_escrow, key='pending_fee', schema=OneOf(LegacyAssetHive(), LegacyAssetHbd()))
get_escrow = convert_assets_to_legacy_format(get_escrow)
get_escrow = OneOf(Null(), get_escrow)


get_expiring_vesting_delegations = Array(
    Map({
        'delegator': AccountName(),
        'expiration': Date(),
        'id': Int(),
        'vesting_shares': LegacyAssetVests(),
    })
)

get_feed_history = convert_assets_to_legacy_format(wallet_bridge_schemas.get_feed_history)


get_hardfork_version = wallet_bridge_schemas.get_hardfork_version


get_key_references = Array(Array(AccountName()))


get_market_history = market_history_schemas.get_market_history['buckets']


get_market_history_buckets = market_history_schemas.get_market_history_buckets['bucket_sizes']


get_next_scheduled_hardfork = Map({
    'hf_version': HardforkVersion(),
    'live_time': Date(),
})


get_open_orders = deepcopy(wallet_bridge_schemas.get_open_orders)
add_schema_to_map(get_open_orders, path='0', key='real_price', schema=FloatAsString())
add_schema_to_map(get_open_orders, path='0', key='rewarded', schema=Bool())
get_open_orders = convert_assets_to_legacy_format(get_open_orders)


get_ops_in_block = deepcopy(wallet_bridge_schemas.get_ops_in_block['ops'])
remove_schema_from_map(get_ops_in_block, path='0.operation_id')
get_ops_in_block = get_ops_in_block


get_order_book = convert_assets_to_legacy_format(market_history_schemas.get_order_book)


get_owner_history = wallet_bridge_schemas.get_owner_history['owner_auths']


get_potential_signatures = database_schemas.get_potential_signatures['keys']


get_recent_trades = convert_assets_to_legacy_format(market_history_schemas.get_recent_trades['trades'])


get_recovery_request = database_schemas.find_account_recovery_requests['requests'][0]


get_required_signatures = database_schemas.get_required_signatures['keys']

get_reward_fund = convert_assets_to_legacy_format(wallet_bridge_schemas.get_reward_fund)


get_savings_withdraw_from = convert_assets_to_legacy_format(database_schemas.list_savings_withdrawals['withdrawals'])


get_savings_withdraw_to = get_savings_withdraw_from

get_ticker = convert_assets_to_legacy_format(market_history_schemas.get_ticker)


get_trade_history = convert_assets_to_legacy_format(market_history_schemas.get_trade_history['trades'])


get_transaction = deepcopy(account_history_schemas.get_transaction)
remove_schema_from_map(get_transaction, path='operations')
add_schema_to_map(get_transaction, key='operations', schema=Array(ArrayStrict(Str(),
                                                                              Map({}, allow_additional_properties=True))))


get_transaction_hex = database_schemas.get_transaction_hex['hex']


get_version = database_schemas.get_version


get_vesting_delegations = convert_assets_to_legacy_format(database_schemas.list_vesting_delegations['delegations'])


get_volume = convert_assets_to_legacy_format(market_history_schemas.get_volume)


get_withdraw_routes = wallet_bridge_schemas.get_withdraw_routes


get_witness_by_account = convert_assets_to_legacy_format(database_schemas.list_witnesses['witnesses'][0])


get_witness_count = Int()


get_witness_schedule = convert_assets_to_legacy_format(database_schemas.get_witness_schedule)


get_witnesses = convert_assets_to_legacy_format(database_schemas.list_witnesses['witnesses'])


list_rc_accounts = convert_assets_to_legacy_format(rc_schemas.list_rc_accounts["rc_accounts"])


list_rc_direct_delegations = rc_schemas.list_rc_direct_delegations["rc_direct_delegations"]


get_witnesses_by_vote = convert_assets_to_legacy_format(database_schemas.list_witnesses['witnesses'])


is_known_transaction = database_schemas.is_known_transaction['is_known']


list_proposal_votes = convert_assets_to_legacy_format(database_schemas.list_proposal_votes['proposal_votes'])


list_proposals = deepcopy(database_schemas.list_proposals['proposals'])
remove_schema_from_map(list_proposals, path='0.status')
list_proposals = convert_assets_to_legacy_format(list_proposals)


lookup_account_names = deepcopy(database_schemas.find_accounts['accounts'])
remove_schema_from_map(lookup_account_names, path='0.last_post_edit')
remove_schema_from_map(lookup_account_names, path='0.is_smt')
add_schema_to_map(lookup_account_names, path='0', key='voting_power', schema=Int())
lookup_account_names = convert_assets_to_legacy_format(lookup_account_names)


lookup_accounts = wallet_bridge_schemas.list_accounts


lookup_witness_accounts = Array(AccountName())


verify_authority = database_schemas.verify_authority['valid']

