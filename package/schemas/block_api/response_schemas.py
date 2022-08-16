from schemas.predefined import *

get_block = AnyOf(
    Map({}),
    Map({
        'block': Map({
            'block_id': TransactionId(),
            'previous': TransactionId(),
            'extensions': Any(),
            'signing_key': PublicKey(),
            'timestamp': Date(),
            'transaction_ids': Array(TransactionId()),
            'transactions': Any(),
            'transaction_merkle_root': TransactionId(),
            'witness': AccountName(),
            'witness_signature': Signature(),
        })

    })
)

get_block_header = AnyOf(
    Map({}),
    Map({
        'header': Map({
            'extensions': Array(),
            'previous': TransactionId(),
            'timestamp': Date(),
            'transaction_merkle_root': TransactionId(),
            'witness': AccountName(),
        })
    })
)

get_block_range = Map({
    'blocks': Array(
        Map({
            'block_id': TransactionId(),
            'extensions': Array(),
            'previous': TransactionId(),
            'signing_key': PublicKey(),
            'timestamp': Date(),
            'transaction_ids': Array(TransactionId()),
            'transaction_merkle_root': TransactionId(),
            'transactions': Array(),
            'witness': AccountName(),
            'witness_signature': Signature(),
        })
    )
})
