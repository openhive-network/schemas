from schemas.predefined import *

get_methods = Array(Str())

get_signature = Map({
    'args': Any(),
    'ret': Any(),
})
