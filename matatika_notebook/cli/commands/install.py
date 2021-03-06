"""CLI 'install' command"""

import click

from matatika_notebook.notebook_installer import install_requirements
from matatika_notebook.cli.commands.root import notebook


@notebook.command(
    "install",
    short_help="Install a requirements.txt to the Notebook utility's virtual enviroment",
)
@click.argument("path", type=click.Path(exists=True))
def install(path):
    """Install required python packages from a requirements.txt"""
    install_requirements(path)
