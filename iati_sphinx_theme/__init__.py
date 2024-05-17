"""A sphinx theme for IATI documentation sites."""

from os import path

__version__ = "0.0.0"


def setup(app):
    app.add_html_theme("iati_sphinx_theme", path.abspath(path.dirname(__file__)))
