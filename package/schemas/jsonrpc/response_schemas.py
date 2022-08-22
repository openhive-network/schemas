from schemas.get_schema import use_optional_schema

from schemas.predefined import *

get_methods = Array(Str())

# TODO schema switch , conditional schema
get_signature = use_optional_schema([
    [
        'condenser_api',
        Map({
            'args': AnyOf(
                Array(),
                Map({}, allow_additional_properties=True),
            ),
            'ret': Map({}, allow_additional_properties=True),
        }),
    ],
    [
        'database_api',
        Map({
            'args': AnyOf(
                Array(),
                Map({}, allow_additional_properties=True),
            ),
            'ret': Map({}, allow_additional_properties=True),
        }),
    ],
    [
        'account_history_api',
        Map({
            'args': AnyOf(
                Array(),
                Map({}, allow_additional_properties=True),
            ),
            'ret': Map({}, allow_additional_properties=True)
        }),
    ],
])
