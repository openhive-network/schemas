## Moved to hiveio-api

The field types of Hive data and the validation of this package are now part of the `hiveio-api` package, generated in
the [hive repository](https://gitlab.syncad.com/hive/hive) (`libraries/plugins/apis/api_generation/python_api_package`,
hand-written modules in `hiveio_api_template/`). See hive/schemas#55. `hiveio-schemas` is no longer developed - its last
release stays available.

| `hiveio-schemas` | `hiveio-api` |
|---|---|
| `schemas.Asset`, `schemas.HiveDateTime`, `schemas.AssetInfo`, `schemas.HIVE_ASSET`, ... | `hiveio_api.Asset`, `hiveio_api.HiveDateTime`, `hiveio_api.AssetInfo`, `hiveio_api.HIVE_ASSET`, ... |
| `schemas.fields.public` | `hiveio_api.fields.public` |
| `schemas.fields.user_friendly` | `hiveio_api.fields.user_friendly` |
| `schemas.fields.validation` | `hiveio_api.fields.validation` |
| `schemas.fields.hive_datetime`, `json_string`, `serializable`, `version` | `hiveio_api.fields.hive_datetime`, `json_string`, `serializable`, `version` |
| `schemas.hive_constants` | `hiveio_api.fields.hive_constants` |
| `schemas.validation` | `hiveio_api.validation` |
| `schemas.errors` | `hiveio_api.validation.errors` |
| `schemas._preconfigured_base_model` (`PreconfiguredBaseModel`) | `hiveio_api.validation.model` |
| `schemas.decoders`, `schemas.encoders` | `hiveio_api.validation.decoders`, `hiveio_api.validation.encoders` |
| `schemas.base` (`field`, `Meta`) | `msgspec` |

Models of API responses, operations and transactions (formerly `schemas.apis`, `schemas.operations`,
`schemas.transaction`) are generated in `hiveio_api` as well (`hiveio_api.<api>`, `hiveio_api.operations`).
