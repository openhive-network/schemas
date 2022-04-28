from jsonschema.exceptions import ValidationError
import pytest

from schemas.predefined import *
from schemas.__private.custom_schemas import AssetAny


@pytest.mark.parametrize(
    'schema, instance', [
        # AssetAny
        (AssetAny(), {
            'amount': '100',
            'precision': 3,
            'nai': '@@000000013'
        }),
        (AssetAny(), {
            'amount': '100',
            'precision': 3,
            'nai': '@@000000021'
        }),
        (AssetAny(), {
            'amount': '100',
            'precision': 6,
            'nai': '@@000000037'
        }),

        # AssetHbd
        (AssetHbd(), {
            'amount': '100',
            'precision': 3,
            'nai': '@@000000013'
        }),

        # AssetHive
        (AssetHive(), {
            'amount': '100',
            'precision': 3,
            'nai': '@@000000021'
        }),

        # AssetVests
        (AssetVests(), {
            'amount': '100',
            'precision': 6,
            'nai': '@@000000037'
        }),

        # Authority
        (Authority(), {
            'weight_threshold': 1,
            'account_auths': [['22', 1]],
            'key_auths': [
                [
                    'STM7AwB4maYkySTZZbx3mtdTaxsKTYyJxhmUZVK9wd53t2qXCvxmB',
                    1
                ]
            ]
        }),

        # Id
        (Id(), '2d8d2a339514593818919aa4ac59215571641dd6'),
        (Id(), '0000000000000000000000000000000000000000'),

        # Key
        (Key(), 'STM7U2ecB3gEwfrLMQtfVkCN8z3kPmXtDH3HSmLgrbsFpV6UXEwKE'),
        (Key(), 'TST7AwB4maYkySTZZbx3mtdTaxsKTYyJxhmUZVK9wd53t2qXCvxmB'),

        # Price
        (Price(AssetHbd(), AssetHive()), {
            "base": {
                'amount': '100',
                'precision': 3,
                'nai': '@@000000013'
            },
            "quote": {
                'amount': '100',
                'precision': 3,
                'nai': '@@000000021'
            }
        }),

        # Manabar
        (Manabar(), {
            'current_mana': '58925267722823',
            'last_update_time': 1646317446
        }),

        #  Proposal
        (Proposal(), {
            'id': 0,
            'proposal_id': 0,
            'creator': 'alice',
            'receiver': 'bob',
            'start_date': '2019-07-01T00:00:00',
            'end_date': '2019-08-01T23:59:59',
            'daily_pay': {
                'amount': '4800000',
                'precision': 3,
                'nai': '@@000000013'
            },
            'subject': 'My Proposal',
            'permlink': 'creator-proposal-permlink',
            'total_votes': '77351826710',
            'status': 'active'
        }),

        #  Version
        (Version(), '0.0.0')
    ]
)
def test_validation_of_correct_type(schema, instance):
    schema.validate(instance)


@pytest.mark.parametrize(
    'schema, instance', [
        # AssetAny
        (AssetAny(), {
            'amount': '100',
            'precision': 4,  # correct 'precision' value == 3 or 6
            'nai': '@@000000013'
        }),
        (AssetAny(), {
            'amount': '100',
            'precision': 3,
            'nai': 'wrong-nai'
        }),

        # AssetHbd
        (AssetHbd(), {
            'amount': '100',
            'precision': 3,
            'nai': 'wrong-nai'
        }),

        # AssetHive
        (AssetHive(), {
            'amount': 3.141593,  # wrong type of 'amount'
            'precision': 3,
            'nai': '@@000000021'
        }),

        # AssetVests
        (AssetVests(), {
            'amount': '100',
            'precision': 7,  # correct 'precision' value == 6
            'nai': '@@000000037'
        }),

        # Authority
        (Authority(), {
            'weight_threshold': 1,
            'account_auths': [['22', 1]],
            'key_auths': [
                [
                    1,
                    'STM7AwB4maYkySTZZbx3mtdTaxsKTYyJxhmUZVK9wd53t2qXCvxmB'
                ]  # key_auths: wrong array order, should be key, int.
            ]
        }),

        # Id
        (Id(), '2d8d2a339514593818919aa4ac59215571641dd'),  # too short, instance != 40 characters
        (Id(), '00000000000000000000000000000000000000001'),  # too long, instance != 40 characters
        (Id(), '0123456789acdef0123456789abcdef012345ggg'),  # Id() supports hexadecimal numbers, 'g' is out of scope

        # Key
        (Key(), 'PPP7U2ecB3gEwfrLMQtfVkCN8z3kPmXtDH3HSmLgrbsFpV6UXEwKE'),  # Bad key prefix
        (Key(), 'TST7AwB4maYkySTZZbx3mtdTaxsKTYyJxhmUZ....../////?????'),  # invalid characters
        (Key(), 'TST7AwB4maYkySTZZbx3mtdTaxsKTYyJxhmUZVK9wd5'),  # not enough characters (the amount required is 50)

        # Price
        (Price(AssetHbd(), AssetHive()), {
            "base": {
                'amount': '100',
                'precision': 3,
                'nai': '@@000000021'
            },
            "quote": {
                'amount': '100',
                'precision': 3,
                'nai': '@@000000013'
            }
        }),  # incorrect assets order

        #  Verison
        (Version(), '0.0.a')

    ]
)
def test_validation_of_incorrect_type(schema, instance):
    with pytest.raises(ValidationError):
        schema.validate(instance)
