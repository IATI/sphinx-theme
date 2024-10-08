# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from os import path

import sphinx.application
from sphinx.locale import get_translation

MESSAGE_CATALOG_NAME = "iati-sphinx-theme"
_ = get_translation(MESSAGE_CATALOG_NAME)


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "IATI Sphinx Theme"
author = "IATI Secretariat"
language = "en"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

locale_dirs = ["locale/"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "iati_sphinx_theme"
html_theme_options = {
    "header_title_text": _("Title"),
}


todo_include_todos = True


def setup(app: sphinx.application.Sphinx) -> None:
    locale_path = path.join(path.abspath(path.dirname(__file__)), "locale")
    app.add_message_catalog(MESSAGE_CATALOG_NAME, locale_path)
