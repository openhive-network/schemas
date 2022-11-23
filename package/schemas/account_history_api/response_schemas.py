from schemas.predefined import *


enum_virtual_ops = Map({
    'ops': Array(ApiOperationObject()),
    'ops_by_block': Array(
        Map({
            'block': Int(),
            'timestamp': Date(),
            'irreversible': Bool(),
            'ops': Array(ApiOperationObject()),
        })
    ),
    'next_block_range_begin': Int(),
    'next_operation_begin': Int(),
})

get_account_history = Map({
    'history': Array(
        ArrayStrict(
            Int(),
            ApiOperationObject(),
        )
    )
})


get_ops_in_block = Map({
    'ops': Array(ApiOperationObject())
})

get_transaction = Map({
    'block_num': Int(),
    'expiration': Date(),
    'extensions': Array(Any()),
    'operations': Array(
        Map({
            'type': Str(),
            'value': Map({}, allow_additional_properties=True),
        }),
    ),
    'ref_block_num': Int(),
    'ref_block_prefix': Int(),
    'signatures': Array(Signature()),
    'transaction_id': TransactionId(),
    'transaction_num': Int(),
})
