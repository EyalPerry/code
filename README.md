# Scala + Jupyter Setup
- Install almond (Jupyter + Scala Support) via coursier `cs launch almond --scala 2.13.16 -- --install`
- edit `~/.local/share/jupyter/kernels/scala/kernel.json`
    - Add `--add-opens=java.base/sun.nio.ch=ALL-UNNAMED` after `java` command to fix spark errors
- You can now select scala interpreter via VS Code Jupyter and run Spark
# Why
- scure, DevOps managed dev env
- cut down on dev machine setup
- start fresh instance of your dev env whenever something goes wrong
- use the same tooling and version across the team
- investigate data, with python or scala + spark + delta - our data stack

# Build
`docker build . -f Dockerfile -t data_eng`
`docker run -it data_eng`