from __future__ import annotations

from typing import Generic, Literal

from pydantic import Field

from schemas._preconfigured_base_model import PreconfiguredBaseModel
# from schemas.fields.assets.hbd import AssetHbd
# from schemas.fields.assets.hive import AssetHive
# from schemas.fields.assets.vests import AssetVest
from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVest
from schemas.fields.basic import (
    AccountName,
    PublicKey,
    WitnessUrl,
)
from schemas.fields.hex import Hex
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.fields.integers import Uint16t, Uint32t
from schemas.fields.resolvables import AnyAsset, AssetUnion
from schemas.hive_constants import HIVE_HBD_INTEREST_RATE, HIVE_MAX_BLOCK_SIZE
from msgspec import field

__all__ = [
    "Authority",
    "DelayedVotes",
    "HbdExchangeRate",
    "LegacyChainProperties",
    "Manabar",
    "Price",
    "Proposal",
    "Props",
    "WitnessProps",
    "RcAccountObject",
    "RdDecayParams",
    "RdDynamicParams",
    "WitnessPropsSerialized",
]


class Authority(PreconfiguredBaseModel):
    weight_threshold: HiveInt
    account_auths: list[tuple[AccountName, HiveInt]]
    key_auths: list[tuple[PublicKey, HiveInt]]


class DelayedVotes(PreconfiguredBaseModel):
    time: HiveDateTime
    val: HiveInt


class HbdExchangeRate(PreconfiguredBaseModel):
    """
    Field similar to price, but just base can be Hive or Hbd. Quote must be Hive.
    To choose format of Assets you can do it like in Price field:
    Legacy -> HbdExchangeRate[AssetHiveLegacy, AssetHbdLegacy](parameters)
    HF26 -> HbdExchangeRate[AssetHiveHF26, AssetHbdHF26](parameters)
    Here Hive also must be first parameter of generic
    """

    base: AssetUnion[AssetHive, AssetHbd]
    quote: AssetUnion[AssetHive, AssetHbd]


class LegacyChainProperties(PreconfiguredBaseModel):
    """
    You can choose of Asset format for this field, to do it:
    Legacy -> LegacyChainProperties[AssetHiveLegacy](parameters)
    Nai -> LegacyChainProperties[AssetHiveHF26](parameters)
    """

    account_creation_fee: AssetHive
    maximum_block_size: Uint32t = Uint32t(HIVE_MAX_BLOCK_SIZE)
    hbd_interest_rate: Uint16t = Uint16t(HIVE_HBD_INTEREST_RATE)


class Manabar(PreconfiguredBaseModel):
    current_mana: HiveInt
    last_update_time: HiveInt


class Price(PreconfiguredBaseModel):
    """
    Valid structure for Price field is:
    base: Hive quote: Hbd or base: Hbd quote: Hive
    You can choose format of Assets, to choose legacy format -> Price[AssetHiveLegacy, AssetHbdLegacy, AssetVestsHF26](parameters).
    For HF26 format -> Price[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26].
    Remember that Hive must be first parameter of generic !
    """

    base: AnyAsset
    quote: AnyAsset


class Proposal(PreconfiguredBaseModel, kw_only=True):
    id_: HiveInt = field(name="id")
    proposal_id: HiveInt
    creator: AccountName
    receiver: AccountName
    start_date: HiveDateTime
    end_date: HiveDateTime
    daily_pay: AssetHbd
    subject: str
    permlink: str
    total_votes: HiveInt
    status: str


class Props(PreconfiguredBaseModel):
    account_creation_fee: AssetHive | None = None
    maximum_block_size: HiveInt | None = None
    hbd_interest_rate: HiveInt | None = None
    account_subsidy_budget: HiveInt | None = None
    account_subsidy_decay: HiveInt | None = None


class WitnessProps(PreconfiguredBaseModel):
    hbd_exchange_rate: HbdExchangeRate | None = None
    url: WitnessUrl | None = None
    new_signing_key: PublicKey | None = None


class RcAccountObject(PreconfiguredBaseModel):
    account: AccountName
    rc_manabar: Manabar
    max_rc_creation_adjustment: AssetVest
    max_rc: HiveInt
    delegated_rc: HiveInt
    received_delegated_rc: HiveInt


class RdDecayParams(PreconfiguredBaseModel):
    decay_per_time_unit: HiveInt
    decay_per_time_unit_denom_shift: HiveInt


class RdDynamicParams(PreconfiguredBaseModel):
    resource_unit: HiveInt
    budget_per_time_unit: HiveInt
    pool_eq: HiveInt
    max_pool_size: HiveInt
    decay_params: RdDecayParams
    min_decay: HiveInt


WitnessPropsSerializedKey = Literal[
    "account_creation_fee",
    "account_subsidy_budget",
    "account_subsidy_decay",
    "key",
    "maximum_block_size",
    "new_signing_key",
    "sbd_exchange_rate",
    "sbd_interest_rate",
    "url",
    "hbd_exchange_rate",
    "hbd_interest_rate",
]

WitnessPropsSerialized = list[tuple[WitnessPropsSerializedKey, Hex]]
