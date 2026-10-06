from __future__ import annotations

from schemas.policies.disable_swap_types import DisableSwapTypesPolicy
from schemas.policies.extra_fields import ExtraFieldsPolicy
from schemas.policies.policy import Policy, set_policies
from schemas.policies.testnet_assets import TestnetAssetsPolicy

__all__ = [
    "set_policies",
    "Policy",
    # PREDEFINED POLICIES
    "TestnetAssetsPolicy",
    "DisableSwapTypesPolicy",
    "ExtraFieldsPolicy",
]
