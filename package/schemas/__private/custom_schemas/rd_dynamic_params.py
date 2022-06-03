from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.fundamental_schemas import Int, Map

if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class RdDynamicParams(CustomSchema):
    def _define_schema(self) -> Schema:
        return Map({
            'resource_unit': Int(),
            'budget_per_time_unit': Int(),
            'pool_eq': Int(),
            'max_pool_size': Int(),
            'decay_params': Map({
                'decay_per_time_unit': Int(),
                'decay_per_time_unit_denom_shift': Int()
            }),
            'min_decay': Int(),
        })
