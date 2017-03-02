# # -*- coding: utf-8 -*-
# """
# UnderstandEngine command line tool
# """
#
# import click
#
# from understand_engine import UnderstandEngine
#
# # Disable the warning that Click displays (as of Click version 5.0) when users
# # use unicode_literals in Python 2.
# # See http://click.pocoo.org/dev/python3/#unicode-literals for more details.
# click.disable_unicode_literals_warning = True
#
# @click.group()
# def main():
#     """UnderstandEngine command line tool."""
#     pass
#
# @main.command()
# @click.option('--text', '-t', help='Text to be summarized')
# def summarize(text):
#     """Summarizing given text."""
#     unen = UnderstandEngine(str(text))
#     click.echo(unen.summarize())
#
# @main.command()
# @click.option('--text', '-t', help='Text to extract keywords out of.')
# def keywords(text):
#     """Extracting keywords out of given text."""
#     unen = UnderstandEngine(str(text))
#     click.echo(unen.keywords())
#
# @main.command()
# @click.option('--text', '-t', help='Text to analyze polarity and subjectivity out of.')
# def analyze(text):
#     """Analyzing polarity and subjectivity out of given text."""
#     unen = UnderstandEngine(str(text))
#     click.echo(unen.analyze())
#
# @main.command()
# @click.option('--text', '-t', help='Sample text')
# def clean(text):
#     click.echo(text)
