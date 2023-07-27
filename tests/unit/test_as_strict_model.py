from __future__ import annotations

from typing import Any, Final

import pytest
from pydantic import ValidationError

from schemas.preconfigured_base_model import PreconfiguredBaseModel


class Model(PreconfiguredBaseModel):
    foo: int = 1


ModelStrict = Model.as_strict_model()


def test_if_field_is_required() -> None:
    # ARRANGE
    expected_message: Final[str] = "field required"

    # ACT
    with pytest.raises(ValidationError) as error:
        ModelStrict()

    # ASSERT
    assert expected_message in str(error.value)


def test_strict_model_creation() -> None:
    # ARRANGE
    new_value: Final[int] = 2

    # ACT
    instance = ModelStrict(foo=new_value)

    # ASSERT
    assert instance.foo == new_value


class ParentModel(PreconfiguredBaseModel):
    bar: Model = Model()
    baz: int = 3


@pytest.mark.parametrize("is_child_given", [True, False], ids=["child given", "child not given"])
def test_if_all_fields_in_nested_structure_are_required(is_child_given: bool) -> None:
    # ARRANGE
    data_to_unpack: dict[Any, Any] = {"bar": {}} if is_child_given else {}
    expected_message = "field required"
    number_of_occurrences = 2  # 2 fields - 'foo' and 'bar' or 'bar' and 'baz'

    ParentModelStrict = ParentModel.as_strict_model()  # noqa: N806

    # ACT
    with pytest.raises(ValidationError) as error:
        ParentModelStrict(**data_to_unpack)

    # ASSERT
    assert str(error.value).count(expected_message) == number_of_occurrences
    if is_child_given:
        assert "foo" in str(error.value)
