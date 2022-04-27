# Base docker file having defined environment for build and run of HAF instance.
# docker build --target=ci-base-image -t registry.gitlab.syncad.com/hive/hafah/ci-base-image:ubuntu20.04-xxx -f Dockerfile .

ARG CI_REGISTRY_IMAGE=registry.gitlab.syncad.com/hive/hafah
ARG CI_IMAGE_TAG=:ubuntu20.04-2

FROM python:3.8-alpine as ci-base-image

ENV LANG=en_US.UTF-8

RUN apk update && DEBIAN_FRONTEND=noniteractive apk add  \
  bash \
  joe \
  sudo \
  ca-certificates \
  wget \

SHELL ["/bin/bash", "-c"] 

FROM $CI_REGISTRY_IMAGE/ci-base-image$CI_IMAGE_TAG AS instance

ENV LANG=en_US.UTF-8

USER hafah_user
WORKDIR /home/hafah_user

SHELL ["/bin/bash", "-c"] 

ADD --chown=hafah_user:hafah_user . ./app
ADD --chown=hafah_user:hafah_user ./docker/docker_entrypoint.sh .

RUN sudo -n /home/hafah_user/app/docker/docker_build.sh /home/hafah_user ${USE_POSTGREST}

