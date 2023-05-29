from __future__ import annotations

from enum import Enum


class TransactionStatus(Enum):
    STATE_1 = "expired_reversible"
    STATE_2 = "too_old"
    STATE_3 = "within_irreversible_block"
    STATE_4 = "within_mempool"
    STATE_5 = "within_reversible_block"
    STATE_6 = "unknown"

    @classmethod
    def list_values(cls) -> list[str]:
        return [c.value for c in cls]
