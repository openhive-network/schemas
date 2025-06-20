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


class HiveVersionFromExecutable(PreconfiguredBaseModel):
    blockchain_version: HardforkVersion
    hive_revision: TransactionId
    fc_revision: TransactionId
    node_type: NodeType
    haf_revision: TransactionId | None = None


class HiveVersion(HiveVersionFromExecutable):
    chain_id: Sha256
