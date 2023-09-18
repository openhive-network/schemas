from __future__ import annotations

from typing import Literal

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import HiveInt


class FindTransaction(PreconfiguredBaseModel):
    block_num: HiveInt | None
    rc_cost: HiveInt | None
    status: Literal[
        "unknown",
        "within_mempool",
        "within_reversible_block",
        "within_irreversible_block",
        "expired_reversible",
        "expired_irreversible",
        "too_old",
    ]
