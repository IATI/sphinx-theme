"""A sphinx theme for IATI documentation sites."""

__version__ = "0.0.0"

from os import path


def setup(app):
    app.add_html_theme('iati_sphinx_theme', path.abspath(path.dirname(__file__)))
