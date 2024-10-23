from __future__ import annotations

from typing import Literal

from pydantic import Field

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.app_status_api.block_stats import BlockStats
from schemas.apis.app_status_api.rc_stats import FullRcStats, RegularRcStats
from schemas.fields.hex import TransactionId
from schemas.fields.hive_datetime import HiveDateTime

KnownStatuses = Literal[
    "signals attached",
    "interrupted",
    "syncing",
    "syncing",
    "entering live mode",
    "finished syncing",
    "replaying",
    "finished replaying",
    "exiting with open database error",
    "P2P stopped",
    "P2P started",
    "loading snapshot",
    "finished loading snapshot",
    "dumping snapshot",
    "finished dumping snapshot",
    "beekeeper is starting",
    "beekeeper is ready",
    "opening beekeeper failed. Beekeeper API is disabled",
    "chain API ready",
]


class BaseStatusItem(PreconfiguredBaseModel):
    timestamp: HiveDateTime


class StatusItem(BaseStatusItem):
    status: KnownStatuses | str

    def __eq__(self, value: object) -> bool:
        if isinstance(value, str):
            return value == self.status
        return super().__eq__(value)


class WebserverItem(BaseStatusItem):
    address: str
    port: int


class ForkItem(PreconfiguredBaseModel):
    new_head_block_num: int
    new_head_block_id: TransactionId


class HivedBenchmark(PreconfiguredBaseModel):
    n: int
    """current block number"""
    rt: int
    """measured real time (in microseconds)"""
    ct: int
    """measured cpu time (in microseconds)"""
    cm: int
    """measured consumed memory"""
    pm: int
    """measured peak in consumed memory"""


class RcStatsItem(PreconfiguredBaseModel):
    rc_stats: RegularRcStats | FullRcStats


class BlockStatsItem(PreconfiguredBaseModel):
    block_stats: BlockStats


class HivedBenchmarkItem(PreconfiguredBaseModel):
    multiindex_stats: HivedBenchmark


class KnownRecords(PreconfiguredBaseModel):
    rc_stats: RcStatsItem | None = None
    hived_benchmark: HivedBenchmarkItem | None = None
    block_stats: BlockStatsItem | None = None


class KnownWebservers(PreconfiguredBaseModel):
    WS: WebserverItem | None = None
    HTTP: WebserverItem | None = None
    P2P: WebserverItem | None = None
