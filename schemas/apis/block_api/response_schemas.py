from __future__ import annotations

from typing import NoReturn

from typing_extensions import Self

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.block_api.fundaments_of_responses import GetBlockHeaderFundament, Hf26Block
from schemas.fields.hive_list import HiveList
from schemas.optional_response import OptionalResponse


class EmptyResponse(PreconfiguredBaseModel, OptionalResponse):
    def is_set(self) -> bool:
        return False

    @property
    def ensure(self) -> NoReturn:
        raise ValueError("Member is not set")


class NonEmptyResponse(OptionalResponse):
    def is_set(self) -> bool:
        return True

    @property
    def ensure(self) -> Self:
        return self


class GetBlockBase(PreconfiguredBaseModel, NonEmptyResponse):
    block: Hf26Block


class GetBlockHeaderBase(PreconfiguredBaseModel, NonEmptyResponse):
    header: GetBlockHeaderFundament


GetBlock = GetBlockBase | EmptyResponse
GetBlockHeader = GetBlockHeaderBase | EmptyResponse


class GetBlockRange(PreconfiguredBaseModel):
    blocks: HiveList[Hf26Block]
