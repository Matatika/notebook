"""CLI 'run' command"""

import click
import os

from matatika_notebook.notebook_converter import convert_notebook
from matatika_notebook.notebook_runner import run_notebook
from matatika_notebook.utils import get_list_of_paths
from .root import notebook


@notebook.command("run", short_help="Run the notebook")
@click.argument("path", type=click.Path(exists=True))
@click.option(
    "--format",
    "-f",
    "format_",
    type=click.STRING,
    help="What format you want to convert your notebook into. Supported formats: PDF",
)
@click.option(
    "--config",
    "-c",
    "config_",
    type=click.STRING,
    default=None,
    help="What config to use when converting your notebook. Configurable formats: PDF",
)
def run(path, format_, config_):
    """Run a notebook or all notebooks in a directory"""

    path_list = get_list_of_paths(path)

    run_notebook(path_list)

    if format_:
        convert_notebook(path_list, format_, config_)
