from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import HiveList
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.block_api.fundaments_of_responses import Block, EmptyModel, GetBlockFundament, GetBlockHeaderFundament

GetBlock = EmptyModel | GetBlockFundament


class GetBlockHeaderNotEmpty(PreconfiguredBaseModel):
    header: GetBlockHeaderFundament


GetBlockHeader = EmptyModel | GetBlockHeaderNotEmpty


class GetBlockRange(PreconfiguredBaseModel):
    blocks: HiveList[Block]
