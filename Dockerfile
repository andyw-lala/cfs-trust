# Dockerfile for CFS Trust
# Copyright 2019-2021 Hewlett Packard Enterprise Development LP

FROM arti.dev.cray.com/baseos-docker-master-local/alpine:3.12.4 as service
WORKDIR /app
RUN mkdir /app/src
COPY /src/ /app/src
COPY /src/cfsssh/cloudinit/ /app/src/cloudinit
COPY setup.py README.md .version /app/
ADD constraints.txt requirements.txt /app/
RUN apk add --no-cache linux-headers gcc g++ python3-dev py3-pip musl-dev libffi-dev openssl-dev git jq curl openssh-client nginx && \
    python3 -m pip install --upgrade pip && \
    pip3 install --no-cache-dir -U pip && \
    pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --no-cache-dir . && \
    rm -rf /app/*
ENTRYPOINT [ "python3", "-m", "cfsssh.setup.service" ]
