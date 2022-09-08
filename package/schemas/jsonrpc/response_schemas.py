from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.schema_selector import SchemaSelector
from schemas.predefined import *

if TYPE_CHECKING:
    from schemas.get_schema import Request


get_methods = Array(Str())

<<<<<<< HEAD
get_signature = Map({
<<<<<<< HEAD
    'args': Any(),
    'ret': Any(),
=======
    'args': AnyOf(
        Array(),
        Map({}, allow_additional_properties=True),
        Null(),
=======

def __get_api_name(request: Request) -> str:
    return request.params['method'].split('.')[0]


get_signature = SchemaSelector([
    (
        lambda request: __get_api_name(request) == 'condenser_api',
        Map({
            'args': AnyOf(
                Map({}, allow_additional_properties=True),
                Array(Any()),
            ),
            'ret': AnyOf(
                Array(),
                Map({}, allow_additional_properties=True),
                Int(),
                Null(),
                Str(),
                Bool(),
            )
        }),
>>>>>>> 9e11c31 (Adjust schema `jsonrpc` to SchemaSelector)
    ),
    (
        lambda request: __get_api_name(request) == 'database_api',
        Map({
            'args': AnyOf(
                Map({}, allow_additional_properties=True),
                Null(),
            ),
            'ret': AnyOf(
                Map({}, allow_additional_properties=True),
                Null(),
                Array(Any()),
            )
        }),
    ),
<<<<<<< HEAD
>>>>>>> 2a73928 (Add schemas to `jsonrpc` API)
})
=======
    (
        lambda request: __get_api_name(request) == 'account_by_key_api',
        Map({
            'args': Map({}, allow_additional_properties=True),
            'ret': AnyOf(
                Map({}, allow_additional_properties=True),
            )
        }),
    ),
    (
        lambda request: __get_api_name(request) == 'wallet_bridge_api',
        Map({
            'args': AnyOf(
                Map({}, allow_additional_properties=True),
                Null(),
            ),
            'ret': AnyOf(
                Map({}, allow_additional_properties=True),
                Array(Any()),
                Null(),
                Bool(),
                HardforkVersion(),
            )
        }),
    ),
    (
        lambda request: __get_api_name(request) == 'account_history_api',
        Map({
            'args': AnyOf(
                Map({}, allow_additional_properties=True),
                Null(),
            ),
            'ret': AnyOf(
                Map({}, allow_additional_properties=True),
                Array(Any()),
                Null(),
                Bool(),
            )
        }),
    ),
    (
        lambda call:
            call == 'block_api' or
            call == 'debug_node_api' or
            call == 'chain_api' or
            call == 'jsonrpc' or
            call == 'market_history_api' or
            call == 'network_broadcast_api' or
            call == 'rc_api' or
            call == 'reputation_api' or
            call == 'rewards_api' or
            call == 'transaction_status_api' or
            call == 'witness_api' or
            call == 'network_node_api',
        Map({
            'args': AnyOf(
                Map({}, allow_additional_properties=True),
                Null(),
            ),
            'ret': AnyOf(
                Map({}, allow_additional_properties=True),
                Array(Any()),
                Null(),
                Bool(),
            )
        }),
    ),
])
>>>>>>> 9e11c31 (Adjust schema `jsonrpc` to SchemaSelector)
