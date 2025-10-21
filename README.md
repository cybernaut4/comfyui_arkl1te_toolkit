# Arkl1te's Toolkit

A collection of custom nodes for ComfyUI by Arkl1te

> [!NOTE]
> This projected was created with a [cookiecutter](https://github.com/Comfy-Org/cookiecutter-comfy-extension) template. It helps you start writing custom nodes without worrying about the Python setup.

# Features

A set of convenient nodes. Mainly for string operations.

- String nodes:
    - PadZeroes
    - AnythingToString
    - Concatenate
- Int nodes:
    - GetNewFileIndex

## Installation

1. Clone this repository under `ComfyUI/custom_nodes`.
2. Restart ComfyUI.

## Develop

To install the dev dependencies and pre-commit (will run the ruff hook), do:

```bash
cd arkl1te_toolkit
pip install -e .[dev]
pre-commit install
```

The `-e` flag above will result in a "live" install, in the sense that any changes you make to your node extension will automatically be picked up the next time you run ComfyUI.