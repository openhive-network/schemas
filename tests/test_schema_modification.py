from schemas.__private.modify.schema_expander import add_schema_to_array, add_schema_to_map
from schemas.predefined import *


def test_single_addition_to_outer_map():
    schema = Map({})
    add_schema_to_map(schema, key='number', schema=Int())

    assert schema == Map({'number': Int()})


def test_single_addition_to_inner_map():
    schema = Map({
        'inner_map': Map({})
    })
    add_schema_to_map(schema, path='inner_map', key='number', schema=Int())

    assert schema == Map({
        'inner_map': Map({
            'number': Int()
        })
    })


def test_single_addition_to_map_nested_in_different_types():
    schema = Array(
        ArrayStrict(
            Map({
                'values': AnyOf(
                    Str(),
                    Int(),
                    Map({})
                ),
                'name': AccountName(),
            })
        )
    )

    add_schema_to_map(schema, path='0.0.values.2', key='additional_key', schema=Int())

    assert schema == Array(
        ArrayStrict(
            Map({
                'values': AnyOf(
                    Str(),
                    Int(),
                    Map({
                        'additional_key': Int(),
                    })
                ),
                'name': AccountName(),
            })
        )
    )


def test_single_addition_to_outer_array():
    schema = Array(Str())
    add_schema_to_array(schema, schema=Int())

    assert schema == Array(Str(), Int())


def test_single_addition_with_index_to_outer_array():
    schema = ArrayStrict(Str(), AccountName(), Hex())
    add_schema_to_array(schema, index=2, schema=Int())

    assert schema == ArrayStrict(Str(), AccountName(), Int(), Hex())


def test_single_addition_to_inner_array():
    schema = Array(
        Array(Str())
    )
    add_schema_to_array(schema, path='0', schema=Int())

    assert schema == Array(
        Array(Str(), Int())
    )


def test_single_addition_to_array_nested_in_different_types():
    schema = Array(
        ArrayStrict(
            Map({
                'values': AnyOf(
                    Str(),
                    Int(),
                    Array(Str())
                ),
                'name': AccountName(),
            })
        )
    )

    add_schema_to_array(schema, path='0.0.values.2', schema=Int())

    assert schema == Array(
        ArrayStrict(
            Map({
                'values': AnyOf(
                    Str(),
                    Int(),
                    Array(Str(), Int())
                ),
                'name': AccountName(),
            })
        )
    )

