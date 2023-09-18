from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import HiveList
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.block_api.fundaments_of_responses import GetBlockHeaderFundament, Hf26Block


class GetBlockBase(PreconfiguredBaseModel):
    block: Hf26Block


GetBlock = GetBlockBase | PreconfiguredBaseModel


class GetBlockHeaderBase(PreconfiguredBaseModel):
    header: GetBlockHeaderFundament


GetBlockHeader = GetBlockHeaderBase | PreconfiguredBaseModel


class GetBlockRange(PreconfiguredBaseModel):
    blocks: HiveList[Hf26Block]
