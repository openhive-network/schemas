from __future__ import annotations

from typing import Literal

from msgspec import field

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import AccountName
from schemas.fields.hex import BlockId
from schemas.fields.hive_datetime import HiveDateTime

__all__ = ["BlockStats", "KnownBlockStatsBlockType"]

KnownBlockStatsBlockType = Literal[
    "broken",
    "forked",
    "ignored",
    "gen",
    "p2p",
    "sync",
    "old",
    "pacemaker",
    "pacemaker-sync",
    "debug",
    "queen",
    "pacemaker",
]


class BlockStatsBeforeItem(PreconfiguredBaseModel):
    inc: int
    """the number of transactions that came from API/P2P to the node between this block and the previous one"""
    ok: int
    """amount of the {inc} transactions that have been accepted (went to pending)"""
    auth: int
    """amount of the {inc} transactions that failed authorization check"""
    rc: int
    """amount of the {inc} transactions that failed because of rc costs"""


class BlockStatsAfterItem(PreconfiguredBaseModel):
    exp: int
    """the number of pending transactions that have expired"""
    fail: int
    """the number of pending transactions that are no longer valid"""
    appl: int
    """the number of pending transactions successfully reapplied after block processing"""
    post: int
    """
    the number of pending transactions that did not fit the time
    limit and were postponed to next block processing without reapplication
    """
    drop: int
    """
    the number of transactions that would otherwise become postponed that were
    dropped from pending due to exceeded mempool size limit
    """
    size: int
    """size of mempool in bytes left after handling all pending transactions"""


class BlockStatsExecItem(PreconfiguredBaseModel):
    offset: int
    """
    the offset from block timestamp (block handling) to moment of
    adding block to processing queue (in microseconds)

    #### Note
        in some cases such offset makes no sense (f.e. sync blocks) in which case it is set to artificial value (usually zero)
    """
    pre: int
    """time it took block handling request to wait in queue before it was picked up for processing (in microseconds)"""
    work: int
    """
    Time of main work on the block before it was accepted and passed for broadcast (in microseconds)

    #### Note
        Because of above main work depends on `type` of block processing, f.e.:
            - for `gen` it is creation of the block
            - for `p2p` it is application of transactions contained in block
    """
    post: int
    """Time (in microseconds) for all remaining work after block was passed for broadcast, including reapplication of pending transactions"""
    all_: int = field(name="all")
    """the sum of the above (in microseconds)"""


class BlockStats(PreconfiguredBaseModel):
    num: int
    """block number"""
    lib: int
    """last irreversible block number"""
    type_: KnownBlockStatsBlockType = field(name="type")
    """block processing type"""
    id_: BlockId = field(name="id")
    """block id"""
    ts: HiveDateTime
    """block timestamp"""
    bp: AccountName
    """block producer"""
    txs: int
    """number of transactions in the block"""
    size: int
    """block packed (uncompressed binary stream) size"""
    offset: int
    """
    Offset from block timestamp (in microseconds) of the completion of main work on the block and passing it for further broadcast

    #### Note
        Because of above main work depends on `type` of block processing
    """
    before: BlockStatsBeforeItem
    """statistics about transactions before processing block"""
    after: BlockStatsAfterItem
    """statistics about transactions after processing block"""
    exec_: BlockStatsExecItem = field(name="exec")
    """statistics about times during block processing"""
