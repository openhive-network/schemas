# from __future__ import annotations

# from typing import TypeVar

# from schemas.fields.assets._base import AssetHF26, AssetLegacy
# from schemas.fields.assets._symbol import HbdSymbolType
# from schemas.fields.assets.asset_info import AssetInfo
# from schemas.fields.hive_int import HiveInt

# __all__ = [
#     # MAINNET
#     "AssetHbdHF26",
#     "AssetHbdLegacy",
#     "AssetHbdT",
#     # TESTNET
#     "AssetTbdHF26",
#     "AssetTbdLegacy",
#     "AssetTbdT",
# ]


# class AssetHbdHF26(AssetHF26):
#     @staticmethod
#     def get_asset_information() -> AssetInfo:
#         return HbdSymbolType.get_asset_information()

#     nai: str = get_asset_information().nai
#     precision: HiveInt = get_asset_information().precision


# class AssetTbdHF26(AssetHbdHF26):
#     __testnet__ = True


# class AssetHbdLegacy(AssetLegacy):
#     @classmethod
#     def get_asset_information(cls) -> AssetInfo:
#         return HbdSymbolType.get_asset_information()


# class AssetTbdLegacy(AssetHbdLegacy):
#     __testnet__ = True


# AssetHbdT = TypeVar("AssetHbdT", AssetHbdHF26, AssetHbdLegacy)
# AssetTbdT = TypeVar("AssetTbdT", AssetTbdHF26, AssetTbdLegacy)
