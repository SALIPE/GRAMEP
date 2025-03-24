FROM alpine:latest

WORKDIR /usr/src/app

RUN apk add --no-cache \
    python3 \
    py3-pip \
    build-base \
    python3-dev \
    libffi-dev \
    openssl-dev \
    curl

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

RUN rustc --version && cargo --version

RUN python3 -m venv /usr/src/app/.venv

# Ensure we're using the virtual environment's pip and Python
ENV PATH="/usr/src/app/.venv/bin:/root/.cargo/bin:${PATH}"

RUN pip install --upgrade pip
RUN pip install gramep
