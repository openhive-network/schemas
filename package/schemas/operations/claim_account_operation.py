from pydantic import conint

from schemas.package.schemas.predefined import AccountName, AssetHive, LegacyAssetHive
from preconfigure_base_model import PreconfiguredBaseModel
"""
If a user wants to pay a fee in RC fee should be equal 0.
"""


class ClaimAccountOperation(PreconfiguredBaseModel):
    creator: AccountName
    fee: AssetHive | LegacyAssetHive | conint(ge=0, le=0)  # conint equal 0 add to enable user pay in RC
