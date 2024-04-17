# IATI Sphinx Theme

## Development

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
black iati_sphinx_theme
isort iati_sphinx_theme
flake8 iati_sphinx_theme
```

### Documentation with live preview

1. Install the theme locally:
    ```
    pip install -e .
    ```

2. Start the docs development server:
    ```
    sphinx-autobuild docs docs/_build/html
    ```
