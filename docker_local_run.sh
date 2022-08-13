#!/bin/bash

# vscode使わない限り0.0.0.0と指定しないと、ネットワークの外から見えない。
tmpfile=$(mktemp)
cp ./.devcontainer/.env $tmpfile
sed -i 's/BIND=127.0.0.1/BIND=0.0.0.0/' $tmpfile

docker run --rm -it  \
    -p 8080:8080/tcp \
    --env-file=$tmpfile \
    cloudfastapi:latest

