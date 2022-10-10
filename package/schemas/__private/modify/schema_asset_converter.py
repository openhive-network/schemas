import copy
from typing import Union
from schemas.__private.fundamental_schemas import Schema
from schemas.predefined import *


def __convert_array_or_any_of(schema: Union[AnyOf, Array, ArrayStrict], *, to_legacy) -> Union[Array, ArrayStrict]:
    for index in range(len(schema)):
        schema[index] = convert_assets_to_legacy_format(schema[index]) if to_legacy else \
            convert_assets_to_nai_format(schema[index])
    return schema


def __convert_asset_any(schema: Union[AssetAny, LegacyAssetAny], *, to_legacy) -> Union[AssetAny, LegacyAssetAny]:
    return LegacyAssetAny() if to_legacy else AssetAny()


def __convert_asset_hive(schema: Union[AssetHive, LegacyAssetHive], *, to_legacy) -> Union[AssetHive, LegacyAssetHive]:
    return LegacyAssetHive() if to_legacy else AssetHive()


def __convert_asset_hbd(schema: Union[AssetHbd, LegacyAssetHbd], *, to_legacy) -> Union[AssetHbd, LegacyAssetHbd]:
    return LegacyAssetHbd() if to_legacy else AssetHbd()


def __convert_asset_vest(schema: Union[AssetVests, LegacyAssetVests], *, to_legacy) -> Union[AssetVests, LegacyAssetVests]:
    return LegacyAssetVests() if to_legacy else AssetVests()


def __convert_custom_schema(schema: Union[HbdExchangeRate, Price, Proposal], *, to_legacy) -> \
        Union[HbdExchangeRate, Price, Proposal]:
    schema.legacy_format = to_legacy
    return schema


def __convert_map(schema: Map, *, to_legacy: bool) -> Map:
    keys = schema.keys()
    for key in keys:
        schema[key] = convert_assets_to_legacy_format(schema[key]) if to_legacy else convert_assets_to_nai_format(schema[key])
    return schema


convert = {
    AnyOf: __convert_array_or_any_of,
    Array: __convert_array_or_any_of,
    ArrayStrict: __convert_array_or_any_of,
    AssetAny: __convert_asset_any,
    AssetHive: __convert_asset_hive,
    AssetHbd: __convert_asset_hbd,
    AssetVests: __convert_asset_vest,
    HbdExchangeRate: __convert_custom_schema,
    LegacyAssetAny: __convert_asset_any,
    LegacyAssetHive: __convert_asset_hive,
    LegacyAssetHbd: __convert_asset_hbd,
    LegacyAssetVests: __convert_asset_vest,
    Map: __convert_map,
    Price: __convert_custom_schema,
    Proposal: __convert_custom_schema,
}


def convert_assets_to_legacy_format(schema: Schema) -> Schema:
    output_schema = copy.deepcopy(schema)
    try:
        return convert[type(output_schema)](output_schema, to_legacy=True)
    except KeyError:
        return output_schema


def convert_assets_to_nai_format(schema: Schema) -> Schema:
    output_schema = copy.deepcopy(schema)
    try:
        return convert[type(output_schema)](output_schema, to_legacy=False)
    except KeyError:
        return output_schema
