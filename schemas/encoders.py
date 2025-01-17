

from typing import Any

from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVest
from schemas.fields.hive_int import HiveInt


def enc_hook_base(obj: Any):
    if isinstance(obj, HiveInt):
        return int(obj.value)
    if isinstance(obj, (AssetHbd | AssetHive | AssetVest)):
        return obj.as_legacy()