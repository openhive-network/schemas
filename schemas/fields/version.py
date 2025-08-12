from __future__ import annotations

from typing import Annotated

import msgspec

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import NodeType
from schemas.fields.hex import Revision, Sha256

__all__ = [
    "HardforkVersion",
    "HiveVersion",
    "Version",
]


Version = Annotated[str, msgspec.Meta(pattern=r"^\d+\.\d+\.\d+$")]

HardforkVersion = Version


class HiveVersionFromExecutable(PreconfiguredBaseModel):
    blockchain_version: HardforkVersion
    hive_revision: Revision
    fc_revision: Revision
    node_type: NodeType
    haf_revision: Revision | None = None


class HiveVersion(PreconfiguredBaseModel):
    chain_id: Sha256
    blockchain_version: HardforkVersion
    hive_revision: Revision
    fc_revision: Revision
    node_type: NodeType
    haf_revision: Revision | None = None
