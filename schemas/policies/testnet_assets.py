from __future__ import annotations

from dataclasses import dataclass

from schemas.policies.policy import Policy


@dataclass
class TestnetAssets(Policy):
    use_testnet_assets: bool

    def apply(self) -> None:
        from schemas.fields.assets.asset_info import AssetInfo

        AssetInfo.AssetConfig.testnet_asset = self.use_testnet_assets
