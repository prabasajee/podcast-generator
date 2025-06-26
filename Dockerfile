FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/* \
    && pip3 install PyYAML

COPY feed.py /usr/bin/feed.py

COPY encryption.sh /encryption.sh

ENTRYPOINT ["/encryption.sh"]