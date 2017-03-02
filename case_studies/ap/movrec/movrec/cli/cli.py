# -*- coding: utf-8 -*-
"""
Movrec command line tool
"""

import click
import pprint

from movrec import Movrec

# Disable the warning that Click displays (as of Click version 5.0) when users
# use unicode_literals in Python 2.
# See http://click.pocoo.org/dev/python3/#unicode-literals for more details.
click.disable_unicode_literals_warning = True

@click.group()
def main():
	"""Movrec command line tool."""
	pass

@main.command()
@click.option('--movie_id', '-id', help='Finds movies similar to movie_id')
def similar_movies(movie_id):
	m = Movrec(only_ids=True)
	m.load()
	m.similar_movies(movie_id)

@main.command()
@click.option('--movie_id', '-id', help='Finds movies similar to movie_id via user behaviour')
def similar_movies_via_user_behaviour(movie_id):
	m = Movrec(only_ids=True)
	m.load()
	m.similar_movies_via_user_behaviour(movie_id)
