"""A sphinx theme for IATI documentation sites."""

from os import path

import sphinx.application

__version__ = "0.0.0"


def setup(app: sphinx.application.Sphinx) -> None:
    app.add_html_theme("iati_sphinx_theme", path.abspath(path.dirname(__file__)))
