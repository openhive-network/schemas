from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_schemas import Uint16t, Uint32t

HIVE_100_PERCENT: Final[int] = 10000
HIVE_1_PERCENT: Final[int] = int(HIVE_100_PERCENT / 100)
HIVE_MAX_TRANSACTION_SIZE: Final[int] = 1024 * 64
HIVE_MIN_BLOCK_SIZE_LIMIT: Final[int] = HIVE_MAX_TRANSACTION_SIZE
MAXIMUM_BLOCK_SIZE: Final[Uint32t] = Uint32t(HIVE_MIN_BLOCK_SIZE_LIMIT * 2)
HBD_INTEREST_RATE: Final[Uint16t] = Uint16t(10 * HIVE_1_PERCENT)
