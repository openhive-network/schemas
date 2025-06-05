from __future__ import annotations

from typing import NoReturn, cast

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


class GetBlockBaseEnsured(PreconfiguredBaseModel):
    block: Hf26Block


class GetBlockHeaderBaseEnsured(PreconfiguredBaseModel):
    header: GetBlockHeaderFundament


class GetBlockBase(PreconfiguredBaseModel):
    block: Hf26Block | None = None

    def is_set(self) -> bool:
        return self.block is not None

    @property
    def ensure(self) -> GetBlockBaseEnsured:
        return cast(GetBlockBaseEnsured, self)


class GetBlockHeaderBase(PreconfiguredBaseModel):
    header: GetBlockHeaderFundament | None = None

    def is_set(self) -> bool:
        return self.header is not None

    @property
    def ensure(self) -> GetBlockHeaderBaseEnsured:
        return cast(GetBlockHeaderBaseEnsured, self)


GetBlock = GetBlockBase
GetBlockHeader = GetBlockHeaderBase


class GetBlockRange(PreconfiguredBaseModel):
    blocks: HiveList[Hf26Block]
