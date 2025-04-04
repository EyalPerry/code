# Scala
- install sdkman
- Install openjdk 17 (via sdkman)
- Install scala 2.13
- install coursier
# VS Code
- Install Python Extension
- Install Jupyter Extention
- Install Metals Extension
# Python
- install poetry
- create venv `python -m venv venv`
- use venv as interpreter in jupyter notebook and vscode
- run `poetry install --with dev` to install project deps
# Scala + Jupyter Setup
- Install almond (Jupyter + Scala Support) via coursier `cs launch almond --scala 2.13.16 -- --install`
- edit `~/.local/share/jupyter/kernels/scala/kernel.json`
    - Add `--add-opens=java.base/sun.nio.ch=ALL-UNNAMED` after `java` command to fix spark errors
- You can now select scala interpreter via VS Code Jupyter and run Spark

# Why
- scure, DevOps managed dev env
- cut down on dev machine setup
- use the same tooling and version
- investigate data, with python or scala + spark + delta - our data stack

docker build . -f .devcontainer/Dockerfile -t data_eng