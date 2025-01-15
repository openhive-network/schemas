from __future__ import annotations

from msgspec import field
from pydantic import Field

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.block_api.fundaments_of_responses import SignedBlockBase
from schemas.fields.assets._base import AssetHive
from schemas.fields.basic import AccountName
from schemas.fields.compound import Props, RdDynamicParams
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.fields.resolvables import OptionallyEmpty
from schemas.fields.version import HardforkVersion
from schemas.transaction import Transaction


class DebugGenerateBlocks(PreconfiguredBaseModel):
    blocks: HiveInt


class DebugGenerateBlocksUntil(DebugGenerateBlocks):
    """Identical like debug_generate_blocks"""


class DebugGetHardforkPropertyObject(PreconfiguredBaseModel, kw_only=True):
    id_: HiveInt = field(name="id")
    processed_hardforks: list[HiveDateTime]
    last_hardfork: HiveInt
    current_hardfork_version: HardforkVersion
    next_hardfork: HardforkVersion
    next_hardfork_time: HiveDateTime


class DebugGetHeadBlock(PreconfiguredBaseModel):
    block: SignedBlockBase[Transaction] | None = None


class DebugGetJsonSchema(PreconfiguredBaseModel):
    schema_: str = field(name="schema")


class DebugGetWitnessSchedule(PreconfiguredBaseModel, kw_only=True):
    id_: HiveInt = field(name="id")
    current_virtual_time: HiveInt
    next_shuffle_block_num: HiveInt
    current_shuffled_witnesses: list[OptionallyEmpty[AccountName]]
    num_scheduled_witnesses: HiveInt
    elected_weight: HiveInt
    timeshare_weight: HiveInt
    miner_weight: HiveInt
    witness_pay_normalization_factor: HiveInt
    median_props: Props[AssetHive]
    majority_version: HardforkVersion
    max_voted_witnesses: HiveInt
    max_miner_witnesses: HiveInt
    max_runner_witnesses: HiveInt
    hardfork_required_witnesses: HiveInt
    account_subsidy_rd: RdDynamicParams
    account_subsidy_witness_rd: RdDynamicParams
    min_witness_account_subsidy_decay: HiveInt


class DebugHasHardfork(PreconfiguredBaseModel):
    has_hardfork: bool


class DebugPopBlock(PreconfiguredBaseModel):
    """Empty model"""


class DebugPushBlocks(DebugGenerateBlocks):
    """Identical like debug_generate_blocks"""


class DebugSetHardfork(PreconfiguredBaseModel):
    """Empty model"""


class DebugSetVestPrice(PreconfiguredBaseModel):
    """Empty model"""


class DebugThrowException(PreconfiguredBaseModel):
    """Empty model"""
