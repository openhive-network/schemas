from schemas.__private.modify.schema_asset_converter import convert_assets_to_legacy_format, convert_assets_to_nai_format
import pytest
from schemas.predefined import *

ASSERT_ARGUMENTS = [
        # Fundamental schemas
        (AssetHive(), LegacyAssetHive()),
        (AssetHbd(), LegacyAssetHbd()),
        (AssetVests(), LegacyAssetVests()),
        (AssetAny(), LegacyAssetAny()),
        (AnyOf(AssetHbd(), AssetHive()), AnyOf(LegacyAssetHbd(), LegacyAssetHive())),
        # Custom schemas
        (HbdExchangeRate(), HbdExchangeRate(legacy_format=True)),
        (Price(), Price(legacy_format=True)),
        (Proposal(), Proposal(legacy_format=True)),
    ]


@pytest.mark.parametrize(
    'value_to_convert, expected_value', ASSERT_ARGUMENTS
)
def test_single_asset_conversion_to_legacy(value_to_convert, expected_value):
    assert convert_assets_to_legacy_format(value_to_convert) == expected_value


@pytest.mark.parametrize(
    'expected_value, value_to_convert', ASSERT_ARGUMENTS
)
def test_single_asset_conversion_to_nai(expected_value, value_to_convert):
    assert convert_assets_to_nai_format(value_to_convert) == expected_value


def test_array_asset_conversion_to_legacy():
    assert convert_assets_to_legacy_format(Array(Int(), AssetAny())) == Array(Int(), LegacyAssetAny())


def test_array_asset_conversion_to_nai():
    assert convert_assets_to_nai_format(Array(Int(), LegacyAssetAny())) == Array(Int(), AssetAny())


def test_map_asset_conversion_to_legacy():
    first = Map({
        'id': Int(),
        'name': AccountName(),
        'savings_hbd_balance': AssetHbd(),
    })

    second = Map({
        'id': Int(),
        'name': AccountName(),
        'savings_hbd_balance': LegacyAssetHbd(),
    })

    assert convert_assets_to_legacy_format(first) == second


def test_map_asset_conversion_to_nai():
    first = Map({
        'id': Int(),
        'name': AccountName(),
        'savings_hbd_balance': LegacyAssetHbd(),
    })

    second = Map({
        'id': Int(),
        'name': AccountName(),
        'savings_hbd_balance': AssetHbd(),
    })

    assert convert_assets_to_nai_format(first) == second


def test_map_asset_conversion_with_required_keys():
    first = Map({
        'requests': Array(
            Map({
                'id': Int(),
                'owner': AccountName(),
                'requestid': Int(),
                'collateral_amount': LegacyAssetHive(),
                'converted_amount': LegacyAssetHbd(),
                'conversion_date': Date(),
            }, required_keys=['id', 'owner', 'requestid'])
        ),
        'sequence': Int(),
    }, required_keys=['requests'])

    second = Map({
        'requests': Array(
            Map({
                'id': Int(),
                'owner': AccountName(),
                'requestid': Int(),
                'collateral_amount': AssetHive(),
                'converted_amount': AssetHbd(),
                'conversion_date': Date(),
            }, required_keys=['id', 'owner', 'requestid'])
        ),
        'sequence': Int(),
    },  required_keys=['requests'])

    assert convert_assets_to_nai_format(first) == second


def test_nested_maps_asset_conversion_to_legacy():
    first = Map({
        'request': Map({
            'id': Int(),
            'owner': AccountName(),
            'requestid': Int(),
            'collateral_amount': AssetHive(),
            'converted_amount': AssetHbd(),
            'conversion_date': Date(),
        })
    })

    second = Map({
        'request': Map({
            'id': Int(),
            'owner': AccountName(),
            'requestid': Int(),
            'collateral_amount': LegacyAssetHive(),
            'converted_amount': LegacyAssetHbd(),
            'conversion_date': Date(),
        })
    })

    assert convert_assets_to_legacy_format(first) == second


def test_nested_maps_asset_conversion_to_nai():
    first = Map({
        'request': Map({
            'id': Int(),
            'owner': AccountName(),
            'requestid': Int(),
            'collateral_amount': LegacyAssetHive(),
            'converted_amount': LegacyAssetHbd(),
            'conversion_date': Date(),
        })
    })

    second = Map({
        'request': Map({
            'id': Int(),
            'owner': AccountName(),
            'requestid': Int(),
            'collateral_amount': AssetHive(),
            'converted_amount': AssetHbd(),
            'conversion_date': Date(),
        })
    })

    assert convert_assets_to_nai_format(first) == second


def test_nested_maps_and_array_asset_conversion_to_legacy():
    first = Map({
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

    second = Map({
        'requests': Array(
            Map({
                'id': Int(),
                'owner': AccountName(),
                'requestid': Int(),
                'collateral_amount': LegacyAssetHive(),
                'converted_amount': LegacyAssetHbd(),
                'conversion_date': Date(),
            })
        )
    })

    assert convert_assets_to_legacy_format(first) == second


def test_nested_maps_and_array_asset_conversion_to_nai():
    first = Map({
        'requests': Array(
            Map({
                'id': Int(),
                'owner': AccountName(),
                'requestid': Int(),
                'collateral_amount': LegacyAssetHive(),
                'converted_amount': LegacyAssetHbd(),
                'conversion_date': Date(),
            })
        )
    })

    second = Map({
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

    assert convert_assets_to_nai_format(first) == second
