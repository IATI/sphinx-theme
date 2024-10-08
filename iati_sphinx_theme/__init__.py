"""A sphinx theme for IATI documentation sites."""

from os import path

import sphinx.application


def setup(app: sphinx.application.Sphinx) -> None:
    app.add_html_theme("iati_sphinx_theme", path.abspath(path.dirname(__file__)))

    locale_path = path.join(path.abspath(path.dirname(__file__)), "locale")
    app.add_message_catalog("iati-sphinx-theme", locale_path)

    app.config["html_permalinks_icon"] = "#"
    app.config["html_favicon"] = "static/favicon-16x16.png"
