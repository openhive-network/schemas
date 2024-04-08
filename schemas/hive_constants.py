"""
This file contains global constants closely related to the behavior of the blockchain, its configuration and specific
rules prevailing in the hive network. e.g.:
 - single block generation time,
 - maximum transaction/block size,
 - number of witnesses in the schedule.
"""
from __future__ import annotations

from typing import Final

HIVE_TIME_FORMAT: Final[str] = "%Y-%m-%dT%H:%M:%S"
HIVE_100_PERCENT: Final[int] = 10000
HIVE_1_PERCENT: Final[int] = int(HIVE_100_PERCENT / 100)
HIVE_MAX_TRANSACTION_SIZE: Final[int] = 1024 * 64
HIVE_MIN_BLOCK_SIZE: Final[int] = HIVE_MAX_TRANSACTION_SIZE
HIVE_MAX_BLOCK_SIZE: Final[int] = HIVE_MIN_BLOCK_SIZE * 2
HIVE_HBD_INTEREST_RATE: Final[int] = 10 * HIVE_1_PERCENT
HIVE_MAX_WITNESS_URL_LENGTH: Final[int] = 2048
