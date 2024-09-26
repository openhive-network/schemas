from __future__ import annotations

from typing import Literal

from pydantic import Field

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import AccountName
from schemas.fields.hex import TransactionId
from schemas.fields.hive_datetime import HiveDateTime

__all__ = ["BlockStats", "KnownBlockStatsBlockType"]

KnownBlockStatsBlockType = Literal[
    "broken", "forked", "ignored", "gen", "p2p", "sync", "old", "pacemaker", "pacemaker-sync"
]


class BlockStatsBeforeItem(PreconfiguredBaseModel):
    inc: int
    """the number of transactions that came from API/P2P to the node between this block and the previous one"""
    ok: int
    """amount of the {inc} transactions that have been accepted (went to pending)"""
    auth: int
    """amount of the {inc} transactions that failed because of authorities"""
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
    """the number of pending transactions that missed the time limit and were moved to a new list without reapplication"""


class BlockStatsExecItem(PreconfiguredBaseModel):
    offset: int
    """the offset for sending the block creation request by the witness (in microseconds)"""
    pre: int
    """time between the offset and the actual start of block creation by the witness (in microseconds)"""
    work: int
    """actual processing time (in microseconds)"""
    post: int
    """time for everything that remains (inserting into fork_db, etc.) (in microseconds)"""
    all_: int = Field(alias="all")
    """the sum of the above (in microseconds)"""


class BlockStats(PreconfiguredBaseModel):
    num: int
    """block number"""
    lib: int
    """last irreversible block number"""
    type_: KnownBlockStatsBlockType = Field(alias="type")
    """block processing type"""
    id_: TransactionId = Field(alias="id")
    """block id"""
    ts: HiveDateTime
    """block timestamp"""
    bp: AccountName
    """block producer"""
    txs: int
    """number of transactions in the block"""
    size: int
    """block packed size"""
    offset: int
    """offset in microseconds of the completion of work on the block itself"""
    before: BlockStatsBeforeItem
    """statistics about transactions before processing block"""
    after: BlockStatsAfterItem
    """statistics about transactions after processing block"""
    exec_: BlockStatsExecItem = Field(alias="exec")
    """statistics about times during block processing"""
