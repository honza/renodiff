# -*- coding: utf-8 -*-

import click

from renodiff import run


@click.command()
def main(args=None):
    """
    Console script for renodiff

    Example usage:

    git show | renodiff
    """
    stdin_text = click.get_text_stream('stdin')
    try:
        run(stdin_text.read())
        return 0
    except:
        return -1
