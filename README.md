# IATI Sphinx Theme

## How do I use IATI Sphinx Theme?

Please see the [IATI Sphinx Theme Documentation](https://iati-sphinx-theme.readthedocs-hosted.com/en/latest/) for usage instructions.

## How do I contribute to IATI Sphinx Theme?

### Install dependencies

```
pip install -r requirements_dev.txt
```

### Update dependencies

```
python -m piptools compile --extra=dev -o requirements_dev.txt pyproject.toml
pip install -r requirements_dev.txt
```

### Run linting

```
black iati_sphinx_theme/ docs/
isort iati_sphinx_theme/ docs/
flake8 iati_sphinx_theme/ docs/
mypy iati_sphinx_theme/ docs/
```

### Documentation with live preview

1. In one terminal, build the CSS in watch mode

   ```
   npm run build:watch
   ```

2. In a separate terminal, install the Sphinx theme then start the docs development server:

   ```
   pip install -e .
   sphinx-autobuild -a docs docs/_build/html --watch iati_sphinx_theme/
   ```

### Testing a local version of the theme against another project

To run a local version of the theme with another project, e.g. `my-docs`, take the following steps:

1. Clone the `sphinx-theme` repository, and checkout the branch or tag you want to use.

2. Run the following command in the `sphinx-theme` directory, to build the CSS for the theme.

   ```
   npm run build
   ```

3. Go to `my-docs` directory, and install the Sphinx theme

   ```
   pip install -e /path/to/sphinx-theme
   ```

4. Set the `html_theme` option in your `conf.py`

   ```python
   html_theme = "iati_sphinx_theme"
   ```

5. Start the docs development server:

   ```
   pip install sphinx-autobuild
   sphinx-autobuild docs docs/_build/html
   ```

### Translation

There are three parts to translation in this repository:

1. Translating the theme's built-in strings from the HTML templates in the `iati_sphinx_theme` directory. The message catalog name is `iati-sphinx-theme.[pot|po|mo]` and is found in the `iati_sphinx_theme/locale` directory. These are bundled with the published theme in order for consumers to have access to the translations.
2. Translating the user-configurable strings for the theme, found in `docs/conf.py` file in the `html_theme_options` object. The message catalog name is `iati-sphinx-theme.[pot|po|mo]` and is located in the `docs/locale` directory. These must be translated by the consumer of the theme, as they are variable. Because this theme is used for its own documentation, we do this step in this repository too.
3. Translating the documentation in the `.rst` files found in the `docs` directory. There is a message catalog for each file. For example, for `index.rst` there is an `index.[pot|po|mo]`.

Each of these has a slightly different method of extracting text, so a `Makefile` exists to make running the commands easier.

1. Extract text into `.pot` files

   ```
   make extract
   ```

2. Update existing `.po` files based on `.pot` files

   ```
   make update
   ```

3. Optionally, initialise a `.po` file for a new language

   ```
   make init lang=es
   ```

4. Add translations to the `.po` files

5. Compile to `.mo` files (only applies to the theme's built-in strings, so that they can be bundled with the theme)

   ```
   make compile
   ```
