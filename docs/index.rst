=================
IATI Sphinx Theme
=================

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
    "plausible_domain": "example.com",
    "tool_name": "IATI Tool",
    "tool_url": "https://tool.iatistandard.org/",
  }

There is more information on each option below.

:code:`github_repository`
-------------------------

This should be a link to the Github repository for the documentation site, and is used to link to the source code in the footer of the site.

:code:`plausible_domain`
------------------------

To integrate with Plausible Analytics, add the :code:`plausible_domain` option in your project's :code:`conf.py` file.

If your docs site is a subdomain for the site it is documenting, use the top level domain for cross-subdomain tracking.
For example, for the Sphinx site :code:`docs.example.com`, use :code:`example.com` as your :code:`plausible_domain`.

.. code-block:: python

  html_theme_options = {
    "plausible_domain": "example.com"
  }

:code:`tool_name`
-----------------

The name of the tool which your Sphinx site documents.

:code:`tool_url`
----------------

The URL of the tool which your Sphinx site documents.
