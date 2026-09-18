# CH-315-modeling-lab
Repository for collaboration on subissions in  the CH-315 course.

## Installation

Install Conda, clone this repository, and open a terminal in the repository’s root directory.

### 1. Create and activate the environment

```bash
conda create -n modeling-lab python=3.12 pip
conda activate modeling-lab
```

The environment name can differ between collaborators; the Python and package versions are what matter.

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
python -m pip check
```

If the repository includes `requirements-lock.txt`, install from that file **instead** to use the recorded package versions:

```bash
python -m pip install -r requirements-lock.txt
python -m pip check
```

### 3. Register the notebook kernel

```bash
python -m ipykernel install --user --name modeling-lab --display-name "Python (modeling-lab)"
```

Select **Python (modeling-lab)** in your notebook editor. Restart the kernel after installing or updating packages.

### 4. Enable notebook Git tools

Run these commands inside the repository with the environment activated:

```bash
nbstripout --install --attributes .gitattributes
nbdime config-git --enable
```

The notebook rules in `.gitattributes` should be consolidated into:

```gitattributes
*.ipynb filter=nbstripout diff=jupyternotebook merge=jupyternotebook
```

- **nbstripout** removes outputs and execution counts from staged notebooks while preserving outputs in your working copy.
- **nbdime** provides notebook-aware local comparisons and merges.

Each collaborator must run the setup commands in their own clone; pulling `.gitattributes` alone is insufficient.

### Before working

Activate the environment:

```bash
conda activate modeling-lab
```

Before committing, restart the notebook kernel and run all cells from top to bottom to check that the notebook runs independently of previous session state.