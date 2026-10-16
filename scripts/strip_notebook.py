"""Git clean filter: remove all metadata, then strip outputs with nbstripout."""

import argparse
from pathlib import Path
import shlex
import subprocess
import sys

import nbformat
from nbstripout import strip_output


def clean_notebook(source):
    notebook = nbformat.reads(source, as_version=nbformat.NO_CONVERT)
    if notebook.nbformat != 4:
        raise ValueError("This filter requires notebook format 4")

    notebook.metadata = {}
    for cell in notebook.cells:
        # Clear tags and keep_output/init_cell flags before stripping outputs.
        cell.metadata = {}

    strip_output(notebook, keep_output=False, keep_count=False, keep_id=False)
    nbformat.validate(notebook)
    return nbformat.writes(notebook) + "\n"


def install():
    command = shlex.join([sys.executable, str(Path(__file__).resolve())])
    for key, value in {
        "filter.nbstripout.clean": command,
        "filter.nbstripout.smudge": "cat",
        "filter.nbstripout.required": "true",
    }.items():
        subprocess.run(["git", "config", "--local", key, value], check=True)
    print("Installed the all-metadata nbstripout filter in this clone.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--install", action="store_true", help="configure this clone's Git filter")
    args = parser.parse_args()
    if args.install:
        install()
    else:
        source = sys.stdin.buffer.read().decode("utf-8")
        sys.stdout.buffer.write(clean_notebook(source).encode("utf-8"))


if __name__ == "__main__":
    main()
