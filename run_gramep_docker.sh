#!/bin/bash

SOURCE=~/Desktop/datasets/denv

docker run --rm \
    --mount type=bind,source="$SOURCE",target=/app \
    gramep:latest
