from schemas.predefined import *

get_methods = Array(Str())

def select_this_one(request) -> bool:
    return isinstance(request.params['1'], int)

#TODO schema switch , conditional schema
get_signature = SuperWrapper([
    [
        select_this_one,
        Map({
            'args': AnyOf(
                Array(),
                Map({}, allow_additional_properties=True),
            ),
            'ret': Map({}, allow_additional_properties=True)
        },
    ],
    [
        select_this_one,
        Map({
            'args': AnyOf(
                Array(),
                Map({}, allow_additional_properties=True),
            ),
            'ret': Map({}, allow_additional_properties=True)
        },
    ],
    [
        select_this_one,
        Map({
            'args': AnyOf(
                Array(),
                Map({}, allow_additional_properties=True),
            ),
            'ret': Map({}, allow_additional_properties=True)
        },
    ],
)
