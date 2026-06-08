# Linear Algebra Python

[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![GitHub repo size](https://img.shields.io/github/repo-size/venkatavikas69/linear-algebra-python)](https://github.com/venkatavikas69/linear-algebra-python)
[![Top language](https://img.shields.io/github/languages/top/venkatavikas69/linear-algebra-python)](https://github.com/venkatavikas69/linear-algebra-python)

A hands-on Python project for practicing the core concepts from 3Blue1Brown's *Essence of Linear Algebra*. This repository combines code, notes, and visual visualizations for vectors, vector addition, linear combinations, span, and basis vectors.

---

## 📌 Project Overview

- **Chapter 1**: Vectors, vector representation, plotting, vector addition, scalar multiplication, and magnitude.
- **Chapter 2**: Linear combinations, span, basis vectors, independence, and geometric intuition.
- **Notes**: Markdown notes for each chapter in the root folder.
- **Visualizations**: Generated PNG plots inside each chapter's `outputs/` folder.

---

## 📁 Repository Structure

- `chapter1_notes.md` — notes for Chapter 1.
- `chapter2_span_basis_notes.md` — notes for Chapter 2.
- `code/chapter1/chapter1_vectors.py` — Chapter 1 Python practice script.
- `code/chapter2/linear_combinations_ch2.py` — Chapter 2 Python practice script.
- `code/chapter1/outputs/` — saved Chapter 1 plot images.
- `code/chapter2/outputs/` — saved Chapter 2 plot images.
- `requirements.txt` — Python dependencies.
- `setup.txt` — development environment setup instructions.

---

## 🗂 Repository Organization

- `code/` — chapter scripts, examples, and plotting utilities.
- `chapter1_notes.md`, `chapter2_span_basis_notes.md` — learning notes and chapter summaries.
- `code/*/outputs/` — generated visualization images.
- `requirements.txt` — installed package list.
- `setup.txt` — local environment setup instructions.
- `.gitignore` — files and folders excluded from version control.

---

## 🚀 Getting Started

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Run a chapter script

```bash
python code/chapter1/chapter1_vectors.py
python code/chapter2/linear_combinations_ch2.py
```

Each script saves plots into its own `outputs/` directory.

---

## 📚 Documentation

This repository now includes an MkDocs site in the `docs/` folder.

Build the documentation locally:

```bash
mkdocs build
```

Preview the site locally:

```bash
mkdocs serve
```

The GitHub Actions workflow in `.github/workflows/deploy-docs.yml` can publish the built site to GitHub Pages automatically.

---

## 📦 Dependencies

- `numpy`
- `matplotlib`
- `pandas` (optional for future data exploration)
- `scikit-learn` (optional for later linear algebra applications)
- `seaborn` (optional visualization support)
- `jupyterlab` (optional interactive exploration)

> For the current scripts, only `numpy` and `matplotlib` are required.

---

## 🧠 Notes and References

- [Chapter 1 - Vectors](chapter1_notes.md)
- [Chapter 2 - Linear Combinations & Basis](chapter2_span_basis_notes.md)

---

## 📷 Example Visualizations

- `code/chapter1/outputs/plot1_vector.png` — vector representation.
- `code/chapter1/outputs/plot2_addition.png` — tip-to-tail vector addition.
- `code/chapter1/outputs/plot3_scalar.png` — scalar multiplication examples.
- `code/chapter2/outputs/ch2_plot1_basis.png` — standard basis decomposition.
- `code/chapter2/outputs/ch2_plot2_span.png` — span and linear dependence.

---

## ✅ Progress

- [x] Chapter 1
- [x] Chapter 2
- [ ] Chapter 3
- [ ] Chapter 4

---

## 🤝 Contributing

Contributions are welcome! See [`CONTRIBUTING.md`](CONTRIBUTING.md) for issue reports, feature requests, and pull request guidelines.

---

## 💡 Tips

- Run scripts from the repository root.
- Open the generated images to inspect how the vectors are drawn.
- Use the notes files to connect the visuals with the linear algebra concepts.
