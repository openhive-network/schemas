from schemas.__private.modify.schema_expander import add_schema_to_array, add_schema_to_map
from schemas.__private.modify.schema_reducer import remove_schema_from_map, remove_schema_from_array
from schemas.predefined import *


def test_single_addition_to_outer_map():
    schema = Map({})
    add_schema_to_map(schema, key='number', schema=Int())

    assert schema == Map({'number': Int()})


def test_single_addition_to_proposal():
    schema = Proposal()
    add_schema_to_map(schema, key='number', schema=Int())

    assert schema == Map({
            'id': Int(),
            'proposal_id': Int(),
            'creator': Str(),
            'receiver': Str(),
            'start_date': Date(),
            'end_date': Date(),
            'daily_pay': AssetHbd(),
            'subject': Str(),
            'permlink': Str(),
            'total_votes': Int(),
            'status': Str(),
            'number': Int(),
        })


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


def test_single_deletion_in_outer_map():
    schema = Map({'number': Int()})
    remove_schema_from_map(schema, path='number')
    assert schema == Map({})


def test_single_deletion_in_proposal():
    schema = Proposal()
    remove_schema_from_map(schema, path='status')

    assert schema == Map({
            'id': Int(),
            'proposal_id': Int(),
            'creator': Str(),
            'receiver': Str(),
            'start_date': Date(),
            'end_date': Date(),
            'daily_pay': AssetHbd(),
            'subject': Str(),
            'permlink': Str(),
            'total_votes': Int(),
        })


def test_single_deletion_in_inner_map():
    schema = Map({
        'inner_map': Map({
            'id': Int()
        })
    })
    remove_schema_from_map(schema, path='inner_map.id')

    assert schema == Map({
        'inner_map': Map({})
    })


def test_single_deletion_in_map_nested_in_different_types():
    schema = Array(
        ArrayStrict(
            Map({
                'values': AnyOf(
                    Str(),
                    Int(),
                    Map({
                        'key_to_delete': Str(),
                    })
                ),
                'name': AccountName(),
            })
        )
    )

    remove_schema_from_map(schema, path='0.0.values.2.key_to_delete')

    assert schema == Array(
        ArrayStrict(
            Map({
                'values': AnyOf(
                    Str(),
                    Int(),
                    Map({
                    })
                ),
                'name': AccountName(),
            })
        )
    )


def test_single_deletion_in_outer_array():
    schema = Array(Int(), Str())
    remove_schema_from_array(schema, path='1')
    assert schema == Array(Int())


def test_single_deletion_in_inner_array():
    schema = Array(
        Array(
            Hex(), Str(), Int(),
        ))
    remove_schema_from_array(schema, path='0.2')
    assert schema == Array(
        Array(
            Hex(), Str(),
        )
    )

