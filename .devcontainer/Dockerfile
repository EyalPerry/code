FROM ubuntu:24.04

ARG JAVA_VERSION=17
ARG SCALA_VERSION=2.13.16

ENV DEBIAN_FRONTEND=noninteractive \
    JDK_JAVA_OPTIONS="--add-opens=java.base/sun.nio.ch=ALL-UNNAMED" \
    PATH="/root/.local/bin:$PATH" \
    PYTHONPATH="/container/.venv/lib/python3.12/site-packages:/container/src" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN apt-get update && apt update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    build-essential \
    curl \
    unzip \
    zip \
    git \
    gzip \
    ca-certificates \
    bash \
    pipx \
    openjdk-${JAVA_VERSION}-jdk \
    && apt install gh \
    && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf awscliv2.zip aws \
    && curl https://install.duckdb.org | sh \
    && curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl \
    && curl -fL "https://github.com/coursier/launchers/raw/master/cs-x86_64-pc-linux.gz" | gzip -d > /usr/local/bin/cs && chmod +x /usr/local/bin/cs \
    && bash -c "cs install scala:${SCALA_VERSION} && cs install scalac:${SCALA_VERSION} && cs launch almond --scala ${SCALA_VERSION} -- --install" \
    && pipx install poetry \ 
    && pipx install jupyter --include-deps \
    && apt-get clean && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache/pip /root/.cache/pypoetry /tmp/poetry_cache


WORKDIR /container

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root && rm -rf ${POETRY_CACHE_DIR}

COPY . .

RUN poetry install && rm -rf ${POETRY_CACHE_DIR}

CMD [ "bash" ]