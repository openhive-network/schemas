from __future__ import annotations

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.block_api.fundaments_of_responses import Block, EmptyModel, GetBlockFundament, GetBlockHeaderFundament

GetBlock = EmptyModel | GetBlockFundament


class GetBlockHeaderNotEmpty(PreconfiguredBaseModel):
    header: list[GetBlockHeaderFundament]


GetBlockHeader = EmptyModel | GetBlockHeaderNotEmpty


class GetBlockRange(PreconfiguredBaseModel):
    blocks: list[Block]