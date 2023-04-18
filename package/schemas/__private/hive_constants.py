from __future__ import annotations

from typing import Final

"""
This file contains global constants closely related to the behavior of the blockchain, its configuration and specific
rules prevailing in the hive network. e.g.:
 - single block generation time,
 - maximum transaction/block size,
 - number of witnesses in the schedule.
"""
HIVE_100_PERCENT: Final[int] = 10000
HIVE_1_PERCENT: Final[int] = int(HIVE_100_PERCENT / 100)
HIVE_MAX_TRANSACTION_SIZE: Final[int] = 1024 * 64
HIVE_MIN_BLOCK_SIZE_LIMIT: Final[int] = HIVE_MAX_TRANSACTION_SIZE
MAXIMUM_BLOCK_SIZE: Final[int] = HIVE_MIN_BLOCK_SIZE_LIMIT * 2
HBD_INTEREST_RATE: Final[int] = 10 * HIVE_1_PERCENT
