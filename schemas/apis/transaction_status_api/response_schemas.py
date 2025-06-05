from __future__ import annotations

from typing import Literal

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.hive_int import HiveInt


class FindTransaction(PreconfiguredBaseModel, kw_only=True):
    block_num: HiveInt | None = None
    rc_cost: HiveInt | None = None
    status: Literal[
        "unknown",
        "within_mempool",
        "within_reversible_block",
        "within_irreversible_block",
        "expired_reversible",
        "expired_irreversible",
        "too_old",
    ]
