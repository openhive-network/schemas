from __future__ import annotations

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.validation import HardforkVersion, NodeType, Revision

__all__ = [
    "HiveVersionFromExecutable",
]


class HiveVersionFromExecutable(PreconfiguredBaseModel):
    """Version of hived given by its executable (`hived --version`) - strings checked by the forms of validation."""

    blockchain_version: HardforkVersion
    hive_revision: Revision
    fc_revision: Revision
    node_type: NodeType
    haf_revision: Revision | None = None
