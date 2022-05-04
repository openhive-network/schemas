from threading import Lock
from typing import Dict
from warnings import warn

import CppHeaderParser

from schemas.predefined import *

__operation_definitions = None
__operation_definitions_lock = Lock()


def adapt_hive_operations_to_schema(operation_name: str):
    global __operation_definitions

    types_used_in_hive = {'account_name_type': Str(maxLength=16),
                          'flat_set< account_name_type>': Str(maxLength=16),
                          'asset': AssetAny(),
                          'authority': Authority(),
                          'block_id': Id(),
                          'bool': Bool(),
                          'comment_options_extensions_type': Array(), ##??
                          'extensions_type': Array(), ##??
                          'hive::protocol::comment_options_extensions_type': Map({
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
                                      })
                                  )
                              )

                          }),
                          'int16_t': Int(),
                          'public_key_type': Key(),
                          'string': Str(),
                          'optional< authority>': Authority(),
                          'optional< public_key_type>': Key(),
                          'price': Price(),
                          'time_point_sec': Date(),
                          'uint16_t': Int(),
                          'uint32_t': Int(),
                          'vector< char>': Str(),
                          }

    #TODO operacja ma być sprawdzana pod kątem assetów, jeśli asset nie jest zdefiniowany ma zostać użyty AssetAny i rzucony warning
    assets_details = {
        'account_create_operation': {
          'fee': AssetHive(),
        },
        'account_create_with_delegation_operation': {
            'fee': AssetHive(),
            'delegation': AssetVests(),
        },


        'comment_options_operation': {
            'max_accepted_payout': AssetHbd(),
        },


        'claim_account_operation': {
            'fee': AssetHive(),
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
        'transfer_to_vesting_operation': {
            'amount': AssetHive(),
        },
        'transfer_operation': {
            'amount': AssetAny(),  # asset nie jest doprecyzowany w cpp
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
        }
    }
    # TODO to ca przyjdzie type.find(key) if >1 and in types_used_in_hive
    with __operation_definitions_lock:
        if __operation_definitions is None:
            __operation_definitions = CppHeaderParser.CppHeader(
                '/home/dev/hive/libraries/protocol/include/hive/protocol/hive_operations.hpp'
            )

    schema_as_dict = {}
    for attribute in __operation_definitions.CLASSES[operation_name]['properties']['public']:
        if attribute['type'] not in types_used_in_hive:
            k = list(types_used_in_hive.keys())
            # bierze klucz i sprawdza czy jest częścią tego co przyszło w attribute['type']
            if types_used_in_hive.keys() in attribute['type']:
                print()
            else:
                warn(f'{attribute["type"]}')
                raise KeyError(f'{attribute["type"]}')

        if attribute['type'] == 'asset':
            schema_as_dict.update({attribute['name']: assets_details[operation_name][attribute['name']]})
        else:
            schema_as_dict.update({attribute['name']: types_used_in_hive[attribute['type']]})

    return Map(schema_as_dict)

    # schema_as_dict = {}
    # for attribute in __operation_definitions.CLASSES[operation_name]['properties']['public']:
    #     if attribute['type'] not in types_used_in_hive:
    #         warn(f'{attribute["type"]}')
    #         raise KeyError(f'{attribute["type"]}')
    #
    #     if attribute['type'] == 'asset':
    #         schema_as_dict.update({attribute['name']: assets_details[operation_name][attribute['name']]})
    #     else:
    #         schema_as_dict.update({attribute['name']: types_used_in_hive[attribute['type']]})
    #
    # return Map(schema_as_dict)


f = adapt_hive_operations_to_schema('witness_set_properties_operation')


import pytest
@pytest.mark.parametrize(
    'method_name', [
         'account_create_operation',
         'account_create_with_delegation_operation',
         'account_update_operation',
         'account_update2_operation',
         'comment_operation',
         'beneficiary_route_type',
         'comment_payout_beneficiaries',
         'votable_asset_info_v1',
         'allowed_vote_assets',
         'comment_options_operation',
         'claim_account_operation',
         'create_claimed_account_operation',
         'delete_comment_operation',
         'vote_operation',
         'transfer_operation',
         'escrow_transfer_operation',
         'escrow_approve_operation',
         'escrow_dispute_operation',
         'escrow_release_operation',
         'transfer_to_vesting_operation',
         'withdraw_vesting_operation',
         'set_withdraw_vesting_route_operation',
         'legacy_chain_properties',
         'witness_update_operation',
         'witness_set_properties_operation',
         'account_witness_vote_operation',
         'account_witness_proxy_operation',
         'custom_operation',
         'custom_json_operation',
         'custom_binary_operation',
         'feed_publish_operation',
         'convert_operation',
         'collateralized_convert_operation',
         'limit_order_create_operation',
         'limit_order_create2_operation',
         'limit_order_cancel_operation',
         'pow',
         'pow_operation',
         'pow2_input',
         'pow2',
         'equihash_pow',
         'pow2_operation',
         'report_over_production_operation',
         'request_account_recovery_operation',
         'recover_account_operation',
         'reset_account_operation',
         'set_reset_account_operation',
         'change_recovery_account_operation',
         'transfer_to_savings_operation',
         'transfer_from_savings_operation',
         'cancel_transfer_from_savings_operation',
         'decline_voting_rights_operation',
         'claim_reward_balance_operation',
         'claim_reward_balance2_operation',
         'delegate_vesting_shares_operation',
         'recurrent_transfer_operation',
         'serialization_functor<comment_options_extension>',
         'variant_creator_functor<comment_options_extension>',
         'serialization_functor<pow2_work>',
         'variant_creator_functor<pow2_work>'
    ]
)
def test_params_types(method_name):
    x = adapt_hive_operations_to_schema(method_name)
    print()
