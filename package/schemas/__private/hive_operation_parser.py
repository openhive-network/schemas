from __future__ import annotations

from pathlib import Path
from threading import Lock
from typing import TYPE_CHECKING
from warnings import warn

import CppHeaderParser

from schemas.__private.fundamental_schemas import AnyOf, Array, ArrayStrict, Bool, Date, Int, Null, Map, Str, OneOf

from schemas.__private.custom_schemas.account_name import AccountName
from schemas.__private.custom_schemas.asset_any import AssetAny
from schemas.__private.custom_schemas.asset_hbd import AssetHbd
from schemas.__private.custom_schemas.asset_hive import AssetHive
from schemas.__private.custom_schemas.asset_vests import AssetVests
from schemas.__private.custom_schemas.authority import Authority
from schemas.__private.custom_schemas.price import Price
from schemas.__private.custom_schemas.public_key import PublicKey
from schemas.__private.custom_schemas.signature import Signature
from schemas.__private.custom_schemas.transaction_id import TransactionId

if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema

operations_schemas = []
__operation_definitions = {}
__operation_definitions_lock = Lock()


def adapt_hive_operations_to_schema() -> Schema:
    global __operation_definitions
    global operations_schemas
    SMT_OPERATIONS_SUPPORTED = False

    with __operation_definitions_lock:
        if not __operation_definitions:
            files_to_parse = [
                Path(__file__).joinpath('../../../../../../libraries/protocol/include/hive/protocol/hive_operations.hpp').resolve(),
                Path(__file__).joinpath('../../../../../../libraries/protocol/include/hive/protocol/hive_virtual_operations.hpp').resolve(),
                Path(__file__).joinpath('../../../../../../libraries/protocol/include/hive/protocol/sps_operations.hpp').resolve(),
                *((
                    Path(__file__).joinpath('../../../../../../libraries/protocol/include/hive/protocol/smt_operations.hpp').resolve(),)
                    if SMT_OPERATIONS_SUPPORTED else ()),
            ]
            for file in files_to_parse:
                __operation_definitions.update(CppHeaderParser.CppHeader(file).CLASSES)
        else:
            return AnyOf(*operations_schemas)

    schemas_for_types_in_hive = {
        'account_name_type': AccountName(),
        'asset_symbol_type': Map({
            'nai': AnyOf(
                AssetHbd.Nai(),
                AssetHive.Nai(),
                AssetVests.Nai(),
            ),
            'decimals': Int(),
        }),
        'authority': Authority(),
        'block_id': TransactionId(),
        'block_id_type': TransactionId(),
        'bool': Bool(),
        'comment_options_extensions_type': Map({
            'author': Str(),
            'premlink': Str(),
            'max_accepted_payout': AssetHbd(),
            'percent_hbd': Int(),
            'allow_votes': Bool(),
            'allow_curation_rewards': Bool(),
            'extensions': Array(
                ArrayStrict(
                    Int(),
                    Map({
                        'beneficiaries': Array(
                            Map({
                                'account': Str(),
                                'weight': Int(),
                            })
                        )
                    }),
                )
            )

        }),
        'custom_id_type': Int(),
        'extensions_type': Array(),  # FIXME: 'temporary schema'
        'flat_map< string, vector< char> >': Map({'props': Array(Str())}),
        'flat_set< account_name_type>': Array(AccountName()),
        'flat_set_ex<int64_t>': Array(Int()),
        'hive::protocol::comment_options_extensions_type': Array(
            ArrayStrict(
                Int(),
                Map({
                    'beneficiaries': Array(
                        Map({
                            'account': Str(),
                            'weight': Int(),
                        }),
                    )
                }),
            )
        ),
        'hive::protocol::update_proposal_extensions_type': Array(
            AnyOf(
                Null(),
                Date(),
            ),
        ),
        'hive::protocol::pow2_work': Map({
            'work': OneOf(
                Map({
                    'input': Map({
                        'worker_account': AccountName(),
                        'prev_block': TransactionId(),
                        'nonce': Int(),
                    }),
                    'pow_summary': Int(),
                }),
                Map({
                    'input': Map({
                        'worker_account': AccountName(),
                        'prev_block': TransactionId(),
                        'nonce': Int(),
                    }),
                    'proof': Map({
                        'n': Int(),
                        'k': Int(),
                        'seed': Int(),
                        'inputs': Array(Int()),
                    }),
                    'prev_block': TransactionId(),
                    'pow_summary': Int(),
                }),
            ),
            'new_owner_key': PublicKey(),
            'props': Map({
                'account_creation_fee': AssetHive(),
                'maximum_block_size': Int(),
                'hbd_interest_rate': Int(),
            }),
        }, required_keys=['work', 'props']),
        'int16_t': Int(),
        'int64_t': Int(),
        'legacy_chain_properties': Map({
            'account_creation_fee': AssetHive(),
            'maximum_block_size': Int(),
            'hbd_interest_rate': Int(),
        }),
        'pow': Map({
            'worker_account': Str(),
            'block_id': TransactionId(),
            'nonce': Int(),
            'work': Map({
                'worker': PublicKey(),
                'input': TransactionId(),
                'signature': Signature(),
                'work': TransactionId(),
            }),
            'props': Map({
                'account_creation_fee': AssetHive(),
                'maximum_block_size': Int(),
                'hbd_interest_rate': Int(),
            }),
        }),
        'pow2_input': Map({
            'worker_account': Str(),
            'prev_block': TransactionId(),
            'nonce': Int(),
        }),
        'price': Price(AssetAny(), AssetAny()),
        'public_key_type': PublicKey(),
        'signed_block_header': Signature(),
        'share_type': Int(),
        'smt_emissions_unit': Array(ArrayStrict(AccountName(), Int())),
        'std::vector< account_name_type>': Array(AccountName()),
        'string': Str(),
        'time_point_sec': Date(),
        'transaction_id_type': TransactionId(),
        'uint8_t': Int(),
        'uint16_t': Int(),
        'uint32_t': Int(),
        'uint64_t': Int(),
        'ushare_type': Int(),
        'vector< authority>': Array(Authority()),
        'vector< asset>': Array(AssetHive()),
        'vector< beneficiary_route_type>': Array(
            Map({
                'account': Str(),
                'weight': Int(),
            }),
        ),
        'vector< char>': Map({
            'data': Str(),
        }),
    }

    asset_types_for_properties_in_hive = {
        # hive_operations
        'account_create_operation': {
          'fee': AssetHive(),
        },
        'account_created_operation': {
            'initial_vesting_shares': AssetVests(),
            'initial_delegation': AssetVests(),
        },
        'author_reward_operation': {
            'hbd_payout': AssetHbd(),
            'hive_payout': AssetHive(),
            'vesting_payout': AssetVests(),
            'curators_vesting_payout': AssetVests(),
        },
        'account_create_with_delegation_operation': {
            'fee': AssetHive(),
            'delegation': AssetVests(),
        },
        'comment_options_operation': {
            'max_accepted_payout': AssetHbd(),
        },
        'comment_reward_operation': {
            'payout': AssetHbd(),
            'total_payout_value': AssetHbd(),
            'curator_payout_value': AssetHbd(),
            'beneficiary_payout_value': AssetHbd(),
        },
        'claim_account_operation': {
            'fee': AssetHive(),
        },
        'curation_reward_operation': {
            'reward': AssetVests(),
        },
        'escrow_transfer_operation': {
            'hbd_amount': AssetHbd(),
            'hive_amount': AssetHive(),
            'fee': AssetHbd(),
        },
        'escrow_release_operation': {
            'hbd_amount': AssetHbd(),
            'hive_amount': AssetHive(),
        },
        'fill_convert_request_operation': {
            'amount_in': AssetHbd(),
            'amount_out': AssetHive(),
        },
        'fill_vesting_withdraw_operation': {
            'withdrawn': AssetVests(),
            'deposited': AssetHive(),
        },
        'interest_operation': {
            'interest': AssetHbd(),
        },
        'liquidity_reward_operation': {
            'payout': AssetHive(),
        },
        'transfer_to_vesting_operation': {
            'amount': AssetHive(),
        },
        'transfer_to_vesting_completed_operation': {
            'hive_vested': AssetHive(),
            'vesting_shares_received': AssetVests(),
        },
        'transfer_operation': {
            'amount': AssetHbd(),
        },
        'update_proposal_operation': {
            'daily_pay': AssetHbd(),
        },
        'withdraw_vesting_operation': {
            'vesting_shares': AssetVests(),
        },
        'witness_update': {
            'fee': AssetHive(),
        },
        'convert_operation': {
            'amount': AssetHbd(),
        },
        'collateralized_convert_operation': {
            'amount': AssetHive(),
        },
        'limit_order_create_operation': {
            'amount_to_sell': AssetHive(),
            'min_to_receive': AssetHbd(),
        },
        'limit_order_create2_operation': {
            'amount_to_sell': AssetHbd(),
        },
        'transfer_from_savings_operation': {
            'amount': AssetHbd(),
        },
        'claim_reward_balance_operation': {
            'reward_hive': AssetHive(),
            'reward_hbd': AssetHbd(),
            'reward_vests': AssetVests(),
        },
        'delegate_vesting_shares_operation': {
            'vesting_shares': AssetVests(),
        },
        'recurrent_transfer_operation': {
            'amount': AssetHive(),
        },
        'witness_update_operation': {
            'fee': AssetHive(),
        },
        'transfer_to_savings_operation': {
            'amount': AssetHbd(),
        },
        # hive_virtual_operations
        'return_vesting_delegation_operation': {
            'vesting_shares': AssetVests()
        },
        'comment_benefactor_reward_operation': {
            'hbd_payout': AssetHbd(),
            'hive_payout': AssetHive(),
            'vesting_payout': AssetVests(),
        },
        'producer_reward_operation': {
            'vesting_shares': AssetVests(),
        },
        'clear_null_account_balance_operation': {
            'total_cleared': Array(AssetHive()),
        },
        'consolidate_treasury_balance_operation': {
            'total_moved': Array(AssetHbd()),
        },
        'sps_fund_operation': {
            'additional_funds': AssetHbd(),
        },
        'sps_convert_operation': {
            'hive_amount_in': AssetHive(),
            'hbd_amount_out': AssetHbd(),
        },
        'hardfork_hive_operation': {
            'hbd_transferred': AssetHbd(),
            'hive_transferred': AssetHive(),
            'vests_converted': AssetVests(),
            'total_hive_from_vests': AssetHive(),
        },
        'hardfork_hive_restore_operation': {
            'hbd_transferred': AssetHbd(),
            'hive_transferred': AssetHive(),
        },
        'fill_recurrent_transfer_operation': {
            'amount': AssetHive(),
        },
        'failed_recurrent_transfer_operation': {
            'amount': AssetHive(),
        },
        'pow_reward_operation': {
            'reward': AssetHive(),
        },
        'effective_comment_vote_operation': {
            'pending_payout': AssetHive()
        },
        'proposal_pay_operation': {
            'payment': AssetHbd(),
        },
        'create_proposal_operation': {
            'daily_pay': AssetHbd(),
        },
        'fill_transfer_from_savings_operation': {
            'amount': AssetHive(),
        },
        'fill_order_operation': {
            'current_pays': AssetHbd(),
            'open_pays': AssetHive(),
        },
        'vesting_shares_split_operation': {
            'vesting_shares_before_split': AssetVests(),
            'vesting_shares_after_split': AssetVests(),
        },
        'fill_collateralized_convert_request_operation': {
            'amount_in': AssetHive(),
            'amount_out': AssetHbd(),
            'excess_collateral': AssetHive(),
        },
        #zależna od 'limit_order_create', w zależności co 'zastawimy/sprzedamy' limit_order_cancelled przyjmie tą wartość Asseta
        'limit_order_cancelled_operation': {
            'amount_back': AssetAny(),
        },
    }

    for operation in __operation_definitions.keys():
        if operation.find('_operation') > 0:
            schema_as_dict = {}
            required_keys = []
            for attribute in __operation_definitions[operation]['properties']['public']:
                if attribute['type'] in schemas_for_types_in_hive:
                    schema_as_dict[attribute['name']] = schemas_for_types_in_hive[attribute['type']]
                    required_keys.append(attribute['name'])
                elif attribute['type'] == 'asset':
                    try:
                        schema_as_dict[attribute['name']] = asset_types_for_properties_in_hive[operation][attribute['name']]
                        required_keys.append(attribute['name'])
                    except KeyError:
                        warn(f'Asset type for {operation} is not defined. AssetAny was used automatically.')
                        schema_as_dict[attribute['name']] = AssetAny()
                elif 'optional' in attribute['type']:
                    if 'authority' in attribute['type']:
                        schema_as_dict[attribute['name']]: Authority()
                    elif 'public_key_type' in attribute['type']:
                        schema_as_dict[attribute['name']] = PublicKey()
                else:
                    raise KeyError(f'Schema creation for the "{operation}" has not been completed. '
                                   f'Not found valid schema to complete "{attribute["type"]}" type.')
            operations_schemas.append(ArrayStrict(Str(pattern=operation.replace('_operation', '')), Map(schema_as_dict, required_keys=required_keys)))

    return AnyOf(*operations_schemas)
