from __future__ import annotations

from schemas.block_api.fundaments_of_responses import GetBlockEmptyModel, GetBlockNotEmptyModel

GetBlock = GetBlockEmptyModel | GetBlockNotEmptyModel
