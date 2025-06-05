from __future__ import annotations

from msgspec import field

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVests
from schemas.fields.basic import (
    AccountName,
    PublicKey,
    WitnessUrl,
)
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.fields.integers import Uint16t, Uint32t
from schemas.fields.resolvables import AnyAsset, AssetUnionAssetHiveAssetHbd
from schemas.hive_constants import HIVE_HBD_INTEREST_RATE, HIVE_MAX_BLOCK_SIZE

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
]


class Authority(PreconfiguredBaseModel):
    weight_threshold: HiveInt
    account_auths: list[tuple[AccountName, HiveInt]]
    key_auths: list[tuple[PublicKey, HiveInt]]


class DelayedVotes(PreconfiguredBaseModel):
    time: HiveDateTime
    val: HiveInt


class HbdExchangeRate(PreconfiguredBaseModel):
    base: AssetUnionAssetHiveAssetHbd
    quote: AssetUnionAssetHiveAssetHbd


class LegacyChainProperties(PreconfiguredBaseModel):
    account_creation_fee: AssetHive
    maximum_block_size: Uint32t = Uint32t(HIVE_MAX_BLOCK_SIZE)
    hbd_interest_rate: Uint16t = Uint16t(HIVE_HBD_INTEREST_RATE)


class Manabar(PreconfiguredBaseModel):
    current_mana: HiveInt
    last_update_time: HiveInt


class Price(PreconfiguredBaseModel):
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


class WitnessProps(Props):
    hbd_exchange_rate: HbdExchangeRate | None = None
    url: WitnessUrl | None = None
    new_signing_key: PublicKey | None = None


class RcAccountObject(PreconfiguredBaseModel):
    account: AccountName
    rc_manabar: Manabar
    max_rc_creation_adjustment: AssetVests
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
