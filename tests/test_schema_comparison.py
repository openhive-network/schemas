from schemas.predefined import *


def test_same_simple_ints_comparison():
    assert Int() == Int()


def test_ints_with_and_without_options():
    assert Int() != Int(minimum=0)


def test_same_maps_comparison():
    first = second = Map({
        'id': Int(),
        'name': AccountName(),
        'owner': Authority(),
    })

    assert first == second


def test_maps_with_different_children_schemas_comparison():
    first = Map({
        'id': Int(),
        'name': AccountName(),
        'owner': Authority(),
    })

    second = Map({
        'id': Int(maximum=5),
        'name': AccountName(),
        'owner': Authority(),
    })

    assert first != second


def test_maps_with_different_keys_comparison():
    first = Map({
        'id': Int(),
        'name': AccountName(),
        'owner': Authority(),
    })

    second = Map({
        'modified_id': Int(),  # Here key is changed
        'name': AccountName(),
        'owner': Authority(),
    })

    assert first != second
