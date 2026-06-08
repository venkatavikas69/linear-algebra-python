# Deployment and Documentation Setup Steps

This file summarizes the repository updates and the deployment workflow for MkDocs and GitHub Pages.

## What was added

1. **README improvements**
   - Cleaned and organized the main `README.md`.
   - Added project overview, repository structure, setup instructions, documentation notes, and contributing guidance.

2. **GitHub Pages site setup**
   - Added MkDocs configuration in `mkdocs.yml`.
   - Added site content under `docs/`:
     - `docs/index.md`
     - `docs/getting_started.md`
     - `docs/notes.md`
     - `docs/contributing.md`
   - Added chapter notes as internal site pages:
     - `docs/chapter1_notes.md`
     - `docs/chapter2_span_basis_notes.md`

3. **Custom site styling**
   - Created custom CSS at `docs/css/custom.css`.
   - Added a custom SVG logo at `docs/images/logo.svg`.
   - Updated `mkdocs.yml` to include the custom CSS and logo.

4. **GitHub Actions deployment workflow**
   - Updated `.github/workflows/static.yml` to build MkDocs and deploy only the generated `site/` directory.
   - Set workflow permissions:
     - `contents: write`
     - `pages: write`
     - `id-token: write`

5. **Dependencies**
   - Added `mkdocs` to `requirements.txt`.
   - Installed MkDocs in the repository virtual environment.

## How to use it locally

1. Activate the virtual environment:

```bash
source .venv/bin/activate
```

2. Install dependencies if needed:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Build the documentation site:

```bash
mkdocs build
```

4. Preview the site locally:

```bash
mkdocs serve
```

Then open the local URL shown in the terminal.

## How deployment works

1. The `static.yml` workflow runs on `push` to `main` and on manual dispatch.
2. It checks out the repository.
3. It installs Python and dependencies.
4. It runs `mkdocs build`.
5. It uploads the generated `site/` folder to GitHub Pages.
6. GitHub Pages serves the built site.

## Repository settings required

- GitHub Actions must be allowed to read and write repository contents.
- GitHub Pages should be configured to use the GitHub Actions workflow as the source.
- The workflow permissions must include:
  - `contents: write`
  - `pages: write`
  - `id-token: write`

## Important files

- `README.md`
- `mkdocs.yml`
- `docs/index.md`
- `docs/getting_started.md`
- `docs/notes.md`
- `docs/chapter1_notes.md`
- `docs/chapter2_span_basis_notes.md`
- `docs/css/custom.css`
- `.github/workflows/static.yml`
- `requirements.txt`

## Notes

- The MkDocs navigation is controlled in `mkdocs.yml`.
- The site content is written in Markdown under `docs/`.
- The GitHub Actions workflow deploys the built `site/` output only.
- If you want a different theme or visual design, update `docs/css/custom.css` or the `mkdocs.yml` theme settings.
