from __future__ import annotations

import re

from pydantic import ConstrainedStr

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import NodeType
from schemas.fields.hex import Sha256, TransactionId

__all__ = [
    "HardforkVersion",
    "HiveVersion",
    "Version",
]


class Version(ConstrainedStr):
    regex = re.compile(r"^\d+\.\d+\.\d+$")


HardforkVersion = Version


class HiveVersion(PreconfiguredBaseModel):
    blockchain_version: HardforkVersion
    hive_revision: TransactionId
    fc_revision: TransactionId
    node_type: NodeType
    chain_id: Sha256 | None = None
