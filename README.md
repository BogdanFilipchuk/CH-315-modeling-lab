# CH-315-modeling-lab
Repository for collaboration on subissions in  the CH-315 course.

## Installation

Clone this repository, and open a terminal in the repository’s root directory.

### 1. Create and activate the environment

```bash
conda create -n modeling-lab python=3.12 pip
conda activate modeling-lab
```

The environment name can differ between collaborators but the Python and package versions are what matter!

### 2. Install dependencies

`requirements.txt` lists the direct dependencies. Install the pinned versions from `requirements-lock.txt` so collaborators use the same package versions:

```bash
python -m pip install -r requirements-lock.txt
python -m pip check
```

Run these commands again in the activated environment after pulling dependency changes.

### 3. Register the notebook kernel

```bash
python -m ipykernel install --user --name modeling-lab --display-name "Python (modeling-lab)"
```

Select **Python (modeling-lab)** in your notebook editor. Restart the kernel after installing or updating packages.

### 4. Enable notebook Git tools

Run these commands inside the repository with the environment activated:

```bash
python scripts/strip_notebook.py --install
nbdime config-git --enable
```

The notebook rules are already tracked in `.gitattributes`:

```gitattributes
*.ipynb filter=nbstripout diff=jupyternotebook merge=jupyternotebook
```

- **nbstripout**, through `scripts/strip_notebook.py`, removes all notebook and cell metadata (including kernel information and tags), outputs, and execution counts from staged notebooks. It also normalizes cell IDs using nbstripout's default behavior. Code, Markdown, and embedded attachments are preserved. Your working copy retains its metadata and outputs when you stage changes.
- **nbdime** provides notebook-aware local comparisons and merges.

Each collaborator must run the setup commands in their own clone, including anyone who previously installed plain nbstripout; pulling `.gitattributes` alone is insufficient. Use the wrapper's install command instead of `nbstripout --install`, which would replace the all-metadata filter. Rerun setup after moving the repository or recreating the environment, since the filter records absolute paths.

Fresh clones and checked-out notebooks have no saved kernel selection, so select **Python (modeling-lab)** in your editor when needed. Cell tags and other metadata-dependent settings (such as slideshow or grading annotations) are not shared through Git. Metadata stripping reduces incidental merge conflicts; edits to the same code or Markdown can still conflict.

To apply this policy to notebooks already tracked by Git, start with no unrelated notebook edits, then run:

```bash
git add --renormalize -- '*.ipynb'
git diff --cached
```

This stages cleaned notebooks without modifying the working files. Review and commit the cleanup; old commits retain their original metadata.

### Before working

Activate the environment:

```bash
conda activate modeling-lab
```

Before committing, restart the notebook kernel and run all cells from top to bottom to check that the notebook runs independently of previous session state.
