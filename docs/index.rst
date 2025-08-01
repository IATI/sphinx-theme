=================
IATI Sphinx Theme
=================

.. toctree::
   :titlesonly:
   :maxdepth: 1
   :hidden:

   Home <self>

.. toctree::
   :titlesonly:
   :maxdepth: 1
   :caption: Examples
   :hidden:

   examples/videos

.. toctree::
   :titlesonly:
   :maxdepth: 1
   :caption: Development
   :hidden:

   kitchen-sink/index

Installation
============

1.
  Install the theme in your Sphinx project.

  .. code-block:: none

    pip install iati-sphinx-theme

2.
  In your project's :code:`conf.py` set the :code:`html_theme`.

  .. code-block:: python

    html_theme = "iati_sphinx_theme"

Configuration
=============

This theme has multiple options, which can be configured using the :code:`html_theme_options` object in your :code:`conf.py` file.

.. code-block:: python

  html_theme_options = {
    "github_repository": "https://github.com/organisation/repository",
    "header_title_text": "IATI Sphinx Theme",
    "header_eyebrow_text": "IATI Tools: Documentation",
    "languages": ["en", "fr", "es"],
    "plausible_domain": "example.com",
    "project_title": "IATI Sphinx Theme: Documentation",
    "tool_nav_items": {
      "IATI Tool": "https://tool.iatistandard.org/"
    },
  }

There is more information on each option below.

:code:`github_repository`
-------------------------

This should be a link to the Github repository for the documentation site, and is used to link to the source code in the footer of the site.

:code:`header_title_text`
-------------------------

The title text to display in the header.
Defaults to the value of :code:`project` in :code:`conf.py`.

:code:`header_eyebrow_text`
---------------------------

The text above the title in the header.
Defaults to "IATI Tools: Documentation".

:code:`languages`
-----------------

A list of languages which the documentation is available in, used to populate the language switcher component. Defaults to English only.

:code:`plausible_domain`
------------------------

To integrate with Plausible Analytics, add the :code:`plausible_domain` option in your project's :code:`conf.py` file.

If your docs site is a subdomain for the site it is documenting, use the top level domain for cross-subdomain tracking.
For example, for the Sphinx site :code:`docs.example.com`, use :code:`example.com` as your :code:`plausible_domain`.

.. code-block:: python

  html_theme_options = {
    "plausible_domain": "example.com"
  }

:code:`project_title`
---------------------

The text to use in the breadcrumb and tool navigation components.

:code:`tool_nav_items`
----------------------

Items to include in the header tool nav bar.
Defaults to a single item that links back to the site's homepage.

Custom roles
============

:code:`iati-reference`
----------------------

When referencing elements of the standard, use the :code:`iati-reference` role. For example:

.. code-block:: rst

  :iati-reference:`iati-activities/iati-activity/iati-identifier`

The code above will apply the following styles:

:iati-reference:`iati-activities/iati-activity/iati-identifier`

Translation
===========

The IATI Sphinx Theme is translatable. The following languages are currently supported:

- English (:code:`en`)
- French  (:code:`fr`)
- Spanish  (:code:`es`)

Built-in strings
----------------

To enable translation of built-in strings, you must add the theme to the :code:`locale_dirs` list in your :code:`conf.py`.

.. code-block:: python

  import os
  import iati_sphinx_theme

  local_dirs = [
    "locale",
    os.path.join(os.path.dirname(iati_sphinx_theme.__file__), "locale")
  ]

User-defined strings
--------------------

User-defined strings must be translated by the user of the theme.
These are configured in your :code:`conf.py` file under :code:`html_theme_options`.
In order to translate these, complete the following steps in the same location as the `conf.py` file:

1. Mark strings as translatable using :code:`sphinx.locale.get_translation`, usually renamed to :code:`_()`.

.. code-block:: python

  import os
  from sphinx.locale import get_translation

  MESSAGE_CATALOG_NAME = "iati-sphinx-theme"
  _ = get_translation(MESSAGE_CATALOG_NAME)

  html_theme_options = {
      "header_title_text": _("Title"),
      "tool_name": _("IATI Example Tool"),
  }

  def setup(app):
      locale_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "locale")
      app.add_message_catalog(MESSAGE_CATALOG_NAME, locale_path)

2. Extract translatable strings to :code:`locale/iati-sphinx-theme.pot`.

.. code-block::

  pybabel extract conf.py -o locale/iati-sphinx-theme.pot

3. Create or update :code:`.po` files for desired languages.

.. code-block::

  # To add a new language
  pybabel init -i locale/iati-sphinx-theme.pot -d locale --domain=iati-sphinx-theme -l es

  # To update an existing language
  pybabel update -i locale/iati-sphinx-theme.pot -d locale --domain=iati-sphinx-theme -l es

4. Compile the :code:`.mo` files.
   This must be done before Sphinx builds the project, for example using `Read the Docs' pre_build job <https://docs.readthedocs.io/en/stable/config-file/v2.html#build-jobs>`_,
   or by compiling and committing the files to version control.

.. code-block::

  pybabel compile -d locale --domain=iati-sphinx-theme

5. Continue with your project's usual translation workflow.
