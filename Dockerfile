FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-yaml \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY feed.py /usr/bin/feed.py

COPY encryption.sh /encryption.sh

ENTRYPOINT ["/encryption.sh"]