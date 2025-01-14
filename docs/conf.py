# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "IATI Sphinx Theme"
copyright = "2024 IATI Secretariat"
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


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "iati_sphinx_theme"
html_theme_options = {
    "github_repository": "https://github.com/IATI/sphinx-theme",
    "languages": {
        "en": "English",
    },
    # Uncomment below lines to display tool navigation
    # "tool_name": "IATI Example Tool",
    # "tool_url": "https://example.com/",
}

todo_include_todos = True
