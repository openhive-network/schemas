from pydantic import BaseModel, Extra, conint

from schemas.predefined import AccountName, AssetHive, LegacyAssetHive
"""
If a user wants to pay a fee in RC fee should be equal 0. 
"""


class ClaimAccountOperation(BaseModel, extra=Extra.forbid):
    creator: AccountName
    fee: AssetHive | LegacyAssetHive | conint(ge=0, le=0)  # conint equal 0 add to enable user pay in RC
