#! /bin/bash

REGISTRY="registry.gitlab.syncad.com/hive/schemas"
BASE_IMAGE="ubuntu22.04"
VERSION="1"

URL="${REGISTRY}/ci-base-image:${BASE_IMAGE}-${VERSION}"

docker build -t "${URL}" -f Dockerfile.CI .
