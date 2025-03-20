from __future__ import annotations

from enum import IntEnum
from typing import Final, Literal, NamedTuple, get_args

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.hex import Hex
from schemas.fields.hive_int import HiveInt
from schemas.operation import Operation
from schemas.operations import AnyEveryOperation

__all__ = ["FullRcStats", "RegularRcStats"]


operation_names: Final[list[str]] = [
    op.get_name_with_suffix() for op in get_args(AnyEveryOperation) if issubclass(op, Operation)
]
KnownOperationNames = Literal[tuple(operation_names)]  # type: ignore[valid-type]


class Rank(IntEnum):
    FREE = 0
    PLANKTON = 1
    REDFISH = 2
    MINNOW = 3
    DOLPHIN = 4
    ORCA = 5
    WHALE = 6
    LEVIATHAN = 7


class RcHiveIntTuple(NamedTuple):
    history_rc: HiveInt
    tokens_rc: HiveInt
    market_rc: HiveInt
    state_rc: HiveInt
    exec_rc: HiveInt


class BpHiveIntTuple(NamedTuple):
    history_bp: HiveInt
    tokens_bp: HiveInt
    market_bp: HiveInt
    state_bp: HiveInt
    exec_bp: HiveInt


class ResourceConsumptionHiveIntTuple(NamedTuple):
    history_bytes: HiveInt
    tokens: HiveInt
    market_bytes: HiveInt
    state_hbytes: HiveInt
    exec_ns: HiveInt


class RcOperationStatsBase(PreconfiguredBaseModel):
    count: HiveInt
    """amount of operations taken for calculations"""


class RegularRcOperationStats(RcOperationStatsBase):
    avg_cost: HiveInt
    """average cost of transaction with such operation (if just with one operation)"""


class FullRcOperationStats(RcOperationStatsBase):
    cost: RcHiveIntTuple
    """average cost of transaction (if just with one operation) grouped by type of resource"""
    usage: ResourceConsumptionHiveIntTuple
    """average usage of resources"""


class RcCantAffordItem(PreconfiguredBaseModel):
    vote: HiveInt
    """amount of users that no longer can afford vote_operation"""
    comment: HiveInt
    """amount of users that no longer can afford comment_operation"""
    transfer: HiveInt
    """amount of users that no longer can afford transfer_operation"""


class RegularRcPayerStats(PreconfiguredBaseModel):
    rank: Rank
    """rank of users grouped in this bucket (also known as RC wealth) identified by max rc

    B = billions;
    T = trillions = 1'000B;
    Q = quadrillions = 1'000T;


```
┌──────┬───────────┬─────────┬───────────┐
│ rank │ more than │ maximum │   alias   │
├──────┼───────────┼─────────┼───────────┤
│  0   │     -     │   10B   │   free    │
│  1   │    10B    │  100B   │ plankton  │
│  2   │   100B    │   1T    │  redfish  │
│  3   │    1T     │   10T   │  minnow   │
│  4   │    10T    │  100T   │  dolphin  │
│  5   │   100T    │   1Q    │   orca    │
│  6   │    1Q     │   10Q   │   whale   │
│  7   │    10Q    │    -    │ leviathan │
└──────┴───────────┴─────────┴───────────┘
```
    """
    count: HiveInt
    """number of transactions paid by users"""
    lt5: HiveInt
    """amount of users that had less than 5% of their mana after transaction"""
    lt10: HiveInt
    """amount of users that had less than 10% of their mana after transaction"""
    lt20: HiveInt
    """amount of users that had less than 20% of their mana after transaction"""
    cant_afford: RcCantAffordItem | None = None


class FullRcPayerStats(RegularRcPayerStats):
    cost: RcHiveIntTuple
    """total costs of resources by payers"""
    usage: ResourceConsumptionHiveIntTuple
    """average usage of resources by payers"""


# source: https://hive.blog/hive-139531/@andablackwidow/rc-stats-in-1-27
class RcStatsBase(PreconfiguredBaseModel):
    block: HiveInt
    """starting block of the day covered by the report"""
    regen: HiveInt
    """global RC regen at starting block"""
    budget: RcHiveIntTuple
    """block-budget for each resource"""
    pool: RcHiveIntTuple
    """content of each resource pool at starting block"""
    share: BpHiveIntTuple
    """resource popularity share at starting block"""
    vote: HiveInt
    """average cost of vote at starting block"""
    comment: HiveInt
    """average cost of comment at starting block"""
    transfer: HiveInt
    """average cost of transfer at starting block"""


class RegularRcStats(RcStatsBase):
    ops: dict[KnownOperationNames | str, RegularRcOperationStats]  # type: ignore[valid-type]
    """basic stats for each type of operation that was executed during reported day - number of operations executed and average cost"""
    payers: list[RegularRcPayerStats]
    """stats for users that paid for transactions during reported day, split between ranks 0..7 (levels of "RC wealth")"""


class FullRcStats(RcStatsBase):
    stamp: Hex
    """hash of state for rc status of the day"""
    ops: dict[KnownOperationNames | str, FullRcOperationStats]  # type: ignore[valid-type]
    """stats for each type of operation that was executed during reported day"""
    payers: list[FullRcPayerStats]
    """stats for users that paid for transactions during reported day, split between ranks 0..7 (levels of "RC wealth")"""
