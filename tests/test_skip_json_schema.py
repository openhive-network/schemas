from typing import Any, Generic, TypeVar
from msgspec import Struct, json
from msgspec import inspect as mi
import msgspec
from typing_extensions import Annotated
from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.hive_int import HiveInt
from schemas.decoders import SkipJsonModel, dec_hook_hf26, schema_hook


class HiveIntModel(PreconfiguredBaseModel):
    field: int


# --- Przykładowy model ---
class MyModel(PreconfiguredBaseModel):
    a: SkipJsonModel[list[HiveIntModel]]
    b: int

# --- Użycie ---
def test_skip():
    data = {"a": [{"field": 123}, {"field": 456}, {"field": 789}], "b": 42}
    # data = {"a": {"field": 123}, "b": 42}

    schema = json.schema(MyModel, schema_hook=schema_hook)

    decoded = msgspec.convert(obj=data, type=MyModel, dec_hook=dec_hook_hf26)

    pass