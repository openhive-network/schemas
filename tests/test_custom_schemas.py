from jsonschema.exceptions import ValidationError
import pytest

from schemas.predefined import *
from schemas.__private.custom_schemas import AssetAny, LegacyAssetAny


@pytest.mark.parametrize(
    'schema, instance', [
        # AccountName
        (AccountName(), 'account-name'),
        (AccountName(), 'account---name'),
        (AccountName(), 'account.name'),

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

        #  HardforkVersion
        (HardforkVersion(), '0.0.0'),

        # Hex
        (Hex(), '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'),
        (Hex(), 'd94aa5bbc88beaf09b67f825aa4450cf5105d111149ba6db560b582c7dbb026c7fc9c2eb5051815a72b17f6896ed59d3851d'),
        (Hex(minLength=10), '0123456789'),
        (Hex(maxLength=9), '012345'),

        #LegacyAssetAny
        (LegacyAssetAny(), '1.000 HBD'),
        (LegacyAssetAny(), '1.000 TBD'),
        (LegacyAssetAny(), '1.000 HIVE'),
        (LegacyAssetAny(), '1.000 TESTS'),
        (LegacyAssetAny(), '1.000000 VESTS'),

        #LegacyAssetHbd
        (LegacyAssetHbd(), '1.000 HBD'),
        (LegacyAssetHbd(), '1.000 TBD'),  # HBD representation in the hive testnet

        #LegacyAssetHive
        (LegacyAssetHive(), '1.000 HIVE'),
        (LegacyAssetHive(), '1.000 TESTS'),  # HIVE representation in the hive testnet

        #LegacyAssetVests
        (LegacyAssetVests(), '100.000000 VESTS'),

        # Manabar
        (Manabar(), {
            'current_mana': '58925267722823',
            'last_update_time': 1646317446
        }),

        #Permlink
        (Permlink(), 256 * '0'),

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

        # PublicKey
        (PublicKey(), 'STM7U2ecB3gEwfrLMQtfVkCN8z3kPmXtDH3HSmLgrbsFpV6UXEwKEa'),
        (PublicKey(), 'TST7AwB4maYkySTZZbx3mtdTaxsKTYyJxhmUZVK9wd53t2qXCvxmBa'),

        # Signature
        (Signature(), '204f8ad56a8f5cf722a02b035a61b500aa59b9519b2c33c77a80c0a714680a5a5a7a340d909d19996613c5e4ae92146b9add8a7a663eef37d837ef881477313043'),
        (Signature(), 130 * '0'),

        # TransactionId
        (TransactionId(), '2d8d2a339514593818919aa4ac59215571641dd6'),
        (TransactionId(), '0000000000000000000000000000000000000000'),
    ]
)
def test_validation_of_correct_type(schema, instance):
    schema.validate(instance)


@pytest.mark.parametrize(
    'schema, instance', [
        # AccountName
        (AccountName(), 'ac'),  # not enough characters minimum is 3 characters
        (AccountName(), 'account-name-longer-than-16-characters'),
        (AccountName(), 'invalid-characters-@'),
        (AccountName(), '---'),
        (AccountName(), 'a.a'),
        (AccountName(), '-aa'),
        (AccountName(), '...'),

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
                ]  # key_auths: wrong array order, should be PublicKey, Int.
            ]
        }),

        #  HardforkVersion
        (HardforkVersion(), '0.0.a'),

        # Hex
        (Hex(), 'ghijklmnoprstuvwxyz'),  # there is no such hexadecimal digits
        (Hex(), 'ghijklmno000prstuvwxyz'),  # hexadecimal number nested in non-hexadecimal string
        (Hex(), '000ghijklmnoprstuvwxyz'),  # hexadecimal prefix
        (Hex(), 'ghijklmnoprstuvwxyz000'),  # hexadecimal suffix
        (Hex(minLength=5), '0123'),
        (Hex(maxLength=5), '012345'),

        # LegacyAssetAny
        (LegacyAssetAny(), '1.0 HBD'),  # required thousandths of HBD
        (LegacyAssetAny(), '1.0 TBD'),  # required thousandths of TBD
        (LegacyAssetAny(), '1.0 HIVE'),  # required thousandths of Hive
        (LegacyAssetAny(), '1.0 TESTS'),  # required thousandths of Tests
        (LegacyAssetAny(), '1.0 VESTS'),  # millionths of Vests required

        # LegacyAssetHbd
        (LegacyAssetHbd(), '1.000HBD'),  # missing space between amount and token
        (LegacyAssetHbd(), '1.000TBD'),

        # LegacyAssetHive
        (LegacyAssetHive(), '1.000HIVE'),
        (LegacyAssetHive(), '1.000TESTS'),

        # LegacyAssetVests
        (LegacyAssetVests(), '100.000000VESTS'),

        # Permlink
        (Permlink(), 257 * '0'),  # too many characters

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

        # PublicKey
        (PublicKey(), 'PPP7U2ecB3gEwfrLMQtfVkCN8z3kPmXtDH3HSmLgrbsFpV6UXEwKEa'),  # Bad key prefix
        (PublicKey(), 'TST7AwB4maYkySTZZbx3mtdTaxsKTYyJxhmUZ....../////??????'),  # invalid characters
        (PublicKey(), 'STM5J2CVu'),  # not enough characters (the minimum required is 7)
        (PublicKey(), 'TST5J2CVuKtMCoLzoWb5SXDex5vGVeKETfs7YYUxy6Jh9WTx2PJns911111'),  # too many characters (maximum <= 51)

        # Signature
        (Signature(), 129 * '0'),  # too short, instance != 130 characters
        (Signature(), 131 * '0'),  # too long, instance != 130 characters

        # TransactionId
        (TransactionId(), '2d8d2a339514593818919aa4ac59215571641dd'),  # too short, instance != 40 characters
        (TransactionId(), '00000000000000000000000000000000000000001'),  # too long, instance != 40 characters
        (TransactionId(), '0123456789acdef0123456789abcdef012345ggg'),  # TransactionId() supports hexadecimal numbers, 'g' is out of scope
    ]
)
def test_validation_of_incorrect_type(schema, instance):
    with pytest.raises(ValidationError):
        schema.validate(instance)
