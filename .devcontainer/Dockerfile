FROM ubuntu:24.04

ARG PYTHON_MINOR_VERSION=13
ARG JDK_MAJOR_VERSION=21
ARG SCALA_VERSION=2.13.16

ENV DEBIAN_FRONTEND=noninteractive \
    JDK_JAVA_OPTIONS="--add-opens=java.base/sun.nio.ch=ALL-UNNAMED" \
    PATH="/root/.local/bin:$PATH" \
    PYTHONPATH="/container/.venv/lib/python3.${PYTHON_MINOR_VERSION}/site-packages:/container/src" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    CLASSPATH="/container/target/dependency/*"

RUN apt-get update \
    && apt-get install -y \
    software-properties-common \
    curl \
    unzip \
    zip \
    git \
    gzip \
    bash \
    pipx \
    openjdk-${JDK_MAJOR_VERSION}-jdk \
    maven \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get install -y python3.${PYTHON_MINOR_VERSION} \
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
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache/*

WORKDIR /container

COPY pom.xml ./
RUN mvn dependency:copy-dependencies -DoutputDirectory=target/dependency

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root && rm -rf /tmp/* /root/.cache/*

COPY . .

RUN poetry install && rm -rf /tmp/* /root/.cache/*

CMD [ "bash" ]