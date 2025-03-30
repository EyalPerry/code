# VS Code
- Install Python Extension
- Install Jupyter Extention
- Install Metals Extension for Scala Language Support
# Python + Jupyter Setup
- install poetry
- create venv `python -m venv venv`
- use venv as interpreter in jupyter notebook and vscode
- run `poetry install --with dev` to install project deps
# Scala + Jupyter Setup
- Install Coursier
- Install Almond (Jupyter + Scala Support)
- Alter almond kernel file `~/.local/share/jupyter/kernels/scala`
with following content
```json
{
  "argv": [
    "/home/<your-user>/.local/share/coursier/bin/almond",
    "--connection-file",
    "{connection_file}"
  ],
  "display_name": "Scala",
  "language": "scala"
}
```
