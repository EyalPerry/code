FROM ubuntu:24.04

# avoid interactive apt prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install core packages
RUN apt-get update && apt-get install -y \
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
    && rm -rf /var/lib/apt/lists/*

# Install SDKMAN
RUN curl -s "https://get.sdkman.io" | bash

# Install JVM Deps
RUN bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install java 17.0.14-tem && sdk install scala 2.13.16"

# Install Coursier
RUN curl -fL "https://github.com/coursier/launchers/raw/master/cs-x86_64-pc-linux.gz" | gzip -d > /usr/local/bin/cs && chmod +x /usr/local/bin/cs

# Install Almond (Scala Jupyter Kernel)
RUN bash -c "cs launch almond --scala 2.13.16 -- --install"

ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH="/app/.venv/lib/python3.12/site-packages:/app/src"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

RUN pipx install poetry

WORKDIR /app

COPY . .

RUN poetry install --with dev

RUN chmod +x /app/entrypoint.sh