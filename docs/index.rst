=================
IATI Sphinx Theme
=================

.. toctree::
   :hidden:

   Home <self>

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

Plausible Analytics
-------------------

To integrate with Plausible Analytics, add the :code:`plausible_domain` option to the :code:`html_theme_options` object in your project's :code:`conf.py`.

If your documentation site is a subdomain and you want cross-subdomain tracking, use the top level domain.
For example, for the documentation site :code:`docs.example.com`, use :code:`example.com` as your :code:`plausible_domain`.

.. code-block:: python

  html_theme_options = {
    "plausible_domain": "example.com"
  }

Translation
-----------

The IATI Sphinx Theme is translatable.

Strings built into the theme will be translated automatically into supported languages.
The following languages are currently supported:

- English (:code:`en`)

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

4. Continue with your project's usual translation workflow.
