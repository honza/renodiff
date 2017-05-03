# -*- coding: utf-8 -*-

# renodiff - Convert your git patch to a reno release note Edit Add topics
# Copyright (C) 2017  Honza Pokorny <me@honza.ca>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
