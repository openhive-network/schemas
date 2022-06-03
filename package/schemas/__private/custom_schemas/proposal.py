from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.custom_schemas.asset_hbd import AssetHbd
from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.fundamental_schemas import Date, Int, Map, Str


if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class Proposal(CustomSchema):
    def _define_schema(self) -> Schema:
        return Map({
            'id': Int(),
            'proposal_id': Int(),
            'creator': Str(),
            'receiver': Str(),
            'start_date': Date(),
            'end_date': Date(),
            'daily_pay': AssetHbd(),
            'subject': Str(),
            'permlink': Str(),
            'total_votes': Int(),
            'status': Str(),
        })
