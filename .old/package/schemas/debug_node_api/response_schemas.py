from schemas.predefined import *

debug_get_hardfork_property_object = Map({
    'id': Int(),
    'processed_hardforks': Array(Date()),
    'last_hardfork': Int(),
    'current_hardfork_version': HardforkVersion(),
    'next_hardfork': HardforkVersion(),
    'next_hardfork_time': Date()
})

debug_get_witness_schedule = Map({
    'id': Int(),
    'current_virtual_time': Int(),
    'next_shuffle_block_num': Int(),
    'current_shuffled_witnesses': Array(AnyOf(AccountName(), Str(pattern=''))),
    'num_scheduled_witnesses': Int(),
    'elected_weight': Int(),
    'timeshare_weight': Int(),
    'miner_weight': Int(),
    'witness_pay_normalization_factor': Int(),
    'median_props': Map({
        'account_creation_fee': AssetHive(),
        'maximum_block_size': Int(),
        'hbd_interest_rate': Int(),
        'account_subsidy_budget': Int(),
        'account_subsidy_decay': Int(),
    }),
    'majority_version': HardforkVersion(),
    'max_voted_witnesses': Int(),
    'max_miner_witnesses': Int(),
    'max_runner_witnesses': Int(),
    'hardfork_required_witnesses': Int(),
    'account_subsidy_rd': RdDynamicParams(),
    'account_subsidy_witness_rd': RdDynamicParams(),
    'min_witness_account_subsidy_decay': Int(),
})

debug_get_head_block = Map({
    'block': Map({
        'previous': TransactionId(),
        'timestamp': Date(),
        'witness': AccountName(),
        'transaction_merkle_root': Str(),
        'extensions': Array(Any()),
        'witness_signature': Signature(),
        'transactions': Array(
            Map({
                'ref_block_num': Int(),
                'ref_block_prefix': Int(),
                'expiration': Date(),
                'operations': Array(
                    Map({
                        'type': Str(),
                        'value': Map({}, allow_additional_properties=True)
                    })
                ),
                'extensions': Array(Any()),
                'signatures': Array(Signature())
            })
        )
    })
})

debug_has_hardfork = Map({
    'has_hardfork': Bool(),
})

debug_set_hardfork = Map({})

debug_push_blocks = Map({'blocks': Int()})

debug_get_json_schema = Map({'schema': Str()})

debug_generate_blocks_until = Map({'blocks': Int()})

debug_generate_blocks = Map({'blocks': Int()})
