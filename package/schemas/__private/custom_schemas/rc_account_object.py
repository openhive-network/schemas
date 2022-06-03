from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.custom_schemas.account_name import AccountName
from schemas.__private.custom_schemas.asset_vests import AssetVests
from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.custom_schemas.manabar import Manabar
from schemas.__private.fundamental_schemas import Int, Map

if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class RcAccountObject(CustomSchema):
    def _define_schema(self) -> Schema:
        return Map({
            'account': AccountName(),
            'rc_manabar': Manabar(),
            'max_rc_creation_adjustment': AssetVests(),
            'max_rc': Int(),
            'delegated_rc': Int(),
            'received_delegated_rc': Int(),
        })