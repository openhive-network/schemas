from __future__ import annotations

from schemas.policies.disable_swap_types import DisableSwapTypes
from schemas.policies.extra_fields import ExtraFieldsPolicy
from schemas.policies.missing_fields_in_get_config import MissingFieldsInGetConfig
from schemas.policies.policy import Policy, set_policies
from schemas.policies.testnet_assets import TestnetAssets

__all__ = [
    "set_policies",
    "Policy",
    # PREDEFINED POLICIES
    "MissingFieldsInGetConfig",
    "TestnetAssets",
    "DisableSwapTypes",
    "ExtraFieldsPolicy",
]
