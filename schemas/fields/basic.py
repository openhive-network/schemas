"""
It is file with fields that are used to create model of operation and responses from api
"""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, Generic

from pydantic import ConstrainedList, ConstrainedStr, PrivateAttr
from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import BaseModelT, PreconfiguredBaseModel
from schemas.fields.assets.hbd import AssetHbdT
from schemas.fields.assets.hive import AssetHiveT
from schemas.fields.hive_int import HiveInt
from schemas.fields.integers import Uint16t, Uint32t
from schemas.hive_constants import HIVE_HBD_INTEREST_RATE, HIVE_MAX_BLOCK_SIZE


class EmptyString(ConstrainedStr):
    min_length = 0
    max_length = 0


class AccountName(ConstrainedStr):
    __name_segment = PrivateAttr(r"[a-z][a-z0-9\-]+[a-z0-9]")
    regex = rf"^{__name_segment.default}(?:\.{__name_segment.default})*$"
    min_length = 3
    max_length = 16


class PublicKey(ConstrainedStr):
    regex = re.compile(r"^(?:STM|TST)[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{7,51}$")


class Authority(PreconfiguredBaseModel):
    weight_threshold: HiveInt
    account_auths: list[tuple[AccountName, HiveInt]]
    key_auths: list[tuple[PublicKey, HiveInt]]


class CustomIdType(ConstrainedStr):
    max_length = 32


class HbdExchangeRate(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    """
    Field similar to price, but just base can be Hive or Hbd. Quote must be Hive.
    To choose format of Assets you can do it like in Price field:
    Legacy -> HbdExchangeRate[AssetHiveLegacy, AssetHbdLegacy](parameters)
    HF26 -> HbdExchangeRate[AssetHiveHF26, AssetHbdHF26](parameters)
    Here Hive also must be first parameter of generic
    """

    base: AssetHiveT | AssetHbdT
    quote: AssetHiveT | AssetHbdT


class LegacyChainProperties(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT]):
    """
    You can choose of Asset format for this field, to do it:
    Legacy -> LegacyChainProperties[AssetHiveLegacy](parameters)
    Nai -> LegacyChainProperties[AssetHiveHF26](parameters)
    """

    account_creation_fee: AssetHiveT
    maximum_block_size: Uint32t = Uint32t(HIVE_MAX_BLOCK_SIZE)
    hbd_interest_rate: Uint16t = Uint16t(HIVE_HBD_INTEREST_RATE)


if TYPE_CHECKING:
    HiveList = list
else:

    class HiveList(ConstrainedList, Generic[BaseModelT]):
        """Some responses could return empty list, it should not raise any error. This type makes it possible"""

        min_items = 0
