from __future__ import annotations

from typing import Final, Literal, get_args

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.hex import Hex
from schemas.fields.hive_int import HiveInt
from schemas.operation import Operation
from schemas.operations import AnyEveryOperation

RcHiveIntTuple = tuple[HiveInt, HiveInt, HiveInt, HiveInt, HiveInt]
operation_names: Final[list[str]] = [
    x.get_name_with_suffix() for x in get_args(AnyEveryOperation) if issubclass(x, Operation)
]
KnownOperationNames = Literal[tuple(operation_names)]  # type: ignore[valid-type]

__all__ = ["FullRcStats", "RegularRcStats"]


class RcOperationStatsBase(PreconfiguredBaseModel):
    count: HiveInt
    """amount of operations taken for calculations"""


class RegularRcOperationStats(RcOperationStatsBase):
    avg_cost: HiveInt
    """average cost of transaction with such operation (if just with one operation)"""


class FullRcOperationStats(RcOperationStatsBase):
    cost: RcHiveIntTuple
    """average cost of transaction (if just with one operation) grouped by ???"""
    usage: RcHiveIntTuple
    """average usage of rc at ??? grouped by ???"""


class RcCantAffordItem(PreconfiguredBaseModel):
    vote: HiveInt
    """amount of users that no longer can afford vote_operation"""
    comment: HiveInt
    """amount of users that no longer can afford comment_operation"""
    transfer: HiveInt
    """amount of users that no longer can afford transfer_operation"""


class RegularRcPayerStats(PreconfiguredBaseModel):
    rank: HiveInt
    """rank of users grouped in this bucket (also known as RC wealth)

    AMR = account max rc

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
    """average cost of ??? at ??? grouped by ???"""
    usage: RcHiveIntTuple
    """average usage of rc at ??? grouped by ???"""


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
    share: RcHiveIntTuple
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
