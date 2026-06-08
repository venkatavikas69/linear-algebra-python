# Getting Started

## Requirements

- Python 3.11+ recommended
- `numpy`
- `matplotlib`
- `mkdocs`

## Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the example scripts

```bash
python code/chapter1/chapter1_vectors.py
python code/chapter2/linear_combinations_ch2.py
```

## Build the documentation site

```bash
mkdocs build
```

## Preview locally

```bash
mkdocs serve
```
