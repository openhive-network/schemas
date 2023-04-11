from pydantic import Extra, BaseModel


class PreconfiguredBaseModel(BaseModel):
    class Config:
        extra = Extra.forbid
