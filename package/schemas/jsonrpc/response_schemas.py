from schemas.predefined import *

get_methods = Array(Str())

get_signature = Map({
    'args': AnyOf(
        Array(),
        Map({}, allow_additional_properties=True),
    ),
    'ret': Map({}, allow_additional_properties=True)
})
