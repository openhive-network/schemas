"""
This file contains global constants closely related to the behavior of the blockchain, its configuration and specific
rules prevailing in the hive network, used by the field types. e.g.:
 - the format of time,
 - the maximum length of a witness URL.
"""

from __future__ import annotations

from typing import Final

HIVE_TIME_FORMAT: Final[str] = "%Y-%m-%dT%H:%M:%S"
HIVE_MAX_WITNESS_URL_LENGTH: Final[int] = 2048
