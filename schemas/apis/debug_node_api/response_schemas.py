from __future__ import annotations

from pydantic import Field

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHiveHF26, EmptyString, HiveDateTime, HiveInt
from schemas.__private.hive_fields_custom_schemas import HardforkVersion, Props, RdDynamicParams
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.block_api.fundaments_of_responses import SignedBlock
from schemas.transaction_model.transaction import Transaction


class DebugGenerateBlocks(PreconfiguredBaseModel):
    blocks: HiveInt


class DebugGenerateBlocksUntil(DebugGenerateBlocks):
    """Identical like debug_generate_blocks"""


class DebugGetHardforkPropertyObject(PreconfiguredBaseModel):
    id_: HiveInt = Field(alias="id")
    processed_hardforks: list[HiveDateTime]
    last_hardfork: HiveInt
    current_hardfork_version: HardforkVersion
    next_hardfork: HardforkVersion
    next_hardfork_time: HiveDateTime


class DebugGetJsonSchema(PreconfiguredBaseModel):
    schema_: str = Field(alias="schema")


class DebugGetWitnessSchedule(PreconfiguredBaseModel):
    id_: HiveInt = Field(alias="id")
    current_virtual_time: HiveInt
    next_shuffle_block_num: HiveInt
    current_shuffled_witnesses: list[AccountName | EmptyString]
    num_scheduled_witnesses: HiveInt
    elected_weight: HiveInt
    timeshare_weight: HiveInt
    miner_weight: HiveInt
    witness_pay_normalization_factor: HiveInt
    median_props: Props[AssetHiveHF26]
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


class DebugGetHeadBlock(PreconfiguredBaseModel):
    block: SignedBlock[Transaction] | None = None
